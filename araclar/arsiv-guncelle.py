#!/usr/bin/env python3
"""Bakım: kaynak repolarda yeni commit var mı, yıldızlara yeni repo eklenmiş mi? Güncelleme git ile takip edilir.

  python3 araclar/arsiv-guncelle.py                      # sadece RAPOR (hiçbir şeyi değiştirmez)
  python3 araclar/arsiv-guncelle.py --uygula --dal       # ÖNERİLEN (aylık): güncellemeyi 'guncelleme/YYYY-AA' dalında yapar,
                                                         # notlar/guncelleme-gecmisi.md'ye kayıt düşer, dalda commit atar,
                                                         # master'a geri döner. master DEĞİŞMEZ.
  python3 araclar/arsiv-guncelle.py --birlestir <dal>    # kullanıcı onayından sonra: dalı master'a birleştirir (--no-ff),
                                                         # doğrulama + kapsam denetimi + testleri çalıştırır, dalı siler
  python3 araclar/arsiv-guncelle.py --uygula             # (eski yol) güncellemeyi doğrudan bulunulan dalda yapar
  python3 araclar/arsiv-guncelle.py --aylik --kuru       # aylık zincirin yan etkisiz PLANI: ön kontrol + rapor + özet (dal, commit, damga YOK)
  python3 araclar/arsiv-guncelle.py --siki               # rapor modu; GitHub'a ulaşılamadıysa ya da kaynak kontrol edilemediyse çıkış 2
  python3 araclar/arsiv-guncelle.py --help               # bu metin (hiçbir şey çalıştırmaz)

Çıkış kodu: 0 = sorun yok · 1 = erişilemeyen kaynak (rapor modu) ya da hata
            2 = YALNIZ --siki ile: GitHub'a ulaşılamadı ya da bazı kaynaklar kontrol edilemedi (yalnız yerel kontroller yapıldı)
Not: --aylik'in yazma adımları (dal açma, takip, damga) henüz yok; şimdilik yalnız --aylik --kuru çalışır.

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
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, GhBulunamadi, gh_api, json_oku, repo_guncel  # noqa: E402

GECMIS = KOK / "notlar" / "guncelleme-gecmisi.md"
ANA_DAL = "master"
DAMGA = KOK / "notlar" / "son-aylik-calisma.json"  # yerel, git'e girmez (.gitignore); bu aşamada yalnız OKUNUR
ESIK_DAL_GUN = 45      # bekleyen dal bu günden eskiyse uyarı
ESIK_KACAN_GUN = 35    # son aylık çalışma bu günden eskiyse "kaçan ay"
IZINLI_RAPOR_YOLLARI = ("notlar/proje-durumu.md", "notlar/program-denetimi.md")
URETILEN_NOTLAR = ("notlar/proje-kullanimi.md", "notlar/proje-durumu.md", "notlar/program-denetimi.md", "notlar/yol-denetimi.md")
BEKLEYEN_DESENLER = ("guncelleme/*", "takip/*")
# her rapor() başında sıfırlanan durum
ATLANAN = []
ADI_DEGISEN = {}
ULASILAMAYAN = []
CEVRIMDISI = False


def calistir(*komut):
    print("$", " ".join(komut))
    subprocess.run(komut, cwd=KOK, check=True)


def git(*args):
    return subprocess.run(["git", *args], cwd=KOK, capture_output=True, text=True)


def kirli_dosyalar():
    """Kaydedilmemiş değişiklikler: [(XY, yol)]. Hiçbir yol ayıklanmaz (.gitignore'dakiler zaten çıkmaz)."""
    parca = git("status", "--porcelain", "-z").stdout.split("\0")
    sonuc, i = [], 0
    while i < len(parca):
        p = parca[i]
        i += 1
        if len(p) < 4:
            continue
        xy, yol = p[:2], p[3:]
        if "R" in xy or "C" in xy:
            i += 1  # bir sonraki NUL parçası eski yoldur
        sonuc.append((xy, yol))
    return sonuc


def kirli_ozet(kirli, sinir=10):
    yollar = [y for _, y in kirli]
    return ", ".join(yollar[:sinir]) + (f" … +{len(yollar) - sinir}" if len(yollar) > sinir else "")


def yoksayiliyor_mu(yol):
    """git check-ignore: 0 (yoksayılıyor) ve 128 (git deposu değil) True; 1 False."""
    return git("check-ignore", "-q", str(yol)).returncode in (0, 128)


def bekleyen_dallar():
    """Onay bekleyen dallar (guncelleme/* ve takip/*): [{'dal','gun','birlesmis'}]."""
    adlar = git("branch", "--list", *BEKLEYEN_DESENLER, "--format=%(refname:short)").stdout.split()
    sonuc = []
    for dal in adlar:
        ct = git("log", "-1", "--format=%ct", dal).stdout.strip()
        gun = (date.today() - date.fromtimestamp(int(ct))).days if ct.isdigit() else 0
        birlesmis = git("merge-base", "--is-ancestor", dal, ANA_DAL).returncode == 0
        sonuc.append({"dal": dal, "gun": gun, "birlesmis": birlesmis})
    return sonuc


def gh_hazir():
    """(ok, kalan, neden): gh kurulu ve oturum açık mı? Ağ hatasında beklemeden döner."""
    try:
        r = subprocess.run(["gh", "api", "rate_limit", "--jq", ".resources.core.remaining"],
                           capture_output=True, text=True, timeout=30)
    except FileNotFoundError:
        return False, None, "gh kurulu değil"
    except subprocess.TimeoutExpired:
        return False, None, "zaman aşımı"
    if r.returncode != 0 or not r.stdout.strip().isdigit():
        return False, None, "gh oturumu yok ya da ağ yok"
    return True, int(r.stdout.strip()), ""


def kaynak_cek_atla_var():
    """kaynak-cek.py --atla destekliyor mu? (--help çıktısına bakar; argparse olduğu için güvenli)"""
    try:
        r = subprocess.run([sys.executable, str(KOK / "araclar" / "kaynak-cek.py"), "--help"],
                           cwd=KOK, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return "--atla" in r.stdout


def damga_oku():
    """notlar/son-aylik-calisma.json (yok ya da bozuksa {})."""
    try:
        d = json.loads(DAMGA.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def rapor():
    """Kaynakları kontrol eder. (degisen, sorunlu, ayrinti) döndürür.
    GitHub'a ulaşılamıyorsa kaynak karşılaştırması atlanır (CEVRIMDISI); geçici ağ hatası alan kaynaklar ULASILAMAYAN'a girer."""
    global ADI_DEGISEN, ULASILAMAYAN, CEVRIMDISI
    ADI_DEGISEN, ULASILAMAYAN, CEVRIMDISI = {}, [], False
    ok, _kalan, neden = gh_hazir()
    if not ok:
        print(f"UYARI: GitHub'a ulaşılamıyor ({neden}). Kaynak karşılaştırması ATLANDI; yalnız yerel kontroller yapıldı.")
        CEVRIMDISI = True
        subprocess.run([sys.executable, str(KOK / "araclar" / "dogrula.py")], cwd=KOK)
        return [], [], {}
    skiller = json_oku(REGISTRY, {"skiller": []})["skiller"]
    mevcut = {}
    for s in skiller:  # kaynakta kaldırılmış kayıt eski commit'te kalır; her ay sahte "değişti" sinyali vermesin
        if not s.get("kaynak_durumu"):
            mevcut.setdefault(s["repo"], s["commit"])
    for s in skiller:
        mevcut.setdefault(s["repo"], s["commit"])  # repodaki tüm kayıtlar kaldırılmışsa eski commit'e düş
    degisen, sorunlu, ayrinti = [], [], {}
    repolar = sorted({k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4")})
    art_arda = 0
    for i, repo in enumerate(repolar):
        try:
            yanit = gh_api(f"repos/{repo}/commits/HEAD")
            yeni = yanit["sha"]
        except GhBulunamadi:
            art_arda = 0
            sorunlu.append(repo)
            print(f"! {repo}: erişilemiyor (silinmiş, private ya da adı değişmiş olabilir). Arşiv kopyası korunuyor. "
                  "İpucu: B adımındaki github-skill-listesi.py \"AD DEĞİŞMİŞ\" satırına bak.")
            continue
        except Exception as e:  # noqa: BLE001  geçici ağ / hız sınırı
            art_arda += 1
            ULASILAMAYAN.append(repo)
            print(f"! {repo}: şimdilik kontrol edilemedi ({str(e).strip().splitlines()[-1][:120] if str(e).strip() else type(e).__name__})")
            if art_arda >= 3:
                kalan = repolar[i + 1:]
                ULASILAMAYAN.extend(kalan)
                print("UYARI: art arda 3 kaynak kontrol edilemedi; kalanlar atlandı (ağ/hız sınırı).")
                break
            continue
        art_arda = 0
        try:  # adı değişmiş repo: commit yanıtındaki html_url yeni adı verir (ek çağrı yok)
            m = re.search(r"github\.com/([^/]+/[^/]+)/commit/", str(yanit.get("html_url", "")))
            if m:
                bilinen = {repo.lower(), str(repo_guncel(repo)).lower()}
                if m.group(1).lower() not in bilinen:
                    ADI_DEGISEN[repo] = m.group(1)
                    print(f"~ AD DEĞİŞMİŞ: {repo} -> {m.group(1)} (yeni kaynak DEĞİL; kaynaklar.json'da 'repo'yu yeni adla değiştir, "
                          "eski adı \"eski_adlar\"a yaz; rehber/09)")
        except Exception:  # noqa: BLE001
            pass
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
            except Exception:  # noqa: BLE001
                not_ = " (karşılaştırma şimdilik yapılamadı)"
        ayrinti[repo] = {"eski": eski, "yeni": yeni, "dosya": len(dosyalar), "not": not_}
        print(f"~ {repo}: {(eski or '-')[:7]} -> {yeni[:7]}  skill dosyası değişikliği: {len(dosyalar)}{not_}")
        for f in dosyalar[:10]:
            print(f"    {f}")
    if ULASILAMAYAN:
        print(f"Kontrol edilemeyen kaynak: {len(ULASILAMAYAN)} (geçici); sonra tekrar çalıştır.")
    if not degisen:
        if not ULASILAMAYAN:
            print("Tüm kaynaklar güncel.")
    else:
        etkilenen_projeler(degisen)
    subprocess.run([sys.executable, str(KOK / "araclar" / "dogrula.py"), "--github"], cwd=KOK)
    return degisen, sorunlu, ayrinti


def etkilenen_projeler(repolar):
    """Değişen kaynaklardan skill kullanan projeleri yazar (proje bilgisinin tek yeri: araclar/proje-kullanimi.py)."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("projekullanimi", Path(__file__).parent / "proje-kullanimi.py")
        pk = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pk)
        kullanan = pk.kullanan_projeler(repolar=repolar)
    except Exception as e:  # noqa: BLE001
        print(f"(etkilenen projeler listelenemedi: {e})")
        return {}
    if kullanan:
        print("Bu kaynaklardan skill kullanan projeler (güncellemeden sonra: skill-ekle.py <proje> --durum / --guncelle --kuru):")
        for proje, adlar in sorted(kullanan.items()):
            print(f"  {proje}: {', '.join(adlar)}")
    else:
        print("Değişen kaynaklardan skill kullanan kurulu proje yok.")
    return kullanan


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
    kirli = kirli_dosyalar()
    if kirli:
        sys.exit(f"DURDU: kütüphanede kaydedilmemiş değişiklik var ({len(kirli)} dosya): {kirli_ozet(kirli)}. "
                 "Önce kaydet (git commit) ya da geri al. Aylık plan için: python3 araclar/arsiv-guncelle.py --aylik --kuru "
                 "(kirli ağaçta salt okuma plan üretir).")
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
        # Popüler skill repoları (REST araması; yıldız listesi/trending okunamadığında da çalışır): rapor, ekleme yok
        if subprocess.run([sys.executable, "araclar/populer-tarama.py"], cwd=KOK).returncode:
            print("UYARI: popüler skill taraması yapılamadı; notlar/populer-skiller.md eski kaldı")
        # Konu takibi (e-ticaret, mobil…): yeni aday skill repoları raporlanır, eklenmez
        if subprocess.run([sys.executable, "araclar/konu-takip.py"], cwd=KOK).returncode:
            print("UYARI: konu takibi taraması yapılamadı; önceki konu-takip.json ile devam")
        calistir(sys.executable, "araclar/kaynak-cek.py")
        calistir(sys.executable, "araclar/arsiv-yerlestir.py")
        # Sabit yol taraması (salt okuma, notlar/yol-denetimi.md): hata güncellemeyi durdurmaz
        if subprocess.run([sys.executable, "araclar/yol-tara.py"], cwd=KOK).returncode:
            print("UYARI: yol taraması yapılamadı; notlar/yol-denetimi.md eski kaldı")
        # Programlar (skill olmayan yapılar) denetimi: hata güncellemeyi durdurmaz
        if subprocess.run([sys.executable, "araclar/program-denetim.py"], cwd=KOK).returncode:
            print("UYARI: program denetimi yapılamadı; notlar/program-denetimi.md eski kaldı")
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
        sys.exit(f"Dal yok: {dal}. Bekleyen güncelleme dalları (guncelleme/* ve takip/*): "
                 + (", ".join(git("branch", "--list", *BEKLEYEN_DESENLER, "--format=%(refname:short)").stdout.split()) or "-"))
    kirli = kirli_dosyalar()
    if kirli:
        sys.exit(f"DURDU: kütüphanede kaydedilmemiş değişiklik var ({len(kirli)} dosya): {kirli_ozet(kirli)}; "
                 "önce kaydet ya da geri al.")
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


def _dal_adi_onizle(onek):
    """Açılacak dalın adı (açmaz): <onek>/YYYY-AA, doluysa -2, -3…"""
    dal = f"{onek}/{date.today():%Y-%m}"
    n = 2
    while git("rev-parse", "--verify", "--quiet", f"refs/heads/{dal}").returncode == 0:
        dal = f"{onek}/{date.today():%Y-%m}-{n}"
        n += 1
    return dal


def _kilit_canli_pid():
    """Canlı bir güncelleme kilidi varsa pid'i, yoksa None (dosyaya yazmaz)."""
    if not KILIT.exists():
        return None
    try:
        k = json.loads(KILIT.read_text())
        pid = int(k["pid"])
        return pid if subprocess.run(["kill", "-0", str(pid)], capture_output=True).returncode == 0 else None
    except Exception:  # noqa: BLE001
        return None


def aylik(kuru):
    """Aylık zincir. Bu aşamada YALNIZ --kuru: ön kontrol + rapor + liste raporu + PLAN + hızlı özet.
    Dal açmaz, commit atmaz, damga ya da özet dosyası yazmaz; git'e yalnız okuma komutları gönderir."""
    if not kuru:
        sys.exit("--aylik şimdilik yalnız --kuru ile çalışır (yazma adımları: dal açma, takip dalı, damga henüz yapılmadı). "
                 "Kaynak güncellemesi için: --uygula --dal.")
    print(f"AYLIK ZİNCİR — {date.today().isoformat()} (kuru: hiçbir şey değişmez)")
    pid = _kilit_canli_pid()
    if pid:
        sys.exit(f"DURDU: başka bir güncelleme sürüyor (pid {pid}).")
    damga = damga_oku()
    try:
        gun = (date.today() - date.fromisoformat(str(damga.get("son_calisma", ""))[:10])).days
    except ValueError:
        gun = None
    if gun is None:
        print("Aylık çalışma damgası yok (ilk kurulum ya da yeni makine).")
    elif gun > ESIK_KACAN_GUN:
        print(f"KAÇAN AY: son çalışma {gun} gün önce ({str(damga['son_calisma'])[:10]}). Bu koşu kaçan ayı da kapsar.")
    engeller = []
    dal = git("branch", "--show-current").stdout.strip()
    if dal != ANA_DAL:
        engeller.append(f"dal '{dal}' (master değil)")
    kirli = kirli_dosyalar()
    if kirli:
        neden = f"kirli ağaç ({len(kirli)} dosya): {kirli_ozet(kirli)}"
        if all(y in URETILEN_NOTLAR for _, y in kirli):
            adlar = " ".join(y for _, y in kirli)
            neden += (f"; yalnız rapor dosyaları değişmiş ({', '.join(y for _, y in kirli)}); onayınla kaydet "
                      f"(git add {adlar} && git commit) ya da geri al (git checkout -- {adlar})")
        engeller.append(neden)
    bekleyen = bekleyen_dallar()
    for b in bekleyen:
        engeller.append(f"bekleyen dal: {b['dal']} ({b['gun']} gün)")
    ok, _kalan, gneden = gh_hazir()
    if not ok:
        engeller.append(f"GitHub'a ulaşılamıyor ({gneden})")
    for e in engeller:
        print(f"Ön kontrol: {e}")
    degisen, sorunlu, _ayrinti = rapor()
    if ok:
        try:
            r = subprocess.run([sys.executable, str(KOK / "araclar" / "github-skill-listesi.py")], cwd=KOK,
                               capture_output=True, text=True, timeout=300)
            if r.stdout.strip():
                print(r.stdout.rstrip())
            if r.returncode != 0:
                print("UYARI: yıldız listesi kontrolü yapılamadı")
        except (OSError, subprocess.TimeoutExpired):
            print("UYARI: yıldız listesi kontrolü yapılamadı")
    if engeller:
        plan = "yalnız rapor (yazma adımı yapılmayacak; engeller: " + "; ".join(engeller) + ")"
    elif ULASILAMAYAN:
        plan = f"yalnız rapor ({len(ULASILAMAYAN)} kaynak şimdilik kontrol edilemedi; sonra tekrar çalıştır)"
    elif degisen and sorunlu and not kaynak_cek_atla_var():
        plan = "kısmi (erişilemeyen kaynak var; kaynak-cek.py --atla yok)"
    elif degisen:
        plan = f"güncelleme dalı {_dal_adi_onizle('guncelleme')} ({len(degisen)} kaynakta değişiklik)"
    else:
        plan = f"takip dalı {_dal_adi_onizle('takip')} (kaynaklarda değişiklik yok; yalnız trend/konu taraması)"
    print(f"PLAN: {plan}")
    ozet = KOK / "araclar" / "aylik-ozet.py"
    if ozet.exists():
        try:
            r = subprocess.run([sys.executable, str(ozet), "--hizli"], cwd=KOK, capture_output=True, text=True, timeout=120)
            print(r.stdout.rstrip() if r.stdout.strip() else "UYARI: aylık özet üretilemedi")
        except (OSError, subprocess.TimeoutExpired):
            print("UYARI: aylık özet üretilemedi")
    else:
        print("UYARI: aylık özet üretilemedi (araclar/aylik-ozet.py yok)")
    return 0


def main():
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print(__doc__)
        return 0
    if "--birlestir" in sys.argv:
        i = sys.argv.index("--birlestir")
        if i + 1 >= len(sys.argv):
            sys.exit("Kullanım: --birlestir guncelleme/YYYY-AA  (ya da takip/YYYY-AA)")
        return birlestir(sys.argv[i + 1])
    if "--aylik" in sys.argv:
        return aylik("--kuru" in sys.argv)
    siki = "--siki" in sys.argv
    degisen, sorunlu, ayrinti = rapor()
    bekleyen = bekleyen_dallar()
    for b in bekleyen:
        print(f"Onay bekleyen dal: {b['dal']} ({b['gun']} gün önce hazırlandı)")
        if b["birlesmis"]:
            print(f"{b['dal']} zaten master'a birleşmiş; silebilirsin: git branch -d {b['dal']}")
        elif b["gun"] > ESIK_DAL_GUN:
            print(f"UYARI: {b['dal']} {ESIK_DAL_GUN} günden eski: birleştir (--birlestir {b['dal']}) ya da sil (git branch -D {b['dal']}).")
    if bekleyen:
        print("(--birlestir <dal> ya da git branch -D <dal>)")
    if "--uygula" not in sys.argv or not degisen:
        if "--uygula" in sys.argv and CEVRIMDISI:
            sys.exit("DURDU: GitHub'a ulaşılamıyor; güncelleme yapılamaz. Hiçbir şey değişmedi.")
        if sorunlu:
            return 1
        return 2 if siki and (CEVRIMDISI or ULASILAMAYAN) else 0
    if sorunlu:
        sys.exit(f"DURDU: erişilemeyen kaynaklar var ({', '.join(sorunlu)}). kaynaklar.json'da bu kayıtların 'tip' alanını "
                 "'KAYIP' yap (arşivdeki kopyaları korunur). Kaydı SİLME: güvenlik kilidi skillleri kayıp sayıp güncellemeyi durdurur; "
                 "bilerek çıkarmak istiyorsan skilleri kaynaklar.json -> arsivden_cikarilanlar'a da yaz.")
    if ULASILAMAYAN:
        sys.exit(f"DURDU: {len(ULASILAMAYAN)} kaynak şimdilik kontrol edilemedi (geçici ağ/hız sınırı: "
                 f"{', '.join(ULASILAMAYAN[:5])}{' …' if len(ULASILAMAYAN) > 5 else ''}). Sonra tekrar çalıştır. Hiçbir şey değişmedi.")
    if bekleyen and "--dal" in sys.argv:
        sys.exit(f"DURDU: önce bekleyen güncelleme dalını birleştir ya da sil: {', '.join(b['dal'] for b in bekleyen)}")
    return uygula(degisen, ayrinti, "--dal" in sys.argv)


if __name__ == "__main__":
    sys.exit(main())
