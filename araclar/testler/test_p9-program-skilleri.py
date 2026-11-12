#!/usr/bin/env python3
"""P9 testleri (A serisi): skill-ekle.py --program-skill (programla gelen skile BAĞ) ve --dondur (projenin kendi donmuş kopyası).
Yalnız geçici klasör ve sahte veri: HOME geçici klasöre alınır; sahte program klasörü, sahte genel skill klasörü ve sahte programlar.json
kullanılır; gerçek ~/.claude, ~/.openmontage, gerçek programlar.json ve gerçek projeler okunmaz/yazılmaz. Sahte program ve genel klasörlerin
içeriği HER işlemden sonra aynı kalmalı (karma karşılaştırması). Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
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
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
TMP = Path(tempfile.mkdtemp(prefix="p9test-"))
GERCEK_HOME = os.environ.get("HOME")
os.environ["HOME"] = str(TMP / "home")        # modül içi Path.home() geçici klasöre baksın
(TMP / "home").mkdir()
SONUC = []
ESKI_KOMIT = "2956d5701"                      # P9 öncesi skill-ekle.py (git show; salt okur)


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-900:]}"))


def modul_yukle(ad, yol):
    spec = importlib.util.spec_from_file_location(ad, yol)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


se = modul_yukle("se_p9", ARACLAR / "skill-ekle.py")
sayac = [0]
PROG = TMP / "program" / "skills"             # sahte program skill klasörü (kartta skill_koku)
PROG2 = TMP / "home" / "prog2" / "skills"     # ev altında: kartta '~/prog2/skills'
GENEL = TMP / "home" / ".claude" / "skills"   # sahte "makine geneli" klasör
SAHTE_KAYIT = []


def fm(ad):
    return f"---\nname: {ad}\ndescription: test skill\n---\n"


def kayit(ad, **ek):
    sayac[0] += 1
    d = TMP / "arsiv" / f"{sayac[0]}-{ad}"
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(fm(ad) + "x\n", encoding="utf-8")
    s = {"id": ad, "ad": ad, "klasor_adi": ad, "kaynak_yol": f"skills/{ad}", "repo": "o/r", "yol": str(d),
         "klasor_hash": f"h{sayac[0]}", "commit": "c1", "kategori": "test/x", "durum": "tercih", "aciklama": "test skill",
         "teknoloji_oto": ["react"], "uyum": {"codex": "uyumlu"}, "degerlendirme": {"puan": 1, "not": "-"},
         "lisans": "MIT", "skill_md_kb": 1, "varyantlar": None}
    s.update(ek)
    return s


sahte_kayit_yap = kayit                       # 'kayit' adı sonraki bölümlerde başka değere bağlanır


def uygula(alan, ad, icerik="x\n"):
    d = alan / ad
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(fm(ad) + icerik, encoding="utf-8")
    return d


for n in ("alfa", "beta", "gama"):
    SAHTE_KAYIT.append(kayit(n))
se.canli_global = lambda s: {}
se.hesap_skilleri = lambda: {}
se.guncelleme_suruyor = lambda: None
se.registry = lambda: SAHTE_KAYIT
se.ARAC_JSON = TMP / "yok-araclar.json"

# ------------------------------------------------------------------ sahte program, sahte genel klasör, sahte kartlar
for n in ("ffmpeg", "video_toolkit", "hyperframes-x", "Alfa", "HFX"):
    uygula(PROG, n)
(PROG / "ffmpeg" / "ref").mkdir()
(PROG / "ffmpeg" / "ref" / "ek.md").write_text("ek\n", encoding="utf-8")
(PROG / "bos-klasor").mkdir()
uygula(PROG2, "hfx")
uygula(GENEL, "eski-skill", "eski\n")
(GENEL / "eski-skill" / "ek.txt").write_text("ek\n", encoding="utf-8")
(GENEL / "eski-skill" / ".DS_Store").write_text("x", encoding="utf-8")
os.symlink(str(PROG / "ffmpeg"), GENEL / "takma")                      # program skiline giden bağ
GIZLI_ISARET = "COK-GIZLI-ISARET-9f3a"
for ad, dosya in (("g-env", ".env"), ("g-auth", "Auth.JSON"), ("g-envl", ".env.local"), ("g-pem", "anahtar.PEM"), ("g-npmrc", ".npmrc"),
                  ("g-idrsa", "id_rsa"), ("g-cred", "credentials")):
    d = uygula(GENEL, ad)
    (d / dosya).write_text(GIZLI_ISARET, encoding="utf-8")
d = uygula(GENEL, "g-ssh")
(d / ".ssh").mkdir()
(d / ".ssh" / "k").write_text("x", encoding="utf-8")
d = uygula(GENEL, "b-dis")
os.symlink("/etc/hosts", d / "dis.txt")                                  # klasör dışına giden bağ
d = uygula(GENEL, "b-kirik")
os.symlink("yok-boyle-dosya", d / "kirik.txt")
d = uygula(GENEL, "b-ic")
(d / "asil.md").write_text("asil\n", encoding="utf-8")
os.symlink("asil.md", d / "ic.md")                                       # kaynak içinde çözülen dosya bağı: gerçek dosya olur
d = uygula(GENEL, "b-klasor")
(d / "alt").mkdir()
(d / "alt" / "a.md").write_text("a\n", encoding="utf-8")
os.symlink("alt", d / "alt-bag")                                         # klasör bağı: reddedilir
d = uygula(GENEL, "b-dongu")
os.symlink(".", d / "dongu")                                             # kendini gösteren klasör bağı: sonsuz döngü olmamalı
d = uygula(GENEL, "b-fifo")
os.mkfifo(d / "boru")
d = uygula(GENEL, "b-dev")
with open(d / "buyuk.bin", "wb") as f:
    f.truncate(201 * 1024 * 1024)                                        # seyrek (sparse) 201 MB
d = uygula(GENEL, "b-orta")
with open(d / "orta.bin", "wb") as f:
    f.truncate(51 * 1024 * 1024)                                         # 50 MB üstü: yalnız UYARI
d = uygula(GENEL, "b-ad")
(d / "SKILL.md").write_text("---\nname: baska-ad\ndescription: x\n---\n", encoding="utf-8")
d = uygula(GENEL, "b-atla")
(d / "node_modules").mkdir()
(d / "node_modules" / "m.js").write_text("m", encoding="utf-8")
(d / "__pycache__").mkdir()
(d / "__pycache__" / "m.pyc").write_text("m", encoding="utf-8")
(GENEL / "b-skillsiz").mkdir()
(GENEL / "b-skillsiz" / "x.md").write_text("x", encoding="utf-8")

KART = TMP / "programlar.json"
KART_ICERIK = {"surum": 2, "programlar": {
    "fakeprog": {"ad": "Sahte", "yerinde": {"tur": "git-checkout", "yol": str(TMP / "program")}, "kutuphane_commit": "abc1234def5678",
                 "skill_koku": str(PROG)},
    "hfaketest": {"ad": "Sahte2", "yerinde": {"tur": "npm-global", "yol": "x"}, "kutuphane_surumu": "1.0.0", "skill_koku": "~/prog2/skills"},
    "bossprog": {"ad": "Bos", "skill_koku": ""},
    "goreliprog": {"ad": "Goreli", "skill_koku": "goreli/yol"},
    "eksikprog": {"ad": "Eksik", "skill_koku": str(TMP / "yok-program" / "skills")},
}}
KART.write_text(json.dumps(KART_ICERIK), encoding="utf-8")
se.PROGRAMLAR = KART


def agac(d: Path):
    s = {}
    for p in sorted(d.rglob("*")):
        rel = str(p.relative_to(d))
        s[rel] = ("symlink->" + str(p.readlink())) if p.is_symlink() else ("fifo" if p.is_fifo() else
                  (p.stat().st_size if (p.is_file() and p.stat().st_size > 1_000_000) else p.read_bytes()) if p.is_file() else "dir")
    return s


def koruma_ozeti():
    return (agac(TMP / "program"), agac(TMP / "home" / ".claude"), agac(TMP / "home" / "prog2"))


KORUMA = koruma_ozeti()


def degismedi():
    return koruma_ozeti() == KORUMA


def calistir(*args, mod=None):
    """modül main()'ini süreç içinde çalıştırır: (çıkış kodu, stdout+stderr)"""
    mod = mod or se
    eski, eski_in = sys.argv, sys.stdin
    sys.argv = ["skill-ekle.py"] + [str(a) for a in args]
    sys.stdin = io.StringIO("")                 # etkileşimsiz: onay sorusu açılmasın
    out, err = io.StringIO(), io.StringIO()
    kod = 0
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                kod = mod.main() or 0
            except SystemExit as e:
                kod = e.code if isinstance(e.code, int) else (0 if e.code is None else 2)
                if isinstance(e.code, str):
                    print(e.code)
    finally:
        sys.argv, sys.stdin = eski, eski_in
    return kod, out.getvalue() + err.getvalue()


def yeni_proje(ad=None):
    if ad:
        d = TMP / "projeler" / ad
        d.mkdir(parents=True)
        return d
    return Path(tempfile.mkdtemp(dir=TMP, prefix="proje-"))


def kilit_oku(p):
    return json.loads((p / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))


def kilit_yaz(p, k):
    (p / ".skill-kutuphanesi" / "kilit.json").write_text(json.dumps(k, ensure_ascii=False, indent=2), encoding="utf-8")


def blok(p, dosya="CLAUDE.md"):
    f = p / dosya
    return f.read_text(encoding="utf-8") if f.exists() else ""


def kurulu(*args, arac=None):
    """yeni projede çalıştırır: (proje, kod, çıktı)"""
    p = yeni_proje()
    ek = ["--arac", arac] if arac else []
    k, o = calistir(p, *args, *ek, "--evet")
    return p, k, o


