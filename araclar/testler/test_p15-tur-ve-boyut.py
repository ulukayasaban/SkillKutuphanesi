#!/usr/bin/env python3
"""P15 testleri: tur-belirle.py (saf karar işlevi), boyut-hesapla.py (saf işlevler, sahte npm/PyPI/HF yanıtı, yerel disk),
dogrula.py kaynak tür/bölüm/boyut şema denetimi. Ağ yok, gerçek ev klasörü yok; yalnız sahte veri ve geçici klasör.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import importlib.util
import json
import os
import shutil
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


tb = yukle("tur_belirle_t", "tur-belirle.py")
bh = yukle("boyut_hesapla_t", "boyut-hesapla.py")
dg = yukle("dogrula_t", "dogrula.py")


def dosya(yol, size=100):
    return {"path": yol, "type": "blob", "size": size}


def agac_skiller(n, ek=()):
    return [dosya(f"skills/s{i}/SKILL.md") for i in range(n)] + list(ek)


# ---------------------------------------------------------------- tür kararı
r = tb.tur_karari(agac_skiller(3), {}, None)
test("lisans yok -> EKLENMEZ", r["durum"] == "EKLENMEZ" and r["tur"] is None and "lisans yok" in r["gerekce"], r)
r = tb.tur_karari(agac_skiller(3), {}, "belirtilmemiş")
test("lisans 'belirtilmemiş' -> EKLENMEZ", r["durum"] == "EKLENMEZ", r)
# kökte lisans yok ama skil klasörlerinde LICENSE var: EKLENMEZ olmaz, normal tür önerisi + "lisans skil başına" işareti
r = tb.tur_karari(agac_skiller(3, [dosya("skills/s0/LICENSE.txt"), dosya("skills/s1/LICENSE")]), {}, "belirtilmemiş")
test("kökte lisans yok, skil klasörlerinde var -> EKLENMEZ değil, tür önerilir, 'lisans skil başına' işareti",
     r["durum"] == "KESIN" and r["tur"] == "koleksiyon" and r["isaretler"]["lisans_skil_basina"] is True
     and any("lisans skil başına" in x for x in r["ajan_karar"]) and any("skil başına" in x for x in r["uyarilar"]), r)
r = tb.tur_karari(agac_skiller(3, [dosya("LICENSE"), dosya("docs/LICENSE")]), {}, None)
test("LICENSE dosyası var ama skil klasöründe değil (kök / docs) -> EKLENMEZ", r["durum"] == "EKLENMEZ" and not r["isaretler"]["lisans_skil_basina"], r)
r = tb.tur_karari(agac_skiller(3, [dosya("skills/s0/LICENSE")]), {}, "MIT")
test("kök lisansı varsa skil başına işareti yok", r["isaretler"]["lisans_skil_basina"] is False and r["durum"] == "KESIN", r)
r = tb.tur_karari([dosya("README.md"), dosya("tool.py")], {}, "MIT")
test("SKILL.md 0 -> referans (bölüm not)", r["tur"] == "referans" and r["bolum"] == "not" and r["durum"] == "KESIN", r)
r = tb.tur_karari(agac_skiller(199), {}, "MIT")
test("199 skil dev-koleksiyon DEĞİL (koleksiyon)", r["tur"] == "koleksiyon", r["tur"])
r = tb.tur_karari(agac_skiller(200), {}, "MIT")
test("200 skil -> dev-koleksiyon (fihrist)", r["tur"] == "dev-koleksiyon" and r["bolum"] == "fihrist", r)
r = tb.tur_karari([dosya("SKILL.md"), dosya("README.md")], {}, "Apache-2.0")
test("1 SKILL.md -> tek-skil (arşiv)", r["tur"] == "tek-skil" and r["bolum"] == "arsiv", r)
r = tb.tur_karari(agac_skiller(5), {}, "MIT")
test("birden çok SKILL.md -> koleksiyon", r["tur"] == "koleksiyon" and r["durum"] == "KESIN", r)
test("her çıktıda 'program mı / riskli mi: ajan bakar' satırı var", any("program mı / riskli mi" in x for x in r["ajan_karar"]), r["ajan_karar"])
r = tb.tur_karari(agac_skiller(2), {}, "NOASSERTION")
test("NOASSERTION lisans: ajan karar verir, EKLENMEZ değil", r["durum"] != "EKLENMEZ" and any("lisans belirsiz" in x for x in r["ajan_karar"]), r)

# kit adayı: skillerin yarısından fazlası köke / üst dizine bağlı
kit_agac = agac_skiller(4, [dosya("config/settings.json"), dosya("hooks/pre.sh")])
kit_icerik = {
    "skills/s0/SKILL.md": "Ayarı `config/settings.json` içinden oku.",
    "skills/s1/SKILL.md": "Betik: ../../hooks/pre.sh çalıştır.",
    "skills/s2/SKILL.md": "hooks/pre.sh dosyasını çağır.",
    "skills/s3/SKILL.md": "Kendi başına çalışır.",
}
r = tb.tur_karari(kit_agac, kit_icerik, "MIT")
test("skillerin yarısından fazlası köke bağlı -> kit ADAYI (katalog)", r["tur"] == "kit" and r["durum"] == "ADAY" and r["bolum"] == "katalog", r)
test("kit adayı AJAN KARAR VERİR işaretli", any("AJAN KARAR VERİR" in x for x in r["ajan_karar"]), r["ajan_karar"])
kit_icerik["skills/s1/SKILL.md"] = "Bağımsız."
kit_icerik["skills/s2/SKILL.md"] = "Bağımsız."
r = tb.tur_karari(kit_agac, kit_icerik, "MIT")
test("yarısı köke bağlı DEĞİLSE (1/4) kit değil", r["tur"] == "koleksiyon", r["tur"])
# skilin kendi scripts/ klasörü köke atıf sayılmaz
yerel_agac = [dosya("skills/a/SKILL.md"), dosya("skills/a/scripts/x.py"), dosya("scripts/build.py"), dosya("skills/b/SKILL.md")]
evet, _ = tb.kok_atifi("skills/a", "scripts/x.py çalıştır", yerel_agac)
test("skilin kendi scripts/ klasörüne atıf köke bağlılık sayılmaz", not evet)
evet, k = tb.kok_atifi("skills/b", "scripts/build.py çalıştır", yerel_agac)
test("kökteki scripts/ klasörüne atıf köke bağlılıktır", evet and k == "scripts/", (evet, k))
evet, _ = tb.kok_atifi("skills/b", "https://github.com/scripts/build.py adresine bak", yerel_agac)
test("URL içindeki yol atıf sayılmaz", not evet)

# ürün adayı: skil dışı çok kaynak kodu
urun = agac_skiller(2) + [dosya(f"src/m{i}.ts") for i in range(30)] + [dosya("skills/s0/x.py")]
r = tb.tur_karari(urun, {}, "MIT")
test("skil dışı çok kod -> urun-skil ADAYI, ajan urun-skil/repo-ici seçer",
     r["tur"] == "urun-skil" and r["durum"] == "ADAY" and any("repo-ici" in x and "AJAN KARAR VERİR" in x for x in r["ajan_karar"]), r)
az_kod = agac_skiller(2) + [dosya(f"src/m{i}.ts") for i in range(5)]
r = tb.tur_karari(az_kod, {}, "MIT")
test("az kod (< 20 dosya) ürün adayı yapmaz", r["tur"] == "koleksiyon", r["tur"])
r = tb.tur_karari([dosya("SKILL.md")] + [dosya(f"src/m{i}.ts") for i in range(40)], {}, "MIT")
test("kökte SKILL.md varsa her şey skil içindedir (tek-skil)", r["tur"] == "tek-skil", r["tur"])

# işaretler
isar = tb.tur_karari([dosya("package.json"), dosya(".claude-plugin/plugin.json"), dosya("a.mp4", 5 * 1048576), dosya("SKILL.md", 1000)],
                     {}, "MIT", "2020-01-01T00:00:00Z")["isaretler"]
test("işaretler: .claude-plugin, package.json, medya", isar["claude_plugin"] and isar["kok_package_json"] and isar["medya_dosya_sayisi"] == 1
     and isar["medya_mb"] == 5.0 and isar["kok_pyproject"] is False, isar)
test("12 aydan eski son push -> bakımsız", isar["bakimsiz"] is True, isar)
uyar = tb.tur_karari([dosya("SKILL.md")], {}, "MIT", "2026-11-01T00:00:00Z", bugun=__import__("datetime").date(2026, 11, 18))
test("yakın push -> bakımsız değil", uyar["isaretler"]["bakimsiz"] is False and not uyar["uyarilar"], uyar)

# ---------------------------------------------------------------- boyut işlevleri
agac = [dosya("a.md", 2048), dosya("v.mp4", 1048576), dosya("sub/b.py", 1024), dosya("sub/w.woff2", 4096), {"path": "sub", "type": "tree"},
        dosya("x/y.bin", None)]
t, m, s, bs = bh.agac_boyutu(agac)
test("agac_boyutu: toplam, medya ayrı, dosya ve boyutsuz sayısı", (t, m, s, bs) == (2048 + 1048576 + 1024 + 4096, 1048576 + 4096, 5, 1), (t, m, s, bs))
t, m, s, bs = bh.agac_boyutu(agac, "sub")
test("agac_boyutu --yol yalnız o klasörün altı", (t, m, s) == (1024 + 4096, 4096, 2), (t, m, s))
test("medya_mi: uzantıya göre", all(bh.ortak.medya_mi(x) for x in ("a.PNG", "m.safetensors", "f.woff2")) and not bh.ortak.medya_mi("a.py"))
test("paket_adi: yorum, -r, URL atlanır; sürüm ve extras ayrılır",
     [bh.paket_adi(x) for x in ("numpy==1.26.4", "Pillow>=10 # not", "-r base.txt", "git+https://x/y", "# yorum", "requests[socks]>=2", "my_pkg")]
     == ["numpy", "pillow", None, None, None, "requests", "my-pkg"])
tur, adlar = bh.bagimliliklar("a/package.json", json.dumps({"dependencies": {"react": "^18", "yerel": "workspace:*"}, "devDependencies": {"vite": "5"}}))
test("package.json: dependencies + devDependencies, workspace atlanır", tur == "npm" and adlar == ["react", "vite"], (tur, adlar))
tur, adlar = bh.bagimliliklar("requirements-dev.txt", "pytest\nnumpy==1\n")
test("requirements*.txt tanınır", tur == "pypi" and adlar == ["numpy", "pytest"], (tur, adlar))
tur, adlar = bh.bagimliliklar("pyproject.toml", '[project]\nname="x"\ndependencies=["httpx>=0.2", "rich"]\n')
test("pyproject.toml [project].dependencies okunur", tur == "pypi" and adlar == ["httpx", "rich"], (tur, adlar))
test("bozuk pyproject çökmez", bh.bagimliliklar("pyproject.toml", "[[[")[1] == [])
test("tanınmayan dosya (None, [])", bh.bagimliliklar("README.md", "x") == (None, []))

ip = bh.ipuclari(["npx playwright install chromium", "model = AutoModel.from_pretrained('org/model-x')", "import whisper\nimport torch"], ())
adlar = [x["ad"] for x in ip]
test("ipuçları: playwright sabit tablo, HF modeli, whisper bilinmeyen, torch sabit",
     any("playwright" in a for a in adlar) and any("org/model-x" in a for a in adlar) and any("whisper" in a for a in adlar)
     and any("torch" in a for a in adlar) and all(x.get("not") is None for x in ip), ip)
ip = bh.ipuclari(["import torch"], {"torch"})
test("torch zaten PyPI bağımlılığıysa sabit tabloya çift yazılmaz", not any("torch" in x["ad"] for x in ip), ip)

# hesapla: sahte ağ işlevleri
NPM = {"react": {"kurulu": 100 * 1024, "bagimlilik": ["loose-envify"]}, "loose-envify": {"kurulu": 10 * 1024, "bagimlilik": ["js-tokens"]},
       "vite": {"kurulu": 200 * 1024, "bagimlilik": []}}
PYPI = {"httpx": {"wheel": 1048576, "bagimlilik": ["certifi"]}, "certifi": {"wheel": 524288, "bagimlilik": ["gizli-paket"]}}
metinler = {"package.json": json.dumps({"dependencies": {"react": "1"}, "devDependencies": {"vite": "5", "yok-paket": "1"}}),
            "requirements.txt": "httpx\nolmayan-paket\n", "README.md": "npx playwright install\nfrom_pretrained('org/buyuk')\nimport whisper"}
cagrilar = []


def sahte_npm(ad):
    cagrilar.append(("npm", ad))
    return NPM.get(ad)


def sahte_pypi(ad):
    cagrilar.append(("pypi", ad))
    return PYPI.get(ad)


def sahte_hf(mid):
    return None if mid == "org/buyuk" else 5 * 1048576


COZ_YOK_NPM = lambda m: (None, ["npm sahte hata: tek düzey yönteme düşüldü"])
COZ_YOK_PY = lambda g, d: (None, ["uv sahte hata: tek düzey yönteme düşüldü"])
hs = bh.hesapla([dosya("a.md", 1048576), dosya("v.mp4", 3 * 1048576)], metinler, sahte_npm, sahte_pypi, sahte_hf,
                npm_coz=COZ_YOK_NPM, py_coz=COZ_YOK_PY)
test("hesapla: kutuphane_kb medyasız", hs["kutuphane_kb"] == 1024, hs["kutuphane_kb"])
beklenen = 4 + (100 + 10) / 1024 + (1 + 0.5) * bh.WHEEL_KATSAYISI + 400
test("hesapla: kurulum_mb = repo + npm (2 düzey) + PyPI wheel x katsayı + sabit tablo", abs(hs["kurulum_mb"] - round(beklenen, 1)) < 0.2, (hs["kurulum_mb"], beklenen))
h = hs["hesaplanamayan"]
test("erişilemeyen npm paketi hesaplanamayan'a yazılır (dev dahil)", any("yok-paket" in x for x in h), h)
test("devDependencies kurulum_mb'ye sayılmaz, ayrı bilgi; devdahil değer ondan büyük", hs["ayrinti"]["npm_dev_mb"] > 0 and hs["ayrinti"]["npm_mb"] < 0.2
     and any("geliştirme bağımlılıkları kurulum_mb'ye SAYILMADI" in x for x in h)
     and hs["ayrinti"]["kurulum_mb_devdahil"] > hs["kurulum_mb"], hs["ayrinti"])
test("uv/npm çözümü yoksa geri düşüş nedeni hesaplanamayan'da ve yöntem 'tek düzey'",
     any("uv sahte hata" in x for x in h) and any("npm sahte hata" in x for x in h)
     and hs["ayrinti"]["cozum"]["pypi"].startswith("tek düzey") and hs["ayrinti"]["cozum"]["npm"].startswith("tek düzey"), (h, hs["ayrinti"]["cozum"]))
test("erişilemeyen PyPI paketi hesaplanamayan'a yazılır", any("olmayan-paket" in x for x in h), h)
test("2. düzey bağımlılık (certifi) sayılır, 3. düzey (gizli-paket) sorgulanmaz",
     ("pypi", "certifi") in cagrilar and ("pypi", "gizli-paket") not in cagrilar and ("npm", "js-tokens") not in cagrilar, cagrilar)
test("geçişli bağımlılık notu hesaplanamayan'da", any("geçişli" in x for x in h), h)
test("bulunamayan HF modeli ve whisper hesaplanamayan'da", any("org/buyuk" in x for x in h) and any("whisper" in x for x in h), h)
test("sabit tablo girdisi 'sabit tablo' diye işaretli", any(x.get("not") == "sabit tablo" for x in hs["ayrinti"]["ipuclari"]), hs["ayrinti"]["ipuclari"])

hs2 = bh.hesapla([dosya("a.md", 1024)], {"package.json": json.dumps({"dependencies": {"react": "1"}})}, lambda a: None, sahte_pypi, sahte_hf,
                 npm_coz=COZ_YOK_NPM, py_coz=COZ_YOK_PY)
test("ağ tamamen başarısızsa çökmez; paket hesaplanamayan'da", any("react" in x for x in hs2["hesaplanamayan"]) and hs2["kurulum_mb"] < 0.01, hs2)

# PyPI wheel seçimi: ağ olmadan, http_json taklit edilir
asil = bh.http_json
asil_mimari = bh.HEDEF_MIMARI
bh.HEDEF_MIMARI = "arm64"
bh.http_json = lambda url: {"urls": [
    {"packagetype": "bdist_wheel", "filename": "p-1.0-py3-none-any.whl", "size": 100},
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp313-cp313-macosx_11_0_arm64.whl", "size": 500},
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp313-cp313-manylinux_2_28_x86_64.whl", "size": 7000},
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp27-cp27mu-win_arm64.whl", "size": 9999},
    {"packagetype": "sdist", "filename": "p-1.0.tar.gz", "size": 50}],
    "info": {"requires_dist": ["numpy>=1", "pytest; extra == 'test'", 'tomli; python_version<"3.11"']}}
b = bh.pypi_bilgi("p")
test("PyPI: hedef platformun (macOS) en büyük wheel'i seçilir (Linux wheel'i değil); extra ve Linux'a özel bağımlılıklar atlanır", b["wheel"] == 500 and b["bagimlilik"] == ["numpy", "tomli"], b)
bh.http_json = lambda url: {"urls": [{"packagetype": "sdist", "filename": "q.tar.gz", "size": 70}], "info": {}}
bh.HEDEF_MIMARI = "x86_64"
bh.http_json = lambda url: {"urls": [
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp313-cp313-macosx_11_0_arm64.whl", "size": 900},
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp313-cp313-macosx_10_9_x86_64.whl", "size": 400},
    {"packagetype": "bdist_wheel", "filename": "p-1.0-cp313-cp313-macosx_10_9_universal2.whl", "size": 600}], "info": {}}
test("PyPI: mimari süzgeci (Intel makinede arm64 wheel sayılmaz, universal2 sayılır)", bh.pypi_bilgi("p")["wheel"] == 600)
bh.HEDEF_MIMARI = asil_mimari
bh.http_json = lambda url: {"urls": [{"packagetype": "sdist", "filename": "q.tar.gz", "size": 70}], "info": {}}
test("PyPI: wheel yoksa sdist boyutu", bh.pypi_bilgi("q")["wheel"] == 70)
bh.http_json = lambda url: None
test("PyPI/npm/HF ağ hatası -> None (çökmez)", bh.pypi_bilgi("x") is None and bh.npm_bilgi("x") is None and bh.hf_boyut("a/b") is None)
bh.http_json = lambda url: {"dist": {"unpackedSize": 1234}, "dependencies": {"b": "1", "a": "1"}}
test("npm: unpackedSize ve bağımlılık adları", bh.npm_bilgi("pkg") == {"kurulu": 1234, "bagimlilik": ["a", "b"]})
bh.http_json = lambda url: {"siblings": [{"size": 10}, {"size": 20}, {"rfilename": "x"}]}
test("HF: siblings boyut toplamı", bh.hf_boyut("a/b") == 30)
bh.http_json = asil

# ---------------------------------------------------------------- tam bağımlılık listesi (alt işlemler sahte)
import subprocess as _sp
KILIT = {"lockfileVersion": 3, "packages": {
    "": {"name": "kok"},
    "node_modules/a": {"version": "1.0.0", "resolved": "https://registry.npmjs.org/a/-/a-1.0.0.tgz"},
    "node_modules/a/node_modules/b": {"version": "2.0.0", "resolved": "https://registry.npmjs.org/b/-/b-2.0.0.tgz"},
    "node_modules/@s/c": {"version": "3.0.0", "resolved": "https://registry.npmjs.org/@s/c/-/c-3.0.0.tgz", "dev": True},
    "node_modules/esbuild-darwin-x64": {"version": "0.1.0", "resolved": "https://registry.npmjs.org/e/-/e.tgz", "optional": True, "os": ["darwin"], "cpu": ["x64"]},
    "node_modules/esbuild-darwin-arm64": {"version": "0.1.0", "resolved": "https://registry.npmjs.org/e/-/e2.tgz", "optional": True, "os": ["darwin"], "cpu": ["arm64"]},
    "node_modules/esbuild-linux-x64": {"version": "0.1.0", "resolved": "https://registry.npmjs.org/e/-/e3.tgz", "optional": True, "os": ["linux"], "cpu": ["x64"]},
    "node_modules/esbuild-win": {"version": "0.1.0", "resolved": "https://registry.npmjs.org/e/-/e4.tgz", "os": ["!darwin", "!linux"]},
    "node_modules/yerel": {"resolved": "packages/yerel", "link": True},
    "node_modules/gomulu": {"version": "9.9.9", "inBundle": True, "resolved": "https://registry.npmjs.org/g/-/g.tgz"},
    "node_modules/gitdep": {"version": "1.0.0", "resolved": "git+ssh://git@github.com/x/y.git#abc"},
    "packages/yerel": {"name": "yerel", "version": "0.0.1"}}}
notlar = []
kp = bh.kilit_paketleri(KILIT, os_ad="darwin", cpu="x64", notlar=notlar)
test("kilit: iç içe ve kapsamlı paket adı/sürümü çıkar, dev bayrağı korunur",
     kp.get(("a", "1.0.0")) is False and kp.get(("b", "2.0.0")) is False and kp.get(("@s/c", "3.0.0")) is True, kp)
test("kilit: platform süzgeci (darwin/x64 kalır; arm64, linux ve '!darwin' paketi elenir)",
     ("esbuild-darwin-x64", "0.1.0") in kp and ("esbuild-darwin-arm64", "0.1.0") not in kp
     and ("esbuild-linux-x64", "0.1.0") not in kp and ("esbuild-win", "0.1.0") not in kp, kp)
test("kilit: kök, çalışma alanı bağı, gömülü paket sayılmaz; git bağımlılığı atlanıp notlanır",
     not any(k[0] in ("kok", "yerel", "gomulu", "gitdep") for k in kp) and any("git/dosya" in x for x in notlar), (kp, notlar))
kp2 = bh.kilit_paketleri(KILIT, os_ad="darwin", cpu="arm64")
test("kilit: arm64 makinede arm64 paketi kalır, x64 elenir", ("esbuild-darwin-arm64", "0.1.0") in kp2 and ("esbuild-darwin-x64", "0.1.0") not in kp2, kp2)


class SahteCalistir:
    """subprocess.run yerine: komutu ve cwd'yi kaydeder, geçici klasöre isteğe göre dosya yazar."""
    def __init__(self, dosya=None, rc=0, stdout="", hata=None, stderr=""):
        self.dosya, self.rc, self.stdout, self.hata, self.stderr, self.cagri = dosya, rc, stdout, hata, stderr, []

    def __call__(self, komut, cwd=None, **k):
        self.cagri.append((list(komut), cwd, k, sorted(os.listdir(cwd)) if cwd and os.path.isdir(cwd) else None,
                           Path(cwd, "package.json").read_text(encoding="utf-8") if cwd and os.path.exists(os.path.join(cwd, "package.json")) else None))
        if self.hata:
            raise self.hata
        if self.dosya:
            Path(cwd, self.dosya[0]).write_text(self.dosya[1], encoding="utf-8")
        return _sp.CompletedProcess(komut, self.rc, self.stdout, self.stderr)


