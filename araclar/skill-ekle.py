#!/usr/bin/env python3
"""Projeye skill / rol / profil ekler. SADECE verilen proje klasörüne yazar; global klasörlere asla dokunmaz.

Projede oluşanlar:
  .agents/skills/<skill>/          Codex'in okuduğu kopya (varsa Codex'e özel sürüm)
  .claude/skills/<skill>           Claude Code: symlink -> ../../.agents/skills/<skill>
                                   (skill'in Claude'a özel sürümü varsa symlink yerine o sürümün kopyası)
  .claude/agents/<rol>.md          Claude alt-agent'ı (frontmatter 'skills:' = sadece o rolün skilleri)
  .codex/agents/<rol>.toml         Codex alt-agent'ı (rol dışı proje skilleri [[skills.config]] ile kapalı)
  AGENTS.md / CLAUDE.md            işaretli blok (sadece o blok yeniden yazılır)
  .skill-kutuphanesi/kilit.json    hangi skill, hangi commit, hangi rol, kurulu içerik parmak izi
  .skill-kutuphanesi/yedek/        her işlemden önce otomatik yedek (son 10; --yedekler, --geri-al [ad])
  .skill-kutuphanesi/son-rapor.md  son UYGULANAN kurulumun ön kontrol raporu (--kuru hiçbir dosya yazmaz)

Güvenlik kuralları:
  * Her işlemden önce ÖN KONTROL çalışır. HATA varsa işlem yapılmaz (--zorla ile yedek alınarak geçilebilir).
    UYARI varsa onay istenir; etkileşimsiz çalışmada (agent) --evet verilmedikçe işlem yapılmaz.
  * Kütüphanedeki TÜM skiller taranır; seçilmeyen ama ilgili adaylar raporda listelenir (hiçbiri görmezden gelinmez).
  * Projedeki, kütüphaneden gelmeyen aynı isimli skill'in üzerine asla yazılmaz.
  * Elle değiştirilmiş kurulu skill güncelleme/kaldırmada ezilmez (--zorla ile yedeklenip ezilir).
  * Hata olursa yapılan değişiklikler yedekten otomatik geri alınır. Elle geri alma: --geri-al

Örnekler:
  python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --kuru     # önce sadece rapor
  python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --evet     # uygula
  python3 araclar/skill-ekle.py ~/Projeler/site --rol motion-gelistirici --opsiyonel --evet
  python3 araclar/skill-ekle.py ~/Projeler/site --skill design-taste-frontend gsap-core --rol-adi ui-tasarimci --evet
  python3 araclar/skill-ekle.py ~/Projeler/site --oner "3d ürün tanıtım sitesi scroll animasyonlu"
  python3 araclar/skill-ekle.py ~/Projeler/site --durum | --dogrula | --guncelle | --yenile | --geri-al
  python3 araclar/skill-ekle.py ~/Projeler/site --kaldir gsap-core     (ya da --kaldir hepsi)
  python3 araclar/skill-ekle.py --listele --kategori 03 --teknoloji react
"""
import argparse
import json
import os
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GLOBAL_KLASORLER, KOK, REGISTRY, global_durum, json_oku, json_yaz, klasor_hash  # noqa: E402

ROLLER = KOK / "roller"
PROFILLER = KOK / "profiller"
BLOK_BAS, BLOK_SON = "<!-- skill-kutuphanesi:basla -->", "<!-- skill-kutuphanesi:bitir -->"
URETILDI = "skill-kutuphanesi tarafından üretildi"
META = ".skill-kutuphanesi"
KILIT_SURUM = 3
ROL_ADI = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
YEDEK_SAYISI = 10
# --zorla ile bile GEÇİLEMEYEN hatalar (güvenlik / tutarlılık)
ZORLANAMAZ = {"gecersiz-rol-adi", "global-baglanti", "proje-disi-baglanti", "ayni-klasor", "bulunamadi",
              "isim-cakismasi", "onyukleme-siniri", "farkli-kaynak", "kendi-agent-dosyan"}
SINIR_ROL_SKILL = 12          # bir role önerilen en fazla skill
SINIR_ROL_KB = 150            # bir rolün önyüklenen SKILL.md toplamı (KB)
SINIR_CLAUDE_ONYUKLEME = 32   # Claude alt-agent 'skills:' sınırı

ES_ANLAM = {  # Türkçe sorgu -> İngilizce açıklamalarda aranacak kelimeler
    "animasyon": "animation animate motion", "hareket": "motion animation", "kaydırma": "scroll", "scroll": "scroll",
    "3d": "3d three webgl", "üç boyut": "3d three", "tasarım": "design ui ux", "arayüz": "ui interface frontend",
    "renk": "color palette", "yazı tipi": "font typography", "tipografi": "typography font", "marka": "brand",
    "logo": "logo brand", "test": "test testing", "hata": "debug bug error", "doküman": "document docs",
    "belge": "document", "rapor": "report document", "sunum": "presentation slides pptx", "tablo": "spreadsheet xlsx",
    "excel": "xlsx spreadsheet", "word": "docx", "pdf": "pdf", "oyun": "game", "video": "video",
    "ses": "audio voice speech", "seslendirme": "tts text-to-speech voice narration", "müzik": "music",
    "altyazı": "caption subtitle", "görsel": "image visual", "resim": "image", "erişilebilirlik": "accessibility a11y",
    "performans": "performance", "güvenlik": "security", "veritabanı": "database", "api": "api",
    "plan": "plan planning", "inceleme": "review", "diyagram": "diagram", "not": "notes obsidian",
    "araştırma": "research", "web sitesi": "website web landing", "site": "website web", "tanıtım": "promo launch marketing landing",
    "ürün": "product", "panel": "dashboard admin", "mobil": "mobile", "e-ticaret": "ecommerce shop",
    "yapay zeka": "ai generative", "ajan": "agent", "otomasyon": "automation", "karakter": "character",
}
TEKNOLOJI_IPUCU = {  # package.json bağımlılığı -> teknoloji etiketi
    "react": "react", "next": "next.js", "vue": "vue", "svelte": "svelte", "tailwindcss": "tailwind",
    "three": "three.js", "@react-three/fiber": "r3f", "gsap": "gsap", "motion": "motion", "framer-motion": "motion",
    "lenis": "lenis", "lottie-web": "lottie", "playwright": "playwright", "@playwright/test": "playwright",
    "typescript": "typescript", "remotion": "remotion",
}


# ================================================================== yardımcılar
class Rapor:
    def __init__(self):
        self.satirlar = []

    def ekle(self, seviye, kod, mesaj):
        self.satirlar.append((seviye, kod, mesaj))

    def say(self, seviye):
        return sum(1 for s in self.satirlar if s[0] == seviye)

    def gruplu(self, seviye):
        """'ad: açıklama' biçimindeki aynı kod + aynı açıklamalı satırları tek satırda toplar."""
        gruplar = {}
        for s, kod, m in self.satirlar:
            if s != seviye:
                continue
            ad, ayir, govde = m.partition(": ")
            anahtar = (kod, govde if ayir and " " not in ad else m)
            gruplar.setdefault(anahtar, []).append(ad if ayir and " " not in ad else None)
        for (kod, govde), adlar in gruplar.items():
            adlar = [a for a in adlar if a]
            yield kod, (f"{', '.join(adlar)}: {govde}" if adlar else govde)

    def yazdir(self):
        for seviye in ("HATA", "UYARI", "BİLGİ"):
            for kod, m in self.gruplu(seviye):
                print(f"  [{seviye}] {kod}: {m}")

    def markdown(self, baslik):
        out = [f"# {baslik}", "", f"Tarih: {datetime.now():%Y-%m-%d %H:%M}", ""]
        for seviye in ("HATA", "UYARI", "BİLGİ"):
            liste = list(self.gruplu(seviye))
            if liste:
                out += [f"## {seviye} ({self.say(seviye)})", ""] + [f"- **{k}**: {m}" for k, m in liste] + [""]
        return "\n".join(out)


def registry():
    r = json_oku(REGISTRY)
    if not r or not r.get("skiller"):
        sys.exit("registry.json yok ya da boş. Önce: python3 araclar/arsiv-yerlestir.py")
    return r["skiller"]


