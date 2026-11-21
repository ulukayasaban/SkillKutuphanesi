#!/usr/bin/env python3
"""P14 testleri: skil başına bağımlılık (kaynaklar.json -> skill_bagimlilik) ve teknoloji_oto 'api-anahtari' deseni.
Kapsam: arsiv-yerlestir.py repo düzeyindeki 'bagimlilik'i varsayılan alır, 'skill_bagimlilik' {kaynak_yol: metin} o skill için
yerine geçer (registry + KAYNAK.md), yeniden çalıştırmada kalıcıdır, boş metin bağımlılığı kaldırır; dogrula.py anahtarı tanır,
registry'de karşılığı olmayan ya da işlenmemiş geçersiz kılmayı UYARI sayar; api-anahtari deseni gerçek anahtar/belirteç
kullanımını yakalar, tasarım/LLM/ödeme token'ı gibi metinleri yakalamaz.
Yalnız geçici klasör ve sahte veri: HOME geçici klasöre alınır, gerçek registry/kaynaklar/ev klasörü okunmaz ya da yazılmaz;
ağ kullanılmaz (kullanılırsa test düşer). Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import os
import re
import shutil
import sys
import tempfile
import urllib.request
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p14test-"))
os.environ["HOME"] = str(TMP / "home")          # modül içi Path.home() geçici klasöre baksın (ortak.py içe aktarılmadan ÖNCE)
(TMP / "home").mkdir()
sys.path.insert(0, str(ARACLAR))
SONUC = []


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-900:]}"))


def modul_yukle(ad, dosya):
    spec = importlib.util.spec_from_file_location(ad, ARACLAR / dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ay = modul_yukle("ay_p14", "arsiv-yerlestir.py")
dg = modul_yukle("dg_p14", "dogrula.py")


def yaz(yol, metin):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(metin, encoding="utf-8")


def yakala(f, *a, argv=None, **k):
    """(dönüş ya da SystemExit kodu, stdout+stderr)"""
    eski = sys.argv
    if argv is not None:
        sys.argv = argv
    o = io.StringIO()
    try:
        with contextlib.redirect_stdout(o), contextlib.redirect_stderr(o):
            try:
                r = f(*a, **k)
            except SystemExit as x:
                r = x.code if isinstance(x.code, int) else (0 if x.code is None else 1)
                if isinstance(x.code, str):
                    print(x.code)
    finally:
        sys.argv = eski
    return r, o.getvalue()


def ag_yasak(*a, **k):
    raise AssertionError("AĞ KULLANILDI")


# ================================================================== 1. api-anahtari deseni (ağsız, saf regex)
DESEN = ay.TEKNOLOJI_DESENLERI["api-anahtari"]


def eslesir(metin):
    return bool(re.search(DESEN, metin, re.I))


OLUMLU = ["Set OPENAI_API_KEY in your shell", "Pass your api key with --key", "needs an API-key", "apiKey: process.env.X",
          "Create a personal access token", "Authorization: Bearer $TOKEN", "send a bearer token", "accessToken from OAuth",
          "the auth token is read from .env", "export GITHUB_TOKEN=...", "HF_TOKEN must be set", "TWILIO_AUTH_TOKEN",
          "gh auth login --with-token", "az acr login --expose-token", "use service tokens for headless devices",
          "Token 只从环境变量读取", "read the token from the environment variable", "GitHub\ntoken and S3 credentials"]
OLUMSUZ = ["`ease:` token sets the curve", "Use design tokens for color and spacing", "max_new_tokens=512",
           "AutoTokenizer.from_pretrained(name)", "the purchase token from Play Billing", "output tokens cost more",
           "DEFAULT_IMAGE_TOKEN + prompt", "PAD_TOKEN id", "Every token counts", "tokenization of input text",
           "csrf token in the form", "semantic tokens in the theme"]
for m in OLUMLU:
    test(f"api-anahtari yakalar: {m!r}", eslesir(m))
for m in OLUMSUZ:
    test(f"api-anahtari yakalamaz: {m!r}", not eslesir(m))
test("api-anahtari tek yerde: API_ANAHTARI_DESENI", DESEN == ay.API_ANAHTARI_DESENI)

# ================================================================== 2. skil başına bağımlılık (sahte kütüphane kökü)
LIB = TMP / "lib"
GECICI = LIB / ".gecici"
REG = LIB / "registry.json"
ARSIV = LIB / "arsiv"
REPO = "ornek/coklu"
REPO_BAG = "Ana skill X servisinin API anahtarını ister (X_API_KEY)."
ALT_BAG = "Yalnız yerel araç: ffmpeg ve Python; anahtar gerekmez."
KAYIT = {"repo": REPO, "tur": "koleksiyon", "bolum": "arsiv", "oncelik": 2, "bagimlilik": REPO_BAG,
         "skill_bagimlilik": {"skills/alt": ALT_BAG}}


def kaynaklar_yaz(kayitlar):
    yaz(LIB / "kaynaklar.json", json.dumps({"ayna_klasorler": [], "max_dosya_mb": 5, "konum_haric": [], "skill_ici_haric": [],
                                            "arsivden_cikarilanlar": [], "repolar": kayitlar}, ensure_ascii=False, indent=2))


kaynaklar_yaz([KAYIT])
yaz(LIB / "kategoriler.json", json.dumps({"alanlar": {"d-ai-otomasyon": {"kategoriler": {"04-skill-plugin-yazimi": "x"}}}}))
yaz(LIB / "kategori-kurallari.json", json.dumps({"ad_kurallari": [], "yol_kurallari": [], "repo_varsayilan": {}}))
yaz(LIB / "ucret-siniflandirma.json", json.dumps({"siniflar": {}}))
yaz(LIB / "gelistiriciler.json", json.dumps({"repolar": {}}))
(LIB / "notlar").mkdir()


def fm(ad):
    return f"---\nname: {ad}\ndescription: Test skili {ad}: ornek isler icin kullan, baska islerde kullanma.\n---\n"


kok_dizin = GECICI / "cekilen" / "ornek__coklu"
yaz(kok_dizin / "ana" / "SKILL.md", fm("ana") + "Set X_API_KEY before running.\n")
yaz(kok_dizin / "alt" / "SKILL.md", fm("alt") + "Animate with `ease:` token sets the curve.\n")


def manifest_kaydi(ad, yol, ust=None):
    return {"repo": REPO, "tur": "koleksiyon", "bolum": "arsiv", "oncelik": 2, "kimlik": "ornek__coklu", "commit": "b" * 40, "lisans": "MIT",
            "klasor_adi": ad, "kaynak_yol": yol, "asil_ad": None, "ust_skill": ust, "aynalar": [], "atlanan_dosyalar": [],
            "varyantlar": {}, "varyant_yollari": {}, "ad": ad, "aciklama": ad, "bagimlilik": REPO_BAG,  # kaynak-cek repo metnini yazar
            "beklenen_dosya": 1, "inen_dosya": 1, "varyant_eksik": [], "yerel": f"cekilen/ornek__coklu/{ad}"}


yaz(GECICI / "cekilen" / "manifest.json", json.dumps({
    "kayitlar": [manifest_kaydi("ana", ""), manifest_kaydi("alt", "skills/alt", ust="ana")], "bilesenler": [],
    "denetim": {REPO: {"commit": "b" * 40, "skill_md": {"SKILL.md": "secildi", "skills/alt/SKILL.md": "secildi"}}}}))

for ad, deger in dict(KOK=LIB, ARSIV=ARSIV, GECICI=GECICI, REGISTRY=REG, KATEGORILER=LIB / "kategoriler.json",
                      KURALLAR=LIB / "kategori-kurallari.json", GELISTIRICILER=LIB / "gelistiriciler.json",
                      TREND=LIB / "trend.json").items():
    setattr(ay, ad, deger)
_urlopen = urllib.request.urlopen
urllib.request.urlopen = ag_yasak


def yerlestir():
    return yakala(ay.main, argv=["arsiv-yerlestir.py"])


def kayit(ad):
    d = json.loads(REG.read_text(encoding="utf-8"))
    return next((s for s in d["skiller"] if s["ad"] == ad), None)


def kaynak_md(s):
    return (LIB / s["yol"] / "KAYNAK.md").read_text(encoding="utf-8") if s else ""


def dogrula_uyarilari():
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    return h, u


try:
    test("skill_bagimliligi: geçersiz kılma kaynak_yol ile eşleşir",
         ay.skill_bagimliligi({"repo": REPO, "kaynak_yol": "skills/alt", "bagimlilik": REPO_BAG},
                              ay.skill_bagimlilik_ozel([KAYIT])) == ALT_BAG)
    test("skill_bagimliligi: başka yol repo varsayılanını alır",
         ay.skill_bagimliligi({"repo": REPO, "kaynak_yol": "", "bagimlilik": REPO_BAG}, ay.skill_bagimlilik_ozel([KAYIT])) == REPO_BAG)
    test("skill_bagimliligi: aynı yol başka repoda etkilenmez",
         ay.skill_bagimliligi({"repo": "baska/repo", "kaynak_yol": "skills/alt", "bagimlilik": None},
                              ay.skill_bagimlilik_ozel([KAYIT])) is None)

    kod, cikti = yerlestir()
    ana, alt = kayit("ana"), kayit("alt")
    test("arsiv-yerlestir çalıştı (çıkış 0, iki kayıt)", not kod and ana and alt, cikti)
    test("repo varsayılanı: kök skill repo metnini alır", ana and ana["bagimlilik"] == REPO_BAG, ana)
    test("geçersiz kılma: alt skill kendi metnini alır", alt and alt["bagimlilik"] == ALT_BAG, alt)
    test("KAYNAK.md geçersiz kılınan metni yazar, repo metnini yazmaz",
         f"**Bağımlılık:** {ALT_BAG}" in kaynak_md(alt) and REPO_BAG not in kaynak_md(alt), kaynak_md(alt))
    test("KAYNAK.md kök skillde repo metnini yazar", f"**Bağımlılık:** {REPO_BAG}" in kaynak_md(ana), kaynak_md(ana))
    test("api-anahtari: kök skillde var (X_API_KEY)", ana and "api-anahtari" in ana["teknoloji_oto"], ana and ana["teknoloji_oto"])
    test("api-anahtari: '`ease:` token' satırı etiket vermez", alt and "api-anahtari" not in alt["teknoloji_oto"],
         alt and alt["teknoloji_oto"])
    h, u = dogrula_uyarilari()
    test("dogrula: skill_bagimlilik bilinen anahtar, işlenmiş geçersiz kılma uyarı vermez",
         not h and not [x for x in u if "skill_bagimlilik" in x or "bilinmeyen anahtar" in x], (h, u))

    # registry'ye elle yazılan değer bir sonraki çalışmada ezilir; kalıcı olan kaynaklar.json'daki geçersiz kılmadır
    d = json.loads(REG.read_text(encoding="utf-8"))
    for s in d["skiller"]:
        if s["ad"] == "alt":
            s["bagimlilik"] = "elle yazıldı"
    REG.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    h, u = dogrula_uyarilari()
    test("dogrula: registry geçersiz kılmayla uyuşmuyorsa UYARI (işlenmemiş)",
         any("registry'ye işlenmemiş" in x and "skills/alt" in x for x in u), u)
    kod, cikti = yerlestir()
    alt = kayit("alt")
    test("yeniden çalıştırma: geçersiz kılma kalıcı (elle değer ezildi, doğru metin geri geldi)",
         not kod and alt and alt["bagimlilik"] == ALT_BAG, (cikti, alt))

    # boş metin = bu skill için bağımlılık yok (repo metnine düşmez)
    kaynaklar_yaz([{**KAYIT, "skill_bagimlilik": {"skills/alt": ""}}])
    kod, cikti = yerlestir()
    alt = kayit("alt")
    test("boş geçersiz kılma: bağımlılık yok, KAYNAK.md'de Bağımlılık satırı yok",
         not kod and alt and alt["bagimlilik"] is None and "Bağımlılık" not in kaynak_md(alt), (cikti, alt and alt["bagimlilik"]))
    test("boş geçersiz kılma: kök skill repo metnini korur", kayit("ana")["bagimlilik"] == REPO_BAG)

    # geçersiz kılma alanı kaldırılınca repo varsayılanına dönülür
    kaynaklar_yaz([{k: v for k, v in KAYIT.items() if k != "skill_bagimlilik"}])
    kod, cikti = yerlestir()
    test("geçersiz kılma kaldırılınca alt skill repo metnine döner", not kod and kayit("alt")["bagimlilik"] == REPO_BAG, cikti)

    # registry'de karşılığı olmayan anahtar ve bozuk biçim UYARI
    kaynaklar_yaz([{**KAYIT, "skill_bagimlilik": {"skills/tasindi": "x"}}])
    h, u = dogrula_uyarilari()
    test("dogrula: registry'de olmayan kaynak_yol anahtarı UYARI", any("registry'de yok" in x and "skills/tasindi" in x for x in u), u)
    kaynaklar_yaz([{**KAYIT, "skill_bagimlilik": ["skills/alt"]}])
    h, u = dogrula_uyarilari()
    test("dogrula: sözlük olmayan skill_bagimlilik UYARI", any("biçiminde değil" in x for x in u), u)
    test("dogrula: bu denetimler HATA üretmez", not h, h)
finally:
    urllib.request.urlopen = _urlopen
    shutil.rmtree(TMP, ignore_errors=True)

gecen = sum(1 for _, ok in SONUC if ok)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
