#!/usr/bin/env python3
"""Tutarlılık kontrolü. Hata varsa çıkış kodu 1.

- Her registry kaydının klasörü + SKILL.md + KAYNAK.md var mı
- Arşivde registry'de olmayan klasör var mı
- 'tercih' durumunda aynı isimden iki kayıt var mı
- Roller/profiller var olan skillere/rollere mi bakıyor
- Bir rol aynı örtüşme grubundan en fazla 1 birincil + 1 tamamlayıcı alıyor mu
- Kaynaklar.json yıldızlı repoların hepsini kapsıyor mu (--github ile)
- CLAUDE.md == AGENTS.md (HATA); BASLA.md, notlar/kararlar.md, paket dosyaları, .gitignore korumaları, kayıt şemaları
  (programlar/projeler/yedekler/yapay-zeka-araclari/kaynaklar), yeni kaynak kayıtlarının onay kapıları, belgelerdeki
  araç/bayrak adları ve eski anlatım (hepsi UYARI; HATA yalnız ayrışmayan JSON kayıt dosyası ve CLAUDE/AGENTS farkı)
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import (ACIKLAMA_SINIRI, ARSIV, FM_BASTA, KAYNAKLAR, KOK, REGISTRY, frontmatter, frontmatter_onar,  # noqa: E402
                   frontmatter_teshis, git_blob_hash, json_oku, klasor_hash, YAMALAR, repo_guncel, yol_istisna_denetimi)


def tetikleme_denetimi(skiller, hatalar, uyarilar):
    """Kurulumda projeye konacak SKILL.md'yi (onarım uygulanmış haliyle) araçların göreceği gibi okur: frontmatter
    dosya başında mı, YAML ayrışıyor mu, description var mı ve 40..1024 karakter mi? Arşivdeki orijinallere dokunmaz."""
    try:
        import yaml
    except ImportError:
        yaml = None
    for s in skiller:
        duz = s.get("aciklama_duzeltme") or {}
        if duz:
            if not duz.get("description"):
                hatalar.append(f"aciklama_duzeltme boş: {s['id']}")
            elif duz.get("skill_md_hash") and duz["skill_md_hash"] != s.get("skill_md_hash"):
                uyarilar.append(f"aciklama_duzeltme eskidi (SKILL.md kaynakta değişti): {s['id']} -> yeni description'a bak; "
                                "gerek kalmadıysa aciklama_duzeltme'yi sil, kalıyorsa skill_md_hash'i güncelle")
        for rel in ((s.get("yama") or {}).get("dosyalar") or {}):
            orj, yama = KOK / s["yol"] / rel, YAMALAR / s["id"] / rel
            if not yama.is_file():
                hatalar.append(f"yama dosyası yok: yamalar/{s['id']}/{rel}")
            elif not orj.is_file() or git_blob_hash(orj.read_bytes()) != s["yama"]["dosyalar"][rel]:
                uyarilar.append(f"yama eskidi (orijinal kaynakta değişti; kurulumda uygulanmaz): {s['id']}/{rel} -> "
                                "yeni sürümü dene; sorun sürüyorsa yamayı yenile, düzeldiyse yamayı sil")
        for yol in [s["yol"]] + list((s.get("varyantlar") or {}).values()):
            f = KOK / yol / "SKILL.md"
            if not f.exists():
                continue
            metin, _ = frontmatter_onar(f.read_text(encoding="utf-8", errors="replace"), s["ad"], duz.get("description"))
            sorun = frontmatter_teshis(metin)
            fm = {}
            if not sorun:
                govde = FM_BASTA.match(metin).group(3)
                try:
                    fm = yaml.safe_load(govde) if yaml else frontmatter(metin)
                except yaml.YAMLError as e:
                    sorun.append("YAML ayrışmıyor: " + str(e).splitlines()[0])
                if not isinstance(fm, dict):
                    fm = {}
            ac = fm.get("description") if isinstance(fm.get("description"), str) else ""
            if not sorun and not ac.strip():
                sorun.append("description yok")
            elif not sorun and len(ac) > ACIKLAMA_SINIRI:
                sorun.append(f"description {len(ac)} karakter > {ACIKLAMA_SINIRI}")
            elif not sorun and len(ac.strip()) < 40:
                sorun.append(f"description çok kısa ({len(ac.strip())} karakter)")
            if sorun:
                (hatalar if not s.get("gizli") else uyarilar).append(
                    f"kurulunca tetiklenmez: {yol} -> {'; '.join(sorun)} (registry.json aciklama_duzeltme)")


# --- P8: belge ve kayıt denetimleri -------------------------------------------------------------------------------
# Birleştirme kuralı: buradaki HER yeni denetim yalnız UYARI'dır. HATA yalnız (a) var olan bir JSON kayıt dosyasının
# ayrıştırılamaması ve (b) CLAUDE.md ile AGENTS.md'nin eşit olmamasıdır (arsiv-guncelle --birlestir HATA'da master'ı geri alır).
# Hiçbiri başka bir aracı çalıştırmaz (tek istisna: program-denetim.py --sema --ozet-json, ağsız); bayraklar kaynak
# metninden okunur, --help'e güvenilmez (birçok araçta argparse yok, --help aracı çalıştırır).
KAYNAK_TIPLERI = ("T1", "T2", "T3", "T4", "T5", "T6", "KAYIP", "EMEKLI")
KAYNAK_ANAHTARLARI = ("repo", "tip", "oncelik", "not", "haric", "dahil", "dahil_degil", "bagimlilik", "kimlik", "dosya_haric",
                      "program", "kok_dosyalari", "eski_adlar", "ad_devral", "eklendi", "onay", "kayip_tarihi")
ZORUNLU_ARACLAR = ("claude-code", "codex", "antigravity", "cursor", "vscode-copilot")
GITIGNORE_KALIPLARI = ("/.env", "/.env.*", "!/.env.example", "/araclar/.env", "/*.pem", "/*.key", "/*.p12", "/*.pfx",
                       "/programlar/**/.env", "/yedek/", "/.skill-kutuphanesi/", "/*.bundle", "/*.yedek",
                       "/notlar/son-aylik-calisma.json", "/notlar/aylik-ozet.md")
REHBER13_DIZGILERI = ("git revert -m 1", "gh auth login", "git bundle create", "yedekler.json", "rehber/12")
# Paket dosyası tablosu (yol -> paket). notlar/genel-klasor-tabani.json bilerek yok: yalnız boşaltma gününde yazılır,
# o güne dek eksikliği kalıcı bir uyarı olurdu (sürümü varsa E5 denetler).
PAKET_DOSYALARI = (
    ("rehber/12-genel-klasor-bosaltma.md", "P2"), ("rehber/13-yedek-ve-geri-alma.md", "P3"),
    ("rehber/14-yapay-zeka-araclari.md", "P1"), ("promptlar/13-program-kur-guncelle.md", "P6"),
    ("promptlar/14-kaynak-cikar.md", "P7"), ("promptlar/15-yeni-yapay-zeka-araci.md", "P1"),
    ("promptlar/16-genel-klasor-bosaltma.md", "P2"), ("yapay-zeka-araclari.json", "P1"), ("yedekler.json", "P3"),
    ("araclar/genel-bekci.py", "P2"), ("araclar/git-durum.py", "P3"), ("araclar/yedek-denetim.py", "P3"),
    ("araclar/aylik-ozet.py", "P4"), ("araclar/kaynak-cikar.py", "P7"),
)
BELGE_TARAMASI = ("CLAUDE.md", "AGENTS.md", "BASLA.md", "README.md")
ESKI_ANLATIM = (re.compile(r"(?i)global skill klasörlerin[^\n]*değişmez"), re.compile(r"(?i)eski agent'ların[^\n]*devam eder"))


def _metin(f):
    try:
        return Path(f).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _json_kayit(kok, yol, h):
    """Var olan JSON kayıt dosyası -> (nesne | None, dosya_var_mi). Ayrışmıyorsa HATA (kural a)."""
    f = Path(kok) / yol
    if not f.is_file():
        return None, False
    try:
        return json.loads(f.read_text(encoding="utf-8")), True
    except (ValueError, OSError) as e:
        h.append(f"{yol} okunamadı: {str(e)[:100]}")
        return None, True


def esitlik_denetimi(kok=KOK):
    """CLAUDE.md ile AGENTS.md birebir aynı olmalı (HATA). GEMINI.md varsa BASLA.md'ye işaret etmeli (UYARI)."""
    kok = Path(kok)
    h, u = [], []
    a, b = kok / "CLAUDE.md", kok / "AGENTS.md"
    if not a.is_file() or not b.is_file():
        h.append("CLAUDE.md/AGENTS.md eksik")
    elif a.read_bytes() != b.read_bytes():
        h.append("CLAUDE.md ile AGENTS.md aynı değil (cp CLAUDE.md AGENTS.md)")
    g = kok / "GEMINI.md"
    if g.is_file() and "BASLA.md" not in _metin(g):
        u.append("GEMINI.md BASLA.md'ye işaret etmiyor")
    return h, u