def bul(skiller, anahtar):
    """Kullanıcı isteği için: id ile tam eşleşme; yoksa ad ile 'tercih' kaydı."""
    for s in skiller:
        if s["id"] == anahtar:
            return s
    adaylar = sorted((s for s in skiller if s["ad"] == anahtar), key=lambda s: s["durum"] != "tercih")
    return adaylar[0] if adaylar else None


def kaynak_bul(skiller, k):
    """Kurulu bir skill'i KAYNAĞINA göre bul (repo + repo içi yol). id değişse bile doğru skill bulunur;
    kaynak artık yoksa None (başka bir repo'nun aynı adlı skill'i ASLA yerine konmaz)."""
    if "kaynak_yol" in k:
        return next((s for s in skiller if s["repo"] == k["repo"] and s["kaynak_yol"] == k["kaynak_yol"]), None)
    s = next((s for s in skiller if s["id"] == k["id"]), None)  # eski kilit: sadece aynı repodan kabul et
    return s if s and s["repo"] == k.get("repo", s["repo"]) else None


def canli_global(s):
    """Global klasörler kurulum anında yeniden okunur (registry'deki bilgi eskimiş olabilir)."""
    return global_durum(s["ad"], s.get("ana_hash") or s["klasor_hash"])


def kurulum_adi(s, kilit=None):
    """Projede kullanılacak klasör/skill adı.
    - Kilitte bu KAYNAK zaten kuruluysa: o ad (ad sonradan değişmez, çift kurulum olmaz).
    - Alternatif sürüm: <ad>--<kaynak>.
    - Global klasörde aynı adlı FARKLI içerik varsa (Claude'da kişisel skill proje skill'ini ezer): <ad>--kutuphane."""
    if kilit:
        for ad, k in kilit["skiller"].items():
            if k.get("repo") == s["repo"] and k.get("kaynak_yol", None) == s["kaynak_yol"]:
                return ad
    ad = s["ad"] if ROL_ADI.match(s["ad"]) else (re.sub(r"[^a-z0-9-]+", "-", s["ad"].lower()).strip("-")[:64] or "skill")
    if "@" in s["id"]:
        ad = f"{ad}--{s['id'].split('@')[1]}"
    elif any(v == "farkli" for v in canli_global(s).values()):
        ad = f"{ad}--kutuphane"
    return ad[:64]


def meta(proje):
    return proje / META


def kilit_oku(proje):
    k = json_oku(meta(proje) / "kilit.json")
    if k is None:
        eski = proje / ".agents" / "skills" / "SKILLS.lock.json"  # sürüm 1 kilidi
        k = json_oku(eski) if eski.exists() else None
    if k is None:
        k = {"surum": KILIT_SURUM, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}}
    k.setdefault("roller", [])
    k.setdefault("skiller", {})
    k.setdefault("profil", None)
    for v in k["skiller"].values():
        v.setdefault("roller", [])
    k["surum"] = KILIT_SURUM
    return k


def kilit_yaz(proje, kilit):
    kilit["guncelleme"] = date.today().isoformat()
    kilit["proje_yolu"] = str(proje)
    meta(proje).mkdir(exist_ok=True)
    json_yaz(meta(proje) / "kilit.json", kilit)


def kurulu_hash(proje, ad):
    h = proje / ".agents" / "skills" / ad
    c = proje / ".claude" / "skills" / ad
    return {"codex": klasor_hash(h) if h.is_dir() else None,
            "claude": klasor_hash(c) if (c.is_dir() and not c.is_symlink()) else "symlink" if c.is_symlink() else None}


def elle_degismis(proje, ad, kayit):
    beklenen = kayit.get("kurulu_hash")
    return bool(beklenen) and kurulu_hash(proje, ad) != beklenen


