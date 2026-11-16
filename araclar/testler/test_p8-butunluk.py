#!/usr/bin/env python3
"""P8 testleri: dogrula.py'nin belge ve kayıt denetimleri, ortak.py ek işlevleri, alt test yükleyicisi.

Yalnız geçici klasör ve sahte veri kullanır; gerçek kütüphane dosyalarına ve gerçek ev klasörlerine bakmaz, ağ kullanmaz.
Tek alt süreçler: geçici git deposunda `git` ve geçici ağaca yazılmış küçük sahte araç betikleri.
Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse. test.py'yi çağırmaz.
"""
import ast
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date, timedelta
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


dg = yukle(ARACLAR / "dogrula.py", "dogrula_p8")
ortak = yukle(ARACLAR / "ortak.py", "ortak_p8")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def sahte_kok(**kw):
    """sahte_kok({"a/b.md": "metin"}) -> geçici klasör. Anahtar sözlük olarak verilir (yol/ayrı ad)."""
    k = Path(tempfile.mkdtemp(prefix="p8-"))
    GECICI.append(k)
    return k


def yaz(kok, dosyalar):
    for yol, metin in dosyalar.items():
        f = Path(kok) / yol
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(metin if isinstance(metin, str) else json.dumps(metin, ensure_ascii=False), encoding="utf-8")
    return kok


def kok_yap(dosyalar=None):
    return yaz(sahte_kok(), dosyalar or {})


def git(kok, *a, env=None):
    e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
             GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    e.update(env or {})
    return subprocess.run(["git", *a], cwd=kok, capture_output=True, text=True, env=e)


GIT_VAR = shutil.which("git") is not None
if not GIT_VAR:
    print("  BİLGİ: git yok; git'li durumlar atlandı")

ESIT = "# Başlık\nmetin\n"
KARARLAR = "# K\n## Geçerli kararlar\n## Değişen kararlar\n## Karar bekleyenler\n## Kabul edilen bekleyenler (x)\n"
BASLA_TAM = "Bkz `notlar/kararlar.md` ve DURUM.md.\n"


def var(liste, parca):
    return any(parca in x for x in liste)


# 1-2 eşitlik
k = kok_yap({"CLAUDE.md": ESIT, "AGENTS.md": ESIT})
t("1a eşitlik: aynı dosyalar -> mesaj yok", dg.esitlik_denetimi(k) == ([], []))
yaz(k, {"AGENTS.md": ESIT + " "})
h, u = dg.esitlik_denetimi(k)
t("1b eşitlik: tek bayt farkı -> HATA 'aynı değil'", len(h) == 1 and "aynı değil" in h[0] and u == [], (h, u))
k = kok_yap({"CLAUDE.md": ESIT})
h, u = dg.esitlik_denetimi(k)
t("1c eşitlik: AGENTS.md yok -> HATA 'eksik'", len(h) == 1 and "eksik" in h[0], h)
k = kok_yap({"CLAUDE.md": ESIT, "AGENTS.md": ESIT})
t("2a GEMINI.md yok -> hiçbir şey", dg.esitlik_denetimi(k) == ([], []))
yaz(k, {"GEMINI.md": "bos"})
h, u = dg.esitlik_denetimi(k)
t("2b GEMINI.md BASLA.md'ye işaret etmiyor -> UYARI (HATA değil)", h == [] and var(u, "GEMINI.md"), (h, u))
yaz(k, {"GEMINI.md": "önce BASLA.md oku"})
t("2c GEMINI.md BASLA.md'yi anıyor -> mesaj yok", dg.esitlik_denetimi(k) == ([], []))

# 3-5 giriş belgeleri
k = kok_yap()
h, u = dg.giris_belgeleri_denetimi(k)
t("3a BASLA.md ve kararlar.md yok -> iki UYARI, HATA yok", h == [] and sorted(u) == ["BASLA.md yok", "notlar/kararlar.md yok"], (h, u))
k = kok_yap({"BASLA.md": BASLA_TAM, "notlar/kararlar.md": KARARLAR, "CLAUDE.md": "> BASLA.md oku\n# x\n"})
t("3b her şey var -> mesaj yok", dg.giris_belgeleri_denetimi(k) == ([], []), dg.giris_belgeleri_denetimi(k))
for eksik in ("## Karar bekleyenler", "## Kabul edilen bekleyenler (x)"):
    yaz(k, {"notlar/kararlar.md": KARARLAR.replace(eksik, "## Baska")})
    h, u = dg.giris_belgeleri_denetimi(k)
    t(f"3c kararlar.md'de '{eksik[:25]}' başlığı yok -> UYARI", h == [] and var(u, eksik.split(" (")[0]), (h, u))
yaz(k, {"notlar/kararlar.md": KARARLAR})
yaz(k, {"CLAUDE.md": "# x\nBASLA.md ikinci satırda\n"})
h, u = dg.giris_belgeleri_denetimi(k)
t("4a CLAUDE.md ilk satırı BASLA.md'siz -> UYARI", h == [] and var(u, "ilk satırı"), (h, u))
yaz(k, {"CLAUDE.md": "> BASLA.md\n"})
t("4b ilk satırda BASLA.md -> mesaj yok", dg.giris_belgeleri_denetimi(k) == ([], []))
yaz(k, {"BASLA.md": BASLA_TAM + "`araclar/yok.py` ve `rehber/var.md`\n", "rehber/var.md": "x"})
h, u = dg.giris_belgeleri_denetimi(k)
t("5 BASLA.md olmayan dosyayı anıyor -> yalnız o UYARI, var olan sessiz",
   h == [] and len(u) == 1 and "araclar/yok.py" in u[0], (h, u))
