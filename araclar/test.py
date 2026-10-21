#!/usr/bin/env python3
"""Uçtan uca test: geçici bir projede skill-ekle.py'nin tüm güvenlik senaryolarını dener.
Global klasörlerin test boyunca değişmediğini de kontrol eder. Kütüphaneyi değiştirmez.

Kullanım: python3 araclar/test.py
"""
import hashlib
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
                h.update(p.name.encode())
                h.update(str(p.lstat().st_mtime_ns).encode())
    return h.hexdigest()


def agac(p: Path):
    return sorted(str(x.relative_to(p)) for x in p.rglob("*"))


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
    (proje / ".agents" / "skills" / "gsap-core").mkdir(parents=True)
    (proje / ".agents" / "skills" / "gsap-core" / "SKILL.md").write_text("---\nname: gsap-core\n---\nbenim\n", encoding="utf-8")
    kod, out = calistir(proje, "--skill", "gsap-core", "--evet")
    test("projedeki kendi skill'inin üzerine yazılmaz", kod == 2 and "projede-kendi-skillin" in out
         and "benim" in (proje / ".agents" / "skills" / "gsap-core" / "SKILL.md").read_text(encoding="utf-8"), out)
    shutil.rmtree(proje / ".agents" / "skills" / "gsap-core")

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

    for g in GLOBAL_KLASORLER.values():
        kod, out = calistir(g, "--skill", "gsap-core", "--evet")
        test(f"güvenlik: {g} reddedilir", kod != 0 and "Güvenlik" in out, out)
        break
    kod, out = calistir(KOK, "--skill", "gsap-core", "--evet")
    test("güvenlik: kütüphanenin kendisi reddedilir", kod != 0 and "Güvenlik" in out, out)

    test("global klasörler test boyunca DEĞİŞMEDİ", parmak_izi() == once)
    shutil.rmtree(kok, ignore_errors=True)
    basarisiz = [a for a, ok in SONUC if not ok]
    print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
    sys.exit(1 if basarisiz else 0)


if __name__ == "__main__":
    main()