# ================================================================== yedek / geri alma
def yedekle(proje, adlar, neden):
    zaman = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    y = meta(proje) / "yedek" / zaman
    y.mkdir(parents=True)
    hedefler = [".claude/agents", ".codex/agents", "AGENTS.md", "CLAUDE.md", f"{META}/kilit.json"]
    hedefler += [f".agents/skills/{a}" for a in adlar] + [f".claude/skills/{a}" for a in adlar]
    var_olan = []
    for rel in hedefler:
        kaynak = proje / rel
        if kaynak.is_symlink():
            (y / rel).parent.mkdir(parents=True, exist_ok=True)
            os.symlink(os.readlink(kaynak), y / rel)
            var_olan.append(rel)
        elif kaynak.is_dir():
            shutil.copytree(kaynak, y / rel, symlinks=True)
            var_olan.append(rel)
        elif kaynak.is_file():
            (y / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(kaynak, y / rel)
            var_olan.append(rel)
    json_yaz(y / "yedek.json", {"neden": neden, "zaman": zaman, "hedefler": hedefler, "var_olan": var_olan})
    yedekler = sorted((meta(proje) / "yedek").iterdir())
    for eski in yedekler[:-YEDEK_SAYISI]:
        shutil.rmtree(eski, ignore_errors=True)
    return y


def sil_yol(p: Path):
    if p.is_symlink() or p.is_file():
        p.unlink()
    elif p.is_dir():
        shutil.rmtree(p)


def geri_yukle(proje, y: Path):
    bilgi = json_oku(y / "yedek.json")
    for rel in bilgi["hedefler"]:
        sil_yol(proje / rel)
    for rel in bilgi["var_olan"]:
        k, h = y / rel, proje / rel
        h.parent.mkdir(parents=True, exist_ok=True)
        if k.is_symlink():
            os.symlink(os.readlink(k), h)
        elif k.is_dir():
            shutil.copytree(k, h, symlinks=True)
        else:
            shutil.copy2(k, h)
    return bilgi


# ================================================================== kurulum
def metin_oku(f: Path):
    return f.read_bytes().decode("utf-8")


def metin_yaz(f: Path, metin: str):
    f.write_bytes(metin.encode("utf-8"))  # satır sonları (CRLF/LF) olduğu gibi kalır


def yollari_yeniden_adlandir(klasor: Path, eski_adlar, yeni: str):
    """Skill kendi yolunu içeriyorsa (.claude/skills/<ad>/scripts…) yeniden adlandırınca bu yolları da düzelt."""
    eski_adlar = {a for a in eski_adlar if a and a != yeni}
    if not eski_adlar:
        return
    desen = re.compile(r"(\.(?:claude|agents|codex)/skills/)(?:" + "|".join(re.escape(a) for a in eski_adlar)
                       + r")(?=[/\s`'\")\]]|$)", re.M)
    for f in klasor.rglob("*"):
        if f.is_file() and f.suffix.lower() in (".md", ".sh", ".cmd", ".ps1", ".py", ".js", ".mjs", ".json", ".txt", ""):
            try:
                metin = metin_oku(f)
            except (UnicodeDecodeError, OSError):
                continue
            yeni_metin = desen.sub(lambda m: m.group(1) + yeni, metin)
            if yeni_metin != metin:
                metin_yaz(f, yeni_metin)


def kardes_haritasi(s, skiller, kilit, kur_listesi=None, adlar=None):
    """Skill'in ../<kardeş>/ bağlantıları için {kardeş adı: (projedeki kurulum adı, kurulu mu)}.
    Öncelik: bu işlemde kurulan, sonra projede zaten kurulu olan; ikisi de yoksa kardeşin alacağı ad tahmin edilir."""
    harita = {}
    for kad, bilgi in (s.get("kardes_bagimliliklari") or {}).items():
        bulunan = None
        for sid, (x, _) in (kur_listesi or {}).items():
            if x["ad"] == kad or x.get("klasor_adi") == kad:
                bulunan = (sid == bilgi["id"], adlar[sid])
                if bulunan[0]:
                    break
        if not bulunan:
            for ad, k in kilit["skiller"].items():
                x = kaynak_bul(skiller, k)
                if x and (x["ad"] == kad or x.get("klasor_adi") == kad):
                    bulunan = (x["id"] == bilgi["id"], ad)
                    if bulunan[0]:
                        break
        if bulunan:
            harita[kad] = (bulunan[1], True)
        else:
            x = next((x for x in skiller if x["id"] == bilgi["id"]), None)
            harita[kad] = (kurulum_adi(x, kilit) if x else kad, False)
    return harita


def kardes_yollarini_yeniden_adlandir(klasor: Path, harita):
    """../<kardeş>/... bağlantılarını kardeşin projedeki adına çevirir (ör. ../hyperframes/ -> ../hyperframes--kutuphane/).
    Sadece skill kökünden tam bir seviye yukarı çıkan yollar değişir (dosya derinliğine göre ../ sayısı)."""
    harita = {k: v for k, v in harita.items() if k != v}
    if not harita:
        return
    adlar = "|".join(re.escape(a) for a in sorted(harita, key=len, reverse=True))
    for f in klasor.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in (".md", ".mdx", ".txt", ".sh", ".py", ".js", ".mjs", ".json", ""):
            continue
        try:
            metin = metin_oku(f)
        except (UnicodeDecodeError, OSError):
            continue
        onek = re.escape("../" * len(f.relative_to(klasor).parts))
        desen = re.compile(r"(?<![\w./-])(" + onek + r")(" + adlar + r")(?=[/)\s`'\"#]|$)", re.M)
        yeni_metin = desen.sub(lambda m: m.group(1) + harita[m.group(2)], metin)
        if yeni_metin != metin:
            metin_yaz(f, yeni_metin)


def isim_esitle(skill_md: Path, ad: str):
    """SADECE frontmatter içindeki name alanını klasör adına eşitler (gövdedeki örnek yaml'lara dokunmaz)."""
    metin = metin_oku(skill_md)
    m = re.match(r"^(\ufeff?---[ \t]*(\r?\n))(.*?)(\r?\n---[ \t]*(?:\r?\n|$))", metin, re.S)
    if not m:
        nl = "\r\n" if "\r\n" in metin else "\n"
        metin_yaz(skill_md, f"---{nl}name: {ad}{nl}description: {ad}{nl}---{nl}{nl}" + metin)
        return
    bas, nl, govde, son = m.group(1), m.group(2), m.group(3), m.group(4)
    nm = re.search(r"^name:[ \t]*(.*)$", govde, re.M)
    if nm and nm.group(1).strip().strip("'\"") == ad:
        return
    govde = (govde[:nm.start()] + f"name: {ad}" + govde[nm.end():]) if nm else f"name: {ad}{nl}" + govde
    metin_yaz(skill_md, bas + govde + son + metin[m.end():])


def frontmatter_adi(skill_md: Path):
    m = re.match(r"^\ufeff?---[ \t]*\r?\n(.*?)\r?\n---", metin_oku(skill_md), re.S)
    nm = re.search(r"^name:[ \t]*(.*)$", m.group(1), re.M) if m else None
    return nm.group(1).strip().strip("'\"") if nm else None


def hazirla(kaynak: Path, hedef: Path, s, ad, kardes=None):
    """Geçici klasöre kopyala, adı ve iç yolları düzelt, sonra yerine taşı (yarım kurulum kalmaz)."""
    gecici = hedef.parent / f".{ad}.kurulum-tmp"
    sil_yol(gecici)
    gecici.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(kaynak, gecici, ignore=shutil.ignore_patterns("KAYNAK.md"))
    isim_esitle(gecici / "SKILL.md", ad)
    yollari_yeniden_adlandir(gecici, {s["ad"], s.get("klasor_adi")}, ad)
    kardes_yollarini_yeniden_adlandir(gecici, {k: v[0] for k, v in (kardes or {}).items()})
    sil_yol(hedef)
    gecici.rename(hedef)


def kur(s, proje: Path, ad: str, kardes=None):
    codex_hedef = proje / ".agents" / "skills" / ad
    claude_hedef = proje / ".claude" / "skills" / ad
    var = s.get("varyantlar") or {}
    hazirla(KOK / var.get("codex", s["yol"]), codex_hedef, s, ad, kardes)
    claude_hedef.parent.mkdir(parents=True, exist_ok=True)
    if var.get("claude"):
        hazirla(KOK / var["claude"], claude_hedef, s, ad, kardes)
    else:
        sil_yol(claude_hedef)
        os.symlink(os.path.relpath(codex_hedef, claude_hedef.parent), claude_hedef)


# ================================================================== agent dosyaları
def toml_str(x):
    return json.dumps(x, ensure_ascii=False)  # JSON dizgesi geçerli bir TOML temel dizgesidir


def onyuklenebilir(s):
    return not any("disable-model-invocation" in x for x in s.get("yapisal_sorunlar", []))


def agent_dosyalari(proje: Path, kilit: dict, skiller):
    rol_kur = {}
    for ad, k in kilit["skiller"].items():
        for r in k["roller"]:
            rol_kur.setdefault(r, []).append(ad)
    tum = sorted(kilit["skiller"])
    if kilit["roller"]:
        (proje / ".claude" / "agents").mkdir(parents=True, exist_ok=True)
        (proje / ".codex" / "agents").mkdir(parents=True, exist_ok=True)
    for rol in kilit["roller"]:
        if not ROL_ADI.match(rol):  # savunma: geçersiz ad asla dosya yoluna dönüşmez
            continue
        tanim = json_oku(ROLLER / f"{rol}.json") or {"aciklama": rol, "gorev": f"{rol} rolü."}
        benim = sorted(rol_kur.get(rol, []))
        onyukle = [a for a in benim if onyuklenebilir(kaynak_bul(skiller, kilit["skiller"][a]) or {})]
        elle = [a for a in benim if a not in onyukle]
        talimat = (f"{tanim['gorev']}\n\nBu rolün skilleri: {', '.join(benim) or '-'}.\n"
                   "İşe başlamadan önce ilgili skill'in SKILL.md dosyasını oku ve kurallarına uy. "
                   "Skill'de olmayan bir konuda varsayım yapma; emin değilsen ana agent'a sor."
                   + (f"\nŞu skiller otomatik yüklenmez, gerektiğinde açıkça çağır: {', '.join(elle)}." if elle else ""))
        (proje / ".claude" / "agents" / f"{rol}.md").write_text(
            "---\n" f"name: {rol}\n" f"description: {json.dumps(tanim['aciklama'], ensure_ascii=False)}\n"
            + ("skills:\n" + "".join(f"  - {a}\n" for a in onyukle) if onyukle else "")
            + "---\n\n" f"<!-- {URETILDI}; elle değiştirme, skill-ekle.py --yenile ile yeniden üret -->\n\n{talimat}\n",
            encoding="utf-8")
        toml = [f"# {URETILDI}; elle değiştirme, skill-ekle.py --yenile ile yeniden üret",
                f"name = {json.dumps(rol)}", f'description = {toml_str(tanim["aciklama"])}',
                f"developer_instructions = {toml_str(talimat)}"]
        for a in tum:
            if a not in benim:  # Codex'te allowlist yok: rol dışı proje skilleri kapatılır
                toml += ["", "[[skills.config]]",
                         f'path = {json.dumps(str((proje / ".agents" / "skills" / a / "SKILL.md").resolve()), ensure_ascii=False)}',
                         "enabled = false"]
        (proje / ".codex" / "agents" / f"{rol}.toml").write_text("\n".join(toml) + "\n", encoding="utf-8")
    for klasor, uz in ((proje / ".claude" / "agents", ".md"), (proje / ".codex" / "agents", ".toml")):
        if klasor.is_dir():
            for f in klasor.glob(f"*{uz}"):
                if f.stem not in kilit["roller"] and URETILDI in f.read_text(encoding="utf-8"):
                    f.unlink()


def blok_yaz(dosya: Path, icerik: str):
    eski = dosya.read_text(encoding="utf-8") if dosya.exists() else ""
    blok = f"{BLOK_BAS}\n{icerik}\n{BLOK_SON}"
    if (BLOK_BAS in eski) != (BLOK_SON in eski) or eski.count(BLOK_BAS) > 1:
        raise RuntimeError(f"{dosya.name}: skill-kutuphanesi işaretleri bozuk (başlangıç/bitiş eşleşmiyor); "
                           "kullanıcı metnini korumak için dokunulmadı. İşaretleri elle düzelt.")
    if BLOK_BAS in eski and BLOK_SON in eski:
        yeni = re.sub(re.escape(BLOK_BAS) + r".*?" + re.escape(BLOK_SON), lambda _: blok, eski, flags=re.S)
    else:
        yeni = (eski.rstrip() + "\n\n" if eski.strip() else "") + blok + "\n"
    dosya.write_text(yeni, encoding="utf-8")


def talimat_bloklari(proje: Path, kilit: dict):
    if not kilit["skiller"]:
        for f in ("AGENTS.md", "CLAUDE.md"):
            d = proje / f
            if d.exists() and BLOK_BAS in d.read_text(encoding="utf-8"):
                t = re.sub(r"\n*" + re.escape(BLOK_BAS) + r".*?" + re.escape(BLOK_SON) + r"\n?", "\n",
                           d.read_text(encoding="utf-8"), flags=re.S).strip()
                d.unlink() if not t else d.write_text(t + "\n", encoding="utf-8")
        return
    s = ["## Proje skilleri (SkillKutuphanesi)", "",
         f"Profil: {kilit.get('profil') or '-'} · Güncelleme: {kilit['guncelleme']}", "",
         "| Skill | Roller | Kaynak |", "|---|---|---|"]
    for ad, k in sorted(kilit["skiller"].items()):
        s.append(f"| `{ad}` | {', '.join(k['roller']) or 'genel'} | {k['repo']} |")
    s += ["", "Roller: " + (", ".join(f"`{r}`" for r in kilit["roller"]) or "-"),
          "Skiller `.agents/skills/` (Codex) ve `.claude/skills/` (Claude) altında. Bu skilleri elle düzenleme; "
          "değişiklik/güncelleme: `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> --guncelle`"]
    for f in ("AGENTS.md", "CLAUDE.md"):
        blok_yaz(proje / f, "\n".join(s))


def tumunu_yaz(proje, kilit, skiller):
    kilit_yaz(proje, kilit)
    agent_dosyalari(proje, kilit, skiller)
    talimat_bloklari(proje, kilit)


# ================================================================== öneri (tüm kütüphane taraması)
def proje_teknolojileri(proje: Path):
    tek = set()
    pj = proje / "package.json"
    if pj.exists():
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
            for k in {**d.get("dependencies", {}), **d.get("devDependencies", {})}:
                if k in TEKNOLOJI_IPUCU:
                    tek.add(TEKNOLOJI_IPUCU[k])
        except (json.JSONDecodeError, OSError):
            pass
    if any((proje / f).exists() for f in ("requirements.txt", "pyproject.toml")):
        tek.add("python")
    return tek


DURAK = {"ile", "ve", "veya", "için", "icin", "bir", "bu", "şu", "olan", "gibi", "çok", "daha", "yapmak", "yapacağız",
         "the", "and", "for", "with", "use", "using", "when", "this", "that", "from", "your", "you"}


def tr_kucuk(x):
    return x.replace("İ", "i").replace("I", "ı").lower()


def kelimeler(metin):
    metin = tr_kucuk(metin)
    ek = " ".join(v for k, v in ES_ANLAM.items() if k in metin)
    sozcuk = re.findall(r"[\w.+#-]+", metin + " " + ek, re.U)
    # Türkçe karakter içeren kelimeler İngilizce açıklamalarda eşleşmez; onlar ES_ANLAM ile çevrildi
    return {w for w in sozcuk if w not in DURAK and (len(w) > 2 or w in ("3d", "ai", "ui", "ux"))
            and re.fullmatch(r"[a-z0-9.+#-]+", w)}


def puanla(s, sorgu, teknolojiler):
    metin = " ".join([s["id"], s["aciklama"], s.get("ozet_tr", ""), s.get("kullanim_alani", ""),
                      s["kategori"].replace("-", " ")]).lower()
    eslesen = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
    tek = set(s.get("teknoloji") or s["teknoloji_oto"])
    tek_esl = tek & teknolojiler
    p = 3 * len(eslesen) + 2 * len(tek_esl)
    if p:
        p += s["degerlendirme"]["puan"] / 50
        if s["durum"] == "alternatif":
            p -= 1
    return p, eslesen, tek_esl


def kutuphane_taramasi(skiller, sorgu_metni, teknolojiler, haric_idler=(), n=12, gizli=False, kategori_basi=None):
    """TÜM skilleri puanlar. kategori_basi verilirse her kategoriden en fazla o kadar (tek kategoriye yığılmasın)."""
    sorgu = kelimeler(sorgu_metni)
    sonuc, gizli_esl = [], 0
    for s in skiller:
        p, e, t = puanla(s, sorgu, teknolojiler)
        if p <= 0 or s["id"] in haric_idler:
            continue
        if s.get("gizli") and not gizli:
            gizli_esl += 1
            continue
        sonuc.append((p, s, e, t))
    sonuc.sort(key=lambda x: -x[0])
    if kategori_basi:
        sayac, secilen = {}, []
        for x in sonuc:
            k = x[1]["kategori"]
            if sayac.get(k, 0) < kategori_basi:
                secilen.append(x)
                sayac[k] = sayac.get(k, 0) + 1
        return secilen[:n], len(sonuc), gizli_esl
    return sonuc[:n], len(sonuc), gizli_esl


# ================================================================== ön kontrol
def proje_yapisi_kontrol(proje, roller, rapor: Rapor):
    """Projede skill/agent klasörleri güvenli mi? (symlink ile başka yere/globale gidiyor mu, rol adları geçerli mi)"""
    korunan = [g.resolve() for g in GLOBAL_KLASORLER.values()] + [KOK.resolve(), (Path.home() / ".openmontage").resolve()]
    hedefler = {}
    for rel in (".agents/skills", ".claude/skills", ".claude/agents", ".codex/agents", ".agents", ".claude", ".codex"):
        p = proje / rel
        if p.is_symlink() or p.exists():
            gercek = p.resolve()
            if any(gercek == k or k in gercek.parents for k in korunan):
                rapor.ekle("HATA", "global-baglanti", f"{rel} -> {gercek}: global/korunan bir klasöre gidiyor; işlem yapılmaz")
            elif proje.resolve() not in [gercek, *gercek.parents]:
                rapor.ekle("HATA", "proje-disi-baglanti", f"{rel} -> {gercek}: proje dışına gidiyor; işlem yapılmaz")
            hedefler[rel] = gercek
    if ".agents/skills" in hedefler and hedefler.get(".agents/skills") == hedefler.get(".claude/skills"):
        rapor.ekle("HATA", "ayni-klasor", ".claude/skills ve .agents/skills aynı klasöre gidiyor (symlink); "
                   "araç sürümleri ve bağlantılar bozulur. İkisini ayrı klasör yap.")
    for rol in roller:
        if not ROL_ADI.match(rol or ""):
            rapor.ekle("HATA", "gecersiz-rol-adi", f"'{rol}': rol adı sadece küçük harf, rakam ve - içerebilir")
            continue
        for dosya in (proje / ".claude" / "agents" / f"{rol}.md", proje / ".codex" / "agents" / f"{rol}.toml"):
            if dosya.exists() and URETILDI not in dosya.read_text(encoding="utf-8", errors="replace"):
                rapor.ekle("HATA", "kendi-agent-dosyan", f"{dosya.relative_to(proje)} senin dosyan (kütüphane üretmedi); "
                           "üzerine yazılmaz. Rolü farklı adla ekle ya da dosyayı yeniden adlandır")


def on_kontrol(proje, kilit, plan, roller, skiller, rapor: Rapor, zorla=False):
    """plan: [(skill kaydı, rol|None)] -> (kur_listesi {id: (s, roller)}, adlar {id: kurulum adı})"""
    proje_yapisi_kontrol(proje, roller, rapor)
    kur_listesi, adlar, hedef_adlar = {}, {}, {}
    for s, rol in plan:
        kur_listesi.setdefault(s["id"], (s, set()))[1].add(rol)
    for sid, (s, _) in kur_listesi.items():
        adlar[sid] = ad = kurulum_adi(s, kilit)
        if ad in hedef_adlar:
            rapor.ekle("HATA", "isim-cakismasi", f"{sid} ve {hedef_adlar[ad]} aynı adla ({ad}) kurulacaktı")
        hedef_adlar[ad] = sid

    for sid, (s, rol_kumesi) in kur_listesi.items():
        ad = adlar[sid]
        onceki = kilit["skiller"].get(ad)
        for yer in (proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad):
            if (yer.exists() or yer.is_symlink()) and not onceki:
                rapor.ekle("HATA", "projede-kendi-skillin",
                           f"{yer.relative_to(proje)} zaten var ve kütüphaneden gelmemiş; üzerine yazılmaz "
                           f"(--zorla ile yedeklenip değiştirilir)")
        if onceki and (onceki.get("repo"), onceki.get("kaynak_yol", s["kaynak_yol"])) != (s["repo"], s["kaynak_yol"]):
            rapor.ekle("HATA", "farkli-kaynak", f"{ad} projede {onceki.get('repo')}:{onceki.get('kaynak_yol', '?')} kaynağından "
                       f"kurulu; {s['repo']}:{s['kaynak_yol']} ile değiştirilmez (önce --kaldir)")
        canli = canli_global(s)
        if onceki and ad == s["ad"] and any(v == "farkli" for v in canli.values()):
            rapor.ekle("UYARI", "global-cakisma-yeni", f"{ad}: globale sonradan aynı adlı FARKLI skill eklenmiş; Claude'da global "
                       "sürüm kazanır. Kütüphane sürümü için: --kaldir ve yeniden ekle (ekli adla kurulur)")
        if onceki and elle_degismis(proje, ad, onceki):
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} projede elle değiştirilmiş; ezilmez (--zorla: yedekle ve ez)")
        if ad != s["ad"]:
            neden = "global klasörde aynı adlı FARKLI skill var (kişisel skill proje skill'ini ezerdi)" \
                if "--kutuphane" in ad else "aynı adlı alternatif sürüm"
            rapor.ekle("BİLGİ", "ekli-ad", f"{s['id']} -> `{ad}` adıyla kurulacak: {neden}"
                       + ("; skill içindeki kendi yol referansları da düzeltilecek" if s.get("yol_bagimliligi") else ""))
        if any(v == "ayni" for v in canli.values()):
            rapor.ekle("BİLGİ", "globalde-ayni", f"{ad}: bilgisayarında birebir aynısı global olarak da var (sorun değil)")
        u = s["uyum"]
        if u["codex"] == "uyarlanabilir":
            rapor.ekle("UYARI", "codex-uyum", f"{ad}: {u['not'][:220]}")
        elif u["codex"] == "konu-claude-ozel":
            rapor.ekle("UYARI", "claude-ozel", f"{ad}: konu Claude Code'a özel; Codex'te sadece kavram referansı")
        if s.get("varyantlar"):
            rapor.ekle("BİLGİ", "arac-surumu", f"{ad}: " + ", ".join(s["varyantlar"]) + " için ayrı uyarlanmış sürüm kurulacak")
        if s["durum"] == "alternatif":
            tercih = next((x for x in skiller if x["ad"] == s["ad"] and x["durum"] == "tercih"), None)
            rapor.ekle("UYARI", "alternatif-surum", f"{s['id']} alternatif sürüm; tercih edilen: {tercih['id'] if tercih else '?'}")
            if tercih and tercih["id"] in kur_listesi:
                rapor.ekle("UYARI", "ayni-skill-iki-surum", f"{s['ad']} için hem tercih hem alternatif kuruluyor; agent karışabilir")
        if s["lisans"] in ("belirtilmemiş", "NOASSERTION"):
            rapor.ekle("UYARI", "lisans", f"{ad}: lisans belirtilmemiş ({s['repo']}); ticari kullanımda dikkat")
        if s["degerlendirme"]["not"] == "D":
            rapor.ekle("UYARI", "dusuk-puan", f"{ad}: değerlendirme {s['degerlendirme']['puan']}/100 (D)")
        for y in s.get("yapisal_sorunlar", []):
            rapor.ekle("UYARI" if "disable-model" in y or "uzun" in y else "BİLGİ", "yapi", f"{ad}: {y}")
        if s.get("kirik_baglantilar"):
            rapor.ekle("UYARI", "kirik-baglanti", f"{ad}: SKILL.md'nin gösterdiği {len(s['kirik_baglantilar'])} dosya "
                       f"kaynakta da yok ya da arşive alınmadı: {', '.join(s['kirik_baglantilar'][:5])}")
        for kad, (kurulum, kurulu) in kardes_haritasi(s, skiller, kilit, kur_listesi, adlar).items():
            bilgi = s["kardes_bagimliliklari"][kad]
            if not kurulu:
                rapor.ekle("UYARI", "kardes-eksik", f"{ad}: {bilgi['dosya_sayisi']} dosyası ../{kad}/ bağlantısıyla kardeş "
                           f"skill'e dayanıyor ama '{kad}' projeye kurulmuyor; bağlantılar boşa düşer (ekle: --skill {bilgi['id']})")
            elif kurulum != kad:
                rapor.ekle("BİLGİ", "kardes-yol", f"{ad}: ../{kad}/ bağlantıları projedeki ada çevrilecek: ../{kurulum}/")
        if s.get("kaynak_durumu") == "kaynakta-kaldirildi":
            rapor.ekle("UYARI", "kaynakta-kaldirildi", f"{ad}: geliştiricisi bu skill'i {s.get('kaldirilma_tarihi', '?')} "
                       f"tarihli güncellemede kaldırdı ({s['repo']}); arşivdeki son sürüm kuruluyor, artık güncellenmeyecek")
        elif s.get("kaynak_durumu") == "kayip":
            rapor.ekle("UYARI", "kaynak-kayip", f"{ad}: kaynak repo erişilemiyor ({s['repo']}); arşivdeki son sürüm kuruluyor")
        if s.get("bagimlilik"):
            rapor.ekle("UYARI", "bagimlilik", f"{ad}: {s['bagimlilik']}")
        if s.get("notlar"):
            rapor.ekle("BİLGİ", "inceleme-notu", f"{ad}: {s['notlar']}")
        if s.get("gizli"):
            rapor.ekle("BİLGİ", "gizli-katalog", f"{ad}: varsayılan listede gizli kategoriden ({s['kategori']})")
        if s.get("ust_skill"):
            rapor.ekle("BİLGİ", "alt-skill", f"{ad}: '{s['ust_skill']}' skill'inin alt klasörü; tek başına da çalışır")
        if s.get("inceleme") == "yeniden-incelenecek":
            rapor.ekle("UYARI", "inceleme-eskidi", f"{ad}: içeriği son güncellemede değişti, inceleme notları eski sürüme ait "
                       "(rehber/07-kategori-inceleme.md ile yeniden incele)")
        if s.get("inceleme", "otomatik") == "otomatik":
            rapor.ekle("BİLGİ", "incelenmedi", f"{ad}: henüz elle incelenmedi (otomatik bilgilerle)")

    # rol bazında bağlam ve örtüşme
    for rol in roller:
        rs = [s for s, rk in kur_listesi.values() if rol in rk]
        eski = [kaynak_bul(skiller, k) for a, k in kilit["skiller"].items() if rol in k["roller"]]
        rs += [x for x in eski if x and x["id"] not in {y["id"] for y in rs}]
        kb = sum(x["skill_md_kb"] for x in rs)
        if len(rs) > SINIR_CLAUDE_ONYUKLEME:
            rapor.ekle("HATA", "onyukleme-siniri", f"rol {rol}: {len(rs)} skill > Claude alt-agent sınırı {SINIR_CLAUDE_ONYUKLEME}")
        elif len(rs) > SINIR_ROL_SKILL or kb > SINIR_ROL_KB:
            rapor.ekle("UYARI", "baglam-yuku", f"rol {rol}: {len(rs)} skill, {kb:.0f} KB SKILL.md önyüklenecek "
                       f"(öneri ≤{SINIR_ROL_SKILL} skill, ≤{SINIR_ROL_KB} KB); agent bağlamı dolabilir")
        gruplar = {}
        for x in rs:
            if x.get("ortusme_grubu"):
                gruplar.setdefault((x["ortusme_grubu"], x.get("ortusme_rolu")), []).append(x["id"])
        for (g, r), ids in gruplar.items():
            if r == "birincil" and len(ids) > 1:
                rapor.ekle("UYARI", "ortusme", f"rol {rol}: '{g}' grubundan {len(ids)} birincil skill: {', '.join(ids)}")
        surumler = {}
        for x in rs:
            surumler.setdefault(x["ad"], []).append(x["id"])
        for a, ids in surumler.items():
            if len(ids) > 1:
                rapor.ekle("UYARI", "ortusme", f"rol {rol}: aynı skill'in birden fazla sürümü: {', '.join(ids)}")
    return kur_listesi, adlar


