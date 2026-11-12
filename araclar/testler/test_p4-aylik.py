#!/usr/bin/env python3
"""P4 testleri: aylik-ozet.py, arsiv-guncelle.py'nin salt okuma/rapor tarafı (aşama 1) ve --aylik zinciri (aşama 2).
Yalnız geçici dizin ve sahte veri; gerçek ev, gerçek kütüphane, gerçek gh ve ağ KULLANILMAZ.
Çalıştırma: python3 araclar/testler/test_p4-aylik.py   (son satır: N/N test geçti)"""
import contextlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import traceback
from datetime import date, datetime, timedelta
from pathlib import Path

GERCEK = Path(__file__).resolve().parent.parent.parent
OZET = GERCEK / "araclar" / "aylik-ozet.py"
GUNCELLE = GERCEK / "araclar" / "arsiv-guncelle.py"
TMP = Path(tempfile.mkdtemp(prefix="p4test-")).resolve()
EV = TMP / "ev"
BIN = TMP / "bin"
EV.mkdir()
BIN.mkdir()
(BIN / "gh").write_text('#!/bin/sh\ncase "$GHMODE" in\n  ok) echo 5000;;\n  *) exit 1;;\nesac\n')
(BIN / "gh").chmod(0o755)
ENV = dict(os.environ, HOME=str(EV), PATH=f"{BIN}:{os.environ['PATH']}", GHMODE="ok",
           GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
           GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
os.environ.update({k: ENV[k] for k in ("HOME", "PATH", "GHMODE", "GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_COMMITTER_NAME",
                                       "GIT_COMMITTER_EMAIL", "GIT_CONFIG_GLOBAL", "GIT_CONFIG_SYSTEM")})
sayac = [0]
FAKE = '''import sys, json, time, pathlib
k = pathlib.Path(__file__).resolve().parent.parent
ad = pathlib.Path(__file__).stem
(k / ".isaret").mkdir(exist_ok=True)
(k / ".isaret" / (ad + ".arg")).write_text(" ".join(sys.argv[1:]))
c = json.loads((k / ".isaret" / (ad + ".cfg")).read_text()) if (k / ".isaret" / (ad + ".cfg")).exists() else {}
if "--help" in sys.argv:
    print("usage: --atla"); sys.exit(0)
if c.get("uyku"): time.sleep(c["uyku"])
if c.get("yaz"): (k / c["yaz"]).write_text("x")
if c.get("ham") is not None: sys.stdout.write(c["ham"])
elif "--ozet-json" in sys.argv: print(json.dumps(c.get("json") or {"arac": ad, "durum": "temiz", "satirlar": [ad + " tamam"], "karar_bekleyen": []}))
sys.exit(c.get("kod", 0))
'''
ARACLAR = ["git-durum", "yedek-denetim", "genel-bekci", "program-denetim", "proje-kullanimi", "skill-ekle", "konu-takip"]


def sh(kok, *a):
    return subprocess.run(["git", *a], cwd=kok, capture_output=True, text=True, env=ENV)


def kutuphane(araclar=True, ozet_kopya=False):
    sayac[0] += 1
    kok = TMP / f"lib{sayac[0]}"
    (kok / "araclar").mkdir(parents=True)
    (kok / "notlar").mkdir()
    sh(kok, "init", "-q", "-b", "master")
    (kok / ".gitignore").write_text(".isaret/\n.guncelleme-kilidi\n.gecici/\nnotlar/son-aylik-calisma.json\nnotlar/aylik-ozet.md\n")
    for ad in (ARACLAR + ["dogrula", "github-skill-listesi", "kaynak-cek"] if araclar else []):
        (kok / "araclar" / f"{ad}.py").write_text(FAKE)
    if ozet_kopya:
        (kok / "araclar" / "aylik-ozet.py").write_text(OZET.read_text(encoding="utf-8"))
    (kok / "kaynaklar.json").write_text(json.dumps({"repolar": []}))
    sh(kok, "add", "-A")
    sh(kok, "commit", "-q", "-m", "ilk")
    return kok


def cfg(kok, ad, **c):
    (kok / ".isaret").mkdir(exist_ok=True)
    (kok / ".isaret" / f"{ad}.cfg").write_text(json.dumps(c))


def arac_json(ad, durum="temiz", satirlar=None, karar=None):
    return {"arac": ad, "durum": durum, "satirlar": satirlar or [ad + " tamam"], "karar_bekleyen": karar or []}


def ozet(kok, *a, js=True):
    r = subprocess.run([sys.executable, str(OZET), "--kok", str(kok), *(["--ozet-json"] if js else []), *a],
                       capture_output=True, text=True, env=ENV, timeout=120)
    return (json.loads(r.stdout) if js else r.stdout), r


def isaret(kok, ad):
    return (kok / ".isaret" / f"{ad}.arg").exists()


def damga(kok, **d):
    (kok / "notlar").mkdir(exist_ok=True)
    (kok / "notlar" / "son-aylik-calisma.json").write_text(json.dumps(d))


def gun_once(n):
    return (date.today() - timedelta(days=n)).isoformat()


def metin(d):
    return "\n".join(d["satirlar"] + d["karar_bekleyen"])


# ------------------------------------------------------------------ A: aylik-ozet.py
def t01_birlesme():
    k = kutuphane()
    for ad in ARACLAR:
        cfg(k, ad, json=arac_json(ad, "temiz", None, ["ortak karar cümlesi bir"]))
    cfg(k, "git-durum", json=arac_json("git-durum", "dikkat", ["gd satiri"], ["ortak karar cümlesi bir", "ikinci karar"]))
    d, r = ozet(k)
    assert r.returncode == 0 and d["arac"] == "aylik-ozet"
    assert d["karar_bekleyen"].count("ortak karar cümlesi bir") == 1 and "ikinci karar" in d["karar_bekleyen"]
    assert d["durum"] == "dikkat"


def t02_eksik_arac():
    k = kutuphane()
    (k / "araclar" / "yedek-denetim.py").unlink()
    d, r = ozet(k)
    assert r.returncode == 0 and d["durum"] == "dikkat"
    assert "yedek-denetim: araç kütüphanede yok (atlandı)" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert isaret(k, "git-durum") and isaret(k, "genel-bekci") and not isaret(k, "yedek-denetim")


def t03_cikis1_cop():
    k = kutuphane()
    cfg(k, "yedek-denetim", ham="çöp çıktı\n", kod=1)
    d, r = ozet(k)
    md = (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert "yedek-denetim: çalışmadı (çıkış 1)" in md and d["durum"] == "dikkat"
    assert isaret(k, "genel-bekci")


def t04_sema_bozuk():
    k = kutuphane()
    cfg(k, "genel-bekci", json={"arac": "genel-bekci", "durum": "kötü", "satirlar": [], "karar_bekleyen": []})
    ozet(k)
    assert "genel-bekci: çıktı biçimi bozuk" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")


def t05_zaman_asimi():
    k = kutuphane()
    cfg(k, "git-durum", uyku=5)
    ozet(k, "--zaman-asimi", "1")
    assert "git-durum: zaman aşımı (1 sn)" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")


def t06_json_oncesi_cop():
    k = kutuphane()
    cfg(k, "git-durum", ham="uyarı satırı\n" + json.dumps(arac_json("git-durum", "dikkat", ["gercek satir"])) + "\n")
    ozet(k)
    md = (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert "gercek satir" in md and "çıktı biçimi bozuk" not in md


def t07_damga():
    k = kutuphane()
    d, _ = ozet(k, "--hizli")
    assert "ilk kurulum" in "\n".join(d["satirlar"]) and not any("Aylık çalışmayı şimdi" in c for c in d["karar_bekleyen"])
    damga(k, son_calisma=gun_once(10) + "T10:00:00+03:00", son_sonuc="guncellendi", son_basarili=gun_once(10))
    d, _ = ozet(k, "--hizli")
    assert not any("şimdi yapayım" in c for c in d["karar_bekleyen"]) and "10 gün önce" in metin(d)
    damga(k, son_calisma=gun_once(40) + "T10:00:00+03:00", son_sonuc="guncellendi")
    d, _ = ozet(k, "--hizli")
    assert any("şimdi yapayım" in c for c in d["karar_bekleyen"]) and d["durum"] == "dikkat"
    damga(k, son_calisma=gun_once(80) + "T10:00:00+03:00", son_sonuc="guncellendi")
    d, _ = ozet(k, "--hizli")
    assert d["durum"] == "sorun"
    damga(k, son_calisma=gun_once(5) + "T10:00:00+03:00", son_sonuc="kismi", son_neden="kirli ağaç")
    d, _ = ozet(k, "--hizli", "--siki")
    assert d["durum"] == "dikkat" and "yarım kaldı: kismi — kirli ağaç" in _tum_md(k)
    damga(k, son_calisma=gun_once(5) + "T10:00:00+03:00", son_sonuc="guncellendi", atlanan_kaynaklar=["a/b"], ad_degisen={"x/y": "x/z"})
    d, _ = ozet(k, "--hizli")
    assert any("a/b" in c and "KAYIP" in c for c in d["karar_bekleyen"]) and any("x/y → x/z" in c for c in d["karar_bekleyen"])


def _dal_kur(k):
    env = dict(ENV, GIT_AUTHOR_DATE=f"{gun_once(50)}T10:00:00", GIT_COMMITTER_DATE=f"{gun_once(50)}T10:00:00")
    subprocess.run(["git", "switch", "-q", "-c", "guncelleme/2026-10"], cwd=k, env=env)
    (k / "notlar" / "guncelleme-gecmisi.md").write_text(
        "# G\n\n- **Karar bekleyen yeni skiller** (3; arşive alınmadı): `a`\n- **Yeniden incelenecek** (2): `b` (x)\n")
    subprocess.run(["git", "add", "-A"], cwd=k, env=env)
    subprocess.run(["git", "commit", "-q", "-m", "dal"], cwd=k, env=env)
    sh(k, "switch", "-q", "master")
    sh(k, "branch", "takip/2026-09")  # master'da: zaten birleşmiş
    sh(k, "switch", "-q", "-c", "takip/2026-11")
    (k / "x.txt").write_text("x")
    sh(k, "add", "-A")
    sh(k, "commit", "-q", "-m", "takip")
    sh(k, "switch", "-q", "master")


def t08_dallar():
    k = kutuphane()
    _dal_kur(k)
    d, _ = ozet(k)
    m = (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert "guncelleme/2026-10 45 günden eski" in m and d["durum"] == "dikkat"
    assert "Bekleyen dal takip/2026-11 (0 gün" in m and "takip/2026-11 45 günden" not in m
    assert "takip/2026-09 zaten master'a birleşmiş; silebilirsin" in m
    assert not any("takip/2026-09" in c for c in d["karar_bekleyen"])
    assert "guncelleme/2026-10: 3 yeni skill karar bekliyor (kaynaklar.json 'dahil'/'haric')" in d["karar_bekleyen"]
    assert "guncelleme/2026-10: 2 skill yeniden incelenecek (rehber/07)" in d["karar_bekleyen"]


def _tum_md(k, *a):
    ozet(k, *a)
    return (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")


def t09_yedek_regex():
    k = kutuphane()
    (k / "araclar" / "konu-takip.py").unlink()
    (k / "araclar" / "program-denetim.py").write_text("import sys; sys.exit(3)\n")
    (k / "notlar" / "konu-takip.md").write_text("## e\n**odaklı aday: 1**\n## m\n**odaklı aday: 3**\n")
    (k / "notlar" / "populer-skiller.md").write_text("# P\n\n## Yeni adaylar (12) — x\n")
    (k / "notlar" / "github-trend.md").write_text(
        "## Son taramada trend'de olup kütüphanede olmayan repolar\n\n| Repo | SKILL.md | Şu an |\n|---|---|---|\n"
        "| a/b | 4 | x |\n| c/d | 0 | x |\n| e/f | 2 | x |\n")
    (k / "notlar" / "program-denetimi.md").write_text("| hyperframes | 1 | YENİ SÜRÜM VAR |\n")
    (k / "notlar" / "kararlar.md").write_text("# K\n\n## Karar bekleyenler\n- [ ] ilk açık karar\n- [x] bitmiş karar\n- [ ] ikinci açık karar\n")
    d, _ = ozet(k)
    assert "4 odaklı aday repo karar bekliyor (notlar/konu-takip.md)" in d["karar_bekleyen"]
    assert "12 yeni aday repo (notlar/populer-skiller.md)" in d["karar_bekleyen"]
    assert "2 trend aday repo (SKILL.md içeren; notlar/github-trend.md)" in d["karar_bekleyen"]
    assert "hyperframes: yeni sürüm var, güncelleme onayı bekliyor (rehber/11)" in d["karar_bekleyen"]
    assert "ilk açık karar" in d["karar_bekleyen"] and "ikinci açık karar" in d["karar_bekleyen"] and "bitmiş karar" not in d["karar_bekleyen"]
    # bozuk dosyalar: çökme yok
    (k / "notlar" / "konu-takip.md").write_bytes(b"\xff\xfe\x00bozuk")
    (k / "notlar" / "github-trend.md").write_text("## Son taramada trend'de olup kütüphanede olmayan repolar\n| x |\n")
    d, r = ozet(k)
    assert r.returncode == 0 and "Traceback" not in r.stderr and d["arac"] == "aylik-ozet"


def t10_rapor_yasi():
    k = kutuphane()
    (k / "notlar" / "populer-skiller.md").write_text(f"# P\n\n> `x` üretir · {gun_once(60)} · y\n")
    (k / "trend.json").write_text(json.dumps({"son_tarama": gun_once(3)}))
    (k / "notlar" / "yol-denetimi.md").write_text("# Y\n\n> tarih yok burada\n")
    md = _tum_md(k)
    assert "populer-skiller: 60 gün eski" in md and "github-trend: " in md and "yol-denetimi: tarih okunamadı" in md
    assert "| populer-skiller | " in md and "| dikkat |" in md
    d, _ = ozet(k)
    assert d["durum"] == "dikkat"
    assert not any("github-trend" in s and "eski" in s for s in d["satirlar"])


def t11_hizli_alt_kume():
    k = kutuphane()
    d, r = ozet(k, "--hizli")
    for ad in ("genel-bekci", "git-durum", "yedek-denetim", "konu-takip"):
        assert isaret(k, ad), ad
    # skill-ekle --araclar sürüm komutları çalıştırır: hızlı kipte koşmaz
    assert not isaret(k, "program-denetim") and not isaret(k, "proje-kullanimi") and not isaret(k, "skill-ekle")
    assert "--gh-yok" in (k / ".isaret" / "git-durum.arg").read_text()
    assert not (k / "notlar" / "aylik-ozet.md").exists() and r.returncode == 0
    t, _ = ozet(k, "--hizli", js=False)
    assert len(t.strip().splitlines()) <= 15
    t2, _ = ozet(k, "--oturum", js=False)
    assert t2 == t


def t12_hizli_tam_ozet_yasi():
    k = kutuphane()
    meta = {"zaman": f"{gun_once(50)}T10:00:00+03:00", "mod": "tam", "durum": "temiz", "araclar": {}, "karar_sayisi": 0}
    (k / "notlar" / "aylik-ozet.md").write_text(f"<!-- aylik-ozet: {json.dumps(meta)} -->\n# x\n")
    d, _ = ozet(k, "--hizli")
    assert "Son tam özet: " in metin(d) and "(50 gün önce)" in metin(d) and d["durum"] == "dikkat"
    d, _ = ozet(kutuphane(), "--hizli")
    assert d["durum"] == "temiz" and "her şey yolunda" in metin(d)


def t13_ozet_json_tam():
    k = kutuphane()
    r = subprocess.run([sys.executable, str(OZET), "--kok", str(k), "--ozet-json"], capture_output=True, text=True, env=ENV)
    d = json.loads(r.stdout)
    assert set(d) == {"arac", "durum", "satirlar", "karar_bekleyen"} and d["arac"] == "aylik-ozet"
    assert len(r.stdout.strip().splitlines()) == 1


def t14_siki():
    k = kutuphane()
    damga(k, son_calisma=gun_once(80) + "T10:00:00+03:00", son_sonuc="guncellendi")
    _, r = ozet(k, "--hizli", "--siki")
    assert r.returncode == 1
    _, r = ozet(k, "--hizli")
    assert r.returncode == 0
    damga(k, son_calisma=gun_once(40) + "T10:00:00+03:00", son_sonuc="guncellendi")
    _, r = ozet(k, "--hizli", "--siki")
    assert r.returncode == 0


def t15_md_yazma_ve_ignore():
    k = kutuphane()
    d, _ = ozet(k)
    md = (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    ilk = md.splitlines()[0]
    assert ilk.startswith("<!-- aylik-ozet: ") and json.loads(ilk[len("<!-- aylik-ozet: "):-4])["mod"] == "tam"
    assert "## Senin kararını bekleyenler" in md
    # .gitignore'da değilse YAZILMAZ
    k2 = kutuphane()
    (k2 / ".gitignore").write_text(".isaret/\n")
    sh(k2, "commit", "-qam", "gi")
    d, _ = ozet(k2)
    assert not (k2 / "notlar" / "aylik-ozet.md").exists()
    assert any(".gitignore'da değil" in s for s in d["satirlar"]) and d["durum"] == "dikkat"


def t16_sozlesme_ihlali():
    k = kutuphane()
    (k / "notlar" / "x.md").write_text("a")
    (k / "notlar" / "proje-durumu.md").write_text("a")
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "izli")
    cfg(k, "genel-bekci", yaz="notlar/x.md")
    d, _ = ozet(k, "--paralel", "1")
    assert d["durum"] == "dikkat"
    md = (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert "genel-bekci --ozet-json ile dosya yazdı: notlar/x.md" in md and "| genel-bekci | dikkat |" in md
    # izinli yol ihlal sayılmaz
    k2 = kutuphane()
    (k2 / "notlar" / "proje-durumu.md").write_text("a")
    sh(k2, "add", "-A")
    sh(k2, "commit", "-qm", "izli")
    cfg(k2, "proje-kullanimi", yaz="notlar/proje-durumu.md")
    ozet(k2, "--paralel", "1")
    assert "sözleşme ihlali" not in (k2 / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    # uyumlu araçlarla özet sonrası git status boş
    k3 = kutuphane()
    ozet(k3)
    assert sh(k3, "status", "--porcelain").stdout.strip() == ""


def t17_gorev_kopyasi():
    k = kutuphane()
    canli = TMP / "canli-gorev.md"
    (k / "zamanlanmis").mkdir()
    (k / "zamanlanmis" / "aylik-guncelleme.SKILL.md").write_text("aynı")
    canli.write_text("aynı")
    md = _tum_md(k, "--gorev-yolu", str(canli))
    assert "kütüphane kopyasından farklı" not in md
    canli.write_text("farklı")
    d, _ = ozet(k, "--gorev-yolu", str(canli))
    assert "Zamanlanmış görev metni güncellensin mi?" in d["karar_bekleyen"]
    assert "kütüphane kopyasından farklı" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    d, _ = ozet(k, "--gorev-yolu", str(TMP / "yok.md"))
    assert "Zamanlanmış görev metni güncellensin mi?" not in d["karar_bekleyen"]


def t18_metin_cumleleri():
    k = kutuphane()
    t, _ = ozet(k, "--hizli", js=False)
    assert "her şey yolunda" in t and len(t.strip().splitlines()) == 1
    cfg(k, "git-durum", json=arac_json("git-durum", "dikkat", ["gd"], ["bir karar"]))
    t, _ = ozet(k, js=False)
    assert "Senin kararını bekleyen 1 şey:" in t and "  1. bir karar" in t and "Ayrıntı: notlar/aylik-ozet.md" in t
    cfg(k, "git-durum", json=arac_json("git-durum", "dikkat", ["gd"]))
    t, _ = ozet(k, js=False)
    assert "Senin kararını bekleyen bir şey yok." in t and "• git-durum (dikkat): gd" in t


def t19_gizlilik():
    k = kutuphane()
    (k / ".env").write_text("SIR_DEGER_12345")
    cfg(k, "git-durum", json=arac_json("git-durum", "dikkat", ["u" * 400], ["k" * 400]))
    t, _ = ozet(k, js=False)
    assert all(len(s) <= 320 for s in t.splitlines()) and "SIR_DEGER_12345" not in t
    assert "SIR_DEGER_12345" not in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    d, _ = ozet(k)
    assert all(len(s) <= SATIR for s in d["karar_bekleyen"])


SATIR = 300


def agac(k):
    return sorted((str(p.relative_to(k)), p.stat().st_size) for p in k.rglob("*")
                  if p.is_file() and ".git/" not in str(p) and ".isaret" not in str(p) and p.name != "aylik-ozet.md")


def t20_salt_okuma():
    k = kutuphane()
    once = (agac(k), sh(k, "status", "--porcelain").stdout, sh(k, "branch").stdout, sh(k, "rev-parse", "HEAD").stdout)
    ozet(k)
    ozet(k, "--hizli")
    sonra = (agac(k), sh(k, "status", "--porcelain").stdout, sh(k, "branch").stdout, sh(k, "rev-parse", "HEAD").stdout)
    assert once == sonra


def t21_triyaj_ve_kabul():
    k = kutuphane()
    adaylar = [f"org{i}/repo{i} (★{100 - i}, e-ticaret)" for i in range(5)] + [f"t{i}/tr{i} (trend, 3 skill)" for i in range(5)] \
        + [f"p{i}/po{i} (★9, popüler)" for i in range(5)]
    cfg(k, "konu-takip", json=arac_json("konu-takip", "dikkat", ["özet"], adaylar))
    d, _ = ozet(k)
    k_ = d["karar_bekleyen"]
    satir = [c for c in k_ if c.startswith("konu takibi:")]
    assert len(satir) == 1 and "en az 5 aday" in satir[0] and "org0/repo0" in satir[0] and "konu-takip.py --karar" in satir[0]
    assert len([c for c in k_ if c.startswith(("trend:", "popüler:"))]) == 2
    assert not any("(★" in c and "e-ticaret" in c for c in k_)
    cfg(k, "konu-takip", json=arac_json("konu-takip", "dikkat", ["özet"], [f"r{i}/x{i} (★1, k)" for i in range(8)]))
    d, _ = ozet(k)
    s = [c for c in d["karar_bekleyen"] if c.startswith("konu takibi:")][0]
    assert "en az 8 aday" in s and "ilk 5: r0/x0, r1/x1, r2/x2, r3/x3, r4/x4" in s and "+3 daha" in s
    # kabul edilenler
    cfg(k, "git-durum", json=arac_json("git-durum", "dikkat", ["g"], ["11 commit GitHub'a gönderilsin mi?"]))
    (k / "notlar" / "kararlar.md").write_text(
        "# K\n\n## Kabul edilen bekleyenler (aylık özette susturulur)\n- commit GitHub'a gönderilsin\n- kısa\n")
    d, _ = ozet(k)
    assert not any("GitHub'a gönderilsin" in c for c in d["karar_bekleyen"])
    (k / "notlar" / "kararlar.md").write_text(
        f"# K\n\n## Kabul edilen bekleyenler (x)\n- commit GitHub'a gönderilsin | {gun_once(1)}\n")
    d, _ = ozet(k)
    assert any("GitHub'a gönderilsin" in c for c in d["karar_bekleyen"])  # tarih geçmiş: süzgeç kalktı
    (k / "notlar" / "kararlar.md").write_text("# K\n\n## Kabul edilen bekleyenler (x)\n- gönder\n")
    d, _ = ozet(k)
    assert any("GitHub'a gönderilsin" in c for c in d["karar_bekleyen"])  # 8 karakterden kısa ifade yok sayılır


def t22_arac_listesi():
    k = kutuphane()
    (k / "araclar" / "ortak.py").write_text('OZET_ARACLARI = [("git-durum", []), ("yeni-arac", ["--x"])]\n')
    (k / "araclar" / "yeni-arac.py").write_text(FAKE)
    ozet(k)
    assert isaret(k, "yeni-arac") and "--x" in (k / ".isaret" / "yeni-arac.arg").read_text()
    assert isaret(k, "konu-takip") and isaret(k, "skill-ekle") and isaret(k, "git-durum")
    assert not isaret(k, "yedek-denetim")  # fake ortak listesinde yok
    (k / "araclar" / "ortak.py").write_text("X = 1\n")  # OZET_ARACLARI yok -> sabit yedek
    k2 = k
    for f in (k2 / ".isaret").iterdir():
        f.unlink()
    ozet(k2)
    assert isaret(k2, "yedek-denetim") and isaret(k2, "proje-kullanimi")
    assert "--yaz" in (k2 / ".isaret" / "proje-kullanimi.arg").read_text()
    ozet(k2, "--yazmadan")
    assert "--yaz" not in (k2 / ".isaret" / "proje-kullanimi.arg").read_text().replace("--saglik", "")


def t23_bekleyen_birincil_yedek():
    k = kutuphane()
    (k / "notlar" / "populer-skiller.md").write_text("# P\n\n## Yeni adaylar (99) — x\n")
    cfg(k, "konu-takip", json=arac_json("konu-takip", "temiz", ["x"], []))
    d, _ = ozet(k)
    assert not any("99 yeni aday" in c for c in d["karar_bekleyen"])  # araç çalıştı: md okunmaz
    cfg(k, "konu-takip", ham="bozuk", kod=1)
    d, _ = ozet(k)
    assert "99 yeni aday repo (notlar/populer-skiller.md)" in d["karar_bekleyen"]
    assert "konu-takip: yedek okuma (araç çalışmadı)" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")


def t24_damga_yok_yedek_tarih():
    k = kutuphane()
    (k / "notlar" / "guncelleme-gecmisi.md").write_text(f"# G\n\n## {gun_once(50)} — `guncelleme/x`\n\n## 2020-01-01 — `eski`\n")
    d, _ = ozet(k, "--hizli")
    assert f"Aylık çalışma damgası yok; son kayıtlı güncelleme {gun_once(50)} (50 gün önce)" in _tum_md(k)
    assert any("şimdi yapayım" in c for c in d["karar_bekleyen"])
    (k / "notlar" / "guncelleme-gecmisi.md").write_text(f"# G\n\n## {gun_once(10)} — `g`\n")
    d, _ = ozet(k, "--hizli")
    assert not any("şimdi yapayım" in c for c in d["karar_bekleyen"])
    (k / "notlar" / "guncelleme-gecmisi.md").unlink()
    d, _ = ozet(k, "--hizli")
    assert not any("şimdi yapayım" in c for c in d["karar_bekleyen"]) and "ilk kurulum" in metin(d)


def t25_kayip_kaynak():
    k = kutuphane()
    damga(k, son_calisma=gun_once(3) + "T10:00:00+03:00", son_sonuc="guncellendi", atlanan_kaynaklar=["a/b", "c/d"])
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": [{"repo": "a/b", "tip": "KAYIP"}, {"repo": "c/d", "tip": "T1"}]}))
    d, _ = ozet(k)
    assert not any(c.startswith("a/b ") for c in d["karar_bekleyen"])
    assert "KAYIP işaretli kaynak: a/b" in (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    assert any(c.startswith("c/d kaynakta erişilemiyor") for c in d["karar_bekleyen"])
    (k / "notlar" / "kararlar.md").write_text("# K\n\n## Kabul edilen bekleyenler (x)\n- c/d kaynakta erişilemiyor\n")
    d, _ = ozet(k, "--hizli")
    assert not any(c.startswith("c/d ") for c in d["karar_bekleyen"])


def t26_cokme_yok():
    k = kutuphane()
    (k / "notlar" / "son-aylik-calisma.json").write_text("{bozuk json")
    (k / "kaynaklar.json").write_text("bozuk")
    d, r = ozet(k, "--hizli")
    assert r.returncode == 0 and "Traceback" not in r.stderr and d["arac"] == "aylik-ozet"
    d, r = ozet(TMP / "yok-dizin", "--hizli")
    assert r.returncode == 0 and "Traceback" not in r.stderr and d["arac"] == "aylik-ozet"


# ------------------------------------------------------------------ B: arsiv-guncelle.py (modül içi, yamalı)
def yukle(kok):
    spec = importlib.util.spec_from_file_location(f"arsiv_guncelle_{sayac[0]}_{id(kok)}", GUNCELLE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.KOK = kok
    m.GECMIS = kok / "notlar" / "guncelleme-gecmisi.md"
    m.KILIT = kok / ".guncelleme-kilidi"
    m.DAMGA = kok / "notlar" / "son-aylik-calisma.json"
    m.REGISTRY = kok / "registry.json"
    m.KAYNAKLAR = kok / "kaynaklar.json"
    m.etkilenen_projeler = lambda repolar: {}
    m.repo_guncel = lambda r: r
    return m


def cikti(f, *a, **kw):
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        try:
            s = f(*a, **kw)
        except SystemExit as e:
            s = ("EXIT", e.code)
    return s, b.getvalue()


def kaynak_kur(k, repolar, commit="c1"):
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": [{"repo": r, "tip": "T1"} for r in repolar]}))
    (k / "registry.json").write_text(json.dumps({"skiller": [{"repo": r, "commit": commit} for r in repolar]}))
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "kaynak")


def sahte_api(davranis, cagri=None):
    def gh_api(yol):
        if cagri is not None:
            cagri.append(yol)
        repo = "/".join(yol.split("/")[1:3])
        b = davranis[repo]
        if b == "404":
            raise _GB("yok")
        if b == "err":
            raise RuntimeError("ağ")
        return b
    return gh_api


_GB = None


def t30_kirli_dosyalar():
    k = kutuphane()
    (k / "a b.txt").write_text("1")
    (k / "türkçe-ğüş.txt").write_text("1")
    (k / "eski.txt").write_text("x")
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "e")
    sh(k, "mv", "eski.txt", "yeni ad.txt")
    (k / "araclar" / "git-durum.py").write_text("# değişti\n")
    (k / "notlar" / "son-aylik-calisma.json").write_text("{}")
    m = yukle(k)
    kirli = dict((y, xy) for xy, y in m.kirli_dosyalar())
    assert kirli["yeni ad.txt"].startswith("R") and "eski.txt" not in kirli
    assert "M" in kirli["araclar/git-durum.py"] and "notlar/son-aylik-calisma.json" not in kirli
    assert m.kirli_ozet(m.kirli_dosyalar(), 1).endswith("… +1")
    assert m.yoksayiliyor_mu(k / "notlar" / "aylik-ozet.md") is True and m.yoksayiliyor_mu(k / "x.py") is False
    (k / "neu.txt").write_text("1")
    assert ("??", "neu.txt") in m.kirli_dosyalar()


def t31_uygula_kirli():
    k = kutuphane()
    (k / "kirli ağaç.txt").write_text("x")
    m = yukle(k)
    s, c = cikti(m.uygula, [], {}, True)
    assert s[0] == "EXIT" and "kirli ağaç.txt" in s[1] and "--aylik --kuru" in s[1] and "(1 dosya)" in s[1]
    assert not (k / ".guncelleme-kilidi").exists()


def t32_gh_hazir():
    m = yukle(kutuphane())
    os.environ["GHMODE"] = "ok"
    assert m.gh_hazir() == (True, 5000, "")
    os.environ["GHMODE"] = "fail"
    ok, kalan, neden = m.gh_hazir()
    assert (ok, kalan) == (False, None) and "gh" in neden
    os.environ["GHMODE"] = "ok"
    eski = os.environ["PATH"]
    os.environ["PATH"] = "/yok"
    try:
        assert m.gh_hazir() == (False, None, "gh kurulu değil")
    finally:
        os.environ["PATH"] = eski
    gercek = m.subprocess.run
    m.subprocess.run = lambda *a, **kw: (_ for _ in ()).throw(m.subprocess.TimeoutExpired("gh", 30))
    try:
        assert m.gh_hazir() == (False, None, "zaman aşımı")
    finally:
        m.subprocess.run = gercek


def t33_rapor_cevrimdisi():
    k = kutuphane()
    kaynak_kur(k, ["a/b"])
    m = yukle(k)
    global _GB
    _GB = m.GhBulunamadi
    cagri = []
    m.gh_api = sahte_api({"a/b": {"sha": "x"}}, cagri)
    os.environ["GHMODE"] = "fail"
    try:
        s, c = cikti(m.rapor)
    finally:
        os.environ["GHMODE"] = "ok"
    assert s == ([], [], {}) and cagri == [] and m.CEVRIMDISI is True
    assert "ATLANDI" in c and "Traceback" not in c
    assert "--github" not in (k / ".isaret" / "dogrula.arg").read_text()


def t34_rapor_hatalar():
    k = kutuphane()
    r = ["o/r1", "o/r2", "o/r3", "o/r4", "o/r5"]
    kaynak_kur(k, r, commit="c1")
    m = yukle(k)
    global _GB
    _GB = m.GhBulunamadi
    ok = {"sha": "c1"}
    m.gh_api = sahte_api({"o/r1": "404", "o/r2": "err", "o/r3": "err", "o/r4": "err", "o/r5": ok})
    s, c = cikti(m.rapor)
    assert s[1] == ["o/r1"] and m.ULASILAMAYAN == ["o/r2", "o/r3", "o/r4", "o/r5"] and "art arda 3" in c
    assert "! o/r1: erişilemiyor (silinmiş, private ya da adı değişmiş olabilir)" in c and "Kontrol edilemeyen kaynak: 4" in c
    assert "Tüm kaynaklar güncel." not in c
    m.gh_api = sahte_api({"o/r1": "err", "o/r2": ok, "o/r3": "err", "o/r4": "err", "o/r5": ok})
    s, c = cikti(m.rapor)
    assert m.ULASILAMAYAN == ["o/r1", "o/r3", "o/r4"] and "art arda 3" not in c and s[1] == []  # sayaç sıfırlandı
    assert "--github" in (k / ".isaret" / "dogrula.arg").read_text()
    m.gh_api = sahte_api({x: ok for x in r})
    s, c = cikti(m.rapor)
    assert "Tüm kaynaklar güncel." in c and m.ULASILAMAYAN == []


def t35_ad_degisikligi():
    k = kutuphane()
    kaynak_kur(k, ["eski/ad"])
    m = yukle(k)
    global _GB
    _GB = m.GhBulunamadi
    yeni = {"sha": "c1", "html_url": "https://github.com/yeni/isim/commit/c1"}
    m.gh_api = sahte_api({"eski/ad": yeni})
    s, c = cikti(m.rapor)
    assert m.ADI_DEGISEN == {"eski/ad": "yeni/isim"} and "AD DEĞİŞMİŞ: eski/ad -> yeni/isim" in c
    m.repo_guncel = lambda r: "yeni/isim"  # kaynaklar.json eski_adlar ile zaten eşleşiyor
    cikti(m.rapor)
    assert m.ADI_DEGISEN == {}
    m.repo_guncel = lambda r: r
    m.gh_api = sahte_api({"eski/ad": {"sha": "c1"}})  # html_url yok: sessiz
    cikti(m.rapor)
    assert m.ADI_DEGISEN == {}
    m.gh_api = sahte_api({"eski/ad": {"sha": "c1", "html_url": "https://github.com/ESKI/Ad/commit/c1"}})  # büyük/küçük harf
    cikti(m.rapor)
    assert m.ADI_DEGISEN == {}


def t36_main_kapilar_ve_cikis():
    k = kutuphane()
    m = yukle(k)
    argv = sys.argv

    def calis(args, rapor_donus, **durum):
        sys.argv = ["arsiv-guncelle.py", *args]
        m.rapor = lambda: (m.__dict__.update(durum) or rapor_donus)
        m.uygula = lambda *a: "UYGULANDI"
        try:
            return cikti(m.main)
        finally:
            sys.argv = argv

    s, c = calis([], ([], [], {}), CEVRIMDISI=True, ULASILAMAYAN=[])
    assert s == 0
    s, c = calis(["--siki"], ([], [], {}), CEVRIMDISI=True, ULASILAMAYAN=[])
    assert s == 2
    s, c = calis(["--siki"], ([], [], {}), CEVRIMDISI=False, ULASILAMAYAN=["x/y"])
    assert s == 2
    s, c = calis(["--siki"], ([], [], {}), CEVRIMDISI=False, ULASILAMAYAN=[])
    assert s == 0
    s, c = calis(["--siki"], ([], ["a/b"], {}), CEVRIMDISI=False, ULASILAMAYAN=[])
    assert s == 1  # eski davranış: erişilemeyen kaynak çıkış 1
    s, c = calis(["--uygula", "--dal"], (["a/b"], ["c/d"], {}), CEVRIMDISI=False, ULASILAMAYAN=[])
    assert s[0] == "EXIT" and "DURDU: erişilemeyen kaynaklar var (c/d)" in s[1] and "'KAYIP'" in s[1]
    s, c = calis(["--uygula", "--dal"], (["a/b"], [], {}), CEVRIMDISI=False, ULASILAMAYAN=["x/y", "z/w"])
    assert s[0] == "EXIT" and "DURDU: 2 kaynak şimdilik kontrol edilemedi" in s[1] and "Hiçbir şey değişmedi" in s[1]
    s, c = calis(["--uygula", "--dal"], ([], [], {}), CEVRIMDISI=True, ULASILAMAYAN=[])
    assert s[0] == "EXIT" and "GitHub'a ulaşılamıyor" in s[1]
    s, c = calis(["--uygula", "--dal"], (["a/b"], [], {}), CEVRIMDISI=False, ULASILAMAYAN=[])
    assert s == "UYGULANDI"
    sh(k, "branch", "takip/2026-11")  # bekleyen dal artık takip/* ile de engeller
    s, c = calis(["--uygula", "--dal"], (["a/b"], [], {}), CEVRIMDISI=False, ULASILAMAYAN=[])
    assert s[0] == "EXIT" and "takip/2026-11" in s[1]


def t37_bekleyen_dallar():
    k = kutuphane()
    _dal_kur(k)
    m = yukle(k)
    d = {x["dal"]: x for x in m.bekleyen_dallar()}
    assert set(d) == {"guncelleme/2026-10", "takip/2026-09", "takip/2026-11"}
    assert d["guncelleme/2026-10"]["gun"] in (50, 51) and d["guncelleme/2026-10"]["birlesmis"] is False
    assert d["takip/2026-09"]["birlesmis"] is True and d["takip/2026-11"]["gun"] == 0
    m.rapor = lambda: ([], [], {})
    sys.argv = ["x"]
    try:
        s, c = cikti(m.main)
    finally:
        sys.argv = ["x"]
    assert "Onay bekleyen dal: guncelleme/2026-10 (50 gün önce hazırlandı)" in c or "(51 gün" in c
    assert "UYARI: guncelleme/2026-10 45 günden eski: birleştir (--birlestir guncelleme/2026-10) ya da sil (git branch -D guncelleme/2026-10)." in c
    assert "takip/2026-09 zaten master'a birleşmiş; silebilirsin: git branch -d takip/2026-09" in c
    assert "UYARI: takip/2026-11" not in c


def t38_birlestir_eski_mesajlar():
    k = kutuphane()
    sh(k, "branch", "takip/2026-08")
    m = yukle(k)
    s, c = cikti(m.birlestir, "olmayan/dal")
    assert s[0] == "EXIT" and s[1].startswith("Dal yok: olmayan/dal. Bekleyen güncelleme dalları") and "takip/2026-08" in s[1]
    (k / "kirli.txt").write_text("x")
    s, c = cikti(m.birlestir, "takip/2026-08")
    assert s[0] == "EXIT" and "kirli.txt" in s[1] and "kaydedilmemiş" in s[1]
    # içe aktarmada yan etki yok: damga/kilit yazılmadı
    assert not (k / ".guncelleme-kilidi").exists() and not (k / "notlar" / "son-aylik-calisma.json").exists()


def t39_aylik_kuru():
    k = kutuphane(ozet_kopya=True)
    kaynak_kur(k, ["a/b"], commit="c1")
    m = yukle(k)
    global _GB
    _GB = m.GhBulunamadi
    m.gh_api = sahte_api({"a/b": {"sha": "c2"}})
    (k / "notlar" / "program-denetimi.md").write_text("x")
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "p")

    def durum():
        return (sh(k, "status", "--porcelain").stdout, sh(k, "branch").stdout, sh(k, "rev-parse", "HEAD").stdout,
                (k / "notlar" / "son-aylik-calisma.json").exists(), (k / "notlar" / "aylik-ozet.md").exists())

    once = durum()
    s, c = cikti(m.aylik, True)
    assert s == 0 and "AYLIK ZİNCİR —" in c and "PLAN: güncelleme dalı guncelleme/" in c and "Ön kontrol" not in c
    assert "Aylık özet (hızlı" in c and durum() == once  # özet --hizli çalıştı, hiçbir şey yazılmadı
    assert "liste ok" not in c and "--github" in (k / ".isaret" / "dogrula.arg").read_text()
    # değişiklik yok -> takip planı
    m.gh_api = sahte_api({"a/b": {"sha": "c1"}})
    s, c = cikti(m.aylik, True)
    assert "PLAN: takip dalı takip/" in c and durum() == once
    # yalnız rapor dosyası değişik
    (k / "notlar" / "program-denetimi.md").write_text("değişti")
    s, c = cikti(m.aylik, True)
    assert "yalnız rapor dosyaları değişmiş (notlar/program-denetimi.md)" in c and "PLAN: yalnız rapor" in c
    assert "git add notlar/program-denetimi.md" in c and sh(k, "rev-parse", "HEAD").stdout == once[2]
    (k / "baska.txt").write_text("x")
    s, c = cikti(m.aylik, True)
    assert "Ön kontrol: kirli ağaç (2 dosya)" in c and "baska.txt" in c
    (k / "baska.txt").unlink()
    sh(k, "checkout", "--", "notlar/program-denetimi.md")
    # bekleyen dal, master değil, gh yok
    sh(k, "branch", "takip/2026-10")
    s, c = cikti(m.aylik, True)
    assert "Ön kontrol: bekleyen dal: takip/2026-10" in c and "PLAN: yalnız rapor" in c
    sh(k, "branch", "-q", "-D", "takip/2026-10")
    sh(k, "switch", "-q", "-c", "baska")
    s, c = cikti(m.aylik, True)
    assert "dal 'baska' (master değil)" in c
    sh(k, "switch", "-q", "master")
    os.environ["GHMODE"] = "fail"
    try:
        s, c = cikti(m.aylik, True)
    finally:
        os.environ["GHMODE"] = "ok"
    assert "Ön kontrol: GitHub'a ulaşılamıyor" in c and "ATLANDI" in c and "PLAN: yalnız rapor" in c
    # kaçan ay
    damga(k, son_calisma=gun_once(40) + "T10:00:00+03:00", son_sonuc="guncellendi")
    m.gh_api = sahte_api({"a/b": {"sha": "c1"}})
    s, c = cikti(m.aylik, True)
    assert "KAÇAN AY: son çalışma 40 gün önce" in c
    # canlı kilit
    (k / ".guncelleme-kilidi").write_text(json.dumps({"pid": os.getpid()}))
    s, c = cikti(m.aylik, True)
    assert s[0] == "EXIT" and "başka bir güncelleme sürüyor" in s[1]


def t40_yardim_ve_belgeler():
    r = subprocess.run([sys.executable, str(GUNCELLE), "--help"], capture_output=True, text=True, env=dict(ENV, GHMODE="fail"), timeout=20)
    assert r.returncode == 0 and "--aylik --kuru" in r.stdout and "Çıkış kodu" in r.stdout and "Traceback" not in r.stderr
    r = subprocess.run([sys.executable, str(OZET), "--help"], capture_output=True, text=True, env=ENV, timeout=20)
    assert r.returncode == 0 and "--hizli" in r.stdout
    for dosya in ("rehber/02-guncelleme-yonergesi.md", "promptlar/08-aylik-guncelleme-onayi.md"):
        t = (GERCEK / dosya).read_text(encoding="utf-8")
        for k in ("aylik-ozet.py", "--birlestir", "takip/"):
            assert k in t, (dosya, k)
    t = (GERCEK / "rehber" / "02-guncelleme-yonergesi.md").read_text(encoding="utf-8")
    assert "--aylik --kuru" in t and "--damga-yaz" not in t  # aşama 2 bayrakları belgelenmemiş
    assert "--takip" not in t.replace("takip/", "")


def t41_karar_komutlari_var_olan_bayrak():
    # karar metni yalnız kodda gerçekten var olan bayrakları önermeli
    k = kutuphane()
    damga(k, son_calisma=gun_once(50) + "T10:00:00+03:00", son_sonuc="guncellendi", son_basarili=gun_once(50))
    d, _ = ozet(k, "--hizli")
    soru = [c for c in d["karar_bekleyen"] if "Aylık çalışmayı şimdi" in c]
    assert soru, d["karar_bekleyen"]
    assert "--aylik --kuru" in soru[0] and "arsiv-guncelle.py --aylik;" in soru[0]
    kaynak = GUNCELLE.read_text(encoding="utf-8")
    for bay in set(re.findall(r"--[a-z]+(?:-[a-z]+)*", soru[0])):
        assert bay in kaynak, bay
    assert "arsiv-guncelle.py --aylik)" not in soru[0]


def t42_ozet_json_yazma_davranisi():
    k = kutuphane()
    d, _ = ozet(k, "--hizli")
    assert not (k / "notlar" / "aylik-ozet.md").exists()
    ozet(k)  # tam mod --ozet-json ile de özet dosyasını yazar (belgelenmiş davranış)
    assert (k / "notlar" / "aylik-ozet.md").exists()
    assert "tam modda --ozet-json de notlar/aylik-ozet.md yazar" in OZET.read_text(encoding="utf-8")


def t43_sonuc_eki_ve_dikkat_sebebi():
    import importlib.util
    sp = importlib.util.spec_from_file_location("aylik_ozet_t43", OZET)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    assert m.sonuc_eki(None) == "" and m.sonuc_eki("guncellendi") == ": guncellendi"
    k = m.kontrol("program-denetim", "dikkat", ["etsyotomasyon: güncel", "hyperframes: YENİ SÜRÜM VAR (0.9.34)"])
    assert "YENİ SÜRÜM" in m.dikkat_sebebi(k)
    k = m.kontrol("x", "dikkat", ["a: 0 aday", "b"], ["karar maddesi"])
    assert m.dikkat_sebebi(k) == "karar maddesi"
    k = m.kontrol("konu-takip", "dikkat", ["e-ticaret: 0 odaklı aday"])
    k["tam_liste"] = [["a", "b"], ["c"]]
    assert m.dikkat_sebebi(k) == "3 aday karar bekliyor"
    kod = OZET.read_text(encoding="utf-8")
    assert "{damga.get('son_sonuc', '?')}" not in kod and "salt okuma · git'e" not in kod


def t44_cikti_koruma_ve_hizli_yonlendirme():
    k = kutuphane()
    yasak = Path.home() / ".claude" / "p4-test-yazilmamali.md"
    r = subprocess.run([sys.executable, str(OZET), "--kok", str(k), "--ozet-json", "--cikti", str(yasak)], capture_output=True, text=True, env=ENV)
    assert not yasak.exists() and "yazamaz" in r.stdout
    d, _ = ozet(k, "--hizli")
    assert not any("daha: notlar/aylik-ozet.md" in x for x in d["satirlar"])

# ------------------------------------------------------------------ C: aşama 2 — --aylik zinciri
ZINCIR_ARACLAR = ["gelistirici-bilgisi", "github-trend", "populer-tarama", "konu-takip", "kaynak-cek", "arsiv-yerlestir", "yol-tara",
                  "program-denetim", "kapsam-denetimi", "katalog-uret", "skill-readme", "skill-calistir", "dogrula", "github-skill-listesi"]


def zincir_kutuphane(repolar=("a/b", "c/d")):
    """Sahte kütüphane: sahte araçlar, arşiv klasörü, kayıtlı kaynaklar (commit c1). Gerçek ağ/ev yok."""
    k = kutuphane(ozet_kopya=True)
    for ad in ZINCIR_ARACLAR + ARACLAR:
        if ad != "aylik-ozet":
            (k / "araclar" / f"{ad}.py").write_text(FAKE)
    (k / "arsiv").mkdir()
    (k / "arsiv" / "x.txt").write_text("1")
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": [{"repo": r, "tip": "T1"} for r in repolar]}))
    (k / "registry.json").write_text(json.dumps({"skiller": [
        {"repo": r, "commit": "c1", "kaynak_yol": "s", "id": r.replace("/", "-") + "-s", "klasor_hash": "h"} for r in repolar]}))
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "kaynak")
    return k


def zincir(k, davranis, siki=False):
    """--aylik (kuru değil) zincirini sahte GitHub yanıtlarıyla koşturur. -> (donus, cikti, modül)"""
    global _GB
    m = yukle(k)
    _GB = m.GhBulunamadi
    m.gh_api = sahte_api(davranis)
    s, c = cikti(m.aylik, False, siki)
    return s, c, m


def stamp(k):
    return json.loads((k / "notlar" / "son-aylik-calisma.json").read_text(encoding="utf-8"))


def t45_aylik_tam_zincir():
    k = zincir_kutuphane()
    once = sh(k, "rev-parse", "HEAD").stdout
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": "404"})
    assert s == 0, c
    for adim in ("Adım 1/5", "Adım 2/5", "Adım 3/5", "Adım 4/5", "Adım 5/5"):
        assert adim in c, adim
    assert "Bu ay erişilemedi: c/d" in c and "SONUÇ: tamam" in c and "ATLANAN KAYNAKLAR: c/d" in c and "Aylık özet —" in c
    dal = re.search(r"^DAL: (guncelleme/\S+)$", c, re.M).group(1)
    assert sh(k, "branch", "--show-current").stdout.strip() == "master" and sh(k, "rev-parse", "HEAD").stdout == once
    assert sh(k, "status", "--porcelain").stdout == "" and not (k / ".guncelleme-kilidi").exists()
    assert dal in sh(k, "branch", "--list", "guncelleme/*").stdout
    assert "--atla c/d" in (k / ".isaret" / "kaynak-cek.arg").read_text()
    assert "c/d" in sh(k, "show", f"{dal}:notlar/guncelleme-gecmisi.md").stdout  # tarihçe kaydında atlanan kaynak
    d = stamp(k)
    assert d["sonuc"] == "tamam" and d["dal"] == dal and d["atlanan_kaynaklar"] == ["c/d"] and d["ozet_durumu"] in ("temiz", "dikkat", "sorun")
    assert d["tarih"][:10] == date.today().isoformat() and d["son_basarili"] and d["gecmis"][0]["sonuc"] == "tamam"
    # özet damgayı okur ve atlanan kaynağı karar olarak sorar (otomatik KAYIP işaretlenmez)
    d2, _ = ozet(k, "--hizli")
    assert any("c/d" in x and "KAYIP olarak işaretlensin mi" in x for x in d2["karar_bekleyen"])
    assert json.loads((k / "kaynaklar.json").read_text())["repolar"][1]["tip"] == "T1"


def t46_aylik_bekleyen_dal():
    k = zincir_kutuphane()
    once = sh(k, "rev-parse", "HEAD").stdout
    env = dict(ENV, GIT_COMMITTER_DATE=(datetime.now() - timedelta(days=50)).isoformat(), GIT_AUTHOR_DATE=(datetime.now() - timedelta(days=50)).isoformat())
    sh(k, "switch", "-q", "-c", "takip/2026-09")
    subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", "eski"], cwd=k, env=env, check=True)
    sh(k, "switch", "-q", "master")
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": {"sha": "c1"}})
    assert s == 0 and "SONUÇ: bekleyen-dal" in c and "Onay bekleyen dal: takip/2026-09 (50 gün" in c and "45 günden eski" in c, c
    assert "NEDEN: bekleyen dal: takip/2026-09" in c and "Yeni güncelleme dalı AÇILMAYACAK" in c
    assert sh(k, "branch", "--list", "guncelleme/*", "takip/*", "--format=%(refname:short)").stdout.split() == ["takip/2026-09"]
    assert sh(k, "rev-parse", "HEAD").stdout == once and sh(k, "branch", "--show-current").stdout.strip() == "master"
    assert "~ a/b:" in c and "Aylık özet —" in c  # salt okuma adımları sürdü
    assert not isaret(k, "kaynak-cek") and stamp(k)["sonuc"] == "bekleyen-dal" and stamp(k)["dal"] is None
    d, _ = ozet(k, "--hizli")
    assert d["durum"] == "dikkat" and any("takip/2026-09" in x for x in d["karar_bekleyen"]) and "bekleyen-dal" in "\n".join(d["satirlar"])


def t47_aylik_kirli_agac():
    k = zincir_kutuphane()
    (k / "baska.txt").write_text("elle")
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": {"sha": "c1"}})
    assert s == 0 and "SONUÇ: kismi" in c and "kirli ağaç (1 dosya): baska.txt" in c and "Atlandı: ön kontrol engeli" in c
    assert sh(k, "branch", "--list", "guncelleme/*", "takip/*").stdout.strip() == ""
    assert (k / "baska.txt").read_text() == "elle" and not isaret(k, "kaynak-cek")
    assert stamp(k)["sonuc"] == "kismi" and "baska.txt" in stamp(k)["neden"]
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": {"sha": "c1"}}, siki=True)
    assert s == 2
    # yalnız rapor dosyası değişikse: kaydetme/geri alma yönergesi
    (k / "baska.txt").unlink()
    (k / "notlar" / "proje-durumu.md").write_text("x")
    sh(k, "add", "-A")
    sh(k, "commit", "-qm", "r")
    (k / "notlar" / "proje-durumu.md").write_text("y")
    s, c, _ = zincir(k, {"a/b": {"sha": "c1"}, "c/d": {"sha": "c1"}})
    assert "yalnız rapor dosyaları değişmiş (notlar/proje-durumu.md)" in c and "SONUÇ: kismi" in c


def t48_aylik_cevrimdisi():
    k = zincir_kutuphane()
    once = sh(k, "rev-parse", "HEAD").stdout
    os.environ["GHMODE"] = "fail"
    try:
        s, c, _ = zincir(k, {})
    finally:
        os.environ["GHMODE"] = "ok"
    assert s == 0 and "SONUÇ: kismi" in c and "gh auth login" in c and "GitHub'a ulaşılamıyor" in c and "Kaynak karşılaştırması ATLANDI" in c
    assert "--github" not in (k / ".isaret" / "dogrula.arg").read_text()  # yerel kontrol yapıldı, ağ yok
    assert sh(k, "rev-parse", "HEAD").stdout == once and sh(k, "branch", "--list", "guncelleme/*", "takip/*").stdout.strip() == ""
    assert not isaret(k, "kaynak-cek") and "Aylık özet —" in c
    d = stamp(k)
    assert d["sonuc"] == "kismi" and "GitHub'a ulaşılamıyor" in d["neden"]
    m = yukle(k)
    import unittest.mock as um
    with um.patch.object(m.subprocess, "run", side_effect=subprocess.TimeoutExpired("gh", 30)):
        assert m.gh_hazir() == (False, None, "zaman aşımı")  # takılmaz


def t49_aylik_hata_damgasi():
    k = zincir_kutuphane()
    once = sh(k, "rev-parse", "HEAD").stdout
    cfg(k, "arsiv-yerlestir", kod=1)
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": {"sha": "c1"}})
    assert s == 1 and "SONUÇ: basarisiz" in c and "NEDEN:" in c, c
    assert sh(k, "branch", "--list", "guncelleme/*").stdout.strip() == "" and sh(k, "rev-parse", "HEAD").stdout == once
    assert sh(k, "branch", "--show-current").stdout.strip() == "master" and sh(k, "status", "--porcelain").stdout == ""
    assert not (k / ".guncelleme-kilidi").exists()
    d = stamp(k)
    assert d["sonuc"] == "basarisiz" and d["neden"] and d["dal"] is None and d["son_basarili"] is None
    assert "Aylık özet —" in c  # güncelleme düşse de özet ve damga çalıştı
    # beklenmeyen istisna da damgalanır
    k2 = zincir_kutuphane()
    m = yukle(k2)
    m.rapor = lambda: (_ for _ in ()).throw(RuntimeError("patladı"))
    s, c = cikti(m.aylik, False)
    assert s == 1 and "beklenmeyen hata: RuntimeError" in c and stamp(k2)["sonuc"] == "basarisiz"


def t50_aylik_takip():
    k = zincir_kutuphane()
    once = sh(k, "rev-parse", "HEAD").stdout
    # değişiklik yok, takip taraması yeni dosya üretir -> takip dalı
    cfg(k, "konu-takip", yaz="notlar/konu-takip.md")
    s, c, _ = zincir(k, {"a/b": {"sha": "c1"}, "c/d": {"sha": "c1"}})
    assert s == 0 and "SONUÇ: tamam" in c and re.search(r"^DAL: takip/\S+$", c, re.M), c
    dal = re.search(r"^DAL: (takip/\S+)$", c, re.M).group(1)
    assert sh(k, "rev-parse", "HEAD").stdout == once and sh(k, "branch", "--show-current").stdout.strip() == "master"
    assert "konu-takip.md" in sh(k, "show", "--stat", dal).stdout and stamp(k)["dal"] == dal
    # takip dalı yeni bir koşuyu engeller
    s, c, _ = zincir(k, {"a/b": {"sha": "c2"}, "c/d": {"sha": "c1"}})
    assert "SONUÇ: bekleyen-dal" in c
    # değişiklik hiç yok -> boş dal silinir
    k = zincir_kutuphane()
    s, c, _ = zincir(k, {"a/b": {"sha": "c1"}, "c/d": {"sha": "c1"}})
    assert s == 0 and "SONUÇ: tamam" in c and "DAL:" not in c and sh(k, "branch", "--list", "takip/*").stdout.strip() == ""
    assert stamp(k)["dal"] is None
    # üç tarama da düşerse geri al, kısmi
    k = zincir_kutuphane()
    for ad in ("github-trend", "populer-tarama", "konu-takip"):
        cfg(k, ad, kod=1)
    s, c, _ = zincir(k, {"a/b": {"sha": "c1"}, "c/d": {"sha": "c1"}})
    assert "SONUÇ: kismi" in c and "taramalar yapılamadı" in c and sh(k, "branch", "--list", "takip/*").stdout.strip() == ""
    assert sh(k, "branch", "--show-current").stdout.strip() == "master"


def t51_damga_yaz_ve_sinirlar():
    k = zincir_kutuphane()
    m = yukle(k)
    try:
        m.damga_yaz("durduruldu")
        assert False
    except ValueError:
        pass
    for i in range(14):
        assert m.damga_yaz("kismi" if i % 2 else "tamam", dal=f"d{i}", neden="n", atlanan=["z/y", "a/b", "z/y"])
    d = stamp(k)
    assert len(d["gecmis"]) == 12 and d["gecmis"][0]["dal"] == "d13" and d["atlanan_kaynaklar"] == ["a/b", "z/y"]
    assert d["sonuc"] == "kismi" and d["son_basarili"]  # kismi son_basarili'yi silmez
    m.damga_ozet_durumu("dikkat")
    assert stamp(k)["ozet_durumu"] == "dikkat" and len(stamp(k)["gecmis"]) == 12
    # .gitignore'da değilse yazmaz
    (k / "notlar" / "son-aylik-calisma.json").unlink()
    (k / ".gitignore").write_text(".isaret/\n")
    c, g = cikti(m.damga_yaz, "tamam")
    assert c is False and "gitignore'da değil" in g and not (k / "notlar" / "son-aylik-calisma.json").exists()


def t52_damga_ozeti_yeni_biciim():
    k = kutuphane()
    damga(k, tarih=gun_once(40) + "T10:00:00+03:00", sonuc="tamam", dal=None, neden="", atlanan_kaynaklar=[])
    d, _ = ozet(k, "--hizli")
    soru = [c for c in d["karar_bekleyen"] if "Aylık çalışmayı şimdi" in c]
    assert soru and "40 gün önce" in "\n".join(d["satirlar"]) and "arsiv-guncelle.py --aylik" in soru[0]
    damga(k, tarih=gun_once(3) + "T10:00:00+03:00", sonuc="bekleyen-dal", neden="bekleyen dal: takip/2026-10 (3 gün)")
    d, _ = ozet(k, "--hizli")
    assert d["durum"] == "dikkat" and "yarım kaldı: bekleyen-dal — bekleyen dal: takip/2026-10" in _tum_md(k)
    damga(k, tarih=gun_once(3) + "T10:00:00+03:00", sonuc="tamam")
    d, _ = ozet(k, "--hizli")
    assert not any("şimdi yapayım" in c for c in d["karar_bekleyen"]) and "3 gün önce" in metin(d)
    # 45 günü aşan bekleyen dal çağrılır
    env = dict(ENV, GIT_COMMITTER_DATE=(datetime.now() - timedelta(days=60)).isoformat(), GIT_AUTHOR_DATE=(datetime.now() - timedelta(days=60)).isoformat())
    sh(k, "switch", "-q", "-c", "guncelleme/2026-08")
    subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", "eski"], cwd=k, env=env, check=True)
    sh(k, "switch", "-q", "master")
    d, _ = ozet(k, "--hizli")
    assert d["durum"] == "dikkat" and "guncelleme/2026-08 45 günden eski" in _tum_md(k)


def t53_zamanlanmis_gorev_karsilastirma():
    k = kutuphane()
    (k / "zamanlanmis").mkdir()
    (k / "zamanlanmis" / "aylik-guncelleme.SKILL.md").write_text("metin")
    canli = TMP / "canli53.md"
    canli.write_text("metin")
    md = lambda: (k / "notlar" / "aylik-ozet.md").read_text(encoding="utf-8")
    d, _ = ozet(k, "--gorev-yolu", str(canli))
    assert "| zamanlanmis-gorev | temiz |" in md() and "Zamanlanmış görev metni güncellensin mi?" not in d["karar_bekleyen"]
    canli.write_text("başka")
    d, _ = ozet(k, "--gorev-yolu", str(canli))
    assert "| zamanlanmis-gorev | dikkat |" in md() and "Zamanlanmış görev metni güncellensin mi?" in d["karar_bekleyen"]
    d, _ = ozet(k, "--gorev-yolu", str(TMP / "yok53.md"))
    assert "| zamanlanmis-gorev | dikkat |" in md() and "bulunamadı" in md()
    # gerçek kütüphane kopyası var, düzgün biçimde
    kopya = (GERCEK / "zamanlanmis" / "aylik-guncelleme.SKILL.md").read_text(encoding="utf-8")
    assert kopya.startswith("---\nname: skill-kutuphanesi-aylik-guncelleme\ndescription:") and "arsiv-guncelle.py --aylik" in kopya
    assert "--birlestir" in kopya and "push" in kopya and "--uygula" not in kopya.split("Adımlar:")[1]


def t54_zincir_birlestirmez_gondermez():
    import inspect
    src = "".join(inspect.getsource(f) for f in (_oku_modul().aylik_calistir, _oku_modul().takip, _oku_modul()._dal_geri_al, _oku_modul()._ozet_sonrasi_temizlik))
    for yasak in ('"push"', '"merge"', '"--birlestir"', "birlestir(", '"gh", "pr"'):
        assert yasak not in src, yasak
    assert src.count('"branch", "-D"') == 2  # yalnız takip()'in kendi açtığı dal: boş kalınca ve hata geri almasında


def _oku_modul():
    spec = importlib.util.spec_from_file_location("ag_inspect", GUNCELLE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def t55_belgeler_aylik():
    r = (GERCEK / "rehber" / "02-guncelleme-yonergesi.md").read_text(encoding="utf-8")
    p = (GERCEK / "promptlar" / "08-aylik-guncelleme-onayi.md").read_text(encoding="utf-8")
    z = (GERCEK / "zamanlanmis" / "aylik-guncelleme.SKILL.md").read_text(encoding="utf-8")
    for dosya, t in (("rehber/02", r), ("promptlar/08", p), ("zamanlanmis", z)):
        for k in ("--aylik", "--birlestir", "bekleyen"):
            assert k in t, (dosya, k)
    for k in ("son-aylik-calisma.json", "kismi", "bekleyen-dal", "tamam", "basarisiz", "gh auth login"):
        assert k in r, k
    assert "--aylik --kuru" in r


TESTLER = [(n, f) for n, f in sorted(globals().items()) if n.startswith("t") and n[1:3].isdigit() and callable(f)]


def main():
    gecen = 0
    for ad, f in TESTLER:
        try:
            f()
            gecen += 1
        except Exception:  # noqa: BLE001
            print(f"BAŞARISIZ {ad}:\n{traceback.format_exc()}")
    print(f"{gecen}/{len(TESTLER)} test geçti")
    return 0 if gecen == len(TESTLER) else 1


if __name__ == "__main__":
    sys.exit(main())