pj = json.dumps({"dependencies": {"a": "^1", "yerel": "workspace:*", "gh": "github:x/y", "dosya": "file:../x"}, "devDependencies": {"v": "5"}})
sc = SahteCalistir(("package-lock.json", json.dumps(KILIT)))
kilit, nt = bh.npm_kilit_uret(pj, calistir=sc, npm_yolu="/sahte/npm")
komut, cwd, kw, _, yazilan = sc.cagri[0]
test("npm kilit: yalnız kilit üretir (--package-lock-only --ignore-scripts, paket indirmez), zaman aşımı 180 sn",
     kilit == KILIT and "--package-lock-only" in komut and "--ignore-scripts" in komut and "--no-audit" in komut and kw["timeout"] == 180 and "install" in komut, sc.cagri)
test("npm kilit: workspace/file/git bağımlılıkları geçici package.json'dan çıkarılır, geri kalanı kalır",
     json.loads(yazilan)["dependencies"] == {"a": "^1"} and json.loads(yazilan)["devDependencies"] == {"v": "5"}, yazilan)
test("npm kilit: geçici klasör kütüphane dışında ve iş bitince silinmiş", not os.path.exists(cwd) and "SkillKutuphanesi" not in cwd, cwd)
sc = SahteCalistir(hata=_sp.TimeoutExpired("npm", 180))
kilit, nt = bh.npm_kilit_uret(pj, calistir=sc, npm_yolu="/sahte/npm")
test("npm kilit: zaman aşımında çökmez, None + neden, geçici klasör silinir", kilit is None and any("180 sn" in x for x in nt) and not os.path.exists(sc.cagri[0][1]), nt)
sc = SahteCalistir(rc=1, stderr="E404 yok")
kilit, nt = bh.npm_kilit_uret(pj, calistir=sc, npm_yolu="/sahte/npm")
test("npm kilit: hata çıkışında None + neden (E404), geçici klasör silinir", kilit is None and any("E404" in x for x in nt) and not os.path.exists(sc.cagri[0][1]), nt)
asil_which = bh.shutil.which
bh.shutil.which = lambda a: None
test("npm yoksa None + neden", bh.npm_kilit_uret(pj)[0] is None and "npm bulunamadı" in bh.npm_kilit_uret(pj)[1][0])
test("uv yoksa None + 'tek düzey' nedeni (uv_coz)", bh.uv_coz([("requirements.txt", "a\n")]) == (None, ["uv bulunamadı: tek düzey yönteme düşüldü"]))
bh.shutil.which = asil_which

