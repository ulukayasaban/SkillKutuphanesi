#!/usr/bin/env python3
"""Bakım: kaynak repolarda yeni commit var mı, yıldızlara yeni repo eklenmiş mi? Güncelleme git ile takip edilir.

  python3 araclar/arsiv-guncelle.py                      # sadece RAPOR (hiçbir şeyi değiştirmez)
  python3 araclar/arsiv-guncelle.py --uygula --dal       # ÖNERİLEN (aylık): güncellemeyi 'guncelleme/YYYY-AA' dalında yapar,
                                                         # notlar/guncelleme-gecmisi.md'ye kayıt düşer, dalda commit atar,
                                                         # master'a geri döner. master DEĞİŞMEZ.
  python3 araclar/arsiv-guncelle.py --birlestir <dal>    # kullanıcı onayından sonra: dalı master'a birleştirir (--no-ff),
                                                         # doğrulama + kapsam denetimi + testleri çalıştırır, dalı siler
  python3 araclar/arsiv-guncelle.py --uygula             # (eski yol) güncellemeyi doğrudan bulunulan dalda yapar

Sıra (--uygula): geliştirici bilgisi -> indir -> yerleştir -> kapsam denetimi -> katalog -> doğrula -> geçmiş kaydı -> commit
Güvenceler:
  * --uygula, kütüphane klasöründe kaydedilmemiş değişiklik varsa başlamaz (elle düzenlemelerin karışmasın).
  * --dal modunda bir adım hata verirse dal geri alınır ve silinir, master'a dönülür; master hiç değişmez.
  * Geçmişi yeniden yazılmış (force-push) ya da silinmiş repo çökme yerine raporlanır.
Projeler otomatik güncellenmez; her proje için ayrıca:  skill-ekle.py <proje> --durum / --guncelle
"""
import shutil
import json
import os
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, GhBulunamadi, gh_api, json_oku  # noqa: E402

GECMIS = KOK / "notlar" / "guncelleme-gecmisi.md"
ANA_DAL = "master"


def calistir(*komut):
    print("$", " ".join(komut))
    subprocess.run(komut, cwd=KOK, check=True)


def git(*args):
    return subprocess.run(["git", *args], cwd=KOK, capture_output=True, text=True)


def rapor():
    """Kaynakları kontrol eder. (degisen, sorunlu, ayrinti) döndürür."""
    skiller = json_oku(REGISTRY, {"skiller": []})["skiller"]
    mevcut = {}
    for s in skiller:  # kaynakta kaldırılmış kayıt eski commit'te kalır; her ay sahte "değişti" sinyali vermesin
        if not s.get("kaynak_durumu"):
            mevcut.setdefault(s["repo"], s["commit"])
    for s in skiller:
        mevcut.setdefault(s["repo"], s["commit"])  # repodaki tüm kayıtlar kaldırılmışsa eski commit'e düş
    degisen, sorunlu, ayrinti = [], [], {}
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
        ayrinti[repo] = {"eski": eski, "yeni": yeni, "dosya": len(dosyalar), "not": not_}
        print(f"~ {repo}: {(eski or '-')[:7]} -> {yeni[:7]}  skill dosyası değişikliği: {len(dosyalar)}{not_}")
        for f in dosyalar[:10]:
            print(f"    {f}")
    if not degisen:
        print("Tüm kaynaklar güncel.")
    subprocess.run([sys.executable, str(KOK / "araclar" / "dogrula.py"), "--github"], cwd=KOK)
    return degisen, sorunlu, ayrinti