yaz(k, {"BASLA.md": "hiçbir şey anmıyor"})
t("5b BASLA.md kararlar.md ve DURUM.md'yi anmıyor -> iki UYARI", len(dg.giris_belgeleri_denetimi(k)[1]) == 2)

# 6 paket dosyaları
k = kok_yap()
h, u = dg.paket_dosyalari_denetimi(k)
t("6a boş ağaç: her paket dosyası UYARI, HATA yok",
   h == [] and all(var(u, y) for y, _p in dg.PAKET_DOSYALARI) and var(u, ".gitignore"), (h, u[:3]))
t("6b rehber/12 eksikliği UYARI'dır (HATA değil)", var(u, "rehber/12-genel-klasor-bosaltma.md") and h == [])
t("6c notlar/genel-klasor-tabani.json yokluğu uyarı üretmez (yalnız boşaltma gününde yazılır)", not var(u, "genel-klasor-tabani"), u)
yaz(k, {"rehber/13-yedek-ve-geri-alma.md": "git revert -m 1 gh auth login git bundle create yedekler.json"})
u = dg.paket_dosyalari_denetimi(k)[1]
t("6d rehber/13'te 'rehber/12' yok -> UYARI (eksik dizgi adıyla)", any(x.startswith("rehber/13-yedek-ve-geri-alma.md eksik içerik") and x.endswith("rehber/12") for x in u), u)
yaz(k, {"rehber/13-yedek-ve-geri-alma.md": "git revert -m 1 gh auth login git bundle create yedekler.json rehber/12"})
u = dg.paket_dosyalari_denetimi(k)[1]
t("6e rehber/13 beş dizgiyle tam -> o UYARI yok", not any("rehber/13-yedek-ve-geri-alma.md eksik" in x for x in u), u)
tam = "\n".join(dg.GITIGNORE_KALIPLARI) + "\n"
yaz(k, {".gitignore": tam})
t("6f .gitignore tam -> .gitignore UYARISI yok", not var(dg.paket_dosyalari_denetimi(k)[1], ".gitignore"))
for eksik in ("/notlar/son-aylik-calisma.json", "/notlar/aylik-ozet.md"):
    yaz(k, {".gitignore": tam.replace(eksik, "")})
    t(f"6g .gitignore'da {eksik} yok -> UYARI", var(dg.paket_dosyalari_denetimi(k)[1], eksik))
yaz(k, {".gitignore": "", "notlar/kararlar.md": KARARLAR + "\n.gitignore değişikliği reddedildi\n"})
t("6h kararlar.md '.gitignore değişikliği reddedildi' diyorsa .gitignore denetimi atlanır", not var(dg.paket_dosyalari_denetimi(k)[1], ".gitignore'da"))

# 7 E1 programlar.json
SEMA_TAM = ("import json\nHAYIR = '\"--sema\"'\nprint(json.dumps({'arac': 'program-denetim', 'durum': 'sorun', "
            "'satirlar': ['HATA: kart bozuk', 'UYARI: eksik alan', 'bilgi satiri'], 'karar_bekleyen': []}))\n")
k = kok_yap({"programlar.json": "{bozuk"})
h, u = dg.kayit_semalari_denetimi(k)
t("7a programlar.json ayrışmıyor -> HATA", len(h) == 1 and "programlar.json okunamadı" in h[0], (h, u))
k = kok_yap({"programlar.json": {"x": 1}})
h, u = dg.kayit_semalari_denetimi(k)
t("7b geçerli ama 'programlar' sözlüğü yok -> UYARI", h == [] and var(u, "programlar"), (h, u))
k = kok_yap({"programlar.json": {"programlar": {"a": {}}}})
t("7c program-denetim.py yoksa şema alt süreci çalışmaz (UYARI da yok)", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"araclar/program-denetim.py": SEMA_TAM})
h, u = dg.kayit_semalari_denetimi(k)
t("7d sahte program-denetim: HATA ve UYARI satırları UYARI olur, bilgi satırı sayılmaz",
   h == [] and sorted(u) == ["programlar.json kart şeması: HATA: kart bozuk", "programlar.json kart şeması: UYARI: eksik alan"], (h, u))
yaz(k, {"araclar/program-denetim.py": "# \"--sema\"\nprint('saçma')\n"})
h, u = dg.kayit_semalari_denetimi(k)
t("7e çıktı JSON değil -> UYARI 'çalışmadı'", h == [] and var(u, "çalışmadı"), (h, u))
yaz(k, {"araclar/program-denetim.py": "# \"--sema\"\nimport sys\nsys.exit(3)\n"})
h, u = dg.kayit_semalari_denetimi(k)
t("7f çıkış kodu 3 -> UYARI 'çalışmadı'", h == [] and var(u, "çalışmadı"), (h, u))
yaz(k, {"araclar/program-denetim.py": "raise SystemExit('çalıştırıldı')\n"})
t("7g kaynakta '--sema' yoksa araç hiç çalıştırılmaz", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"programlar.json": {"programlar": {"hf": {"giris_yolu": {"araclar": {"claude-code": {}, "yok-arac": {}}}}}},
        "araclar/program-denetim.py": "# x\n"})
t("7h araç kaydı dosyası yoksa giris_yolu çapraz denetimi atlanır", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"yapay-zeka-araclari.json": {"araclar": [{"anahtar": z} for z in dg.ZORUNLU_ARACLAR]}})
h, u = dg.kayit_semalari_denetimi(k)
t("7i giris_yolu araç anahtarı tanımsız -> UYARI", h == [] and var(u, "program hf: giris_yolu araç anahtarı yok: yok-arac") and not var(u, "claude-code: "), (h, u))

