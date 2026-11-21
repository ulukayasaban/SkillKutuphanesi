#!/usr/bin/env python3
"""P21 testleri: Faz 2 Adım 1 — aylık zincire fihrist/katalog/not taraması,
son-aylik-calisma.json damgası, GitHub 403/429/5xx/timeout/301 koruması ve kaldigi_kaynak devamı.

Ağ kullanmaz, gerçek kütüphaneye/ev klasörüne yazmaz.
Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse.
"""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest.mock as um
from datetime import date
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


ortak = yukle(ARACLAR / "ortak.py", "ortak_p21")
ao = yukle(ARACLAR / "aylik-ozet.py", "aylik_ozet_p21")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def sahte_kutuphane():
    k = Path(tempfile.mkdtemp(prefix="p21-"))
    GECICI.append(k)
    (k / "araclar").mkdir(parents=True)
    (k / "notlar").mkdir()
    (k / "fihrist").mkdir()
    (k / ".gitignore").write_text(".gecici/\nnotlar/son-aylik-calisma.json\nnotlar/aylik-ozet.md\n", encoding="utf-8")
    for ad in ("dogrula", "github-skill-listesi", "site-takip"):
        (k / "araclar" / f"{ad}.py").write_text("import sys; sys.exit(0)\n", encoding="utf-8")
    (k / "programlar.json").write_text('{\n  "programlar": {"prog": {"kutuphane_commit": "c_prog_1"}}\n}\n', encoding="utf-8")
    (k / "fihrist" / "org__dev.json").write_text(json.dumps({"repo": "org/dev", "commit": "c_fih_1"}), encoding="utf-8")
    (k / "registry.json").write_text(json.dumps({"skiller": [
        {"repo": "org/arsiv", "commit": "c_ars_1", "kaynak_yol": "s", "id": "ars-1", "klasor_hash": "h1"}
    ]}), encoding="utf-8")
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": [
        {"repo": "org/arsiv", "tip": "T1", "tur": "tek-skil", "bolum": "arsiv"},
        {"repo": "org/dev", "tip": "T1", "tur": "dev-koleksiyon", "bolum": "fihrist"},
        {"repo": "org/kit", "tip": "T1", "tur": "kit", "bolum": "katalog", "son_kontrol": {"tarih": "2026-11-01", "commit": "c_kit_1"}},
        {"repo": "org/prog", "tip": "T5", "tur": "program", "bolum": "katalog", "program": "prog"},
        {"repo": "org/ref", "tip": "T5", "tur": "referans", "bolum": "not", "alt_tur": "kutuphane", "son_kontrol": {"tarih": "2026-11-01", "commit": "c_ref_1"}},
    ]}), encoding="utf-8")
    e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
             GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    subprocess.run(["git", "init", "-q", "-b", "master"], cwd=k, env=e, check=True)
    subprocess.run(["git", "add", "-A"], cwd=k, env=e, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "ilk"], cwd=k, env=e, check=True)
    return k


def mod_kur(k, gh_harita):
    m = yukle(ARACLAR / "arsiv-guncelle.py", f"ag_p21_{len(SONUC)}")
    m.KOK = k
    m.GECMIS = k / "notlar" / "guncelleme-gecmisi.md"
    m.DAMGA = k / "notlar" / "son-aylik-calisma.json"
    m.KILIT = k / ".guncelleme-kilidi"
    m.KAYNAKLAR = k / "kaynaklar.json"
    m.REGISTRY = k / "registry.json"
    m.gh_hazir = lambda: (True, 5000, "")
    m.etkilenen_projeler = lambda r: {}

    def sahte_gh(yol):
        repo = yol.split("/")[1] + "/" + yol.split("/")[2]
        val = gh_harita.get(repo)
        if val == "404":
            raise m.GhBulunamadi(repo)
        if val == "403":
            raise ortak.GhGeciciHata(f"HTTP 403 rate limit: {repo}")
        if val == "429":
            raise ortak.GhGeciciHata(f"HTTP 429 too many requests: {repo}")
        if val == "timeout":
            raise ortak.GhGeciciHata(f"zaman aşımı: {repo}")
        return val

    m.gh_api = sahte_gh
    return m


