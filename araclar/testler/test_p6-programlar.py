#!/usr/bin/env python3
"""P6 testleri: araclar/program-denetim.py (kart şeması, ön kontrol, ağ sınıflaması, rapor uyumluluğu).
Yalnız geçici klasör ve sahte veri: gerçek ev klasörü, gerçek kütüphane kartları ve ağ kullanılmaz
(--ev/--kok/--yedek-koku geçici klasöre bakar; gh_api, urlopen, git_okuma, disk_usage sahtelenir).
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import re
import contextlib
import copy
import importlib.util
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import urllib.error
from datetime import date
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))
os.environ["GIT_CONFIG_GLOBAL"] = "/dev/null"
os.environ["GIT_CONFIG_NOSYSTEM"] = "1"

spec = importlib.util.spec_from_file_location("progden", ARACLAR / "program-denetim.py")
pd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pd)

TMP = Path(tempfile.mkdtemp(prefix="p6test-"))
gecen = toplam = 0


def test(ad, kosul, detay=""):
    global gecen, toplam
    toplam += 1
    if kosul:
        gecen += 1
    else:
        print(f"HATA: {ad} {str(detay)[:300]}")


@contextlib.contextmanager
def yama(**kw):
    """Modül özniteliklerini geçici değiştir ('urllib.request.urlopen' için nokta kullan)."""
    eski = []
    for ad, deger in kw.items():
        hedef, _, nitelik = ad.rpartition("__")
        nesne = pd
        for parca in (hedef.split("_dot_") if hedef else []):
            nesne = getattr(nesne, parca)
        eski.append((nesne, nitelik, getattr(nesne, nitelik)))
        setattr(nesne, nitelik, deger)
    try:
        yield
    finally:
        for nesne, nitelik, v in reversed(eski):
            setattr(nesne, nitelik, v)


def calistir(args):
    """main'i süreç içinde çalıştır: (çıkış, stdout, stderr)."""
    o, e = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e):
        try:
            kod = pd.main(args)
        except SystemExit as x:
            kod = x.code
    return kod, o.getvalue(), e.getvalue()


def klasor(ad):
    d = TMP / ad
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    return d


# ------------------------------------------------------------------ kart üretimi
SHA = "a" * 40
GECERLI_DEGER = {"ucret": "ucretsiz", "giris_yolu.hepsi.durum": "yok", "kutuphane_commit": SHA, "kutuphane_surumu": "1.2.0",
                 "yerinde.dal": "main"}


def doldur(v, ad, yol="", ek=None):
    ek = ek or {}
    if isinstance(v, dict):
        return {k: doldur(x, ad, f"{yol}.{k}" if yol else k, ek) for k, x in v.items()}
    if isinstance(v, list):
        return [doldur(x, ad, yol, ek) for x in v]
    if isinstance(v, str) and pd.YER_TUTUCU in v:
        if yol in ek:
            return ek[yol]
        if yol == "ad":
            return ad
        if yol == "repo":
            return f"o/{ad}"
        return GECERLI_DEGER.get(yol, "deger")
    return v


def gecerli_kart(tur, ad, ev=None):
    ek = {}
    if tur == "kaynak":
        ek = {"kutuphane_surumu": "1.2.0", "kaynak_kopyasi": f"programlar/{ad}/kaynak"}
    elif tur == "npm-global":
        ek = {"yerinde.yol": str((ev or TMP) / f"{ad}-pkg"), "yerinde.paket": f"{ad}-paket", "kutuphane_surumu": "1.2.0"}
    else:
        ek = {"yerinde.yol": str((ev or TMP) / f"{ad}-repo")}
    k = doldur(pd.iskelet(tur), ad, ek=ek)
    k["guncelleme_adimlari"][0] = "program-denetim.py --oncesi çalıştırılır"
    return k


def kok_hazirla(kok, kartlar, kayit_atla=(), kaynak_metin=True):
    """kartlar: {ad: kart}. kok altında KAYNAK.md, kaynaklar.json, kaynak/ ve kart.json yazar; kart dosyasının yolunu döner."""
    kok = Path(kok)
    kayitlar = []
    for ad, k in kartlar.items():
        (kok / "programlar" / ad).mkdir(parents=True, exist_ok=True)
        metin = f"# {ad}\n" + " ".join(str(k.get(a, "")) for a in ("kutuphane_surumu", "kutuphane_commit")) if kaynak_metin else "# bos\n"
        (kok / "programlar" / ad / "KAYNAK.md").write_text(metin, encoding="utf-8")
        if k.get("kaynak_kopyasi"):
            (kok / k["kaynak_kopyasi"]).mkdir(parents=True, exist_ok=True)
            (kok / k["kaynak_kopyasi"] / "a.txt").write_text("x")
        if ad not in kayit_atla:
            kayitlar.append({"repo": k["repo"], "tip": "T5", "program": ad})
    (kok / "kaynaklar.json").write_text(json.dumps({"repolar": kayitlar}), encoding="utf-8")
    yol = kok / "kart.json"
    yol.write_text(json.dumps({"sema": 2, "programlar": kartlar}, ensure_ascii=False), encoding="utf-8")
    return yol


def sema(kart_belge, kok):
    return pd.sema_denetle(kart_belge, kok=kok)


def hatalar(bulgu):
    return [b for b in bulgu if b[0] == "HATA"]


def uyarilar(bulgu):
    return [b for b in bulgu if b[0] == "UYARI"]


# ================================================================== S: şema
for tur in ("kaynak", "npm-global", "git-checkout"):
    sk = pd.iskelet(tur)
    json.dumps(sk, ensure_ascii=False)
    b = sema({"sema": 2, "programlar": {pd.YER_TUTUCU: sk}}, KOK)
    test(f"1. iskelet {tur}: geçerli JSON, yalnız 'doldurulmamış' hataları var", b and all("doldurulmamış" in x[3] for x in b),
         [x for x in b if "doldurulmamış" not in x[3]][:3])

KOKLER = {}
for tur in ("kaynak", "npm-global", "git-checkout"):
    kok = klasor(f"kok-{tur}")
    kart = gecerli_kart(tur, "kp")
    kok_hazirla(kok, {"kp": kart})
    KOKLER[tur] = (kok, kart)
    b = sema({"sema": 2, "programlar": {"kp": kart}}, kok)
    test(f"2. geçerli {tur} kartı: 0 HATA, 0 UYARI", not b, b[:3])

# 3. çekirdek alanı tek tek çıkar -> tam bir HATA, o alanı adlandırır
for tur, (kok, kart) in KOKLER.items():
    for alan in pd.CEKIRDEK_ALANLAR:
        if alan == "yedek" and tur == "kaynak":
            continue
        k = copy.deepcopy(kart)
        del k[alan]
        b = sema({"sema": 2, "programlar": {"kp": k}}, kok)
        test(f"3. {tur}: çekirdek '{alan}' eksik -> tam bir HATA", len(b) == 1 and b[0][0] == "HATA" and b[0][2] == alan, b)
    # isteğe bağlı alan eksik -> hiç bulgu yok; geçersiz -> yalnız UYARI
    for alan in pd.ISTEGE_BAGLI_ALANLAR:
        k = copy.deepcopy(kart)
        k.pop(alan, None)
        test(f"3. {tur}: isteğe bağlı '{alan}' eksik -> bulgu yok", not sema({"sema": 2, "programlar": {"kp": k}}, kok))
        k[alan] = "bozuk"
        b = sema({"sema": 2, "programlar": {"kp": k}}, kok)
        test(f"3. {tur}: isteğe bağlı '{alan}' geçersiz -> yalnız UYARI", b and not hatalar(b) and all(x[2].startswith(alan) for x in b), b)

