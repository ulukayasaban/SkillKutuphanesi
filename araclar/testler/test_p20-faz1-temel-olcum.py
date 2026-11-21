#!/usr/bin/env python3
"""P20 testleri: Faz 1 (Temel ve ölçüm) — gecici_tip_senkron, arsive_cekilir, kaynaklar.json senkronu,
dogrula.py (alt_tur, onay.kim: kural, bolum: not, olcum.jsonl), skill-ekle/proje-kullanimi surum_modu
bellek varsayılanı, olcum.py ve ince BASLA.md / AGENTS.md / CLAUDE.md (<= 3 KB).

Ağ kullanmaz, gerçek ev klasörlerine veya 4 projeye yazmaz.
Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse.
"""
import importlib.util
import json
import os
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


ortak = yukle(ARACLAR / "ortak.py", "ortak_p20")
dg = yukle(ARACLAR / "dogrula.py", "dogrula_p20")
ol = yukle(ARACLAR / "olcum.py", "olcum_p20")
se = yukle(ARACLAR / "skill-ekle.py", "skill_ekle_p20")
pk = yukle(ARACLAR / "proje-kullanimi.py", "proje_kullanimi_p20")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def sahte_kok(dosyalar=None):
    k = Path(tempfile.mkdtemp(prefix="p20-"))
    GECICI.append(k)
    for yol, metin in (dosyalar or {}).items():
        f = k / yol
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(metin if isinstance(metin, str) else json.dumps(metin, ensure_ascii=False), encoding="utf-8")
    return k


def git(kok, *a):
    e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
             GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    return subprocess.run(["git", *a], cwd=kok, capture_output=True, text=True, env=e)


# 1. ortak.gecici_tip_senkron
t("1a gecici_tip_senkron: temel türler doğru türetilir",
  ortak.gecici_tip_senkron({"tur": "tek-skil", "tip": "T1"}) == "T1"
  and ortak.gecici_tip_senkron({"tur": "koleksiyon", "tip": "T1"}) == "T1"
  and ortak.gecici_tip_senkron({"tur": "urun-skil", "tip": "T1"}) == "T2"
  and ortak.gecici_tip_senkron({"tur": "repo-ici", "tip": "T3"}) == "T3"
  and ortak.gecici_tip_senkron({"tur": "kendi", "tip": "T7"}) == "T7"
  and ortak.gecici_tip_senkron({"tur": "site", "tip": "T8"}) == "T8"
  and ortak.gecici_tip_senkron({"tur": "kit", "tip": "T1"}) == "T1")
t("1b gecici_tip_senkron: referans alt_tur (kutuphane->T5, tasarim_teknolojisi->T6)",
  ortak.gecici_tip_senkron({"tur": "referans", "alt_tur": "kutuphane", "tip": "T1"}) == "T5"
  and ortak.gecici_tip_senkron({"tur": "referans", "alt_tur": "tasarim_teknolojisi", "tip": "T6"}) == "T6")
t("1c gecici_tip_senkron: KAYIP, EMEKLI, T4 ve program korunur",
  ortak.gecici_tip_senkron({"tur": "tek-skil", "tip": "KAYIP"}) == "KAYIP"
  and ortak.gecici_tip_senkron({"tur": "koleksiyon", "tip": "EMEKLI"}) == "EMEKLI"
  and ortak.gecici_tip_senkron({"tur": "dev-koleksiyon", "tip": "T4"}) == "T4"
  and ortak.gecici_tip_senkron({"tur": "dev-koleksiyon", "tip": "T1"}) == "T1"
  and ortak.gecici_tip_senkron({"tur": "program", "tip": "T5"}) == "T5"
  and ortak.gecici_tip_senkron({"tur": "program", "tip": "T2"}) == "T2")

# 2. ortak.arsive_cekilir
t("2a arsive_cekilir: bolum ana kaynak (arsiv True, katalog/not/bos fihrist False)",
  ortak.arsive_cekilir({"tip": "T1", "bolum": "arsiv"}) is True
  and ortak.arsive_cekilir({"tip": "T1", "bolum": "not"}) is False
  and ortak.arsive_cekilir({"tip": "T1", "bolum": "katalog"}) is False
  and ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist"}) is False
  and ortak.arsive_cekilir({"tip": "T1", "bolum": "fihrist", "arsivde_tut": ["skills/a"]}) is True)
