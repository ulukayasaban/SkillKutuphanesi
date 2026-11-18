#!/usr/bin/env python3
"""Kaynak boyutu hesabı (hiçbir şey kurulmaz, hiçbir dosya yazılmaz). notlar/plan-tur-surecleri.md bölüm 8.

  python3 araclar/boyut-hesapla.py owner/ad [--yol alt/klasor] [--json]     (ağ; yalnız okur)
  python3 araclar/boyut-hesapla.py --yerel <klasör> [--json]                (gerçek disk boyutu; karşılaştırma için)

Hesap:
  kutuphane_kb  = repo (ya da --yol) altındaki dosyaların boyutu, medya/ikili dosyalar HARİÇ (GitHub ağacındaki size).
  kurulum_mb    = repo toplamı + TAM bağımlılık listesi + sabit tablodaki indirmeler. Varsayılan geliştirme bağımlılıkları (dev) HARİÇ
                (--dev-yok); --dev ile başlık değer dev dahil olur. İki değer de her çıktıda görünür (kurulum_mb, kurulum_mb_devdahil).
                İçerikte (düzyazıda) anılan Hugging Face modelleri kurulum_mb'ye EKLENMEZ, bilgi olarak hesaplanamayan listesine yazılır.
Tam bağımlılık listesi (hiçbir şey kurulmaz; geçici klasör, iş bitince silinir):
  npm   : repoda package-lock.json varsa o; yoksa package.json geçici klasöre yazılıp `npm install --package-lock-only --ignore-scripts
          --no-audit --no-fund` (yalnız kilit üretir). Kilitteki her ad@sürümün boyutu npm kaydından (dist.unpackedSize); os/cpu alanı
          bu makineye uymayan isteğe bağlı paketler sayılmaz; aynı ad@sürüm bir kez.
  Python: `uv pip compile <dosyalar> --python-platform <bu makine> --python-version 3.12` (yalnız çözer, kurmaz). Her ad==sürümün macOS wheel boyutu PyPI'dan,
          x WHEEL_KATSAYISI. uv yoksa ya da çözüm başarısızsa eski tek düzey (doğrudan + requires_dist) yönteme düşülür, nedeni yazılır.
  Alt işlemler 180 sn ile sınırlı; hata ve zaman aşımı aracı çökertmez, hesaplanamayan'a yazılır.
Tarayıcı indirmesi: puppeteer-core / playwright-core indirmez; yalnız `puppeteer`, `playwright`, `@playwright/test` paketi ya da açık
`playwright install` / `remotion browser ensure` / `puppeteer browsers install` satırı sayılır (sabit tablo). Görülemeyenler her raporda yazılır: kurulum betiğinin ayrıca
kurduğu parçalar ve çalışırken inen modeller.
urllib kullanılır; her istek 15 sn zaman aşımlı. Ağ hatası aracı çökertmez.
"""
import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ortak  # noqa: E402

WHEEL_KATSAYISI = 3.7      # PyPI: kurulu boyut ~ wheel boyutu x katsayı (açılmış dosyalar, .pyc, dist-info). Tek sabit; 2026-11-18 sınaması: OpenMontage venv'inde çözümle kesişen 53 paketin kurulu/wheel oranı 3,66 (tüm venv 3,2).
ZAMAN_ASIMI = 15
KILIT_AZAMI = 60_000_000    # okunan en büyük package-lock.json (bayt)
ALT_ISLEM_ZAMAN_ASIMI = 180  # npm / uv alt işlemi
NPM_COZUM_AZAMI = 6        # tek çalıştırmada kilidi üretilen en çok package.json
COZUM_PYTHON = "3.12"       # uv çözümünde varsayılan Python sürümü (bu makinenin en yeni Python'u çoğu kitaplığın wheel'ini henüz taşımaz)
DEV_EKSTRALARI = ("dev", "test", "tests", "testing", "development")
IPUCU_DOSYA = 60           # ipucu için içeriği okunan dosya üst sınırı
BAGIMLILIK_DOSYA = 25      # okunan bağımlılık dosyası üst sınırı
NPM_ARALIK = 400           # tek çalıştırmada sorgulanan en çok npm/PyPI paketi (her iki düzey toplamı)
YOK_SAY = ("node_modules/", "/vendor/", "/test/", "/tests/", "/examples/", "/fixtures/")
# Sabit tablo (kaba, "sabit tablo" olarak işaretlenir): {desen: (ad, MB, açıklama)}
SABIT_TABLO = [   # metin satırlarında aranan AÇIK indirme komutları (düzyazıda anılan "remotion", "chromium" sayılmaz)
    (r"playwright\s+install", "playwright tarayıcıları (chromium)", 400),
    (r"remotion\s+browser\s+ensure", "Remotion Chrome Headless Shell", 150),
    (r"(?:@puppeteer/browsers|puppeteer\s+browsers)\s+install", "puppeteer indirdiği Chrome", 300),
]
# Paket olarak bağımlılık listesinde (npm ya da PyPI) bulunursa: ({paket adları}, ad, MB). *-core paketleri tarayıcı indirmez, listede yok.
SABIT_PAKET = [
    ({"puppeteer"}, "puppeteer indirdiği Chrome", 300),
    ({"playwright", "@playwright/test"}, "playwright tarayıcıları (chromium)", 400),
]
# Tarayıcılar aynı disk alanını paylaşır: eşleşenlerin yalnız en büyüğü kurulum_mb'ye eklenir (diğerleri listede kalır).
# torch yalnız bağımlılık olarak sayılmıyorsa tabloya girer (wheel PyPI'dan zaten sayılır)
SABIT_TORCH = (r"\btorch\b|\bpytorch\b", "torch (PyTorch)", 800)
IPUCU_ANAHTARLARI = [
    (r"huggingface\.co/([\w.-]+/[\w.-]+)", "hf"),
    (r"from_pretrained\(\s*[\"']([\w.-]+/[\w.-]+)[\"']", "hf"),
    (r"snapshot_download\([^)]*?repo_id\s*=\s*[\"']([\w.-]+/[\w.-]+)[\"']", "hf"),
    (r"\b(whisper|faster-whisper|faster_whisper)\b", "whisper"),
    (r"\b(torch|tensorflow|onnxruntime)\b", "ml-kutuphane"),
]


