#!/usr/bin/env python3
"""Duman testi: kütüphanenin TÜM sürecinin çalıştığını uçtan uca, hızlıca dener. Kütüphaneyi ve global klasörleri değiştirmez.

  python3 araclar/duman-testi.py            # ~3-5 dk (ağ: GitHub kontrolü + kapsam denetimi)
  python3 araclar/duman-testi.py --araclar  # + gerçek Claude ve Codex'in kurulan skilleri gördüğünü sorar (birkaç dk daha)
  python3 araclar/duman-testi.py --kirli-ok # commit öncesi deneme: çalışma ağacı kirli olsa da 1. adım başarısız sayılmaz

Adımlar:
  1. Git: master'da, temiz, bekleyen/bozuk durum yok
  2. dogrula.py --github (registry, roller, profiller, örtüşme grupları, git'e girmeyen arşiv dosyası, yıldızlar;
     0 hata; bilinmeyen uyarı yok, emekli-rol uyarısı kabul)
  3. kapsam-denetimi.py (her SKILL.md açıklanmış mı; GitHub'dan bağımsız sayım)
  4. katalog-uret.py idempotent mi (yeniden üretince git'te fark çıkmamalı)
  5. test.py (skill-ekle güvenlik senaryoları)
  6. arsiv-guncelle.py rapor modu çalışıyor mu (hiçbir şey değiştirmeden)
  7. skill-ekle: --listele, --oner, tüm profillerin --opsiyonel --kuru'su (HATA/bağlam yok, --kuru dosya yazmaz)
  8. Gerçek kurulum yaşam döngüsü (geçici proje): --evet → --dogrula → --durum → --guncelle --kuru → --kaldir hepsi → --geri-al
  9. (--araclar) Claude ve Codex kurulan skilleri görüyor mu
 10. Kütüphane araçları genel skill klasörlerine yazmadı mı
 11. Rapor araçları (salt okuma, --ozet-json): tek JSON nesnesi, çıkış 0, kütüphaneye hiçbir şey yazmaz
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, OZET_ARACLARI, genel_fark, genel_izleri, ozet_json_gecerli  # noqa: E402

PY = sys.executable
SONUC = []


def kos(*args, cwd=KOK, timeout=900):
    r = subprocess.run(list(args), cwd=cwd, capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout + r.stderr


def adim(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {ayrinti.strip()[-500:]}"))


def main():
    araclar = "--araclar" in sys.argv
    once_iz = genel_izleri()
    print("1) Git")
    dal = kos("git", "branch", "--show-current")[1].strip()
    kirli = kos("git", "status", "--porcelain")[1].strip()
    adim(f"master dalında ({dal})", dal == "master")
    if "--kirli-ok" in sys.argv:
        print("     bilgi: --kirli-ok: çalışma ağacı kirliyse bu adım sayılmaz" + (f" ({len(kirli.splitlines())} değişiklik)" if kirli else ""))
    else:
        adim("çalışma ağacı temiz", not kirli,
             "\n".join(kirli.splitlines()[:8]) + "\n     önce commit (kullanıcı onayıyla), sonra duman testi")
    _, wt = kos("git", "worktree", "list")
    adim("ek worktree yok", len(wt.strip().splitlines()) == 1, wt)
    _, bek = kos("git", "branch", "--list", "guncelleme/*", "--format=%(refname:short)")
    print(f"     bilgi: onay bekleyen güncelleme dalı: {bek.split() or '-'}")

    print("2) Doğrulama")
    k, o = kos(PY, "araclar/dogrula.py", "--github")
    adim("dogrula.py --github: 0 hata", k == 0 and " 0 hata" in o, o)
    # dogrula.py'nin bugün bilinen tek uyarısı (rol emekli skil kullanıyor); sona erince yeniden sorulur
    KABUL_UYARI = re.compile(r"^UYARI: rol [\w-]+: '[^']+' emekli/kaynakta kaldırılmış; arşiv kopyası kullanılıyor")
    KABUL_SON = "2027-02-11"
    # Yama A (CLAUDE.md/AGENTS.md işaretçisi) onaylanıp uygulanana dek geçerli geçici kabul
    KABUL_YAMA_A = re.compile(r"^UYARI: CLAUDE\.md ilk satırı BASLA\.md'ye işaret etmiyor")
    KABUL_YAMA_A_SON = "2026-12-31"
    uyarilar = [s for s in o.splitlines() if s.startswith("UYARI:")]
    bugun_iso = date.today().isoformat()
    bilinmeyen = [s for s in uyarilar
                  if not ((KABUL_UYARI.match(s) and bugun_iso <= KABUL_SON)
                          or (KABUL_YAMA_A.match(s) and bugun_iso <= KABUL_YAMA_A_SON))]
    if len(bilinmeyen) != len(uyarilar):
        print(f"     bilgi: kabul edilen emekli-rol uyarısı: {len(uyarilar) - len(bilinmeyen)} (son {KABUL_SON})")
    adim("dogrula.py: bilinmeyen uyarı yok", not bilinmeyen, "\n".join(bilinmeyen))

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

    print("10) Genel skill klasörleri")
    fark = genel_fark(once_iz, genel_izleri())
    adim("kütüphane araçları ve bu test genel skill klasörlerine yazmadı", not fark,
         "değişen girdiler: " + ", ".join(fark[:6]) + " (testten mi dışarıdan mı? HyperFrames, skills aracı ya da Codex aynı anda yazmış olabilir: python3 araclar/genel-bekci.py)")
    adim("kütüphane değişmedi", kos("git", "status", "--porcelain")[1].strip() == kirli)

    print("11) Rapor araçları (salt okuma, --ozet-json)")
    AG_YOK = {"program-denetim": ["--oncesi", "hyperframes", "--cevrimdisi"],  # ağa çıkmasın; çıkış 0 ve geçerli JSON ister
              "git-durum": ["--gh-yok"]}
    for ad, ek in OZET_ARACLARI + [("aylik-ozet", ["--hizli"])]:
        arg = AG_YOK.get(ad, ek)
        k, o = kos(PY, f"araclar/{ad}.py", *arg, "--ozet-json")
        obj, neden = ozet_json_gecerli(o) if k == 0 else (None, f"çıkış kodu {k}")
        adim(f"{ad} --ozet-json: tek JSON nesnesi, çıkış 0", obj is not None, neden + " " + o[-200:])
    k, o = kos(PY, "araclar/aylik-ozet.py", "--hizli")
    adim("aylik-ozet --hizli (metin): çıkış 0, Traceback yok, en çok 15 satır", k == 0 and "Traceback" not in o and len(o.strip().splitlines()) <= 15,
         f"{len(o.strip().splitlines())} satır\n" + o[-300:])
    adim("rapor araçları kütüphane dosyalarına hiçbir şey yazmadı", kos("git", "status", "--porcelain")[1].strip() == kirli)

    hata = [a for a, ok in SONUC if not ok]
    print(f"\nDuman testi: {len(SONUC) - len(hata)}/{len(SONUC)} adım geçti" + (f" · BAŞARISIZ: {', '.join(hata)}" if hata else ""))
    sys.exit(1 if hata else 0)


if __name__ == "__main__":
    main()
