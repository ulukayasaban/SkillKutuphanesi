#!/usr/bin/env python3
"""P13 testleri: siteden alınan skiller (yerel kaynak T8, site/<ad>/) ve site takibi (K-57).
Kapsam: site-takip.py (AYNI, DEĞİŞTİ, önek karşılaştırması, yönlendirmeden gerçeğe dönüşme, erişilemedi, 3xx/404/403, rapor başlığı,
--yazmadan, --indir, --siki, istek başlıkları, kayıt şeması ve zorunluluklar), dogrula.py site denetimi (HATA/UYARI), aylik-ozet.py
site takibi satırı, arsiv-guncelle.py zincir çağrısı, kendi/ ile site/ ayrımı (kaynak-cek ağsız, arsiv-yerlestir sahip/lisans skill
başına, T7 kayıtları değişmez, kapsam-denetimi, aylık kaynak raporu, gelistirici-bilgisi).
Yalnız geçici klasör ve sahte veri: HOME geçici klasöre alınır, gerçek kütüphane ve ev klasörü okunmaz ya da yazılmaz; gerçek ağ
kullanılmaz (urllib.request.urlopen ve site-takip._ac sahte). Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import types
import urllib.error
import urllib.request
from datetime import date, timedelta
from email.message import Message
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p13test-"))
os.environ["HOME"] = str(TMP / "home")          # Path.home() geçici klasöre baksın (ortak.py içe aktarılmadan ÖNCE)
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


import ortak  # noqa: E402

st = modul_yukle("st_p13", "site-takip.py")
dg = modul_yukle("dg_p13", "dogrula.py")
ao = modul_yukle("ao_p13", "aylik-ozet.py")
kc = modul_yukle("kc_p13", "kaynak-cek.py")
ay = modul_yukle("ay_p13", "arsiv-yerlestir.py")
kd = modul_yukle("kd_p13", "kapsam-denetimi.py")
ag = modul_yukle("ag_p13", "arsiv-guncelle.py")
gb = modul_yukle("gb_p13", "gelistirici-bilgisi.py")


def yaz(yol, metin):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    (yol.write_bytes(metin) if isinstance(metin, bytes) else yol.write_text(metin, encoding="utf-8"))


def sha(b):
    return hashlib.sha256(b).hexdigest()


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


def agac_izi(*klasorler):
    iz = {}
    for k in klasorler:
        for p in sorted(Path(k).rglob("*")) if Path(k).exists() else []:
            if p.is_file():
                iz[str(p)] = sha(p.read_bytes())
    return iz


# ---------------------------------------------------------------- ağ yasak + sahte HTTP
AG_CAGRILARI = []


def ag_yasak(*a, **k):
    AG_CAGRILARI.append((a, k))
    raise AssertionError("AĞ KULLANILDI")


_urlopen = urllib.request.urlopen
urllib.request.urlopen = ag_yasak

SITE = "https://ornek.test/stil/"
GOVDE = {}       # url -> (kod, bytes, konum)
ISTEKLER = []


class _Yanit:
    def __init__(self, kod, govde):
        self.status, self._g = kod, govde

    def read(self, n=-1):
        return self._g

    def getcode(self):
        return self.status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def sahte_ac(istek, zaman_asimi):
    ISTEKLER.append({"url": istek.full_url, "yontem": istek.get_method(), "basliklar": dict(istek.header_items()), "zaman": zaman_asimi})
    d = GOVDE.get(istek.full_url)
    if d is None:
        raise urllib.error.URLError("ağ yok (sahte)")
    if d == "zaman":
        raise TimeoutError("timed out")
    kod, govde, konum = d
    if kod >= 300:
        h = Message()
        if konum:
            h["Location"] = konum
        raise urllib.error.HTTPError(istek.full_url, kod, "x", h, io.BytesIO(govde))
    return _Yanit(kod, govde)


st._ac = sahte_ac

# ---------------------------------------------------------------- sahte kütüphane: kendi/ (T7) + site/ (T8)
LIB = TMP / "lib"
SKILL_SITE = b"---\nname: stil\ndescription: Ornek site skili: stil cikarma isleri icin kullan, baska islerde kullanma.\n---\nsite metni\n"
EK = b"\n---\n## Ready-made styles (added by the library)\n"
UZUN = b"uzun prompt cam\n"
YON = b"<html>yonlendirme</html>"
ANA = b"<html>ana sayfa</html>"
yaz(LIB / "site" / "stil" / "SKILL.md", SKILL_SITE + EK)
yaz(LIB / "site" / "stil" / "references" / "cam.txt", UZUN)
yaz(LIB / "site" / "stil" / "KAYNAK.md", "kaynak notu\n")
yaz(LIB / "site" / "README.md", "site klasörü\n")
yaz(LIB / "kendi" / "kendi-skil" / "SKILL.md",
    "---\nname: kendi-skil\ndescription: Kullanicinin kendi test skili: ornek isler icin kullan, baska islerde kullanma.\n---\nkendi\n")
yaz(LIB / "arsiv" / "x" / "SKILL.md", "arsiv\n")
T7 = {"repo": "yerel/kendi", "tip": "T7", "oncelik": 1, "yerel": "kendi", "lisans": "Kendi (özel)", "eklendi": "2026-11-12",
      "onay": {"kim": "kullanıcı", "tarih": "2026-11-12"}}
T8 = {"repo": "yerel/site", "tip": "T8", "oncelik": 1, "yerel": "site", "eklendi": "2026-11-15",
      "onay": {"kim": "kullanıcı", "tarih": "2026-11-15"}}


def kaynaklar_yaz(kayitlar):
    yaz(LIB / "kaynaklar.json", json.dumps({"ayna_klasorler": [], "max_dosya_mb": 5, "konum_haric": [r"(^|/)tests?/"],
                                            "skill_ici_haric": [r"(^|/)node_modules/", r"(^|/)\.git/"], "arsivden_cikarilanlar": [],
                                            "repolar": kayitlar}, ensure_ascii=False, indent=2))


def dosyalar():
    return [
        {"ad": "skill", "url": SITE + "stil-skill.md", "tur": "asil", "bayt": len(SKILL_SITE), "sha256": sha(SKILL_SITE),
         "karsilastirma": "onek", "yerel_dosya": "SKILL.md"},
        {"ad": "ana-sayfa", "url": SITE, "tur": "asil", "bayt": len(ANA), "sha256": sha(ANA), "etkiler": ["references/kartlar/"]},
        {"ad": "cam", "url": SITE + "uzun/cam.txt", "tur": "asil", "bayt": len(UZUN), "sha256": sha(UZUN), "karsilastirma": "tam",
         "yerel_dosya": "references/cam.txt"},
        {"ad": "bilim", "url": SITE + "uzun/bilim.txt", "tur": "yonlendirme", "bayt": len(YON), "sha256": sha(YON)},
        {"ad": "ascii", "url": SITE + "uzun/ascii.txt", "tur": "yonlendirme", "bayt": len(YON), "sha256": sha(YON)},
    ]


def kayit(**deg):
    s = {"skill": "stil", "kaynak": "yerel/site", "yerel": "site/stil", "site": SITE, "sahip": "Ornek Yazar", "sahip_tipi": "kisi",
         "sahip_url": "https://ornek.test/", "lisans": "belirtilmemiş", "resmi_kaynak": False, "kayit_tarihi": "2026-11-15",
         "dosyalar": dosyalar()}
    s.update(deg)
    return s


def site_yaz(skiller):
    yaz(LIB / "site-takip.json", json.dumps({"surum": 1, "zaman_asimi_sn": 7, "skiller": skiller}, ensure_ascii=False, indent=2))


def sitenin_hali(**deg):
    """Varsayılan: hepsi aynı. bilim: 302 yönlendirme; ascii: 404 ama gövde kayıttaki yönlendirme sayfası."""
    GOVDE.clear()
    GOVDE.update({SITE + "stil-skill.md": (200, SKILL_SITE, None), SITE: (200, ANA, None), SITE + "uzun/cam.txt": (200, UZUN, None),
                  SITE + "uzun/bilim.txt": (302, b"<html>302</html>", SITE), SITE + "uzun/ascii.txt": (404, YON, None)})
    GOVDE.update(deg)


def calis(*args):
    return yakala(st.calistir, list(args), kok=LIB)


def rapor():
    return st.rapor_oku(LIB)


kaynaklar_yaz([T7, T8])
site_yaz([kayit()])

try:
    # ================================================================== 1. hepsi AYNI (önek, tam, 302 ve 404-gövdeli yönlendirme)
    sitenin_hali()
    once = agac_izi(LIB / "site", LIB / "kendi", LIB / "arsiv")
    kod, cikti = calis()
    r = rapor()
    test("site-takip: hepsi AYNI, çıkış 0", kod == 0 and r and r["sayilar"] == {"AYNI": 5, "DEĞİŞTİ": 0, "YENİ İÇERİK": 0, "ERİŞİLEMEDİ": 0}, cikti)
    md = (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8")
    test("önek karşılaştırması: SKILL.md'nin sonundaki kütüphane eki farkı yaratmaz, yerel kopya uyumlu",
         "| skill | asil | **AYNI** |" in md and "uyumlu (`SKILL.md`, onek)" in md, md)
    test("yönlendirme satırları 'gerçek dosya değil' diye durur (302 ve 404 + kayıttaki gövde)",
         md.count("yönlendirme, gerçek dosya değil") == 2, md)
    test("rapor başlığı makine okunur (zaman, sayılar, skill başına)", r and r["skiller"]["stil"]["AYNI"] == 5 and "zaman" in r, r)
    test("araç site/, kendi/ ve arsiv/ içine yazmadı", agac_izi(LIB / "site", LIB / "kendi", LIB / "arsiv") == once)
    test("istekler yalnız GET, genel User-Agent, kimlik/çerez başlığı yok, zaman aşımı kayıttan",
         ISTEKLER and all(i["yontem"] == "GET" and i["zaman"] == 7 and "site-takip" in i["basliklar"].get("User-agent", "")
                          and not {"Authorization", "Cookie"} & set(i["basliklar"]) for i in ISTEKLER), ISTEKLER[:2])
    test("yönlendirme kaydı izlenmez (302 hedefine ikinci istek yok)", sum(1 for i in ISTEKLER if i["url"] == SITE) == 1, ISTEKLER)

    # ================================================================== 2. DEĞİŞTİ
    sitenin_hali(**{SITE + "uzun/cam.txt": (200, b"yeni cam metni\n", None)})
    kod, cikti = calis()
    r = rapor()
    test("asıl dosya değişince DEĞİŞTİ, çıkış yine 0", kod == 0 and r["sayilar"]["DEĞİŞTİ"] == 1 and r["degisen"] == ["stil: cam DEĞİŞTİ"], (cikti, r))
    md = (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8")
    test("rapor yeni özeti verir, skill kendiliğinden güncellenmez", sha(b"yeni cam metni\n") in md and UZUN == (LIB / "site" / "stil" / "references" / "cam.txt").read_bytes(), md)
    kod, cikti = calis("--siki")
    test("--siki: değişiklik varsa çıkış 1", kod == 1, cikti)
    sitenin_hali(**{SITE + "stil-skill.md": (200, SKILL_SITE + b"sitede yeni satir\n", None)})
    kod, cikti = calis()
    test("önekli dosya sitede değişince DEĞİŞTİ (yerel kopya kayıtla hâlâ uyumlu)",
         rapor()["degisen"] == ["stil: skill DEĞİŞTİ"] and "uyumlu" in (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8"), cikti)

    # ================================================================== 3. yönlendirmeden gerçek dosyaya
    sitenin_hali(**{SITE + "uzun/bilim.txt": (200, b"bilim icin gercek uzun prompt\n", None)})
    kod, cikti = calis()
    r = rapor()
    test("yönlendirme gerçek içeriğe dönüşünce YENİ İÇERİK", r["sayilar"]["YENİ İÇERİK"] == 1 and r["degisen"] == ["stil: bilim YENİ İÇERİK"], (cikti, r))
    sitenin_hali(**{SITE + "uzun/cam.txt": (200, YON, None)})
    calis()
    md = (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8")
    test("asıl dosya yönlendirme sayfasına dönüşürse DEĞİŞTİ ('kaldırılmış olabilir')", "kaldırılmış olabilir" in md and rapor()["sayilar"]["DEĞİŞTİ"] == 1, md)
    sitenin_hali(**{SITE + "uzun/cam.txt": (301, b"", SITE + "yeni/cam.txt"), SITE + "yeni/cam.txt": (200, UZUN, None)})
    calis()
    test("asıl dosya başka adrese taşınıp içerik aynıysa AYNI (yönlendirme notuyla)",
         rapor()["sayilar"]["AYNI"] == 5 and "yönlendiriliyor" in (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8"))

    # ================================================================== 4. erişilemedi: KAYIP sayılmaz
    GOVDE.clear()
    kod, cikti = calis()
    r = rapor()
    test("ağ yoksa hepsi ERİŞİLEMEDİ, çıkış 0, KAYIP önerilmez",
         kod == 0 and r["sayilar"]["ERİŞİLEMEDİ"] == 5 and "KAYIP olarak" not in cikti and "KAYIP sayılmaz" in
         (LIB / "notlar" / "site-takip.md").read_text(encoding="utf-8"), cikti)
    sitenin_hali(**{SITE: (403, b"yasak", None), SITE + "uzun/cam.txt": (503, b"", None), SITE + "stil-skill.md": "zaman",
                    SITE + "uzun/bilim.txt": (404, b"<html>baska 404</html>", None)})
    calis()
    r = rapor()
    test("403, 503, zaman aşımı ve gövdesi farklı 404 ERİŞİLEMEDİ (DEĞİŞTİ değil)",
         r["sayilar"]["ERİŞİLEMEDİ"] == 4 and r["sayilar"]["DEĞİŞTİ"] == 0 and sorted(r["erisilemeyen"]) ==
         ["stil: ana-sayfa", "stil: bilim", "stil: cam", "stil: skill"], r)

    # ================================================================== 5. --yazmadan, --indir
    (LIB / "notlar" / "site-takip.md").unlink()
    sitenin_hali(**{SITE + "uzun/cam.txt": (200, b"yeni cam\n", None)})
    kod, cikti = calis("--yazmadan")
    test("--yazmadan rapor dosyası yazmaz", not (LIB / "notlar" / "site-takip.md").exists() and "DEĞİŞTİ" in cikti, cikti)
    kod, cikti = calis("--yazmadan", "--indir")
    hedef = TMP / "home" / "Documents" / "Claude" / "deneme" / f"site-takip-{date.today().isoformat()}"
    test("--indir yalnız değişen dosyayı kütüphane dışına, ev klasöründeki deneme klasörüne yazar",
         (hedef / "stil" / "cam.txt").read_bytes() == b"yeni cam\n" and len(list((hedef / "stil").iterdir())) == 1
         and json.loads((hedef / "OZETLER.json").read_text())[0]["sha256"] == sha(b"yeni cam\n"), cikti)
    calis("--yazmadan", "--indir")
    test("ikinci indirme yeni boş klasör açar (-2), öncekinin üstüne yazmaz", (hedef.parent / (hedef.name + "-2") / "stil" / "cam.txt").exists())
    test("indirme kütüphanenin içine bir şey yazmadı", agac_izi(LIB / "site", LIB / "kendi", LIB / "arsiv") == once)
    sitenin_hali()
    kod, cikti = calis("--yazmadan", "--indir")
    test("değişiklik yoksa --indir klasör açmaz", "İndirilecek değişen dosya yok" in cikti and not (hedef.parent / (hedef.name + "-3")).exists(), cikti)

    # ================================================================== 6. kayıt şeması ve zorunluluklar
    h, u = st.kayit_denetle(json.loads((LIB / "site-takip.json").read_text()), LIB)
    test("geçerli kayıtta 0 hata 0 uyarı", not h and not u, (h, u))
    bozuk = kayit()
    del bozuk["sahip"]
    bozuk["dosyalar"][0] = dict(bozuk["dosyalar"][0], sha256="XYZ", karsilastirma="yarim")
    bozuk["dosyalar"][2] = {k: v for k, v in bozuk["dosyalar"][2].items() if k != "yerel_dosya"} | {"karsilastirma": "onek"}
    bozuk["fazla"] = 1
    site_yaz([bozuk])
    kod, cikti = calis()
    test("şema hatası: eksik sahip, bozuk sha256, bilinmeyen karşılaştırma, önekte yerel_dosya yok -> çıkış 2, takip yapılmaz",
         kod == 2 and "eksik alan: sahip" in cikti and "sha256 64 haneli" in cikti and "karsilastirma tam, onek" in cikti
         and "'onek' için yerel_dosya" in cikti and "bilinmeyen alan: fazla" in cikti and "takip yapılmadı" in cikti, cikti)
    site_yaz([])
    h, u = st.kayit_denetle(json.loads((LIB / "site-takip.json").read_text()), LIB)
    test("site/<ad>/ için kayıt yoksa HATA (kayıt zorunlu)", any("site/stil" in x and "zorunlu" in x for x in h), h)
    (LIB / "site-takip.json").unlink()
    h, u = st.kayit_denetle(None, LIB)
    test("site-takip.json hiç yokken site skili varsa HATA", any("site-takip.json yok" in x for x in h), h)
    yaz(LIB / "kendi" / "kendi-skil" / "x.txt", "x")
    site_yaz([kayit(), kayit(skill="kendi-skil", yerel="kendi/kendi-skil")])
    h, u = st.kayit_denetle(json.loads((LIB / "site-takip.json").read_text()), LIB)
    test("kendi/ altındaki skile site kaydı yazılırsa HATA (yanlış yer)", any("kendi/" in x and "K-57" in x for x in h), h)
    site_yaz([kayit(kaynak="yerel/kendi")])
    h, u = st.kayit_denetle(json.loads((LIB / "site-takip.json").read_text()), LIB)
    test("kayıt T8 olmayan kaynağı gösterirse HATA", any("T8" in x for x in h), h)
    yaz(LIB / "site" / "stil" / "references" / "cam.txt", b"elle degisti\n")
    site_yaz([kayit()])
    h, u = st.kayit_denetle(json.loads((LIB / "site-takip.json").read_text()), LIB)
    test("yerel kopya kayıttaki özetle uyuşmazsa UYARI (HATA değil)", not h and any("uyuşmuyor" in x for x in u), (h, u))
    yaz(LIB / "site" / "stil" / "references" / "cam.txt", UZUN)

    # ================================================================== 7. dogrula.py site denetimi
    (LIB / "araclar").mkdir(exist_ok=True)
    shutil.copy2(ARACLAR / "site-takip.py", LIB / "araclar" / "site-takip.py")
    shutil.copy2(ARACLAR / "ortak.py", LIB / "araclar" / "ortak.py")
    h, u = [], []
    dg._e7_site_takip(LIB, h, u)
    test("dogrula: geçerli site kaydında hata yok", not h, h)
    site_yaz([])
    h, u = [], []
    dg._e7_site_takip(LIB, h, u)
    test("dogrula: site skilinin kaydı yoksa HATA", any("site takibi:" in x and "zorunlu" in x for x in h), h)
    yaz(LIB / "site-takip.json", "{bozuk")
    h, u = [], []
    dg._e7_site_takip(LIB, h, u)
    test("dogrula: site-takip.json ayrışmıyorsa HATA", any("site-takip.json okunamadı" in x for x in h), h)
    site_yaz([kayit()])
    test("dogrula: rapor dosyası .gitignore kalıplarında", "/notlar/site-takip.md" in dg.GITIGNORE_KALIPLARI)

    # ================================================================== 8. aylik-ozet site satırı (ağsız)
    bugun = date.today()

    def ozet_raporu(say, gun=0, degisen=(), erisilemeyen=()):
        meta = {"zaman": (bugun - timedelta(days=gun)).isoformat() + "T10:00:00+03:00", "sayilar": say, "skiller": {},
                "degisen": list(degisen), "erisilemeyen": list(erisilemeyen)}
        yaz(LIB / "notlar" / "site-takip.md", f"<!-- site-takip: {json.dumps(meta, ensure_ascii=False)} -->\n# Site takibi\n")

    ozet_raporu({"AYNI": 5, "DEĞİŞTİ": 0, "YENİ İÇERİK": 0, "ERİŞİLEMEDİ": 0})
    k = ao.site_takip_kontrol(LIB, bugun)
    test("aylik-ozet: değişiklik yoksa temiz, karar yok", k["durum"] == "temiz" and not k["karar_bekleyen"] and "DEĞİŞTİ 0" in k["satirlar"][0], k)
    ozet_raporu({"AYNI": 3, "DEĞİŞTİ": 1, "YENİ İÇERİK": 1, "ERİŞİLEMEDİ": 0}, degisen=["stil: cam DEĞİŞTİ", "stil: bilim YENİ İÇERİK"])
    k = ao.site_takip_kontrol(LIB, bugun)
    test("aylik-ozet: DEĞİŞTİ/YENİ İÇERİK karar bekleyenlere girer (tarih ve sayı ile)",
         len(k["karar_bekleyen"]) == 1 and bugun.isoformat() in k["karar_bekleyen"][0] and "1 dosya değişti" in k["karar_bekleyen"][0]
         and "stil: cam" in k["karar_bekleyen"][0], k)
    ozet_raporu({"AYNI": 0, "DEĞİŞTİ": 0, "YENİ İÇERİK": 0, "ERİŞİLEMEDİ": 5}, erisilemeyen=["stil: skill"])
    k = ao.site_takip_kontrol(LIB, bugun)
    test("aylik-ozet: ERİŞİLEMEDİ dikkat olur, KAYIP kararı sorulmaz",
         k["durum"] == "dikkat" and not k["karar_bekleyen"] and "KAYIP sayılmaz" in " ".join(k["dikkat_satirlar"]), k)
    ozet_raporu({"AYNI": 5, "DEĞİŞTİ": 0, "YENİ İÇERİK": 0, "ERİŞİLEMEDİ": 0}, gun=60)
    test("aylik-ozet: rapor 45 günden eskiyse dikkat", ao.site_takip_kontrol(LIB, bugun)["durum"] == "dikkat")
    (LIB / "notlar" / "site-takip.md").unlink()
    test("aylik-ozet: rapor yoksa temiz (çökmez)", ao.site_takip_kontrol(LIB, bugun)["durum"] == "temiz")

    # ================================================================== 9. arsiv-guncelle zincir çağrısı
    cagrilar = []
    ag.KOK = LIB
    gercek_run = ag.subprocess.run
    ag.subprocess = types.SimpleNamespace(run=lambda a, **k: cagrilar.append(a) or types.SimpleNamespace(
        returncode=0, stdout="  DEĞİŞTİ      cam\nSite takibi: AYNI 4 · DEĞİŞTİ 1\nbaşka satır\n", stderr=""),
        TimeoutExpired=ag.subprocess.TimeoutExpired, SubprocessError=ag.subprocess.SubprocessError,
        CalledProcessError=ag.subprocess.CalledProcessError, DEVNULL=ag.subprocess.DEVNULL)
    r, c = yakala(ag._site_takip_calistir)
    test("aylık zincir site-takip.py'yi çağırır ve sonucu özetler", cagrilar and cagrilar[-1][-1].endswith("site-takip.py")
         and "Site takibi: AYNI 4" in c and "DEĞİŞTİ" in c and "başka satır" not in c, (cagrilar, c))
    r, c = yakala(ag._site_takip_calistir, kuru=True)
    test("kuru koşuda --yazmadan verilir", cagrilar[-1][-1] == "--yazmadan", cagrilar[-1])
    ag.subprocess.run = lambda a, **k: types.SimpleNamespace(returncode=2, stdout="HATA: kayıt\n", stderr="")
    r, c = yakala(ag._site_takip_calistir)
    test("kayıt hatası zinciri durdurmaz, UYARI basar", r == 2 and "UYARI: site takibi çıkış 2" in c, c)
    (LIB / "araclar" / "site-takip.py").unlink()
    r, c = yakala(ag._site_takip_calistir)
    test("araç yoksa BİLGİ ile atlanır", r is None and "BİLGİ" in c, c)

    # ================================================================== 10. kendi/ ve site/ ayrımı: çekme, yerleştirme, kapsam, aylık rapor
    GECICI = LIB / ".gecici"
    REG = LIB / "registry.json"
    yaz(LIB / "kategoriler.json", json.dumps({"alanlar": {"d-ai-otomasyon": {"kategoriler": {"04-skill-plugin-yazimi": "x"}}}}))
    yaz(LIB / "kategori-kurallari.json", json.dumps({"ad_kurallari": [], "yol_kurallari": [], "repo_varsayilan": {}}))
    yaz(LIB / "ucret-siniflandirma.json", json.dumps({"siniflar": {}}))
    yaz(LIB / "gelistiriciler.json", json.dumps({"repolar": {}}))
    shutil.rmtree(LIB / "arsiv")
    for m, kw in ((kc, dict(GECICI=GECICI, KAYNAKLAR=LIB / "kaynaklar.json", KOK=LIB, repo_agaci=ag_yasak, repo_lisansi=ag_yasak,
                            klon_dosyalari_al=ag_yasak, indir=ag_yasak)),
                  (ay, dict(KOK=LIB, ARSIV=LIB / "arsiv", GECICI=GECICI, REGISTRY=REG, KATEGORILER=LIB / "kategoriler.json",
                            KURALLAR=LIB / "kategori-kurallari.json", GELISTIRICILER=LIB / "gelistiriciler.json", TREND=LIB / "trend.json")),
                  (kd, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG, repo_agaci=ag_yasak)),
                  (ag, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG, gh_hazir=lambda: (True, 5000, ""), gh_api=ag_yasak,
                            etkilenen_projeler=lambda r: {})),
                  (gb, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", gh_api=ag_yasak))):
        for a, v in kw.items():
            setattr(m, a, v)
    ag.subprocess = types.SimpleNamespace(run=lambda *a, **k: types.SimpleNamespace(returncode=0, stdout="", stderr=""),
                                          CalledProcessError=Exception)
    AG_CAGRILARI.clear()
    k1, c1 = yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])
    k2, c2 = yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/site"])
    man = json.loads((GECICI / "cekilen" / "manifest.json").read_text(encoding="utf-8"))
    test("kaynak-cek: yerel/site (T8) ağsız çekildi, yerel/kendi ile yan yana",
         not k1 and not k2 and sorted((x["repo"], x["tip"], x["klasor_adi"]) for x in man["kayitlar"]) ==
         [("yerel/kendi", "T7", "kendi-skil"), ("yerel/site", "T8", "stil")] and not AG_CAGRILARI, (c1, c2))
    test("site/README.md skill sayılmadı", "site/README.md" not in json.dumps(man["denetim"]), man["denetim"])
    kod, cikti = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    d = json.loads(REG.read_text(encoding="utf-8"))
    s8 = next((x for x in d["skiller"] if x["repo"] == "yerel/site"), {})
    s7 = next((x for x in d["skiller"] if x["repo"] == "yerel/kendi"), {})
    test("arsiv-yerlestir: site skili T8, lisans ve sahip skill başına site-takip.json'dan",
         not kod and s8.get("tip") == "T8" and s8.get("lisans") == "belirtilmemiş" and s8.get("gelistirici", {}).get("sahip") == "Ornek Yazar"
         and s8["gelistirici"].get("ana_sayfa") == SITE and s8["gelistirici"].get("resmi_kaynak") is False, (cikti, s8.get("gelistirici")))
    test("arsiv-yerlestir: kendi skili 'Kendi (özel)' ve 'kullanıcı' olarak kaldı (site bilgisi sızmadı)",
         s7.get("lisans") == "Kendi (özel)" and s7.get("gelistirici", {}).get("sahip") == "kullanıcı", s7.get("gelistirici"))
    kmd = (LIB / s8["yol"] / "KAYNAK.md").read_text(encoding="utf-8") if s8 else ""
    test("site skilinin KAYNAK.md'si siteyi ve site/ klasörünü anlatır, GitHub adresi yazmaz",
         SITE in kmd and "`site/stil`" in kmd and "github.com" not in kmd and "Ornek Yazar" in kmd, kmd)
    test("site skilinin lisans puanı belirtilmemiş lisansa göre (15 değil 3)",
         any(x.startswith("lisans 3/15") for x in s8.get("degerlendirme", {}).get("ayrinti", [])), s8.get("degerlendirme"))
    gel = {"sahip": "kullanıcı", "lisans": "Kendi (özel)", "resmi_kaynak": True, "sahip_tipi": "kisi",
           "guven": {"puan": 18, "ayrinti": ["lisans 5/5", "resmî/kurum 5/5"], "derece": "D"}}
    yeni = ortak.site_gelistirici(gel, kayit())
    test("site_gelistirici kaynak kaydını değiştirmez, güveni lisans/resmî farkı kadar düşürür",
         gel["sahip"] == "kullanıcı" and gel["guven"]["puan"] == 18 and yeni["guven"]["puan"] == 8 and yeni["sahip"] == "Ornek Yazar", yeni)
    kod, cikti = yakala(kd.main)
    test("kapsam-denetimi: işlenmiş site kaynağında 0 sorun, GitHub'a sorulmadı", not kod and "sorun: 0" in cikti and not AG_CAGRILARI, cikti)
    yaz(LIB / "site" / "yeni-site-skili" / "SKILL.md", "---\nname: yeni-site-skili\ndescription: x\n---\n")
    kod, cikti = yakala(kd.main)
    test("kapsam-denetimi: site/ içinde işlenmemiş skill varsa sorun", kod == 1 and "yeni-site-skili" in cikti, cikti)
    shutil.rmtree(LIB / "site" / "yeni-site-skili")
    kod, cikti = yakala(ag.rapor)
    degisen = kod[0] if isinstance(kod, tuple) else []
    test("aylık kaynak raporu: işlenmiş site/ değişmemiş sayılır", "yerel/site" not in degisen and not AG_CAGRILARI, (kod, cikti))
    yaz(LIB / "site" / "stil" / "references" / "cam.txt", b"elle guncellendi\n")
    kod, cikti = yakala(ag.rapor)
    degisen, sorunlu = (kod[0], kod[1]) if isinstance(kod, tuple) else ([], [])
    test("aylık kaynak raporu: site/ düzenlenince yerel/site değişen kaynak, erişilemeyen değil",
         "yerel/site" in degisen and "yerel/site" not in sorunlu and "site/ düzenlenmiş" in cikti, (kod, cikti))
    yaz(LIB / "site" / "stil" / "references" / "cam.txt", UZUN)
    kod, cikti = yakala(gb.main, argv=["gelistirici-bilgisi.py"])
    g = json.loads((LIB / "gelistiriciler.json").read_text(encoding="utf-8"))["repolar"]
    test("gelistirici-bilgisi: yerel/site GitHub'a sorulmadı, kaynak düzeyinde sahip 'site (skill başına)', kendi 'kullanıcı'",
         not AG_CAGRILARI and g.get("yerel/site", {}).get("sahip") == "site (skill başına)" and g["yerel/site"]["resmi_kaynak"] is False
         and g.get("yerel/kendi", {}).get("sahip") == "kullanıcı", (cikti, g.get("yerel/site")))
    h, u = dg.kayit_semalari_denetimi(LIB)
    test("dogrula: T8 tipi şemada kabul edilir", not [x for x in h + u if "tip bilinmiyor" in x], h + u)

    test("test boyunca gerçek ağa çıkılmadı", AG_CAGRILARI == [], AG_CAGRILARI)
finally:
    urllib.request.urlopen = _urlopen
    shutil.rmtree(TMP, ignore_errors=True)

gecen = sum(1 for _, ok in SONUC if ok)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