def kapsam_raporu(proje, roller, kur_listesi, skiller, rapor: Rapor, ek_sorgu=""):
    """Kütüphanedeki tüm skilleri tarar; kurulmayan ama ilgili adayları raporlar (hiçbiri görmezden gelinmez)."""
    teknolojiler = proje_teknolojileri(proje)
    secilen = set(kur_listesi)
    gorunur = sum(1 for s in skiller if not s.get("gizli"))
    rapor.ekle("BİLGİ", "tarama", f"Kütüphanedeki {len(skiller)} skill tarandı (görünür {gorunur}, gizli "
               f"{len(skiller) - gorunur}); projede tespit edilen teknoloji: {', '.join(sorted(teknolojiler)) or '-'}")
    for rol in roller or [None]:
        tanim = json_oku(ROLLER / f"{rol}.json") if rol else None
        metin = ((tanim or {}).get("aciklama", "") + " " + (tanim or {}).get("gorev", "") + " " + ek_sorgu).strip()
        if not metin and not teknolojiler:
            continue
        adaylar, n, gizli_n = kutuphane_taramasi(skiller, metin, teknolojiler, haric_idler=secilen, n=6, kategori_basi=2)
        if adaylar:
            rapor.ekle("BİLGİ", f"ek-aday{':' + rol if rol else ''}",
                       f"{n} ilgili skill daha var; ilk {len(adaylar)}: " +
                       ", ".join(f"{s['id']} ({s['kategori'].split('/')[1]}, {s['degerlendirme']['puan']})" for _, s, _, _ in adaylar)
                       + (f" · gizli katalogda {gizli_n} eşleşme" if gizli_n else ""))