def giris_belgeleri_denetimi(kok=KOK):
    kok = Path(kok)
    h, u = [], []
    basla, karar = kok / "BASLA.md", kok / "notlar" / "kararlar.md"
    if not basla.is_file():
        u.append("BASLA.md yok")
    if not karar.is_file():
        u.append("notlar/kararlar.md yok")
    else:
        satirlar = _metin(karar).splitlines()
        for b in ("## Geçerli kararlar", "## Değişen kararlar", "## Karar bekleyenler", "## Kabul edilen bekleyenler"):
            if not any(s.startswith(b) for s in satirlar):
                u.append(f"notlar/kararlar.md'de '{b}' başlığı yok")
    ilk = (_metin(kok / "CLAUDE.md").splitlines() or [""])[0]
    if (kok / "CLAUDE.md").is_file() and "BASLA.md" not in ilk:
        u.append("CLAUDE.md ilk satırı BASLA.md'ye işaret etmiyor")
    if basla.is_file():
        t = _metin(basla)
        for yol in sorted(set(re.findall(r"`((?:araclar|rehber|promptlar|notlar)/[\w./-]+\.(?:py|md|json|txt))`", t))):
            if not (kok / yol).exists():
                u.append(f"BASLA.md olmayan dosyayı anıyor: {yol}")
        for gerekli in ("notlar/kararlar.md", "DURUM.md"):
            if gerekli not in t:
                u.append(f"BASLA.md {gerekli} dosyasını anmıyor")
    return h, u


def paket_dosyalari_denetimi(kok=KOK):
    kok = Path(kok)
    h, u = [], []
    for yol, paket in PAKET_DOSYALARI:
        if not (kok / yol).exists():
            u.append(f"{paket} dosyası yok: {yol}")
    gi = kok / ".gitignore"
    if ".gitignore değişikliği reddedildi" not in _metin(kok / "notlar" / "kararlar.md"):
        satirlar = {s.strip() for s in _metin(gi).splitlines()}
        eksik = [k for k in GITIGNORE_KALIPLARI if k not in satirlar]
        if eksik:
            u.append(f".gitignore'da yedek/gizli koruma satırı eksik: {', '.join(eksik[:6])}")
    r13 = kok / "rehber" / "13-yedek-ve-geri-alma.md"
    if r13.is_file():
        t = _metin(r13)
        eksik = [d for d in REHBER13_DIZGILERI if d not in t]
        if eksik:
            u.append(f"rehber/13-yedek-ve-geri-alma.md eksik içerik: {', '.join(eksik)}")
    return h, u