# 8 E2 projeler.json
k = kok_yap({"projeler.json": {"tarama_kokleri": "bir-dize", "ek_projeler": [], "notlar": {}}})
h, u = dg.kayit_semalari_denetimi(k)
t("8a tarama_kokleri metin -> UYARI, HATA yok", h == [] and var(u, "tarama_kokleri"), (h, u))
yaz(k, {"projeler.json": {"tarama_kokleri": [], "yoksay": [{"neden": "x"}]}})
t("8b yoksay kaydında yol yok -> UYARI", var(dg.kayit_semalari_denetimi(k)[1], "yoksay"))
yaz(k, {"projeler.json": {"tarama_kokleri": ["/yok/olan/kok-p8"]}})
t("8c olmayan tarama kökü -> UYARI", var(dg.kayit_semalari_denetimi(k)[1], "tarama kökü"))
yaz(k, {"projeler.json": {"tarama_kokleri": [str(k)], "yoksay": [{"yol": "/a/b", "neden": "n"}], "bilinen_projeler": {}}})
t("8d geçerli projeler.json -> mesaj yok", dg.kayit_semalari_denetimi(k) == ([], []), dg.kayit_semalari_denetimi(k))
yaz(k, {"projeler.json": "{x"})
h, u = dg.kayit_semalari_denetimi(k)
t("8e projeler.json ayrışmıyor -> HATA", len(h) == 1 and "projeler.json okunamadı" in h[0])

# 9 E3 yedekler.json
def yedek(**ek):
    r = {"kimlik": "a", "yol": "/x", "tur": "diger", "ne": "n", "tarih": "2026-11-11", "geri_yukleme": "g", "gizli_icerir": "hayir"}
    r.update(ek)
    return r


k = kok_yap({"yedekler.json": {"surum": 1, "yedekler": [yedek()]}, "araclar/yedek-denetim.py": "TURLER = ('diger', 'program')\n"})
t("9a geçerli yedekler.json -> mesaj yok", dg.kayit_semalari_denetimi(k) == ([], []), dg.kayit_semalari_denetimi(k))
for ad, d, parca in (("kimlik tekrarı", {"surum": 1, "yedekler": [yedek(), yedek()]}, "kimlik tekrarlanıyor"),
                     ("gizli_icerir belki", {"surum": 1, "yedekler": [yedek(gizli_icerir="belki")]}, "gizli_icerir"),
                     ("surum 2", {"surum": 2, "yedekler": [yedek()]}, "surum"),
                     ("eksik alan", {"surum": 1, "yedekler": [{"kimlik": "z"}]}, "eksik alan"),
                     ("geçersiz tür", {"surum": 1, "yedekler": [yedek(tur="uzay")]}, "tür geçersiz")):
    yaz(k, {"yedekler.json": d})
    h, u = dg.kayit_semalari_denetimi(k)
    t(f"9b yedekler.json {ad} -> UYARI, HATA yok", h == [] and var(u, parca), (h, u))
(k / "araclar" / "yedek-denetim.py").unlink()
yaz(k, {"yedekler.json": {"surum": 1, "yedekler": [yedek(tur="uzay")]}})
t("9c yedek-denetim.py yoksa tür denetimi atlanır", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"yedekler.json": "[bozuk"})
t("9d yedekler.json ayrışmıyor -> HATA", len(dg.kayit_semalari_denetimi(k)[0]) == 1)

# 10 E4 yapay-zeka-araclari.json
def arac(a, tarih=None, **ek):
    r = {"anahtar": a, "ad": a, "kurulu": True, "proje_skill_okur": [".agents/skills"], "dogrulama_tarihi": tarih or "2026-11-11", "surumler": {}}
    r.update(ek)
    return r


bes = list(dg.ZORUNLU_ARACLAR)
k = kok_yap({"yapay-zeka-araclari.json": {"surum": 1, "araclar": [arac(a) for a in bes]}})
t("10a gerçek biçim (liste) ve beş araç -> mesaj yok", dg.kayit_semalari_denetimi(k) == ([], []), dg.kayit_semalari_denetimi(k))
yaz(k, {"yapay-zeka-araclari.json": {"araclar": [arac(a) for a in bes if a != "vscode-copilot"]}})
t("10b vscode-copilot yok -> UYARI 'araç kaydı yok'", var(dg.kayit_semalari_denetimi(k)[1], "araç kaydı yok: vscode-copilot"))
r = arac("codex"); del r["dogrulama_tarihi"]
yaz(k, {"yapay-zeka-araclari.json": {"araclar": [arac(a) for a in bes if a != "codex"] + [r]}})
t("10c kayıtta dogrulama_tarihi yok -> UYARI", var(dg.kayit_semalari_denetimi(k)[1], "eksik alan: dogrulama_tarihi"))
yaz(k, {"yapay-zeka-araclari.json": {"araclar": [arac(a, "dün" if a == "codex" else None) for a in bes]}})
t("10d dogrulama_tarihi 'dün' -> UYARI", var(dg.kayit_semalari_denetimi(k)[1], "AAAA-AA-GG"))
eski = (date.today() - timedelta(days=200)).isoformat()
yaz(k, {"yapay-zeka-araclari.json": {"araclar": [arac(a, eski) for a in bes]}})
t("10e 200 günlük tarih -> mesaj YOK (bayatlık dogrula'nın işi değil)", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"yapay-zeka-araclari.json": {"araclar": {a: arac(a) for a in bes}}})
t("10f sözlük biçimi de kabul edilir", dg.kayit_semalari_denetimi(k) == ([], []))
t("10g arac_anahtarlari liste ve sözlükten aynı kümeyi verir", dg.arac_anahtarlari(k) == set(bes))
yaz(k, {"yapay-zeka-araclari.json": "{x"})
t("10h bozuk JSON -> HATA; anahtar kümesi boş", len(dg.kayit_semalari_denetimi(k)[0]) == 1 and dg.arac_anahtarlari(k) == set())