# 3b. kütüphane kapısı sözleşmesi: --sema --ozet-json
kok, kart = KOKLER["npm-global"]
k1 = copy.deepcopy(kart)
k1["disariya_yazar"] = "bozuk"
d1 = klasor("s3b")
(d1 / "a.json").write_text(json.dumps({"sema": 2, "programlar": {"kp": k1}}))
kod, o, e = calistir(["--sema", "--ozet-json", "--kart", str(d1 / "a.json"), "--kok", str(kok)])
n = json.loads(o)
test("3b. isteğe bağlı alan hatası: durum dikkat, satırlar UYARI ile başlar", n["durum"] == "dikkat" and n["satirlar"]
     and all(s.startswith("UYARI:") for s in n["satirlar"]) and kod == 0, n)
k2 = copy.deepcopy(kart)
del k2["geri_alma"]
(d1 / "b.json").write_text(json.dumps({"sema": 2, "programlar": {"kp": k2}}))
kod, o, e = calistir(["--sema", "--ozet-json", "--kart", str(d1 / "b.json"), "--kok", str(kok)])
n = json.loads(o)
test("3b. çekirdek hata: durum sorun, HATA satırı, çıkış 0 (siki yok)", n["durum"] == "sorun" and n["satirlar"][0].startswith("HATA:") and kod == 0, n)
(d1 / "c.json").write_text("{bozuk json")
kod, o, e = calistir(["--sema", "--ozet-json", "--kart", str(d1 / "c.json"), "--kok", str(kok)])
n = json.loads(o)
test("3b. okunamayan programlar.json: tek satır 'HATA: programlar.json okunamadı'", n["durum"] == "sorun" and len(n["satirlar"]) == 1
     and n["satirlar"][0].startswith("HATA: programlar.json okunamadı") and kod == 0, n)

# 4. sıralı değer hataları
kok, kart = KOKLER["npm-global"]
def b_alan(deg):
    return sema({"sema": 2, "programlar": {"kp": deg}}, kok)
k = copy.deepcopy(kart); k["ucret"] = "bedava"
test("4. geçersiz ucret -> HATA", any(x[0] == "HATA" and x[2] == "ucret" for x in b_alan(k)))
k = copy.deepcopy(kart); k["giris_yolu"]["hepsi"]["durum"] = "x"
b = b_alan(k)
test("4. geçersiz giris_yolu durumu -> HATA ve beklenen değerler yazılı", any(x[2] == "giris_yolu.hepsi.durum" and "program-klasoru" in x[3] for x in b), b)
k = copy.deepcopy(kart); h = k["giris_yolu"].pop("hepsi"); k["giris_yolu"]["araclar"] = {"bilinmeyen": h}
b = b_alan(k)
test("4. bilinmeyen araç anahtarı -> HATA", any("bilinmeyen araç" in x[3] for x in b), b)
k = copy.deepcopy(kart); h = k["giris_yolu"].pop("hepsi"); k["giris_yolu"]["araclar"] = {a: h for a in pd.ARAC_ANAHTARLARI[:-1]}
b = b_alan(k)
test("4. beş araçtan biri eksik ('hepsi' yok) -> HATA", any("araç eksik: vscode-copilot" in x[3] for x in b), b)
k = copy.deepcopy(kart); k["giris_yolu"]["araclar"] = {a: h for a in pd.ARAC_ANAHTARLARI}; k["giris_yolu"].pop("hepsi", None)
k["giris_yolu"]["araclar"]["gemini-cli"] = h
test("4. beş araç + isteğe bağlı gemini-cli geçerli", not hatalar(b_alan(k)), b_alan(k))
k = copy.deepcopy(kart); k["disariya_yazar"] = [{"yol": "~/x", "tur": "yok-tur", "ne": "n", "yedeklenir": True, "dogrulandi": True}]
test("4. geçersiz disariya_yazar.tur -> UYARI", [x[0] for x in b_alan(k)] == ["UYARI"], b_alan(k))
kg = copy.deepcopy(KOKLER["git-checkout"][1]); kg["yerel_yamalar"] = {"bilinen": [{"yol": "a", "tur": "x", "yedek": "kopya"}]}
b = sema({"sema": 2, "programlar": {"kp": kg}}, KOKLER["git-checkout"][0])
test("4. geçersiz yerel_yamalar.bilinen.tur -> UYARI", [x[0] for x in b] == ["UYARI"], b)
k = copy.deepcopy(kart); k["kirici_surum"] = {"surum_hatti": "patch"}
test("4. geçersiz kirici_surum.surum_hatti -> UYARI", [x[0] for x in b_alan(k)] == ["UYARI"], b_alan(k))

# 5. venv <-> sabit_surumler
kokg, kartg = KOKLER["git-checkout"]
k = copy.deepcopy(kartg); k["venv"] = ".venv"
test("5. venv var, sabit_surumler yok -> HATA", any("birlikte" in x[3] for x in sema({"sema": 2, "programlar": {"kp": k}}, kokg)))
k = copy.deepcopy(kartg); k["sabit_surumler"] = {"numpy": "1.0"}
test("5. sabit_surumler var, venv yok -> HATA", any("birlikte" in x[3] for x in sema({"sema": 2, "programlar": {"kp": k}}, kokg)))
k = copy.deepcopy(kartg); k["venv"] = ".venv"; k["sabit_surumler"] = ["numpy"]
test("5. sabit_surumler liste -> HATA", any(x[2] == "sabit_surumler" and "sözlük" in x[3] for x in sema({"sema": 2, "programlar": {"kp": k}}, kokg)))

# 6. gizli değer, proje adı, KAYNAK.md, kaynaklar.json, adım
k = copy.deepcopy(kartg); sirr = "sk-" + "A1b2C3d4E5f6G7h8I9j0K1"
k["ne_yapar"] = f"anahtar {sirr}"
b = sema({"sema": 2, "programlar": {"kp": k}}, kokg)
test("6. gizli biçimli metin -> HATA ve mesajda değer yok", any("gizli değer" in x[3] for x in b) and sirr not in json.dumps(b), b)
kp = klasor("kok-proje"); (kp / "projeler.json").write_text(json.dumps({"notlar": {"BenimProjem": {}}, "ek_projeler": []}))
shutil.copytree(kokg / "programlar", kp / "programlar"); shutil.copy(kokg / "kaynaklar.json", kp / "kaynaklar.json")
k = copy.deepcopy(kartg); k["ne_yapar"] = "BenimProjem için uygun"
b = sema({"sema": 2, "programlar": {"kp": k}}, kp)
test("6. projeler.json'daki proje adı -> UYARI (kural 6)", [x[0] for x in b] == ["UYARI"] and "proje adı" in b[0][3], b)
kk = klasor("kok-kaynaksiz"); kok_hazirla(kk, {"kp": kartg}, kaynak_metin=False)
test("6. KAYNAK.md kayıtlı commit metnini taşımıyor -> HATA", any(x[2] == "KAYNAK.md" and "uyuşmuyor" in x[3] for x in sema({"sema": 2, "programlar": {"kp": kartg}}, kk)))
kk2 = klasor("kok-kayitsiz"); kok_hazirla(kk2, {"kp": kartg}, kayit_atla=("kp",))
test("6. kaynaklar.json'da program kaydı yok -> HATA", any("program kaydı yok" in x[3] for x in sema({"sema": 2, "programlar": {"kp": kartg}}, kk2)))
k = copy.deepcopy(kartg); k["guncelleme_adimlari"] = ["bir şey"]
test("6. guncelleme_adimlari '--oncesi' içermiyor -> HATA", any(x[2] == "guncelleme_adimlari" for x in sema({"sema": 2, "programlar": {"kp": k}}, kokg)))
b = sema({"programlar": {"kp": kartg}, "sema": 1}, kokg)
test("6. 'sema' işareti 2 değil -> UYARI", [x[0] for x in b] == ["UYARI"], b)

