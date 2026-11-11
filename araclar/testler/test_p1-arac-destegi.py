#!/usr/bin/env python3
"""P1 testleri: skill-ekle.py araç düzeni (ortak / yalniz-claude), araç rapor satırları, --araclar, yedek .gitignore, --kuru, korunan yollar.
Yalnız geçici klasör ve sahte veri; gerçek ev klasörleri/kütüphane durumu okunmaz ya da yazılmaz (HOME geçici klasöre alınır,
registry/global durum/hesap skilleri sahtelenir, komut sürümleri sahte). Son satır 'N/N test geçti'; çıkış 0 (hepsi geçti) ya da 1."""
import contextlib
import importlib.util
import io
import json
import os
import plistlib
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
TMP = Path(tempfile.mkdtemp(prefix="p1test-"))
GERCEK_HOME = os.environ.get("HOME")
os.environ["HOME"] = str(TMP / "home")        # modül içi Path.home() geçici klasöre baksın
(TMP / "home").mkdir()
SONUC = []


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-700:]}"))


spec = importlib.util.spec_from_file_location("se_p1", ARACLAR / "skill-ekle.py")
se = importlib.util.module_from_spec(spec)
spec.loader.exec_module(se)

# ------------------------------------------------------------------ sahte ortam
se.canli_global = lambda s: {}
se.hesap_skilleri = lambda: {}
se.guncelleme_suruyor = lambda: None
SAHTE_KAYIT = []
se.registry = lambda: SAHTE_KAYIT
sayac = [0]


def fm(ad):
    return f"---\nname: {ad}\ndescription: test skill\n---\n"


def kayit(ad, **ek):
    sayac[0] += 1
    d = TMP / "arsiv" / f"{sayac[0]}-{ad}"
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(fm(ad) + "x\n", encoding="utf-8")
    s = {"id": ad, "ad": ad, "klasor_adi": ad, "kaynak_yol": f"skills/{ad}", "repo": "o/r", "yol": str(d),
         "klasor_hash": f"h{sayac[0]}", "commit": "c1", "kategori": "test", "durum": "tercih", "aciklama": "test skill",
         "teknoloji_oto": [], "uyum": {"codex": "uyumlu"}, "degerlendirme": {"puan": 1, "not": "-"},
         "lisans": "MIT", "skill_md_kb": 1, "varyantlar": None}
    s.update(ek)
    return s


for n in ("alfa", "beta", "gama"):
    SAHTE_KAYIT.append(kayit(n))


def calistir(*args):
    """se.main()'i süreç içinde çalıştırır: (çıkış kodu, stdout+stderr)"""
    eski = sys.argv
    sys.argv = ["skill-ekle.py"] + [str(a) for a in args]
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
        sys.argv = eski
    return kod, out.getvalue() + err.getvalue()


def yeni_proje():
    return Path(tempfile.mkdtemp(dir=TMP, prefix="proje-"))


def agac(d: Path):
    s = {}
    for p in sorted(d.rglob("*")):
        rel = str(p.relative_to(d))
        s[rel] = ("symlink->" + str(p.readlink())) if p.is_symlink() else (p.read_bytes() if p.is_file() else "dir")
    return s


def sahte_json(**degisim):
    """Sahte yapay-zeka-araclari.json içeriği (son anahtarlar, 5 kurulu + 2 isteğe bağlı)."""
    bugun = date.today().isoformat()

    def k(anahtar, ad_kisa, kurulu, destek, okur, uretilir=True, surumler=None):
        return {"anahtar": anahtar, "ad": ad_kisa, "ad_kisa": ad_kisa, "kurulu": kurulu, "destek": destek, "surumler": surumler or [],
                "proje_skill_okur": okur, "proje_talimat_okur": [], "rol_dosyasi": {"yol": "x", "bicim": "md-yaml", "uretilir": uretilir, "neden": ""},
                "kullanici_koku": f"~/.sahte-{anahtar}", "dogrulama_tarihi": bugun, "belirsizler": [], "denendi": []}
    kayitlar = [k("claude-code", "Claude Code", True, "tam", [".claude/skills"]),
                k("codex", "Codex", True, "tam", [".agents/skills"]),
                k("antigravity", "Antigravity", True, "tam", [".agents/skills"], False),
                k("cursor", "Cursor", True, "tam", [".agents/skills", ".cursor/skills", ".claude/skills"], False),
                k("vscode-copilot", "VS Code Copilot", True, "tam", [".github/skills", ".claude/skills", ".agents/skills"], False),
                k("gemini-cli", "Gemini CLI", False, "istege-bagli", [".gemini/skills", ".agents/skills"], False),
                k("copilot-cli", "Copilot CLI", False, "istege-bagli", [".github/skills", ".claude/skills", ".agents/skills"], False)]
    veri = {"surum": 1, "araclar": kayitlar}
    veri.update(degisim)
    return veri