# 11 E5
k = kok_yap({"notlar/genel-klasor-tabani.json": {"surum": 2}})
h, u = dg.kayit_semalari_denetimi(k)
t("11a taban surum 2 -> UYARI", h == [] and var(u, "surum"), (h, u))
yaz(k, {"notlar/genel-klasor-tabani.json": {"surum": 1, "yazildi": "2026-09-01"}})
t("11b 60+ günlük taban -> mesaj yok", dg.kayit_semalari_denetimi(k) == ([], []))

# 12 E6 kaynaklar.json
def kaynak(repo="a/b", tip="T1", **ek):
    r = {"repo": repo, "tip": tip}
    r.update(ek)
    return r


k = kok_yap({"kaynaklar.json": {"repolar": [kaynak(tip="EMEKLI"), kaynak("c/d", "KAYIP", kayip_tarihi="2026-11-10", oncelik=3, **{"not": "x"})]}})
t("12a EMEKLI ve KAYIP(kayip_tarihi) geçerli -> mesaj yok", dg.kayit_semalari_denetimi(k) == ([], []), dg.kayit_semalari_denetimi(k))
tum = {"repolar": [kaynak("a/b", "X9"), kaynak("c/d", oncelik="yüksek"), kaynak("e/f", bilinmeyen=1), kaynak("g/h"),
                   kaynak("G/H"), kaynak("yok-bölü"), "dize"]}
yaz(k, {"kaynaklar.json": tum})
h, u = dg.kayit_semalari_denetimi(k)
t("12b bilinmeyen tip, metin öncelik, yabancı anahtar, harf farklı kopya, bölüsüz ad, kayıt dize -> hepsi UYARI, HATA yok",
   h == [] and var(u, "tip bilinmiyor") and var(u, "oncelik") and var(u, "bilinmeyen anahtar") and var(u, "tekrarlanıyor")
   and var(u, "sahip/ad") and var(u, "sözlük değil"), (h, u))
yaz(k, {"kaynaklar.json": {"repolar": [kaynak("v/n", "T2", dahil=["^a/"]), kaynak("v/n", "T5", kimlik="n-kutuphane")]}})
t("12c aynı repo farklı tip/kimlikle (T2 + T5) kopya sayılmaz", dg.kayit_semalari_denetimi(k) == ([], []))
yaz(k, {"kaynaklar.json": {"repolar": "liste değil"}})
t("12d 'repolar' liste değil -> UYARI", var(dg.kayit_semalari_denetimi(k)[1], "repolar"))

# 13 K kapıları
LEGACY = {"repolar": [kaynak("eski/bir"), kaynak("eski/iki", "T2", eski_adlar=["eski/adi"])], "arsivden_cikarilanlar": [],
          "arsivden_cikarilan_repolar": []}
ONAY = {"kim": "kullanıcı", "tarih": "2026-11-11", "commit": "a" * 40}


def git_kok(simdi=None, ekstra=None):
    k = kok_yap({"kaynaklar.json": LEGACY})
    git(k, "init", "-q")
    git(k, "add", "-A")
    git(k, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "ilk")
    if simdi is not None:
        yaz(k, {"kaynaklar.json": simdi})
    yaz(k, ekstra or {})
    return k


def kap(k, skiller=None):
    return dg.kaynak_kapilari_denetimi(k, skiller)


