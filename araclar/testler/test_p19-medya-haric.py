#!/usr/bin/env python3
"""P19 testleri: arşive geri gelmeyecek medya dışlama listesi (kaynaklar.json -> medya_haric).
Kapsam:
- ortak.py: medya_haric_yol_gecerli, medya_haric_kumesi, medya_haric_skill_kumesi, klasor_hash (haric_yollar), yerel_agac (tam_haric)
- kaynak-cek.py: dosyalari_listele ve agac_klasor_hash medya_haric dosyalarını indirmez/saymaz, atlanan_dosyalar'a eklemez
- arsiv-yerlestir.py: .gecici içinde dışlanan dosya bulunsa bile arşive kopyalamaz, güncellemede geri getirmez, diğer dosyalar aynen gelir,
  klasor_hash/KAYNAK.md/registry.json üzerinde yanlış fark üretmez (incelenmiş skill bu yüzden yeniden-incelenecek olmaz)
- dogrula.py: medya_haric şeması (düz liste ve {yol: neden} sözlüğü geçerli; yol geçişi '..', mutlak yol, ters bölü, boş yol HATA;
  listede olup arşivde hâlâ duran dosya veya hiçbir skil klasöründe görünmeyen yol UYARI)
Yalnız geçici klasör ve sahte veri; gerçek kütüphane dosyalarına ve ev klasörüne dokunmaz, ağ kullanmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import urllib.request
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p19test-"))
os.environ["HOME"] = str(TMP / "home")
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

kc = modul_yukle("kc_p19", "kaynak-cek.py")
ay = modul_yukle("ay_p19", "arsiv-yerlestir.py")
dg = modul_yukle("dg_p19", "dogrula.py")
ag = modul_yukle("ag_p19", "arsiv-guncelle.py")
kd = modul_yukle("kd_p19", "kapsam-denetimi.py")


def yaz(yol, veri):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(veri, bytes):
        yol.write_bytes(veri)
    elif isinstance(veri, str):
        yol.write_text(veri, encoding="utf-8")
    else:
        yol.write_text(json.dumps(veri, ensure_ascii=False, indent=2), encoding="utf-8")


def fm(ad, aciklama="Ornek medya testi skili: belirli isler icin kullan, digerlerinde kullanma."):
    return f"---\nname: {ad}\ndescription: {aciklama}\n---\n"


def yakala(f, *a, argv=None, **k):
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


_urlopen = urllib.request.urlopen
urllib.request.urlopen = ag_yasak

try:
    # ================================================================== 1. Yol doğrulama ve küme yardımcıları
    gecerli_yollar = ["docs/a.gif", "skills/foo/docs/a.gif", "assets/admin_2026-01.json.gz", ".claude/skills/x/a.png"]
    gecersiz_yollar = ["", " ", "/etc/passwd", "~/a.gif", "../a.gif", "skills/../a.gif", "skills/foo/..", "./a.gif",
                       "skills//a.gif", "skills/a.gif/", "skills\\a.gif", "C:/a.gif", "a\0b.gif", None, 123]
    test("1a. medya_haric_yol_gecerli: geçerli göreli yolları kabul eder",
         all(ortak.medya_haric_yol_gecerli(y) for y in gecerli_yollar))
    test("1b. medya_haric_yol_gecerli: yol geçişi ('..', '.'), mutlak yol, ters bölü ve boş yolları reddeder",
         all(not ortak.medya_haric_yol_gecerli(y) for y in gecersiz_yollar))

    kayit_sozluk = {"repo": "o/r", "medya_haric": {"skills/foo/docs/a.gif": "belge-gorseli", "ortak/b.png": "kullanilmiyor"}}
    kayit_liste = {"repo": "o/r", "medya_haric": ["skills/foo/docs/a.gif", "ortak/b.png"]}
    test("1c. medya_haric_kumesi: hem sözlük hem düz liste biçimini aynı kümeye çevirir",
         ortak.medya_haric_kumesi(kayit_sozluk) == {"skills/foo/docs/a.gif", "ortak/b.png"}
         and ortak.medya_haric_kumesi(kayit_liste) == {"skills/foo/docs/a.gif", "ortak/b.png"})
    test("1d. medya_haric_skill_kumesi: alt klasördeki skill için hem repo-göreli hem skill-göreli yolu eşler",
         "docs/a.gif" in ortak.medya_haric_skill_kumesi(kayit_sozluk, "skills/foo")
         and "ortak/b.png" in ortak.medya_haric_skill_kumesi(kayit_sozluk, "skills/foo"))
    test("1e. medya_haric_skill_kumesi: kökteki skill ('') için tüm geçerli yolları döndürür",
         ortak.medya_haric_skill_kumesi({"medya_haric": ["docs/cover.webp"]}, "") == {"docs/cover.webp"})

    # ================================================================== 2. kaynak-cek.py: dosyalari_listele ve agac_klasor_hash
    AYAR = {"skill_ici_haric": [r"(^|/)node_modules/"], "max_dosya_mb": 5, "konum_haric": [], "ayna_klasorler": []}
    agac_ornek = [
        {"path": "skills/foo/SKILL.md", "type": "blob", "sha": "s1", "size": 100},
        {"path": "skills/foo/scripts/run.py", "type": "blob", "sha": "s2", "size": 200},
        {"path": "skills/foo/docs/a.gif", "type": "blob", "sha": "s3", "size": 500000},
        {"path": "skills/foo/docs/keep.png", "type": "blob", "sha": "s4", "size": 1200},
    ]
    dosyalar, atlanan = kc.dosyalari_listele(kayit_sozluk, agac_ornek, "skills/foo", AYAR)
    rel_list = [rel for _, rel in dosyalar]
    test("2a. dosyalari_listele: medya_haric dosyası listeye girmez, diğer dosyalar aynen gelir",
         sorted(rel_list) == ["SKILL.md", "docs/keep.png", "scripts/run.py"], rel_list)
    test("2b. dosyalari_listele: medya_haric dosyası atlanan_dosyalar'a girmez (KAYNAK.md'de gereksiz fark yaratmaz)",
         "docs/a.gif" not in atlanan and atlanan == [], atlanan)

    # agac_klasor_hash: medya_haric dosyası değişse veya silinse bile ağaç klasör hash'i değişmez
    agac_degismis = [
        {"path": "skills/foo/SKILL.md", "type": "blob", "sha": "s1", "size": 100},
        {"path": "skills/foo/scripts/run.py", "type": "blob", "sha": "s2", "size": 200},
        {"path": "skills/foo/docs/a.gif", "type": "blob", "sha": "YENI_SHA_999", "size": 999999},
        {"path": "skills/foo/docs/keep.png", "type": "blob", "sha": "s4", "size": 1200},
    ]
    agac_silinmis = [e for e in agac_ornek if e["path"] != "skills/foo/docs/a.gif"]
    test("2c. agac_klasor_hash: dışlanan medya dosyası değişse ya da silinse bile hash aynı kalır",
         kc.agac_klasor_hash(agac_ornek, "skills/foo", AYAR, kayit_sozluk)
         == kc.agac_klasor_hash(agac_degismis, "skills/foo", AYAR, kayit_sozluk)
         == kc.agac_klasor_hash(agac_silinmis, "skills/foo", AYAR, kayit_sozluk))

    # ================================================================== 3. arsiv-yerlestir.py ve güncelleme döngüsü (sahte depo)
    LIB = TMP / "lib"
    GECICI = LIB / ".gecici"
    REG = LIB / "registry.json"
    ARSIV = LIB / "arsiv"
    KENDI = LIB / "kendi"
    REPO = "ornek/medya-depo"
    KAYIT = {
        "repo": REPO, "tip": "T1", "oncelik": 2,
        "medya_haric": {
            "skills/foo/docs/a.gif": "belge-gorseli",
            "skills/foo/assets/unused.bin": "kullanilmiyor",
        },
    }
    T7_KAYIT = {
        "repo": "yerel/kendi", "tip": "T7", "oncelik": 1, "yerel": "kendi", "lisans": "Kendi (özel)",
        "medya_haric": ["kendi-skil/docs/demo.gif"],
    }

    def kaynaklar_yaz(repolar):
        yaz(LIB / "kaynaklar.json", {
            "ayna_klasorler": [], "max_dosya_mb": 5, "konum_haric": [], "skill_ici_haric": [r"(^|/)node_modules/"],
            "arsivden_cikarilanlar": [], "repolar": repolar,
        })

    kaynaklar_yaz([KAYIT, T7_KAYIT])
    yaz(LIB / "kategoriler.json", {"alanlar": {"g-video-ses-medya": {"kategoriler": {"04-motion-graphics-karakter": "x"}}}})
    yaz(LIB / "kategori-kurallari.json", {"ad_kurallari": [], "yol_kurallari": [], "repo_varsayilan": {
        REPO: "g-video-ses-medya/04-motion-graphics-karakter",
        "yerel/kendi": "g-video-ses-medya/04-motion-graphics-karakter",
    }})
    yaz(LIB / "ucret-siniflandirma.json", {"siniflar": {}})
    yaz(LIB / "gelistiriciler.json", {"repolar": {}})
    (LIB / "notlar").mkdir()

    # Yerel kaynak (T7) klasörü: içinde dışlanan demo.gif ve korunacak keep.py var
    yaz(KENDI / "kendi-skil" / "SKILL.md", fm("kendi-skil") + "Govde\n")
    yaz(KENDI / "kendi-skil" / "scripts" / "keep.py", "print('kalsin')\n")
    yaz(KENDI / "kendi-skil" / "docs" / "demo.gif", b"GIF89a-demo-icerik")

    # .gecici/cekilen içinde sahte indirilen skill (sanki dışlanan dosyalar .gecici'de varmış gibi de test edilir)
    cekilen_foo = GECICI / "cekilen" / "ornek__medya-depo" / "foo"
    yaz(cekilen_foo / "SKILL.md", fm("foo") + "Foo govde\n")
    yaz(cekilen_foo / "scripts" / "calis.py", "print('ok')\n")
    yaz(cekilen_foo / "docs" / "kalsin.png", b"\x89PNG-kalsin")
    yaz(cekilen_foo / "docs" / "a.gif", b"GIF89a-buyuk-belge-gorseli")
    yaz(cekilen_foo / "assets" / "unused.bin", b"\x00\x01\x02-kullanilmiyor")

    for m, kw in (
        (kc, dict(GECICI=GECICI, KAYNAKLAR=LIB / "kaynaklar.json", KOK=LIB, repo_agaci=ag_yasak, repo_lisansi=ag_yasak,
                  klon_dosyalari_al=ag_yasak, indir=ag_yasak)),
        (ay, dict(KOK=LIB, ARSIV=ARSIV, GECICI=GECICI, REGISTRY=REG, KATEGORILER=LIB / "kategoriler.json",
                  KURALLAR=LIB / "kategori-kurallari.json", GELISTIRICILER=LIB / "gelistiriciler.json", TREND=LIB / "trend.json")),
        (ag, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG)),
        (kd, dict(KOK=LIB, KAYNAKLAR=LIB / "kaynaklar.json", REGISTRY=REG, repo_agaci=ag_yasak)),
    ):
        for k, v in kw.items():
            setattr(m, k, v)

    # T7 kaynağını kaynak-cek ile çek, sonra T1 kaydını manifeste ekle
    kod_kc, cikti_kc = yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])
    test("3a. kaynak-cek (yerel): medya_haric dosyasını .gecici'ye kopyalamaz, diğer dosyaları kopyalar",
         not kod_kc
         and not (GECICI / "cekilen" / "yerel__kendi" / "kendi-skil" / "docs" / "demo.gif").exists()
         and (GECICI / "cekilen" / "yerel__kendi" / "kendi-skil" / "scripts" / "keep.py").exists(), cikti_kc)

    def manifest_yaz(commit_sha="a" * 40):
        m = json.loads((GECICI / "cekilen" / "manifest.json").read_text(encoding="utf-8"))
        m["kayitlar"] = [x for x in m["kayitlar"] if x["repo"] != REPO]
        m["kayitlar"].append({
            "repo": REPO, "tip": "T1", "oncelik": 2, "kimlik": "ornek__medya-depo", "commit": commit_sha, "lisans": "MIT",
            "klasor_adi": "foo", "kaynak_yol": "skills/foo", "asil_ad": None, "ust_skill": None, "aynalar": [],
            "atlanan_dosyalar": ["docs/a.gif"],  # eski manifestte kalmış olsa bile arsiv-yerlestir temizlemeli
            "varyantlar": {}, "varyant_yollari": {}, "ad": "foo", "aciklama": "foo",
            "bagimlilik": None, "beklenen_dosya": 3, "inen_dosya": 3, "varyant_eksik": [],
            "yerel": "cekilen/ornek__medya-depo/foo",
        })
        m["denetim"][REPO] = {"commit": commit_sha, "skill_md": {"skills/foo/SKILL.md": "secildi"}}
        yaz(GECICI / "cekilen" / "manifest.json", m)

    manifest_yaz("a" * 40)
    kod_ay, cikti_ay = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    reg1 = json.loads(REG.read_text(encoding="utf-8"))
    s_foo = next((s for s in reg1["skiller"] if s["id"] == "foo"), None)
    s_kendi = next((s for s in reg1["skiller"] if s["id"] == "kendi-skil"), None)
    foo_arsiv = LIB / s_foo["yol"]
    test("3b. arsiv-yerlestir: dışlanan dosyalar (.gecici'de olsa bile) arşive GELMEZ",
         not kod_ay and s_foo is not None
         and not (foo_arsiv / "docs" / "a.gif").exists()
         and not (foo_arsiv / "assets" / "unused.bin").exists()
         and not (LIB / s_kendi["yol"] / "docs" / "demo.gif").exists(), cikti_ay)
    test("3c. arsiv-yerlestir: diğer dosyalar (SKILL.md, scripts/calis.py, docs/kalsin.png) aynen arşive gelir",
         (foo_arsiv / "SKILL.md").is_file()
         and (foo_arsiv / "scripts" / "calis.py").read_text(encoding="utf-8") == "print('ok')\n"
         and (foo_arsiv / "docs" / "kalsin.png").read_bytes() == b"\x89PNG-kalsin")
    kmd1 = (foo_arsiv / "KAYNAK.md").read_text(encoding="utf-8")
    test("3d. arsiv-yerlestir: dışlanan dosya atlanan_dosyalar ve KAYNAK.md içinde görünmez",
         s_foo["atlanan_dosyalar"] == [] and "a.gif" not in kmd1 and "Arşive alınmayan dosyalar" not in kmd1,
         (s_foo["atlanan_dosyalar"], kmd1))

    # İncelenmiş skill olarak işaretle; şimdi güncelleme (yeni commit) simülasyonu yap:
    # Kaynakta yalnız dışlanan medya dosyası değişmiş olsun -> klasor_hash değişmemeli, inceleme 'incelendi' kalmalı,
    # silinen medya dosyaları güncellemede arşive GERİ GELMEMELİ!
    hash1 = s_foo["klasor_hash"]
    for s in reg1["skiller"]:
        if s["id"] == "foo":
            s["inceleme"] = "incelendi"
            s["inceleme_tarihi"] = "2026-11-19"
            s["inceleme_commit"] = "a" * 40
    yaz(REG, reg1)

    # Güncellemede .gecici içindeki dışlanan dosya değişiyor ve yeniden mevcut
    yaz(cekilen_foo / "docs" / "a.gif", b"GIF89a-YENI-SURUM-GUNCELLEME")
    yaz(cekilen_foo / "assets" / "unused.bin", b"\xff\xfe-YENI")
    # Yerel kaynakta da dışlanan demo.gif değişsin -> yerel_commit değişmemeli
    onceki_kendi_commit = s_kendi["commit"]
    yaz(KENDI / "kendi-skil" / "docs" / "demo.gif", b"GIF89a-degisti-ama-dislaniyor")
    yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])
    manifest_yaz("b" * 40)
    kod_ay2, cikti_ay2 = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    reg2 = json.loads(REG.read_text(encoding="utf-8"))
    s_foo2 = next(s for s in reg2["skiller"] if s["id"] == "foo")
    s_kendi2 = next(s for s in reg2["skiller"] if s["id"] == "kendi-skil")

    test("3e. güncelleme: dışlanan dosyalar güncellemede arşive GERİ GELMEZ",
         not kod_ay2
         and not (foo_arsiv / "docs" / "a.gif").exists()
         and not (foo_arsiv / "assets" / "unused.bin").exists()
         and not (LIB / s_kendi2["yol"] / "docs" / "demo.gif").exists(), cikti_ay2)
    test("3f. güncelleme: yalnız dışlanan dosya değiştiğinde klasor_hash değişmez ve inceleme 'yeniden-incelenecek' OLMAZ",
         s_foo2["klasor_hash"] == hash1 and s_foo2["inceleme"] == "incelendi",
         (s_foo2["klasor_hash"], hash1, s_foo2["inceleme"]))
    test("3g. yerel kaynak: dışlanan medya dosyası değiştiğinde yerel commit ve kapsam denetimi etkilenmez",
         s_kendi2["commit"] == onceki_kendi_commit)

    kaynaklar_yaz([T7_KAYIT])
    kod_kd, cikti_kd = yakala(kd.main)
    test("3h. kapsam-denetimi: yerel kaynakta medya_haric varken 0 sorun",
         not kod_kd and "sorun: 0" in cikti_kd, cikti_kd)
    kaynaklar_yaz([KAYIT, T7_KAYIT])

    # ================================================================== 4. dogrula.py şema ve arşivde kalan dosya uyarısı
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4a. dogrula: geçerli medya_haric (sözlük ve düz liste) ve temiz arşivde 0 hata 0 uyarı",
         h == [] and not [x for x in u if "medya_haric" in x or "bilinmeyen anahtar" in x], (h, u))

    # Arşivde dışlanan dosya hâlâ duruyorsa UYARI vermeli
    yaz(foo_arsiv / "docs" / "a.gif", b"GIF89a-kalinti")
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4b. dogrula: medya_haric listesinde olup arşivde hâlâ duran dosya UYARI verir (HATA değil)",
         h == [] and any("medya_haric dosyası arşivde hâlâ duruyor" in x and "docs/a.gif" in x for x in u), (h, u))
    (foo_arsiv / "docs" / "a.gif").unlink()

    # Hiçbir skil klasöründe görünmeyen yol UYARI vermeli
    kaynaklar_yaz([{**KAYIT, "medya_haric": {"skills/olmayan-skil/docs/a.gif": "belge-gorseli"}}, T7_KAYIT])
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4c. dogrula: çok skilli/alt klasörlü kaynakta hiçbir skil klasörüne uymayan medya_haric yolu UYARI verir",
         h == [] and any("hiçbir skil klasöründe görünmüyor" in x for x in u), (h, u))

    # Geçersiz yol geçişi (..) ve mutlak yol HATA vermeli
    for kotu_yol in ("../kacis.gif", "skills/foo/../../kacis.gif", "/mutlak/yol.gif", "skills\\ters.gif", ""):
        hatalar = dg.kaynak_tur_hatalari({"repo": REPO, "tip": "T1", "medya_haric": [kotu_yol]})
        test(f"4d. dogrula: geçersiz yol ({kotu_yol!r}) reddedilir (HATA)",
             any("medya_haric geçersiz yol" in x for x in hatalar), hatalar)

    # Bozuk tip (sayı, metin, iç içe bozuk sözlük) HATA vermeli
    for kotu_deger in ("skills/foo/a.gif", 123, [123], {"skills/foo/a.gif": 123}):
        hatalar = dg.kaynak_tur_hatalari({"repo": REPO, "tip": "T1", "medya_haric": kotu_deger})
        test(f"4e. dogrula: bozuk medya_haric şeması ({type(kotu_deger).__name__}) HATA verir",
             any("medya_haric" in x for x in hatalar), hatalar)
finally:
    urllib.request.urlopen = _urlopen
    shutil.rmtree(TMP, ignore_errors=True)

gecen = sum(1 for _, ok in SONUC if ok)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
