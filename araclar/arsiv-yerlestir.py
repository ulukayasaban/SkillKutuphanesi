#!/usr/bin/env python3
"""Aşama 2: .gecici/cekilen'deki skilleri tekilleştirir, kategoriye yerleştirir, registry.json'u üretir.

Kurallar:
- Aynı isim + aynı SKILL.md içeriği -> tek kopya (öncelikli kaynak); diğerleri 'kopya_kaynaklar'
- Aynı isim + farklı içerik         -> öncelikli olan 'tercih', diğerleri 'ad@kaynak' kimliğiyle 'alternatif'
- Claude/Codex'e özel uyarlanmış sürümler -> arsiv/_varyantlar/<id>/<arac>/  (kurulumda o araca kurulur)
- Skill olmayan komut/agent dosyaları     -> arsiv/_bilesenler/<kaynak>/...   (otomatik kurulmaz)
- Elle yapılan inceleme alanları korunur (ELLE_ALANLAR).
Kullanım: python3 araclar/arsiv-yerlestir.py
"""
import hashlib
import math
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import (ACIKLAMA_SINIRI, ARSIV, GECICI, KATEGORILER, KOK, REGISTRY, boyut, frontmatter,  # noqa: E402
                   frontmatter_onar, frontmatter_teshis, global_durum, symlink_taslaklari,
                   taslak_baglantilarini_cevir, TREND, TREND_BONUS, json_oku, json_yaz, klasor_hash, skill_md_hash, trend_durumu)

KURALLAR = KOK / "kategori-kurallari.json"
GELISTIRICILER = KOK / "gelistiriciler.json"
GIZLI_TIPLER = ("T3", "T4")

# İnceleme sırasında elle doldurulan alanlar: yeniden yerleştirmede korunur.
ELLE_ALANLAR = ["ozet_tr", "kullanim_alani", "kullanma", "teknoloji", "gerekli_paketler", "proje_tipleri",
                "roller", "zorluk", "kalite", "kalite_notu", "ortusme_grubu", "ortusme_rolu", "inceleme",
                "notlar", "uyum_elle", "kategori_elle", "durum_elle", "inceleyen", "inceleme_tarihi", "uygulama_grubu",
                "inceleme_commit", "onceki_inceleme", "aciklama_duzeltme", "yama"]

TEKNOLOJI_DESENLERI = {
    "react": r"\breact\b", "next.js": r"next\.?js|\bnext/|app router", "vue": r"\bvue\b", "svelte": r"\bsvelte\b",
    "tailwind": r"tailwind", "typescript": r"typescript|\.tsx?\b", "three.js": r"three\.?js|\bTHREE\.",
    "r3f": r"react-three-fiber|@react-three|\br3f\b", "gsap": r"\bgsap\b", "motion": r"framer-motion|motion/react|\bmotion\.dev",
    "lenis": r"\blenis\b", "lottie": r"lottie", "webgl": r"webgl|glsl|shader", "css": r"\bcss\b",
    "python": r"\bpython\b|\.py\b|\bpip install", "node": r"\bnode(\.js)?\b|\bnpm\b|\bnpx\b", "playwright": r"playwright",
    "html": r"\bhtml\b", "canvas": r"\bcanvas\b", "obsidian": r"obsidian", "git": r"\bgit\b", "docker": r"docker",
    "ffmpeg": r"ffmpeg", "remotion": r"remotion", "api-anahtari": r"api[_ -]?key|_API_KEY|token",
}
CLAUDE_OZEL_DESEN = (r"TodoWrite|AskUserQuestion|\bTask tool\b|subagent_type|\$\{CLAUDE_PLUGIN_ROOT\}|"
                     r"\bSkill tool\b|\.claude/(agents|commands|hooks|settings)|hooks\.json|/plugin\b|claude --")
CLAUDE_FM_ALANLARI = {"when_to_use", "argument-hint", "arguments", "disable-model-invocation", "user-invocable",
                      "disallowed-tools", "model", "effort", "context", "agent", "background", "hooks", "paths", "shell"}
ACIKLAMA_KISA = 40  # bundan kısa description'da 'ne zaman' bilgisi olmaz; aciklama_duzeltme yazılır
AD_GECERLI = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def kurallari_uygula(kural, kayit):
    if kayit["tip"] == "T3":
        return kural["repo_varsayilan"]["_T3"]
    ad, repo = kayit["ad"], kayit["repo"]
    for k in kural.get("yol_kurallari", []):  # repo içi klasöre göre (ör. knowledge-work-plugins/sales/...): ad kurallarından önce
        if k["repo"] == repo and re.search(k["desen"], kayit.get("kaynak_yol", ""), re.I):
            return k["kategori"]
    for k in kural.get("ad_kurallari", []):
        if k.get("repo") and k["repo"] != repo:  # repo'ya özel kural: başka repodaki aynı adlı skill etkilenmez
            continue
        if re.search(k["desen"], ad, re.I):
            return k["kategori"]
    return kural.get("repo_varsayilan", {}).get(repo, "d-ai-otomasyon/04-skill-plugin-yazimi")


def kisa_kaynak(repo):
    return re.sub(r"[^a-z0-9]+", "-", repo.split("/")[0].lower()).strip("-")