UV_CIKTI = "httpx==0.27.0\ncertifi==2024.8.30\n    # via httpx\nPyYAML==6.0.2\nsix==1.16.0 ; sys_platform == 'x'\nHTTPX==0.27.0\n"
test("uv çıktısı ayrıştırılır: ad küçük harf, sürüm, yorum satırı atlanır, tekrarsız",
     bh.uv_cikti_ayristir(UV_CIKTI) == [("certifi", "2024.8.30"), ("httpx", "0.27.0"), ("pyyaml", "6.0.2"), ("six", "1.16.0")], bh.uv_cikti_ayristir(UV_CIKTI))
sc = SahteCalistir(stdout=UV_CIKTI)
bh_plat = bh._uv_platformu()
liste, nt = bh.uv_coz([("requirements.txt", "httpx\n-r base.txt\n-e .\n# yorum\ngit+https://x/y.git\n"),
                       ("alt/pyproject.toml", '[project]\nname="x"\ndependencies=["a"]\n[project.optional-dependencies]\ndev=["pytest"]\nogr=["b"]\n')],
                      dev=True, calistir=sc, uv_yolu="/sahte/uv")
komut, cwd, kw, _, _ = sc.cagri[0]
test("uv_coz: `uv pip compile` (kurmaz, derlemez), --no-build, çıktı stdout, 180 sn, dev ekstrası eklenir",
     komut[1:3] == ["pip", "compile"] and "--no-build" in komut and komut[komut.index("--extra") + 1] == "dev" and komut.count("--extra") == 1
     and kw["timeout"] == 180 and len(liste) == 4 and ("install" not in komut and "sync" not in komut and "venv" not in komut), (komut, liste))