if GIT_VAR:
    k = git_kok()
    t("13a eski kayıtlar (değişmemiş) -> mesaj yok", kap(k) == ([], []), kap(k))
    yeni = dict(LEGACY, repolar=LEGACY["repolar"] + [kaynak("yeni/kayit", "T1")])
    k = git_kok(yeni)
    h, u = kap(k)
    t("13b onaysız yeni kayıt -> tam bir G-ONAY UYARISI, HATA yok", h == [] and len(u) == 1 and "kaynak kaydında onay yok: yeni/kayit" in u[0], (h, u))
    yeni = dict(LEGACY, repolar=LEGACY["repolar"] + [kaynak("yeni/kayit", "T1", eklendi="2026-11-11", onay=ONAY)])
    k = git_kok(yeni)
    t("13c onaylı yeni kayıt -> mesaj yok", kap(k) == ([], []), kap(k))
    yeni = dict(LEGACY, repolar=[kaynak("eski/bir"), kaynak("yeni/ad", "T2", eski_adlar=["eski/iki"])])
    k = git_kok(yeni)
    t("13d yeniden adlandırılan kayıt (eski ad eski_adlar'da) yeni sayılmaz", kap(k) == ([], []), kap(k))
    yeni = dict(LEGACY, repolar=[kaynak("ESKI/BIR"), kaynak("eski/iki", "T2", eski_adlar=["eski/adi"])])
    k = git_kok(yeni)
    t("13e harf büyüklüğü farkı yeni kayıt sayılmaz", kap(k) == ([], []), kap(k))
    yeni = dict(LEGACY, arsivden_cikarilanlar=[{"repo": "x/y", "neden": "ok"}],
                arsivden_cikarilan_repolar=[{"repo": "z/w", "neden": "<NEDEN>", "onay": {"kim": "k", "tarih": "2026-11-11"}, "geri_alma": "g"}])
    k = git_kok(yeni)
    h, u = kap(k)
    t("13f yeni çıkarma kayıtları: onaysız ve '<NEDEN' taşıyan -> iki UYARI", h == [] and len(u) == 2, (h, u))
    yeni = dict(LEGACY, arsivden_cikarilan_repolar=[{"repo": "z/w", "neden": "n", "onay": {"kim": "k", "tarih": "2026-11-11"}, "geri_alma": "g"}])
    t("13g tam çıkarma kaydı -> mesaj yok", kap(git_kok(yeni)) == ([], []))
    yeni = dict(LEGACY, arsivden_cikarilan_repolar=[{"repo": "z/w", "neden": "n", "onay": {"kim": "k", "tarih": "2026-11-11"}}])
    t("13h geri_alma'sız çıkarılan repo kaydı -> UYARI", len(kap(git_kok(yeni))[1]) == 1)
    # sahte kapılar
    yeni = dict(LEGACY, repolar=LEGACY["repolar"] + [kaynak("yeni/kayit", "T1", eklendi="2026-11-11", onay=dict(ONAY))])
    sk = [{"repo": "yeni/kayit", "lisans": "AGPL-3.0"}]
    k = git_kok(yeni, {"araclar/kaynak-cek.py": "def lisans_riskli(l):\n    return True\n"})
    h, u = kap(k, sk)
    t("13i riskli lisans, lisans_onay boş -> UYARI", h == [] and len(u) == 1 and "AGPL-3.0" in u[0] and "lisans_onay" in u[0], (h, u))
    yeni2 = dict(LEGACY, repolar=LEGACY["repolar"] + [kaynak("yeni/kayit", "T1", eklendi="2026-11-11", onay=dict(ONAY, lisans_onay="kullanıcı evet dedi"))])
    k = git_kok(yeni2, {"araclar/kaynak-cek.py": "def lisans_riskli(l):\n    return True\n"})
    t("13j lisans_onay dolu -> mesaj yok", kap(k, sk) == ([], []), kap(k, sk))
    k = git_kok(yeni, {"araclar/yol-tara.py": "def kapi_kontrol(repo, skill_id, skiller):\n    raise RuntimeError('x')\n"})
    h, u = kap(k)
    t("13k yol kapısı çöker -> UYARI 'çalışmadı'", h == [] and len(u) == 1 and "yol kapısı çalışmadı: yeni/kayit" in u[0], (h, u))
    k = git_kok(yeni, {"araclar/yol-tara.py": "def kapi_kontrol(repo, skill_id, skiller):\n    return ['ilk sorun', 'ikinci'], 3, None\n"})
    h, u = kap(k)
    t("13l yol kapısı takıldı, yol_onay boş -> UYARI (ilk sorun gösterilir)", h == [] and len(u) == 1 and "yol kapısı takıldı: yeni/kayit: ilk sorun" in u[0], (h, u))
    yeni3 = dict(LEGACY, repolar=LEGACY["repolar"] + [kaynak("yeni/kayit", "T1", eklendi="2026-11-11", onay=dict(ONAY, yol_onay="kullanıcı evet"))])
    k = git_kok(yeni3, {"araclar/yol-tara.py": "def kapi_kontrol(repo, skill_id, skiller):\n    return ['ilk sorun'], 3, None\n"})
    t("13m yol_onay dolu -> mesaj yok", kap(k) == ([], []))
    k = git_kok(yeni, {"araclar/yol-tara.py": "def kapi_kontrol(repo, skill_id, skiller):\n    return [], 0, 'hedef yok'\n"})
    t("13n yol kapısı hata döndürür -> UYARI 'çalışmadı'", var(kap(k)[1], "yol kapısı çalışmadı"))
    # git yok / HEAD yok: kapılar sessiz
    k = kok_yap({"kaynaklar.json": yeni})
    t("13o git deposu yoksa yeni-kayıt kapıları sessiz", kap(k) == ([], []), kap(k))
# KAYIP: git gerektirmez
k = kok_yap({"kaynaklar.json": {"repolar": [kaynak("a/b", "KAYIP")]}})
t("13p KAYIP kaydında kayip_tarihi yok -> UYARI (git olmadan da)", len(kap(k)[1]) == 1 and "kayip_tarihi" in kap(k)[1][0])
yaz(k, {"kaynaklar.json": {"repolar": [kaynak("a/b", "KAYIP", kayip_tarihi="2026-11-10")]}})
t("13q kayip_tarihi var -> mesaj yok", kap(k) == ([], []))
t("13r kaynaklar.json hiç yoksa kapılar sessiz", kap(kok_yap()) == ([], []))

# 14-18 bayrak denetimi
ARAC_A = "import sys\nap.add_argument('--var')\nif \"--eski\" in sys.argv: pass\nx = sys.argv.index(\"--uygula\")\n"
k = kok_yap({"araclar/a.py": ARAC_A, "README.md": "`python3 araclar/a.py --var --yok`\n"})
h, u = dg.bayrak_denetimi(k)
t("14 var, eski ve index bayrakları geçerli; yalnız --yok UYARI", h == [] and len(u) == 1 and "'--yok'" in u[0] and "README.md:1" in u[0], (h, u))
yaz(k, {"README.md": "`python3 araclar/a.py --var --eski --uygula --help`\n"})
t("14b --eski, --uygula (sys.argv.index) ve --help kabul", dg.bayrak_denetimi(k) == ([], []), dg.bayrak_denetimi(k))
yaz(k, {"BASLA.md": "`python3 araclar/a.py \\\n   --var --devam-yok`\n"})
h, u = dg.bayrak_denetimi(k)
t("15 ters bölülü satır birleştirilir; devam satırındaki bayrak denetlenir, satır no ilk satır",
   len(u) == 1 and "--devam-yok" in u[0] and "BASLA.md:1" in u[0], u)
