#!/usr/bin/env python3
"""Hangi proje hangi skili kullanıyor? Proje bilgisinin TEK yeri: kütüphane kayıtlarına (registry.json inceleme alanları,
kaynaklar.json notları, kategori/referans kartları) proje adı yazılmaz; proje ↔ skill eşlemesi buradan okunur.

  python3 araclar/proje-kullanimi.py                 # projeleri tara -> notlar/proje-kullanimi.md (hiçbir projeyi değiştirmez)
  python3 araclar/proje-kullanimi.py --skill <id>    # bu skili/kaynağı kullanan projeler (ör. silmeden / tercih değiştirmeden önce)
  python3 araclar/proje-kullanimi.py --repo owner/ad
  python3 araclar/proje-kullanimi.py --program AD [--siki]   # bu programın skillerine bağlı projeler ve hedefin şimdi var olup olmadığı (salt okuma)
  python3 araclar/proje-kullanimi.py --kontrol       # rapor güncel mi? (hiçbir şey yazmaz; kabukta çıkış kodu hep 0, sıkı denetim: --kontrol --siki)
  python3 araclar/proje-kullanimi.py --saglik [--siki] [--ozet-json [--yaz]]   # proje sağlığı -> notlar/proje-durumu.md (salt okuma)
  python3 araclar/proje-kullanimi.py --tara-kayitsiz [--siki]                  # kilitsiz ama skill klasörü olan klasörleri listele (yazmaz)
  python3 araclar/proje-kullanimi.py --ekle <yol> [--neden ..] | --cikar <ad> --neden .. | --tasindi <ad> <yeni-yol>
                                     | --yoksay <yol> --neden .. [--altini-da]   [--evet]   # yalnız projeler.json; --evet yoksa sadece plan

skill-ekle.py projede değişiklik yapan her işlemden sonra raporu kendisi yeniler; dogrula.py raporun güncelliğini ve
kayıt dosyalarında proje adı geçmediğini denetler; arsiv-guncelle.py değişen kaynakları kullanan projeleri listeler.

Kaynak: her projenin `.skill-kutuphanesi/kilit.json` dosyası (skill-ekle.py yazar) ve varsa `elle-kurulan.json`.
Projeler `projeler.json` -> `tarama_kokleri` altında bir seviye aranır; başka yerdeki projeler `ek_projeler` listesine yazılır.
Projeye özel elle notlar (ör. "şu tarihten beri bu sürüm kullanılıyor") `projeler.json` -> `notlar` -> <proje> -> <skill id>.
"""
import argparse
import contextlib
import copy
import fnmatch
import io
import json
import os
import re
import stat
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GLOBAL_KLASORLER, KOK, REGISTRY, json_oku, json_yaz, klasor_hash, repo_guncel  # noqa: E402

AYAR = KOK / "projeler.json"
RAPOR = KOK / "notlar" / "proje-kullanimi.md"
DURUM_RAPORU = KOK / "notlar" / "proje-durumu.md"
PROGRAMLAR = KOK / "programlar.json"
SKILL_KLASORLERI = (".claude/skills", ".agents/skills", ".cursor/skills", ".codex/skills", ".github/skills", ".gemini/skills")
TALIMAT_ISARETLERI = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", ".cursor/rules",
                      ".agents/rules", ".claude/agents", ".codex/agents", ".agents/agents", ".github/agents")
ATLANAN_KLASORLER = {"node_modules", "__pycache__", "site-packages", "venv", "env", "dist", "build", "target", "vendor",
                     "Pods", "DerivedData", "Library", "Trash"}   # ayrıca "." ile başlayan her ad
ESKI_GUN = 60                                                      # kilitteki son işlem bundan eskiyse BİLGİ satırı
DIKKAT_DOGRULA = ("skillOverrides güncel değil",)                  # dogrula satırlarından 'sorun' değil 'dikkat' olanlar
DOGRULA_TEKRAR = ("elle değiştirilmiş", "kaynağı kütüphanede artık yok", "proje taşınmış (")  # P5 bunları kendisi bildirir
AYAR_ANAHTARLARI = ("tarama_kokleri", "ek_projeler", "kayitsiz_tarama", "yoksay", "bilinen_projeler", "kendi_skilleri", "notlar")
GUVENLIK_SATIRI = "Bu araç hiçbir proje klasörüne ve genel skill klasörüne yazmaz."
TARIH_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DIS_AD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")          # kilitteki dis_skiller anahtarı (skill-ekle.py ile aynı kural)
BAG_KIRIK_IPUCU = " (program kurulu değilse bu beklenir: program kurulunca skill-ekle.py <proje> --yenile onarır)"

_CIKIS = 0                 # kabuk çıkış kodu: yalnız yeni kipler ve --kontrol --siki değiştirir (eski kipler hep 0)
_SE_ONBELLEK = [None]      # skill-ekle.py modülü (tembel yüklenir; testler yerine sahte nesne koyar)


def _norm(p):
    return unicodedata.normalize("NFC", str(Path(p).expanduser().resolve()))


def _norm_ust(p):
    """Son parçayı AÇMADAN normalleştir (yalnız üst klasör çözülür): yoksayılan klasöre hiç dokunmamak için."""
    p = Path(p).expanduser()
    return unicodedata.normalize("NFC", str(Path(os.path.realpath(p.parent)) / p.name))


def _cikanlar(ayar):
    sonuc = set()
    for rec in (ayar.get("bilinen_projeler") or {}).values():
        if isinstance(rec, dict) and rec.get("durum") == "takipten-cikti" and rec.get("yol"):
            sonuc.add(_norm(rec["yol"]))
    return sonuc


def projeleri_bul(ayar):
    """Bulunan projeler; 'takipten-cikti' olanlar hariç (rapor, aylık liste ve doğrulama onları görmez)."""
    ham = projeleri_bul_ham(ayar)
    cik = _cikanlar(ayar)
    return [y for y in ham if _norm(y) not in cik] if cik else ham


def projeleri_bul_ham(ayar):
    yollar = []
    for kok in ayar.get("tarama_kokleri", []):
        kok = Path(kok).expanduser()
        if kok.is_dir():
            yollar += sorted(p.parent.parent for p in kok.glob("*/.skill-kutuphanesi/kilit.json"))
    yollar += [Path(p).expanduser() for p in ayar.get("ek_projeler", [])]
    gorulen, sonuc = set(), []
    for y in yollar:
        y = y.resolve()
        if y in gorulen or y == KOK or not (y / ".skill-kutuphanesi" / "kilit.json").exists():
            continue
        gorulen.add(y)
        sonuc.append(y)
    return sonuc


def oku(ayar):
    projeler = []
    for yol in projeleri_bul(ayar):
        kilit = json_oku(yol / ".skill-kutuphanesi" / "kilit.json", {}) or {}
        elle = json_oku(yol / ".skill-kutuphanesi" / "elle-kurulan.json", None)
        if isinstance(elle, dict):
            elle = elle.get("skiller", elle)
        projeler.append({"ad": yol.name, "yol": yol, "kilit": kilit, "elle": sorted(elle) if elle else []})
    return projeler


def dis_kayitlari(kilit):
    """Kilitteki programla gelen (bağ) ve donmuş skiller: {ad: kayıt}. Geçersiz anahtar/tür atlanır (skill-ekle.py --dogrula bildirir)."""
    d = kilit.get("dis_skiller") if isinstance(kilit, dict) else None
    if not isinstance(d, dict):
        return {}
    return {k: g for k, g in d.items() if isinstance(k, str) and DIS_AD.fullmatch(k) and isinstance(g, dict)
            and g.get("ad") == k and g.get("tur") in ("program-bag", "donmus")}


def dis_sayilari(kilit):
    d = dis_kayitlari(kilit)
    return sum(1 for g in d.values() if g["tur"] == "program-bag"), sum(1 for g in d.values() if g["tur"] == "donmus")


def kisa_yol(yol):
    try:
        return "~/" + str(yol.relative_to(Path.home()))
    except ValueError:
        return str(yol)