test("uv_coz: çıktı stdout'tan okunur (-o verilmez: `-o -` '-' adlı dosya yazar), Python sürümü sabit", "-o" not in komut and "--output-file" not in komut
     and komut[komut.index("--python-version") + 1] == bh.COZUM_PYTHON, komut)
test("uv_coz: platform bu makineye göre verilir (macOS)", sys.platform != "darwin" or ("--python-platform" in komut and komut[komut.index("--python-platform") + 1] == bh_plat), komut)
test("uv_coz: -r/-e/URL satırları çözüme girmez ve notlanır; geçici klasör silinir", any("3 satır" in x for x in nt) and not os.path.exists(cwd), (nt, cwd))
sc = SahteCalistir(rc=1, stderr="No solution found")
liste, nt = bh.uv_coz([("requirements.txt", "a\n")], calistir=sc, uv_yolu="/sahte/uv")
test("uv_coz: çözüm başarısızsa None + neden, geçici klasör silinir", liste is None and any("No solution" in x for x in nt) and not os.path.exists(sc.cagri[0][1]), nt)
sc = SahteCalistir(hata=_sp.TimeoutExpired("uv", 180))
liste, nt = bh.uv_coz([("requirements.txt", "a\n")], calistir=sc, uv_yolu="/sahte/uv")
test("uv_coz: zaman aşımında çökmez", liste is None and any("180 sn" in x for x in nt), nt)

