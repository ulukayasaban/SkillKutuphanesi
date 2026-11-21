#!/usr/bin/env python3
"""P23 testleri: Faz 2 Adım 3 — toplu-onay-rapor.py (YALNIZ rapor, salt okuma).

- takip modunda 2+ projede aynı kaynak+skill+hedef_surum -> tek toplu onay grubu
- surum_modu alanı olmayan kilit -> bellekte 'yalniz_onayli' sayılır, diske yazmaz, toplu gruba girmez
- dondur modu -> raporda ve toplu gruplarda görünmez
- elle_degistirildi / lisans değişikliği / ücret değişikliği -> tekil onaya düşer
- kaynak 404 (kayip) -> kaynak_404_uyarilari, yerel kopya korunur

Ağ kullanmaz, gerçek ev/proje klasörlerine yazmaz.
Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse.
"""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

SONUC = []
GECICI = []


def yukle(dosya, ad):
    spec = importlib.util.spec_from_file_location(ad, dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tor = yukle(ARACLAR / "toplu-onay-rapor.py", "tor_p23")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def kilit_dosyasi_yaz(kok, ad, kilit):
    p = kok / ad
    f = p / ".skill-kutuphanesi" / "kilit.json"
    f.parent.mkdir(parents=True, exist_ok=True)
    metin = json.dumps(kilit, ensure_ascii=False, indent=2)
    f.write_text(metin, encoding="utf-8")
    return p, f, metin


registry_skiller = [
    {"id": "gsap-core", "ad": "gsap-core", "repo": "greensock/gsap-skills", "kaynak_yol": "skills/gsap-core",
     "commit": "new_111", "klasor_hash": "h_new_1", "lisans": "MIT", "ucret": "ucretsiz"},
    {"id": "lisans-deg", "ad": "lisans-deg", "repo": "org/lis", "kaynak_yol": "skills/lisans-deg",
     "commit": "new_222", "klasor_hash": "h_new_2", "lisans": "AGPL-3.0", "ucret": "ucretsiz"},
    {"id": "ucret-deg", "ad": "ucret-deg", "repo": "org/ucr", "kaynak_yol": "skills/ucret-deg",
     "commit": "new_333", "klasor_hash": "h_new_3", "lisans": "MIT", "ucret": "ucretli"},
    {"id": "kayip-skil", "ad": "kayip-skil", "repo": "org/yok", "kaynak_yol": "skills/kayip-skil",
     "commit": "old_404", "klasor_hash": "h_old_4", "kaynak_durumu": "kayip"},
]
onceki_skiller = [
    {"id": "lisans-deg", "lisans": "MIT", "ucret": "ucretsiz"},
    {"id": "ucret-deg", "lisans": "MIT", "ucret": "ucretsiz"},
]

projeler = [
    # 1. takip: gsap-core (toplu grup adayı) + elle_degistirildi (tekil)
    {"ad": "ProjeA", "yol": "/tmp/a", "elle_degisenler": {"lisans-deg"}, "kilit": {
        "surum_modu": "takip",
        "skiller": {
            "gsap-core": {"id": "gsap-core", "repo": "greensock/gsap-skills", "commit": "old_1", "klasor_hash": "h_old_1"},
            "lisans-deg": {"id": "lisans-deg", "repo": "org/lis", "commit": "old_2", "klasor_hash": "h_old_2"},
        },
    }},
    # 2. takip: gsap-core (ProjeA ile toplu grup) + ucret-deg (ücret değişti -> tekil) + kayip-skil (404)
    {"ad": "ProjeB", "yol": "/tmp/b", "elle_degisenler": set(), "kilit": {
        "surum_modu": "takip",
        "skiller": {
            "gsap-core": {"id": "gsap-core", "repo": "greensock/gsap-skills", "commit": "old_1", "klasor_hash": "h_old_1"},
            "ucret-deg": {"id": "ucret-deg", "repo": "org/ucr", "commit": "old_3", "klasor_hash": "h_old_3", "ucret": "ucretsiz"},
            "kayip-skil": {"id": "kayip-skil", "repo": "org/yok", "commit": "old_404", "klasor_hash": "h_old_4"},
        },
    }},
    # 3. surum_modu alanı OLMAYAN kilit -> bellekte yalniz_onayli sayılır (toplu gruba girmez!)
    {"ad": "ProjeC_Modsuz", "yol": "/tmp/c", "elle_degisenler": set(), "kilit": {
        "skiller": {
            "gsap-core": {"id": "gsap-core", "repo": "greensock/gsap-skills", "commit": "old_1", "klasor_hash": "h_old_1"},
        },
    }},
    # 4. dondur -> raporda ve toplu gruplarda GÖRÜNMEZ
    {"ad": "ProjeD_Dondur", "yol": "/tmp/d", "elle_degisenler": set(), "kilit": {
        "surum_modu": "dondur",
        "skiller": {
            "gsap-core": {"id": "gsap-core", "repo": "greensock/gsap-skills", "commit": "old_1", "klasor_hash": "h_old_1"},
        },
    }},
]

sonuc = tor.etki_raporu_hesapla(projeler, registry_skiller, onceki_skiller=onceki_skiller)

# 1. Toplu grup doğrulaması
t("1a 2 takip projesi tek toplu grupta birleşir (ProjeA, ProjeB); ProjeC_Modsuz ve ProjeD_Dondur girmez",
  len(sonuc["toplu_gruplar"]) == 1
  and sonuc["toplu_gruplar"][0]["skill_adi"] == "gsap-core"
  and sonuc["toplu_gruplar"][0]["projeler"] == ["ProjeA", "ProjeB"], sonuc["toplu_gruplar"])

# 2. surum_modu alanı olmayan kilit -> yalniz_onayli sayılır (tekil onayda görünür)
modsuz_tekil = [x for x in sonuc["tekil_onaylar"] if x["proje"] == "ProjeC_Modsuz"]
t("2 surum_modu olmayan kilit bellekte yalniz_onayli sayılır ve tekil onaya düşer",
  len(modsuz_tekil) == 1 and modsuz_tekil[0]["surum_modu"] == "yalniz_onayli"
  and "yalniz_onayli" in modsuz_tekil[0]["nedenler"], modsuz_tekil)

# 3. dondur projeler hiç görünmez
tum_rapor_metni = json.dumps(sonuc, ensure_ascii=False)
t("3 dondur modundaki proje etki raporunda görünmez",
  "ProjeD_Dondur" not in tum_rapor_metni and sonuc["ozet"]["dondurulan_proje_sayisi"] == 1, sonuc["ozet"])

# 4. elle_degistirildi + lisans değişimi + ücret değişimi -> tekil onay
lis_tekil = next((x for x in sonuc["tekil_onaylar"] if x["proje"] == "ProjeA" and x["skill_adi"] == "lisans-deg"), None)
ucr_tekil = next((x for x in sonuc["tekil_onaylar"] if x["proje"] == "ProjeB" and x["skill_adi"] == "ucret-deg"), None)
t("4 elle_degistirildi, lisans_degisti ve ucret_degisti tekil onaya düşer",
  lis_tekil is not None
  and any("elle_degistirildi" in n for n in lis_tekil["nedenler"])
  and any("lisans_degisti" in n for n in lis_tekil["nedenler"])
  and ucr_tekil is not None
  and any("ucret_degisti" in n for n in ucr_tekil["nedenler"]), (lis_tekil, ucr_tekil))

# 5. Kaynak 404 uyarısı
t("5 kaynak 404 uyarısı üretilir ve yerel kopya korunur",
  len(sonuc["kaynak_404_uyarilari"]) == 1 and sonuc["kaynak_404_uyarilari"][0]["durum"] == "kaynak_404",
  sonuc["kaynak_404_uyarilari"])

# 6. Gerçek diskte surum_modu olmayan kilit dosyası CLI sonrasında bayt bayt değişmez
tmp = Path(tempfile.mkdtemp(prefix="p23-"))
GECICI.append(tmp)
_, kf, ham_metin = kilit_dosyasi_yaz(tmp, "ProjeDisk", {
    "skiller": {"gsap-core": {"id": "gsap-core", "repo": "greensock/gsap-skills", "commit": "old_1", "klasor_hash": "h_old_1"}}
})
girdi_json = tmp / "girdi.json"
girdi_json.write_text(json.dumps({
    "projeler": [{"ad": "ProjeDisk", "yol": str(tmp / "ProjeDisk"), "kilit": json.loads(ham_metin)}],
    "skiller": registry_skiller,
}), encoding="utf-8")

r_oz = subprocess.run([sys.executable, str(ARACLAR / "toplu-onay-rapor.py"), "--girdi-json", str(girdi_json), "--ozet-json"],
                      capture_output=True, text=True)
r_js = subprocess.run([sys.executable, str(ARACLAR / "toplu-onay-rapor.py"), "--girdi-json", str(girdi_json), "--json"],
                      capture_output=True, text=True)
oz_obj = json.loads(r_oz.stdout.strip()) if r_oz.returncode == 0 and r_oz.stdout.strip() else {}
t("6a CLI (--ozet-json, --json) çıkış 0 ve geçerli sözleşme",
  r_oz.returncode == 0 and r_js.returncode == 0 and oz_obj.get("arac") == "toplu-onay-rapor", (r_oz.stdout, r_js.stderr))
t("6b CLI çalıştıktan sonra kilit.json bayt bayt değişmez (salt okuma)",
  kf.read_text(encoding="utf-8") == ham_metin)

kaynak_kod = (ARACLAR / "toplu-onay-rapor.py").read_text(encoding="utf-8")
t("6c toplu-onay-rapor.py kaynak kodunda hiçbir yazma çağrısı yok",
  "write_text" not in kaynak_kod and "json_yaz" not in kaynak_kod and "kilit_yaz" not in kaynak_kod)

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
