#!/usr/bin/env python3
"""P17 testleri: arsivde_tut (dogrula, ortak.arsive_cekilir, kaynak-cek, kapsam-denetimi),
fihrist-uret bilesenler ve arsivde_tut desteği, yeni fihriste-tasi.py (--kuru / --evet) ve
kaynak-cikar skil/bileşen çıkarma yardımcıları.
Yalnız geçici klasör ve sahte veri; gerçek kütüphane dosyalarına dokunmaz, ağ kullanmaz.
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


def sessiz(f, *a, **k):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            r = f(*a, **k)
        except SystemExit as e:
            r = e.code if e.code is not None else 0
    return r, out.getvalue(), err.getvalue()


def yaz(yol, veri):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(veri if isinstance(veri, str) else json.dumps(veri, ensure_ascii=False, indent=2), encoding="utf-8")


def agac_ozeti(kok):
    return sorted(
        (str(p.relative_to(kok)), p.stat().st_size, p.read_bytes())
        for p in Path(kok).rglob("*")
        if p.is_file() and ".git" not in p.relative_to(kok).parts
    )


def git_temiz_hazirla(kok):
    """Geçici kütüphane klasörünü temiz bir git çalışma ağacına dönüştürür."""
    for cmd in (
        ["git", "init", "-q"],
        ["git", "config", "user.email", "test@example.com"],
        ["git", "config", "user.name", "Test"],
        ["git", "add", "-A"],
        ["git", "commit", "-q", "-m", "baslangic"],
    ):
        r = subprocess.run(cmd, cwd=str(kok), capture_output=True, text=True)
        assert r.returncode == 0, f"{cmd}: {r.stderr}"


import ortak  # noqa: E402

dg = yukle("dogrula_p17", "dogrula.py")
kc = yukle("kaynak_cek_p17", "kaynak-cek.py")
kd = yukle("kapsam_p17", "kapsam-denetimi.py")
fu = yukle("fihrist_uret_p17", "fihrist-uret.py")
kcik = yukle("kaynak_cikar_p17", "kaynak-cikar.py")
ft = yukle("fihriste_tasi_p17", "fihriste-tasi.py")

C40 = "a" * 40
AYAR_BASIT = {"konum_haric": ["(^|/)tests?/"], "ayna_klasorler": [], "skill_ici_haric": [], "arsivden_cikarilanlar": []}

# ---------------------------------------------------------------- 1. arsivde_tut & dogrula.py
test("1a. dogrula: bolum fihrist + arsivde_tut metin listesi (kök '' dahil) geçerli",
     dg.kaynak_tur_hatalari({"repo": "o/r", "tip": "T1", "tur": "dev-koleksiyon", "bolum": "fihrist", "arsivde_tut": ["skills/a", ""]}) == [])
test("1b. dogrula: arsivde_tut bolum arsiv ile HATA",
     any("arsivde_tut" in x and "fihrist" in x for x in dg.kaynak_tur_hatalari(
         {"repo": "o/r", "tip": "T1", "tur": "koleksiyon", "bolum": "arsiv", "arsivde_tut": ["skills/a"]})))
test("1c. dogrula: arsivde_tut bolum yokken HATA",
     any("arsivde_tut" in x for x in dg.kaynak_tur_hatalari({"repo": "o/r", "tip": "T1", "arsivde_tut": ["skills/a"]})))
test("1d. dogrula: arsivde_tut bolum katalog ile HATA",
     any("arsivde_tut" in x for x in dg.kaynak_tur_hatalari({"repo": "o/r", "tip": "T1", "tur": "kit", "bolum": "katalog", "arsivde_tut": ["skills/a"]})))
test("1e. dogrula: arsivde_tut liste değilse ya da metin dışı öğe varsa HATA",
     bool(dg.kaynak_tur_hatalari({"repo": "o/r", "bolum": "fihrist", "arsivde_tut": "skills/a"}))
     and bool(dg.kaynak_tur_hatalari({"repo": "o/r", "bolum": "fihrist", "arsivde_tut": [123]})))
test("1f. dogrula: arsivde_tut KAYNAK_ANAHTARLARI içinde (bilinmeyen anahtar uyarısı yok)",
     "arsivde_tut" in dg.KAYNAK_ANAHTARLARI)

# ---------------------------------------------------------------- 2. ortak.arsive_cekilir
test("2a. arsive_cekilir: bolum fihrist + dolu arsivde_tut -> True",
     ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}) is True)
test("2b. arsive_cekilir: bolum fihrist + kök skil [''] -> True",
     ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist", "arsivde_tut": [""]}) is True)
test("2c. arsive_cekilir: bolum fihrist + boş arsivde_tut [] -> False",
     ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist", "arsivde_tut": []}) is False)
test("2d. arsive_cekilir: bolum fihrist + arsivde_tut yok -> False",
     ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist"}) is False)
test("2e. arsive_cekilir: KAYIP veya katalog + arsivde_tut -> False",
     ortak.arsive_cekilir({"durum": "kayip", "tur": "dev-koleksiyon", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}) is False
     and ortak.arsive_cekilir({"tur": "kit", "bolum": "katalog", "arsivde_tut": ["skills/a"]}) is False)

# ---------------------------------------------------------------- 3. kaynak-cek.py
agac3 = [{"path": p, "type": "blob", "sha": f"h{i}", "size": 20} for i, p in enumerate([
    "skills/a/SKILL.md", "skills/b/SKILL.md", "skills/c/SKILL.md",
    "agents/uzman.md", "commands/kur.md", "skills/a/agents/ic.md", ".github/agents/gh.md", "tests/agents/t.md"])]
kayit3 = {"repo": "dev/kol", "tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}
sec3, den3 = kc.skill_klasorlerini_sec(kayit3, agac3, AYAR_BASIT)
test("3a. kaynak-cek: bolum fihrist + arsivde_tut yalnız tutulan skili seçer, diğerleri 'fihristte'",
     list(sec3.keys()) == ["a"] and sec3["a"]["yol"] == "skills/a"
     and den3["skills/a/SKILL.md"] == "secildi"
     and den3["skills/b/SKILL.md"] == "fihristte" and den3["skills/c/SKILL.md"] == "fihristte", (sec3, den3))
sec3_tum, _ = kc.skill_klasorlerini_sec(kayit3, agac3, AYAR_BASIT, tutulan_uygula=False)
test("3b. kaynak-cek: tutulan_uygula=False (fihrist-uret) tüm skilleri seçer",
     set(sec3_tum.keys()) == {"a", "b", "c"}, sec3_tum)
test("3c. kaynak-cek: bolum fihrist kaydında bileşenler çekilmez",
     kc.bilesenleri_bul(kayit3, agac3, sec3, AYAR_BASIT) == [])
test("3d. kaynak-cek: fihrist_atla=False iken bileşenler (skil içi/.github/tests hariç) bulunur",
     sorted(kc.bilesenleri_bul(kayit3, agac3, sec3_tum, AYAR_BASIT, fihrist_atla=False)) == ["agents/uzman.md", "commands/kur.md"])

# ---------------------------------------------------------------- 4. kapsam-denetimi.py
tmp4 = Path(tempfile.mkdtemp(prefix="p17kd-"))
try:
    (tmp4 / "notlar").mkdir()
    yaz(tmp4 / "arsiv" / "a-kat" / "a" / "SKILL.md", "---\nname: a\ndescription: Tutulan skil\n---\n")
    yaz(tmp4 / "kaynaklar.json", {"repolar": [{"repo": "dev/kol", "tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}]})
    yaz(tmp4 / "registry.json", {
        "skiller": [{"id": "a", "ad": "a", "repo": "dev/kol", "kaynak_yol": "skills/a", "yol": "arsiv/a-kat/a"}],
        "bilesenler": [],
        "denetim": {"dev/kol": {"commit": C40, "skill_md": {"skills/a/SKILL.md": "secildi", "skills/b/SKILL.md": "fihristte"}}},
    })
    eski_kd = (kd.KOK, kd.REGISTRY, kd.KAYNAKLAR, kd.agac_al)
    try:
        kd.KOK, kd.REGISTRY, kd.KAYNAKLAR = tmp4, tmp4 / "registry.json", tmp4 / "kaynaklar.json"
        # c/SKILL.md denetimde hiç olmasa bile arsivde_tut dışında olduğu için 'fihristte' sayılır (sorun değil)
        kd.agac_al = lambda repo, sha=None: {
            "tree": [{"path": p, "type": "blob", "sha": "x"} for p in ("skills/a/SKILL.md", "skills/b/SKILL.md", "skills/c/SKILL.md")],
            "truncated": False,
        }
        r, out, _ = sessiz(kd.main)
        test("4a. kapsam-denetimi: arsivde_tut dışındaki SKILL.md'ler 'fihristte' sayılır, 0 sorun",
             r == 0 and "SORUN" not in out and "'fihristte': 2" in out and "'secildi': 1" in out, (r, out))

        # arsivde_tut içindeki bir yol registry'de yoksa SORUN
        yaz(tmp4 / "kaynaklar.json", {"repolar": [{"repo": "dev/kol", "tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a", "skills/b"]}]})
        r2, out2, _ = sessiz(kd.main)
        test("4b. kapsam-denetimi: arsivde_tut içindeki yol arşivde değilse SORUN (çıkış 1)",
             r2 == 1 and "SORUN" in out2 and "skills/b" in out2, (r2, out2))
    finally:
        kd.KOK, kd.REGISTRY, kd.KAYNAKLAR, kd.agac_al = eski_kd
finally:
    shutil.rmtree(tmp4, ignore_errors=True)

# ---------------------------------------------------------------- 5. fihrist-uret.py (bilesenler & arsivde_tut) & dogrula şeması
b1 = fu.bilesen_girdisi("plugins/x/agents/mimari.md", "---\nname: mimari-uzman\ndescription: Mimari inceleme yapar.\n---\nGövde")
b2 = fu.bilesen_girdisi("plugins/x/commands/kur.md", "# /kur\n\nProjeyi hazırlar ve doğrular.\n\n## Argümanlar\n")
b3 = fu.bilesen_girdisi("agents/yok.md", None)
test("5a. bilesen_girdisi: ajan/komut türü, frontmatter ve ilk paragraf açıklaması, okunamayan fallback",
     b1 == {"tur": "ajan", "ad": "mimari-uzman", "aciklama": "Mimari inceleme yapar.", "yol": "plugins/x/agents/mimari.md"}
     and b2 == {"tur": "komut", "ad": "kur", "aciklama": "Projeyi hazırlar ve doğrular.", "yol": "plugins/x/commands/kur.md"}
     and b3 == {"tur": "ajan", "ad": "yok", "aciklama": "", "yol": "agents/yok.md"}, (b1, b2, b3))

tmp5 = Path(tempfile.mkdtemp(prefix="p17fu-"))
eski_ortak5 = {a: getattr(ortak, a) for a in ("repo_agaci", "ham_metin", "KAYNAKLAR", "REGISTRY")}
eski_fihrist5 = fu.FIHRIST
try:
    yaz(tmp5 / "kaynaklar.json", {"konum_haric": [], "ayna_klasorler": [], "skill_ici_haric": [], "repolar": [
        {"repo": "dev/kol", "tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}]})
    yaz(tmp5 / "registry.json", {"skiller": []})  # registry boş olsa bile arsivde_tut'tan arsivde:true gelmeli
    icerikler5 = {
        "skills/a/SKILL.md": "---\nname: a\ndescription: Skil A\n---\n",
        "skills/b/SKILL.md": "---\nname: b\ndescription: Skil B\n---\n",
        "agents/uzman.md": "---\nname: uzman\ndescription: Uzman ajan\n---\n",
        "commands/calistir.md": "---\ndescription: Çalıştırma komutu\n---\n",
    }
    ortak.repo_agaci = lambda repo, sha=None: (C40, {"tree": [{"path": p, "type": "blob", "sha": "x", "size": 5} for p in icerikler5], "truncated": False, "_kaynak": "api"})
    ortak.ham_metin = lambda repo, yol, ref="HEAD", azami=0: icerikler5.get(yol)
    ortak.KAYNAKLAR, ortak.REGISTRY = tmp5 / "kaynaklar.json", tmp5 / "registry.json"
    fu.FIHRIST = tmp5 / "fihrist"
    r5, out5, _ = sessiz(fu.main, ["dev/kol"])
    f5 = json.loads((tmp5 / "fihrist" / "dev__kol.json").read_text(encoding="utf-8"))
    test("5b. fihrist-uret main: bilesenler yazılır, tüm skiller alınır, arsivde:true arsivde_tut'tan gelir",
         r5 == 0 and len(f5["skiller"]) == 2
         and f5["skiller"][0].get("arsivde") is True and "arsivde" not in f5["skiller"][1]
         and f5["bilesenler"] == [
             {"tur": "ajan", "ad": "uzman", "aciklama": "Uzman ajan", "yol": "agents/uzman.md"},
             {"tur": "komut", "ad": "calistir", "aciklama": "Çalıştırma komutu", "yol": "commands/calistir.md"},
         ] and "2 bileşen" in out5, (r5, f5, out5))
    test("5c. fihrist-uret çıktısı dogrula.fihrist_hatalari'ndan geçer",
         dg.fihrist_hatalari(f5, "dev/kol") == [], dg.fihrist_hatalari(f5, "dev/kol"))
finally:
    for a, v in eski_ortak5.items():
        setattr(ortak, a, v)
    fu.FIHRIST = eski_fihrist5
    shutil.rmtree(tmp5, ignore_errors=True)

iyi_genis = {
    "repo": "o/r", "commit": C40, "tarih": "2026-11-19", "skil_sayisi": 1,
    "skiller": [{"ad": "x", "aciklama": "A", "yol": "skills/x", "inceleme": {
        "commit": C40, "tarih": "2026-11-19", "sonuc": "incelendi", "not": "iyi",
        "ozet_tr": "Türkçe özet", "kalite": 4, "teknoloji": ["python"],
        "aciklama_tr": {"ne": "Ne yapar", "ne_zaman": "Ne zaman"},
    }}],
    "bilesenler": [{"tur": "ajan", "ad": "a", "aciklama": "Ajan", "yol": "agents/a.md"}],
}
test("5d. dogrula fihrist_hatalari: genişletilmiş inceleme ve bilesenler geçerli",
     dg.fihrist_hatalari(iyi_genis, "o/r") == [], dg.fihrist_hatalari(iyi_genis, "o/r"))
test("5e. dogrula fihrist_hatalari: bilesenler tur='agent' (ajan değil) ve tekrarlanan yol HATA",
     len(dg.fihrist_hatalari({**iyi_genis, "bilesenler": [
         {"tur": "agent", "ad": "a", "aciklama": "", "yol": "agents/a.md"},
         {"tur": "komut", "ad": "b", "aciklama": "", "yol": "agents/a.md"},
     ]}, "o/r")) >= 2)
test("5f. dogrula fihrist_hatalari: bozuk genişletilmiş inceleme (kalite=9, aciklama_tr bozuk) HATA",
     len(dg.fihrist_hatalari({**iyi_genis, "skiller": [{"ad": "x", "aciklama": "A", "yol": "skills/x", "inceleme": {
         "commit": C40, "tarih": "2026-11-19", "sonuc": "incelendi", "kalite": 9, "aciklama_tr": {"ne": 5}}}]}, "o/r")) >= 2)


# ---------------------------------------------------------------- 6. fihriste-tasi.py (uçtan uca geçici kütüphane)
def kur_sahte_kutuphane(projeli=True, md_yedek=False, git_kur=True):
    t = Path(tempfile.mkdtemp(prefix="p17ft-"))
    kok = t / "lib"
    proj_kok = t / "projeler"
    kok.mkdir()
    proj_kok.mkdir()

    # Arşiv dosyaları
    yaz(kok / "arsiv" / "cat" / "kept-role" / "SKILL.md", "---\nname: kept-role\ndescription: Rolden tutulan\n---\n" + "x" * 200)
    yaz(kok / "arsiv" / "cat" / "kept-role" / "KAYNAK.md", "# kept-role\n")
    yaz(kok / "arsiv" / "cat" / "kept-proj" / "SKILL.md", "---\nname: kept-proj\ndescription: Projeden tutulan\n---\n" + "y" * 200)
    yaz(kok / "arsiv" / "cat" / "kept-proj" / "KAYNAK.md", "# kept-proj\n")
    yaz(kok / "arsiv" / "cat" / "reviewed" / "SKILL.md", "---\nname: reviewed\ndescription: İncelenmiş skil\n---\n" + "z" * 1500)
    yaz(kok / "arsiv" / "cat" / "reviewed" / "KAYNAK.md", "# reviewed\n")
    yaz(kok / "arsiv" / "_varyantlar" / "reviewed" / "claude" / "SKILL.md", "varyant\n" * 50)
    yaz(kok / "arsiv" / "cat" / "shared" / "SKILL.md", "---\nname: shared\ndescription: Ortak adlı\n---\n" + "w" * 1000)
    yaz(kok / "arsiv" / "cat" / "shared" / "KAYNAK.md", "# shared\n")
    yaz(kok / "arsiv" / "cat" / "shared@other" / "SKILL.md", "---\nname: shared\ndescription: Diğer kaynak\n---\n")
    yaz(kok / "arsiv" / "cat" / "shared@other" / "KAYNAK.md", "# shared@other\n")
    yaz(kok / "arsiv" / "_bilesenler" / "dev__kol" / "agents" / "uzman.md", "---\nname: uzman\ndescription: Uzman\n---\n" + "a" * 300)
    yaz(kok / "arsiv" / "_bilesenler" / "dev__kol" / "commands" / "kur.md", "---\ndescription: Kur\n---\n" + "b" * 300)
    yaz(kok / "arsiv" / "_bilesenler" / "other__repo" / "agents" / "diger.md", "---\nname: diger\n---\n")

    yaz(kok / "kaynaklar.json", {"repolar": [
        {"repo": "dev/kol", "tip": "T1", "oncelik": 4, "tur": "koleksiyon", "bolum": "arsiv",
         "skill_bagimlilik": {"skills/kept-role": "python", "skills/reviewed": "node"}},
        {"repo": "other/repo", "tip": "T1", "oncelik": 2, "tur": "koleksiyon", "bolum": "arsiv"},
        {"repo": "prog/app", "tip": "T1", "program": "myapp"},
    ]})
    yaz(kok / "registry.json", {
        "guncelleme": "2026-11-10",
        "skiller": [
            {"id": "kept-role", "ad": "kept-role", "durum": "tercih", "repo": "dev/kol", "tip": "T1",
             "kaynak_yol": "skills/kept-role", "yol": "arsiv/cat/kept-role", "commit": C40, "inceleme": "otomatik"},
            {"id": "kept-proj", "ad": "kept-proj", "durum": "tercih", "repo": "dev/kol", "tip": "T1",
             "kaynak_yol": "skills/kept-proj", "yol": "arsiv/cat/kept-proj", "commit": C40, "inceleme": "otomatik"},
            {"id": "reviewed", "ad": "reviewed", "durum": "tercih", "repo": "dev/kol", "tip": "T1",
             "kaynak_yol": "skills/reviewed", "yol": "arsiv/cat/reviewed",
             "varyantlar": {"claude": "arsiv/_varyantlar/reviewed/claude"},
             "commit": C40, "inceleme": "incelendi", "inceleme_tarihi": "2026-10-21", "inceleyen": "claude",
             "ozet_tr": "Elle Türkçe özet", "kalite": 4, "kalite_notu": "İyi kalite", "notlar": "Dikkatli kullan",
             "kullanim_alani": "Web", "kullanma": "Mobil", "zorluk": "orta", "teknoloji": ["python"],
             "ortusme_grubu": "g1", "ortusme_rolu": "alternatif"},
            {"id": "shared", "ad": "shared", "durum": "tercih", "repo": "dev/kol", "tip": "T1",
             "kaynak_yol": "skills/shared", "yol": "arsiv/cat/shared", "commit": C40, "arsiv_tarihi": "2026-11-01",
             "inceleme": "otomatik"},
            {"id": "shared@other", "ad": "shared", "durum": "alternatif", "repo": "other/repo", "tip": "T1",
             "kaynak_yol": "skills/shared", "yol": "arsiv/cat/shared@other", "commit": C40, "inceleme": "otomatik"},
        ],
        "bilesenler": [
            {"repo": "dev/kol", "commit": C40, "tur": "agent", "kaynak_yol": "agents/uzman.md",
             "yol": "arsiv/_bilesenler/dev__kol/agents/uzman.md", "ad": "uzman"},
            {"repo": "dev/kol", "commit": C40, "tur": "komut", "kaynak_yol": "commands/kur.md",
             "yol": "arsiv/_bilesenler/dev__kol/commands/kur.md", "ad": "kur"},
            {"repo": "other/repo", "commit": C40, "tur": "agent", "kaynak_yol": "agents/diger.md",
             "yol": "arsiv/_bilesenler/other__repo/agents/diger.md", "ad": "diger"},
        ],
        "denetim": {
            "dev/kol": {"commit": C40, "skill_md": {
                "skills/kept-role/SKILL.md": "secildi",
                "skills/kept-proj/SKILL.md": "secildi",
                "skills/reviewed/SKILL.md": "secildi",
                "skills/shared/SKILL.md": "secildi",
            }},
        },
    })
    yaz(kok / "fihrist" / "dev__kol.json", {
        "repo": "dev/kol", "commit": C40, "tarih": "2026-11-19", "skil_sayisi": 4,
        "skiller": [
            {"ad": "kept-proj", "aciklama": "Projeden tutulan", "yol": "skills/kept-proj", "arsivde": True},
            {"ad": "kept-role", "aciklama": "Rolden tutulan", "yol": "skills/kept-role", "arsivde": True},
            {"ad": "reviewed", "aciklama": "İncelenmiş skil", "yol": "skills/reviewed", "arsivde": True},
            {"ad": "shared", "aciklama": "Ortak adlı", "yol": "skills/shared", "arsivde": True},
        ],
        "bilesenler": [
            {"tur": "ajan", "ad": "uzman", "aciklama": "Uzman", "yol": "agents/uzman.md"},
            {"tur": "komut", "ad": "kur", "aciklama": "Kur", "yol": "commands/kur.md"},
        ],
    })
    yaz(kok / "roller" / "r1.json", {"ad": "r1", "cekirdek": ["kept-role"], "opsiyonel": []})
    yaz(kok / "profiller" / "p1.json", {"ad": "p1", "roller": ["r1"], "ek_skiller": []})
    yaz(kok / "ucret-siniflandirma.json", {"_aciklama": "t", "siniflar": {
        "kept-role": ["ucretsiz", "kalsın"],
        "reviewed": ["kismen", "temizlenecek"],
        "shared": ["ucretsiz", "kardeş shared@other yüzünden korunmalı"],
    }})
    yaz(kok / "aciklama-tr.json", {
        "kept-role": {"ne": "Kalsın", "ne_zaman": "Her zaman", "kaynak": "1"},
        "shared": {"ne": "Paylaşılan işi yapar.", "ne_zaman": "Paylaşım gerekince.", "kaynak": "2"},
    })
    yaz(kok / "yol-istisnalari.json", {"_aciklama": "t", "istisnalar": {
        "dev/kol::skills/kept-role": {"ad": "kept-role", "kayitlar": []},
        "dev/kol::skills/reviewed": {"ad": "reviewed", "kayitlar": []},
        "other/repo::skills/shared": {"ad": "shared@other", "kayitlar": []},
    }})
    if projeli:
        yaz(proj_kok / "OrnekProje" / ".skill-kutuphanesi" / "kilit.json", {"skiller": {
            "kept-proj": {"id": "kept-proj", "repo": "dev/kol", "kaynak_yol": "skills/kept-proj", "roller": []}
        }})
    yaz(kok / "projeler.json", {"tarama_kokleri": [str(proj_kok)]})
    if md_yedek:
        yaz(kok / "notlar" / "proje-kullanimi.md",
            "# Proje kullanımı\n\n## MdProje\n\n| Skill | Kaynak | Commit | Roller | Not |\n|---|---|---|---|---|\n"
            "| `kept-proj` | dev/kol | `aaaaaaa` | — |  |\n")
    if git_kur:
        git_temiz_hazirla(kok)
    return t, kok


# 6a. Ön koşullar: fihrist yoksa veya program kaynağıysa dur (çıkış 2)
t6a, kok6a = kur_sahte_kutuphane()
try:
    (kok6a / "fihrist" / "dev__kol.json").unlink()
    once = agac_ozeti(kok6a)
    r, out, err = sessiz(ft.main, ["dev/kol", "--kuru"], kok=kok6a)
    test("6a. fihriste-tasi: fihrist dosyası yoksa çıkış 2, dosya değişmez",
         r == 2 and "fihrist-uret.py" in err and agac_ozeti(kok6a) == once, (r, out, err))
    r_pr, _, err_pr = sessiz(ft.main, ["prog/app", "--kuru"], kok=kok6a)
    test("6b. fihriste-tasi: program kaynağı reddedilir (çıkış 2)", r_pr == 2 and "Program" in err_pr, (r_pr, err_pr))
finally:
    shutil.rmtree(t6a, ignore_errors=True)

# 6c. Kullanılan skil arsivde_tut'ta değilken HATA (hem --kuru hem --evet hiçbir şeye dokunmaz)
t6c, kok6c = kur_sahte_kutuphane()
try:
    once = agac_ozeti(kok6c)
    r1, out1, _ = sessiz(ft.main, ["dev/kol", "--kuru"], kok=kok6c)
    r2, out2, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role"], kok=kok6c)
    test("6c. fihriste-tasi: rolde/projede kullanılan skil arsivde_tut'ta değilken HATA (çıkış 1) ve dosya değişmez",
         r1 == 1 and "HATA:" in out1 and "kept-role" in out1 and "kept-proj" in out1
         and r2 == 1 and "kept-proj" in out2 and "HATA:" in out2 and agac_ozeti(kok6c) == once, (r1, r2, out2))
    r3, out3, _ = sessiz(ft.main, ["dev/kol", "--kuru", "--arsivde-tut", "skills/kept-role", "--arsivde-tut", "skills/kept-proj", "--arsivde-tut", "skills/yok"], kok=kok6c)
    test("6d. fihriste-tasi: arşivde olmayan arsivde_tut yolu HATA (çıkış 1)",
         r3 == 1 and "bulunamadı" in out3 and "skills/yok" in out3, (r3, out3))
finally:
    shutil.rmtree(t6c, ignore_errors=True)

# 6e. Proje bilgisi canlı kilitten yokken notlar/proje-kullanimi.md yedeğinden yakalanır
t6e, kok6e = kur_sahte_kutuphane(projeli=False, md_yedek=True)
try:
    r, out, _ = sessiz(ft.main, ["dev/kol", "--kuru", "--arsivde-tut", "skills/kept-role"], kok=kok6e)
    test("6e. fihriste-tasi: canlı proje yokken notlar/proje-kullanimi.md içindeki proje kullanımı yakalanır -> HATA",
         r == 1 and "MdProje" in out and "kept-proj" in out, (r, out))
finally:
    shutil.rmtree(t6e, ignore_errors=True)

# 6f. --kuru (ve varsayılan bayraksız): rapor tam, hiçbir dosya değişmez; --evet: tam taşıma
t6f, kok6f = kur_sahte_kutuphane()
try:
    once = agac_ozeti(kok6f)
    rk, outk, _ = sessiz(ft.main, ["dev/kol", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok6f)
    test("6f. fihriste-tasi varsayılan (--kuru): dosya değişmez; çıkacak/kalacak/yer/not/çıplak ad/katalog raporda",
         rk == 0 and agac_ozeti(kok6f) == once
         and "2 skil, 2 bileşen" in outk and "Arşivde kalacak: 2 skil" in outk
         and "1 inceleme notu, 2 Türkçe açıklama" in outk
         and "shared@other" in outk and "katalog-uret.py" in outk, (rk, outk))

    re_, oute, erre = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role", "--arsivde-tut", "skills/kept-proj"], kok=kok6f)
    test("6g. fihriste-tasi --evet: çıkış 0, rapor çıktı ve katalog yenileme uyarısı var",
         re_ == 0 and "FİHRİSTE TAŞIMA UYGULANDI" in oute and "katalog-uret.py" in oute and "skill-readme.py" in oute, (re_, oute, erre))

    # (a) fihrist dosyası: inceleme ve aciklama_tr taşındı, arsivde yalnız tutulanlarda, şema temiz
    fih = json.loads((kok6f / "fihrist" / "dev__kol.json").read_text(encoding="utf-8"))
    f_yol = {x["yol"]: x for x in fih["skiller"]}
    test("6h. fihriste-tasi --evet (a): inceleme notları (ozet_tr, kalite, not) ve aciklama-tr fihriste taşındı",
         f_yol["skills/reviewed"].get("inceleme", {}).get("ozet_tr") == "Elle Türkçe özet"
         and f_yol["skills/reviewed"]["inceleme"].get("kalite") == 4
         and f_yol["skills/reviewed"]["inceleme"].get("not") == "Dikkatli kullan"
         and f_yol["skills/reviewed"]["inceleme"].get("sonuc") == "incelendi"
         and f_yol["skills/shared"].get("inceleme", {}).get("aciklama_tr") == {"ne": "Paylaşılan işi yapar.", "ne_zaman": "Paylaşım gerekince."}
         and f_yol["skills/kept-role"].get("arsivde") is True and f_yol["skills/kept-proj"].get("arsivde") is True
         and "arsivde" not in f_yol["skills/reviewed"] and "arsivde" not in f_yol["skills/shared"]
         and dg.fihrist_hatalari(fih, "dev/kol") == [], fih)

    # (b) arsiv/ ve registry.json: çıkarılanlar gitti, kalanlar ve diğer repo korundu
    reg = json.loads((kok6f / "registry.json").read_text(encoding="utf-8"))
    reg_ids = {s["id"]: s for s in reg["skiller"]}
    test("6i. fihriste-tasi --evet (b): tutulan skiller korundu, diğerleri + varyant + bileşenler arşiv ve registry'den çıktı",
         set(reg_ids) == {"kept-role", "kept-proj", "shared@other"}
         and (kok6f / "arsiv" / "cat" / "kept-role" / "SKILL.md").exists()
         and (kok6f / "arsiv" / "cat" / "kept-proj" / "SKILL.md").exists()
         and not (kok6f / "arsiv" / "cat" / "reviewed").exists()
         and not (kok6f / "arsiv" / "_varyantlar" / "reviewed").exists()
         and not (kok6f / "arsiv" / "cat" / "shared").exists()
         and not (kok6f / "arsiv" / "_bilesenler" / "dev__kol").exists()
         and (kok6f / "arsiv" / "_bilesenler" / "other__repo" / "agents" / "diger.md").exists()
         and [b["repo"] for b in reg["bilesenler"]] == ["other/repo"], (reg_ids, reg["bilesenler"]))

    # (c) kaynaklar.json: tur, bolum, arsivde_tut, skill_bagimlilik temizliği ve dogrula uyumu
    kay = json.loads((kok6f / "kaynaklar.json").read_text(encoding="utf-8"))
    k_dev = next(k for k in kay["repolar"] if k["repo"] == "dev/kol")
    test("6j. fihriste-tasi --evet (c): kaynak kaydı tur=dev-koleksiyon, bolum=fihrist, arsivde_tut doğru; dogrula 0 hata",
         k_dev["tur"] == "dev-koleksiyon" and k_dev["bolum"] == "fihrist"
         and k_dev["arsivde_tut"] == ["skills/kept-proj", "skills/kept-role"]
         and k_dev.get("skill_bagimlilik") == {"skills/kept-role": "python"}
         and dg.kaynak_tur_hatalari(k_dev) == [], k_dev)
    h8, u8 = [], []
    dg._e8_fihrist_kit(kok6f, h8, u8)
    test("6k. fihriste-tasi --evet: _e8_fihrist_kit 0 hata 0 uyarı", h8 == [] and u8 == [], (h8, u8))

    # (d) yardımcı dosyalar temizlendi, kalan skillerinki ve paylaşılan kardeşinki korundu
    uc = json.loads((kok6f / "ucret-siniflandirma.json").read_text(encoding="utf-8"))["siniflar"]
    atr = json.loads((kok6f / "aciklama-tr.json").read_text(encoding="utf-8"))
    yi = json.loads((kok6f / "yol-istisnalari.json").read_text(encoding="utf-8"))["istisnalar"]
    test("6l. fihriste-tasi --evet (d): ucret, aciklama-tr, yol-istisnalari temizlendi; kalan ve kardeş korundu",
         set(uc) == {"kept-role", "shared"} and set(atr) == {"kept-role"}
         and set(yi) == {"dev/kol::skills/kept-role", "other/repo::skills/shared"}, (uc, atr, yi))

    # (e) çıplak ad / tercih el değişimi
    test("6m. fihriste-tasi --evet (e): aynı adlı kardeş shared@other 'tercih' oldu (kimlik değişmedi) ve raporlandı",
         reg_ids["shared@other"]["durum"] == "tercih" and "shared@other" in oute and "yeni tercih" in oute, (reg_ids["shared@other"], oute))

    # denetim güncellemesi sonrası kapsam-denetimi 0 sorun (uçtan uca)
    test("6n. fihriste-tasi --evet: registry denetim kaydında çıkarılanlar 'fihristte', tutulanlar 'secildi'",
         reg["denetim"]["dev/kol"]["skill_md"] == {
             "skills/kept-role/SKILL.md": "secildi",
             "skills/kept-proj/SKILL.md": "secildi",
             "skills/reviewed/SKILL.md": "fihristte",
             "skills/shared/SKILL.md": "fihristte",
         }, reg["denetim"])
    (kok6f / "notlar").mkdir(exist_ok=True)
    # other/repo ve prog/app için denetim kaydı ekleyip kapsam-denetimi'ni uçtan uca koştur
    reg["denetim"]["other/repo"] = {"commit": C40, "skill_md": {"skills/shared/SKILL.md": "secildi"}}
    reg["denetim"]["prog/app"] = {"commit": C40, "skill_md": {}}
    yaz(kok6f / "registry.json", reg)
    eski_kd2 = (kd.KOK, kd.REGISTRY, kd.KAYNAKLAR, kd.agac_al)
    try:
        kd.KOK, kd.REGISTRY, kd.KAYNAKLAR = kok6f, kok6f / "registry.json", kok6f / "kaynaklar.json"
        kd.agac_al = lambda repo, sha=None: {
            "tree": [{"path": p, "type": "blob", "sha": "x"} for p in (
                ("skills/kept-role/SKILL.md", "skills/kept-proj/SKILL.md", "skills/reviewed/SKILL.md", "skills/shared/SKILL.md")
                if repo == "dev/kol" else ("skills/shared/SKILL.md",) if repo == "other/repo" else ())],
            "truncated": False,
        }
        rkd, outkd, _ = sessiz(kd.main)
        test("6n2. fihriste-tasi --evet sonrası kapsam-denetimi: 0 sorun, tutulanlar secildi, diğerleri fihristte",
             rkd == 0 and "SORUN" not in outkd and "'fihristte': 2" in outkd, (rkd, outkd))
    finally:
        kd.KOK, kd.REGISTRY, kd.KAYNAKLAR, kd.agac_al = eski_kd2
finally:
    shutil.rmtree(t6f, ignore_errors=True)

# 6p. Profilde (ek_skiller) kullanılan skil arsivde_tut'ta değilken HATA
t6p, kok6p = kur_sahte_kutuphane(projeli=False)
try:
    yaz(kok6p / "roller" / "r1.json", {"ad": "r1", "cekirdek": [], "opsiyonel": []})
    yaz(kok6p / "profiller" / "p1.json", {"ad": "p1", "roller": ["r1"], "ek_skiller": ["reviewed"]})
    rp, outp, _ = sessiz(ft.main, ["dev/kol", "--kuru"], kok=kok6p)
    test("6p. fihriste-tasi: profil ek_skiller içindeki skil arsivde_tut'ta değilken HATA",
         rp == 1 and "HATA:" in outp and "reviewed" in outp and "profiller/p1.json" in outp, (rp, outp))
finally:
    shutil.rmtree(t6p, ignore_errors=True)

# 6o. Hiç tutulan skil yoksa (arsivde_tut boş) ve çok kayıtlı repo (T1 + T4)
t6o, kok6o = kur_sahte_kutuphane(projeli=False, git_kur=False)
try:
    yaz(kok6o / "roller" / "r1.json", {"ad": "r1", "cekirdek": [], "opsiyonel": []})
    yaz(kok6o / "notlar" / "proje-kullanimi.md", "# Proje kullanımı\n\n(Bu repoyu kullanan proje yok)\n")
    kay0 = json.loads((kok6o / "kaynaklar.json").read_text(encoding="utf-8"))
    kay0["repolar"].append({"repo": "dev/kol", "tur": "koleksiyon", "bolum": "arsiv", "oncelik": 9, "dahil": ["^ent/"], "kimlik": "dev-ent"})
    yaz(kok6o / "kaynaklar.json", kay0)
    git_temiz_hazirla(kok6o)
    r0, out0, _ = sessiz(ft.main, ["dev/kol", "--evet"], kok=kok6o)
    kay_son = [k for k in json.loads((kok6o / "kaynaklar.json").read_text(encoding="utf-8"))["repolar"] if k["repo"] == "dev/kol"]
    reg_son = json.loads((kok6o / "registry.json").read_text(encoding="utf-8"))
    test("6o. fihriste-tasi --evet (0 tutulan, T1+T4 çok kayıt): tüm kayıtlar fihrist, arsivde_tut yok, denetim temiz, arsive_cekilir False",
         r0 == 0 and len(kay_son) == 2
         and all(k["tur"] == "dev-koleksiyon" and k["bolum"] == "fihrist" and "arsivde_tut" not in k and not ortak.arsive_cekilir(k) for k in kay_son)
         and "dev/kol" not in reg_son["denetim"] and all(s["repo"] != "dev/kol" for s in reg_son["skiller"]),
         (r0, out0, kay_son, reg_son["denetim"]))
finally:
    shutil.rmtree(t6o, ignore_errors=True)

# ---------------------------------------------------------------- 7. Bağımsız inceleme düzeltmeleri (bulgu 1..6)

# 7a-7b (Bulgu 1): inceleme notu veya aciklama-tr fihristte karşılık bulamıyorsa --evet DURUR (HATA), veri kaybı olmaz
t7a, kok7a = kur_sahte_kutuphane(git_kur=False)
try:
    f7a = json.loads((kok7a / "fihrist" / "dev__kol.json").read_text(encoding="utf-8"))
    # reviewed (elle inceleme notu var) fihristten çıkarılmış olsun
    f7a["skiller"] = [x for x in f7a["skiller"] if x["yol"] != "skills/reviewed"]
    f7a["skil_sayisi"] = len(f7a["skiller"])
    yaz(kok7a / "fihrist" / "dev__kol.json", f7a)
    git_temiz_hazirla(kok7a)
    once7a = agac_ozeti(kok7a)
    r7a, out7a, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7a)
    test("7a. Bulgu 1: inceleme notu olan skil fihristte yoksa --evet HATA ile durur, hiçbir dosya değişmez",
         r7a == 1 and "HATA:" in out7a and "skills/reviewed" in out7a and agac_ozeti(kok7a) == once7a, (r7a, out7a))
finally:
    shutil.rmtree(t7a, ignore_errors=True)

t7b, kok7b = kur_sahte_kutuphane(git_kur=False)
try:
    f7b = json.loads((kok7b / "fihrist" / "dev__kol.json").read_text(encoding="utf-8"))
    # shared (otomatik ama aciklama-tr.json'da Türkçe açıklaması var) fihristte yok
    f7b["skiller"] = [x for x in f7b["skiller"] if x["yol"] != "skills/shared"]
    f7b["skil_sayisi"] = len(f7b["skiller"])
    yaz(kok7b / "fihrist" / "dev__kol.json", f7b)
    git_temiz_hazirla(kok7b)
    once7b = agac_ozeti(kok7b)
    r7b, out7b, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7b)
    test("7b. Bulgu 1: yalnız aciklama-tr kaydı olan skil fihristte yoksa --evet HATA ile durur, aciklama-tr silinmez",
         r7b == 1 and "HATA:" in out7b and "skills/shared" in out7b and agac_ozeti(kok7b) == once7b, (r7b, out7b))
finally:
    shutil.rmtree(t7b, ignore_errors=True)

# 7c-7d (Bulgu 2): proje bilgisi doğrulanamıyorsa veya kullanım girdisi eşleşmiyorsa HATA ve --evet DURUR
t7c, kok7c = kur_sahte_kutuphane(projeli=False, md_yedek=False, git_kur=False)
try:
    yaz(kok7c / "roller" / "r1.json", {"ad": "r1", "cekirdek": [], "opsiyonel": []})
    git_temiz_hazirla(kok7c)
    once7c = agac_ozeti(kok7c)
    r7c_k, out7c_k, _ = sessiz(ft.main, ["dev/kol", "--kuru"], kok=kok7c)
    r7c_e, out7c_e, _ = sessiz(ft.main, ["dev/kol", "--evet"], kok=kok7c)
    test("7c. Bulgu 2: canlı proje ve proje-kullanimi.md yoksa proje kullanımı doğrulanamaz -> HATA (kuru ve evet durur)",
         r7c_k == 1 and r7c_e == 1 and "HATA:" in out7c_e and "proje kullanımı doğrulanamadı" in out7c_e
         and agac_ozeti(kok7c) == once7c, (r7c_k, r7c_e, out7c_e))
finally:
    shutil.rmtree(t7c, ignore_errors=True)

t7d, kok7d = kur_sahte_kutuphane(projeli=False, md_yedek=False, git_kur=False)
try:
    yaz(kok7d / "roller" / "r1.json", {"ad": "r1", "cekirdek": [], "opsiyonel": []})
    # notlar/proje-kullanimi.md içinde bu repo için registry ile eşleşmeyen skil adı var
    yaz(kok7d / "notlar" / "proje-kullanimi.md",
        "# Proje kullanımı\n\n## EskiProje\n\n| Skill | Kaynak | Commit | Roller | Not |\n|---|---|---|---|---|\n"
        "| `eslesmeyen-skil` | dev/kol | `aaaaaaa` | — |  |\n")
    git_temiz_hazirla(kok7d)
    once7d = agac_ozeti(kok7d)
    r7d, out7d, _ = sessiz(ft.main, ["dev/kol", "--evet"], kok=kok7d)
    # Ayrıca kullanilan_skilleri_bul doğrudan rol/profil/canlı proje eşleşmeme testi
    _, esl_direct = ft.kullanilan_skilleri_bul(
        [{"id": "a", "ad": "a", "durum": "tercih", "kaynak_yol": "skills/a"}],
        {
            "proje_bilgisi": "var",
            "roller": [{"dosya": "roller/r.json", "alan": "cekirdek", "girdi": "hayalet-rol"}],
            "profiller": [{"dosya": "profiller/p.json", "alan": "ek_skiller", "girdi": "hayalet-profil"}],
            "projeler": [{"proje": "P", "skiller": [{"kurulu_ad": "hayalet-proje", "id": "hayalet-proje"}]}],
        },
    )
    test("7d. Bulgu 2: eşleşmeyen proje/rol/profil kullanım girdisi sessizce atlanmaz -> HATA ve dosya değişmez",
         r7d == 1 and "HATA:" in out7d and "eslesmeyen-skil" in out7d and agac_ozeti(kok7d) == once7d
         and len(esl_direct) == 3, (r7d, out7d, esl_direct))
finally:
    shutil.rmtree(t7d, ignore_errors=True)

# 7e-7g (Bulgu 3): kaynak-cikar.arsivden_cikar ortak kök, paylaşılan/üst klasör ve dosya-vs-klasör koruması
t7e = Path(tempfile.mkdtemp(prefix="p17bulgu3-"))
try:
    yaz(t7e / "arsiv" / "cat" / "kept" / "SKILL.md", "kalsın\n")
    yaz(t7e / "arsiv" / "cat" / "drop" / "SKILL.md", "silinecek\n")
    yaz(t7e / "arsiv" / "_varyantlar" / "kept" / "claude" / "SKILL.md", "var-kalsın\n")
    yaz(t7e / "arsiv" / "_bilesenler" / "other__repo" / "agents" / "a.md", "bil-kalsın\n")
    yaz(t7e / "disari.txt", "dışarı\n")
    kalan_sk = [{"id": "kept", "yol": "arsiv/cat/kept", "varyantlar": {"claude": "arsiv/_varyantlar/kept/claude"}}]
    kalan_bl = [{"ad": "a", "yol": "arsiv/_bilesenler/other__repo/agents/a.md"}]

    def reddedildi(cik_sk, cik_bl):
        try:
            kcik.arsivden_cikar(t7e, cik_sk, cik_bl, kalan_skiller=kalan_sk, kalan_bilesenler=kalan_bl)
            return False
        except ValueError:
            return True

    once7e = agac_ozeti(t7e)
    ortak_kokler_ok = all(
        reddedildi([{"id": "bad", "yol": y}], [])
        for y in ("arsiv", "arsiv/", "arsiv/_varyantlar", "arsiv/_bilesenler", "../disari.txt")
    )
    varyant_kok_ok = reddedildi([{"id": "bad", "yol": "arsiv/cat/drop", "varyantlar": {"claude": "arsiv/_varyantlar"}}], [])
    bilesen_kok_ok = reddedildi([], [{"ad": "bad", "yol": "arsiv/_bilesenler"}])
    test("7e. Bulgu 3: arsiv/, arsiv/_varyantlar, arsiv/_bilesenler ortak kökleri ve arsiv dışı yollar reddedilir, hiçbir şey silinmez",
         ortak_kokler_ok and varyant_kok_ok and bilesen_kok_ok and agac_ozeti(t7e) == once7e)

    paylasilan_ok = (
        reddedildi([{"id": "bad", "yol": "arsiv/cat/kept"}], [])
        and reddedildi([{"id": "bad", "yol": "arsiv/cat"}], [])
        and reddedildi([{"id": "bad", "yol": "arsiv/cat/kept/alt"}], [])
        and reddedildi([{"id": "bad", "yol": "arsiv/cat/drop", "varyantlar": {"claude": "arsiv/_varyantlar/kept"}}], [])
        and reddedildi([], [{"ad": "bad", "yol": "arsiv/_bilesenler/other__repo/agents/a.md"}])
        and reddedildi([{"id": "bad", "yol": "arsiv/_bilesenler/other__repo"}], [])
    )
    test("7f. Bulgu 3: kalan skil/varyant/bileşenle paylaşılan, üst veya iç klasörler reddedilir; drop bile silinmez",
         paylasilan_ok and agac_ozeti(t7e) == once7e and (t7e / "arsiv" / "cat" / "drop" / "SKILL.md").exists())

    # p dosya ise shutil.rmtree istisna atmaz; dosya atlanır ve sonraki geçerli skil silinir
    yaz(t7e / "arsiv" / "cat" / "dosya-skil", "bu bir dosya\n")
    sonuc7g = kcik.arsivden_cikar(
        t7e,
        [{"id": "dosya-skil", "yol": "arsiv/cat/dosya-skil"}, {"id": "drop", "yol": "arsiv/cat/drop"}],
        [],
        kalan_skiller=kalan_sk,
        kalan_bilesenler=kalan_bl,
    )
    test("7g. Bulgu 3: skil yolu dosya ise shutil.rmtree çökmez (atlanan), geçerli skil silinir, kalanlar korunur",
         sonuc7g["silinen_skil_klasoru"] == 1 and sonuc7g["atlanan"] == ["arsiv/cat/dosya-skil"]
         and (t7e / "arsiv" / "cat" / "dosya-skil").is_file()
         and not (t7e / "arsiv" / "cat" / "drop").exists()
         and (t7e / "arsiv" / "cat" / "kept" / "SKILL.md").exists(), sonuc7g)
finally:
    shutil.rmtree(t7e, ignore_errors=True)

# 7h-7i (Bulgu 4): --evet öncesi git temizliği, atomik JSON yazımı ve önce JSON sonra arşiv silme sırası
t7h, kok7h = kur_sahte_kutuphane(git_kur=True)
try:
    yaz(kok7h / "kirli.txt", "commit edilmemis\n")
    once7h = agac_ozeti(kok7h)
    r7h_k, out7h_k, _ = sessiz(ft.main, ["dev/kol", "--kuru", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7h)
    r7h_e, out7h_e, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7h)
    # git deposu olmayan klasörde de --evet durmalı
    t7h2, kok7h2 = kur_sahte_kutuphane(git_kur=False)
    try:
        once7h2 = agac_ozeti(kok7h2)
        r7h2, out7h2, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7h2)
    finally:
        shutil.rmtree(t7h2, ignore_errors=True)
    test("7h. Bulgu 4: git kirliyse veya git deposu değilse --evet HATA ile durur (dosya değişmez); --kuru çalışır",
         r7h_k == 0 and r7h_e == 1 and "git çalışma ağacı temiz" in out7h_e and agac_ozeti(kok7h) == once7h
         and r7h2 == 1 and "HATA:" in out7h2 and agac_ozeti(kok7h) == once7h, (r7h_k, r7h_e, out7h_e, r7h2, out7h2))
finally:
    shutil.rmtree(t7h, ignore_errors=True)

t7i, kok7i = kur_sahte_kutuphane(git_kur=True)
try:
    plan7i = ft.planla(kok7i, "dev/kol", arsivde_tut=["skills/kept-role", "skills/kept-proj"])
    adim_sirasi = []
    gercek_replace = os.replace
    gercek_modul = ft._modul

    def izle_replace(src, dst):
        adim_sirasi.append(("json", Path(dst).name))
        return gercek_replace(src, dst)

    class _IzleyiciKcik:
        def __init__(self, asil):
            self._asil = asil

        def __getattr__(self, ad):
            return getattr(self._asil, ad)

        def arsivden_cikar(self, *a, **kw):
            adim_sirasi.append(("arsiv_sil", len(kw.get("kalan_skiller", ()))))
            return self._asil.arsivden_cikar(*a, **kw)

    os.replace = izle_replace
    ft._modul = lambda ad: _IzleyiciKcik(gercek_modul(ad)) if ad == "kaynak-cikar" else gercek_modul(ad)
    try:
        ft.uygula(kok7i, plan7i)
    finally:
        os.replace = gercek_replace
        ft._modul = gercek_modul

    tmp_kalinti = list(kok7i.rglob("*.tmp"))
    test("7i. Bulgu 4: tüm JSON yazımları atomik os.replace ile önce yapılır, arsivden_cikar en son çağrılır, .tmp kalmaz",
         len(adim_sirasi) >= 4
         and all(tur == "json" for tur, _ in adim_sirasi[:-1])
         and adim_sirasi[-1][0] == "arsiv_sil"
         and adim_sirasi[-1][1] == 3
         and tmp_kalinti == [], (adim_sirasi, tmp_kalinti))

    # JSON yazımında hata olursa hiçbir arşiv klasörü silinmez ve geçici dosya kalmaz
    t7i2, kok7i2 = kur_sahte_kutuphane(git_kur=True)
    try:
        plan7i2 = ft.planla(kok7i2, "dev/kol", arsivde_tut=["skills/kept-role", "skills/kept-proj"])
        once7i2 = agac_ozeti(kok7i2)
        gercek_yaz = ft._atomik_json_toplu_yaz

        def patla(yazilacaklar):
            raise OSError("disk dolu simülasyonu")

        ft._atomik_json_toplu_yaz = patla
        try:
            hata_geldi = False
            try:
                ft.uygula(kok7i2, plan7i2)
            except OSError:
                hata_geldi = True
        finally:
            ft._atomik_json_toplu_yaz = gercek_yaz
        test("7i2. Bulgu 4: JSON yazımı yarıda hata verirse arşiv klasörleri zarar görmez",
             hata_geldi and agac_ozeti(kok7i2) == once7i2 and (kok7i2 / "arsiv" / "cat" / "reviewed" / "SKILL.md").exists())
    finally:
        shutil.rmtree(t7i2, ignore_errors=True)
finally:
    shutil.rmtree(t7i, ignore_errors=True)

# 7j (Bulgu 5): kaynak-cek bolum: fihrist + arsivde_tut boş/yoksa hiçbir skil seçilmez
kayit_bos = {"repo": "dev/kol", "tip": "T1", "bolum": "fihrist", "arsivde_tut": []}
kayit_yok = {"repo": "dev/kol", "tip": "T1", "bolum": "fihrist"}
sec_bos, den_bos = kc.skill_klasorlerini_sec(kayit_bos, agac3, AYAR_BASIT)
sec_yok, den_yok = kc.skill_klasorlerini_sec(kayit_yok, agac3, AYAR_BASIT)
test("7j. Bulgu 5: kaynak-cek bolum fihrist kaydında arsivde_tut boş [] veya yoksa 0 skil seçilir, tümü 'fihristte'",
     sec_bos == {} and sec_yok == {}
     and den_bos == {"skills/a/SKILL.md": "fihristte", "skills/b/SKILL.md": "fihristte", "skills/c/SKILL.md": "fihristte"}
     and den_yok == den_bos, (sec_bos, den_bos, sec_yok, den_yok))

# 7k-7l (Bulgu 6): çok kayıtlı repoda aynı tip farklı dahil/haric kurallarıyla doğru kayda atama + uymayan yol HATA
kay_cok = {
    "repolar": [
        {"repo": "dev/cok", "tur": "koleksiyon", "bolum": "arsiv", "dahil": ["^grup-a/"], "kimlik": "dev-a"},
        {"repo": "dev/cok", "tur": "koleksiyon", "bolum": "arsiv", "dahil": ["^grup-b/"], "haric": ["^grup-b/gizli/"], "kimlik": "dev-b"},
    ]
}
sk_cok = [
    {"id": "sa", "ad": "sa", "repo": "dev/cok", "tip": "T1", "kaynak_yol": "grup-a/sa"},
    {"id": "sb", "ad": "sb", "repo": "dev/cok", "tip": "T1", "kaynak_yol": "grup-b/sb"},
    {"id": "sg", "ad": "sg", "repo": "dev/cok", "tip": "T1", "kaynak_yol": "grup-b/gizli/sg"},
]
guncel_cok = ft.kaynak_kaydini_guncelle(kay_cok, "dev/cok", ["grup-a/sa", "grup-b/sb"], sk_cok)
ka, kb = guncel_cok["repolar"]
agac_cok = [
    {"path": "grup-a/sa/SKILL.md", "type": "blob", "sha": "h1", "size": 10},
    {"path": "grup-b/sb/SKILL.md", "type": "blob", "sha": "h2", "size": 10},
    {"path": "grup-b/diger/SKILL.md", "type": "blob", "sha": "h3", "size": 10},
]
sec_a, _ = kc.skill_klasorlerini_sec(ka, agac_cok, AYAR_BASIT)
sec_b, _ = kc.skill_klasorlerini_sec(kb, agac_cok, AYAR_BASIT)
test("7k. Bulgu 6: aynı tip (T1+T1) farklı dahil kurallı kayıtlarda arsivde_tut doğru kayda atanır ve kaynak-cek seçer",
     ka.get("arsivde_tut") == ["grup-a/sa"] and kb.get("arsivde_tut") == ["grup-b/sb"]
     and list(sec_a) == ["sa"] and list(sec_b) == ["sb"], (ka, kb, sec_a, sec_b))

uymayan_hata = False
try:
    ft.kaynak_kaydini_guncelle(kay_cok, "dev/cok", ["grup-b/gizli/sg"], sk_cok)
except ValueError:
    uymayan_hata = True

t7l, kok7l = kur_sahte_kutuphane(git_kur=False)
try:
    kay7l = json.loads((kok7l / "kaynaklar.json").read_text(encoding="utf-8"))
    for k in kay7l["repolar"]:
        if k["repo"] == "dev/kol":
            k["dahil"] = ["^skills/kept-role/"]
    yaz(kok7l / "kaynaklar.json", kay7l)
    git_temiz_hazirla(kok7l)
    once7l = agac_ozeti(kok7l)
    r7l, out7l, _ = sessiz(ft.main, ["dev/kol", "--evet", "--arsivde-tut", "skills/kept-role,skills/kept-proj"], kok=kok7l)
    test("7l. Bulgu 6: hiçbir kaydın dahil/haric kuralına uymayan arsivde_tut yolu HATA (planla ve kaynak_kaydini_guncelle)",
         uymayan_hata and r7l == 1 and "HATA:" in out7l and "skills/kept-proj" in out7l and "kurallarına uymuyor" in out7l
         and agac_ozeti(kok7l) == once7l, (uymayan_hata, r7l, out7l))
finally:
    shutil.rmtree(t7l, ignore_errors=True)

gecen = sum(1 for _, k in SONUC if k)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