# hesapla: tam liste akışı (kilit repoda, uv sahte, boyutlar sahte; aynı ad@sürüm bir kez sorgulanır)
npm_sorgu, py_sorgu, kilit_uretim = [], [], []
def n_boy(ad, v):
    npm_sorgu.append((ad, v))
    return {"a": 10, "b": 20, "@s/c": 40, "esbuild-darwin-x64": 80}.get(ad, 1) * 1048576
def p_boy(ad, v):
    py_sorgu.append((ad, v))
    return {"httpx": 1, "certifi": 2, "pytest": 4}.get(ad, 1) * 1048576
def uv_sahte(girdi, dev):
    return ([("httpx", "0.27"), ("certifi", "1")] + ([("pytest", "8")] if dev else []), [])
tam = bh.hesapla([dosya("a.md", 1048576)],
                 {"package.json": pj, "package-lock.json": json.dumps(KILIT), "requirements.txt": "httpx\n", "requirements-dev.txt": "pytest\n"},
                 npm_coz=lambda m: kilit_uretim.append(m) or (None, ["kullanılmamalı"]), py_coz=uv_sahte, npm_boyut=n_boy, pypi_boyut=p_boy)
ay = tam["ayrinti"]
test("hesapla: npm toplamı kilitten (a, b, esbuild-darwin-x64 + 1 sabit) ve dev (@s/c) ayrı",
     not kilit_uretim and abs(ay["npm_mb"] - (10 + 20 + 80)) < 0.01 and ay["npm_dev_paket"] == 1 and abs(ay["npm_dev_mb"] - 40) < 0.01
     and ay["cozum"]["npm"] == "repodaki package-lock.json", (kilit_uretim, ay))