# ---------------------------------------------------------------- ağ yardımcıları
def http_json(url):
    """GET -> JSON ya da None (ağ/ayrıştırma hatasında)."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "skill-kutuphanesi"}), timeout=ZAMAN_ASIMI) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except (OSError, ValueError):
        return None


def npm_bilgi(ad):
    """{'kurulu': bayt, 'bagimlilik': [ad]} ya da None. dist.unpackedSize = açılmış paket boyutu."""
    d = http_json(f"https://registry.npmjs.org/{urllib.parse.quote(ad, safe='@')}/latest")
    if not isinstance(d, dict):
        return None
    boyut = (d.get("dist") or {}).get("unpackedSize")
    return {"kurulu": boyut if isinstance(boyut, int) else None, "bagimlilik": sorted((d.get("dependencies") or {}))}


HEDEF_PLATFORM = "macosx"   # kütüphanenin çalıştığı makine; wheel seçiminde ve ortam işaretlerinde (marker) bu platform esas alınır
HEDEF_MIMARI = {"amd64": "x86_64", "aarch64": "arm64"}.get(platform.machine().lower(), platform.machine().lower())   # x86_64 | arm64
_DIGER_PLATFORM = re.compile(r"""(platform_system|sys_platform|os_name)\s*==\s*['"](Linux|linux|win32|Windows|nt)['"]""")


def _wheel_uyumlu(ad):
    """wheel dosya adı hedef platformda (macOS, bu makinenin mimarisi; evrensel 'any' dahil) ve yaygın Python 3'te kurulabilir mi (kaba süzgeç)?"""
    m = re.match(r"^.+?-.+?(?:-\d[^-]*)?-([^-]+)-([^-]+)-([^-]+)\.whl$", ad)
    if not m:
        return False
    py, _abi, plat = m.groups()
    py_ok = any(t in py for t in ("py3", "cp310", "cp311", "cp312", "cp313", "cp3"))
    if not py_ok:
        return False
    if plat == "any":
        return True
    if HEDEF_PLATFORM not in plat:
        return False
    # macOS wheel'inde mimari: bu makinenin mimarisi, universal2 ya da (Intel makinede) eski 'intel'/'fat' etiketi
    return HEDEF_MIMARI in plat or "universal" in plat or (HEDEF_MIMARI == "x86_64" and ("intel" in plat or "fat" in plat))


def marker_hedefte_gecerli(gereksinim):
    """requires_dist satırındaki ortam işareti yalnız başka bir platformu (Linux, Windows) hedefliyorsa False."""
    isaret = gereksinim.split(";", 1)[1] if ";" in gereksinim else ""
    return not _DIGER_PLATFORM.search(isaret)


def _pypi_boyut(d):
    """PyPI JSON'undan en büyük uyumlu wheel boyutu; yoksa sdist; yoksa None."""
    urls = d.get("urls") or []
    wheeller = [u["size"] for u in urls if u.get("packagetype") == "bdist_wheel" and _wheel_uyumlu(u.get("filename", "")) and isinstance(u.get("size"), int)]
    sdist = [u["size"] for u in urls if u.get("packagetype") == "sdist" and isinstance(u.get("size"), int)]
    return max(wheeller) if wheeller else (max(sdist) if sdist else None)


def pypi_bilgi(ad):
    """{'wheel': bayt | None, 'bagimlilik': [ad]} ya da None. En büyük uyumlu wheel; yoksa sdist."""
    d = http_json(f"https://pypi.org/pypi/{urllib.parse.quote(ad)}/json")
    if not isinstance(d, dict):
        return None
    boyut = _pypi_boyut(d)
    bag = []
    for r in (d.get("info") or {}).get("requires_dist") or []:
        if "extra ==" in r or "extra==" in r or not marker_hedefte_gecerli(r):
            continue
        m = re.match(r"\s*([A-Za-z0-9][A-Za-z0-9._-]*)", r)
        if m:
            bag.append(m.group(1))
    return {"wheel": boyut, "bagimlilik": sorted(set(bag))}


def pypi_surum_boyut(ad, surum):
    """Belirli sürümün macOS wheel boyutu (bayt) ya da None."""
    d = http_json(f"https://pypi.org/pypi/{urllib.parse.quote(ad)}/{urllib.parse.quote(surum)}/json")
    return _pypi_boyut(d) if isinstance(d, dict) else None


def npm_surum_boyut(ad, surum):
    """Belirli sürümün açılmış boyutu (bayt, dist.unpackedSize) ya da None."""
    d = http_json(f"https://registry.npmjs.org/{urllib.parse.quote(ad, safe='@')}/{urllib.parse.quote(surum)}")
    b = ((d or {}).get("dist") or {}).get("unpackedSize") if isinstance(d, dict) else None
    return b if isinstance(b, int) else None


def hf_boyut(model_id):
    """Hugging Face model deposunun toplam dosya boyutu (bayt) ya da None."""
    d = http_json(f"https://huggingface.co/api/models/{model_id}?blobs=true")
    if not isinstance(d, dict):
        return None
    toplam = sum(s.get("size") or 0 for s in d.get("siblings") or [])
    return toplam or None


def toplu(islev, adlar):
    """İşlevi adlara paralel uygular (8 iş parçacığı): {ad: sonuç}. Sıra ve sonuç eşlemesi korunur."""
    adlar = list(adlar)
    with ThreadPoolExecutor(8) as ex:
        return dict(zip(adlar, ex.map(islev, adlar)))


# ---------------------------------------------------------------- tam bağımlılık listesi (kurulmadan)
def _node_os():
    return {"darwin": "darwin", "linux": "linux", "win32": "win32"}.get(sys.platform, sys.platform)