def rapor_metni(projeler, ayar, registry):
    """registry: {(repo, kaynak_yol): güncel kimlik}. Kilit yazıldıktan sonra tercih değiştiyse kimlik kaymış olabilir.
    Çıktıda tarih YOKTUR: içerik sadece kullanım değişince değişir (gereksiz git farkı olmaz). -> (metin, {skill: [projeler]})"""
    registry_idler = set(registry.values())
    notlar = ayar.get("notlar", {})
    s = ["# Proje kullanımı — hangi proje hangi skili kullanıyor",
         "",
         "> `araclar/proje-kullanimi.py` üretir (skill-ekle.py her kurulum/güncelleme/kaldırmadan sonra yeniler); elle düzenleme. "
         "Kaynak: projelerin `.skill-kutuphanesi/kilit.json` dosyaları. Elle notlar `projeler.json` → `notlar`.",
         "> Proje bilgisi yalnızca burada tutulur; skill ve kaynak kayıtlarına proje adı yazılmaz.",
         "",
         "| Proje | Yol | Skill | Araç | Blok | Son işlem |",
         "|---|---|---|---|---|---|"]
    for p in projeler:
        k = p["kilit"]
        nb, nd = dis_sayilari(k)
        dis_ek = f" (+{nb} bağ, {nd} donmuş)" if nb + nd else ""
        s.append(f"| [{p['ad']}](#{p['ad'].lower().replace(' ', '-')}) | `{kisa_yol(p['yol'])}` | {len(k.get('skiller', {}))}{dis_ek} | "
                 f"{', '.join(k.get('araclar', [])) or '—'} | {k.get('blok') or 'tam'} | {k.get('guncelleme') or '—'} |")
    kullanan = {}
    for p in projeler:
        k = p["kilit"]
        s += ["", f"## {p['ad']}", ""]
        if k.get("profil") or k.get("roller"):
            s.append(f"Profil: {k.get('profil') or '—'} · Roller: {', '.join(k.get('roller', [])) or '—'}")
            s.append("")
        s += ["| Skill | Kaynak | Commit | Roller | Not |", "|---|---|---|---|---|"]
        pn = notlar.get(p["ad"], {})
        for ad, v in sorted(k.get("skiller", {}).items()):
            sid = v.get("id", ad)
            guncel = registry.get((repo_guncel(v.get("repo")), v.get("kaynak_yol")))
            ek = pn.get(sid, "") or pn.get(guncel or "", "")
            if guncel is None and sid not in registry_idler:
                ek = ("kütüphanede artık yok · " + ek).rstrip(" ·")
            elif guncel and guncel != sid:
                ek = (f"kütüphanede şimdi `{guncel}` · " + ek).rstrip(" ·")
            kullanan.setdefault(guncel or sid, []).append(p["ad"])
            kurulu = f"`{ad}`" if ad == sid else f"`{ad}` (kimlik `{sid}`)"
            s.append(f"| {kurulu} | {repo_guncel(v.get('repo', '?'))} | `{str(v.get('commit', ''))[:7]}` | "
                     f"{', '.join(v.get('roller', [])) or '—'} | {ek} |")
        if p["elle"]:
            s += ["", "Kütüphane dışı, elle kurulan: " + ", ".join(f"`{a}`" for a in p["elle"])]
        dis = dis_kayitlari(k)
        baglar = [(a, g) for a, g in sorted(dis.items()) if g["tur"] == "program-bag"]
        donmus = [a for a, g in sorted(dis.items()) if g["tur"] == "donmus"]
        if baglar:
            s += ["", "Programla gelen (bağ): " + ", ".join(f"`{a}` ({g.get('program', '?')})" for a, g in baglar)]
        if donmus:
            s += ["", "Donmuş (projenin kendi kopyası): " + ", ".join(f"`{a}`" for a in donmus)]
    s += ["", "## Skill → projeler (birden fazla projede kullanılanlar)", "", "| Skill | Projeler |", "|---|---|"]
    for sid, pl in sorted(kullanan.items(), key=lambda x: (-len(x[1]), x[0])):
        if len(pl) > 1:
            s.append(f"| `{sid}` | {', '.join(pl)} |")
    bag_kullanan = {}
    for p in projeler:
        for a, g in dis_kayitlari(p["kilit"]).items():
            if g["tur"] == "program-bag":
                bag_kullanan.setdefault((str(g.get("program", "?")), a), []).append(p["ad"])
    if bag_kullanan:
        s += ["", "## Programla gelen skiller → projeler", "", "| Program | Skill | Projeler |", "|---|---|---|"]
        for (prog, a), pl in sorted(bag_kullanan.items()):
            s.append(f"| {prog} | `{a}` | {', '.join(sorted(pl))} |")
    s.append("")
    return "\n".join(s), kullanan


def hesapla():
    ayar = json_oku(AYAR, {}) or {}
    projeler = oku(ayar)
    reg = json_oku(REGISTRY, {}) or {}
    esleme = {(x.get("repo"), x.get("kaynak_yol")): x["id"] for x in reg.get("skiller", [])}
    metin, kullanan = rapor_metni(projeler, ayar, esleme)
    return ayar, projeler, metin, kullanan


def guncel_mi():
    """(güncel mi, proje sayısı). Bu bilgisayarda hiç proje bulunamazsa (başka makine/bulut) denetim yapılmaz: (True, 0)."""
    _, projeler, metin, _ = hesapla()
    if not projeler:
        return True, 0
    return RAPOR.exists() and RAPOR.read_text(encoding="utf-8") == metin, len(projeler)


def rapor_guncelle():
    """Raporu yeniden üretir; içerik değiştiyse yazar ve True döner. Hiç proje bulunamazsa mevcut rapora dokunmaz."""
    _, projeler, metin, _ = hesapla()
    if not projeler or (RAPOR.exists() and RAPOR.read_text(encoding="utf-8") == metin):
        return False
    RAPOR.write_text(metin, encoding="utf-8")
    return True


def kullanan_projeler(repolar=(), idler=()):
    """{proje adı: [kurulu skill adları]}: verilen kaynaklardan (owner/ad) ya da kimliklerden skill kullanan projeler."""
    repolar = {repo_guncel(r).lower() for r in repolar}
    sonuc = {}
    for p in oku(json_oku(AYAR, {}) or {}):
        for ad, v in sorted(p["kilit"].get("skiller", {}).items()):
            if repo_guncel(v.get("repo", "")).lower() in repolar or v.get("id", ad) in idler:
                sonuc.setdefault(p["ad"], []).append(ad)
    return sonuc

# ================================================================== P5: proje sağlığı, kayıtsız tarama, ayar değişiklikleri
def _skill_ekle():
    """skill-ekle.py modülü (yalnız --saglik ve yazıcılar yükler; yüklenemezse None)."""
    if _SE_ONBELLEK[0] is None:
        try:
            import importlib.util
            s = importlib.util.spec_from_file_location("skillekle", Path(__file__).parent / "skill-ekle.py")
            m = importlib.util.module_from_spec(s)
            s.loader.exec_module(m)
            _SE_ONBELLEK[0] = m
        except Exception:  # noqa: BLE001
            return None
    return _SE_ONBELLEK[0]