# 7. --sema --siki çıkış kodları
kart_iyi = KOKLER["npm-global"]
d7 = klasor("s7")
kok_iyi = klasor("kok-s7"); yol_iyi = kok_hazirla(kok_iyi, {"kp": copy.deepcopy(KOKLER["npm-global"][1])})
bozuk = copy.deepcopy(KOKLER["npm-global"][1]); del bozuk["cikarma"]
kok_boz = klasor("kok-s7b"); yol_boz = kok_hazirla(kok_boz, {"kp": bozuk})
test("7. --sema --siki: geçerli kart çıkış 0", calistir(["--sema", "--siki", "--kart", str(yol_iyi), "--kok", str(kok_iyi)])[0] == 0)
test("7. --sema --siki: bozuk kart çıkış 1", calistir(["--sema", "--siki", "--kart", str(yol_boz), "--kok", str(kok_boz)])[0] == 1)
test("7. --sema (siki yok): bozuk kart yine çıkış 0", calistir(["--sema", "--kart", str(yol_boz), "--kok", str(kok_boz)])[0] == 0)
kod, o, e = calistir(["--sema", "--ozet-json", "--kart", str(yol_iyi), "--kok", str(kok_iyi)])
test("7. --sema --ozet-json: stdout tek JSON nesnesi", json.loads(o)["durum"] == "temiz" and o.count("\n") == 1, o)

# ================================================================== N: ağ sınıflaması
class Yanit:
    def __init__(self, veri):
        self.veri = veri

    def read(self):
        return json.dumps(self.veri).encode()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def urlopen_hata(hata):
    def f(*a, **k):
        raise hata
    return f


with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 404, "nf", {}, None))):
    test("8. npm_son_surum 404 -> None, sınıf '404'", pd.npm_son_surum("paketx", 3) is None and pd._SON_HATA[("npm", "paketx")] == "404")
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.URLError("ag yok"))):
    test("8. npm_son_surum ağ hatası -> None, sınıf 'ag'", pd.npm_son_surum("paketx") is None and pd._SON_HATA[("npm", "paketx")] == "ag")
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 500, "x", {}, None))):
    test("8. npm_son_surum HTTP 500 -> 'ag' (404 değil)", pd.npm_son_surum("paketx") is None and pd._SON_HATA[("npm", "paketx")] == "ag")
with yama(urllib_dot_request__urlopen=lambda *a, **k: Yanit({"version": "2.0.0"})):
    test("8. npm_son_surum başarı -> sürüm, hata kaydı silinir, imza (paket, zaman_asimi) aynı",
         pd.npm_son_surum("paketx", 5) == "2.0.0" and ("npm", "paketx") not in pd._SON_HATA)

def gh_hata(hata):
    def f(yol, deneme=4):
        raise hata
    return f

with yama(gh_api=gh_hata(pd.GhBulunamadi("x"))):
    test("9. git_son GhBulunamadi -> (None, None), '404'", pd.git_son("o/r", "main", "c" * 40) == (None, None) and pd._SON_HATA[("git", "o/r")] == "404")
with yama(gh_api=gh_hata(RuntimeError("gh api kapalı"))):
    test("9. git_son API kapalı -> 'kapali'", pd.git_son("o/r", "main") == (None, None) and pd._SON_HATA[("git", "o/r")] == "kapali")
with yama(gh_api=gh_hata(ValueError("baska"))):
    test("9. git_son başka hata -> 'ag'", pd.git_son("o/r", "main") == (None, None) and pd._SON_HATA[("git", "o/r")] == "ag")
with yama(gh_api=lambda yol, deneme=4: {"sha": "s" * 40, "ahead_by": 3}):
    test("9. git_son başarı: dönüş değerleri eskisi gibi, hata kaydı silinir",
         pd.git_son("o/r", "main", "c" * 40) == ("s" * 40, 3) and ("git", "o/r") not in pd._SON_HATA
         and pd.git_son("o/r", "main", "s" * 40) == ("s" * 40, 0))

def gh_taslak(tablo):
    def f(yol, deneme=4):
        for k, v in tablo.items():
            if yol == f"repos/{k}":
                if isinstance(v, Exception):
                    raise v
                return v
        raise pd.GhBulunamadi(yol)
    return f

KAYNAKLAR = {"repolar": [{"repo": "yeni/ad", "eski_adlar": ["eski/ad"], "program": "x"}]}
test("10. repo_durumu: full_name farklı -> taşınmış", pd.repo_durumu("eski/ad", gh=gh_taslak({"eski/ad": {"full_name": "Yeni/Ad"}}), kaynaklar=KAYNAKLAR) == ("taşınmış", "Yeni/Ad"))
test("10. repo_durumu: var", pd.repo_durumu("o/r", gh=gh_taslak({"o/r": {"full_name": "o/r"}}), kaynaklar={}) == ("var", None))
test("10. repo_durumu: 404 + eski ad yanıt veriyor -> taşınmış",
     pd.repo_durumu("yeni/ad", gh=gh_taslak({"eski/ad": {"full_name": "yeni/ad2"}}), kaynaklar=KAYNAKLAR) == ("taşınmış", "yeni/ad2"))
test("10. repo_durumu: her yerde 404 -> kayıp", pd.repo_durumu("yeni/ad", gh=gh_taslak({}), kaynaklar=KAYNAKLAR) == ("kayıp", None))
test("10. repo_durumu: API kapalı", pd.repo_durumu("o/r", gh=gh_taslak({"o/r": RuntimeError("gh api kapalı: x")}), kaynaklar={}) == ("kapalı", None))
test("10. repo_durumu: ağ hatası", pd.repo_durumu("o/r", gh=gh_taslak({"o/r": RuntimeError("zaman aşımı")}), kaynaklar={}) == ("ağ", None))

# 11. kaynak kopyalı kartta releases 404
kokk, kartk = KOKLER["kaynak"]
yol_k = kok_hazirla(kokk, {"kp": kartk})
def kaynak_calistir(tablo):
    with yama(gh_api=gh_taslak(tablo)):
        return calistir(["--kart", str(yol_k), "--cikti", str(kokk / "r.md"), "--kok", str(kokk), "--ev", str(kokk / "ev")])
kod, o, e = kaynak_calistir({"o/kp": {"full_name": "o/kp"}})
test("11. kaynak kartı: release yok + repo var -> UYARI, durum öğrenilemedi, çıkış 0",
     kod == 0 and "repo'da yayımlanmış release yok" in o and "öğrenilemedi" in o, o)
kod, o, e = kaynak_calistir({})
test("11. kaynak kartı: repo 404 -> KAYIP (404), çıkış 0", kod == 0 and "KAYIP (404)" in o and "KAYIP (404)" in (kokk / "r.md").read_text(), o)

# 12. eski ad ve origin
with yama(repo_takma_adlari=lambda: {"old/x": "new/x"}):
    test("12. kart_eski_ad: eski adı kullanan kart", pd.kart_eski_ad({"repo": "old/x"}) == "new/x")
    test("12. kart_eski_ad: güncel ad None", pd.kart_eski_ad({"repo": "new/x"}) is None)
    for url, beklenen in (("https://github.com/new/x.git\n", "güncel"), ("https://github.com/old/x.git\n", "eski-ad"), ("git@github.com:baska/y.git\n", "farklı")):
        with yama(git_okuma=lambda *a, _u=url: _u):
            test(f"12. origin_durumu {beklenen}", pd.origin_durumu("/x", {"repo": "new/x"}) == beklenen)