def _node_cpu():
    return {"x86_64": "x64", "arm64": "arm64"}.get(HEDEF_MIMARI, HEDEF_MIMARI)


def _liste_uyar(deger, hedef):
    """npm os/cpu alanı: ['darwin', '!win32'] biçimi. Alan yoksa her yerde kurulur."""
    if not deger:
        return True
    if isinstance(deger, str):
        deger = [deger]
    poz = [x for x in deger if not x.startswith("!")]
    if hedef in [x[1:] for x in deger if x.startswith("!")]:
        return False
    return (hedef in poz) if poz else True


def kilit_paketleri(kilit, os_ad=None, cpu=None, notlar=None):
    """package-lock.json (v2/v3) içeriğinden {(ad, sürüm): dev_mi}. Yalnız bu makineye uyan paketler (os/cpu alanı);
    çalışma alanı bağları ve paketin içine gömülü (inBundle) bağımlılıklar sayılmaz. dev_mi: yalnız geliştirmede gereken."""
    os_ad, cpu = os_ad or _node_os(), cpu or _node_cpu()
    paketler, atlanan = {}, 0
    for anahtar, e in (kilit.get("packages") or {}).items():
        if not anahtar or "node_modules/" not in anahtar or not isinstance(e, dict) or e.get("link") or e.get("inBundle"):
            continue
        ad = e.get("name") or anahtar.rsplit("node_modules/", 1)[1]
        surum = e.get("version")
        cozum = str(e.get("resolved") or "")
        if not surum or (cozum and not cozum.startswith(("http://", "https://"))):
            atlanan += 1
            continue
        if not (_liste_uyar(e.get("os"), os_ad) and _liste_uyar(e.get("cpu"), cpu)):
            continue
        k = (ad, surum)
        paketler[k] = paketler.get(k, True) and bool(e.get("dev"))
    if atlanan and notlar is not None:
        notlar.append(f"kilitte {atlanan} paket kayıt dışı kaynaktan (git/dosya): boyutu sayılmadı")
    return paketler


def npm_kilit_uret(paket_json_metni, calistir=subprocess.run, npm_yolu=None):
    """package.json'dan kilit üretir (paket İNDİRMEZ, betik ÇALIŞTIRMAZ). Geçici klasör `finally` ile silinir.
    Döner: (kilit sözlüğü | None, [not])."""
    npm = npm_yolu or shutil.which("npm")
    if not npm:
        return None, ["npm bulunamadı: tek düzey yönteme düşüldü"]
    try:
        d = json.loads(paket_json_metni)
    except ValueError:
        return None, ["package.json okunamadı: tek düzey yönteme düşüldü"]
    yeni = {"name": "boyut-hesabi", "version": "0.0.0", "private": True}
    for bolum in ("dependencies", "devDependencies", "optionalDependencies"):
        yeni[bolum] = {k: v for k, v in (d.get(bolum) or {}).items()
                       if isinstance(v, str) and not v.startswith(("workspace:", "file:", "link:", "git", "http", "github:"))}
    tmp = tempfile.mkdtemp(prefix="boyut-npm-")
    try:
        Path(tmp, "package.json").write_text(json.dumps(yeni), encoding="utf-8")
        try:
            r = calistir([npm, "install", "--package-lock-only", "--ignore-scripts", "--no-audit", "--no-fund", "--loglevel=error"],
                         cwd=tmp, capture_output=True, text=True, timeout=ALT_ISLEM_ZAMAN_ASIMI)
        except subprocess.TimeoutExpired:
            return None, [f"npm kilit üretimi {ALT_ISLEM_ZAMAN_ASIMI} sn'de bitmedi: tek düzey yönteme düşüldü"]
        except OSError as e:
            return None, [f"npm çalıştırılamadı ({e}): tek düzey yönteme düşüldü"]
        kilit_yolu = Path(tmp, "package-lock.json")
        if r.returncode or not kilit_yolu.exists():
            return None, [f"npm kilit üretimi başarısız (çıkış {r.returncode}: {(r.stderr or '').strip()[-160:]}): tek düzey yönteme düşüldü"]
        try:
            return json.loads(kilit_yolu.read_text(encoding="utf-8")), []
        except ValueError:
            return None, ["üretilen package-lock.json okunamadı: tek düzey yönteme düşüldü"]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def py_dev_dosyasi(yol):
    """requirements-dev.txt, requirements_test.txt gibi geliştirme dosyaları."""
    ad = yol.rsplit("/", 1)[-1].lower()
    return bool(re.fullmatch(r"requirements[\w.-]*\.txt", ad)) and bool(re.search(r"dev|test|lint|doc", ad[len("requirements"):]))


def py_dev_ekstralari(metin):
    """pyproject.toml optional-dependencies içinde geliştirme sayılan ekstra adları."""
    try:
        d = tomllib.loads(metin)
    except (tomllib.TOMLDecodeError, ValueError):
        return []
    return [k for k in ((d.get("project") or {}).get("optional-dependencies") or {}) if k.lower() in DEV_EKSTRALARI]


def _uv_platformu():
    if sys.platform == "darwin":
        return {"x86_64": "x86_64-apple-darwin", "arm64": "aarch64-apple-darwin"}.get(HEDEF_MIMARI)
    return None


