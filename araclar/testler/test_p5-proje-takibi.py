#!/usr/bin/env python3
"""P5 testleri: araclar/proje-kullanimi.py (proje sağlığı, kayıtsız tarama, ayar yazıcıları, çıkış kodları).
Yalnız geçici klasör ve sahte veri; gerçek ev klasörü, gerçek projeler.json, registry.json ve kütüphane git'i kullanılmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import builtins
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
from datetime import date
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p5test-")).resolve()
HOME = TMP / "home"
HOME.mkdir()
os.environ["HOME"] = str(HOME)          # Path.home() ve ortak.GLOBAL_KLASORLER geçici klasöre baksın
SONUC = []


def T(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("✅ " if kosul else "❌ ") + ad + ("" if kosul else f"  -> {str(ayrinti)[:400]}"))


def yukle(ad, dosya):
    s = importlib.util.spec_from_file_location(ad, ARACLAR / dosya)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


sys.path.insert(0, str(ARACLAR))
pk = yukle("pk_test", "proje-kullanimi.py")
import ortak  # noqa: E402

KUT = TMP / "kutuphane"
(KUT / "notlar").mkdir(parents=True)
(KUT / "registry.json").write_text(json.dumps({"skiller": []}), encoding="utf-8")


def yenile_ortam(ad="o"):
    """Her test için temiz bir 'kütüphane' + 'Documents' ve pk modül değişkenlerini oraya çevir."""
    global KUT
    kok = TMP / ad
    if kok.exists():
        shutil.rmtree(kok)
    (kok / "kut" / "notlar").mkdir(parents=True)
    (kok / "docs").mkdir()
    KUT = kok / "kut"
    (KUT / "registry.json").write_text(json.dumps({"skiller": []}), encoding="utf-8")
    pk.KOK = KUT
    pk.AYAR = KUT / "projeler.json"
    pk.RAPOR = KUT / "notlar" / "proje-kullanimi.md"
    pk.DURUM_RAPORU = KUT / "notlar" / "proje-durumu.md"
    pk.REGISTRY = KUT / "registry.json"
    pk._SE_ONBELLEK[0] = None
    return kok, kok / "docs"


def ayar_yaz(ayar):
    pk.AYAR.write_text(json.dumps(ayar, ensure_ascii=False, indent=2), encoding="utf-8")


def sk(i, commit="aaaaaaa1", h="H1", **ek):
    return {"id": i, "ad": i, "repo": "o/r", "kaynak_yol": i, "klasor_hash": h, "commit": commit, **ek}


def proje_yap(docs, ad, kilitli_skiller=(), disk=(), guncelleme="2026-11-07", kilit_ek=None, kilit_yaz=True):
    p = docs / ad
    p.mkdir(parents=True, exist_ok=True)
    for n in disk:
        d = p / ".agents" / "skills" / n
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(f"---\nname: {n}\ndescription: d\n---\n", encoding="utf-8")
    if kilit_yaz:
        m = p / ".skill-kutuphanesi"
        m.mkdir(exist_ok=True)
        k = {"surum": 3, "kutuphane": str(pk.KOK), "profil": None, "roller": [], "proje_yolu": str(p.resolve()),
             "guncelleme": guncelleme, "araclar": ["claude", "codex"], "arac_secimi": "secildi",
             "skiller": {n: {"id": n, "repo": "o/r", "kaynak_yol": n, "commit": "aaaaaaa1", "klasor_hash": "H1",
                             "roller": [], "varyantlar": []} for n in kilitli_skiller}}
        k.update(kilit_ek or {})
        (m / "kilit.json").write_text(json.dumps(k), encoding="utf-8")
    return p.resolve()


class SE:
    """skill-ekle.py yerine sahte modül: kilit okuma gerçek, kararlar tablolardan."""
    def __init__(self):
        self.elle, self.eksik, self.dogrula_satirlari, self.kilit = set(), set(), {}, None
        self.cagrilar = []

    def kilit_oku(self, proje):
        k = json.loads((Path(proje) / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))
        k.setdefault("skiller", {})
        k.setdefault("roller", [])
        k.setdefault("arac_secimi", "secildi" if "araclar" in k else "varsayilan")
        return k

    def kaynak_bul(self, skiller, k):
        return next((s for s in skiller if s["repo"] == k.get("repo") and s["kaynak_yol"] == k.get("kaynak_yol")), None)

    def elle_degismis(self, proje, ad, k):
        return (Path(proje).name, ad) in self.elle

    def kurulum_eksik(self, proje, ad, kilit):
        return (Path(proje).name, ad) in self.eksik

    def dogrula(self, proje, skiller, sessiz=False):
        return list(self.dogrula_satirlari.get(Path(proje).name, []))

    def guncelleme_suruyor(self):
        return self.kilit


def se_tak():
    se = SE()
    pk._SE_ONBELLEK[0] = se
    return se


def cik(f, *a, **kw):
    """f'i çağır; (stdout, hata) döndür. SystemExit -> kod."""
    tampon = io.StringIO()
    kod = None
    with contextlib.redirect_stdout(tampon), contextlib.redirect_stderr(tampon):
        try:
            r = f(*a, **kw)
        except SystemExit as e:
            kod = e.code if isinstance(e.code, int) else 1
            r = None
    return tampon.getvalue(), (kod if kod is not None else r)


def metinler(P):
    return [t for _, t in P["satirlar"]]


def hepsi(P, parca):
    return any(parca in t for t in metinler(P))


def agac_ozeti(*kokler):
    h = hashlib.sha256()
    for k in kokler:
        for dp, dn, fn in os.walk(k):
            dn.sort()
            for f in sorted(fn):
                p = os.path.join(dp, f)
                h.update(p.encode())
                try:
                    h.update(b"L" + os.readlink(p).encode() if os.path.islink(p) else open(p, "rb").read())
                except OSError:
                    pass
            for d in dn:
                h.update(os.path.join(dp, d).encode())
    return h.hexdigest()


GUN = date(2026, 11, 11)
SKILLER = [sk("a"), sk("b"), sk("c")]

# ------------------------------------------------------------------ 1 ayar_kontrol
kok, docs = yenile_ortam("t1")
iyi = json.loads((ARACLAR.parent / "projeler.json").read_text(encoding="utf-8"))
yol_psik = docs / "Psikolojik"
iyi_t = {"tarama_kokleri": [str(docs)], "ek_projeler": [], "kayitsiz_tarama": {"kokler": [], "derinlik": 4, "en_cok_klasor": 100},
         "yoksay": [{"yol": str(yol_psik), "altini_da": True, "neden": "karar", "tarih": "2026-11-11"}],
         "bilinen_projeler": {"X": {"yol": str(docs / "X"), "tur": "kilitli", "durum": "takipten-cikti", "eklendi": "2026-11-11"}},
         "kendi_skilleri": {"X": ["x-*"]}, "notlar": {"X": {"a": "b"}}}
