#!/usr/bin/env python3
"""P7 testleri: kaynak-cikar.py, kaynak-cek.py (--atla, lisans_riskli), yol-tara.py (--siki), listeye-ekle.py (küçük harf düzeltmesi),
konu-takip.py (ortak eleme, --karar doğrulaması, --bekleyenler) ve rehber/prompt metinleri.
Yalnız geçici klasör ve sahte veri: gerçek registry/konu-takip/ev klasörü, ağ ve gh kullanılmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import builtins
import contextlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))
import ortak  # noqa: E402


def yukle(ad):
    spec = importlib.util.spec_from_file_location(ad.replace("-", "_") + "_p7t", ARACLAR / f"{ad}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


kc, kt, yt, le, kcik = (yukle(x) for x in ("kaynak-cek", "konu-takip", "yol-tara", "listeye-ekle", "kaynak-cikar"))
TMP = Path(tempfile.mkdtemp(prefix="p7test-"))
gecen = toplam = 0


def test(ad, kosul, detay=""):
    global gecen, toplam
    toplam += 1
    if kosul:
        gecen += 1
    else:
        print(f"HATA: {ad} {str(detay)[:400]}")


@contextlib.contextmanager
def yama(nesne, **kw):
    eski = {k: getattr(nesne, k) for k in kw}
    for k, v in kw.items():
        setattr(nesne, k, v)
    try:
        yield
    finally:
        for k, v in eski.items():
            setattr(nesne, k, v)


def yakala(f, *a, **k):
    """(dönüş ya da SystemExit kodu, stdout, stderr)"""
    o, e = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e):
        try:
            r = f(*a, **k)
        except SystemExit as x:
            r = x.code if x.code is not None else 0
    return r, o.getvalue(), e.getvalue()


def argv_ile(argv, f):
    eski = sys.argv
    sys.argv = argv
    try:
        return yakala(f)
    finally:
        sys.argv = eski


def yaz(yol, icerik):
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(icerik if isinstance(icerik, str) else json.dumps(icerik, ensure_ascii=False, indent=1), encoding="utf-8")


def goruntu(kok):
    return sorted((str(p.relative_to(kok)), p.stat().st_size, p.stat().st_mtime_ns) for p in Path(kok).rglob("*"))


# ------------------------------------------------------------------ kaynak-cikar: geçici kütüphane
C40 = "a" * 40


def kur_kok(ad, projeli=True):
    kok = TMP / ad
    proj = TMP / (ad + "-projeler")
    shutil.rmtree(kok, ignore_errors=True)
    shutil.rmtree(proj, ignore_errors=True)
    proj.mkdir(parents=True)
    yaz(kok / "kaynaklar.json", {"repolar": [
        {"repo": "own/gsap", "tip": "T1", "oncelik": 3, "eski_adlar": ["old/gsap"]},
        {"repo": "own/prog", "tip": "T1", "program": "prg"},
        {"repo": "own/lost", "tip": "KAYIP"},
        {"repo": "ref/card", "tip": "T6"},
        {"repo": "dev/devral", "tip": "T1", "ad_devral": ["shared"]},
        {"repo": "other/x", "tip": "T1"}, {"repo": "old/holder", "tip": "T1"}],
        "arsivden_cikarilan_repolar": [{"repo": "gone/repo", "tarih": "2026-10-01", "neden": "x", "geri_alma": "y"}, "str/form"]})
    sk = lambda i, repo, durum="tercih", **k: {"id": i, "ad": k.pop("ad", i), "repo": repo, "durum": durum, "kaynak_yol": k.pop("yol", ""),
                                               "commit": k.pop("commit", C40), **k}
    yaz(kok / "registry.json", {"skiller": [
        sk("gsap-core", "own/gsap", ortusme_grubu="g1", ortusme_rolu="birincil"),
        sk("gsap-utils", "own/gsap", ortusme_grubu="g1", ortusme_rolu="tamamlayıcı"),
        sk("dupname", "own/gsap", yol="a/dup"),
        sk("dupname@other/x", "other/x", "alternatif", ad="dupname", yol="d"),
        sk("lostskill", "own/lost", kaynak_durumu="kayip", commit="b" * 40),
        sk("shared", "dev/devral"),
        sk("shared@old/holder", "old/holder", "alternatif", ad="shared"),
        sk("progskill", "own/prog")]})
    yaz(kok / "roller" / "r1.json", {"ad": "r1", "cekirdek": ["gsap-core"], "opsiyonel": ["gsap-utils"]})
    yaz(kok / "roller" / "r2.json", {"ad": "r2", "cekirdek": ["dupname"], "opsiyonel": []})
    yaz(kok / "profiller" / "p1.json", {"ad": "p1", "roller": ["r1"], "ek_skiller": ["gsap-core"]})
    yaz(kok / "konu-takip.json", {"konular": {"k": {"repolar": {"own/gsap": {}}}}})
    yaz(kok / "notlar" / "referans" / "tasarim.md", "# T\n\n### Kart — `ref/card` · v1\n**Skill:** x\n")
    yaz(kok / "trend.json", {})
    if projeli:
        yaz(proj / "ProjeA" / ".skill-kutuphanesi" / "kilit.json", {"skiller": {
            "gsap-core": {"id": "gsap-core", "repo": "old/gsap", "kaynak_yol": "", "roller": ["r1"]}}})
    yaz(kok / "projeler.json", {"tarama_kokleri": [str(proj)]})
    return kok


def rapor(kok, tur, hedef, **k):
    return kcik.rapor_uret(kok, tur, hedef, bugun="2026-11-12", **k)


K = kur_kok("kok1")
r1 = rapor(K, "repo", "own/gsap", neden="gerekçe metni")
test("1. repo raporu: rol/profil/proje/kayıt satırları, karar engel",
     r1["karar"] == "engel" and {x["girdi"] for x in r1["roller"]} == {"gsap-core", "gsap-utils", "dupname"}
     and r1["profiller"][0]["girdi"] == "gsap-core" and r1["projeler"][0]["proje"] == "ProjeA"
     and any(k["dosya"] == "konu-takip.json" for k in r1["kayitlar"]), r1)
rs = rapor(K, "skill", "dupname@other/x")
rd = rapor(K, "skill", "dupname")
test("2. rol çıplak adla yalnız tercih skille eşleşir; alternatifte eşleşmez",
     any(x["girdi"] == "dupname" for x in rd["roller"]) and rs["roller"] == [], (rd["roller"], rs["roller"]))
n = [int(re.match(r"(\d+)\.", x).group(1)) for x in r1["adimlar"]]
t_rep = " ".join(r1["adimlar"])
t_skl = " ".join(rapor(K, "skill", "gsap-core")["adimlar"])
r_bos = rapor(kur_kok("kok_bos", projeli=False), "repo", "other/x")
n_bos = [int(re.match(r"(\d+)\.", x).group(1)) for x in r_bos["adimlar"]]
test("3. adım sırası sabit, koşullu adımlar (2,3,5) isabet yoksa düşer, repo/skill adım 4 farklı",
     n == sorted(n) and {0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12} <= set(n) and 5 not in n
     and not ({2, 3, 5} & set(n_bos)) and "arsivden_cikarilan_repolar'a" in t_rep and "arsivden_cikarilanlar'a" in t_skl
     and all("KULLANMA" in a for a in r1["adimlar"] if "--kayba-izin-ver" in a), (n, n_bos))
d_s = rapor(K, "skill", "lostskill")["defter_taslagi"]
d_r = r1["defter_taslagi"]
test("4. defter taslağı geçerli JSON, son_commit/tarih/neden doğru",
     d_s["defter"] == "arsivden_cikarilanlar" and d_s["kayit"]["son_commit"] == "b" * 40 and d_s["kayit"]["tarih"] == "2026-11-12"
     and "<NEDEN" in d_s["kayit"]["neden"] and d_r["kayit"]["neden"] == "gerekçe metni" and d_r["defter"] == "arsivden_cikarilan_repolar"
     and json.loads(json.dumps(d_r))["kayit"]["skill_sayisi"] == 3, (d_s, d_r))
rp = rapor(K, "repo", "own/prog")
cikti_p = kcik.metin_uret(rp)
test("5. program korumu: reddedildi, adım yok, rehber/11 yönlendirmesi", rp["karar"] == "reddedildi" and rp["adimlar"] == []
     and "rehber/11" in rp["mesaj"] and "Programı çıkarma" in rp["mesaj"] and "Programı çıkarma" in cikti_p, rp)
with yama(ortak, KOK=K):
    c6a = yakala(kcik.main, ["--repo", "own/gsap"])
    c6b = yakala(kcik.main, ["--repo", "own/gsap", "--kuru", "--uygula"])
    c6c = yakala(kcik.main, ["--kuru"])
    c5 = yakala(kcik.main, ["--repo", "own/prog", "--kuru", "--siki"])
    c5b = yakala(kcik.main, ["--repo", "own/prog", "--kuru"])
test("5b. --siki program kaydında çıkış 1, --siki yoksa 0", c5[0] == 1 and c5b[0] == 0, (c5, c5b))
test("6. --kuru yoksa 2 ve ileti; --uygula 2; hedefsiz 2", c6a[0] == 2 and "yalnız --kuru var" in c6a[1] and c6b[0] == 2 and c6c[0] == 2,
     (c6a, c6b[0], c6c))
try:
    rapor(K, "repo", "yok/boyle")
    yok = False
except kcik.HedefHata:
    yok = True
try:
    rapor(K, "skill", "shared")
    belirsiz = "x"
except kcik.HedefHata as e:
    belirsiz = str(e)
with yama(ortak, KOK=K):
    c7 = yakala(kcik.main, ["--repo", "yok/boyle", "--kuru"])
    c7b = yakala(kcik.main, ["--skill", "dupname@other/x", "--kuru"])
# "shared" tam kimlikle bulunur; çıplak ad belirsizliği için dupname@x ile dupname iki ayrı id; belirsiz ad: ad="shared" iki kayıt, biri id=shared (tam eşleşir)
test("7. bilinmeyen hedef 2; birden çok kayıt (aynı ad, tam kimlik yok) listelenir",
     yok and c7[0] == 2 and c7b[0] == 0 and belirsiz == "x", (yok, c7, belirsiz))
K2 = kur_kok("kok_belirsiz")
yaz(K2 / "registry.json", {"skiller": [{"id": "a@x", "ad": "ortak", "repo": "own/gsap", "durum": "tercih"},
                                         {"id": "a@y", "ad": "ortak", "repo": "own/gsap", "durum": "alternatif"}]})
try:
    rapor(K2, "skill", "ortak")
    bel2 = ""
except kcik.HedefHata as e:
    bel2 = str(e)
test("7b. belirsiz çıplak ad -> hata ve kimlik listesi", "Birden çok kayıt" in bel2 and "a@x" in bel2 and "a@y" in bel2, bel2)
r_yok = rapor(kur_kok("kok_np", projeli=False), "repo", "own/gsap")
yb = kur_kok("kok_p2")
yaz(yb / "projeler.json", {"tarama_kokleri": [str(TMP / "kok_p2-projeler")]})
shutil.rmtree(TMP / "kok_p2-projeler" / "ProjeA")
(TMP / "kok_p2-projeler" / "Baska" / ".skill-kutuphanesi").mkdir(parents=True)
yaz(TMP / "kok_p2-projeler" / "Baska" / ".skill-kutuphanesi" / "kilit.json", {"skiller": {"x": {"id": "x", "repo": "z/z"}}})
r_var = rapor(yb, "repo", "own/gsap")
tx = kcik.metin_uret(r_yok)
test("8. proje yok -> BİLİNMİYOR, hazir olmaz; proje var ama kullanan yok -> 'Hiçbir projede'",
     r_yok["proje_bilgisi"] == "yok" and "etki BİLİNMİYOR" in tx and r_yok["karar"] != "hazir"
     and r_var["proje_bilgisi"] == "var" and r_var["projeler"] == [] and "Hiçbir projede kullanılmıyor." in kcik.metin_uret(r_var),
     (r_yok["proje_bilgisi"], r_var["proje_bilgisi"]))
ra = rapor(K, "repo", "old/gsap")
rb = rapor(K, "repo", "OWN/GSAP")
test("9. eski ad ve büyük harf aynı kayda çözülür", ra["hedef"]["repo"] == rb["hedef"]["repo"] == "own/gsap", (ra["hedef"], rb["hedef"]))
rdv = rapor(K, "repo", "dev/devral")
rsh = rapor(K, "skill", "shared@old/holder")
test("10. ad_devral: kayıt ve eski sahip kimliği, başka kaydın devri raporlanır",
     rdv["ad_devri"]["bu_kaydin"] == [{"ad": "shared", "devredilen_kimlikler": ["shared@old/holder"]}]
     and rsh["ad_devri"]["baska_kayitlarin"] == [{"repo": "dev/devral", "ad": "shared"}], (rdv["ad_devri"], rsh["ad_devri"]))
rl = rapor(K, "repo", "own/lost")
rz = rapor(K, "repo", "gone/repo")
rz2 = rapor(K, "repo", "str/form")
test("11. KAYIP kayıt raporlanır ve adımlar yazılır; çıkarılmış repo -> 'Zaten çıkarılmış', karar yok",
     rl["hedef"]["kayip"] is True and rl["adimlar"] and rz["karar"] == "yok" and "Zaten çıkarılmış" in rz["mesaj"]
     and rz2["karar"] == "yok", (rl["hedef"], rz))
K3 = kur_kok("kok_orphan")
yaz(K3 / "registry.json", {"skiller": [{"id": "yetim", "ad": "yetim", "repo": "orp/han", "durum": "tercih", "commit": C40}]})
ro = rapor(K3, "repo", "orp/han")
test("12. yetim (registry var, kayıt yok): not yazılır, çökmez", any("orphan" in x for x in ro["notlar"]) and ro["hedef"]["skill_sayisi"] == 1, ro["notlar"])
K4 = kur_kok("kok_ro")
once = goruntu(K4)
rapor(K4, "repo", "own/gsap")
with yama(ortak, KOK=K4):
    yakala(kcik.main, ["--repo", "own/gsap", "--kuru"])
    c14 = yakala(kcik.main, ["--repo", "own/gsap", "--kuru", "--json"])
sonra = goruntu(K4)
test("13. salt okuma: ağaç (ad, boyut, mtime) öncesi ve sonrası aynı; yeni dosya yok", once == sonra)
try:
    j = json.loads(c14[1])
    anahtarlar = {"arac", "mod", "hedef", "karar", "engeller", "dikkatler", "projeler", "proje_bilgisi", "roller", "profiller", "registry",
                  "ad_devri", "kayitlar", "github", "defter_taslagi", "adimlar", "geri_alma"}
    ok14 = anahtarlar <= set(j) and len(c14[1].strip().splitlines()) == 1
except ValueError:
    ok14 = False
test("14. --json tek satır, tek nesne, tüm anahtarlar", ok14, c14[1][:200])


def sahte_gh(cevaplar):
    def f(args):
        for k, v in cevaplar.items():
            if k in " ".join(args):
                if isinstance(v, Exception):
                    raise v
                return v
        return (1, "", "")
    return f


g404 = rapor(K, "repo", "own/lost", github=True, gh=sahte_gh({"repos/own/lost": (1, "", "gh: Not Found (HTTP 404)"), "starred": (1, "", "")}),
             listeler=lambda: [])
gyeni = rapor(K, "repo", "own/gsap", github=True, gh=sahte_gh({"repos/own/gsap": (0, "yeni/ad\n", ""), "starred": (0, "", "")}),
              listeler=lambda: [{"name": "L", "items": {"nodes": [{"nameWithOwner": "OWN/gsap"}]}}])


def patla():
    raise RuntimeError("graphql kapalı")


ghata = rapor(K, "repo", "own/gsap", github=True, gh=sahte_gh({"repos": RuntimeError("yok")}), listeler=patla)
test("15. --github: 404 kaynak kayıp; yeni ad AD DEĞİŞMİŞ; hata okunamadı ve çalışma sürer",
     "404" in g404["github"]["erisim"] and g404["github"]["yildiz"] == "yıldızsız"
     and gyeni["github"]["yeni_ad"] == "yeni/ad" and any("AD DEĞİŞMİŞ" in d for d in gyeni["dikkatler"]) and gyeni["github"]["listeler"] == ["L"]
     and ghata["github"]["erisim"] == "okunamadı" and ghata["github"]["listeler"] == "okunamadı", (g404["github"], gyeni["github"], ghata["github"]))

# ------------------------------------------------------------------ konu-takip
AYAR = {"repolar": [{"repo": "lib/One", "tip": "T1", "eski_adlar": ["Old/One"]}, {"repo": "lib/Kayip", "tip": "KAYIP"}],
        "arsivden_cikarilan_repolar": ["Gone/Str", {"repo": "Gone/Dict"}],
        "takip_konulari": [{"konu": "k", "kategori": "c", "min_yildiz": 10, "sorgular": ["q"], "odak": "skill"}]}
BUGUN = date(2026, 11, 11)


def durum0():
    return {"degerlendirilen": {"Mixed/Red": {"karar": "reddedildi", "neden": "n", "tarih": "2026-10-01"},
                                "ok/eklenen": {"karar": "eklendi", "neden": "n", "tarih": "2026-10-02"}},
            "izlenen": {"Wait/Me": {"neden": "w", "tarih": "2026-01-01"}},
            "konular": {"k": {"repolar": {}, "son_tarama": "2026-11-04"}}}


e = kt.elenecekler(AYAR, durum0())
test("16. elenecekler: eski ad, str/dict çıkarılan, karar, izlenen; hepsi küçük harf; eleniyor harfe bakmaz",
     {"lib/one", "old/one", "lib/kayip"} <= e["kaynak"] and e["cikarilan"] == {"gone/str", "gone/dict"} and "mixed/red" in e["karar"]
     and e["izlenen"] == {"wait/me"} and kt.eleniyor("MIXED/RED", e) and kt.eleniyor("WAIT/ME", e) and not kt.eleniyor("WAIT/ME", e, False)
     and not kt.eleniyor("yeni/repo", e), e)
d = durum0()
m, h = kt.karar_uygula(d, AYAR, {}, "new/watch", "izle", "neden", bugun=BUGUN)
vade_once = kt.izlenen_vadesi({"tarih": "2026-08-01"}, BUGUN)
vade_yeni = kt.izlenen_vadesi({"tarih": "2026-11-01"}, BUGUN)
test("17. izle yalnız izlenen'e yazar; vade 90 gün sonra", h is None and "new/watch" in d["izlenen"] and "new/watch" not in d["degerlendirilen"]
     and d["izlenen"]["new/watch"]["tarih"] == "2026-11-11" and vade_once[1] is True and vade_yeni[1] is False
     and vade_yeni[0] == "2027-01-30", (d, vade_once, vade_yeni))
d = durum0()
snap = json.dumps(d, sort_keys=True)
_, h1 = kt.karar_uygula(d, AYAR, {}, "mixed/red", "izle", "x", bugun=BUGUN)
_, h2 = kt.karar_uygula(d, AYAR, {}, "ok/eklenen", "reddedildi", "x", bugun=BUGUN)
unut = json.dumps(d, sort_keys=True) == snap
m3, h3 = kt.karar_uygula(d, AYAR, {}, "mixed/red", "eklendi", "artık uygun", bugun=BUGUN)
test("18. reddedildi->izle ve eklendi->reddedildi reddedilir (kayıt değişmez); reddedildi->eklendi serbest",
     h1 and "REDDEDİLDİ" in h1 and h2 and "EKLENDİ" in h2 and unut and h3 is None and d["degerlendirilen"]["Mixed/Red"]["karar"] == "eklendi"
     and any("güncellendi" in x for x in m3), (h1, h2, h3, m3))
d = durum0()
kt.karar_uygula(d, AYAR, {}, "mixed/red", "reddedildi", "tekrar", bugun=BUGUN)
test("19. büyük/küçük harf farklı yazım aynı anahtarı kullanır, ikinci kayıt oluşmaz",
     [k for k in d["degerlendirilen"] if k.lower() == "mixed/red"] == ["Mixed/Red"], d["degerlendirilen"])
d = durum0()
snap = json.dumps(d, sort_keys=True)
_, ha = kt.karar_uygula(d, AYAR, {}, "bozuk repo adi", "eklendi", "x")
_, hb = kt.karar_uygula(d, AYAR, {}, "a/b", "belki", "x")
_, hc = kt.karar_uygula(d, AYAR, {}, "lib/one", "reddedildi", "x")
mw, hw = kt.karar_uygula(d, AYAR, {}, "tamamen/yeni", "reddedildi", "")
test("20. geçersiz ad/karar ve kütüphane reposu hata (kayıt değişmez); bilinmeyen repo uyarıyla yazılır",
     ha and "geçersiz repo adı" in ha and hb and "karar:" in hb and hc and "kütüphanede olan repoya" in hc
     and hw is None and any("UYARI" in x for x in mw) and d["degerlendirilen"]["tamamen/yeni"]["neden"] == "-"
     and json.dumps({k: v for k, v in d.items() if k != "degerlendirilen"}, sort_keys=True)
     == json.dumps({k: v for k, v in durum0().items() if k != "degerlendirilen"}, sort_keys=True), (ha, hb, hc, mw))
kd = TMP / "kt"
kd.mkdir()
duz = durum0()
duz["konular"]["k"]["repolar"] = {
    "a/izl": {"yildiz": 50, "aciklama": "skill x", "sorgular": ["q"], "skill_yollari": ["x"]},
    "Wait/me": {"yildiz": 50, "aciklama": "skill", "sorgular": ["q"], "skill_yollari": ["x"]},
    "MIXED/RED": {"yildiz": 50, "aciklama": "skill", "sorgular": ["q"], "skill_yollari": ["x"]},
    "lib/one": {"yildiz": 50, "aciklama": "skill", "sorgular": ["q"], "skill_yollari": ["x"]},
    "b/aday": {"yildiz": 50, "aciklama": "skill harika", "sorgular": ["q"], "skill_yollari": ["x"]},
    "c/aday": {"yildiz": 80, "aciklama": "skill iyi", "sorgular": ["q"], "skill_yollari": ["x"]},
    "d/dusuk": {"yildiz": 1, "aciklama": "skill", "sorgular": ["q"], "skill_yollari": ["x"]}}
duz["izlenen"]["Wait/Me"]["tarih"] = "2020-01-01"
with yama(kt, DURUM=kd / "d.json", RAPOR=kd / "r.md", KAYNAKLAR=kd / "k.json", TREND=kd / "yok-trend.json"):
    yaz(kd / "k.json", AYAR)
    kt.rapor(duz, AYAR)
    md_ = (kd / "r.md").read_text(encoding="utf-8")
aday_tablo = md_.split("## İzlenenler")[0]
izl_bolum = md_.split("## İzlenenler")[1].split("## Değerlendirilen")[0]
test("21. rapor: izlenen aday tablosunda yok, İzlenenler bölümünde ve vadesi gelmiş; farklı harfli reddedilen gizli",
     "Wait/me" not in aday_tablo and "MIXED/RED" not in aday_tablo and "lib/one" not in aday_tablo and "b/aday" in aday_tablo
     and "Wait/Me" in izl_bolum and "⏰ zamanı geldi" in izl_bolum and "odaklı aday: 3" in md_, md_[:1500])
beklenen = [r for r, v in duz["konular"]["k"]["repolar"].items() if kt.aday_mi(r, v, AYAR["takip_konulari"][0], kt.elenecekler(AYAR, duz))]
with yama(kt, DURUM=kd / "d.json", RAPOR=kd / "r.md", KAYNAKLAR=kd / "k.json", TREND=kd / "yok-trend.json", KOK=kd):
    yaz(kd / "d.json", duz)
    _, o22, _ = argv_ile(["konu-takip.py", "--rapor"], kt.main)
test("22. aday_mi tek ölçüt: rapor tablosu, özet sayısı ve main çıktısı aynı sayı",
     len(beklenen) == 3 and "odaklı aday 3" in o22 and "odaklı aday: 3" in md_, (beklenen, o22))

yaz(kd / "pop.md", "# P\n\n> `x` üretir · 2026-11-04 · 15 sorgu\n\n## Yeni adaylar (3)\n| Repo | ★ | SKILL.md |\n|---|---|---|\n"
    + "".join(f"| [p/r{i}](https://github.com/p/r{i}) | {1000 - i} | 3 | MIT |\n" for i in range(8))
    + "| [Mixed/Red](https://github.com/Mixed/Red) | 5000 | 2 | MIT |\n\n## Skill içermeyen eşleşmeler (1)\nx\n")


def cal(durum, trend, pop, json_mod=True, siki=False):
    kayit = kd / "oz"
    shutil.rmtree(kayit, ignore_errors=True)
    kayit.mkdir()
    with yama(kt, DURUM=kayit / "d.json", KAYNAKLAR=kayit / "k.json", TREND=kayit / "t.json", POPULER=kayit / "p.md"):
        yaz(kayit / "k.json", AYAR)
        if durum is not None:
            yaz(kayit / "d.json", durum) if isinstance(durum, dict) else (kayit / "d.json").write_text(durum)
        if trend is not None:
            yaz(kayit / "t.json", trend)
        if pop is not None:
            (kayit / "p.md").write_text(pop, encoding="utf-8")
        once_ = goruntu(kayit)
        r = yakala(kt.bekleyenler_calistir, json_mod, siki)
        return r, goruntu(kayit) == once_


tr = {"son_tarama": "2026-11-09", "son_liste": {"t/one": {}, "t/rej": {}, "t/zero": {}, "Wait/Me": {}},
      "skill_sayisi": {"t/one": {"skill": 3}, "t/rej": {"skill": 2}, "t/zero": {"skill": 0}, "Wait/Me": {"skill": 4}}}
duz2 = durum0()
duz2["degerlendirilen"]["t/rej"] = {"karar": "reddedildi", "neden": "n", "tarih": "2026-10-01"}
duz2["izlenen"]["Wait/Me"]["tarih"] = "2026-11-01"
duz2["konular"]["k"]["son_tarama"] = date.today().isoformat()
(r23, _, _), degismedi = cal(duz2, tr, (kd / "pop.md").read_text(encoding="utf-8"))
test("23a. --ozet-json: tek JSON satırı, doğru anahtarlar, dosya yazılmaz, çıkış 0",
     r23 == 0 and degismedi, r23)
(_, jo, _), _ = cal(duz2, tr, (kd / "pop.md").read_text(encoding="utf-8"))
try:
    jj = json.loads(jo)
    ok23 = set(jj) == {"arac", "durum", "satirlar", "karar_bekleyen"} and len(jo.strip().splitlines()) == 1 and jj["arac"] == "konu-takip"
except ValueError:
    jj, ok23 = {}, False
test("23b. özet nesnesi biçimi", ok23 and jj["durum"] == "dikkat", jo[:300])
dur_temiz = durum0()
dur_temiz["izlenen"] = {}
dur_temiz["konular"]["k"]["son_tarama"] = date.today().isoformat()
tr_temiz = {"son_tarama": date.today().isoformat(), "son_liste": {}, "skill_sayisi": {}}
pop_temiz = f"# P\n\n> x · {date.today().isoformat()} · 1\n\n## Yeni adaylar (0)\n| Repo |\n|---|\n\n## Sonraki\n"
(_, jt, _), _ = cal(dur_temiz, tr_temiz, pop_temiz)
(_, jbayat, _), _ = cal(dur_temiz, tr_temiz, pop_temiz.replace(date.today().isoformat(), "2026-01-01"))
(rs1, js, _), _ = cal("{bozuk json", None, None)
(rs2, _, _), _ = cal("{bozuk json", None, None, siki=True)
(_, jb2, _), _ = cal(dur_temiz, tr_temiz, pop_temiz)
test("23c. temiz -> temiz; bayat (>45 gün) -> dikkat; okunamayan konu-takip.json -> sorun; --siki yalnız sorun için 1",
     json.loads(jt)["durum"] == "temiz" and json.loads(jbayat)["durum"] == "dikkat" and json.loads(js)["durum"] == "sorun"
     and rs1 == 0 and rs2 == 1, (jt, jbayat, js, rs1, rs2))
durum_8 = durum0()
durum_8["izlenen"] = {}
aday8 = {f"s/a{i}": {"yildiz": 100 + i, "aciklama": "skill", "sorgular": ["q"], "skill_yollari": ["x"]} for i in range(8)}
durum_8["konular"]["k"]["repolar"] = aday8
durum_8["konular"]["k"]["son_tarama"] = date.today().isoformat()
dd, satir, bek = kt.bekleyenler(AYAR, durum_8, {}, None, BUGUN)
konu_bek = [b for b in bek if "(★" in b and ", k)" in b]
test("24. triyaj: 8 aday -> en çok 5 ad, en yüksek ★ önce, toplam satırda",
     len(konu_bek) == 5 and konu_bek[0].startswith("s/a7 ") and any(s.startswith("k: 8 odaklı aday") for s in satir), (bek, satir))
dd, satir, bek = kt.bekleyenler(AYAR, duz2, tr, (kd / "pop.md").read_text(encoding="utf-8"), date(2026, 11, 11))
trend_bek = [b for b in bek if "(trend," in b]
pop_bek = [b for b in bek if "(★" in b and "popüler" in b]
dd2, satir2, _ = kt.bekleyenler(AYAR, duz2, None, None, BUGUN)
dd3, satir3, _ = kt.bekleyenler(AYAR, duz2, {"son_tarama": "2026-11-09", "son_liste": {}, "skill_sayisi": {}}, "# bölümsüz\n", BUGUN)
duz_son = json.loads(json.dumps(duz2))
duz_son["degerlendirilen"]["p/r0"] = {"karar": "reddedildi", "neden": "n", "tarih": "2026-11-05"}
_, satir4, bek4 = kt.bekleyenler(AYAR, duz_son, tr, (kd / "pop.md").read_text(encoding="utf-8"), BUGUN)
_, satir5, _ = kt.bekleyenler(AYAR, duz2, tr, (kd / "pop.md").read_text(encoding="utf-8").replace("2026-11-04", "2026-01-01"), BUGUN)
test("25. trend: reddedilen/izlenen/skill=0 sayılmaz; eksik rapor dikkat (sorun değil); taramadan sonra karar verilen kaybolur; eski tarih dikkat",
     trend_bek == ["t/one (trend, 3 skill)"] and any(s == "trend: 1 aday, son tarama 2026-11-09 (2 gün önce)" for s in satir)
     and any(s.startswith("popüler: 8 aday") for s in satir)  # Mixed/Red elendi (9 satırdan 8)
     and "trend: rapor yok" in satir2 and "popüler: rapor yok" in satir2 and dd2 == "dikkat"
     and any("okunamadı" in s for s in satir3) and dd3 == "dikkat"
     and any(s.startswith("popüler: 7 aday") for s in satir4) and not any("p/r0 " in b for b in bek4)
     and dd == "dikkat" and any("rapor 2026-01-01" in s and "gün)" in s for s in satir5) and len(pop_bek) == 5,
     (satir, satir2, satir3, satir4, satir5, trend_bek))

# ------------------------------------------------------------------ kaynak-cek
kume, tan = kc.atla_kumesi(" Own/A , ,old/b ,zz/x", [{"repo": "own/a", "tip": "T1"}, {"repo": "own/b", "tip": "T2"}, {"repo": "p/q", "tip": "T5"}],
                           cevir=lambda r: {"old/b": "own/B"}.get(r.lower(), r))
kume0, tan0 = kc.atla_kumesi("", [], cevir=lambda r: (_ for _ in ()).throw(AssertionError("boş değerde çağrılmamalı")))
kume_t5, tan_t5 = kc.atla_kumesi("p/q", [{"repo": "p/q", "tip": "T5"}], cevir=lambda r: r)
test("26. atla_kumesi: virgül/boşluk/büyük harf/eski ad -> aynı küçük harfli küme; T1-T4 olmayan tanımsız; boşta cevir çağrılmaz",
     kume == {"own/a", "own/b", "zz/x"} and tan == ["zz/x"] and kume0 == set() and tan0 == [] and tan_t5 == ["p/q"], (kume, tan, tan_t5))

kk = TMP / "kc"
kk.mkdir()
yaz(kk / "kaynaklar.json", {"repolar": [{"repo": "own/a", "tip": "T1"}, {"repo": "own/a", "tip": "T4", "dahil": ["^x/"]},
                                         {"repo": "ref/t5", "tip": "T5"}],
                            "konum_haric": [], "skill_ici_haric": [], "ayna_klasorler": [], "max_dosya_mb": 5})
cagrildi = []


def agac_yok(repo):
    cagrildi.append(repo)
    raise AssertionError("atlanan repo için repo_agaci çağrıldı")


def agac_404(repo):
    cagrildi.append(repo)
    raise kc.GhBulunamadi("404")


with yama(kc, KAYNAKLAR=kk / "kaynaklar.json", GECICI=kk / "gecici", repo_agaci=agac_yok), yama(ortak, KAYNAKLAR=kk / "kaynaklar.json", _TAKMA_ADLAR=None):
    r27, o27, _ = argv_ile(["kaynak-cek.py", "--atla", "OWN/A"], kc.main)
mani = json.loads((kk / "gecici" / "cekilen" / "manifest.json").read_text(encoding="utf-8"))
test("27. --atla: UYARI bir kez, repo_agaci çağrılmaz, manifestte yok, SystemExit yok (iki kayıt tek uyarı)",
     r27 is None and o27.count("UYARI: own/a atlandı (arşiv kopyası korunur)") == 1 and cagrildi == [] and mani["kayitlar"] == []
     and "Toplam kayıt: 0" in o27, (r27, o27))
with yama(kc, KAYNAKLAR=kk / "kaynaklar.json", GECICI=kk / "gecici2", repo_agaci=agac_404), yama(ortak, KAYNAKLAR=kk / "kaynaklar.json", _TAKMA_ADLAR=None):
    r28a, o28a, _ = argv_ile(["kaynak-cek.py", "--atla", "yok/kayit"], kc.main)
    cagrildi.clear()
    r28b, o28b, e28b = argv_ile(["kaynak-cek.py"], kc.main)
test("28. --atla bilinmeyen repo: yok sayıldı; bayraksız eski yol (erişilemiyor -> SystemExit) aynen",
     "T1-T4 kaydı yok; yok sayıldı" in o28a and isinstance(r28a, str) and "erişilemiyor" in r28a and "erişilemiyor" in (str(r28b) + o28b + e28b)
     and cagrildi == ["own/a"], (r28a, o28a, r28b, o28b, e28b))
h29 = subprocess.run([sys.executable, str(ARACLAR / "kaynak-cek.py"), "--help"], capture_output=True, text=True)
test("29. kaynak-cek.py --help --atla gösterir", h29.returncode == 0 and "--atla" in h29.stdout, h29.stderr[:200])
test("30. lisans_riskli", all(kc.lisans_riskli(x) for x in ("belirtilmemiş", "NOASSERTION", "yok", "AGPL-3.0", "CC-BY-NC-4.0", "PolyForm-Noncommercial-1.0.0", "", None))
     and not any(kc.lisans_riskli(x) for x in ("MIT", "Apache-2.0", "BSD-3-Clause")))

# ------------------------------------------------------------------ yol-tara
yk = TMP / "yt"
yk.mkdir()
yaz(yk / "registry.json", {"skiller": [
    {"id": "temiz", "ad": "temiz", "repo": "o/r", "durum": "tercih", "kaynak_yol": "a"},
    {"id": "cozumsuz", "ad": "cozumsuz", "repo": "o/r", "durum": "tercih", "kaynak_yol": "b"},
    {"id": "istisnali", "ad": "istisnali", "repo": "o/r2", "durum": "tercih", "kaynak_yol": "c"},
    {"id": "yazar", "ad": "yazar", "repo": "o/r3", "durum": "tercih", "kaynak_yol": "d"},
    {"id": "eski", "ad": "eski", "repo": "o/r4", "durum": "tercih", "kaynak_yol": "e"},
    {"id": "bilgi", "ad": "bilgi", "repo": "o/r5", "durum": "tercih", "kaynak_yol": "f"}]})
DEG = {"temiz": {"sutun": "temiz", "satirlar": [], "sayim": {}, "cevrilecek": []},
       "cozumsuz": {"sutun": "cozulemez", "satirlar": [("UYARI", "genel-yol", "x")], "sayim": {}, "cevrilecek": []},
       "istisnali": {"sutun": "istisna", "satirlar": [("BİLGİ", "yol-istisna", "x")], "sayim": {}, "cevrilecek": []},
       "yazar": {"sutun": "yalniz-sayim", "satirlar": [("UYARI", "genele-yazabilir", "cp ... ~/.claude/skills")], "sayim": {}, "cevrilecek": []},
       "eski": {"sutun": "istisna", "satirlar": [("UYARI", "istisna-eskidi", "hash")], "sayim": {}, "cevrilecek": []},
       "bilgi": {"sutun": "temiz", "satirlar": [("BİLGİ", "kardes-yol", "x"), ("UYARI", "eklenti-koku", "y")], "sayim": {}, "cevrilecek": []}}


def sahte_deg(s, skiller, kurulacak_idler=None, istisnalar=None):
    if s["id"] == "patlar":
        raise RuntimeError("patladı")
    return DEG[s["id"]]


def yol_cal(argv):
    with yama(yt, REGISTRY=yk / "registry.json", GECICI=yk / "gecici", KOK=yk), yama(ortak, yol_degerlendir=sahte_deg, _TAKMA_ADLAR={}), \
            yama(yt.ortak, skill_yol_taramasi=lambda s, sk: [], skill_adlari=lambda s, sk: [s["id"]], istisna_anahtari=lambda s: s["id"],
                 yol_istisnalari=lambda: {}):
        return argv_ile(["yol-tara.py"] + argv, yt.main)


s_cozumsuz = yol_cal(["--skill", "cozumsuz", "--siki"])
s_cozumsuz0 = yol_cal(["--skill", "cozumsuz"])
s_temiz = yol_cal(["--skill", "temiz", "--siki"])
s_istisna = yol_cal(["--skill", "istisnali", "--siki"])
s_repo_hic = yol_cal(["--repo", "yok/yok", "--siki"])
s_yalniz = yol_cal(["--siki"])
s_yazar = yol_cal(["--repo", "o/r3", "--siki"])
s_eski = yol_cal(["--repo", "o/r4", "--siki"])
s_bilgi = yol_cal(["--repo", "o/r5", "--siki"])
s_repo_karma = yol_cal(["--repo", "o/r", "--siki"])
test("31. varsayılan çıkış kodları: --skill değersiz/--bogus/bilinmeyen skill 0 ve rapor dosyası yazılmaz",
     yol_cal(["--skill"])[0] == 0 and yol_cal(["--bogus"])[0] == 0 and yol_cal(["--skill", "yok-boyle-skill"])[0] == 0
     and not (yk / "notlar").exists() and s_cozumsuz0[0] == 0, (yol_cal(["--skill"]), s_cozumsuz0))
with yama(yt, REGISTRY=yk / "registry.json", GECICI=yk / "gecici", KOK=yk), yama(ortak, yol_degerlendir=sahte_deg, _TAKMA_ADLAR={}):
    kp = yt.kapi_kontrol(repo="o/r3")
    kp_hic = yt.kapi_kontrol(repo="yok/yok")
    kp_ok = yt.kapi_kontrol(skill_id="temiz")
test("32. --siki: çözülemez TAKILDI+1; --siki'siz 0; temiz/istisna GEÇTİ+0; repo yok 1; yalnız --siki 2; genele-yazabilir ve istisna-eskidi sayılır; BİLGİ ve eklenti-koku sayılmaz",
     s_cozumsuz[0] == 1 and "YOL KAPISI: TAKILDI" in s_cozumsuz[1] and "KAPI: cozumsuz" in s_cozumsuz[1] and s_cozumsuz0[0] == 0
     and s_temiz[0] == 0 and "YOL KAPISI: GEÇTİ (1 skill tarandı)" in s_temiz[1] and s_istisna[0] == 0
     and s_repo_hic[0] == 1 and "TAKILDI (taranamadı" in s_repo_hic[1] and s_yalniz[0] == 2 and "--siki için" in s_yalniz[1]
     and s_yazar[0] == 1 and s_eski[0] == 1 and s_bilgi[0] == 0 and s_repo_karma[0] == 1
     and kp[0] and kp[1] == 1 and kp[2] is None and kp_hic[2] and kp_hic[1] == 0 and kp_ok == ([], 1, None),
     (s_cozumsuz, s_temiz, s_istisna, s_repo_hic, s_yalniz, s_yazar, s_eski, s_bilgi, kp, kp_hic))
# çökme: --siki altında istisna 1
yaz(yk / "registry.json", {"skiller": [{"id": "patlar", "ad": "patlar", "repo": "o/p", "durum": "tercih", "kaynak_yol": "z"}]})
s_cokme = yol_cal(["--skill", "patlar", "--siki"])
yaz(yk / "registry.json", "{bozuk")
s_bozuk = yol_cal(["--repo", "o/r", "--siki"])
test("32b. tarama sırasında istisna ya da bozuk registry --siki'de 1 (hiçbir şey taranmadı 'geçti' sayılmaz)",
     s_cokme[0] == 1 and "TAKILDI" in s_cokme[1] and s_bozuk[0] == 1 and "TAKILDI" in s_bozuk[1], (s_cokme, s_bozuk))

# ------------------------------------------------------------------ listeye-ekle
lk = TMP / "le"
lk.mkdir()
yaz(lk / "k.json", {"repolar": [], "github_skill_listesi": "yapay-zeka-skillleri"})
cagri = []
LISTELER = [{"id": "L1", "name": "Yapay Zeka Skillleri", "slug": "yapay-zeka-skillleri", "items": {"nodes": []}},
            {"id": "L2", "name": "Korunan", "slug": "korunan", "items": {"nodes": [{"nameWithOwner": "Owner/repo"}]}}]


def sahte_gql(q, **kw):
    if "viewer" in q:
        return {"data": {"viewer": {"lists": {"nodes": [{"slug": "yapay-zeka-skillleri", "description": "d"}]}}}}
    cagri.append(kw)
    return {}


class Sonuc:
    def __init__(self, rc=0, out="", err=""):
        self.returncode, self.stdout, self.stderr = rc, out, err


def sahte_run(args, **kw):
    if "repos/" in " ".join(args):
        return Sonuc(0, '{"id":"NODE1"}')
    return Sonuc(0)


eski_input = builtins.input
builtins.input = lambda *a: "e"
try:
    with yama(le, KAYNAKLAR=lk / "k.json"), yama(le.gsl, listeler=lambda: LISTELER, gql=sahte_gql), yama(le.subprocess, run=sahte_run):
        r33, o33, _ = argv_ile(["listeye-ekle.py", "owner/Repo"], le.main)
        r33b, _, _ = argv_ile(["listeye-ekle.py", "OWNER/REPO"], le.main)
finally:
    builtins.input = eski_input
test("33. küçük/büyük harf farklı yazımda korunan liste üyeliği düşmez (hedef + korunan birlikte gönderilir)",
     r33 == 0 and r33b == 0 and len(cagri) == 2 and all(c["l"] == ["L1", "L2"] for c in cagri) and all(c["item"] == "NODE1" for c in cagri), (r33, cagri, o33))

# ------------------------------------------------------------------ belgeler
r03 = (KOK / "rehber" / "03-yeni-skill-ekleme.md").read_text(encoding="utf-8")
p07 = (KOK / "promptlar" / "07-yeni-skill-reposu-ekle.md").read_text(encoding="utf-8")
p14 = KOK / "promptlar" / "14-kaynak-cikar.md"
r09 = (KOK / "rehber" / "09-ad-kimlik-ve-cakisma.md").read_text(encoding="utf-8")


def sirali(metin):
    m = [re.search(rf"(?m)^(?:\d+\. )?A{i}[ :]", metin) for i in range(1, 10)]
    pos = [k.start() if k else -1 for k in m]
    return all(p >= 0 for p in pos) and pos == sorted(pos)


def sirali_p(metin):
    pos = [metin.find(t) for t in ("A1:", "A2:", "A3:", "A4-A8", "A8:", "A9:")]
    return all(p >= 0 for p in pos) and pos == sorted(pos)


hk = subprocess.run([sys.executable, str(ARACLAR / "kaynak-cikar.py"), "--help"], capture_output=True, text=True)
hy = subprocess.run([sys.executable, str(ARACLAR / "yol-tara.py"), "--help"], capture_output=True, text=True)
test("34. rehber/03 ve promptlar/07 A1..A9 sırayla; A17/find yok; kaynak-cikar/YOL KAPISI geçiyor; promptlar/14 var; --help çalışır; rehber/09 tamam",
     re.search(r"A1\b", r03) and sirali(r03) and sirali_p(p07) and "A17" not in r03 + p07 and "find ~ -path" not in r03 + p07
     and "kaynak-cikar.py --repo" in r03 and "YOL KAPISI" in r03 and p14.exists() and "rehber/03-yeni-skill-ekleme.md" in p14.read_text(encoding="utf-8")
     and hk.returncode == 0 and "--kuru" in hk.stdout and "yalnız" in hk.stdout and hy.returncode == 0 and "--siki" in hy.stdout
     and "programlar.json" in r09 and "konu-takip.json" in r09 and "Kaynak çıkarılırsa" in r09,
     (hk.stderr[:100], hy.stderr[:100]))

yardim_ok, yardim_ayrinti = True, []
for ad_ in ("konu-takip", "github-trend", "populer-tarama"):
    onceki = {n: (KOK / n).stat().st_mtime if (KOK / n).exists() else None for n in ("konu-takip.json", "trend.json", "notlar/konu-takip.md", "notlar/github-trend.md", "notlar/populer-skiller.md")}
    rh = subprocess.run([sys.executable, str(ARACLAR / f"{ad_}.py"), "--help"], capture_output=True, text=True, timeout=30)
    sonra_ = {n: (KOK / n).stat().st_mtime if (KOK / n).exists() else None for n in onceki}
    if rh.returncode != 0 or not rh.stdout.strip() or onceki != sonra_:
        yardim_ok = False
        yardim_ayrinti.append(ad_)
test("35. konu-takip/github-trend/populer-tarama --help tarama başlatmaz, dosya yazmaz", yardim_ok, yardim_ayrinti)

shutil.rmtree(TMP, ignore_errors=True)
print(f"{gecen}/{toplam} test geçti")
sys.exit(0 if gecen == toplam else 1)