def gecmis_yaz(dal, ayrinti, onceki):
    """notlar/guncelleme-gecmisi.md'ye bu güncellemenin kaydını ekler (en yeni üstte)."""
    reg = json_oku(REGISTRY)["skiller"]
    ok = {(s["repo"], s["kaynak_yol"]): s for s in onceki}
    yk = {(s["repo"], s["kaynak_yol"]): s for s in reg}
    icerik = sorted(yk[k]["id"] for k in ok.keys() & yk.keys() if ok[k]["klasor_hash"] != yk[k]["klasor_hash"])
    eklenen = sorted(yk[k]["id"] for k in yk.keys() - ok.keys())
    kalkan = sorted(ok[k]["id"] for k in ok.keys() - yk.keys())
    yeni_emekli = sorted(s["id"] for s in reg if s.get("kaynak_durumu") == "kaynakta-kaldirildi"
                         and ok.get((s["repo"], s["kaynak_yol"]), {}).get("kaynak_durumu") != "kaynakta-kaldirildi")
    eskiyen = sorted(s["id"] for s in reg if s.get("inceleme") == "yeniden-incelenecek")
    satir = [f"## {date.today().isoformat()} — `{dal}`", "",
             f"Durum: **master'a birleştirilmeyi bekliyor** (onay sonrası: `python3 araclar/arsiv-guncelle.py --birlestir {dal}`)", "",
             "| Kaynak | Eski | Yeni | Değişen skill dosyası |", "|---|---|---|---|"]
    satir += [f"| {r} | `{(a['eski'] or '-')[:7]}` | `{a['yeni'][:7]}` | {a['dosya']}{a['not']} |" for r, a in ayrinti.items()]
    bekleyen = [f"{r}: {y}" for r, d in (json_oku(REGISTRY).get("denetim") or {}).items()
                for y, k in d.get("skill_md", {}).items() if k == "dahil-disi"]
    satir += ["",
              f"- **Karar bekleyen yeni skiller** ({len(bekleyen)}; arşive alınmadı): "
              + (", ".join(f"`{x}`" for x in bekleyen[:15]) + (f" … (+{len(bekleyen) - 15})" if len(bekleyen) > 15 else "") or "-")
              + " → almak için kaynaklar.json `dahil`, almamak için `haric`",
              f"- İçeriği değişen skill ({len(icerik)}): {', '.join(f'`{x}`' for x in icerik) or '-'}",
              f"- Yeni eklenen skill ({len(eklenen)}): {', '.join(f'`{x}`' for x in eklenen) or '-'}",
              f"- Kaynakta kaldırılıp arşivde korunan (bu güncellemede) ({len(yeni_emekli)}): {', '.join(f'`{x}`' for x in yeni_emekli) or '-'}",
              f"- Registry'den düşen ({len(kalkan)}): {', '.join(f'`{x}`' for x in kalkan) or '-'}",
              f"- **Yeniden incelenecek** ({len(eskiyen)}): {', '.join(f'`{x}`' for x in eskiyen) or '-'} "
              "(rehber/07-kategori-inceleme.md)", ""]
    bas = "# Güncelleme Geçmişi\n\n> `araclar/arsiv-guncelle.py --uygula --dal` her güncellemede buraya kayıt ekler (en yeni üstte). " \
          "Ayrıntı: `git log --oneline -- registry.json`.\n\n"
    eski_metin = GECMIS.read_text(encoding="utf-8") if GECMIS.exists() else bas
    if not eski_metin.startswith("# Güncelleme Geçmişi"):
        eski_metin = bas + eski_metin
    govde = eski_metin[len(bas):] if eski_metin.startswith(bas) else eski_metin.split("\n\n", 2)[-1]
    GECMIS.write_text(bas + "\n".join(satir) + "\n" + govde, encoding="utf-8")
    return icerik, eskiyen


KILIT = KOK / ".guncelleme-kilidi"  # .gitignore'da; skill-ekle.py bu dosyayı görünce kurulum/güncellemeyi bekletir