test("hesapla: Python tam çözümden (3 paket x katsayı), dev (pytest) ayrı; devdahil > devharic",
     ay["pypi_paket"] == 2 and abs(ay["pypi_wheel_mb"] - 3) < 0.01 and abs(ay["pypi_kurulu_mb"] - 3 * bh.WHEEL_KATSAYISI) < 0.01
     and ay["pypi_dev_paket"] == 1 and abs(ay["pypi_dev_kurulu_mb"] - 4 * bh.WHEEL_KATSAYISI) < 0.01
     and abs(tam["kurulum_mb"] - (1 + 110 + 3 * bh.WHEEL_KATSAYISI)) < 0.2
     and abs(ay["kurulum_mb_devdahil"] - (tam["kurulum_mb"] + 40 + 4 * bh.WHEEL_KATSAYISI)) < 0.2, (tam["kurulum_mb"], ay))
test("hesapla: aynı ad@sürüm bir kez sorgulanır; çözülmüş (geçişli) paketlerin hepsi sorgulanır",
     len(npm_sorgu) == len(set(npm_sorgu)) == 4 and len(py_sorgu) == len(set(py_sorgu)) == 3, (npm_sorgu, py_sorgu))
test("hesapla: görülemeyenler (kurulum betiği, çalışırken inen model) her raporda yazılır",
     any("kurulum betiğiyle ayrıca" in x for x in tam["hesaplanamayan"]) and not any("geçişli" in x for x in tam["hesaplanamayan"]), tam["hesaplanamayan"])
