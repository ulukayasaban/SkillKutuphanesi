#!/usr/bin/env python3
"""P10 testleri: kullanıcının kendi skilleri için yerel kaynak (T7, kendi/ klasörü).
Kapsam: kaynak-cek.py yerel dalı (ağ yok), node_modules/package-lock/gizli dosya adı, arsiv-yerlestir.py (kayıt, KAYNAK.md, kısmi
çalıştırmada kayıp sayılmama), kapsam-denetimi.py yerel denetimi, kullanıcı düzenlemesi (hash değişir, inceleme eskir, projede güncelleme
görünür), aynı adlı halka açık skilde çıplak kimlik, arsiv-guncelle.py değişiklik sezgisi, dogrula.py şema kabulü.
Yalnız geçici klasör ve sahte veri: HOME geçici klasöre alınır, gerçek registry/kaynaklar/ev klasörü okunmaz ya da yazılmaz;
ağ (urllib, GitHub) kullanılmaz: kullanılırsa test düşer. Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import os
import re
import shutil
import sys
import tempfile
import types
import urllib.request
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p10test-"))
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


import ortak  # noqa: E402

kc = modul_yukle("kc_p10", "kaynak-cek.py")
ay = modul_yukle("ay_p10", "arsiv-yerlestir.py")
kd = modul_yukle("kd_p10", "kapsam-denetimi.py")
ag = modul_yukle("ag_p10", "arsiv-guncelle.py")
dg = modul_yukle("dg_p10", "dogrula.py")
se = modul_yukle("se_p10", "skill-ekle.py")
gb = modul_yukle("gb_p10", "gelistirici-bilgisi.py")


def yaz(yol, metin):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(metin, encoding="utf-8")


def fm(ad, aciklama="Kendi test skili: ornek isler icin kullan, baska islerde kullanma."):
    return f"---\nname: {ad}\ndescription: {aciklama}\n---\n"


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


# ---------------------------------------------------------------- sahte kütüphane kökü
LIB = TMP / "lib"
KENDI = LIB / "kendi"
ARAC_HARIC = [r"(^|/)node_modules/", r"(^|/)\.git/", r"\.(mp4|mov|webm|mkv|avi)$", r"-rendered\.html$"]
T7_KAYIT = {"repo": "yerel/kendi", "tur": "kendi", "bolum": "arsiv", "oncelik": 1, "yerel": "kendi", "lisans": "Kendi (özel)",
            "dosya_haric": [r"(^|/)package-lock\.json$"], "eklendi": "2026-11-12",
            "onay": {"kim": "kullanıcı", "tarih": "2026-11-12"}, "not": "sahte yerel kaynak"}
T1_KAYIT = {"repo": "ornek/halka", "tur": "tek-skil", "bolum": "arsiv", "oncelik": 3}


def kaynaklar_yaz(kayitlar):
    yaz(LIB / "kaynaklar.json", json.dumps({"ayna_klasorler": [], "max_dosya_mb": 5, "konum_haric": [r"(^|/)tests?/"],
                                            "skill_ici_haric": ARAC_HARIC, "arsivden_cikarilanlar": [],
                                            "repolar": kayitlar}, ensure_ascii=False, indent=2))


kaynaklar_yaz([T7_KAYIT, T1_KAYIT])
yaz(LIB / "kategoriler.json", json.dumps({"alanlar": {"d-ai-otomasyon": {"kategoriler": {"04-skill-plugin-yazimi": "x"}}}}))
yaz(LIB / "kategori-kurallari.json", json.dumps({"ad_kurallari": [], "yol_kurallari": [], "repo_varsayilan": {}}))
yaz(LIB / "ucret-siniflandirma.json", json.dumps({"siniflar": {}}))
yaz(LIB / "gelistiriciler.json", json.dumps({"repolar": {}}))
(LIB / "notlar").mkdir()

# kendi/ içeriği: bir skill; node_modules, package-lock ve gizli görünen adlar KOPYALANMAMALI
yaz(KENDI / "ornek-skil" / "SKILL.md", fm("ornek-skil") + "ilk surum\n")
yaz(KENDI / "ornek-skil" / "scripts" / "arac.py", "print('merhaba')\n")
yaz(KENDI / "ornek-skil" / "scripts" / "node_modules" / "paket" / "index.js", "module.exports = 1;\n")
yaz(KENDI / "ornek-skil" / "scripts" / "package-lock.json", "{}\n")
yaz(KENDI / "ornek-skil" / ".env", "SAHTE=gizli-degil-test\n")
yaz(KENDI / "ornek-skil" / "anahtar.pem", "sahte\n")

# ağ yasak: ağa çıkan her yol testi düşürür
AG_CAGRILARI = []


def ag_yasak(*a, **k):
    AG_CAGRILARI.append((a, k))
    raise AssertionError("AĞ KULLANILDI")


def yama_uygula(nesne, **kw):
    eski = {k: getattr(nesne, k) for k in kw}
    for k, v in kw.items():
        setattr(nesne, k, v)
    return eski


def yama_geri(nesne, eski):
    for k, v in eski.items():
        setattr(nesne, k, v)


GECICI = LIB / ".gecici"
REG = LIB / "registry.json"
ARSIV = LIB / "arsiv"
yamalar = [
    (kc, dict(GECICI=GECICI, KAYNAKLAR=LIB / "kaynaklar.json", KOK=LIB, repo_agaci=ag_yasak, repo_lisansi=ag_yasak,
              klon_dosyalari_al=ag_yasak, indir=ag_yasak)),
    (ay, dict(KOK=LIB, ARSIV=ARSIV, GECICI=GECICI, REGISTRY=REG, KATEGORILER=LIB / "kategoriler.json",
              KURALLAR=LIB / "kategori-kurallari.json", GELISTIRICILER=LIB / "gelistiriciler.json", TREND=LIB / "trend.json")),
    (kd, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG, repo_agaci=ag_yasak)),
    (ag, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG, gh_hazir=lambda: (True, 5000, ""), gh_api=ag_yasak,
              etkilenen_projeler=lambda r: {})),
    (gb, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", gh_api=ag_yasak)),
]
for m, kw in yamalar:
    yama_uygula(m, **kw)
ag.subprocess = types.SimpleNamespace(run=lambda *a, **k: types.SimpleNamespace(returncode=0, stdout="", stderr=""),
                                      CalledProcessError=Exception)
_urlopen = urllib.request.urlopen
urllib.request.urlopen = ag_yasak


def cek():
    return yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])


def yerlestir():
    return yakala(ay.main, argv=["arsiv-yerlestir.py"])


def manifest():
    return json.loads((GECICI / "cekilen" / "manifest.json").read_text(encoding="utf-8"))


def reg():
    return json.loads(REG.read_text(encoding="utf-8"))


def reg_yaz(d):
    REG.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def t7(d, ad):
    return next((s for s in d["skiller"] if s["repo"] == "yerel/kendi" and s["ad"] == ad), None)


try:
    # ================================================================== 1. yerel kaynak ağsız çekilir
    kod, cikti = cek()
    m = manifest()
    kay = next((x for x in m["kayitlar"] if x["repo"] == "yerel/kendi"), None)
    test("yerel kaynak çekildi (çıkış 0, 1 skill)", not kod and kay and kay["klasor_adi"] == "ornek-skil" and "Toplam kayıt: 1" in cikti, cikti)
    test("yerel çekme ağ kullanmadı", AG_CAGRILARI == [], AG_CAGRILARI)
    test("yerel kaynağın sürüm kimliği 40 haneli ve lisans kayıttan", bool(kay) and re.fullmatch(r"[0-9a-f]{40}", kay["commit"])
         and kay["lisans"] == "Kendi (özel)" and kay["tur"] == "kendi", kay)
    yerel_dizin = GECICI / "cekilen" / "yerel__kendi" / "ornek-skil"
    test("SKILL.md ve betik alındı", (yerel_dizin / "SKILL.md").exists() and (yerel_dizin / "scripts" / "arac.py").exists())
    test("node_modules alınmadı", not (yerel_dizin / "scripts" / "node_modules").exists())
    test("package-lock.json alınmadı (kayıttaki dosya_haric)", not (yerel_dizin / "scripts" / "package-lock.json").exists())
    test("gizli görünen dosya adları (.env, *.pem) alınmadı ve uyarıldı",
         not (yerel_dizin / ".env").exists() and not (yerel_dizin / "anahtar.pem").exists() and "gizli görünen dosya adı alınmadı" in cikti, cikti)
    test("kaynak klasörde gizli dosyalar olduğu gibi duruyor (silinmedi)", (KENDI / "ornek-skil" / ".env").exists())

    # node_modules içerik karşılaştırmasında sayılmaz; package-lock (eski skillerin hash'i için) sayılmaya devam eder
    h0 = ortak.klasor_hash(KENDI / "ornek-skil")
    yaz(KENDI / "ornek-skil" / "scripts" / "node_modules" / "paket" / "baska.js", "yeni dosya\n")
    h1 = ortak.klasor_hash(KENDI / "ornek-skil")
    yaz(KENDI / "ornek-skil" / "scripts" / "package-lock.json", '{"degisti": true}\n')
    h2 = ortak.klasor_hash(KENDI / "ornek-skil")
    test("klasor_hash node_modules'ı saymaz", h0 == h1)
    test("klasor_hash package-lock.json'ı saymaya devam eder (geriye uyum)", h1 != h2)
    test("node_modules içeren dosya ortak.yerel_agac ağacında yok", all("node_modules" not in e["path"] for e in ortak.yerel_agac(KENDI)[0]))
    k1 = ortak.yerel_commit(ortak.yerel_agac(KENDI, [r"(^|/)package-lock\.json$"])[0])
    yaz(KENDI / "ornek-skil" / "scripts" / "package-lock.json", '{"degisti": 2}\n')
    k2 = ortak.yerel_commit(ortak.yerel_agac(KENDI, [r"(^|/)package-lock\.json$"])[0])
    test("hariç tutulan package-lock.json sürüm kimliğini değiştirmez", k1 == k2)

    # ================================================================== 2. arşive yerleşir, kayıp sayılmaz
    # halka açık (T1) sahte skill de manifeste girer: kısmi çalıştırma senaryosu için
    halka = GECICI / "cekilen" / "ornek__halka" / "halka-skil"
    yaz(halka / "SKILL.md", fm("halka-skil") + "halka acik\n")
    m = manifest()
    m["kayitlar"].append({"repo": "ornek/halka", "tur": "tek-skil", "bolum": "arsiv", "oncelik": 3, "kimlik": "ornek__halka", "commit": "a" * 40, "lisans": "MIT",
                          "klasor_adi": "halka-skil", "kaynak_yol": "halka-skil", "asil_ad": None, "ust_skill": None, "aynalar": [],
                          "atlanan_dosyalar": [], "varyantlar": {}, "varyant_yollari": {}, "ad": "halka-skil", "aciklama": "halka",
                          "bagimlilik": None, "beklenen_dosya": 1, "inen_dosya": 1, "varyant_eksik": [],
                          "yerel": "cekilen/ornek__halka/halka-skil"})
    m["denetim"]["ornek/halka"] = {"commit": "a" * 40, "skill_md": {"halka-skil/SKILL.md": "secildi"}}
    (GECICI / "cekilen" / "manifest.json").write_text(json.dumps(m), encoding="utf-8")
    kod, cikti = yerlestir()
    d = reg()
    s = t7(d, "ornek-skil")
    test("arsiv-yerlestir: yerel skill kayda girdi (tercih, kimlik çıplak ad)",
         not kod and s and s["id"] == "ornek-skil" and s["durum"] == "tercih" and s["repo"] == "yerel/kendi", cikti)
    test("kayıt dosyası arşivde, node_modules ve package-lock arşive girmedi",
         s and (LIB / s["yol"] / "SKILL.md").exists() and not list((LIB / s["yol"]).rglob("node_modules"))
         and not list((LIB / s["yol"]).rglob("package-lock.json")), cikti)
    kmd = (LIB / s["yol"] / "KAYNAK.md").read_text(encoding="utf-8") if s else ""
    test("KAYNAK.md yerel kaynağı anlatır, sahte GitHub adresi yazmaz", "github.com/yerel" not in kmd and "kendi/ornek-skil" in kmd, kmd)
    test("toplam kayıt 2 (yerel 1 + halka açık 1)", len(d["skiller"]) == 2, len(d["skiller"]))
    test("registry denetimi yerel kaynağı da tutuyor", "yerel/kendi" in d["denetim"]
         and d["denetim"]["yerel/kendi"]["skill_md"].get("ornek-skil/SKILL.md") == "secildi", d["denetim"].keys())
    id1, yol1, hash1, halka_id = s["id"], s["yol"], s["klasor_hash"], t7(d, "halka-skil") or next(x for x in d["skiller"] if x["ad"] == "halka-skil")
    # incelendi say: düzenlemeden sonra "yeniden-incelenecek" olmalı
    s["inceleme"] = "incelendi"
    s["kalite"] = 4
    reg_yaz(d)

    # kısmi çalıştırma: yalnız halka açık kaynak indirildi, yerel kaynak manifestte YOK -> kayıp sayılmaz, olduğu gibi korunur
    m = manifest()
    m["kayitlar"] = [x for x in m["kayitlar"] if x["repo"] != "yerel/kendi"]
    m["denetim"].pop("yerel/kendi", None)
    (GECICI / "cekilen" / "manifest.json").write_text(json.dumps(m), encoding="utf-8")
    kod, cikti = yerlestir()
    d = reg()
    s = t7(d, "ornek-skil")
    test("kısmi çalıştırmada yerel kaynak kayıp sayılmadı (DURDU yok, kayıt aynı)",
         not kod and "DURDU" not in cikti and s and s["id"] == id1 and s["yol"] == yol1 and s["klasor_hash"] == hash1
         and not s.get("kaynak_durumu") and s.get("inceleme") == "incelendi", cikti)
    test("kısmi çalıştırmada yerel kaynağın denetim kaydı korundu", "yerel/kendi" in d["denetim"], d["denetim"].keys())
    test("yerel kaynak 'kayıp' ya da 'kaynakta-kaldirildi' olarak işaretlenmedi", all(not x.get("kaynak_durumu") for x in d["skiller"]), cikti)

    # ================================================================== 3. kapsam-denetimi yerel dalı
    kaynaklar_yaz([T7_KAYIT])                       # yalnız yerel kaynak: GitHub'a sorulacak kaynak yok
    kod, cikti = yakala(kd.main)
    test("kapsam-denetimi: işlenmiş yerel kaynakta 0 sorun, GitHub'a sorulmadı", not kod and "sorun: 0" in cikti and not AG_CAGRILARI, cikti)
    yaz(KENDI / "yeni-skil" / "SKILL.md", fm("yeni-skil") + "henuz islenmedi\n")
    kod, cikti = yakala(kd.main)
    test("kapsam-denetimi: kendi/ içinde işlenmemiş skill varsa sorun (çıkış 1)", kod == 1 and "yeni-skil" in cikti, cikti)
    shutil.rmtree(KENDI / "yeni-skil")
    kaynaklar_yaz([T7_KAYIT, T1_KAYIT])

    # ================================================================== 4. kullanıcı düzenlemesi: hash değişir, inceleme eskir, projede güncelleme görünür
    # önce yerel kaynağı yeniden çek (manifest) ve yerleştir; sahte proje bu kayıttan kurulur
    cek()
    m = manifest()
    kay0 = next(x for x in m["kayitlar"] if x["repo"] == "yerel/kendi")
    kod, cikti = yerlestir()
    d = reg()
    s = t7(d, "ornek-skil")
    test("yeniden çekme + yerleştirme aynı içerikte hash'i değiştirmedi", s["klasor_hash"] == hash1 and s["commit"] == kay0["commit"], cikti)

    def mutlak(liste):
        out = []
        for x in liste:
            y = dict(x)
            y["yol"] = str(LIB / x["yol"])
            out.append(y)
        return out

    se.canli_global = lambda s: {}
    se.hesap_skilleri = lambda: {}
    se.guncelleme_suruyor = lambda: None
    se.ARAC_JSON = TMP / "yok-araclar.json"
    se.registry = lambda: mutlak(reg()["skiller"])

    def se_calistir(*args):
        return yakala(se.main, argv=["skill-ekle.py"] + [str(a) for a in args])

    proje = TMP / "proje"
    proje.mkdir()
    kod, cikti = se_calistir(proje, "--arac", "yalniz-claude", "--skill", "ornek-skil", "--evet")
    kurulu = proje / ".claude" / "skills" / "ornek-skil" / "SKILL.md"
    test("yerel skill projeye kütüphane skili gibi kuruldu", not kod and kurulu.exists(), cikti)
    kod, cikti = se_calistir(proje, "--durum")
    test("kurulumdan hemen sonra güncelleme yok", "GÜNCELLEME VAR" not in cikti, cikti)

    # kullanıcı kendi/ içinde skili düzenler
    yaz(KENDI / "ornek-skil" / "SKILL.md", fm("ornek-skil") + "ikinci surum: duzenlendi\n")
    kod, cikti = cek()
    kay1 = next(x for x in manifest()["kayitlar"] if x["repo"] == "yerel/kendi")
    test("düzenleme yerel sürüm kimliğini değiştirdi", kay1["commit"] != kay0["commit"], cikti)
    kod, cikti = yerlestir()
    d = reg()
    s = t7(d, "ornek-skil")
    test("düzenleme klasor_hash'i değiştirdi, kimlik aynı kaldı", s["klasor_hash"] != hash1 and s["id"] == id1, cikti)
    test("incelenmiş skill düzenlenince 'yeniden-incelenecek' oldu (elle alanlar korundu)",
         s.get("inceleme") == "yeniden-incelenecek" and s.get("kalite") == 4, s.get("inceleme"))
    kod, cikti = se_calistir(proje, "--durum")
    test("projede --durum güncelleme gösterir", "GÜNCELLEME VAR" in cikti, cikti)
    kod, cikti = se_calistir(proje, "--guncelle", "--kuru")
    test("projede --guncelle --kuru yeni içeriği güncellenecek diye sayar", "guncellenecek" in cikti.lower() or "güncellenecek" in cikti.lower(), cikti)
    kod, cikti = se_calistir(proje, "--guncelle", "--evet")
    test("onaylı güncelleme düzenlenen içeriği projeye taşıdı", "ikinci surum" in kurulu.read_text(encoding="utf-8"), cikti)

    # ================================================================== 5. aylık zincir: kendi/ değişince 'değişen kaynak' sayılır
    kaynaklar_yaz([T7_KAYIT])                       # yalnız yerel kaynak: GitHub'a sorulacak kaynak yok
    AG_CAGRILARI.clear()
    kod, cikti = yakala(ag.rapor)
    degisen, sorunlu, _ayr = kod if isinstance(kod, tuple) else ([], [], {})
    test("arsiv-guncelle: işlenmiş yerel kaynak değişmemiş sayılır, GitHub'a sorulmaz", "yerel/kendi" not in degisen and not AG_CAGRILARI, (kod, cikti))
    yaz(KENDI / "ornek-skil" / "SKILL.md", fm("ornek-skil") + "ucuncu surum\n")
    kod, cikti = yakala(ag.rapor)
    degisen, sorunlu, _ayr = kod if isinstance(kod, tuple) else ([], [], {})
    test("arsiv-guncelle: kendi/ düzenlenince 'yerel/kendi' değişen kaynak olur ve erişilemeyen sayılmaz",
         "yerel/kendi" in degisen and "yerel/kendi" not in sorunlu and not AG_CAGRILARI, (kod, cikti))
    kaynaklar_yaz([T7_KAYIT, T1_KAYIT])
    cek()
    yerlestir()

    # ================================================================== 6. aynı adlı halka açık skill: çıplak kimlik el değiştirmez
    yaz(KENDI / "halka-skil" / "SKILL.md", fm("halka-skil", "Kendi sürümüm: ornek isler icin kullan, baska islerde kullanma.") + "benim surumum\n")
    cek()
    kod, cikti = yerlestir()
    d = reg()
    halka_s = next(x for x in d["skiller"] if x["repo"] == "ornek/halka")
    kendi_s = t7(d, "halka-skil")
    test("aynı adlı halka açık skill çıplak kimliğini korudu", halka_s["id"] == "halka-skil", [(x["id"], x["repo"]) for x in d["skiller"]])
    test("aynı adlı kendi skilim 'ad@yerel' kimliğini aldı", kendi_s and kendi_s["id"] == "halka-skil@yerel", cikti)
    test("iki kayıt da arşivde ayrı klasörlerde", halka_s["yol"] != kendi_s["yol"] and (LIB / kendi_s["yol"] / "SKILL.md").exists()
         and (LIB / halka_s["yol"] / "SKILL.md").exists())

    # ================================================================== 7. dogrula.py şema: T7 ve yerel/lisans alanları kabul edilir
    kaynaklar_yaz([T7_KAYIT, T1_KAYIT])
    h, u = dg.kayit_semalari_denetimi(LIB)
    kaynak_satirlari = [x for x in h + u if "kaynaklar.json" in x]
    test("dogrula: yerel ve lisans anahtarları şemada kabul edilir", not [x for x in kaynak_satirlari if "kaldırılmış" in x or "bilinmeyen anahtar" in x], kaynak_satirlari)
    bozuk = dict(T7_KAYIT, tip="T9")
    kaynaklar_yaz([bozuk])
    h, u = dg.kayit_semalari_denetimi(LIB)
    test("dogrula: kaldırılmış 'tip' alanı reddedilir", any("kaldırılmış 'tip'" in x for x in h + u), h + u)
    kaynaklar_yaz([T7_KAYIT, T1_KAYIT])

    # ================================================================== 8. gelistirici-bilgisi T7'yi GitHub'dan sormaz
    kaynaklar_yaz([T7_KAYIT])
    AG_CAGRILARI.clear()
    kod, cikti = yakala(gb.main, argv=["gelistirici-bilgisi.py"])
    gel = json.loads((LIB / "gelistiriciler.json").read_text(encoding="utf-8"))["repolar"].get("yerel/kendi") or {}
    test("gelistirici-bilgisi: yerel kaynak için GitHub'a sorulmadı", not AG_CAGRILARI, (kod, cikti))
    test("gelistirici-bilgisi: yerel kaynağa GitHub'sız geliştirici kaydı yazıldı (kullanıcı, resmî, güven hesaplı)",
         gel.get("sahip") == "kullanıcı" and gel.get("resmi_kaynak") is True and (gel.get("guven") or {}).get("puan") is not None
         and gel["guven"].get("sira") is None, gel)
    kaynaklar_yaz([T7_KAYIT, T1_KAYIT])

    test("test boyunca ağa çıkılmadı", AG_CAGRILARI == [], AG_CAGRILARI)
finally:
    urllib.request.urlopen = _urlopen
    shutil.rmtree(TMP, ignore_errors=True)

gecen = sum(1 for _, ok in SONUC if ok)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