def uv_coz(girdiler, dev=False, calistir=subprocess.run, uv_yolu=None):
    """girdiler: [(yol, metin)] (requirements*.txt / pyproject.toml). `uv pip compile` ile TAM çözülmüş liste (kurmaz, derlemez:
    --no-build, kaynak paketlerin kurulum betiği çalıştırılmaz). dev=True: pyproject'ta dev ekstraları da dahil.
    Döner: ([(ad, sürüm)] | None, [not]). Başarısızlıkta liste None, nedeni notta."""
    uv = uv_yolu or shutil.which("uv")
    if not uv:
        return None, ["uv bulunamadı: tek düzey yönteme düşüldü"]
    tmp = tempfile.mkdtemp(prefix="boyut-uv-")
    notlar = []
    try:
        yollar, ekstra = [], []
        for i, (yol, metin) in enumerate(girdiler):
            klasor = Path(tmp, f"d{i}")
            klasor.mkdir()
            ad = yol.rsplit("/", 1)[-1]
            if ad.lower() == "pyproject.toml":
                if dev:
                    for x in py_dev_ekstralari(metin):
                        ekstra += ["--extra", x]
            else:
                satirlar = metin.splitlines()
                temiz = [x for x in satirlar if not x.strip() or x.lstrip().startswith("#") or paket_adi(x)]
                dusen = sum(1 for x in satirlar if x.strip() and not x.lstrip().startswith("#") and not paket_adi(x))
                if dusen:
                    notlar.append(f"{yol}: {dusen} satır (-r, -e, URL, yerel yol, seçenek) çözümde yok")
                metin = "\n".join(temiz) + "\n"
            (klasor / ad).write_text(metin, encoding="utf-8")
            yollar.append(str(klasor / ad))
        komut = [uv, "pip", "compile", *yollar, "--quiet", "--no-header", "--no-annotate", "--no-build", "--python-version", COZUM_PYTHON,
                 *ekstra]   # çıktı stdout'a: `-o -` "-" adlı DOSYA yazar
        plat = _uv_platformu()
        if plat:
            komut += ["--python-platform", plat]
        try:
            r = calistir(komut, cwd=tmp, capture_output=True, text=True, timeout=ALT_ISLEM_ZAMAN_ASIMI)
        except subprocess.TimeoutExpired:
            return None, [f"uv çözümü {ALT_ISLEM_ZAMAN_ASIMI} sn'de bitmedi: tek düzey yönteme düşüldü"]
        except OSError as e:
            return None, [f"uv çalıştırılamadı ({e}): tek düzey yönteme düşüldü"]
        if r.returncode:
            return None, [f"uv çözümü başarısız (çıkış {r.returncode}: {(r.stderr or '').strip()[-200:]}): tek düzey yönteme düşüldü"]
        return uv_cikti_ayristir(r.stdout), notlar
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def uv_cikti_ayristir(metin):
    """`uv pip compile` çıktısı -> [(ad, sürüm)] (sıralı, tekrarsız)."""
    sonuc = set()
    for satir in metin.splitlines():
        m = re.match(r"^([A-Za-z0-9][A-Za-z0-9._-]*)==([^\s;#]+)", satir)
        if m:
            sonuc.add((m.group(1).lower().replace("_", "-"), m.group(2)))
    return sorted(sonuc)


def _surum_boyutlari(anahtarlar, getir, etiket, hesaplanamayan):
    """{(ad, sürüm): bayt}. Aynı ad@sürüm bir kez sorgulanır (paralel, 16 iş parçacığı); bulunamayanlar tek satırda not edilir."""
    anahtarlar = sorted(set(anahtarlar))
    with ThreadPoolExecutor(16) as ex:
        sonuc = dict(zip(anahtarlar, ex.map(lambda k: getir(*k), anahtarlar)))
    eksik = [f"{a}@{v}" for (a, v), b in sonuc.items() if b is None]
    if eksik:
        hesaplanamayan.append(f"{etiket} paketi boyutu alınamadı ({len(eksik)}): " + ", ".join(eksik[:10]) + (" ..." if len(eksik) > 10 else ""))
    return {k: b for k, b in sonuc.items() if b is not None}


# ---------------------------------------------------------------- saf işlevler (test edilebilir)
def agac_boyutu(agac, yol=None):
    """(toplam_bayt, medya_bayt, dosya_sayisi, boyutsuz_dosya). `yol` verilirse yalnız o klasörün altı."""
    on = (yol.strip("/") + "/") if yol else ""
    toplam = medya = say = boyutsuz = 0
    for x in agac:
        if x["type"] != "blob" or (on and not x["path"].startswith(on)):
            continue
        b = x.get("size")
        say += 1
        if b is None:
            boyutsuz += 1
            continue
        toplam += b
        if ortak.medya_mi(x["path"]):
            medya += b
    return toplam, medya, say, boyutsuz


def paket_adi(satir):
    """requirements satırından paket adı ya da None (yorum, -r, -e, URL, yerel yol atlanır)."""
    s = satir.split("#", 1)[0].strip()
    if not s or s.startswith(("-", ".", "/")) or "://" in s or s.startswith("git+"):
        return None
    m = re.match(r"([A-Za-z0-9][A-Za-z0-9._-]*)", s)
    return m.group(1).lower().replace("_", "-") if m else None


def bagimliliklar(yol, metin, dev=True):
    """Bağımlılık dosyasından ('npm'|'pypi', [paket adları]). Tanınmayan dosya -> (None, []).
    dev=False: package.json devDependencies alınmaz (yayınlanan paketi kuran kişiye inmez)."""
    ad = yol.rsplit("/", 1)[-1].lower()
    if ad == "package.json":
        try:
            d = json.loads(metin)
        except ValueError:
            return "npm", []
        paketler = []
        for bolum in ("dependencies", "devDependencies") if dev else ("dependencies",):
            for k, v in (d.get(bolum) or {}).items():
                if isinstance(v, str) and not v.startswith(("workspace:", "file:", "link:", "git", "http", "github:", "npm:")):
                    paketler.append(k)
        return "npm", sorted(set(paketler))
    if re.fullmatch(r"requirements[\w.-]*\.txt", ad):
        if not dev and py_dev_dosyasi(yol):
            return "pypi", []
        return "pypi", sorted({p for p in map(paket_adi, metin.splitlines()) if p})
    if ad == "pyproject.toml":
        try:
            d = tomllib.loads(metin)
        except (tomllib.TOMLDecodeError, ValueError):
            return "pypi", []
        liste = list((d.get("project") or {}).get("dependencies") or [])
        for kume in ((d.get("tool") or {}).get("poetry") or {}).get("dependencies", {}):
            if kume.lower() != "python":
                liste.append(kume)
        return "pypi", sorted({p for p in map(paket_adi, liste) if p})
    return None, []