# ================================================================== O: ön kontrol
BUGUN = date(2026, 11, 11)


def ev_hazirla(ad, zshenv=None, zshrc=None, settings=None):
    ev = klasor(ad)
    if zshenv is not None:
        (ev / ".zshenv").write_text(zshenv)
    if zshrc is not None:
        (ev / ".zshrc").write_text(zshrc)
    if settings is not None:
        (ev / ".claude").mkdir()
        (ev / ".claude" / "settings.json").write_text(settings)
    return ev


def yedek_yap(ev, ad, tarih="2026-11-11", onceki=None, zorunlu=(), kayit=True, ek=None, n=None):
    d = ev / "Documents" / "Claude" / "yedek" / (f"{ad}-{tarih}" + (f"-{n}" if n else ""))
    d.mkdir(parents=True, exist_ok=True)
    for z in zorunlu:
        (d / z).write_text("x") if "." in z else ((d / z).mkdir(exist_ok=True), (d / z / "f").write_text("x"))
    if kayit:
        (d / "KAYIT.json").write_text(json.dumps({"program": ad, "tarih": tarih, "onceki": onceki or {"surum": "1.2.0", "commit": ""}, "icerik": []}))
    for yol, icerik in (ek or {}).items():
        (d / yol).parent.mkdir(parents=True, exist_ok=True)
        (d / yol).write_text(icerik)
    return d


def npm_ortam(ad="np", ortam=None, pkg_surum="1.2.0"):
    """Geçici ev + npm kartı. Dönen: (ev, kok, kart, kart_yolu)."""
    ev = ev_hazirla(f"ev-{ad}", zshenv="export GEREKLI_ANAHTAR=1\n", zshrc="export GEREKLI_ANAHTAR=1\n", settings=json.dumps({"env": {"GEREKLI_ANAHTAR": "1"}}))
    (ev / f"{ad}-pkg").mkdir()
    (ev / f"{ad}-pkg" / "package.json").write_text(json.dumps({"version": pkg_surum}))
    kart = gecerli_kart("npm-global", ad, ev)
    kart["yedek"]["zorunlu"] = ["KAYIT.json", "veri"]
    kart["ortam_anahtarlari"] = ortam if ortam is not None else [{"ad": "GEREKLI_ANAHTAR", "beklenen": "1", "gerekli": True,
                                                                  "nerede": ["~/.zshenv", "~/.zshrc", "~/.claude/settings.json"], "not": ""}]
    kok = klasor(f"kok-{ad}")
    yol = kok_hazirla(kok, {ad: kart})
    return ev, kok, kart, yol


def ctx_yap(ev, kok=None, **kw):
    return pd._ctx(ev=ev, kok=kok or KOK, bugun=kw.pop("bugun", BUGUN), environ=kw.pop("environ", {}), **kw)


# 14. yedek kontrolü
ev, kok, kart, yol = npm_ortam("yd")
def yk(ev_=ev, kurulu="1.2.0", **kw):
    return pd.yedek_kontrol("yd", kart, ctx_yap(ev_, kok, **kw), kurulu)
test("14. yedek klasörü yok -> HATA 'yedek yok'", any(x[0] == "HATA" and "yedek yok" in x[2] for x in yk()))
d = yedek_yap(ev, "yd", tarih="2026-11-01", zorunlu=["veri"])
test("14. yedek eski -> HATA", any("yedek eski" in x[2] for x in yk()))
shutil.rmtree(d)
d = yedek_yap(ev, "yd", zorunlu=["veri"])
s_ = yk()
test("14. geçerli yedek -> tek TAMAM", [x[0] for x in s_] == ["TAMAM"], s_)
(d / "KAYIT.json").unlink()
test("14. KAYIT.json yok -> HATA", any("KAYIT.json" in x[2] for x in yk() if x[0] == "HATA"))
(d / "KAYIT.json").write_text("{bozuk")
test("14. KAYIT.json geçersiz -> HATA", any("KAYIT.json" in x[2] for x in yk() if x[0] == "HATA"))
(d / "KAYIT.json").write_text(json.dumps({"tarih": "2026-11-05", "onceki": {"surum": "1.2.0"}}))
test("14. KAYIT.json tarihi klasörle uyuşmuyor -> HATA", any("tarihi" in x[2] for x in yk()))
(d / "KAYIT.json").write_text(json.dumps({"tarih": "2026-11-11", "onceki": {"surum": "0.9.0"}}))
test("14. KAYIT.json onceki kurulu değil -> HATA 'yedek başka sürümün'", any("yedek başka sürümün (kurulu değil)" in x[2] for x in yk()))
(d / "KAYIT.json").write_text(json.dumps({"tarih": "2026-11-11", "onceki": {"surum": "1.2.0"}}))
shutil.rmtree(d / "veri")
test("14. zorunlu klasör yok -> HATA 'yedekte yok'", any("yedekte yok: veri" in x[2] for x in yk()))
(d / "veri").mkdir()
test("14. zorunlu klasör boş -> HATA", any("yedekte yok: veri" in x[2] for x in yk()))
(d / "veri" / "ic" / "derin").mkdir(parents=True)
(d / "veri" / "ic" / "derin" / "config.json").write_text("{}") if False else (d / "veri" / "ic" / "derin" / ".env").write_text("X=1")
b = yk()
test("14. iç içe .env -> HATA 'yedekte gizli dosya var' (yalnız yol)", any("yedekte gizli dosya var: veri/ic/derin/.env" in x[2] for x in b), b)
shutil.rmtree(d / "veri"); (d / "veri").mkdir(); (d / "veri" / "f").write_text("x")
kart["yedek"]["yasak_adlar"] = ["config.json"]
(d / "veri" / "config.json").write_text("{}")
test("14. kartın yasak_adlar listesi (config.json) uygulanır", any("config.json" in x[2] for x in yk()))
(d / "veri" / "config.json").unlink()
kart["yedek"]["yasak_adlar"] = []
test("14. her şey düzelince yine TAMAM", [x[0] for x in yk()] == ["TAMAM"])
yedek_yap(ev, "yd", zorunlu=["veri"], n=2, onceki={"surum": "9.9.9"})
test("14. aynı gün iki yedek: en yeni (-2) kullanılır", any("yedek başka sürümün" in x[2] for x in yk()))

# 15. ortam
ev15 = ev_hazirla("ev15", zshenv="export HYPERFRAMES_SKIP_SKILLS=1\nOTHER_API_KEY=eski\n", zshrc="export OTHER_API_KEY=SECRETVALUE123\nexport HYPERFRAMES_SKIP_SKILLS=1\n",
                  settings=json.dumps({"env": {"HYPERFRAMES_SKIP_SKILLS": "1"}}))
orn = lambda **k: {"ortam_anahtarlari": [dict({"ad": "HYPERFRAMES_SKIP_SKILLS", "beklenen": "1", "gerekli": True,
                                              "nerede": ["~/.zshenv", "~/.zshrc", "~/.claude/settings.json"], "not": ""}, **k)]}
r = pd.ortam_kontrol(orn(), ctx_yap(ev15))
test("15. ortam 3/3 -> TAMAM", r == [("TAMAM", "ortam", "HYPERFRAMES_SKIP_SKILLS: 3/3 yerde tanımlı")], r)
(ev15 / ".zshenv").write_text("# export HYPERFRAMES_SKIP_SKILLS=1\n")
r = pd.ortam_kontrol(orn(), ctx_yap(ev15))
test("15. ortam 2/3 (yorum satırı sayılmaz) -> UYARI ve eksik dosya adı", r[0][0] == "UYARI" and "2/3" in r[0][2] and "~/.zshenv" in r[0][2], r)
for f in (".zshenv", ".zshrc", ".claude/settings.json"):
    (ev15 / f).unlink()
