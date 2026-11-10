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
             kod == 0 and "kardes-eksik" not in out and not kirik3 and kl3[ad3].get("kardes") == {kad: kardes_ad},
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

    # Programlar: her kartın kaynak kopyası ve KAYNAK.md'si yerinde, repo kaynaklar.json'da 'program' alanıyla kayıtlı
    _prog = json_oku(KOK / "programlar.json", {"programlar": {}})["programlar"]
    _kay = {r["repo"]: r for r in json_oku(KOK / "kaynaklar.json")["repolar"]}
    for _ad, _p in _prog.items():
        _k = KOK / _p["kaynak_kopyasi"]
        test(f"program {_ad}: kaynak kopyası ve KAYNAK.md var, kaynaklar.json'da program kaydı eşleşiyor",
             _k.is_dir() and any(_k.iterdir()) and (_k.parent / "KAYNAK.md").exists()
             and _kay.get(_p["repo"], {}).get("program") == _ad)
    spec = importlib.util.spec_from_file_location("progden", KOK / "araclar" / "program-denetim.py")
    progden = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(progden)
    test("program denetimi: sürüm karşılaştırma (eski/güncel/anlaşılmaz)",
         progden.durum("0.5.0", "v0.6.0") == "YENİ SÜRÜM VAR" and progden.durum("0.5.0", "v0.5.0") == "güncel"
         and progden.durum("0.5.0", None) == "öğrenilemedi")

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
    test("global klasörler test boyunca DEĞİŞMEDİ", parmak_izi() == once)
    shutil.rmtree(kok, ignore_errors=True)
    basarisiz = [a for a, ok in SONUC if not ok]
    print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
    sys.exit(1 if basarisiz else 0)


if __name__ == "__main__":
    main()
