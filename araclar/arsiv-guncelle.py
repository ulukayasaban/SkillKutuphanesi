#!/usr/bin/env python3
"""Bakım: kaynak repolarda yeni commit var mı, yıldızlara yeni repo eklenmiş mi?

  python3 araclar/arsiv-guncelle.py            # sadece RAPOR (hiçbir şeyi değiştirmez)
  python3 araclar/arsiv-guncelle.py --uygula   # değişen repoları yeniden çeker, arşivi yerleştirir,
                                               # kataloğu üretir, doğrular ve git'e kayıt noktası atar
Projeler otomatik güncellenmez; her proje için ayrıca:  skill-ekle.py <proje> --guncelle
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, gh_api, json_oku  # noqa: E402


def calistir(*komut):
    print("$", " ".join(komut))
    subprocess.run(komut, cwd=KOK, check=True)


def main():
    uygula = "--uygula" in sys.argv
    skiller = json_oku(REGISTRY, {"skiller": []})["skiller"]
    mevcut = {}
    for s in skiller:
        mevcut.setdefault(s["repo"], s["commit"])
    degisen = []
    for repo in sorted({k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4")}):
        yeni = gh_api(f"repos/{repo}/commits/HEAD")["sha"]
        eski = mevcut.get(repo)
        if eski != yeni:
            degisen.append(repo)
            fark = gh_api(f"repos/{repo}/compare/{eski}...{yeni}") if eski else None
            dosyalar = [f["filename"] for f in (fark or {}).get("files", []) if "SKILL" in f["filename"] or "skills/" in f["filename"]]
            print(f"~ {repo}: {(eski or '-')[:7]} -> {yeni[:7]}  (skill ile ilgili değişen dosya: {len(dosyalar)})")
            for f in dosyalar[:10]:
                print(f"    {f}")
    if not degisen:
        print("Tüm kaynaklar güncel.")
    subprocess.run([sys.executable, str(KOK / "araclar" / "dogrula.py"), "--github"], cwd=KOK)
    if uygula and degisen:
        calistir(sys.executable, "araclar/gelistirici-bilgisi.py")
        calistir(sys.executable, "araclar/kaynak-cek.py")
        calistir(sys.executable, "araclar/arsiv-yerlestir.py")
        calistir(sys.executable, "araclar/kapsam-denetimi.py")
        calistir(sys.executable, "araclar/katalog-uret.py")
        calistir(sys.executable, "araclar/dogrula.py")
        import shutil
        shutil.rmtree(KOK / ".gecici", ignore_errors=True)  # geçici indirmeler silinir, yer kaplamaz
        calistir("git", "add", "-A")
        calistir("git", "commit", "-q", "-m", "Arşiv güncellemesi: " + ", ".join(degisen))
        print("Geri almak için:  git -C ~/Documents/SkillKutuphanesi revert HEAD")


if __name__ == "__main__":
    main()