t("2b arsive_cekilir: KAYIP/EMEKLI False, bolum yokken tip yedeği çalışır",
  ortak.arsive_cekilir({"tip": "KAYIP", "bolum": "arsiv"}) is False
  and ortak.arsive_cekilir({"tip": "EMEKLI", "bolum": "arsiv"}) is False
  and ortak.arsive_cekilir({"tip": "T1"}) is True
  and ortak.arsive_cekilir({"tip": "T5"}) is False)

# 3. Gerçek kaynaklar.json (salt okuma) senkron kontrolü
kaynaklar = json.loads((KOK / "kaynaklar.json").read_text(encoding="utf-8"))["repolar"]
eksik_tb = [k.get("repo") for k in kaynaklar if not k.get("tur") or not k.get("bolum")]
eksik_ref = [k.get("repo") for k in kaynaklar if k.get("tur") == "referans" and k.get("alt_tur") not in ortak.REFERANS_ALT_TURLERI]
uyumsuz_tip = [(k.get("repo"), k.get("tip"), ortak.gecici_tip_senkron(k))
               for k in kaynaklar if k.get("tip") != ortak.gecici_tip_senkron(k)]
t("3a gerçek kaynaklar.json: tüm kayıtlarda tur+bolum dolu, referansta alt_tur dolu, tip senkronlu",
  not eksik_tb and not eksik_ref and not uyumsuz_tip, (eksik_tb[:3], eksik_ref[:3], uyumsuz_tip[:3]))

# 4. dogrula.py Faz 1 eklemeleri
t("4a dogrula alt_tur: geçerli referans sessiz, geçersiz değer ve referans dışı tür HATA",
  dg.kaynak_tur_hatalari({"repo": "a/b", "tur": "referans", "bolum": "not", "alt_tur": "kutuphane"}) == []
  and dg.kaynak_tur_hatalari({"repo": "a/b", "tur": "referans", "bolum": "not", "alt_tur": "tasarim_teknolojisi"}) == []
  and any("alt_tur geçersiz" in x for x in dg.kaynak_tur_hatalari({"repo": "a/b", "tur": "referans", "bolum": "not", "alt_tur": "yanlis"}))
  and any("yalnız tur 'referans'" in x for x in dg.kaynak_tur_hatalari({"repo": "a/b", "tur": "kit", "bolum": "katalog", "alt_tur": "kutuphane"})))

if shutil.which("git"):
    legacy = {"repolar": [{"repo": "eski/bir", "tip": "T1", "tur": "tek-skil", "bolum": "arsiv"}]}
    k = sahte_kok({"kaynaklar.json": legacy})
    git(k, "init", "-q")
    git(k, "add", "-A")
    git(k, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "ilk")
    onay_kural = {"kim": "kural", "tarih": "2026-11-21", "commit": "a" * 40}
    yeni = {"repolar": legacy["repolar"] + [
        {"repo": "yeni/kural", "tip": "T5", "tur": "referans", "bolum": "not", "alt_tur": "kutuphane",
         "eklendi": "2026-11-21", "onay": onay_kural}
    ]}
    (k / "kaynaklar.json").write_text(json.dumps(yeni, ensure_ascii=False), encoding="utf-8")
    (k / "araclar").mkdir(exist_ok=True)
    (k / "araclar" / "yol-tara.py").write_text("def kapi_kontrol(r, s, l):\n    return ['sorun'], 1, None\n", encoding="utf-8")
    h, u = dg.kaynak_kapilari_denetimi(k)
    t("4b kaynak_kapilari: onay.kim='kural' kabul edilir ve bolum='not' yol_onay aramaz", h == [] and u == [], (h, u))
    yeni_kotu = {"repolar": legacy["repolar"] + [
        {"repo": "yeni/kim", "tip": "T5", "tur": "referans", "bolum": "not", "alt_tur": "kutuphane",
         "eklendi": "2026-11-21", "onay": {"kim": "yabanci", "tarih": "2026-11-21", "commit": "a" * 40}}
    ]}
    (k / "kaynaklar.json").write_text(json.dumps(yeni_kotu, ensure_ascii=False), encoding="utf-8")
    h, u = dg.kaynak_kapilari_denetimi(k)
    t("4c kaynak_kapilari: bilinmeyen onay.kim UYARI verir", h == [] and any("onay.kim geçersiz" in x for x in u), (h, u))