# ================================================================== komutlar
def istek_coz(a, skiller):
    roller, istek, profil = list(a.rol or []), [], None
    if a.profil:
        profil = json_oku(PROFILLER / f"{a.profil}.json")
        if not profil:
            sys.exit(f"Profil yok: {a.profil}. Mevcut: {', '.join(sorted(p.stem for p in PROFILLER.glob('*.json')))}")
        roller += profil["roller"]
        istek += [(x, a.rol_adi) for x in profil.get("ek_skiller", [])]
    if a.planlayici:
        roller.append("planlayici")
    roller = list(dict.fromkeys(roller))
    for r in roller:
        t = json_oku(ROLLER / f"{r}.json")
        if not t:
            sys.exit(f"Rol yok: {r}. Mevcut: {', '.join(sorted(p.stem for p in ROLLER.glob('*.json')))}")
        istek += [(x, r) for x in t["cekirdek"]] + ([(x, r) for x in t.get("opsiyonel", [])] if a.opsiyonel else [])
    if a.rol_adi and a.rol_adi not in roller:
        roller.append(a.rol_adi)
    istek += [(x, a.rol_adi) for x in (a.skill or [])]
    plan, bulunamayan = [], []
    for anahtar, rol in istek:
        s = bul(skiller, anahtar)
        (plan.append((s, rol)) if s else bulunamayan.append(anahtar))
    return plan, roller, (a.profil if profil else None), bulunamayan