r = pd.ortam_kontrol(orn(), ctx_yap(ev15))
test("15. ortam 0/3, gerekli -> HATA", r[0][0] == "HATA" and "hiçbir yerde" in r[0][2], r)
r = pd.ortam_kontrol(orn(), ctx_yap(ev15, environ={"HYPERFRAMES_SKIP_SKILLS": "1"}))
test("15. ortam 0/3 ama süreç ortamında tanımlı -> HATA değil", r and r[0][0] != "HATA", r)
r = pd.ortam_kontrol(orn(gerekli=False), ctx_yap(ev15))
test("15. ortam gerekli değil, hiçbir yerde yok -> BİLGİ", r[0][0] == "BİLGİ" and "isteğe bağlı" in r[0][2], r)
(ev15 / ".zshenv").write_text("export HYPERFRAMES_SKIP_SKILLS=0\n")
(ev15 / ".zshrc").write_text("export OTHER_API_KEY=SECRETVALUE123\nexport HYPERFRAMES_SKIP_SKILLS=0\n")
r = pd.ortam_kontrol(orn(), ctx_yap(ev15))
yazi = json.dumps(r, ensure_ascii=False)
test("15. değer beklenenden farklı -> UYARI; değerin kendisi ve başka satırdaki gizli değer çıktıda yok",
     any("beklenenden farklı" in x[2] for x in r) and "SECRETVALUE123" not in yazi and "=0" not in yazi, r)
(ev15 / ".claude").mkdir(exist_ok=True); (ev15 / ".claude" / "settings.json").write_text("{bozuk")
r = pd.ortam_kontrol({"ortam_anahtarlari": [{"ad": "X", "beklenen": "1", "gerekli": False, "nerede": ["~/.claude/settings.json"], "not": ""}]}, ctx_yap(ev15))
test("15. bozuk settings.json -> UYARI 'okunamadı'", any(x[0] == "UYARI" and "okunamadı" in x[2] for x in r), r)

# 16. yerel yamalar
def yp(*bil):
    return {"yerel_yamalar": {"bilinen": [{"yol": y, "tur": t, "yedek": "kopya", "yeniden_uygula": True} for y, t in bil]}}
r = pd.yama_kontrol(yp(("a.py", "izlenen"), ("b.txt", "izlenmeyen")), " M a.py\n?? b.txt\n")
test("16. her değişiklik kayıtlı -> TAMAM", [x[0] for x in r] == ["TAMAM"], r)
r = pd.yama_kontrol(yp(("a.py", "izlenen")), " M a.py\n M x/gizemli.py\n")
test("16. kayıtsız yol -> HATA ve yalnız o yol", [x[0] for x in r] == ["HATA"] and "x/gizemli.py" in r[0][2], r)
r = pd.yama_kontrol(yp(("onbellek/", "izlenmeyen")), "?? onbellek/\n?? onbellek/alt/dosya.bin\n")
test("16. klasör öneki kaydı eşleşir", [x[0] for x in r] == ["TAMAM"], r)
r = pd.yama_kontrol(yp(("yeni.py", "izlenen")), "R  eski.py -> yeni.py\n")
test("16. yeniden adlandırma: yeni yol esas", [x[0] for x in r] == ["TAMAM"], r)
r = pd.yama_kontrol(yp(("boşluklu dosya.txt", "izlenmeyen")), '?? "boşluklu dosya.txt"\n')
test("16. tırnaklı yol (boşluk) çözülür", [x[0] for x in r] == ["TAMAM"], r)
r = pd.yama_kontrol(yp(("a.py", "izlenen"), ("kayip.py", "izlenen")), " M a.py\n")
test("16. kayıtlı ama değişmemiş -> BİLGİ", ("BİLGİ", "yerel değişiklik", "kayıtlı ama değişmemiş: kayip.py (yama upstream'e girmiş ya da kaybolmuş olabilir)") in r, r)
r = pd.yama_kontrol(yp(), None)
test("16. status okunamadı -> HATA", [x[0] for x in r] == ["HATA"], r)
r = pd.yama_kontrol(yp(), "".join(f" M d{i}.py\n" for i in range(25)))
test("16. 25 kayıtsız yol: 20 satır + '… ve 5 tane daha'", len(r) == 21 and "ve 5 tane daha" in r[-1][2], len(r))
r = pd.yama_kontrol({}, " M a.py\n")
test("16. kartta yerel_yamalar yok: değişiklik kayıtsız sayılır (güvenli durma)", r[0][0] == "HATA", r)

# 17. kırıcı kural
npmk = {"yerinde": {"tur": "npm-global"}, "kirici_surum": {"surum_hatti": "minor"}}
test("17. 0.9.23 -> 0.9.33 aday değil", pd.kirici_adayi(npmk, "0.9.23", "0.9.33") == [])
test("17. 0.9.23 -> 0.10.0 aday (minor)", len(pd.kirici_adayi(npmk, "0.9.23", "0.10.0")) == 1)
test("17. 0.9.23 -> 1.0.0 aday", len(pd.kirici_adayi(npmk, "0.9.23", "1.0.0")) == 1)
gitk = {"yerinde": {"tur": "git-checkout"}, "kirici_surum": {"esik_commit": 50, "izle_dosyalar": ["requirements.txt"]},
        "yerel_yamalar": {"bilinen": [{"yol": "lib/a.py", "tur": "izlenen"}]}}
test("17. git 244 geride (eşik 50) aday; 10 geride değil", pd.kirici_adayi(gitk, "x", "y", 244) and not pd.kirici_adayi(gitk, "x", "y", 10))
test("17. izle_dosyalar yeni commit'lerde değişiyor -> aday", pd.kirici_adayi(gitk, "x", "y", 1, ["requirements.txt"]))
n17 = pd.kirici_adayi(gitk, "x", "y", 1, ["lib/a.py"])
test("17. yamalı dosyaya dokunan commit -> neden listesinde", n17 and "yamalı" in n17[0], n17)
test("17. 'major' hattı: 1.2 -> 2.0 aday, 1.2 -> 1.9 değil",
     pd.kirici_adayi({"yerinde": {}, "kirici_surum": {"surum_hatti": "major"}}, "1.2.0", "2.0.0") and
     not pd.kirici_adayi({"yerinde": {}, "kirici_surum": {"surum_hatti": "major"}}, "1.2.0", "1.9.0"))

# 18. giriş yolu ve gizli dosya
ev18 = klasor("ev18"); (ev18 / "kilavuz.md").write_text("k")
p18 = {"giris_yolu": {"kural": "k", "kilavuz": "~/kilavuz.md", "araclar": {
    "codex": {"durum": "program-klasoru", "yol": "~/kilavuz.md", "nasil": "n"},
    "cursor": {"durum": "program-klasoru", "yol": "~/yok.md", "nasil": "n"},
    "claude-code": {"durum": "karar-bekliyor", "yol": "", "nasil": "n"}}}}
r = pd.giris_kontrol(p18, ctx_yap(ev18))
test("18. var olan yol BİLGİ; yok olan program-klasoru yolu UYARI; karar-bekliyor BİLGİ",
     ("BİLGİ", "giriş yolu", "codex: program-klasoru (~/kilavuz.md var)") in r and any(x[0] == "UYARI" and "giriş yolu kırık: cursor" in x[2] for x in r)
     and ("BİLGİ", "giriş yolu", "claude-code: kullanıcı kararı bekliyor") in r, r)
gizli = ev18 / "anahtar.env"; gizli.write_text("COK_GIZLI_METIN"); gizli.chmod(0)
try:
    r = pd.gizli_kontrol({"gizli_dosyalar": ["~/anahtar.env", "~/yok.env"]}, ctx_yap(ev18))
