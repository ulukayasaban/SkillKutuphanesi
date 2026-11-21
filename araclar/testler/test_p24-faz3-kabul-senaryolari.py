#!/usr/bin/env python3
"""P24 testleri: Faz 3a — notlar/yeni-surec-plani.md Bölüm 9.B'deki 14 kabul senaryosunun TAMAMI (çevrimdışı, sahte veri).

Ağ kullanmaz; gerçek kütüphaneye, ev klasörlerine, projelere ve olcum.jsonl dosyasına yazmaz (her şey geçici klasörde).
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
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

SONUC = []
GECICI = []
SHA = "a" * 40


def yukle(dosya, ad):
    spec = importlib.util.spec_from_file_location(ad, ARACLAR / dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ortak = yukle("ortak.py", "ortak_p24")
yr = yukle("yeni-repo.py", "yeni_repo_p24")
kt = yukle("konu-takip.py", "konu_takip_p24")
tor = yukle("toplu-onay-rapor.py", "tor_p24")
ol = yukle("olcum.py", "olcum_p24")
dg = yukle("dogrula.py", "dogrula_p24")
se = yukle("skill-ekle.py", "skill_ekle_p24")
st = yukle("site-takip.py", "site_takip_p24")
ay = yukle("arsiv-yerlestir.py", "arsiv_yerlestir_p24")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def gecici(on="p24-"):
    d = Path(tempfile.mkdtemp(prefix=on))
    GECICI.append(d)
    return d


def blob(yol, size=100):
    return {"path": yol, "type": "blob", "size": size}


def kay(**k):
    """Sahte kaynak kaydı."""
    return k


def git_kok(dal="yeni-surec-faz3", kirli=False):
    k = gecici()
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": []}), encoding="utf-8")
    (k / "registry.json").write_text(json.dumps({"skiller": [{"id": "var-olan", "ad": "var-olan", "repo": "eski/repo"}]}), encoding="utf-8")
    (k / "konu-takip.json").write_text(json.dumps({"degerlendirilen": {}, "konular": {}, "izlenen": {}}), encoding="utf-8")
    (k / "kendi" / "benim-skilim").mkdir(parents=True)
    (k / "kendi" / "benim-skilim" / "SKILL.md").write_text("---\nname: benim-skilim\n---\n", encoding="utf-8")
    e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
             GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    subprocess.run(["git", "init", "-q", "-b", dal], cwd=k, env=e, check=True)
    subprocess.run(["git", "add", "-A"], cwd=k, env=e, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "ilk"], cwd=k, env=e, check=True)
    if kirli:
        (k / "kirli.txt").write_text("x", encoding="utf-8")
    return k


def girdi(repo, aciklama="Bir skill", lisans="MIT", agac=None, icerikler=None, **meta):
    return {"repo": repo, "meta": dict({"aciklama": aciklama, "lisans": lisans, "commit": SHA}, **meta),
            "agac": agac if agac is not None else [blob("SKILL.md")],
            "icerikler": icerikler if icerikler is not None else {"SKILL.md": "---\nname: " + repo.split("/")[1] + "\n---\n"}}


def oku(k, ad):
    return json.loads((k / ad).read_text(encoding="utf-8"))


# ------------------------------------------------------------------ 1. KESİN tek skill: onaysız kayıt + çıkış kapısı + olcum
k1 = git_kok()
uyg = yr.otomatik_isle(k1, [girdi("o/tek-skill")], uygula=True, bugun="2026-11-21")
kayitlar = oku(k1, "kaynaklar.json")["repolar"]
c1 = kayitlar[0] if kayitlar else {}
t("1a KESİN tek skill onaysız (kim=kural) arşive kaydedilir: tur=tek-skil, bolum=arsiv",
  len(kayitlar) == 1 and c1.get("onay", {}).get("kim") == "kural" and c1.get("tur") == "tek-skil" and c1.get("bolum") == "arsiv", kayitlar)
t("1b kayıt dogrula kaynak şemasından geçer (HATA yok) ve arşive çekilir sayılır",
  dg.kaynak_tur_hatalari(c1) == [] and ortak.arsive_cekilir(c1) is True, dg.kaynak_tur_hatalari(c1))
oj1 = k1 / "olcum.jsonl"
ol.olcum_yaz(yol=oj1, kok=k1, tur="yeni_repo", islenen_repo=1, sure_sn=2.0, token_veya_kota=0, onay_sayisi=0, hata_tekrar=0)
t("1c olcum.jsonl satırı (geçici klasörde) yazılır ve şemadan geçer", len(ol.olcum_oku(oj1)) == 1 and ol.dosya_dogrula(oj1) == [])

# ------------------------------------------------------------------ 2. K-58: sorulmadan ret, kayıt yok
k2 = git_kok()
yr.otomatik_isle(k2, [girdi("x/c2", aciklama="Cobalt strike and mimikatz c2 server toolkit")], uygula=True, bugun="2026-11-21")
kt2 = oku(k2, "konu-takip.json")
t("2a K-58 repo onaysız reddedilir: konu-takip.json karar=reddedildi neden=K-58",
  (kt2.get("kuyruk", {}).get("x/c2") or {}).get("durum") == "reddedildi" and (kt2["kuyruk"]["x/c2"]).get("neden") == "K-58", kt2)
t("2b K-58 repo kaynaklar.json'a girmez", oku(k2, "kaynaklar.json")["repolar"] == [])

# ------------------------------------------------------------------ 3. savunma amaçlı güvenlik: riskli sayılmaz
s3 = yr.guvenlik_siniflandir("org/sec-audit", "OWASP hardening, vulnerability scan and dependency check", [blob("SKILL.md")],
                             {"SKILL.md": "---\nname: sec-audit\n---\nRun security audit and secret scan.\n"}, konular=["security", "devsecops"])
k3 = git_kok()
yr.otomatik_isle(k3, [girdi("org/sec-audit", aciklama="OWASP hardening and security audit skill")], uygula=True, bugun="2026-11-21")
t("3 savunma amaçlı güvenlik skili 'temiz' (K-58 değil) ve normal türle kaydedilir",
  s3[0] == "temiz" and [x["repo"] for x in oku(k3, "kaynaklar.json")["repolar"]] == ["org/sec-audit"], (s3, oku(k3, "kaynaklar.json")))

# ------------------------------------------------------------------ 4. ADAY / boş açıklama / CLAUDE.md / gri alan / lisanssız: akış durmaz, tek toplu mesaj
k4 = git_kok()
g4 = [
    girdi("x/lisanssiz", lisans=None),
    girdi("x/bos-aciklama", aciklama=""),
    girdi("x/claude-md", agac=[blob("CLAUDE.md")], icerikler={}),
    girdi("x/gri", aciklama="Local proxy and mitmproxy traffic inspector"),
    girdi("x/urun-aday", agac=[blob("skills/a/SKILL.md"), blob("skills/b/SKILL.md")] + [blob(f"src/m{i}.ts") for i in range(25)],
          icerikler={"skills/a/SKILL.md": "---\nname: ua\n---\n", "skills/b/SKILL.md": "---\nname: ub\n---\n"}),
    girdi("x/normal"),
]
yr.otomatik_isle(k4, g4, uygula=True, bugun="2026-11-21")
kt4 = oku(k4, "konu-takip.json")
nedenler = {v["neden"] for v in kt4["kuyruk"].values() if v["durum"] == "bekliyor"}
oz4 = kt.kuyruk_ozeti(kt4)
t("4a belirsiz repolar kuyruğa 'bekliyor' olarak düşer, normal repo akışı durmadan kaydedilir",
  {"lisans_yok", "aciklama_veya_skill_yok", "gri_guvenlik", "tur_aday"} <= nedenler
  and [x["repo"] for x in oku(k4, "kaynaklar.json")["repolar"]] == ["x/normal"], (nedenler, oku(k4, "kaynaklar.json")))
t("4b kuyruk tek toplu mesajda sunulur (5 bekleyen)", oz4["toplam_bekleyen"] == 5 and "tek toplu onay" in oz4["mesaj"], oz4)

# ------------------------------------------------------------------ 5. dev koleksiyon / kit / program / referans / medya
dev_agac = [blob(f"skills/s{i}/SKILL.md") for i in range(200)]
ref_agac = [blob("README.md"), blob("src/a.py")]
kit_agac = [blob("skills/a/SKILL.md"), blob("skills/b/SKILL.md"), blob("config/x.json")]
kit_ic = {"skills/a/SKILL.md": "---\nname: ka\n---\nBkz ../config/x.json\n", "skills/b/SKILL.md": "---\nname: kb\n---\nBkz ../config/x.json\n"}
medya_agac = [blob("SKILL.md"), blob("demo.mp4", 5 * 1024 * 1024)]
sonuc5 = {}
for repo, ag, ic in (("d/dev", dev_agac, {}), ("r/ref", ref_agac, {}), ("k/kit", kit_agac, kit_ic), ("m/medya", medya_agac, None)):
    g = girdi(repo, agac=ag, icerikler=ic)
    sonuc5[repo] = yr.hafif_kapi_degerlendir(repo, g["meta"], g["agac"], g["icerikler"], {"repolar": []}, {"skiller": []}, bugun="2026-11-21")
dev5 = sonuc5["d/dev"].get("kayit", {})
ref5 = sonuc5["r/ref"].get("kayit", {})
t("5a 200+ SKILL.md dev koleksiyon -> bolum fihrist (arşive çekilmez, arsivde_tut doluysa çekilir)",
  dev5.get("tur") == "dev-koleksiyon" and dev5.get("bolum") == "fihrist" and ortak.arsive_cekilir(dev5) is False
  and ortak.arsive_cekilir(dict(dev5, arsivde_tut=["skills/s1"])) is True, sonuc5["d/dev"])
t("5b SKILL.md'siz referans -> bolum not (alt_tur dolu, arşive çekilmez)",
  ref5.get("tur") == "referans" and ref5.get("bolum") == "not" and ref5.get("alt_tur") in ortak.REFERANS_ALT_TURLERI
  and ortak.arsive_cekilir(ref5) is False, sonuc5["r/ref"])
tb = yukle("tur-belirle.py", "tur_belirle_p24")
kit5 = tb.tur_karari(kit_agac, kit_ic, "MIT")
t("5c kit adayı bolum katalog (kuyruğa ADAY), kit ve program arşive çekilmez",
  kit5["tur"] == "kit" and kit5["bolum"] == "katalog" and sonuc5["k/kit"]["karar"] == "KUYRUK"
  and ortak.arsive_cekilir({"tur": "kit", "bolum": "katalog"}) is False and ortak.arsive_cekilir({"tur": "program", "bolum": "katalog"}) is False, kit5)
m5 = sonuc5["m/medya"].get("kayit", {})
t("5d büyük medya (5 MB mp4) dışlanır: medya_haric + ne_indirir yazılır", "demo.mp4" in (m5.get("medya_haric") or {}) and bool(m5.get("ne_indirir")), sonuc5["m/medya"])

# ------------------------------------------------------------------ 6. ilk kurulum: yalniz_onayli varsayılan, kit betiği çalışmaz
proje6 = gecici("p24-proje-")
kl6 = se.kilit_oku(proje6)
t("6a yeni projede kilit varsayılan surum_modu 'yalniz_onayli' (diske yazılmaz)", kl6.get("surum_modu") == "yalniz_onayli"
  and not (proje6 / ".skill-kutuphanesi" / "kilit.json").exists())
klon6 = gecici("p24-klon-")
(klon6 / "kur.sh").write_text("#!/bin/sh\ntouch /tmp/p24-calisti-mi-OLMAMALI\n", encoding="utf-8")
(klon6 / "README.md").write_text("kit\n", encoding="utf-8")
kit_kaydi = {"repo": "o/kit", "ad": "Kit", "kurulum_betigi": {"var": True, "yol": "kur.sh", "ne_yapar": "x"}, "genel_klasore_yazar": False}
inc6 = se.gecici_kit_incele(klon6, kit_kaydi, proje6, kl6, "iskelet", [], set())
t("6b kit kurulum betiği çalıştırılmaz (yalnız statik okuma; atlanan_adimlar'da raporlanır)",
  any("kurulum betiği çalıştırılmadı" in x for x in inc6["atlanan_adimlar"]) and not Path("/tmp/p24-calisti-mi-OLMAMALI").exists(), inc6["atlanan_adimlar"])

# ------------------------------------------------------------------ 7-9. toplu onay etki raporu (takip / elle / lisans / dondur)
kayit_reg = [
    {"id": "gsap-core", "ad": "gsap-core", "repo": "g/gsap", "kaynak_yol": "skills/gsap-core", "commit": "new1", "klasor_hash": "hn1", "lisans": "MIT", "ucret": "ucretsiz"},
    {"id": "lis", "ad": "lis", "repo": "o/lis", "kaynak_yol": "skills/lis", "commit": "new2", "klasor_hash": "hn2", "lisans": "AGPL-3.0", "ucret": "ucretsiz"},
    {"id": "ucr", "ad": "ucr", "repo": "o/ucr", "kaynak_yol": "skills/ucr", "commit": "new3", "klasor_hash": "hn3", "lisans": "MIT", "ucret": "ucretli"},
]
onceki = [{"id": "lis", "lisans": "MIT", "ucret": "ucretsiz"}, {"id": "ucr", "lisans": "MIT", "ucret": "ucretsiz"}]
sk = lambda i, repo, c="old1": {"id": i, "repo": repo, "commit": c, "klasor_hash": "ho1"}  # noqa: E731
projeler = [
    {"ad": "PA", "yol": "/tmp/pa", "elle_degisenler": {"lis"}, "kilit": {"surum_modu": "takip", "skiller": {"gsap-core": sk("gsap-core", "g/gsap"), "lis": sk("lis", "o/lis")}}},
    {"ad": "PB", "yol": "/tmp/pb", "elle_degisenler": set(), "kilit": {"surum_modu": "takip", "skiller": {"gsap-core": sk("gsap-core", "g/gsap"), "ucr": dict(sk("ucr", "o/ucr"), ucret="ucretsiz")}}},
    {"ad": "PD", "yol": "/tmp/pd", "elle_degisenler": set(), "kilit": {"surum_modu": "dondur", "skiller": {"gsap-core": sk("gsap-core", "g/gsap")}}},
]
s7 = tor.etki_raporu_hesapla(projeler, kayit_reg, onceki_skiller=onceki)
t("7a aynı skill + hedef sürüm 2 takip projesinde tek toplu onay grubunda sunulur",
  len(s7["toplu_gruplar"]) == 1 and s7["toplu_gruplar"][0]["projeler"] == ["PA", "PB"], s7["toplu_gruplar"])
# atomik güncelleme: yedekle -> bozma -> geri yükle (geri alma)
p7 = gecici("p24-proje7-")
(p7 / ".claude" / "skills" / "gsap-core").mkdir(parents=True)
(p7 / ".claude" / "skills" / "gsap-core" / "SKILL.md").write_text("eski\n", encoding="utf-8")
yd7 = se.yedekle(p7, ["gsap-core"], "p24-test")
(p7 / ".claude" / "skills" / "gsap-core" / "SKILL.md").write_text("YARIM\n", encoding="utf-8")
se.geri_yukle(p7, yd7)
t("7b güncelleme öncesi yedek alınır; yarım kalan proje yedekten geri yüklenir (atomik geri alma)",
  (p7 / ".claude" / "skills" / "gsap-core" / "SKILL.md").read_text(encoding="utf-8") == "eski\n" and callable(se.guvenli_islem))
tek8 = {(x["proje"], x["skill_adi"]): x["nedenler"] for x in s7["tekil_onaylar"]}
t("8 elle_degistirildi, lisans ve ücret değişimi toplu gruba girmez, tekil onaya düşer",
  any("elle_degistirildi" in n for n in tek8.get(("PA", "lis"), [])) and any("lisans_degisti" in n for n in tek8.get(("PA", "lis"), []))
  and any("ucret_degisti" in n for n in tek8.get(("PB", "ucr"), [])), tek8)
t("9 dondur projesi etki raporunda ve gruplarında görünmez", "PD" not in json.dumps(s7, ensure_ascii=False) and s7["ozet"]["dondurulan_proje_sayisi"] == 1, s7["ozet"])

# ------------------------------------------------------------------ 10. kesin 404: yerel kopya silinmez, uyarı; site erişilemezse KAYIP sayılmaz
reg10 = [{"id": "k", "ad": "k", "repo": "o/yok", "kaynak_yol": "skills/k", "commit": "c", "klasor_hash": "h", "kaynak_durumu": "kayip"}]
pr10 = [{"ad": "P", "yol": "/tmp/p10", "elle_degisenler": set(), "kilit": {"surum_modu": "takip", "skiller": {"k": sk("k", "o/yok", "c")}}}]
s10 = tor.etki_raporu_hesapla(pr10, reg10)
t("10a kaynak 404 -> uyarı kaydı düşer (kaynak_404), yerel kopya silinmez (rapor salt okuma)",
  len(s10["kaynak_404_uyarilari"]) == 1 and s10["kaynak_404_uyarilari"][0]["durum"] == "kaynak_404", s10["kaynak_404_uyarilari"])
with um.patch.object(st, "getir", return_value={"kod": 404, "govde": b"baska", "konum": None, "hata": "HTTP 404"}):
    r10 = st.dosya_kontrol({"url": "https://ornek.test/x", "sha256": "0" * 64, "tur": "asil"}, 5)
t("10b site 404 verirse ERİŞİLEMEDİ, 'KAYIP sayılmaz' notu", r10["durum"] == "ERİŞİLEMEDİ" and "KAYIP sayılmaz" in r10["not_"], r10)

# ------------------------------------------------------------------ 11. API hız sınırı / zaman aşımı: KAYIP değil, kaldigi_kaynak + yarim_kaldi + devam
ag = yukle("arsiv-guncelle.py", "arsiv_guncelle_p24")


def sahte_kutuphane():
    k = gecici("p24-ag-")
    for d in ("araclar", "notlar", "fihrist"):
        (k / d).mkdir()
    (k / "araclar" / "dogrula.py").write_text("import sys; sys.exit(0)\n", encoding="utf-8")
    (k / ".gitignore").write_text(".gecici/\nnotlar/son-aylik-calisma.json\nnotlar/aylik-ozet.md\n", encoding="utf-8")
    (k / "programlar.json").write_text('{"programlar": {}}\n', encoding="utf-8")
    (k / "fihrist" / "org__dev.json").write_text(json.dumps({"repo": "org/dev", "commit": "c_fih_1"}), encoding="utf-8")
    (k / "registry.json").write_text(json.dumps({"skiller": [{"repo": "org/arsiv", "commit": "c1", "kaynak_yol": "s", "id": "a", "klasor_hash": "h"}]}), encoding="utf-8")
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": [
        kay(repo="org/arsiv", tur="tek-skil", bolum="arsiv"),
        kay(repo="org/dev", tur="dev-koleksiyon", bolum="fihrist"),
        kay(repo="org/ref", tur="referans", bolum="not", alt_tur="kutuphane", son_kontrol={"tarih": "2026-11-01", "commit": "c_ref_1"}),
    ]}), encoding="utf-8")
    return k


def mod_kur(k, harita):
    m = yukle("arsiv-guncelle.py", f"ag_p24_{len(SONUC)}")
    m.KOK, m.GECMIS, m.DAMGA = k, k / "notlar" / "guncelleme-gecmisi.md", k / "notlar" / "son-aylik-calisma.json"
    m.KILIT, m.KAYNAKLAR, m.REGISTRY = k / ".guncelleme-kilidi", k / "kaynaklar.json", k / "registry.json"
    m.gh_hazir = lambda: (True, 5000, "")
    m.etkilenen_projeler = lambda r: {}

    def sahte_gh(yol):
        repo = "/".join(yol.split("/")[1:3])
        v = harita.get(repo)
        if v == "429":
            raise ortak.GhGeciciHata(f"HTTP 429 rate limit: {repo}")
        if v == "timeout":
            raise ortak.GhGeciciHata(f"zaman aşımı: {repo}")
        return v
    m.gh_api = sahte_gh
    return m


k11 = sahte_kutuphane()
m11 = mod_kur(k11, {"org/arsiv": {"sha": "c1"}, "org/dev": "429", "org/ref": "timeout"})
with contextlib.redirect_stdout(io.StringIO()):
    deg11, sor11, _ = m11.rapor(tum_bolumler=True)
t("11a 429/zaman aşımı kaynakları sorunlu/KAYIP sayılmaz; geçici hata ve kaldigi_kaynak kaydedilir",
  sor11 == [] and m11.GECICI_HATA_SAYISI == 2 and m11.KALDIGI_KAYNAK == "org/dev" and "org/dev" in m11.ULASILAMAYAN, (sor11, m11.GECICI_HATA_SAYISI, m11.KALDIGI_KAYNAK))
m11.damga_yaz("kismi", neden="geçici hata", taranan=m11.BOLUM_TARAMA, kaldigi_kaynak=m11.KALDIGI_KAYNAK, gecici_hata_sayisi=m11.GECICI_HATA_SAYISI)
d11 = oku(k11, "notlar/son-aylik-calisma.json")
t("11b damga durum=yarim_kaldi ve kaldigi_kaynak yazılır", d11["durum"] == "yarim_kaldi" and d11["kaldigi_kaynak"] == "org/dev", d11)
m11b = mod_kur(k11, {"org/arsiv": "429", "org/dev": {"sha": "c_fih_1"}, "org/ref": {"sha": "c_ref_1"}})
with contextlib.redirect_stdout(io.StringIO()):
    m11b.rapor(kaldigi_kaynak="org/dev", tum_bolumler=True)
t("11c kontrol noktasından devam: önceki kaynak atlanır, kalanlar temiz taranır",
  m11b.BOLUM_TARAMA["arsiv"] == 0 and m11b.BOLUM_TARAMA["fihrist"] == 1 and m11b.GECICI_HATA_SAYISI == 0, m11b.BOLUM_TARAMA)

# ------------------------------------------------------------------ 12. ad çakışması: eski ad ezilmez, yeni repo kuyruğa
k12 = git_kok()
yr.otomatik_isle(k12, [girdi("x/cakisan-kendi", icerikler={"SKILL.md": "---\nname: benim-skilim\n---\n"}),
                       girdi("x/cakisan-reg", icerikler={"SKILL.md": "---\nname: var-olan\n---\n"})], uygula=True, bugun="2026-11-21")
kt12 = oku(k12, "konu-takip.json")
t("12a mevcut yerel/arşiv skiliyle ad çakışan yeni repolar onaysız girmez, ad_cakismasi kuyruğuna alınır",
  all((kt12["kuyruk"].get(r) or {}).get("neden") == "ad_cakismasi" for r in ("x/cakisan-kendi", "x/cakisan-reg"))
  and oku(k12, "kaynaklar.json")["repolar"] == [], kt12)
kimlik_kayit = lambda repo, kh, yol="skills/x": {"ad": "x", "repo": repo, "kaynak_yol": yol, "_kh": kh, "oncelik": 3}  # noqa: E731
yeni12 = ay.kimlik_ata({"x": [kimlik_kayit("aaa/yeni", "H2"), kimlik_kayit("zzz/eski", "H1")]}, {("zzz/eski", "skills/x"): {"durum": "tercih", "id": "x"}})
d12 = {x["repo"]: x for x in yeni12}
t("12b eski çıplak kimlik korunur; çakışan yeni kayıt ad@kaynak alır (ad ezilmez)",
  d12["zzz/eski"]["id"] == "x" and d12["aaa/yeni"]["id"].startswith("x@") and ay.kimlik_devri(True, True, False) == "korunur", yeni12)

# ------------------------------------------------------------------ 13. kirli ağaç: süreç başlamaz; yarım kalan --geri-al
kk = git_kok(kirli=True)
ok13, neden13 = yr.on_kapi_kontrol(kk)
try:
    yr.otomatik_isle(kk, [girdi("o/yeni")], uygula=True)
    durdu = False
except RuntimeError:
    durdu = True
t("13a kirli çalışma ağacında ön-kapı durdurur, hiçbir kayıt yazılmaz",
  ok13 is False and durdu and oku(kk, "kaynaklar.json")["repolar"] == [], neden13)
p13 = gecici("p24-proje13-")
(p13 / ".claude" / "skills" / "s1").mkdir(parents=True)
(p13 / ".claude" / "skills" / "s1" / "SKILL.md").write_text("tam\n", encoding="utf-8")
y13 = se.yedekle(p13, ["s1"], "p24-geri-al")
(p13 / ".claude" / "skills" / "s1" / "SKILL.md").write_text("YARIM-KALDI\n", encoding="utf-8")
se.geri_yukle(p13, y13)
t("13b yarıda kalan tek proje yedekten geri alınır", (p13 / ".claude" / "skills" / "s1" / "SKILL.md").read_text(encoding="utf-8") == "tam\n")

# ------------------------------------------------------------------ 14. 1 yeni repo + 1 aylık tur: olcum.jsonl 5 metrik
k14 = gecici("p24-olcum-")
(k14 / "arsiv").mkdir()
(k14 / "arsiv" / "a.bin").write_bytes(b"x" * 1024 * 1024)
oj14 = k14 / "olcum.jsonl"
r1 = ol.olcum_yaz(yol=oj14, kok=k14, tur="yeni_repo", islenen_repo=1, sure_sn=3.5, token_veya_kota=0, onay_sayisi=0, hata_tekrar=0)
(k14 / "arsiv" / "b.bin").write_bytes(b"y" * 512 * 1024)
r2 = ol.olcum_yaz(yol=oj14, kok=k14, tur="aylik_takip", islenen_repo=4, sure_sn=10.0, token_veya_kota=1, onay_sayisi=1, hata_tekrar=0)
bes = ("sure_sn", "token_veya_kota", "disk_mb", "onay_sayisi", "hata_tekrar")
t("14a yeni_repo ve aylik_takip satırları 5 metriği taşır (disk farkı dahil)",
  [x["tur"] for x in ol.olcum_oku(oj14)] == ["yeni_repo", "aylik_takip"] and all(a in r1 and a in r2 for a in bes) and r2["disk_fark_mb"] == 0.5, (r1, r2))
t("14b olcum.jsonl dogrula şemasından geçer (0 hata, 0 uyarı); sayısal hedef yazılmaz",
  dg.kayit_semalari_denetimi(k14) == ([], []) and ol.dosya_dogrula(oj14) == [], dg.kayit_semalari_denetimi(k14))

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