def onay(a, rapor):
    kesin = sorted({k for s, k, _ in rapor.satirlar if s == "HATA" and k in ZORLANAMAZ})
    if kesin:
        print(f"\nDURDU: şu hatalar --zorla ile de geçilemez: {', '.join(kesin)}")
        return False
    if rapor.say("HATA") and not a.zorla:
        print(f"\nDURDU: {rapor.say('HATA')} hata var. Düzelt ya da (yedek alınarak) --zorla ile geç.")
        return False
    if a.kuru:
        print("\n[kuru] Hiçbir şey değiştirilmedi.")
        return False
    if rapor.say("UYARI") and not a.evet:
        if sys.stdin.isatty():
            return input(f"\n{rapor.say('UYARI')} uyarı var. Devam edilsin mi? [e/H] ").strip().lower() in ("e", "evet", "y")
        print(f"\nDURDU: {rapor.say('UYARI')} uyarı var. Raporu kullanıcıya göster; onaylarsa --evet ile tekrar çalıştır.")
        return False
    return True


def kardes_adlari(harita):
    return {k: v[0] for k, v in harita.items()}


def kayit_guncelle(kilit, proje, ad, s, roller=(), kardes=None):
    k = kilit["skiller"].setdefault(ad, {"roller": []})
    k.update(id=s["id"], repo=s["repo"], kaynak_yol=s["kaynak_yol"], commit=s["commit"], klasor_hash=s["klasor_hash"],
             varyantlar=sorted(s.get("varyantlar") or {}), kurulu_hash=kurulu_hash(proje, ad))
    if kardes is not None:
        k["kardes"] = kardes_adlari(kardes)
    for r in roller:
        if r and r not in k["roller"]:
            k["roller"].append(r)


def claude_baglanti_saglam(proje, ad):
    c = proje / ".claude" / "skills" / ad
    return (c / "SKILL.md").exists()


def guvenli_islem(proje, yedek, islem):
    """islem() hata verirse yedekten geri alır."""
    try:
        islem()
    except Exception as e:  # noqa: BLE001
        geri_yukle(proje, yedek)
        sys.exit(f"HATA: {e}\nYapılan değişiklikler geri alındı ({yedek.name}).")


def ekle(a, proje, skiller):
    kilit = kilit_oku(proje)
    plan, roller, profil, bulunamayan = istek_coz(a, skiller)
    rapor = Rapor()
    for b in bulunamayan:
        rapor.ekle("HATA", "bulunamadi", f"kütüphanede yok: {b} (ara: skill-ekle.py --ara {b})")
    kur_listesi, adlar = on_kontrol(proje, kilit, plan, roller, skiller, rapor)
    kapsam_raporu(proje, roller, kur_listesi, skiller, rapor, a.oner or "")
    print(f"Proje: {proje}\nKurulacak: {len(kur_listesi)} skill · Roller: {', '.join(roller) or '-'}")
    for sid, (s, rk) in kur_listesi.items():
        print(f"  {sid:42s} -> {adlar[sid]:42s} [{', '.join(sorted(r for r in rk if r)) or 'genel'}]")
    print("\nÖN KONTROL:")
    rapor.yazdir()
    if not onay(a, rapor):
        return 2
    yedek = yedekle(proje, list(adlar.values()), "ekle")

    def islem():
        for sid, (s, rk) in kur_listesi.items():
            ad = adlar[sid]
            k = kilit["skiller"].get(ad)
            kardes = kardes_haritasi(s, skiller, kilit, kur_listesi, adlar)
            if (not k or k["klasor_hash"] != s["klasor_hash"] or a.zorla or k.get("kardes", {}) != kardes_adlari(kardes)
                    or kurulu_hash(proje, ad)["codex"] is None or not claude_baglanti_saglam(proje, ad)):
                kur(s, proje, ad, kardes)
                print(f"  + {ad}")
            kayit_guncelle(kilit, proje, ad, s, rk, kardes)
        kilit["roller"] = list(dict.fromkeys(kilit["roller"] + roller))
        kilit["profil"] = profil or kilit.get("profil")
        tumunu_yaz(proje, kilit, skiller)
        (meta(proje) / "son-rapor.md").write_text(rapor.markdown("Skill ekleme ön kontrol raporu"), encoding="utf-8")
    guvenli_islem(proje, yedek, islem)
    sonuc = dogrula(proje, skiller, sessiz=True)
    print(f"\nTamam: {len(kilit['skiller'])} skill, {len(kilit['roller'])} rol · doğrulama: "
          f"{'✅' if not sonuc else '❌ ' + '; '.join(sonuc)} · yedek: {yedek.name}")
    return 0 if not sonuc else 1


