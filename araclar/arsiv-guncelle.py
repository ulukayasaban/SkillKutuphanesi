#!/usr/bin/env python3
"""Bakım: kaynak repolarda yeni commit var mı, yıldızlara yeni repo eklenmiş mi?

  python3 araclar/arsiv-guncelle.py            # sadece RAPOR (hiçbir şeyi değiştirmez)
  python3 araclar/arsiv-guncelle.py --uygula   # değişiklik varsa: geliştirici bilgisi -> indir -> yerleştir ->
                                               # kapsam denetimi -> katalog -> doğrula -> git kayıt noktası -> geçicileri sil
Güvenceler:
  * --uygula, kütüphane klasöründe kaydedilmemiş değişiklik varsa başlamaz (elle düzenlemelerin karışmasın).
  * Herhangi bir adım hata verirse durur; git kaydı atılmaz; `git checkout -- . && git clean -fd arsiv` ile önceki hâl.
  * Geçmişi yeniden yazılmış (force-push) ya da silinmiş repo çökme yerine raporlanır.
Projeler otomatik güncellenmez; her proje için ayrıca:  skill-ekle.py <proje> --durum / --guncelle
"""
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, GhBulunamadi, gh_api, json_oku  # noqa: E402


def calistir(*komut):
    print("$", " ".join(komut))
    subprocess.run(komut, cwd=KOK, check=True)


def git(*args):
    return subprocess.run(["git", *args], cwd=KOK, capture_output=True, text=True)


def main():
    uygula = "--uygula" in sys.argv
    skiller = json_oku(REGISTRY, {"skiller": []})["skiller"]
    mevcut = {}
    for s in skiller:
        mevcut.setdefault(s["repo"], s["commit"])
    degisen, sorunlu = [], []
    for repo in sorted({k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4")}):
        try:
            yeni = gh_api(f"repos/{repo}/commits/HEAD")["sha"]
        except GhBulunamadi as e:
            sorunlu.append(repo)
            print(f"! {repo}: erişilemiyor (silinmiş/private?). Arşiv kopyası korunuyor. {e}")
            continue
        eski = mevcut.get(repo)
        if eski == yeni:
            continue
        degisen.append(repo)
        dosyalar, not_ = [], ""
        if eski:
            try:
                fark = gh_api(f"repos/{repo}/compare/{eski}...{yeni}")
                dosyalar = [f["filename"] for f in fark.get("files", [])
                            if "SKILL" in f["filename"].upper() or "skills/" in f["filename"]]
            except GhBulunamadi:
                not_ = " (eski commit bulunamadı: geçmiş yeniden yazılmış olabilir; değişiklikleri dikkatle incele)"
        print(f"~ {repo}: {(eski or '-')[:7]} -> {yeni[:7]}  skill dosyası değişikliği: {len(dosyalar)}{not_}")
        for f in dosyalar[:10]:
            print(f"    {f}")
    if not degisen:
        print("Tüm kaynaklar güncel.")
    subprocess.run([sys.executable, str(KOK / "araclar" / "dogrula.py"), "--github"], cwd=KOK)
    if not (uygula and degisen):
        return 1 if sorunlu else 0
    if sorunlu:
        sys.exit(f"DURDU: erişilemeyen kaynaklar var ({', '.join(sorunlu)}). kaynaklar.json'da bu kayıtları kaldır "
                 "ya da 'tip': 'KAYIP' yap; arşivdeki kopyaları korunur.")
    if git("status", "--porcelain").stdout.strip():
        sys.exit("DURDU: kütüphanede kaydedilmemiş değişiklik var. Önce `git -C ~/Documents/SkillKutuphanesi status` "
                 "ile bak, kaydet (git commit) ya da geri al; sonra tekrar çalıştır.")
    calistir(sys.executable, "araclar/gelistirici-bilgisi.py")
    calistir(sys.executable, "araclar/kaynak-cek.py")
    calistir(sys.executable, "araclar/arsiv-yerlestir.py")
    calistir(sys.executable, "araclar/kapsam-denetimi.py")
    calistir(sys.executable, "araclar/katalog-uret.py")
    calistir(sys.executable, "araclar/dogrula.py")
    reg = json_oku(REGISTRY)["skiller"]
    eskiyen = [s["id"] for s in reg if s.get("inceleme") == "yeniden-incelenecek"]
    emekli = [s["id"] for s in reg if s.get("kaynak_durumu") == "kaynakta-kaldirildi"]
    print(f"Yeniden incelenecek (içeriği değişen) skill: {len(eskiyen)}" + (f" -> {', '.join(eskiyen[:30])}" if eskiyen else ""))
    print(f"Kaynakta kaldırılıp arşivde korunan skill: {len(emekli)}")
    calistir("git", "add", "-A")
    calistir("git", "add", "-f", "arsiv")  # skillerin kendi .gitignore dosyaları arşiv dosyalarını gizlemesin
    if git("diff", "--cached", "--quiet").returncode == 0:
        print("Yeni commit'ler skill içeriğini değiştirmemiş; kayıt atılmadı.")
    else:
        calistir("git", "commit", "-q", "-m", "Arşiv güncellemesi: " + ", ".join(degisen))
        print("Geri almak için:  git -C ~/Documents/SkillKutuphanesi revert HEAD")
    shutil.rmtree(KOK / ".gecici", ignore_errors=True)  # sadece her şey başarılıysa silinir
    return 0


if __name__ == "__main__":
    sys.exit(main())
