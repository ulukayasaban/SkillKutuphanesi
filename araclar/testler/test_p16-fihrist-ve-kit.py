#!/usr/bin/env python3
"""P16 testleri: fihrist-uret.py (saf işlevler; sahte ağ ile uçtan uca), dogrula.py fihrist ve kit denetimleri, bolum fihrist/katalog olan
kaynağın arşive çekilmediği araçlar (ortak.arsive_cekilir, kaynak-cek.py, arsiv-guncelle.py, kapsam-denetimi.py).
Ağ yok, gerçek ev klasörü yok; yalnız sahte veri ve geçici klasör. Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import types
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ARACLAR))
SONUC = []


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-900:]}"))


def yukle(ad, dosya):
    spec = importlib.util.spec_from_file_location(ad, ARACLAR / dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


import ortak  # noqa: E402

fu = yukle("fihrist_uret_t", "fihrist-uret.py")
dg = yukle("dogrula_p16", "dogrula.py")


def sessiz(f, *a, **k):
    """(dönüş değeri | SystemExit kodu, stdout) — çıktıyı yakalar."""
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        try:
            r = f(*a, **k)
        except SystemExit as e:
            r = e.code if e.code is not None else 0
    return r, tampon.getvalue()


# ---------------------------------------------------------------- ortak.arsive_cekilir
test("arsive_cekilir: T1 bolum yok -> evet", ortak.arsive_cekilir({"tip": "T1"}) is True)
test("arsive_cekilir: T1 bolum arsiv -> evet", ortak.arsive_cekilir({"tip": "T1", "bolum": "arsiv"}) is True)
test("arsive_cekilir: T1 bolum fihrist -> hayır", ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist"}) is False)
test("arsive_cekilir: T2 bolum katalog -> hayır", ortak.arsive_cekilir({"tip": "T2", "bolum": "katalog"}) is False)
test("arsive_cekilir: T5 (referans) -> hayır", ortak.arsive_cekilir({"tip": "T5"}) is False)
test("arsive_cekilir: T7 yerel -> evet", ortak.arsive_cekilir({"tip": "T7"}) is True)

# ---------------------------------------------------------------- fihrist saf işlevleri
test("aciklama_kisalt: boşluk tek aralık", fu.aciklama_kisalt("  a \n  b\t c ") == "a b c")
uzun = fu.aciklama_kisalt("x" * 500)
test("aciklama_kisalt: 300 karakterde kesilir (en çok 300, … ile biter)", len(uzun) == 300 and uzun.endswith("…"), len(uzun))
test("aciklama_kisalt: 300 ve altı dokunulmaz", fu.aciklama_kisalt("y" * 300) == "y" * 300)
test("aciklama_kisalt: None boş döner", fu.aciklama_kisalt(None) == "")

g = fu.skil_girdisi("skills/pdf", "---\nname: pdf-oku\ndescription: >\n  PDF dosyalarını\n  okur.\n---\nGövde", "o/r")
test("skil_girdisi: frontmatter name ve çok satırlı description", g == {"ad": "pdf-oku", "aciklama": "PDF dosyalarını okur.", "yol": "skills/pdf"}, g)
g = fu.skil_girdisi("skills/pdf", "gövde, frontmatter yok", "o/r")
test("skil_girdisi: frontmatter yoksa ad klasör adından, açıklama boş", g["ad"] == "pdf" and g["aciklama"] == "", g)
g = fu.skil_girdisi("", None, "o/repo-adi")
test("skil_girdisi: kök skil, metin okunamadı -> ad repo adı", g["ad"] == "repo-adi" and g["yol"] == "", g)

girdiler = [{"ad": "b", "aciklama": "B", "yol": "skills/b"}, {"ad": "a", "aciklama": "A", "yol": "skills/a"}]
yeni = fu.fihrist_kur("o/r", "c" * 40, "2026-11-18", girdiler)
test("fihrist_kur: yol sırasına dizer, skil_sayisi doğru, işaret yok",
     [x["yol"] for x in yeni["skiller"]] == ["skills/a", "skills/b"] and yeni["skil_sayisi"] == 2
     and all("arsivde" not in x and "inceleme" not in x for x in yeni["skiller"]) and yeni["commit"] == "c" * 40, yeni)
yeni2 = fu.fihrist_kur("o/r", "d" * 40, "2026-11-19", girdiler, None, {"skills/b"})
test("fihrist_kur: arşivde olan yol arsivde:true alır", [x.get("arsivde") for x in yeni2["skiller"]] == [None, True], yeni2)

# yenileme: eklenen / silinen / adı değişen, inceleme koruma
eski = fu.fihrist_kur("o/r", "c" * 40, "2026-11-01", [
    {"ad": "a", "aciklama": "A", "yol": "skills/a"}, {"ad": "b", "aciklama": "B", "yol": "skills/b"}, {"ad": "z", "aciklama": "Z", "yol": "skills/z"}])
eski["skiller"][0]["inceleme"] = {"commit": "c" * 40, "tarih": "2026-11-02", "sonuc": "temiz", "not": "güvenli"}
eski["skiller"][2]["inceleme"] = {"commit": "c" * 40, "tarih": "2026-11-02", "sonuc": "temiz"}
yenilenen = fu.fihrist_kur("o/r", "d" * 40, "2026-11-18", [
    {"ad": "a", "aciklama": "A2", "yol": "skills/a"}, {"ad": "b-yeni", "aciklama": "B", "yol": "skills/b"}, {"ad": "n", "aciklama": "N", "yol": "skills/n"}], eski)
fark = fu.fark_hesapla(eski, yenilenen)
test("fark_hesapla: eklenen / silinen / adı değişen", fark["eklenen"] == [("skills/n", "n")] and fark["silinen"] == [("skills/z", "z")]
     and fark["ad_degisen"] == [("skills/b", "b", "b-yeni")], fark)
test("yenileme: aynı yolun inceleme notu korunur", yenilenen["skiller"][0].get("inceleme", {}).get("not") == "güvenli", yenilenen["skiller"][0])
test("yenileme: silinen skilin incelemesi düşer ve raporlanır", all(x["yol"] != "skills/z" for x in yenilenen["skiller"]) and fark["inceleme_kaybolan"] == ["skills/z"], fark)
test("fark_hesapla: eski yoksa hepsi eklenen", len(fu.fark_hesapla(None, yenilenen)["eklenen"]) == 3)
satirlar = fu.ozet_satirlari("o/r", yenilenen, eski, fark, okunamayan=2)
test("ozet_satirlari: eklenen, silinen, adı değişen, okunamayan ve düşen inceleme görünür",
     any("eklenen: n" in s for s in satirlar) and any("silinen: z" in s for s in satirlar) and any("adı değişen: b -> b-yeni" in s for s in satirlar)
     and any("2 SKILL.md okunamadı" in s for s in satirlar) and any("inceleme notu düştü" in s for s in satirlar), satirlar)
test("ozet_satirlari: --kuru ve yeni fihrist belirtilir", any("--kuru" in s for s in fu.ozet_satirlari("o/r", yeni, None, fu.fark_hesapla(None, yeni), 0, True))
     and any("yeni fihrist" in s for s in fu.ozet_satirlari("o/r", yeni, None, fu.fark_hesapla(None, yeni))))

# ---------------------------------------------------------------- skil seçimi (dahil/haric, ayna): kaynak-cek.py ile aynı işlev
agac = [{"path": p, "type": "blob", "sha": f"s{i}", "size": 10} for i, p in enumerate([
    "skills/a/SKILL.md", "skills/a/ref.md", "skills/b/SKILL.md", "examples/e/SKILL.md", "tests/t/SKILL.md", "docs/d/skill.md",
    ".claude/skills/a/SKILL.md", "SKILL.md"])]
ayar = {"konum_haric": ["(^|/)tests?/", "(^|/)examples?/"], "ayna_klasorler": [], "skill_ici_haric": [], "arsivden_cikarilanlar": []}
sec = fu.skil_klasorleri_sec([], agac, ayar, "o/r")
test("skil_klasorleri_sec: kayıt yoksa test/örnek hariç hepsi; kök skil '' ; skill.md küçük harf bulunur",
     "" in sec and "skills/b" in sec and "docs/d" in sec and "examples/e" not in sec and "tests/t" not in sec and sec["docs/d"] == "docs/d/skill.md", sec)
sec = fu.skil_klasorleri_sec([{"repo": "o/r", "tip": "T1", "dahil": ["^skills/"]}], agac, ayar, "o/r")
test("skil_klasorleri_sec: dahil deseni yalnız eşleşenleri alır", set(sec) == {"skills/a", "skills/b"}, sec)
sec = fu.skil_klasorleri_sec([{"repo": "o/r", "tip": "T1", "dahil": ["^skills/"], "haric": ["^skills/b/"]}], agac, ayar, "o/r")
test("skil_klasorleri_sec: haric deseni çıkarır", set(sec) == {"skills/a"}, sec)
sec = fu.skil_klasorleri_sec([{"repo": "o/r", "tip": "T1", "dahil": ["^skills/a/"]}, {"repo": "o/r", "tip": "T4", "dahil": ["^docs/"]}], agac, ayar, "o/r")
test("skil_klasorleri_sec: aynı repoya iki kayıt birleşir", set(sec) == {"skills/a", "docs/d"}, sec)

# ---------------------------------------------------------------- fihrist-uret main(): sahte ağ ile uçtan uca
SKILLER = {"skills/a/SKILL.md": "---\nname: a\ndescription: Birinci skil\n---\n", "skills/b/SKILL.md": "---\nname: b\ndescription: İkinci skil\n---\n",
           "skills/c/SKILL.md": "---\nname: c\ndescription: Üçüncü\n---\n"}
state = {"sha": "1" * 40, "tree": ["skills/a/SKILL.md", "skills/b/SKILL.md"], "okunamayan": set(), "cagrilar": []}


def sahte_agac(repo, sha=None):
    state["cagrilar"].append(("agac", repo))
    return state["sha"], {"tree": [{"path": p, "type": "blob", "sha": "x", "size": 5} for p in state["tree"]], "truncated": False, "_kaynak": "api"}


def sahte_ham(repo, yol, ref="HEAD", azami=0):
    state["cagrilar"].append(("ham", yol))
    return None if yol in state["okunamayan"] else SKILLER[yol]


tmp = Path(tempfile.mkdtemp(prefix="p16test-"))
eski_ortak = {a: getattr(ortak, a) for a in ("repo_agaci", "ham_metin", "KAYNAKLAR", "REGISTRY")}
eski_fihrist = fu.FIHRIST
try:
    (tmp / "kaynaklar.json").write_text(json.dumps({"konum_haric": [], "ayna_klasorler": [], "skill_ici_haric": [], "repolar": [
        {"repo": "dev/koleksiyon", "tip": "T1", "oncelik": 4, "bolum": "fihrist"}]}), encoding="utf-8")
    (tmp / "registry.json").write_text(json.dumps({"skiller": [{"repo": "dev/koleksiyon", "kaynak_yol": "skills/b", "id": "b"},
                                                               {"repo": "baska/repo", "kaynak_yol": "skills/a", "id": "a"}]}), encoding="utf-8")
    ortak.repo_agaci, ortak.ham_metin = sahte_agac, sahte_ham
    ortak.KAYNAKLAR, ortak.REGISTRY = tmp / "kaynaklar.json", tmp / "registry.json"
    fu.FIHRIST = tmp / "fihrist"
    hedef = tmp / "fihrist" / "dev__koleksiyon.json"

    r, cikti = sessiz(fu.main, ["dev/koleksiyon", "--kuru"])
    test("main --kuru: özet basar, dosya yazmaz", r == 0 and not hedef.exists() and "2 skil" in cikti and "--kuru" in cikti, (r, cikti))

    r, cikti = sessiz(fu.main, ["dev/koleksiyon"])
    d = json.loads(hedef.read_text(encoding="utf-8")) if hedef.exists() else {}
    test("main: fihrist yazılır (repo, commit, skil_sayisi, ad, açıklama, yol)", r == 0 and d.get("repo") == "dev/koleksiyon" and d.get("commit") == "1" * 40
         and d.get("skil_sayisi") == 2 and d["skiller"][0] == {"ad": "a", "aciklama": "Birinci skil", "yol": "skills/a"}, (r, d))
    test("main: aynı repoda registry'de olan skil arsivde:true, başka reponun aynı yolu işaretlenmez",
         d["skiller"][1].get("arsivde") is True and "arsivde" not in d["skiller"][0], d)
    test("main: üretilen dosya dogrula şemasından geçer", dg.fihrist_hatalari(d, "dev/koleksiyon") == [], dg.fihrist_hatalari(d, "dev/koleksiyon"))

    # yenileme: inceleme notu elle eklendi, kaynakta c eklendi, a silindi
    d["skiller"][0]["inceleme"] = {"commit": "1" * 40, "tarih": "2026-11-18", "sonuc": "temiz", "not": "ok"}
    d["skiller"][1]["inceleme"] = {"commit": "1" * 40, "tarih": "2026-11-18", "sonuc": "temiz"}
    hedef.write_text(json.dumps(d), encoding="utf-8")
    state["sha"], state["tree"] = "2" * 40, ["skills/b/SKILL.md", "skills/c/SKILL.md"]
    r, cikti = sessiz(fu.main, ["dev/koleksiyon"])
    d2 = json.loads(hedef.read_text(encoding="utf-8"))
    test("main yenileme: eklenen ve silinen raporlanır, silinenin inceleme notu düştüğü uyarılır",
         "eklenen: c" in cikti and "silinen: a" in cikti and "inceleme notu düştü" in cikti, cikti)
    test("main yenileme: kalan skilin inceleme notu korunur, commit güncellenir",
         [x["yol"] for x in d2["skiller"]] == ["skills/b", "skills/c"] and d2["skiller"][0].get("inceleme", {}).get("sonuc") == "temiz"
         and d2["commit"] == "2" * 40, d2)

    # SKILL.md okunamadı: ad klasörden, uyarı
    state["okunamayan"] = {"skills/c/SKILL.md"}
    r, cikti = sessiz(fu.main, ["dev/koleksiyon"])
    d3 = json.loads(hedef.read_text(encoding="utf-8"))
    test("main: okunamayan SKILL.md uyarılır, ad klasör adından", "1 SKILL.md okunamadı" in cikti and d3["skiller"][1] == {"ad": "c", "aciklama": "", "yol": "skills/c"}, (cikti, d3))

    # kural eşleşmesi yok: HATA
    state["tree"] = ["README.md"]
    tampon = io.StringIO()
    with contextlib.redirect_stderr(tampon):
        r, _ = sessiz(fu.main, ["dev/koleksiyon"])
    test("main: seçilen SKILL.md yoksa çıkış 2 ve dosya değişmez", r == 2 and "seçilen SKILL.md yok" in tampon.getvalue()
         and json.loads(hedef.read_text(encoding="utf-8"))["commit"] == "2" * 40, (r, tampon.getvalue()))
    tampon = io.StringIO()
    with contextlib.redirect_stderr(tampon):
        r, _ = sessiz(fu.main, ["gecersiz-ad"])
    test("main: geçersiz repo adı çıkış 2", r == 2, r)
finally:
    for a, v in eski_ortak.items():
        setattr(ortak, a, v)
    fu.FIHRIST = eski_fihrist
    shutil.rmtree(tmp, ignore_errors=True)

# ---------------------------------------------------------------- dogrula: fihrist şeması
iyi_f = {"repo": "o/r", "commit": "a" * 40, "tarih": "2026-11-18", "skil_sayisi": 1,
         "skiller": [{"ad": "x", "aciklama": "açıklama", "yol": "skills/x", "arsivde": True,
                      "inceleme": {"commit": "a" * 40, "tarih": "2026-11-18", "sonuc": "temiz", "not": "n"}}]}
test("fihrist_hatalari: geçerli fihrist hata vermez", dg.fihrist_hatalari(iyi_f, "o/r") == [], dg.fihrist_hatalari(iyi_f, "o/r"))
test("fihrist_hatalari: dosya adındaki repo ile uyuşmazlık HATA", any("uyuşmuyor" in x for x in dg.fihrist_hatalari(iyi_f, "baska/repo")))
test("fihrist_hatalari: skil_sayisi listeyle uyuşmazsa HATA", any("skil_sayisi" in x for x in dg.fihrist_hatalari({**iyi_f, "skil_sayisi": 5})))
test("fihrist_hatalari: tarih / commit / repo bozuksa HATA", len(dg.fihrist_hatalari({**iyi_f, "tarih": "dün", "commit": "", "repo": "x"})) >= 3)
test("fihrist_hatalari: ad / yol / açıklama tipi ve arsivde bool", len(dg.fihrist_hatalari({**iyi_f, "skiller": [{"ad": "", "aciklama": 1, "yol": None, "arsivde": "evet"}]})) >= 4)
test("fihrist_hatalari: yol tekrarı HATA", any("tekrarlan" in x for x in dg.fihrist_hatalari({**iyi_f, "skil_sayisi": 2, "skiller": iyi_f["skiller"] * 2})))
test("fihrist_hatalari: kök skil (yol '') geçerli", dg.fihrist_hatalari({**iyi_f, "skiller": [{"ad": "k", "aciklama": "", "yol": ""}]}) == [])
test("fihrist_hatalari: inceleme biçimi bozuksa HATA", any("inceleme" in x for x in dg.fihrist_hatalari(
    {**iyi_f, "skiller": [{"ad": "x", "aciklama": "", "yol": "y", "inceleme": {"sonuc": "temiz"}}]})))
test("fihrist_hatalari: skiller liste değilse HATA, sözlük olmayan dosya HATA", dg.fihrist_hatalari({**iyi_f, "skiller": "x"}) and dg.fihrist_hatalari([]) == ["fihrist dosyası sözlük değil"])

# ---------------------------------------------------------------- dogrula: kit şeması
iyi_k = {"repo": "o/kit", "ad": "Kit", "ne_yapar": "iskelet", "yapi_ozeti": ["skills/: skiller"], "skiller": ["a"],
         "kurulum_betigi": {"var": True, "yol": "kur.sh", "ne_yapar": "paket kurar"}, "genel_klasore_yazar": False, "baslamis_projede": "yalnız skills/"}
test("kit_hatalari: geçerli kit hata vermez", dg.kit_hatalari(iyi_k) == [], dg.kit_hatalari(iyi_k))
test("kit_hatalari: betik yok (var false, yol/ne_yapar yok) geçerli", dg.kit_hatalari({**iyi_k, "kurulum_betigi": {"var": False}}) == [])
test("kit_hatalari: betik var ama yol/ne_yapar yok HATA", any("var true" in x for x in dg.kit_hatalari({**iyi_k, "kurulum_betigi": {"var": True}})))
test("kit_hatalari: genel_klasore_yazar bool değil, listeler bozuk, boş metin HATA",
     len(dg.kit_hatalari({**iyi_k, "genel_klasore_yazar": "hayır", "yapi_ozeti": "x", "skiller": [1], "ne_yapar": " "})) >= 4)
test("kit_hatalari: not metin değilse HATA, not metinse geçerli", dg.kit_hatalari({**iyi_k, "not": "n"}) == [] and dg.kit_hatalari({**iyi_k, "not": 1}))
test("kit_hatalari: sözlük olmayan kayıt HATA", dg.kit_hatalari("x") == ["kit kaydı sözlük değil"])


# ---------------------------------------------------------------- dogrula: kaynak kaydıyla karşılıklı denetim (_e8_fihrist_kit)
def kok_kur(kayitlar, fihristler=None, kitler=None):
    t = Path(tempfile.mkdtemp(prefix="p16kok-"))
    (t / "kaynaklar.json").write_text(json.dumps({"repolar": kayitlar}), encoding="utf-8")
    if fihristler is not None:
        (t / "fihrist").mkdir()
        for ad, d in fihristler.items():
            (t / "fihrist" / ad).write_text(d if isinstance(d, str) else json.dumps(d), encoding="utf-8")
    if kitler is not None:
        (t / "kitler.json").write_text(kitler if isinstance(kitler, str) else json.dumps(kitler), encoding="utf-8")
    return t


def e8(kok):
    h, u = [], []
    dg._e8_fihrist_kit(kok, h, u)
    return h, u


FK = {"repo": "o/r", "tip": "T1", "tur": "dev-koleksiyon", "bolum": "fihrist"}
KK = {"repo": "o/kit", "tip": "T1", "tur": "kit", "bolum": "katalog"}
t = kok_kur([FK])
try:
    h, u = e8(t)
    test("_e8: bolum fihrist kaynağın fihrist dosyası yoksa HATA", len(h) == 1 and "fihrist/o__r.json yok" in h[0] and not u, (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([FK], {"o__r.json": iyi_f})
try:
    h, u = e8(t)
    test("_e8: fihrist dosyası varsa ve geçerliyse hata ve uyarı yok", h == [] and u == [], (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([FK], {"o__r.json": {**iyi_f, "skil_sayisi": 9}})
try:
    h, u = e8(t)
    test("_e8: fihrist şema hatası HATA (dosya adıyla)", len(h) == 1 and h[0].startswith("fihrist/o__r.json:") and "skil_sayisi" in h[0], h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([FK], {"o__r.json": "{bozuk"})
try:
    h, u = e8(t)
    test("_e8: fihrist dosyası ayrıştırılamıyorsa HATA", any("ayrıştırılamadı" in x for x in h), h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([{"repo": "o/r", "tip": "T1"}], {"o__r.json": iyi_f, "x__y.json": {**iyi_f, "repo": "x/y"}})
try:
    h, u = e8(t)
    test("_e8: kaynağı olmayan (bolum fihrist olmayan) fihrist dosyası UYARI, HATA değil", h == [] and len(u) == 2 and all("karşılığı yok" in x for x in u), (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([{"repo": "o/r", "tip": "T1", "bolum": "arsiv"}])
try:
    h, u = e8(t)
    test("_e8: fihrist/ klasörü ve kitler.json hiç yoksa, kaynak da istemiyorsa sessiz", h == [] and u == [], (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK])
try:
    h, u = e8(t)
    test("_e8: tur kit kaynağın kitler.json dosyası yoksa HATA", len(h) == 1 and "kitler.json yok" in h[0], h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler={"_aciklama": "x", "kitler": []})
try:
    h, u = e8(t)
    test("_e8: tur kit kaynağın kitler.json'da kaydı yoksa HATA", len(h) == 1 and "kaydı yok" in h[0], h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler={"kitler": [iyi_k | {"repo": "o/kit"}]})
try:
    h, u = e8(t)
    test("_e8: kit kaydı geçerliyse hata ve uyarı yok", h == [] and u == [], (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler={"kitler": [{**iyi_k, "repo": "o/kit", "genel_klasore_yazar": 1}]})
try:
    h, u = e8(t)
    test("_e8: kit şema hatası HATA (repo adıyla)", len(h) == 1 and "o/kit" in h[0] and "genel_klasore_yazar" in h[0], h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([{"repo": "o/r", "tip": "T1"}], kitler={"kitler": [iyi_k]})
try:
    h, u = e8(t)
    test("_e8: kaynağı olmayan kit kaydı UYARI", h == [] and len(u) == 1 and "o/kit" in u[0], (h, u))
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler={"kitler": [iyi_k, iyi_k]})
try:
    h, u = e8(t)
    test("_e8: aynı kit iki kez HATA", any("tekrarlan" in x for x in h), h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler="{bozuk")
try:
    h, u = e8(t)
    test("_e8: kitler.json ayrıştırılamıyorsa HATA", any("kitler.json" in x for x in h), h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([KK], kitler={"_aciklama": "x"})
try:
    h, u = e8(t)
    test("_e8: kitler.json'da 'kitler' listesi yoksa HATA", any("'kitler' listesi yok" in x for x in h), h)
finally:
    shutil.rmtree(t, ignore_errors=True)
t = kok_kur([FK, KK], {"o__r.json": iyi_f}, {"kitler": [iyi_k]})
try:
    h, u = [], []
    h2, u2 = dg.kayit_semalari_denetimi(t)
    test("kayit_semalari_denetimi: fihrist ve kit denetimi zincire bağlı", h2 == [] and u2 == [], (h2, u2))
    (t / "fihrist" / "o__r.json").unlink()
    h2, u2 = dg.kayit_semalari_denetimi(t)
    test("kayit_semalari_denetimi: fihrist dosyası kaybolunca zincirde HATA", any("fihrist/o__r.json yok" in x for x in h2), h2)
finally:
    shutil.rmtree(t, ignore_errors=True)

# gerçek kütüphanede boş kitler.json var ve geçerli
gercek_kit = ortak.json_oku(ortak.KOK / "kitler.json")
test("kitler.json var, 'kitler' listesi ve açıklaması tanımlı", isinstance(gercek_kit, dict) and isinstance(gercek_kit.get("kitler"), list) and gercek_kit.get("_aciklama"), gercek_kit)

# ---------------------------------------------------------------- kaynak-cikar.py: fihrist ve kit kaydı çıkarma adımları
kcik = yukle("kaynak_cikar_p16", "kaynak-cikar.py")
t = kok_kur([{"repo": "d/k", "tip": "T1", "bolum": "fihrist"}], {"d__k.json": {**iyi_f, "repo": "d/k"}}, {"kitler": [{**iyi_k, "repo": "d/k"}]})
try:
    (t / "registry.json").write_text(json.dumps({"skiller": []}), encoding="utf-8")
    rap = kcik.rapor_uret(t, "repo", "d/k")
    adimlar = " | ".join(rap["adimlar"])
    test("kaynak-cikar: fihrist dosyası ve kit kaydı varsa çıkarma adımlarında 5b / 5c çıkar", "5b. fihrist/d__k.json" in adimlar and "5c. kitler.json" in adimlar, adimlar)
    (t / "fihrist" / "d__k.json").unlink()
    (t / "kitler.json").write_text(json.dumps({"kitler": []}), encoding="utf-8")
    adimlar = " | ".join(kcik.rapor_uret(t, "repo", "d/k")["adimlar"])
    test("kaynak-cikar: fihrist ve kit kaydı yoksa 5b / 5c adımı eklenmez", "5b." not in adimlar and "5c." not in adimlar, adimlar)
finally:
    shutil.rmtree(t, ignore_errors=True)

# ---------------------------------------------------------------- arşive çekilmeyen kaynaklar: kaynak-cek.py
kc = yukle("kaynak_cek_p16", "kaynak-cek.py")
tmp = Path(tempfile.mkdtemp(prefix="p16kc-"))
try:
    (tmp / "kaynaklar.json").write_text(json.dumps({"konum_haric": [], "ayna_klasorler": [], "skill_ici_haric": [], "max_dosya_mb": 1, "repolar": [
        {"repo": "dev/koleksiyon", "tip": "T1", "bolum": "fihrist"}, {"repo": "kit/iskelet", "tip": "T2", "bolum": "katalog"}]}), encoding="utf-8")
    cagri = []

    def agac_yasak(*a, **k):
        cagri.append(a)
        raise AssertionError("fihrist/katalog kaynağı için GitHub'a gidilmemeli")

    kc.KAYNAKLAR, kc.GECICI, kc.repo_agaci = tmp / "kaynaklar.json", tmp / "gecici", agac_yasak
    argv0 = sys.argv
    sys.argv = ["kaynak-cek.py"]
    r, cikti = sessiz(kc.main)
    sys.argv = argv0
    test("kaynak-cek: bolum fihrist/katalog kayıtları çekilmez (ağ çağrısı yok, 0 kayıt)", r in (0, None) and not cagri and "Toplam kayıt: 0" in cikti, (r, cagri, cikti))
    sys.argv = ["kaynak-cek.py", "--repo", "dev/koleksiyon"]
    r, cikti = sessiz(kc.main)
    sys.argv = argv0
    test("kaynak-cek --repo: fihrist kaynağı adıyla istenince de çekilmez", r in (0, None) and not cagri and "Toplam kayıt: 0" in cikti, (r, cagri, cikti))
    k, tanimsiz = kc.atla_kumesi("dev/koleksiyon", [{"repo": "dev/koleksiyon", "tip": "T1", "bolum": "fihrist"}], cevir=lambda x: x)
    test("kaynak-cek --atla: fihrist kaynağı 'T1-T4 kaydı yok' sayılır (çekilen kaynak değil)", tanimsiz == ["dev/koleksiyon"], tanimsiz)
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------------------------------------------------------------- arsiv-guncelle.py rapor(): fihrist/katalog kaynağına commit sorgusu yok
ag = yukle("arsiv_guncelle_p16", "arsiv-guncelle.py")
tmp = Path(tempfile.mkdtemp(prefix="p16ag-"))
try:
    (tmp / "kaynaklar.json").write_text(json.dumps({"skill_ici_haric": [], "repolar": [
        {"repo": "dev/koleksiyon", "tip": "T1", "bolum": "fihrist"}, {"repo": "kit/iskelet", "tip": "T2", "bolum": "katalog"},
        {"repo": "normal/repo", "tip": "T1"}]}), encoding="utf-8")
    (tmp / "registry.json").write_text(json.dumps({"skiller": [{"repo": "normal/repo", "commit": "5" * 40, "id": "n"}]}), encoding="utf-8")
    sorgulanan = []

    def sahte_gh(yol, *a, **k):
        sorgulanan.append(yol)
        return {"sha": "5" * 40}

    ag.KAYNAKLAR, ag.REGISTRY, ag.gh_api = tmp / "kaynaklar.json", tmp / "registry.json", sahte_gh
    ag.gh_hazir = lambda: (True, 100, "")
    ag.subprocess = types.SimpleNamespace(run=lambda *a, **k: None)
    r, cikti = sessiz(ag.rapor)
    test("arsiv-guncelle rapor: yalnız arşive çekilen kaynak sorgulanır (fihrist/katalog atlanır)",
         sorgulanan == ["repos/normal/repo/commits/HEAD"] and "Tüm kaynaklar güncel" in cikti, (sorgulanan, cikti))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------------------------------------------------------------- kapsam-denetimi.py: fihrist/katalog SKILL.md'leri sorun sayılmaz
kd = yukle("kapsam_p16", "kapsam-denetimi.py")
tmp = Path(tempfile.mkdtemp(prefix="p16kd-"))
try:
    (tmp / "notlar").mkdir()
    (tmp / "registry.json").write_text(json.dumps({"skiller": [], "bilesenler": [], "denetim": {}}), encoding="utf-8")
    kayitlar = {"repolar": [{"repo": "dev/koleksiyon", "tip": "T1", "bolum": "fihrist"}, {"repo": "kit/iskelet", "tip": "T1", "bolum": "katalog"}]}
    (tmp / "kaynaklar.json").write_text(json.dumps(kayitlar), encoding="utf-8")
    kd.KOK, kd.REGISTRY, kd.KAYNAKLAR = tmp, tmp / "registry.json", tmp / "kaynaklar.json"
    agac_cagri = []

    def agac_say(repo, sha=None):
        agac_cagri.append(repo)
        return {"tree": [{"path": f"s{i}/SKILL.md", "type": "blob", "sha": "x"} for i in range(5)], "truncated": False}

    kd.agac_al = agac_say
    r, cikti = sessiz(kd.main)
    rapor = (tmp / "notlar" / "kapsam-denetimi.md").read_text(encoding="utf-8")
    test("kapsam-denetimi: fihrist/katalog kaynağı sorun sayılmaz (çıkış 0, 'denetim kaydı yok' ve 'referans' sorunu yok)",
         r == 0 and "SORUN" not in cikti and not agac_cagri, (r, cikti, agac_cagri))
    test("kapsam-denetimi: rapor 'Arşive çekilmeyen kaynaklar' bölümünde ikisini listeler",
         "Arşive çekilmeyen kaynaklar" in rapor and "dev/koleksiyon" in rapor and "kit/iskelet" in rapor, rapor)
    kayitlar["repolar"][0].pop("bolum")
    (tmp / "kaynaklar.json").write_text(json.dumps(kayitlar), encoding="utf-8")
    r, cikti = sessiz(kd.main)
    test("kapsam-denetimi: bolum olmayan T1 kaynağı hâlâ arşivli sayılır ('denetim kaydı yok' sorunu)", r == 1 and "denetim kaydı yok" in cikti, (r, cikti))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------------------------------------------------------------- arsiv-yerlestir / katalog-uret / skill-readme: kaynak kaydı bolumüne bakmaz, registry'den üretir
# (arşive çekilmeyen kaynağın registry'de skili olmadığı için bu araçlar ona hiçbir şey üretmez; kod okumayla doğrulandı, burada yalnız sözleşme sınanır)
ay = (ARACLAR / "arsiv-yerlestir.py").read_text(encoding="utf-8")
test("arsiv-yerlestir: arşive yerleştirilecek kayıtlar kaynak-cek manifestinden gelir (kaynaklar.json'u doğrudan taramaz)",
     'json_oku(GECICI / "cekilen" / "manifest.json")' in ay and "manifest.get(\"kayitlar\")" in ay)

gecen = sum(1 for _, k in SONUC if k)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