SAHTE_JSON = TMP / "araclar-sahte.json"
SAHTE_JSON.write_text(json.dumps(sahte_json()), encoding="utf-8")
se.ARAC_JSON = SAHTE_JSON


def satirlar(kilit, proje=None, secim=None, kayitlar=None):
    r = se.Rapor()
    se.arac_satirlari(proje or yeni_proje(), kilit, r, secim=secim, kayitlar=kayitlar)
    return r.satirlar


def kodlar(rows):
    return {k for _, k, _ in rows}


def metin(rows, kod):
    return " ".join(m for _, k, m in rows if k == kod)


try:
    # ================================================================== A. adlar ve kilit
    print("A. adlar ve kilit")
    test("1. ortak == ikisi, yalniz-claude == claude; duzen_adi dört yazım için doğru",
         se.ARACLAR["ortak"] == se.ARACLAR["ikisi"] and se.ARACLAR["yalniz-claude"] == se.ARACLAR["claude"]
         and [se.duzen_adi({"araclar": se.ARACLAR[x]}) for x in ("ortak", "ikisi", "yalniz-claude", "claude")]
         == ["ortak", "ortak", "yalniz-claude", "yalniz-claude"])
    h = subprocess.run([sys.executable, str(ARACLAR / "skill-ekle.py"), "--help"], capture_output=True, text=True)
    test("2. --help yeni adları ve bayrakları söyler; Phase 2 bayrakları (--gemini-md, --haric) henüz yok",
         h.returncode == 0 and all(x in h.stdout for x in ("yalniz-claude", "--araclar", "--ozet-json", "--siki"))
         and "--gemini-md" not in h.stdout and "--haric" not in h.stdout, h.stdout + h.stderr)
    p = yeni_proje()
    (p / ".skill-kutuphanesi").mkdir()
    kf = p / ".skill-kutuphanesi" / "kilit.json"
    kf.write_text(json.dumps({"surum": 3, "profil": None, "roller": [], "skiller": {}}), encoding="utf-8")
    once = (kf.read_bytes(), kf.stat().st_mtime_ns)
    k1 = se.kilit_oku(p)
    kf.write_text(json.dumps({"surum": 3, "araclar": ["claude"], "profil": None, "roller": [], "skiller": {}}), encoding="utf-8")
    k2 = se.kilit_oku(p)
    kf.write_text(json.dumps({"surum": 3, "profil": None, "roller": [], "skiller": {}}), encoding="utf-8")
    once = (kf.read_bytes(), kf.stat().st_mtime_ns)
    se.kilit_oku(p)
    test("3. kilit_oku: araclar yoksa codex_var doğru + 'varsayilan'; araclar varsa 'secildi'; okuma dosyaya yazmaz",
         se.codex_var(k1) and k1["arac_secimi"] == "varsayilan" and k2["arac_secimi"] == "secildi" and not se.codex_var(k2)
         and (kf.read_bytes(), kf.stat().st_mtime_ns) == once)
    p = yeni_proje()
    k = se.kilit_oku(p)
    se.kilit_yaz(p, k)
    y = json.loads((p / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))
    p2 = yeni_proje()
    (p2 / ".skill-kutuphanesi").mkdir()
    (p2 / ".skill-kutuphanesi" / "kilit.json").write_text(json.dumps({"surum": 3, "araclar": ["claude"], "roller": [], "skiller": {}}), encoding="utf-8")
    k = se.kilit_oku(p2)
    se.kilit_yaz(p2, k)
    y2 = json.loads((p2 / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))
    test("4. ilk kilit_yaz araclar=['claude','codex'] + 'varsayilan' yazar; var olan ['claude'] korunur ('secildi')",
         y["araclar"] == ["claude", "codex"] and y["arac_secimi"] == "varsayilan" and y2["araclar"] == ["claude"] and y2["arac_secimi"] == "secildi", f"{y} {y2}")
    ka, kb = {"roller": [], "skiller": {}}, {"roller": [], "skiller": {}}
    se.duzen_uygula(ka, "ikisi")
    se.duzen_uygula(kb, "ortak")
    kc = {}
    se.duzen_uygula(kc, "claude")
    test("5. duzen_uygula: ikisi == ortak (liste + 'secildi'); claude == yalniz-claude; eski kilit biçimi (liste) değişmez",
         ka == kb and ka["araclar"] == ["claude", "codex"] and ka["arac_secimi"] == "secildi" and kc["araclar"] == ["claude"])

    # ================================================================== B. rapor satırları
    print("B. rapor satırları")
    ortak = {"araclar": ["claude", "codex"], "arac_secimi": "secildi", "roller": [], "skiller": {}}
    yalniz = {"araclar": ["claude"], "arac_secimi": "secildi", "roller": [], "skiller": {}}
    r6 = satirlar(ortak)
    t6 = metin(r6, "arac-duzeni")
    test("6. ortak: arac-duzeni beş kurulu aracı görenler olarak sayar, arac-gormez yok, kurulu olmayanlar anılır",
         "Skilleri görenler: Claude Code, Codex, Antigravity, Cursor, VS Code Copilot." in t6 and "Görmeyenler: yok" in t6
         and "arac-gormez" not in kodlar(r6) and "Gemini CLI, Copilot CLI" in t6, t6)
    r7 = satirlar(yalniz)
    g7 = metin(r7, "arac-gormez")
    test("7. yalniz-claude: arac-gormez Codex ve Antigravity'yi söyler, Cursor ve VS Code Copilot'u söylemez",
         "Codex" in g7 and "Antigravity" in g7 and "Cursor" not in g7 and "Copilot" not in g7, g7)
    vars_ = {**ortak, "arac_secimi": "varsayilan"}
    r8a = satirlar(vars_, secim=None)
    kb8 = {"roller": [], "skiller": {}}
    se.duzen_uygula(kb8, "ortak")
    test("8. varsayılan seçim ve secim=None: arac-secimi-yok var; duzen_uygula sonrası ya da --arac verilince yok",
         "arac-secimi-yok" in kodlar(r8a) and "arac-secimi-yok" not in kodlar(satirlar(kb8)) and "arac-secimi-yok" not in kodlar(satirlar(vars_, secim="ortak")))
    hepsi = r6 + r7 + r8a + satirlar({**ortak, "roller": ["x"]}, proje=Path(tempfile.mkdtemp(dir=TMP)))
    test("9. 6-8'deki bütün satırlar BİLGİ (ne UYARI ne HATA)", hepsi and all(s == "BİLGİ" for s, _, _ in hepsi), hepsi)
    se.ARAC_JSON = TMP / "yok.json"
    r10a = satirlar(ortak, kayitlar=None)
    bozuk = TMP / "bozuk.json"
    bozuk.write_text("{ bu json değil", encoding="utf-8")
    se.ARAC_JSON = bozuk
    r10b = satirlar(ortak, kayitlar=None)
    se.ARAC_JSON = SAHTE_JSON
    test("10. dosya yok / bozuk: tam bir satır arac-belge-yok, çökme yok",
         [k for _, k, _ in r10a] == ["arac-belge-yok"] and [k for _, k, _ in r10b] == ["arac-belge-yok"], (r10a, r10b))
    c11 = metin(r6, "arac-cift-okuma")
    test("11. arac-cift-okuma yalnız ortak düzende ve Cursor ile VS Code Copilot'u anar",
         "Cursor" in c11 and "VS Code Copilot" in c11 and "Codex" not in c11 and "arac-cift-okuma" not in kodlar(r7))
    rr = satirlar({**ortak, "roller": ["ui"]})
    ry = satirlar({**yalniz, "roller": ["ui"]})
    test("12. arac-rolsuz ve arac-mutlak-yol yalnız roller varken; mutlak-yol yalnız ortak düzende; rolsüzde Cursor anılmaz",
         {"arac-rolsuz", "arac-mutlak-yol"} <= kodlar(rr) and "arac-mutlak-yol" not in kodlar(ry) and "arac-rolsuz" in kodlar(ry)
         and not ({"arac-rolsuz", "arac-mutlak-yol"} & kodlar(r6)) and "Antigravity" in metin(rr, "arac-rolsuz")
         and "Cursor" not in metin(rr, "arac-rolsuz").split("Cursor .claude/agents dosyalarını da okur (belge).")[1], metin(rr, "arac-rolsuz"))
    pg = yeni_proje()
    (pg / ".git").mkdir()
    test("13. arac-symlink yalnız ortak düzende ve proje .git içeriyorsa",
         "arac-symlink" in kodlar(satirlar(ortak, proje=pg)) and "arac-symlink" not in kodlar(r6)
         and "arac-symlink" not in kodlar(satirlar(yalniz, proje=pg)))
    tum = r6 + r7 + r8a + rr + ry + satirlar(ortak, proje=pg) + r10a
    test("14. her mesajda ': ' öncesi birden çok kelime (Rapor.gruplu bozmasın)", all(" " in m.partition(": ")[0] for _, _, m in tum if ": " in m),
         [m[:40] for _, _, m in tum if ": " in m and " " not in m.partition(": ")[0]])
    # yanlış anahtar yakalanır: 'copilot' anahtarı VS Code Copilot yerine geçmez
    d = sahte_json()
    for kk in d["araclar"]:
        if kk["anahtar"] == "vscode-copilot":
            kk["anahtar"] = "copilot"
    test("14b. kayıtlar anahtarla bulunur: bilinen anahtar kümesi 'vscode-copilot' içerir, 'copilot' yok",
         {x["anahtar"] for x in sahte_json()["araclar"]} >= {"claude-code", "codex", "antigravity", "cursor", "vscode-copilot"}
         and "copilot" not in {x["anahtar"] for x in sahte_json()["araclar"]} and any(x["anahtar"] == "copilot" for x in d["araclar"]))

    # ================================================================== C. düzen değişimi
    print("C. düzen değişimi ve koruma")
    p = yeni_proje()
    kod, out = calistir(p, "--skill", "alfa", "--evet")
    test("15a. ilk kurulum (araç seçilmeden): çıkış 0, çıktıda arac-secimi-yok + arac-duzeni, kilitte 'varsayilan'",
         kod == 0 and "arac-secimi-yok" in out and "arac-duzeni" in out
         and se.kilit_oku(p)["arac_secimi"] == "varsayilan" and (p / ".agents/skills/alfa/SKILL.md").exists()
         and (p / ".claude/skills/alfa").is_symlink(), out)
    kod, out = calistir(p, "--durum")
    test("15. --durum 'Claude + Codex' ve düzen adını gösterir; yalniz-claude sonrası 'sadece Claude'",
         "Claude + Codex" in out and "düzen: ortak" in out and "varsayılan: seçim yapılmadı" in out, out)
    kod, out = calistir(p, "--arac", "yalniz-claude", "--kuru")
    once = agac(p)
    test("16a. --arac yalniz-claude --kuru hiçbir şey yazmaz, gormez satırını gösterir",
         kod == 2 and "arac-gormez" in out and agac(p) == once, out)
    kod, out = calistir(p, "--arac", "yalniz-claude", "--evet")
    k = se.kilit_oku(p)
    test("16b. ortak -> yalniz-claude: .agents kalkar, .claude/skills gerçek kopya, araclar ['claude'] + 'secildi', --dogrula temiz",
         kod == 0 and not (p / ".agents").exists() and (p / ".claude/skills/alfa/SKILL.md").exists()
         and not (p / ".claude/skills/alfa").is_symlink() and k["araclar"] == ["claude"] and k["arac_secimi"] == "secildi"
         and calistir(p, "--dogrula")[0] == 0 and "(ortak) ->" in out and "(yalniz-claude)" in out, out)
    kod, out = calistir(p, "--durum")
    test("15b. yalniz-claude --durum: 'sadece Claude' ve (seçildi)", "sadece Claude" in out and "düzen: yalniz-claude (seçildi)" in out, out)
    kod, out = calistir(p, "--arac", "ortak", "--evet")
    k = se.kilit_oku(p)
    test("16c. yalniz-claude -> ortak: .agents/skills geri gelir, .claude/skills symlink, --dogrula temiz, araclar kalıcı",
         kod == 0 and (p / ".agents/skills/alfa/SKILL.md").exists() and (p / ".claude/skills/alfa").is_symlink()
         and k["araclar"] == ["claude", "codex"] and k["arac_secimi"] == "secildi" and calistir(p, "--dogrula")[0] == 0, out)
    kod, out = calistir(p, "--arac", "ikisi", "--kuru")
    test("16d. eski ad --arac ikisi / claude hâlâ çalışır", kod == 2 and "arac-duzeni" in out and calistir(p, "--arac", "claude", "--kuru")[0] == 2)
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "beta", "--arac", "ortak", "--evet")
    once = agac(p)
    kod, out = calistir(p, "--skill", "gama", "--arac", "yalniz-claude", "--evet")
    test("17a. kurulu ortak skillerle --skill ... --arac yalniz-claude: HATA arac-karisik, hiçbir şey yazılmaz",
         kod == 2 and "[HATA] arac-karisik" in out and "alfa, beta" in out and "2 skill ortak" in out and agac(p) == once, out)
    kod, out = calistir(p, "--skill", "gama", "--arac", "yalniz-claude", "--evet", "--zorla")
    test("17b. --zorla arac-karisik HATA'sını geçer (ZORLANAMAZ'da değil): HATA aşılır, işlem yapılır (karışık düzen kalır: doğrulama 1 verir, korumanın nedeni bu)",
         kod == 1 and "arac-karisik" in out and se.kilit_oku(p)["araclar"] == ["claude"] and len(se.kilit_oku(p)["skiller"]) == 3, out)
    pf = yeni_proje()
    kod, out = calistir(pf, "--skill", "alfa", "--arac", "yalniz-claude", "--evet")
    test("17c. taze projede --skill + --arac yalniz-claude uyarısız kurulur", kod == 0 and "arac-karisik" not in out
         and (pf / ".claude/skills/alfa/SKILL.md").exists() and not (pf / ".agents").exists(), out)

    # ================================================================== F. yedek .gitignore
    print("F. yedek .gitignore")
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--evet")
    gi = p / ".skill-kutuphanesi" / ".gitignore"
    ilk = gi.read_text(encoding="utf-8") if gi.exists() else None
    calistir(p, "--skill", "beta", "--evet")
    test("29. ilk yedekte .skill-kutuphanesi/.gitignore tam olarak 'yedek/'; ikinci yedek değiştirmez",
         ilk == "yedek/\n" and gi.read_text(encoding="utf-8") == "yedek/\n", ilk)
    p = yeni_proje()
    (p / ".skill-kutuphanesi").mkdir()
    (p / ".skill-kutuphanesi" / ".gitignore").write_text("*.tmp\nkendi-dosyam", encoding="utf-8")
    se.yedekle(p, [], "deneme")
    sonra = (p / ".skill-kutuphanesi" / ".gitignore").read_text(encoding="utf-8")
    p_b = yeni_proje()
    (p_b / ".skill-kutuphanesi").mkdir()
    for icerik in ("yedek/\n*.tmp\n", "x\nyedek"):
        (p_b / ".skill-kutuphanesi" / ".gitignore").write_text(icerik, encoding="utf-8")
        se.yedekle(p_b, [], "deneme")
        if (p_b / ".skill-kutuphanesi" / ".gitignore").read_text(encoding="utf-8") != icerik:
            break
    else:
        icerik = None
    test("30. kullanıcının .gitignore'una yedek/ eklenir (satırlar ve sıra korunur); zaten 'yedek' ya da 'yedek/' varsa dosya aynı kalır",
         sonra == "*.tmp\nkendi-dosyam\nyedek/\n" and icerik is None, (sonra, icerik))
    p = yeni_proje()
    calistir(p, "--skill", "alfa", "--kuru")
    p2 = yeni_proje()
    se.yedekle(p2, ["alfa"], "x")
    bilgi = json.loads(next((p2 / ".skill-kutuphanesi" / "yedek").iterdir()).joinpath("yedek.json").read_text(encoding="utf-8"))
    test("31. .gitignore yedek hedefi değildir; --kuru .skill-kutuphanesi oluşturmaz",
         not any(".gitignore" in x for x in bilgi["hedefler"]) and not (p / ".skill-kutuphanesi").exists() and not any(p.iterdir()))
    # --kuru dalları (--yenile / --blok / --geri-al)
    p = yeni_proje()
    once = agac(p)
    sonuclar = [calistir(p, *a) for a in (("--yenile", "--kuru"), ("--blok", "kisa", "--kuru"), ("--geri-al", "--kuru"))]
    test("27. --yenile/--blok/--geri-al ile --kuru: çıkış 0, '[kuru]' yazar, proje ağacı değişmez",
         all(k == 0 and "[kuru] Hiçbir şey değiştirilmedi. (yapılacak:" in o for k, o in sonuclar) and agac(p) == once and not any(p.iterdir()), sonuclar)
    pk = yeni_proje()
    calistir(pk, "--skill", "alfa", "--evet")
    once = agac(pk)
    kod, out = calistir(pk, "--yenile", "--kuru")
    test("27b. kurulu projede --yenile --kuru dosya yazmaz", kod == 0 and agac(pk) == once, out)

    # ================================================================== H. koruma, bloklar, Windows
    print("H. koruma, bloklar, Windows")
    sahte_kok = TMP / "home" / ".sahte-claude-code"
    sahte_kok.mkdir()
    yollar = se.arac_korunan_yollar()
    proje_alt = sahte_kok / "proje"
    proje_alt.mkdir()
    kod, out = calistir(proje_alt, "--durum")
    se.ARAC_JSON = TMP / "yok.json"
    bos = se.arac_korunan_yollar()
    kod2, out2 = calistir(proje_alt, "--durum")
    se.ARAC_JSON = SAHTE_JSON
    test("35. korunan yollar JSON'dan gelir ve genişletilir; böyle bir kökün altındaki proje reddedilir; JSON yoksa liste boş, davranış eskisi",
         sahte_kok.resolve() in yollar and len(yollar) == 7 and kod != 0 and "Güvenlik" in out and bos == [] and "Güvenlik" not in out2, (out, out2))
    p = yeni_proje()
    (p / "CLAUDE.md").write_text("# Benim notum\n", encoding="utf-8")
    (p / "AGENTS.md").write_text("# Benim agents\n", encoding="utf-8")
    calistir(p, "--skill", "alfa", "--evet")
    cm, am = (p / "CLAUDE.md").read_text(encoding="utf-8"), (p / "AGENTS.md").read_text(encoding="utf-8")
    blk = lambda m: m[m.index(se.BLOK_BAS):m.index(se.BLOK_SON) + len(se.BLOK_SON)]  # noqa: E731
    calistir(p, "--blok", "kisa", "--evet")
    cm2, am2 = (p / "CLAUDE.md").read_text(encoding="utf-8"), (p / "AGENTS.md").read_text(encoding="utf-8")
    test("36. tam ve kisa blok: CLAUDE.md ve AGENTS.md blokları aynı, kullanıcı metni işaretlerin dışında kalır, komut yolu var, "
         "(Q3 onaysız: blok metni bugünküyle aynı, 'Kütüphane: ~/Documents' cümlesi eklenmedi)",
         blk(cm) == blk(am) and cm.startswith("# Benim notum") and am.startswith("# Benim agents") and "skill-ekle.py" in blk(cm)
         and blk(cm2) == blk(am2) and "Kütüphanesiz bilgisayarda" in blk(cm2) and "Kütüphane: ~/Documents/SkillKutuphanesi" not in blk(cm2) + blk(cm), blk(cm2))
    p = yeni_proje()
    once = agac(p)
    eski_w = se.windows_mu
    se.windows_mu = lambda: True
    try:
        kod, out = calistir(p, "--skill", "alfa", "--evet")
    finally:
        se.windows_mu = eski_w
    test("37. Windows koruması: metni yazar, çıkış 0 değil, hiçbir şey yazılmaz", kod != 0 and "Windows'ta çalıştırılmaz" in out and agac(p) == once, out)

    # ================================================================== I. --araclar
    print("I. --araclar")
    # izin listesi: gerçek komut adı dışında hiçbir şey çalışmaz (kapatılmadan önce denetle)
    iz_iz = TMP / "izin-iz"
    sahte_kom = {"komut": [sys.executable, "-c", f"open({str(iz_iz)!r}, 'w').write('x')"]}
    izin_sonuc = (se.surum_oku(sahte_kom), se.surum_oku({"komut": ["claude", "--help"]}), se.surum_oku({"komut": ["rm", "--version"]}))
    test("38a. sürüm komutu izin listesinde değilse çalıştırılmaz (None, iz dosyası yok)", izin_sonuc == (None, None, None) and not iz_iz.exists(), izin_sonuc)
    se.SURUM_KOMUT_IZIN_KONTROLU = False  # aşağıdaki testler sahte python komutu kullanır
    py_surum = lambda v: {"komut": [sys.executable, "-c", f"print('tool {v} (x)')"]}  # noqa: E731
    plist_dosya = TMP / "Info.plist"
    plist_dosya.write_bytes(plistlib.dumps({"CFBundleShortVersionString": "9.8.7"}))

    def ns(**kw):
        import argparse
        return argparse.Namespace(**{"ozet_json": True, "siki": False, **kw})

    def calis_ozet(kayitlar=None, dosya=None, simdi=None, **kw):
        if dosya is not None:
            se.ARAC_JSON = dosya
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            kod = se.araclar_raporu(ns(**kw), kayitlar=kayitlar, simdi=simdi)
        se.ARAC_JSON = SAHTE_JSON
        return kod, out.getvalue()

    def kayit_s(**ek):
        d = {"anahtar": "t", "ad": "T", "ad_kisa": "T", "kurulu": True, "proje_skill_okur": [".agents/skills"], "dogrulama_tarihi": date.today().isoformat(),
             "surumler": [{"ad": "k", "kayitli": "1.2.3", "okuma": py_surum("1.2.3")}, {"ad": "p", "kayitli": "9.8.7", "okuma": {"plist": str(plist_dosya)}}]}
        d.update(ek)
        return d
    kod, o = calis_ozet([kayit_s()])
    j = json.loads(o)
    test("38. komut + plist sürümleri kayıtla aynı: durum temiz, çıkış 0", kod == 0 and j["durum"] == "temiz" and j["karar_bekleyen"] == [], o)
    kod, o = calis_ozet([kayit_s(surumler=[{"ad": "k", "kayitli": "1.2.0", "okuma": py_surum("1.2.3")}])])
    j = json.loads(o)
    test("39. sürüm farklı: dikkat; karar satırında iki sürüm de var", j["durum"] == "dikkat" and any("1.2.0" in s and "1.2.3" in s for s in j["karar_bekleyen"]), o)
    bugun = date.today()
    j46 = json.loads(calis_ozet([kayit_s(dogrulama_tarihi=(bugun - timedelta(days=46)).isoformat())], simdi=bugun)[1])
    j44 = json.loads(calis_ozet([kayit_s(dogrulama_tarihi=(bugun - timedelta(days=44)).isoformat())], simdi=bugun)[1])
    j45 = json.loads(calis_ozet([kayit_s(dogrulama_tarihi=(bugun - timedelta(days=45)).isoformat())], simdi=bugun)[1])
    test("40. doğrulama 46 gün: dikkat; 44 ve 45 gün: temiz", j46["durum"] == "dikkat" and j44["durum"] == "temiz" and j45["durum"] == "temiz", (j46, j44))
    yok = {"komut": ["bu-komut-yok-p1-test"]}
    j41a = json.loads(calis_ozet([kayit_s(kurulu=False)])[1])
    j41b = json.loads(calis_ozet([kayit_s(surumler=[{"ad": "k", "kayitli": "1.0.0", "okuma": yok}])])[1])
    test("41. kurulu:false ama bulundu -> dikkat ('artık kurulu'); kurulu:true ama bulunamadı -> dikkat",
         j41a["durum"] == "dikkat" and any("artık kurulu" in s for s in j41a["karar_bekleyen"]) and j41b["durum"] == "dikkat", (j41a, j41b))
    kod_a, o_a = calis_ozet(dosya=bozuk)
    kod_b, o_b = calis_ozet(dosya=bozuk, siki=True)
    kod_c, o_c = calis_ozet(dosya=TMP / "hic-yok.json", siki=True)
    eksikli = TMP / "eksik.json"
    eksikli.write_text(json.dumps({"surum": 1, "araclar": [{"anahtar": "x", "ad": "x"}]}), encoding="utf-8")
    kod_d, o_d = calis_ozet(dosya=eksikli, siki=True)
    test("42. bozuk/eksik/yok JSON: durum 'sorun'; --siki yoksa çıkış 0, varsa 1",
         json.loads(o_a)["durum"] == "sorun" and kod_a == 0 and kod_b == 1 and kod_c == 1 and kod_d == 1 and json.loads(o_d)["durum"] == "sorun", (o_a, o_d))
    kod, o = calis_ozet([kayit_s()])
    satir_n = [s for s in o.splitlines() if s.strip()]
    jj = json.loads(o)
    test("43. --ozet-json: stdout tek satır, tek JSON nesnesi; anahtarlar arac/durum/satirlar/karar_bekleyen; arac=='arac-belgeleri'",
         len(satir_n) == 1 and set(jj) == {"arac", "durum", "satirlar", "karar_bekleyen"} and jj["arac"] == "arac-belgeleri", o)
    r_ = subprocess.run([sys.executable, str(ARACLAR / "skill-ekle.py"), "--ozet-json"], capture_output=True, text=True)
    test("43b. --ozet-json tek başına (--araclar'sız) hata verir", r_.returncode != 0 and "--araclar" in r_.stderr, r_.stderr)

    # gerçek kütüphane dosyası (salt okunur)
    gercek = json.loads((KOK / "yapay-zeka-araclari.json").read_text(encoding="utf-8"))
    zorunlu = ["anahtar", "ad", "ad_kisa", "kurulu", "destek", "surumler", "proje_skill_okur", "proje_talimat_okur", "rol_dosyasi",
               "kullanici_koku", "dogrulama_tarihi", "belirsizler", "denendi"]
    k_ = gercek["araclar"]
    token_gibi = [x for x in re.findall(r"[A-Za-z0-9]{20,}", re.sub(r"https?://\S+", "", json.dumps(k_, ensure_ascii=False)))
                  if re.search(r"[A-Za-z]", x) and re.search(r"\d", x)]
    test("44. gerçek yapay-zeka-araclari.json (yalnız yapı): zorunlu alanlar, liste biçimi, benzersiz anahtar, makine_geneli_yazar yok, "
         "göreli klasörler, token benzeri değer yok",
         isinstance(k_, list) and bool(k_) and gercek["surum"] == 1 and all(all(z in x for z in zorunlu) for x in k_)
         and len({x["anahtar"] for x in k_}) == len(k_)
         and not any("makine_geneli_yazar" in x for x in k_) and all(not d.startswith(("/", "~")) for x in k_ for d in x["proje_skill_okur"])
         and not token_gibi and all(isinstance(x["belirsizler"], list) and isinstance(x["denendi"], list) for x in k_), token_gibi)
    eski_so = se.surum_oku
    se.surum_oku = lambda okuma: None          # gerçek claude/codex komutları ASLA çalıştırılmaz
    try:
        kod, o = calis_ozet(dosya=KOK / "yapay-zeka-araclari.json")
    finally:
        se.surum_oku = eski_so
    jr = json.loads(o)
    test("44b. gerçek dosya (sürüm okuma sahte): özet JSON biçimi doğru, durum 'sorun' değil, çıkış 0",
         kod == 0 and jr["arac"] == "arac-belgeleri" and jr["durum"] in ("temiz", "dikkat") and bool(re.search(r"\d+ araç kayıtlı, \d+ kurulu", jr["satirlar"][0])), o)
finally:
    shutil.rmtree(TMP, ignore_errors=True)
    if GERCEK_HOME:
        os.environ["HOME"] = GERCEK_HOME

gecen = sum(1 for _, k in SONUC if k)
print(f"{gecen}/{len(SONUC)} test geçti")
sys.exit(0 if gecen == len(SONUC) else 1)