yaz(k, {"BASLA.md": "`git status --porcelain` ve `python3 araclar/a.py --var` ayrı: `gh --bilinmeyen`\n"})
t("16 başka komutların bayrağı ve ayrı backtick bölümü atfedilmez", dg.bayrak_denetimi(k) == ([], []), dg.bayrak_denetimi(k))
yaz(k, {"BASLA.md": "`python3 araclar/yok.py --x`\n"})
h, u = dg.bayrak_denetimi(k)
t("17a olmayan araç -> UYARI 'olmayan araç'", len(u) == 1 and "olmayan araç araclar/yok.py" in u[0], u)
yaz(k, {"araclar/aylik-ozet.py": "ap.add_argument(\"--hizli\")\n", "BASLA.md": "`python3 araclar/aylik-ozet.py --hizli`\n", "README.md": "`python3 araclar/aylik-ozet.py --oturum`\n"})
h, u = dg.bayrak_denetimi(k)
t("17b --hizli geçerli, --oturum (sahte araçta yok) bildirilir", len(u) == 1 and "'--oturum'" in u[0], u)
yaz(k, {"README.md": "x", "BASLA.md": "`python3 araclar/tehlike.py --hicbir`\n", "araclar/tehlike.py": "raise SystemExit('çalıştırıldı')\n"})
try:
    h, u = dg.bayrak_denetimi(k)
    t("18 araç asla çalıştırılmaz (kaynak metni okunur); yalnız bayrak UYARISI", len(u) == 1 and "'--hicbir'" in u[0], u)
except BaseException as e:  # noqa: BLE001
    t("18 araç asla çalıştırılmaz", False, repr(e))
yaz(k, {"araclar/dok.py": '"""Kullanım: python3 araclar/dok.py [--repo owner/ad]"""\nimport sys\n', "BASLA.md": "`python3 araclar/dok.py --repo x/y`\n"})
t("18b aracın dosya başı açıklamasında yazılı bayrak da geçerli sayılır", dg.bayrak_denetimi(k) == ([], []), dg.bayrak_denetimi(k))
yaz(k, {"BASLA.md": "`python3 araclar/testler/test_p8.py`\n"})
t("18c araclar/testler/... yolu araç sayılmaz", dg.bayrak_denetimi(k) == ([], []))

# 19 eski anlatım
k = kok_yap({"README.md": "- Global skill klasörlerin (...) **değişmez**;\neski agent'ların onlarla çalışmaya devam eder.\n",
             "rehber/01-x.md": "Global klasörler hiçbir zaman değişmez; araç reddeder.\n"})
h, u = dg.eski_anlatim_denetimi(k)
t("19a iki eski cümle -> iki UYARI; yanlış alarm koruması (rehber/01 tarzı cümle) sessiz",
   h == [] and len(u) == 2 and all(x.startswith("README.md:") for x in u), (h, u))
yaz(k, {"README.md": "Kütüphane araçları genel klasörlere yazmaz.\n"})
t("19b düzeltilmiş cümle -> mesaj yok", dg.eski_anlatim_denetimi(k) == ([], []))

# 20 birleştirme kuralı: her şey bozukken HATA yok
k = kok_yap({"CLAUDE.md": ESIT, "AGENTS.md": ESIT, "kaynaklar.json": {"repolar": [kaynak("x/y", "X9", oncelik="a"), kaynak("kayip/k", "KAYIP")]},
             "yedekler.json": {"surum": 9, "yedekler": [{"kimlik": "a"}, {"kimlik": "a"}]}, "projeler.json": {"tarama_kokleri": "x"},
             "yapay-zeka-araclari.json": {"araclar": [{"anahtar": "codex", "dogrulama_tarihi": "dün"}]},
             "notlar/genel-klasor-tabani.json": {"surum": 5}, "programlar.json": {"programlar": 3},
             "README.md": "eski agent'ların onlarla çalışmaya devam eder `python3 araclar/yok.py --x`\n"})
h, u = dg.belge_ve_kayit_denetimleri(k)
t("20a her şey bozukken (bozuk şemalar, eksik belgeler, kötü bayrak) HATA YOK, çok UYARI", h == [] and len(u) >= 12, (h, len(u)))
yaz(k, {"programlar.json": "{bozuk"})
h, u = dg.belge_ve_kayit_denetimleri(k)
t("20b ayrışmayan bir JSON kayıt dosyası -> tam bir HATA", len(h) == 1 and "programlar.json okunamadı" in h[0], h)
yaz(k, {"programlar.json": {"programlar": {}}, "AGENTS.md": ESIT + "fark"})
h, u = dg.belge_ve_kayit_denetimleri(k)
t("20c CLAUDE.md != AGENTS.md -> tam bir HATA", len(h) == 1 and "aynı değil" in h[0], h)
yaz(k, {"AGENTS.md": ESIT, "kaynaklar.json": "{x"})
h, u = dg.belge_ve_kayit_denetimleri(k)
t("20d bozuk kaynaklar.json: bir HATA, kapılar çökmez", len(h) == 1 and "kaynaklar.json okunamadı" in h[0], (h, u[:2]))
# beklenmeyen istisna -> UYARI
asil = dg.esitlik_denetimi
dg.esitlik_denetimi = lambda kok: 1 / 0
try:
    h, u = dg.belge_ve_kayit_denetimleri(kok_yap())
    t("20e bir denetim beklenmedik istisna atarsa doğrulama düşmez: UYARI 'çalışmadı'", h == [] and var(u, "eşitlik denetimi çalışmadı"), (h, u[:2]))
finally:
    dg.esitlik_denetimi = asil