def kaldir(a, proje, skiller):
    kilit = kilit_oku(proje)
    hedefler = list(kilit["skiller"]) if a.kaldir == ["hepsi"] else a.kaldir
    rapor = Rapor()
    proje_yapisi_kontrol(proje, [], rapor)
    for ad in hedefler:
        if ad not in kilit["skiller"]:
            rapor.ekle("HATA", "kutuphaneden-degil", f"{ad} bu projeye kütüphaneden eklenmemiş; dokunulmaz")
        elif elle_degismis(proje, ad, kilit["skiller"][ad]):
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş (--zorla: yedekle ve sil)")
        else:
            rapor.ekle("BİLGİ", "silinecek", ad)
    rapor.yazdir()
    if not onay(a, rapor):
        return 2
    yedek = yedekle(proje, hedefler, "kaldir")

    def islem():
        for ad in hedefler:
            if ad in kilit["skiller"]:
                sil_yol(proje / ".claude" / "skills" / ad)
                sil_yol(proje / ".agents" / "skills" / ad)
                del kilit["skiller"][ad]
        if a.kaldir == ["hepsi"]:
            kilit["roller"] = []
        tumunu_yaz(proje, kilit, skiller)
    guvenli_islem(proje, yedek, islem)
    print(f"Kaldırıldı. Geri almak için: --geri-al {yedek.name}")
    return 0


def guncelle(a, proje, skiller):
    kilit = kilit_oku(proje)
    rapor, degisen = Rapor(), []
    proje_yapisi_kontrol(proje, kilit["roller"], rapor)
    for ad, k in kilit["skiller"].items():
        s = kaynak_bul(skiller, k)
        if not s:
            rapor.ekle("UYARI", "kaynak-yok", f"{ad}: kaynağı ({k.get('repo')}:{k.get('kaynak_yol', k['id'])}) kütüphanede artık "
                       "yok; projede olduğu gibi bırakıldı. Başka bir repo'nun aynı adlı skill'i otomatik konmaz")
            continue
        canli = canli_global(s)
        if ad == s["ad"] and any(v == "farkli" for v in canli.values()):
            rapor.ekle("UYARI", "global-cakisma-yeni", f"{ad}: globale aynı adlı FARKLI skill eklenmiş; Claude'da global sürüm "
                       "kazanır. Kütüphane sürümü için --kaldir ve yeniden ekle")
        kardes_degisti = k.get("kardes", {}) != kardes_adlari(kardes_haritasi(s, skiller, kilit))
        if s["klasor_hash"] == k["klasor_hash"]:
            if not claude_baglanti_saglam(proje, ad) or kurulu_hash(proje, ad)["codex"] is None:
                degisen.append((ad, s))
                rapor.ekle("BİLGİ", "onarilacak", f"{ad}: eksik/bozuk kurulum onarılacak")
                continue
            if not kardes_degisti:
                continue
            if elle_degismis(proje, ad, k) and not a.zorla:
                rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; kardeş yolları düzeltilmez (--zorla)")
                continue
            degisen.append((ad, s))
            rapor.ekle("BİLGİ", "kardes-yol", f"{ad}: ../<kardeş>/ bağlantıları projedeki adlara göre yeniden yazılacak")
            continue
        if elle_degismis(proje, ad, k) and not a.zorla:
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; güncellenmez (--zorla: yedekle ve ez)")
            continue
        degisen.append((ad, s))
        rapor.ekle("BİLGİ", "guncellenecek", f"{ad}: {k['commit'][:7]} -> {s['commit'][:7]}")
        for u in s.get("yapisal_sorunlar", []):
            rapor.ekle("BİLGİ", "yapi", f"{ad}: {u}")
    print(f"Güncellenecek/onarılacak: {len(degisen)}")
    rapor.yazdir()
    if not degisen:
        return 1 if rapor.say("HATA") else 0
    if not onay(a, rapor):
        return 2
    yedek = yedekle(proje, [d for d, _ in degisen], "guncelle")

    def islem():
        for ad, s in degisen:
            kardes = kardes_haritasi(s, skiller, kilit)
            kur(s, proje, ad, kardes)
            kayit_guncelle(kilit, proje, ad, s, kardes=kardes)
        tumunu_yaz(proje, kilit, skiller)
    guvenli_islem(proje, yedek, islem)
    print(f"Güncellendi. Geri almak için: --geri-al {yedek.name}")
    return 0


def dogrula(proje, skiller, sessiz=False):
    kilit = kilit_oku(proje)
    sorun = []
    for ad, k in kilit["skiller"].items():
        c, cl = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
        if not (c / "SKILL.md").exists():
            sorun.append(f"{ad}: .agents/skills kopyası yok")
        if not (cl / "SKILL.md").exists():
            sorun.append(f"{ad}: .claude/skills bağlantısı/kopyası çalışmıyor")
        elif cl.is_symlink() and cl.resolve() != c.resolve():
            sorun.append(f"{ad}: .claude/skills bağlantısı yanlış yere gidiyor ({cl.resolve()})")
        if "claude" not in k.get("varyantlar", []) and cl.exists() and not cl.is_symlink():
            sorun.append(f"{ad}: .claude/skills'te beklenmeyen gerçek klasör (symlink olmalıydı)")
        for yer in (c, cl):
            if (yer / "SKILL.md").exists() and frontmatter_adi(yer / "SKILL.md") != ad:
                sorun.append(f"{yer.relative_to(proje)}: SKILL.md name klasör adıyla aynı değil")
        if elle_degismis(proje, ad, k):
            sorun.append(f"{ad}: kurulumdan sonra elle değiştirilmiş")
        if not kaynak_bul(skiller, k):
            sorun.append(f"{ad}: kaynağı kütüphanede artık yok ({k.get('repo')}:{k.get('kaynak_yol', k['id'])})")
    tum = set(kilit["skiller"])
    for rol in kilit["roller"]:
        md, toml = proje / ".claude" / "agents" / f"{rol}.md", proje / ".codex" / "agents" / f"{rol}.toml"
        if not md.exists() or not toml.exists():
            sorun.append(f"rol {rol}: agent dosyası eksik (--yenile)")
            continue
        for a in re.findall(r"^  - (.+)$", md.read_text(encoding="utf-8"), re.M):
            if a not in tum:
                sorun.append(f"rol {rol}: Claude agent'ı olmayan skill'e bakıyor: {a}")
        rol_skilleri = {a for a, k in kilit["skiller"].items() if rol in k["roller"]}
        kapali = set()
        for p in re.findall(r'^path = "(.+)"$', toml.read_text(encoding="utf-8"), re.M):
            if not Path(p).exists():
                sorun.append(f"rol {rol}: Codex agent'ında geçersiz yol (proje taşınmış olabilir, --yenile): {p}")
            kapali.add(Path(p).parent.name)
        acik_kalan = tum - rol_skilleri - kapali
        if acik_kalan:
            sorun.append(f"rol {rol}: Codex'te kapatılmamış rol dışı skiller: {', '.join(sorted(acik_kalan))} (--yenile)")
    if kilit["skiller"]:
        for f in ("AGENTS.md", "CLAUDE.md"):
            d = proje / f
            if not d.exists() or BLOK_BAS not in d.read_text(encoding="utf-8") or BLOK_SON not in d.read_text(encoding="utf-8"):
                sorun.append(f"{f}: skill-kutuphanesi bloğu eksik/bozuk (--yenile)")
    if kilit.get("proje_yolu") and kilit["proje_yolu"] != str(proje):
        sorun.append(f"proje taşınmış ({kilit['proje_yolu']} -> {proje}); --yenile çalıştır")
    for d in (proje / ".agents" / "skills", proje / ".claude" / "skills"):
        if d.is_dir():
            for x in d.iterdir():
                if x.name.endswith(".kurulum-tmp"):
                    sorun.append(f"yarım kalmış kurulum klasörü: {x.relative_to(proje)}")
    if not sessiz:
        print("Doğrulama: " + ("✅ sorun yok" if not sorun else f"❌ {len(sorun)} sorun"))
        for x in sorun:
            print("  -", x)
    return sorun


def durum(proje, skiller):
    kilit = kilit_oku(proje)
    print(f"Proje: {proje}\nProfil: {kilit.get('profil')}  Roller: {', '.join(kilit['roller']) or '-'}")
    for ad, k in sorted(kilit["skiller"].items()):
        s = kaynak_bul(skiller, k)
        if not s:
            isaret = "KAYNAK KÜTÜPHANEDE YOK"
        elif elle_degismis(proje, ad, k):
            isaret = "ELLE DEĞİŞTİRİLMİŞ"
        elif s["klasor_hash"] != k["klasor_hash"]:
            isaret = f"GÜNCELLEME VAR ({k['commit'][:7]} -> {s['commit'][:7]})"
        elif not claude_baglanti_saglam(proje, ad):
            isaret = "CLAUDE BAĞLANTISI BOZUK (--guncelle onarır)"
        else:
            isaret = "güncel"
        print(f"  {ad:42s} {', '.join(k['roller']) or 'genel':34s} {isaret}")


