#!/usr/bin/env python3
"""P11 testleri: program-denetim.py 'uv-tool' yerinde türü (PyPI paketi, uv tool ortamı) ve kart alanı 'skill_klasorleri'
(skill adı -> skill_koku altındaki klasör adı; skill-ekle.py, program-denetim.py ve proje-kullanimi.py aynı hedefi hesaplar).
Yalnız geçici klasör ve sahte veri: HOME geçici klasöre alınır; sahte uv tool ağacı, sahte program klasörü, sahte programlar.json;
urlopen ve pypi_* sahtelenir (gerçek ev klasörü, gerçek kartlar ve ağ kullanılmaz). Sahte program klasörü HER işlemden sonra aynı kalmalı.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import copy
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import types
import urllib.error
from datetime import date
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))
os.environ["GIT_CONFIG_GLOBAL"] = "/dev/null"
os.environ["GIT_CONFIG_NOSYSTEM"] = "1"
TMP = Path(tempfile.mkdtemp(prefix="p11test-"))
EV = TMP / "home"
EV.mkdir()
os.environ["HOME"] = str(EV)                   # Path.home() / expanduser geçici klasöre baksın
gecen = toplam = 0


def test(ad, kosul, detay=""):
    global gecen, toplam
    toplam += 1
    if kosul:
        gecen += 1
    else:
        print(f"HATA: {ad} {str(detay)[-700:]}")


def modul_yukle(ad, yol):
    spec = importlib.util.spec_from_file_location(ad, yol)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


pd = modul_yukle("pd_p11", ARACLAR / "program-denetim.py")
se = modul_yukle("se_p11", ARACLAR / "skill-ekle.py")
pk = modul_yukle("pk_p11", ARACLAR / "proje-kullanimi.py")
import ortak  # noqa: E402


@contextlib.contextmanager
def yama(**kw):
    """pd modülü özniteliklerini geçici değiştir ('urllib.request.urlopen' için nokta kullan)."""
    eski = []
    for ad, deger in kw.items():
        hedef, _, nitelik = ad.rpartition("__")
        nesne = pd
        for parca in (hedef.split("_dot_") if hedef else []):
            nesne = getattr(nesne, parca)
        eski.append((nesne, nitelik, getattr(nesne, nitelik)))
        setattr(nesne, nitelik, deger)
    try:
        yield
    finally:
        for nesne, nitelik, v in reversed(eski):
            setattr(nesne, nitelik, v)


def pd_calistir(args):
    o, e = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e):
        try:
            kod = pd.main(args)
        except SystemExit as x:
            kod = x.code
    return kod, o.getvalue(), e.getvalue()


def klasor(ad):
    d = TMP / ad
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    return d


class Yanit:
    def __init__(self, veri):
        self.veri = veri

    def read(self):
        return json.dumps(self.veri).encode()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def urlopen_hata(hata):
    def f(*a, **k):
        raise hata
    return f


def yasak(*a, **k):
    raise AssertionError("ağa/ikinci kaynağa gidilmemeliydi")


# ------------------------------------------------------------------ sahte uv tool ağacı ve kart üretimi
SHA256 = "ab" * 32


def uv_agaci(ev, ad="pkgx", paket="pkg_x", surum="1.2.0", python="python3.12"):
    """ev/.local/share/uv/tools/<ad>/lib/<python>/site-packages/<paket>-<sürüm>.dist-info/METADATA; döner: tool klasörü."""
    tool = ev / ".local" / "share" / "uv" / "tools" / ad
    di = tool / "lib" / python / "site-packages" / f"{paket}-{surum}.dist-info"
    di.mkdir(parents=True)
    (di / "METADATA").write_text(f"Metadata-Version: 2.1\nName: {paket}\nVersion: {surum}\n\nAçıklama burada\nVersion: 9.9.9\n", encoding="utf-8")
    return tool


def doldur(v, ad, yol="", ek=None):
    ek = ek or {}
    if isinstance(v, dict):
        return {k: doldur(x, ad, f"{yol}.{k}" if yol else k, ek) for k, x in v.items()}
    if isinstance(v, list):
        return [doldur(x, ad, yol, ek) for x in v]
    if isinstance(v, str) and pd.YER_TUTUCU in v:
        if yol in ek:
            return ek[yol]
        return {"ad": ad, "repo": f"o/{ad}", "ucret": "ucretsiz", "giris_yolu.hepsi.durum": "yok"}.get(yol, "deger")
    return v


def uv_kart(ad, tool, paket="pkg-x", surum="1.2.0", **ek_alan):
    k = doldur(pd.iskelet("uv-tool"), ad, ek={"yerinde.yol": str(tool), "yerinde.paket": paket, "kutuphane_surumu": surum})
    k["guncelleme_adimlari"][0] = "program-denetim.py --oncesi çalıştırılır"
    k.update(ek_alan)
    return k


def kok_hazirla(kok, kartlar):
    kok = Path(kok)
    kayit = []
    for ad, k in kartlar.items():
        (kok / "programlar" / ad).mkdir(parents=True, exist_ok=True)
        (kok / "programlar" / ad / "KAYNAK.md").write_text(f"# {ad}\n{k.get('kutuphane_surumu', '')}\n", encoding="utf-8")
        kayit.append({"repo": k["repo"], "tip": "T5", "program": ad})
    (kok / "kaynaklar.json").write_text(json.dumps({"repolar": kayit}), encoding="utf-8")
    yol = kok / "kart.json"
    yol.write_text(json.dumps({"sema": 2, "programlar": kartlar}, ensure_ascii=False), encoding="utf-8")
    return yol


def sema(kartlar, kok):
    return pd.sema_denetle({"sema": 2, "programlar": kartlar}, kok=kok)


def hatalar(b):
    return [x for x in b if x[0] == "HATA"]


# ================================================================== U: uv-tool türü
print("U. uv-tool")
tool1 = uv_agaci(EV)
test("U1. kurulu sürüm METADATA 'Version:' satırından (ad normalleştirme: pkg-x = pkg_x; gövdedeki Version: sayılmaz)",
     pd.uv_kurulu_surum(tool1, "pkg-x") == "1.2.0" and pd.uv_kurulu_surum(tool1, "PKG_X") == "1.2.0", pd.uv_kurulu_surum(tool1, "pkg-x"))
test("U1. paket ya da klasör yoksa None", pd.uv_kurulu_surum(tool1, "baska") is None and pd.uv_kurulu_surum(EV / "yok-klasor", "pkg-x") is None)
test("U1. '~' yolu --ev (modül _EV) ile açılır", (lambda: (setattr(pd, "_EV", EV), pd.uv_kurulu_surum("~/.local/share/uv/tools/pkgx", "pkg-x"))[1])() == "1.2.0")
pd._EV = None
test("U1. 'uv-tool' YERINDE_TURLER ve OZET_TURLER içinde", "uv-tool" in pd.YERINDE_TURLER and "pypi-sha256" in pd.OZET_TURLER)

kart = uv_kart("kp", tool1)
with yama(pypi_son_surum=lambda *a, **k: None):
    r = pd.yerinde_denetle("kp", kart)
test("U2. kart = kurulu, son bilinmiyor -> 'öğrenilemedi'", r["durum"] == "öğrenilemedi" and r["kurulu"] == "1.2.0" and r["tur"] == "uv-tool", r)
with yama(pypi_son_surum=lambda *a, **k: "1.3.0"):
    test("U3. son 1.3.0 -> 'YENİ SÜRÜM VAR'", pd.yerinde_denetle("kp", kart)["durum"] == "YENİ SÜRÜM VAR")
with yama(pypi_son_surum=lambda *a, **k: "1.2.0"):
    test("U3. son 1.2.0 -> 'güncel'", pd.yerinde_denetle("kp", kart)["durum"] == "güncel")
with yama(pypi_son_surum=lambda *a, **k: "1.3.0"):
    test("U4. kart 1.1.0, kurulu 1.2.0 -> 'KART ESKİ'", pd.yerinde_denetle("kp", uv_kart("kp", tool1, surum="1.1.0"))["durum"] == "KART ESKİ")
with yama(pypi_son_surum=yasak):
    r = pd.yerinde_denetle("kp", uv_kart("kp", EV / "yok-tool"))
test("U5. klasör yok -> 'bu bilgisayarda kurulu değil' (PyPI'a sorulmaz)", r["durum"] == "bu bilgisayarda kurulu değil" and r["kurulu"] is None, r)

# PyPI son sürüm: ağ sınıflaması
istek = []
with yama(urllib_dot_request__urlopen=lambda u, **k: (istek.append((u, k)), Yanit({"info": {"version": "2.0.0"}}))[1]):
    s = pd.pypi_son_surum("paketx", 5)
test("U6. pypi_son_surum başarı: info.version; adres https://pypi.org/pypi/<paket>/json; zaman aşımı geçer; hata kaydı silinir",
     s == "2.0.0" and istek[0][0] == "https://pypi.org/pypi/paketx/json" and istek[0][1].get("timeout") == 5 and ("pypi", "paketx") not in pd._SON_HATA, istek)
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 404, "nf", {}, None))):
    test("U6. pypi_son_surum 404 -> None, sınıf '404'", pd.pypi_son_surum("paketx") is None and pd._SON_HATA[("pypi", "paketx")] == "404")
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.URLError("ag yok"))):
    test("U6. pypi_son_surum ağ hatası -> 'ag'", pd.pypi_son_surum("paketx") is None and pd._SON_HATA[("pypi", "paketx")] == "ag")
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 500, "x", {}, None))):
    test("U6. pypi_son_surum HTTP 500 -> 'ag' (404 değil)", pd.pypi_son_surum("paketx") is None and pd._SON_HATA[("pypi", "paketx")] == "ag")
with yama(urllib_dot_request__urlopen=lambda *a, **k: Yanit({"info": {}})):
    test("U6. pypi_son_surum bozuk yanıt -> None", pd.pypi_son_surum("paketx") is None)
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 404, "nf", {}, None))):
    r = pd.yerinde_denetle("kp", kart)
test("U6. son_hata sınıfı yerinde_denetle sonucunda ('404')", r.get("son_hata") == "404" and r["durum"] == "öğrenilemedi", r)

# PyPI wheel özeti
WHEEL = {"packagetype": "bdist_wheel", "filename": "pkg_x-1.2.0-py3-none-any.whl", "digests": {"sha256": SHA256.upper()}}
SDIST = {"packagetype": "sdist", "filename": "pkg_x-1.2.0.tar.gz", "digests": {"sha256": "cd" * 32}}
istek = []
with yama(urllib_dot_request__urlopen=lambda u, **k: (istek.append(u), Yanit({"urls": [SDIST, WHEEL]}))[1]):
    o = pd.pypi_ozet("pkg-x", "1.2.0")
test("U7. pypi_ozet: wheel'in sha256'sı (küçük harf), sdist değil; adres sürüme özgü", o == SHA256 and istek[0] == "https://pypi.org/pypi/pkg-x/1.2.0/json", (o, istek))
with yama(urllib_dot_request__urlopen=lambda *a, **k: Yanit({"urls": [dict(WHEEL, filename="pkg_x-1.2.0-cp312-macosx_arm64.whl"),
                                                                         dict(WHEEL, filename="pkg_x-1.2.0-cp312-win_amd64.whl")]})):
    test("U7. birden çok platform wheel'i ve py3-none-any yok -> None (belirsiz)", pd.pypi_ozet("pkg-x", "1.2.0") is None)
with yama(urllib_dot_request__urlopen=lambda *a, **k: Yanit({"urls": [SDIST]})):
    test("U7. wheel yok -> None", pd.pypi_ozet("pkg-x", "1.2.0") is None)
with yama(urllib_dot_request__urlopen=urlopen_hata(urllib.error.HTTPError("u", 404, "nf", {}, None))):
    test("U7. pypi_ozet 404 -> None, sınıf 'pypi-ozet' 404", pd.pypi_ozet("pkg-x", "9.9.9") is None and pd._SON_HATA[("pypi-ozet", "pkg-x")] == "404")

# şema
KOK_U = klasor("kok-u")
kart_g = uv_kart("kp", tool1)
kok_hazirla(KOK_U, {"kp": kart_g})
b = sema({"kp": kart_g}, KOK_U)
test("U8. geçerli uv-tool kartı: 0 HATA, 0 UYARI (--sema --siki)", not b, b[:3])
yol_u = KOK_U / "kart.json"
test("U8. --sema --siki çıkış 0", pd_calistir(["--sema", "--siki", "--kart", str(yol_u), "--kok", str(KOK_U)])[0] == 0)
k = copy.deepcopy(kart_g)
k["yerinde"]["paket"] = ""
b = sema({"kp": k}, KOK_U)
test("U8. yerinde.paket boş -> HATA", any(x[0] == "HATA" and x[2] == "yerinde.paket" for x in b), b)
k = copy.deepcopy(kart_g)
del k["yerinde"]["paket"]
b = sema({"kp": k}, KOK_U)
test("U8. yerinde.paket yok -> HATA", any(x[0] == "HATA" and x[2] == "yerinde.paket" for x in b), b)
k = copy.deepcopy(kart_g)
k["kutuphane_surumu"] = ""
test("U8. kutuphane_surumu boş -> HATA", any(x[0] == "HATA" and x[2] == "kutuphane_surumu" for x in sema({"kp": k}, KOK_U)))
k = copy.deepcopy(kart_g)
k["yerinde"]["tur"] = "uv-araci"
test("U8. bilinmeyen tür -> HATA, beklenenler arasında uv-tool", any(x[0] == "HATA" and "uv-tool" in x[3] for x in sema({"kp": k}, KOK_U)))
k = copy.deepcopy(kart_g)
k["tedarik_dogrulama"] = {"ozet": {"tur": "pypi-sha256", "deger": SHA256}}
test("U8. pypi-sha256 64 haneli özet: bulgu yok", not sema({"kp": k}, KOK_U))
k["tedarik_dogrulama"]["ozet"]["deger"] = "kisa"
b = sema({"kp": k}, KOK_U)
test("U8. pypi-sha256 bozuk özet -> yalnız UYARI", len(b) == 1 and b[0][0] == "UYARI" and b[0][2] == "tedarik_dogrulama.ozet.deger", b)

sk = pd.iskelet("uv-tool")
json.dumps(sk, ensure_ascii=False)
b = pd.sema_denetle({"sema": 2, "programlar": {pd.YER_TUTUCU: sk}}, kok=KOK)
test("U9. --iskelet uv-tool: geçerli JSON, yalnız 'doldurulmamış' bulguları; tür uv-tool, paket alanı var",
     b and all("doldurulmamış" in x[3] for x in b) and sk["yerinde"]["tur"] == "uv-tool" and "paket" in sk["yerinde"], b[:3])
kod, o, e = pd_calistir(["--iskelet", "uv-tool"])
test("U9. main --iskelet uv-tool çıkış 0 ve geçerli JSON", kod == 0 and json.loads(o)["yerinde"]["tur"] == "uv-tool")

# ön kontrol, tedarik
EV_O = klasor("ev-o")
tool_o = uv_agaci(EV_O)
kart_o = uv_kart("kp", tool_o, tedarik_dogrulama={"yayinci": {"hesap": "x", "ucuncu_taraf": True, "imza": "pypi-kayit"},
                                                  "ozet": {"tur": "pypi-sha256", "deger": SHA256}})
KOK_O = klasor("kok-o")
kok_hazirla(KOK_O, {"kp": kart_o})


def oncesi(kart, tedarik=True, cevrimdisi=False, hedef=None):
    ctx = pd._ctx(ev=EV_O, kok=KOK_O, yedek_koku=EV_O / "yedek", cevrimdisi=cevrimdisi, bugun=date(2026, 11, 12), hedef=hedef, tedarik=tedarik)
    return pd.oncesi_denetle("kp", kart, ctx)


def satir(S, kont, metin=""):
    return [x for x in S if x[1] == kont and metin in x[2]]


with yama(pypi_son_surum=lambda *a, **k: "1.2.0", pypi_ozet=lambda *a, **k: SHA256, gh_api=yasak, repo_durumu=lambda *a, **k: ("var", None)):
    S, sonuc = oncesi(kart_o)
test("U10. --oncesi uv-tool: kurulu 1.2.0, kart eşit, son aynı -> 'GÜNCELLENECEK BİR ŞEY YOK'; şema TAMAM",
     sonuc == "GÜNCELLENECEK BİR ŞEY YOK" and satir(S, "kurulu", "kurulu 1.2.0") and satir(S, "şema")[0][0] == "TAMAM", (sonuc, S[:4]))
cagri = []
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", pypi_ozet=lambda p, s, *a, **k: (cagri.append((p, s)), SHA256)[1],
          repo_durumu=lambda *a, **k: ("var", None)):
    S, sonuc = oncesi(kart_o, hedef="1.3.0")
test("U10. --hedef verilince tedarik o sürümün özetine bakılır; kayıtla aynıysa TAMAM",
     cagri == [("pkg-x", "1.3.0")] and satir(S, "tedarik", "kayıtla aynı"), (cagri, S))
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", pypi_ozet=lambda *a, **k: "ef" * 32, repo_durumu=lambda *a, **k: ("var", None)):
    S, sonuc = oncesi(kart_o)
test("U10. tedarik: PyPI özeti kayıttan farklıysa HATA ve HAZIR DEĞİL", satir(S, "tedarik", "farklı")[0][0] == "HATA" and sonuc == "HAZIR DEĞİL", S)
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", pypi_ozet=lambda *a, **k: None, repo_durumu=lambda *a, **k: ("var", None)):
    S, _ = oncesi(kart_o)
test("U10. tedarik: PyPI özeti alınamazsa UYARI (engel değil)", satir(S, "tedarik", "alınamadı")[0][0] == "UYARI")
with yama(pypi_son_surum=yasak, pypi_ozet=yasak, gh_api=yasak, repo_durumu=yasak):
    S, sonuc = oncesi(kart_o, cevrimdisi=True)
test("U10. çevrimdışı: PyPI'a hiç gidilmez, tedarik ATLANDI", satir(S, "tedarik", "çevrimdışı")[0][0] == "ATLANDI", S)
k2 = copy.deepcopy(kart_o)
k2["tedarik_dogrulama"]["ozet"]["deger"] = ""
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", pypi_ozet=yasak, repo_durumu=lambda *a, **k: ("var", None)):
    S, _ = oncesi(k2)
test("U10. özet değeri boşsa BİLGİ 'kayıtsız'", satir(S, "tedarik", "kayıtsız")[0][0] == "BİLGİ")
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", repo_durumu=lambda *a, **k: ("var", None)):
    S, sonuc = oncesi(uv_kart("kp", tool_o, surum="1.1.0"), tedarik=False)
test("U10. kart eski -> HATA 'kart' ve HAZIR DEĞİL", satir(S, "kart")[0][0] == "HATA" and sonuc == "HAZIR DEĞİL", S)
S, sonuc = oncesi(uv_kart("kp", EV_O / "yok-tool"), cevrimdisi=True)
test("U10. kurulu değilse 'KURULU DEĞİL'", sonuc == "KURULU DEĞİL", S)
k3 = copy.deepcopy(kart_o)
k3["yedek"]["zorunlu"] = ["KAYIT.json", "paket"]
yed = EV_O / "yedek" / "kp-2026-11-12"
(yed / "paket").mkdir(parents=True)
(yed / "paket" / "x").write_text("x")
(yed / "KAYIT.json").write_text(json.dumps({"program": "kp", "tarih": "2026-11-12", "onceki": {"surum": "1.2.0", "commit": ""}}), encoding="utf-8")
with yama(pypi_son_surum=lambda *a, **k: "1.3.0", pypi_ozet=lambda *a, **k: SHA256, repo_durumu=lambda *a, **k: ("var", None)):
    S, sonuc = oncesi(k3)
test("U10. yedek kaydı sürüm metniyle karşılaştırılır: yedek TAMAM; hazır (kırıcı adayı yalnız UYARI)", satir(S, "yedek")[0][0] == "TAMAM", S)

# rapor satırı, özet
yol_r = kok_hazirla(KOK_O, {"kp": kart_o})
with yama(pypi_son_surum=lambda *a, **k: "1.3.0"):
    kod, o, e = pd_calistir(["--kart", str(yol_r), "--cikti", str(KOK_O / "rapor.md"), "--kok", str(KOK_O), "--ev", str(EV_O)])
    kod2, o2, e2 = pd_calistir(["--ozet-json", "--kart", str(yol_r), "--kok", str(KOK_O), "--ev", str(EV_O)])
rapor = (KOK_O / "rapor.md").read_text(encoding="utf-8")
j = json.loads(o2)
test("U11. rapor: satır 'karttaki · kurulu · son · durum', tabloda uv-tool türü, ozet-json 'dikkat'",
     "kp: karttaki 1.2.0 · kurulu 1.2.0 · son 1.3.0 · YENİ SÜRÜM VAR" in o and "| kp | uv-tool | 1.2.0 | 1.2.0 | 1.3.0 | YENİ SÜRÜM VAR |" in rapor
     and j["durum"] == "dikkat" and any("1.2.0 -> 1.3.0" in x for x in j["karar_bekleyen"]), (o, rapor[:400], o2))
with yama(pypi_son_surum=yasak):
    kod, o, e = pd_calistir(["--oncesi", "kp", "--cevrimdisi", "--kart", str(yol_r), "--kok", str(KOK_O), "--ev", str(EV_O)])
test("U11. main --oncesi kp (uv-tool): çıkış 0, 'uv-tool' ve kurulu sürüm başlıkta", kod == 0 and "(uv-tool)" in o and "kurulu 1.2.0" in o, o)
test("U11. --pin-listesi uv-tool kartında (venv yok) etkilenmez: 2 çıkış kodu, hata iletisi", pd_calistir(["--pin-listesi", "kp", "--kart", str(yol_r)])[0] == 2)

# ================================================================== E: skill_klasorleri eşlemesi
print("E. klasör eşleme")
SAHTE_TOOL = EV / "nlmx"
SITE = SAHTE_TOOL / "lib" / "python3.12" / "site-packages" / "notebooklm_tools"


def fm(ad):
    return f"---\nname: {ad}\ndescription: test skill\n---\n"


def skill_yaz(alan, klasor_adi, skill_adi=None, icerik="x\n"):
    d = alan / klasor_adi
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(fm(skill_adi or klasor_adi) + icerik, encoding="utf-8")
    (d / "references").mkdir(exist_ok=True)
    (d / "references" / "a.md").write_text("ref\n", encoding="utf-8")
    return d


skill_yaz(SITE, "data", "nlm-skill")
(SITE / "data" / "AGENTS_SECTION.md").write_text("agents\n", encoding="utf-8")
skill_yaz(SITE, "ek", "ek-skill")                                   # eşlemesiz ikinci skill: klasör adı = skill adı
(SITE / "cli").mkdir()
(SITE / "cli" / "x.py").write_text("x\n", encoding="utf-8")
DUZ = TMP / "duz" / "skills"                                        # eşlemesiz sahte program
skill_yaz(DUZ, "ffmpeg")
skill_yaz(DUZ, "nlm-skill")                                         # eşlemesiz programda skill adı = klasör adı

KOTU = TMP / "kotu" / "skills"                                      # geçersiz eşleme kartları: dışarı kaçılırsa bulunacak 'data' klasörleri hazır
skill_yaz(KOTU, "data", "nlm-skill")
skill_yaz(TMP / "kotu", "data", "nlm-skill")
skill_yaz(KOTU / "a", "data", "nlm-skill")
KART_ESLEME = {"sema": 2, "programlar": {
    "sahte": {"ad": "sahte", "kopya": "yerinde", "yerinde": {"tur": "uv-tool", "yol": "~/nlmx", "paket": "notebooklm-mcp-cli"},
              "kutuphane_surumu": "0.15.8", "skill_koku": "~/nlmx/lib/python3.12/site-packages/notebooklm_tools",
              "skill_klasorleri": {"nlm-skill": "data"}},
    "duz": {"ad": "duz", "yerinde": {"tur": "npm-global", "yol": "x", "paket": "x"}, "kutuphane_surumu": "1.0.0", "skill_koku": str(DUZ)},
    "kotu1": {"ad": "kotu1", "skill_koku": str(KOTU), "skill_klasorleri": {"nlm-skill": "../data"}},
    "kotu2": {"ad": "kotu2", "skill_koku": str(KOTU), "skill_klasorleri": {"nlm-skill": "a/data"}},
    "kotu3": {"ad": "kotu3", "skill_koku": str(KOTU), "skill_klasorleri": {"nlm-skill": ""}},
    "kotu4": {"ad": "kotu4", "skill_koku": str(KOTU), "skill_klasorleri": {"nlm-skill": str(KOTU / "data")}},
    "kotu5": {"ad": "kotu5", "skill_koku": str(KOTU), "skill_klasorleri": {"nlm-skill": ".."}},
}}
KART_YOL = TMP / "programlar-esleme.json"
KART_YOL.write_text(json.dumps(KART_ESLEME), encoding="utf-8")
se.PROGRAMLAR = KART_YOL
pk.PROGRAMLAR = KART_YOL

SAHTE_KAYIT = []
se.canli_global = lambda s: {}
se.hesap_skilleri = lambda: {}
se.guncelleme_suruyor = lambda: None
se.registry = lambda: SAHTE_KAYIT
se.ARAC_JSON = TMP / "yok-araclar.json"


def agac(d: Path):
    s = {}
    for p in sorted(d.rglob("*")):
        rel = str(p.relative_to(d))
        s[rel] = ("symlink->" + str(p.readlink())) if p.is_symlink() else (p.read_bytes() if p.is_file() else "dir")
    return s


def koruma():
    return (agac(SAHTE_TOOL), agac(TMP / "duz"), agac(TMP / "kotu"))


KORUMA = koruma()


def se_calistir(*args):
    eski, eski_in = sys.argv, sys.stdin
    sys.argv = ["skill-ekle.py"] + [str(a) for a in args]
    sys.stdin = io.StringIO("")
    out, err = io.StringIO(), io.StringIO()
    kod = 0
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                kod = se.main() or 0
            except SystemExit as e:
                kod = e.code if isinstance(e.code, int) else (0 if e.code is None else 2)
                if isinstance(e.code, str):
                    print(e.code)
    finally:
        sys.argv, sys.stdin = eski, eski_in
    return kod, out.getvalue() + err.getvalue()


def yeni_proje():
    return Path(tempfile.mkdtemp(dir=TMP, prefix="proje-"))


def kilit_oku(p):
    return json.loads((p / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))


HEDEF = SITE / "data"
# ortak yardımcı
kart_s = KART_ESLEME["programlar"]["sahte"]
test("E1. ortak.program_skill_klasoru: eşlemede varsa eşlenen ad, yoksa skill adı",
     ortak.program_skill_klasoru(kart_s, "nlm-skill") == "data" and ortak.program_skill_klasoru(kart_s, "ek-skill") == "ek-skill"
     and ortak.program_skill_klasoru({"skill_koku": "x"}, "ffmpeg") == "ffmpeg" and ortak.program_skill_klasoru(None, "a") == "a")
test("E1. ortak: ham klasör adı tanınır, skill adı ham sayılmaz; ters eşleme",
     ortak.program_skill_ham_klasoru_mu(kart_s, "data") and not ortak.program_skill_ham_klasoru_mu(kart_s, "nlm-skill")
     and not ortak.program_skill_ham_klasoru_mu(kart_s, "ek") and ortak.program_klasor_skill_adi(kart_s, "data") == "nlm-skill"
     and ortak.program_klasor_skill_adi(kart_s, "ek") == "ek")
for ad_, kart_ in (("kotu1", KART_ESLEME["programlar"]["kotu1"]), ("kotu2", KART_ESLEME["programlar"]["kotu2"]), ("kotu3", KART_ESLEME["programlar"]["kotu3"]),
                   ("kotu4", KART_ESLEME["programlar"]["kotu4"]), ("kotu5", KART_ESLEME["programlar"]["kotu5"])):
    test(f"E1. ortak: geçersiz eşleme ({ad_}) hata listesinde, geçerli eşlemeye sayılmaz",
         bool(ortak.skill_klasorleri_hatalari(kart_)) and ortak.program_skill_klasoru(kart_, "nlm-skill") == "nlm-skill", ortak.skill_klasorleri_hatalari(kart_))
test("E1. ortak: eşleme alanı yoksa hata yok; sözlük değilse hata",
     ortak.skill_klasorleri_hatalari({}) == [] and bool(ortak.skill_klasorleri_hatalari({"skill_klasorleri": ["data"]})))
test("E1. ortak: iki skill aynı klasöre -> hata; anahtar geçersiz skill adı -> hata",
     bool(ortak.skill_klasorleri_hatalari({"skill_klasorleri": {"a": "d", "b": "d"}})) and bool(ortak.skill_klasorleri_hatalari({"skill_klasorleri": {"a/b": "d"}})))

# --- skill-ekle: kuru ve kurulum
p = yeni_proje()
once = agac(p)
k, o = se_calistir(p, "--program-skill", "sahte:nlm-skill", "--kuru")
test("E2. --kuru: hedef .../notebooklm_tools/data gösterilir, skill adı nlm-skill, hata yok, proje ve program değişmez",
     k == 2 and "[kuru]" in o and "notebooklm_tools/data" in o and "sahte:nlm-skill" in o and "HATA" not in o and agac(p) == once and koruma() == KORUMA, o)
p = yeni_proje()
k, o = se_calistir(p, "--program-skill", "sahte:nlm-skill", "--arac", "yalniz-claude", "--evet")
c = p / ".claude" / "skills" / "nlm-skill"
g = kilit_oku(p).get("dis_skiller", {}).get("nlm-skill", {})
test("E3. --evet: bağın ADI nlm-skill, hedefi data klasörü (SKILL.md görünür); kilit hedefi data; proje içinde 'data' adlı bağ yok",
     k == 0 and c.is_symlink() and os.readlink(c) == str(HEDEF) and (c / "SKILL.md").exists() and (c / "references" / "a.md").exists()
     and g.get("hedef") == str(HEDEF) and g.get("ad") == "nlm-skill" and g.get("program") == "sahte" and not (p / ".claude" / "skills" / "data").exists()
     and koruma() == KORUMA, o)
kd, od = se_calistir(p, "--dogrula")
test("E4. --dogrula temiz (bağ çözülüyor)", kd == 0, od)
kd2, od2 = se_calistir(p, "--durum")
test("E4. --durum nlm-skill satırı, kırık değil", kd2 == 0 and "nlm-skill" in od2 and "BAĞ KIRIK" not in od2, od2)
k, o = se_calistir(p, "--yenile")
test("E4. --yenile bağı bozmaz: aynı hedef, dogrula temiz", k == 0 and os.readlink(c) == str(HEDEF) and se_calistir(p, "--dogrula")[0] == 0 and koruma() == KORUMA, o)
k, o = se_calistir(p, "--guncelle", "--kuru")
test("E4. --guncelle --kuru bağ için hata vermez", "kirik" not in o.lower().replace("kırık", "kirik") or "HATA" not in o, o)
c.unlink()
kd, od = se_calistir(p, "--dogrula")
test("E4. bağ elle silinirse --dogrula yakalar (eksik), --yenile onarır", kd == 1 and se_calistir(p, "--yenile")[0] == 0 and c.is_symlink()
     and os.readlink(c) == str(HEDEF) and se_calistir(p, "--dogrula")[0] == 0, od)
k, o = se_calistir(p, "--kaldir", "nlm-skill", "--evet")
test("E5. --kaldir nlm-skill: bağ gitti, kilitten çıktı, program klasörü (data dahil) bayt bayt aynı",
     k == 0 and not c.is_symlink() and "nlm-skill" not in kilit_oku(p).get("dis_skiller", {}) and koruma() == KORUMA and (HEDEF / "SKILL.md").is_file(), o)

# ham klasör adı, eşlemesiz ad, olmayan ad
p = yeni_proje()
once = agac(p)
k, o = se_calistir(p, "--program-skill", "sahte:data", "--evet")
test("E6. ham klasör adı (sahte:data) reddedilir: program-skill-ham-klasor, doğru ad sahte:nlm-skill söylenir, hiçbir şey kurulmaz",
     k != 0 and "program-skill-ham-klasor" in o and "--program-skill sahte:nlm-skill" in o and agac(p) == once and not (p / ".claude").exists(), o)
k, o = se_calistir(p, "--program-skill", "sahte:data", "--evet", "--zorla")
test("E6. --zorla ham klasör reddini geçemez", k != 0 and "program-skill-ham-klasor" in o and agac(p) == once, o)
k, o = se_calistir(p, "--program-skill", "sahte:yok-boyle", "--evet")
liste = [x for x in o.splitlines() if "Programdaki skiller:" in x]
test("E7. olmayan ad: 'Programdaki skiller' listesinde eşlenen klasör skill adıyla (nlm-skill), ham adıyla (data) değil; cli (SKILL.md yok) yok",
     k != 0 and "program-skill-yok" in o and liste and "nlm-skill" in liste[0] and "ek" in liste[0] and "data" not in liste[0] and "cli" not in liste[0], o)
p = yeni_proje()
k, o = se_calistir(p, "--program-skill", "sahte:ek-skill", "--evet")
test("E7. eşlemesi olmayan skill adı (ek-skill) klasör 'ek' ... bulunamaz (klasör adı skill adı olmak zorunda): eski davranış", k != 0 and "program-skill-yok" in o, o)
p = yeni_proje()
k, o = se_calistir(p, "--program-skill", "sahte:ek", "--arac", "yalniz-claude", "--evet")
test("E7. eşlemesiz klasör adı (ek) eskisi gibi kurulur: hedef .../notebooklm_tools/ek", k == 0 and os.readlink(p / ".claude" / "skills" / "ek") == str(SITE / "ek"), o)

# eşleme alanı olmayan kart: eski davranış aynı
p = yeni_proje()
k, o = se_calistir(p, "--program-skill", "duz:ffmpeg", "duz:nlm-skill", "--arac", "yalniz-claude", "--evet")
test("E8. eşlemesiz kart: skill_koku/<ad> (ffmpeg ve nlm-skill), eski davranış aynı; program değişmedi",
     k == 0 and os.readlink(p / ".claude" / "skills" / "ffmpeg") == str(DUZ / "ffmpeg") and os.readlink(p / ".claude" / "skills" / "nlm-skill") == str(DUZ / "nlm-skill")
     and se_calistir(p, "--dogrula")[0] == 0 and koruma() == KORUMA, o)
p = yeni_proje()
k, o = se_calistir(p, "--program-skill", "duz:yok", "--evet")
liste = [x for x in o.splitlines() if "Programdaki skiller:" in x]
test("E8. eşlemesiz kartta 'Programdaki skiller' klasör adlarıdır (ffmpeg, nlm-skill)", k != 0 and liste and "ffmpeg" in liste[0] and "nlm-skill" in liste[0], o)

# geçersiz eşleme: kurulumda reddedilir, şemada HATA
for ad_ in ("kotu1", "kotu2", "kotu3", "kotu4", "kotu5"):
    p = yeni_proje()
    once = agac(p)
    k, o = se_calistir(p, "--program-skill", f"{ad_}:nlm-skill", "--evet")
    test(f"E9. geçersiz eşleme ({ad_}) kurulumda reddedilir: eşleme yok sayılır, skill adı klasörü yok -> program-skill-yok; dışarı çıkılmaz",
         k != 0 and "program-skill-yok" in o and agac(p) == once and koruma() == KORUMA, o)
sema_kartlar = {}
for ad_, v in (("e1", "../x"), ("e2", "a/b"), ("e3", ""), ("e4", "/mutlak/yol"), ("e5", "."), ("e6", ".."), ("e7", 5), ("e8", "a\\b"), ("e9", "ad ile bosluk")):
    kk = uv_kart(ad_, tool1, skill_klasorleri={"nlm-skill": v})
    sema_kartlar[ad_] = kk
KOK_E2 = klasor("kok-e2")
kok_hazirla(KOK_E2, sema_kartlar)
for ad_, kk in sema_kartlar.items():
    b = pd.sema_denetle({"sema": 2, "programlar": {ad_: kk}}, kok=KOK_E2)
    test(f"E10. şema: geçersiz skill_klasorleri değeri ({kk['skill_klasorleri']['nlm-skill']!r}) HATA verir",
         any(x[0] == "HATA" and x[2].startswith("skill_klasorleri") for x in b), b)
kk = uv_kart("ea", tool1, skill_klasorleri={"nlm-skill": "data"}, skilleri=["nlm-skill"])
kok_hazirla(KOK_E2, {"ea": kk})
test("E10. şema: geçerli eşleme {'nlm-skill': 'data'} bulgu vermez", not pd.sema_denetle({"sema": 2, "programlar": {"ea": kk}}, kok=KOK_E2))
for ad_, v in (("eb", {"a/b": "data"}), ("ec", ["data"]), ("ed", {"a": "d", "b": "d"}), ("ee", "data")):
    kk = uv_kart(ad_, tool1, skill_klasorleri=v)
    kok_hazirla(KOK_E2, {ad_: kk})
    test(f"E10. şema: geçersiz yapı {v!r} HATA", bool(hatalar(pd.sema_denetle({"sema": 2, "programlar": {ad_: kk}}, kok=KOK_E2))))
kod, o, e = pd_calistir(["--sema", "--siki", "--kart", str(KOK_E2 / "kart.json"), "--kok", str(KOK_E2)])
test("E10. --sema --siki geçersiz eşlemede çıkış 1", kod == 1)

# dondur: program skili için doğru ad önerilir
p = yeni_proje()
k, o = se_calistir(p, "--dondur", str(HEDEF), "--evet")
test("E11. --dondur <program>/data: dondur-program-skili, önerilen ad nlm-skill (ham 'data' değil); hiçbir şey kurulmaz",
     k != 0 and "dondur-program-skili" in o and "--program-skill sahte:nlm-skill" in o and "sahte:data" not in o and not (p / ".claude").exists(), o)

# --- üç araç aynı hedefi hesaplar
g_kilit = {"ad": "nlm-skill", "tur": "program-bag", "program": "sahte", "hedef": str(HEDEF)}
h_se = se.dis_bag_hedefi(g_kilit)
ctx = pd._ctx(ev=EV, kok=TMP / "bos-kok")
h_pd = pd.bag_hedefi(KART_ESLEME["programlar"]["sahte"], ctx, "nlm-skill")
h_pk = pk._program_hedefi("sahte", "nlm-skill")
test("E12. üç araç aynı bağ hedefini hesaplar (skill-ekle, program-denetim, proje-kullanimi): .../notebooklm_tools/data",
     str(h_se) == h_pd == str(h_pk) == str(HEDEF), (h_se, h_pd, h_pk))
g2 = {"ad": "ffmpeg", "tur": "program-bag", "program": "duz", "hedef": str(DUZ / "ffmpeg")}
test("E12. eşlemesiz kartta üçü de skill_koku/<ad> (eski davranış)",
     str(se.dis_bag_hedefi(g2)) == pd.bag_hedefi(KART_ESLEME["programlar"]["duz"], ctx, "ffmpeg") == str(pk._program_hedefi("duz", "ffmpeg")) == str(DUZ / "ffmpeg"))
test("E12. program-denetim: geçersiz skill adı hedefi None", pd.bag_hedefi(KART_ESLEME["programlar"]["sahte"], ctx, "../x") is None)

# program-denetim 'bağlar' satırları: eşlemeli hedef çözülüyor
baglar = [{"proje": "demo", "skill": "nlm-skill", "program": "sahte", "surum": "0.15.8", "tur_surum": "surum"}]
with yama(proje_baglari=lambda c: baglar):
    S = pd.bag_simdi("sahte", KART_ESLEME["programlar"]["sahte"], ctx, "HATA")
    liste_b = pd.program_baglari("sahte", KART_ESLEME["programlar"]["sahte"], ctx)
test("E13. program-denetim 'bağlar': eşlemeli bağ çözülüyor (TAMAM, hedef var)", S and S[0][0] == "TAMAM" and liste_b[0][2] is True and liste_b[0][1] == str(HEDEF), (S, liste_b))
kart_eslemesiz = {k_: v for k_, v in KART_ESLEME["programlar"]["sahte"].items() if k_ != "skill_klasorleri"}
with yama(proje_baglari=lambda c: baglar):
    S = pd.bag_simdi("sahte", kart_eslemesiz, ctx, "HATA")
test("E13. aynı bağ eşleme olmadan kırık görünür (hedef .../nlm-skill yok): eşleme gerçekten kullanılıyor", S and S[0][0] == "HATA" and "kırık" in S[0][2], S)

# program-denetim --oncesi: eşlemeli bağ git değil -> bilgi; bag_kirilacak git yolunda klasör adı eşlenir
git_arg = []
kart_git = {"skill_koku": str(TMP / "repo" / "skills"), "skill_klasorleri": {"nlm-skill": "data"}, "yerinde": {"tur": "git-checkout", "yol": str(TMP / "repo")}}
with yama(proje_baglari=lambda c: baglar, git_okuma=lambda yol, *a: (git_arg.append(a), "" if a[0] == "cat-file" else None)[1]):
    S = pd.bag_kirilacak("sahte", kart_git, ctx, "a" * 40, "b" * 40, True, kart_git["yerinde"])
test("E13. bag_kirilacak (git): hedef sürümde eşlenen klasör aranır (skills/data/SKILL.md)",
     any(a[0] == "cat-file" and a[-1].endswith("skills/data/SKILL.md") for a in git_arg), git_arg)

# proje-kullanimi --program raporu
proje_pk = yeni_proje()
k, o = se_calistir(proje_pk, "--program-skill", "sahte:nlm-skill", "--arac", "yalniz-claude", "--evet")
ayar = TMP / "projeler-pk.json"
ayar.write_text(json.dumps({"ek_projeler": [str(proje_pk)]}), encoding="utf-8")
pk.AYAR = ayar
cikti = io.StringIO()
with contextlib.redirect_stdout(cikti):
    pk._program_kipi(types.SimpleNamespace(program="sahte", siki=False))
test("E14. proje-kullanimi --program sahte: nlm-skill bağı 'hedef var' (eşlemeli klasör)", "nlm-skill" in cikti.getvalue() and "hedef var" in cikti.getvalue() and "YOK" not in cikti.getvalue(), cikti.getvalue())
# program-denetim aynı projeyi gerçek kilitten okur
kok_pd = klasor("kok-pd")
(kok_pd / "projeler.json").write_text(json.dumps({"ek_projeler": [str(proje_pk)]}), encoding="utf-8")
ctx2 = pd._ctx(ev=EV, kok=kok_pd)
bl = pd.program_baglari("sahte", KART_ESLEME["programlar"]["sahte"], ctx2)
test("E14. program-denetim gerçek kilitten aynı bağı bulur: skill nlm-skill, hedef data, var", len(bl) == 1 and bl[0][0]["skill"] == "nlm-skill" and bl[0][1] == str(HEDEF) and bl[0][2], bl)
k, o = se_calistir(proje_pk, "--kaldir", "nlm-skill", "--evet")
test("E14. temizlik: --kaldir sonrası program yine aynı", k == 0 and koruma() == KORUMA, o)

# gerçek kart: skill_klasorleri yalnız nlm'de ve geçerli (salt okuma)
gercek = json.loads((KOK / "programlar.json").read_text(encoding="utf-8"))["programlar"]
test("E15. gerçek programlar.json: nlm kartı uv-tool, skill_klasorleri {'nlm-skill': 'data'}, skilleri ['nlm-skill'], skill_koku notebooklm_tools",
     gercek["nlm"]["yerinde"]["tur"] == "uv-tool" and gercek["nlm"]["skill_klasorleri"] == {"nlm-skill": "data"} and gercek["nlm"]["skilleri"] == ["nlm-skill"]
     and gercek["nlm"]["skill_koku"].endswith("site-packages/notebooklm_tools") and not ortak.skill_klasorleri_hatalari(gercek["nlm"])
     and gercek["nlm"]["tedarik_dogrulama"]["ozet"]["tur"] == "pypi-sha256")
test("E15. gerçek kartlarda başka program skill_klasorleri taşımıyor (OpenMontage, HyperFrames eskisi gibi)",
     all("skill_klasorleri" not in v for a_, v in gercek.items() if a_ != "nlm"))

shutil.rmtree(TMP, ignore_errors=True)
print(f"{gecen}/{toplam} test geçti")
sys.exit(0 if gecen == toplam else 1)