def _ayar_oku():
    try:
        a = json_oku(AYAR, {}) or {}
        return a if isinstance(a, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def kilit_guvenli_oku(yol):
    """(kilit | None, hata | None). Bozuk kilit çökertmez."""
    f = Path(yol) / ".skill-kutuphanesi" / "kilit.json"
    try:
        ham = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return None, f"kilit.json okunamıyor: {str(e)[:80]}"
    if not isinstance(ham, dict):
        return None, "kilit.json okunamıyor: sözlük değil"
    se = _skill_ekle()
    if se is not None:
        try:
            return se.kilit_oku(Path(yol)), None
        except Exception as e:  # noqa: BLE001
            return None, f"kilit.json okunamıyor: {str(e)[:80]}"
    ham.setdefault("skiller", {})
    ham.setdefault("roller", [])
    return ham, None


def skill_durumu(proje, ad, k, kilit, skiller, se):
    """skill-ekle.py durum() ile aynı sıra: kaynak yok > emekli > elle değişmiş > güncelleme var > kurulum eksik > güncel."""
    s = se.kaynak_bul(skiller, k)
    if not s:
        return "kaynak-yok"
    if s.get("kaynak_durumu") == "kaynakta-kaldirildi":
        return "emekli-kaynakta-kaldirildi"
    if s.get("kaynak_durumu") == "kayip":
        return "emekli-kayip"
    if se.elle_degismis(proje, ad, k):
        return "elle-degismis"
    if s.get("klasor_hash") != k.get("klasor_hash"):
        return "guncelleme-var"
    if se.kurulum_eksik(proje, ad, kilit):
        return "kurulum-eksik"
    return "guncel"


def disk_skilleri(proje):
    """{skill adı: [göreli klasörler]}: SKILL.md içeren çocuk klasörler. Skill klasörünün kendisi bağlantıysa atlanır."""
    sonuc = {}
    proje = Path(proje)
    for rel in SKILL_KLASORLERI:
        d = proje / rel
        if d.is_symlink() or not d.is_dir():
            continue
        try:
            cocuklar = sorted(d.iterdir())
        except OSError:
            continue
        for c in cocuklar:
            if c.name.endswith(".kurulum-tmp") or not c.is_dir():
                continue
            if (c / "SKILL.md").exists():
                sonuc.setdefault(c.name, []).append(f"{rel}/{c.name}")
    return sonuc


def elle_kayitlari(proje):
    f = Path(proje) / ".skill-kutuphanesi" / "elle-kurulan.json"
    if not f.exists():
        return {}, None
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(d, dict):
            d = d.get("skiller", d)
        return (d if isinstance(d, dict) else {}), None
    except Exception as e:  # noqa: BLE001
        return {}, f"elle-kurulan.json okunamıyor: {str(e)[:80]}"


def kendi_mi(proje_adi, skill_adi, ayar):
    desenler = (ayar.get("kendi_skilleri") or {}).get(proje_adi, [])
    return any(fnmatch.fnmatchcase(skill_adi, d) for d in desenler if isinstance(d, str))


def kutuphane_hash_haritasi(skiller):
    return {x["klasor_hash"]: x.get("id", x.get("ad")) for x in skiller if x.get("klasor_hash")}


def izleme_kapsaminda_mi(yol, ayar=None):
    """(bool, neden): klasör bir tarama kökünün hemen altında mı ya da ek_projeler'de mi?"""
    ayar = _ayar_oku() if ayar is None else ayar
    n = _norm(yol)
    for k in ayar.get("tarama_kokleri", []):
        if _norm(Path(n).parent) == _norm(k):
            return True, "tarama kökü altında"
    if n in {_norm(p) for p in ayar.get("ek_projeler", [])}:
        return True, "ek_projeler'de"
    return False, "kapsam dışı: --ekle gerekir"


# ---------------------------------------------------------------- ayar doğrulama
def _sema(ayar):
    """Yapı hataları (yazıcılar bunlarla yazmayı reddeder)."""
    h = []
    for a in ("tarama_kokleri", "ek_projeler"):
        v = ayar.get(a, [])
        if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
            h.append(f"projeler.json: {a} yol listesi olmalı")
    kt = ayar.get("kayitsiz_tarama", {})
    if not isinstance(kt, dict):
        h.append("projeler.json: kayitsiz_tarama sözlük olmalı")
    else:
        if not isinstance(kt.get("kokler", []), list):
            h.append("projeler.json: kayitsiz_tarama.kokler liste olmalı")
        d = kt.get("derinlik", 4)
        if not isinstance(d, int) or isinstance(d, bool) or not 1 <= d <= 6:
            h.append("projeler.json: kayitsiz_tarama.derinlik 1-6 arası tam sayı olmalı")
        e = kt.get("en_cok_klasor", 30000)
        if not isinstance(e, int) or isinstance(e, bool) or e < 1:
            h.append("projeler.json: kayitsiz_tarama.en_cok_klasor pozitif tam sayı olmalı")
    ys = ayar.get("yoksay", [])
    if not isinstance(ys, list):
        h.append("projeler.json: yoksay liste olmalı")
    else:
        for i, y in enumerate(ys):
            if not isinstance(y, dict) or not isinstance(y.get("yol"), str) or not y.get("yol"):
                h.append(f"projeler.json: yoksay[{i}] yol yok")
                continue
            if not isinstance(y.get("neden"), str) or not y["neden"].strip():
                h.append(f"projeler.json: yoksay[{i}] ({y['yol']}) neden boş")
            if not isinstance(y.get("tarih"), str) or not TARIH_RE.match(y["tarih"]):
                h.append(f"projeler.json: yoksay[{i}] ({y['yol']}) tarih YYYY-AA-GG olmalı")
            if "altini_da" in y and not isinstance(y["altini_da"], bool):
                h.append(f"projeler.json: yoksay[{i}] altini_da true/false olmalı")
    bp = ayar.get("bilinen_projeler", {})
    if not isinstance(bp, dict):
        h.append("projeler.json: bilinen_projeler sözlük olmalı")
    else:
        for ad, r in bp.items():
            if not isinstance(r, dict) or not isinstance(r.get("yol"), str):
                h.append(f"projeler.json: bilinen_projeler.{ad} yol yok")
                continue
            if r.get("tur") not in ("kilitli", "elle"):
                h.append(f"projeler.json: bilinen_projeler.{ad} tur 'kilitli' ya da 'elle' olmalı")
            if r.get("durum") not in ("takipte", "takipten-cikti"):
                h.append(f"projeler.json: bilinen_projeler.{ad} durum 'takipte' ya da 'takipten-cikti' olmalı")
            if not isinstance(r.get("eklendi"), str) or not TARIH_RE.match(r["eklendi"]):
                h.append(f"projeler.json: bilinen_projeler.{ad} eklendi tarihi YYYY-AA-GG olmalı")
    ks = ayar.get("kendi_skilleri", {})
    if not isinstance(ks, dict) or not all(isinstance(v, list) for v in ks.values()):
        h.append("projeler.json: kendi_skilleri {proje: [ad ya da desen]} olmalı")
    return h


def ayar_kontrol(ayar):
    """Uyarı satırları. 'BİLGİ:' ile başlayanlar düzeyi yükseltmez."""
    u = _sema(ayar)
    bp = ayar.get("bilinen_projeler", {}) if isinstance(ayar.get("bilinen_projeler"), dict) else {}
    bulunan = []
    try:
        bulunan = projeleri_bul_ham(ayar)
    except Exception:  # noqa: BLE001
        pass
    bilinen = set(bp) | {y.name for y in bulunan}
    for y in ayar.get("yoksay", []) if isinstance(ayar.get("yoksay"), list) else []:
        if isinstance(y, dict) and isinstance(y.get("yol"), str):
            bilinen.add(Path(y["yol"]).name)
    for alan in ("notlar", "kendi_skilleri"):
        v = ayar.get(alan, {})
        for ad in (v if isinstance(v, dict) else {}):
            if ad not in bilinen:
                u.append(f"projeler.json: {alan} içinde bilinmeyen proje: {ad}")
    yollar = {}
    for r in bp.values():
        if isinstance(r, dict) and isinstance(r.get("yol"), str):
            yollar.setdefault(Path(r["yol"]).name, set()).add(_norm_ust(r["yol"]))
    for p in ayar.get("ek_projeler", []) if isinstance(ayar.get("ek_projeler"), list) else []:
        if isinstance(p, str):
            yollar.setdefault(Path(p).name, set()).add(_norm_ust(p))
    for y in bulunan:
        yollar.setdefault(y.name, set()).add(_norm(y))
    for ad, ys in sorted(yollar.items()):
        if len(ys) > 1:
            u.append(f"projeler.json: AYNI AD İKİ YOL: {ad} ({len(ys)} farklı klasör; desteklenmiyor)")
    for y in ayar.get("yoksay", []) if isinstance(ayar.get("yoksay"), list) else []:
        if isinstance(y, dict) and isinstance(y.get("yol"), str) and not Path(y["yol"]).expanduser().exists():
            u.append(f"BİLGİ: yoksay girdisi artık yok: {y['yol']} (temizlenebilir)")
    return u


def hizli_kontrol(ayar=None):
    """dogrula.py için ucuz uyarılar (kayıt dosyası, karma, tarama yok). Bu bilgisayarda hiç proje yoksa sessiz: []."""
    if ayar is None:
        if not AYAR.exists():
            return []
        ayar = _ayar_oku()
    try:
        if not projeleri_bul_ham(ayar):
            return []
        u = [x for x in ayar_kontrol(ayar) if not x.startswith("BİLGİ")]
        bp = ayar.get("bilinen_projeler", {}) if isinstance(ayar.get("bilinen_projeler"), dict) else {}
        for ad, r in sorted(bp.items()):
            if not isinstance(r, dict) or r.get("durum") != "takipte" or not isinstance(r.get("yol"), str):
                continue
            y = Path(r["yol"]).expanduser()
            if not y.exists():
                u.append(f"KAYIP: {ad} ({r['yol']}) klasörü yok -> --saglik; taşındıysa --tasindi, silindiyse --cikar")
            elif r.get("tur") == "kilitli" and not (y / ".skill-kutuphanesi" / "kilit.json").exists():
                u.append(f"KİLİT YOK: {ad} klasör duruyor ama .skill-kutuphanesi/kilit.json yok -> --saglik")
        bp_yollar = {_norm_ust(r["yol"]) for r in bp.values() if isinstance(r, dict) and isinstance(r.get("yol"), str)}
        for p in ayar.get("ek_projeler", []):
            if isinstance(p, str) and not Path(p).expanduser().exists() and _norm_ust(p) not in bp_yollar:
                u.append(f"ek_projeler yolu yok: {p}")
        return ["proje takibi: " + x for x in u]
    except Exception as e:  # noqa: BLE001
        return [f"proje takibi: hızlı kontrol çalışmadı ({str(e)[:80]})"]


# ---------------------------------------------------------------- sağlık modeli
_SIRA = {"bilgi": 0, "dikkat": 1, "sorun": 2}


def _en_kotu(satirlar):
    d = max((_SIRA[x[0]] for x in satirlar), default=0)
    return {0: "temiz", 1: "dikkat", 2: "sorun"}[d]


def _siniflandir(proje, ad, disk, kilitteki, elle, ayar, hash_haritasi, satirlar, sayac):
    """Kilitte olmayan disk skilleri: elle / kendi / kilitsiz kütüphane kopyası / kayıtsız."""
    for n in sorted(disk):
        if n in kilitteki:
            continue
        if n in elle:
            sayac["kendi_elle"] += 1
            continue
        if kendi_mi(Path(proje).name, n, ayar):
            sayac["kendi_elle"] += 1
            continue
        sayac["kayitsiz"] += 1
        kid = None
        try:
            kid = hash_haritasi().get(klasor_hash(Path(proje) / disk[n][0]))
        except Exception:  # noqa: BLE001
            pass
        if kid:
            satirlar.append(("dikkat", f"KİLİTSİZ KÜTÜPHANE KOPYASI: {n} (kütüphanedeki {kid} ile aynı içerik; elle kopyalanmış olabilir; "
                                       f"elle-kurulan.json'a yazılması için kullanıcıya sor)"))
        else:
            satirlar.append(("dikkat", f"KAYITSIZ SKILL: {n} (kilitte, elle-kurulan.json'da ve kendi_skilleri'nde yok)"))
    for n in sorted(set(elle) - set(disk)):
        satirlar.append(("dikkat", f"elle-kurulan.json'da olup klasörü yok: {n}"))


def proje_denetle(yol, ayar, skiller, hash_haritasi, se, bugun, tur="kilitli"):
    """Tek proje için sağlık kaydı. Asla yazmaz; hata olursa 'denetlenemedi' satırı döner."""
    yol = Path(yol)
    ad = yol.name
    sayac = {"kilit_skill": 0, "diskte": 0, "guncelleme_var": 0, "elle_degismis": 0, "kaynak_yok": 0, "emekli": 0,
             "kurulum_eksik": 0, "kayitsiz": 0, "kendi_elle": 0,
             "program_bag": 0, "donmus": 0, "bag_kirik": 0}
    satirlar, araclar, son = [], "—", "—"
    P = {"ad": ad, "yol": kisa_yol(yol), "tur": tur, "satirlar": satirlar, "sayac": sayac, "araclar": araclar, "son_islem": son}
    try:
        disk = disk_skilleri(yol)
        sayac["diskte"] = len(disk)
        elle, ehata = elle_kayitlari(yol)
        if ehata:
            satirlar.append(("sorun", ehata))
        if tur == "elle":
            _siniflandir(yol, ad, disk, {}, elle, ayar, hash_haritasi, satirlar, sayac)
            P["araclar"] = "—"
            P["durum"] = _en_kotu(satirlar)
            return P
        kilit, hata = kilit_guvenli_oku(yol)
        if hata:
            satirlar.append(("sorun", f"KİLİT OKUNAMIYOR: {hata}"))
            P["durum"] = "sorun"
            return P
        kp = kilit.get("proje_yolu")
        if kp and (not os.path.isabs(kp) or _norm(kp) != _norm(yol)):
            if os.path.isabs(kp) and Path(kp).parent.is_dir():
                satirlar.append(("dikkat", f"TAŞINMIŞ (kilit yolu: {kp}) -> skill-ekle.py \"{yol}\" --yenile"))
            else:
                satirlar.append(("dikkat", f"BAŞKA YERDEN KOPYALANMIŞ olabilir (kilit yolu: {kp}) -> kütüphanenin olduğu Mac'te: "
                                           f"skill-ekle.py \"<proje>\" --yenile; skill-ekle bu kopyada çalıştırılmaz"))
        if kilit.get("kutuphane") and kilit["kutuphane"] != str(KOK):
            satirlar.append(("dikkat", f"kilit başka bir kütüphane yoluna ait ({kilit['kutuphane']}) -> promptlar/09"))
        kskill = kilit.get("skiller", {})
        sayac["kilit_skill"] = len(kskill)
        for sad, k in sorted(kskill.items()):
            d = skill_durumu(yol, sad, k, kilit, skiller, se)
            if d == "guncel":
                continue
            if d == "kaynak-yok":
                sayac["kaynak_yok"] += 1
                satirlar.append(("dikkat", f"KAYNAK KÜTÜPHANEDE YOK: {sad} ({k.get('repo')}:{k.get('kaynak_yol', k.get('id'))}) "
                                           f"-> yerine geçeni KATALOG.md'den bul ya da kaldır"))
            elif d.startswith("emekli"):
                sayac["emekli"] += 1
                satirlar.append(("dikkat", f"EMEKLİ: {sad} ({'kaynakta kaldırıldı' if d.endswith('kaldirildi') else 'kaynak kayıp'}; "
                                           f"artık güncellenmez)"))
            elif d == "elle-degismis":
                sayac["elle_degismis"] += 1
                satirlar.append(("dikkat", f"ELLE DEĞİŞTİRİLMİŞ: {sad}"))
            elif d == "guncelleme-var":
                sayac["guncelleme_var"] += 1
                s = se.kaynak_bul(skiller, k) or {}
                satirlar.append(("dikkat", f"GÜNCELLEME VAR: {sad} ({str(k.get('commit', ''))[:7]} -> {str(s.get('commit', ''))[:7]})"))
            elif d == "kurulum-eksik":
                sayac["kurulum_eksik"] += 1
                satirlar.append(("sorun", f"KURULUM EKSİK/BOZUK: {sad} (--guncelle onarır)"))
        dis = dis_kayitlari(kilit)
        sayac["program_bag"], sayac["donmus"] = dis_sayilari(kilit)
        donmus = sorted(a for a, g in dis.items() if g["tur"] == "donmus")
        if donmus:
            satirlar.append(("bilgi", "donmuş skill (kütüphane güncellemez): " + ", ".join(donmus)))
        try:
            dl = se.dogrula(yol, skiller, sessiz=True)
        except Exception as e:  # noqa: BLE001
            dl = [f"doğrulama çalışmadı: {str(e)[:80]}"]
        for x in dl:
            if any(m in x for m in DOGRULA_TEKRAR):
                continue
            if any(m in x for m in DIKKAT_DOGRULA):
                m = re.search(r"hesap skill'i `(.+?)`", x)
                satirlar.append(("dikkat", f"{m.group(1) if m else '?'}: skillOverrides güncel değil (--guncelle)"))
            else:
                if "program bağı kırık" in x:
                    sayac["bag_kirik"] += 1
                    x += BAG_KIRIK_IPUCU
                satirlar.append(("sorun", x))
        _siniflandir(yol, ad, disk, set(kskill) | set(dis), elle, ayar, hash_haritasi, satirlar, sayac)
        g = kilit.get("guncelleme")
        if g:
            P["son_islem"] = g
            try:
                if (bugun - date.fromisoformat(g)).days > ESKI_GUN:
                    satirlar.append(("bilgi", f"son işlem {g} ({ESKI_GUN} günden eski)"))
            except ValueError:
                pass
        if "araclar" in kilit and isinstance(kilit["araclar"], list):
            P["araclar"] = ", ".join(map(str, kilit["araclar"])) or "—"
        else:
            P["araclar"] = "claude, codex (kilitte yok: varsayılan)"
        if "araclar" not in kilit or kilit.get("arac_secimi") == "varsayilan":
            satirlar.append(("bilgi", "araç seçimi kilitte yok (varsayılan: claude, codex)"))
    except Exception as e:  # noqa: BLE001
        satirlar.append(("sorun", f"denetlenemedi: {str(e)[:100]}"))
    P["durum"] = _en_kotu(satirlar)
    return P


# ---------------------------------------------------------------- kayıtsız tarama
_ETIKET = (("claude", (".claude", "CLAUDE.md")), ("agents/codex", (".agents", ".codex", "AGENTS.md")),
           ("cursor", (".cursor",)), ("copilot", (".github",)), ("gemini", (".gemini", "GEMINI.md")))


def _yoksay_listesi(ayar):
    sonuc = []
    for y in ayar.get("yoksay", []) if isinstance(ayar.get("yoksay"), list) else []:
        if isinstance(y, dict) and isinstance(y.get("yol"), str):
            sonuc.append((_norm_ust(y["yol"]), bool(y.get("altini_da")), y))
    return sonuc


def _yoksayilan(n, liste):
    for yn, alt, rec in liste:
        if n == yn or (alt and n.startswith(yn + os.sep)):
            return rec
    return None


def _genel_mi(hedef, taban):
    try:
        t = os.path.normpath(os.path.join(taban, os.path.expanduser(hedef)))
    except Exception:  # noqa: BLE001
        return False
    for g in GLOBAL_KLASORLER.values():
        gn = os.path.normpath(str(g))
        if t == gn or t.startswith(gn + os.sep):
            return True
    return False


def _aday_bak(d, bulunan_kilitli):
    """Klasör d (açılmasına izin var) bir proje kökü mü? -> aday sözlüğü | None. Yalnız ad/tür denetimi, dosya içeriği okunmaz."""
    def var(rel):
        try:
            return os.lstat(os.path.join(d, rel))
        except OSError:
            return None
    isimler, baglanti, bulunan = set(), [], []
    for rel in SKILL_KLASORLERI:
        st = var(rel)
        if st is None:
            continue
        bulunan.append(rel)
        yol = os.path.join(d, rel)
        if stat.S_ISLNK(st.st_mode):
            try:
                hedef = os.readlink(yol)
            except OSError:
                hedef = "?"
            baglanti.append({"klasor": rel, "hedef": hedef, "genel": _genel_mi(hedef, os.path.dirname(yol))})
        elif stat.S_ISDIR(st.st_mode):
            try:
                for e in os.scandir(yol):
                    if e.is_dir() and os.path.exists(os.path.join(e.path, "SKILL.md")) and not e.name.endswith(".kurulum-tmp"):
                        isimler.add(e.name)
            except OSError:
                pass
    kilitli = var(os.path.join(".skill-kutuphanesi", "kilit.json")) is not None
    skilli = bool(isimler or baglanti)
    talimat = [t for t in TALIMAT_ISARETLERI if var(t) is not None]
    if not skilli and not talimat and not kilitli:
        return None
    isaretler = bulunan + talimat
    etiketler = sorted({et for et, on in _ETIKET for i in isaretler if i.split("/")[0] in on})
    return {"sinif": "skilli" if (skilli or kilitli) else "talimat", "skill_sayisi": len(isimler), "araclar": etiketler,
            "baglanti": baglanti, "kilit": kilitli}


def tara_kayitsiz(ayar, bulunan_projeler=(), skiller=None):
    """Kilitsiz ama skill/talimat klasörü olan klasörleri bulur. Salt okuma; bağlantı izlemez; yoksayılan klasörü HİÇ açmaz."""
    kt = ayar.get("kayitsiz_tarama") if isinstance(ayar.get("kayitsiz_tarama"), dict) else {}
    derinlik = kt.get("derinlik", 4) if isinstance(kt.get("derinlik"), int) else 4
    en_cok = kt.get("en_cok_klasor", 30000) if isinstance(kt.get("en_cok_klasor"), int) else 30000
    kokler = kt.get("kokler") or ayar.get("tarama_kokleri", [])
    sonuc = {"kokler": [], "adaylar": [], "yoksayilan": [], "bilgi": [], "sorun": [], "sinira_ulasildi": False,
             "klasor_sayisi": 0, "atlanan_baglanti": 0, "talimat_sayisi": 0, "derinlik": derinlik}
    liste = _yoksay_listesi(ayar)
    bilinen = {_norm(p) for p in bulunan_projeler} | _cikanlar(ayar) | {_norm(KOK)}
    gorulen_aday, gorulen_yoksay = set(), set()
    sayac = 0
    for kok in kokler:
        kp = Path(kok).expanduser()
        sonuc["kokler"].append(kisa_yol(kp))
        if not kp.is_dir():
            sonuc["bilgi"].append(f"tarama kökü klasör değil, atlandı: {kok}")
            continue
        gercek = os.path.realpath(kp)
        yigin = [(gercek, unicodedata.normalize("NFC", gercek), 0)]
        while yigin:
            if sayac >= en_cok:
                sonuc["sinira_ulasildi"] = True
                break
            gercek_d, norm_d, derin = yigin.pop()
            sayac += 1
            try:
                girdiler = list(os.scandir(gercek_d))
            except OSError as e:
                if derin == 0:
                    sonuc["sorun"].append(f"tarama kökü okunamıyor: {kok} ({str(e)[:60]})")
                continue
            for e in sorted(girdiler, key=lambda x: x.name):
                try:
                    klasor = e.is_dir(follow_symlinks=False)
                    baglanti = (not klasor) and e.is_symlink() and e.is_dir()
                except OSError:
                    continue
                if baglanti:
                    sonuc["atlanan_baglanti"] += 1
                    continue
                if not klasor or e.name.startswith(".") or e.name in ATLANAN_KLASORLER:
                    continue
                cn = unicodedata.normalize("NFC", os.path.join(norm_d, e.name))
                rec = _yoksayilan(cn, liste)
                if rec is not None:           # AÇILMADAN: yalnız ad, üst klasörün listesinden geldi
                    if cn not in gorulen_yoksay:
                        gorulen_yoksay.add(cn)
                        sonuc["yoksayilan"].append({"yol": kisa_yol(Path(os.path.join(gercek_d, e.name))), "neden": rec.get("neden", ""),
                                                    "tarih": rec.get("tarih", "")})
                    continue
                if cn in bilinen or derin + 1 > derinlik:
                    continue
                gd = os.path.join(gercek_d, e.name)
                a = _aday_bak(gd, bilinen)
                if a is not None:
                    if a["kilit"] and cn in bilinen:
                        continue
                    if cn in gorulen_aday:
                        continue
                    gorulen_aday.add(cn)
                    if a["sinif"] == "talimat":
                        sonuc["talimat_sayisi"] += 1
                    else:
                        sonuc["adaylar"].append({"yol": kisa_yol(Path(gd)), "sinif": "skilli", "skill_sayisi": a["skill_sayisi"],
                                                 "araclar": a["araclar"], "baglanti": a["baglanti"], "kilit": a["kilit"]})
                    continue
                yigin.append((gd, cn, derin + 1))
        if sonuc["sinira_ulasildi"]:
            break
    sonuc["klasor_sayisi"] = sayac
    sonuc["adaylar"].sort(key=lambda x: x["yol"])
    sonuc["yoksayilan"].sort(key=lambda x: x["yol"])
    return sonuc


# ---------------------------------------------------------------- sağlık sonucu
def saglik_hesapla(ayar, skiller, programlar=None, bugun=None):
    """Tüm sağlık sonucu. Asla yazmaz, asla çökmez."""
    bugun = bugun or date.today()
    se = _skill_ekle()
    bp = ayar.get("bilinen_projeler") if isinstance(ayar.get("bilinen_projeler"), dict) else {}
    ham = projeleri_bul_ham(ayar)
    cik = _cikanlar(ayar)
    takipte = [y for y in ham if _norm(y) not in cik]
    harita = {}

    def hash_haritasi():
        if "h" not in harita:
            harita["h"] = kutuphane_hash_haritasi(skiller)
        return harita["h"]

    projeler = []
    for y in takipte:
        if se is None:
            projeler.append({"ad": y.name, "yol": kisa_yol(y), "tur": "kilitli", "sayac": {}, "araclar": "—", "son_islem": "—",
                             "satirlar": [("sorun", "denetlenemedi: skill-ekle.py yüklenemedi")], "durum": "sorun"})
        else:
            projeler.append(proje_denetle(y, ayar, skiller, hash_haritasi, se, bugun))
    bulunan_ad = {y.name for y in takipte}
    kayip, cikti = [], []
    for ad, r in sorted(bp.items()):
        if not isinstance(r, dict) or not isinstance(r.get("yol"), str):
            continue
        y = Path(r["yol"]).expanduser()
        if r.get("durum") == "takipten-cikti":
            cikti.append(f"{ad}: takipten çıktı {r.get('cikis_tarihi', '?')} — {r.get('cikis_nedeni', '?')}")
            if (y / ".skill-kutuphanesi" / "kilit.json").exists():
                cikti.append(f"{ad}: bilgi: kilit duruyor (silinmedi)")
            continue
        if ad in bulunan_ad and _norm(y) in {_norm(p) for p in takipte}:
            continue
        if r.get("tur") == "elle":
            if y.is_dir() and se is not None:
                projeler.append(proje_denetle(y, ayar, skiller, hash_haritasi, se, bugun, tur="elle"))
            else:
                kayip.append(("sorun", f"KAYIP: {ad} klasörü yok ({r['yol']}) -> taşındıysa --tasindi \"{ad}\" \"<yeni yol>\", "
                                       f"silindiyse --cikar \"{ad}\" --neden \"...\""))
            continue
        if y.exists():
            kayip.append(("sorun", f"KİLİT YOK: {ad} klasör duruyor, .skill-kutuphanesi/kilit.json yok (silinmiş ya da kurulum yarım kaldı) "
                                   f"-> kurulumu yeniden yap (promptlar/09) ya da --cikar"))
        else:
            yeni = next((p for p in takipte if p.name == ad), None)
            if yeni is not None:
                kayip.append(("sorun", f"TAŞINMIŞ görünüyor: {ad} şimdi {kisa_yol(yeni)} -> --tasindi \"{ad}\" \"{kisa_yol(yeni)}\""))
            else:
                kayip.append(("sorun", f"KAYIP: {ad} klasörü yok ({r['yol']}) -> taşındıysa --tasindi \"{ad}\" \"<yeni yol>\", "
                                       f"silindiyse --cikar \"{ad}\" --neden \"...\""))
    for y in takipte:
        if y.name not in bp:
            kayip.append(("dikkat", f"KAYITLI DEĞİL: {y.name} hafızada yok -> --ekle \"{kisa_yol(y)}\" (bilinen_projeler'e yazar)"))
    bilinen_yollar = {_norm_ust(r["yol"]) for r in bp.values() if isinstance(r, dict) and isinstance(r.get("yol"), str)}
    for p in ayar.get("ek_projeler", []):
        if isinstance(p, str) and not Path(p).expanduser().exists() and _norm_ust(p) not in bilinen_yollar:
            kayip.append(("dikkat", f"ek_projeler yolu yok: {p}"))
    projeler.sort(key=lambda p: p["ad"].lower())
    tarama = tara_kayitsiz(ayar, ham, skiller)
    ayar_u = ayar_kontrol(ayar)
    satirlar_hepsi = [x for p in projeler for x in p["satirlar"]] + kayip
    durum = _en_kotu(satirlar_hepsi)
    if tarama["sorun"]:
        durum = "sorun"
    if durum == "temiz" and (any(a["sinif"] == "skilli" for a in tarama["adaylar"]) or tarama["sinira_ulasildi"]
                             or any(not u.startswith("BİLGİ") for u in ayar_u)):
        durum = "dikkat"
    sonuc = {"projeler": projeler, "kaybolanlar": kayip, "takipte_olmayan": cikti, "kayitsiz": tarama,
             "ayar_uyarilari": ayar_u, "durum": durum, "karar_bekleyen": []}
    sonuc["karar_bekleyen"] = _karar_bekleyenler(sonuc)
    return sonuc


def _karar_bekleyenler(s):
    k = []
    sk = [a for a in s["kayitsiz"]["adaylar"] if a["sinif"] == "skilli"]
    for a in sk[:8]:
        k.append(f"Kayıtsız proje: {a['yol']} ({a['skill_sayisi']} skill) -> --ekle ya da --yoksay")
    if len(sk) > 8:
        k.append(f"…ve {len(sk) - 8} kayıtsız klasör daha (--tara-kayitsiz)")
    for p in s["projeler"]:
        g = p["sayac"].get("guncelleme_var", 0)
        if g:
            k.append(f"{p['ad']}: {g} güncelleme -> skill-ekle.py \"{p['ad']}\" --guncelle --kuru, sonra onay")
        n = p["sayac"].get("bag_kirik", 0)
        if n:
            k.append(f"{p['ad']}: {n} kırık program bağı -> skill-ekle.py \"{p['ad']}\" --yenile (program kuruluysa) ya da --kaldir <ad>")
        n = p["sayac"].get("kayitsiz", 0)
        if n:
            k.append(f"{p['ad']}: {n} kayıtsız skill -> elle-kurulan.json ya da kendi_skilleri'ne yazılsın mı?")
    for _, m in s["kaybolanlar"]:
        k.append(m[:150])
    if len(k) > 12:
        k = k[:11] + [f"…ve {len(k) - 11} karar daha (notlar/proje-durumu.md)"]
    return k


def ozet_nesnesi(s):
    """--ozet-json nesnesi: yalnız sayılar ve adlar (D9); satirlar <= 15, her biri <= 160 karakter."""
    pr = [p for p in s["projeler"] if p.get("tur") != "elle"]
    n_s = sum(1 for p in s["projeler"] if p["durum"] == "sorun")
    n_d = sum(1 for p in s["projeler"] if p["durum"] == "dikkat")

    def topla(alan):
        return sum(p["sayac"].get(alan, 0) for p in s["projeler"]), [p["ad"] for p in s["projeler"] if p["sayac"].get(alan, 0)]
    sat = [f"{len(s['projeler'])} proje izleniyor: {n_s} sorun, {n_d} dikkat"]
    for etiket, alan in (("GÜNCELLEME VAR", "guncelleme_var"), ("ELLE DEĞİŞTİRİLMİŞ", "elle_degismis"),
                         ("KAYNAK KÜTÜPHANEDE YOK", "kaynak_yok"), ("KAYITSIZ SKILL", "kayitsiz")):
        n, adlar = topla(alan)
        sat.append(f"{etiket}: {n} skill" + (f" ({', '.join(adlar)})" if adlar else ""))
    nb, _ = topla("program_bag")
    nk, _ = topla("bag_kirik")
    nd, _ = topla("donmus")
    if nb + nd:
        sat.append(f"PROGRAM BAĞI: {nb} bağ ({nk} kırık), {nd} donmuş skill")
    kd = s["kayitsiz"]
    sk = sum(1 for a in kd["adaylar"] if a["sinif"] == "skilli")
    sat.append(f"KAYITSIZ PROJE: {sk} skilli klasör, {kd['talimat_sayisi']} yalnız talimat dosyalı")
    sat.append(f"KAYIP/TAŞINMIŞ/KİLİTSİZ: {sum(1 for d, _ in s['kaybolanlar'] if d == 'sorun')}")
    if kd["sinira_ulasildi"]:
        sat.append("tarama sınıra ulaştı (kayitsiz_tarama.derinlik/en_cok_klasor)")
    if kd["sorun"]:
        sat.append("tarama kökü okunamadı")
    kalan = sum(1 for p in pr if p["durum"] == "sorun" for x in p["satirlar"] if x[0] == "sorun")
    if kalan:
        sat.append(f"Proje sorun satırı: {kalan} (notlar/proje-durumu.md)")
    au = [u for u in s["ayar_uyarilari"] if not u.startswith("BİLGİ")]
    if au:
        sat.append(f"projeler.json uyarısı: {len(au)}")
    return {"arac": "proje-kullanimi", "durum": s["durum"], "satirlar": [x[:160] for x in sat[:15]],
            "karar_bekleyen": [x[:160] for x in s["karar_bekleyen"][:12]]}


def durum_raporu_metni(s, ayar):
    """notlar/proje-durumu.md: deterministik; tarih/saat/yaş yok (yalnız veri alanındaki tarihler)."""
    m = ["# Proje durumu — kayıtlı projelerin sağlığı", "",
         "> `araclar/proje-kullanimi.py --saglik` üretir; elle düzenleme. Salt okuma: hiçbir projeye ve genel skill klasörüne yazılmaz.",
         "> Tarih yoktur: içerik yalnız durum değişince değişir. Ayrıntı: `rehber/10-proje-kullanimi.md`.", "",
         f"**Genel durum: {s['durum']}**", "", "## Projeler",
         "| Proje | Durum | Skill (kilit/klasör) | Güncelleme var | Elle değişmiş | Kaynak yok | Kayıtsız | Kendi/elle | Araçlar | Son işlem |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for p in s["projeler"]:
        c = p["sayac"]
        ad = p["ad"] + (" (elle kurulu)" if p.get("tur") == "elle" else "")
        m.append(f"| {ad} | {p['durum']} | {c.get('kilit_skill', 0)}/{c.get('diskte', 0)} | {c.get('guncelleme_var', 0)} | "
                 f"{c.get('elle_degismis', 0)} | {c.get('kaynak_yok', 0)} | {c.get('kayitsiz', 0)} | {c.get('kendi_elle', 0)} | "
                 f"{p['araclar']} | {p['son_islem']} |")
    dis_p = [p for p in s["projeler"] if p["sayac"].get("program_bag", 0) + p["sayac"].get("donmus", 0) > 0]
    if dis_p:
        m += ["", "## Programla gelen ve donmuş skiller",
              "> Yukarıdaki 'Skill (kilit/klasör)' klasör sayısı bağları ve donmuşları da içerir.", "",
              "| Proje | Bağ | Donmuş | Kırık bağ |", "|---|---|---|---|"]
        for p in dis_p:
            c = p["sayac"]
            m.append(f"| {p['ad']} | {c.get('program_bag', 0)} | {c.get('donmus', 0)} | {c.get('bag_kirik', 0)} |")
    m += ["", "## Ayrıntı"]
    var = False
    for p in s["projeler"]:
        if p["satirlar"]:
            var = True
            m += [f"### {p['ad']} — {p['durum']}"] + [f"- [{d}] {t}" for d, t in p["satirlar"]]
    if not var:
        m.append("Yok.")
    m += ["", "## Kayıp, taşınmış ya da hafızada olmayan"] + ([f"- [{d}] {t}" for d, t in s["kaybolanlar"]] or ["Yok."])
    m += ["", "## Takipte olmayanlar"] + ([f"- {t}" for t in s["takipte_olmayan"]] or ["Yok."])
    kd = s["kayitsiz"]
    m += ["", "## Kayıtsız proje klasörleri",
          f"Tarama: {', '.join('`' + k + '`' for k in kd['kokler']) or '—'} (derinlik {kd['derinlik']}, bağlantılar izlenmedi)."]
    if kd["sinira_ulasildi"]:
        m.append("Tarama sınıra ulaştı: kayitsiz_tarama.derinlik / en_cok_klasor.")
    for b in kd["bilgi"] + kd["sorun"]:
        m.append(f"- {b}")
    sk = [a for a in kd["adaylar"] if a["sinif"] == "skilli"]
    if sk:
        m += ["| Klasör | Sınıf | Skill | Araçlar | Not |", "|---|---|---|---|---|"]
        for a in sk:
            not_ = "; ".join(f"{b['klasor']} bağlantı{' (GENEL KLASÖRE BAĞLI)' if b['genel'] else ''}" for b in a["baglanti"])
            if a["kilit"]:
                not_ = ("kilit var ama izleme kapsamı dışı: --ekle; " + not_).rstrip("; ")
            m.append(f"| `{a['yol']}` | {a['sinif']} | {a['skill_sayisi']} | {', '.join(a['araclar']) or '—'} | {not_} |")
    else:
        m.append("Kayıtsız skilli klasör yok.")
    m.append(f"Yalnız talimat dosyası olan klasör sayısı: {kd['talimat_sayisi']} (işlem gerekmez).")
    m += ["", "### Yoksayılanlar"]
    if kd["yoksayilan"]:
        m += ["| Yol | Neden | Tarih |", "|---|---|---|"] + [f"| `{y['yol']}` | {y['neden']} | {y['tarih']} |" for y in kd["yoksayilan"]]
    else:
        m.append("Yok.")
    m += ["", "## Karar bekleyenler"] + ([f"- {k}" for k in s["karar_bekleyen"]] or ["Yok."])
    m += ["", "## Ayar uyarıları"] + ([f"- {u}" for u in s["ayar_uyarilari"]] or ["Yok."])
    m.append("")
    return "\n".join(m)


# ---------------------------------------------------------------- ayar değişiklikleri (yalnız projeler.json)
class IslemHatasi(Exception):
    """Yazıcı doğrulama hatası: mesaj kullanıcıya gösterilir, çıkış kodu 2."""


def _yol_yaz(p):
    p = Path(p)
    for h in (Path.home(), Path(os.path.realpath(Path.home()))):
        try:
            return "~/" + str(p.relative_to(h))
        except ValueError:
            continue
    return str(p)


def _kilitli_mi(p):
    return (Path(p) / ".skill-kutuphanesi" / "kilit.json").exists()


def _kayit_bul(ayar, ad):
    """bilinen_projeler kaydı; yoksa izlenen projelerden ad ile bulunup yeni kayıt önerilir."""
    bp = ayar.setdefault("bilinen_projeler", {})
    if ad in bp:
        return bp[ad], False
    y = next((p for p in projeleri_bul_ham(ayar) if p.name == ad), None)
    if y is None:
        raise IslemHatasi(f"HATA: {ad} izlenen projelerde yok")
    return {"yol": _yol_yaz(y), "tur": "kilitli", "durum": "takipte", "eklendi": date.today().isoformat()}, True


def ayar_degistir(ayar, islem, **kw):
    """(yeni_ayar, [açıklama satırları]). Yalnız hesaplar; yazmaz. Hata: IslemHatasi."""
    yeni = copy.deepcopy(ayar)
    bugun = kw.get("bugun") or date.today().isoformat()
    neden = (kw.get("neden") or "").strip()
    satir = []
    if islem == "ekle":
        p = Path(kw["yol"]).expanduser()
        if not p.is_dir():
            raise IslemHatasi(f"HATA: {kw['yol']} bir klasör değil")
        p = p.resolve()
        yasak = [KOK.resolve(), Path.home().resolve()] + [Path(g).resolve() for g in GLOBAL_KLASORLER.values()]
        kokler = [Path(k).expanduser().resolve() for k in list(ayar.get("tarama_kokleri", []))
                  + list((ayar.get("kayitsiz_tarama") or {}).get("kokler", []))]
        if p in yasak or p in kokler or ".skill-kutuphanesi" in p.parts or any(g in p.parents for g in yasak[1:]) \
                or KOK.resolve() in p.parents:
            raise IslemHatasi("HATA: bu klasör proje olamaz (kütüphane ve altı, ev dizini, tarama kökünün kendisi ya da genel skill klasörü)")
        ad, kilitli = p.name, _kilitli_mi(p)
        if not kilitli and not neden:
            raise IslemHatasi("HATA: --neden zorunlu (kilitsiz, elle kurulu proje için)")
        bp = yeni.setdefault("bilinen_projeler", {})
        yazim = _yol_yaz(p)
        if ad in bp:
            if _norm(bp[ad]["yol"]) != _norm(p):
                raise IslemHatasi(f"HATA: {ad} adlı başka bir proje zaten kayıtlı ({bp[ad]['yol']}); aynı klasör adı desteklenmiyor")
            if bp[ad].get("durum") == "takipte":
                return yeni, [f"  = bilinen_projeler.{ad}: zaten takipte, değişiklik yok"]
            for a in ("cikis_tarihi", "cikis_nedeni"):
                bp[ad].pop(a, None)
            bp[ad]["durum"] = "takipte"
            satir.append(f"  ~ bilinen_projeler.{ad}: takipten çıkmıştı, yeniden takipte")
        else:
            bp[ad] = {"yol": yazim, "tur": "kilitli" if kilitli else "elle", "durum": "takipte", "eklendi": bugun}
            if not kilitli:
                bp[ad]["neden"] = neden
            satir.append(f"  + bilinen_projeler.{ad}: {yazim} ({bp[ad]['tur']})")
        if kilitli and not izleme_kapsaminda_mi(p, yeni)[0]:
            yeni.setdefault("ek_projeler", []).append(yazim)
            satir.append(f"  + ek_projeler: {yazim}")
        if not kilitli:
            satir.append("  ! kilit yok: güncellenmez, sadece sağlık/envanter; kütüphaneyle yönetmek için önce skill-ekle.py <yol> --kuru")
    elif islem == "cikar":
        if not neden:
            raise IslemHatasi("HATA: --neden zorunlu")
        rec, yeni_kayit = _kayit_bul(yeni, kw["ad"])
        rec.update({"durum": "takipten-cikti", "cikis_tarihi": bugun, "cikis_nedeni": neden})
        yeni["bilinen_projeler"][kw["ad"]] = rec
        satir.append(f"  {'+' if yeni_kayit else '~'} bilinen_projeler.{kw['ad']}: takipten-cikti ({bugun}) — {neden}")
        satir.append("  (proje klasörüne ve kilidine dokunulmaz; yalnız rapordan ve aylık listeden çıkar)")
    elif islem == "tasindi":
        ad = kw["ad"]
        p = Path(kw["yeni_yol"]).expanduser()
        if not p.is_dir():
            raise IslemHatasi(f"HATA: {kw['yeni_yol']} bir klasör değil")
        p = p.resolve()
        rec, yeni_kayit = _kayit_bul(yeni, ad)
        if rec.get("tur") == "kilitli" and not _kilitli_mi(p):
            raise IslemHatasi("HATA: yeni yolda kilit.json yok")
        eski = rec["yol"]
        rec["yol"] = _yol_yaz(p)
        if eski != rec["yol"]:
            rec.setdefault("onceki_yollar", []).append(eski)
        eski_n = _norm_ust(eski)
        ek = yeni.setdefault("ek_projeler", [])
        degisti = False
        for i, x in enumerate(ek):
            if _norm_ust(x) == eski_n:
                ek[i] = rec["yol"]
                degisti = True
        if rec.get("tur") == "kilitli" and not degisti and not izleme_kapsaminda_mi(p, yeni)[0]:
            ek.append(rec["yol"])
            degisti = True
        yeni["bilinen_projeler"][ad] = rec
        satir.append(f"  ~ bilinen_projeler.{ad}.yol: {eski} -> {rec['yol']}")
        if degisti:
            satir.append(f"  ~ ek_projeler: {rec['yol']}")
        if p.name != ad:
            for alan in ("bilinen_projeler", "notlar", "kendi_skilleri"):
                d = yeni.get(alan)
                if isinstance(d, dict) and ad in d:
                    if p.name in d:
                        raise IslemHatasi(f"HATA: {alan} içinde {p.name} adı zaten var")
                    d[p.name] = d.pop(ad)
            satir.append(f"  ~ klasör adı değişti: {ad} -> {p.name} (bilinen_projeler, notlar, kendi_skilleri anahtarları yeniden adlandırıldı)")
        satir.append(f"  Sonraki adım (bu araç çalıştırmaz): python3 araclar/skill-ekle.py \"{rec['yol']}\" --yenile --kuru, onaydan sonra --yenile")
    elif islem == "yoksay":
        if not neden:
            raise IslemHatasi("HATA: --neden zorunlu")
        yazim = _yol_yaz(Path(kw["yol"]).expanduser().resolve()) if Path(kw["yol"]).expanduser().exists() else kw["yol"]
        liste = yeni.setdefault("yoksay", [])
        if any(_norm_ust(y["yol"]) == _norm_ust(yazim) for y in liste if isinstance(y, dict) and "yol" in y):
            raise IslemHatasi(f"HATA: {yazim} zaten yoksay listesinde")
        liste.append({"yol": yazim, "altini_da": bool(kw.get("altini_da")), "neden": neden, "tarih": bugun})
        satir.append(f"  + yoksay: {yazim}{' (altı da)' if kw.get('altini_da') else ''} — {neden}")
    else:
        raise IslemHatasi(f"HATA: bilinmeyen işlem {islem}")
    hatalar = _sema(yeni)
    if hatalar:
        raise IslemHatasi("HATA: değişiklik geçersiz projeler.json üretirdi: " + "; ".join(hatalar))
    return yeni, satir


def _yazici(a):
    """--ekle/--cikar/--tasindi/--yoksay: plan göster; --evet ile yalnız projeler.json yaz. Çıkış: 0 / 2."""
    se = _skill_ekle()
    if se is not None:
        try:
            if se.guncelleme_suruyor():
                print("BEKLE: kütüphane aylık güncelleniyor; birkaç dakika sonra tekrar dene.")
                sys.exit(2)
        except SystemExit:
            raise
        except Exception:  # noqa: BLE001
            pass
    ayar = _ayar_oku()
    try:
        if a.ekle is not None:
            yeni, satir = ayar_degistir(ayar, "ekle", yol=a.ekle, neden=a.neden)
        elif a.cikar is not None:
            yeni, satir = ayar_degistir(ayar, "cikar", ad=a.cikar, neden=a.neden)
        elif a.tasindi is not None:
            yeni, satir = ayar_degistir(ayar, "tasindi", ad=a.tasindi[0], yeni_yol=a.tasindi[1])
        else:
            yeni, satir = ayar_degistir(ayar, "yoksay", yol=a.yoksay, neden=a.neden, altini_da=a.altini_da)
    except IslemHatasi as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)
    if a.evet:
        json_yaz(AYAR, yeni)
        print("\n".join(satir))
        print("projeler.json güncellendi (geri almak: git checkout -- projeler.json).")
        print("notlar/proje-kullanimi.md kendiliğinden yenilenmedi; istersen: python3 araclar/proje-kullanimi.py")
    else:
        print("PLAN (hiçbir şey yazılmadı; onaylıyorsan aynı komuta --evet ekle):")
        print("\n".join(satir))
    print(GUVENLIK_SATIRI)
    return 0


# ---------------------------------------------------------------- kipler
def _saglik_yukle(ayar):
    reg = json_oku(REGISTRY, {}) or {}
    return saglik_hesapla(ayar, reg.get("skiller", []))


def _saglik_kipi(a):
    global _CIKIS
    ayar = _ayar_oku()
    ozet = a.ozet_json
    if not projeleri_bul_ham(ayar):
        if ozet:
            print(json.dumps({"arac": "proje-kullanimi", "durum": "temiz",
                              "satirlar": ["Bu bilgisayarda proje bulunamadı: denetim atlandı"], "karar_bekleyen": []}, ensure_ascii=False))
        else:
            print("Hiç proje bulunamadı (başka bilgisayar/bulut olabilir); notlar/proje-durumu.md değiştirilmedi.")
        return 0
    if ozet:
        tampon = io.StringIO()
        try:
            with contextlib.redirect_stdout(tampon):
                s = _saglik_yukle(ayar)
            nesne = ozet_nesnesi(s)
            if a.yaz:
                metin = durum_raporu_metni(s, ayar)
                if not DURUM_RAPORU.exists() or DURUM_RAPORU.read_text(encoding="utf-8") != metin:
                    DURUM_RAPORU.write_text(metin, encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            s = None
            nesne = {"arac": "proje-kullanimi", "durum": "sorun", "satirlar": [f"denetim çalışmadı: {str(e)[:120]}"], "karar_bekleyen": []}
        print(json.dumps(nesne, ensure_ascii=False))
        if a.siki and nesne["durum"] == "sorun":
            _CIKIS = 1
        return 0
    s = _saglik_yukle(ayar)
    metin = durum_raporu_metni(s, ayar)
    if not DURUM_RAPORU.exists() or DURUM_RAPORU.read_text(encoding="utf-8") != metin:
        DURUM_RAPORU.write_text(metin, encoding="utf-8")
    sk = sum(1 for x in s["kayitsiz"]["adaylar"] if x["sinif"] == "skilli")
    n_s = sum(1 for p in s["projeler"] if p["durum"] == "sorun")
    n_d = sum(1 for p in s["projeler"] if p["durum"] == "dikkat")
    print(f"Proje sağlığı: {len(s['projeler'])} proje izleniyor · {n_s} sorun · {n_d} dikkat · {sk} kayıtsız skilli klasör · "
          f"rapor: {DURUM_RAPORU.relative_to(KOK) if DURUM_RAPORU.is_relative_to(KOK) else DURUM_RAPORU}")
    for p in s["projeler"]:
        print(f"  {p['ad']}: {p['durum']} ({p['sayac'].get('kilit_skill', 0)} skill)")
        if p["durum"] != "temiz":
            for d, t in [x for x in p["satirlar"] if x[0] != "bilgi"][:3]:
                print(f"    - [{d}] {t[:150]}")
    for d, t in s["kaybolanlar"]:
        print(f"  [{d}] {t[:170]}")
    print(f"Genel durum: {s['durum']}")
    print(GUVENLIK_SATIRI)
    if a.siki and s["durum"] == "sorun":
        _CIKIS = 1
    return 0


def _tara_kipi(a):
    global _CIKIS
    ayar = _ayar_oku()
    ham = projeleri_bul_ham(ayar)
    t = tara_kayitsiz(ayar, ham)
    print(f"Tarama: {', '.join(t['kokler']) or '—'} (derinlik {t['derinlik']}, {t['klasor_sayisi']} klasör bakıldı, bağlantılar izlenmedi)")
    sk = [x for x in t["adaylar"] if x["sinif"] == "skilli"]
    if sk:
        print("Kayıtsız skilli klasörler:")
        for x in sk:
            gb = " · GENEL KLASÖRE BAĞLI" if any(b["genel"] for b in x["baglanti"]) else ""
            print(f"  {x['yol']}  ({x['skill_sayisi']} skill; {', '.join(x['araclar']) or '—'}){gb}")
    else:
        print("Kayıtsız skilli klasör yok.")
    print(f"Yalnız talimat dosyası olan klasör sayısı: {t['talimat_sayisi']} (işlem gerekmez).")
    if t["yoksayilan"]:
        print("Yoksayılanlar:")
        for y in t["yoksayilan"]:
            print(f"  {y['yol']} — {y['neden']} ({y['tarih']})")
    if t["sinira_ulasildi"]:
        print("UYARI: tarama sınıra ulaştı -> kayitsiz_tarama.derinlik/en_cok_klasor")
    for b in t["bilgi"] + t["sorun"]:
        print(b)
    print(GUVENLIK_SATIRI)
    if a.siki and t["sorun"]:
        _CIKIS = 1
    return 0


def main(argv=None):
    global _CIKIS
    _CIKIS = 0
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skill", help="bu skill kimliğini kullanan projeleri yaz")
    ap.add_argument("--repo", help="bu kaynaktan (owner/ad) skill kullanan projeleri yaz")
    ap.add_argument("--program", metavar="AD", help="bu programın skillerine bağlı projeleri ve hedefin şimdi var olup olmadığını yaz (salt okuma)")
    ap.add_argument("--kontrol", action="store_true", help="rapor güncel mi? (yazmaz; kabukta çıkış kodu 0, --siki ile güncel değilse 1)")
    ap.add_argument("--siki", action="store_true", help="--kontrol/--saglik/--tara-kayitsiz: sorun varsa çıkış kodu 1")
    ap.add_argument("--saglik", action="store_true", help="her projenin sağlığı -> notlar/proje-durumu.md (salt okuma)")
    ap.add_argument("--ozet-json", action="store_true", help="--saglik özetini tek satır JSON olarak yaz (dosya yazmaz; --yaz ile rapor yenilenir)")
    ap.add_argument("--yaz", action="store_true", help="--ozet-json ile birlikte notlar/proje-durumu.md'yi de yenile")
    ap.add_argument("--tara-kayitsiz", action="store_true", help="kilitsiz ama skill klasörü olan klasörleri listele (yazmaz)")
    ap.add_argument("--ekle", metavar="YOL", help="projeyi takibe al (önce plan; --evet ile projeler.json'a yazar)")
    ap.add_argument("--cikar", metavar="AD", help="projeyi takipten çıkar (--neden zorunlu)")
    ap.add_argument("--tasindi", nargs=2, metavar=("AD", "YENI_YOL"), help="proje taşındı: yolu güncelle")
    ap.add_argument("--yoksay", metavar="YOL", help="klasörü bilerek takipsiz bırak (--neden zorunlu)")
    ap.add_argument("--neden", help="--ekle (kilitsiz), --cikar, --yoksay için gerekçe")
    ap.add_argument("--altini-da", action="store_true", help="--yoksay: klasörün altındakiler de yoksayılsın")
    ap.add_argument("--evet", action="store_true", help="yazıcılar: planı gerçekten projeler.json'a yaz")
    a = ap.parse_args(argv)
    yazicilar = [x for x in (a.ekle, a.cikar, a.tasindi, a.yoksay) if x is not None]
    if len(yazicilar) > 1:
        print("HATA: aynı anda yalnız bir değişiklik bayrağı verilebilir (--ekle, --cikar, --tasindi, --yoksay)", file=sys.stderr)
        sys.exit(2)
    if yazicilar and (a.saglik or a.ozet_json or a.tara_kayitsiz or a.kontrol or a.skill or a.repo or a.program):
        print("HATA: değişiklik bayrağı (--ekle, --cikar, --tasindi, --yoksay) okuma kipleriyle birlikte verilemez", file=sys.stderr)
        sys.exit(2)
    if yazicilar:
        return _yazici(a)
    if a.program and (a.saglik or a.ozet_json or a.tara_kayitsiz or a.kontrol or a.skill or a.repo):
        print("HATA: --program başka okuma kipleriyle birlikte verilemez", file=sys.stderr)
        sys.exit(2)
    if a.evet and not (a.saglik or a.ozet_json or a.tara_kayitsiz or a.kontrol or a.skill or a.repo or a.program):
        print("--evet tek başına bir şey yapmaz (yalnız --ekle/--cikar/--tasindi/--yoksay ile birlikte); yok sayıldı, hiçbir şey yazılmadı.")
        return 0
    if a.program:
        return _program_kipi(a)
    if a.saglik or a.ozet_json:
        return _saglik_kipi(a)
    if a.tara_kayitsiz:
        return _tara_kipi(a)
    if a.kontrol:
        ok, n = guncel_mi()
        print("Proje kullanım raporu güncel." if ok else "Proje kullanım raporu GÜNCEL DEĞİL -> python3 araclar/proje-kullanimi.py"
              + ("" if n else " (bu bilgisayarda proje bulunamadı)"))
        if a.siki and not ok:
            _CIKIS = 1
        return 0 if ok else 1
    return _eski_kipler(a)


def _program_hedefi(program, ad):
    """Bağın şimdiki hedefi (kartın skill_koku/ad yolu); kart ya da skill_koku yoksa None. Kilitteki hedef kullanılmaz."""
    try:
        kart = (json_oku(PROGRAMLAR, {}) or {}).get("programlar", {}).get(program)
    except (OSError, ValueError):
        return None
    sk = kart.get("skill_koku") if isinstance(kart, dict) else None
    if not isinstance(sk, str) or not sk.strip() or not DIS_AD.fullmatch(ad):
        return None
    return Path(sk).expanduser() / ad


def _program_kipi(a):
    """--program AD: bu programın skillerine bağlı projeler (salt okuma). --siki: hedefi YOK olan bağ varsa çıkış 1."""
    global _CIKIS
    ayar = json_oku(AYAR, {}) or {}
    bulundu = kirik = False
    for p in oku(ayar):
        for ad, g in sorted(dis_kayitlari(p["kilit"]).items()):
            if g["tur"] != "program-bag" or g.get("program") != a.program:
                continue
            h = _program_hedefi(a.program, ad)
            var = bool(h) and (h / "SKILL.md").is_file()
            surum = g.get("program_surum")
            surum_m = (str(surum)[:8] if g.get("program_surum_turu") == "commit" else str(surum)) if surum else "sürüm kayıtsız"
            print(f"{p['ad']}: {ad} — program bağı ({a.program} {surum_m}) · hedef {'var' if var else 'YOK'}")
            bulundu = True
            kirik = kirik or not var
    if not bulundu:
        print("Hiçbir projede bu programın bağı yok.")
    if a.siki and kirik:
        _CIKIS = 1
    return 0


def _eski_kipler(a):
    ayar, projeler, metin, kullanan = hesapla()
    if a.skill or a.repo:
        bulundu = False
        for p in projeler:
            for ad, v in sorted(p["kilit"].get("skiller", {}).items()):
                if (a.skill and a.skill in (v.get("id", ad), ad)) or \
                        (a.repo and repo_guncel(v.get("repo", "")).lower() == repo_guncel(a.repo).lower()):
                    print(f"{p['ad']}: {ad} — kimlik {v.get('id', ad)} ({repo_guncel(v.get('repo'))}@{str(v.get('commit', ''))[:7]})")
                    bulundu = True
        if a.skill:
            for p in projeler:
                g = dis_kayitlari(p["kilit"]).get(a.skill)
                if g and g["tur"] == "program-bag":
                    print(f"{p['ad']}: {a.skill} — programla gelen (bağ: {g.get('program', '?')})")
                    bulundu = True
                elif g:
                    print(f"{p['ad']}: {a.skill} — donmuş (projenin kendi kopyası)")
                    bulundu = True
        if not bulundu:
            print("Hiçbir projede kullanılmıyor.")
        return
    if not projeler:
        print("Bu bilgisayarda kütüphaneden skill kurulmuş proje bulunamadı (projeler.json -> tarama_kokleri); rapor değiştirilmedi.")
        return 0
    RAPOR.write_text(metin, encoding="utf-8")
    print(f"{len(projeler)} proje · {len(kullanan)} farklı skill kullanımda · rapor: {RAPOR.relative_to(KOK)}")
    for p in projeler:
        print(f"  {p['ad']}: {len(p['kilit'].get('skiller', {}))} skill")
    bilinmeyen = sorted(set(ayar.get("notlar", {})) - {p["ad"] for p in projeler})
    if bilinmeyen:
        print("UYARI: projeler.json notlarında olup bulunamayan proje: " + ", ".join(bilinmeyen))


if __name__ == "__main__":
    main()
    sys.exit(_CIKIS)