test("hesapla: boyutu alınamayan ad@sürüm tek satırda hesaplanamayan'a yazılır",
     any("boyutu alınamadı (1)" in x and "z@1" in x for x in bh.hesapla([dosya("a.md")], {"requirements.txt": "z\n"},
         py_coz=lambda g, d: ([("z", "1")], []), pypi_boyut=lambda a, v: None)["hesaplanamayan"]))
# yalnız bir kez çözülen package.json (kilit yok): npm_coz çağrılır
kilit_uretim.clear()
h2 = bh.hesapla([dosya("a.md")], {"package.json": pj}, npm_coz=lambda m: kilit_uretim.append(m) or (KILIT, []), npm_boyut=n_boy, py_coz=uv_sahte)
test("hesapla: kilit yoksa npm_coz çağrılır ve yöntem 'npm install --package-lock-only'", len(kilit_uretim) == 1 and h2["ayrinti"]["cozum"]["npm"] == "npm install --package-lock-only", h2["ayrinti"]["cozum"])

# tarayıcı fazla sayımı: *-core paketleri sayılmaz
def tarayici(adlar, metin="", **k):
    kilit = {"packages": {f"node_modules/{a}": {"version": "1.0.0", "resolved": "https://registry.npmjs.org/x/-/x.tgz"} for a in adlar}}
    r = bh.hesapla([dosya("a.md")], {"package.json": json.dumps({"dependencies": {a: "1" for a in adlar}}), "README.md": metin},
                   npm_coz=lambda m: (kilit, []), npm_boyut=lambda a, v: 1024, **k)
    return [x["ad"] for x in r["ayrinti"]["ipuclari"] if x["tur"] == "sabit"], r["ayrinti"]["indirme_mb"]
test("puppeteer-core ve playwright-core tarayıcı indirmez (sayılmaz)", tarayici(["puppeteer-core", "playwright-core"]) == ([], 0.0), tarayici(["puppeteer-core", "playwright-core"]))
test("puppeteer / playwright / @playwright/test paketi tarayıcı sayılır (en büyüğü kurulum_mb'ye)",
     tarayici(["puppeteer"])[1] == 300 and tarayici(["playwright"])[1] == 400 and tarayici(["@playwright/test"])[1] == 400 and tarayici(["puppeteer", "playwright"])[1] == 400)
test("açık `playwright install` ve `remotion browser ensure` satırları sayılır; düzyazıda 'puppeteer-core' sayılmaz",
     tarayici([], "run: npx playwright install chromium")[1] == 400 and tarayici([], "npx remotion browser ensure")[1] == 150
     and tarayici([], "puppeteer-core ve playwright-core kullanır")[0] == []
     and tarayici([], "Remotion ile render edilir; chromium gerekir")[0] == [])

# yerel disk
tmp = Path(tempfile.mkdtemp(prefix="p15test-"))
try:
    (tmp / "a").mkdir()
    (tmp / "a" / "x.txt").write_bytes(b"x" * 10000)
    (tmp / "a" / "v.mp4").write_bytes(b"v" * 20000)
    os.symlink(tmp / "a", tmp / "bag")           # klasör bağı izlenmemeli
    os.link(tmp / "a" / "x.txt", tmp / "sabit.txt")  # sabit bağ bir kez
    y = bh.yerel_boyut(tmp)
    test("yerel_boyut: symlink izlenmez, sabit bağ bir kez, medya ayrı", y["dosya"] == 3, y)  # x.txt, v.mp4, bağın kendisi; sabit bağ sayılmaz
    test("yerel_boyut: görünen boyut iki dosya + bağın kendisi, medya 20000 bayt", 30000 <= y["gorunen_bayt"] < 30200 and y["medya_bayt"] == 20000, y)
    test("yerel_boyut: disk boyutu görünenden küçük olamaz kadar blok sayar", y["disk_mb"] >= y["gorunen_mb"], y)
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------------------------------------------------------------- dogrula şema denetimi
def hatalar(**k):
    """tur ve bolum ZORUNLU (K-65): varsayılan geçerli çift (kit + katalog); denenen alan k ile ezilir."""
    return dg.kaynak_tur_hatalari({"repo": "a/b", "tur": "kit", "bolum": "katalog", **k})