# 21 rapor_yasi_satirlari
bugun = date(2026, 11, 11)
TABLO = [("a.md", 45, "yenile-a"), ("b.md", 45, "yenile-b"), ("c.md", 45, "yenile-c")]
k = kok_yap({"a.md": f"# a\n{(bugun - timedelta(days=50)).isoformat()}\n", "b.md": f"{(bugun - timedelta(days=10)).isoformat()}\n"})
s = ortak.rapor_yasi_satirlari(k, bugun, TABLO)
t("21a 50 günlük -> bir satır ve yenileme komutu; 10 günlük ve olmayan dosya -> yok", len(s) == 1 and "a.md 50 gün" in s[0] and "yenile-a" in s[0], s)
yaz(k, {"a.md": "\n".join(["x"] * 8) + f"\n{(bugun - timedelta(days=99)).isoformat()}\n"})
t("21b tarih yalnız 9. satırdaysa yok sayılır (ve git yoksa atlanır)", ortak.rapor_yasi_satirlari(k, bugun, [("a.md", 45, "y")]) == [])
if GIT_VAR:
    k = kok_yap({"a.md": "tarihsiz rapor\n"})
    git(k, "init", "-q")
    git(k, "add", "-A")
    git(k, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "eski", env={"GIT_COMMITTER_DATE": "2026-01-01T12:00:00", "GIT_AUTHOR_DATE": "2026-01-01T12:00:00"})
    s = ortak.rapor_yasi_satirlari(k, bugun, [("a.md", 45, "y")])
    t("21c tarihsiz dosya: git commit tarihi (%cs) kullanılır", len(s) == 1 and "314 gün" in s[0], s)
k = kok_yap({"a.md": "tarihsiz\n"})
t("21d tarih de git de yoksa atlanır, çökmez", ortak.rapor_yasi_satirlari(k, bugun, [("a.md", 45, "y")]) == [])
t("21e gerçek tablo, sahte kökte (hiçbir dosya yok) -> boş", ortak.rapor_yasi_satirlari(kok_yap(), bugun) == [])

# 22 ozet_json_gecerli
iyi = {"arac": "x", "durum": "temiz", "satirlar": ["a"], "karar_bekleyen": []}
o, _ = ortak.ozet_json_gecerli(json.dumps(iyi))
t("22a geçerli nesne kabul", o == iyi)
t("22b fazladan anahtar hoşgörülür", ortak.ozet_json_gecerli(json.dumps(dict(iyi, ek=1)))[0] is not None)
t("22c karar_bekleyen yok -> hata", ortak.ozet_json_gecerli(json.dumps({k_: v for k_, v in iyi.items() if k_ != "karar_bekleyen"}))[0] is None)
t("22d durum 'iyi' -> hata", ortak.ozet_json_gecerli(json.dumps(dict(iyi, durum="iyi")))[0] is None)
t("22e iki JSON nesnesi art arda -> hata", ortak.ozet_json_gecerli(json.dumps(iyi) + "\n" + json.dumps(iyi))[0] is None)
t("22f satirlar'da metin olmayan -> hata", ortak.ozet_json_gecerli(json.dumps(dict(iyi, satirlar=[1])))[0] is None)
t("22g JSON olmayan metin -> hata", ortak.ozet_json_gecerli("merhaba")[0] is None)

# 23 OZET_ARACLARI
ad_l = [a for a, _e in ortak.OZET_ARACLARI]
t("23a OZET_ARACLARI: (metin, liste) çiftleri, tekrar yok",
   all(isinstance(a, str) and isinstance(e, list) for a, e in ortak.OZET_ARACLARI) and len(set(ad_l)) == len(ad_l))
t("23b beklenen araçlar var, ekstra bayraklarla",
   {"git-durum", "yedek-denetim", "genel-bekci", "program-denetim", "proje-kullanimi", "skill-ekle", "konu-takip"} <= set(ad_l)
   and dict(ortak.OZET_ARACLARI)["skill-ekle"] == ["--araclar"] and dict(ortak.OZET_ARACLARI)["konu-takip"] == ["--bekleyenler"]
   and dict(ortak.OZET_ARACLARI)["proje-kullanimi"] == ["--saglik"])
t("23c listedeki her araç dosyası kütüphanede var (araçlar kaynakta durur)", all((ARACLAR / f"{a}.py").is_file() for a in ad_l), ad_l)

# 24 genel_izleri / genel_fark
g1, g2 = sahte_kok(), sahte_kok()
for g in (g1, g2):
    for ad in ("synced", ".system", "skills-cursor", "gercek-skill"):
        (g / ad).mkdir()
iz = ortak.genel_izleri([g1, g2, g1 / "yok-klasor"])
t("24a yerleşik adlar (synced, .system, skills-cursor) atlanır; eksik klasör çökmez",
   sorted(x.rsplit("/", 1)[1] for x in iz) == ["gercek-skill", "gercek-skill"], iz)
(g1 / "yeni-girdi").mkdir()
iz2 = ortak.genel_izleri([g1, g2])
t("24b yeni girdi genel_fark'ta", ortak.genel_fark(iz, iz2) == [f"{g1}/yeni-girdi"], ortak.genel_fark(iz, iz2))
os.utime(g1 / "gercek-skill", ns=(1_000_000_000, 1_000_000_000))
iz3 = ortak.genel_izleri([g1, g2])
t("24c değişen mtime genel_fark'ta", f"{g1}/gercek-skill" in ortak.genel_fark(iz2, iz3))
t("24d aynı iz -> fark boş", ortak.genel_fark(iz3, dict(iz3)) == [])
pi_once = ortak.genel_parmak_izi([g1, g2])
t("24e parmak izi aynı ağaçta aynı", pi_once == ortak.genel_parmak_izi([g1, g2]))
(g1 / "bir-daha").mkdir()
t("24e2 parmak izi girdi eklenince değişir", pi_once != ortak.genel_parmak_izi([g1, g2]))
t("24f izleme listesi üç genel klasörü ve OpenMontage skill klasörünü içerir",
   all(p in ortak.GENEL_IZLEME_KLASORLERI for p in ortak.GLOBAL_KLASORLER.values())
   and Path.home() / ".openmontage" / ".agents" / "skills" in ortak.GENEL_IZLEME_KLASORLERI)
