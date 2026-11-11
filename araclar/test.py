#!/usr/bin/env python3
"""Uçtan uca test: geçici bir projede skill-ekle.py'nin tüm güvenlik senaryolarını dener.
Global klasörlerin test boyunca değişmediğini de kontrol eder. Kütüphaneyi değiştirmez.

Kullanım: python3 araclar/test.py
"""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GLOBAL_KLASORLER, KOK, json_oku  # noqa: E402

ARAC = [sys.executable, str(KOK / "araclar" / "skill-ekle.py")]
SONUC = []


def calistir(*args, girdi=None):
    r = subprocess.run(ARAC + [str(a) for a in args], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout + r.stderr


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {ayrinti[-600:]}"))


def parmak_izi():
    h = hashlib.sha256()
    for g in list(GLOBAL_KLASORLER.values()) + [Path.home() / ".openmontage" / ".agents" / "skills"]:
        if g.exists():
            for p in sorted(g.iterdir()):
                if p.name in ("synced", ".system"):  # Claude hesap senkronu / Codex'in kendi yerleşik skilleri
                    continue
                h.update(p.name.encode())
                h.update(str(p.lstat().st_mtime_ns).encode())
    return h.hexdigest()


def agac(p: Path):
    """Proje içeriği (yedek klasörü hariç: her işlem yeni yedek bırakır)."""
    return sorted(str(x.relative_to(p)) for x in p.rglob("*") if "/yedek" not in "/" + str(x.relative_to(p)))


def yol_testleri():
    """Sabit yol taraması (ortak.yol_taramasi & ortak.yol_*): yalnız tempfile fixture'ları; global klasörlere ve ~/Documents'a bakmaz."""
    import ortak as o
    kok = Path(tempfile.mkdtemp(prefix="yol-test-"))
    eski_istisna = o.YOL_ISTISNA
    sayac = [0]

    def sifirla():
        o._YOL_ONBELLEK.clear()
        o._SKILLER_INDEKS[:] = [None, 0, None]

    def klasor(ad, dosyalar):
        d = kok / ad
        for rel, m in dosyalar.items():
            (d / rel).parent.mkdir(parents=True, exist_ok=True)
            (d / rel).write_text(m, encoding="utf-8")
        return d

    def tara(ad, dosyalar, adlar=None, bilinen=None):
        return o.yol_taramasi(klasor(ad, dosyalar), adlar or {ad}, bilinen)

    def turler(b):
        return sorted(x["tur"] for x in b)

    def kayit(ad, repo="o/r", kaynak_yol=None, dosyalar=None, **ek):
        sayac[0] += 1
        d = klasor(f"s{sayac[0]}-{ad}", dosyalar or {"SKILL.md": "x\n"})
        return {"id": ad, "ad": ad, "klasor_adi": ad, "kaynak_yol": kaynak_yol or f"skills/{ad}", "repo": repo, "yol": str(d),
                "klasor_hash": f"h{sayac[0]}", **ek}

    try:
        # --- türler
        b = tara("a1", {"SKILL.md": "Çalıştır: `~/.claude/skills/a1/scripts/run.py` sonra.\n", "scripts/run.py": "print(1)\n"})
        x = b[0] if b else {}
        test("yol: genel-kendi (dosya var): kalan, var, sınıf, ham, çevrilebilir",
             len(b) == 1 and x["tur"] == "genel-kendi" and x["kalan"] == "scripts/run.py" and x["var"] is True and x["sinif"] == "ajan"
             and x["ham"] == "~/.claude/skills/a1/scripts/run.py" and x["satir"] == 1 and x["engel"] is None and x["cevrilebilir"] is True, str(b))
        b = tara("a2", {"SKILL.md": "~/.agents/skills/a2/eksik.py\n"})
        test("yol: genel-kendi dosya yoksa engel dosya-yok, çevrilebilir değil",
             b[0]["var"] is False and b[0]["engel"] == "dosya-yok" and b[0]["cevrilebilir"] is False, str(b))
        onekler = ["~/.claude", "$HOME/.agents", "${HOME}/.codex", "$CODEX_HOME", "${CODEX_HOME}", "$CLAUDE_DIR", "/Users/ali/.claude", "/home/ali/.agents",
                   "${CODEX_HOME:-$HOME/.codex}"]
        b = tara("a3", {"SKILL.md": "\n".join(f"{p}/skills/a3/SKILL.md" for p in onekler) + "\n"})
        test("yol: ev önekleri (~ $HOME ${HOME} $CODEX_HOME ${CODEX_HOME} $CLAUDE_DIR /Users /home ${X:-…}) genel-kendi sayılır",
             turler(b) == ["genel-kendi"] * len(onekler) and all(x["cevrilebilir"] for x in b), str(turler(b)))
        b = tara("a4", {"SKILL.md": "~/.claude/skills/bar/SKILL.md ve ~/.claude/skills/zzz/x.md\n"}, bilinen={"bar", "a4"})
        test("yol: genel-baska (bilinen skill) ve ornek-metin (kütüphanede olmayan ad); var bilinmiyor",
             turler(b) == ["genel-baska", "ornek-metin"] and b[0]["hedef"] == "bar" and b[0]["var"] is None and b[0]["cevrilebilir"] is False, str(b))
        b = tara("a4b", {"SKILL.md": "~/.claude/skills/zzz/x.md\n"})
        test("yol: bilinen_adlar verilmezse bilinmeyen hedef genel-baska kalır", turler(b) == ["genel-baska"], str(b))
        b = tara("a5", {"SKILL.md": "~/.claude/skills/_shared/asc/asc.py\n"}, bilinen={"a5"})
        test("yol: _ ile başlayan hedef ortak-dizin", turler(b) == ["ortak-dizin"] and b[0]["hedef"] == "_shared", str(b))
        b = tara("a6", {"SKILL.md": "~/.claude/skills/geo-*/ ve ~/.claude/skills/geo- ve ~/.claude/skills/* ve ~/.claude/skills/<ad>/x ve ~/.claude/skills/{ad} ve ~/.claude/skills/$AD/x\n"})
        test("yol: joker / '-' ile biten ad genel-kalip; <ad> {ad} $AD yer tutucuları bulgu üretmez", turler(b) == ["genel-kalip"] * 3, str(b))
        b = tara("a7", {"SKILL.md": "Bkz ~/.claude/skills/a7. Ayrıca ~/.claude/skills/a7/SKILL.md, ve ~/.claude/skills/a7/…\n"})
        test("yol: cümle sonu noktası ad ve kalana karışmaz; '…' sonrası kesilir", sorted(x["kalan"] for x in b) == ["", "", "SKILL.md"] and all(x["tur"] == "genel-kendi" for x in b), str(b))
        b = tara("a8", {"SKILL.md": "~/.claude/skills/a8/references/x.md:12 ve ~/.claude/skills/a8/references/x.md#baslik; ~/.claude/skills/a8/references/x.md)\n",
                        "references/x.md": "-\n"})
        test("yol: kalan temizliği (:satır, #bağ, ;)", [x["kalan"] for x in b] == ["references/x.md"] * 3 and all(x["var"] for x in b), str([x["kalan"] for x in b]))
        b = tara("a9", {"SKILL.md": "${CLAUDE_PLUGIN_ROOT}/skills/a9/references/r.md\n${CLAUDE_PLUGIN_ROOT}/.claude/skills/sib/SKILL.md\n"
                                    "${CLAUDE_PLUGIN_ROOT}/scripts/x.sh\nuse `${CLAUDE_PLUGIN_ROOT}` here\n${CLAUDE_PLUGIN_ROOT}/skills/dash.html\n"
                                    "${CLAUDE_PLUGIN_ROOT}/skills/<ad>/x\n", "references/r.md": "-\n"}, bilinen={"sib", "a9"})
        test("yol: eklenti-kendi / eklenti-kardes / eklenti-kok-yol / eklenti-kok-anma; skills/<dosya.uzantı> kök yolu; skills/<ad> yer tutucusu kalıp",
             turler(b) == ["eklenti-kardes", "eklenti-kendi", "eklenti-kok-anma", "eklenti-kok-yol", "eklenti-kok-yol", "genel-kalip"]
             and next(x for x in b if x["tur"] == "eklenti-kendi")["cevrilebilir"] is True, str(turler(b)))
        b = tara("b1", {"SKILL.md": "${CLAUDE_SKILL_DIR}/../sib/x.md\n${CLAUDE_SKILL_DIR}/../../hooks/h.sh\n${CLAUDE_SKILL_DIR}/refs/ok.md\n"})
        test("yol: skil-disi-yol: tek '..' kardeş adını hedef alır, >=2 '..' hedefsiz; skill içi yol bulgu değil",
             turler(b) == ["skil-disi-yol"] * 2 and (b[0]["hedef"], b[0]["kalan"]) == ("sib", "x.md") and b[1]["hedef"] is None, str(b))
        b = tara("b2", {"SKILL.md": "oku ../sib/SKILL.md ve [x](../sib/y.md) ve ../node_modules/x/y.js ve ../b2/z.md\n",
                        "references/a.md": "../../sib/q.md ve ../sib/inside.md\n"}, bilinen={"sib", "b2"})
        test("yol: kardes-goreli: linksiz, kütüphanede olan ad, derinliğe uygun; link/bilinmeyen/kendi klasörü/skill-içi bulgu değil",
             turler(b) == ["kardes-goreli"] * 2 and {x["dosya"] for x in b} == {"SKILL.md", "references/a.md"}, str([(x['dosya'], x['ham']) for x in b]))
        b = tara("b3", {"SKILL.md": "## Install\nnpx skills add o/r --skill b3 -g\n## Kullanım\nnpx skills add o/r --skill x --global\n"
                                    "cp -r x ~/.claude/skills/b3\nmkdir -p $CODEX_HOME/skills/y\nls ~/.claude/skills\n"})
        yz = [x for x in b if x["tur"] == "genele-yazar"]
        test("yol: genele-yazar kurulum bandı / ajan adımı ayrımı", [x["alt"] for x in yz] == ["kurulum-bandi", "ajan-adimi"], str(yz))
        test("yol: genele-kopyalar (cp/mkdir hedefi genel skills klasörü); salt ls bulgu değil", turler([x for x in b if x["tur"] == "genele-kopyalar"]) == ["genele-kopyalar"] * 2, str(b))
        # --- sınıf
        d = {"SKILL.md": "x ~/.claude/skills/c1/scripts/a.py ve references/cited.md\n", "README.md": "~/.claude/skills/c1/a\n", "NOTICE": "~/.claude/skills/c1/a\n",
             "AGENTS.md": "~/.claude/skills/c1/a\n", "scripts/a.py": "~/.claude/skills/c1/a\n", "scripts/install.sh": "~/.claude/skills/c1/a\n",
             "scripts/tests/t.py": "~/.claude/skills/c1/a\n", "references/cited.md": "~/.claude/skills/c1/a\n", "references/other.md": "~/.claude/skills/c1/a\n",
             "docs/x.md": "~/.claude/skills/c1/a\n", "ko/SKILL.md": "~/.claude/skills/c1/a\n", "SKILL.zh-CN.md": "~/.claude/skills/c1/a\n",
             "run.sh": "~/.claude/skills/c1/a\n", "setup.md": "~/.claude/skills/c1/a\n", "templates/t.md": "~/.claude/skills/c1/a\n",
             "references/INSTALL.md": "~/.claude/skills/c1/a\n"}
        sn = {x["dosya"]: x["sinif"] for x in tara("c1", d)}
        beklenen = {"SKILL.md": "ajan", "README.md": "dokuman", "NOTICE": "dokuman", "AGENTS.md": "dokuman", "scripts/a.py": "ajan", "scripts/install.sh": "kurucu",
                    "scripts/tests/t.py": "dokuman", "references/cited.md": "ajan", "references/other.md": "dokuman", "docs/x.md": "dokuman", "ko/SKILL.md": "dokuman",
                    "SKILL.zh-CN.md": "dokuman", "run.sh": "ajan", "setup.md": "kurucu", "templates/t.md": "ajan", "references/INSTALL.md": "kurucu"}
        test("yol: dosya sınıfı (ajan/kurucu/dokuman: kök SKILL.md, scripts/, atıflı referans, install*, README*, dil klasörü, atıfsız dosya)", sn == beklenen,
             str({k: (sn.get(k), v) for k, v in beklenen.items() if sn.get(k) != v}))
        # --- engeller
        d = {"SKILL.md": "a ~/.claude/skills/e1/ok.md\nb ~/.claude/skills/e1/x.md ve ~/.agents/skills/e1/x.md\n"
                         "d ~/.claude/skills/e1\ne ~/.claude/skills/e1/yok.md\nbkz references/k.md\n", "ok.md": "-\n", "x.md": "-\n",
             "scripts/r.py": 'P = "~/.claude/skills/e1/ok.md"\n', "scripts/setup.sh": "~/.claude/skills/e1/ok.md\n",
             "README.md": "~/.claude/skills/e1/ok.md\n", "references/k.md": "~/.claude/skills/e1/ok.md ve .claude/skills/e1/ok.md\n"}
        b = tara("e1", d)
        eng = {(x["dosya"], x["satir"]): x["engel"] for x in b if x["tur"] == "genel-kendi"}
        test("yol: engel nedenleri (çevrilebilir / çok kök / kalan boş / dosya yok)",
             eng[("SKILL.md", 1)] is None and eng[("SKILL.md", 2)] == "cok-kok" and eng[("SKILL.md", 3)] == "kalan-bos"
             and eng[("SKILL.md", 4)] == "dosya-yok", str(eng))
        test("yol: engel: betik-ici, kurucu-dosya, dokuman, karisik-dosya",
             eng[("scripts/r.py", 1)] == "betik-ici" and eng[("scripts/setup.sh", 1)] == "kurucu-dosya" and eng[("README.md", 1)] == "dokuman"
             and eng[("references/k.md", 1)] == "karisik-dosya", str(eng))
        test("yol: çevrilebilir = engelsiz + var True + kalan dolu (diğerlerinde asla)",
             [x["cevrilebilir"] for x in b if x["tur"] == "genel-kendi"].count(True) == 1, str([(x["dosya"], x["cevrilebilir"]) for x in b]))
        # --- dosya kapsamı
        d = klasor("f1", {"SKILL.md": "-\n", ".env": "~/.claude/skills/f1/a\n", ".env.local": "~/.claude/skills/f1/a\n", "k.pem": "~/.claude/skills/f1/a\n",
                          "k.key": "~/.claude/skills/f1/a\n", "KAYNAK.md": "~/.claude/skills/f1/a\n", "r.png": "~/.claude/skills/f1/a\n",
                          "buyuk.md": "~/.claude/skills/f1/a\n" + "x" * 2_000_001, "n.md": "ok ~/.claude/skills/f1/a\n"})
        test(".env*, *.pem, *.key, KAYNAK.md, uzantısız-olmayan yabancı uzantı ve 2 MB üstü dosyalar taranmaz", [x["dosya"] for x in o.yol_taramasi(d, {"f1"})] == ["n.md"],
             str(o.yol_taramasi(d, {"f1"})))
        once = sorted(str(p) for p in d.rglob("*"))
        o.yol_taramasi(d, {"f1"})
        test("yol: tarama saf (klasöre hiçbir şey yazmaz), iki çalıştırma aynı sonucu verir", once == sorted(str(p) for p in d.rglob("*"))
             and o.yol_taramasi(d, {"f1"}) == o.yol_taramasi(d, {"f1"}))
        # ===== sertleştirme turu: tarayıcı kenar durumları
        b = tara("g1", {"SKILL.md": "~/.claude/skills/g1/x.md ve ~/.codex/skills/g1/x.md\n$CODEX_HOME/skills/g1/a.md ve ~/.codex/skills/g1/b.md\n"
                                    "${CLAUDE_CONFIG_DIR}/skills/g1/c.md\n"})
        eg = {(x["satir"], x["ham"]): x["engel"] for x in b}
        test("yol: cok-kok yalnız FARKLI kök için ($CODEX_HOME + ~/.codex aynı kök); ${CLAUDE_CONFIG_DIR} ön eki tanınır",
             eg[(1, "~/.claude/skills/g1/x.md")] == "cok-kok" and eg[(2, "$CODEX_HOME/skills/g1/a.md")] != "cok-kok" and eg[(2, "~/.codex/skills/g1/b.md")] != "cok-kok"
             and (3, "${CLAUDE_CONFIG_DIR}/skills/g1/c.md") in eg, str(eg))
        b = tara("g2", {"SKILL.md": "~/.claude/skills/geo$SUF/x ve ~/.claude/skills/a{b}/x ve ~/.claude/skills/z[1]/x\n"})
        test("yol: ad'ın hemen ardından gelen $ { [ yer tutucusu genel-kalip (son karakter koruması)", turler(b) == ["genel-kalip"] * 3, str(b))
        b = tara("g3", {"SKILL.md": "~/.claude/skills/.system/imagegen/SKILL.md\n"}, bilinen={"g3"})
        test("yol: gizli sistem klasörü (.system) bilinen listede olmasa da genel-baska (ornek-metin değil)", turler(b) == ["genel-baska"], str(b))
        b = tara("g4", {"SKILL.md": "/mnt/home/ali/.claude/skills/g4/x.md ve x/~/.claude/skills/g4/y.md ve a$~/.claude/skills/g4/z.md\n"})
        test("yol: ev önekinin önünde yol/sözcük karakteri varsa eşleşmez (lookbehind)", b == [], str(b))
        b = tara("g5", {"SKILL.md": "## Kullanım\nnpx skills add o/r --skill g5\nnpx skills add o/r --skill g5 -g\n"})
        test("yol: -g/--global olmayan npx skills add genele-yazar sayılmaz", turler(b) == ["genele-yazar"] and b[0]["satir"] == 3, str(b))
        # --- sınıf kuralları (dil kuralı kod dosyalarını susturmaz)
        d = {"SKILL.md": "README.md ./references/cited2.md references/dir/ ./.hidden/run.md\n", "README.md": "~/.claude/skills/c2/a\n",
             "references/cited2.md": "~/.claude/skills/c2/a\n", "references/dir/x.md": "~/.claude/skills/c2/a\n", ".hidden/run.md": "~/.claude/skills/c2/a\n",
             "scripts/bootstrap.sh": "~/.claude/skills/c2/a\n", "bin/b.sh": "~/.claude/skills/c2/a\n", "agents/a.md": "~/.claude/skills/c2/a\n",
             "scripts/__tests__/t.js": "~/.claude/skills/c2/a\n", "scripts/fixtures/f.md": "~/.claude/skills/c2/a\n", "scripts/i18n/x.md": "~/.claude/skills/c2/a\n",
             "scripts/CHANGELOG.md": "~/.claude/skills/c2/a\n", "scripts/LICENSE": "~/.claude/skills/c2/a\n", "scripts/readme.md": "~/.claude/skills/c2/a\n",
             "sub/SKILL.md": "~/.claude/skills/c2/a\n", "scripts/export-it.sh": "~/.claude/skills/c2/a\n", "scripts/read_no.py": "~/.claude/skills/c2/a\n",
             "scripts/id/run.sh": "~/.claude/skills/c2/a\n", "scripts/it/x.md": "~/.claude/skills/c2/a\n", "docs/NOTICE.md": "~/.claude/skills/c2/a\n",
             "references/notes_it.md": "~/.claude/skills/c2/a\n"}
        sn = {x["dosya"]: x["sinif"] for x in tara("c2", d) if x["tur"] == "genel-kendi" and x["kalan"] == "a"}
        beklenen = {"README.md": "dokuman", "references/cited2.md": "ajan", "references/dir/x.md": "ajan", ".hidden/run.md": "ajan", "scripts/bootstrap.sh": "kurucu",
                    "bin/b.sh": "ajan", "agents/a.md": "ajan", "scripts/__tests__/t.js": "dokuman", "scripts/fixtures/f.md": "dokuman", "scripts/i18n/x.md": "dokuman",
                    "scripts/CHANGELOG.md": "dokuman", "scripts/LICENSE": "dokuman", "scripts/readme.md": "dokuman", "sub/SKILL.md": "ajan",
                    "scripts/export-it.sh": "ajan", "scripts/read_no.py": "ajan", "scripts/id/run.sh": "ajan", "scripts/it/x.md": "dokuman", "docs/NOTICE.md": "dokuman",
                    "references/notes_it.md": "dokuman"}
        test("yol: dosya sınıfı kenar durumları (atıflı doküman, ./ ve dizin/ atfı, gizli klasör, bootstrap, bin/agents, test klasörleri, dil kodu adlı KOD dosyası ajan, iç içe SKILL.md)",
             sn == beklenen, str({k: (sn.get(k), v) for k, v in beklenen.items() if sn.get(k) != v}))
        # --- kurulum komutu engeli (her komut + yön)
        komutlar = ["ln -s a ~/.claude/skills/e2/x.md", "mkdir -p ~/.claude/skills/e2/x.md", "cp -r a ~/.claude/skills/e2/x.md", "curl -o ~/.claude/skills/e2/x.md u",
                    "wget -O ~/.claude/skills/e2/x.md u", "rm -rf ~/.claude/skills/e2/x.md", "npx skills add o/r -g ~/.claude/skills/e2/x.md", "git clone u ~/.claude/skills/e2/x.md"]
        b = tara("e2", {"SKILL.md": "\n".join(komutlar) + "\ncat ~/.claude/skills/e2/x.md; rm -rf tmp\n", "x.md": "-\n"})
        eg = [x["engel"] for x in b if x["tur"] == "genel-kendi"]
        test("yol: kurulum-komutu engeli her komut için (ln/mkdir -p/cp/curl -o/wget -O/rm -rf/npx skills add/git clone); komut yoldan SONRA gelirse engel değil",
             eg[:len(komutlar)] == ["kurulum-komutu"] * len(komutlar) and eg[-1] == "karisik-dosya", str(eg))
        b = tara("e3", {"SKILL.md": "~/.claude/skills/e3/yok.md ve\n.claude/skills/e3/z.md\n"})
        test("yol: engel önceliği dosya-yok, karisik-dosya'dan önce; ikisi de engeller listesinde",
             b[0]["engel"] == "dosya-yok" and "karisik-dosya" in b[0]["engeller"], str(b))
        b = tara("e4", {"SKILL.md": "ln -s a ~/.claude/skills/e4\nBkz ~/.claude/skills/e4/x.md\nin most installs that's ~/.claude/skills/e4/x.md\n", "x.md": "-\n",
                        "scripts/s.sh": 'echo "kullanım: ~/.claude/skills/e4/x.md"\nSKILL_DIR="~/.claude/skills/e4"\nrun ~/.claude/skills/e4/x.md\n'})
        eg = {(x["dosya"], x["satir"]): (x["engel"], x.get("atama")) for x in b if x["tur"] == "genel-kendi"}
        test("yol: kurulum anlatan dosyada tüm kendi yolları karisik-dosya; açıklama satırı ornek-satir; betikte echo kullanim-metni; atama bayrağı",
             eg[("SKILL.md", 2)][0] == "karisik-dosya" and eg[("SKILL.md", 3)][0] == "ornek-satir" and eg[("scripts/s.sh", 1)][0] == "kullanim-metni"
             and eg[("scripts/s.sh", 2)] == ("kalan-bos", True) and eg[("scripts/s.sh", 3)][0] == "betik-ici", str(eg))
        # --- genele-yazar bandı ve genele-kopyalar kalıpları
        b = tara("h1", {"SKILL.md": "## Install\nnpx skills add a/b --skill other -g\nnpx skills add a/b --skill h1 -g\n", "scripts/x.sh": "# Install deps\nnpx skills add a/b -g\n"})
        al = {(x["dosya"], x["satir"]): x["alt"] for x in b if x["tur"] == "genele-yazar"}
        test("yol: kurulum bandı yalnız markdown + Install başlığı + --skill kendi adı; başka skill kuruluyorsa ya da betik dosyasında ajan-adimi",
             al == {("SKILL.md", 2): "ajan-adimi", ("SKILL.md", 3): "kurulum-bandi", ("scripts/x.sh", 2): "ajan-adimi"}, str(al))
        b = tara("h2", {"SKILL.md": "python3 s.py --dest ~/.codex/skills\nWrite a filesystem skill to `$CODEX_HOME/skills/x`\nbuild --root ~/.codex/skills ~/.agents/skills\n"
                                    "list ~/.claude/skills\n"})
        test("yol: genele-kopyalar --dest/--target ve 'write … to <ev>/skills' kalıbı; --root (okuma kökü) ve salt ls sayılmaz",
             [x["satir"] for x in b if x["tur"] == "genele-kopyalar"] == [1, 2], str(b))
        # --- dosya kapsamı: ikili, geçersiz UTF-8, .yml, gizli adlar, symlink
        d = klasor("f2", {"SKILL.md": "-\n", "ok.yml": "ok ~/.claude/skills/f2/a\n", "n.md": "ok ~/.claude/skills/f2/a\n", "id_rsa": "~/.claude/skills/f2/a\n",
                          ".npmrc": "~/.claude/skills/f2/a\n", "credentials.json": "~/.claude/skills/f2/a\n"})
        (d / "bad.md").write_bytes(b"\xff\xfe ~/.claude/skills/f2/a\n")
        (d / "bin.txt").write_bytes(b"\0 ~/.claude/skills/f2/a\n")
        dis = kok / "f2-disarda.md"
        dis.write_text("~/.claude/skills/f2/a\n", encoding="utf-8")
        try:
            (d / "link.txt").symlink_to(dis)
        except OSError:
            pass
        test("yol: ok.yml taranır; geçersiz UTF-8 çökertmez, NUL'lu ikili, id_rsa/.npmrc/credentials ve symlink okunmaz",
             sorted(x["dosya"] for x in o.yol_taramasi(d, {"f2"})) == ["n.md", "ok.yml"], str(o.yol_taramasi(d, {"f2"})))
        # --- dayanıklılık: kötü niyetli/bozuk girdi taramayı kilitlemez
        import time as _t
        agir = {"uzun-token": "~/.claude/skills/p1/a.md\n" + "a" * 200_000, "npx-satirlar": "npx skills add x -g\n" * 40_000, "yollar": "~/.claude/skills/p1/a.md\n" * 40_000,
                "tek-satir": "~/.claude/skills/p1/a " * 40_000, "plugin": "${CLAUDE_PLUGIN_ROOT}" * 40_000, "cp-tek-satir": "cp a ~/.claude/skills/x " * 30_000}
        yavas, fazla = [], []
        for ad_, m_ in agir.items():
            t0_ = _t.time()
            bb = tara("p-" + ad_, {"SKILL.md": m_}, {"p-" + ad_, "p1"})
            if _t.time() - t0_ > 8:
                yavas.append((ad_, round(_t.time() - t0_, 1)))
            if len(bb) > 2000:
                fazla.append(ad_)
        test("yol: ağır girdilerde (uzun token, 40 bin npx/yol satırı, tek satırda 40 bin yol) 8 sn altında biter; dosya başına en çok 2000 bulgu", not yavas and not fazla, str((yavas, fazla)))
        b = tara("p2", {"SKILL.md": "oku ./.hidden/run.md\n", ".hidden/run.md": "~/.claude/skills/p2/a\n"})
        test("yol: atıf kümesinde './' önekinin noktası gizli klasör adını yemez", b[0]["sinif"] == "ajan", str(b))
        b = tara("q1", {"SKILL.md": "binary: `~/.local/bin/q1`, `${CLAUDE_PLUGIN_ROOT}/bin/q1` (when installed as a plugin), or `~/code/q1/bin/q1`\n"
                                    "run ${CLAUDE_PLUGIN_ROOT}/bin/other\n"})
        test("yol: eklenti-kok-yol 'alternatif' bayrağı yalnız seçenekli satırda", [(x["satir"], x.get("alternatif", False)) for x in b] == [(1, True), (2, False)], str(b))
        # --- adlar, kardeş
        sifirla()
        t1 = {"id": "x", "ad": "x@kaynak", "klasor_adi": "skill", "kaynak_yol": "plugins/wake", "repo": "o/lemo-wake"}
        test("skill_adlari: @kaynak eksiz ad, genel klasör adı ('skill') hariç, kaynak_yol son klasörü, tek skilli repo adı",
             o.skill_adlari(t1) == {"x", "wake"} and o.skill_adlari(t1, [t1]) == {"x", "wake", "lemo-wake"}, str(o.skill_adlari(t1, [t1])))
        t2 = {"id": "y", "ad": "lemo-wake", "klasor_adi": "lemo-wake", "kaynak_yol": "skills/lemo-wake", "repo": "o/lemo-wake"}
        test("skill_adlari: repo adı aynı repodaki başka skill o adı taşıyorsa kendi adı sayılmaz; genel repo adı eklenmez",
             "lemo-wake" not in o.skill_adlari(t1, [t1, t2]) and "skills" not in o.skill_adlari({"id": "q", "ad": "q", "repo": "a/skills", "kaynak_yol": ""}, [{"id": "q", "ad": "q", "repo": "a/skills", "kaynak_yol": ""}]))
        sifirla()
        k1 = {"id": "geo", "ad": "geo", "klasor_adi": "geo", "kaynak_yol": "geo", "repo": "o/g"}
        k2 = {"id": "geo-x", "ad": "geo-x", "klasor_adi": "geo-x", "kaynak_yol": "skills/geo-x", "repo": "o/g"}
        k3 = {"id": "geo@baska", "ad": "geo@baska", "klasor_adi": "geo", "kaynak_yol": "x/geo", "repo": "baska/g"}
        k4 = {"id": "z", "ad": "z", "klasor_adi": "geo", "kaynak_yol": "x/geo", "repo": "o/g"}
        test("kardes_coz: aynı repoda tek aday döner; başka repodaki aynı ad sayılmaz", o.kardes_coz(k2, "geo", [k1, k2, k3]) is k1 and o.kardes_coz(k3, "geo-x", [k1, k2, k3]) is None)
        sifirla()
        test("kardes_coz: iki aday varsa ya da hiç yoksa None; kendisi aday değil", o.kardes_coz(k2, "geo", [k1, k2, k4]) is None and o.kardes_coz(k2, "yok", [k1, k2]) is None
             and o.kardes_coz(k1, "geo", [k1, k2]) is None)
        # --- skill_yol_taramasi: kardeşin arşivine bakar
        sifirla()
        sib = kayit("sib", dosyalar={"SKILL.md": "-\n", "scripts/f.py": "-\n"})
        ben = kayit("ben", dosyalar={"SKILL.md": "~/.claude/skills/sib/scripts/f.py ve ~/.claude/skills/sib/scripts/yok.py ve ../sib/SKILL.md ve ~/.claude/skills/uzak/x\n"})
        uzak = kayit("uzak", repo="baska/r")
        lst = [sib, ben, uzak]
        b = o.skill_yol_taramasi(ben, lst)
        test("skill_yol_taramasi: kardeş çözülür (kardes_id), var kardeşin arşiv klasörüne göre; başka repodakine kardeş denmez",
             sorted((x["ham"], x["hedef"], x.get("kardes_id"), x["var"], x["cevrilebilir"]) for x in b) ==
             sorted([("~/.claude/skills/sib/scripts/f.py", "sib", "sib", True, True), ("~/.claude/skills/sib/scripts/yok.py", "sib", "sib", False, False),
                     ("../sib/SKILL.md", "sib", "sib", True, True), ("~/.claude/skills/uzak/x", "uzak", None, None, False)]), str(b))
        b[0]["tur"] = "bozuk"
        test("skill_yol_taramasi: önbellek kopya döner (çağıran bozamaz)", o.skill_yol_taramasi(ben, lst)[0]["tur"] != "bozuk")
        # --- yol_degerlendir
        d0 = o.yol_degerlendir(ben, lst)
        kodlar0 = [(sv, kod) for sv, kod, _ in d0["satirlar"]]
        test("yol_degerlendir: kurulacak_idler None -> kardeş BİLGİ 'kardeşle düzelir', dosyası olmayan UYARI, bilinmeyen kardeş yok sayılmaz",
             ("BİLGİ", "kardes-eksik") in kodlar0 and ("UYARI", "kardes-eksik") in kodlar0 and d0["kardesler"]["sib"]["kurulu"] is None
             and d0["kardesler"]["sib"]["id"] == "sib" and d0["sutun"] == "cozulemez" and ("UYARI", "genel-yol") in kodlar0, str(d0["satirlar"]))
        d1 = o.yol_degerlendir(ben, lst, {"sib", "ben"})
        test("yol_degerlendir: kardeş kuruluyorsa kardes-yol BİLGİ (UYARI kardes-eksik yalnız eksik dosya için)",
             ("BİLGİ", "kardes-yol") in [(a, b_) for a, b_, _ in d1["satirlar"]] and d1["kardesler"]["sib"]["kurulu"] is True
             and [x for x in d1["satirlar"] if x[1] == "kardes-eksik" and x[0] == "UYARI" and "dosya arşivde yok" in x[2]], str(d1["satirlar"]))
        d2 = o.yol_degerlendir(kayit("ben2", dosyalar={"SKILL.md": "~/.claude/skills/sib/scripts/f.py\n"}, repo="o/r"), lst, {"ben2"})
        test("yol_degerlendir: kardeş kurulmuyorsa UYARI kardes-eksik, sütun kardesle-duzelir", d2["satirlar"][0][:2] == ("UYARI", "kardes-eksik") and d2["sutun"] == "kardesle-duzelir", str(d2))
        e = kayit("kend", dosyalar={"SKILL.md": "~/.claude/skills/kend/a.md\n", "a.md": "-\n", "scripts/s.py": 'X="~/.claude/skills/kend/a.md"\n',
                                    "README.md": "~/.claude/skills/kend/yok.md ${CLAUDE_PLUGIN_ROOT}/x/y\n"})
        d3 = o.yol_degerlendir(e, [e])
        test("yol_degerlendir: kendi yolu çevrilecek (BİLGİ), kodda kalan UYARI genel-yol; doküman sınıfı satır üretmez ama sayıma girer",
             [(a, b_) for a, b_, _ in d3["satirlar"]] == [("BİLGİ", "yol-yerellestirme"), ("UYARI", "genel-yol")] and len(d3["cevrilecek"]) == 1
             and d3["sayim"] == {"genel-kendi": 3, "eklenti-kok-yol": 1} and d3["sutun"] == "cozulemez", str(d3))
        k = kayit("kok", dosyalar={"SKILL.md": "node ${CLAUDE_PLUGIN_ROOT}/scripts/x.mjs\n"})
        d4 = o.yol_degerlendir(k, [k])
        test("yol_degerlendir: eklenti kökü yolu UYARI eklenti-koku, sütun paket-gerekli", d4["satirlar"][0][:2] == ("UYARI", "eklenti-koku") and d4["sutun"] == "paket-gerekli", str(d4))
        t0 = kayit("temiz", dosyalar={"SKILL.md": "yok\n"})
        test("yol_degerlendir: bulgu yoksa temiz, satır yok", o.yol_degerlendir(t0, [t0]) == {"satirlar": [], "sayim": {}, "cevrilecek": [], "kardesler": {}, "sutun": "temiz"})
        y = kayit("yz", dosyalar={"SKILL.md": "## Install\nnpx skills add o/r --skill yz -g\n"})
        dy = o.yol_degerlendir(y, [y])
        test("yol_degerlendir: kurulum bandı genele-yazar yalnız sayılır (satır yok)", dy["satirlar"] == [] and dy["sutun"] == "yalniz-sayim" and dy["sayim"] == {"genele-yazar": 1}, str(dy))
        yk = kayit("ykop", dosyalar={"SKILL.md": "cp -r a ~/.claude/skills/ykop\n"})
        test("yol_degerlendir: ajan dosyasında genele-kopyalar UYARI genele-yazabilir",
             [(a, b_) for a, b_, _ in o.yol_degerlendir(yk, [yk])["satirlar"]] == [("UYARI", "genele-yazabilir")])
        # ===== değerlendirme: her satır kodu ve sütun (parametrik)
        def deg(ad, dosyalar, extra=(), kur=None, repo="o/r", kaynak_yol=None):
            sifirla()
            s_ = kayit(ad, repo=repo, kaynak_yol=kaynak_yol, dosyalar=dosyalar)
            lst_ = [s_, *extra]
            return s_, lst_, o.yol_degerlendir(s_, lst_, kur)

        kd = lambda d_: sorted({(a_, b_) for a_, b_, _ in d_["satirlar"]})  # noqa: E731
        sibx = kayit("sibx", dosyalar={"SKILL.md": "-\n", "a.md": "-\n"})
        uzakb = kayit("uzakb", repo="baska/r2")
        vaka = [
            ("dis1", {"SKILL.md": "${CLAUDE_SKILL_DIR}/../../hooks/h.sh\n"}, [("UYARI", "skil-disi-yol")], "paket-gerekli"),
            ("ort1", {"SKILL.md": "~/.claude/skills/_shared/a.py\n"}, [("UYARI", "genel-yol")], "cozulemez"),
            ("ek1", {"SKILL.md": "${CLAUDE_PLUGIN_ROOT}/skills/ek1/yok.md\n"}, [("UYARI", "eklenti-koku")], "paket-gerekli"),
            ("yk1", {"SKILL.md": "~/.claude/skills/yk1/yok.md\n"}, [("UYARI", "genel-yol")], "paket-gerekli"),
            ("kd1", {"SKILL.md": "~/.claude/skills/kd1/x.md\n", "x.md": "-\n"}, [("BİLGİ", "yol-yerellestirme")], "kurulumda-duzelir"),
            ("ya1", {"SKILL.md": "## Kullanım\nnpx skills add o/r --skill ya1 -g\n"}, [("BİLGİ", "genele-yazabilir")], "yalniz-sayim"),
            ("ku1", {"SKILL.md": "x\n", "scripts/setup.sh": "~/.claude/skills/ku1/a.md\n", "a.md": "-\n"}, [("UYARI", "genel-yol")], "cozulemez"),
            ("km1", {"SKILL.md": "~/.claude/skills/km1/a.md ve .claude/skills/km1/b.md\n", "a.md": "-\n"}, [("UYARI", "genel-yol")], "cozulemez"),
            ("kc1", {"SKILL.md": "git clone u ~/.claude/skills/kc1/x.md\n", "x.md": "-\n"}, [("UYARI", "genele-yazabilir")], "yalniz-sayim"),
            ("at1", {"SKILL.md": 'SKILL_DIR="~/.claude/skills/at1"\npython "$SKILL_DIR/scripts/x.py"\n'}, [("UYARI", "genel-yol")], "cozulemez"),
            ("ec1", {"SKILL.md": "x\n", "scripts/s.sh": 'echo "kullanım: ~/.claude/skills/ec1/a.md"\n', "a.md": "-\n"}, [], "yalniz-sayim"),
            ("al1", {"SKILL.md": "`${CLAUDE_PLUGIN_ROOT}/bin/al1` (when installed as a plugin), or `~/code/al1/bin/al1`\n"}, [("BİLGİ", "eklenti-koku")], "yalniz-sayim"),
            ("eg1", {"SKILL.md": "e.g. ~/.claude/skills/eg1/a.md burada\n", "a.md": "-\n"}, [], "yalniz-sayim"),
            ("kp1", {"SKILL.md": "~/.claude/skills/sibx/a.md\n${CLAUDE_PLUGIN_ROOT}/scripts/x.sh\n"}, [("BİLGİ", "kardes-eksik"), ("UYARI", "eklenti-koku")], "paket-gerekli"),
            ("kp2", {"SKILL.md": "~/.claude/skills/kp2/x.md\n~/.claude/skills/sibx/a.md\n", "x.md": "-\n"}, [("BİLGİ", "kardes-eksik"), ("BİLGİ", "yol-yerellestirme")], "kardesle-duzelir"),
        ]
        for ad_, dos_, bek_, sut_ in vaka:
            _, _, dd_ = deg(ad_, dos_, [sibx, uzakb])
            test(f"yol_degerlendir [{ad_}]: kodlar {bek_} sütun {sut_}", kd(dd_) == sorted(bek_) and dd_["sutun"] == sut_, str(dd_["satirlar"]) + " " + dd_["sutun"])
        _, _, dd_ = deg("kk9", {"SKILL.md": "x\n", "scripts/run.sh": "~/.claude/skills/sibx/a.md\n"}, [sibx], kur={"sibx", "kk9"})
        test("yol_degerlendir: kardeş kuruluyor ama bulgu betik içinde -> BİLGİ kardes-yol + UYARI genel-yol, sütun cozulemez",
             kd(dd_) == [("BİLGİ", "kardes-yol"), ("UYARI", "genel-yol")] and dd_["sutun"] == "cozulemez", str(dd_["satirlar"]))
        # --- doküman sınıfı hiç satır üretmez (her tür sayıma girer)
        _, _, dd_ = deg("dk1", {"SKILL.md": "x\n", "README.md": "~/.claude/skills/_shared/a.py\n~/.claude/skills/uzakb/x.md\n${CLAUDE_SKILL_DIR}/../../h.sh\n../uzakb/x.md\n"
                                                    "cp -r a ~/.claude/skills/z\n${CLAUDE_PLUGIN_ROOT}/skills/uzakb/SKILL.md\n${CLAUDE_PLUGIN_ROOT}/x/y.sh\n"
                                                    "## Kullanım\nnpx skills add o/r --skill q -g\n~/.claude/skills/dk1/yok.md\n"}, [uzakb])
        test("yol_degerlendir: doküman sınıfı bulguları satır üretmez, tüm türler sayıma girer, sütun yalniz-sayim",
             dd_["satirlar"] == [] and dd_["sutun"] == "yalniz-sayim" and {"ortak-dizin", "genel-baska", "skil-disi-yol", "kardes-goreli", "genele-kopyalar", "eklenti-kardes",
                                                                           "eklenti-kok-yol", "genele-yazar", "genel-kendi"} <= set(dd_["sayim"]), str(dd_))
        # --- gövde biçimi
        _, _, dd_ = deg("gv1", {"SKILL.md": "x\n", "scripts/p.sh": "run ~/.claude/skills/gv1/a1.md ve ~/.claude/skills/gv1/a1.md\nrun ~/.claude/skills/gv1/a2.md\n"
                                                                  "run ~/.claude/skills/gv1/a3.md\nrun ~/.claude/skills/gv1/a4.md\nrun ~/.claude/skills/gv1/a5.md\n",
                                "a1.md": "-", "a2.md": "-", "a3.md": "-", "a4.md": "-", "a5.md": "-"})
        gv_ = dd_["satirlar"][0][2] if dd_["satirlar"] else ""
        test("yol_degerlendir: gövde en çok 3 örnek, tekilleştirilmiş, '(+N)' eki", gv_.count("scripts/p.sh:") == 3 and "(+2)" in gv_, gv_)
        _, _, d_a = deg("gv2", {"SKILL.md": "~/.claude/skills/uzakb/x.md\n"}, [uzakb])
        _, _, d_b = deg("gv3", {"SKILL.md": "~/.claude/skills/.system/imagegen/SKILL.md\n"}, [uzakb])
        test("yol_degerlendir: çözülemeyen genel-baska gövdesi 'kütüphanede başka yerde var' / 'kütüphanede yok' ayrımını yapar",
             "başka yerde var: uzakb" in d_a["satirlar"][0][2] and "kütüphanede yok" in d_b["satirlar"][0][2], str((d_a["satirlar"], d_b["satirlar"])))
        # --- göreli kardeş (../<skill>/): çok adaylıda aynı üst klasör ipucu, çözülemezse UYARI
        sifirla()
        uc1 = kayit("uc", repo="o/g", kaynak_yol="plugins/a/skills/uc")
        uc2 = kayit("uc@b", repo="o/g", kaynak_yol="plugins/b/skills/uc")
        uc2["klasor_adi"] = "uc"
        gor = kayit("gor1", repo="o/g", kaynak_yol="plugins/a/skills/gor1", dosyalar={"SKILL.md": "oku ../uc/SKILL.md ve ${CLAUDE_PLUGIN_ROOT}/skills/uc/SKILL.md\n"})
        gor2 = kayit("gor2", repo="o/g", kaynak_yol="plugins/c/skills/gor2", dosyalar={"SKILL.md": "oku ../uc/SKILL.md\n"})
        lst_g = [uc1, uc2, gor, gor2]
        test("kardes_coz: çok adaylıda 'ust' ipucu aynı üst klasördekini seçer; ipucu yoksa ya da eşleşme tek değilse None",
             o.kardes_coz(gor, "uc", lst_g) is None and o.kardes_coz(gor, "uc", lst_g, "ust") is uc1 and o.kardes_coz(gor, "uc", lst_g, "kok") is uc1
             and o.kardes_coz(gor2, "uc", lst_g, "ust") is None)
        bg = {x["tur"]: x.get("kardes_id") for x in o.skill_yol_taramasi(gor, lst_g)}
        test("skill_yol_taramasi: kardes-goreli ve eklenti-kardes çok adaylıda ipucuyla çözülür", bg == {"kardes-goreli": "uc", "eklenti-kardes": "uc"}, str(bg))
        dg_ = o.yol_degerlendir(gor2, lst_g)
        test("yol_degerlendir: çözülemeyen kardes-goreli UYARI genel-yol, sütun cozulemez (sessiz kalmaz)",
             [(a_, b_) for a_, b_, _ in dg_["satirlar"]] == [("UYARI", "genel-yol")] and "göreli kardeş" in dg_["satirlar"][0][2] and dg_["sutun"] == "cozulemez", str(dg_["satirlar"]))
        # --- skill_yol_taramasi: skil-disi-yol/eklenti-kardes kardeş çözümü, önbellek anahtarı, liste büyümesi
        sifirla()
        sb = kayit("sbk", dosyalar={"SKILL.md": "-\n", "scripts/f.py": "-\n"})
        bn = kayit("bnk", dosyalar={"SKILL.md": "${CLAUDE_SKILL_DIR}/../sbk/scripts/f.py ve ${CLAUDE_PLUGIN_ROOT}/.claude/skills/sbk/SKILL.md\n"})
        bb = {x["tur"]: (x.get("kardes_id"), x["var"]) for x in o.skill_yol_taramasi(bn, [sb, bn])}
        test("skill_yol_taramasi: skil-disi-yol (tek '..') ve eklenti-kardes kardeş çözülür, var kardeşin arşivine göre",
             bb == {"skil-disi-yol": ("sbk", True), "eklenti-kardes": ("sbk", True)}, str(bb))
        sifirla()
        bn2 = kayit("bn2", dosyalar={"SKILL.md": "~/.claude/skills/yeni/x.md\n"})
        yeni = kayit("yeni", dosyalar={"SKILL.md": "-\n", "x.md": "-\n"})
        ilk = o.skill_yol_taramasi(bn2, [bn2, uzakb])
        o._SKILLER_INDEKS[:] = [None, 0, None]
        ikinci = o.skill_yol_taramasi(bn2, [bn2, yeni])
        test("skill_yol_taramasi: aynı skill farklı liste ile (kardeş sonradan eklendi) eski önbelleği döndürmez",
             ilk[0].get("kardes_id") is None and ikinci[0].get("kardes_id") == "yeni", str((ilk, ikinci)))
        sifirla()
        lst_i = [bn2]
        o.kardes_coz(bn2, "yeni", lst_i)
        lst_i.append(yeni)
        test("kardes_coz: liste büyüyünce indeks yenilenir (yeni eklenen skill bulunur)", o.kardes_coz(bn2, "yeni", lst_i) is yeni)
        yol_a = kayit("hh1", dosyalar={"SKILL.md": "~/.claude/skills/hh1/a.md\n", "a.md": "-\n"})
        a1_ = o.skill_yol_taramasi(yol_a, [yol_a])
        (Path(yol_a["yol"]) / "a.md").unlink()
        a2_ = o.skill_yol_taramasi(dict(yol_a, klasor_hash="yeni-hash"), [yol_a])
        test("skill_yol_taramasi: klasor_hash değişince önbellek yenilenir (dosya silindi -> var False)", a1_[0]["var"] is True and a2_[0]["var"] is False, str((a1_, a2_)))
        test("skill_adlari: klasor_adi kaynağı (genel olmayan klasor_adi, kaynak_yol son klasöründen farklı)",
             "foo" in o.skill_adlari({"id": "x", "ad": "x", "klasor_adi": "foo", "kaynak_yol": "a/b", "repo": "o/r"}))
        # --- istisna
        sifirla()
        ik = kayit("ik", repo="o/ik", kaynak_yol="skills/ik", dosyalar={"SKILL.md": "${CLAUDE_PLUGIN_ROOT}/scripts/a.sh\n", "references/r.md": "${CLAUDE_PLUGIN_ROOT}/lib/b.sh\n"})
        tum = o.skill_yol_taramasi(ik, [ik])
        anahtar = o.istisna_anahtari(ik)
        test("istisna_anahtari: repo::kaynak_yol", anahtar == "o/ik::skills/ik")
        h = o.bulgu_hash([x for x in tum if x["tur"] == "eklenti-kok-yol"])
        satir_kayma = [dict(x, satir=x["satir"] + 5) for x in tum]
        test("bulgu_hash: satır numarasından bağımsız, içerik değişince değişir", o.bulgu_hash(satir_kayma) == o.bulgu_hash(tum) and o.bulgu_hash(tum[:1]) != o.bulgu_hash(tum))
        kay = {"tur": "eklenti-kok-yol", "dosyalar": ["SKILL.md", "references/r.md"], "karar": "ornek-metin", "neden": "t", "tarih": "2026-01-01", "bulgu_hash": h}
        ist = {anahtar: {"ad": "ik", "kayitlar": [kay]}}
        kal, isl, esk = o.istisna_uygula(ik, tum, ist)
        test("istisna_uygula: dosya listesiyle kapsanan bulgular istisnalı, kalan boş", len(isl) == 2 and kal == [] and esk == [], str((kal, isl, esk)))
        kal, isl, esk = o.istisna_uygula(ik, tum, {anahtar: {"kayitlar": [dict(kay, dosyalar=["SKILL.md"], bulgu_hash=o.bulgu_hash(tum[:1]))]}})
        test("istisna_uygula: yalnız listedeki dosya kapsanır (diğer dosyadaki bulgu kalır)", len(isl) == 1 and len(kal) == 1 and kal[0]["dosya"] == "references/r.md")
        kal, isl, esk = o.istisna_uygula(ik, tum, {anahtar: {"kayitlar": [dict(kay, dosyalar=[], hedefler=[])]}})
        test("istisna_uygula: hedefler ve dosyalar boşsa kayıt geçersiz (kör istisna yok), bulgular kalır", isl == [] and len(kal) == len(tum))
        kal, isl, esk = o.istisna_uygula(ik, tum, {anahtar: {"kayitlar": [dict(kay, bulgu_hash="0" * 64)]}})
        test("istisna_uygula: bulgu_hash tutmuyorsa kayıt düşer, bulgular kalır, eskiyen bildirilir", isl == [] and len(kal) == len(tum) and len(esk) == 1)
        kal, isl, esk = o.istisna_uygula(ik, tum, {"o/baska::x": {"kayitlar": [kay]}})
        test("istisna_uygula: başka skill'in kaydı uygulanmaz", isl == [] and esk == [])
        dg = o.yol_degerlendir(ik, [ik], istisnalar=ist)
        test("yol_degerlendir: istisnalı skill tek satır BİLGİ yol-istisna, sütun istisna",
             [(a, b_) for a, b_, _ in dg["satirlar"]] == [("BİLGİ", "yol-istisna")] and dg["sutun"] == "istisna" and dg["sayim"] == {"eklenti-kok-yol": 2}, str(dg))
        dg = o.yol_degerlendir(ik, [ik], istisnalar={anahtar: {"kayitlar": [dict(kay, bulgu_hash="0" * 64)]}})
        test("yol_degerlendir: eskiyen istisna UYARI istisna-eskidi verir, bulgu UYARI olarak geri gelir",
             ("UYARI", "istisna-eskidi") in [(a, b_) for a, b_, _ in dg["satirlar"]] and ("UYARI", "eklenti-koku") in [(a, b_) for a, b_, _ in dg["satirlar"]])
        # --- dosya + dogrula tarafı
        dosya = kok / "yol-istisnalari.json"
        o.YOL_ISTISNA = dosya
        test("yol_istisna_denetimi: dosya yoksa sessiz, yol_istisnalari() boş", o.yol_istisna_denetimi(lst) == ([], []) and o.yol_istisnalari() == {})
        kayit_gecerli = {"tur": "eklenti-kok-yol", "dosyalar": ["SKILL.md", "references/r.md"], "karar": "ornek-metin", "neden": "t", "tarih": "2026-01-01", "bulgu_hash": h}

        def yaz(ist_):
            dosya.write_text(json.dumps({"_aciklama": "t", "istisnalar": ist_}), encoding="utf-8")
            return o.yol_istisna_denetimi([ik])
        test("yol_istisna_denetimi: geçerli dosya hata/uyarı vermez ve uygulanır", yaz({anahtar: {"ad": "ik", "kayitlar": [kayit_gecerli]}}) == ([], [])
             and anahtar in o.yol_istisnalari())
        # ===== istisna: eşleme kuralları, varsayılan dosya, dayanıklılık
        sifirla()
        bar_s, baz_s = kayit("bar", repo="baska/r3"), kayit("baz", repo="baska/r3")
        ih = kayit("ih", repo="o/ih", kaynak_yol="skills/ih", dosyalar={"SKILL.md": "~/.claude/skills/bar/x.md ve ~/.claude/skills/baz/y.md\n"})
        lst_h = [ih, bar_s, baz_s]
        tum_h = o.skill_yol_taramasi(ih, lst_h)
        ak_h = o.istisna_anahtari(ih)
        bar_b = [x for x in tum_h if x["hedef"] == "bar"]
        kh = {"tur": "genel-baska", "hedefler": ["bar"], "karar": "kabul", "neden": "t", "tarih": "2026-01-01", "bulgu_hash": o.bulgu_hash(bar_b)}
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {ak_h: {"kayitlar": [kh]}})
        test("istisna_uygula: 'hedefler' ile eşleşme (karar kabul): yalnız hedef bar kapsanır, baz kalır", [x["hedef"] for x in isl] == ["bar"] and [x["hedef"] for x in kal] == ["baz"] and esk == [], str((kal, isl, esk)))
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {ak_h: {"kayitlar": [dict(kh, tur="genel-kendi")]}})
        test("istisna_uygula: aynı hedef yanlış tür kapsamaz (bulgu_hash tutmadığı için eskiyen)", isl == [] and len(kal) == len(tum_h) and len(esk) == 1)
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {ak_h: {"kayitlar": [{k_: v_ for k_, v_ in kh.items() if k_ != "bulgu_hash"}]}})
        test("istisna_uygula: bulgu_hash'siz kayıt asla kapsamaz (kör istisna yok)", isl == [] and len(kal) == len(tum_h))
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {ak_h: {"kayitlar": [dict(kh, hedefler=["yokbir"], bulgu_hash=o.bulgu_hash([]))]}})
        test("istisna_uygula: hiçbir bulguyu kapsamayan geçerli kayıt bulguları değiştirmez ve eskiyen sayılmaz", isl == [] and len(kal) == len(tum_h) and esk == [])
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {ak_h: {"kayitlar": [dict(kh, karar="belki")]}})
        test("istisna_uygula: geçersiz kayıt eskiyen listesine alınmaz, sessizce yok sayılır", isl == [] and esk == [])
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {"istisnalar": {ak_h: {"kayitlar": [kh]}}})
        test("istisna_uygula: tam dosya sözlüğü biçimi ({'istisnalar': …}) kabul edilir", len(isl) == 1)
        kal, isl, esk = o.istisna_uygula(ih, tum_h, {"O/Ih::skills/ih": {"kayitlar": [kh]}})
        test("istisna_uygula: anahtar büyük/küçük harfe duyarsız eşlenir (denetimle aynı kural)", len(isl) == 1)
        h_a, h_b = {"dosya": "a", "ham": "h"}, {"dosya": "b", "ham": "h"}
        test("bulgu_hash: sıradan bağımsız; (dosya, ham) çiftinin ikisi de hash'e girer",
             o.bulgu_hash([h_a, h_b]) == o.bulgu_hash([h_b, h_a]) and o.bulgu_hash([h_a]) != o.bulgu_hash([h_b]) and o.bulgu_hash([h_a]) != o.bulgu_hash([dict(h_a, ham="h2")]))
        # --- bozuk yapılar çökertmez
        kotu = [[1], {"kayitlar": None}, {"kayitlar": [1, "x", None]}, {"kayitlar": [dict(kh, hedefler=[[1]])]}, {"kayitlar": [dict(kh, hedefler=[None])]},
                {"kayitlar": [dict(kh, hedefler=[], dosyalar=[{"a": 1}])]}, {"kayitlar": [dict(kh, hedefler="bar")]}, "metin"]
        cokme = []
        for g_ in kotu:
            try:
                o.istisna_uygula(ih, tum_h, {ak_h: g_})
                o.yol_degerlendir(ih, lst_h, istisnalar={ak_h: g_})
            except Exception as e_:  # noqa: BLE001
                cokme.append((g_, repr(e_)))
        test("istisna_uygula / yol_degerlendir: bozuk istisna yapıları (liste, None, iç içe liste, [null], metin) çökertmez", cokme == [], str(cokme))
        test("istisna_kaydi_gecerli: hedefler/dosyalar elemanları boş olmayan metin olmalı ([null], [[1]], ['']) geçersiz",
             not any(o.istisna_kaydi_gecerli(dict(kh, hedefler=h_)) for h_ in ([None], [[1]], [""], ["a", 1])) and o.istisna_kaydi_gecerli(kh))
        sifirla()
        hh_, uu_ = yaz({ak_h: {"kayitlar": [dict(kh, hedefler=[None])]}})
        hh2_, uu2_ = yaz({ak_h: {"kayitlar": [dict(kh, hedefler=[[1]])]}})
        test("yol_istisna_denetimi: elemanları metin olmayan kayıt çökertmez, HATA verir", len(hh_) == 1 and len(hh2_) == 1, str((hh_, uu_, hh2_, uu2_)))
        hh_, uu_ = yaz({"O/IK::skills/ik": {"kayitlar": [kayit_gecerli]}})
        test("yol_istisna_denetimi: anahtar büyük/küçük harf farkı hata/uyarı vermez ve kayıt gerçekten uygulanır",
             (hh_, uu_) == ([], []) and len(o.istisna_uygula(ik, tum, None)[1]) == 2, str((hh_, uu_)))
        yaz({anahtar: {"ad": "ik", "kayitlar": [kayit_gecerli]}})
        _kal, _isl, _esk = o.istisna_uygula(ik, tum)
        test("istisna_uygula: istisnalar=None iken YOL_ISTISNA dosyasından okur", len(_isl) == 2 and _kal == [], str((_kal, _isl)))
        dg2 = o.yol_degerlendir(ik, [ik])
        test("yol_degerlendir: istisnalar=None iken dosyadaki kayıt uygulanır (sütun istisna)", dg2["sutun"] == "istisna", str(dg2))
        ic = kayit("ic", repo="o/ic", kaynak_yol="skills/ic", dosyalar={"SKILL.md": "~/.claude/skills/ic/a.md\n", "a.md": "-\n"})
        tum_ic = o.skill_yol_taramasi(ic, [ic])
        ki = {"tur": "genel-kendi", "dosyalar": ["SKILL.md"], "karar": "kabul", "neden": "t", "tarih": "2026-01-01", "bulgu_hash": o.bulgu_hash(tum_ic)}
        d_once = o.yol_degerlendir(ic, [ic], istisnalar={})
        d_ist = o.yol_degerlendir(ic, [ic], istisnalar={o.istisna_anahtari(ic): {"kayitlar": [ki]}})
        test("yol_degerlendir: istisnalı bulgu otomatik çevrilmez (cevrilecek boş), tek BİLGİ yol-istisna satırı bulgu sayısını söyler",
             len(d_once["cevrilecek"]) == 1 and d_ist["cevrilecek"] == [] and [(a_, b_) for a_, b_, _ in d_ist["satirlar"]] == [("BİLGİ", "yol-istisna")]
             and "1 bulgu" in d_ist["satirlar"][0][2], str(d_ist))
        yt2 = subprocess.run([sys.executable, str(KOK / "araclar" / "yol-tara.py"), "--skill"], capture_output=True, text=True)
        yt3 = subprocess.run([sys.executable, str(KOK / "araclar" / "yol-tara.py"), "--bogus"], capture_output=True, text=True)
        test("yol-tara.py: bayrak hatasında (değersiz --skill, bilinmeyen bayrak) da çıkış kodu 0", yt2.returncode == 0 and yt3.returncode == 0, yt2.stderr + yt3.stderr)
        dosya.write_text("{bozuk", encoding="utf-8")
        hh, uu = o.yol_istisna_denetimi([ik])
        test("yol_istisna_denetimi: bozuk JSON HATA; yol_istisnalari() çökmeden {} döner", len(hh) == 1 and uu == [] and o.yol_istisnalari() == {}, str(hh))
        for ad_, bozuk in (("bilinmeyen karar", dict(kayit_gecerli, karar="belki")), ("boş hedefler ve dosyalar", dict(kayit_gecerli, dosyalar=[], hedefler=[])),
                           ("bulgu_hash yok", {a: v for a, v in kayit_gecerli.items() if a != "bulgu_hash"})):
            hh, uu = yaz({anahtar: {"kayitlar": [bozuk]}})
            test(f"yol_istisna_denetimi: {ad_} -> HATA", len(hh) == 1 and uu == [], str((hh, uu)))
        hh, uu = yaz({"o/yok::skills/yok": {"kayitlar": [kayit_gecerli]}})
        test("yol_istisna_denetimi: registry'de karşılığı olmayan anahtar UYARI (hata değil)", hh == [] and len(uu) == 1, str((hh, uu)))
        hh, uu = yaz({anahtar: {"kayitlar": [dict(kayit_gecerli, bulgu_hash="1" * 64)]}})
        test("yol_istisna_denetimi: bulgu_hash tutmuyorsa UYARI", hh == [] and len(uu) == 1 and "bulgu_hash" in uu[0], str((hh, uu)))
        o.YOL_ISTISNA = eski_istisna
        sk = json_oku(KOK / "registry.json")["skiller"]
        hk, _uk = o.yol_istisna_denetimi(sk)  # uyarı (bulgu_hash eskidi) aylık güncellemede meşrudur: dogrula.py gösterir, burada yalnız HATA denetlenir
        test("yol-istisnalari.json (kütüphanedeki) geçerli: hata yok", hk == [], str(hk))
        yt = subprocess.run([sys.executable, str(KOK / "araclar" / "yol-tara.py"), "--skill", "boyle-bir-skill-yok"], capture_output=True, text=True)
        test("yol-tara.py: bilinmeyen skill çıkış kodu 0 ve dosya yazmaz", yt.returncode == 0 and "bulunamadı" in yt.stdout, yt.stdout + yt.stderr)
    finally:
        o.YOL_ISTISNA = eski_istisna
        sifirla()
        shutil.rmtree(kok, ignore_errors=True)