def uyum_tespit(metin, kayit, fm):
    bulgular = sorted(set(re.findall(CLAUDE_OZEL_DESEN, metin)))
    fm_claude = sorted(set(fm) & CLAUDE_FM_ALANLARI)
    notlar = []
    if fm_claude:
        notlar.append("Claude Code'a özgü frontmatter alanları: " + ", ".join(fm_claude) + " (Codex bunları yok sayar)")
    if kayit.get("varyantlar"):
        notlar.append("Araca özel sürümler mevcut: " + ", ".join(k for k, v in kayit["varyantlar"].items() if v) +
                      " -> kurulumda her araca kendi sürümü konur")
    if kayit["repo"] == "anthropics/claude-code" and "frontend-design" not in kayit["ad"] and "migration" not in kayit["ad"]:
        return {"claude": "tam", "codex": "konu-claude-ozel",
                "not": "Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash "
                       "command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, "
                       "${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. " + " · ".join(notlar)}
    if bulgular and not kayit.get("varyantlar", {}).get("codex"):
        notlar.insert(0, "Claude'a özgü araç adları geçiyor (" + ", ".join(bulgular[:5]) +
                      "); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar")
        return {"claude": "tam", "codex": "uyarlanabilir", "not": " · ".join(notlar)}
    return {"claude": "tam", "codex": "tam", "not": " · ".join(notlar)}


def baglam_yuku(klasor):
    sm = (klasor / "SKILL.md").stat().st_size
    return "kucuk" if sm < 8000 else "orta" if sm < 25000 else "buyuk"


def yapisal_sorunlar(fm, metin, ad):
    """Skill'in araçlarca tanınmasını/doğru tetiklenmesini etkileyen sorunlar. Tetiklenmeyi bozanlar kurulumda
    onarılır: biçim hataları kendiliğinden, eksik/kısa/uzun description registry'deki aciklama_duzeltme ile."""
    s = [x for x in frontmatter_teshis(metin) if x != "frontmatter yok"]
    if not fm:
        s.append("frontmatter yok")
    if not fm.get("description"):
        s.append("description yok")
    elif len(fm["description"]) > ACIKLAMA_SINIRI:
        s.append(f"description çok uzun ({len(fm['description'])} karakter > {ACIKLAMA_SINIRI}); Codex skill'i yüklemez")
    elif len(fm["description"]) < ACIKLAMA_KISA:
        s.append(f"description çok kısa ({len(fm['description'])} karakter); ne zaman kullanılacağı anlaşılmaz")
    if fm.get("name") and not AD_GECERLI.match(fm["name"]):
        s.append(f"name biçimi standart dışı ('{fm['name']}'); kurulumda klasör adına eşitlenir")
    if str(fm.get("disable-model-invocation", "")).lower() == "true":
        s.append("disable-model-invocation: true -> Claude alt-agent'ına önyüklenemez, sadece elle çağrılır")
    return s


def kirik_baglantilar(klasor: Path):
    """SKILL.md'deki göreli markdown bağlantıları arşivde var mı? (http, #, mailto, şablon değişkenleri hariç)"""
    metin = (klasor / "SKILL.md").read_text(encoding="utf-8", errors="replace")
    kirik = []
    for hedef in re.findall(r"\]\(([^)\s]+)\)", metin):
        if re.match(r"^(https?:|#|mailto:|<|\$|\{)", hedef) or "*" in hedef:
            continue
        yol = hedef.split("#")[0]
        if yol and not (klasor / yol).exists():
            kirik.append(yol)
    return sorted(set(kirik))


METIN_UZANTILARI = (".md", ".mdx", ".txt")