t("24g GLOBAL_KLASORLER değişmedi (üç klasör)", sorted(ortak.GLOBAL_KLASORLER) == ["agents", "claude", "codex"])

# 25 alt test yükleyicisi: test.py kaynağından işlev çıkarılır, sahte KOK'a karşı çalışır
kaynak_py = (ARACLAR / "test.py").read_text(encoding="utf-8")
dugum = next(n for n in ast.parse(kaynak_py).body if isinstance(n, ast.FunctionDef) and n.name == "alt_testler")
kaynak_alt = ast.get_source_segment(kaynak_py, dugum)


def yukleyici_calistir(kok):
    kayit = []
    ad = {"KOK": Path(kok), "subprocess": subprocess, "sys": sys, "ALT_TEST_ZAMAN_ASIMI": 20,
          "test": lambda ad_, kosul, ayrinti="": kayit.append((ad_, bool(kosul)))}
    exec(kaynak_alt, ad)
    import io
    from contextlib import redirect_stdout
    tampon = io.StringIO()
    with redirect_stdout(tampon):
        ad["alt_testler"]()
    return kayit, tampon.getvalue()


k = kok_yap({"araclar/testler/test_ok.py": "print('2/2 test geçti')\n",
             "araclar/testler/test_kotu.py": "import sys\nprint('1/2 test geçti')\nsys.exit(1)\n",
             "araclar/testler/test_bos.py": "pass\n",
             "araclar/testler/test_yalan.py": "print('1/2 test geçti')\n",
             "araclar/testler/yardimci.py": "print('3/3 test geçti')\n"})
kayit, _cikti = yukleyici_calistir(k)
sonuc = {a.split()[2].rstrip(":"): ok for a, ok in kayit}
t("25a yükleyici: test_ok geçer; çıkış 1, çıktısız ve çıkış 0 ama N/M uyumsuz olanlar başarısız; yardımcı dosya çalıştırılmaz",
   sonuc == {"test_ok.py": True, "test_kotu.py": False, "test_bos.py": False, "test_yalan.py": False}, (sonuc, kayit))
kayit, cikti = yukleyici_calistir(kok_yap())
t("25b klasör yoksa BİLGİ satırı ve hiç kayıt yok", kayit == [] and "BİLGİ" in cikti, (kayit, cikti))
bos_kok = kok_yap()
(bos_kok / "araclar" / "testler").mkdir(parents=True)
kayit, cikti = yukleyici_calistir(bos_kok)
t("25c klasör boşsa BİLGİ satırı ve hiç kayıt yok", kayit == [] and "BİLGİ" in cikti)
t("25d test.py alt_testler() çağrısı genel parmak izi karşılaştırmasından ÖNCE yapar",
   kaynak_py.index("    alt_testler()\n") < kaynak_py.index('test("global klasörler test boyunca DEĞİŞMEDİ"'))

duman_py = (KOK / "araclar" / "duman-testi.py").read_text(encoding="utf-8")
t("26a duman: Yama A uyarısı tarih sınırlı kabul (sağlık kapısı kırmızı olmaz)",
   "KABUL_YAMA_A" in duman_py and "ilk satırı BASLA" in duman_py and "KABUL_YAMA_A_SON" in duman_py)
t("26b duman adım 11 OZET_ARACLARI döngüsü ve aylik-ozet satır sınırı kodda var (statik)",
   "OZET_ARACLARI" in duman_py and "aylik-ozet" in duman_py and "15" in duman_py)

# dogrula --github: korunan liste ve reddedilen kararı yıldız/liste uyarısından muaf, gerçek yeni repo değil
_ls = [{"slug": "guvenlik", "items": {"nodes": [{"nameWithOwner": "Vx/Riskli"}, None]}},
       {"slug": "yapay-zeka-skillleri", "items": {"nodes": [{"nameWithOwner": "Yeni/Aday"}]}}]
_muaf = dg.github_muaf_repolar(_ls, ["guvenlik"], {"degerlendirilen": {"Sir/Red": {"karar": "reddedildi"}, "A/Eklendi": {"karar": "eklendi"}}})
t("27a korunan listedeki repo uyarıdan muaf (büyük/küçük harfsiz)", "vx/riskli" in _muaf)
t("27b reddedildi kararlı repo muaf", "sir/red" in _muaf)
t("27c karar yok ya da 'eklendi' olan ve korunan olmayan repo muaf DEĞİL (gerçek eksik uyarı verir)",
  "yeni/aday" not in _muaf and "a/eklendi" not in _muaf and "storytold/pdfcraft" not in _muaf)
t("27d konu durumu boş/None ve liste yok -> hata vermez", dg.github_muaf_repolar([], [], None) == set())
_dsrc = (ARACLAR / "dogrula.py").read_text(encoding="utf-8")
t("27e dogrula iki uyarıda da muaf kümesini kullanıyor", _dsrc.count("not in muaf") == 2)
t("27f duman adım 11 yalnız stdout okur (kos_stdout)", "def kos_stdout" in duman_py and 'kos_stdout(PY, f"araclar/{ad}.py"' in duman_py)

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