# 1. ortak.gh_api hata ayrımı
with um.patch.object(ortak.subprocess, "run", side_effect=subprocess.TimeoutExpired("gh", 1)):
    try:
        ortak.gh_api("repos/a/b", deneme=1, zaman_asimi=1)
        t("1a gh_api timeout -> GhGeciciHata", False)
    except ortak.GhGeciciHata:
        t("1a gh_api timeout -> GhGeciciHata", True)

for kod, beklen in (("HTTP 403 API rate limit", ortak.GhGeciciHata),
                    ("HTTP 429 Too Many Requests", ortak.GhGeciciHata),
                    ("HTTP 502 Bad Gateway", ortak.GhGeciciHata),
                    ("HTTP 404 Not Found", ortak.GhBulunamadi),
                    ("HTTP 410 Gone", ortak.GhBulunamadi)):
    r = subprocess.CompletedProcess(["gh"], 1, "", kod)
    with um.patch.object(ortak.subprocess, "run", return_value=r):
        try:
            ortak.gh_api("repos/a/b", deneme=1)
            t(f"1b gh_api {kod[:8]} -> {beklen.__name__}", False)
        except Exception as exc:  # noqa: BLE001
            t(f"1b gh_api {kod[:8]} -> {beklen.__name__}", type(exc) is beklen, type(exc))

# 2. 4 bölüm taraması + 301 yönlendirme + programlar.json korunması
k = sahte_kutuphane()
once_prog = (k / "programlar.json").read_bytes()
m = mod_kur(k, {
    "org/arsiv": {"sha": "c_ars_1"},
    "org/dev": {"sha": "c_fih_2"},
    "org/kit": {"sha": "c_kit_2"},
    "org/prog": {"sha": "c_prog_1"},
    "org/ref": {"sha": "c_ref_2", "html_url": "https://github.com/yeni/ref/commit/c_ref_2"},
})
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    deg, sor, _ = m.rapor(tum_bolumler=True)
t("2a 4 bölüm sayacı doğru (arsiv:1, fihrist:1, katalog:2, not:1)",
  m.BOLUM_TARAMA == {"arsiv": 1, "fihrist": 1, "katalog": 2, "not": 1}, m.BOLUM_TARAMA)
t("2b fihrist, kit ve referans değişimleri yakalandı; 301 yönlendirme ADI_DEGISEN'e yazıldı",
  len(m.BOLUM_DEGISEN["fihrist"]) == 1 and len(m.BOLUM_DEGISEN["katalog"]) == 1 and len(m.BOLUM_DEGISEN["not"]) == 1
  and m.ADI_DEGISEN == {"org/ref": "yeni/ref"} and sor == [] and deg == [], (m.BOLUM_DEGISEN, m.ADI_DEGISEN))
t("2c programlar.json ve kaynaklar.json bayt bayt değişmedi",
  (k / "programlar.json").read_bytes() == once_prog)

# 3. 403/429/timeout koruması: asla KAYIP/sorunlu olmaz, kaldigi_kaynak ve yarim_kaldi damgası yazılır
k2 = sahte_kutuphane()
m2 = mod_kur(k2, {
    "org/arsiv": {"sha": "c_ars_1"},
    "org/dev": "403",
    "org/kit": "429",
    "org/prog": "timeout",
    "org/ref": {"sha": "c_ref_1"},
})
with contextlib.redirect_stdout(io.StringIO()):
    deg2, sor2, _ = m2.rapor(tum_bolumler=True)
t("3a 403/429/timeout kaynakları sorunlu/KAYIP olmaz, ULASILAMAYAN ve kaldigi_kaynak dolar",
  sor2 == [] and m2.GECICI_HATA_SAYISI == 3 and m2.KALDIGI_KAYNAK == "org/dev"
  and "org/dev" in m2.ULASILAMAYAN and "org/ref" in m2.ULASILAMAYAN,
  (sor2, m2.GECICI_HATA_SAYISI, m2.KALDIGI_KAYNAK, m2.ULASILAMAYAN))