def ipuclari(metinler, pypi_paketleri=(), paket_adlari=()):
    """Metinlerde model/tarayıcı ipuçları. Döner: [{ad, tur ('sabit'|'hf'|'bilinmeyen'), mb | model_id}]. Tekrarsız.
    paket_adlari: çözülmüş bağımlılık adları (npm + PyPI); SABIT_PAKET bunlara bakar (puppeteer-core, playwright-core sayılmaz)."""
    sonuc, gorulen = [], set()
    birlesik = "\n".join(metinler)
    adlar = {a.lower() for a in paket_adlari}
    for kume, ad, mb in SABIT_PAKET:
        if adlar & kume and ad not in gorulen:
            gorulen.add(ad)
            sonuc.append({"ad": ad, "tur": "sabit", "mb": mb})
    for desen, ad, mb in SABIT_TABLO:
        if re.search(desen, birlesik, re.I) and ad not in gorulen:
            gorulen.add(ad)
            sonuc.append({"ad": ad, "tur": "sabit", "mb": mb})
    if re.search(SABIT_TORCH[0], birlesik, re.I) and "torch" not in pypi_paketleri:
        sonuc.append({"ad": SABIT_TORCH[1], "tur": "sabit", "mb": SABIT_TORCH[2]})
    for desen, tur in IPUCU_ANAHTARLARI:
        for m in re.finditer(desen, birlesik, re.I):
            if tur == "hf":
                mid = m.group(1).rstrip(".,)")
                if "/" in mid and mid not in gorulen and not mid.lower().startswith(("spaces/", "datasets/", "docs/", "api/", "blog/")):
                    gorulen.add(mid)
                    sonuc.append({"ad": f"Hugging Face modeli {mid}", "tur": "hf", "model_id": mid})
            elif tur == "whisper" and "whisper" not in gorulen:
                gorulen.add("whisper")
                sonuc.append({"ad": "whisper modeli (boyut seçilen modele bağlı)", "tur": "bilinmeyen"})
    return sonuc


def _duzeyli(adlar, getir, alan, etiket, hesaplanamayan, ad_duzelt=lambda x: x):
    """Doğrudan paketler + onların doğrudan bağımlılıkları (2 düzey). Döner: (sayılan paket, toplam bayt, {paket: bayt})."""
    boyutlar = {}
    adlar = adlar[:NPM_ARALIK]
    ilk = toplu(getir, adlar)
    ikinci = set()
    bayt = say = 0
    for ad in adlar:
        b = ilk[ad]
        if b is None or b.get(alan) is None:
            hesaplanamayan.append(f"{etiket} paketi boyutu alınamadı: {ad}")
        else:
            bayt += b[alan]
            say += 1
            boyutlar[ad] = b[alan]
        if b:
            ikinci.update(ad_duzelt(x) for x in b.get("bagimlilik") or [])
    ikinci = sorted(ikinci - set(adlar))[:max(0, NPM_ARALIK - len(adlar))]
    for ad, b in toplu(getir, ikinci).items():
        if b and b.get(alan) is not None:
            bayt += b[alan]
            say += 1
            boyutlar[ad] = b[alan]
        else:
            hesaplanamayan.append(f"{etiket} bağımlılığı (2. düzey) boyutu alınamadı: {ad}")
    return say, bayt, boyutlar


