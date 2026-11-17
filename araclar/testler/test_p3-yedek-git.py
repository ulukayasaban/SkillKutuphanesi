#!/usr/bin/env python3
"""P3 testleri: git-durum.py ve yedek-denetim.py. Yalnız geçici klasör ve sahte veri; gerçek kütüphane/ev klasörü okunmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
TMP = Path(tempfile.mkdtemp(prefix="p3test-"))
HOME = TMP / "home"
HOME.mkdir()
SAHTE_BIN = TMP / "bin"
SAHTE_BIN.mkdir()
ENV = {**os.environ, "HOME": str(HOME), "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1",
       "GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": "t@t"}
os.environ["HOME"] = str(HOME)   # modül içi Path.home() da geçici klasöre baksın

GITIGNORE_BLOK = """/.env
/.env.*
!/.env.example
/araclar/.env
/*.pem
/*.key
/*.p12
/*.pfx
/programlar/**/.env
/yedek/
/.skill-kutuphanesi/
/*.bundle
/*.yedek
/notlar/son-aylik-calisma.json
/notlar/aylik-ozet.md
"""


def yukle(ad, dosya):
    s = importlib.util.spec_from_file_location(ad, ARACLAR / dosya)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


GD = yukle("git_durum", "git-durum.py")
YD = yukle("yedek_denetim", "yedek-denetim.py")
SONUC = []


def test(ad, kosul):
    SONUC.append((ad, bool(kosul)))


def git(d, *a, env=None):
    e = {**ENV, **(env or {})}
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, env=e, stdin=subprocess.DEVNULL)


def yeni_depo(ad, origin=True, gitignore=GITIGNORE_BLOK):
    """Bare origin + çalışma klonu, master, tek commit, senkron."""
    kok = TMP / ad
    kok.mkdir()
    bare = kok / "origin.git"
    calisma = kok / "w"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "master", str(bare)], env=ENV, check=True)
    subprocess.run(["git", "init", "-q", "-b", "master", str(calisma)], env=ENV, check=True)
    (calisma / ".gitignore").write_text(gitignore)
    (calisma / "a.txt").write_text("a\n")
    git(calisma, "add", "-A")
    git(calisma, "commit", "-qm", "ilk")
    if origin:
        git(calisma, "remote", "add", "origin", str(bare))
        git(calisma, "push", "-q", "origin", "master")
        git(calisma, "fetch", "-q", "origin")
    return calisma, bare


def commit(d, ad="x", tarih=None, icerik="x\n"):
    (Path(d) / ad).parent.mkdir(parents=True, exist_ok=True)
    (Path(d) / ad).write_text(icerik)
    git(d, "add", "-A")
    return git(d, "commit", "-qm", f"c {ad}", env={"GIT_COMMITTER_DATE": tarih, "GIT_AUTHOR_DATE": tarih} if tarih else None)


def calistir(arac, *args, env=None, cwd=None):
    e = {**ENV, **(env or {})}
    return subprocess.run([sys.executable, str(ARACLAR / arac), *args], capture_output=True, text=True, env=e, cwd=cwd,
                          stdin=subprocess.DEVNULL)


def gd(depo, **kw):
    b = GD.bilgi_topla(depo, gh_kullan=kw.pop("gh_kullan", False), **kw)
    d, f = GD.degerlendir(b)
    return b, d, f


def metinler(f):
    return " | ".join(x["metin"] for x in f)


def kararlar(f):
    return " | ".join(x["karar"] for x in f if x["karar"])


def agac_anlik(d):
    out = []
    for k, _, dosyalar in os.walk(d):
        if ".git" in Path(k).relative_to(d).parts:
            continue
        for f in dosyalar:
            st_ = os.lstat(os.path.join(k, f))
            out.append((os.path.join(k, f), st_.st_size, st_.st_mtime_ns))
    return sorted(out)


# ---------------------------------------------------------------- git-durum
d, _ = yeni_depo("g1")
b, durum, f = gd(d)
test("1 temiz depo temiz", durum == "temiz")
j = json.loads(calistir("git-durum.py", "--depo", str(d), "--ozet-json", "--gh-yok").stdout)
test("1b temiz ozet-json satiri", j["satirlar"] == ["Git temiz: master GitHub ile aynı, değişiklik yok."] and j["durum"] == "temiz")

d, _ = yeni_depo("g2")
for i in range(4):
    commit(d, f"f{i}")
b, durum, f = gd(d)
test("2 dort commit onde: temiz (esik 5)", b["ahead"] == 4 and durum == "temiz")
j2 = json.loads(calistir("git-durum.py", "--depo", str(d), "--ozet-json", "--gh-yok").stdout)
test("2a onde commit varken ozet-json 'GitHub ile aynı' demez", j2["durum"] == "temiz" and "4 commit" in j2["satirlar"][0] and "aynı" not in j2["satirlar"][0])
commit(d, "f4")
b, durum, f = gd(d)
test("2b bes commit onde: dikkat + push karari", b["ahead"] == 5 and durum == "dikkat" and "push" in kararlar(f))

d, _ = yeni_depo("g3")
commit(d, "eski", tarih="2026-01-01T00:00:00")
b, durum, f = gd(d)
test("3 eski tek commit yastan dikkat", b["ahead"] == 1 and b["en_eski_gun"] > 7 and durum == "dikkat")

# 4 behind: ikinci klon ile origin'e commit
d, bare = yeni_depo("g4")
ikinci = TMP / "g4" / "w2"
subprocess.run(["git", "clone", "-q", str(bare), str(ikinci)], env=ENV, check=True)
commit(ikinci, "uzak")
git(ikinci, "push", "-q", "origin", "master")
ref_once = git(d, "rev-parse", "refs/remotes/origin/master").stdout
b, durum, f = gd(d)
test("4 --uzak olmadan behind 0 ve ref degismez", b["behind"] == 0 and git(d, "rev-parse", "refs/remotes/origin/master").stdout == ref_once)
b, durum, f = gd(d, uzak=True)
test("4b --uzak ile behind 1 dikkat", b["behind"] == 1 and durum == "dikkat" and b["uzak_sonuc"] == "alindi")

# 5 ayrışma
commit(d, "yerel")
r = calistir("git-durum.py", "--depo", str(d), "--uzak", "--gh-yok", "--siki")
b, durum, f = gd(d)
test("5 ayrisma sorun, --siki 1", durum == "sorun" and r.returncode == 1)
test("5b --siki olmadan 0", calistir("git-durum.py", "--depo", str(d), "--gh-yok").returncode == 0)

# 6 kirli + izlenmeyen
d, _ = yeni_depo("g6")
(d / "a.txt").write_text("degisti\n")
(d / "yenik").mkdir()
(d / "yenik" / "x").write_text("x")
b, durum, f = gd(d)
test("6 kirli ve izlenmeyen klasor /", durum == "dikkat" and "yenik/" in b["izlenmeyen"] and "yenik/ commit" in kararlar(f))
d, _ = yeni_depo("g6b")
commit(d, "notlar/proje-kullanimi.md")
git(d, "push", "-q", "origin", "master")
(d / "notlar" / "proje-kullanimi.md").write_text("yeni\n")
b, durum, f = gd(d)
test("6b tek proje-kullanimi degisikligi bilgi, temiz", durum == "temiz" and "aylık görev" in metinler(f))

# 7 rename
d, _ = yeni_depo("g7")
git(d, "mv", "a.txt", "b.txt")
b, durum, f = gd(d)
test("7 rename -z cozulur, eski yol izlenmeyen degil", "a.txt" not in b["izlenmeyen"] and "b.txt" in b["degisen"])

# 8 dallar
d, _ = yeni_depo("g8")
git(d, "branch", "eski-dal")
git(d, "switch", "-q", "-c", "dev")
commit(d, "d1")
git(d, "switch", "-q", "master")
dallar_once = git(d, "branch", "--list").stdout
b, durum, f = gd(d)
t = metinler(f)
test("8 birlesmis artik dal + branch -d karari", "Birleşmiş artık dal: eski-dal" in t and "git branch -d" in kararlar(f))
test("8b birlesmemis dal", "Birleşmemiş yerel dal: dev" in t)
test("8c dallar silinmedi", git(d, "branch", "--list").stdout == dallar_once)

# 9 bekleyen dal
d, _ = yeni_depo("g9")
git(d, "switch", "-q", "-c", "guncelleme/2026-11")
commit(d, "g1", tarih="2026-10-01T00:00:00")
git(d, "switch", "-q", "master")
b, durum, f = gd(d)
test("9 bekleyen dal: dikkat + karar", "Bekleyen güncelleme dalı: guncelleme/2026-11" in metinler(f) and "promptlar/08" in kararlar(f))
d, _ = yeni_depo("g9b")
git(d, "switch", "-q", "-c", "guncelleme/2026-09")
commit(d, "g1", tarih="2026-01-01T00:00:00")
git(d, "switch", "-q", "master")
b, durum, f = gd(d)
test("9b 45 gunden uzun metni", "45 günden uzun" in metinler(f))

# 10 .git esigi
d, _ = yeni_depo("g10")
_, _, f0 = gd(d)
eski = GD.ESIK_GIT_MB
GD.ESIK_GIT_MB = -1
_, du, f1 = gd(d)
GD.ESIK_GIT_MB = eski
test("10 .git esigi", ".git klasörü" not in metinler(f0) and ".git klasörü" in metinler(f1))

# 11 yeni buyuk dosya
d, _ = yeni_depo("g11")
(d / "mod.txt").write_text("x" * 3000000)
git(d, "add", "-A")
git(d, "commit", "-qm", "buyuk")
git(d, "push", "-q", "origin", "master")
(d / "mod.txt").write_text("y" * 3100000)
git(d, "commit", "-qam", "degisti")
(d / "yeni.bin").write_text("z" * 3000000)
git(d, "add", "-A")
git(d, "commit", "-qm", "yeni buyuk")
(d / "izlenmeyen.bin").write_text("q" * 3000000)
GD.ESIK_YENI_DOSYA_MB = 1
b, durum, f = gd(d)
GD.ESIK_YENI_DOSYA_MB = 5
test("11 yeni eklenen buyuk dosya uyarir, degisen eski uyarmaz",
     "yeni.bin" in b["yeni_buyuk"] and "mod.txt" not in b["yeni_buyuk"] and "izlenmeyen.bin" in b["yeni_buyuk"])

# 12 gizli adlar
d, _ = yeni_depo("g12")
for yol in (".env", "a/b.pem", "credentials.json", ".env.example", "arsiv/x/.env", "arsiv/x/k.pem"):
    (d / yol).parent.mkdir(parents=True, exist_ok=True)
    (d / yol).write_text("GIZLI-DEGER")
git(d, "add", "-A", "-f")
git(d, "commit", "-qm", "gizli")
r = calistir("git-durum.py", "--depo", str(d), "--gh-yok")
b, durum, f = gd(d)
test("12 gizli adlar sorun, example ve arsiv haric",
     durum == "sorun" and b["gizli_adlar"] == [".env", "a/b.pem", "credentials.json"] and b["gizli_arsiv_say"] == 2)
test("12b icerik asla yazdirilmaz", "GIZLI-DEGER" not in r.stdout + r.stderr)

# 13 arsiv ignore
d, _ = yeni_depo("g13")
(d / "arsiv" / "s").mkdir(parents=True)
(d / "arsiv" / "s" / ".gitignore").write_text("x.txt\n")
(d / "arsiv" / "s" / "x.txt").write_text("x")
git(d, "add", "arsiv/s/.gitignore")
git(d, "commit", "-qm", "s")
b, durum, f = gd(d)
test("13 arsiv ignore sorunu", durum == "sorun" and "git add -f arsiv" in metinler(f))
git(d, "add", "-f", "arsiv")
git(d, "commit", "-qm", "f")
b, durum, f = gd(d)
test("13b add -f sonrasi yok", "git add -f arsiv" not in metinler(f))

# 14 koruma
d, _ = yeni_depo("g14", gitignore="__pycache__/\n")
b, durum, f = gd(d)
test("14 koruma eksik listelenir", len(b["koruma_eksik"]) == len(GD.KORUMA_PROBLARI))
d, _ = yeni_depo("g14b")
b, _, _ = gd(d)
test("14b tam blok: eksik yok", b["koruma_eksik"] == [])
d, _ = yeni_depo("g14c", gitignore=GITIGNORE_BLOK.replace("/notlar/son-aylik-calisma.json\n", "").replace("/notlar/aylik-ozet.md\n", ""))
b, _, _ = gd(d)
test("14c yalniz iki P4 satiri eksik", sorted(b["koruma_eksik"]) == ["notlar/aylik-ozet.md", "notlar/son-aylik-calisma.json"])

# 15 --uzak yanlis depo
d, _ = yeni_depo("g15", origin=False)
git(d, "remote", "add", "origin", "https://github.com/someone/else.git")
b, durum, f = gd(d, uzak=True)
test("15 baska github deposu reddedilir, fetch yok", durum == "sorun" and b["uzak_sonuc"] == "reddedildi"
     and not (d / ".git" / "FETCH_HEAD").exists())

# 16 gorunurluk
d, _ = yeni_depo("g16", origin=False)
git(d, "remote", "add", "origin", "https://github.com/ulukayasaban/SkillKutuphanesi.git")


def sahte_gh(cikti, kod=0):
    marker = TMP / "gh-cagrildi"
    if marker.exists():
        marker.unlink()
    (SAHTE_BIN / "gh").write_text(f"#!/bin/sh\ntouch '{marker}'\n" + (f"echo {cikti}\n" if cikti else "") + f"exit {kod}\n")
    (SAHTE_BIN / "gh").chmod(0o755)
    return marker


yol_env = {"PATH": f"{SAHTE_BIN}:{os.environ['PATH']}"}
sahte_gh("PUBLIC")
r = calistir("git-durum.py", "--depo", str(d), "--ozet-json", env=yol_env)
test("16 public sorun", json.loads(r.stdout)["durum"] == "sorun" and "public" in r.stdout)
sahte_gh("PRIVATE")
r = calistir("git-durum.py", "--depo", str(d), "--ozet-json", env=yol_env)
test("16b private sorun degil", json.loads(r.stdout)["durum"] != "sorun" or "public" not in r.stdout)
marker = sahte_gh("PUBLIC")
r = calistir("git-durum.py", "--depo", str(d), "--gh-yok", env=yol_env)
test("16c --gh-yok gh cagirmaz", not marker.exists() and r.returncode == 0)
marker = sahte_gh("PUBLIC")
r = calistir("git-durum.py", "--depo", str(d), "--kisa", env=yol_env)
test("16d --kisa gh cagirmaz", not marker.exists())
sahte_gh("", kod=1)
r = calistir("git-durum.py", "--depo", str(d), "--ozet-json", env=yol_env)
test("16e gh hata: bulgu yok, cikis 0", r.returncode == 0 and "public" not in r.stdout)
shutil.rmtree(SAHTE_BIN)
SAHTE_BIN.mkdir()
r = calistir("git-durum.py", "--depo", str(d), "--ozet-json", env={"PATH": "/usr/bin:/bin"})
test("16f gh yok: cikis 0, gecerli json", r.returncode == 0 and json.loads(r.stdout)["arac"] == "git-durum")

# 17 detached
d, _ = yeni_depo("g17")
git(d, "checkout", "-q", "--detach")
b, durum, f = gd(d)
test("17 detached HEAD", durum == "dikkat" and "HEAD bir dala bağlı değil" in metinler(f))

# 18 git deposu degil
bos = TMP / "bos"
bos.mkdir()
r = calistir("git-durum.py", "--depo", str(bos))
r2 = calistir("git-durum.py", "--depo", str(bos), "--siki")
r3 = calistir("git-durum.py", "--depo", str(bos), "--ozet-json")
test("18 depo degil: sorun, --siki 1, json gecerli", r.returncode == 0 and r2.returncode == 1 and json.loads(r3.stdout)["durum"] == "sorun")

# 19 ozet-json saflik
d, _ = yeni_depo("g19")
once = agac_anlik(d)
r = calistir("git-durum.py", "--depo", str(d), "--ozet-json", "--gh-yok")
j = json.loads(r.stdout)
test("19 ozet-json saf", set(j) == {"arac", "durum", "satirlar", "karar_bekleyen"} and j["arac"] == "git-durum" and r.stderr == ""
     and agac_anlik(d) == once)
test("19b --ozet-json --rapor/--kisa kullanim hatasi 2",
     calistir("git-durum.py", "--depo", str(d), "--ozet-json", "--rapor").returncode == 2
     and calistir("git-durum.py", "--depo", str(d), "--ozet-json", "--kisa").returncode == 2)

# 20 salt okuma
d, _ = yeni_depo("g20")
(d / "yeni").mkdir()
(d / "yeni" / "z").write_text("z")
git(d, "status", "--porcelain")   # indeksi bir kez yenile; sonrası araçların indeksi değiştirip değiştirmediğine bakar
a1 = (os.stat(d / ".git" / "index").st_mtime_ns, agac_anlik(d), git(d, "for-each-ref").stdout)
for args in ([], ["--kisa"], ["--ozet-json"], ["--gh-yok"]):
    calistir("git-durum.py", "--depo", str(d), *args)
a2 = (os.stat(d / ".git" / "index").st_mtime_ns, agac_anlik(d), git(d, "for-each-ref").stdout)
test("20 salt okuma: agac, ref, durum, index ayni", a1 == a2)

# 21 --kisa
d, _ = yeni_depo("g21")
test("21 --kisa temiz", calistir("git-durum.py", "--depo", str(d), "--kisa").stdout.strip() == "git: temiz")
(d / "yeni.txt").write_text("x")
k = calistir("git-durum.py", "--depo", str(d), "--kisa").stdout
test("21b --kisa dikkat satiri", k.startswith("DİKKAT") and "git: temiz" not in k)

# 22 rapor
d, _ = yeni_depo("g22")
cikti = TMP / "r.md"
calistir("git-durum.py", "--depo", str(d), "--rapor", "--cikti", str(cikti), "--gh-yok")
yazildi = cikti.exists() and cikti.read_text().startswith("# Git Durumu")
cikti.write_text(cikti.read_text().replace(__import__("datetime").date.today().isoformat(), "2020-01-01"))
os.utime(cikti, (1000000, 1000000))
calistir("git-durum.py", "--depo", str(d), "--rapor", "--cikti", str(cikti), "--gh-yok")
test("22 rapor yazilir, yalniz tarih farkinda yeniden yazilmaz", yazildi and int(cikti.stat().st_mtime) == 1000000)
yok = TMP / "yok.md"
calistir("git-durum.py", "--depo", str(d), "--gh-yok", "--cikti", str(yok))
test("22b --rapor olmadan dosya yazilmaz", not yok.exists())

# 23 stash
d, _ = yeni_depo("g23")
(d / "a.txt").write_text("stashlik\n")
git(d, "stash", "-q")
b, durum, f = gd(d)
test("23 stash bilgi, durum etkilenmez", b["stash"] == 1 and "stash" in metinler(f) and durum == "temiz")

# ---------------------------------------------------------------- yedek-denetim
BUGUN = "2026-11-11"


def kayit(**kw):
    k = {"kimlik": "ayar-2026-11-01", "yol": "", "tur": "ayar-dosyasi", "ne": "deneme", "tarih": "2026-11-01",
         "geri_yukleme": "elle kopyala", "gizli_icerir": "hayir"}
    k.update(kw)
    return k


def yedek_ortam(ad, kayitlar, dosyalar=None, ekstra=None, ust=None):
    kok = TMP / ad / "yedek"
    kok.mkdir(parents=True)
    kutup = TMP / ad / "kutuphane"
    kutup.mkdir()
    for k in kayitlar:
        if not k.get("yol"):
            k["yol"] = str(kok / k["kimlik"])
        if dosyalar is not None:
            p = Path(k["yol"])
            p.mkdir(parents=True, exist_ok=True)
            for dn in dosyalar:
                (p / dn).write_text("GIZLI-DEGER")
                (p / dn).chmod(0o600)
    for e in ekstra or []:
        (kok / e).mkdir()
        (kok / e / "x").write_text("12345")
    veri = {"surum": 1, "kok": str(kok), "ikinci_kopya_iste": False, "yedekler": kayitlar}
    if ust:
        veri.update(ust)
    kf = TMP / ad / "yedekler.json"
    kf.write_text(json.dumps(veri))
    kok.chmod(0o700)  # gerçek yedek klasörü gibi: yalnız sahip (gevşek izin denetimi bunu bekler)
    for c in kok.iterdir():
        if c.is_dir() and not c.is_symlink():
            c.chmod(0o700)
    return kf, kok, kutup


def yd(kf, kok, kutup, *extra):
    r = calistir("yedek-denetim.py", "--kayit", str(kf), "--kok", str(kok), "--kutuphane", str(kutup), "--bugun", BUGUN, *extra)
    return r


def yj(kf, kok, kutup, *extra):
    r = yd(kf, kok, kutup, "--ozet-json", *extra)
    return json.loads(r.stdout), r


kf, kok, kut = yedek_ortam("y24", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", beklenen=["bir.txt", "iki.txt"], silme_gun=30),
                                   kayit(kimlik="b-2026-11-08", tur="genel-skill-klasoru", tarih="2026-11-08", beklenen=["bir.txt"],
                                         silme_olay="boşaltma", silme_olay_tamam=False)], dosyalar=["bir.txt", "iki.txt"])
j, r = yj(kf, kok, kut)
test("24 iki kayit yerinde: temiz, bilgi satirlari", j["durum"] == "temiz" and r.returncode == 0 and "2 yedek kayıtlı" in j["satirlar"][0]
     and any("silme olayı bekleniyor" in s for s in j["satirlar"]) and any("gün sonra silinebilir" in s for s in j["satirlar"]))

# 25 eksik klasor / beklenen
kf, kok, kut = yedek_ortam("y25", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", beklenen=["bir.txt", "yok.txt"], silme_gun=30),
                                   kayit(kimlik="b-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=["bir.txt"])
shutil.rmtree(kok / "b-2026-11-08")
j, r = yj(kf, kok, kut)
t = " | ".join(j["satirlar"])
test("25 yol yok ve beklenen eksik: sorun", j["durum"] == "sorun" and "yedek yok" in t and "beklenen öğe eksik: yok.txt" in t)

# 26 kok yok
kf, kok, kut = yedek_ortam("y26", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=[])
shutil.rmtree(kok)
j, r = yj(kf, kok, kut)
test("26 kok yok: tek dikkat, sorun yok", j["durum"] == "dikkat" and len(j["satirlar"]) == 1 and "yedek klasörü yok" in j["satirlar"][0])

# 27 yanlis yerde
kf, kok, kut = yedek_ortam("y27", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)])
(kut / "icerde").mkdir()
v = json.loads(kf.read_text())
v["yedekler"][0]["yol"] = str(kut / "icerde")
kf.write_text(json.dumps(v))
j, r = yj(kf, kok, kut)
test("27 kutuphane icinde: sorun", j["durum"] == "sorun" and "kütüphane içinde" in " ".join(j["satirlar"]))
skills = HOME / ".claude" / "skills" / "yedek"
skills.mkdir(parents=True)
v["yedekler"][0]["yol"] = str(skills)
kf.write_text(json.dumps(v))
j, r = yj(kf, kok, kut, )
test("27b skill klasoru icinde: sorun", j["durum"] == "sorun" and "skill taranan klasör" in " ".join(j["satirlar"]))

# 28/29 gizli
kf, kok, kut = yedek_ortam("y28", [kayit(kimlik="g-2026-11-10", tarih="2026-11-10", gizli_icerir="evet", silme_gun=30)], dosyalar=["s.txt"])
p = kok / "g-2026-11-10" / "s.txt"
p.chmod(0o644)
mode0 = stat.S_IMODE(p.stat().st_mode)
r = yd(kf, kok, kut)
j, _ = yj(kf, kok, kut)
test("28 gevsek izin dikkat, icerik yazilmaz, mod degismez", j["durum"] == "dikkat" and "izinleri gevşek" in " ".join(j["satirlar"])
     and "GIZLI-DEGER" not in r.stdout + r.stderr and stat.S_IMODE(p.stat().st_mode) == mode0)
p.chmod(0o600)
j, _ = yj(kf, kok, kut)
test("28b chmod 600 sonrasi uyari yok", "izinleri gevşek" not in " ".join(j["satirlar"]))
kf, kok, kut = yedek_ortam("y29", [kayit(kimlik="g-2026-11-10", tarih="2026-11-10", gizli_icerir="evet")], dosyalar=["s.txt"])
j, _ = yj(kf, kok, kut)
test("29 gizli ama silme zamani yok: dikkat", j["durum"] == "dikkat" and "silme zamanı tanımsız" in " ".join(j["satirlar"]))

# 30 silinebilir (gun)
kf, kok, kut = yedek_ortam("y30", [kayit(kimlik="s-2026-10-11", tarih="2026-10-11", silme_gun=30)], dosyalar=["x.txt"])
j, r = yj(kf, kok, kut)
t = " ".join(j["satirlar"])
full = yd(kf, kok, kut).stdout
test("30 gun doldu: SILINEBILIR + karar + rm komutu, klasor durur", "SİLİNEBİLİR" in t and j["karar_bekleyen"] and "rm -r -- '" in full
     and (kok / "s-2026-10-11").exists() and str(kok.resolve()) in full)
kf, kok, kut = yedek_ortam("y30b", [kayit(kimlik="s-2026-10-13", tarih="2026-10-13", silme_gun=30)], dosyalar=["x.txt"])
j, _ = yj(kf, kok, kut)
test("30b 29 gun: bekliyor", "SİLİNEBİLİR" not in " ".join(j["satirlar"]) and "1 gün sonra silinebilir" in " ".join(j["satirlar"]))

# 31/32 olay
kf, kok, kut = yedek_ortam("y31", [kayit(kimlik="o-2026-11-01", silme_olay="boşaltma", silme_olay_tamam=False)], dosyalar=["x.txt"])
j, _ = yj(kf, kok, kut)
test("31 olay bekleniyor: silinebilir degil", "silme olayı bekleniyor: boşaltma" in " ".join(j["satirlar"]) and not j["karar_bekleyen"])
v = json.loads(kf.read_text())
v["yedekler"][0]["silme_olay_tamam"] = True
kf.write_text(json.dumps(v))
j, _ = yj(kf, kok, kut)
test("31b olay tamam: SILINEBILIR", "SİLİNEBİLİR" in " ".join(j["satirlar"]))
kf, kok, kut = yedek_ortam("y32", [kayit(kimlik="o-2026-10-01", tarih="2026-10-01", silme_gun=30, silme_olay="x", silme_olay_tamam=False)], dosyalar=["x.txt"])
j, _ = yj(kf, kok, kut)
test("32 gun tamam ama olay degil: hazir degil", "SİLİNEBİLİR" not in " ".join(j["satirlar"]))
v = json.loads(kf.read_text())
v["yedekler"][0]["silme_olay_tamam"] = True
kf.write_text(json.dumps(v))
j, _ = yj(kf, kok, kut)
test("32b ikisi de tamam: hazir", "SİLİNEBİLİR" in " ".join(j["satirlar"]))

# 33 yas uyarisi
kf, kok, kut = yedek_ortam("y33", [kayit(kimlik="y-2026-08-03", tarih="2026-08-03")], dosyalar=["x.txt"])
j, _ = yj(kf, kok, kut)
test("33 100 gunluk: gundur duruyor", "gündür duruyor" in " ".join(j["satirlar"]) and j["karar_bekleyen"])
kf, kok, kut = yedek_ortam("y33b", [kayit(kimlik="y-2026-10-01", tarih="2026-10-01", gizli_icerir="evet", silme_olay="x")], dosyalar=["x.txt"])
kf, kok, kut = yedek_ortam("y33c", [kayit(kimlik="y-2026-09-30", tarih="2026-09-30")], dosyalar=["x.txt"])
j, _ = yj(kf, kok, kut)
test("33b 42 gun, gizli hayir: uyari yok (esik 90)", "gündür duruyor" not in " ".join(j["satirlar"]))

# 34 kayitsiz
kf, kok, kut = yedek_ortam("y34", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=["x.txt"], ekstra=["gizemli", ".gizli"])
(kok / "gizemli" / "kilitli").write_text("x")
(kok / "gizemli" / "kilitli").chmod(0)
j, r = yj(kf, kok, kut)
(kok / "gizemli" / "kilitli").chmod(0o600)
test("34 kayitsiz klasor dikkat + karar, .gizli yok sayilir, mod 000 dosya sorun cikarmaz",
     r.returncode == 0 and "kayıtsız yedek: gizemli (tanınmayan ad; 0.0 MB)" in " ".join(j["satirlar"]) and ".gizli" not in " ".join(j["satirlar"])
     and "gizemli yedeği kayda alınsın mı?" in j["karar_bekleyen"])

# 35 sema hatalari
kf, kok, kut = yedek_ortam("y35", [
    kayit(kimlik="s1", geri_yukleme=""), kayit(kimlik="s2", tur="uydurma"), kayit(kimlik="s3", tarih="2026-13-45"),
    kayit(kimlik="s4", gizli_icerir="belki"), kayit(kimlik="d1"), kayit(kimlik="d1")], dosyalar=None)
j, r = yj(kf, kok, kut)
t = " ".join(j["satirlar"])
test("35 sema hatalari sorun", j["durum"] == "sorun" and "s1: kayıtta eksik ya da hatalı alan: geri_yukleme" in t and "tur" in t and "tarih" in t
     and "gizli_icerir" in t and "kimlik tekrar ediyor: d1" in t)
bozuk = TMP / "bozuk.json"
bozuk.write_text("{bozuk")
r = calistir("yedek-denetim.py", "--kayit", str(bozuk), "--ozet-json")
test("35b bozuk json: sorun, cikis 0", r.returncode == 0 and json.loads(r.stdout)["durum"] == "sorun")
r = calistir("yedek-denetim.py", "--kayit", str(TMP / "yoktur.json"), "--ozet-json")
test("35c yedekler.json yok: sorun", json.loads(r.stdout)["durum"] == "sorun" and "bulunamadı" in r.stdout)

# 36 silindi
kf, kok, kut = yedek_ortam("y36", [kayit(kimlik="eski-2026-01-01", tarih="2026-01-01", durum="silindi", silindi_tarih="2026-02-01", yol=str(TMP / "y36" / "yok"))])
j, _ = yj(kf, kok, kut)
test("36 silindi kaydi yok sayilir", j["durum"] == "temiz" and "0 yedek kayıtlı" in j["satirlar"][0])

# 37 ikinci kopya
kf, kok, kut = yedek_ortam("y37", [], ust={"ikinci_kopya_iste": True})
j, _ = yj(kf, kok, kut)
test("37 ikinci kopya istendi, paket yok: dikkat", j["durum"] == "dikkat" and "git bundle" in " ".join(j["satirlar"]))
kf, kok, kut = yedek_ortam("y37b", [kayit(kimlik="kutuphane-2026-11-01", tur="git-paketi", tarih="2026-11-01")], dosyalar=["x.bundle"], ust={"ikinci_kopya_iste": True})
j, _ = yj(kf, kok, kut)
test("37b 10 gunluk paket: sorun yok", "git bundle" not in " ".join(j["satirlar"]))
kf, kok, kut = yedek_ortam("y37c", [kayit(kimlik="kutuphane-2026-08-03", tur="git-paketi", tarih="2026-08-03")], dosyalar=["x.bundle"], ust={"ikinci_kopya_iste": True})
j, _ = yj(kf, kok, kut)
test("37c 100 gunluk paket: dikkat", "git bundle" in " ".join(j["satirlar"]))
kf, kok, kut = yedek_ortam("y37d", [], ust={"ikinci_kopya_iste": False})
j, _ = yj(kf, kok, kut)
test("37d istenmediyse sessiz", j["durum"] == "temiz")

# 38 saflik / cikis kodlari
kf, kok, kut = yedek_ortam("y38", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=["x.txt"])
j, r = yj(kf, kok, kut)
test("38 ozet-json saf", set(j) == {"arac", "durum", "satirlar", "karar_bekleyen"} and j["arac"] == "yedek-denetim" and r.stderr == "")
test("38b --ozet-json --rapor 2; --siki temizde 0", yd(kf, kok, kut, "--ozet-json", "--rapor").returncode == 2 and yd(kf, kok, kut, "--siki").returncode == 0)
kf2, kok2, kut2 = yedek_ortam("y38b", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=None)
test("38c --siki sorunda 1, siki olmadan 0", yd(kf2, kok2, kut2, "--siki").returncode == 1 and yd(kf2, kok2, kut2).returncode == 0)

# 40 ad kaliplari
kf, kok, kut = yedek_ortam("y40", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=["x.txt"],
                           ekstra=["genel-klasorler-2026-12-01", "geri-yazilan-2026-12-02", "tuhaf"])
j, _ = yj(kf, kok, kut)
t = " ".join(j["satirlar"])
test("40 bilinen kaliplar adlandirilir", "genel skill klasörü boşaltma yedeği" in t and "geri yazılan genel skill yedeği" in t and "tanınmayan ad" in t)
v = json.loads(kf.read_text())
v["yedekler"].append(kayit(kimlik="genel-klasorler-2026-12-01", tarih="2026-11-10", silme_gun=30, yol=str(kok / "genel-klasorler-2026-12-01")))
kf.write_text(json.dumps(v))
j, _ = yj(kf, kok, kut)
test("40b kayit eklenince kayitsiz bulgusu kalkar", "kayıtsız yedek: genel-klasorler" not in " ".join(j["satirlar"]))

# 41 kayit alani
kf, kok, kut = yedek_ortam("y41", [kayit(kimlik="p-2026-11-08", tur="program", tarih="2026-11-08", kayit="KAYIT.json", silme_gun=30)], dosyalar=["KAYIT.json"])
(kok / "p-2026-11-08" / "KAYIT.json").chmod(0)
j, r = yj(kf, kok, kut)
(kok / "p-2026-11-08" / "KAYIT.json").chmod(0o600)
test("41 kayit dosyasi var: sorun yok (acilmaz, mod 000)", j["durum"] == "temiz" and r.returncode == 0)
(kok / "p-2026-11-08" / "KAYIT.json").unlink()
j, _ = yj(kf, kok, kut)
test("41b kayit dosyasi yok: sorun", j["durum"] == "sorun" and "kayıt dosyası yok" in " ".join(j["satirlar"]))

# 42 koruma blogu sabiti
test("42 GITIGNORE_BLOK P4 satirlarini icerir", "/notlar/son-aylik-calisma.json" in GITIGNORE_BLOK and "/notlar/aylik-ozet.md" in GITIGNORE_BLOK)

# 43 yedek-denetim salt okuma: kok altina hicbir sey yazilmaz
kf, kok, kut = yedek_ortam("y43", [kayit(kimlik="a-2026-11-08", tarih="2026-11-08", silme_gun=30)], dosyalar=["x.txt"], ekstra=["kayitsiz"])
once = agac_anlik(kok.parent)
yd(kf, kok, kut)
yj(kf, kok, kut)
yd(kf, kok, kut, "--kisa")
test("43 yedek-denetim hicbir dosya degistirmez", agac_anlik(kok.parent) == once)

# 44c-44d gevşek izin: gizli bayrağından bağımsız, kök ve her yedek klasörü; kayıtsız yedek de
kf, kok, kut = yedek_ortam("y44a", [kayit(kimlik="n-2026-11-10", tarih="2026-11-10", gizli_icerir="hayir", silme_gun=30)],
                           dosyalar=["s.txt"], ekstra=["kayitsiz-2026-11-10"])
j, _ = yj(kf, kok, kut)
test("44c 700 yedekler: izin uyarisi yok", "izni gevşek" not in " ".join(j["satirlar"]))
(kok / "n-2026-11-10").chmod(0o755)
(kok / "kayitsiz-2026-11-10").chmod(0o755)
kok.chmod(0o755)
r = yd(kf, kok, kut)
j, _ = yj(kf, kok, kut)
t = " ".join(j["satirlar"])
test("44d gizli=hayir ve kayitsiz yedek ile kok gevsekse dikkat (mod degismez)",
     j["durum"] == "dikkat" and "izni gevşek: n-2026-11-10" in t and "izni gevşek: kayitsiz-2026-11-10" in t
     and "yedek klasörünün kendisi" in t and stat.S_IMODE(kok.stat().st_mode) == 0o755)

# 44 --cikti koruması: araç klasörlerine yazılmaz
yasak_hedef = Path.home() / ".claude" / "p3-test-yazilmamali.md"
r44 = subprocess.run([sys.executable, str(ARACLAR / "git-durum.py"), "--gh-yok", "--rapor", "--cikti", str(yasak_hedef)], capture_output=True, text=True)
test("44 git-durum --cikti araç klasörüne yazmaz (çıkış 2)", not yasak_hedef.exists() and r44.returncode == 2 and "yazamaz" in r44.stderr)
r44b = yd(kf, kok, kut, "--rapor", "--cikti", str(yasak_hedef))
test("44b yedek-denetim --cikti araç klasörüne yazmaz", not yasak_hedef.exists() and "yazamaz" in r44b.stderr)

# ---------------------------------------------------------------- sonuc
shutil.rmtree(TMP, ignore_errors=True)
gecen = sum(1 for _, k in SONUC if k)
for ad, k in SONUC:
    if not k:
        print("BAŞARISIZ:", ad)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