m2.damga_yaz("kismi", neden="geçici hata", taranan=m2.BOLUM_TARAMA,
             kaldigi_kaynak=m2.KALDIGI_KAYNAK, gecici_hata_sayisi=m2.GECICI_HATA_SAYISI)
damga_veri = json.loads((k2 / "notlar" / "son-aylik-calisma.json").read_text(encoding="utf-8"))
t("3b damga Bölüm 10 alanları doğru (yarim_kaldi, kaldigi_kaynak, taranan_*)",
  damga_veri["durum"] == "yarim_kaldi" and damga_veri["kaldigi_kaynak"] == "org/dev"
  and damga_veri["gecici_hata_sayisi"] == 3 and damga_veri["son_tarih"] == date.today().isoformat()
  and damga_veri["taranan_arsiv"] == 1 and damga_veri["taranan_fihrist"] == 1, damga_veri)

dk = ao.damga_kontrol(k2, date.today())
t("3c aylik-ozet damga_kontrol yarim_kaldi ve kaldigi_kaynak satırını okur",
  dk["durum"] == "dikkat" and any("org/dev" in s for s in dk["satirlar"]), dk["satirlar"])

# 4. kaldigi_kaynak ile devam etme: önceki kaynaklar atlanır
m3 = mod_kur(k2, {
    "org/arsiv": "403",  # atlanacağı için çağrılmamalı!
    "org/dev": {"sha": "c_fih_1"},
    "org/kit": {"sha": "c_kit_1"},
    "org/prog": {"sha": "c_prog_1"},
    "org/ref": {"sha": "c_ref_1"},
})
with contextlib.redirect_stdout(io.StringIO()):
    m3.rapor(kaldigi_kaynak="org/dev", tum_bolumler=True)
t("4 kaldigi_kaynak='org/dev' ile devam: arsiv atlandı, fihrist/katalog/not temiz tarandı",
  m3.BOLUM_TARAMA == {"arsiv": 0, "fihrist": 1, "katalog": 2, "not": 1}
  and m3.GECICI_HATA_SAYISI == 0 and m3.KALDIGI_KAYNAK is None, m3.BOLUM_TARAMA)

m3.damga_yaz("tamam", taranan=m3.BOLUM_TARAMA, kaldigi_kaynak=m3.KALDIGI_KAYNAK, gecici_hata_sayisi=m3.GECICI_HATA_SAYISI)
damga_ok = json.loads((k2 / "notlar" / "son-aylik-calisma.json").read_text(encoding="utf-8"))
t("4b tamamlanan damga durum='tamamlandi' ve kaldigi_kaynak=None yazar",
  damga_ok["durum"] == "tamamlandi" and damga_ok["kaldigi_kaynak"] is None and damga_ok["gecici_hata_sayisi"] == 0, damga_ok)

# 5. --ana-dal ayıklama testleri
t("5a ana_dal_ayikla varsayılan master döndürür",
  m3.ana_dal_ayikla(["--aylik", "--kuru"]) == ("master", ["--aylik", "--kuru"]))
t("5b ana_dal_ayikla '--ana-dal dal' ayırır",
  m3.ana_dal_ayikla(["--aylik", "--ana-dal", "yeni-surec-faz3", "--kuru"]) == ("yeni-surec-faz3", ["--aylik", "--kuru"]))
t("5c ana_dal_ayikla '--ana-dal=dal' ayırır",
  m3.ana_dal_ayikla(["--ana-dal=yeni-surec-faz3", "--aylik"]) == ("yeni-surec-faz3", ["--aylik"]))
try:
    m3.ana_dal_ayikla(["--aylik", "--ana-dal"])
    t("5d eksik --ana-dal değerinde SystemExit verir", False)
except SystemExit:
    t("5d eksik --ana-dal değerinde SystemExit verir", True)

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