def yedekler_listesi(proje):
    ydir = meta(proje) / "yedek"
    return sorted(ydir.iterdir()) if ydir.is_dir() else []


def geri_al(a, proje):
    yedekler = yedekler_listesi(proje)
    if not yedekler:
        sys.exit("Yedek yok.")
    if a.geri_al is True:
        hedef = next((y for y in reversed(yedekler) if json_oku(y / "yedek.json", {}).get("neden") != "geri-al-oncesi"), None)
    else:
        hedef = next((y for y in yedekler if y.name == a.geri_al), None)
    if not hedef:
        sys.exit("Uygun yedek bulunamadı. Liste: --yedekler")
    kilit = kilit_oku(proje)
    bilgi = json_oku(hedef / "yedek.json")
    adlar = set(kilit["skiller"]) | {r.split("/")[-1] for r in bilgi["hedefler"] if "/skills/" in r}
    once = yedekle(proje, sorted(adlar), "geri-al-oncesi")  # geri almanın kendisi de geri alınabilir
    geri_yukle(proje, hedef)
    shutil.rmtree(hedef)
    print(f"Geri alındı: {bilgi['neden']} ({bilgi['zaman']}). Bunu da geri almak için: --geri-al {once.name}")
    return 0


def oner(a, proje, skiller):
    tek = proje_teknolojileri(proje) if proje else set()
    if a.teknoloji:
        tek.add(a.teknoloji.lower())
    adaylar, n, gizli_n = kutuphane_taramasi(skiller, a.oner, tek, n=a.adet, gizli=a.gizli, kategori_basi=a.kategori_basi)
    print(f"Taranan: {len(skiller)} skill · eşleşen: {n} · teknoloji: {', '.join(sorted(tek)) or '-'}"
          + (f" · gizli katalogda {gizli_n} eşleşme daha (--gizli)" if gizli_n else ""))
    kategori = {}
    for p, s, e, t in adaylar:
        kategori.setdefault(s["kategori"], []).append((p, s, e, t))
    for k, l in kategori.items():
        print(f"\n## {k}")
        for p, s, e, t in l:
            print(f"  {s['id']:40s} puan {s['degerlendirme']['puan']:3d} ({s['degerlendirme']['not']}) · "
                  f"Codex {s['uyum']['codex']:16s} · eşleşen: {', '.join(e + sorted(t))}")
    roller = {}
    for f in ROLLER.glob("*.json"):
        r = json_oku(f)
        ortak = {s["id"] for _, s, _, _ in adaylar} & set(r["cekirdek"] + r.get("opsiyonel", []))
        if ortak:
            roller[f.stem] = len(ortak)
    if roller:
        print("\nBu ihtiyaca en uygun roller: " + ", ".join(f"{r} ({n})" for r, n in sorted(roller.items(), key=lambda x: -x[1])))


def listele(a, skiller):
    n = 0
    for s in skiller:
        if s.get("gizli") and not a.gizli:
            continue
        if a.kategori and a.kategori not in s["kategori"]:
            continue
        if a.teknoloji and a.teknoloji.lower() not in [t.lower() for t in (s.get("teknoloji") or s["teknoloji_oto"])]:
            continue
        if a.ara and a.ara.lower() not in (s["id"] + " " + s["aciklama"] + " " + s.get("ozet_tr", "")).lower():
            continue
        n += 1
        ozet = (s.get("ozet_tr") or s["aciklama"])[:80]
        print(f"{s['kategori']:46s} {s['id']:38s} {s['degerlendirme']['puan']:3d} {s['uyum']['codex']:16s} {ozet}")
    print(f"\n{n} skill")


def main():
    ap = argparse.ArgumentParser(description="SkillKutuphanesi: projeye skill ekle (güvenli)")
    ap.add_argument("proje", nargs="?")
    ap.add_argument("--profil")
    ap.add_argument("--rol", nargs="+")
    ap.add_argument("--skill", nargs="+")
    ap.add_argument("--rol-adi", help="--skill ile eklenenleri bu role bağla (yeni rol adı da olabilir)")
    ap.add_argument("--planlayici", action="store_true")
    ap.add_argument("--opsiyonel", action="store_true", help="rollerin opsiyonel skillerini de ekle")
    ap.add_argument("--kaldir", nargs="+")
    ap.add_argument("--guncelle", action="store_true")
    ap.add_argument("--durum", action="store_true")
    ap.add_argument("--dogrula", action="store_true")
    ap.add_argument("--yenile", action="store_true", help="agent dosyalarını ve blokları yeniden üret (proje taşındıysa)")
    ap.add_argument("--geri-al", nargs="?", const=True, default=None, help="son yedeğe (ya da adı verilen yedeğe) dön")
    ap.add_argument("--yedekler", action="store_true", help="yedekleri listele")
    ap.add_argument("--oner", help="ihtiyacı yaz; tüm kütüphane taranır")
    ap.add_argument("--adet", type=int, default=24)
    ap.add_argument("--kategori-basi", type=int, default=5, help="--oner: her kategoriden en fazla (0 = sınırsız)")
    ap.add_argument("--listele", action="store_true")
    ap.add_argument("--ara")
    ap.add_argument("--kategori")
    ap.add_argument("--teknoloji")
    ap.add_argument("--gizli", action="store_true", help="gizli katalogları (entegrasyon, repo-içi) da göster")
    ap.add_argument("--kuru", action="store_true", help="sadece ön kontrol raporu; hiçbir şey değişmez")
    ap.add_argument("--evet", action="store_true", help="uyarıları onayla (agent/etkileşimsiz kullanım)")
    ap.add_argument("--zorla", action="store_true", help="hataları geç (önce yedek alınır)")
    a = ap.parse_args()
    skiller = registry()

    if a.listele or (a.ara and not a.proje):
        return listele(a, skiller)
    if a.oner and not (a.profil or a.rol or a.skill):
        return oner(a, Path(a.proje).expanduser().resolve() if a.proje else None, skiller)
    if not a.proje:
        ap.error("proje klasörü gerekli")
    proje = Path(a.proje).expanduser().resolve()
    korunan = [g.resolve() for g in GLOBAL_KLASORLER.values()] + [KOK.resolve(), (Path.home() / ".openmontage").resolve(),
                                                                   (Path.home() / ".claude").resolve(), (Path.home() / ".codex").resolve()]
    if proje == Path.home().resolve() or any(proje == k or k in proje.parents for k in korunan):
        sys.exit(f"Güvenlik: {proje} bir proje klasörü değil (global skill klasörü, kütüphane ya da ev dizini).")
    if not proje.is_dir():
        sys.exit(f"Klasör yok: {proje}")
    if a.durum:
        return durum(proje, skiller)
    if a.dogrula:
        return 1 if dogrula(proje, skiller) else 0
    if a.yedekler:
        for y in yedekler_listesi(proje):
            b = json_oku(y / "yedek.json", {})
            print(f"  {y.name}  {b.get('neden', '?')}")
        return 0
    if a.geri_al:
        return geri_al(a, proje)
    if a.yenile:
        kilit = kilit_oku(proje)
        rapor = Rapor()
        proje_yapisi_kontrol(proje, kilit["roller"], rapor)
        if rapor.say("HATA"):
            rapor.yazdir()
            return 2
        yedek = yedekle(proje, list(kilit["skiller"]), "yenile")
        guvenli_islem(proje, yedek, lambda: tumunu_yaz(proje, kilit, skiller))
        return 1 if dogrula(proje, skiller) else 0
    if a.kaldir:
        return kaldir(a, proje, skiller)
    if a.guncelle:
        return guncelle(a, proje, skiller)
    if not (a.profil or a.rol or a.skill or a.planlayici):
        ap.error("--profil, --rol veya --skill ver")
    return ekle(a, proje, skiller)


if __name__ == "__main__":
    sys.exit(main() or 0)