finally:
    gizli.chmod(stat.S_IRUSR | stat.S_IWUSR)
test("18. gizli dosya: erişilemez dosya 'var' görünür, içerik hiç okunmaz/yazdırılmaz; yoksa UYARI",
     r[0][0] == "BİLGİ" and "anahtar.env" in r[0][2] and r[1][0] == "UYARI" and "COK_GIZLI_METIN" not in json.dumps(r), r)
test("18. gizli_dosyalar alanı yoksa 'kayıtsız' BİLGİ", pd.gizli_kontrol({}, ctx_yap(ev18)) == [("BİLGİ", "gizli", "kayıtsız")])

# 19. sabit sürümler (sahte dist-info)
def sahte_venv(kok, paketler):
    site = kok / ".venv" / "lib" / "python3.10" / "site-packages"
    for ad, surum in paketler.items():
        di = site / f"{ad}-{surum}.dist-info"
        di.mkdir(parents=True)
        (di / "METADATA").write_text(f"Metadata-Version: 2.1\nName: {ad}\nVersion: {surum}\n\nbody\n")
ev19 = klasor("ev19"); (ev19 / "gp-repo").mkdir()
sahte_venv(ev19 / "gp-repo", {"numpy": "1.26.4", "torch": "2.2.2"})
k19 = {"kopya": "yerinde", "yerinde": {"tur": "git-checkout", "yol": str(ev19 / "gp-repo")}, "venv": ".venv", "sabit_surumler": {"numpy": "1.26.4", "torch": "2.2.2"}}
kur19, git_hepsi = "c" * 40, None
def oncesi19(k, **kw):
    with yama(git_kurulu=lambda y: (kur19, 0, 0), git_okuma=lambda *a: "" if "status" in a else "main\n", repo_durumu=lambda r, **q: ("var", None)):
        return pd.oncesi_denetle("gp", k, ctx_yap(ev19, cevrimdisi=True, **kw))[0]
r = [x for x in oncesi19(k19) if x[1] == "sabit sürümler"]
test("19. pin tutuyor -> '2/2 tutuyor'", r == [("TAMAM", "sabit sürümler", "2/2 tutuyor")], r)
k19b = copy.deepcopy(k19); k19b["sabit_surumler"]["numpy"] = "2.0.0"
r = [x for x in oncesi19(k19b) if x[1] == "sabit sürümler"]
test("19. pin farkı -> HATA ve paket adı", r and r[0][0] == "HATA" and "numpy" in r[0][2], r)
k19c = copy.deepcopy(k19); k19c["yerinde"]["yol"] = str(ev19 / "baska")
(ev19 / "baska").mkdir()
r = [x for x in oncesi19(k19c) if x[1] == "sabit sürümler"]
test("19. venv yok -> HATA 'venv yok'", r == [("HATA", "sabit sürümler", "venv yok")], r)
test("19. --pin-listesi: sıralı ad==sürüm satırları",
     calistir(["--pin-listesi", "gp", "--kart", str(kok_hazirla(klasor("kok-pin"), {"gp": dict(gecerli_kart("git-checkout", "gp", ev19), venv=".venv", sabit_surumler={"numpy": "1.26.4"})})), "--ev", str(ev19)])[1]
     == "numpy==1.26.4\ntorch==2.2.2\n")
kodp, op, ep = calistir(["--pin-listesi", "kp", "--kart", str(KOKLER["npm-global"][0] / "kart.json")])
test("24. --pin-listesi venv'siz kart -> çıkış 2", kodp == 2, (kodp, ep))

# 20. disk yeri
with yama(shutil__disk_usage=lambda p: __import__('types').SimpleNamespace(total=0, used=0, free=2 * 10 ** 9)):
    kd = copy.deepcopy(k19); kd["kirici_surum"] = {"esik_commit": 1, "izle_dosyalar": [], "deneme_klasoru": "~/d", "deneme_disk_gb": 8}
    with yama(git_kurulu=lambda y: (kur19, 0, 0), git_okuma=lambda *a: "" if "status" in a else "main\n", repo_durumu=lambda r, **q: ("var", None),
              git_son=lambda *a: ("d" * 40, 99), git_karsilastir=lambda *a: (99, [], False)):
        r = pd.oncesi_denetle("gp", kd, ctx_yap(ev19))[0]
test("20. deneme için disk az -> UYARI", any(x[0] == "UYARI" and "yer az" in x[2] for x in r), r)

# 21. uçtan uca npm kartı
ev, kok, kart, yol = npm_ortam("e2e")
yedek_yap(ev, "e2e", tarih=__import__("datetime").date.today().isoformat(), zorunlu=["veri"], onceki={"surum": "1.2.0"})   # taze yedek: bugünün tarihi (sabit tarih tazelik_gun sonra eskir)
ARGS = ["--oncesi", "e2e", "--kart", str(yol), "--kok", str(kok), "--ev", str(ev)]
with yama(npm_son_surum=lambda *a, **k: "1.3.0", gh_api=gh_taslak({"o/e2e": {"full_name": "o/e2e"}})):
    kod, o, e = calistir(ARGS)
test("21. hazır: 'SONUÇ: HAZIR', çıkış 0", kod == 0 and "SONUÇ: HAZIR\n" in o and "YENİ SÜRÜM VAR" in o, o)
shutil.rmtree(ev / "Documents")
with yama(npm_son_surum=lambda *a, **k: "1.3.0", gh_api=gh_taslak({"o/e2e": {"full_name": "o/e2e"}})):
    kod, o, e = calistir(ARGS)
    kod2, o2, e2 = calistir(ARGS + ["--siki"])
    kod3, o3, e3 = calistir(ARGS + ["--ozet-json"])
test("21. yedek yok: 'HAZIR DEĞİL (1 engel)', çıkış 0", kod == 0 and "SONUÇ: HAZIR DEĞİL (1 engel)" in o, o)
test("21. yedek yok + --siki: çıkış 1", kod2 == 1)
nes = json.loads(o3)
test("21. --ozet-json: tam dört anahtar, stdout'ta başka çıktı yok, durum sorun",
     set(nes) == {"arac", "durum", "satirlar", "karar_bekleyen"} and o3.strip().count("\n") == 0 and nes["durum"] == "sorun"
     and nes["arac"] == "program-denetim --oncesi e2e", nes)
with yama(npm_son_surum=lambda *a, **k: "1.2.0", gh_api=gh_taslak({})):
    kod, o, e = calistir(ARGS)
test("21. güncel: 'GÜNCELLENECEK BİR ŞEY YOK'", "SONUÇ: GÜNCELLENECEK BİR ŞEY YOK" in o and kod == 0, o)
shutil.rmtree(ev / "e2e-pkg")
kod, o, e = calistir(ARGS)
test("21. paket klasörü yok: 'KURULU DEĞİL'", "SONUÇ: KURULU DEĞİL" in o and kod == 0, o)
yedek_yap(ev, "e2e", zorunlu=["veri"], onceki={"surum": "1.2.0"})
(ev / "e2e-pkg").mkdir(); (ev / "e2e-pkg" / "package.json").write_text(json.dumps({"version": "1.2.5"}))
with yama(npm_son_surum=lambda *a, **k: "1.3.0", gh_api=gh_taslak({"o/e2e": {"full_name": "o/e2e"}})):
    kod, o, e = calistir(ARGS)
test("21. kurulu sürüm karttan farklı: HATA 'kart' (KART ESKİ), HAZIR DEĞİL", "HATA    kart" in o and "SONUÇ: HAZIR DEĞİL" in o, o)