yol_psik.mkdir()
proje_yap(docs, "P1", ["a"])
iyi_t["bilinen_projeler"]["P1"] = {"yol": str(docs / "P1"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"}
T("1a gerçek projeler.json şeması geçerli (yapı hatası yok)", pk._sema(iyi) == [], pk._sema(iyi))
T("1b doğru yapılmış ayar: uyarı yok", pk.ayar_kontrol(iyi_t) == [], pk.ayar_kontrol(iyi_t))
kotu = json.loads(json.dumps(iyi_t))
kotu["yoksay"][0]["tarih"] = "11.11.2026"
T("1c bozuk tarih -> uyarı", any("tarih" in u for u in pk.ayar_kontrol(kotu)))
kotu = json.loads(json.dumps(iyi_t))
kotu["yoksay"][0]["neden"] = " "
T("1d boş neden -> uyarı", any("neden boş" in u for u in pk.ayar_kontrol(kotu)))
kotu = json.loads(json.dumps(iyi_t))
kotu["notlar"]["Bilinmeyen"] = {}
T("1e bilinmeyen proje adı -> uyarı", any("bilinmeyen proje: Bilinmeyen" in u for u in pk.ayar_kontrol(kotu)))
kotu = json.loads(json.dumps(iyi_t))
kotu["bilinen_projeler"]["Y"] = {"yol": str(TMP / "baska" / "P1"), "tur": "elle", "durum": "takipte", "eklendi": "2026-11-11"}
T("1f aynı klasör adı iki yol -> AYNI AD İKİ YOL", any("AYNI AD İKİ YOL: P1" in u for u in pk.ayar_kontrol(kotu)), pk.ayar_kontrol(kotu))
kotu = json.loads(json.dumps(iyi_t))
kotu["bilinen_projeler"]["P1"]["durum"] = "belki"
T("1g bozuk durum değeri -> yapı hatası", any("durum" in u for u in pk._sema(kotu)))
kotu = json.loads(json.dumps(iyi_t))
kotu["yoksay"][0]["yol"] = str(docs / "yok-boyle-klasor")
T("1h silinmiş yoksay yolu -> BİLGİ", any(u.startswith("BİLGİ: yoksay girdisi artık yok") for u in pk.ayar_kontrol(kotu)))

# ------------------------------------------------------------------ 2 projeleri_bul
kok, docs = yenile_ortam("t2")
proje_yap(docs, "A1", ["a"])
proje_yap(docs, "B1", ["a"])
proje_yap(docs, "C-kilitsiz", [], disk=["a"], kilit_yaz=False)
ayar = {"tarama_kokleri": [str(docs)]}
T("2a projeleri_bul: kilitli 2 proje, kilitsiz sayılmaz", sorted(y.name for y in pk.projeleri_bul(ayar)) == ["A1", "B1"])
ayar["bilinen_projeler"] = {"A1": {"yol": str(docs / "A1"), "tur": "kilitli", "durum": "takipten-cikti", "eklendi": "2026-11-11"}}
T("2b takipten-cikti projeleri_bul'da yok", [y.name for y in pk.projeleri_bul(ayar)] == ["B1"])
T("2c projeleri_bul_ham hâlâ ikisini verir", sorted(y.name for y in pk.projeleri_bul_ham(ayar)) == ["A1", "B1"])
T("2d kullanan_projeler/oku de takipten çıkanı görmez", [p["ad"] for p in pk.oku(ayar)] == ["B1"])

# ------------------------------------------------------------------ 3 rapor biçimi değişmedi
kok, docs = yenile_ortam("t3")
proje_yap(docs, "A1", ["a", "b"])
eski_ayar = {"tarama_kokleri": [str(docs)], "ek_projeler": [], "notlar": {"A1": {"a": "not"}}}
yeni_ayar = {**eski_ayar, "kayitsiz_tarama": {}, "yoksay": [], "bilinen_projeler": {}, "kendi_skilleri": {}}
reg = {("o/r", "a"): "a", ("o/r", "b"): "b"}
m1, _ = pk.rapor_metni(pk.oku(eski_ayar), eski_ayar, reg)
m2, _ = pk.rapor_metni(pk.oku(yeni_ayar), yeni_ayar, reg)
T("3 rapor_metni: yeni alanlar rapor metnini değiştirmez", m1 == m2 and "| A1 |" in m1.replace("[A1](#a1)", "A1"))

# ------------------------------------------------------------------ 4 kilit_guvenli_oku
kok, docs = yenile_ortam("t4")
p = proje_yap(docs, "K", ["a"])
T("4a sağlam kilit okunur (se yok -> ham)", pk.kilit_guvenli_oku(p)[1] is None and "a" in pk.kilit_guvenli_oku(p)[0]["skiller"])
(p / ".skill-kutuphanesi" / "kilit.json").write_text("{bozuk", encoding="utf-8")
k, h = pk.kilit_guvenli_oku(p)
T("4b bozuk JSON -> (None, 'kilit.json okunamıyor')", k is None and h.startswith("kilit.json okunamıyor"), h)
(p / ".skill-kutuphanesi" / "kilit.json").write_text("[1]", encoding="utf-8")
T("4c liste -> (None, hata)", pk.kilit_guvenli_oku(p)[0] is None)
k, h = pk.kilit_guvenli_oku(docs / "yok")
T("4d kilit yok -> (None, hata), istisna yok", k is None and h is not None)

# ------------------------------------------------------------------ 5 skill_durumu
kok, docs = yenile_ortam("t5")
se = se_tak()
p = proje_yap(docs, "S", ["a"])
kil = pk.kilit_guvenli_oku(p)[0]
k0 = kil["skiller"]["a"]
reg0 = [sk("a")]


def dur(skiller, elle=False, eksik=False):
    se.elle = {("S", "a")} if elle else set()
    se.eksik = {("S", "a")} if eksik else set()
    return pk.skill_durumu(p, "a", k0, kil, skiller, se)


T("5a güncel", dur(reg0) == "guncel")
T("5b kaynak yok", dur([]) == "kaynak-yok")
T("5c emekli (kaynakta kaldırıldı)", dur([sk("a", kaynak_durumu="kaynakta-kaldirildi")]) == "emekli-kaynakta-kaldirildi")
T("5d emekli (kayıp)", dur([sk("a", kaynak_durumu="kayip")]) == "emekli-kayip")
T("5e elle değişmiş", dur(reg0, elle=True) == "elle-degismis")
T("5f güncelleme var", dur([sk("a", h="H2")]) == "guncelleme-var")
T("5g kurulum eksik", dur(reg0, eksik=True) == "kurulum-eksik")
T("5h öncelik: kaynak yok > elle; emekli > elle; elle > güncelleme > eksik",
  dur([], elle=True) == "kaynak-yok" and dur([sk("a", kaynak_durumu="kayip")], elle=True) == "emekli-kayip"
  and dur([sk("a", h="H2")], elle=True, eksik=True) == "elle-degismis" and dur([sk("a", h="H2")], eksik=True) == "guncelleme-var")

# ------------------------------------------------------------------ 6 sağlık: temel durumlar
kok, docs = yenile_ortam("t6")
se = se_tak()
ayar = {"tarama_kokleri": [str(docs)]}
proje_yap(docs, "Temiz", ["a"], disk=["a"])
s = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)
P = s["projeler"][0]
T("6a temiz proje -> temiz", P["durum"] == "temiz" and s["durum"] in ("temiz", "dikkat"), (P["durum"], P["satirlar"]))
S2 = [sk("a", h="H2", commit="bbbbbbb2"), sk("b"), sk("c")]
P = pk.saglik_hesapla(ayar, S2, bugun=GUN)["projeler"][0]
T("6b güncelleme var -> dikkat + sayaç + kısa commit", P["durum"] == "dikkat" and P["sayac"]["guncelleme_var"] == 1
  and hepsi(P, "GÜNCELLEME VAR: a (aaaaaaa -> bbbbbbb)"), P["satirlar"])
se.dogrula_satirlari["Temiz"] = ["a: .agents/skills kopyası yok"]
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("6c yapı sorunu (dogrula) -> sorun", P["durum"] == "sorun" and hepsi(P, "kopyası yok"))
se.dogrula_satirlari["Temiz"] = ["a: kurulumdan sonra elle değiştirilmiş", "a: kaynağı kütüphanede artık yok (o/r:a)", "proje taşınmış (x -> y); --yenile çalıştır"]
se.elle = {("Temiz", "a")}
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("6d elle değişmiş bir kez listelenir (dogrula tekrarı süzülür), dikkat", P["durum"] == "dikkat" and sum("ELLE DEĞİŞTİRİLMİŞ" in t or "elle değiştirilmiş" in t for t in metinler(P)) == 1, P["satirlar"])
se.elle = set()
se.dogrula_satirlari["Temiz"] = [f"/x/.claude/settings.json: hesap skill'i `a` için skillOverrides güncel değil; (--guncelle)"]
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("6e skillOverrides satırı dikkat ve yol/değer içermez", P["durum"] == "dikkat" and hepsi(P, "a: skillOverrides güncel değil") and not hepsi(P, "/x/"), P["satirlar"])
se.dogrula_satirlari.clear()
se.eksik = {("Temiz", "a")}
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("6f kurulum eksik -> sorun", P["durum"] == "sorun" and P["sayac"]["kurulum_eksik"] == 1)
se.eksik = set()
(docs / "Temiz" / ".skill-kutuphanesi" / "kilit.json").write_text("{bozuk", encoding="utf-8")
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("6g bozuk kilit -> KİLİT OKUNAMIYOR (sorun), çökmez", P["durum"] == "sorun" and hepsi(P, "KİLİT OKUNAMIYOR"))

# ------------------------------------------------------------------ 7 taşınmış / başka yerden
kok, docs = yenile_ortam("t7")
se = se_tak()
ayar = {"tarama_kokleri": [str(docs)]}
(docs / "Eski").mkdir()
proje_yap(docs, "M", ["a"], disk=["a"], kilit_ek={"proje_yolu": str(docs.resolve() / "Eski" / "M")})
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("7a kilit yolunun üstü bu bilgisayarda var -> TAŞINMIŞ", hepsi(P, "TAŞINMIŞ (kilit yolu:") and not hepsi(P, "BAŞKA YERDEN"), P["satirlar"])
for yabanci in ("/Users/baska/Documents/M", "C:\\Users\\x\\M"):
    k = json.loads((docs / "M" / ".skill-kutuphanesi" / "kilit.json").read_text())
    k["proje_yolu"] = yabanci
    (docs / "M" / ".skill-kutuphanesi" / "kilit.json").write_text(json.dumps(k))
    P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
    T(f"7b {yabanci[:12]}... -> BAŞKA YERDEN KOPYALANMIŞ", hepsi(P, "BAŞKA YERDEN KOPYALANMIŞ") and P["durum"] == "dikkat", P["satirlar"])

# ------------------------------------------------------------------ 8 kütüphane yolu, 9 kaynak yok, 17 araç alanı
kok, docs = yenile_ortam("t8")
se = se_tak()
ayar = {"tarama_kokleri": [str(docs)]}
proje_yap(docs, "L", ["a"], disk=["a"], kilit_ek={"kutuphane": "/baska/kutuphane"})
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("8 kutuphane yolu farklı -> dikkat satırı", hepsi(P, "başka bir kütüphane yoluna ait") and P["durum"] == "dikkat")
P = pk.saglik_hesapla(ayar, [], bugun=GUN)["projeler"][0]
T("9 kaynak kütüphanede yok -> KAYNAK KÜTÜPHANEDE YOK, sayaç", hepsi(P, "KAYNAK KÜTÜPHANEDE YOK: a") and P["sayac"]["kaynak_yok"] == 1)
kok, docs = yenile_ortam("t17")
se = se_tak()
ayar = {"tarama_kokleri": [str(docs)]}
proje_yap(docs, "Eski", ["a"], disk=["a"])
k = json.loads((docs / "Eski" / ".skill-kutuphanesi" / "kilit.json").read_text())
del k["araclar"], k["arac_secimi"]
k["bilinmeyen_yeni_alan"] = {"x": 1}
(docs / "Eski" / ".skill-kutuphanesi" / "kilit.json").write_text(json.dumps(k))
P = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"][0]
T("17a araclar'sız kilit + bilinmeyen alan: hata yok, 'bilgi' satırı, düzey yükselmez",
  P["durum"] == "temiz" and ("bilgi", "araç seçimi kilitte yok (varsayılan: claude, codex)") in P["satirlar"]
  and "varsayılan" in P["araclar"], P["satirlar"])
proje_yap(docs, "Yeni2", ["a"], disk=["a"], kilit_ek={"araclar": ["claude", "antigravity"]})
P = [x for x in pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"] if x["ad"] == "Yeni2"][0]
T("17b bilinmeyen araç adı olduğu gibi yazılır, hata yok", P["araclar"] == "claude, antigravity" and P["durum"] == "temiz")
proje_yap(docs, "Kirli", ["a"], disk=["a"], guncelleme="2026-01-01")
P = [x for x in pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)["projeler"] if x["ad"] == "Kirli"][0]
T("9b 60 günden eski son işlem -> yalnız bilgi", any(d == "bilgi" and "60 günden eski" in t for d, t in P["satirlar"]) and P["durum"] == "temiz")

# ------------------------------------------------------------------ 10 disk sınıflaması
kok, docs = yenile_ortam("t10")
se = se_tak()
ayar = {"tarama_kokleri": [str(docs)], "kendi_skilleri": {"Pr": ["kendi-*"]}}
p = proje_yap(docs, "Pr", ["a"], disk=["a", "elle1", "kendi-x", "kopya", "tuhaf"])
(p / ".skill-kutuphanesi" / "elle-kurulan.json").write_text(json.dumps({"skiller": {"elle1": {"repo": "o/r"}, "hayalet": {}}}))
# kopya: içeriği kütüphane karmasıyla aynı olan klasör
kopya_h = ortak.klasor_hash(p / ".agents" / "skills" / "kopya")
sk_kopya = sk("kutup-kopya", h=kopya_h)
P = pk.saglik_hesapla(ayar, SKILLER + [sk_kopya], bugun=GUN)["projeler"][0]
T("10a elle-kurulan.json'daki skill: sessiz, sayılır", P["sayac"]["kendi_elle"] == 2 and not hepsi(P, "elle1"))
T("10b kendi_skilleri deseni: sessiz", not hepsi(P, "kendi-x"))
T("10c kütüphane karmasıyla aynı -> KİLİTSİZ KÜTÜPHANE KOPYASI", hepsi(P, "KİLİTSİZ KÜTÜPHANE KOPYASI: kopya (kütüphanedeki kutup-kopya"), P["satirlar"])
T("10d diğeri -> KAYITSIZ SKILL", hepsi(P, "KAYITSIZ SKILL: tuhaf") and P["sayac"]["kayitsiz"] == 2)
T("10e elle-kurulan.json'da olup klasörü yok -> ters satır", hepsi(P, "elle-kurulan.json'da olup klasörü yok: hayalet"))
# symlink + gerçek klasör tek sayılır
(p / ".claude" / "skills").mkdir(parents=True)
os.symlink("../../.agents/skills/a", p / ".claude" / "skills" / "a")
T("10f .claude symlink + .agents gerçek klasör: bir skill", sorted(pk.disk_skilleri(p)["a"]) == [".agents/skills/a", ".claude/skills/a"])
T("10g disk_skilleri 5 farklı ad sayar", len(pk.disk_skilleri(p)) == 5, pk.disk_skilleri(p))

# ------------------------------------------------------------------ 11 kaybolanlar
kok, docs = yenile_ortam("t11")
se = se_tak()
proje_yap(docs, "Var", ["a"], disk=["a"])
proje_yap(docs, "Bilinmiyor", ["a"], disk=["a"])
(docs / "KilitsizDuruyor").mkdir()
bp = {"Var": {"yol": str(docs / "Var"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
      "KilitsizDuruyor": {"yol": str(docs / "KilitsizDuruyor"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
      "Silinmis": {"yol": str(docs / "Silinmis"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
      "Tasinan": {"yol": str(docs / "eskiyer" / "Tasinan"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
      "Cikmis": {"yol": str(docs / "CikmisYok"), "tur": "kilitli", "durum": "takipten-cikti", "eklendi": "2026-11-11",
                 "cikis_tarihi": "2026-11-11", "cikis_nedeni": "silindi"}}
proje_yap(docs, "Tasinan", ["a"], disk=["a"])
ayar = {"tarama_kokleri": [str(docs)], "bilinen_projeler": bp, "ek_projeler": [str(docs / "ekyok")]}
s = pk.saglik_hesapla(ayar, SKILLER, bugun=GUN)
kb = " | ".join(t for _, t in s["kaybolanlar"])
T("11a klasör duruyor kilit yok -> KİLİT YOK", "KİLİT YOK: KilitsizDuruyor" in kb)
T("11b silinmiş -> KAYIP", "KAYIP: Silinmis" in kb)
T("11c aynı ad başka yolda -> TAŞINMIŞ görünüyor", "TAŞINMIŞ görünüyor: Tasinan" in kb)
T("11d izlenen ama hafızada olmayan -> KAYITLI DEĞİL", "KAYITLI DEĞİL: Bilinmiyor" in kb)
T("11e takipten-cikti + klasör yok -> KAYIP yok, takipte_olmayan'da", "Cikmis" not in kb and any("Cikmis: takipten çıktı 2026-11-11" in t for t in s["takipte_olmayan"]))
T("11f ek_projeler'de olmayan yol -> uyarı", "ek_projeler yolu yok" in kb)
T("11g kayıp varsa genel durum sorun", s["durum"] == "sorun")

# ------------------------------------------------------------------ 12-16 tarama
def ag(*parcalar):
    return Path(*parcalar)


def skilli(d, ad="s"):
    (d / ".claude" / "skills" / ad).mkdir(parents=True, exist_ok=True)
    (d / ".claude" / "skills" / ad / "SKILL.md").write_text("---\nname: s\n---\n", encoding="utf-8")


kok, docs = yenile_ortam("t12")
skilli(docs / "a")
(docs / "b").mkdir()
(docs / "b" / "AGENTS.md").write_text("x", encoding="utf-8")
(docs / "c" / "d" / "e" / "f").mkdir(parents=True)
(docs / "c" / "d" / "e" / "f" / ".agents" / "skills" / "s").mkdir(parents=True)
(docs / "c" / "d" / "e" / "f" / ".agents" / "skills" / "s" / "SKILL.md").write_text("x", encoding="utf-8")
reg_p = proje_yap(docs, "kayitli", ["a"])
skilli(docs / "node_modules" / "x")
skilli(docs / ".gizli")
ayar = {"tarama_kokleri": [str(docs)], "kayitsiz_tarama": {"derinlik": 4}}
t = pk.tara_kayitsiz(ayar, [reg_p])
yollar = [x["yol"].split("/docs/")[-1] for x in t["adaylar"]]
T("12a skilli klasör bulunur, derin (4) olan da", "a" in yollar and "c/d/e/f" in yollar, yollar)
T("12b yalnız talimat dosyalı sayılır ama aday değil", t["talimat_sayisi"] == 1 and "b" not in yollar)
T("12c kayıtlı proje, node_modules ve nokta klasör aday değil", not any(y.startswith(("kayitli", "node_modules", ".gizli")) for y in yollar))
t3 = pk.tara_kayitsiz({**ayar, "kayitsiz_tarama": {"derinlik": 3}}, [reg_p])
T("12d derinlik 3'te derin klasör görünmez", [x["yol"].split("/docs/")[-1] for x in t3["adaylar"]] == ["a"])
T("12e araç etiketi", [x for x in t["adaylar"] if x["yol"].endswith("/a")][0]["araclar"] == ["claude"])

kok, docs = yenile_ortam("t13")
gercek = docs / "gercek"
skilli(gercek)
os.symlink(gercek, docs / "baglanti")
(docs / "x").mkdir()
os.symlink(docs / "x", docs / "x" / "dongu")
ayar = {"tarama_kokleri": [str(docs)]}
t0 = time.time()
t = pk.tara_kayitsiz(ayar, [])
T("13a bağlantılı klasör aday olmaz, sayılır; döngü takılmaz", [x["yol"].split("/docs/")[-1] for x in t["adaylar"]] == ["gercek"]
  and t["atlanan_baglanti"] >= 2 and time.time() - t0 < 5)
p2 = docs / "bagliskill"
(p2 / ".claude").mkdir(parents=True)
genel_dizin = HOME / ".claude" / "skills"
genel_dizin.mkdir(parents=True)
os.symlink(genel_dizin, p2 / ".claude" / "skills")
q = docs / "baska"
(q / ".claude").mkdir(parents=True)
(docs / "baskaHedef").mkdir()
os.symlink(docs / "baskaHedef", q / ".claude" / "skills")
t = pk.tara_kayitsiz(ayar, [])
byl = {x["yol"].split("/docs/")[-1]: x for x in t["adaylar"]}
T("13b skills klasörü bağlantıysa 'baglanti'; genel klasöre gidiyorsa genel=True, değilse False",
  byl["bagliskill"]["baglanti"][0]["genel"] is True and byl["baska"]["baglanti"][0]["genel"] is False, byl)

kok, docs = yenile_ortam("t14")
for i in range(40):
    (docs / f"k{i}" / "alt").mkdir(parents=True)
t0 = time.time()
t = pk.tara_kayitsiz({"tarama_kokleri": [str(docs)], "kayitsiz_tarama": {"en_cok_klasor": 5}}, [])
T("14 klasör sınırı: sinira_ulasildi, kısmi sonuç, hızlı", t["sinira_ulasildi"] and t["klasor_sayisi"] == 5 and time.time() - t0 < 5, t["klasor_sayisi"])
bos_kok = TMP / "olmayan-kok"
t = pk.tara_kayitsiz({"tarama_kokleri": [str(bos_kok)]}, [])
T("14b olmayan kök: bilgi satırı, sorun değil", t["bilgi"] and not t["sorun"])

# 15 yoksay + açılmama kanıtı
kok, docs = yenile_ortam("t15")
x = docs / "Psikolojik Danışman Sosyal Medya"
skilli(x)
skilli(x / "alt")
skilli(docs / "tam")
skilli(docs / "KIT" / "derin")
(docs / "tam" / "ic").mkdir()
yoksay = [{"yol": str(docs / "Psikolojik Danışman Sosyal Medya"), "altini_da": True, "neden": "karar A", "tarih": "2026-11-11"},
          {"yol": str(docs / "tam"), "altini_da": False, "neden": "karar B", "tarih": "2026-11-11"}]
ayar = {"tarama_kokleri": [str(docs)], "yoksay": yoksay}
kayit = []
_o_scandir, _o_lstat, _o_stat = os.scandir, os.lstat, os.stat


def _kaydet(f):
    def sar(p, *a, **k):
        if isinstance(p, (str, bytes, os.PathLike)):
            kayit.append(os.fsdecode(p))
        return f(p, *a, **k)
    return sar


os.scandir, os.lstat, os.stat = _kaydet(_o_scandir), _kaydet(_o_lstat), _kaydet(_o_stat)
try:
    t = pk.tara_kayitsiz(ayar, [])
finally:
    os.scandir, os.lstat, os.stat = _o_scandir, _o_lstat, _o_stat
adlar = {y["yol"].split("/docs/")[-1]: y for y in t["yoksayilan"]}
T("15a yoksayılanlar neden/tarihle listelenir, aday olmaz",
  set(adlar) == {"Psikolojik Danışman Sosyal Medya", "tam"} and adlar["tam"]["neden"] == "karar B"
  and not any("Psikolojik" in a["yol"] or a["yol"].endswith("/tam") for a in t["adaylar"]), (adlar, t["adaylar"]))
yasak = [os.path.join(os.path.realpath(docs), "Psikolojik Danışman Sosyal Medya"), os.path.join(os.path.realpath(docs), "tam")]
kayit_nfc = [unicodedata.normalize("NFC", k) for k in kayit]
ihlal = [k for k in kayit_nfc if any(k == y or k.startswith(y + os.sep) for y in yasak)]
T("15b açılmama kanıtı: yoksayılan klasöre scandir/lstat/stat HİÇ yapılmadı", not ihlal and len(kayit) > 3, ihlal[:3])
ayar_nfd = {"tarama_kokleri": [str(docs)], "yoksay": [{**yoksay[0], "yol": unicodedata.normalize("NFD", yoksay[0]["yol"])}]}
t = pk.tara_kayitsiz(ayar_nfd, [])
T("15d NFD yazılmış yol NFC klasörle eşleşir", len(t["yoksayilan"]) == 1 and not any("Psikolojik" in a["yol"] for a in t["adaylar"]), t["yoksayilan"])
T("15e KIT klasörü yoksay listesinde değilse aday (sınama)", any("KIT" in a["yol"] for a in t["adaylar"]))

# 16 .env hiç açılmaz, değer hiçbir çıktıda yok
kok, docs = yenile_ortam("t16")
se = se_tak()
pr = proje_yap(docs, "Gizli", ["a"], disk=["a"])
(pr / ".env").write_text("TOKEN=GIZLI-DEGER-123\n", encoding="utf-8")
(pr / ".env.local").write_text("GIZLI-DEGER-123", encoding="utf-8")
(docs / "Aday").mkdir()
(docs / "Aday" / ".env").write_text("GIZLI-DEGER-123", encoding="utf-8")
skilli(docs / "Aday")
ayar_yaz({"tarama_kokleri": [str(docs)]})
acilan = []
_o_open, _o_io = builtins.open, io.open


def _acilis(f):
    def sar(p, *a, **k):
        if isinstance(p, (str, bytes, os.PathLike)):
            acilan.append(os.fsdecode(p))
        return f(p, *a, **k)
    return sar


builtins.open, io.open = _acilis(_o_open), _acilis(_o_io)
try:
    c1, _ = cik(pk.main, ["--saglik"])
    c2, _ = cik(pk.main, ["--tara-kayitsiz"])
    c3, _ = cik(pk.main, ["--saglik", "--ozet-json", "--yaz"])
finally:
    builtins.open, io.open = _o_open, _o_io
rapor = pk.DURUM_RAPORU.read_text(encoding="utf-8")
T("16 .env açılmaz ve değeri hiçbir çıktıda/raporda yok", "GIZLI-DEGER-123" not in c1 + c2 + c3 + rapor
  and not any(Path(a).name.startswith(".env") for a in acilan), [a for a in acilan if ".env" in a])

# ------------------------------------------------------------------ 18 yazıcılar
kok, docs = yenile_ortam("t18")
se = se_tak()
home_docs = HOME / "Documents"
home_docs.mkdir()
pa = proje_yap(docs, "Pa", ["a"], disk=["a"])
(docs / "Pa" / "CLAUDE.md").write_text("x")
ayar0 = {"tarama_kokleri": [str(docs)], "ek_projeler": [], "notlar": {"Pa": {"a": "n"}}, "kendi_skilleri": {"Pa": ["z-*"]}}
ayar_yaz(ayar0)
once_p = agac_ozeti(docs)
once_kut = agac_ozeti(KUT)
c, kod = cik(pk.main, ["--cikar", "Pa", "--neden", "silindi"])
T("18a dry run: PLAN yazılır, hiçbir dosya değişmez", "PLAN (hiçbir şey yazılmadı" in c and agac_ozeti(KUT) == once_kut and kod == 0, c)
c, kod = cik(pk.main, ["--cikar", "Pa"])
T("18b --cikar --neden'siz exit 2", kod == 2 and "--neden zorunlu" in c)
c, kod = cik(pk.main, ["--cikar", "Pa", "--neden", "kapandı", "--evet"])
a1 = json.loads(pk.AYAR.read_text(encoding="utf-8"))
T("18c --cikar --evet: izlenen ama hafızada olmayan proje için kayıt oluşur", a1["bilinen_projeler"]["Pa"]["durum"] == "takipten-cikti"
  and a1["bilinen_projeler"]["Pa"]["cikis_nedeni"] == "kapandı" and "projeler.json güncellendi" in c, c)
T("18d takipten çıkan projeleri_bul'da yok; proje klasörü bayt bayt aynı", pk.projeleri_bul(a1) == [] and agac_ozeti(docs) == once_p)
c, kod = cik(pk.main, ["--cikar", "Yoktur", "--neden", "x"])
T("18e bilinmeyen ad -> HATA, exit 2", kod == 2 and "izlenen projelerde yok" in c)
# ekle: kilitli, kapsam dışı
dis = TMP / "t18" / "baska-yer"
dis.mkdir()
pd = proje_yap(dis, "Dis", ["a"], disk=["a"])
ayar_yaz({"tarama_kokleri": [str(docs)], "ek_projeler": []})
c, kod = cik(pk.main, ["--ekle", str(pd), "--evet"])
a2 = json.loads(pk.AYAR.read_text(encoding="utf-8"))
T("18f --ekle kilitli kapsam dışı: bilinen_projeler(kilitli) + ek_projeler", a2["bilinen_projeler"]["Dis"]["tur"] == "kilitli"
  and a2["ek_projeler"] == [str(pd)] and [y.name for y in pk.projeleri_bul(a2)] == ["Pa", "Dis"], (a2, c))
elle = docs / "ElleKurulu"
(elle / ".agents" / "skills" / "q").mkdir(parents=True)
(elle / ".agents" / "skills" / "q" / "SKILL.md").write_text("x")
c, kod = cik(pk.main, ["--ekle", str(elle)])
T("18g --ekle kilitsiz: --neden zorunlu", kod == 2 and "--neden zorunlu" in c)
c, kod = cik(pk.main, ["--ekle", str(elle), "--neden", "elle kurulu", "--evet"])
a3 = json.loads(pk.AYAR.read_text(encoding="utf-8"))
T("18h --ekle kilitsiz -> tur elle + neden; ek_projeler'e yazılmaz", a3["bilinen_projeler"]["ElleKurulu"]["tur"] == "elle"
  and a3["bilinen_projeler"]["ElleKurulu"]["neden"] == "elle kurulu" and str(elle) not in a3["ek_projeler"], a3)
for kotu_yol in (str(KUT), str(HOME), str(ortak.GLOBAL_KLASORLER["claude"])):
    ortak.GLOBAL_KLASORLER["claude"].mkdir(parents=True, exist_ok=True)
    c, kod = cik(pk.main, ["--ekle", kotu_yol])
    T(f"18i --ekle reddeder: {Path(kotu_yol).name}", kod == 2 and "proje olamaz" in c, c)
c, kod = cik(pk.main, ["--ekle", str(docs / "yok-boyle")])
T("18j --ekle klasör değilse HATA", kod == 2 and "bir klasör değil" in c)
(KUT / "arsiv").mkdir(exist_ok=True)
ayar_yaz({"tarama_kokleri": [str(docs)], "ek_projeler": []})
for kotu_yol in (str(KUT / "arsiv"), str(docs)):
    c, kod = cik(pk.main, ["--ekle", kotu_yol, "--neden", "x", "--evet"])
    T(f"18k --ekle reddeder (kütüphane altı / tarama kökü): {Path(kotu_yol).name}", kod == 2 and "proje olamaz" in c
      and "bilinen_projeler" not in json.loads(pk.AYAR.read_text(encoding="utf-8")), c)
c, kod = cik(pk.main, ["--saglik", "--ekle", str(elle), "--neden", "x", "--evet"])
T("18l okuma kipi + yazıcı bayrağı birlikte -> 2, hiçbir şey yazılmaz",
  kod == 2 and "bilinen_projeler" not in json.loads(pk.AYAR.read_text(encoding="utf-8")), c)
# tasindi
yeni_ad = docs / "PaYeni"
shutil.copytree(docs / "Pa", yeni_ad, symlinks=True)
ayar_yaz({"tarama_kokleri": [str(docs)], "ek_projeler": [str(docs / "Pa")], "notlar": {"Pa": {"a": "n"}}, "kendi_skilleri": {"Pa": ["z-*"]},
          "bilinen_projeler": {"Pa": {"yol": str(docs / "Pa"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"}}})
c, kod = cik(pk.main, ["--tasindi", "Pa", str(yeni_ad), "--evet"])
a4 = json.loads(pk.AYAR.read_text(encoding="utf-8"))
T("18k --tasindi: ad değişince üç sözlükte anahtar yeniden adlanır, yol ve onceki_yollar, ek_projeler",
  "PaYeni" in a4["bilinen_projeler"] and "Pa" not in a4["bilinen_projeler"] and "PaYeni" in a4["notlar"] and "PaYeni" in a4["kendi_skilleri"]
  and a4["bilinen_projeler"]["PaYeni"]["onceki_yollar"] == [str(docs / "Pa")] and a4["ek_projeler"] == [str(yeni_ad)]
  and "skill-ekle.py" in c and "--yenile --kuru" in c, (a4, c))
c, kod = cik(pk.main, ["--tasindi", "PaYeni", str(docs / "yokki")])
T("18l --tasindi yeni yol yoksa HATA", kod == 2 and "bir klasör değil" in c)
(docs / "kilitsizyer").mkdir()
c, kod = cik(pk.main, ["--tasindi", "PaYeni", str(docs / "kilitsizyer")])
T("18m --tasindi kilitli projeyi kilitsiz yere reddeder", kod == 2 and "kilit.json yok" in c)
# yoksay
c, kod = cik(pk.main, ["--yoksay", str(docs / "Z"), "--evet"])
T("18n --yoksay --neden'siz reddedilir", kod == 2)
c, kod = cik(pk.main, ["--yoksay", str(docs / "Z"), "--neden", "önemsiz", "--altini-da", "--evet"])
a5 = json.loads(pk.AYAR.read_text(encoding="utf-8"))
T("18o --yoksay yazar: altini_da, neden, bugün", a5["yoksay"][-1]["altini_da"] is True and a5["yoksay"][-1]["neden"] == "önemsiz"
  and a5["yoksay"][-1]["tarih"] == date.today().isoformat())
c, kod = cik(pk.main, ["--yoksay", str(docs / "Z"), "--neden", "tekrar"])
T("18p aynı yolu ikinci kez yoksay reddedilir", kod == 2 and "zaten" in c)
c, kod = cik(pk.main, ["--cikar", "x", "--yoksay", "y", "--neden", "n"])
T("18q iki yazıcı bayrağı birlikte exit 2", kod == 2)
c, kod = cik(pk.main, ["--evet"])
T("18r tek başına --evet yok sayılır", "yok sayıldı" in c or "bir şey yapmaz" in c)
se.kilit = {"pid": 1}
once_kut = agac_ozeti(KUT)
c, kod = cik(pk.main, ["--cikar", "PaYeni", "--neden", "n", "--evet"])
T("18s kütüphane güncellenirken yazıcı reddedilir (BEKLE), dosya değişmez", kod == 2 and "BEKLE" in c and agac_ozeti(KUT) == once_kut)
se.kilit = None
once_proje = agac_ozeti(docs, dis)
cik(pk.main, ["--yoksay", str(docs / "Q"), "--neden", "n", "--evet"])
T("18t yazıcılar projeleri hiç değiştirmez", agac_ozeti(docs, dis) == once_proje)
T("18u yazıcı sonrası yalnız projeler.json değişti (rapor dosyaları yazılmadı)", sorted(x.name for x in (KUT / "notlar").iterdir()) == [], sorted(x.name for x in (KUT / "notlar").iterdir()))

# ------------------------------------------------------------------ 19 --ozet-json
kok, docs = yenile_ortam("t19")
se = se_tak()
proje_yap(docs, "J", ["a"], disk=["a", "yabanci"])
skilli(docs / "Aday")
ayar_yaz({"tarama_kokleri": [str(docs)], "bilinen_projeler": {}})
c, kod = cik(pk.main, ["--saglik", "--ozet-json"])
try:
    o = json.loads(c)
    tamam = (set(o) == {"arac", "durum", "satirlar", "karar_bekleyen"} and o["arac"] == "proje-kullanimi" and o["durum"] in ("temiz", "dikkat", "sorun")
             and isinstance(o["satirlar"], list) and len(o["satirlar"]) <= 15 and all(len(x) <= 160 for x in o["satirlar"] + o["karar_bekleyen"])
             and len(o["karar_bekleyen"]) <= 12 and c.count("\n") == 1)
except Exception as e:  # noqa: BLE001
    tamam, o = False, str(e)
T("19a --ozet-json: stdout yalnız tek JSON nesnesi, alanlar ve sınırlar", tamam and kod == 0, c[:300])
T("19b --ozet-json dosya yazmaz (--yaz yok)", not pk.DURUM_RAPORU.exists())
cik(pk.main, ["--saglik", "--ozet-json", "--yaz"])
T("19c --yaz ile rapor yazılır", pk.DURUM_RAPORU.exists())

# ------------------------------------------------------------------ 21 belirlilik, 22 başka bilgisayar
kok, docs = yenile_ortam("t21")
se = se_tak()
proje_yap(docs, "D", ["a"], disk=["a", "yabanci"])
ayar_yaz({"tarama_kokleri": [str(docs)], "bilinen_projeler": {}})
cik(pk.main, ["--saglik"])
r1 = pk.DURUM_RAPORU.read_text(encoding="utf-8")
m1 = pk.DURUM_RAPORU.stat().st_mtime_ns
time.sleep(0.02)
cik(pk.main, ["--saglik"])
T("21a iki çalıştırma aynı baytlar, ikincisi dosyayı yeniden yazmaz", pk.DURUM_RAPORU.read_text(encoding="utf-8") == r1 and pk.DURUM_RAPORU.stat().st_mtime_ns == m1)
kalan = re.sub(r"\| \d{4}-\d{2}-\d{2} \|", "|", r1)
T("21b tarih/saat yalnız 'Son işlem' sütununda (rapor başka tarih içermez)", not re.search(r"\d{4}-\d{2}-\d{2}", kalan) and "## Kayıtsız proje klasörleri" in r1
  and "## Karar bekleyenler" in r1 and "## Ayar uyarıları" in r1, kalan[:300])
kok, docs = yenile_ortam("t22")
bp5 = {f"P{i}": {"yol": str(docs / f"P{i}"), "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"} for i in range(5)}
ayar_yaz({"tarama_kokleri": [str(docs)], "bilinen_projeler": bp5})
c1, k1 = cik(pk.main, ["--saglik"])
c2, k2 = cik(pk.main, ["--saglik", "--ozet-json"])
T("22a bu bilgisayarda proje yok: rapor oluşmaz, ileti, ozet 'temiz', çıkış 0", not pk.DURUM_RAPORU.exists() and "Hiç proje bulunamadı" in c1
  and json.loads(c2)["durum"] == "temiz" and k1 == 0 and k2 == 0)
T("22b hizli_kontrol: proje yoksa sessiz []", pk.hizli_kontrol(json.loads(pk.AYAR.read_text())) == [] and pk._SE_ONBELLEK[0] is None)
proje_yap(docs, "P0", ["a"])
t0 = time.time()
hz = pk.hizli_kontrol(json.loads(pk.AYAR.read_text()))
T("22c hizli_kontrol: kayıp projeler KAYIP uyarısı, hızlı, skill-ekle yüklemez", sum("KAYIP:" in u for u in hz) == 4 and time.time() - t0 < 0.2
  and all(u.startswith("proje takibi:") for u in hz) and pk._SE_ONBELLEK[0] is None, hz)
T("22d hizli_kontrol: ayar yok -> []", pk.hizli_kontrol({}) == [])

# ------------------------------------------------------------------ 23 gerçek skill-ekle.durum() ile çapraz denetim
se_gercek = yukle("skillekle_test", "skill-ekle.py")
se_gercek.hesap_gizleme_eksik = lambda proje, kilit: []
kok, docs = yenile_ortam("t23")
pk._SE_ONBELLEK[0] = se_gercek


def gercek_proje(ad="G"):
    p = docs / ad
    (p / ".agents" / "skills" / "x").mkdir(parents=True)
    (p / ".agents" / "skills" / "x" / "SKILL.md").write_text("---\nname: x\ndescription: d\n---\ngövde\n", encoding="utf-8")
    (p / ".claude" / "skills").mkdir(parents=True)
    os.symlink("../../.agents/skills/x", p / ".claude" / "skills" / "x")
    H = ortak.klasor_hash(p / ".agents" / "skills" / "x")
    blok = f"{se_gercek.BLOK_BAS}\nx\n{se_gercek.BLOK_SON}\n"
    (p / "CLAUDE.md").write_text(blok, encoding="utf-8")
    (p / "AGENTS.md").write_text(blok, encoding="utf-8")
    m = p / ".skill-kutuphanesi"
    m.mkdir()
    kilit = {"surum": 3, "kutuphane": str(pk.KOK), "profil": None, "roller": [], "proje_yolu": str(p.resolve()), "guncelleme": "2026-11-07",
             "araclar": ["claude", "codex"], "arac_secimi": "secildi",
             "skiller": {"x": {"id": "x", "repo": "o/r", "kaynak_yol": "x", "commit": "c0ffee1", "klasor_hash": H, "varyantlar": [],
                               "roller": [], "kurulu_hash": {"codex": H, "claude": "symlink"}}}}
    (m / "kilit.json").write_text(json.dumps(kilit), encoding="utf-8")
    return p.resolve(), H


def gercek_durum(p, skiller):
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        se_gercek.durum(p, skiller)
    return tampon.getvalue()


G, H = gercek_proje()
reg_g = [{"id": "x", "ad": "x", "repo": "o/r", "kaynak_yol": "x", "klasor_hash": H, "commit": "c0ffee1"}]
kil = pk.kilit_guvenli_oku(G)[0]
k0 = kil["skiller"]["x"]
ESLEME = {"guncel": "güncel", "guncelleme-var": "GÜNCELLEME VAR", "elle-degismis": "ELLE DEĞİŞTİRİLMİŞ", "kaynak-yok": "KAYNAK KÜTÜPHANEDE YOK",
          "kurulum-eksik": "KURULUM EKSİK/BOZUK"}


def kontrol(skiller, beklenen_kod):
    kod = pk.skill_durumu(G, "x", k0, kil, skiller, se_gercek)
    yazi = gercek_durum(G, skiller)
    return kod == beklenen_kod and ESLEME[beklenen_kod] in yazi, (kod, yazi)


ok, ay = kontrol(reg_g, "guncel")
T("23a gerçek durum(): güncel", ok, ay)
ok, ay = kontrol([{**reg_g[0], "klasor_hash": "baska"}], "guncelleme-var")
T("23b gerçek durum(): GÜNCELLEME VAR", ok, ay)
ok, ay = kontrol([], "kaynak-yok")
T("23c gerçek durum(): KAYNAK KÜTÜPHANEDE YOK", ok, ay)
(G / ".agents" / "skills" / "x" / "SKILL.md").write_text("---\nname: x\ndescription: d\n---\nELLE DEĞİŞTİ\n", encoding="utf-8")
ok, ay = kontrol(reg_g, "elle-degismis")
T("23d gerçek durum(): ELLE DEĞİŞTİRİLMİŞ", ok, ay)
(G / ".agents" / "skills" / "x" / "SKILL.md").write_text("---\nname: x\ndescription: d\n---\ngövde\n", encoding="utf-8")
os.remove(G / ".claude" / "skills" / "x")
shutil.copytree(G / ".agents" / "skills" / "x", G / ".claude" / "skills" / "x")
ok, ay = kontrol(reg_g, "kurulum-eksik")
T("23e gerçek durum(): KURULUM EKSİK/BOZUK", ok, ay)
shutil.rmtree(G / ".claude" / "skills" / "x")
os.symlink("../../.agents/skills/x", G / ".claude" / "skills" / "x")
s = pk.saglik_hesapla({"tarama_kokleri": [str(docs)]}, reg_g, bugun=GUN)
T("23f gerçek skill-ekle ile sağlam proje: temiz", s["projeler"][0]["durum"] == "temiz", s["projeler"][0]["satirlar"])

# ------------------------------------------------------------------ 24 geriye uyumluluk (süreç içi)
kok, docs = yenile_ortam("t24")
for ad in ("projeleri_bul", "oku", "rapor_metni", "hesapla", "guncel_mi", "rapor_guncelle", "kullanan_projeler", "kisa_yol", "AYAR", "RAPOR"):
    if not hasattr(pk, ad):
        T(f"24a {ad} var", False)
T("24a eski modül arayüzü yerinde", all(hasattr(pk, a) for a in ("projeleri_bul", "oku", "rapor_metni", "hesapla", "guncel_mi",
                                                                  "rapor_guncelle", "kullanan_projeler", "kisa_yol", "AYAR", "RAPOR")))
proje_yap(docs, "R", ["a"])
ayar_yaz({"tarama_kokleri": [str(docs)]})
(KUT / "registry.json").write_text(json.dumps({"skiller": [sk("a")]}), encoding="utf-8")
c, kod = cik(pk.main, ["--skill", "boyle-bir-skill-yok"])
T("24b --skill bilinmeyen: 'Hiçbir projede kullanılmıyor.', rapor yazılmaz", "Hiçbir projede kullanılmıyor." in c and not pk.RAPOR.exists())
cik(pk.main, [])
T("24c bayraksız çalıştırma raporu yazar", pk.RAPOR.exists())
c, kod = cik(pk.main, ["--kontrol"])
T("24d --kontrol güncel -> 0", kod == 0 and "güncel" in c)
pk.RAPOR.write_text("eski", encoding="utf-8")
c, kod = cik(pk.main, ["--kontrol"])
T("24e --kontrol bayat -> main() 1 döndürür (eski davranış), _CIKIS 0 kalır", kod == 1 and pk._CIKIS == 0)
c, kod = cik(pk.main, ["--kontrol", "--siki"])
T("24f --kontrol --siki bayat -> _CIKIS 1", pk._CIKIS == 1)

# ------------------------------------------------------------------ 20 çıkış kodları (gerçek alt süreç)
kok = TMP / "t20"
shutil.rmtree(kok, ignore_errors=True)
(kok / "kut" / "araclar").mkdir(parents=True)
(kok / "kut" / "notlar").mkdir()
(kok / "docs").mkdir()
(kok / "evx").mkdir()
for f in ("proje-kullanimi.py", "ortak.py"):
    shutil.copy(ARACLAR / f, kok / "kut" / "araclar" / f)
(kok / "kut" / "registry.json").write_text(json.dumps({"skiller": []}), encoding="utf-8")
ORT = {**os.environ, "HOME": str(kok / "evx")}


def alt(*arg):
    r = subprocess.run([sys.executable, str(kok / "kut" / "araclar" / "proje-kullanimi.py"), *arg], capture_output=True, text=True,
                       env=ORT, cwd=str(kok / "docs"))
    return r.returncode, r.stdout, r.stderr


def ayar_k(a):
    (kok / "kut" / "projeler.json").write_text(json.dumps(a), encoding="utf-8")


ayar_k({"tarama_kokleri": [str(kok / "docs")]})
kod, c, _ = alt("--saglik", "--siki")
T("20a proje yokken --saglik --siki 0", kod == 0 and "Hiç proje bulunamadı" in c)
pk_docs = kok / "docs"
(pk_docs / "Pq" / ".skill-kutuphanesi").mkdir(parents=True)
(pk_docs / "Pq" / ".skill-kutuphanesi" / "kilit.json").write_text(json.dumps({"surum": 3, "kutuphane": str(kok / "kut"), "skiller": {}, "roller": [],
                                                                              "proje_yolu": str((pk_docs / "Pq").resolve())}), encoding="utf-8")
# skill-ekle.py bu kopyada yok -> 'denetlenemedi' = sorun fixture
kod, c, _ = alt("--saglik")
T("20b sorun durumunda --saglik çıkış 0", kod == 0 and "sorun" in c, c)
kod, c, _ = alt("--saglik", "--siki")
T("20c sorun + --siki çıkış 1", kod == 1)
kod, c, _ = alt("--saglik", "--ozet-json", "--siki")
T("20d --ozet-json --siki sorunda 1, stdout tek JSON", kod == 1 and json.loads(c)["durum"] == "sorun")
shutil.copy(ARACLAR / "skill-ekle.py", kok / "kut" / "araclar" / "skill-ekle.py")
kod, c, _ = alt("--saglik", "--siki")
T("20e temiz fixture + --siki çıkış 0", kod == 0 and "Genel durum: temiz" in c or kod == 0 and "Genel durum: dikkat" in c, c)
kod, c, _ = alt("--tara-kayitsiz", "--siki")
T("20f --tara-kayitsiz --siki: kayıtsız skilli klasör olsa da 0", kod == 0)
skilli(pk_docs / "Kayitsiz")
kod, c, _ = alt("--tara-kayitsiz", "--siki")
T("20g kayıtsız skilli klasör (dikkat) --siki ile 0", kod == 0 and "Kayitsiz" in c)
ayar_k({"tarama_kokleri": [str(pk_docs)], "kayitsiz_tarama": {"kokler": [str(kok / "evx" / "olmayan")]}})
kod, c, _ = alt("--tara-kayitsiz", "--siki")
T("20h olmayan tarama kökü sorun değil: 0", kod == 0)
yasak_kok = kok / "izinsiz"
yasak_kok.mkdir()
os.chmod(yasak_kok, 0)
try:
    ayar_k({"tarama_kokleri": [str(pk_docs)], "kayitsiz_tarama": {"kokler": [str(yasak_kok)]}})
    kod, c, _ = alt("--tara-kayitsiz", "--siki")
    izinsiz_ok = (kod == 1) or (os.geteuid() == 0)
    T("20i okunamayan tarama kökü + --siki -> 1", izinsiz_ok, (kod, c))
finally:
    os.chmod(yasak_kok, 0o755)
ayar_k({"tarama_kokleri": [str(pk_docs)]})
kod, c, _ = alt("--kontrol")
T("20j rapor yokken düz --kontrol kabukta 0 (eski davranış)", kod == 0 and "GÜNCEL DEĞİL" in c, (kod, c))
kod, c, _ = alt("--kontrol", "--siki")
T("20k bayat rapor + --kontrol --siki -> 1", kod == 1)
kod, c, _ = alt()
T("20l bayraksız çalıştırma 0 ve raporu yazar", kod == 0 and (kok / "kut" / "notlar" / "proje-kullanimi.md").exists())
kod, c, _ = alt("--kontrol", "--siki")
T("20m güncel rapor + --kontrol --siki -> 0", kod == 0 and "güncel" in c)
kod, c, _ = alt("--skill", "yok")
T("20n --skill çıkış 0", kod == 0 and "Hiçbir projede kullanılmıyor." in c)
kod, c, e = alt("--ekle", "a", "--cikar", "b")
T("20o iki yazıcı bayrağı -> 2", kod == 2)
kod, c, e = alt("--cikar", "Pq")
T("20p --cikar --neden'siz -> 2", kod == 2)
kod, c, e = alt("--yok-boyle-bayrak")
T("20q bilinmeyen bayrak -> 2 (argparse)", kod == 2)

# ------------------------------------------------------------------ 25 salt okuma kipleri hiçbir şey değiştirmez
kok, docs = yenile_ortam("t25")
se = se_tak()
proje_yap(docs, "R1", ["a"], disk=["a", "b"])
skilli(docs / "Aday")
os.symlink(docs / "Aday", docs / "lnk")
ayar_yaz({"tarama_kokleri": [str(docs)]})
once = agac_ozeti(docs, HOME)
once_ayar = pk.AYAR.read_bytes()
cik(pk.main, ["--saglik"])
cik(pk.main, ["--tara-kayitsiz"])
cik(pk.main, ["--saglik", "--ozet-json"])
T("25 salt okuma kipleri projeleri, ev klasörünü ve projeler.json'u değiştirmez", agac_ozeti(docs, HOME) == once and pk.AYAR.read_bytes() == once_ayar)

# ------------------------------------------------------------------ sonuç
shutil.rmtree(TMP, ignore_errors=True)
gecen = sum(1 for _, k in SONUC if k)
for ad, k in SONUC:
    if not k:
        print("BAŞARISIZ:", ad)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
