#!/usr/bin/env python3
"""Duman testi: kütüphanenin TÜM sürecinin çalıştığını uçtan uca, hızlıca dener. Kütüphaneyi ve global klasörleri değiştirmez.

  python3 araclar/duman-testi.py            # ~3-5 dk (ağ: GitHub kontrolü + kapsam denetimi)
  python3 araclar/duman-testi.py --araclar  # + gerçek Claude ve Codex'in kurulan skilleri gördüğünü sorar (birkaç dk daha)

Adımlar:
  1. Git: master'da, temiz, bekleyen/bozuk durum yok
  2. dogrula.py --github (registry, roller, profiller, örtüşme grupları, git'e girmeyen arşiv dosyası, yıldızlar)
  3. kapsam-denetimi.py (her SKILL.md açıklanmış mı; GitHub'dan bağımsız sayım)
  4. katalog-uret.py idempotent mi (yeniden üretince git'te fark çıkmamalı)
  5. test.py (skill-ekle güvenlik senaryoları)
  6. arsiv-guncelle.py rapor modu çalışıyor mu (hiçbir şey değiştirmeden)
  7. skill-ekle: --listele, --oner, tüm profillerin --opsiyonel --kuru'su (HATA/bağlam yok, --kuru dosya yazmaz)
  8. Gerçek kurulum yaşam döngüsü (geçici proje): --evet → --dogrula → --durum → --guncelle --kuru → --kaldir hepsi → --geri-al
  9. (--araclar) Claude ve Codex kurulan skilleri görüyor mu
 10. Global skill klasörleri değişmedi mi
"""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GLOBAL_KLASORLER, KOK  # noqa: E402

PY = sys.executable
SONUC = []