def arac_anahtarlari(kok=KOK):
    """yapay-zeka-araclari.json -> anahtar kümesi (liste biçimi; sözlük biçimi de kabul). Yok ya da bozuksa boş küme."""
    try:
        d = json.loads((Path(kok) / "yapay-zeka-araclari.json").read_text(encoding="utf-8"))
        a = d["araclar"]
        if isinstance(a, dict):
            return set(a)
        return {r["anahtar"] for r in a if isinstance(r, dict) and isinstance(r.get("anahtar"), str)}
    except (OSError, ValueError, KeyError, TypeError):
        return set()


def _yukle(dosya, ad):
    import importlib.util
    spec = importlib.util.spec_from_file_location(ad, dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _e1_programlar(kok, h, u):
    d, var = _json_kayit(kok, "programlar.json", h)
    if not var or d is None:
        return
    if not isinstance(d.get("programlar") if isinstance(d, dict) else None, dict):
        u.append("programlar.json: 'programlar' sözlüğü yok")
        return
    arac = Path(kok) / "araclar" / "program-denetim.py"
    if arac.is_file() and '"--sema"' in _metin(arac):
        try:
            r = subprocess.run([sys.executable, str(arac), "--sema", "--ozet-json"], cwd=kok, capture_output=True,
                               text=True, timeout=60, stdin=subprocess.DEVNULL)
            o = json.loads(r.stdout)
            if r.returncode != 0 or not isinstance(o, dict) or not isinstance(o.get("satirlar"), list):
                raise ValueError("çıkış")
            for s in o["satirlar"]:
                if isinstance(s, str) and s.startswith(("HATA:", "UYARI:")):
                    u.append(f"programlar.json kart şeması: {s}")
        except (ValueError, OSError, subprocess.SubprocessError):
            u.append("program şema denetimi çalışmadı (python3 araclar/program-denetim.py --sema)")
    for ad, kart in d["programlar"].items():  # gerçek kart içeriği kontrolü (testten buraya taşındı): güncelleme adımlarında '--oncesi'
        ad_ = kart.get("guncelleme_adimlari") if isinstance(kart, dict) else None
        if isinstance(ad_, list) and not any(isinstance(x, str) and "program-denetim.py --oncesi" in x for x in ad_):
            u.append(f"program {ad}: guncelleme_adimlari'nda 'program-denetim.py --oncesi' yok")
    anahtarlar = arac_anahtarlari(kok)
    if anahtarlar:
        for ad, kart in d["programlar"].items():
            gy = kart.get("giris_yolu") if isinstance(kart, dict) else None
            ar = gy.get("araclar") if isinstance(gy, dict) else None
            for k in (ar if isinstance(ar, dict) else {}):
                if k not in anahtarlar:
                    u.append(f"program {ad}: giris_yolu araç anahtarı yok: {k}")


def _e2_projeler(kok, h, u):
    d, var = _json_kayit(kok, "projeler.json", h)
    if not var or d is None:
        return
    if not isinstance(d, dict):
        u.append("projeler.json: üst düzey sözlük değil")
        return
    for k in ("tarama_kokleri", "ek_projeler"):
        if k in d and not (isinstance(d[k], list) and all(isinstance(x, str) for x in d[k])):
            u.append(f"projeler.json: '{k}' metin listesi değil")
    if "notlar" in d and not isinstance(d["notlar"], dict):
        u.append("projeler.json: 'notlar' sözlük değil")
    for k in ("bilinen_projeler", "program_kullanimi", "kendi_skilleri"):
        if k in d and not isinstance(d[k], dict):
            u.append(f"projeler.json: '{k}' sözlük değil")
    if "yoksay" in d:
        y = d["yoksay"]
        if not (isinstance(y, list) and all(isinstance(x, dict) and x.get("yol") and x.get("neden") for x in y)):
            u.append("projeler.json: 'yoksay' kayıtlarında yol ya da neden eksik")
    if isinstance(d.get("tarama_kokleri"), list):
        for yol in d["tarama_kokleri"]:
            if isinstance(yol, str) and not Path(yol).expanduser().exists():
                u.append(f"projeler.json: tarama kökü bu bilgisayarda yok: {yol}")


def _e3_yedekler(kok, h, u):
    d, var = _json_kayit(kok, "yedekler.json", h)
    if not var or d is None:
        return
    if not isinstance(d, dict) or d.get("surum") != 1:
        u.append("yedekler.json: surum 1 değil")
    kayitlar = d.get("yedekler") if isinstance(d, dict) else None
    if not isinstance(kayitlar, list):
        u.append("yedekler.json: 'yedekler' listesi yok")
        return
    turler = None
    ydosya = Path(kok) / "araclar" / "yedek-denetim.py"
    if ydosya.is_file():
        try:
            turler = tuple(getattr(_yukle(ydosya, "yedek_denetim_p8"), "TURLER"))
        except Exception:  # noqa: BLE001
            turler = None
    gorulen = set()
    for i, k in enumerate(kayitlar):
        if not isinstance(k, dict):
            u.append(f"yedekler.json: kayıt {i + 1} sözlük değil")
            continue
        eksik = [a for a in ("kimlik", "yol", "tur", "ne", "tarih", "geri_yukleme", "gizli_icerir") if a not in k]
        if eksik:
            u.append(f"yedekler.json: {k.get('kimlik', i + 1)} kaydında eksik alan: {', '.join(eksik)}")
        if k.get("gizli_icerir") not in ("evet", "hayir") and "gizli_icerir" in k:
            u.append(f"yedekler.json: {k.get('kimlik')} gizli_icerir 'evet' ya da 'hayir' olmalı")
        if k.get("kimlik") in gorulen:
            u.append(f"yedekler.json: kimlik tekrarlanıyor: {k.get('kimlik')}")
        gorulen.add(k.get("kimlik"))
        if turler and "tur" in k and k["tur"] not in turler:
            u.append(f"yedekler.json: {k.get('kimlik')} tür geçersiz: {k['tur']}")


def _tarih_gecerli(s):
    from datetime import date
    try:
        date.fromisoformat(s)
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", s))
    except (ValueError, TypeError):
        return False


def _e4_araclar(kok, h, u):
    d, var = _json_kayit(kok, "yapay-zeka-araclari.json", h)
    if not var or d is None:
        return
    a = d.get("araclar") if isinstance(d, dict) else None
    kayitlar = list(a.values()) if isinstance(a, dict) else a
    if not isinstance(kayitlar, list):
        u.append("yapay-zeka-araclari.json: 'araclar' listesi yok")
        return
    anahtarlar = arac_anahtarlari(kok)
    for z in ZORUNLU_ARACLAR:
        if z not in anahtarlar:
            u.append(f"araç kaydı yok: {z}")
    for r in kayitlar:
        if not isinstance(r, dict):
            u.append("yapay-zeka-araclari.json: kayıt sözlük değil")
            continue
        eksik = [x for x in ("anahtar", "ad", "kurulu", "proje_skill_okur", "dogrulama_tarihi", "surumler") if x not in r]
        if eksik:
            u.append(f"yapay-zeka-araclari.json: {r.get('anahtar', '?')} kaydında eksik alan: {', '.join(eksik)}")
        if "dogrulama_tarihi" in r and not _tarih_gecerli(r["dogrulama_tarihi"]):
            u.append(f"yapay-zeka-araclari.json: {r.get('anahtar', '?')} dogrulama_tarihi AAAA-AA-GG değil")


def _e5_taban(kok, h, u):
    d, var = _json_kayit(kok, "notlar/genel-klasor-tabani.json", h)
    if var and d is not None and (not isinstance(d, dict) or d.get("surum") != 1):
        u.append("notlar/genel-klasor-tabani.json: surum 1 değil")


def _e6_kaynaklar(kok, h, u):
    d, var = _json_kayit(kok, "kaynaklar.json", h)
    if not var or d is None:
        return
    kayitlar = d.get("repolar") if isinstance(d, dict) else None
    if not isinstance(kayitlar, list):
        u.append("kaynaklar.json: 'repolar' listesi yok")
        return
    gorulen = set()
    for k in kayitlar:
        if not isinstance(k, dict):
            u.append("kaynaklar.json: kayıt sözlük değil")
            continue
        repo = k.get("repo")
        if not isinstance(repo, str) or not re.fullmatch(r"[\w.-]+/[\w.-]+", repo):
            u.append(f"kaynaklar.json: repo adı 'sahip/ad' biçiminde değil: {repo!r}")
            continue
        anahtar = (repo.lower(), k.get("tip"), k.get("kimlik"))  # aynı repo farklı tip/kimlikle birkaç kez olabilir (T2 + T5 gibi)
        if anahtar in gorulen:
            u.append(f"kaynaklar.json: aynı repo, tip ve kimlikle tekrarlanıyor: {repo}")
        gorulen.add(anahtar)
        if k.get("tip") not in KAYNAK_TIPLERI:
            u.append(f"kaynaklar.json: {repo} tip bilinmiyor: {k.get('tip')!r}")
        if "oncelik" in k and (isinstance(k["oncelik"], bool) or not isinstance(k["oncelik"], int)):
            u.append(f"kaynaklar.json: {repo} oncelik sayı değil")
        yabanci = [x for x in k if x not in KAYNAK_ANAHTARLARI]
        if yabanci:
            u.append(f"kaynaklar.json: {repo} bilinmeyen anahtar: {', '.join(yabanci)}")


def kayit_semalari_denetimi(kok=KOK):
    h, u = [], []
    for f in (_e1_programlar, _e2_projeler, _e3_yedekler, _e4_araclar, _e5_taban, _e6_kaynaklar):
        f(kok, h, u)
    return h, u


def _git_head_kaynaklar(kok):
    try:
        r = subprocess.run(["git", "show", "HEAD:kaynaklar.json"], cwd=kok, capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            return None
        return json.loads(r.stdout)
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def kaynak_kapilari_denetimi(kok=KOK, skiller=None):
    """P7'nin yeni-kayıt kapıları. YENİ = HEAD'deki kaynaklar.json'da (repo ya da eski_adlar) karşılığı olmayan kayıt.
    HEAD okunamazsa (git yok, dosya yok) kapılar sessizce atlanır. Hepsi UYARI."""
    kok = Path(kok)
    h, u = [], []
    try:
        simdi = json.loads((kok / "kaynaklar.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return h, u  # ayrışmama zaten E6'da HATA
    for k in simdi.get("repolar", []):
        if isinstance(k, dict) and k.get("tip") == "KAYIP" and not k.get("kayip_tarihi"):
            u.append(f"kayıp kaynakta kayip_tarihi yok: {k.get('repo')}")
    eski = _git_head_kaynaklar(kok)
    if not isinstance(eski, dict):
        return h, u
    adlar = set()
    for k in eski.get("repolar", []):
        if isinstance(k, dict):
            adlar.add(str(k.get("repo", "")).lower())
            adlar.update(str(x).lower() for x in (k.get("eski_adlar") or []))
    kk = None
    lisans_riskli = kapi = None
    try:
        lisans_riskli = _yukle(kok / "araclar" / "kaynak-cek.py", "kaynak_cek_p8").lisans_riskli
    except Exception:  # noqa: BLE001
        lisans_riskli = None
    try:
        kapi = _yukle(kok / "araclar" / "yol-tara.py", "yol_tara_p8").kapi_kontrol
    except Exception:  # noqa: BLE001
        kapi = None
    for k in simdi.get("repolar", []):
        if not isinstance(k, dict) or not isinstance(k.get("repo"), str):
            continue
        adlari = {k["repo"].lower()} | {str(x).lower() for x in (k.get("eski_adlar") or [])}
        if adlari & adlar:
            continue  # yeni değil (yeniden adlandırma da yeni sayılmaz)
        repo = k["repo"]
        onay = k.get("onay") if isinstance(k.get("onay"), dict) else {}
        if not (k.get("eklendi") and _tarih_gecerli(k.get("eklendi")) and onay.get("kim") and onay.get("tarih")
                and re.fullmatch(r"[0-9a-f]{40}", str(onay.get("commit", "")))):
            u.append(f"kaynak kaydında onay yok: {repo} (rehber/03 A4)")
        if lisans_riskli and not onay.get("lisans_onay"):
            for s in (skiller or []):
                if s.get("repo") == repo and lisans_riskli(s.get("lisans")):
                    u.append(f"lisans {s.get('lisans') or 'belirsiz'} için onay.lisans_onay yok: {repo}")
                    break
        if kapi and not onay.get("yol_onay"):
            try:
                sorunlar, _taranan, hata = kapi(repo, None, skiller)
                if hata:
                    u.append(f"yol kapısı çalışmadı: {repo}")
                elif sorunlar:
                    u.append(f"yol kapısı takıldı: {repo}: {sorunlar[0]}")
            except Exception:  # noqa: BLE001
                u.append(f"yol kapısı çalışmadı: {repo}")
    for anahtar in ("arsivden_cikarilan_repolar", "arsivden_cikarilanlar"):
        once = {json.dumps(x, sort_keys=True, ensure_ascii=False) for x in eski.get(anahtar, [])}
        for x in simdi.get(anahtar, []):
            if json.dumps(x, sort_keys=True, ensure_ascii=False) in once or not isinstance(x, dict):
                continue
            on = x.get("onay") if isinstance(x.get("onay"), dict) else {}
            if not (on.get("kim") and on.get("tarih")) or "<NEDEN" in str(x.get("neden", "")) \
                    or (anahtar == "arsivden_cikarilan_repolar" and not x.get("geri_alma")):
                u.append(f"{anahtar} kaydında onay/neden/geri_alma eksik: {x.get('repo')} (rehber/03)")
    return h, u


def _arac_bayraklari(metin):
    """Aracın bayrakları: tırnak içindeki '--x' dizgileri + dosya başı açıklamasındaki (docstring) kullanım satırları."""
    bay = set(re.findall(r"""["'](--[a-z][a-z0-9-]*)(?=[=\s"'])""", metin))
    m = re.match(r"""\s*(?:#[^\n]*\n)*\s*(?:[rR])?(\"\"\"|\'\'\')(.*?)\1""", metin, re.S)
    if m:
        bay |= set(re.findall(r"(?<![\w-])(--[a-z][a-z0-9-]*)", m.group(2)))
    return bay | {"--help", "-h"}


def bayrak_denetimi(kok=KOK):
    """Belgelerde anılan araclar/<araç>.py ve bayrakları var mı? Bayraklar kaynak metninden okunur (--help çalıştırılmaz)."""
    kok = Path(kok)
    h, u = [], []
    belgeler = [kok / b for b in BELGE_TARAMASI] + sorted((kok / "rehber").glob("*.md")) + sorted((kok / "promptlar").glob("*.md"))
    onbellek = {}
    for b in belgeler:
        if not b.is_file():
            continue
        satirlar = _metin(b).splitlines()
        i = 0
        while i < len(satirlar):
            no, satir = i + 1, satirlar[i]
            while satir.endswith("\\") and i + 1 < len(satirlar):
                i += 1
                satir = satir[:-1] + " " + satirlar[i].strip()
            i += 1
            for m in re.finditer(r"araclar/([a-z][\w-]*)\.py([^`\n]*)", satir):
                ad, kalan = m.group(1), m.group(2)
                arac = kok / "araclar" / f"{ad}.py"
                if not arac.is_file():
                    u.append(f"{b.relative_to(kok)}:{no}: olmayan araç araclar/{ad}.py")
                    continue
                if ad not in onbellek:
                    onbellek[ad] = _arac_bayraklari(_metin(arac))
                for bayrak in re.findall(r"(?<![\w-])(--[a-z][a-z0-9-]*)", kalan):
                    if bayrak not in onbellek[ad]:
                        u.append(f"{b.relative_to(kok)}:{no}: araclar/{ad}.py '{bayrak}' bayrağını tanımıyor")
    return h, u


def eski_anlatim_denetimi(kok=KOK):
    kok = Path(kok)
    h, u = [], []
    belgeler = [kok / b for b in BELGE_TARAMASI] + sorted((kok / "rehber").glob("*.md")) + sorted((kok / "promptlar").glob("*.md"))
    for b in belgeler:
        for no, satir in enumerate(_metin(b).splitlines(), 1):
            if any(d.search(satir) for d in ESKI_ANLATIM):
                u.append(f"{b.relative_to(kok)}:{no}: eski anlatım (genel klasörler boşaltılacak, notlar/kararlar.md K-04): {satir.strip()[:60]}")
    return h, u


def belge_ve_kayit_denetimleri(kok=KOK, skiller=None):
    """Tüm P8 denetimleri -> (hatalar, uyarilar). Hiçbiri doğrulamayı düşüremez: beklenmedik hata UYARI olur."""
    hatalar, uyarilar = [], []
    for ad, f in (("eşitlik", esitlik_denetimi), ("giriş belgeleri", giris_belgeleri_denetimi),
                  ("paket dosyaları", paket_dosyalari_denetimi), ("kayıt şemaları", kayit_semalari_denetimi),
                  ("kaynak kapıları", lambda k: kaynak_kapilari_denetimi(k, skiller)),
                  ("bayraklar", bayrak_denetimi), ("eski anlatım", eski_anlatim_denetimi)):
        try:
            h, u = f(kok)
        except Exception as e:  # noqa: BLE001
            h, u = [], [f"{ad} denetimi çalışmadı ({type(e).__name__}: {str(e)[:80]})"]
        hatalar += h
        uyarilar += u
    return hatalar, uyarilar


def main():
    hatalar, uyarilar = [], []
    skiller = json_oku(REGISTRY)["skiller"]
    ids = {s["id"]: s for s in skiller}
    for s in skiller:
        k = KOK / s["yol"]
        if not (k / "SKILL.md").exists():
            hatalar.append(f"SKILL.md yok: {s['yol']}")
        if not (k / "KAYNAK.md").exists():
            hatalar.append(f"KAYNAK.md yok: {s['yol']}")
        if k.exists() and s.get("ana_hash") and klasor_hash(k) != s["ana_hash"]:
            hatalar.append(f"arşivdeki dosyalar registry ile uyuşmuyor (elle değiştirilmiş?): {s['yol']}")
        for arac, v in (s.get("varyantlar") or {}).items():
            if not (KOK / v / "SKILL.md").exists():
                hatalar.append(f"araç sürümü eksik: {s['id']} -> {v}")
            elif s.get("varyant_hash", {}).get(arac) and klasor_hash(KOK / v) != s["varyant_hash"][arac]:
                hatalar.append(f"araç sürümü registry ile uyuşmuyor: {v}")
    tetikleme_denetimi(skiller, hatalar, uyarilar)
    try:
        h_y, u_y = yol_istisna_denetimi(skiller)  # yol-istisnalari.json (dosya yoksa sessiz)
    except Exception as e:  # noqa: BLE001  bozuk istisna dosyası tüm doğrulamayı düşürmesin: HATA satırı olur
        h_y, u_y = [f"yol-istisnalari.json denetlenemedi ({type(e).__name__}: {str(e)[:100]})"], []
    hatalar += h_y
    uyarilar += u_y
    for s in skiller:
        if s.get("ucret") == "belirsiz" and not s.get("gizli"):
            uyarilar.append(f"ücret sınıflandırılmadı: {s['id']} ({s.get('ucret_notu', '')[:90]})")
        if "ucret" not in s:
            hatalar.append(f"ücret alanı yok: {s['id']} (arsiv-yerlestir.py çalıştır)")
    eksik_gel = sorted({s["repo"] for s in skiller if not s.get("gelistirici")})
    if eksik_gel:
        uyarilar.append(f"geliştirici bilgisi yok (değerlendirme puanı düşük çıkar): {', '.join(eksik_gel[:6])} "
                        "-> python3 araclar/gelistirici-bilgisi.py && python3 araclar/arsiv-yerlestir.py")
    kayitli = {str((KOK / s["yol"]).resolve()) for s in skiller}
    for sm in ARSIV.rglob("KAYNAK.md"):
        if str(sm.parent.resolve()) not in kayitli:
            hatalar.append(f"registry'de olmayan klasör: {sm.parent.relative_to(KOK)}")
    for ad, n in Counter(s["ad"] for s in skiller if s["durum"] == "tercih").items():
        if n > 1:
            hatalar.append(f"aynı isimde birden fazla 'tercih': {ad}")
    for f in sorted((KOK / "roller").glob("*.json")):
        r = json_oku(f)
        for x in r["cekirdek"] + r.get("opsiyonel", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"rol {f.stem}: skill yok -> {x}")
        for x in r["cekirdek"] + r.get("opsiyonel", []):
            s = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
            if s and (s.get("kaynak_durumu") in ("kaynakta-kaldirildi", "kayip") or s.get("ortusme_rolu") == "emekli"):
                uyarilar.append(f"rol {f.stem}: '{x}' emekli/kaynakta kaldırılmış; arşiv kopyası kullanılıyor (yerine yenisini düşün)")
        for x in r["cekirdek"]:
            s = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
            if s and s.get("ucret") == "ucretli" and "ucretli_bilincli" not in r:
                uyarilar.append(f"rol {f.stem}: çekirdekte ÜCRETLİ skill '{x}' (ücretsiz alternatif varsa çekirdeğe onu koy; "
                                "rol bilinçli olarak ücretliyse rol dosyasına \"ucretli_bilincli\": \"gerekçe\" ekle)")
            if s and s.get("inceleme") == "yeniden-incelenecek":
                uyarilar.append(f"rol {f.stem}: çekirdek skill '{x}' güncellemeden sonra yeniden incelenmeli")
        gruplar = Counter()
        for x in r["cekirdek"]:
            s = ids.get(x)
            if s and s.get("ortusme_grubu"):
                gruplar[(s["ortusme_grubu"], s.get("ortusme_rolu"))] += 1
        for (g, rol), n in gruplar.items():
            if rol == "birincil" and n > 1:
                uyarilar.append(f"rol {f.stem}: '{g}' grubundan {n} birincil skill")
    # Örtüşme grupları: 'alternatif' üyesi olan grubun mutlaka bir 'birincil'i olmalı (yoksa alternatif neye alternatif?)
    gruplar = {}
    for s in skiller:
        if s.get("ortusme_grubu"):
            gruplar.setdefault(s["ortusme_grubu"], []).append(s)
    for g, uyeler in sorted(gruplar.items()):
        roller_g = {u.get("ortusme_rolu") for u in uyeler}
        if "alternatif" in roller_g and "birincil" not in roller_g:
            uyarilar.append(f"örtüşme grubu '{g}': alternatifler var ama birincil yok ({', '.join(u['id'] for u in uyeler[:4])}…)")
        gecersiz = roller_g - {"birincil", "tamamlayıcı", "alternatif", "emekli", None}
        if gecersiz:
            hatalar.append(f"örtüşme grubu '{g}': geçersiz rol değeri {sorted(map(str, gecersiz))}")
    roller = {f.stem for f in (KOK / "roller").glob("*.json")}
    for f in sorted((KOK / "profiller").glob("*.json")):
        p = json_oku(f)
        for r in p["roller"]:
            if r not in roller:
                hatalar.append(f"profil {f.stem}: rol yok -> {r}")
        for x in p.get("ek_skiller", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"profil {f.stem}: skill yok -> {x}")
    # PROMPT UYUMU: promptlar/11 (başka projenin agent'ı) sabit bilgi içermez; her şeyi bu yapılardan okur.
    # Kütüphane ne kadar büyürse büyüsün bu sözleşme bozulmamalı.
    import re as _re
    p11 = KOK / "promptlar" / "11-guvenilir-skill-secimi-mevcut-proje.md"
    if p11.exists():
        for f in set(_re.findall(r"~/Documents/SkillKutuphanesi/([\w./-]+\.(?:md|json|py))", p11.read_text(encoding="utf-8"))):
            if not (KOK / f).exists():
                hatalar.append(f"prompt 11 olmayan dosyaya bakıyor: {f}")
    for s in skiller:  # prompt 11'deki kanıt sorgusunun okuduğu alanlar
        if not all(k in s for k in ("id", "ad", "durum", "degerlendirme", "ucret", "uyum", "yol", "repo", "teknoloji_oto")) \
                or "puan" not in s["degerlendirme"] or "codex" not in s["uyum"]:
            hatalar.append(f"prompt uyumu: {s['id']} kaydında kanıt alanı eksik (arsiv-yerlestir.py çalıştır)")
    gel = json_oku(KOK / "gelistiriciler.json", {"repolar": {}})
    guvensiz = sorted({s["repo"] for s in skiller if not (s.get("gelistirici") or {}).get("guven")})
    if guvensiz:
        uyarilar.append(f"prompt uyumu: kaynak güveni yok: {', '.join(guvensiz[:5])} -> gelistirici-bilgisi.py, arsiv-yerlestir.py, katalog-uret.py")
    rehber = KOK / "notlar" / "guven-siralamasi.md"
    if not rehber.exists():
        hatalar.append("prompt uyumu: notlar/guven-siralamasi.md yok -> katalog-uret.py")
    else:
        t = rehber.read_text(encoding="utf-8")
        for b in ("## 0.", "## 1.", "## 2.", "## 3.", "## 4."):
            if b not in t:
                hatalar.append(f"prompt uyumu: guven-siralamasi.md bölümü eksik: {b}")
        eksik_r = [r for r, v in gel["repolar"].items() if (v.get("guven") or {}).get("sira") or (v.get("guven") or {}).get("referans_sira")]
        eksik_r = [r for r in eksik_r if f"| {r} |" not in t]
        if eksik_r or gel.get("guncelleme", "") not in t:
            uyarilar.append(f"prompt uyumu: guven-siralamasi.md eski ({', '.join(eksik_r[:4]) or 'tarih'}) -> katalog-uret.py")
    # Prompt 11'in andığı komut bayrakları ve ön kontrol kodları skill-ekle.py'de gerçekten var mı? (yeniden adlandırma promptu sessizce bozmasın)
    if p11.exists():
        ptxt = p11.read_text(encoding="utf-8")
        ekle_kaynak = (KOK / "araclar" / "skill-ekle.py").read_text(encoding="utf-8")
        for bayrak in sorted(set(_re.findall(r"(?<![\w-])(--[a-z]+(?:-[a-z]+)*)", ptxt))):
            if bayrak not in ekle_kaynak and bayrak not in ("--porcelain", "--skip-git-repo-check"):
                hatalar.append(f"prompt 11 olmayan bayrağı anıyor: {bayrak} (skill-ekle.py)")
        kodlar04 = set(_re.findall(r"^\| `([a-z]+(?:-[a-z]+)+)` \|", (KOK / "rehber" / "04-kontrol-listesi.md").read_text(encoding="utf-8"), _re.M))
        for kod in sorted(set(_re.findall(r"`([a-z]+(?:-[a-z]+)+)`", ptxt)) & kodlar04):
            if kod not in ekle_kaynak:
                hatalar.append(f"prompt 11 olmayan ön kontrol kodunu anıyor: {kod} (skill-ekle.py)")
        for jeton in ("kaynak-yok", "emekli"):  # prompt 11 ADIM 10: --durum çıktısında geçmesi beklenen sözcükler
            if jeton in ptxt and jeton not in ekle_kaynak:
                hatalar.append(f"prompt 11 --durum çıktısında '{jeton}' bekliyor ama skill-ekle.py üretmiyor")
    rehber2 = KOK / "notlar" / "guven-siralamasi.md"
    if rehber2.exists() and "| Kart |" not in rehber2.read_text(encoding="utf-8"):
        hatalar.append("prompt uyumu: guven-siralamasi.md bölüm 3'te 'Kart' sütunu yok (prompt 11 ADIM 3 buna dayanır)")
    # Roldeki bir skill son kayıttan beri başka bir KAYNAĞA geçtiyse (öncelik/yeni kaynak yüzünden) fark edilsin
    git_eski = subprocess.run(["git", "show", "HEAD:registry.json"], cwd=KOK, capture_output=True, text=True)
    if git_eski.returncode == 0:
        try:
            eski_reg = {x["id"]: x["repo"] for x in json.loads(git_eski.stdout)["skiller"]}
            eski_tercih = {x["ad"]: x["repo"] for x in json.loads(git_eski.stdout)["skiller"] if x["durum"] == "tercih"}
            for f in sorted((KOK / "roller").glob("*.json")):
                r = json_oku(f)
                for x in r["cekirdek"] + r.get("opsiyonel", []):
                    simdi = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
                    once = eski_reg.get(x) or eski_tercih.get(x)
                    if simdi and once and simdi["repo"] != repo_guncel(once):  # repo taşınması (eski_adlar) kaynak değişimi değildir
                        uyarilar.append(f"rol {f.stem}: '{x}' kaynağı değişti ({once} -> {simdi['repo']}); rolün istediği sürüm bu mu? "
                                        "(sabitlemek için registry.json'da durum_elle)")
        except (ValueError, KeyError):
            pass
    kartlar = (KOK / "notlar" / "referans" / "tasarim-teknolojileri.md").read_text(encoding="utf-8") + \
        (KOK / "notlar" / "referans" / "kutuphaneler.md").read_text(encoding="utf-8")
    kartsiz = [k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T5", "T6")
               and f"`{k['repo']}`" not in kartlar and f"| {k['repo']} |" not in kartlar]
    if kartsiz:
        uyarilar.append(f"prompt uyumu: referans kütüphanesinin kartı/satırı yok: {', '.join(kartsiz[:5])} "
                        "-> notlar/referans/tasarim-teknolojileri.md (T6 kart) ya da kutuphaneler.md (T5 satır)")
    # Skillerin kendi .gitignore'u yüzünden git'e girmeyen arşiv dosyası var mı? (git yedeği eksik kalır)
    gi = subprocess.run(["git", "status", "--ignored", "--porcelain", "arsiv"], cwd=KOK, capture_output=True, text=True)
    from ortak import GURULTU
    for satir in gi.stdout.splitlines():
        if satir.startswith("!! ") and not GURULTU.search(satir[3:].rstrip("/")):
            hatalar.append(f"git'e girmeyen arşiv dosyası (skill'in kendi .gitignore'u): {satir[3:]} -> `git add -f arsiv`")
    if "--github" in sys.argv:
        r = subprocess.run(["gh", "api", "graphql", "--paginate", "-f",
                            "query=query($endCursor:String){viewer{starredRepositories(first:100,after:$endCursor)"
                            "{pageInfo{hasNextPage endCursor} nodes{nameWithOwner}}}}",
                            "--jq", ".data.viewer.starredRepositories.nodes[].nameWithOwner"],
                           capture_output=True, text=True)
        if r.returncode != 0 or not r.stdout.strip():
            uyarilar.append("GitHub yıldız listesi okunamadı (gh auth status?); yeni repo kontrolü YAPILMADI")
        # GitHub repo adları büyük/küçük harfe duyarsızdır (ör. LottieFiles/… ↔ lottiefiles/…): karşılaştırma küçük harfle
        tanimli = {k["repo"].lower() for k in json_oku(KAYNAKLAR)["repolar"]}
        # Skill listesindeki ('Yapay Zeka Skillleri') ama kütüphanede olmayan repolar: yeni eklenecek skill kaynakları
        hs = json_oku(KAYNAKLAR).get("github_skill_listesi", "yapay-zeka-skillleri")
        # Listedeki TÜM öğeler (GitHub sayfa başına 100 öğe verir; sayfalanmazsa yeni eklenen repolar kaçar)
        import importlib.util
        spec = importlib.util.spec_from_file_location("gsl", Path(__file__).parent / "github-skill-listesi.py")
        gsl = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gsl)
        try:
            liste_repolari = [x["nameWithOwner"] for l in gsl.listeler() if l["slug"] == hs for x in l["items"]["nodes"] if x]
        except RuntimeError:
            liste_repolari = []
            uyarilar.append("GitHub skill listesi okunamadı; YENİ SKILL REPOSU kontrolü YAPILMADI")
        for repo in liste_repolari:
            if repo.lower() not in tanimli:
                uyarilar.append(f"YENİ SKILL REPOSU (skill listesinde, kütüphanede yok): {repo} -> rehber/03-yeni-skill-ekleme.md")
        for repo in r.stdout.split():
            if repo.lower() not in tanimli:
                uyarilar.append(f"yıldızlı ama kaynaklar.json'da yok: {repo}")
    # Proje bilgisi tek yerde (notlar/proje-kullanimi.md): rapor güncel mi, kayıt dosyalarına proje adı sızmış mı?
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("projekullanimi", Path(__file__).parent / "proje-kullanimi.py")
        pk = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pk)
        ok, _n = pk.guncel_mi()
        if not ok:
            uyarilar.append("notlar/proje-kullanimi.md güncel değil (projelerde kurulu skiller değişmiş) -> python3 araclar/proje-kullanimi.py")
        ayar_p = json_oku(KOK / "projeler.json", {}) or {}
        if hasattr(pk, "hizli_kontrol"):
            for u in pk.hizli_kontrol(ayar_p):
                uyarilar.append(u)
        adlar_p = {p.name for p in pk.projeleri_bul(ayar_p)} | set(ayar_p.get("notlar", {})) \
            | set(ayar_p.get("bilinen_projeler", {})) | set(ayar_p.get("program_kullanimi", {})) \
            | set(ayar_p.get("kendi_skilleri", {})) \
            | {Path(y["yol"]).name for y in ayar_p.get("yoksay", []) if isinstance(y, dict) and y.get("yol")}
        skill_adlari = {s["ad"].lower() for s in skiller} | {s["repo"].split("/")[1].lower() for s in skiller}
        adlar_p = sorted(a for a in adlar_p if len(a) >= 5 and a.lower() not in skill_adlari)
        if adlar_p:
            desen = re.compile(r"(?<![\w-])(" + "|".join(re.escape(a) for a in adlar_p) + r")(?![\w-])")
            for dosya in ("kaynaklar.json", "registry.json", "ucret-siniflandirma.json", "kategori-kurallari.json", "programlar.json"):
                bulunan = sorted(set(desen.findall((KOK / dosya).read_text(encoding="utf-8"))))
                if bulunan:
                    uyarilar.append(f"{dosya}: kayıtta proje adı geçiyor ({', '.join(bulunan)}); değerlendirme projeden bağımsız "
                                    "yazılır, proje bilgisi projeler.json -> notlar'a taşınmalı (CLAUDE.md kural 6)")
    except Exception as e:  # noqa: BLE001
        uyarilar.append(f"proje kullanım denetimi çalışmadı: {e}")
    h2, u2 = belge_ve_kayit_denetimleri(skiller=skiller)
    hatalar += h2
    uyarilar += u2
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    print(f"{len(skiller)} skill · {len(hatalar)} hata · {len(uyarilar)} uyarı")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