def hesapla(agac, dosya_metinleri, npm_getir=npm_bilgi, pypi_getir=pypi_bilgi, hf_getir=hf_boyut, yol=None,
            npm_coz=npm_kilit_uret, py_coz=uv_coz, npm_boyut=npm_surum_boyut, pypi_boyut=pypi_surum_boyut):
    """Saf toplama (ağ ve alt işlem işlevleri enjekte edilir). dosya_metinleri: {yol: metin} (package.json, package-lock.json, requirements*.txt,
    pyproject.toml, README...). npm_coz(package.json metni) -> (kilit | None, [not]); py_coz([(yol, metin)], dev) -> ([(ad, sürüm)] | None, [not]).
    Çözüm başarısızsa o parça eski tek düzey yöntemle (npm_getir / pypi_getir) sayılır, nedeni hesaplanamayan'a yazılır.
    Döner: {kutuphane_kb, kurulum_mb (dev hariç), hesaplanamayan, ayrinti: {..., kurulum_mb_devdahil}}."""
    toplam, medya, say, boyutsuz = agac_boyutu(agac, yol)
    hesaplanamayan = []
    if boyutsuz:
        hesaplanamayan.append(f"{boyutsuz} dosyanın boyutu okunamadı (git kipi)")
    ayr = {"repo_mb": round(toplam / 1048576, 2), "medya_mb": round(medya / 1048576, 2), "dosya": say,
           "npm_paket": 0, "npm_mb": 0.0, "npm_dev_paket": 0, "npm_dev_mb": 0.0,
           "pypi_paket": 0, "pypi_wheel_mb": 0.0, "pypi_kurulu_mb": 0.0, "pypi_dev_paket": 0, "pypi_dev_kurulu_mb": 0.0,
           "indirme_mb": 0.0, "cozum": {}}
    kurulum = toplam / 1048576
    paket_adlari = set()

    # ---- npm
    pkg_dosyalari = sorted((y for y in dosya_metinleri if y.rsplit("/", 1)[-1].lower() == "package.json"), key=lambda y: (y.count("/"), y))
    npm_prod, npm_dev, tek_prod, tek_dev, yontem, cozulen = {}, {}, set(), set(), set(), 0
    for y in pkg_dosyalari:
        metin = dosya_metinleri[y]
        kok = y.rpartition("/")[0]
        kilit_yolu = (kok + "/" if kok else "") + "package-lock.json"
        kilit = None
        if kilit_yolu in dosya_metinleri:
            try:
                kilit = json.loads(dosya_metinleri[kilit_yolu])
                yontem.add("repodaki package-lock.json")
            except ValueError:
                hesaplanamayan.append(f"{kilit_yolu} okunamadı: kilit üretilecek")
        if kilit is None and cozulen < NPM_COZUM_AZAMI:
            cozulen += 1
            kilit, notlar = npm_coz(metin)
            hesaplanamayan.extend(notlar)
            if kilit is not None:
                yontem.add("npm install --package-lock-only")
        elif kilit is None:
            hesaplanamayan.append(f"{y}: en çok {NPM_COZUM_AZAMI} package.json'un kilidi üretilir; bu dosya tek düzey sayıldı")
        if kilit is not None:
            notlar = []
            for k, dev in kilit_paketleri(kilit, notlar=notlar).items():
                (npm_dev if dev else npm_prod)[k] = True
            hesaplanamayan.extend(n for n in notlar if n not in hesaplanamayan)
        else:
            yontem.add("tek düzey (doğrudan + 1 düzey)")
            tek_prod.update(bagimliliklar(y, metin, dev=False)[1])
            tek_dev.update(set(bagimliliklar(y, metin)[1]) - set(bagimliliklar(y, metin, dev=False)[1]))
    for k in list(npm_dev):
        if k in npm_prod:
            del npm_dev[k]                       # bir yerde üretimde gerekiyorsa dev sayılmaz
    paket_adlari.update(a for a, _ in list(npm_prod) + list(npm_dev))
    npm_bayt = npm_dev_bayt = 0
    if npm_prod or npm_dev:
        boy = _surum_boyutlari(list(npm_prod) + list(npm_dev), npm_boyut, "npm", hesaplanamayan)
        ayr["npm_paket"], npm_bayt = sum(1 for k in npm_prod if k in boy), sum(boy.get(k, 0) for k in npm_prod)
        ayr["npm_dev_paket"], npm_dev_bayt = sum(1 for k in npm_dev if k in boy), sum(boy.get(k, 0) for k in npm_dev)
        en_buyuk = {f"{a}@{v}": b for (a, v), b in boy.items()}
    else:
        en_buyuk = {}
    if tek_prod or tek_dev:
        say1, bayt1, boy1 = _duzeyli(sorted(tek_prod), npm_getir, "kurulu", "npm", hesaplanamayan)
        ayr["npm_paket"] += say1
        npm_bayt += bayt1
        paket_adlari.update(boy1)
        if tek_prod:
            hesaplanamayan.append("npm geçişli bağımlılıklar 2. düzeyin ötesinde sayılmadı (kilit çıkarılamadı); platforma özel ikili paketler eksik olabilir")
        if tek_dev:
            say2, bayt2, _ = _duzeyli(sorted(tek_dev - tek_prod), npm_getir, "kurulu", "npm (devDependencies)", hesaplanamayan)
            ayr["npm_dev_paket"] += say2
            npm_dev_bayt += bayt2
        en_buyuk.update(boy1)
    ayr["npm_mb"], ayr["npm_dev_mb"] = round(npm_bayt / 1048576, 2), round(npm_dev_bayt / 1048576, 2)
    if yontem:
        ayr["cozum"]["npm"] = " + ".join(sorted(yontem))

    # ---- Python
    py_dosyalar = [(y, m) for y, m in dosya_metinleri.items() if bagimliliklar(y, m)[0] == "pypi" and y.rsplit("/", 1)[-1].lower() != "readme.md"]
    py_prod_d = [(y, m) for y, m in py_dosyalar if not py_dev_dosyasi(y)]
    py_dev_d = [(y, m) for y, m in py_dosyalar if py_dev_dosyasi(y)]
    py_prod = py_dev = None
    py_wheel = {}
    py_tek_adlar = {x for y, m in py_prod_d for x in bagimliliklar(y, m, dev=False)[1]}
    if py_dosyalar:
        liste, notlar = py_coz(py_prod_d, False) if py_prod_d else ([], [])
        hesaplanamayan.extend(notlar)
        if liste is not None:
            py_prod = set(liste)
            ayr["cozum"]["pypi"] = "uv pip compile (tam çözüm, kurulmadan)"
            if py_dev_d or any(py_dev_ekstralari(m) for y, m in py_prod_d if y.rsplit("/", 1)[-1].lower() == "pyproject.toml"):
                tum, n2 = py_coz(py_prod_d + py_dev_d, True)
                hesaplanamayan.extend(n for n in n2 if n not in hesaplanamayan)
                py_dev = (set(tum) - py_prod) if tum is not None else set()
        if py_prod is None:
            ayr["cozum"]["pypi"] = "tek düzey (doğrudan + requires_dist)"
    if py_prod is not None:
        paket_adlari.update(a for a, _ in py_prod | (py_dev or set()))
        boy = _surum_boyutlari(list(py_prod | (py_dev or set())), pypi_boyut, "PyPI", hesaplanamayan)
        py_bayt = sum(boy.get(k, 0) for k in py_prod)
        py_dev_bayt = sum(boy.get(k, 0) for k in (py_dev or ()))
        ayr["pypi_paket"], ayr["pypi_dev_paket"] = sum(1 for k in py_prod if k in boy), sum(1 for k in (py_dev or ()) if k in boy)
        en_buyuk.update({f"{a}=={v}": b for (a, v), b in boy.items()})
    elif py_tek_adlar:
        say3, py_bayt, boy3 = _duzeyli(sorted(py_tek_adlar), pypi_getir, "wheel", "PyPI", hesaplanamayan,
                                       ad_duzelt=lambda x: x.lower().replace("_", "-"))
        py_dev_bayt = 0
        ayr["pypi_paket"] = say3
        paket_adlari.update(boy3)
        hesaplanamayan.append("PyPI geçişli bağımlılıklar 2. düzeyin ötesinde sayılmadı (uv çözümü yok); sürüm sabitleri ve ek paketler eksik olabilir")
        en_buyuk.update(boy3)
    else:
        py_bayt = py_dev_bayt = 0
    ayr["pypi_wheel_mb"] = round(py_bayt / 1048576, 2)
    ayr["pypi_kurulu_mb"] = round(py_bayt * WHEEL_KATSAYISI / 1048576, 2)
    ayr["pypi_dev_wheel_mb"] = round(py_dev_bayt / 1048576, 2)
    ayr["pypi_dev_kurulu_mb"] = round(py_dev_bayt * WHEEL_KATSAYISI / 1048576, 2)
    ayr["en_buyuk_paketler"] = sorted(en_buyuk.items(), key=lambda kv: -kv[1])[:8]

    # ---- model / tarayıcı ipuçları
    indirme = 0.0
    ip = ipuclari(list(dosya_metinleri.values()), {a for a, _ in (py_prod or set())} | py_tek_adlar, paket_adlari)
    sabitler = [x for x in ip if x["tur"] == "sabit" and x["ad"] != SABIT_TORCH[1]]
    en_buyuk_tarayici = max(sabitler, key=lambda x: x["mb"], default=None)
    for x in ip:
        if x["tur"] == "sabit":
            x["not"] = "sabit tablo"
            if x["ad"] == SABIT_TORCH[1] or x is en_buyuk_tarayici:
                indirme += x["mb"]
            else:
                x["not"] += "; tarayıcı grubunda en büyüğü sayıldı, bu sayılmadı"
        elif x["tur"] == "hf":
            # Düzyazıda anılan model gerçekten inecek mi bilinmez: boyutu bulunursa bilgi olarak yazılır, kurulum_mb'ye EKLENMEZ.
            b = hf_getir(x["model_id"])
            if b:
                x["mb"] = round(b / 1048576, 1)
                x["not"] = "olası indirme, kurulum_mb'ye eklenmedi"
                hesaplanamayan.append(f"olası model indirmesi (içerikte anılıyor, gerçekten inip inmediği bilinmiyor): {x['model_id']} ~{x['mb']} MB")
            else:
                hesaplanamayan.append(f"model boyutu bulunamadı: {x['model_id']}")
        else:
            hesaplanamayan.append(x["ad"])
    ayr["indirme_mb"] = round(indirme, 1)
    ayr["ipuclari"] = ip
    if ayr["npm_dev_paket"] or ayr["pypi_dev_paket"]:
        hesaplanamayan.append(f"geliştirme bağımlılıkları kurulum_mb'ye SAYILMADI: npm {ayr['npm_dev_paket']} paket ~{ayr['npm_dev_mb']} MB, "
                              f"PyPI {ayr['pypi_dev_paket']} paket ~{ayr['pypi_dev_kurulu_mb']} MB (kurulum_mb_devdahil'e dahil)")
    hesaplanamayan.append("hesabın göremediği: bağımlılık listesinde olmayıp kurulum betiğiyle ayrıca kurulan parçalar ve çalışırken inen modeller")
    kurulum += npm_bayt / 1048576 + py_bayt * WHEEL_KATSAYISI / 1048576 + indirme
    ayr["kurulum_mb_devdahil"] = round(kurulum + ayr["npm_dev_mb"] + ayr["pypi_dev_kurulu_mb"], 1)  # repo klonlanıp kurulursa (program/kit)
    return {"kutuphane_kb": round((toplam - medya) / 1024), "kurulum_mb": round(kurulum, 1),
            "hesaplanamayan": hesaplanamayan, "tarih": date.today().isoformat(), "ayrinti": ayr}


