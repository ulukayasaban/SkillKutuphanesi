#!/usr/bin/env python3
"""P19 testleri: arşive geri gelmeyecek medya dışlama listesi (kaynaklar.json -> medya_haric).
Daraltılmış tasarım: YALNIZ tam, repo-göreli, tek DOSYA yolları (NFC normalizasyonlu, harf duyarlı;
skill-göreli biçim, klasör/ön ek eşleşmesi, joker YOK).
Kapsam (bağımsız inceleme bulguları 1..7):
- Bulgu 1: Çok skilli repoda başka skile sızmama (skill-göreli yol yok, else dalı yok)
- Bulgu 2: Klasör yolu atlanmaz; dogrula.py kaynak/arşiv/skil klasörü girdisini HATA sayar
- Bulgu 3: Yerel kaynaklar (T7/T8) dahil tüm araçlar tek ortak medya_haric_mi işlevini kullanır
- Bulgu 4: SKILL.md ve KAYNAK.md girdisi dogrula.py'de HATA ve hiçbir araçta (onemli_dosyalar dahil) dışlanmaz
- Bulgu 5: Unicode NFC/NFD normalizasyonu + harf duyarlı eşleşme + harf büyüklüğü farkında dogrula.py UYARI
- Bulgu 6: _varyantlar altındaki dışlanan medya denetimi + SKILL.md bağlantısı kirik_baglantilar puanını düşürmez, KAYNAK.md'de 'dışlandı' yazar
- Bulgu 7: arsiv-guncelle.py gerçek kontrol() akışı + gerçek dosya değişikliğinde klasor_hash değişimi negatif testi
Yalnız geçici klasör ve sahte veri; gerçek kütüphane dosyalarına ve ev klasörüne dokunmaz, ağ kullanmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unicodedata
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


def fm(ad, aciklama="Ornek medya testi skili belirli isler icin kullan digerlerinde kullanma."):
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
    # ================================================================== 1. Yol doğrulama ve tek ortak yardımcı
    gecerli_yollar = ["docs/a.gif", "skills/foo/docs/a.gif", "assets/admin_2026-01.json.gz", ".claude/skills/x/a.png"]
    gecersiz_yollar = ["", " ", "/etc/passwd", "~/a.gif", "../a.gif", "skills/../a.gif", "skills/foo/..", "./a.gif",
                       "skills//a.gif", "skills/a.gif/", "skills\\a.gif", "C:/a.gif", "a\0b.gif",
                       "skills/foo/*.gif", "skills/foo/docs/?.png", None, 123]
    test("1a. medya_haric_yol_gecerli: geçerli tam repo-göreli yolları kabul eder",
         all(ortak.medya_haric_yol_gecerli(y) for y in gecerli_yollar))
    test("1b. medya_haric_yol_gecerli: yol geçişi, mutlak yol, ters bölü, joker (*, ?) ve boş yolları reddeder",
         all(not ortak.medya_haric_yol_gecerli(y) for y in gecersiz_yollar))

    kayit_sozluk = {
        "repo": "o/r",
        "medya_haric": {
            "skills/foo/docs/a.gif": "belge-gorseli",
            "docs/logo.png": "kok-gorseli",
            "skills/foo/SKILL.md": "yasak-skill",
            "skills/foo/KAYNAK.md": "yasak-kaynak",
        },
    }
    kayit_liste = {"repo": "o/r", "medya_haric": ["skills/foo/docs/a.gif", "docs/logo.png", "skills/foo/skill.md"]}
    test("1c. medya_haric_kumesi: sözlük ve düz listeyi aynı NFC kümeye çevirir; SKILL.md ve KAYNAK.md kümeye girmez",
         ortak.medya_haric_kumesi(kayit_sozluk) == {"skills/foo/docs/a.gif", "docs/logo.png"}
         and ortak.medya_haric_kumesi(kayit_liste) == {"skills/foo/docs/a.gif", "docs/logo.png"})

    kume = ortak.medya_haric_kumesi(kayit_sozluk)
    test("1d. medya_haric_mi / skill_kumesi (bulgu 1): başka skile ve skill-göreli yola SIZMAZ",
         ortak.medya_haric_mi("docs/a.gif", kume, "skills/foo")
         and not ortak.medya_haric_mi("docs/a.gif", kume, "skills/bar")
         and not ortak.medya_haric_mi("docs/logo.png", kume, "skills/foo")
         and not ortak.medya_haric_mi("docs/logo.png", kume, "skills/bar")
         and ortak.medya_haric_skill_kumesi(kayit_sozluk, "skills/foo") == {"docs/a.gif"}
         and ortak.medya_haric_skill_kumesi(kayit_sozluk, "skills/bar") == set())
    test("1e. medya_haric_mi: kökteki skill ('') için repo-göreli yolu doğrudan eşler",
         ortak.medya_haric_mi("docs/logo.png", kume, "")
         and not ortak.medya_haric_mi("docs/a.gif", kume, ""))

    # Bulgu 5: NFC/NFD normalizasyonu + harf duyarlı eşleşme
    nfc_yol = unicodedata.normalize("NFC", "skills/foo/docs/örnek.png")
    nfd_yol = unicodedata.normalize("NFD", "skills/foo/docs/örnek.png")
    kume_uni = ortak.medya_haric_kumesi({"medya_haric": [nfc_yol, "skills/foo/docs/a.gif"]})
    test("1f. medya_haric_mi (bulgu 5): NFC/NFD eşleşir, harf büyüklüğü farkında (A.GIF vs a.gif) eşleşmez",
         ortak.medya_haric_mi(nfd_yol, kume_uni)
         and ortak.medya_haric_mi(unicodedata.normalize("NFD", "docs/örnek.png"), kume_uni, "skills/foo")
         and not ortak.medya_haric_mi("docs/A.GIF", kume_uni, "skills/foo"))

    # Bulgu 4: onemli_dosyalar / klasor_hash SKILL.md'yi asla dışlamaz
    tmp_sk = TMP / "koruma_sk"
    yaz(tmp_sk / "SKILL.md", fm("koruma") + "icerik 1\n")
    yaz(tmp_sk / "docs" / "a.gif", b"gif")
    h_normal = ortak.klasor_hash(tmp_sk, {"skills/koruma/docs/a.gif"}, kaynak_yol="skills/koruma")
    h_skill_haric = ortak.klasor_hash(tmp_sk, {"skills/koruma/docs/a.gif", "skills/koruma/SKILL.md"}, kaynak_yol="skills/koruma")
    yaz(tmp_sk / "SKILL.md", fm("koruma") + "icerik 2 DEGISEN\n")
    h_skill_degisti = ortak.klasor_hash(tmp_sk, {"skills/koruma/docs/a.gif", "skills/koruma/SKILL.md"}, kaynak_yol="skills/koruma")
    test("1g. onemli_dosyalar/klasor_hash (bulgu 4): SKILL.md haric_yollar'da olsa bile asla dışlanmaz",
         h_normal == h_skill_haric and h_skill_degisti != h_skill_haric)

    # ================================================================== 2. kaynak-cek.py: dosyalari_listele ve agac_klasor_hash
    AYAR = {"skill_ici_haric": [r"(^|/)node_modules/"], "max_dosya_mb": 5, "konum_haric": [], "ayna_klasorler": []}
    agac_cok = [
        {"path": "skills/foo/SKILL.md", "type": "blob", "sha": "s1", "size": 100},
        {"path": "skills/foo/scripts/run.py", "type": "blob", "sha": "s2", "size": 200},
        {"path": "skills/foo/docs/a.gif", "type": "blob", "sha": "s3", "size": 500000},
        {"path": "skills/foo/docs/keep.png", "type": "blob", "sha": "s4", "size": 1200},
        {"path": "skills/foo/docs/logo.png", "type": "blob", "sha": "s5", "size": 900},
        {"path": nfd_yol, "type": "blob", "sha": "s6", "size": 800},
        {"path": "skills/bar/SKILL.md", "type": "blob", "sha": "b1", "size": 100},
        {"path": "skills/bar/docs/a.gif", "type": "blob", "sha": "b2", "size": 400},
        {"path": "skills/bar/docs/logo.png", "type": "blob", "sha": "b3", "size": 500},
    ]
    kayit_cok = {"repo": "o/r", "medya_haric": ["skills/foo/docs/a.gif", "docs/logo.png", nfc_yol]}
    dosyalar_foo, atlanan_foo = kc.dosyalari_listele(kayit_cok, agac_cok, "skills/foo", AYAR)
    dosyalar_bar, _ = kc.dosyalari_listele(kayit_cok, agac_cok, "skills/bar", AYAR)
    rel_foo = sorted(rel for _, rel in dosyalar_foo)
    rel_bar = sorted(rel for _, rel in dosyalar_bar)
    test("2a. dosyalari_listele (bulgu 1, 5): foo'da a.gif ve NFD örnek.png dışlanır; bar'daki a.gif ve logo.png SIZMADAN gelir",
         rel_foo == ["SKILL.md", "docs/keep.png", "docs/logo.png", "scripts/run.py"]
         and rel_bar == ["SKILL.md", "docs/a.gif", "docs/logo.png"], (rel_foo, rel_bar))
    test("2b. dosyalari_listele: medya_haric dosyası atlanan_dosyalar'a girmez",
         atlanan_foo == [], atlanan_foo)

    agac_medya_degisti = [dict(e, sha="YENI_SHA") if e["path"] == "skills/foo/docs/a.gif" else e for e in agac_cok]
    agac_gercek_degisti = [dict(e, sha="GERCEK_YENI") if e["path"] == "skills/foo/scripts/run.py" else e for e in agac_cok]
    h_ag1 = kc.agac_klasor_hash(agac_cok, "skills/foo", AYAR, kayit_cok)
    h_ag2 = kc.agac_klasor_hash(agac_medya_degisti, "skills/foo", AYAR, kayit_cok)
    h_ag3 = kc.agac_klasor_hash(agac_gercek_degisti, "skills/foo", AYAR, kayit_cok)
    test("2c. agac_klasor_hash (bulgu 7): dışlanan medya değişince hash aynı kalır, gerçek dosya değişince DEĞİŞİR",
         h_ag1 == h_ag2 and h_ag1 != h_ag3)

    # ================================================================== 3. Uçtan uca akış (çok skil, varyant, yerel T7/T8, arsiv-guncelle)
    LIB = TMP / "lib"
    GECICI = LIB / ".gecici"
    REG = LIB / "registry.json"
    ARSIV = LIB / "arsiv"
    KENDI = LIB / "kendi"
    SITE = LIB / "site"
    REPO = "ornek/medya-depo"
    KAYIT = {
        "repo": REPO, "tip": "T1", "oncelik": 2,
        "medya_haric": {
            "skills/foo/docs/a.gif": "belge-gorseli",
            "skills/foo/assets/unused.bin": "kullanilmiyor",
            "skills/foo/docs/örnek.png": "unicode-nfc",
            ".claude/skills/foo/docs/v.gif": "varyant-gorseli",
        },
    }
    T7_KAYIT = {
        "repo": "yerel/kendi", "tip": "T7", "oncelik": 1, "yerel": "kendi", "lisans": "Kendi (özel)",
        "medya_haric": ["kendi-skil/docs/demo.gif"],
    }
    T8_KAYIT = {
        "repo": "yerel/site", "tip": "T8", "oncelik": 1, "yerel": "site",
        "medya_haric": ["site-skil/docs/site-demo.gif"],
    }

    def kaynaklar_yaz(repolar):
        yaz(LIB / "kaynaklar.json", {
            "ayna_klasorler": [], "max_dosya_mb": 5, "konum_haric": [], "skill_ici_haric": [r"(^|/)node_modules/"],
            "arsivden_cikarilanlar": [], "repolar": repolar,
        })

    kaynaklar_yaz([KAYIT, T7_KAYIT, T8_KAYIT])
    yaz(LIB / "kategoriler.json", {"alanlar": {"g-video-ses-medya": {"kategoriler": {"04-motion-graphics-karakter": "x"}}}})
    yaz(LIB / "kategori-kurallari.json", {"ad_kurallari": [], "yol_kurallari": [], "repo_varsayilan": {
        REPO: "g-video-ses-medya/04-motion-graphics-karakter",
        "yerel/kendi": "g-video-ses-medya/04-motion-graphics-karakter",
        "yerel/site": "g-video-ses-medya/04-motion-graphics-karakter",
    }})
    yaz(LIB / "ucret-siniflandirma.json", {"siniflar": {}})
    yaz(LIB / "gelistiriciler.json", {"repolar": {}})
    yaz(LIB / "site-takip.json", {"skiller": [{"skill": "site-skil", "sahip": "ornek", "lisans": "MIT", "site": "https://ornek.test"}]})
    (LIB / "notlar").mkdir()

    # T7 yerel kaynak: kendi-skil (demo.gif dışlanır, keep.py kalır) + ikinci yerel skill (demo.gif kalır)
    yaz(KENDI / "kendi-skil" / "SKILL.md", fm("kendi-skil") + "Govde\n")
    yaz(KENDI / "kendi-skil" / "scripts" / "keep.py", "print('kalsin')\n")
    yaz(KENDI / "kendi-skil" / "docs" / "demo.gif", b"GIF89a-demo-icerik")
    yaz(KENDI / "kendi-diger" / "SKILL.md", fm("kendi-diger") + "Diger govde\n")
    yaz(KENDI / "kendi-diger" / "docs" / "demo.gif", b"GIF89a-kalsin-diger")

    # T8 yerel site kaynağı
    yaz(SITE / "site-skil" / "SKILL.md", fm("site-skil") + "Site govde\n")
    yaz(SITE / "site-skil" / "docs" / "site-demo.gif", b"GIF89a-site-disla")
    yaz(SITE / "site-skil" / "docs" / "keep.png", b"\x89PNG-site-kalsin")

    # .gecici/cekilen içinde çok skilli repo: foo (dışlanan medya + SKILL.md bağlantısı + varyant + NFD dosya) ve bar
    cekilen_foo = GECICI / "cekilen" / "ornek__medya-depo" / "foo"
    yaz(cekilen_foo / "SKILL.md", fm("foo") + "Foo govde\n![demo](docs/a.gif)\n[keep](docs/kalsin.png)\n")
    yaz(cekilen_foo / "scripts" / "calis.py", "print('ok')\n")
    yaz(cekilen_foo / "docs" / "kalsin.png", b"\x89PNG-kalsin")
    yaz(cekilen_foo / "docs" / "a.gif", b"GIF89a-buyuk-belge-gorseli")
    yaz(cekilen_foo / "docs" / unicodedata.normalize("NFD", "örnek.png"), b"\x89PNG-nfd")
    yaz(cekilen_foo / "assets" / "unused.bin", b"\x00\x01\x02-kullanilmiyor")

    cekilen_foo_v = GECICI / "cekilen" / "ornek__medya-depo" / "_varyant" / "foo" / "claude"
    yaz(cekilen_foo_v / "SKILL.md", fm("foo") + "Claude varyant govde\n")
    yaz(cekilen_foo_v / "docs" / "v.gif", b"GIF89a-varyant-disla")
    yaz(cekilen_foo_v / "docs" / "v-keep.png", b"\x89PNG-varyant-kalsin")

    cekilen_bar = GECICI / "cekilen" / "ornek__medya-depo" / "bar"
    yaz(cekilen_bar / "SKILL.md", fm("bar") + "Bar govde\n")
    yaz(cekilen_bar / "docs" / "a.gif", b"GIF89a-bar-gerekli")

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

    # T7 ve T8 kaynaklarını kaynak-cek ile çek
    kod_kc7, cikti_kc7 = yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])
    kod_kc8, cikti_kc8 = yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/site"])
    test("3a. kaynak-cek (T7/T8 yerel): tam repo-göreli dışlanan dosyayı almaz, diğer skilin aynı adlı dosyasını alır",
         not kod_kc7 and not kod_kc8
         and not (GECICI / "cekilen" / "yerel__kendi" / "kendi-skil" / "docs" / "demo.gif").exists()
         and (GECICI / "cekilen" / "yerel__kendi" / "kendi-diger" / "docs" / "demo.gif").exists()
         and not (GECICI / "cekilen" / "yerel__site" / "site-skil" / "docs" / "site-demo.gif").exists()
         and (GECICI / "cekilen" / "yerel__site" / "site-skil" / "docs" / "keep.png").exists(), (cikti_kc7, cikti_kc8))

    def manifest_yaz(commit_sha="a" * 40):
        m = json.loads((GECICI / "cekilen" / "manifest.json").read_text(encoding="utf-8"))
        m["kayitlar"] = [x for x in m["kayitlar"] if x["repo"] != REPO]
        m["kayitlar"].extend([
            {
                "repo": REPO, "tip": "T1", "oncelik": 2, "kimlik": "ornek__medya-depo", "commit": commit_sha, "lisans": "MIT",
                "klasor_adi": "foo", "kaynak_yol": "skills/foo", "asil_ad": None, "ust_skill": None, "aynalar": [],
                "atlanan_dosyalar": ["docs/a.gif"],
                "varyantlar": {"claude": "cekilen/ornek__medya-depo/_varyant/foo/claude"},
                "varyant_yollari": {"claude": ".claude/skills/foo"},
                "ad": "foo", "aciklama": "foo", "bagimlilik": None, "beklenen_dosya": 3, "inen_dosya": 3, "varyant_eksik": [],
                "yerel": "cekilen/ornek__medya-depo/foo",
            },
            {
                "repo": REPO, "tip": "T1", "oncelik": 2, "kimlik": "ornek__medya-depo", "commit": commit_sha, "lisans": "MIT",
                "klasor_adi": "bar", "kaynak_yol": "skills/bar", "asil_ad": None, "ust_skill": None, "aynalar": [],
                "atlanan_dosyalar": [], "varyantlar": {}, "varyant_yollari": {},
                "ad": "bar", "aciklama": "bar", "bagimlilik": None, "beklenen_dosya": 2, "inen_dosya": 2, "varyant_eksik": [],
                "yerel": "cekilen/ornek__medya-depo/bar",
            },
        ])
        m["denetim"][REPO] = {"commit": commit_sha, "skill_md": {"skills/foo/SKILL.md": "secildi", "skills/bar/SKILL.md": "secildi"}}
        yaz(GECICI / "cekilen" / "manifest.json", m)

    manifest_yaz("a" * 40)
    kod_ay, cikti_ay = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    reg1 = json.loads(REG.read_text(encoding="utf-8"))
    s_foo = next(s for s in reg1["skiller"] if s["id"] == "foo")
    s_bar = next(s for s in reg1["skiller"] if s["id"] == "bar")
    s_kendi = next(s for s in reg1["skiller"] if s["id"] == "kendi-skil")
    s_site = next(s for s in reg1["skiller"] if s["id"] == "site-skil")
    foo_arsiv = LIB / s_foo["yol"]
    foo_var = LIB / s_foo["varyantlar"]["claude"]
    bar_arsiv = LIB / s_bar["yol"]

    test("3b. arsiv-yerlestir (bulgu 5, 6): ana, varyant, NFD Unicode, T7 ve T8 dışlanan dosyaları arşive GELMEZ",
         not kod_ay
         and not (foo_arsiv / "docs" / "a.gif").exists()
         and not (foo_arsiv / "assets" / "unused.bin").exists()
         and not any("rnek.png" in p.name for p in (foo_arsiv / "docs").iterdir())
         and not (foo_var / "docs" / "v.gif").exists()
         and (foo_var / "docs" / "v-keep.png").exists()
         and not (LIB / s_kendi["yol"] / "docs" / "demo.gif").exists()
         and not (LIB / s_site["yol"] / "docs" / "site-demo.gif").exists(), cikti_ay)

    test("3c. arsiv-yerlestir (bulgu 1): çok skilli repoda bar/docs/a.gif sızmadan aynen arşive gelir",
         (bar_arsiv / "docs" / "a.gif").read_bytes() == b"GIF89a-bar-gerekli"
         and (foo_arsiv / "scripts" / "calis.py").read_text(encoding="utf-8") == "print('ok')\n"
         and (foo_arsiv / "docs" / "kalsin.png").read_bytes() == b"\x89PNG-kalsin")

    # Bulgu 2: _kopyala_medya_haric klasör yolunu asla atlamaz
    tmp_kl_hedef = TMP / "kl_hedef"
    ay._kopyala_medya_haric(cekilen_foo, tmp_kl_hedef, {"skills/foo/scripts", "skills/foo/docs/a.gif"}, kaynak_yol="skills/foo")
    test("3d. _kopyala_medya_haric (bulgu 2): klasör yolu yazılsa bile klasör ve içindeki dosyalar ATLANMAZ",
         (tmp_kl_hedef / "scripts" / "calis.py").is_file() and not (tmp_kl_hedef / "docs" / "a.gif").exists())

    # Bulgu 6: SKILL.md'den dışlanan medyaya giden bağlantı kirik_baglantilar puanını düşürmez ve KAYNAK.md'de 'dışlandı' yazar
    kmd1 = (foo_arsiv / "KAYNAK.md").read_text(encoding="utf-8")
    yapi_notu = next((x for x in s_foo["degerlendirme"]["ayrinti"] if x.startswith("yapı ")), "")
    test("3e. kirik_baglantilar ve KAYNAK.md (bulgu 6): dışlanan medya kırık sayılmaz (yapı 5/5), KAYNAK.md'de 'dışlandı' yazar",
         s_foo["kirik_baglantilar"] == []
         and yapi_notu == "yapı 5/5"
         and "dışlandı" in kmd1 and "docs/a.gif" in kmd1
         and "unused.bin" not in kmd1 and s_foo["atlanan_dosyalar"] == [],
         (s_foo["kirik_baglantilar"], yapi_notu, kmd1))

    # Güncelleme simülasyonu: yalnız dışlanan medya değişince hash değişmez ve inceleme 'incelendi' kalır
    hash1 = s_foo["klasor_hash"]
    for s in reg1["skiller"]:
        if s["id"] == "foo":
            s["inceleme"] = "incelendi"
            s["inceleme_tarihi"] = "2026-11-19"
            s["inceleme_commit"] = "a" * 40
    yaz(REG, reg1)

    yaz(cekilen_foo / "docs" / "a.gif", b"GIF89a-YENI-SURUM-GUNCELLEME")
    yaz(cekilen_foo_v / "docs" / "v.gif", b"GIF89a-YENI-VARYANT")
    onceki_kendi_commit = s_kendi["commit"]
    yaz(KENDI / "kendi-skil" / "docs" / "demo.gif", b"GIF89a-degisti-ama-dislaniyor")
    yakala(kc.main, argv=["kaynak-cek.py", "--repo", "yerel/kendi"])
    manifest_yaz("b" * 40)
    kod_ay2, cikti_ay2 = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    reg2 = json.loads(REG.read_text(encoding="utf-8"))
    s_foo2 = next(s for s in reg2["skiller"] if s["id"] == "foo")
    s_kendi2 = next(s for s in reg2["skiller"] if s["id"] == "kendi-skil")

    test("3f. güncelleme: dışlanan dosyalar geri gelmez, klasor_hash değişmez ve inceleme 'incelendi' kalır",
         not kod_ay2
         and not (foo_arsiv / "docs" / "a.gif").exists()
         and not (foo_var / "docs" / "v.gif").exists()
         and s_foo2["klasor_hash"] == hash1 and s_foo2["inceleme"] == "incelendi"
         and s_kendi2["commit"] == onceki_kendi_commit,
         (s_foo2["klasor_hash"], hash1, s_foo2["inceleme"]))

    # Bulgu 7: gerçek dosya değişince klasor_hash DEĞİŞİR ve incelenmiş skill 'yeniden-incelenecek' olur (negatif test)
    yaz(cekilen_foo / "scripts" / "calis.py", "print('gercek-degisiklik')\n")
    manifest_yaz("c" * 40)
    kod_ay3, cikti_ay3 = yakala(ay.main, argv=["arsiv-yerlestir.py"])
    reg3 = json.loads(REG.read_text(encoding="utf-8"))
    s_foo3 = next(s for s in reg3["skiller"] if s["id"] == "foo")
    test("3g. negatif test (bulgu 7): gerçek dosya değişince klasor_hash DEĞİŞİR ve inceleme 'yeniden-incelenecek' olur",
         not kod_ay3 and s_foo3["klasor_hash"] != hash1 and s_foo3["inceleme"] == "yeniden-incelenecek",
         (s_foo3["klasor_hash"], hash1, s_foo3["inceleme"]))

    # kapsam-denetimi yerel kaynaklarda 0 sorun
    kaynaklar_yaz([T7_KAYIT, T8_KAYIT])
    kod_kd, cikti_kd = yakala(kd.main)
    test("3h. kapsam-denetimi: yerel kaynaklarda (T7/T8) medya_haric varken 0 sorun",
         not kod_kd and "sorun: 0" in cikti_kd, cikti_kd)

    # Bulgu 7: arsiv-guncelle.py gerçek rapor() akışı (ağ yok: yalnız yerel kaynaklar, gh_hazir ve subprocess yamalı)
    ag.gh_hazir = lambda: (True, 5000, "")
    ag.etkilenen_projeler = lambda repolar: {}
    eski_run = ag.subprocess.run
    ag.subprocess.run = lambda *a, **k: subprocess.CompletedProcess(a, 0)
    try:
        # Dışlanan demo.gif yeniden değişsin -> rapor() değişiklik bildirmemeli
        yaz(KENDI / "kendi-skil" / "docs" / "demo.gif", b"GIF89a-kontrol-disliyor")
        (deg1, sor1, _), out1 = yakala(ag.rapor)
        # Şimdi gerçek dosya keep.py değişsin -> rapor() yerel/kendi değişti demeli
        yaz(KENDI / "kendi-skil" / "scripts" / "keep.py", "print('gercek-degisim-kontrol')\n")
        (deg2, sor2, _), out2 = yakala(ag.rapor)
        test("3i. arsiv-guncelle.rapor() (bulgu 3, 7): dışlanan medya değişince sessiz, gerçek dosya değişince 'yerel/kendi' bildirir",
             deg1 == [] and sor1 == [] and deg2 == ["yerel/kendi"] and sor2 == [],
             (deg1, deg2, out1, out2))
    finally:
        ag.subprocess.run = eski_run
    kaynaklar_yaz([KAYIT, T7_KAYIT, T8_KAYIT])

    # ================================================================== 4. dogrula.py denetimleri (bulgu 2, 4, 5, 6)
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4a. dogrula: geçerli medya_haric ve temiz arşivde 0 hata, 0 medya_haric uyarısı",
         h == [] and not [x for x in u if "medya_haric" in x or "bilinmeyen anahtar" in x], (h, u))

    # Ana arşivde kalan dışlanan dosya -> UYARI
    yaz(foo_arsiv / "docs" / "a.gif", b"GIF89a-kalinti")
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4b. dogrula: ana arşivde kalan dışlanan dosya UYARI verir (HATA değil)",
         h == [] and any("medya_haric dosyası arşivde hâlâ duruyor" in x and "docs/a.gif" in x for x in u), (h, u))
    (foo_arsiv / "docs" / "a.gif").unlink()

    # Bulgu 6: _varyantlar altında kalan dışlanan dosya -> UYARI
    yaz(foo_var / "docs" / "v.gif", b"GIF89a-varyant-kalinti")
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4c. dogrula (bulgu 6): _varyantlar altında kalan dışlanan dosya UYARI verir",
         h == [] and any("_varyantlar/foo/claude/docs/v.gif" in x and "arşivde hâlâ duruyor" in x for x in u), (h, u))
    (foo_var / "docs" / "v.gif").unlink()

    # Bulgu 2: Klasör yolu (arşiv alt klasörü, skil klasörü, yerel kaynak klasörü) -> HATA
    kaynaklar_yaz([
        {**KAYIT, "medya_haric": ["skills/foo/docs", "skills/foo"]},
        {**T7_KAYIT, "medya_haric": ["kendi-skil/docs"]},
        T8_KAYIT,
    ])
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4d. dogrula (bulgu 2): arşiv/skil/yerel klasör yolu girdisi HATA verir",
         any("arşivde klasör gösteriyor" in x and "docs" in x for x in h)
         and any("skil klasörünü gösteriyor" in x and "skills/foo" in x for x in h)
         and any("klasör gösteriyor" in x and "kendi-skil/docs" in x for x in h), (h, u))

    # Bulgu 4: SKILL.md ve KAYNAK.md girdisi -> HATA
    for yasak in ("skills/foo/SKILL.md", "skills/foo/skill.md", "skills/foo/KAYNAK.md", "KAYNAK.md"):
        hatalar = dg.kaynak_tur_hatalari({"repo": REPO, "tip": "T1", "medya_haric": [yasak]})
        test(f"4e. dogrula (bulgu 4): {yasak!r} girdisi HATA verir",
             any("SKILL.md veya KAYNAK.md dışlanamaz" in x for x in hatalar), hatalar)

    # Bulgu 5: Harf büyüklüğü farkıyla eşleşen girdi -> UYARI (arşivde ve yerel kaynakta)
    kaynaklar_yaz([
        {**KAYIT, "medya_haric": ["skills/foo/docs/KALSIN.PNG"]},
        {**T7_KAYIT, "medya_haric": ["kendi-skil/docs/DEMO.GIF"]},
        T8_KAYIT,
    ])
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4f. dogrula (bulgu 5): harf büyüklüğü farkıyla eşleşen girdi arşivde ve yerel kaynakta UYARI verir",
         h == []
         and any("harf büyüklüğü farkıyla" in x and "KALSIN.PNG" in x for x in u)
         and any("harf büyüklüğü farkıyla" in x and "DEMO.GIF" in x for x in u), (h, u))

    # Hiçbir skil klasöründe görünmeyen yol (ve çıplak skill-göreli yol) -> UYARI
    kaynaklar_yaz([{**KAYIT, "medya_haric": ["skills/olmayan-skil/docs/a.gif", "docs/ciplak.gif"]}, T7_KAYIT, T8_KAYIT])
    h, u = [], []
    dg._e6_kaynaklar(LIB, h, u)
    test("4g. dogrula: hiçbir skil klasörüne uymayan yol (çıplak yol dahil) UYARI verir",
         h == []
         and any("hiçbir skil klasöründe görünmüyor" in x and "olmayan-skil" in x for x in u)
         and any("hiçbir skil klasöründe görünmüyor" in x and "docs/ciplak.gif" in x for x in u), (h, u))

    # Geçersiz yol geçişi, mutlak yol, ters bölü, joker -> HATA
    for kotu_yol in ("../kacis.gif", "skills/foo/../../kacis.gif", "/mutlak/yol.gif", "skills\\ters.gif", "skills/foo/*.gif", ""):
        hatalar = dg.kaynak_tur_hatalari({"repo": REPO, "tip": "T1", "medya_haric": [kotu_yol]})
        test(f"4h. dogrula: geçersiz yol ({kotu_yol!r}) reddedilir (HATA)",
             any("medya_haric geçersiz yol" in x for x in hatalar), hatalar)

    # Bozuk tip -> HATA
    for kotu_deger in ("skills/foo/a.gif", 123, [123], {"skills/foo/a.gif": 123}):
        hatalar = dg.kaynak_tur_hatalari({"repo": REPO, "tip": "T1", "medya_haric": kotu_deger})
        test(f"4i. dogrula: bozuk medya_haric şeması ({type(kotu_deger).__name__}) HATA verir",
             any("medya_haric" in x for x in hatalar), hatalar)
finally:
    urllib.request.urlopen = _urlopen
    shutil.rmtree(TMP, ignore_errors=True)

gecen = sum(1 for _, ok in SONUC if ok)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