try:
    # ================================================================== A. bağ: kuru, kurulum, yerleşim, kilit
    print("A. bağ")
    p = yeni_proje()
    once = agac(p)
    k, o = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--kuru")
    test("1. --kuru: çıkış 2, [kuru], proje ağacı değişmez, üç BİLGİ satırı ve bağ özeti var",
         k == 2 and "[kuru]" in o and agac(p) == once and "bag-makineye-ozel" in o and "bag-programla-guncel" in o
         and "Programla gelen (bağ): 1" in o and "fakeprog:ffmpeg" in o and "abc1234d" in o and degismedi(), o)
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg", "--arac", "ortak")
    h, c = p / ".agents" / "skills" / "ffmpeg", p / ".claude" / "skills" / "ffmpeg"
    kl = kilit_oku(p)
    g = kl.get("dis_skiller", {}).get("ffmpeg", {})
    test("2. ortak kurulum: .agents/skills/x mutlak bağ, .claude/skills/x göreli bağ, SKILL.md görünür, kilit tam alanlar, çıkış 0, --dogrula temiz",
         k == 0 and h.is_symlink() and os.readlink(h) == str(PROG / "ffmpeg") and c.is_symlink()
         and os.readlink(c) == "../../.agents/skills/ffmpeg" and (c / "SKILL.md").exists()
         and set(g) == {"ad", "tur", "program", "hedef", "tarih", "program_surum", "program_surum_turu"}
         and g["tur"] == "program-bag" and g["program"] == "fakeprog" and g["hedef"] == str(PROG / "ffmpeg")
         and g["program_surum"] == "abc1234def5678" and g["program_surum_turu"] == "commit"
         and kl["skiller"] == {} and calistir(p, "--dogrula")[0] == 0 and degismedi(), o)
    p2, k2, o2 = kurulu("--program-skill", "hfaketest:hfx")
    g2 = kilit_oku(p2)["dis_skiller"]["hfx"]
    b2 = blok(p2)
    test("3. ikinci kart (npm-global, ~ yolu): sürüm 'surum', blok ~ ile kısaltılmış yolu yazar, ev adı yok; CLAUDE.md ve AGENTS.md bloğu aynı",
         k2 == 0 and g2["program_surum"] == "1.0.0" and g2["program_surum_turu"] == "surum" and g2["hedef"] == str(PROG2 / "hfx")
         and "Programla gelen skiller" in b2 and "~/prog2/skills/hfx" in b2 and str(TMP / "home") not in b2
         and "Bağlı skillerin dosyalarını düzenleme" in b2 and "| Skill |" not in b2 and "Profil:" not in b2
         and blok(p2, "AGENTS.md") == b2, b2)
    p3, k3, o3 = kurulu("--program-skill", "fakeprog:ffmpeg", arac="yalniz-claude")
    c3, h3 = p3 / ".claude" / "skills" / "ffmpeg", p3 / ".agents"
    test("4. yalniz-claude: yalnız .claude/skills/x mutlak bağ; .agents yok; AGENTS.md yok; blok CLAUDE.md'de",
         k3 == 0 and c3.is_symlink() and os.readlink(c3) == str(PROG / "ffmpeg") and not h3.exists() and not (p3 / "AGENTS.md").exists()
         and "Programla gelen skiller" in blok(p3) and calistir(p3, "--dogrula")[0] == 0, o3)

    # ================================================================== B. hata kodları (hiçbir şey yazılmaz, --zorla geçmez)
    print("B. hata kodları")
    p = yeni_proje()
    once = agac(p)
    vaka = [("nope:ffmpeg", "program-bilinmiyor"), ("bossprog:x", "program-skillsiz"), ("goreliprog:x", "program-skillsiz"),
            ("eksikprog:x", "program-kurulu-degil"), ("fakeprog:yok-boyle", "program-skill-yok"), ("fakeprog:bos-klasor", "program-skill-yok"),
            ("foo", "program-skill-bicim"), (":x", "program-skill-bicim"), ("fakeprog:", "program-skill-bicim"),
            ("fakeprog:../x", "program-skill-ad"), ("fakeprog:a/b", "program-skill-ad"), ("fakeprog:.x", "program-skill-ad"),
            ("fakeprog:" + "x" * 70, "program-skill-ad"), ("fakeprog:ffmpeg\n", "program-skill-ad"), ("fakeprog:x.kurulum-tmp", "program-skill-ad"),
            ("fakeprog:*", "program-skill-ad"), ("fakeprog:a..b", "program-skill-yok")]
    bos = []
    for istek, kod in vaka:
        k, o = calistir(p, "--program-skill", istek, "--kuru")
        k_z, o_z = calistir(p, "--program-skill", istek, "--zorla", "--evet")
        if not (k == 2 and f"[HATA] {kod}" in o and agac(p) == once and k_z == 2 and "--zorla ile de geçilemez" in o_z):
            bos.append((istek, kod, k, o[-300:]))
    test("5. program-skill hata kodları: bilinmeyen/skillsiz/göreli/kurulu değil/yok/biçim/ad (../ a/b .x 70 karakter satır sonu .kurulum-tmp *); "
         "hiçbiri yazmaz, --zorla geçmez", not bos and degismedi(), bos)
    k, o = calistir(p, "--program-skill", "fakeprog:yok-boyle", "--kuru")
    test("5b. program-skill-yok iletisi programdaki skill adlarını sayar; video_toolkit (alt çizgi) kabul edilir",
         "ffmpeg" in o and "video_toolkit" in o and calistir(p, "--program-skill", "fakeprog:video_toolkit", "--kuru")[1].count("[HATA]") == 0)
    k, o = calistir(p, "--program-skill", "fakeprog:ffmpeg", "fakeprog:FFMPEG", "--kuru")
    test("5c. aynı çalışmada aynı ad iki kez (harf boyutu farklı): dis-ad-cakismasi", k == 2 and "dis-ad-cakismasi" in o)

    # ================================================================== C. karışık çalışma, çakışma, tekrar
    print("C. karışık çalışma, çakışma, tekrar")
    p = yeni_proje()
    k, o = calistir(p, "--skill", "alfa", "--rol-adi", "r1", "--program-skill", "fakeprog:ffmpeg", "--evet")
    kl = kilit_oku(p)
    d_o = calistir(p, "--durum")[1]
    toml = (p / ".codex" / "agents" / "r1.toml").read_text(encoding="utf-8") if (p / ".codex" / "agents" / "r1.toml").exists() else ""
    md = (p / ".claude" / "agents" / "r1.md").read_text(encoding="utf-8")
    test("6. kütüphane + bağ aynı çalışmada: iki tür ayrı anahtarda; --durum iki satır; rol dosyaları bağı anmaz; blok ikisini de yazar",
         k == 0 and "alfa" in kl["skiller"] and "ffmpeg" in kl["dis_skiller"] and "ffmpeg" not in kl["skiller"]
         and re.search(r"alfa\s+r1\s+güncel", d_o) and re.search(r"ffmpeg\s+bağ: fakeprog\s+programla güncel \(bağ\)", d_o)
         and "ffmpeg" not in toml and "ffmpeg" not in md and "| `alfa` |" in blok(p) and "`ffmpeg` (fakeprog," in blok(p), d_o + toml)
    # çakışmalar
    p = yeni_proje()
    k, o = calistir(p, "--skill", "alfa", "--program-skill", "fakeprog:Alfa", "--kuru")
    a1 = k == 2 and "dis-ad-cakismasi" in o
    calistir(p, "--skill", "alfa", "--evet")
    k, o = calistir(p, "--program-skill", "fakeprog:Alfa", "--evet")
    a2 = k == 2 and "dis-ad-cakismasi" in o
    k, o = calistir(p, "--dondur", str(uygula(GENEL, "alfa")), "--kuru")
    a4 = k == 2 and "dondur-kutuphane-adi" in o
    shutil.rmtree(GENEL / "alfa")
    p5 = yeni_proje()
    calistir(p5, "--program-skill", "hfaketest:hfx", "--evet")
    k, o = calistir(p5, "--program-skill", "fakeprog:HFX", "--evet")
    a5 = k == 2 and "dis-ad-cakismasi" in o
    uygula(GENEL, "hfx")
    k, o = calistir(p5, "--dondur", GENEL / "hfx", "--evet")
    a6 = k == 2 and "dis-ad-cakismasi" in o
    shutil.rmtree(GENEL / "hfx")
    k, o = calistir(p5, "--dondur", GENEL / "eski-skill", GENEL / "eski-skill", "--kuru")
    a7 = k == 2 and "dis-ad-cakismasi" in o
    test("7. ad çakışmaları: kütüphane+bağ, kurulu kütüphane+bağ (harf boyutu), donmuş=kurulu kütüphane adı, bağ+donmuş, bağ HFX/hfx, aynı ad iki kez",
         a1 and a2 and a4 and a5 and a6 and a7, (a1, a2, a4, a5, a6, a7))
    # sonradan, dış-bayraksız çalışmada aynı adlı kütüphane skili: bağın üzerine yazılmaz, --zorla geçmez
    p = yeni_proje()
    SAHTE_KAYIT.append(kayit("ffmpeg"))
    try:
        calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
        once = agac(p)
        k, o = calistir(p, "--skill", "ffmpeg", "--evet")
        k_z, o_z = calistir(p, "--skill", "ffmpeg", "--zorla", "--evet")
        test("8. önce bağ, sonra AYRI çalışmada aynı adlı --skill: dis-ad-cakismasi, --zorla ile de geçmez, bağ ve kilit aynen kalır",
             k == 2 and "dis-ad-cakismasi" in o and k_z == 2 and "geçilemez" in o_z and agac(p) == once and "ffmpeg" not in kilit_oku(p)["skiller"]
             and degismedi(), o + o_z)
    finally:
        SAHTE_KAYIT.pop()
    # tekrar çalışma (idempotent) ve değişen hedef
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg")
    k1 = kilit_oku(p)
    k, o = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
    k2 = kilit_oku(p)
    kart_yeni = json.loads(json.dumps(KART_ICERIK))
    kart_yeni["programlar"]["fakeprog"]["skill_koku"] = str(PROG2)
    uygula(PROG2, "ffmpeg")
    KART.write_text(json.dumps(kart_yeni), encoding="utf-8")
    k_f, o_f = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
    KART.write_text(json.dumps(KART_ICERIK), encoding="utf-8")
    shutil.rmtree(PROG2 / "ffmpeg")
    test("9. ikinci aynı çalışma: bag-var, çıkış 0, dis_skiller aynı (tarih dahil); hedef değişince bag-farkli (ZORLANAMAZ)",
         k == 0 and "bag-var" in o and k1["dis_skiller"] == k2["dis_skiller"] and k_f == 2 and "bag-farkli" in o_f and "geçilemez" in o_f, o + o_f)
    # Windows
    eski_win = se.windows_mu
    se.windows_mu = lambda: True
    try:
        p = yeni_proje()
        once = agac(p)
        kw1, ow1 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
        kw2, ow2 = calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
        kw3, ow3 = calistir(p, "--skill", "alfa", "--evet")
    finally:
        se.windows_mu = eski_win
    test("10. Windows: --program-skill ve --dondur açık iletiyle durur ve hiçbir şey yazmaz; ek bayraksız çıkış iletisi eskisi gibi",
         kw1 != 0 and kw2 != 0 and "Windows'a bağlanamaz" in ow1 and "Windows'a bağlanamaz" in ow2 and agac(p) == once
         and "Windows'ta çalıştırılmaz" in ow3)

    # ================================================================== D. dondurma
    print("D. dondurma")
    p = yeni_proje()
    k, o = calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    kl = kilit_oku(p)
    g = kl.get("dis_skiller", {}).get("eski-skill", {})
    h, c = p / ".agents" / "skills" / "eski-skill", p / ".claude" / "skills" / "eski-skill"
    d_o = calistir(p, "--durum")[1]
    test("11. --dondur gerçek klasör: gerçek klasör (bağ değil), içerik aynı, .DS_Store yok, .claude göreli bağ, kilit tur=donmus + icerik_hash + dosya_sayisi, "
         "--durum donmuş satırı, kaynak değişmedi",
         k == 0 and h.is_dir() and not h.is_symlink() and (h / "ek.txt").read_text() == "ek\n" and not (h / ".DS_Store").exists()
         and c.is_symlink() and os.readlink(c) == "../../.agents/skills/eski-skill"
         and set(g) == {"ad", "tur", "hedef", "tarih", "icerik_hash", "dosya_sayisi"} and g["tur"] == "donmus" and g["dosya_sayisi"] == 2
         and g["hedef"] == str(GENEL / "eski-skill") and re.search(r"eski-skill\s+donmuş\s+donmuş \(kütüphane güncellemez\)", d_o)
         and not any(x.is_symlink() for x in h.rglob("*")) and degismedi(), o + d_o)
    (h / "ek.txt").write_text("ben düzenledim\n", encoding="utf-8")
    kg, og = calistir(p, "--guncelle")
    kd, od = calistir(p, "--dogrula")
    test("12. donmuş dosyayı düzenle: --guncelle 'guncellenecek' demez, --dogrula 'elle değiştirilmiş' demez (çıkış 0)",
         kg == 0 and "guncellenecek" not in og and "Güncellenecek/onarılacak: 0" in og and kd == 0 and "elle" not in od, og + od)
    # reddedilenler
    p = yeni_proje()
    once = agac(p)
    ret = {"takma": "dondur-program-skili", "g-env": "dondur-gizli", "g-auth": "dondur-gizli", "g-envl": "dondur-gizli", "g-pem": "dondur-gizli",
           "g-npmrc": "dondur-gizli", "g-idrsa": "dondur-gizli", "g-cred": "dondur-gizli", "g-ssh": "dondur-gizli", "b-dis": "dondur-dis-baglanti",
           "b-kirik": "dondur-dis-baglanti", "b-klasor": "dondur-dis-baglanti", "b-dongu": "dondur-dis-baglanti", "b-fifo": "dondur-ozel-dosya",
           "b-dev": "dondur-cok-buyuk", "b-skillsiz": "dondur-kaynak-yok"}
    bos = []
    for ad, kod in ret.items():
        k, o = calistir(p, "--dondur", GENEL / ad, "--kuru")
        k_z, o_z = calistir(p, "--dondur", GENEL / ad, "--zorla", "--evet")
        if not (k == 2 and f"[HATA] {kod}" in o and agac(p) == once and k_z == 2 and "--zorla ile de geçilemez" in o_z):
            bos.append((ad, kod, k, o[-300:]))
    test("13. dondurma reddi: program skiline bağ, gizli adlar (.env Auth.JSON .env.local .pem .npmrc id_rsa credentials .ssh), kaynak dışı/kırık/klasör/döngü "
         "bağı, FIFO, 201 MB, SKILL.md yok; hiçbiri yazmaz ve --zorla geçmez", not bos and degismedi(), bos)
    k, o = calistir(p, "--dondur", GENEL / "takma", "--kuru")
    k2, o2 = calistir(p, "--dondur", GENEL / "g-env", "--kuru")
    test("13b. iletiler: program skili --program-skill fakeprog:ffmpeg önerir; gizli dosyanın İÇERİĞİ hiçbir çıktıda yok (açılmadı)",
         "--program-skill fakeprog:ffmpeg" in o and GIZLI_ISARET not in o + o2 and "dosya açılmadı" in o2, o + o2)
    k, o = calistir(p, "--dondur", "goreli/yol", "--kuru")
    k_s, o_s = calistir(p, "--dondur", p / ".claude" / "skills" / "x", "--kuru")
    (p / ".claude" / "skills" / "kendi").mkdir(parents=True)
    (p / ".claude" / "skills" / "kendi" / "SKILL.md").write_text(fm("kendi"), encoding="utf-8")
    k_k, o_k = calistir(p, "--dondur", p / ".claude" / "skills" / "kendi", "--kuru")
    test("14. dondur-yol (göreli), dondur-kendisi (projenin kendi skill klasörü), dondur-ad (.x gibi adlar)",
         "dondur-yol" in o and "dondur-kendisi" in o_k and "dondur-ad" in calistir(p, "--dondur", GENEL / ".x", "--kuru")[1], o + o_k)
    # içeride çözülen dosya bağı gerçek dosya olur; atlananlar; UYARI'lar
    p = yeni_proje()
    k, o = calistir(p, "--dondur", GENEL / "b-ic", "--evet")
    ic = p / ".agents" / "skills" / "b-ic" / "ic.md"
    p_a = yeni_proje()
    k_a, o_a = calistir(p_a, "--dondur", GENEL / "b-atla", "--evet")
    p_b = yeni_proje()
    k_b, o_b = calistir(p_b, "--dondur", GENEL / "b-ad", "--kuru")
    k_b2, o_b2 = calistir(p_b, "--dondur", GENEL / "b-ad", "--evet")
    p_c = yeni_proje()
    k_c, o_c = calistir(p_c, "--dondur", GENEL / "b-orta", "--evet")
    test("15. dosya bağı kaynak içinde çözülüyorsa gerçek dosya olur; node_modules/__pycache__ kopyalanmaz (BİLGİ); ad farkı ve 50 MB üstü UYARI "
         "(--evet ister, verilince kurar)",
         k == 0 and ic.is_file() and not ic.is_symlink() and ic.read_text() == "asil\n"
         and k_a == 0 and not (p_a / ".agents" / "skills" / "b-atla" / "node_modules").exists() and "dondurma-atlanan" in o_a
         and k_b == 2 and "dondur-ad-farkli" in o_b and "UYARI" in o_b and k_b2 == 0
         and k_c == 0 and (p_c / ".agents" / "skills" / "b-orta" / "orta.bin").exists() and degismedi(), o + o_a + o_b + o_c)
    k_c3, o_c3 = calistir(yeni_proje(), "--dondur", GENEL / "b-orta", "--kuru")
    test("15b. 50 MB üstü: dondur-buyuk UYARI (HATA değil)", "[UYARI] dondur-buyuk" in o_c3 and "[HATA]" not in o_c3, o_c3)

    # ================================================================== E. dogrula / durum / kaldır / yenile
    print("E. dogrula, durum, kaldir, yenile")
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg", "fakeprog:video_toolkit")
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    kd, od = calistir(p, "--dogrula")
    gec = TMP / "program-gecici"
    os.rename(TMP / "program", gec)
    try:
        kd1, od1 = calistir(p, "--dogrula")
        ku1, ou1 = calistir(p, "--durum")
        kg, og = calistir(p, "--guncelle")
    finally:
        os.rename(gec, TMP / "program")
    test("16. --dogrula: sağlamda 0; program klasörü yok -> 'program bağı kırık' + 'program klasörü yok', çıkış 1; --durum BAĞ KIRIK; --guncelle UYARI bag-kirik",
         kd == 0 and kd1 == 1 and "program bağı kırık" in od1 and "program klasörü yok" in od1 and "BAĞ KIRIK" in ou1
         and "bag-kirik" in og and degismedi(), od + od1 + ou1 + og)
    ffh = p / ".agents" / "skills" / "ffmpeg"
    ffh.unlink()
    ffh.mkdir()
    (ffh / "SKILL.md").write_text("elle", encoding="utf-8")
    kg, og = calistir(p, "--dogrula")
    kd2, od2 = calistir(p, "--durum")
    shutil.rmtree(ffh)
    os.symlink(str(PROG / "ffmpeg"), ffh)
    shutil.rmtree(p / ".agents" / "skills" / "eski-skill")
    k3, o3 = calistir(p, "--dogrula")
    k4, o4 = calistir(p, "--durum")
    test("17. slot gerçek klasör: 'bağ yerine gerçek klasör'; donmuş klasör silinince 'donmuş skill klasörü yok' ve --durum DONMUŞ KLASÖR YOK; program klasörü dokunulmadı",
         kg == 1 and "bağ yerine gerçek klasör" in og and "KURULUM EKSİK/BOZUK" in od2 and k3 == 1 and "donmuş skill klasörü yok" in o3
         and "DONMUŞ KLASÖR YOK" in o4 and degismedi(), og + od2 + o3 + o4)
    # kaldır: bağ
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg", "fakeprog:video_toolkit")
    k, o = calistir(p, "--kaldir", "ffmpeg", "--evet")
    kl = kilit_oku(p)
    test("18. --kaldir bağ: iki slot gitti, kilitten çıktı, diğer bağ kaldı, blok güncel, program klasörü bayt bayt aynı",
         k == 0 and not (p / ".claude" / "skills" / "ffmpeg").is_symlink() and not (p / ".agents" / "skills" / "ffmpeg").is_symlink()
         and "ffmpeg" not in kl["dis_skiller"] and "video_toolkit" in kl["dis_skiller"] and "`ffmpeg`" not in blok(p)
         and "`video_toolkit`" in blok(p) and degismedi(), o)
    k, o = calistir(p, "--kaldir", "video_toolkit", "--evet")
    test("18b. son bağ kaldırılınca blok silinir (CLAUDE.md'de başka metin yoksa dosya da gider), kilitte dis_skiller anahtarı kalmaz",
         k == 0 and "dis_skiller" not in kilit_oku(p) and not (p / "CLAUDE.md").exists() and not (p / "AGENTS.md").exists())
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg")
    ff = p / ".claude" / "skills" / "ffmpeg"
    ff.unlink()
    ff.mkdir()
    (ff / "SKILL.md").write_text("kullanıcı verisi", encoding="utf-8")
    k1, o1 = calistir(p, "--kaldir", "ffmpeg", "--evet")
    k2, o2 = calistir(p, "--kaldir", "ffmpeg", "--zorla", "--evet")
    test("19. slot gerçek klasöre dönüşmüşse --kaldir bag-degismis ile durur, --zorla ile de geçmez, kullanıcı verisi silinmez",
         k1 == 2 and "bag-degismis" in o1 and k2 == 2 and "bag-degismis" in o2 and (ff / "SKILL.md").read_text() == "kullanıcı verisi" and degismedi(), o1 + o2)
    # kaldır: donmuş
    p = yeni_proje()
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    kk, ok_ = calistir(p, "--kaldir", "eski-skill", "--kuru")
    yedekler_once = calistir(p, "--yedekler")[1]
    k, o = calistir(p, "--kaldir", "eski-skill", "--evet")
    yed = sorted((p / ".skill-kutuphanesi" / "yedek").iterdir())[-1]
    yedek_ad = yed.name
    yedek_var = (yed / ".agents" / "skills" / "eski-skill" / "ek.txt").is_file()
    gone = not (p / ".agents" / "skills" / "eski-skill").exists() and "dis_skiller" not in kilit_oku(p)
    kg, og = calistir(p, "--geri-al", yedek_ad)
    kl = kilit_oku(p)
    test("20. --kaldir donmuş: önce yedekte kopya var, klasör gitti; dondurma-yedek bilgisi; --geri-al klasörü, bağı ve kilit kaydını geri getirir; --kuru yazmaz",
         kk == 2 and "dondurma-yedek" in ok_ and k == 0 and yedek_var and gone
         and (p / ".agents" / "skills" / "eski-skill" / "ek.txt").is_file() and (p / ".claude" / "skills" / "eski-skill").is_symlink()
         and "eski-skill" in kl.get("dis_skiller", {}) and degismedi(), ok_ + o + og)
    # donmuş + elle değiştirilmiş: kaldırma UYARI ister
    (p / ".agents" / "skills" / "eski-skill" / "ek.txt").write_text("degisti", encoding="utf-8")
    k1, o1 = calistir(p, "--kaldir", "eski-skill")
    k2, o2 = calistir(p, "--kaldir", "eski-skill", "--evet")
    test("20b. donmuş kopya sonradan değiştirilmişse --kaldir UYARI dondurma-degismis verir ve --evet ister",
         k1 == 2 and "dondurma-degismis" in o1 and k2 == 0, o1 + o2)
    # hepsi + bilinmeyen
    p, k, o = kurulu("--skill", "alfa", "--program-skill", "fakeprog:ffmpeg")
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    k, o = calistir(p, "--kaldir", "hepsi", "--evet")
    kl = kilit_oku(p)
    k_b, o_b = calistir(p, "--kaldir", "yok-boyle", "--kuru")
    k_c, o_c = calistir(p, "--kaldir", "../../x", "--zorla", "--evet")
    test("21. --kaldir hepsi yalnız kütüphane skillerini kaldırır (bağ ve donmuş kalır); bilinmeyen/geçersiz ad kutuphaneden-degil",
         k == 0 and kl["skiller"] == {} and set(kl["dis_skiller"]) == {"ffmpeg", "eski-skill"} and (p / ".claude" / "skills" / "ffmpeg").is_symlink()
         and k_b == 2 and "kutuphaneden-degil" in o_b and "programdan ya da dondurma" in o_b and "kutuphaneden-degil" in o_c, o_b + o_c)
    # yenile
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg", "hfaketest:hfx")
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    for ad in ("ffmpeg", "hfx"):
        (p / ".claude" / "skills" / ad).unlink()
    (p / ".agents" / "skills" / "hfx").unlink()
    shutil.rmtree(p / ".agents" / "skills" / "eski-skill")
    kk, ok_ = calistir(p, "--yenile", "--kuru")
    once = agac(p)
    os.rename(PROG2 / "hfx", PROG2 / "hfx-gec")
    try:
        k1, o1 = calistir(p, "--yenile")
    finally:
        os.rename(PROG2 / "hfx-gec", PROG2 / "hfx")
    test("22. --yenile: silinen bağ ve .claude bağı yeniden kurulur; hedefi olmayan bağ KURULMAZ ('hedef yok', asılı bağ yok); donmuş klasör yoksa 'donmuş klasör yok'; "
         "--kuru yazmaz", kk == 0 and "[kuru]" in ok_ and (p / ".agents" / "skills" / "ffmpeg").is_symlink()
         and (p / ".claude" / "skills" / "ffmpeg" / "SKILL.md").exists() and "hedef yok" in o1 and "donmuş klasör yok" in o1
         and not (p / ".agents" / "skills" / "hfx").exists() and not (p / ".agents" / "skills" / "hfx").is_symlink() and degismedi(), o1)
    k2, o2 = calistir(p, "--yenile")
    test("22b. program geri gelince --yenile hfx bağını da kurar", (p / ".claude" / "skills" / "hfx" / "SKILL.md").exists(), o2)

    # ================================================================== F. araç düzeni geçişi, guncelle, blok, geri uyum
    print("F. düzen geçişi, güncelle, blok, geri uyum")
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--program-skill", "fakeprog:ffmpeg", "--evet")
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    ino = os.stat(p / ".agents" / "skills" / "eski-skill").st_ino
    k1, o1 = calistir(p, "--arac", "yalniz-claude", "--evet")
    c = p / ".claude" / "skills"
    gecis1 = (k1 == 0 and not (p / ".agents").exists() and os.readlink(c / "ffmpeg") == str(PROG / "ffmpeg")
              and (c / "eski-skill").is_dir() and not (c / "eski-skill").is_symlink() and os.stat(c / "eski-skill").st_ino == ino
              and (c / "eski-skill" / "ek.txt").read_text() == "ek\n" and calistir(p, "--dogrula")[0] == 0)
    k2, o2 = calistir(p, "--arac", "ortak", "--evet")
    h = p / ".agents" / "skills"
    gecis2 = (k2 == 0 and h.joinpath("ffmpeg").is_symlink() and os.readlink(h / "ffmpeg") == str(PROG / "ffmpeg")
              and os.readlink(c / "ffmpeg") == "../../.agents/skills/ffmpeg" and (h / "eski-skill").is_dir() and not (h / "eski-skill").is_symlink()
              and os.stat(h / "eski-skill").st_ino == ino and os.readlink(c / "eski-skill") == "../../.agents/skills/eski-skill"
              and calistir(p, "--dogrula")[0] == 0)
    test("23. --arac yalniz-claude ve geri ortak: bağlar yeniden döşenir, donmuş gerçek klasör TAŞINIR (aynı inode, aynı içerik), her adımda --dogrula temiz, "
         "boş .agents kalmaz, program klasörü aynı", gecis1 and gecis2 and degismedi(), (gecis1, gecis2, o1, o2))
    # guncelle
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--program-skill", "fakeprog:ffmpeg", "--evet")
    calistir(p, "--dondur", GENEL / "eski-skill", "--evet")
    k, o = calistir(p, "--guncelle")
    os.rename(TMP / "program", gec)
    try:
        k_b, o_b = calistir(p, "--guncelle")
    finally:
        os.rename(gec, TMP / "program")
    test("24. --guncelle: dış skiller 'guncellenecek' olarak hiç anılmaz; dis-skiller bilgisi; kırık bağ UYARI bag-kirik (çıkış 0, güncellenecek 0)",
         k == 0 and "dis-skiller" in o and "1 skill programla güncel (bağ), 1 donmuş" in o and "guncellenecek" not in o
         and "bag-kirik" in o_b and "Güncellenecek/onarılacak: 0" in o_b, o + o_b)
    # blok kuralları
    p = yeni_proje()
    (p / "CLAUDE.md").write_text("# Benim notlarım\nöylesine\n", encoding="utf-8")
    calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
    b1 = blok(p)
    calistir(p, "--kaldir", "ffmpeg", "--evet")
    b2 = blok(p)
    test("25. blok: yalnız dış skilli projede blok var; son dış skill kalkınca blok silinir, blok dışı kullanıcı metni korunur",
         "# Benim notlarım" in b1 and "skill-kutuphanesi:basla" in b1 and "skill-kutuphanesi:basla" not in b2 and b2.strip() == "# Benim notlarım\nöylesine", b1 + b2)
    # kısa blok
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--blok", "kisa", "--program-skill", "fakeprog:ffmpeg", "--evet")
    bk = blok(p)
    test("25b. kısa blokta da dış skiller yazılır; --yenile bloğu aynen üretir", "1 skill" in bk and "`ffmpeg` (fakeprog," in bk and calistir(p, "--yenile")[0] == 0
         and blok(p) == bk, bk)
    # kilit_yaz: boş dis_skiller anahtarı eskisi gibi
    p = yeni_proje()
    se.kilit_yaz(p, se.kilit_oku(p))
    ilk = "dis_skiller" in kilit_oku(p)
    kl2 = se.kilit_oku(p)
    kl2["dis_skiller"] = {}
    se.kilit_yaz(p, kl2)
    bosalan = "dis_skiller" in kilit_oku(p)
    kl3 = se.kilit_oku(p)
    kl3["dis_skiller"] = {"x": {"ad": "x", "tur": "program-bag", "program": "fakeprog", "hedef": str(PROG / "x")}}
    se.kilit_yaz(p, kl3)
    kl4 = se.kilit_oku(p)
    se.kilit_yaz(p, kl4)
    test("26. kilit_yaz: hiç olmayan dis_skiller yazılmaz; boşalan anahtar silinir; dolu anahtar kilit_oku/kilit_yaz döngüsünden kaybolmaz",
         not ilk and not bosalan and "x" in kilit_oku(p).get("dis_skiller", {}), (ilk, bosalan))
    # eski biçim kilit
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--evet")
    kl = kilit_oku(p)
    kd, od = calistir(p, "--dogrula")
    kdu, odu = calistir(p, "--durum")
    test("27. dis_skiller'siz (eski biçim) kilit okunur, --durum/--dogrula çalışır, kilit dis_skiller yazmaz", "dis_skiller" not in kl and kd == 0 and kdu == 0
         and "güncel" in odu)

    # ================================================================== G. güvenlik
    print("G. güvenlik")
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg")
    kl = kilit_oku(p)
    kl["dis_skiller"]["ffmpeg"]["hedef"] = "/etc"                       # kilit elle bozulmuş: hedef karttan türetilmeli
    kl["dis_skiller"]["../../x"] = {"ad": "../../x", "tur": "program-bag", "program": "fakeprog", "hedef": "/etc"}
    kl["dis_skiller"]["ffmpeg\n"] = {"ad": "ffmpeg\n", "tur": "donmus", "hedef": "/etc"}
    kl["dis_skiller"]["bilinmez"] = {"ad": "bilinmez", "tur": "uzaylı", "hedef": "/etc"}
    kilit_yaz(p, kl)
    kd, od = calistir(p, "--dogrula")
    (p / ".claude" / "skills" / "ffmpeg").unlink()
    (p / ".agents" / "skills" / "ffmpeg").unlink()
    ky, oy = calistir(p, "--yenile")
    kl2 = kilit_oku(p)
    kk, ok_ = calistir(p, "--kaldir", "../../x", "--evet")
    test("28. elle bozulmuş kilit: geçersiz anahtar/ad/tür kayıtları yok sayılır ve dogrula bildirir; --yenile bağı kilitteki /etc'ye değil karttaki hedefe kurar; "
         "kilit hedefi kartla düzelir; ../../x --kaldir ile hiçbir yola dokunmaz",
         "geçersiz dış skill kaydı" in od and "bilinmeyen dış skill türü" in od and "kilitteki hedef karttaki program yolundan farklı" in od
         and os.readlink(p / ".agents" / "skills" / "ffmpeg") == str(PROG / "ffmpeg") and kl2["dis_skiller"]["ffmpeg"]["hedef"] == str(PROG / "ffmpeg")
         and kk == 2 and "kutuphaneden-degil" in ok_ and Path("/etc/hosts").exists() and degismedi(), od + oy + ok_)
    # yedek / geri alma bağı izlemez, 10'dan fazla işlemde döndürme program klasörüne inmez
    p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg")
    for _ in range(13):
        calistir(p, "--yenile")
    yedekler = sorted((p / ".skill-kutuphanesi" / "yedek").iterdir())
    bag_yedek = [y for y in yedekler if (y / ".agents" / "skills" / "ffmpeg").is_symlink()]
    test("29. 13 işlemde yedek döner (en çok 10); yedekteki bağ BAĞ olarak saklanır (içerik kopyalanmaz); döndürme sırasında program klasörü aynı",
         len(yedekler) <= se.YEDEK_SAYISI and bool(bag_yedek) and all(not (y / ".agents" / "skills" / "ffmpeg").is_dir() or
                                                                      (y / ".agents" / "skills" / "ffmpeg").is_symlink() for y in yedekler) and degismedi())
    # geri al
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--evet")
    once_kilit = kilit_oku(p)
    calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
    kg, og = calistir(p, "--geri-al")
    test("30. --geri-al bağ kurulumunu geri alır: bağlar silinir, kilit önceki hâline döner (dis_skiller yok), program klasörü aynı",
         kg == 0 and not (p / ".agents" / "skills" / "ffmpeg").is_symlink() and not (p / ".claude" / "skills" / "ffmpeg").is_symlink()
         and "dis_skiller" not in kilit_oku(p) and kilit_oku(p)["skiller"].keys() == once_kilit["skiller"].keys() and degismedi(), og)
    # global-baglanti hâlâ yakalanır; bağ ÇOCUĞU tetiklemez
    p = yeni_proje()
    gb = TMP / "home" / ".openmontage"
    (gb / "x").mkdir(parents=True)
    (p / ".claude").mkdir()
    os.symlink(str(gb), p / ".claude" / "skills")
    k1, o1 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--kuru")
    p_c, k_c, o_c = kurulu("--program-skill", "fakeprog:ffmpeg")
    r = se.Rapor()
    se.proje_yapisi_kontrol(p_c, [], r)
    test("31. .claude/skills'in kendisi ~/.openmontage'e giden bağsa global-baglanti HATA; bağlı çocuk (program klasörüne) bu hatayı tetiklemez",
         "global-baglanti" in o1 and not any(x[1] == "global-baglanti" for x in r.satirlar), o1)
    shutil.rmtree(gb)
    # hesap skilleri
    se.hesap_skilleri = lambda: {"ffmpeg": {}}
    try:
        p, k, o = kurulu("--program-skill", "fakeprog:ffmpeg")
        ayar = json.loads((p / ".claude" / "settings.json").read_text(encoding="utf-8")) if (p / ".claude" / "settings.json").exists() else {}
    finally:
        se.hesap_skilleri = lambda: {}
    test("32. Claude hesabında aynı adlı skill varsa bağlı ad için skillOverrides 'off' yazılır", any(v == "off" for v in ayar.get("skillOverrides", {}).values()), ayar)
    # projede kendi skilli
    p = yeni_proje()
    (p / ".claude" / "skills" / "ffmpeg").mkdir(parents=True)
    (p / ".claude" / "skills" / "ffmpeg" / "SKILL.md").write_text(fm("ffmpeg") + "benim", encoding="utf-8")
    k1, o1 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
    k2, o2 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--zorla", "--evet")
    test("33. projede kütüphaneden gelmemiş aynı adlı skill: projede-kendi-skillin (üzerine yazılmaz); --zorla yedekleyip değiştirir (eski davranış)",
         k1 == 2 and "projede-kendi-skillin" in o1 and k2 == 0 and (p / ".claude" / "skills" / "ffmpeg").is_symlink(), o1 + o2)
    # git: bağ yolları ignore edilmiyorsa UYARI
    if shutil.which("git"):
        p = yeni_proje()
        subprocess.run(["git", "init", "-q", str(p)], capture_output=True)
        k1, o1 = calistir(p, "--program-skill", "fakeprog:ffmpeg")
        (p / ".gitignore").write_text(".claude/skills/*\n.agents/skills/*\n", encoding="utf-8")
        k2, o2 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--evet")
        test("34. proje git deposuysa ve bağ yolları .gitignore'da değilse UYARI bag-git-izlenir (--evet ister); ignore edilince uyarı yok",
             k1 == 2 and "bag-git-izlenir" in o1 and k2 == 0 and "bag-git-izlenir" not in o2, o1 + o2)
    else:
        test("34. (git yok: atlandı)", True)
    # kapsam raporu: yalnız bağ/dondurma çalışmasında kütüphane adayı listelenmez; plan varsa eskisi gibi
    p = yeni_proje()
    (p / "package.json").write_text(json.dumps({"dependencies": {"react": "1"}}), encoding="utf-8")
    k1, o1 = calistir(p, "--program-skill", "fakeprog:ffmpeg", "--kuru")
    k2, o2 = calistir(p, "--skill", "alfa", "--kuru")
    k3, o3 = calistir(p, "--skill", "alfa", "--program-skill", "fakeprog:ffmpeg", "--kuru")
    test("35. kapsam raporu: yalnız bağ çalışmasında 'tarama' satırı yok; plan varsa (tek başına ya da bağla) eskisi gibi var",
         "] tarama:" not in o1 and "] tarama:" in o2 and "] tarama:" in o3, o1 + o2)

    # ================================================================== H. yalnız kütüphane skilleri olan proje: P9 öncesiyle birebir aynı
    print("H. P9 öncesiyle karşılaştırma")
    eski_kaynak = subprocess.run(["git", "-C", str(KOK), "show", f"{ESKI_KOMIT}:araclar/skill-ekle.py"], capture_output=True, text=True)
    if eski_kaynak.returncode == 0:
        (TMP / "eski").mkdir()
        (TMP / "eski" / "skill-ekle.py").write_text(eski_kaynak.stdout, encoding="utf-8")
        eski = modul_yukle("se_p9_eski", TMP / "eski" / "skill-ekle.py")
        for m in (eski,):
            m.canli_global = se.canli_global
            m.hesap_skilleri = se.hesap_skilleri
            m.guncelleme_suruyor = se.guncelleme_suruyor
            m.registry = se.registry
            m.ARAC_JSON = se.ARAC_JSON
        pa, pb = yeni_proje("a/proje"), None
        pb = yeni_proje("b/proje")
        for d in (pa, pb):
            (d / "package.json").write_text(json.dumps({"dependencies": {"react": "1"}}), encoding="utf-8")
            (d / "CLAUDE.md").write_text("# benim\n", encoding="utf-8")

        def temiz(metin, proje):
            return re.sub(r"--geri-al \S+", "--geri-al X", re.sub(r"yedek: \S+", "yedek: X", metin.replace(str(proje.resolve()), "<P>").replace(str(proje), "<P>")))

        farklar = []
        komutlar = [("--skill", "alfa", "beta", "--rol-adi", "r1", "--kuru"), ("--skill", "alfa", "beta", "--rol-adi", "r1", "--evet"),
                    ("--durum",), ("--dogrula",), ("--guncelle",), ("--yenile",), ("--arac", "yalniz-claude", "--evet"), ("--durum",),
                    ("--arac", "ortak", "--evet"), ("--blok", "kisa"), ("--kaldir", "beta", "--evet"), ("--durum",), ("--dogrula",)]
        for kom in komutlar:
            ka, oa = calistir(pa, *kom)
            kb, ob = calistir(pb, *kom, mod=eski)
            if (ka, temiz(oa, pa)) != (kb, temiz(ob, pb)):
                farklar.append((kom, ka, kb, temiz(oa, pa)[-400:], temiz(ob, pb)[-400:]))

        def kilit_norm(d):
            k = kilit_oku(d)
            k.pop("guncelleme", None)
            k.pop("proje_yolu", None)
            return k

        def metin_agaci(d):
            out = {}
            for f in sorted(d.rglob("*")):
                rel = str(f.relative_to(d))
                if ".skill-kutuphanesi/yedek" in rel or rel.endswith("son-rapor.md"):
                    continue
                out[rel] = ("L:" + str(f.readlink())) if f.is_symlink() else (f.read_text(encoding="utf-8").replace(str(d.resolve()), "<P>").replace(str(d), "<P>")
                                                                           if f.is_file() else "dir")
            return out
        test("36. yalnız kütüphane skilli proje: kuru/kurulum/durum/dogrula/guncelle/yenile/araç geçişi/kısa blok/kaldır çıktıları, kilit ve proje ağacı "
             "P9 öncesi sürümle birebir aynı", not farklar and kilit_norm(pa) == kilit_norm(pb) and metin_agaci(pa) == metin_agaci(pb), farklar[:2])
    else:
        test("36. (P9 öncesi kaynak git'ten okunamadı: atlandı)", True)

    # ================================================================== I. dayanıklılık
    print("I. dayanıklılık")
    tek = se.Rapor()
    test("37. DIS_AD fullmatch: satır sonlu ad, boşluk, .., / reddedilir; video_toolkit, a..b, A.B kabul edilir; .kurulum-tmp sonekli ad geçersiz",
         not any(se.dis_ad_gecerli(x) for x in ("ffmpeg\n", "a b", "..", "../x", "a/b", ".x", "", "x" * 65, "a.kurulum-tmp", None))
         and all(se.dis_ad_gecerli(x) for x in ("video_toolkit", "a..b", "A.B", "x" * 64)))
    test("38. kaynak/program klasörleri tüm testler boyunca bayt bayt aynı kaldı", degismedi())
    test("39. gerçek ev klasöründe bir şey oluşmadı (HOME geçiciydi)", not (Path(GERCEK_HOME or "/nonexistent") / ".skill-kutuphanesi").exists())
    # === PART B testleri bu satırın altına (try bloğunun içine), son özet bloğunun üstüne eklenir ===
    # ================================================================== PART B: program-denetim.py ve proje-kullanimi.py
    print("PART B. program kartı alanı, denetim ve takip")
    pd = modul_yukle("pd_p9", ARACLAR / "program-denetim.py")
    pk = modul_yukle("pk_p9", ARACLAR / "proje-kullanimi.py")
    sys.path.insert(0, str(ARACLAR))

    def git_calistir(repo, *a):
        return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *a],
                              capture_output=True, text=True, stdin=subprocess.DEVNULL, check=True).stdout.strip()

    BTMP = TMP / "b"
    BTMP.mkdir()
    BEV = BTMP / "ev"
    BEV.mkdir()
    # --- B1 şema
    def sk_bulgu(deger, var=True, yerinde=True, kok=None):
        kart = {"ad": "xp", "repo": "o/r", "tur": "t", "lisans": "MIT", "ne_yapar": "x", "veri_yeri": "x", "ag": "x", "ucret": "ucretsiz",
                "kendini_gunceller": False, "skilleri": [], "asla": ["x"], "guncelleme_adimlari": ["program-denetim.py --oncesi xp"]}
        if yerinde:
            kart.update({"kopya": "yerinde", "yerinde": {"tur": "npm-global", "yol": "x", "paket": "x"}, "kutuphane_surumu": "1.0.0"})
        if var is not None:
            kart["skill_koku"] = deger
        b = pd.sema_denetle({"xp": kart}, kok=kok or BTMP, ev=BEV)
        return [x for x in b if x[2] == "skill_koku"]
    test("B1. skill_koku yok -> sessiz; boş metin geçerli; sayı HATA; göreli yol HATA",
         sk_bulgu(None, var=None) == [] and sk_bulgu("") == [] and [x[0] for x in sk_bulgu(5)] == ["HATA"]
         and [x[0] for x in sk_bulgu("goreli/yol")] == ["HATA"] and [x[0] for x in sk_bulgu("  ")] == [])
    (BEV / "var" / "skills").mkdir(parents=True)
    test("B1. geçerli yol + klasör yok (yerinde kart) -> UYARI; klasör var -> sessiz; '~/' ev altında çözülür; kaynak kartta klasör bakılmaz",
         [x[0] for x in sk_bulgu(str(BTMP / "yok-yok"))] == ["UYARI"] and sk_bulgu(str(BEV / "var" / "skills")) == []
         and sk_bulgu("~/var/skills") == [] and [x[0] for x in sk_bulgu("~/yok-boyle")] == ["UYARI"]
         and sk_bulgu(str(BTMP / "yok-yok"), yerinde=False) == [])
    test("B1. '<DOLDUR>' değeri skill_koku'nda sessiz (yalnız doldurulmamış bulgusu)",
         all(x[0] == "HATA" and "doldurulmamış" in x[3] for x in sk_bulgu("<DOLDUR>")))
    kod_s = pd.main(["--sema", "--siki"]) if False else None
    with contextlib.redirect_stdout(io.StringIO()):
        kod_s = pd.main(["--sema", "--siki"])
    gercek_kart = json.loads((KOK / "programlar.json").read_text(encoding="utf-8"))["programlar"]
    test("B1. gerçek programlar.json: üç karta skill_koku eklendi; --sema --siki çıkış 0",
         kod_s == 0 and gercek_kart["openmontage"]["skill_koku"] == "~/.openmontage/.agents/skills"
         and gercek_kart["hyperframes"]["skill_koku"] == "/usr/local/lib/node_modules/hyperframes/dist/skills"
         and gercek_kart["etsyotomasyon"]["skill_koku"] == "")

    # --- B2..B5 için sahte npm programı + projeler (se ile gerçek bağ kurulumu)
    BNPM = BTMP / "npmprog"
    (BNPM / "dist" / "skills").mkdir(parents=True)
    (BNPM / "package.json").write_text(json.dumps({"version": "1.0.0"}), encoding="utf-8")
    for n in ("zz", "yy"):
        uygula(BNPM / "dist" / "skills", n)
    BKOK = BTMP / "kok"
    (BKOK / "notlar").mkdir(parents=True)
    BDOCS = BTMP / "docs"
    BDOCS.mkdir()
    BKART = {"ad": "npmprog", "kopya": "yerinde", "yerinde": {"tur": "npm-global", "yol": str(BNPM), "paket": "npmprog"},
             "kutuphane_surumu": "1.0.0", "skill_koku": str(BNPM / "dist" / "skills")}
    KART_ICERIK["programlar"]["npmprog"] = BKART
    KART.write_text(json.dumps(KART_ICERIK), encoding="utf-8")

    def bctx(**kw):
        return pd._ctx(ev=BEV, kok=BKOK, bugun=None, environ={}, **kw)

    def satirlar(S):
        return [(x[0], x[1], x[2]) for x in S]

    pd.repo_durumu = lambda r: ("var", None)          # ağ yok
    # B2: bağ yokken çıktı aynı (projeler.json yok / boş tarama kökü)
    S0, s0 = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.1.0"))
    (BKOK / "projeler.json").write_text(json.dumps({"tarama_kokleri": [str(BDOCS)]}), encoding="utf-8")
    S1, s1 = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.1.0"))
    test("B2. bağ yokken (projeler.json yok / projede bağ yok) --oncesi satırları ve sonuç birebir aynı; 'bağlar' satırı yok",
         S0 == S1 and s0 == s1 and not any(x[1] == "bağlar" for x in S1))
    pa, pb = BDOCS / "proje-a", BDOCS / "proje-b"
    pa.mkdir()
    pb.mkdir()
    ka, oa = calistir(pa, "--program-skill", "npmprog:zz", "npmprog:yy", "--evet")
    kb, ob = calistir(pb, "--program-skill", "npmprog:zz", "--evet")
    test("B2. sahte projelerde bağlar se.main ile kuruldu", ka == 0 and kb == 0 and (pa / ".claude" / "skills" / "yy").exists(), oa + ob)
    ctx_a = bctx(cevrimdisi=True, hedef="1.1.0")
    S2, s2 = pd.oncesi_denetle("npmprog", BKART, ctx_a)
    bag2 = [x for x in S2 if x[1] == "bağlar"]
    test("B2. bağlar sağlam: TAMAM satırı (3 bağ, projeler ve skiller); güncelleme bekleyen yolda npm için 'indirilmeden' BİLGİ (B4)",
         bag2[0][0] == "TAMAM" and "3 bağ" in bag2[0][2] and "proje-a" in bag2[0][2] and "proje-b" in bag2[0][2]
         and any(x[0] == "BİLGİ" and "indirilmeden" in x[2] for x in bag2) and not any(x[0] in ("HATA", "UYARI") for x in bag2), bag2)
    # kurulu değil, bağ yok: eski çıktı
    S2b, _ = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.0.0"))
    test("B4. hedef kurulu sürümle aynıysa 'indirilmeden' satırı yok (hedef yok ya da aynı)",
         not any("indirilmeden" in x[2] for x in S2b)
         and not any("indirilmeden" in x[2] for x in pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True))[0]))
    # hedef klasör kaldırıldı
    gizli_yy = BNPM / "dist" / "skills" / "yy"
    yedek_yy = BNPM / "yy-yedek"
    gizli_yy.rename(yedek_yy)
    S3, s3 = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.1.0"))
    kirik3 = [x for x in S3 if x[1] == "bağlar" and x[0] == "UYARI"]
    S3b, s3b = pd.oncesi_denetle("npmprog", BKART, bctx(hedef="1.0.0"))      # güncellenecek bir şey yok görünümü
    kirik3b = [x for x in S3b if x[1] == "bağlar" and x[0] == "HATA"]
    test("B2. hedef kaldırıldı + güncelleme bekliyor -> bağlar UYARI (HATA değil); sonuç, bağsız durumla aynı (bağ HAZIR DEĞİL sebebi olmaz)",
         kirik3 and all(x[0] == "UYARI" for x in kirik3) and "proje-a: yy" in kirik3[0][2] and "~" not in kirik3[0][2].replace("~/", "")
         and not any(x[0] == "HATA" and x[1] == "bağlar" for x in S3) and s3 == s0
         and [x for x in S3 if x[0] == "HATA"] == [x for x in S0 if x[0] == "HATA"], S3)
    test("B2. 'GÜNCELLENECEK BİR ŞEY YOK' görünümünde kırık bağ HATA (iki bağ: proje-a yy); sonuç yine HAZIR DEĞİL değil",
         s3b == "GÜNCELLENECEK BİR ŞEY YOK" and len(kirik3b) == 1 and "yy bağı kırık" in kirik3b[0][2], S3b)
    gizli_yy.exists() or yedek_yy.rename(gizli_yy)
    # KURULU DEĞİL + kırık bağ (bu durumda bağlar zaten kırık görünür: program dizini gerçekten yoksa)
    (BNPM / "package.json").rename(BNPM / "package.json.k")
    gizli_yy.rename(yedek_yy)
    S4, s4 = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True))
    yedek_yy.rename(gizli_yy)
    (BNPM / "package.json.k").rename(BNPM / "package.json")
    test("B2. KURULU DEĞİL + kırık bağ: sonuç 'KURULU DEĞİL' (HAZIR DEĞİL çıkmaz); bağlar satırı UYARI",
         s4 == "KURULU DEĞİL" and any(x[0] == "UYARI" and x[1] == "bağlar" for x in S4) and not any(x[0] == "HATA" and x[1] == "bağlar" for x in S4), S4)
    # JSON nesnesi: sorun satırları ve kod
    S5, _ = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.1.0"))
    # kart yok / skill_koku yok: bağlar hedefi bilinmiyor -> kırık (UYARI), hata vermez
    kart_sk_yok = {k: v for k, v in BKART.items() if k != "skill_koku"}
    S6, _ = pd.oncesi_denetle("npmprog", kart_sk_yok, bctx(cevrimdisi=True, hedef="1.1.0"))
    test("B2. kartta skill_koku yoksa bağlar 'kartta skill_koku yok' der, çökmez",
         any("kartta skill_koku yok" in x[2] for x in S6 if x[1] == "bağlar"), S6)
    # kilitte bozuk/kötü amaçlı anahtar: yol bileşeni olarak kullanılmaz
    kk = kilit_oku(pb)
    kk["dis_skiller"]["../kotu"] = {"ad": "../kotu", "tur": "program-bag", "program": "npmprog", "hedef": "/etc"}
    kk["dis_skiller"]["bos"] = "metin"
    kilit_yaz(pb, kk)
    S7, _ = pd.oncesi_denetle("npmprog", BKART, bctx(cevrimdisi=True, hedef="1.1.0"))
    test("B2. kilitte geçersiz anahtar ('../kotu') ve sözlük olmayan kayıt yok sayılır (hedef karttan türetilir)",
         not any("kotu" in x[2] for x in S7) and "3 bağ" in [x for x in S7 if x[1] == "bağlar"][0][2])
    kk["dis_skiller"].pop("../kotu")
    kk["dis_skiller"].pop("bos")
    kilit_yaz(pb, kk)

    # --- B3 git programı: gerçek geçici depo, ikinci commit'te skill kalkar
    REPO = BTMP / "repo"
    (REPO / "skills" / "a").mkdir(parents=True)
    (REPO / "skills" / "b").mkdir(parents=True)
    (REPO / "skills" / "a" / "SKILL.md").write_text(fm("a"), encoding="utf-8")
    (REPO / "skills" / "b" / "SKILL.md").write_text(fm("b"), encoding="utf-8")
    git_calistir(REPO, "init", "-q", "-b", "main") if (REPO / ".git").exists() is False and subprocess.run(
        ["git", "-C", str(REPO), "init", "-q", "-b", "main"], capture_output=True).returncode == 0 else None
    git_calistir(REPO, "add", ".")
    git_calistir(REPO, "commit", "-q", "-m", "bir")
    c1 = git_calistir(REPO, "rev-parse", "HEAD")
    git_calistir(REPO, "checkout", "-q", "-b", "diger")
    git_calistir(REPO, "rm", "-q", "-r", "skills/b")
    git_calistir(REPO, "commit", "-q", "-m", "iki")
    c2 = git_calistir(REPO, "rev-parse", "HEAD")
    git_calistir(REPO, "checkout", "-q", "main")
    GKART = {"ad": "gitprog", "kopya": "yerinde", "yerinde": {"tur": "git-checkout", "yol": str(REPO), "dal": "main"},
             "kutuphane_commit": c1, "skill_koku": str(REPO / "skills")}
    KART_ICERIK["programlar"]["gitprog"] = GKART
    KART.write_text(json.dumps(KART_ICERIK), encoding="utf-8")
    pg = BDOCS / "proje-g"
    pg.mkdir()
    kg, og = calistir(pg, "--program-skill", "gitprog:a", "gitprog:b", "--evet")
    test("B3. git programı için bağlar kuruldu (a, b)", kg == 0 and (pg / ".claude" / "skills" / "b").exists(), og)
    kayit = []
    orj_okuma, orj_run = pd.git_okuma, subprocess.run

    def kayitli_run(cmd, *a, **k):
        kayit.append(list(cmd))
        return orj_run(cmd, *a, **k)
    subprocess.run = kayitli_run
    try:
        Sg, sg = pd.oncesi_denetle("gitprog", GKART, bctx(cevrimdisi=True, hedef=c2))
        Sg_yok, _ = pd.oncesi_denetle("gitprog", GKART, bctx(cevrimdisi=True, hedef="deadbeef" * 5))
        Sg_x, _ = pd.oncesi_denetle("gitprog", GKART, bctx(cevrimdisi=True, hedef="-x"))
    finally:
        subprocess.run = orj_run
    bg = [x for x in Sg if x[1] == "bağlar"]
    test("B3. hedef commit yerel depoda: 'bağ kırılacak' yalnız b için (UYARI), a için TAMAM; HAZIR DEĞİL sebebi bağlar değil",
         any(x[0] == "UYARI" and "bağ kırılacak" in x[2] and "proje-g: b " in x[2] for x in bg)
         and not any("proje-g: a " in x[2] and x[0] == "UYARI" for x in bg) and any(x[0] == "TAMAM" and "1 bağın hedefi" in x[2] for x in bg)
         and not any(x[0] == "HATA" for x in bg), Sg)
    test("B3. hedef commit depoda yok -> BİLGİ 'hedef commit yerel depoda yok' (uyarı yok); '--hedef -x' seçenek gibi git'e verilmez",
         any(x[0] == "BİLGİ" and "yerel depoda yok" in x[2] for x in Sg_yok if x[1] == "bağlar")
         and any(x[0] == "BİLGİ" and "sha" in x[2] for x in Sg_x if x[1] == "bağlar")
         and not any(len(c) > 5 and c[-1] == "-x" or any(t.startswith("-x") for t in c[4:]) for c in kayit))
    yasak = {"fetch", "pull", "clone", "checkout", "switch", "merge", "reset", "push", "add", "commit"}
    test("B3. ağ yok, değiştiren git komutu yok (çağrı kaydı): fetch/pull/clone/checkout/switch...",
         kayit and not any(yasak & set(c) for c in kayit) and any("cat-file" in c for c in kayit), kayit[:6])
    # --- B5 rapor()
    def sahte_yerinde(ad, p):
        y = p.get("yerinde") or {}
        t = y.get("tur")
        return {"ad": ad, "tur": t, "kart": p.get("kutuphane_commit") if t == "git-checkout" else p.get("kutuphane_surumu"),
                "kurulu": "1.0.0", "son": "1.0.0", "geride": None, "degisen": 0, "izlenmeyen": 0, "pin": None, "pin_fark": [], "durum": "güncel"}
    orj_yd = pd.yerinde_denetle
    pd.yerinde_denetle = sahte_yerinde
    try:
        doc = {"sema": 2, "programlar": {"npmprog": BKART}}
        bos_kok = BTMP / "bos-kok"
        bos_kok.mkdir()

        def rapor_al(kok):
            c = pd._ctx(ev=BEV, kok=kok, environ={})
            g = io.StringIO()
            with contextlib.redirect_stdout(g):
                out, B, _ = pd.rapor(None, c, doc)
            return out, B, g.getvalue()
        out_a, B_a, g_a = rapor_al(bos_kok)
        (BKOK / "projeler.json").write_text(json.dumps({"tarama_kokleri": [str(BTMP / "yok-tarama")]}), encoding="utf-8")
        out_b, B_b, g_b = rapor_al(BKOK)
        test("B5. rapor(): bağ yokken metin, B ve çıktı birebir aynı; 'Programla gelen skiller' bölümü yok",
             out_a == out_b and B_a == B_b and g_a == g_b and not any("bağlar" in x for x in out_b))
        (BKOK / "projeler.json").write_text(json.dumps({"tarama_kokleri": [str(BDOCS)]}), encoding="utf-8")
        gizli_yy.rename(yedek_yy)
        out_c, B_c, _ = rapor_al(BKOK)
        metin_c = "\n".join(out_c)
        test("B5. rapor(): bağ var + yy kırık -> bölüm, tablo satırları, B satırları/sorun/karar, ## Dikkat satırı",
             "## Programla gelen skiller (bağlar)" in metin_c and "| npmprog | proje-a | yy | HAYIR |" in metin_c
             and "| npmprog | proje-a | zz | evet |" in metin_c and "npmprog: 3 bağ, 1 kırık" in B_c["satirlar"]
             and "npmprog 1 kırık bağ" in B_c["sorun"] and any("1 kırık bağ" in x for x in B_c["karar"])
             and "- npmprog · bağ kırık: proje-a/yy" in metin_c and metin_c.index("## Dikkat") < metin_c.index("## Programla gelen"), metin_c[-600:])
        # --ozet-json ve --siki
        kart_dosya = BTMP / "kart.json"
        kart_dosya.write_text(json.dumps(doc), encoding="utf-8")

        def ana(*extra):
            g = io.StringIO()
            with contextlib.redirect_stdout(g):
                kod = pd.main(["--kart", str(kart_dosya), "--kok", str(BKOK), "--ev", str(BEV), "--ozet-json", *extra])
            return kod, json.loads(g.getvalue().strip().splitlines()[-1])
        k1, j1 = ana()
        k2, j2 = ana("--siki")
        test("B5. --ozet-json şekli aynı (arac, durum, satirlar, karar_bekleyen), kırık bağ durumu 'sorun'; --siki çıkış 1, normal 0",
             set(j1) == {"arac", "durum", "satirlar", "karar_bekleyen"} and j1["durum"] == "sorun" and k1 == 0 and k2 == 1
             and any("kırık bağ" in x for x in j1["karar_bekleyen"]))
        yedek_yy.rename(gizli_yy)
        k3, j3 = ana("--siki")
        test("B5. bağlar onarılınca bağ kaynaklı sorun kalmaz (bağlar satırı 3 bağ, 0 kırık)",
             "npmprog: 3 bağ, 0 kırık" in j3["satirlar"] and "npmprog 1 kırık bağ" not in str(j3), j3)
    finally:
        pd.yerinde_denetle = orj_yd
        if yedek_yy.exists():
            yedek_yy.rename(gizli_yy)

    # --- B6 proje-kullanimi rapor_metni
    pk.PROGRAMLAR = BKOK / "programlar.json"
    pk.AYAR = BKOK / "projeler.json"
    pk.RAPOR = BKOK / "notlar" / "proje-kullanimi.md"
    pk.DURUM_RAPORU = BKOK / "notlar" / "proje-durumu.md"
    pk.REGISTRY = BKOK / "registry.json"
    (BKOK / "registry.json").write_text(json.dumps({"skiller": []}), encoding="utf-8")
    pk._SE_ONBELLEK[0] = se
    (BKOK / "programlar.json").write_text(json.dumps({"programlar": {"npmprog": BKART, "gitprog": GKART}}), encoding="utf-8")
    ayar = {"tarama_kokleri": [str(BDOCS)]}
    (BKOK / "projeler.json").write_text(json.dumps(ayar), encoding="utf-8")
    pl = pk.oku(ayar)
    test("B6. oku(): üç proje bulundu (a, b, g)", sorted(p["ad"] for p in pl) == ["proje-a", "proje-b", "proje-g"])
    # dış skilli olmayan kilitler: P9 öncesi rapor_metni ile baytı baytına aynı
    eski_kaynak = subprocess.run(["git", "-C", str(KOK), "show", f"{ESKI_KOMIT}:araclar/proje-kullanimi.py"], capture_output=True, text=True)
    pl_bos = [{"ad": "x1", "yol": BTMP / "x1", "kilit": {"skiller": {"alfa": {"id": "alfa", "repo": "o/r", "kaynak_yol": "alfa", "commit": "c1"}}, "araclar": ["claude"]}, "elle": ["eski"]},
              {"ad": "x2", "yol": BTMP / "x2", "kilit": {"skiller": {}}, "elle": []}]
    if eski_kaynak.returncode == 0:
        (BTMP / "pk_eski.py").write_text(eski_kaynak.stdout, encoding="utf-8")
        pk_eski = modul_yukle("pk_eski_p9", BTMP / "pk_eski.py")
        m_yeni, k_yeni = pk.rapor_metni(pl_bos, {}, {})
        m_eski, k_eski = pk_eski.rapor_metni(pl_bos, {}, {})
        test("B6. dış skill yokken rapor_metni P9 öncesiyle bayt bayt aynı; kullanan sözlüğü aynı", m_yeni == m_eski and k_yeni == k_eski)
    else:
        test("B6. (P9 öncesi kaynak okunamadı: atlandı)", True)
    m_dis, k_dis = pk.rapor_metni(pl, ayar, {})
    test("B6. dış skill var: özet hücresinde '(+N bağ, M donmuş)', proje satırı, sonda 'Programla gelen skiller → projeler'; kullanan sözlüğü değişmez",
         "| 0 (+2 bağ, 0 donmuş) |" in m_dis and "Programla gelen (bağ): `yy` (npmprog), `zz` (npmprog)" in m_dis
         and "## Programla gelen skiller → projeler" in m_dis and "| npmprog | `zz` | proje-a, proje-b |" in m_dis
         and "| gitprog | `b` | proje-g |" in m_dis and m_dis.rstrip("\n").splitlines()[-1].startswith("| npmprog | `zz`")
         and k_dis == {}, m_dis[-1500:])

    # --- B7 sınıflandırma ve sağlık
    skiller_l = SAHTE_KAYIT

    def denetle(proje):
        return pk.proje_denetle(proje, ayar, skiller_l, lambda: {}, se, pk.date.today())
    Pa, Pb = denetle(pa), denetle(pg)
    test("B7. bağlı disk skilleri KAYITSIZ sayılmaz; sayaçlar; kırık yok",
         Pa["sayac"]["program_bag"] == 2 and Pa["sayac"]["kayitsiz"] == 0 and Pa["sayac"]["bag_kirik"] == 0 and not any("KAYITSIZ" in t for _, t in Pa["satirlar"]), Pa)
    test("B7. sağlıklı bağlı proje 'temiz'", Pa["durum"] == "temiz" and Pb["durum"] == "temiz", (Pa["satirlar"], Pb["satirlar"]))
    # donmuş
    pf = BDOCS / "proje-f"
    pf.mkdir()
    kf, of = calistir(pf, "--dondur", GENEL / "eski-skill", "--evet")
    Pf = denetle(pf)
    test("B7. donmuş skill KAYITSIZ sayılmaz; tek 'bilgi' satırı; proje 'temiz'; sayaç donmus=1",
         kf == 0 and Pf["sayac"]["donmus"] == 1 and Pf["sayac"]["kayitsiz"] == 0 and Pf["durum"] == "temiz"
         and [x for x in Pf["satirlar"] if "donmuş" in x[1]] == [("bilgi", "donmuş skill (kütüphane güncellemez): eski-skill")], Pf)
    # asılı bağ: program klasörü kalkınca dogrula tek 'sorun' satırı verir, KAYITSIZ sayılmaz
    gizli_yy.rename(yedek_yy)
    try:
        Pk = denetle(pa)
        bk = [x for x in Pk["satirlar"] if x[0] == "sorun" and "program bağı kırık" in x[1]]
        test("B7. asılı bağ: dogrula'dan tek 'sorun' satırı (program bağı kırık + ipucu), sayac bag_kirik == 1, KAYITSIZ yok, durum 'sorun'",
             len(bk) == 1 and "program kurulu değilse" in bk[0][1] and Pk["sayac"]["bag_kirik"] == 1 and Pk["sayac"]["kayitsiz"] == 0
             and Pk["durum"] == "sorun", Pk["satirlar"])
        proje_listesi = [Pk, Pf]
        s_ = {"projeler": proje_listesi, "kaybolanlar": [], "takipte_olmayan": [], "durum": "sorun", "karar_bekleyen": [],
              "ayar_uyarilari": [], "kayitsiz": {"kokler": [], "derinlik": 1, "sinira_ulasildi": False, "bilgi": [], "sorun": [], "adaylar": [],
                                                  "yoksayilan": [], "talimat_sayisi": 0}}
        s_["karar_bekleyen"] = pk._karar_bekleyenler(s_)
        metin_d = pk.durum_raporu_metni(s_, ayar)
        oz = pk.ozet_nesnesi(s_)
        test("B7. karar bekleyen kırık bağ girdisi; durum raporunda yeni bölüm; ozet_nesnesi 'PROGRAM BAĞI' satırı, <= 15 satır",
             any("1 kırık program bağı" in x and "--yenile" in x for x in s_["karar_bekleyen"])
             and "## Programla gelen ve donmuş skiller" in metin_d and "| proje-a | 2 | 0 | 1 |" in metin_d
             and any(x.startswith("PROGRAM BAĞI: 2 bağ (1 kırık), 1 donmuş skill") for x in oz["satirlar"]) and len(oz["satirlar"]) <= 15, oz)
        # dış skill yokken bölüm/satır yok
        s2_ = dict(s_, projeler=[dict(Pa, sayac=dict(Pa["sayac"], program_bag=0, donmus=0, bag_kirik=0))])
        test("B7. dış skill yokken durum raporunda bölüm yok, ozet_nesnesi'nde PROGRAM BAĞI yok",
             "Programla gelen ve donmuş" not in pk.durum_raporu_metni(s2_, ayar)
             and not any(x.startswith("PROGRAM BAĞI") for x in pk.ozet_nesnesi(s2_)["satirlar"]))
    finally:
        yedek_yy.rename(gizli_yy)

    # --- B8 --program, --skill
    def pk_calistir(*args):
        pk._CIKIS = 0
        k, o = calistir(*args, mod=pk)
        return k, o, pk._CIKIS
    k, o, cks = pk_calistir("--program", "npmprog")
    test("B8. --program: her bağ 'hedef var' ve sürüm; çıkış 0",
         k == 0 and "proje-a: zz — program bağı (npmprog 1.0.0) · hedef var" in o and "proje-b: zz" in o and "YOK" not in o and cks == 0, o)
    k, o, cks = pk_calistir("--program", "gitprog")
    test("B8. --program git programı: sürüm 8 haneli commit", k == 0 and f"gitprog {c1[:8]}) · hedef var" in o, o)
    k, o, cks = pk_calistir("--program", "yok-program")
    test("B8. bilinmeyen/bağsız program -> 'Hiçbir projede bu programın bağı yok.'", "Hiçbir projede bu programın bağı yok." in o and k == 0)
    gizli_yy.rename(yedek_yy)
    try:
        k, o, cks = pk_calistir("--program", "npmprog", "--siki")
        k0, o0, cks0 = pk_calistir("--program", "npmprog")
        test("B8. hedef kaldırılınca 'hedef YOK'; --siki çıkış 1, siki olmadan 0",
             "proje-a: yy — program bağı (npmprog 1.0.0) · hedef YOK" in o and cks == 1 and cks0 == 0, o)
    finally:
        yedek_yy.rename(gizli_yy)
    k, o, _ = pk_calistir("--program", "npmprog", "--ekle", str(pa))
    test("B8. --program ile --ekle birlikte -> çıkış 2 (hata)", k == 2 and "birlikte verilemez" in o, o)
    k, o, _ = pk_calistir("--skill", "zz")
    k_f, o_f, _ = pk_calistir("--skill", "eski-skill")
    k_y, o_y, _ = pk_calistir("--skill", "yok-boyle")
    test("B8. --skill ad ile dış skilleri de bulur; yoksa 'Hiçbir projede kullanılmıyor.'",
         "proje-a: zz — programla gelen (bağ: npmprog)" in o and "proje-f: eski-skill — donmuş (projenin kendi kopyası)" in o_f
         and "Hiçbir projede kullanılmıyor." in o_y)
    # --- B9 belgeler
    claude_md = (KOK / "CLAUDE.md").read_bytes()
    basla = (KOK / "BASLA.md").read_text(encoding="utf-8")
    metin_c = claude_md.decode("utf-8")
    ayar_gercek = json.loads((KOK / "projeler.json").read_text(encoding="utf-8")) if (KOK / "projeler.json").exists() else {}
    adlar = set((ayar_gercek.get("notlar") or {}).keys()) | {Path(str(x)).name for x in (ayar_gercek.get("ek_projeler") or [])}
    kart_metin = (KOK / "programlar.json").read_text(encoding="utf-8")
    proje_adi_var = [a for a in adlar if len(a) >= 4 and re.search(r"(?<![\w])" + re.escape(a) + r"(?![\w])", kart_metin)]
    test("B9. CLAUDE.md == AGENTS.md; BASLA.md ve CLAUDE.md --program-skill, --dondur, --program geçer; programlar.json'da proje adı yok",
         claude_md == (KOK / "AGENTS.md").read_bytes()
         and all(x in basla and x in metin_c for x in ("--program-skill", "--dondur", "proje-kullanimi.py --program")) and not proje_adi_var, proje_adi_var)
    test("B9. kararlar.md K-28 altında kurulum yolu satırı; rehber/10 ve /11 --program ve 'bağlar' anlatır",
         "K-28 kurulum yolu yazıldı" in (KOK / "notlar" / "kararlar.md").read_text(encoding="utf-8")
         and "--program <ad>" in (KOK / "rehber" / "10-proje-kullanimi.md").read_text(encoding="utf-8")
         and "`bağlar`" in (KOK / "rehber" / "11-program-yonetimi.md").read_text(encoding="utf-8")
         and "3b. python3 araclar/proje-kullanimi.py --program" in (KOK / "promptlar" / "13-program-kur-guncelle.md").read_text(encoding="utf-8"))
    test("B9. sahte program klasörleri B testlerinde de bayt bayt aynı (A fixture'ları)", degismedi())
    # --- B10 inceleme düzeltmeleri
    print("B10. inceleme düzeltmeleri")
    pg, kg, og = kurulu("--program-skill", "fakeprog:ffmpeg", arac="yalniz-claude")
    cg = pg / ".claude" / "skills" / "ffmpeg"
    cg.unlink()
    cg.mkdir()
    (cg / "BENIM.txt").write_text("benim", encoding="utf-8")
    k, o = calistir(pg, "--program-skill", "fakeprog:ffmpeg", "--evet")
    k2, o2 = calistir(pg, "--program-skill", "fakeprog:ffmpeg", "--evet", "--zorla")
    test("B10. bağ yerinde elle konmuş gerçek klasör: HATA bag-gercek-klasor (--zorla ile de), klasör silinmez",
         k != 0 and k2 != 0 and "bag-gercek-klasor" in o and (cg / "BENIM.txt").is_file() and not cg.is_symlink(), o + o2)
    gz = {}
    for ad, dosya in (("g2-sa", "service_account.json"), ("g2-sec", "secret.json"), ("g2-key", "apikey.txt"), ("g2-p8", "AuthKey_X.p8"),
                      ("g2-jks", "store.jks"), ("g2-gc", ".gitconfig")):
        d = uygula(GENEL, ad)
        (d / dosya).write_text(GIZLI_ISARET, encoding="utf-8")
        gz[ad] = d
    d = uygula(GENEL, "g2-kube")
    (d / ".kube").mkdir()
    (d / ".kube" / "config").write_text("x", encoding="utf-8")
    gz["g2-kube"] = d
    d = uygula(GENEL, "g2-docker")
    (d / ".docker").mkdir()
    (d / ".docker" / "config.json").write_text("x", encoding="utf-8")
    gz["g2-docker"] = d
    sonuc = {}
    for ad, d in gz.items():
        pp = yeni_proje()
        kk, oo = calistir(pp, "--dondur", d, "--evet")
        sonuc[ad] = (kk != 0 and "dondur-gizli" in oo and not (pp / ".claude" / "skills" / ad).exists())
    test("B10. daha çok gizli ad (service_account, secret, apikey, .p8, .jks, .kube, .docker, .gitconfig) dondur-gizli ile reddedilir",
         all(sonuc.values()), sonuc)
    ust = TMP / "kapsayan"
    uygula(ust, "x")
    (ust / "SKILL.md").write_text(fm("kapsayan") + "x\n", encoding="utf-8")
    pk = ust / "proj"
    pk.mkdir()
    k, o = calistir(pk, "--dondur", ust, "--evet")
    test("B10. kaynak projeyi içeren klasör: HATA dondur-kendisi, proje boş kalır (kopya kendi içine inmez)",
         k != 0 and "dondur-kendisi" in o and not (pk / ".claude").exists() and not (pk / ".skill-kutuphanesi").exists(), o)
    eski_tavan = se.DONDUR_TAVAN_KLASOR
    se.DONDUR_TAVAN_KLASOR = 20
    try:
        d = uygula(GENEL, "b-cokklasor")
        for i in range(30):
            (d / f"k{i}").mkdir()
        pp = yeni_proje()
        k, o = calistir(pp, "--dondur", d, "--evet")
    finally:
        se.DONDUR_TAVAN_KLASOR = eski_tavan
    test("B10. klasör sayısı tavanı aşılınca dondur-cok-buyuk", k != 0 and "dondur-cok-buyuk" in o, o)

    # ================================================================== C. ön kontrol: ../<kardeş>/ kardeşi bağ ya da donmuş skill olarak projede
    print("C. kardes-eksik ve dış skiller")

    def kardesli(ad, kardes_ad):
        k = sahte_kayit_yap(ad, kardes_bagimliliklari={kardes_ad: {"id": kardes_ad, "dosya_sayisi": 1}})
        (Path(k["yol"]) / "SKILL.md").write_text(fm(ad) + f"Oku ../{kardes_ad}/ref.md\n", encoding="utf-8")
        SAHTE_KAYIT.append(k)
        return k

    def kardes_uyari(o, kardes_ad):
        return [l for l in o.splitlines() if "kardes-eksik" in l and f"../{kardes_ad}/" in l]
    kardesli("kd-kullanan", "hyperframes-x")
    kardesli("kd-donmus", "eski-skill")
    kardesli("kd-yabanci", "yok-boyle-kardes")
    p = yeni_proje()
    k, o = calistir(p, "--skill", "kd-kullanan", "--kuru")
    test("C1. kardeş projede yok: UYARI kardes-eksik (taban davranış korunur)", len(kardes_uyari(o, "hyperframes-x")) == 1, o)
    pb = yeni_proje()
    k, o = calistir(pb, "--program-skill", "fakeprog:hyperframes-x", "--evet")
    k2, o2 = calistir(pb, "--skill", "kd-kullanan", "--kuru")
    test("C2. kardeş projede program bağı olarak kayıtlı (kilit dis_skiller): kardes-eksik UYARI yok", k == 0 and not kardes_uyari(o2, "hyperframes-x"), o + o2)
    p = yeni_proje()
    k, o = calistir(p, "--skill", "kd-kullanan", "--program-skill", "fakeprog:hyperframes-x", "--kuru")
    test("C3. kardeş aynı çalışmada --program-skill ile isteniyor: kardes-eksik UYARI yok", not kardes_uyari(o, "hyperframes-x"), o)
    pd = yeni_proje()
    k, o = calistir(pd, "--dondur", GENEL / "eski-skill", "--evet")
    k2, o2 = calistir(pd, "--skill", "kd-donmus", "--kuru")
    test("C4. kardeş projede donmuş skill olarak kayıtlı: kardes-eksik UYARI yok", k == 0 and not kardes_uyari(o2, "eski-skill"), o + o2)
    p = yeni_proje()
    k, o = calistir(p, "--skill", "kd-donmus", "--dondur", GENEL / "eski-skill", "--kuru")
    test("C5. kardeş aynı çalışmada --dondur ile isteniyor: kardes-eksik UYARI yok", not kardes_uyari(o, "eski-skill"), o)
    p = yeni_proje()
    k, o = calistir(p, "--skill", "kd-yabanci", "--program-skill", "fakeprog:hyperframes-x", "--kuru")
    test("C6. başka adlı kardeş için UYARI sürer (dış skill adı yalnız kendi adını karşılar)", len(kardes_uyari(o, "yok-boyle-kardes")) == 1, o)
    pk = yeni_proje()
    calistir(pk, "--program-skill", "fakeprog:hyperframes-x", "--evet")
    k, o = calistir(pk, "--skill", "kd-kullanan", "--evet")
    kl = kilit_oku(pk)
    test("C7. kardeş bağ olarak varken kurulum geçer, kilitte skill ve bağ birlikte durur, --dogrula temiz",
         k == 0 and "kd-kullanan" in kl["skiller"] and "hyperframes-x" in kl.get("dis_skiller", {}) and calistir(pk, "--dogrula")[0] == 0, o)

    test("B10. sahte program ve genel klasörler değişmedi (yeni sahte skiller dışında)", agac(TMP / "program") == KORUMA[0])

finally:
    shutil.rmtree(TMP, ignore_errors=True)
    if GERCEK_HOME:
        os.environ["HOME"] = GERCEK_HOME

gecen = sum(1 for _, k in SONUC if k)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