ko = sahte_kok()
h, u = dg.kayit_semalari_denetimi(ko)
t("4d _e9_olcum: dosya yokken sessiz", h == [] and u == [], (h, u))
iyi_satir = {"tarih": "2026-11-21", "tur": "yeni_repo", "islenen_repo": 1, "sure_sn": 1.2,
             "token_veya_kota": 0, "disk_mb": 10.5, "disk_fark_mb": 0.0, "onay_sayisi": 0, "hata_tekrar": 0}
(ko / "olcum.jsonl").write_text(json.dumps(iyi_satir) + "\n", encoding="utf-8")
t("4e _e9_olcum: geçerli olcum.jsonl sessiz", dg.kayit_semalari_denetimi(ko) == ([], []))
(ko / "olcum.jsonl").write_text(json.dumps({"tarih": "2026-11-21", "tur": "yanlis"}) + "\n", encoding="utf-8")
h, u = dg.kayit_semalari_denetimi(ko)
t("4f _e9_olcum: şema dışı satır UYARI", h == [] and len(u) >= 1, (h, u))
(ko / "olcum.jsonl").write_text("{bozuk\n", encoding="utf-8")
h, u = dg.kayit_semalari_denetimi(ko)
t("4g _e9_olcum: bozuk JSON satırı HATA", len(h) == 1 and "olcum.jsonl:1 okunamadı" in h[0], (h, u))

# 5. skill-ekle & proje-kullanimi surum_modu bellek varsayılanı
kp = sahte_kok()
eski_ham = json.dumps({"surum": 3, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}}, ensure_ascii=False)
kf = kp / ".skill-kutuphanesi" / "kilit.json"
kf.parent.mkdir(parents=True, exist_ok=True)
kf.write_text(eski_ham, encoding="utf-8")
okunan = se.kilit_oku(kp)
t("5a kilit_oku: surum_modu yoksa bellekte 'yalniz_onayli' döner ve diske yazmaz",
  okunan.get("surum_modu") == "yalniz_onayli" and kf.read_text(encoding="utf-8") == eski_ham)
yeni_k = se.kilit_oku(sahte_kok())
t("5b yeni kilit_oku: varsayılan surum_modu='yalniz_onayli'", yeni_k.get("surum_modu") == "yalniz_onayli")
kw = sahte_kok()
se.kilit_yaz(kw, {"surum": 3, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}})
t("5c kilit_yaz + kilit_oku: varsayılan 'yalniz_onayli' diske yazılmaz, kilit_oku bellekte döner",
  "surum_modu" not in json.loads((kw / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))
  and se.kilit_oku(kw).get("surum_modu") == "yalniz_onayli")