# ---------------------------------------------------------------- yerel disk (karşılaştırma)
def yerel_boyut(klasor):
    """du benzeri gerçek disk boyutu: symlink izlenmez (bağın kendisi sayılır), sabit bağlar bir kez. Döner sözlük (MB)."""
    kok = Path(klasor).expanduser()
    gorulen, disk, gorunen, medya, say = set(), 0, 0, 0, 0
    buyukler = {}
    for yol, dizinler, dosyalar in os.walk(kok, followlinks=False):
        for ad in dosyalar + dizinler:
            p = os.path.join(yol, ad)
            try:
                st = os.lstat(p)
            except OSError:
                continue
            if st.st_nlink > 1 and (st.st_dev, st.st_ino) in gorulen:
                continue
            gorulen.add((st.st_dev, st.st_ino))
            disk += st.st_blocks * 512
            if os.path.isdir(p) and not os.path.islink(p):
                continue
            gorunen += st.st_size
            say += 1
            if ortak.medya_mi(p):
                medya += st.st_size
            ust = os.path.relpath(p, kok).split(os.sep)[0]
            buyukler[ust] = buyukler.get(ust, 0) + st.st_blocks * 512
    ust_liste = sorted(buyukler.items(), key=lambda kv: -kv[1])[:8]
    return {"klasor": str(kok), "disk_mb": round(disk / 1048576, 1), "gorunen_mb": round(gorunen / 1048576, 1),
            "medya_mb": round(medya / 1048576, 1), "gorunen_bayt": gorunen, "medya_bayt": medya, "dosya": say,
            "en_buyuk_ust_girdiler": [{"ad": k, "mb": round(v / 1048576, 1)} for k, v in ust_liste]}