def api_hakki_kontrol(gerekli=1500):
    """Güncellemeden önce GitHub API hakkı yeterli mi? Yetmezse HİÇBİR ŞEY başlamaz (yarım ay-ortası çökme olmasın)."""
    r = subprocess.run(["gh", "api", "rate_limit", "--jq", ".resources.core.remaining"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip().isdigit():
        sys.exit("DURDU: GitHub API'ye ulaşılamıyor ya da oturum yok (`gh auth status`). Hiçbir şey değişmedi.")
    kalan = int(r.stdout.strip())
    if kalan < gerekli:
        sys.exit(f"DURDU: GitHub API hakkı yetersiz (kalan {kalan}, gereken ~{gerekli}). Saat başı yenilenir; sonra tekrar çalıştır. "
                 "Hiçbir şey değişmedi.")
    print(f"GitHub API hakkı: {kalan}")


def uygula(degisen, ayrinti, dal_modu):
    if git("status", "--porcelain").stdout.strip():
        sys.exit("DURDU: kütüphanede kaydedilmemiş değişiklik var. Önce `git -C ~/Documents/SkillKutuphanesi status` "
                 "ile bak, kaydet (git commit) ya da geri al; sonra tekrar çalıştır.")
    api_hakki_kontrol()
    onceki = json_oku(REGISTRY)["skiller"]
    dal = git("branch", "--show-current").stdout.strip()
    if KILIT.exists():
        try:
            k = json.loads(KILIT.read_text())
            canli = Path(f"/proc/{k['pid']}").exists() or subprocess.run(["kill", "-0", str(k["pid"])], capture_output=True).returncode == 0
        except Exception:  # noqa: BLE001
            canli = False
        if canli:
            sys.exit(f"DURDU: başka bir güncelleme sürüyor (pid {k['pid']}, {k.get('baslangic')}).")
    KILIT.write_text(json.dumps({"pid": os.getpid(), "baslangic": datetime.now().isoformat(timespec="seconds")}))
    try:
        return _uygula(degisen, ayrinti, dal_modu, onceki, dal)
    finally:
        KILIT.unlink(missing_ok=True)


def _uygula(degisen, ayrinti, dal_modu, onceki, dal):
    if dal_modu:
        if dal != ANA_DAL:
            sys.exit(f"DURDU: --dal modu '{ANA_DAL}' dalından başlatılmalı (şu an '{dal}').")
        dal = f"guncelleme/{date.today():%Y-%m}"
        n = 2
        while git("rev-parse", "--verify", "--quiet", f"refs/heads/{dal}").returncode == 0:
            dal = f"guncelleme/{date.today():%Y-%m}-{n}"
            n += 1
        calistir("git", "switch", "-q", "-c", dal)
    try:
        calistir(sys.executable, "araclar/gelistirici-bilgisi.py")
        # GitHub Trending: ağ/sayfa sorunu güncellemeyi durdurmaz (önceki trend geçmişi kullanılır)
        if subprocess.run([sys.executable, "araclar/github-trend.py", "--aday"], cwd=KOK).returncode:
            print("UYARI: GitHub trend taraması yapılamadı; önceki trend.json ile devam")
        # Konu takibi (e-ticaret, mobil…): yeni aday skill repoları raporlanır, eklenmez
        if subprocess.run([sys.executable, "araclar/konu-takip.py"], cwd=KOK).returncode:
            print("UYARI: konu takibi taraması yapılamadı; önceki konu-takip.json ile devam")
        calistir(sys.executable, "araclar/kaynak-cek.py")
        calistir(sys.executable, "araclar/arsiv-yerlestir.py")
        calistir(sys.executable, "araclar/kapsam-denetimi.py")
        calistir(sys.executable, "araclar/katalog-uret.py")
        # Türkçe skill rehberi (çevirisi eksik/eskimiş skiller İngilizce görünür; çeviri ücretli olduğu için elle: ceviri-tr.py)
        calistir(sys.executable, "araclar/skill-readme.py")
        # Çalıştırma testi (agent'sız): yeni gelen bozuk skill güncellemeyi durdurmaz, TEST_RAPORU.md'de görünür
        if subprocess.run([sys.executable, "araclar/skill-calistir.py"], cwd=KOK).returncode:
            print("UYARI: çalıştırma testinde HATA veren skill var -> TEST_RAPORU.md (yama: rehber/03)")
        calistir(sys.executable, "araclar/dogrula.py")
        icerik, eskiyen = gecmis_yaz(dal, ayrinti, onceki)
        print(f"İçeriği değişen skill: {len(icerik)} · yeniden incelenecek: {len(eskiyen)}"
              + (f" -> {', '.join(eskiyen[:30])}" if eskiyen else ""))
        calistir("git", "add", "-A")
        calistir("git", "add", "-f", "arsiv")  # skillerin kendi .gitignore dosyaları arşiv dosyalarını gizlemesin
        calistir("git", "commit", "-q", "-m", f"Arşiv güncellemesi ({date.today().isoformat()}): " + ", ".join(degisen))
    except (subprocess.CalledProcessError, SystemExit, Exception) as e:  # noqa: BLE001
        print(f"HATA: güncelleme yarıda kaldı: {e}")
        if dal_modu:
            git("reset", "-q", "--hard")
            git("clean", "-fdq", "arsiv", "notlar")
            git("switch", "-q", ANA_DAL)
            git("branch", "-D", dal)
            print(f"'{dal}' dalı geri alındı ve silindi; master değişmedi.")
        sys.exit(1)
    shutil.rmtree(KOK / ".gecici", ignore_errors=True)
    if dal_modu:
        calistir("git", "switch", "-q", ANA_DAL)
        ozet = git("diff", "--stat", f"{ANA_DAL}...{dal}").stdout.strip().splitlines()
        print(f"\nGüncelleme '{dal}' dalında hazır; master değişmedi. Özet: {ozet[-1] if ozet else '-'}")
        print(f"İncele:   git -C ~/Documents/SkillKutuphanesi log {ANA_DAL}..{dal}  ·  notlar/guncelleme-gecmisi.md (dalda)")
        print(f"Onayla:   python3 araclar/arsiv-guncelle.py --birlestir {dal}")
        print(f"Reddet:   git -C ~/Documents/SkillKutuphanesi branch -D {dal}")
    else:
        print("Geri almak için:  git -C ~/Documents/SkillKutuphanesi revert HEAD")
    return 0


def birlestir(dal):
    if git("rev-parse", "--verify", "--quiet", f"refs/heads/{dal}").returncode != 0:
        sys.exit(f"Dal yok: {dal}. Bekleyen güncelleme dalları: "
                 + (", ".join(git("branch", "--list", "guncelleme/*", "--format=%(refname:short)").stdout.split()) or "-"))
    if git("status", "--porcelain").stdout.strip():
        sys.exit("DURDU: kütüphanede kaydedilmemiş değişiklik var; önce kaydet ya da geri al.")
    if git("branch", "--show-current").stdout.strip() != ANA_DAL:
        calistir("git", "switch", "-q", ANA_DAL)
    once = git("rev-parse", "HEAD").stdout.strip()
    calistir("git", "merge", "--no-ff", "-q", "-m", f"Birleştir: {dal} (kullanıcı onayıyla)", dal)
    try:
        calistir(sys.executable, "araclar/dogrula.py")
        calistir(sys.executable, "araclar/kapsam-denetimi.py")
        calistir(sys.executable, "araclar/test.py")
    except subprocess.CalledProcessError:
        git("reset", "-q", "--hard", once)
        sys.exit(f"HATA: birleştirme sonrası kontroller geçmedi; master eski hâline ({once[:7]}) döndürüldü, dal duruyor.")
    if GECMIS.exists():
        t = GECMIS.read_text(encoding="utf-8")
        eski = f"Durum: **master'a birleştirilmeyi bekliyor** (onay sonrası: `python3 araclar/arsiv-guncelle.py --birlestir {dal}`)"
        if eski in t:
            GECMIS.write_text(t.replace(eski, f"Durum: **master'a birleştirildi** ({datetime.now():%Y-%m-%d %H:%M})"), encoding="utf-8")
            calistir("git", "commit", "-q", "-am", f"Güncelleme geçmişi: {dal} birleştirildi")
    calistir("git", "branch", "-d", dal)
    print(f"'{dal}' master'a birleştirildi ve dal silindi. Projeler için: skill-ekle.py <proje> --durum / --guncelle --kuru")
    return 0


def main():
    if "--birlestir" in sys.argv:
        i = sys.argv.index("--birlestir")
        if i + 1 >= len(sys.argv):
            sys.exit("Kullanım: --birlestir guncelleme/YYYY-AA")
        return birlestir(sys.argv[i + 1])
    degisen, sorunlu, ayrinti = rapor()
    bekleyen = git("branch", "--list", "guncelleme/*", "--format=%(refname:short)").stdout.split()
    if bekleyen:
        print(f"Onay bekleyen güncelleme dalı: {', '.join(bekleyen)} (--birlestir <dal> ya da git branch -D <dal>)")
    if "--uygula" not in sys.argv or not degisen:
        return 1 if sorunlu else 0
    if sorunlu:
        sys.exit(f"DURDU: erişilemeyen kaynaklar var ({', '.join(sorunlu)}). kaynaklar.json'da bu kayıtların 'tip' alanını "
                 "'KAYIP' yap (arşivdeki kopyaları korunur). Kaydı SİLME: güvenlik kilidi skillleri kayıp sayıp güncellemeyi durdurur; "
                 "bilerek çıkarmak istiyorsan skilleri kaynaklar.json -> arsivden_cikarilanlar'a da yaz.")
    if bekleyen and "--dal" in sys.argv:
        sys.exit(f"DURDU: önce bekleyen güncelleme dalını birleştir ya da sil: {', '.join(bekleyen)}")
    return uygula(degisen, ayrinti, "--dal" in sys.argv)


if __name__ == "__main__":
    sys.exit(main())