se.kilit_yaz(kw, {"surum": 3, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}, "surum_modu": "takip"})
t("5d kilit_yaz: var olan 'takip' modu korunur",
  json.loads((kw / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8")).get("surum_modu") == "takip")
(kw / ".skill-kutuphanesi" / "kilit.json").write_text(
    json.dumps({"surum": 3, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}, "surum_modu": "gecersiz"}),
    encoding="utf-8",
)
rapor_p = pk.proje_denetle(kw, {}, [], lambda: {}, se, "2026-11-21")
t("5e proje_denetle: geçersiz surum_modu dikkat uyarısı üretir",
  any("geçersiz surum_modu" in s for _, s in rapor_p["satirlar"]), rapor_p["satirlar"])

# 6. olcum.py (disk ölçümü, yazıcı, fark, şema reddi, CLI)
kd = sahte_kok()
(kd / "arsiv").mkdir()
(kd / "fihrist").mkdir()
(kd / ".git").mkdir()
(kd / "arsiv" / "a.bin").write_bytes(b"x" * 1024 * 1024)
(kd / "fihrist" / "f.bin").write_bytes(b"y" * 512 * 1024)
os.link(kd / "arsiv" / "a.bin", kd / "arsiv" / "a_link.bin")
(kd / "diger").mkdir()
(kd / "diger" / "b.bin").write_bytes(b"z" * 1024 * 1024)
os.symlink(kd / "diger", kd / "arsiv" / "link_klasor")
t("6a disk_olcum_mb: hardlink çift sayılmaz, symlink izlenmez, dış klasör sayılmaz",
  ol.disk_olcum_mb(kd) == 1.5, ol.disk_olcum_mb(kd))

oj = kd / "olcum.jsonl"
r1 = ol.olcum_yaz(kuru=True, yol=oj, kok=kd, tur="yeni_repo", islenen_repo=1, sure_sn=3.5, token_veya_kota=0, onay_sayisi=0, hata_tekrar=0)
t("6b olcum_yaz --kuru: dosya oluşturmaz", not oj.exists() and r1["disk_fark_mb"] == 0.0)
r1 = ol.olcum_yaz(yol=oj, kok=kd, tur="yeni_repo", islenen_repo=1, sure_sn=3.5, token_veya_kota=0, onay_sayisi=0, hata_tekrar=0)
(kd / "arsiv" / "c.bin").write_bytes(b"c" * 512 * 1024)
r2 = ol.olcum_yaz(yol=oj, kok=kd, tur="aylik_takip", islenen_repo=4, sure_sn=10.0, token_veya_kota=1, onay_sayisi=1, hata_tekrar=0, not_metni="tur2")
t("6c olcum_yaz: 2 satır ve disk_fark_mb doğru (+0.5 MB)",
  len(ol.olcum_oku(oj)) == 2 and r1["disk_fark_mb"] == 0.0 and r2["disk_fark_mb"] == 0.5 and r2["not"] == "tur2", (r1, r2))

hata_yakalandi = False
try:
    ol.olcum_yaz(yol=oj, kok=kd, tur="hatali_tur", islenen_repo=1, sure_sn=1, token_veya_kota=0, onay_sayisi=0, hata_tekrar=0)
except ValueError:
    hata_yakalandi = True
t("6d olcum_yaz: geçersiz şemada ValueError ve yazmaz", hata_yakalandi and len(ol.olcum_oku(oj)) == 2)

rc_dog = subprocess.run([sys.executable, str(ARACLAR / "olcum.py"), "--dosya", str(oj), "--dogrula"], capture_output=True, text=True)
rc_oz = subprocess.run([sys.executable, str(ARACLAR / "olcum.py"), "--dosya", str(oj), "--ozet"], capture_output=True, text=True)
rc_dk = subprocess.run([sys.executable, str(ARACLAR / "olcum.py"), "--kok", str(kd), "--disk"], capture_output=True, text=True)
t("6e olcum.py CLI (--dogrula, --ozet, --disk) çıkış 0",
  rc_dog.returncode == 0 and rc_oz.returncode == 0 and rc_dk.returncode == 0 and "2.00 MB" in rc_dk.stdout,
  (rc_dog.returncode, rc_oz.returncode, rc_dk.stdout))

# 7. Açılış belgeleri (salt okuma)
basla_f, agents_f, claude_f = KOK / "BASLA.md", KOK / "AGENTS.md", KOK / "CLAUDE.md"
arsiv_basla = KOK / "rehber" / "00-basla-ayrintili.md"
basla_txt = basla_f.read_text(encoding="utf-8")
t("7a BASLA.md, AGENTS.md, CLAUDE.md <= 3072 bayt ve eşitlik/işaretçi tam",
  basla_f.stat().st_size <= 3072 and agents_f.stat().st_size <= 3072 and claude_f.stat().st_size <= 3072
  and agents_f.read_bytes() == claude_f.read_bytes()
  and "BASLA.md" in claude_f.read_text(encoding="utf-8").splitlines()[0],
  (basla_f.stat().st_size, agents_f.stat().st_size, claude_f.stat().st_size))
t("7b rehber/00-basla-ayrintili.md mevcut ve BASLA.md surum_modu varsayılanını belgeliyor",
  arsiv_basla.is_file() and arsiv_basla.stat().st_size > 3072
  and "surum_modu" in basla_txt and "yalniz_onayli" in basla_txt)

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