def kurulum_yol_testleri():
    """Kurulum tarafındaki sabit yol çevirisi (skill-ekle.py hazirla/yollari_yerellestir/kur/ekle/guncelle, ortak.onarim_izi): YALNIZ tempfile projeleri.
    Hassas durumlar için tempfile içinde küçük sentetik skill klasörleri, gerçek akışlar için arşivden code-tour kullanılır; arşiv klasörlerine dokunulmaz."""
    import importlib.util
    import re
    import ortak as o
    spec = importlib.util.spec_from_file_location("se_yol", KOK / "araclar" / "skill-ekle.py")
    se = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(se)
    kok = Path(tempfile.mkdtemp(prefix="kurulum-yol-test-"))
    eski_istisna = o.YOL_ISTISNA
    sayac = [0]

    def sifirla():
        o._YOL_ONBELLEK.clear()
        o._SKILLER_INDEKS[:] = [None, 0, None]

    def ozet(d: Path):
        """{göreli yol: içerik özeti ya da 'symlink->hedef'}"""
        sonuc = {}
        for p in sorted(d.rglob("*")):
            rel = str(p.relative_to(d))
            if p.is_symlink():
                sonuc[rel] = "symlink->" + str(p.readlink())
            elif p.is_file():
                sonuc[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
        return sonuc

    def fm(ad):
        return f"---\nname: {ad}\ndescription: test skill\n---\n"

    def kayit(ad, dosyalar, repo="o/r", varyant=None, **ek):
        sayac[0] += 1
        d = kok / "arsiv" / f"{sayac[0]}-{ad}"
        for rel, m in {"SKILL.md": fm(ad) + "x\n", **dosyalar}.items():
            (d / rel).parent.mkdir(parents=True, exist_ok=True)
            (d / rel).write_text(m, encoding="utf-8")
        s = {"id": ad, "ad": ad, "klasor_adi": ad, "kaynak_yol": f"skills/{ad}", "repo": repo, "yol": str(d), "klasor_hash": f"h{sayac[0]}",
             "commit": "c1", **ek}
        if varyant:
            vd = kok / "arsiv" / f"{sayac[0]}-{ad}-claude"
            for rel, m in {"SKILL.md": fm(ad) + "x\n", **varyant}.items():
                (vd / rel).parent.mkdir(parents=True, exist_ok=True)
                (vd / rel).write_text(m, encoding="utf-8")
            s["varyantlar"] = {"claude": str(vd)}
        return s

    def yeni_proje():
        return Path(tempfile.mkdtemp(dir=kok, prefix="p-"))

    def okulines(p: Path):
        return p.read_text(encoding="utf-8").split("\n")

    def kur_dongusu(liste, secilen, proje, codex=True, adlar_ek=None, kilit=None):
        """ekle()'nin kur döngüsünün aynısı: (kilit, {id: kardeş haritası}, {id: uyarılar})"""
        kur_l = {x["id"]: (x, set()) for x in secilen}
        adlar = {x["id"]: (adlar_ek or {}).get(x["id"], x["ad"]) for x in secilen}
        kilit = kilit or {"surum": 3, "skiller": {}, "roller": []}
        haritalar, uyarilar = {}, {}
        for s in secilen:
            ad = adlar[s["id"]]
            kardes = se.kardes_haritasi(s, liste, kilit, kur_l, adlar)
            uyarilar[s["id"]] = se.kur(s, proje, ad, kardes, codex, liste)
            se.kayit_guncelle(kilit, proje, ad, s, kardes=kardes, skiller=liste)
            haritalar[s["id"]] = kardes
        return kilit, haritalar, uyarilar

    def on(s, liste, secilen=None, kilitli=None, adlar_ek=None):
        """on_kontrol'ün sabit yol satırları: [(seviye, kod, mesaj)]"""
        secilen = secilen or [s]
        kur_l = {x["id"]: (x, set()) for x in secilen}
        adlar = {x["id"]: (adlar_ek or {}).get(x["id"], x["ad"]) for x in secilen}
        kilit = {"surum": 3, "skiller": dict(kilitli or {}), "roller": []}
        kidler = set(kur_l) | {x["id"] for k in kilit["skiller"].values() if (x := se.kaynak_bul(liste, k))}
        r = se.Rapor()
        se.sabit_yol_satirlari(r, s, adlar[s["id"]], liste, kilit, kur_l, adlar, kidler)
        return r.satirlar

    def sk_(rows):
        return sorted({(a, b) for a, b, _ in rows})

    try:
        sk = json_oku(KOK / "registry.json")["skiller"]
        ct = next(x for x in sk if x["id"] == "code-tour")
        ct_arsiv = KOK / ct["yol"]
        ct_once = ozet(ct_arsiv)

        # ============ a. kur() dalları: kendi sabit yolu çevrilir, hedef kurulan kopyada VAR
        ana_dosya = {"SKILL.md": fm("yt-ana") + "# yt-ana\nRun `~/.claude/skills/yt-ana/refs/a.md` first.\nAlso ${CLAUDE_PLUGIN_ROOT}/.claude/skills/yt-ana/refs/a.md here.\n",
                     "refs/a.md": "-\n"}
        ana = kayit("yt-ana", ana_dosya)
        liste_a = [ana]
        arsiv_ana_once = ozet(Path(ana["yol"]))
        p = yeni_proje()
        kur_dongusu(liste_a, [ana], p)
        ana_md = p / ".agents" / "skills" / "yt-ana" / "SKILL.md"
        satir = okulines(ana_md)
        test("kur varsayılan: ana kopyada ~/ ve ${CLAUDE_PLUGIN_ROOT} yolları .agents/skills/<ad>/… olur (hedef kopyada var)",
             "Run `.agents/skills/yt-ana/refs/a.md` first." in satir and "Also .agents/skills/yt-ana/refs/a.md here." in satir
             and (p / ".agents" / "skills" / "yt-ana" / "refs" / "a.md").exists() and "~/.claude" not in ana_md.read_text(encoding="utf-8")
             and "CLAUDE_PLUGIN_ROOT" not in ana_md.read_text(encoding="utf-8"), "\n".join(satir))
        test("kur varsayılan: Claude tarafı symlink (aynı içerik), arşiv dosyası değişmedi",
             (p / ".claude" / "skills" / "yt-ana").is_symlink() and "Run `.agents/skills/yt-ana/refs/a.md` first." in okulines(p / ".claude" / "skills" / "yt-ana" / "SKILL.md")
             and (Path(ana["yol"]) / "SKILL.md").read_text(encoding="utf-8") == ana_dosya["SKILL.md"])
        pc = yeni_proje()
        kur_dongusu(liste_a, [ana], pc, codex=False)
        c_md = pc / ".claude" / "skills" / "yt-ana" / "SKILL.md"
        satir = okulines(c_md)
        test("kur sadece-Claude: gerçek kopyada yollar .claude/skills/<ad>/… olur, .agents kopyası yok, hedef var",
             not (pc / ".claude" / "skills" / "yt-ana").is_symlink() and not (pc / ".agents" / "skills" / "yt-ana").exists()
             and "Run `.claude/skills/yt-ana/refs/a.md` first." in satir and "Also .claude/skills/yt-ana/refs/a.md here." in satir
             and (pc / ".claude" / "skills" / "yt-ana" / "refs" / "a.md").exists() and ".agents/skills" not in c_md.read_text(encoding="utf-8"), "\n".join(satir))
        vy = kayit("yt-var", {"SKILL.md": fm("yt-var") + "Run `~/.claude/skills/yt-var/refs/a.md` now.\n", "refs/a.md": "-\n"},
                   varyant={"SKILL.md": fm("yt-var") + "Run `~/.claude/skills/yt-var/refs/a.md` now.\n", "refs/a.md": "-\n", "ek.md": "-\n"})
        pv = yeni_proje()
        kur_dongusu([vy], [vy], pv)
        h_md, c_md = pv / ".agents" / "skills" / "yt-var" / "SKILL.md", pv / ".claude" / "skills" / "yt-var" / "SKILL.md"
        test("kur claude varyantı: ana kopya .agents/skills, varyant kopyası .claude/skills yoluna çevrilir; her ikisinde hedef var",
             "Run `.agents/skills/yt-var/refs/a.md` now." in okulines(h_md) and "Run `.claude/skills/yt-var/refs/a.md` now." in okulines(c_md)
             and not (pv / ".claude" / "skills" / "yt-var").is_symlink() and (pv / ".agents" / "skills" / "yt-var" / "refs" / "a.md").exists()
             and (pv / ".claude" / "skills" / "yt-var" / "refs" / "a.md").exists(), h_md.read_text(encoding="utf-8") + c_md.read_text(encoding="utf-8"))
        pr = yeni_proje()
        kur_dongusu(liste_a, [ana], pr, adlar_ek={"yt-ana": "yt-ana--kutuphane"})
        r_md = pr / ".agents" / "skills" / "yt-ana--kutuphane" / "SKILL.md"
        test("kur: yeniden adlandırılmış kurulumda (yt-ana--kutuphane) sabit yol kurulum adına çevrilir",
             "Run `.agents/skills/yt-ana--kutuphane/refs/a.md` first." in okulines(r_md) and (pr / ".agents" / "skills" / "yt-ana--kutuphane" / "refs" / "a.md").exists(),
             r_md.read_text(encoding="utf-8"))
        # ============ b. kod dosyaları çevrilmez + UYARI genel-yol; doküman sessiz; install*/setup* çevrilmez + UYARI
        yol_satiri = 'P = "~/.claude/skills/yt-kod/refs/a.md"\n'
        kod_d = {"SKILL.md": fm("yt-kod") + "Plain text.\n", "refs/a.md": "-\n",
                 "scripts/run.py": yol_satiri, "scripts/x.js": "const p = '~/.claude/skills/yt-kod/refs/a.md';\n", "scripts/y.sh": "cat ~/.claude/skills/yt-kod/refs/a.md\n",
                 "scripts/z.ts": "const p = '~/.claude/skills/yt-kod/refs/a.md';\n", "scripts/runner": "#!/bin/sh\ncat ~/.claude/skills/yt-kod/refs/a.md\n",
                 "README.md": "See ~/.claude/skills/yt-kod/refs/a.md\n", "scripts/install.sh": "cat ~/.claude/skills/yt-kod/refs/a.md\n",
                 "setup.md": "Use ~/.claude/skills/yt-kod/refs/a.md\n"}
        kod = kayit("yt-kod", kod_d)
        pk = yeni_proje()
        uy_kod = kur_dongusu([kod], [kod], pk)[2]
        inst = pk / ".agents" / "skills" / "yt-kod"
        degismeyen = {rel: (inst / rel).read_text(encoding="utf-8") == m for rel, m in kod_d.items() if rel not in ("SKILL.md",)}
        test("kod dosyaları (.py .js .ts .sh, shebang'li), README, install*/setup* kurulumda çevrilmez (arşivle aynı)",
             all(degismeyen.values()) and len(degismeyen) == 9, str(degismeyen))
        rows = on(kod, [kod])
        gy = [m for sv, kd, m in rows if kd == "genel-yol"]
        test("ön kontrol: kod ve install/setup dosyaları UYARI genel-yol (betik/kurulum dosyası), çevrilecek satırı yok",
             ("UYARI", "genel-yol") in sk_(rows) and gy and all("README.md" not in m for m in gy) and not any(kd == "yol-yerellestirme" for _, kd, _ in rows)
             and "scripts/run.py" in " ".join(gy) and "(+4)" in " ".join(gy) and uy_kod["yt-kod"] == [], str(rows))  # 7 kod/kurucu bulgusu (3 örnek + 4); README sayılmaz
        dok = kayit("yt-dok", {"SKILL.md": fm("yt-dok") + "Plain.\n", "README.md": "See ~/.claude/skills/yt-dok/refs/a.md\n", "docs/x.md": "~/.claude/skills/yt-dok/refs/a.md\n",
                               "NOTICE": "~/.claude/skills/yt-dok/refs/a.md\n", "refs/a.md": "-\n"})
        pd = yeni_proje()
        kur_dongusu([dok], [dok], pd)
        test("doküman sınıfı dosyalar (README, docs/, NOTICE) çevrilmez ve ön kontrolde hiçbir satır/uyarı üretmez",
             on(dok, [dok]) == [] and (pd / ".agents" / "skills" / "yt-dok" / "README.md").read_text(encoding="utf-8") == "See ~/.claude/skills/yt-dok/refs/a.md\n", str(on(dok, [dok])))
        # ============ c. satır kuralları
        sat_d = {"SKILL.md": fm("yt-sat") + "Use ~/.claude/skills/yt-sat/refs/a.md here\nBoth ~/.claude/skills/yt-sat/refs/a.md and ~/.agents/skills/yt-sat/refs/a.md\n"
                 "Dir ~/.claude/skills/yt-sat\nGone ~/.claude/skills/yt-sat/refs/yok.md\nSee references/inst.md\n",
                 "references/inst.md": "cp -r a ~/.claude/skills/yt-sat/refs/a.md\nsee ~/.claude/skills/yt-sat/refs/a.md\n", "refs/a.md": "-\n"}
        sat = kayit("yt-sat", sat_d)
        ps = yeni_proje()
        kur_dongusu([sat], [sat], ps)
        sl = okulines(ps / ".agents" / "skills" / "yt-sat" / "SKILL.md")
        test("satır kuralı: tek köklü ve hedefi olan satır çevrilir (olumlu)", "Use .agents/skills/yt-sat/refs/a.md here" in sl, "\n".join(sl))
        test("satır kuralı: iki yerleşim kökü olan satır çevrilmez",
             "Both ~/.claude/skills/yt-sat/refs/a.md and ~/.agents/skills/yt-sat/refs/a.md" in sl, "\n".join(sl))
        test("satır kuralı: kalan boş yol çevrilmez", "Dir ~/.claude/skills/yt-sat" in sl, "\n".join(sl))
        test("satır kuralı: arşivde hedef dosya yoksa çevrilmez", "Gone ~/.claude/skills/yt-sat/refs/yok.md" in sl, "\n".join(sl))
        test("satır kuralı: kurulum komutu argümanı olan dosyada (cp -r …) hiçbir satır çevrilmez",
             (ps / ".agents" / "skills" / "yt-sat" / "references" / "inst.md").read_text(encoding="utf-8") == sat_d["references/inst.md"])
        # ============ d. kardeş çifti
        ka_d = {"SKILL.md": fm("yt-ka") + "Read ~/.claude/skills/yt-kb/refs/x.md and\n~/.claude/skills/yt-kb/refs/y.md plus own ~/.claude/skills/yt-ka/refs/a.md\n",
                "scripts/r.py": 'P = "~/.claude/skills/yt-kb/refs/x.md"\n', "refs/a.md": "-\n"}
        ka = kayit("yt-ka", ka_d)
        kb = kayit("yt-kb", {"SKILL.md": fm("yt-kb") + "b\n", "refs/x.md": "-\n", "refs/y.md": "-\n"})
        liste_k = [ka, kb]
        rows = on(ka, liste_k, [ka, kb])
        ky = [(sv, m) for sv, kd, m in rows if kd == "kardes-yol"]
        pk2 = yeni_proje()
        kilit_k, harita_k, _ = kur_dongusu(liste_k, [ka, kb], pk2)
        kmd = okulines(pk2 / ".agents" / "skills" / "yt-ka" / "SKILL.md")
        test("kardeş birlikte: kardes-yol BİLGİ tek satır ve sayı gerçek (2 çevrilen yol; betikteki 3. yol sayılmaz)",
             len(ky) == 1 and ky[0][0] == "BİLGİ" and "2 sabit yol" in ky[0][1] and not any(kd == "kardes-eksik" for _, kd, _ in rows), str(rows))
        test("kardeş birlikte: sabit kardeş yolları kardeşin proje içi yoluna çevrilir (hedef var), betikteki yol çevrilmez",
             "Read .agents/skills/yt-kb/refs/x.md and" in kmd and ".agents/skills/yt-kb/refs/y.md plus own .agents/skills/yt-ka/refs/a.md" in kmd
             and (pk2 / ".agents" / "skills" / "yt-kb" / "refs" / "y.md").exists()
             and (pk2 / ".agents" / "skills" / "yt-ka" / "scripts" / "r.py").read_text(encoding="utf-8") == ka_d["scripts/r.py"], "\n".join(kmd))
        test("kardeş birlikte: kilitte genel:<kardeş> girdisi var ve kardeşin kurulum adını tutar",
             kilit_k["skiller"]["yt-ka"]["kardes"] == {"genel:yt-kb": "yt-kb"} and harita_k["yt-ka"]["genel:yt-kb"] == ("yt-kb", True), str(kilit_k["skiller"]["yt-ka"]))
        rows = on(ka, liste_k)
        pe = yeni_proje()
        kilit_e, harita_e, uy_e = kur_dongusu(liste_k, [ka], pe)
        emd = okulines(pe / ".agents" / "skills" / "yt-ka" / "SKILL.md")
        test("kardeş eksik: kardes-eksik UYARI (tek), kardes-yol yok",
             [kd for _, kd, _ in rows].count("kardes-eksik") == 1 and ("UYARI", "kardes-eksik") in sk_(rows) and not any(kd == "kardes-yol" for _, kd, _ in rows), str(rows))
        test("kardeş eksik: sabit kardeş yolları çevrilmez, kilitte genel:<kardeş> yok, kendi yolu yine çevrilir",
             "Read ~/.claude/skills/yt-kb/refs/x.md and" in emd and "~/.claude/skills/yt-kb/refs/y.md plus own .agents/skills/yt-ka/refs/a.md" in emd
             and "genel:yt-kb" not in kilit_e["skiller"]["yt-ka"]["kardes"], "\n".join(emd))
        sifir = kayit("yt-sifir", {"SKILL.md": fm("yt-sifir") + "x\n", "scripts/r.py": 'P = "~/.claude/skills/yt-kb/refs/x.md"\n'})
        rs = on(sifir, [sifir, kb], [sifir, kb])
        test("çevrilebilir bulgu sıfırsa kardes-yol satırı yok (kardeş kurulu olsa bile)", not any(kd == "kardes-yol" for _, kd, _ in rs), str(rs))
        # ============ e. aynı ad, farklı kimlik
        kf = kayit("yt-kf", {"SKILL.md": fm("yt-kf") + "Read ~/.claude/skills/yt-kb/refs/x.md\n"})
        baska_kb = {"id": "yt-kb@x", "ad": "yt-kb", "klasor_adi": "yt-kb", "kaynak_yol": "skills/yt-kb", "repo": "o/x", "yol": kb["yol"], "klasor_hash": "hx", "commit": "c2"}
        liste_f = [kf, kb, baska_kb]
        kilit_f = {"surum": 3, "skiller": {"yt-kb": {"id": "yt-kb@x", "repo": "o/x", "kaynak_yol": "skills/yt-kb", "roller": []}}, "roller": []}
        rows = on(kf, liste_f, [kf], kilit_f["skiller"])
        pf = yeni_proje()
        kilit2, harita_f, _ = kur_dongusu(liste_f, [kf], pf, kilit=json.loads(json.dumps(kilit_f)))
        fmd = okulines(pf / ".agents" / "skills" / "yt-kf" / "SKILL.md")
        test("aynı ad farklı kimlik: kardes-farkli-kaynak UYARI, yol çevrilmez, harita kardeşi kurulu saymaz",
             ("UYARI", "kardes-farkli-kaynak") in sk_(rows) and "Read ~/.claude/skills/yt-kb/refs/x.md" in fmd and "genel:yt-kb" not in harita_f["yt-kf"], str(rows) + "\n".join(fmd))
        # ============ f. aynı kardeş kimliğe göre bir kez (kardes_bagimliliklari + sabit yol)
        ke = kayit("yt-ke", {"SKILL.md": fm("yt-ke") + "Read ~/.claude/skills/yt-kb/refs/x.md and ../yt-kb/refs/y.md\n"},
                   kardes_bagimliliklari={"yt-kb": {"id": "yt-kb", "dosya_sayisi": 1}})
        liste_ke = [ke, kb]
        rows = on(ke, liste_ke)
        eks = [m for _, kd, m in rows if kd == "kardes-eksik"]
        test("tekilleştirme: kardeş kurulmuyorsa hem ../ hem sabit yolla anılsa da TEK kardes-eksik", len(eks) == 1 and "yt-kb" in eks[0], str(rows))
        rows = on(ke, liste_ke, [ke, kb], adlar_ek={"yt-kb": "yt-kb--kutuphane"})
        ky = [m for _, kd, m in rows if kd == "kardes-yol"]
        test("tekilleştirme: kardeş kuruluyorsa TEK kardes-yol satırı, iki parça birleşir (../ yeniden adlandırma + sabit yol sayısı)",
             len(ky) == 1 and "../yt-kb--kutuphane/" in ky[0] and "1 sabit yol" in ky[0] and not any(kd == "kardes-eksik" for _, kd, _ in rows), str(rows))
        # ============ n. tüm yeni ön kontrol kodları ve seviyeleri
        n1 = kayit("yt-n1", {"SKILL.md": fm("yt-n1") + "Run ${CLAUDE_PLUGIN_ROOT}/scripts/x.sh\n"})
        n2 = kayit("yt-n2", {"SKILL.md": fm("yt-n2") + "Run ${CLAUDE_SKILL_DIR}/../../hooks/h.sh\n"})
        n3 = kayit("yt-n3", {"SKILL.md": fm("yt-n3") + "cp -r x ~/.claude/skills/baska-skill\n"})
        n4 = kayit("yt-n4", {"SKILL.md": fm("yt-n4") + "## Kullanım\nnpx skills add o/r --skill x --global\n"})
        n5 = kayit("yt-n5", {"SKILL.md": fm("yt-n5") + "Run ${CLAUDE_PLUGIN_ROOT}/scripts/a.sh\n"}, repo="o/n5", kaynak_yol="skills/yt-n5")
        n6 = kayit("yt-n6", {"SKILL.md": fm("yt-n6") + "Run ${CLAUDE_PLUGIN_ROOT}/scripts/a.sh\n"}, repo="o/n6", kaynak_yol="skills/yt-n6")
        liste_n = [n1, n2, n3, n4, n5, n6, ana, kod, ka, kb]
        sifirla()
        ist_dosya = kok / "istisna.json"
        o.YOL_ISTISNA = ist_dosya
        tum5 = o.skill_yol_taramasi(n5, liste_n)
        kay5 = {"tur": "eklenti-kok-yol", "dosyalar": ["SKILL.md"], "karar": "ornek-metin", "neden": "t", "tarih": "2026-01-01", "bulgu_hash": o.bulgu_hash(tum5)}
        ist_dosya.write_text(json.dumps({"_aciklama": "t", "istisnalar": {o.istisna_anahtari(n5): {"ad": "yt-n5", "kayitlar": [kay5]},
                                                                           o.istisna_anahtari(n6): {"ad": "yt-n6", "kayitlar": [dict(kay5, bulgu_hash="0" * 64)]}}}), encoding="utf-8")
        beklenen = {"yt-ana": ("BİLGİ", "yol-yerellestirme"), "yt-kod": ("UYARI", "genel-yol"), "yt-n1": ("UYARI", "eklenti-koku"), "yt-n2": ("UYARI", "skil-disi-yol"),
                    "yt-n3": ("UYARI", "genele-yazabilir"), "yt-n4": ("BİLGİ", "genele-yazabilir"), "yt-n5": ("BİLGİ", "yol-istisna"), "yt-n6": ("UYARI", "istisna-eskidi")}
        bulunan = {}
        for s_ in (ana, kod, n1, n2, n3, n4, n5, n6):
            bulunan[s_["id"]] = sk_(on(s_, liste_n))
        test("ön kontrol seviyeleri: yol-yerellestirme BİLGİ, genel-yol/eklenti-koku/skil-disi-yol UYARI, genele-yazabilir UYARI ve BİLGİ, yol-istisna BİLGİ, istisna-eskidi UYARI",
             all(v in bulunan[k_] for k_, v in beklenen.items()), str({k_: (v, bulunan[k_]) for k_, v in beklenen.items() if v not in bulunan[k_]}))
        o.YOL_ISTISNA = eski_istisna
        sifirla()
        rk = on(ka, liste_k, [ka, kb]) + on(ka, liste_k)
        test("ön kontrol seviyeleri: kardes-eksik UYARI, kardes-yol BİLGİ, kardes-farkli-kaynak UYARI",
             {("UYARI", "kardes-eksik"), ("BİLGİ", "kardes-yol")} <= set(sk_(rk)) and ("UYARI", "kardes-farkli-kaynak") in sk_(on(kf, liste_f, [kf], kilit_f["skiller"])), str(rk))
        kodlar = {"yol-yerellestirme", "genel-yol", "eklenti-koku", "skil-disi-yol", "kardes-eksik", "kardes-yol", "genele-yazabilir", "yol-istisna", "istisna-eskidi", "kardes-farkli-kaynak"}
        test("YOL_KODLARI sabiti tam bu on kodu içerir", set(se.YOL_KODLARI) == kodlar, str(se.YOL_KODLARI))
        # ============ j. yollari_yeniden_adlandir: ev önekli yola dokunmaz, proje içi biçimler adlandırılır
        jd = kok / "ad-degis"
        jd.mkdir()
        (jd / "SKILL.md").write_text("A ~/.claude/skills/old/x.md\nB $HOME/.agents/skills/old/x.md\nC ${HOME}/.codex/skills/old/x.md\nD /Users/biri/.claude/skills/old/x.md\n"
                                     "E /home/biri/.agents/skills/old/x.md\nF .claude/skills/old/x.md\nG ${CLAUDE_PROJECT_DIR}/.claude/skills/old/x.md\n", encoding="utf-8")
        se.yollari_yeniden_adlandir(jd, {"old"}, "new")
        jl = okulines(jd / "SKILL.md")
        test("yollari_yeniden_adlandir: ~/, $HOME/, ${HOME}/, /Users/<ad>/, /home/<ad>/ önekli yollara dokunmaz",
             jl[:5] == ["A ~/.claude/skills/old/x.md", "B $HOME/.agents/skills/old/x.md", "C ${HOME}/.codex/skills/old/x.md", "D /Users/biri/.claude/skills/old/x.md",
                        "E /home/biri/.agents/skills/old/x.md"], str(jl))
        test("yollari_yeniden_adlandir: proje içi biçim (.claude/skills/x ve ${CLAUDE_PROJECT_DIR}/.claude/skills/x) yine adlandırılır",
             jl[5] == "F .claude/skills/new/x.md" and jl[6] == "G ${CLAUDE_PROJECT_DIR}/.claude/skills/new/x.md", str(jl))
        # ============ k. dar geçiş (madde 8)
        kd_ = {"SKILL.md": fm("yt-dar") + "Run python .agents/skills/yt-dar/scripts/go.py now\nMissing .agents/skills/yt-dar/scripts/yok.py\nBoth .agents/skills/yt-dar/scripts/go.py and .claude/skills/yt-dar/scripts/go.py\n",
               "scripts/go.py": "print(1)\n", "README.md": "Run .agents/skills/yt-dar/scripts/go.py\n", "scripts/t.py": "P = '.agents/skills/yt-dar/scripts/go.py'\n"}
        dar = kayit("yt-dar", kd_)
        pdar = yeni_proje()
        kur_dongusu([dar], [dar], pdar, codex=False, adlar_ek={"yt-dar": "yt-dar2"})
        dd = pdar / ".claude" / "skills" / "yt-dar2"
        dl = okulines(dd / "SKILL.md")
        test("dar geçiş (sadece-Claude): proje içi .agents/skills/<kendi>/… -> .claude/skills/<kurulum adı>/… ve hedef var",
             "Run python .claude/skills/yt-dar2/scripts/go.py now" in dl and (dd / "scripts" / "go.py").exists(), "\n".join(dl))
        test("dar geçiş: hedefi olmayan yol, iki köklü satır, doküman ve kod dosyası çevrilmez",
             "Missing .agents/skills/yt-dar2/scripts/yok.py" in dl and "Both .agents/skills/yt-dar2/scripts/go.py and .claude/skills/yt-dar2/scripts/go.py" in dl
             and (dd / "README.md").read_text(encoding="utf-8") == "Run .agents/skills/yt-dar2/scripts/go.py\n"
             and (dd / "scripts" / "t.py").read_text(encoding="utf-8") == "P = '.agents/skills/yt-dar2/scripts/go.py'\n", "\n".join(dl))
        pdv = yeni_proje()
        kur_dongusu([dar], [dar], pdv)
        dvl = okulines(pdv / ".agents" / "skills" / "yt-dar" / "SKILL.md")
        test("dar geçiş varsayılan kurulumda ÇALIŞMAZ: SKILL.md arşivdekiyle birebir aynı (.agents/skills/<ad>/… kalır)",
             "\n".join(dvl) == kd_["SKILL.md"] and (pdv / ".claude" / "skills" / "yt-dar").is_symlink(), "\n".join(dvl))
        # ============ m. onek=None: hazirla çıktısı eski yolla (kopya + onarımlar + adlandırma) aynı; skill-calistir onek geçirir
        def eski_hazirla(kaynak, hedef, s, ad, kardes=None):
            gecici = hedef.parent / f".{ad}.eski-tmp"
            shutil.copytree(kaynak, gecici, ignore=shutil.ignore_patterns("KAYNAK.md"))
            se.symlink_taslaklarini_coz(gecici)
            se.yamalari_uygula(gecici, s)
            se.aciklama_onar(gecici / "SKILL.md", s, ad)
            se.isim_esitle(gecici / "SKILL.md", ad, s.get("aciklama"))
            se.yollari_yeniden_adlandir(gecici, {s["ad"], s.get("klasor_adi")}, ad)
            se.kardes_yollarini_yeniden_adlandir(gecici, {k: v[0] for k, v in (kardes or {}).items()})
            gecici.rename(hedef)
        ornek_idler = ["code-tour", "etsy-seller", "ui-ux-pro-max", "swift-code-reviewer", "gsap-core"]
        ornekler = [x for x in sk if x["id"] in ornek_idler] + [x for x in sk if x.get("aciklama_duzeltme")][:6] + [x for x in sk if x.get("yama")][:2]
        farklar = []
        for i, x in enumerate(ornekler):
            a_d, b_d = kok / "m-eski" / str(i) / "x", kok / "m-yeni" / str(i) / "x"
            a_d.parent.mkdir(parents=True), b_d.parent.mkdir(parents=True)
            ad_ = x["ad"] + ("--kutuphane" if x["id"] == "gsap-core" else "")
            eski_hazirla(KOK / x["yol"], a_d, x, ad_)
            uy_ = se.hazirla(KOK / x["yol"], b_d, x, ad_, onek=None, skiller=sk)
            if ozet(a_d) != ozet(b_d) or uy_ != []:
                farklar.append(x["id"])
        test(f"hazirla(onek=None): {len(ornekler)} gerçek skill için eski yolla (kopya + onarım + adlandırma) bayt bayt aynı, uyarı yok, yol çevirisi çalışmaz", not farklar, str(farklar))
        a_d, b_d = kok / "m-eski" / "ct" / "x", kok / "m-yeni" / "ct" / "x"
        a_d.parent.mkdir(parents=True), b_d.parent.mkdir(parents=True)
        se.hazirla(ct_arsiv, a_d, ct, "code-tour", onek=".agents/skills", skiller=sk)
        se.hazirla(ct_arsiv, b_d, ct, "code-tour", onek=None, skiller=sk)
        test("hazirla: onek verilince code-tour kopyası değişir, onek=None iken değişmez (olumlu ve olumsuz kontrol)",
             ozet(a_d) != ozet(b_d) and ".agents/skills/code-tour/scripts/validate_tour.py" in (a_d / "SKILL.md").read_text(encoding="utf-8")
             and "~/.agents/skills/code-tour/scripts/validate_tour.py" in (b_d / "SKILL.md").read_text(encoding="utf-8"))
        sc_kaynak = (KOK / "araclar" / "skill-calistir.py").read_text(encoding="utf-8")
        cagrilar = []
        for m_ in re.finditer(r"se\.hazirla\(", sc_kaynak):  # dengeli parantezle çağrının tamamı
            derin, j_ = 1, m_.end()
            while derin and j_ < len(sc_kaynak):
                derin += {"(": 1, ")": -1}.get(sc_kaynak[j_], 0)
                j_ += 1
            cagrilar.append(sc_kaynak[m_.start():j_])
        test("skill-calistir.py: her se.hazirla çağrısı onek ve skiller geçirir (kaynakta)", len(cagrilar) == 2 and all("onek=" in c and "skiller=" in c for c in cagrilar), str(cagrilar))
        spec_c = importlib.util.spec_from_file_location("sk_calistir_yol", KOK / "araclar" / "skill-calistir.py")
        sc = importlib.util.module_from_spec(spec_c)
        spec_c.loader.exec_module(sc)
        kayitli = []
        gercek_hazirla = sc.se.hazirla
        sc.se.hazirla = lambda *a, **k: (kayitli.append((a[3], k.get("onek"), k.get("skiller") is sk)), gercek_hazirla(*a, **k))[1]
        try:
            sc.skill_test(ct, kok / "calistir-ct", sk)
            vx = next(x for x in sk if (x.get("varyantlar") or {}).get("claude") and not x.get("gizli"))
            sc.skill_test(vx, kok / "calistir-vx", sk)
        finally:
            sc.se.hazirla = gercek_hazirla
        test("skill-calistir.skill_test: ana sürüm .agents/skills, claude varyantı .claude/skills öneki ve skiller listesiyle hazirla çağırır",
             (ct["ad"], ".agents/skills", True) in kayitli and (vx["ad"], ".claude/skills", True) in kayitli and (vx["ad"], ".agents/skills", True) in kayitli, str(kayitli))
        # ============ g. onarim_izi: çevrilecek yolu olmayanlarda eskiyle aynı, olanlarda değişir
        def eski_iz(s):
            d = (s.get("aciklama_duzeltme") or {}).get("description")
            oto = [y for y in s.get("yapisal_sorunlar", []) if "dosya başında değil" in y or "tırnaksız" in y]
            yama = [f"{rel}:{o.git_blob_hash((o.YAMALAR / s['id'] / rel).read_bytes()) if (o.YAMALAR / s['id'] / rel).exists() else '-'}"
                    for rel in sorted(((s.get('yama') or {}).get('dosyalar') or {}))]
            if not d and not oto and not yama:
                return None
            return hashlib.sha1(f"{o.ONARIM_SURUMU}|{d or ''}|{'|'.join(oto)}|{'|'.join(yama)}".encode()).hexdigest()[:12]
        bilinen6 = {"ui-ux-pro-max", "siege", "swift-code-reviewer", "code-tour", "etsy-seller", "mp-integrate"}
        orn = list({x["id"]: x for x in [x for x in sk if x.get("aciklama_duzeltme") or x.get("yama") or x["id"] in bilinen6] + sk[::12]}.values())
        degisen, yanlis_ayni, yanlis_fark = [], [], []
        for x in orn:
            yeni_, eski_ = o.onarim_izi(x, sk), eski_iz(x)
            cev = bool(o.yol_izi(x, sk))
            if yeni_ != eski_:
                degisen.append(x["id"])
            if not cev and yeni_ != eski_:
                yanlis_ayni.append(x["id"])
            if cev and yeni_ == eski_:
                yanlis_fark.append(x["id"])
        test(f"onarim_izi: {len(orn)} skill örneğinde (aciklama_duzeltme ve yamalılar dahil) çevrilecek yolu olmayanlarda eski formülle birebir aynı",
             len(orn) >= 300 and not yanlis_ayni and any(x.get("aciklama_duzeltme") for x in orn) and any(x.get("yama") for x in orn), str(yanlis_ayni[:5]))
        test("onarim_izi: çevrilecek kendi yolu olan skill'lerde değişir (bilinen beş skill dahil; yamalı etsy-seller hariç), yalnız onlarda",
             not yanlis_fark and (bilinen6 - {"etsy-seller"}) <= set(degisen) and "etsy-seller" not in degisen  # yamalı dosyadaki yol çevrilmez: iz değişmez
             and set(degisen) <= bilinen6 | {x["id"] for x in orn if o.yol_izi(x, sk)},
             str((sorted(set(degisen)), yanlis_fark[:5])))
        # ============ h-i-l. gerçek akışlar (CLI, code-tour): ekle iz farkında kur çağırır, elle değişiklik korunur, guncelle mesajı, idempotans, kaldır
        def kilit_yaz(proje, f):
            kp = proje / ".skill-kutuphanesi" / "kilit.json"
            k = json.loads(kp.read_text(encoding="utf-8"))
            f(k)
            kp.write_text(json.dumps(k, ensure_ascii=False, indent=2), encoding="utf-8")

        def eski_kurulum(proje):
            """Eski sürümün kurduğu gibi: arşiv kopyası olduğu gibi (çevrilmemiş), kilitte iz yok, kurulu_hash kopyayla uyumlu."""
            hedef = proje / ".agents" / "skills" / "code-tour"
            shutil.rmtree(hedef)
            shutil.copytree(ct_arsiv, hedef, ignore=shutil.ignore_patterns("KAYNAK.md"))
            kilit_yaz(proje, lambda k: (k["skiller"]["code-tour"].update(kurulu_hash=se.kurulu_hash(proje, "code-tour")), k["skiller"]["code-tour"].pop("onarim", None)))

        beklenen_iz = o.onarim_izi(ct, sk)
        p1 = yeni_proje()
        (p1 / "benim-notum.txt").write_text("dokunma\n", encoding="utf-8")
        kod1, out1 = calistir(p1, "--skill", "code-tour", "--evet")
        md1 = p1 / ".agents" / "skills" / "code-tour" / "SKILL.md"
        yeni_yol = ".agents/skills/code-tour/scripts/validate_tour.py"
        test("gerçek kurulum (code-tour): ~/.agents/skills/… yolları proje içine çevrilir, hedef var, doğrulama temiz, kilitte onarım izi yazılı",
             kod1 == 0 and "doğrulama: ✅" in out1 and yeni_yol in md1.read_text(encoding="utf-8") and "~/.agents/skills/code-tour" not in md1.read_text(encoding="utf-8")
             and (p1 / ".agents" / "skills" / "code-tour" / "scripts" / "validate_tour.py").exists()
             and json_oku(p1 / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]["onarim"] == beklenen_iz and beklenen_iz, out1)
        # l. idempotans
        agac1, hash1 = ozet(p1 / ".agents" / "skills" / "code-tour"), json_oku(p1 / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]["kurulu_hash"]
        kod2, out2 = calistir(p1, "--skill", "code-tour", "--evet")
        kil2 = json_oku(p1 / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]
        test("idempotans: ikinci kurulum no-op (kopya aynı bayt, kurulu_hash aynı, yeniden kurulmadı)",
             kod2 == 0 and "+ code-tour" not in out2 and ozet(p1 / ".agents" / "skills" / "code-tour") == agac1 and kil2["kurulu_hash"] == hash1 and kil2["onarim"] == beklenen_iz, out2)
        kodd, outd = calistir(p1, "--dogrula")
        test("idempotans: kurulumdan hemen sonra --dogrula temiz", kodd == 0, outd)
        kodg, outg = calistir(p1, "--guncelle", "--kuru")
        test("idempotans: kurulumdan sonra --guncelle yeni iş önermez", "yol-yerellestirme" not in outg and "sabit yol çevirisi" not in outg, outg)
        kodk, outk = calistir(p1, "--kaldir", "code-tour", "--evet")
        test("kaldır: kopya ve kilit kaydı temiz kalkar, kullanıcının dosyası durur",
             kodk == 0 and not (p1 / ".agents" / "skills" / "code-tour").exists() and not (p1 / ".claude" / "skills" / "code-tour").exists()
             and "code-tour" not in json_oku(p1 / ".skill-kutuphanesi" / "kilit.json")["skiller"] and (p1 / "benim-notum.txt").read_text(encoding="utf-8") == "dokunma\n", outk)
        pcl = yeni_proje()
        kodc, outc = calistir(pcl, "--skill", "code-tour", "--arac", "claude", "--evet")
        cmd = pcl / ".claude" / "skills" / "code-tour" / "SKILL.md"
        test("gerçek kurulum --arac claude: yollar .claude/skills/code-tour/… olur, hedef var, doğrulama temiz",
             kodc == 0 and ".claude/skills/code-tour/scripts/validate_tour.py" in cmd.read_text(encoding="utf-8") and not (pcl / ".agents" / "skills" / "code-tour").exists()
             and (pcl / ".claude" / "skills" / "code-tour" / "scripts" / "validate_tour.py").exists() and calistir(pcl, "--dogrula")[0] == 0, outc)
        agac_cl = ozet(pcl / ".claude" / "skills" / "code-tour")
        kodc2, outc2 = calistir(pcl, "--skill", "code-tour", "--evet")
        test("idempotans (sadece-Claude): ikinci kurulum no-op", kodc2 == 0 and "+ code-tour" not in outc2 and ozet(pcl / ".claude" / "skills" / "code-tour") == agac_cl, outc2)
        # h. ekle: eski izli kilit -> kur çağrılır ve kopya çevrilir
        ph = yeni_proje()
        calistir(ph, "--skill", "code-tour", "--evet")
        eski_kurulum(ph)
        ham_md = ph / ".agents" / "skills" / "code-tour" / "SKILL.md"
        once_ham = "~/.agents/skills/code-tour/scripts/validate_tour.py" in ham_md.read_text(encoding="utf-8")
        koh, outh = calistir(ph, "--skill", "code-tour", "--evet")
        test("ekle(): eski izli (izsiz) kilitte kur çağrılır, kopya yeniden yazılır, yeni iz damgalanır",
             once_ham and koh == 0 and "+ code-tour" in outh and yeni_yol in ham_md.read_text(encoding="utf-8")
             and "~/.agents/skills/code-tour" not in ham_md.read_text(encoding="utf-8")
             and json_oku(ph / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]["onarim"] == beklenen_iz, outh)
        # h. elle değiştirilmiş kopya: --zorla olmadan yeniden kurulmaz ve iz damgalanmaz; --zorla ile kurulur
        pe2 = yeni_proje()
        calistir(pe2, "--skill", "code-tour", "--evet")
        eski_kurulum(pe2)
        elle = pe2 / ".agents" / "skills" / "code-tour" / "SKILL.md"
        with elle.open("a", encoding="utf-8") as f_:
            f_.write("\nelle eklendi\n")
        kilit_yaz(pe2, lambda k: k["skiller"]["code-tour"].update(onarim="eski-iz-0001"))
        koe, oute = calistir(pe2, "--skill", "code-tour", "--evet")
        k_e = json_oku(pe2 / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]
        test("ekle(): elle değiştirilmiş kopya --zorla olmadan yeniden kurulmaz, yeni iz DAMGALANMAZ, değişiklik korunur",
             koe == 2 and "elle-degistirilmis" in oute and k_e["onarim"] == "eski-iz-0001" and "elle eklendi" in elle.read_text(encoding="utf-8")
             and "~/.agents/skills/code-tour/scripts" in elle.read_text(encoding="utf-8"), oute)
        koz, outz = calistir(pe2, "--skill", "code-tour", "--zorla", "--evet")
        test("ekle(): --zorla ile yeniden kurulur (elle ekleme gider, yollar çevrilir, iz yazılır)",
             koz == 0 and "+ code-tour" in outz and "elle eklendi" not in elle.read_text(encoding="utf-8") and yeni_yol in elle.read_text(encoding="utf-8")
             and json_oku(pe2 / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]["onarim"] == beklenen_iz, outz)
        # i. guncelle: aynı karma, yalnız iz farklı -> 'sabit yol çevirisi' (yol-yerellestirme)
        pg = yeni_proje()
        calistir(pg, "--skill", "code-tour", "--evet")
        eski_kurulum(pg)
        kog, outg2 = calistir(pg, "--guncelle", "--kuru")
        test("guncelle(): aynı karma, yalnız iz farklıysa yol-yerellestirme koduyla 'sabit yol çevirisi' bildirilir",
             "yol-yerellestirme" in outg2 and "sabit yol çevirisi" in outg2 and "code-tour: kurulan kopyaya uygulanacak" in outg2 and "elle-degistirilmis" not in outg2, outg2)
        gm = pg / ".agents" / "skills" / "code-tour" / "SKILL.md"
        test("guncelle --kuru: kopyaya dokunmaz", "~/.agents/skills/code-tour/scripts/validate_tour.py" in gm.read_text(encoding="utf-8"))
        kog2, outg3 = calistir(pg, "--guncelle", "--evet")
        test("guncelle --evet: kopya çevrilir, iz yazılır, --dogrula temiz",
             kog2 == 0 and yeni_yol in gm.read_text(encoding="utf-8") and json_oku(pg / ".skill-kutuphanesi" / "kilit.json")["skiller"]["code-tour"]["onarim"] == beklenen_iz
             and calistir(pg, "--dogrula")[0] == 0, outg3)
        # ============ p. doğrulanmış bulgu düzeltmeleri
        import argparse
        import contextlib
        import io
        import time
        # p1. claude varyantı kendi sabit yollarıyla taranır (ana arşive göre değil)
        vr = kayit("yt-vr", {"SKILL.md": fm("yt-vr") + "Main: ~/.claude/skills/yt-vr/ref/a.md\n", "ref/a.md": "-\n"},
                   varyant={"SKILL.md": fm("yt-vr") + "Variant differs ~/.claude/skills/yt-vr/ref/a.md ok\nVariant also ~/.claude/skills/yt-vr/ref/b.md\n",
                            "ref/a.md": "-\n", "ref/b.md": "-\n"})
        pvr = yeni_proje()
        uy_vr = kur_dongusu([vr], [vr], pvr)[2]["yt-vr"]
        vmd = okulines(pvr / ".claude" / "skills" / "yt-vr" / "SKILL.md")
        test("varyant kopya: varyantın KENDİ sabit yolları çevrilir ve yanıltıcı 'çevrilemedi' uyarısı çıkmaz",
             "Variant differs .claude/skills/yt-vr/ref/a.md ok" in vmd and "Variant also .claude/skills/yt-vr/ref/b.md" in vmd and uy_vr == [], str((vmd, uy_vr)))
        pvr2 = yeni_proje()
        kur_dongusu([vr], [vr], pvr2, codex=False)
        test("varyant kopya (sadece-Claude): aynı sonuç",
             "Variant also .claude/skills/yt-vr/ref/b.md" in okulines(pvr2 / ".claude" / "skills" / "yt-vr" / "SKILL.md"))
        # p2. guncelle: aynı adlı farklı kimlikli kardeş çalışan bağlantıyı bozmaz, kardes-farkli-kaynak UYARI
        sl = kayit("yt-sl", {"SKILL.md": fm("yt-sl") + "Read ../yt-kb/refs/x.md\n"}, kardes_bagimliliklari={"yt-kb": {"id": "yt-kb", "dosya_sayisi": 1}})
        liste_sl = [sl, kb, baska_kb]
        psl = yeni_proje()
        kilit_sl, _, _ = kur_dongusu(liste_sl, [baska_kb, sl], psl, adlar_ek={"yt-kb@x": "yt-kb--x"})
        kilit_sl["skiller"]["yt-sl"]["kardes"] = {"yt-kb": "yt-kb--x"}  # eski kodun yazdığı biçim (kardeş adla eşleniyordu)
        cikti = io.StringIO()
        with contextlib.redirect_stdout(cikti):
            kg = se.guncelle(argparse.Namespace(zorla=False, evet=True, kuru=True), psl, liste_sl, kilit=kilit_sl)
        test("guncelle: aynı adlı farklı kimlikli kardeş kardeş-yol yeniden yazımı BAŞLATMAZ; kardes-farkli-kaynak UYARI verir",
             kg == 0 and "yeniden yazılacak" not in cikti.getvalue() and "kardes-farkli-kaynak" in cikti.getvalue()
             and "Güncellenecek/onarılacak: 0" in cikti.getvalue(), cikti.getvalue())
        # p3. kardes-farkli-kaynak aynı kardeş için tek kez (../ bağlantısı + sabit yol)
        kilitli_x = {"yt-kb": {"id": "yt-kb@x", "repo": "o/x", "kaynak_yol": "skills/yt-kb", "roller": []}}
        rows = on(ke, [ke, kb, baska_kb], [ke], kilitli_x)
        test("tekilleştirme: kardes-farkli-kaynak, kardeş hem ../ hem sabit yolla anılsa da TEK satır",
             [kd for _, kd, _ in rows].count("kardes-farkli-kaynak") == 1, str(rows))
        # p4. dar geçiş: ${CLAUDE_PROJECT_DIR}/ ve $CLAUDE_PROJECT_DIR/ önekli .agents/skills/<kendi> da çevrilir, başka mutlak yol çevrilmez
        ev = kayit("yt-ev", {"SKILL.md": fm("yt-ev") + "B: ./.agents/skills/yt-ev/ref/a.md and ${CLAUDE_PROJECT_DIR}/.agents/skills/yt-ev/ref/a.md\n"
                             "C: $CLAUDE_PROJECT_DIR/.agents/skills/yt-ev/ref/a.md\nD: /opt/x/.agents/skills/yt-ev/ref/a.md\n", "ref/a.md": "-\n"})
        pev = yeni_proje()
        kur_dongusu([ev], [ev], pev, codex=False)
        emd = okulines(pev / ".claude" / "skills" / "yt-ev" / "SKILL.md")
        test("dar geçiş: ./, ${CLAUDE_PROJECT_DIR}/ ve $CLAUDE_PROJECT_DIR/ önekli .agents/skills/<kendi> sadece-Claude kopyada .claude/skills'e çevrilir; başka mutlak yol değişmez",
             "B: ./.claude/skills/yt-ev/ref/a.md and ${CLAUDE_PROJECT_DIR}/.claude/skills/yt-ev/ref/a.md" in emd
             and "C: $CLAUDE_PROJECT_DIR/.claude/skills/yt-ev/ref/a.md" in emd and "D: /opt/x/.agents/skills/yt-ev/ref/a.md" in emd, "\n".join(emd))
        # p5. satır içi değiştirme uzun yolun önekini bozmaz
        px = kayit("yt-px", {"SKILL.md": fm("yt-px") + "Two: ~/.claude/skills/yt-px/ref/a.md and ~/.claude/skills/yt-px/ref/a.mdx\n", "ref/a.md": "-\n"})
        ppx = yeni_proje()
        kur_dongusu([px], [px], ppx)
        test("satır içi değiştirme: çevrilebilir yolun önekini taşıyan daha uzun (çevrilemeyen) yol değişmez",
             "Two: .agents/skills/yt-px/ref/a.md and ~/.claude/skills/yt-px/ref/a.mdx" in okulines(ppx / ".agents" / "skills" / "yt-px" / "SKILL.md"),
             "\n".join(okulines(ppx / ".agents" / "skills" / "yt-px" / "SKILL.md")))
        # p6. dar geçiş aşırı uzun satırda ikinci dereceden yavaşlamaz
        uz_klasor = kok / "uzun-arsiv"
        (uz_klasor / "ref").mkdir(parents=True)
        (uz_klasor / "ref" / "a.md").write_text("-\n", encoding="utf-8")
        parca = "see .agents/skills/foo/ref/a.md and more text padding "
        bas_t = time.time()
        orta, n_orta = o.ev_ici_kendi_cevir(parca * 300, {"foo"}, "foo", ".claude/skills", uz_klasor)
        uzun, n_uzun = o.ev_ici_kendi_cevir(parca * 3000, {"foo"}, "foo", ".claude/skills", uz_klasor)
        test("dar geçiş: satır başına tek tarama (16 KB satırda 300 yol hızlı çevrilir), 20.000 karakterden uzun satır çevrilmez",
             n_orta == 300 and orta.count(".claude/skills/foo/ref/a.md") == 300 and n_uzun == 0 and time.time() - bas_t < 5, f"{n_orta} {n_uzun} {time.time() - bas_t:.1f}s")
        # p7. ön kontrol yamalı dosyadaki yolu çevrilecek saymaz (kurulum yamalı dosyada çeviri yapmaz)
        ym_d = {"SKILL.md": fm("yt-ym") + "Run ~/.claude/skills/yt-ym/ref/a.md\n", "ref/a.md": "-\n"}
        ym0, ym1 = kayit("yt-ym", ym_d), kayit("yt-ym2", {"SKILL.md": fm("yt-ym2") + "Run ~/.claude/skills/yt-ym2/ref/a.md\n", "ref/a.md": "-\n"}, yama={"dosyalar": {"SKILL.md": "x"}})
        test("ön kontrol: yamalı dosyadaki sabit yol 'çevrilecek' sayılmaz, yamasız aynı dosya sayılır",
             len(o.yol_degerlendir(ym0, [ym0])["cevrilecek"]) == 1 and o.yol_degerlendir(ym1, [ym1])["cevrilecek"] == []
             and not any(kd == "yol-yerellestirme" for _, kd, _ in on(ym1, [ym1])), str(on(ym1, [ym1])))
        # p8. ekle() savunma dalı: on_kontrol HATA'sı atlatılsa bile elle değiştirilmiş kopya yeniden kurulmaz, kilitteki iz/damga değişmez
        ed = kayit("yt-ed", {"SKILL.md": fm("yt-ed") + "Run ~/.claude/skills/yt-ed/ref/a.md\n", "ref/a.md": "-\n"})
        ped = yeni_proje()
        kilit_ed, _, _ = kur_dongusu([ed], [ed], ped)
        kilit_ed["skiller"]["yt-ed"]["onarim"] = "eski-iz-0001"
        se.tumunu_yaz(ped, kilit_ed, [ed])
        ed_md = ped / ".agents" / "skills" / "yt-ed" / "SKILL.md"
        with ed_md.open("a", encoding="utf-8") as f_:
            f_.write("elle eklendi\n")
        asil = (se.istek_coz, se.on_kontrol, se.kapsam_raporu)
        try:
            se.istek_coz = lambda a_, sk_: ([(ed, None)], [], None, [])
            se.on_kontrol = lambda proje_, kilit_, plan_, roller_, sk_, rapor_, zorla_=False: ({ed["id"]: (ed, set())}, {ed["id"]: "yt-ed"})  # HATA'sız ön kontrol
            se.kapsam_raporu = lambda *a_, **k_: None
            with contextlib.redirect_stdout(io.StringIO()) as cikti_ed:
                se.ekle(argparse.Namespace(arac=None, blok=None, oner=None, zorla=False, evet=True, kuru=False, skill=["yt-ed"]), ped, [ed])
        finally:
            se.istek_coz, se.on_kontrol, se.kapsam_raporu = asil
        test("ekle() savunma dalı: elle değiştirilmiş kopya yeniden kurulmaz, kilitteki onarım izi aynen kalır",
             "elle eklendi" in ed_md.read_text(encoding="utf-8") and "yeniden kurulmadı" in cikti_ed.getvalue()
             and json_oku(ped / ".skill-kutuphanesi" / "kilit.json")["skiller"]["yt-ed"]["onarim"] == "eski-iz-0001", cikti_ed.getvalue())
        # o. arşivler ve sentetik kaynaklar dokunulmadı
        test("arşiv klasörü (code-tour) tüm bu işlemlerden sonra bayt bayt aynı; sentetik arşivler değişmedi",
             ozet(ct_arsiv) == ct_once and ozet(Path(ana["yol"])) == arsiv_ana_once and (Path(kod["yol"]) / "scripts" / "run.py").read_text(encoding="utf-8") == yol_satiri)
    finally:
        o.YOL_ISTISNA = eski_istisna
        sifirla()
        shutil.rmtree(kok, ignore_errors=True)


def main():
    once = parmak_izi()
    kok = Path(tempfile.mkdtemp(prefix="skill-test-"))
    proje = kok / "proje"
    proje.mkdir()
    (proje / "AGENTS.md").write_text("# Benim notlarım\n\nBu satır korunmalı.\n", encoding="utf-8")
    (proje / "package.json").write_text('{"dependencies": {"next": "16", "three": "0.186", "gsap": "3.15"}}', encoding="utf-8")
    print(f"Geçici proje: {proje}")

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--kuru")
    test("kuru çalıştırma hiçbir şey kurmaz", not (proje / ".agents").exists() and "ÖN KONTROL" in out, out)
    test("ön kontrol tüm kütüphaneyi tarar", "skill tarandı" in out and "ek-aday" in out, out)
    test("package.json teknolojileri tespit edilir", "next.js" in out and "three.js" in out, out)

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi")
    test("uyarı varken onaysız (etkileşimsiz) kurulum durur", kod == 2 and not (proje / ".agents" / "skills").exists(), out)

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--evet")
    test("profil kurulumu başarılı ve doğrulama temiz", kod == 0 and "doğrulama: ✅" in out, out)
    kilit = json_oku(proje / ".skill-kutuphanesi" / "kilit.json")
    test("kilit dosyası oluştu", kilit and len(kilit["skiller"]) >= 8)
    test("Claude agent dosyaları oluştu", (proje / ".claude" / "agents" / "3d-gelistirici.md").exists())
    test("Codex agent dosyaları oluştu", (proje / ".codex" / "agents" / "3d-gelistirici.toml").exists())
    toml = (proje / ".codex" / "agents" / "3d-gelistirici.toml").read_text(encoding="utf-8")
    test("Codex rol dışı skilleri kapatır", "enabled = false" in toml and "impeccable" in toml)
    test("AGENTS.md'deki kullanıcı metni korunur", "Bu satır korunmalı." in (proje / "AGENTS.md").read_text(encoding="utf-8"))

    farkli = [a for a in kilit["skiller"] if a.endswith("--kutuphane")]
    if farkli:
        sm = (proje / ".agents" / "skills" / farkli[0] / "SKILL.md").read_text(encoding="utf-8")
        test("globalde farklı sürümü olan skill ekli adla kurulur ve name eşitlenir", f"name: {farkli[0]}" in sm)

    c_imp, x_imp = proje / ".claude" / "skills" / "impeccable", proje / ".agents" / "skills" / "impeccable"
    if (KOK / "arsiv" / "_varyantlar" / "impeccable").exists():
        test("araç sürümü: Claude'a gerçek kopya (symlink değil)", c_imp.is_dir() and not c_imp.is_symlink())
        test("araç sürümü: Claude kopyası .claude yolunu, Codex kopyası .agents yolunu kullanır",
             ".claude/skills/impeccable" in (c_imp / "SKILL.md").read_text(encoding="utf-8")
             and ".agents/skills/impeccable" in (x_imp / "SKILL.md").read_text(encoding="utf-8"))
    sym = next((p for p in (proje / ".claude" / "skills").iterdir() if p.is_symlink()), None)
    test("varyantı olmayan skill Claude'a symlink ile bağlanır", sym is not None and (sym / "SKILL.md").exists())

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--evet")
    test("aynı kurulumu tekrar çalıştırmak güvenli (idempotent)", kod == 0, out)

    (proje / ".claude" / "skills" / "benim-skillim").mkdir(parents=True)
    # profille kurulmamış bir kütüphane skill'i seç (rol içerikleri değişse de test sağlam kalsın)
    kurulu = {a.removesuffix("--kutuphane") for a in (json_oku(proje / ".skill-kutuphanesi" / "kilit.json") or {}).get("skiller", {})}
    kendi = next(a for a in ("pixijs-2d", "gsap-core", "d3-viz") if a not in kurulu and not (proje / ".agents" / "skills" / a).exists())
    (proje / ".agents" / "skills" / kendi).mkdir(parents=True)
    (proje / ".agents" / "skills" / kendi / "SKILL.md").write_text(f"---\nname: {kendi}\n---\nbenim\n", encoding="utf-8")
    kod, out = calistir(proje, "--skill", kendi, "--evet")
    test("projedeki kendi skill'inin üzerine yazılmaz", kod == 2 and "projede-kendi-skillin" in out
         and "benim" in (proje / ".agents" / "skills" / kendi / "SKILL.md").read_text(encoding="utf-8"), out)
    shutil.rmtree(proje / ".agents" / "skills" / kendi)

    hedef = next(iter(kilit["skiller"]))
    (proje / ".agents" / "skills" / hedef / "SKILL.md").open("a", encoding="utf-8").write("\nelle eklendi\n")
    kod, out = calistir(proje, "--kaldir", hedef, "--evet")
    test("elle değiştirilmiş skill silinmez", kod == 2 and "elle-degistirilmis" in out, out)
    kod, out = calistir(proje, "--dogrula")
    test("doğrulama elle değişikliği yakalar", kod == 1 and "elle değiştirilmiş" in out, out)

    kod, out = calistir(proje, "--kaldir", "yok-boyle-skill", "--evet")
    test("kütüphaneden gelmeyen skill kaldırılmaz", kod == 2 and "kutuphaneden-degil" in out, out)

    once_agac = agac(proje)
    kod, out = calistir(proje, "--kaldir", "hepsi", "--evet", "--zorla")
    test("hepsini kaldır (zorla, yedekli)", kod == 0 and not any((proje / ".agents" / "skills").iterdir()), out)
    test("kullanıcı metni kaldırmadan sonra da korunur", "Bu satır korunmalı." in (proje / "AGENTS.md").read_text(encoding="utf-8"))
    test("kendi klasörüne (benim-skillim) dokunulmaz", (proje / ".claude" / "skills" / "benim-skillim").exists())
    kod, out = calistir(proje, "--geri-al")
    test("geri al: önceki duruma döner", kod == 0 and agac(proje) == once_agac, out)

    yeni = kok / "tasinmis-proje"
    shutil.move(str(proje), str(yeni))
    kod, out = calistir(yeni, "--dogrula")
    test("proje taşınınca doğrulama uyarır", kod == 1 and "taşınmış" in out, out)
    kod, out = calistir(yeni, "--yenile")
    out2 = calistir(yeni, "--dogrula")[1]
    test("--yenile Codex yollarını düzeltir", "taşınmış" not in out2 and "geçersiz yol" not in out2, out2)

    # --- inceleme sonrası eklenen senaryolar
    p2 = kok / "proje2"
    p2.mkdir()
    kod, out = calistir(p2, "--skill", "gsap-core", "--kuru")
    test("--kuru projeye hiçbir dosya yazmaz", not any(p2.iterdir()), out)

    kod, out = calistir(p2, "--skill", "gsap-core", "--rol-adi", "../../kacis", "--evet", "--zorla")
    test("geçersiz rol adı --zorla ile bile reddedilir (proje dışına yazılamaz)",
         kod == 2 and "gecersiz-rol-adi" in out and not (kok / "kacis.md").exists() and not (p2 / "kacis.md").exists(), out)

    (p2 / ".claude" / "agents").mkdir(parents=True)
    (p2 / ".claude" / "agents" / "planlayici.md").write_text("benim agent'ım\n", encoding="utf-8")
    kod, out = calistir(p2, "--rol", "planlayici", "--evet", "--zorla")
    test("kullanıcının kendi agent dosyasının üzerine yazılmaz",
         kod == 2 and "kendi-agent-dosyan" in out
         and (p2 / ".claude" / "agents" / "planlayici.md").read_text(encoding="utf-8") == "benim agent'ım\n", out)
    shutil.rmtree(p2 / ".claude")

    (p2 / ".agents" / "skills").mkdir(parents=True)
    (p2 / ".claude").mkdir()
    (p2 / ".claude" / "skills").symlink_to("../.agents/skills")
    kod, out = calistir(p2, "--skill", "gsap-core", "--evet", "--zorla")
    test(".claude/skills ve .agents/skills aynı klasörse kurulum yapılmaz", kod == 2 and "ayni-klasor" in out, out)
    (p2 / ".claude" / "skills").unlink()

    kod, out = calistir(p2, "--skill", "gsap-core", "gsap-timeline", "--rol-adi", "animasyoncu", "--evet")
    test("tek tek skill + özel rol adı kurulur", kod == 0, out)
    (p2 / ".agents" / "skills" / "gsap-core" / ".DS_Store").write_bytes(b"x")
    kod, out = calistir(p2, "--dogrula")
    test(".DS_Store elle değişiklik sayılmaz", kod == 0, out)

    import json as _j
    kp = p2 / ".skill-kutuphanesi" / "kilit.json"
    kl = _j.loads(kp.read_text(encoding="utf-8"))
    kl["skiller"]["gsap-timeline"]["kaynak_yol"] = "yok/boyle/bir/yol"
    kl["skiller"]["gsap-timeline"]["klasor_hash"] = "eski"
    kp.write_text(_j.dumps(kl), encoding="utf-8")
    once_tl = (p2 / ".agents" / "skills" / "gsap-timeline" / "SKILL.md").read_bytes()
    kod, out = calistir(p2, "--guncelle", "--evet")
    test("kaynağı kaybolan skill'in yerine başka repo'nun aynı adlı skill'i konmaz",
         "kaynak-yok" in out and (p2 / ".agents" / "skills" / "gsap-timeline" / "SKILL.md").read_bytes() == once_tl, out)

    # --- sadece Claude kullanan proje (--arac claude)
    p3 = kok / "proje-claude"
    p3.mkdir()
    (p3 / "AGENTS.md").write_text("# Kendi notum\n", encoding="utf-8")
    kod, out = calistir(p3, "--skill", "gsap-core", "gsap-timeline", "--rol-adi", "animasyoncu", "--evet")
    # klasör kopyalanınca symlink'in aynı içerikli gerçek kopyaya dönmesi (Etsy-Arif'te görülen durum)
    l = p3 / ".claude" / "skills" / "gsap-core"
    l.unlink()
    shutil.copytree(p3 / ".agents" / "skills" / "gsap-core", l)
    kod, out = calistir(p3, "--durum")
    test("symlink yerine aynı içerikli kopya elle değişiklik sayılmaz", "ELLE" not in out, out)
    once3 = agac(p3)
    kod, out = calistir(p3, "--arac", "claude", "--kuru")
    test("--arac claude --kuru hiçbir şey değiştirmez", agac(p3) == once3, out)
    kod, out = calistir(p3, "--arac", "claude", "--evet")
    test("--arac claude: Claude'da gerçek kopya, .agents/.codex kaldırılır",
         kod == 0 and (p3 / ".claude" / "skills" / "gsap-core" / "SKILL.md").exists()
         and not (p3 / ".claude" / "skills" / "gsap-core").is_symlink()
         and not (p3 / ".agents").exists() and not (p3 / ".codex" / "agents" / "animasyoncu.toml").exists()
         and (p3 / ".claude" / "agents" / "animasyoncu.md").exists(), out)
    test("--arac claude: AGENTS.md'deki kullanıcı metni kalır, blok çıkar",
         (p3 / "AGENTS.md").read_text(encoding="utf-8") == "# Kendi notum\n"
         and "skill-kutuphanesi:basla" in (p3 / "CLAUDE.md").read_text(encoding="utf-8"))
    kod, out = calistir(p3, "--dogrula")
    test("sadece Claude projesi doğrulamadan temiz geçer", kod == 0, out)
    kod, out = calistir(p3, "--blok", "kisa")
    cm = (p3 / "CLAUDE.md").read_text(encoding="utf-8")
    test("--blok kisa: tablo yok, işaretler ve skill sayısı var, doğrulama temiz",
         kod == 0 and "skill-kutuphanesi:basla" in cm and "| Skill |" not in cm and "2 skill `.claude/skills/`" in cm, out)
    kod, out = calistir(p3, "--skill", "d3-viz", "--evet")
    test("sadece Claude projesine yeni skill .agents oluşturmadan kurulur",
         kod == 0 and not (p3 / ".agents").exists() and (p3 / ".claude" / "skills" / "d3-viz" / "SKILL.md").exists(), out)
    cm = (p3 / "CLAUDE.md").read_text(encoding="utf-8")
    test("kısa blok sonraki kurulumda korunur ve sayı güncellenir", "| Skill |" not in cm and "3 skill" in cm, cm)
    kod, out = calistir(p3, "--blok", "tam")
    test("--blok tam: tablo geri gelir", kod == 0 and "| `d3-viz` |" in (p3 / "CLAUDE.md").read_text(encoding="utf-8"), out)
    (p3 / ".claude" / "skills" / "gsap-core" / "SKILL.md").open("a", encoding="utf-8").write("\nelle\n")
    kod, out = calistir(p3, "--dogrula")
    test("sadece Claude projesinde elle değişiklik yakalanır", kod == 1 and "elle değiştirilmiş" in out, out)
    kod, out = calistir(p3, "--arac", "ikisi", "--evet", "--zorla")
    test("--arac ikisi: Codex düzenine geri dönülebilir",
         kod == 0 and (p3 / ".agents" / "skills" / "gsap-core" / "SKILL.md").exists()
         and (p3 / ".claude" / "skills" / "gsap-core").is_symlink(), out)

    sys.path.insert(0, str(KOK / "araclar"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("se", KOK / "araclar" / "skill-ekle.py")
    se = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(se)
    sm = kok / "SKILL.md"
    sm.write_bytes(b"---\r\ndescription: x\r\n---\r\n\r\n```yaml\r\nname: ornek\r\n```\r\n")
    se.isim_esitle(sm, "yeni-ad")
    b = sm.read_bytes()
    test("ad eşitleme sadece frontmatter'a dokunur ve CRLF'yi korur",
         b.startswith(b"---\r\nname: yeni-ad\r\n") and b"name: ornek\r\n" in b, b.decode())

    # --- frontmatter/description onarımı (tetiklenme): kurulan kopyada düzeltilir
    from ortak import frontmatter, frontmatter_onar, frontmatter_teshis
    m, y = frontmatter_onar("<!-- uyarı -->\n---\nname: a\ndescription: \"x y\"\n---\n# Govde\n", "a")
    test("yorum arkasındaki frontmatter başa alınır, yorum korunur",
         m.startswith("---\nname: a\n") and "<!-- uyarı -->" in m and not frontmatter_teshis(m), m)
    m, y = frontmatter_onar("---\nname: a\ndescription: Track flakes in issue #12: rerun jobs.\nlicense: MIT\n---\n", "a")
    test("YAML'ı bozan tırnaksız description tırnaklanır, içerik aynı kalır",
         'description: "Track flakes in issue #12: rerun jobs."\nlicense: MIT' in m and not frontmatter_teshis(m), m)
    m, y = frontmatter_onar("# Baslik\n\n---\n\nmetin\n", "a", "Does X. Use when Y.")
    test("frontmatter yoksa düzeltme description'ıyla eklenir (gövdedeki --- çizgisi frontmatter sayılmaz)",
         m.startswith('---\nname: a\ndescription: "Does X. Use when Y."\n---\n\n# Baslik') and y == ["frontmatter eklendi"], m)
    m, y = frontmatter_onar("---\nname: a\ndescription: >\n  eski\n  uzun\nlicense: MIT\n---\nx\n", "a", "Yeni: aciklama")
    test("çok satırlı description düzeltmeyle tek satır olur, diğer alanlar korunur",
         frontmatter(m) == {"name": "a", "description": "Yeni: aciklama", "license": "MIT"}, m)
    m, y = frontmatter_onar("---\nname: a\nmeta:\n  k: v\n---\nx\n", "a", "Does X. Use when Y.")
    test("description yoksa name'in altına eklenir", m.startswith('---\nname: a\ndescription: "Does X. Use when Y."\nmeta:'), m)
    duz = "---\nname: a\ndescription: Saglam bir aciklama, Use when gerekli.\n---\n"
    test("sağlam frontmatter'a dokunulmaz", frontmatter_onar(duz, "a") == (duz, []))

    # --- kaynakta git symlink'i olan '../<kardeş>' taslakları ve kurulum yamaları
    ty = kok / "taslakli"
    (ty / "alt").mkdir(parents=True)
    (ty / "kardes-a").write_text("../kardes-a", encoding="utf-8")
    (ty / "SKILL.md").write_text("---\nname: taslakli\ndescription: x\n---\n[a](./kardes-a/SKILL.md) `kardes-a/x.md` [d](./yok/b.md)\n",
                                 encoding="utf-8")
    (ty / "alt" / "n.md").write_text("[a](../kardes-a/SKILL.md)\n", encoding="utf-8")
    se.symlink_taslaklarini_coz(ty)
    test("symlink taslağı silinir, bağlantıları kardeş yoluna çevrilir (diğer yollar değişmez)",
         not (ty / "kardes-a").exists() and "[a](../kardes-a/SKILL.md) `../kardes-a/x.md` [d](./yok/b.md)" in
         (ty / "SKILL.md").read_text(encoding="utf-8") and (ty / "alt" / "n.md").read_text(encoding="utf-8") == "[a](../../kardes-a/SKILL.md)\n",
         (ty / "SKILL.md").read_text(encoding="utf-8") + (ty / "alt" / "n.md").read_text(encoding="utf-8"))
    import ortak
    from ortak import git_blob_hash, yamalari_uygula
    eski_yamalar = ortak.YAMALAR
    ortak.YAMALAR = kok / "yamalar"
    try:
        (ortak.YAMALAR / "y-skill" / "scripts").mkdir(parents=True)
        (ortak.YAMALAR / "y-skill" / "scripts" / "a.py").write_text("print('duzeltildi')\n", encoding="utf-8")
        yk = kok / "yamali"
        (yk / "scripts").mkdir(parents=True)
        (yk / "scripts" / "a.py").write_text("print 'bozuk'\n", encoding="utf-8")
        kayit = {"id": "y-skill", "yama": {"dosyalar": {"scripts/a.py": git_blob_hash(b"print 'bozuk'\n")}}}
        test("yama, orijinal yazıldığı sürümle aynıysa uygulanır",
             yamalari_uygula(yk, kayit) == [("scripts/a.py", "uygulandi")]
             and (yk / "scripts" / "a.py").read_text(encoding="utf-8") == "print('duzeltildi')\n")
        (yk / "scripts" / "a.py").write_text("print('kaynakta yeni surum')\n", encoding="utf-8")
        test("kaynak değiştiyse yama uygulanmaz (yeni sürüm ezilmez)",
             yamalari_uygula(yk, kayit) == [("scripts/a.py", "eskidi")]
             and "yeni surum" in (yk / "scripts" / "a.py").read_text(encoding="utf-8"))
    finally:
        ortak.YAMALAR = eski_yamalar

    # --- Claude hesabındaki aynı adlı skill (anthropic-skills:<ad>) proje settings.json'da gizlenir
    eski_hesap = se.hesap_skilleri
    se.hesap_skilleri = lambda: {"docx": kok, "pdf": kok}
    try:
        hp = kok / "hesap-proje"
        (hp / ".claude").mkdir(parents=True)
        ayar = hp / ".claude" / "settings.json"
        ayar.write_text('{"permissions": {"allow": ["Bash(npm test)"]}, "skillOverrides": {"anthropic-skills:pdf": "on"}}',
                        encoding="utf-8")
        kl = {"skiller": {"docx": {}, "pdf": {}, "baska": {}}}
        se.hesap_gizle(hp, kl)
        d = json.loads(ayar.read_text(encoding="utf-8"))
        test("hesap skill'i 'off' yapılır, kullanıcının ayarları ve bilerek yazdığı 'on' korunur",
             d["permissions"] == {"allow": ["Bash(npm test)"]} and d["skillOverrides"] == {"anthropic-skills:docx": "off",
             "anthropic-skills:pdf": "on"} and kl["hesap_gizlenen"] == ["anthropic-skills:docx"], json.dumps(d) + str(kl))
        del kl["skiller"]["docx"]
        se.hesap_gizle(hp, kl)
        d = json.loads(ayar.read_text(encoding="utf-8"))
        test("skill kaldırılınca sadece aracın eklediği anahtar silinir",
             d["skillOverrides"] == {"anthropic-skills:pdf": "on"} and "hesap_gizlenen" not in kl, json.dumps(d))
        ayar.write_text("{bozuk", encoding="utf-8")
        hata = se.hesap_gizle(hp, {"skiller": {"docx": {}}})
        test("bozuk settings.json'a dokunulmaz, hata bildirilir", hata and ayar.read_text(encoding="utf-8") == "{bozuk", str(hata))
        ayar.unlink()
        kl = {"skiller": {"docx": {}}}
        se.hesap_gizle(hp, kl)
        kl["skiller"] = {}
        se.hesap_gizle(hp, kl)
        test("araç oluşturduğu settings.json boş kalınca siler", not ayar.exists())
    finally:
        se.hesap_skilleri = eski_hesap

    # --- kardeş skill bağımlılıkları (../<kardeş>/ bağlantıları)
    kd = kok / "kardes"
    ana_kok = kok / "baska-kategori" / "ana"  # arşivde kardeşler farklı kategori klasörlerinde durur
    for yer, govde in {ana_kok: "# ana\n", kd / "yan": "[r](../ana/references/x.md) [k](../yok-skill/a.md) [d](../../disari.md)\n"}.items():
        (yer / "references").mkdir(parents=True)
        (yer / "SKILL.md").write_text(f"---\nname: {yer.name}\n---\n{govde}", encoding="utf-8")
    (ana_kok / "references" / "x.md").write_text("x", encoding="utf-8")
    (kd / "yan" / "references" / "r.md").write_text("[a](../../ana/references/x.md) `../ana/` ../anaconda/\n", encoding="utf-8")
    spec_y = importlib.util.spec_from_file_location("ay", KOK / "araclar" / "arsiv-yerlestir.py")
    ay = importlib.util.module_from_spec(spec_y)
    spec_y.loader.exec_module(ay)
    kayit = lambda ad: {"id": ad, "ad": ad, "klasor_adi": ad, "repo": "r/r", "durum": "tercih"}
    kardes, cozulen = ay.kardes_baglantilari(kd / "yan", {"ana": [(kayit("ana"), ana_kok)]}, kayit("yan"))
    test("arşiv: ../<kardeş>/ bağlantısı kardeş bağımlılığı sayılır, kırık sayılmaz",
         kardes == {"ana": {"id": "ana", "dosya_sayisi": 2}} and cozulen == {"../ana/references/x.md"}
         and "../ana/references/x.md" in ay.kirik_baglantilar(kd / "yan"), str((kardes, cozulen)))
    se.kardes_yollarini_yeniden_adlandir(kd / "yan", {"ana": "ana--kutuphane"})
    test("kurulum: kardeş yolları dosya derinliğine göre projedeki ada çevrilir",
         "](../ana--kutuphane/references/x.md)" in (kd / "yan" / "SKILL.md").read_text(encoding="utf-8")
         and (kd / "yan" / "references" / "r.md").read_text(encoding="utf-8")
         == "[a](../../ana--kutuphane/references/x.md) `../ana/` ../anaconda/\n",
         (kd / "yan" / "references" / "r.md").read_text(encoding="utf-8"))

    reg = json_oku(KOK / "registry.json")["skiller"]
    idler = {s["id"]: s for s in reg}
    ornek = next((s for s in reg if s["durum"] == "tercih" and not s.get("kirik_baglantilar")
                  and len(s.get("kardes_bagimliliklari") or {}) == 1
                  and not idler[next(iter(s["kardes_bagimliliklari"].values()))["id"]].get("kardes_bagimliliklari")), None)
    if ornek:
        kad, bilgi = next(iter(ornek["kardes_bagimliliklari"].items()))
        p3 = kok / "proje3"
        p3.mkdir()
        kod, out = calistir(p3, "--skill", ornek["id"], "--kuru")
        test("kardeş skill kurulmuyorsa uyarılır", "kardes-eksik" in out and "kirik-baglanti" not in out, out)
        kod, out = calistir(p3, "--skill", ornek["id"], bilgi["id"], "--evet")
        kl3 = json_oku(p3 / ".skill-kutuphanesi" / "kilit.json")["skiller"]
        ad3 = next(a for a, k in kl3.items() if k["id"] == ornek["id"])
        kardes_ad = next(a for a, k in kl3.items() if k["id"] == bilgi["id"])
        kok3 = p3 / ".agents" / "skills" / ad3
        import os as _os, re as _re
        kirik3 = [h for f in kok3.rglob("*.md") for h in _re.findall(r"\]\(([^)\s#]+)", f.read_text(encoding="utf-8"))
                  if h.startswith("../") and _os.path.normpath(f.parent / h).startswith(str(kok3.parent))
                  and not Path(_os.path.normpath(f.parent / h)).exists()]
        test(f"kardeşle birlikte kurulunca ../{kad}/ bağlantıları projede çözülür (kardeş adı: {kardes_ad})",
             kod == 0 and not [l for l in out.splitlines() if "kardes-eksik" in l and (f"'{kad}'" in l or f"{kad} (" in l)]
             and not kirik3 and kl3[ad3].get("kardes") == {kad: kardes_ad},
             out + str(kirik3))

    kod, out = calistir(p2, "--kaldir", "gsap-core", "--evet")
    kod2, out2 = calistir(p2, "--geri-al")
    test("geri al: kaldırılan skill geri gelir", kod2 == 0 and (p2 / ".agents" / "skills" / "gsap-core" / "SKILL.md").exists(), out2)
    ad = out2.strip().split("--geri-al ")[-1].split()[0] if "--geri-al " in out2 else ""
    kod3, out3 = calistir(p2, "--geri-al", ad)
    test("geri almanın kendisi de geri alınabilir", kod3 == 0 and not (p2 / ".agents" / "skills" / "gsap-core").exists(), out3)

    # Kaynakta kaldırılan (emekli) skill kurulmak istenirse ön kontrol uyarır
    reg = json_oku(KOK / "registry.json")["skiller"]
    emekli = next((s for s in reg if s.get("kaynak_durumu") == "kaynakta-kaldirildi" and s["durum"] == "tercih"), None)
    if emekli:
        p3 = kok / "proje-emekli"
        p3.mkdir()
        kod, out = calistir(p3, "--skill", emekli["id"], "--kuru")
        test("emekli skill için ön kontrol 'kaynakta-kaldirildi' uyarısı verir", "kaynakta-kaldirildi" in out and not any(p3.iterdir()), out)

    # 'emekli' rolündeki (eski/yerine geçeni olan) skill ön kontrolde uyarı verir
    om_eski = next((s for s in reg if s.get("ortusme_rolu") == "emekli" and s["repo"] == "OpenMontageInc/OpenMontage" and s["durum"] == "tercih"), None)
    if om_eski:
        p4 = kok / "proje-emekli-om"
        p4.mkdir()
        kod, out = calistir(p4, "--skill", om_eski["id"], "--kuru")
        test("emekli (eski kopya) skill için ön kontrol 'emekli' uyarısı verir", "[UYARI] emekli" in out, out)

    # Ücretli skill ön kontrolde 'ucretli' uyarısı verir; ücretsiz skill vermez
    ucretli = next((s for s in reg if s.get("ucret") == "ucretli" and not s.get("gizli") and s["durum"] == "tercih"), None)
    ucretsiz = next((s for s in reg if s.get("ucret") == "ucretsiz" and not s.get("gizli") and s["durum"] == "tercih"
                     and not s.get("globalde")), None)
    if ucretli and ucretsiz:
        p5 = kok / "proje-ucret"
        p5.mkdir()
        kod, out = calistir(p5, "--skill", ucretli["id"], "--kuru")
        kod2, out2 = calistir(p5, "--skill", ucretsiz["id"], "--kuru")
        test("ücretli skill 'ucretli' uyarısı verir, ücretsiz vermez",
             "[UYARI] ucretli" in out and "[UYARI] ucretli" not in out2, out + out2)

    # Ücret dedektörü: yeni arşiv (.arsiv-yeni) yolundan okur; İngilizce "replicate"/"prepaid" yanlış pozitif vermez
    import importlib.util
    spec = importlib.util.spec_from_file_location("yerlestir", KOK / "araclar" / "arsiv-yerlestir.py")
    yer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(yer)
    yeni_arsiv = kok / "arsiv-yeni"
    for ad, metin in (("ucretli-iz", "Set FAL_KEY and call fal.ai"), ("fiil", "Replicate the experiment; book prepaid expenses.")):
        (yeni_arsiv / ad).mkdir(parents=True)
        (yeni_arsiv / ad / "SKILL.md").write_text(f"---\nname: {ad}\n---\n{metin}\n")
    s1 = {"id": "ucretli-iz", "ad": "ucretli-iz", "yol": "arsiv/ucretli-iz", "tip": "T1"}
    s2 = {"id": "fiil", "ad": "fiil", "yol": "arsiv/fiil", "tip": "T1"}
    test("ücret dedektörü yeni arşivdeki SKILL.md'yi okur (yeni skill sessizce 'ücretsiz' sayılmaz)",
         yer.ucret_belirle(s1, {}, yeni_arsiv)[0] == "belirsiz")
    test("'replicate' fiili / 'prepaid' muhasebe terimi ücretli iz sayılmaz", yer.ucret_belirle(s2, {}, yeni_arsiv)[0] == "ucretsiz")

    # Kimlik/tercih ataması KARARLI olmalı (yeni kaynak eşit öncelikte eskinin yerini alamaz; elle tercih ezilmez; tek tercih)
    def kayit(repo, kh, oncelik=3, yol="skills/x"):
        return {"ad": "x", "repo": repo, "kaynak_yol": yol, "_kh": kh, "oncelik": oncelik}
    eski = {("zzz/eski", "skills/x"): {"durum": "tercih", "id": "x"}}
    yeni = yer.kimlik_ata({"x": [kayit("aaa/yeni", "H2"), kayit("zzz/eski", "H1")]}, eski)
    d = {k["repo"]: k for k in yeni}
    test("kimlik: eşit öncelikte alfabetik önce gelen YENİ kaynak eski kaydın tercihini/kimliğini almaz",
         d["zzz/eski"]["durum"] == "tercih" and d["zzz/eski"]["id"] == "x" and d["aaa/yeni"]["durum"] == "alternatif", str(yeni))
    yeni = yer.kimlik_ata({"x": [kayit("aaa/yeni", "H1"), kayit("zzz/eski", "H1")]}, eski)
    test("kimlik: birebir aynı içerikte ESKİ (incelenmiş) kayıt temsilci kalır, yeni kopya olarak notlanır",
         len(yeni) == 1 and yeni[0]["repo"] == "zzz/eski" and any("aaa/yeni" in c for c in yeni[0].get("kopya_kaynaklar", [])), str(yeni))
    eski2 = {("zzz/eski", "skills/x"): {"durum": "tercih", "durum_elle": True, "id": "x"}}
    yeni = yer.kimlik_ata({"x": [kayit("aaa/oto", "H3", oncelik=1), kayit("zzz/eski", "H1", oncelik=5)]}, eski2)
    test("kimlik: elle verilen tercih (durum_elle) otomatik tercihi ezer ve aynı adda TEK tercih kalır",
         sorted(k["durum"] for k in yeni) == ["alternatif", "tercih"]
         and next(k for k in yeni if k["durum"] == "tercih")["repo"] == "zzz/eski", str(yeni))

    eski3 = {("aaa/p", "skills/x"): {"durum": "alternatif", "id": "x@aaa"}, ("zzz/q", "skills/x"): {"durum": "tercih", "id": "x"}}
    yeni = yer.kimlik_ata({"x": [kayit("aaa/p", "H1"), kayit("zzz/q", "H2")]}, eski3)
    d = {k["repo"]: k for k in yeni}
    test("kimlik: eşit öncelikte ÖNCEKİ tercih kalır (alfabetik sıra çevirmez) ve kimlikler korunur (tam çalıştırma kaymaz)",
         d["zzz/q"]["durum"] == "tercih" and d["zzz/q"]["id"] == "x" and d["aaa/p"]["id"] == "x@aaa" and d["aaa/p"]["durum"] == "alternatif", str(yeni))
    yeni = yer.kimlik_ata({"x": [kayit("aaa/p", "H1"), kayit("zzz/q", "H2")]}, eski3)
    test("kimlik: aynı girdiyle ikinci çalıştırma aynı sonucu verir (idempotent)",
         [(k["repo"], k["id"], k["durum"]) for k in sorted(yeni, key=lambda k: k["repo"])]
         == [(k["repo"], k["id"], k["durum"]) for k in sorted(yer.kimlik_ata({"x": [kayit("aaa/p", "H1"), kayit("zzz/q", "H2")]}, eski3), key=lambda k: k["repo"])])

    # Çıplak ad kendiliğinden el değiştirmez (kısmi eklemede yeni kaynak öncelikle kazansa bile); devir sadece ad_devral ile
    test("kimlik devri: eski kayıt çıplak adı taşıyorsa ve devir işaretli değilse kimlik KORUNUR",
         yer.kimlik_devri(True, True, False) == "korunur")
    test("kimlik devri: ad_devral işaretliyse çıplak ad yeni kazanana DEVREDİLİR", yer.kimlik_devri(True, True, True) == "devret")
    test("kimlik devri: kaybeden yeni kayıtsa ad@kaynak alır; kimliği zaten ekliyse dokunulmaz",
         yer.kimlik_devri(False, True, False) == "ekle" and yer.kimlik_devri(True, False, True) == "yok"
         and yer.kimlik_devri(False, False, False) == "yok")

    # Trend: seviye hesabı, değerlendirme bonusu ve öneride sadece konuya uygun skille bonus
    from ortak import trend_durumu
    from datetime import date as _d, timedelta as _td
    gun = lambda n: (_d.today() - _td(days=n)).isoformat()  # noqa: E731  (testler tarihten bağımsız: hep bugüne göre)
    tr = {"son_tarama": gun(3), "gecmis": {"a/b": {"ilk": gun(30), "son": gun(3), "gorulme": 3},
                                           "c/d": {"ilk": gun(200), "son": gun(60), "gorulme": 1},
                                           "e/f": {"ilk": gun(900), "son": gun(500), "gorulme": 1}}}
    test("trend seviyeleri: trendde / yakinda / gecmiste / yok",
         [(trend_durumu(r, tr) or {}).get("seviye") for r in ("a/b", "c/d", "e/f", "x/y")] == ["trendde", "yakinda", "gecmiste", None])
    tr_eski = {"son_tarama": gun(60), "gecmis": {"a/b": {"ilk": gun(90), "son": gun(60), "gorulme": 3}}}
    test("trend bonusu söner: tarama durursa (60 gün önce) 'trendde' olmaz, 'yakinda'ya düşer",
         trend_durumu("a/b", tr_eski)["seviye"] == "yakinda")
    spec = importlib.util.spec_from_file_location("skillekle", KOK / "araclar" / "skill-ekle.py")
    ekle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ekle)
    taban = {"id": "x", "aciklama": "android compose helper", "kategori": "b/08-mobil", "teknoloji_oto": [],
             "degerlendirme": {"puan": 80}, "durum": "tercih", "ucret": "ucretsiz"}
    p_yok = ekle.puanla(dict(taban), ["android"], set())[0]
    p_trend = ekle.puanla(dict(taban, trend={"seviye": "trendde"}), ["android"], set())[0]
    p_alakasiz = ekle.puanla(dict(taban, trend={"seviye": "trendde"}), ["video"], set())[0]
    test("öneride trend bonusu: uygun skill öne çıkar, alakasız skill trend yüzünden öneriye girmez",
         p_trend > p_yok and p_alakasiz == 0, f"{p_yok} {p_trend} {p_alakasiz}")

    # Programlar: kaynak kartında kopya ve KAYNAK.md yerinde; yerinde kartında alanlar tam (program bu bilgisayarda kurulu olmak ZORUNDA DEĞİL)
    _prog = json_oku(KOK / "programlar.json", {"programlar": {}})["programlar"]
    _kay = {r["repo"]: r for r in json_oku(KOK / "kaynaklar.json")["repolar"]}
    for _ad, _p in _prog.items():
        _kart_kaynak = (KOK / "programlar" / _ad / "KAYNAK.md").exists() and _kay.get(_p["repo"], {}).get("program") == _ad
        if _p.get("kopya", "kaynak") == "yerinde":
            _y = _p.get("yerinde") or {}
            _tur = _y.get("tur")
            _alanlar = (_tur in ("npm-global", "git-checkout") and bool(str(_y.get("yol", "")).strip())
                        and (bool(_y.get("paket")) if _tur == "npm-global" else bool(_y.get("dal")))
                        and bool(_p.get("kutuphane_surumu") or _p.get("kutuphane_commit"))
                        and "kaynak_kopyasi" not in _p)
            test(f"program {_ad} (yerinde): tür/yol/paket-dal/sürüm alanları tam, KAYNAK.md ve kaynaklar.json program kaydı var",
                 _alanlar and _kart_kaynak)
            continue
        _k = KOK / _p["kaynak_kopyasi"]
        test(f"program {_ad}: kaynak kopyası ve KAYNAK.md var, kaynaklar.json'da program kaydı eşleşiyor",
             _k.is_dir() and any(_k.iterdir()) and _kart_kaynak)
    spec = importlib.util.spec_from_file_location("progden", KOK / "araclar" / "program-denetim.py")
    progden = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(progden)
    test("program denetimi: sürüm karşılaştırma (eski/güncel/anlaşılmaz)",
         progden.durum("0.5.0", "v0.6.0") == "YENİ SÜRÜM VAR" and progden.durum("0.5.0", "v0.5.0") == "güncel"
         and progden.durum("0.5.0", None) == "öğrenilemedi")
    _sha1, _sha2 = "a" * 40, "b" * 40
    _yd = progden.yerinde_durum
    def _t(ad, kosul):
        test(f"yerinde durum: {ad}", bool(kosul))
    _t("npm güncel", _yd("npm-global", "1.2.0", "1.2.0", "1.2.0") == "güncel")
    _t("npm yeni sürüm var", _yd("npm-global", "1.2.0", "1.2.0", "1.3.0") == "YENİ SÜRÜM VAR")
    _t("npm kurulu > son: güncel", _yd("npm-global", "1.2.0", "1.2.0", "1.1.0") == "güncel")
    _t("npm kart eski (son var)", _yd("npm-global", "1.2.0", "1.2.1", "1.2.1") == "KART ESKİ")
    _t("npm kart eski (son yok)", _yd("npm-global", "1.2.0", "1.2.1", None) == "KART ESKİ")
    _t("npm kart boş, kurulu dolu: kart eski", _yd("npm-global", None, "1.2.1", "1.2.1") == "KART ESKİ")
    _t("npm kurulu değil", _yd("npm-global", "1.2.0", None, "1.3.0") == "bu bilgisayarda kurulu değil")
    _t("npm son yok: öğrenilemedi", _yd("npm-global", "1.2.0", "1.2.0", None) == "öğrenilemedi")
    _t("npm son bozuk: öğrenilemedi", _yd("npm-global", "1.2.0", "1.2.0", "bozuk") == "öğrenilemedi")
    _t("npm 'v' öneki yok sayılır", _yd("npm-global", "v1.2.0", "1.2.0", "1.2.0") == "güncel")
    _t("npm kısa sürüm 1.2 = 1.2.0", _yd("npm-global", "1.2", "1.2.0", "1.2.0") == "güncel")
    _t("npm ön-sürüm eşit: öğrenilemedi (KART ESKİ değil)", _yd("npm-global", "1.2.0-beta.1", "1.2.0-beta.1", "1.2.0") == "öğrenilemedi")
    _t("npm ön-sürüm kurulu, kart farklı: kart eski", _yd("npm-global", "1.1.0", "1.2.0-beta.1", "1.2.0") == "KART ESKİ")
    _t("git güncel", _yd("git-checkout", _sha1, _sha1, _sha1) == "güncel")
    _t("git yeni sürüm var", _yd("git-checkout", _sha1, _sha1, _sha2) == "YENİ SÜRÜM VAR")
    _t("git sha farklı, geride 3: yeni sürüm var", _yd("git-checkout", _sha1, _sha1, _sha2, 3) == "YENİ SÜRÜM VAR")
    _t("git sha farklı, geride bilinmiyor: yeni sürüm var", _yd("git-checkout", _sha1, _sha1, _sha2, None) == "YENİ SÜRÜM VAR")
    _t("git yerel ileride (geride 0): güncel", _yd("git-checkout", _sha1, _sha1, _sha2, 0) == "güncel")
    _t("git kart eski", _yd("git-checkout", _sha1, _sha2, _sha2) == "KART ESKİ")
    _t("git kurulu değil", _yd("git-checkout", _sha1, None, _sha2) == "bu bilgisayarda kurulu değil")
    _t("git son yok: öğrenilemedi", _yd("git-checkout", _sha1, _sha1, None) == "öğrenilemedi")
    _t("git kısa önek eşleşir", _yd("git-checkout", _sha1[:8], _sha1, _sha1) == "güncel")
    _t("git çok kısa önek eşleşmez", _yd("git-checkout", "abc", "abc", "abc") == "KART ESKİ")
    test("sürüm ayıklama: sondaki sıfırlar atılır, ön-sürüm anlaşılmaz",
         progden.surum_ayikla("1.2") == progden.surum_ayikla("1.2.0") == progden.surum_ayikla("v1.2.0.0")
         and progden.surum_ayikla("1.2.1") > progden.surum_ayikla("1.2") and progden.surum_ayikla("1.0.0-rc1") is None)
    # git_kurulu: git_okuma sahte (gerçek git ve gerçek yol yok)
    _gok = progden.git_okuma
    def _sahte(top, sha="s" * 40, st=" M a\n?? b\n"):
        def f(yol, *args):
            return {"--show-toplevel": top, "HEAD": sha, "--porcelain": st}[args[-1]]
        return f
    try:
        _yol = "/tmp/sahte-yol"
        progden.git_okuma = _sahte(_yol + "\n")
        test("git_kurulu: yol deponun kökü, status okunur", progden.git_kurulu(_yol) == ("s" * 40, 1, 1))
        progden.git_okuma = _sahte("/tmp/baska-ust-depo\n")
        test("git_kurulu: yol deponun kökü değilse (üst klasördeki depo) kurulu sayılmaz", progden.git_kurulu(_yol) == (None, 0, 0))
        progden.git_okuma = _sahte(None)
        test("git_kurulu: depo değil/yol yok", progden.git_kurulu(_yol) == (None, 0, 0))
        progden.git_okuma = _sahte(_yol, st=None)
        test("git_kurulu: status başarısızsa değişen/izlenmeyen None (temiz sayılmaz)", progden.git_kurulu(_yol) == ("s" * 40, None, None))
        test("yerel_metin: status okunamadı -> öğrenilemedi",
             progden.yerel_metin({"tur": "git-checkout", "kurulu": "x", "degisen": None, "izlenmeyen": None}) == "öğrenilemedi"
             and progden.yerel_metin({"tur": "git-checkout", "kurulu": "x", "degisen": 0, "izlenmeyen": 0}) == "temiz"
             and progden.yerel_metin({"tur": "npm-global", "kurulu": "1", "degisen": 0, "izlenmeyen": 0}) == "-")
    finally:
        progden.git_okuma = _gok
    test("git status --porcelain sayımı: değişen / izlenmeyen",
         progden.porcelain_say(" M a.py\nM  b.py\n?? c.txt\n?? d/\n!! e.log\n") == (2, 2)
         and progden.porcelain_say("") == (0, 0) and progden.porcelain_say(None) == (0, 0))
    _ku = progden.kisit_uyar
    test("sabit sürüm kısıtı: tam eşleşme ve ==", _ku("1.2.3", "1.2.3") is True and _ku("==1.2.3", "1.2.3") is True
         and _ku("1.2.3", "1.2.4") is False and _ku("1.0", None) is False)
    test("sabit sürüm kısıtı: aralık ve anlaşılmaz", _ku(">=1.0,<2", "1.9.1") is True and _ku(">=1.0,<2", "2.0") is False
         and _ku("~=1.0", "1.0") is None)
    test("sabit sürüm kısıtı: ön-sürüm metni eşitse True, farklıysa False (anlaşılmadı değil)",
         _ku("1.0.0rc1", "1.0.0rc1") is True and _ku("==1.0.0rc1", "1.0.0rc1") is True and _ku("1.0.0rc1", "1.0.0rc2") is False)
    test("sabit sürüm kısıtı: kısa/uzun sürüm eşit sayılır", _ku("2.0", "2.0.0") is True and _ku("<=1.0", "1.0.0") is True)
    with tempfile.TemporaryDirectory() as _gt:
        _gt = Path(_gt)
        test("package.json okuma: sürüm var / dosya yok / bozuk dosya",
             progden.npm_kurulu_surum(_gt / "yok") is None
             and (_gt.joinpath("pkg").mkdir() or _gt.joinpath("pkg", "package.json").write_text('{"name":"x","version":"2.4.1"}') > 0)
             and progden.npm_kurulu_surum(_gt / "pkg") == "2.4.1"
             and (_gt.joinpath("kotu").mkdir() or _gt.joinpath("kotu", "package.json").write_text("{bozuk") > 0)
             and progden.npm_kurulu_surum(_gt / "kotu") is None)
        _site = _gt / "venv" / "lib" / "python3.11" / "site-packages"
        for _dn, _ad, _sv in (("Foo_Bar-1.5.0.dist-info", "Foo_Bar", "1.5.0"), ("numpy-1.26.4.dist-info", "numpy", "1.26.4"),
                              ("hasarli-0.1.dist-info", None, None)):
            (_site / _dn).mkdir(parents=True)
            if _ad:
                (_site / _dn / "METADATA").write_text(f"Metadata-Version: 2.1\nName: {_ad}\nVersion: {_sv}\n\nVersion: sahte\n")
        _okunan = progden.dist_info_oku(_gt / "venv")
        test("dist-info okuma: ad normalleşir, gövdedeki 'Version:' sayılmaz, METADATA'sız klasör atlanır",
             _okunan == {"foo-bar": "1.5.0", "numpy": "1.26.4"} and progden.dist_info_oku(_gt / "yok") == {}, str(_okunan))
        for _dn, _sv in (("zeta-2.0.0.dist-info", "2.0.0"), ("zeta-1.0.0.dist-info", "1.0.0"), ("zeta-1.5.0.dist-info", "1.5.0")):
            (_site / _dn).mkdir()
            (_site / _dn / "METADATA").write_text(f"Name: zeta\nVersion: {_sv}\n")
        test("dist-info okuma: aynı paketin birden çok kaydı varsa en yüksek sürüm (sıradan bağımsız)",
             progden.dist_info_oku(_gt / "venv").get("zeta") == "2.0.0")
        _uyan, _fark = progden.pin_karsilastir({"foo.bar": "1.5.0", "numpy": "1.26.0", "yok-paket": "1.0", "x": "~=1"},
                                               dict(_okunan, x="1.0"))
        test("sabit sürüm karşılaştırma: uyan sayısı ve farklar (farklı sürüm, kurulu değil, anlaşılmayan kısıt)",
             _uyan == 1 and len(_fark) == 3 and any("numpy" in f and "1.26.4" in f for f in _fark)
             and any("kurulu değil" in f for f in _fark) and any("anlaşılmadı" in f for f in _fark), str(_fark))
        # yerinde kart: uçtan uca, geçici kart + geçici rapor (ağ yok: yol yoksa ağa gidilmez; gerçek program yolları kullanılmaz)
        _kart = {"programlar": {"deneme": {"repo": "x/y", "kopya": "yerinde", "kutuphane_surumu": "1.0.0",
                                           "yerinde": {"tur": "npm-global", "yol": str(_gt / "yok-program"), "paket": "yok-paket"}}}}
        (_gt / "kart.json").write_text(json.dumps(_kart))
        _pk = progden.main(["--kart", str(_gt / "kart.json"), "--cikti", str(_gt / "rapor.md")])
        _rapor = (_gt / "rapor.md").read_text(encoding="utf-8") if (_gt / "rapor.md").exists() else ""
        test("program denetimi: kurulu olmayan 'yerinde' kart hata değil, rapora 'bu bilgisayarda kurulu değil' yazılır, çıkış 0",
             _pk == 0 and "bu bilgisayarda kurulu değil" in _rapor and "Yerinde izlenen" in _rapor, _rapor)

    # bozuk 'yerinde' kartlar çıkış kodunu bozmaz; ağa gidilmez (npm_son_surum sahte)
    with tempfile.TemporaryDirectory() as _gt2:
        _gt2 = Path(_gt2)
        (_gt2 / "pkg").mkdir()
        (_gt2 / "pkg" / "package.json").write_text('{"version":"1.0.0"}')
        _nson, _nku = progden.npm_son_surum, progden.npm_kurulu_surum
        progden.npm_son_surum = lambda *a, **k: None
        try:
            _bozuk = {"programlar": {
                "liste-pin": {"repo": "x/y", "kopya": "yerinde", "kutuphane_surumu": "1.0.0", "venv": ".venv", "sabit_surumler": ["numpy"],
                              "yerinde": {"tur": "npm-global", "yol": str(_gt2 / "pkg"), "paket": "p"}},
                "reposuz": {"kopya": "yerinde", "kutuphane_surumu": "1.0.0",
                            "yerinde": {"tur": "npm-global", "yol": str(_gt2 / "pkg"), "paket": "p"}}}}
            (_gt2 / "k.json").write_text(json.dumps(_bozuk))
            _c1 = progden.main(["--kart", str(_gt2 / "k.json"), "--cikti", str(_gt2 / "r1.md")])
            test("program denetimi: bozuk sabit_surumler ve repo'suz kart çökmez, çıkış 0", _c1 == 0 and (_gt2 / "r1.md").exists())
            progden.npm_kurulu_surum = lambda *a, **k: 1 / 0
            _c2 = progden.main(["--kart", str(_gt2 / "k.json"), "--cikti", str(_gt2 / "r2.md")])
            _r2 = (_gt2 / "r2.md").read_text(encoding="utf-8")
            test("program denetimi: denetim sırasında beklenmeyen hata -> 'öğrenilemedi', çıkış 0", _c2 == 0 and "öğrenilemedi" in _r2, _r2)
        finally:
            progden.npm_son_surum, progden.npm_kurulu_surum = _nson, _nku

    # Kapsam denetimi: GitHub'da silinmiş kaynak (404) denetimi çökertmez (aylık zincir geri alınmasın)
    import ortak as _ortak
    spec = importlib.util.spec_from_file_location("kapsam", KOK / "araclar" / "kapsam-denetimi.py")
    kapsam = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(kapsam)
    def _yok(repo, sha=None):
        raise _ortak.GhBulunamadi(f"{repo}: HTTP 404")
    def _var(repo, sha=None):
        return "abc", {"tree": [], "truncated": False, "_kaynak": "api"}
    kapsam.repo_agaci = _yok
    test("kapsam denetimi: silinmiş repo (404) çökertmez, 'erişilemeyen' olarak döner", kapsam.agac_al("x/silinmis") is None)
    kapsam.repo_agaci = _var
    test("kapsam denetimi: var olan repo ağacı normal döner", kapsam.agac_al("x/var") == {"tree": [], "truncated": False, "_kaynak": "api"})

    for g in GLOBAL_KLASORLER.values():
        kod, out = calistir(g, "--skill", "gsap-core", "--evet")
        test(f"güvenlik: {g} reddedilir", kod != 0 and "Güvenlik" in out, out)
        break
    kod, out = calistir(KOK, "--skill", "gsap-core", "--evet")
    test("güvenlik: kütüphanenin kendisi reddedilir", kod != 0 and "Güvenlik" in out, out)

    # Repo GitHub'da taşınırsa (kaynaklar.json -> eski_adlar) kilitteki eski ad kaynağını bulmaya devam eder
    import ortak as _ortak
    _onceki_takma = _ortak._TAKMA_ADLAR
    _ortak._TAKMA_ADLAR = {"eski-sahip/depo": "yeni-sahip/depo"}
    try:
        _reg = [{"id": "x", "ad": "x", "repo": "yeni-sahip/depo", "kaynak_yol": "skills/x", "durum": "tercih"}]
        test("repo adı değişikliği: kilitteki eski repo adı güncel kaynağı bulur",
             ekle.kaynak_bul(_reg, {"id": "x", "repo": "Eski-Sahip/Depo", "kaynak_yol": "skills/x"}) is _reg[0]
             and ekle.kurulum_adi(_reg[0], {"skiller": {"x-eski-ad": {"repo": "eski-sahip/depo", "kaynak_yol": "skills/x"}}}) == "x-eski-ad")
        test("repo adı değişikliği: başka repodaki aynı adlı skill yerine konmaz",
             ekle.kaynak_bul(_reg, {"id": "x", "repo": "baska/depo", "kaynak_yol": "skills/x"}) is None)
    finally:
        _ortak._TAKMA_ADLAR = _onceki_takma
    _adas = next((s for s in json_oku(KOK / "registry.json")["skiller"]
                  if s["durum"] == "tercih" and s["id"] == s["ad"] and not s.get("gizli")
                  and any(x["ad"] == s["ad"] and x["id"] != s["id"] for x in json_oku(KOK / "registry.json")["skiller"])), None)
    if _adas:
        pa = kok / "p-adas"
        pa.mkdir()
        kod, out = calistir(pa, "--skill", _adas["id"], "--kuru")
        test("ön kontrol: aynı adlı başka skill varsa 'ayni-ad' bilgisi kurulan kaynağı ve diğerlerini gösterir",
             "ayni-ad" in out and _adas["repo"] in out, out[-500:])
    pk_k = subprocess.run([sys.executable, str(KOK / "araclar" / "proje-kullanimi.py"), "--kontrol"], capture_output=True, text=True)
    test("proje-kullanimi --kontrol: test projeleri (geçici klasör) raporu etkilemez, rapor güncel", pk_k.returncode == 0, pk_k.stdout)
    pk = subprocess.run([sys.executable, str(KOK / "araclar" / "proje-kullanimi.py"), "--skill", "boyle-bir-skill-yok"],
                        capture_output=True, text=True)
    test("proje-kullanimi: bilinmeyen skill için boş sonuç, rapor yazmaz", pk.returncode == 0 and "kullanılmıyor" in pk.stdout,
         pk.stdout + pk.stderr)
    yol_testleri()
    kurulum_yol_testleri()
    test("global klasörler test boyunca DEĞİŞMEDİ", parmak_izi() == once)
    shutil.rmtree(kok, ignore_errors=True)
    basarisiz = [a for a, ok in SONUC if not ok]
    print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
    sys.exit(1 if basarisiz else 0)


if __name__ == "__main__":
    main()