# ---------------------------------------------------------------- ağ kipi
def repo_hesapla(repo, yol=None):
    sha, govde = ortak.repo_agaci(repo)
    agac = govde["tree"]
    on = (yol.strip("/") + "/") if yol else ""
    dosyalar = [x["path"] for x in agac if x["type"] == "blob" and x["path"].startswith(on)
                and not any(k in "/" + x["path"] for k in YOK_SAY)]
    bag = [p for p in dosyalar if bagimliliklar(p, "")[0] is not None or p.rsplit("/", 1)[-1].lower() in ("package.json", "pyproject.toml")]
    bag = sorted(bag, key=lambda p: (p.count("/"), p))[:BAGIMLILIK_DOSYA]
    # package.json ile aynı klasördeki package-lock.json (büyük olabilir: ayrı ve geniş okunur)
    kilitler = [p for p in dosyalar if p.rsplit("/", 1)[-1] == "package-lock.json"
                and (p.rpartition("/")[0] + "/package.json").lstrip("/") in bag]
    oncelik = [p for p in dosyalar if re.search(r"(^|/)(README[\w.-]*\.md|SKILL\.md|Makefile|Dockerfile|install[\w.-]*\.(sh|py|ps1)|setup[\w.-]*\.(sh|py)|"
                                                 r"[\w.-]*preflight[\w.-]*\.py)$", p, re.I)]
    oncelik = sorted(oncelik, key=lambda p: (p.count("/"), p))
    okunacak = list(dict.fromkeys(bag + oncelik))[:BAGIMLILIK_DOSYA + IPUCU_DOSYA]
    with ThreadPoolExecutor(8) as ex:
        metinler = list(ex.map(lambda p: ortak.ham_metin(repo, p, sha, 300_000), okunacak))
    icerik = {p: m for p, m in zip(okunacak, metinler) if m}
    for p in kilitler[:NPM_COZUM_AZAMI]:
        m = ortak.ham_metin(repo, p, sha, KILIT_AZAMI)
        if m and len(m) < KILIT_AZAMI:       # kesilmiş kilit geçerli JSON olamaz: üretilecek
            icerik[p] = m
    ortak.klon_temizle(govde)
    r = hesapla(agac, icerik, yol=yol)
    ayni = len(okunacak) - sum(1 for p in okunacak if p in icerik)
    if ayni:
        r["hesaplanamayan"].append(f"{ayni} dosya okunamadı (bağımlılık/ipucu taraması eksik olabilir)")
    r["repo"], r["commit"], r["yol"] = repo, sha, yol
    r["okunan_dosya"] = sorted(icerik)
    return r


def yaz(r, dev=False):
    a = r["ayrinti"]
    print(f"{r['repo']}{(' / ' + r['yol']) if r.get('yol') else ''}  (commit {str(r['commit'])[:9]})")
    print(f"  kutuphane_kb : {r['kutuphane_kb']:,} KB  (medyasız; medya {a['medya_mb']} MB ayrı)")
    print(f"  kurulum_mb   : {a['kurulum_mb_devharic']:,} MB  geliştirme bağımlılıkları HARİÇ" + ("" if not dev else "  (başlık değer: --dev)"))
    print(f"  kurulum_mb   : {a['kurulum_mb_devdahil']:,} MB  geliştirme bağımlılıkları DAHİL (kit / klonlanıp kurulan program için bu değer yazılır)"
          + ("  (başlık değer)" if dev else ""))
    print(f"    repo {a['repo_mb']} MB ({a['dosya']} dosya) + npm {a['npm_mb']} MB ({a['npm_paket']} paket; dev {a['npm_dev_paket']} paket {a['npm_dev_mb']} MB) + "
          f"PyPI {a['pypi_kurulu_mb']} MB (wheel {a['pypi_wheel_mb']} MB x {WHEEL_KATSAYISI}, {a['pypi_paket']} paket; dev {a['pypi_dev_paket']} paket "
          f"{a['pypi_dev_kurulu_mb']} MB) + indirmeler {a['indirme_mb']} MB")
    print("    çözüm: " + (", ".join(f"{k}: {v}" for k, v in a["cozum"].items()) or "bağımlılık dosyası yok"))
    print("    en büyük paketler: " + ", ".join(f"{k} {v / 1048576:.0f} MB" for k, v in a.get("en_buyuk_paketler", [])))
    for x in a["ipuclari"]:
        print(f"    ipucu: {x['ad']}" + (f" ~{x['mb']} MB" if "mb" in x else "") + (f" [{x['not']}]" if x.get("not") else ""))
    print(f"  hesaplanamayan ({len(r['hesaplanamayan'])}):")
    for h in r["hesaplanamayan"][:25]:
        print(f"    - {h}")
    if len(r["hesaplanamayan"]) > 25:
        print(f"    ... +{len(r['hesaplanamayan']) - 25}")


def main():
    ap = argparse.ArgumentParser(description="Kaynak boyut hesabı (yalnız okur)")
    ap.add_argument("repo", nargs="?", help="owner/ad")
    ap.add_argument("--yol", help="reponun alt klasörü")
    ap.add_argument("--yerel", help="gerçek disk boyutu (ağ yok)")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dev", action="store_true", help="başlık kurulum_mb geliştirme bağımlılıkları dahil (kit / klonlanıp kurulan program)")
    g.add_argument("--dev-yok", action="store_true", help="başlık kurulum_mb dev hariç (varsayılan)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if bool(a.repo) == bool(a.yerel):
        print("owner/ad ya da --yerel <klasör> verilmeli (ikisi birden değil)", file=sys.stderr)
        return 2
    if a.yerel:
        r = yerel_boyut(a.yerel)
        print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else
              f"{r['klasor']}: disk {r['disk_mb']:,} MB, görünen {r['gorunen_mb']:,} MB, medya {r['medya_mb']} MB, {r['dosya']} dosya\n"
              + "\n".join(f"  {x['mb']:>9,} MB  {x['ad']}" for x in r["en_buyuk_ust_girdiler"]))
        return 0
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", a.repo):
        print("repo 'owner/ad' biçiminde olmalı", file=sys.stderr)
        return 2
    try:
        r = repo_hesapla(a.repo, a.yol)
    except (RuntimeError, OSError) as e:
        print(f"HATA: {a.repo} okunamadı: {e}", file=sys.stderr)
        return 2
    r["ayrinti"]["kurulum_mb_devharic"] = r["kurulum_mb"]
    if a.dev:
        r["kurulum_mb"] = r["ayrinti"]["kurulum_mb_devdahil"]
    if a.json:
        kayit = {k: r[k] for k in ("kutuphane_kb", "kurulum_mb", "hesaplanamayan", "tarih")}
        kayit["kurulum_mb_devharic"], kayit["kurulum_mb_devdahil"] = r["ayrinti"]["kurulum_mb_devharic"], r["ayrinti"]["kurulum_mb_devdahil"]
        print(json.dumps(kayit, ensure_ascii=False, indent=2))
    else:
        yaz(r, a.dev)
    return 0


if __name__ == "__main__":
    sys.exit(main())