def kardes_baglantilari(klasor: Path, indeks, kendi):
    """Skill'in .md dosyalarındaki ../<kardeş>/... bağlantıları: hedef arşivdeki kardeş skillde var mı?
    indeks: klasör adı -> [(skill kaydı, arşivdeki klasörü)]. Aynı repodaki kardeş tercih edilir.
    Döner: ({kardeş adı: {"id", "dosya_sayisi"}}, SKILL.md'de kardeşte bulunan bağlantılar kümesi)"""
    kardesler, cozulen = {}, set()
    taslaklar = symlink_taslaklari(klasor)  # kaynakta symlink olan '../<kardeş>' dosyaları: kurulumda kardeş yoluna çevrilir
    for f in sorted(klasor.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in METIN_UZANTILARI:
            continue
        derinlik = len(f.relative_to(klasor).parts) - 1
        metin = taslak_baglantilarini_cevir(f.read_text(encoding="utf-8", errors="replace"), taslaklar, derinlik)
        for hedef in re.findall(r"\]\(([^)\s]+)\)", metin):
            yol = hedef.split("#")[0]
            onek = "../" * (derinlik + 1)
            if not yol.startswith(onek) or yol.startswith(onek + "../"):
                continue
            ad, _, kalan = yol[len(onek):].partition("/")
            if not ad or ad == kendi["klasor_adi"]:
                continue
            adaylar = sorted(indeks.get(ad, []), key=lambda x: (x[0]["repo"] != kendi["repo"], x[0]["durum"] != "tercih"))
            if not adaylar or (kalan and not any((d / kalan).exists() for _, d in adaylar)):
                continue
            s, _ = next(((s, d) for s, d in adaylar if not kalan or (d / kalan).exists()))
            k = kardesler.setdefault(ad, {"id": s["id"], "dosyalar": set()})
            k["dosyalar"].add(str(f.relative_to(klasor)))
            if derinlik == 0:
                cozulen.add(yol)
                if ad in taslaklar:  # orijinal metindeki taslak yolu (./X/… ya da X/…) da çözülmüş sayılır
                    cozulen.update({"./" + yol[3:], yol[3:]})
    return ({a: {"id": k["id"], "dosya_sayisi": len(k["dosyalar"])} for a, k in sorted(kardesler.items())}, cozulen)


def degerlendir(s, gel):
    """0-100 otomatik puan. Elle 'kalite' (1-5) varsa ağırlıklı katılır."""
    p, ac = 0, []
    if gel:
        gun = (date.today() - date.fromisoformat(gel["son_guncelleme"])).days
        bakim = 25 if gun <= 90 else 18 if gun <= 180 else 10 if gun <= 365 else 3
        p += bakim; ac.append(f"bakım {bakim}/25 ({gun} gün önce)")
        gv = gel.get("guven")
        if gv:  # GitHub etkileşimleri (yıldız, hız, katkıcı, commit, fork, izleyici, sürüm…) kaynaklar arası sıralaması
            top = round(30 * gv["puan"] / 100)
            p += top; ac.append(f"GitHub güveni {top}/30 (güven {gv['puan']} {gv['derece']}" + (f", #{gv['sira']}/{gv['toplam']})" if gv.get("sira") else ")"))
        else:  # eski gelistiriciler.json (güven hesaplanmamış): yıldız + kaynak tipi
            top = min(20, round(4 * math.log10(max(gel["yildiz"], 1) + 1)))
            p += top; ac.append(f"topluluk {top}/20 (★{gel['yildiz']})")
        lis = 15 if gel["lisans"] not in ("yok", "NOASSERTION", "belirtilmemiş") else 3
        p += lis; ac.append(f"lisans {lis}/15 ({gel['lisans']})")
        if not gv:
            res = 10 if gel["resmi_kaynak"] else 5 if gel["sahip_tipi"] == "kurum" else 3
            p += res; ac.append(f"kaynak {res}/10 ({'resmî' if gel['resmi_kaynak'] else gel['sahip_tipi']})")
        if gel.get("arsivlenmis"):
            p -= 15; ac.append("repo arşivlenmiş -15")
    uy = {"tam": 15, "uyarlanabilir": 10, "konu-claude-ozel": 5}[s["uyum"]["codex"]]
    p += uy; ac.append(f"Codex uyumu {uy}/15")
    yk = {"kucuk": 10, "orta": 8, "buyuk": 5}[s["baglam_yuku"]]
    p += yk; ac.append(f"bağlam yükü {yk}/10")
    yp = max(0, 5 - 2 * len([x for x in s["yapisal_sorunlar"] if "disable-model" not in x]))
    if s.get("kirik_baglantilar"):
        yp = max(0, yp - 2)
    p += yp; ac.append(f"yapı {yp}/5")
    if s.get("kalite"):
        p = round(0.6 * p + 0.4 * s["kalite"] * 20); ac.append(f"elle kalite {s['kalite']}/5 (%40 ağırlık)")
    t = s.get("trend")
    if t:  # GitHub Trending'e girmiş kaynak (araclar/github-trend.py)
        p += TREND_BONUS[t["seviye"]]; ac.append(f"GitHub trend +{TREND_BONUS[t['seviye']]} ({t['seviye']}, son {t['son']})")
    p = max(0, min(100, p))
    return {"puan": p, "not": "A" if p >= 80 else "B" if p >= 65 else "C" if p >= 50 else "D", "ayrinti": ac}


# "replicate" (İngilizce fiil) ve "prepaid" (muhasebe terimi) tek başına yanlış pozitif verir: servis adı/plan bağlamıyla aranır
UCRET_IZI = re.compile(r"\b[A-Z][A-Z0-9]*_API_KEY\b|primaryEnv|requires? (an? )?[\w .-]{0,30}api key|prepaid (credits?|plan|balance)|"
                       r"paid (plan|tier|api)|replicate\.com|REPLICATE_API|\breplicate (api|model)|"
                       r"\b(elevenlabs|heygen|fal\.ai|runpod|atlas ?cloud|dashscope|volcengine|fish\.audio|minimax)\b", re.I)


def ucret_belirle(s, tablo, kok_arsiv=None):
    """Ücret sınıfı: elle tablo > T4 toplu 'kismen' > ücretli servis izi varsa 'belirsiz' > 'ucretsiz'."""
    for anahtar in (s["id"], s["ad"]):
        if anahtar in tablo:
            sinif, not_ = tablo[anahtar]
            return sinif, not_, "elle"
    if s.get("tip") == "T4":
        return "kismen", "Composio hesabı gerekir (ücretsiz katman var); bağlanan uygulamanın kendi planı geçerli", "toplu"
    # Yeni arşiv henüz .arsiv-yeni içinde: yol "arsiv/..." oraya çevrilir (yoksa yeni skiller hiç taranmadan ücretsiz sayılırdı)
    sm = (kok_arsiv / Path(s["yol"]).relative_to("arsiv") if kok_arsiv else KOK / s["yol"]) / "SKILL.md"
    metin = sm.read_text(encoding="utf-8", errors="ignore") if sm.exists() else ""
    iz = sorted({m.group(0) for m in UCRET_IZI.finditer(metin)})[:5]
    if iz:
        return "belirsiz", "ücretli servis izi: " + ", ".join(iz) + " -> ucret-siniflandirma.json'a ekle", "otomatik"
    return "ucretsiz", "", "otomatik"


def kaynak_md(k):
    satirlar = [
        f"# {k['ad']}", "",
        "> Bu dosya SkillKutuphanesi tarafından eklendi; skill'in kendi dosyaları değiştirilmedi.", "",
        f"- **Kaynak repo:** https://github.com/{k['repo']}",
        f"- **Repo içindeki yol:** `{k['kaynak_yol'] or '(kök)'}`",
        f"- **Commit:** `{k['commit']}`",
        f"- **Lisans:** {k['lisans']}",
        f"- **Geliştirici:** {k['gelistirici'].get('sahip', '?')} ({k['gelistirici'].get('sahip_tipi', '?')})"
        if k.get("gelistirici") else "- **Geliştirici:** ?",
        f"- **Arşive alınma:** {k['arsiv_tarihi']}",
        f"- **Durum:** {k['durum']}",
    ]
    if k.get("ust_skill"):
        satirlar.append(f"- **Üst skill:** `{k['ust_skill']}` (bu skill onun alt klasörü; ayrıca da kurulabilir)")
    if k.get("bagimlilik"):
        satirlar.append(f"- **Bağımlılık:** {k['bagimlilik']}")
    if k.get("varyantlar"):
        satirlar.append("- **Araç sürümleri:** " + ", ".join(f"{a} → `{v}`" for a, v in k["varyantlar"].items()))
    if k.get("kardes_bagimliliklari"):
        satirlar.append("- **Kardeş skill bağımlılıkları** (`../<ad>/` bağlantıları; birlikte kurulmalı): "
                        + ", ".join(f"`{a}`" for a in k["kardes_bagimliliklari"]))
    if k.get("kirik_baglantilar"):
        satirlar.append("- **SKILL.md'de olup bulunamayan dosyalar:** " + ", ".join(f"`{x}`" for x in k["kirik_baglantilar"][:15]))
    if k.get("kopya_kaynaklar"):
        satirlar.append("- **Birebir aynısı şuralarda da var:** " + ", ".join(k["kopya_kaynaklar"]))
    if k.get("atlanan_dosyalar"):
        satirlar.append(f"- **Arşive alınmayan dosyalar ({len(k['atlanan_dosyalar'])}):** "
                        + ", ".join(f"`{x}`" for x in k["atlanan_dosyalar"][:15]))
    return "\n".join(satirlar) + "\n"


def kimlik_ata(gruplar, eski_kaynak):
    """Aynı adlı skiller içinde tercih/alternatif ve kimlik (id) ataması. KARARLIDIR: yeni eklenen bir kaynak, eşit öncelikte
    daha önce kayıtlı olanın yerini alamaz (kimlik kayması ve elle inceleme notlarının kaybı olmasın).
      1. sıra: (öncelik, daha önce kayıtlı olan, repo, yol)
      2. birebir aynı içerikte daha önce kayıtlı (incelenmiş olabilir) kayıt temsilci kalır, yenisi 'kopya' olarak not edilir
      3. elle verilen tercih (durum_elle) otomatik tercihi ezer; aynı adda tek 'tercih' kalır
    """
    def eskiden_var(k):
        return (k["repo"], k["kaynak_yol"]) in eski_kaynak

    def onceki(k):
        return eski_kaynak.get((k["repo"], k["kaynak_yol"]), {})

    yeni, kullanilan = [], set()
    for ad, liste in sorted(gruplar.items()):
        # Eşit öncelikte: önceki TERCİH kazanır, sonra diğer eski kayıtlar, en son yeniler (alfabetik sıra tercihi çevirmesin)
        liste.sort(key=lambda x: (x["oncelik"], 0 if onceki(x).get("durum") == "tercih" else 1 if eskiden_var(x) else 2,
                                  x["repo"], x["kaynak_yol"]))
        tekil = []
        for k in liste:
            ayni = next((t for t in tekil if t["_kh"] == k["_kh"]), None)  # TÜM klasör aynıysa kopya
            if ayni and eskiden_var(k) and not eskiden_var(ayni):
                # eski (incelenmiş) kayıt temsilci kalır; kayıt sırası/önceliği temsilcinin yerinde
                k.setdefault("kopya_kaynaklar", []).extend(ayni.get("kopya_kaynaklar", []))
                k["kopya_kaynaklar"].append(f"{ayni['repo']}:{ayni['kaynak_yol'] or '.'}")
                tekil[tekil.index(ayni)] = k
            elif ayni:
                ayni.setdefault("kopya_kaynaklar", []).append(f"{k['repo']}:{k['kaynak_yol'] or '.'}")
            else:
                tekil.append(k)
        # 1. geçiş: eski kayıtlar KİMLİKLERİNİ korur (roller/projeler çıplak adla çözülür; tam çalıştırmada kimlik kaymasın)
        for k in tekil:
            oid = onceki(k).get("id")
            if oid and (oid == ad or oid.startswith(ad + "@")) and oid not in kullanilan:
                k["id"] = oid
                kullanilan.add(oid)
        # 2. geçiş: yeni kayıtlar kuralla: ilk sıradaki çıplak ad, diğerleri ad@kaynak
        for i, k in enumerate(tekil):
            k["durum"] = "tercih" if i == 0 else "alternatif"
            if "id" not in k:
                kid = ad if i == 0 else f"{ad}@{kisa_kaynak(k['repo'])}"
                n = 2
                while kid in kullanilan:
                    kid = f"{ad}@{kisa_kaynak(k['repo'])}-{n}"
                    n += 1
                kullanilan.add(kid)
                k["id"] = kid
            yeni.append(k)
        elle_tercih = [k for k in tekil if onceki(k).get("durum_elle") and onceki(k).get("durum") == "tercih"]
        elle_alt = {id(k) for k in tekil if onceki(k).get("durum_elle") and onceki(k).get("durum") == "alternatif"}
        if elle_tercih or elle_alt:
            secilen = elle_tercih[0] if elle_tercih else next((k for k in tekil if id(k) not in elle_alt), tekil[0])
            for k in tekil:
                k["durum"] = "tercih" if k is secilen else "alternatif"
    return yeni


def main():
    manifest = json_oku(GECICI / "cekilen" / "manifest.json")
    if not manifest:
        sys.exit("Önce araclar/kaynak-cek.py çalıştır.")
    if not manifest.get("kayitlar"):
        sys.exit("DURDU: indirme manifestinde hiç kayıt yok (kaynak-cek.py hiçbir şey indirmedi). Arşive dokunulmadı.")
    # İndirme önbelleği (.gecici) kaynak listesinden SONRADAN silinen/kaldırılan repoların kayıtlarını taşıyabilir: onları diriltme
    _ayar0 = json_oku(KOK / "kaynaklar.json")
    _aktif = {(k["repo"], k["tip"]) for k in _ayar0["repolar"]}
    _cikar = {c["repo"] for c in _ayar0.get("arsivden_cikarilan_repolar", [])}
    manifest["kayitlar"] = [m for m in manifest["kayitlar"] if (m["repo"], m["tip"]) in _aktif and m["repo"] not in _cikar]
    manifest["bilesenler"] = [b for b in manifest.get("bilesenler", []) if b["repo"] in {r for r, _ in _aktif} and b["repo"] not in _cikar]
    eksik = [m for m in manifest["kayitlar"] if m["inen_dosya"] < m["beklenen_dosya"] or m.get("varyant_eksik")]
    if eksik:
        sys.exit("HATA: eksik inen skiller: " + ", ".join(f"{m['repo']}:{m['klasor_adi']}" for m in eksik))
    kural = json_oku(KURALLAR, {})
    kategoriler = json_oku(KATEGORILER)
    gelistiriciler = json_oku(GELISTIRICILER, {"repolar": {}})["repolar"]
    gecerli_kat = {f"{a}/{k}" for a, v in kategoriler["alanlar"].items() for k in v["kategoriler"]}
    eski_liste = json_oku(REGISTRY, {"skiller": []})["skiller"]
    # Elle inceleme alanları KAYNAĞA (repo + repo içi yol) bağlıdır; öncelik değişip id kaysa bile doğru skill'e gider
    eski_kaynak = {(s["repo"], s["kaynak_yol"]): s for s in eski_liste}

    gruplar = {}
    for k in manifest["kayitlar"]:
        k["ad"] = re.sub(r"[^a-z0-9._-]+", "-", k["ad"].strip().lower()).strip("-") or k["klasor_adi"]
        k["_yerel"] = GECICI / k["yerel"]
        if not (k["_yerel"] / "SKILL.md").exists():
            print(f"UYARI: SKILL.md inmemiş -> {k['repo']}:{k['kaynak_yol']}")
            continue
        k["_smh"] = skill_md_hash(k["_yerel"])
        k["_kh"] = klasor_hash(k["_yerel"])
        gruplar.setdefault(k["ad"], []).append(k)

    yeni = kimlik_ata(gruplar, eski_kaynak)

    # Yeni arşiv önce geçici klasöre kurulur; her şey başarılıysa eskisiyle yer değiştirir (yarım arşiv kalmaz)
    YENI = KOK / ".arsiv-yeni"
    shutil.rmtree(YENI, ignore_errors=True)
    YENI.mkdir()

    def goreli(p: Path) -> str:
        return "arsiv/" + str(p.relative_to(YENI))
    skiller, bekleyen = [], []
    bugun = date.today().isoformat()
    for k in yeni:
        onceki = eski_kaynak.get((k["repo"], k["kaynak_yol"]), {})
        kat = onceki["kategori"] if onceki.get("kategori_elle") else kurallari_uygula(kural, k)
        if k["tip"] == "T4":
            kat = "e-entegrasyon-katalogu/01-uygulama-entegrasyonlari"
        if kat not in gecerli_kat:
            print(f"UYARI geçersiz kategori {kat} -> {k['id']}")
            kat = "d-ai-otomasyon/04-skill-plugin-yazimi"
        hedef = YENI / kat / k["id"]
        shutil.copytree(k["_yerel"], hedef)
        varyantlar = {}
        for arac, yerel in (k.get("varyantlar") or {}).items():
            if yerel:
                vh = YENI / "_varyantlar" / k["id"] / arac
                shutil.copytree(GECICI / yerel, vh)
                varyantlar[arac] = goreli(vh)
        k["varyantlar"] = varyantlar
        metin = (hedef / "SKILL.md").read_text(encoding="utf-8", errors="replace")
        # Araçların göreceği hali (yorum arkasındaki frontmatter başa alınmış) okunur; teşhis orijinal metinden yapılır
        fm = frontmatter(frontmatter_onar(metin, k["ad"])[0])
        tum_metin = metin  # teknoloji tespiti sadece SKILL.md'den (referans dosyaları gürültü yapıyor)
        gel = gelistiriciler.get(k["repo"])
        adlar = "|".join(re.escape(x) for x in {k["klasor_adi"].split("~")[0], k["ad"]})
        yol_bag = sorted(set(re.findall(r"\.(?:claude|agents|codex)/skills/(?:" + adlar + r")\b", metin)))
        ana_hash = klasor_hash(hedef)
        varyant_hash = {a: klasor_hash(YENI / Path(v).relative_to("arsiv")) for a, v in varyantlar.items()}
        kurulum_hash = hashlib.sha256((ana_hash + "".join(f"|{a}:{h}" for a, h in sorted(varyant_hash.items()))).encode()).hexdigest()
        kayit = {
            "id": k["id"], "ad": k["ad"], "durum": k["durum"], "kategori": kat, "alan": kat.split("/")[0],
            "yol": goreli(hedef), "varyantlar": varyantlar,
            "repo": k["repo"], "kaynak_yol": k["kaynak_yol"], "commit": k["commit"], "lisans": k["lisans"],
            "tip": k["tip"], "gizli": k["tip"] in GIZLI_TIPLER,
            "arsiv_tarihi": onceki.get("arsiv_tarihi") if onceki.get("commit") == k["commit"] else bugun,
            "ust_skill": k.get("ust_skill"), "bagimlilik": k.get("bagimlilik"),
            "kopya_kaynaklar": k.get("kopya_kaynaklar", []), "ayna_sayisi": len(k["aynalar"]),
            "atlanan_dosyalar": k.get("atlanan_dosyalar", []),
            "aciklama": ((onceki.get("aciklama_duzeltme") or {}).get("description") or fm.get("description")
                         or k["aciklama"])[:600],  # kurulan kopyanın description'ı (öneri/katalog bununla arar)
            "teknoloji_oto": sorted(t for t, d in TEKNOLOJI_DESENLERI.items() if re.search(d, tum_metin, re.I)),
            "uyum": onceki.get("uyum_elle") or uyum_tespit(metin, k, fm),
            "yapisal_sorunlar": yapisal_sorunlar(fm, metin, k["ad"]),
            "yol_bagimliligi": bool(yol_bag),
            "kirik_baglantilar": kirik_baglantilar(hedef),
            "baglam_yuku": baglam_yuku(hedef), "boyut_kb": round(boyut(hedef) / 1024),
            "skill_md_kb": round((hedef / "SKILL.md").stat().st_size / 1024, 1),
            "klasor_adi": k["klasor_adi"].split("~")[0],
            "skill_md_hash": k["_smh"], "ana_hash": ana_hash, "varyant_hash": varyant_hash,
            "klasor_hash": kurulum_hash,  # ana + araç sürümleri: herhangi biri değişirse güncelleme görünür
            "globalde": global_durum(k["ad"], ana_hash),
            "gelistirici": gel or {}, "inceleme": "otomatik",
        }
        for alan in ELLE_ALANLAR:
            if alan in onceki:
                kayit[alan] = onceki[alan]
        if onceki.get("durum_elle"):
            kayit["durum"] = onceki["durum"]
        # İncelenmiş bir skill'in içeriği güncellemede değiştiyse inceleme eskidi: yeniden incelenecek olarak işaretle
        if (onceki.get("inceleme") in ("incelendi", "toplu-incelendi")
                and onceki.get("klasor_hash") and onceki["klasor_hash"] != kayit["klasor_hash"]):
            kayit["inceleme"] = "yeniden-incelenecek"
            kayit["onceki_inceleme"] = {"inceleme": onceki["inceleme"], "tarih": onceki.get("inceleme_tarihi"),
                                        "commit": onceki.get("inceleme_commit") or onceki.get("commit")}
        skiller.append(kayit)
        bekleyen.append((k, kayit, hedef, gel))

    # Kardeş bağımlılıkları: ../<kardeş-skill>/... bağlantıları kırık değil, kardeş skill'e bağımlılıktır
    indeks = {}
    for _, kayit, hedef, _ in bekleyen:
        for ad in {kayit["klasor_adi"], kayit["ad"]}:
            indeks.setdefault(ad, []).append((kayit, hedef))
    for k, kayit, hedef, gel in bekleyen:
        kardes, cozulen = kardes_baglantilari(hedef, indeks, kayit)
        if kardes:
            kayit["kardes_bagimliliklari"] = kardes
        kayit["kirik_baglantilar"] = [x for x in kayit["kirik_baglantilar"] if x not in cozulen]
        kayit["degerlendirme"] = degerlendir(kayit, gel)
        (hedef / "KAYNAK.md").write_text(kaynak_md({**k, **kayit}), encoding="utf-8")

    # Korunan eski kayıtlar:
    #  - KAYIP kaynaklar (silinmiş/private olmuş repo)
    #  - Kaynakta KALDIRILAN skiller (repo duruyor ama skill yeni commit'te yok; ör. emekliye ayrılan iş akışı skilleri)
    # Eski arşiv kopyası ve kayıt (elle inceleme alanlarıyla) korunur; projeler ve roller bozulmaz.
    kayip = {k["repo"] for k in json_oku(KOK / "kaynaklar.json")["repolar"] if k["tip"] == "KAYIP"}
    cekilen_repolar = {m["repo"] for m in manifest["kayitlar"]}
    yeni_kaynaklar = {(x["repo"], x["kaynak_yol"]) for x in skiller}
    kullanilan_id = {x["id"] for x in skiller}
    arsivlenen_repolar = {k["repo"] for k in json_oku(KOK / "kaynaklar.json")["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4")}
    korunan_indirilmeyen = set()
    # Kullanıcı kararıyla arşivden çıkarılanlar (ör. emekli eski sürümler): korunmaz, kayıp kilidine takılmaz
    _ayar = json_oku(KOK / "kaynaklar.json")
    cikarilan = {(c["repo"], c["kaynak_yol"]) for c in _ayar.get("arsivden_cikarilanlar", [])}
    cikarilan_repo = {c["repo"] for c in _ayar.get("arsivden_cikarilan_repolar", [])}  # bütün repo bilerek kaldırıldı
    for s in eski_liste:
        kaynak = (s["repo"], s["kaynak_yol"])
        if kaynak in yeni_kaynaklar or kaynak in cikarilan or s["repo"] in cikarilan_repo:
            continue
        if s["repo"] in kayip:
            s["kaynak_durumu"] = "kayip"
        elif s["repo"] not in cekilen_repolar and s["repo"] in arsivlenen_repolar:
            # Bu çalıştırmada İNDİRİLMEMİŞ kaynak (ör. `kaynak-cek.py --repo X` ile tek repo eklendi):
            # kayıt ve arşiv kopyası OLDUĞU GİBİ korunur; aksi hâlde kısmi çalıştırma tüm arşivi silerdi.
            korunan_indirilmeyen.add(s["id"])
        elif s["repo"] in cekilen_repolar and s.get("tip") in ("T1", "T2", "T3", "T4"):
            s["kaynak_durumu"] = "kaynakta-kaldirildi"
            s.setdefault("kaldirilma_tarihi", bugun)
            s.setdefault("kaldirildigi_commit", next(m["commit"] for m in manifest["kayitlar"] if m["repo"] == s["repo"]))
        else:
            continue
        if s["id"] not in korunan_indirilmeyen and any(x["ad"] == s["ad"] and x["durum"] == "tercih" for x in skiller):
            s["durum"] = "alternatif"  # aynı adın güncel bir tercihi varsa o kazanır
        if s["id"] in kullanilan_id and s["id"] not in korunan_indirilmeyen:
            s["id"] = f"{s['ad']}@{kisa_kaynak(s['repo'])}-eski"
        elif s["id"] in kullanilan_id:
            # Korunan (indirilmeyen) skill kimliğini korur (projelerdeki kilit dosyaları ona bağlı);
            # aynı kimliği almış YENİ indirilen skill 'ad@kaynak' kimliğine taşınır. Tercihi aşağıda öncelik belirler.
            y = next(x for x in skiller if x["id"] == s["id"])
            yeni_id = f"{y['ad']}@{kisa_kaynak(y['repo'])}"
            n = 2
            while yeni_id in kullanilan_id:
                yeni_id = f"{y['ad']}@{kisa_kaynak(y['repo'])}-{n}"
                n += 1
            eski_k = YENI / Path(y["yol"]).relative_to("arsiv")
            yeni_k = eski_k.parent / yeni_id
            eski_k.rename(yeni_k)
            vk = YENI / "_varyantlar" / y["id"]
            if vk.exists():
                vk.rename(YENI / "_varyantlar" / yeni_id)
                y["varyantlar"] = {a: v.replace(f"/_varyantlar/{y['id']}/", f"/_varyantlar/{yeni_id}/")
                                   for a, v in (y.get("varyantlar") or {}).items()}
            print(f"KİMLİK: yeni {y['repo']} '{y['id']}' -> '{yeni_id}' (korunan {s['repo']} kimliğini korur)")
            y["id"], y["yol"] = yeni_id, goreli(yeni_k)
            kullanilan_id.add(yeni_id)
        kullanilan_id.add(s["id"])
        eski_yol = KOK / s["yol"]
        if not (eski_yol / "SKILL.md").exists():
            print(f"UYARI: KAYIP kaynağın arşiv kopyası da yok: {s['yol']}")
            continue
        hedef_yeni = YENI / s["kategori"] / s["id"]  # id değişmiş olabilir (-eski): yeni yola kopyala
        shutil.copytree(eski_yol, hedef_yeni)
        s["yol"] = goreli(hedef_yeni)
        yeni_var = {}
        for arac, v in (s.get("varyantlar") or {}).items():
            if (KOK / v).exists():
                vh = YENI / "_varyantlar" / s["id"] / arac
                shutil.copytree(KOK / v, vh)
                yeni_var[arac] = goreli(vh)
        s["varyantlar"] = yeni_var
        skiller.append(s)

    # Kısmi indirme: korunan (indirilmeyen) bir skill ile yeni indirilen skill aynı adı taşıyorsa çakışmayı çöz
    oncelik = {}
    for k in json_oku(KOK / "kaynaklar.json")["repolar"]:
        oncelik[k["repo"]] = min(oncelik.get(k["repo"], 99), k.get("oncelik", 5))
    korunan = {s["id"]: s for s in skiller if s["id"] in korunan_indirilmeyen}
    for y in [s for s in skiller if s["id"] not in korunan_indirilmeyen]:
        adaylar = [k for k in korunan.values() if k["ad"] == y["ad"]]
        # Rakip: korunanlar içinde TERCİH olan (yoksa en yüksek öncelikli); rastgele bir alternatifle kıyaslanırsa
        # yeni skill onu geçip ikinci bir 'tercih' olabiliyordu (ör. code-review: anthropics tercih dururken mattpocock)
        rakip = next((k for k in adaylar if k["durum"] == "tercih"), None) or \
            (min(adaylar, key=lambda k: oncelik.get(k["repo"], 5)) if adaylar else None)
        if not rakip:
            continue
        if rakip.get("ana_hash") == y.get("ana_hash"):
            # birebir aynı içerik: yeni kayıt eklenmez, korunanın kopya kaynağı olur
            rakip.setdefault("kopya_kaynaklar", []).append(f"{y['repo']}:{y['kaynak_yol'] or '.'}")
            shutil.rmtree(YENI / Path(y["yol"]).relative_to("arsiv"), ignore_errors=True)
            skiller.remove(y)
            print(f"ÇAKIŞMA: {y['id']} birebir aynısı {rakip['id']} -> kopya olarak not edildi")
            continue
        yeni_kazanir = oncelik.get(y["repo"], 5) < oncelik.get(rakip["repo"], 5)
        # Gizli (repo-içi T3 / entegrasyon T4) skill görünür skill'i asla geçmez (repo bazlı öncelik aynı repodaki
        # resmî bir kayıttan gelebilir: ör. remotion-dev/remotion T2 öncelik 1 + T3 repo-içi 'release')
        if y.get("gizli") != rakip.get("gizli"):
            yeni_kazanir = not y.get("gizli")
        # elle verilen karar (durum_elle) önceliği ezer
        if (rakip.get("durum_elle") and rakip["durum"] == "tercih") or (y.get("durum_elle") and y["durum"] == "alternatif"):
            yeni_kazanir = False
        elif y.get("durum_elle") and y["durum"] == "tercih":
            yeni_kazanir = True
        elif rakip.get("durum_elle") and rakip["durum"] == "alternatif":
            # korunan elle 'alternatif': ona dokunma; yeni skill indirme sırasındaki (aynı adlı yenilerle) kararını korur
            print(f"ÇAKIŞMA: '{y['ad']}' -> korunan {rakip['id']} elle alternatif; {y['id']} durumu: {y['durum']}")
            continue
        kaybeden = rakip if yeni_kazanir else y
        kazanan = y if yeni_kazanir else rakip
        if kazanan["durum"] != "tercih" and not any(x["ad"] == kazanan["ad"] and x["durum"] == "tercih" and x is not kaybeden for x in skiller):
            kazanan["durum"] = "tercih"
        kaybeden["durum"] = "alternatif"
        if kaybeden["id"] == kaybeden["ad"]:
            yeni_id = f"{kaybeden['ad']}@{kisa_kaynak(kaybeden['repo'])}"
            n = 2
            while yeni_id in kullanilan_id:
                yeni_id = f"{kaybeden['ad']}@{kisa_kaynak(kaybeden['repo'])}-{n}"
                n += 1
            eski_k = YENI / Path(kaybeden["yol"]).relative_to("arsiv")
            yeni_k = eski_k.parent / yeni_id
            if eski_k.exists():
                eski_k.rename(yeni_k)
            vk = YENI / "_varyantlar" / kaybeden["id"]
            if vk.exists():
                vk.rename(YENI / "_varyantlar" / yeni_id)
                kaybeden["varyantlar"] = {a: v.replace(f"/_varyantlar/{kaybeden['id']}/", f"/_varyantlar/{yeni_id}/")
                                          for a, v in (kaybeden.get("varyantlar") or {}).items()}
            kaybeden["id"] = yeni_id
            kaybeden["yol"] = goreli(yeni_k)
            kullanilan_id.add(yeni_id)
        print(f"ÇAKIŞMA: '{kazanan['ad']}' -> tercih {kazanan['id']} ({kazanan['repo']}), alternatif {kaybeden['id']} ({kaybeden['repo']})")

    bilesenler = []
    # indirilmeyen kaynakların bileşenleri korunur
    for b in json_oku(REGISTRY, {}).get("bilesenler", []):
        if b["repo"] not in cekilen_repolar and b["repo"] in arsivlenen_repolar and (KOK / b["yol"]).exists():
            h = YENI / Path(b["yol"]).relative_to("arsiv")
            h.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(KOK / b["yol"], h)
            bilesenler.append(b)
    for b in manifest.get("bilesenler", []):
        h = YENI / "_bilesenler" / b["kimlik"] / b["yol"]
        h.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(GECICI / b["yerel"], h)
        tur = "komut" if "/commands/" in "/" + b["yol"] else "agent"
        bilesenler.append({"repo": b["repo"], "commit": b["commit"], "tur": tur, "kaynak_yol": b["yol"],
                           "yol": goreli(h), "ad": Path(b["yol"]).stem})

    for s in skiller:  # kısmi çalıştırma yolu aynı kopyayı her seferinde yeniden ekliyordu: sırayı koruyarak tekilleştir
        if s.get("kopya_kaynaklar"):
            s["kopya_kaynaklar"] = list(dict.fromkeys(s["kopya_kaynaklar"]))
    ucret_tablo = json_oku(KOK / "ucret-siniflandirma.json", {"siniflar": {}})["siniflar"]
    trend = json_oku(TREND, {})
    for s in skiller:
        s["ucret"], s["ucret_notu"], s["ucret_kaynagi"] = ucret_belirle(s, ucret_tablo, YENI)
        t = trend_durumu(s["repo"], trend)
        if t:
            s["trend"] = t
        else:
            s.pop("trend", None)
        if gelistiriciler.get(s["repo"]):  # indirilmeyen (korunan) kayıtlar da güncel geliştirici bilgisini alsın
            s["gelistirici"] = gelistiriciler[s["repo"]]
        s["degerlendirme"] = degerlendir(s, s.get("gelistirici"))  # trend ve korunan kayıtlar dahil hepsi güncel puanla
    skiller.sort(key=lambda s: (s["kategori"], s["id"]))
    # Güvenlik kilidi: önceki registry'deki kaynakların hepsi ya yeniden yerleşmiş ya da korunmuş olmalı.
    yeni_k = {(s["repo"], s["kaynak_yol"]) for s in skiller}
    kayip_k = [s["id"] for s in eski_liste if (s["repo"], s["kaynak_yol"]) not in yeni_k
               and (s["repo"], s["kaynak_yol"]) not in cikarilan and s["repo"] not in cikarilan_repo
               and not any(f"{s['repo']}:{s['kaynak_yol'] or '.'}" in x.get("kopya_kaynaklar", []) for x in skiller)]
    if kayip_k and "--kayba-izin-ver" not in sys.argv:
        shutil.rmtree(YENI, ignore_errors=True)
        sys.exit(f"DURDU (güvenlik kilidi): önceki {len(kayip_k)} skill yeni arşivde yok ({', '.join(kayip_k[:8])}…). "
                 "Arşive ve registry'ye DOKUNULMADI. Bilerek kaldırıyorsan --kayba-izin-ver ile çalıştır.")
    reg_yeni = KOK / ".registry-yeni.json"
    json_yaz(reg_yeni, {"_aciklama": "TEK GERÇEK KAYNAK. araclar/arsiv-yerlestir.py üretir; inceleme alanları elle doldurulur ve korunur.",
                        "guncelleme": bugun, "skiller": skiller, "bilesenler": bilesenler,
                        "denetim": {**{r: d for r, d in json_oku(REGISTRY, {}).get("denetim", {}).items()
                                        if r not in cekilen_repolar and r in arsivlenen_repolar},
                                     **manifest.get("denetim", {})}})
    # Yer değiştirme: önce her şey hazır, sonra iki hızlı rename
    eski_arsiv = KOK / ".arsiv-eski"
    shutil.rmtree(eski_arsiv, ignore_errors=True)
    if ARSIV.exists():
        ARSIV.rename(eski_arsiv)
    try:
        YENI.rename(ARSIV)
        os.replace(reg_yeni, REGISTRY)
    except Exception:
        if eski_arsiv.exists() and not ARSIV.exists():
            eski_arsiv.rename(ARSIV)
        raise
    shutil.rmtree(eski_arsiv, ignore_errors=True)
    tercih = sum(1 for s in skiller if s["durum"] == "tercih")
    print(f"Arşive yerleşen: {len(skiller)} (tercih {tercih}, alternatif {len(skiller) - tercih}, "
          f"gizli {sum(s['gizli'] for s in skiller)}, araç sürümlü {sum(1 for s in skiller if s['varyantlar'])}, "
          f"bileşen {len(bilesenler)})")


if __name__ == "__main__":
    main()