def kos(*args, cwd=KOK, timeout=900):
    r = subprocess.run(list(args), cwd=cwd, capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout + r.stderr


def adim(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {ayrinti.strip()[-500:]}"))


def parmak_izi():
    h = hashlib.sha256()
    for g in GLOBAL_KLASORLER.values():
        if g.exists():
            for p in sorted(g.iterdir()):
                if p.name == "synced":  # Claude uygulamasının hesap senkronizasyonu (bizim araçlarımız yazmaz)
                    continue
                h.update(p.name.encode())
                h.update(str(p.lstat().st_mtime_ns).encode())
    return h.hexdigest()


def main():
    araclar = "--araclar" in sys.argv
    once_iz = parmak_izi()
    print("1) Git")
    dal = kos("git", "branch", "--show-current")[1].strip()
    kirli = kos("git", "status", "--porcelain")[1].strip()
    adim(f"master dalında ({dal})", dal == "master")
    adim("çalışma ağacı temiz", not kirli, kirli)
    _, wt = kos("git", "worktree", "list")
    adim("ek worktree yok", len(wt.strip().splitlines()) == 1, wt)
    _, bek = kos("git", "branch", "--list", "guncelleme/*", "--format=%(refname:short)")
    print(f"     bilgi: onay bekleyen güncelleme dalı: {bek.split() or '-'}")

    print("2) Doğrulama")
    k, o = kos(PY, "araclar/dogrula.py", "--github")
    adim("dogrula.py --github: 0 hata", k == 0 and " 0 hata" in o, o)
    adim("dogrula.py: 0 uyarı", " 0 uyarı" in o, o)

    print("3) Kapsam denetimi")
    k, o = kos(PY, "araclar/kapsam-denetimi.py")
    adim("her SKILL.md açıklanmış (0 sorun)", k == 0 and "sorun: 0" in o, o)

    print("4) Katalog idempotent")
    k, o = kos(PY, "araclar/katalog-uret.py")
    fark = kos("git", "status", "--porcelain")[1].strip()
    adim("katalog yeniden üretilince fark yok", k == 0 and fark == kirli, fark)

    print("5) Güvenlik testleri")
    k, o = kos(PY, "araclar/test.py")
    adim(o.strip().splitlines()[-1] if o.strip() else "test.py", k == 0, o)

    print("6) Güncelleme raporu")
    k, o = kos(PY, "araclar/arsiv-guncelle.py")
    adim("arsiv-guncelle.py rapor modu çalışıyor", "Traceback" not in o, o)
    adim("rapor modu hiçbir şey değiştirmedi", kos("git", "status", "--porcelain")[1].strip() == kirli)

    print("7) Öneri, liste, profiller")
    k, o = kos(PY, "araclar/skill-ekle.py", "--listele", "--kategori", "03")
    adim("--listele çalışıyor", k == 0 and " skill" in o, o)
    k, o = kos(PY, "araclar/skill-ekle.py", "--oner", "next.js landing page gsap animasyon")
    adim("--oner tüm kütüphaneyi tarıyor", k == 0 and "Taranan:" in o, o)
    bos = Path(tempfile.mkdtemp(prefix="duman-kuru-"))
    profiller = sorted(p.stem for p in (KOK / "profiller").glob("*.json"))
    sorunlu = []
    for p in profiller:
        k, o = kos(PY, "araclar/skill-ekle.py", str(bos), "--profil", p, "--opsiyonel", "--kuru")
        if "[HATA]" in o or "baglam-yuku" in o or "Traceback" in o:
            sorunlu.append(p)
    adim(f"{len(profiller)} profilin --opsiyonel --kuru'su temiz", not sorunlu, ", ".join(sorunlu))
    adim("--kuru hiçbir dosya yazmadı", not any(bos.iterdir()))
    shutil.rmtree(bos, ignore_errors=True)

    print("8) Kurulum yaşam döngüsü")
    pj = Path(tempfile.mkdtemp(prefix="duman-proje-"))
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--profil", "landing-page", "--evet")
    adim("kurulum (--evet) + otomatik doğrulama ✅", k == 0 and "doğrulama: ✅" in o, o)
    kilit = json.loads((pj / ".skill-kutuphanesi" / "kilit.json").read_text(encoding="utf-8"))
    n = len(kilit["skiller"])
    adim(f"{n} skill hem .agents/skills hem .claude/skills'te", all(
        (pj / ".agents" / "skills" / a / "SKILL.md").exists() and (pj / ".claude" / "skills" / a / "SKILL.md").exists()
        for a in kilit["skiller"]))
    adim("Claude ve Codex agent dosyaları", all((pj / ".claude" / "agents" / f"{r}.md").exists()
                                               and (pj / ".codex" / "agents" / f"{r}.toml").exists() for r in kilit["roller"]))
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--dogrula")
    adim("--dogrula temiz", k == 0, o)
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--durum")
    adim("--durum: hepsi güncel", k == 0 and o.count("güncel") >= n, o)
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--guncelle", "--kuru")
    adim("--guncelle --kuru: güncellenecek yok", k == 0 and "Güncellenecek/onarılacak: 0" in o, o)
    if araclar:
        print("9) Gerçek araçlar")
        kos("git", "init", "-q", cwd=pj)
        k, o = kos("claude", "-p", "Do not use tools. Reply exactly: 'SKILLS=<count of skills in this project .claude/skills>'",
                   "--max-turns", "1", cwd=pj, timeout=600)
        adim(f"Claude {n} skill'i görüyor", f"SKILLS={n}" in o, o)
        k, o = kos("codex", "exec", "--skip-git-repo-check", "-s", "read-only",
                   "Do not run commands. Reply exactly: 'SKILLS=<count of skills whose SKILL.md is inside this project .agents/skills folder>'",
                   cwd=pj, timeout=600)
        adim(f"Codex {n} skill'i görüyor", f"SKILLS={n}" in o, o[-300:])
        shutil.rmtree(pj / ".git", ignore_errors=True)
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--kaldir", "hepsi", "--evet")
    adim("--kaldir hepsi", k == 0 and not any((pj / ".agents" / "skills").iterdir()), o)
    k, o = kos(PY, "araclar/skill-ekle.py", str(pj), "--geri-al")
    adim("--geri-al: skiller geri geldi", k == 0 and len(list((pj / ".agents" / "skills").iterdir())) == n, o)
    shutil.rmtree(pj, ignore_errors=True)

    print("10) Global klasörler")
    adim("global skill klasörleri değişmedi", parmak_izi() == once_iz)
    adim("kütüphane değişmedi", kos("git", "status", "--porcelain")[1].strip() == kirli)

    hata = [a for a, ok in SONUC if not ok]
    print(f"\nDuman testi: {len(SONUC) - len(hata)}/{len(SONUC)} adım geçti" + (f" · BAŞARISIZ: {', '.join(hata)}" if hata else ""))
    sys.exit(1 if hata else 0)


if __name__ == "__main__":
    main()