# 22. gerçek git deposu
def git(yol, *a):
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(yol), *a], capture_output=True, text=True)
if shutil.which("git"):
    ev22 = klasor("ev22"); rep = ev22 / "gp-repo"; rep.mkdir()
    git(rep, "init", "-q"); (rep / "a.txt").write_text("1"); (rep / "b.txt").write_text("1")
    git(rep, "add", "."); git(rep, "commit", "-q", "-m", "ilk")
    sha22 = git(rep, "rev-parse", "HEAD").stdout.strip(); dal22 = git(rep, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    (rep / "a.txt").write_text("2"); (rep / "b.txt").write_text("2")
    k22 = gecerli_kart("git-checkout", "gp", ev22)
    k22["yerinde"]["dal"] = dal22; k22["kutuphane_commit"] = sha22
    k22["yerel_yamalar"] = {"bilinen": [{"yol": "a.txt", "tur": "izlenen", "amac": "x", "yedek": "kopya", "yeniden_uygula": True}]}
    k22["yedek"]["zorunlu"] = ["KAYIT.json"]
    kok22 = klasor("kok22"); yol22 = kok_hazirla(kok22, {"gp": k22})
    yedek_yap(ev22, "gp", onceki={"commit": sha22})
    kod, o, e = calistir(["--oncesi", "gp", "--kart", str(yol22), "--kok", str(kok22), "--ev", str(ev22), "--cevrimdisi"])
    test("22. gerçek git: yalnız kayıtsız b.txt HATA, a.txt değil", "kayıtsız yerel değişiklik: b.txt" in o and "kayıtsız yerel değişiklik: a.txt" not in o, o)
    (rep / "c.txt").write_text("3"); git(rep, "add", "c.txt"); git(rep, "commit", "-q", "-m", "ikinci")
    kod, o, e = calistir(["--oncesi", "gp", "--kart", str(yol22), "--kok", str(kok22), "--ev", str(ev22), "--cevrimdisi"])
    test("22. gerçek git: HEAD kayınca KART ESKİ HATA", "HATA    kart" in o and "karttan farklı" in o, o)
    # git okuma sırasında depo değişmedi (salt okuma): indeks bile yenilenmedi
    test("22. ön kontrol depoyu değiştirmedi", git(rep, "status", "--porcelain").stdout.count("\n") >= 2)
else:
    test("22. git yok: atlandı", True)

# 23. bilinmeyen program ve --cevrimdisi
kod, o, e = calistir(["--oncesi", "nope", "--kart", str(yol), "--kok", str(kok)])
test("23. --oncesi bilinmeyen program: çıkış 2, kart adları listelenir", kod == 2 and "program yok: nope" in e and "e2e" in e, (kod, e))
cagri = []
def yasak(*a, **k):
    cagri.append(a)
    raise AssertionError("ağa gidildi")
with yama(gh_api=yasak, urllib_dot_request__urlopen=yasak, npm_son_surum=yasak, git_son=yasak, git_karsilastir=yasak, npm_integrity=yasak):
    kod, o, e = calistir(ARGS + ["--cevrimdisi", "--tedarik"])
test("23. --cevrimdisi: hiçbir ağ çağrısı yok, 'atlandı: çevrimdışı' yazar", not cagri and "atlandı: çevrimdışı" in o and kod == 0, (cagri, o))

# 13. tedarik doğrulaması (--tedarik)
ev13, kok13, kart13, yol13 = npm_ortam("td")
kart13["tedarik_dogrulama"] = {"yayinci": {"hesap": "h", "ucuncu_taraf": True, "imza": "yok", "not": ""},
                               "ozet": {"tur": "npm-integrity", "deger": "sha512-AAA", "ne_icin": "x", "kayit_tarihi": "2026-11-11"}, "kural": "k"}
for canli, beklenen in (("sha512-AAA", "TAMAM"), ("sha512-BBB", "HATA"), (None, "UYARI")):
    cagrilar = []
    with yama(npm_integrity=lambda *a, _c=canli: (cagrilar.append(a), _c)[1]):
        r = pd.tedarik_kontrol(kart13, ctx_yap(ev13, kok13, tedarik=True), "1.2.0", "1.3.0")
    ent = [x for x in r if x[1] == "tedarik" and "imzasız" not in x[2]]
    test(f"13. --tedarik: integrity canlı={canli} -> {beklenen}", ent and ent[0][0] == beklenen and len(cagrilar) == 1, r)
cagrilar = []
yedek_yap(ev13, "td", zorunlu=["veri"])
(ev13 / "Documents" / "Claude" / "yedek" / "td-2026-11-11" / "veri").mkdir(exist_ok=True)
with yama(npm_son_surum=lambda *a, **k: "1.3.0", npm_integrity=lambda *a: cagrilar.append(a), gh_api=gh_taslak({"o/td": {"full_name": "o/td"}})):
    kod, o, e = calistir(["--oncesi", "td", "--kart", str(yol13), "--kok", str(kok13), "--ev", str(ev13)])
test("13. --tedarik yokken tedarik satırı ve integrity çağrısı yok", not cagrilar and "tedarik" not in o, o)

# ================================================================== R: rapor ve uyumluluk
# 25. eski biçimli (v2 alanları olmayan) kartlar
d25 = klasor("r25"); (d25 / "pkg").mkdir(); (d25 / "pkg" / "package.json").write_text('{"version":"1.0.0"}')
eski = {"programlar": {
    "liste-pin": {"repo": "x/y", "kopya": "yerinde", "kutuphane_surumu": "1.0.0", "venv": ".venv", "sabit_surumler": ["numpy"],
                  "yerinde": {"tur": "npm-global", "yol": str(d25 / "pkg"), "paket": "p"}},
    "reposuz": {"kopya": "yerinde", "kutuphane_surumu": "1.0.0", "yerinde": {"tur": "npm-global", "yol": str(d25 / "pkg"), "paket": "p"}}}}
(d25 / "k.json").write_text(json.dumps(eski))
with yama(npm_son_surum=lambda *a, **k: None):
    kod, o, e = calistir(["--kart", str(d25 / "k.json"), "--cikti", str(d25 / "r.md"), "--kok", str(d25), "--ev", str(d25)])
rap = (d25 / "r.md").read_text(encoding="utf-8")
test("25. eski biçimli kartlar: çıkış 0, rapor yazıldı, '## Kart şeması' hataları gösterir", kod == 0 and "## Kart şeması" in rap and "HATA:" in rap, rap[-400:])
with yama(npm_son_surum=lambda *a, **k: None, npm_kurulu_surum=lambda *a, **k: 1 / 0):
    kod, o, e = calistir(["--kart", str(d25 / "k.json"), "--cikti", str(d25 / "r2.md"), "--kok", str(d25), "--ev", str(d25)])
test("25. beklenmeyen hata: 'öğrenilemedi', çıkış 0", kod == 0 and "öğrenilemedi" in (d25 / "r2.md").read_text(encoding="utf-8"))

# 26. --ozet-json eşlemesi (normal koşu)
ev26, kok26, kart26, yol26 = npm_ortam("r26", ortam=[])
(ev26 / "r26-pkg" / "package.json").write_text(json.dumps({"version": "1.2.0"}))
def normal(son, pkg="1.2.0", extra=()):
    (ev26 / "r26-pkg" / "package.json").write_text(json.dumps({"version": pkg}))
    with yama(npm_son_surum=lambda *a, **k: son):
        return calistir(["--ozet-json", "--kart", str(yol26), "--cikti", str(kok26 / "r.md"), "--kok", str(kok26), "--ev", str(ev26), *extra])
kod, o, e = normal("1.2.0")
test("26. her şey güncel -> durum temiz", json.loads(o)["durum"] == "temiz" and kod == 0, o)
kod, o, e = normal("1.3.0")
nes = json.loads(o)
test("26. YENİ SÜRÜM VAR -> dikkat, karar_bekleyen programı içerir", nes["durum"] == "dikkat" and nes["karar_bekleyen"] == ["r26 1.2.0 -> 1.3.0 güncellemesi: kullanıcı onayı bekliyor"], nes)
kod, o, e = normal("1.3.0", pkg="1.2.9")
test("26. KART ESKİ -> sorun", json.loads(o)["durum"] == "sorun", o)
kod, o, e = normal("1.3.0", pkg="1.2.9", extra=("--siki",))
test("26. KART ESKİ + --siki -> çıkış 1", kod == 1)
# stdout saflığı: UYARI baskıları stderr'e gider
with yama(npm_son_surum=lambda *a, **k: "1.2.0", npm_kurulu_surum=lambda *a, **k: 1 / 0):
    kod, o, e = calistir(["--ozet-json", "--kart", str(yol26), "--cikti", str(kok26 / "r.md"), "--kok", str(kok26), "--ev", str(ev26)])
test("26. UYARI baskıları stderr'de, stdout tek JSON nesnesi", "UYARI: r26: denetim hatası" in e and json.loads(o) and o.strip().count("\n") == 0, (o, e))

# 26b. --ozet-json hiçbir dosya yazmaz
cikti26 = kok26 / "yazilmamali.md"
with yama(npm_son_surum=lambda *a, **k: "1.3.0"):
    calistir(["--ozet-json", "--kart", str(yol26), "--cikti", str(cikti26), "--kok", str(kok26), "--ev", str(ev26)])
    calistir(["--sema", "--ozet-json", "--kart", str(yol26), "--cikti", str(cikti26), "--kok", str(kok26), "--ev", str(ev26)])
test("26b. --ozet-json (düz ve --sema) rapor dosyası yazmaz", not cikti26.exists())
cikti26.write_text("eski"); os.utime(cikti26, (1000, 1000))
with yama(npm_son_surum=lambda *a, **k: "1.3.0"):
    calistir(["--ozet-json", "--kart", str(yol26), "--cikti", str(cikti26), "--kok", str(kok26), "--ev", str(ev26)])
test("26b. var olan rapor dosyası değişmez (içerik ve mtime)", cikti26.read_text() == "eski" and int(cikti26.stat().st_mtime) == 1000)

# 27. okunamayan --kart
(d25 / "bozuk.json").write_text("{yok")
kod, o, e = calistir(["--ozet-json", "--kart", str(d25 / "bozuk.json")])
test("27. okunamayan kart: durum sorun, çıkış 0", json.loads(o)["durum"] == "sorun" and kod == 0, o)
kod, o, e = calistir(["--ozet-json", "--siki", "--kart", str(d25 / "bozuk.json")])
test("27. okunamayan kart + --siki: çıkış 1", kod == 1)

# 28. rapor idempotansı
with yama(npm_son_surum=lambda *a, **k: "1.2.0"):
    argv28 = ["--kart", str(yol26), "--cikti", str(kok26 / "rapor28.md"), "--kok", str(kok26), "--ev", str(ev26)]
    calistir(argv28)
    os.utime(kok26 / "rapor28.md", (5000, 5000))
    calistir(argv28)
test("28. değişmeyen veride rapor yeniden yazılmaz", int((kok26 / "rapor28.md").stat().st_mtime) == 5000)
rapor_metni = (kok26 / "rapor28.md").read_text(encoding="utf-8")
test("28. mevcut tablo başlıkları aynen duruyor", "| Program | Tür | Karttaki | Kurulu | Son | Durum | Yerel değişiklik | Sabit sürümler |" in rapor_metni
     and "## Yerinde izlenen programlar (kaynak kopyası yok)" in rapor_metni)

# 29. mevcut davranış korunuyor (araclar/test.py'deki durum sözcükleri)
yd = pd.yerinde_durum
test("29. durum sözcükleri değişmedi", [yd("npm-global", "1.2.0", "1.2.0", "1.3.0"), yd("npm-global", "1.2.0", "1.2.1", "1.2.1"),
                                        yd("npm-global", "1.2.0", None, "1.3.0"), yd("npm-global", "1.2.0", "1.2.0", None),
                                        yd("git-checkout", SHA, SHA, SHA), yd("git-checkout", SHA, "b" * 40, "b" * 40)]
     == ["YENİ SÜRÜM VAR", "KART ESKİ", "bu bilgisayarda kurulu değil", "öğrenilemedi", "güncel", "KART ESKİ"])
test("29. durum() ve pin_karsilastir çıktıları değişmedi", pd.durum("0.5.0", "v0.5.0") == "güncel" and pd.durum("0.5.0", "v0.6.0") == "YENİ SÜRÜM VAR"
     and pd.pin_karsilastir({"numpy": "1.26.4", "torch": "2.2.2"}, {"numpy": "1.26.4", "torch": "2.3.0"}) == (1, ["torch: karttaki 2.2.2, kurulu 2.3.0"]))
with yama(git_okuma=lambda yol, *a: {"--show-toplevel": "/tmp/s\n", "HEAD": "s" * 40, "--porcelain": " M a\n?? b\n"}[a[-1]]):
    test("29. git_kurulu çıktısı değişmedi", pd.git_kurulu("/tmp/s") == ("s" * 40, 1, 1))

# gerçek kütüphane kartı kontrolleri (salt okuma, ağ yok)
doc_gercek, hata_gercek = pd.kart_yukle(KOK / "programlar.json")
b = pd.sema_denetle(doc_gercek, kok=KOK) if doc_gercek else [("HATA", "-", "-", hata_gercek)]
test("30. gerçek programlar.json: kart şeması 0 hata", not hatalar(b), b[:3])
# (gerçek kartlarda '--oncesi' içerik kontrolü dogrula.py'de UYARI; testte gerçek değer yok)
fk = {"sema": 2, "programlar": {}}
test("30. sahte veride sema_denetle: boş sözlükte HATA yok, çekirdek alanı eksik kartta HATA var",
     not hatalar(pd.sema_denetle(fk, kok=KOK, kaynaklar={}))
     and bool(hatalar(pd.sema_denetle({"sema": 2, "programlar": {"x": {}}}, kok=KOK, kaynaklar={}))),
     pd.sema_denetle({"sema": 2, "programlar": {"x": {}}}, kok=KOK, kaynaklar={}))
yazan = [ln for ln in (ARACLAR / "program-denetim.py").read_text(encoding="utf-8").splitlines()
         if ("write_text" in ln or "json_yaz" in ln or '"fetch"' in ln or '"pip"' in ln or '["npm"' in ln or '"install"' in ln)
         and not ln.strip().startswith("#")]
test("30. araç kodunda yazma/fetch/npm/pip çağrısı yok (rapor yazımı dışında)", len(yazan) == 1 and "hedef.write_text" in yazan[0], yazan)

# 31. rehber var olmayan komut bayrağını birinci seçenek olarak yazmıyor
pk_kod = (ARACLAR / "proje-kullanimi.py").read_text(encoding="utf-8")
rehber_metin = (KOK / "rehber" / "11-program-yonetimi.md").read_text(encoding="utf-8")
test("31. rehberdeki proje-kullanimi.py bayrakları kodda var",
     all(f'"{b}"' in pk_kod for b in set(re.findall(r"proje-kullanimi\.py (--[a-z-]+)", rehber_metin))),
     set(re.findall(r"proje-kullanimi\.py (--[a-z-]+)", rehber_metin)))

shutil.rmtree(TMP, ignore_errors=True)
print(f"{gecen}/{toplam} test geçti")
sys.exit(0 if gecen == toplam else 1)