def ham(**k):
    """Varsayılansız: yalnız verilen alanlar (zorunluluk testleri için)."""
    return dg.kaynak_tur_hatalari({"repo": "a/b", **k})


test("tur ve bolum yoksa HATA (K-65 zorunlu)", any("tür/bölüm alanı eksik" in x for x in ham()))
test("yalnız tur verilirse (bolum yok) HATA", any("tür/bölüm alanı eksik" in x for x in ham(tur="kit")))
test("yalnız bolum verilirse (tur yok) HATA", any("tür/bölüm alanı eksik" in x for x in ham(bolum="katalog")))
test("tam kayıt (tur + bolum) boş liste", hatalar() == [])
test("geçerli tur+bolum çiftleri hata vermez", all(hatalar(tur=t, bolum=b) == [] for t, b in dg.KAYNAK_TURLERI.items()))
test("geçersiz tur HATA", any("tur geçersiz" in x for x in hatalar(tur="dev")))
test("geçersiz bolum HATA", any("bolum geçersiz" in x for x in hatalar(bolum="depo")))
test("tur-bolum uyumsuzluğu HATA (dev-koleksiyon + arsiv)", any("uyuşmuyor" in x for x in hatalar(tur="dev-koleksiyon", bolum="arsiv")))
test("uyumsuz: kit + arsiv, referans + katalog, koleksiyon + fihrist",
     all(any("uyuşmuyor" in x for x in hatalar(tur=t, bolum=b)) for t, b in (("kit", "arsiv"), ("referans", "katalog"), ("koleksiyon", "fihrist"))))
test("tek_basina bool olmalı", any("tek_basina" in x for x in hatalar(tek_basina="evet")) and hatalar(tek_basina=False) == [])
test("kurulmayan_parcalar metin listesi olmalı", any("kurulmayan" in x for x in hatalar(kurulmayan_parcalar="hooks")) and hatalar(kurulmayan_parcalar=["hooks"]) == [])
test("son_kontrol {tarih, commit} biçimi", hatalar(son_kontrol={"tarih": "2026-11-18", "commit": "abc"}) == []
     and any("son_kontrol" in x for x in hatalar(son_kontrol={"tarih": "dün", "commit": "abc"})))
test("arac_uyumu bool alanları; bilinmeyen anahtar HATA", hatalar(arac_uyumu={"claude": True, "windows": False}) == []
     and any("arac_uyumu" in x for x in hatalar(arac_uyumu={"claude": "evet"})) and any("arac_uyumu" in x for x in hatalar(arac_uyumu={"vim": True})))
iyi = {"kutuphane_kb": 10, "kurulum_mb": 1.5, "hesaplanamayan": [], "tarih": "2026-11-18"}
test("boyut geçerli biçim", hatalar(boyut=iyi) == [] and hatalar(boyut={**iyi, "gercek_mb": 2}) == [])
test("boyut.kurulum_mb_devdahil isteğe bağlı sayı", hatalar(boyut={**iyi, "kurulum_mb_devdahil": 9.5}) == []
     and any("kurulum_mb_devdahil" in x for x in hatalar(boyut={**iyi, "kurulum_mb_devdahil": "x"})))
test("boyut: eksik/yanlış alanlar HATA", len(hatalar(boyut={"kutuphane_kb": "x", "hesaplanamayan": "a"})) >= 3 and any("gercek_mb" in x for x in hatalar(boyut={**iyi, "gercek_mb": "b"})))
test("yeni alanlar KAYNAK_ANAHTARLARI'nda", all(a in dg.KAYNAK_ANAHTARLARI for a in
     ("tur", "bolum", "tur_gerekce", "ne_ister", "ne_indirir", "tek_basina", "kurulmayan_parcalar", "son_kontrol", "arac_uyumu", "boyut")))

# _e6_kaynaklar: tür hatası gerçekten HATA listesine düşer; tür/bölüm eksik kayıt da HATA (K-65), tam kayıt sessiz
tmp = Path(tempfile.mkdtemp(prefix="p15test-"))
try:
    (tmp / "kaynaklar.json").write_text(json.dumps({"repolar": [
        {"repo": "a/iyi", "tip": "T2", "tur": "kit", "bolum": "katalog"},
        {"repo": "a/eksik", "tip": "T2"},
        {"repo": "a/kotu", "tip": "T2", "tur": "kit", "bolum": "arsiv"}]}), encoding="utf-8")
    h, u = [], []
    dg._e6_kaynaklar(tmp, h, u)
    test("_e6_kaynaklar: uyumsuz tur-bolum ve eksik tür/bölüm HATA listesine düşer, tam kayıt sessiz",
         len(h) == 2 and any("a/kotu" in x for x in h) and any("a/eksik" in x for x in h) and not any("a/iyi" in x for x in h) and not u, (h, u))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

gecen = sum(1 for _, k in SONUC if k)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
