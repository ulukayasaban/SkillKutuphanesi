#!/usr/bin/env python3
"""P2 testleri: araclar/genel-bekci.py. Yalnız geçici klasör ve sahte ev; gerçek ev klasörü ve gerçek kütüphane tabanı kullanılmaz.
Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import hashlib
import importlib.util
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
ARAC = ARACLAR / "genel-bekci.py"
GERCEK_TABAN = KOK / "notlar" / "genel-klasor-tabani.json"
GERCEK_TABAN_VARDI = GERCEK_TABAN.exists()
TMP = Path(tempfile.mkdtemp(prefix="p2test-"))
SONUC = []
SIRLAR = ["SECRETVALUE123", "SECRETVALUE456", "FAKE_SECRET_AAA", "FAKE_API_KEY", "SECRETPROJ"]
TARIH = "2026-11-12"
KART = TMP / "kart.json"
KART.write_text(json.dumps({"programlar": {"hyperframes": {"skilleri": ["cardskill"]}}}), encoding="utf-8")
SAYAC = [0]


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    if not kosul:
        print(f"  BAŞARISIZ: {ad} {ayrinti}"[:600])


def yaz(p, metin="x"):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(metin, encoding="utf-8")


def ev_kur():
    """Her çağrıda yeni sahte ev: (ev, taban_yolu)."""
    SAYAC[0] += 1
    kok = TMP / f"s{SAYAC[0]}"
    ev = kok / "ev"
    ev.mkdir(parents=True)
    (ev / ".openmontage/.agents/skills/x").mkdir(parents=True)
    yaz(ev / ".openmontage/.agents/skills/x/SKILL.md")
    yaz(ev / ".openmontage/skills/z/a.md")
    cl = ev / ".claude/skills"
    cl.mkdir(parents=True)
    os.symlink(str(ev / ".openmontage/.agents/skills/x"), cl / "x")
    os.symlink("../../.agents/skills/y", cl / "y")
    for i in range(3):
        yaz(cl / f"hyperframes/f{i}.md")
    yaz(cl / "design-dna/SKILL.md", "dd")
    yaz(cl / "mystery/SKILL.md")
    yaz(cl / "cardskill/SKILL.md")
    yaz(cl / "synced/a/b/SKILL.md")
    (cl / ".trash").mkdir()
    yaz(cl / ".DS_Store")
    yaz(ev / ".agents/skills/y/SKILL.md")
    yaz(ev / ".agents/skills/microsoft-foundry/SKILL.md")
    yaz(ev / ".agents/skills/localhf/SKILL.md")
    yaz(ev / ".agents/skills/localother/SKILL.md")
    yaz(ev / ".agents/.skill-lock.json", json.dumps({"skills": {
        "y": {"source": "heygen-com/hyperframes", "sourceType": "github"},
        "microsoft-foundry": {"source": "microsoft/foo", "sourceType": "github"},
        "localhf": {"source": "/Users/x/SECRETPROJ/hf-skills/localhf", "sourceType": "local"},
        "localother": {"source": "/Users/x/SECRETPROJ/baska/localother", "sourceType": "local"}}}))
    cx = ev / ".codex/skills"
    cx.mkdir(parents=True)
    os.symlink("../../.agents/skills/y", cx / "y")
    os.symlink("../../.claude/skills/hyperframes", cx / "hf")
    yaz(cx / "playwright/SKILL.md")
    yaz(cx / ".system/x")
    for d in (".gemini/skills", ".gemini/antigravity-cli/skills", ".cursor/skills", ".copilot/skills"):
        (ev / d).mkdir(parents=True)
    yaz(ev / ".cursor/skills-cursor/v/SKILL.md")
    yaz(ev / ".claude/commands/a.md", "komut")
    yaz(ev / ".claude/agents/b.md", "ajan")
    yaz(ev / ".claude/CLAUDE.md", "talimat FAKE_SECRET_AAA")
    yaz(ev / ".gemini/GEMINI.md", "gemini")
    yaz(ev / ".zshenv", "export HYPERFRAMES_SKIP_SKILLS=1\n")
    yaz(ev / ".zshrc", "export FAKE_API_KEY=SECRETVALUE123\nexport HYPERFRAMES_SKIP_SKILLS=1  # not\n")
    yaz(ev / ".claude/settings.json", json.dumps({"env": {"HYPERFRAMES_SKIP_SKILLS": "1", "TOKEN": "SECRETVALUE456"}}))
    return ev, kok / "taban.json"


def calistir(ev, taban, *args, env_ekle=None, ev_ver=True):
    assert str(ev).startswith(str(TMP)) or not ev_ver, "gerçek ev kullanılamaz"
    kom = [sys.executable, str(ARAC)]
    if ev_ver:
        kom += ["--ev", str(ev)]
    kom += ["--taban", str(taban), "--kart", str(KART)]
    if not any(a in ("--rapor", "--rapor-yok", "--taban-yaz", "--plan", "--yedek-dogrula", "--ozet-json") for a in args):
        kom.append("--rapor-yok")
    env = {**os.environ}
    env.pop("SKILL_BEKCI_EV", None)
    env.update(env_ekle or {})
    return subprocess.run(kom + list(args), capture_output=True, text=True, env=env)


def taban_yaz(ev, taban, *ek):
    r = calistir(ev, taban, "--taban-yaz", "--evet", "--tarih", TARIH, *ek)
    assert r.returncode == 0, r.stdout + r.stderr
    return r


def durum(r):
    m = re.search(r"bekçisi: (\S+)", r.stdout)
    return m.group(1) if m else None


def anlik(ev):
    s = {}
    for k, dirs, files in os.walk(ev, followlinks=False):
        for ad in dirs + files:
            p = os.path.join(k, ad)
            st = os.lstat(p)
            s[p] = (st.st_size, int(st.st_mtime), os.readlink(p) if os.path.islink(p) else None)
    return s


def taban_oku(t):
    return json.loads(Path(t).read_text(encoding="utf-8"))


def satir_var(r, parca):
    return any(parca in s for s in r.stdout.splitlines())


# 1
r = subprocess.run([sys.executable, str(ARAC), "--help"], capture_output=True, text=True)
test("1 --help", r.returncode == 0 and all(x in r.stdout for x in ("--taban-yaz", "--plan", "--ozet-json", "--ev", "--kart", "--kalacak", "--yedek-dogrula", "--siki")))

# 2
ev, tb = ev_kur()
r = calistir(ev, tb)
test("2 taban yok: dikkat, TABAN YOK, çıkış 0", durum(r) == "DİKKAT" and "TABAN YOK" in r.stdout and r.returncode == 0)
test("2b --siki ile de 0", calistir(ev, tb, "--siki").returncode == 0)
test("2c tabansız ozet-json karar_bekleyen onay ister", "onay" in calistir(ev, tb, "--ozet-json").stdout)

# 3
r = calistir(ev, tb, "--taban-yaz")
test("3 kuru çalışma dosya yazmaz", not tb.exists() and "Kuru çalışma" in r.stdout and r.returncode == 0)

# 4
taban_yaz(ev, tb)
ham = tb.read_text(encoding="utf-8")
T = taban_oku(tb)
yollar = [g["yol"] for g in T["girdiler"]]
test("4 taban geçerli, sıralı, ~/ yollu, sırsız, kirik yok",
     T["surum"] == 1 and yollar == sorted(yollar) and all(y.startswith("~/") for y in yollar) and str(ev) not in ham
     and "kirik" not in ham and not any(s in ham for s in SIRLAR), ham[:200])
G = {g["yol"]: g for g in T["girdiler"]}

# 5
test("5 sahipler", G["~/.claude/skills/x"]["sahip"] == "openmontage" and G["~/.claude/skills/y"]["sahip"] == "hyperframes"
     and G["~/.agents/skills/y"]["sahip"] == "hyperframes" and G["~/.agents/skills/microsoft-foundry"]["sahip"] == "skills aracı"
     and G["~/.claude/skills/design-dna"]["sahip"] == "kullanıcı" and G["~/.claude/skills/mystery"]["sahip"] == "bilinmiyor"
     and G["~/.claude/skills/hyperframes"]["sahip"] == "hyperframes", str({k: v["sahip"] for k, v in G.items()}))

# 6
test("6 durumlar", all(G[y]["durum"] == "boşaltılacak" for y in ("~/.claude/skills/x", "~/.claude/skills/hyperframes", "~/.agents/skills/y", "~/.agents/.skill-lock.json", "~/.codex/skills/y"))
     and all(G[y]["durum"] == "kalacak" for y in ("~/.claude/skills/.trash", "~/.codex/skills/playwright", "~/.claude/commands/a.md", "~/.claude/agents/b.md", "~/.claude/CLAUDE.md", "~/.gemini/GEMINI.md")))

# 7
test("7 satıcı girdileri izinli, satırlarda yok", {i["yol"] for i in T["izinli"]} >= {"~/.claude/skills/synced", "~/.codex/skills/.system", "~/.cursor/skills-cursor"}
     and not any("/synced" in y or "/.system" in y or "skills-cursor" in y for y in yollar))
yaz(ev / ".claude/skills/synced/a/b/yeni.md")
yaz(ev / ".codex/skills/.system/yeni.md")
r = calistir(ev, tb)
test("7b izinli içine yazı rapor satırı üretmez", durum(r) == "TEMİZ" and "yeni.md" not in r.stdout and "synced" not in r.stdout, r.stdout)

# 8
once = tb.read_bytes()
r = calistir(ev, tb, "--taban-yaz", "--evet")
test("8 ikinci yazım reddedilir", r.returncode == 1 and "--yenile" in r.stdout and tb.read_bytes() == once)

# 9
for ek in ([], ["--siki"]):
    r = calistir(ev, tb, *ek)
    test(f"9 taban sonrası temiz {ek}", durum(r) == "TEMİZ" and r.returncode == 0 and "boşaltılacak girdi duruyor" in r.stdout, r.stdout)

# 10
(ev / ".agents/skills/yeniskill").mkdir()
r = calistir(ev, tb)
test("10 YENİ: sorun, çıkış 0", durum(r) == "SORUN" and satir_var(r, "YENİ      ~/.agents/skills/yeniskill") and r.returncode == 0, r.stdout)
test("10b --siki çıkış 1", calistir(ev, tb, "--siki").returncode == 1)
shutil.rmtree(ev / ".agents/skills/yeniskill")

# 11
shutil.rmtree(ev / ".agents/skills/microsoft-foundry")
r = calistir(ev, tb)
test("11 boşaltılan: temiz", durum(r) == "TEMİZ" and "boşaltılan: 1" in r.stdout, r.stdout)
os.remove(ev / ".claude/commands/a.md")
r = calistir(ev, tb)
test("11b kalacak komut KAYIP: dikkat", durum(r) == "DİKKAT" and satir_var(r, "KAYIP     ~/.claude/commands/a.md"), r.stdout)

# 12
ev, tb = ev_kur()
taban_yaz(ev, tb)
os.remove(ev / ".claude/skills/x")
os.symlink("/baska/yer", ev / ".claude/skills/x")
yaz(ev / ".claude/skills/design-dna/yeni.md")
r = calistir(ev, tb)
test("12 hedef ve dosya sayısı DEĞİŞTİ", durum(r) == "DİKKAT" and satir_var(r, "DEĞİŞTİ   ~/.claude/skills/x (hedef:") and satir_var(r, "DEĞİŞTİ   ~/.claude/skills/design-dna (dosya sayısı: 1 -> 2)"), r.stdout)

# 13
ev, tb = ev_kur()
yaz(ev / "hedef.txt")
os.symlink(str(ev / "hedef.txt"), ev / ".claude/commands/lnk.md")
taban_yaz(ev, tb)
os.remove(ev / "hedef.txt")
shutil.rmtree(ev / ".openmontage/.agents/skills/x")
r = calistir(ev, tb)
test("13 kalacak yuvada KIRIK BAĞ, boşaltılacakta yalnız sayı", satir_var(r, "KIRIK BAĞ ~/.claude/commands/lnk.md") and not satir_var(r, "KIRIK BAĞ ~/.claude/skills/x")
     and "kırık bağ (boşaltılacak): 1" in r.stdout and durum(r) == "DİKKAT", r.stdout)

# 14
ev, tb = ev_kur()
taban_yaz(ev, tb)
(ev / ".gemini/antigravity/skills").mkdir(parents=True)
r = calistir(ev, tb)
test("14 boş YENİ KLASÖR: dikkat", durum(r) == "DİKKAT" and satir_var(r, "YENİ KLASÖR ~/.gemini/antigravity/skills (0 girdi)"), r.stdout)
yaz(ev / ".gemini/antigravity/skills/c/SKILL.md")
(ev / ".gemini/antigravity-2/skills").mkdir(parents=True)
r = calistir(ev, tb)
test("14b dolu YENİ KLASÖR: sorun; glob yenisini bulur", durum(r) == "SORUN" and satir_var(r, "YENİ KLASÖR ~/.gemini/antigravity-2/skills"), r.stdout)
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
test("14c karar_bekleyen rehber/14 cümlesi", any(k == "Yeni bir yapay zeka aracı klasörü göründü (rehber/14): ~/.gemini/antigravity/skills — araç ise ek_klasorler'e eklensin mi, değilse izinli/yoksay mı?" for k in j["karar_bekleyen"]), str(j))

# 15
ev, tb = ev_kur()
taban_yaz(ev, tb)
yaz(ev / ".foo/skills/x/a.md")
yaz(ev / ".openmontage/skills/yeni/a.md")
r = calistir(ev, tb)
test("15 keşif: .foo bulunur, .openmontage yoksayılır", satir_var(r, "YENİ KLASÖR ~/.foo/skills") and "openmontage/skills" not in r.stdout, r.stdout)

# 16
ev, tb = ev_kur()
taban_yaz(ev, tb)
(ev / ".windsurf/skills").mkdir(parents=True)
T = taban_oku(tb)
T["ek_klasorler"] = [{"ad": "windsurf", "yol": "~/.windsurf/skills", "tur": "skill"}]
tb.write_text(json.dumps(T), encoding="utf-8")
r = calistir(ev, tb, "--taban-yaz", "--evet", "--yenile", "--tarih", TARIH)
yaz(ev / ".windsurf/skills/w/SKILL.md")
r2 = calistir(ev, tb)
test("16 ek_klasorler izlenir, yenile listeyi korur", r.returncode == 0 and taban_oku(tb)["ek_klasorler"][0]["ad"] == "windsurf" and satir_var(r2, "YENİ      ~/.windsurf/skills/w"), r.stdout + r2.stdout)

# 17 ortam
def ortam(duzen):
    e, t = ev_kur()
    duzen(e)
    return calistir(e, t)


r = ortam(lambda e: None)
test("17 üçü de var", "3 dosyanın 3'ünde var." in r.stdout)
r = ortam(lambda e: yaz(e / ".zshenv", "# export HYPERFRAMES_SKIP_SKILLS=1\nFOO=1\n"))
test("17b yorum satırı sayılmaz", "2'sinde var" in r.stdout and "EKSİK: ~/.zshenv (satır yok)" in r.stdout and "SORUN" in r.stdout, r.stdout)
r = ortam(lambda e: yaz(e / ".zshenv", "export HYPERFRAMES_SKIP_SKILLS=0\n"))
test("17c değer 0 geçersiz", "~/.zshenv (geçersiz değer)" in r.stdout and "SORUN" in r.stdout)
r = ortam(lambda e: yaz(e / ".claude/settings.json", json.dumps({"env": {"TOKEN": "SECRETVALUE456"}})))
test("17d settings anahtarsız sorun", "~/.claude/settings.json (satır yok)" in r.stdout and "SORUN" in r.stdout and "SECRETVALUE456" not in r.stdout + r.stderr)
r = ortam(lambda e: yaz(e / ".claude/settings.json", "{bozuk"))
test("17e bozuk JSON okunamadı", "~/.claude/settings.json (okunamadı)" in r.stdout and "SORUN" in r.stdout)
r = ortam(lambda e: os.remove(e / ".zshenv"))
test("17f dosya yok", "~/.zshenv (dosya yok)" in r.stdout and "SORUN" in r.stdout)


def zshrc_klasor(e):
    os.remove(e / ".zshrc")
    (e / ".zshrc").mkdir()


r = ortam(zshrc_klasor)
test("17g klasör: okunamadı, OS metni sızmaz", "~/.zshrc (okunamadı)" in r.stdout and "Errno" not in r.stdout + r.stderr and "directory" not in (r.stdout + r.stderr).lower())
r = ortam(lambda e: yaz(e / ".zshrc", ("export FAKE_API_KEY=SECRETVALUE123\n" + "a" * 299 + "\n") * 5000 + "export HYPERFRAMES_SKIP_SKILLS=1\n"))
test("17h 1 MB sınırı", "~/.zshrc (satır yok)" in r.stdout and "SECRETVALUE123" not in r.stdout + r.stderr, r.stdout[:300])
r = ortam(lambda e: yaz(e / ".zshrc", 'export HYPERFRAMES_SKIP_SKILLS="1"\n'))
test("17i tırnaklı değer geçerli", "3 dosyanın 3'ünde var." in r.stdout)

# 18 sızıntı
ev, tb = ev_kur()
rapor = TMP / "rapor18.md"
tum = ""
for args in ([], ["--ayrinti"], ["--ozet-json"], ["--taban-yaz"], ["--rapor", str(rapor)]):
    r = calistir(ev, tb, *args)
    tum += r.stdout + r.stderr
taban_yaz(ev, tb)
for args in ([], ["--ayrinti"], ["--ozet-json"], ["--rapor", str(rapor)], ["--plan", "3"], ["--plan", "4"], ["--plan", "5a"], ["--plan", "5b"], ["--plan", "6"], ["--plan", "7"], ["--yedek-dogrula", str(TMP / "yok-yedek")]):
    r = calistir(ev, tb, *args)
    tum += r.stdout + r.stderr
tum += tb.read_text(encoding="utf-8") + (rapor.read_text(encoding="utf-8") if rapor.exists() else "")
test("18 sırlar hiçbir çıktıda yok", not any(s in tum for s in SIRLAR) and rapor.exists(), [s for s in SIRLAR if s in tum])

# 19 ozet-json
ev, tb = ev_kur()
taban_yaz(ev, tb)
bos = TMP / "bos-notlar"
r = calistir(ev, tb, "--ozet-json")
try:
    d = json.loads(r.stdout)
    tek = len(r.stdout.strip().splitlines()) == 1
except ValueError:
    d, tek = {}, False
test("19 ozet-json tek nesne", tek and set(d) == {"arac", "durum", "satirlar", "karar_bekleyen"} and d["arac"] == "genel-bekci"
     and d["durum"] in ("temiz", "dikkat", "sorun") and r.stderr == "" and len(d["satirlar"]) <= 12, r.stdout)
ev2, tb2 = ev_kur()
for i in range(20):
    (ev2 / f".agents/skills/yeni{i}").mkdir()
taban_yaz(ev2, tb2)
for i in range(20):
    (ev2 / f".agents/skills/yeniB{i}").mkdir()
d = json.loads(calistir(ev2, tb2, "--ozet-json").stdout)
test("19b 12 satır sınırı", len(d["satirlar"]) == 12 and d["satirlar"][-1].startswith("... ve") and len(d["karar_bekleyen"]) <= 10, str(d["satirlar"]))
test("19c ozet-json + plan = 2", calistir(ev, tb, "--ozet-json", "--plan", "3").returncode == 2)

# 20 talimat/komut/ajan: yalnız var
ev, tb = ev_kur()
taban_yaz(ev, tb)
satir = [g for g in taban_oku(tb)["girdiler"] if g["yol"] in ("~/.claude/commands/a.md", "~/.claude/agents/b.md", "~/.claude/CLAUDE.md")]
test("20 satırlarda bayt/mtime yok", all(set(g) == {"yol", "bolge", "tur", "sahip", "durum"} for g in satir), str(satir))
yaz(ev / ".claude/CLAUDE.md", "çok daha uzun yeni içerik " * 50)
yaz(ev / ".claude/commands/a.md", "yeni " * 100)
os.utime(ev / ".claude/commands/a.md", (1, 1))
r = calistir(ev, tb)
test("20b içerik değişimi olay değil", durum(r) == "TEMİZ" and "DEĞİŞTİ" not in r.stdout, r.stdout)
os.remove(ev / ".claude/agents/b.md")
yaz(ev / ".claude/commands/yeni.md")
r = calistir(ev, tb)
test("20c KAYIP ve YENİ dikkat", durum(r) == "DİKKAT" and satir_var(r, "KAYIP     ~/.claude/agents/b.md") and satir_var(r, "YENİ      ~/.claude/commands/yeni.md"), r.stdout)
ev, tb = ev_kur()
taban_yaz(ev, tb)
yaz(ev / ".agents/.skill-lock.json", (ev / ".agents/.skill-lock.json").read_text(encoding="utf-8") + " " * 10)
r = calistir(ev, tb)
test("20d kilit boyutu DEĞİŞTİ", durum(r) == "DİKKAT" and satir_var(r, "DEĞİŞTİ   ~/.agents/.skill-lock.json (boyut:"), r.stdout)
ev, tb = ev_kur()
taban_yaz(ev, tb)
os.remove(ev / ".claude/commands/a.md")
os.symlink(str(ev / ".claude/agents/b.md"), ev / ".claude/commands/a.md")
r = calistir(ev, tb)
test("20e dosya yerine bağ: tür DEĞİŞTİ", satir_var(r, "DEĞİŞTİ   ~/.claude/commands/a.md (tür: dosya -> bag)"), r.stdout)

# 21 bozuk taban
ev, tb = ev_kur()
tb.write_text("{", encoding="utf-8")
r = calistir(ev, tb)
test("21 bozuk taban: sorun", durum(r) == "SORUN" and "TABAN OKUNAMADI" in r.stdout and r.returncode == 0)
tb.write_text(json.dumps({"surum": 2, "girdiler": []}), encoding="utf-8")
r = calistir(ev, tb)
test("21b bilinmeyen sürüm", durum(r) == "SORUN" and "taban sürümü desteklenmiyor" in r.stdout)
tb.unlink()
taban_yaz(ev, tb)
T = taban_oku(tb)
T["girdiler"][0]["sahip"] = "uzaylı"
tb.write_text(json.dumps(T), encoding="utf-8")
r = calistir(ev, tb)
test("21c geçersiz sahip: yolu söyler", durum(r) == "SORUN" and T["girdiler"][0]["yol"] in r.stdout and "sahip geçersiz" in r.stdout, r.stdout)

# 22 yenile
ev, tb = ev_kur()
taban_yaz(ev, tb)
T = taban_oku(tb)
os.remove(ev / ".claude/commands/a.md")                      # kalacak, kayboldu
shutil.rmtree(ev / ".agents/skills/microsoft-foundry")        # boşaltılacak, kayboldu
yaz(ev / ".claude/skills/yenisi/SKILL.md")                   # yeni
r = calistir(ev, tb, "--taban-yaz", "--evet", "--yenile", "--tarih", TARIH)
T2 = taban_oku(tb)
G2 = {g["yol"]: g for g in T2["girdiler"]}
test("22 yenile: kabul edildi/düşürüldü, rapor temiz", r.returncode == 0 and "kabul edildi: ~/.claude/skills/yenisi" in r.stdout
     and "düşürüldü (kalacak idi): ~/.claude/commands/a.md" in r.stdout and "TEMİZ" in r.stdout and "~/.agents/skills/microsoft-foundry" not in G2
     and G2["~/.claude/skills/yenisi"]["durum"] == "kalacak" and G2["~/.claude/skills/x"]["durum"] == "boşaltılacak"
     and T2["izinli"] == T["izinli"] and T2["gecmis"][-1]["islem"] == "yenile", r.stdout)
test("22b yenileme sonrası rapor temiz", durum(calistir(ev, tb)) == "TEMİZ")

# 23 yazma koruması
ev, tb = ev_kur()
hedef = ev / ".claude/skills/x.json"
r = calistir(ev, hedef, "--taban-yaz", "--evet")
test("23 izlenen klasöre yazma reddi", r.returncode == 1 and not hedef.exists() and "Yazma reddedildi" in r.stdout)
r = calistir(ev, tb, "--rapor", str(ev / ".agents/skills/rapor.md"))
test("23b rapor da izlenen klasöre yazılmaz", not (ev / ".agents/skills/rapor.md").exists())

# 24 plan 3
ev, tb = ev_kur()
taban_yaz(ev, tb)
once = anlik(ev)
r = calistir(ev, tb, "--plan", "3", "--tarih", "2026-12-01")
sat = r.stdout.splitlines()
test("24 plan 3 içeriği", r.returncode == 0 and "ONAY GEREKİR" in r.stdout and "readlink" in r.stdout and "genel-klasorler-2026-12-01" in r.stdout
     and "ln -s" in r.stdout and sum(1 for s in sat if s.startswith("rm -- ")) == 2 and "playwright" not in r.stdout and ".system" not in r.stdout
     and "hiçbir komutu kendisi çalıştırmaz" in r.stdout, r.stdout)
test("24b plan hiçbir şeyi değiştirmez", anlik(ev) == once)

# 25
r = calistir(ev, tb, "--plan", "4")
test("25 plan 4 adım 3 bitmeden durur", "ÖNCEKİ ADIM BİTMEMİŞ: adım 3 (2 girdi)" in r.stdout and "rm --" not in r.stdout and r.returncode == 0)
test("25b --siki ile çıkış 1", calistir(ev, tb, "--plan", "4", "--siki").returncode == 1)

# 26
r = calistir(ev, tb, "--plan", "5a")
test("26 bağımlı bağ plan 5a'yı durdurur", "BAĞIMLI: ~/.codex/skills/hf -> ~/.claude/skills/hyperframes" in r.stdout and "mv --" not in r.stdout, r.stdout)

# 27 adım adım (elle simülasyon)
planlar = {}
for a in ("3", "4", "5a", "5b", "6", "7"):
    planlar[a] = ""
r3 = calistir(ev, tb, "--plan", "3").stdout
for n in ("y", "hf"):
    os.remove(ev / ".codex/skills" / n)
r4 = calistir(ev, tb, "--plan", "4").stdout
rm4 = [s for s in r4.splitlines() if s.startswith("rm -- ")]
test("27 plan 4: yalnız claude bağları", len(rm4) == 2 and not any(x in r4 for x in ("synced", "hyperframes'", "design-dna", "mystery")) and "rm -- " + "'" + str(ev / ".claude/skills/hyperframes") not in r4, r4)
for n in ("x", "y"):
    os.remove(ev / ".claude/skills" / n)
r5a = calistir(ev, tb, "--plan", "5a").stdout
mv5a = [s for s in r5a.splitlines() if s.startswith("mv -- ") and "claude-skills" in s and ".claude/skills" in s]
test("27b plan 5a: yalnız hyperframes sahipli klasörler, mv", len(mv5a) == 2 and all(("hyperframes" in s or "cardskill" in s) for s in mv5a) and "FARKLI DİSK" in r5a, r5a)
shutil.rmtree(ev / ".claude/skills/hyperframes")
shutil.rmtree(ev / ".claude/skills/cardskill")
r5b = calistir(ev, tb, "--plan", "5b").stdout
mv5b = [x for x in r5b.splitlines() if x.startswith("mv -- ") and ".claude/skills" in x]
test("27c plan 5b: yalnız diğer klasörler", len(mv5b) == 2 and any("design-dna" in x for x in mv5b) and any("mystery" in x for x in mv5b), r5b)
shutil.rmtree(ev / ".claude/skills/design-dna")
shutil.rmtree(ev / ".claude/skills/mystery")
r6 = calistir(ev, tb, "--plan", "6").stdout
ic = [i for i, s in enumerate(r6.splitlines()) if s.startswith("cp -p")]
im = [i for i, s in enumerate(r6.splitlines()) if s.startswith("mv --") and "skill-lock.json" in s]
test("27d plan 6: kilit önce cp -p sonra mv", len(ic) == 1 and len(im) == 1 and ic[0] < im[0], r6)
test("27e hiçbir planda rm -rf yok", all("rm -rf" not in x and "rm -r " not in x for x in (r3, r4, r5a, r5b, r6, calistir(ev, tb, "--plan", "7").stdout)))
for p in (r3, r4, r5a, r5b, r6):
    for s in p.splitlines():
        if s.startswith("#"):
            continue
        disi = re.sub(r"'[^']*'|\"[^\"]*\"", "", s)
        if re.search(r"[*?]", disi):
            test("33c plan satırında tırnaksız glob yok", False, s)
            break
    else:
        continue
    break
else:
    test("33c plan satırında tırnaksız glob yok", True)
test("33c2 yedek satırları tek tek yol adı verir", all("*" not in s for s in r4.splitlines() if s.startswith("printf")) and len([s for s in r4.splitlines() if s.startswith("printf")]) == 2)

# 28
ev, tb = ev_kur()
r = calistir(ev, tb, "--plan", "3")
test("28 tabansız plan: DURDUR, komut yok", "DURDUR" in r.stdout and "rm --" not in r.stdout and r.returncode == 0)
r1 = calistir(ev, tb, "--plan", "1")
r2 = calistir(ev, tb, "--plan", "2")
test("28b plan 1 ve 2 elle", "Bu adım elle" in r1.stdout and "Bu adım elle" in r2.stdout and r1.returncode == 0)

# 29 yedek doğrula
ev, tb = ev_kur()
taban_yaz(ev, tb)
yedek = TMP / "yedek29"
(yedek / "claude-skills").mkdir(parents=True)
tsvs = {"codex": [], "claude": []}
for b, d in (("codex", ev / ".codex/skills"), ("claude", ev / ".claude/skills")):
    for n in sorted(os.listdir(d)):
        if os.path.islink(d / n):
            tsvs[b].append(f"{d / n}\t{os.readlink(d / n)}")
            os.remove(d / n)
    (yedek / f"bag-listesi-{b}.tsv").write_text("\n".join(tsvs[b]) + "\n", encoding="utf-8")
shutil.move(str(ev / ".claude/skills/hyperframes"), str(yedek / "claude-skills/hyperframes"))
r = calistir(ev, tb, "--yedek-dogrula", str(yedek))
test("29 yedek tamam", r.returncode == 0 and "yedekte tamam: 5" in r.stdout and "YEDEKTE YOK" not in r.stdout, r.stdout)
yaz(yedek / "claude-skills/hyperframes/ekstra.md")
r = calistir(ev, tb, "--yedek-dogrula", str(yedek))
test("29b değişen yedek FARKLI", r.returncode == 1 and "FARKLI: ~/.claude/skills/hyperframes" in r.stdout)
os.remove(yedek / "claude-skills/hyperframes/ekstra.md")
satirlar = (yedek / "bag-listesi-claude.tsv").read_text(encoding="utf-8").splitlines()
(yedek / "bag-listesi-claude.tsv").write_text("\n".join(satirlar[1:]) + "\n", encoding="utf-8")
r = calistir(ev, tb, "--yedek-dogrula", str(yedek))
test("29c eksik tsv satırı YEDEKTE YOK", r.returncode == 1 and "YEDEKTE YOK" in r.stdout)
test("29d olmayan klasör çıkış 1", calistir(ev, tb, "--yedek-dogrula", str(TMP / "hic-yok")).returncode == 1)

# 30 hiçbir şey yazılmaz
ev, tb = ev_kur()
taban_yaz(ev, tb)
once = anlik(ev)
for args in ([], ["--ayrinti"], ["--siki"], ["--ozet-json"], ["--taban-yaz"], ["--plan", "3"], ["--plan", "7"], ["--yedek-dogrula", str(TMP)], ["--rapor", str(TMP / "r30.md")]):
    calistir(ev, tb, *args)
tmpler = [p for p in tb.parent.iterdir() if p.name.endswith(".tmp")]
test("30 sahte ev değişmedi, .tmp kalmadı", anlik(ev) == once and not tmpler)

# 31 SKILL_BEKCI_EV
ev, tb = ev_kur()
r = calistir(ev, tb, env_ekle={"SKILL_BEKCI_EV": str(ev)}, ev_ver=False)
test("31 ortam değişkeni kullanılır", "3 dosyanın 3'ünde var." in r.stdout, r.stdout)
r = calistir(ev, tb, env_ekle={"SKILL_BEKCI_EV": str(TMP / "yok-ev")})
test("31b --ev kazanır", "3 dosyanın 3'ünde var." in r.stdout)

# 32 belirlenimcilik
ev, tb = ev_kur()
taban_yaz(ev, tb)
a1 = taban_oku(tb)
tb.unlink()
taban_yaz(ev, tb)
a2 = taban_oku(tb)
for a in (a1, a2):
    a.pop("yazildi"), a.pop("gecmis")
test("32 iki yazım aynı", a1 == a2)
rap = TMP / "r32.md"
calistir(ev, tb, "--rapor", str(rap))
ilk = rap.read_text(encoding="utf-8")
rap.write_text(re.sub(r"\d{4}-\d{2}-\d{2}", "2000-01-01", ilk, count=1), encoding="utf-8")
calistir(ev, tb, "--rapor", str(rap))
test("32b yalnız tarih farkıysa rapor yeniden yazılmaz", "2000-01-01" in rap.read_text(encoding="utf-8"))

# 33a
ev, tb = ev_kur()
taban_yaz(ev, tb)
G = {g["yol"]: g for g in taban_oku(tb)["girdiler"]}
ham = tb.read_text(encoding="utf-8")
test("33a hf-skills yerel kaynak hyperframes, diğeri skills aracı; kaynak yazılmaz", G["~/.agents/skills/localhf"]["sahip"] == "hyperframes"
     and G["~/.agents/skills/localother"]["sahip"] == "skills aracı" and G["~/.claude/skills/cardskill"]["sahip"] == "hyperframes" and "SECRETPROJ" not in ham)

# 33b --kalacak
ev, tb = ev_kur()
taban_yaz(ev, tb)
once = tb.read_bytes()
r = calistir(ev, tb, "--taban-yaz", "--yenile", "--kalacak", "~/.claude/skills/hyperframes")
test("33b kalacak --evet olmadan değişmez", tb.read_bytes() == once and "kalacak yapıldı" in r.stdout)
r = calistir(ev, tb, "--taban-yaz", "--yenile", "--evet", "--kalacak", "~/.claude/skills/hyperframes")
test("33b2 kalacak yapıldı", r.returncode == 0 and "kalacak yapıldı: ~/.claude/skills/hyperframes" in r.stdout and
     {g["yol"]: g for g in taban_oku(tb)["girdiler"]}["~/.claude/skills/hyperframes"]["durum"] == "kalacak")
r = calistir(ev, tb, "--taban-yaz", "--yenile", "--evet", "--kalacak", "~/.claude/skills/yok-boyle")
test("33b3 bilinmeyen yol: Tabanda yok", r.returncode == 1 and "Tabanda yok" in r.stdout)
for n in ("y", "hf"):
    os.remove(ev / ".codex/skills" / n)
for n in ("x", "y"):
    os.remove(ev / ".claude/skills" / n)
r = calistir(ev, tb, "--plan", "5a")
test("33b4 kalacak girdi plandan çıkar", "ADIM 5a" in r.stdout and "hyperframes" not in "\n".join(s for s in r.stdout.splitlines() if s.startswith("mv --")), r.stdout)

# 33
ev, tb = ev_kur()
os.makedirs(ev / ".agents/skills/y/__pycache__", exist_ok=True)
yaz(ev / ".agents/skills/y/__pycache__/a.pyc")
taban_yaz(ev, tb)
r = calistir(ev, tb, "--ayrinti")
test("33 .DS_Store ve __pycache__ satırlarda yok", ".DS_Store" not in r.stdout + (tb.read_text(encoding="utf-8")) and "__pycache__" not in r.stdout)

# 34
r = calistir(TMP / "olmayan-ev", TMP / "t34.json", "--ozet-json")
try:
    d = json.loads(r.stdout)
    ok = len(r.stdout.strip().splitlines()) == 1 and d["durum"] == "sorun" and r.returncode == 0
except ValueError:
    ok = False
test("34 olmayan ev: tek JSON, sorun, çıkış 0", ok, r.stdout)

# 35 modül olarak içe aktarma
spec = importlib.util.spec_from_file_location("genel_bekci", ARAC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
test("35 modül yüklenir, ortam regex'i tek sabit desen", mod.ANAHTAR_RE.match("export HYPERFRAMES_SKIP_SKILLS=1") and not mod.ANAHTAR_RE.match("#export HYPERFRAMES_SKIP_SKILLS=1"))

# 37 plan: yedekte aynı ad varsa mv öncesi durdurma denetimi
test("37 plan 5b: mv öncesi yedekte aynı ad denetimi", "mv -- " in r5b and "YEDEKTE AYNI AD VAR" in r5b)

# 38-43 bilinen yazıcılar (BILINEN_YAZICILAR) ve kabuk ipucu
def karar_satiri(j, yol):
    return next((k for k in j["karar_bekleyen"] if k.startswith(f"Yeni girdi {yol} ")), "")


FOUNDRY = "yazan: VS Code Foundry Toolkit uzantısı; durdurmak: VS Code ayarı windowsaistudio.autoCheckFoundrySkill=false"
COPILOT = "yazan: VS Code GitHub Copilot for Azure uzantısı; durdurmak: kurulum bildiriminde \"Don't Ask Again\" (ayarı yok)"
AZ = "microsoft/azure-skills"

# 38 kilit kaynağı azure-skills: microsoft-foundry -> Foundry Toolkit, diğer adlar -> Copilot for Azure, tanınmayan -> eski metin
ev, tb = ev_kur()
shutil.rmtree(ev / ".agents/skills/microsoft-foundry")
yaz(ev / ".agents/.skill-lock.json", json.dumps({"skills": {
    "y": {"source": "heygen-com/hyperframes", "sourceType": "github"},
    "localhf": {"source": "/Users/x/SECRETPROJ/hf-skills/localhf", "sourceType": "local"},
    "localother": {"source": "/Users/x/SECRETPROJ/baska/localother", "sourceType": "local"},
    "microsoft-foundry": {"source": AZ, "sourceType": "github"},
    "azure-prepare": {"source": AZ, "sourceType": "github"},
    "azure-deploy": {"source": "https://github.com/SECRETPROJ/../microsoft/azure-skills.git", "sourceType": "git"},
    "azure-benzeri": {"source": "microsoft/azure-skills-extra", "sourceType": "github"}}}))
taban_yaz(ev, tb)
for n in ("microsoft-foundry", "azure-prepare", "azure-deploy", "azure-benzeri", "tanimsiz"):
    yaz(ev / ".agents/skills" / n / "SKILL.md")
os.symlink("../../.agents/skills/azure-prepare", ev / ".claude/skills/azure-prepare")
r = calistir(ev, tb)
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
ra = calistir(ev, tb, "--ayrinti")
kf = karar_satiri(j, "~/.agents/skills/microsoft-foundry")
test("38 microsoft-foundry + azure-skills kilidi: Foundry ipucu, sahip aynı",
     kf == mod.KARAR_YENI.format(y="~/.agents/skills/microsoft-foundry", s="skills aracı; " + FOUNDRY)
     and satir_var(r, "YENİ      ~/.agents/skills/microsoft-foundry (klasör, sahip: skills aracı)") and "Copilot" not in kf, kf)
kp = karar_satiri(j, "~/.agents/skills/azure-prepare")
test("38b başka azure-skills adı: Copilot for Azure ipucu", kp == mod.KARAR_YENI.format(y="~/.agents/skills/azure-prepare", s="skills aracı; " + COPILOT), kp)
test("38c URL biçimli kaynak da tanınır; benzer ad (azure-skills-extra) tanınmaz",
     COPILOT in karar_satiri(j, "~/.agents/skills/azure-deploy")
     and karar_satiri(j, "~/.agents/skills/azure-benzeri") == mod.KARAR_YENI.format(y="~/.agents/skills/azure-benzeri", s="skills aracı"), str(j["karar_bekleyen"]))
test("38d ~/.claude/skills aynası (bağ) hedef adıyla tanınır", COPILOT in karar_satiri(j, "~/.claude/skills/azure-prepare"), str(j["karar_bekleyen"]))
test("38e tanınmayan girdi: karar metni eskisiyle aynı", karar_satiri(j, "~/.agents/skills/tanimsiz") == mod.KARAR_YENI.format(y="~/.agents/skills/tanimsiz", s="bilinmiyor"))
test("38f ozet-json biçimi aynı, karar satırları 300 karakteri aşmaz", set(j) == {"arac", "durum", "satirlar", "karar_bekleyen"} and j["durum"] == "sorun"
     and all(len(k) <= 300 for k in j["karar_bekleyen"]), str(j))
test("38g --ayrinti kimlik ve kanıt yerini verir; düz raporda kanıt yok",
     "ms-windows-ai-studio.windows-ai-studio" in ra.stdout and "Foundry Toolkit.log" in ra.stdout and "@azure.log" in ra.stdout
     and "kanıt:" not in r.stdout, ra.stdout)
test("38h kaynak metni hiçbir çıktıda yok", "SECRETPROJ" not in r.stdout + ra.stdout + json.dumps(j, ensure_ascii=False) + r.stderr + ra.stderr)
calistir(ev, tb, "--taban-yaz", "--yenile", "--evet", "--tarih", TARIH)
ham = tb.read_text(encoding="utf-8")
test("38i yazıcı bilgisi tabana yazılmaz", "yazan" not in ham and "_yazici" not in ham and "SECRETPROJ" not in ham and durum(calistir(ev, tb)) == "TEMİZ")

# 39 kilit dosyası yok: klasör adı microsoft-foundry ise yine Foundry; başka ad eski metin
ev, tb = ev_kur()
shutil.rmtree(ev / ".agents/skills/microsoft-foundry")
os.remove(ev / ".agents/.skill-lock.json")
taban_yaz(ev, tb)
yaz(ev / ".agents/skills/microsoft-foundry/SKILL.md")
yaz(ev / ".agents/skills/azure-prepare/SKILL.md")
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
test("39 kilitsiz microsoft-foundry: Foundry ipucu", karar_satiri(j, "~/.agents/skills/microsoft-foundry")
     == mod.KARAR_YENI.format(y="~/.agents/skills/microsoft-foundry", s="bilinmiyor; " + FOUNDRY), str(j["karar_bekleyen"]))
test("39b kilitsiz ve manifestsiz azure adı: eski metin", karar_satiri(j, "~/.agents/skills/azure-prepare")
     == mod.KARAR_YENI.format(y="~/.agents/skills/azure-prepare", s="bilinmiyor"))

# 40 kilit okunamaz: çökme yok; ad eşleşmesi sürer, kaynak eşleşmesi yok
for bozuk in ("{bozuk", "[1, 2]", None):
    ev, tb = ev_kur()
    shutil.rmtree(ev / ".agents/skills/microsoft-foundry")
    taban_yaz(ev, tb)
    os.remove(ev / ".agents/.skill-lock.json")
    if bozuk is None:
        (ev / ".agents/.skill-lock.json").mkdir()
    else:
        yaz(ev / ".agents/.skill-lock.json", bozuk)
    yaz(ev / ".agents/skills/microsoft-foundry/SKILL.md")
    yaz(ev / ".agents/skills/azure-prepare/SKILL.md")
    r = calistir(ev, tb, "--ayrinti")
    ro = calistir(ev, tb, "--ozet-json")
    j = json.loads(ro.stdout)
    test(f"40 kilit okunamaz ({bozuk or 'klasör'}): çökme yok, Foundry adı tanınır",
         r.returncode == 0 and ro.returncode == 0 and "Traceback" not in r.stderr + ro.stderr
         and "çalışırken hata verdi" not in ro.stdout and FOUNDRY in karar_satiri(j, "~/.agents/skills/microsoft-foundry")
         and karar_satiri(j, "~/.agents/skills/azure-prepare") == mod.KARAR_YENI.format(y="~/.agents/skills/azure-prepare", s="bilinmiyor"),
         r.stdout + r.stderr + ro.stdout)

# 41 Copilot for Azure manifesti: listedeki ad tanınır; bozuk manifest çökme vermez
ev, tb = ev_kur()
taban_yaz(ev, tb)
yaz(ev / ".agents/.copilot-for-azure-skills-manifest.json", json.dumps({"skills": ["azure-prepare", 3, None]}))
yaz(ev / ".agents/skills/azure-prepare/SKILL.md")
yaz(ev / ".agents/skills/azure-baska/SKILL.md")
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
test("41 manifestteki ad: Copilot for Azure ipucu; listede olmayan eski metin", COPILOT in karar_satiri(j, "~/.agents/skills/azure-prepare")
     and karar_satiri(j, "~/.agents/skills/azure-baska") == mod.KARAR_YENI.format(y="~/.agents/skills/azure-baska", s="bilinmiyor"), str(j["karar_bekleyen"]))
test("41b manifest izlenen girdi değildir", not any("copilot-for-azure-skills-manifest" in s for s in j["satirlar"]), str(j["satirlar"]))
yaz(ev / ".agents/.copilot-for-azure-skills-manifest.json", "{bozuk")
r = calistir(ev, tb)
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
test("41c bozuk manifest: çökme yok, eski metin", r.returncode == 0 and "Traceback" not in r.stderr
     and karar_satiri(j, "~/.agents/skills/azure-prepare") == mod.KARAR_YENI.format(y="~/.agents/skills/azure-prepare", s="bilinmiyor"))

# 42 kilit dosyasının kendisi YENİ: içindeki kayıtların yazıcıları birlikte
ev, tb = ev_kur()
os.remove(ev / ".agents/.skill-lock.json")
taban_yaz(ev, tb)
yaz(ev / ".agents/.skill-lock.json", json.dumps({"skills": {"microsoft-foundry": {"source": AZ}, "azure-prepare": {"source": AZ}}}))
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
kk = karar_satiri(j, "~/.agents/.skill-lock.json")
ra = calistir(ev, tb, "--ayrinti").stdout
test("42 yeni kilit dosyası: iki yazıcı, 300 karakter sınırı, durdurma yolları --ayrinti'de",
     "yazan: VS Code Foundry Toolkit uzantısı ya da VS Code GitHub Copilot for Azure uzantısı; durdurmak: --ayrinti satırlarında" in kk
     and len(kk) <= 300 and "yazan: ~/.agents/.skill-lock.json: VS Code Foundry Toolkit" in ra
     and "autoCheckFoundrySkill=false" in ra and "Don't Ask Again" in ra, kk + ra)
os.remove(ev / ".agents/.skill-lock.json")
yaz(ev / ".agents/.skill-lock.json", json.dumps({"skills": {"baska": {"source": "owner/repo"}}}))
j = json.loads(calistir(ev, tb, "--ozet-json").stdout)
test("42b tanınmayan kilit: eski metin", karar_satiri(j, "~/.agents/.skill-lock.json") == mod.KARAR_YENI.format(y="~/.agents/.skill-lock.json", s="skills aracı"))

# 43 kabuk dosyasında satır yok: kurulum betiği ipucu; başka nedenlerde ipucu yok
r = ortam(lambda e: yaz(e / ".zshrc", "# >>> baska >>>\nexport FOO=1\n# <<< baska <<<\n"))
test("43 ~/.zshrc satır yok: ipucu", "EKSİK: ~/.zshrc (satır yok)" in r.stdout and "kurulum betiği silmiş olabilir" in r.stdout
     and "dosyanın sonuna geri eklenir (onayla)" in r.stdout and "SORUN" in r.stdout, r.stdout)
r2 = ortam(lambda e: yaz(e / ".zshenv", "FOO=1\n"))
r3 = ortam(lambda e: yaz(e / ".claude/settings.json", json.dumps({"env": {}})))
r4 = ortam(lambda e: os.remove(e / ".zshenv"))
r5 = ortam(lambda e: yaz(e / ".zshrc", "export HYPERFRAMES_SKIP_SKILLS=0\n"))
test("43b ~/.zshenv satır yok: ipucu; settings.json, dosya yok ve geçersiz değerde yok",
     "kurulum betiği" in r2.stdout and all("kurulum betiği" not in x.stdout for x in (r3, r4, r5)) and "kurulum betiği" not in ortam(lambda e: None).stdout)

# 36 gerçek taban oluşmadı
test("36 gerçek taban dosyası yazılmadı", GERCEK_TABAN.exists() == GERCEK_TABAN_VARDI)

shutil.rmtree(TMP, ignore_errors=True)
gecen = sum(1 for _, k in SONUC if k)
for ad, k in SONUC:
    if not k:
        print("BAŞARISIZ:", ad)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
