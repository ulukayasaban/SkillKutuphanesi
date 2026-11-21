#!/usr/bin/env python3
"""Bakım: kaynak repolarda yeni commit var mı, yıldızlara yeni repo eklenmiş mi? Güncelleme git ile takip edilir.

  python3 araclar/arsiv-guncelle.py                      # sadece RAPOR (hiçbir şeyi değiştirmez)
  python3 araclar/arsiv-guncelle.py --uygula --dal       # ÖNERİLEN (aylık): güncellemeyi 'guncelleme/YYYY-AA' dalında yapar,
                                                         # notlar/guncelleme-gecmisi.md'ye kayıt düşer, dalda commit atar,
                                                         # master'a geri döner. master DEĞİŞMEZ.
  python3 araclar/arsiv-guncelle.py --birlestir <dal>    # kullanıcı onayından sonra: dalı master'a birleştirir (--no-ff),
                                                         # doğrulama + kapsam denetimi + testleri çalıştırır, dalı siler
  python3 araclar/arsiv-guncelle.py --uygula             # (eski yol) güncellemeyi doğrudan bulunulan dalda yapar
  python3 araclar/arsiv-guncelle.py --aylik              # AYLIK ZİNCİR (zamanlanmış görevin tek komutu): ön kontrol -> kaynak raporu
                                                         # (+ site takibi, site-takip.py; git dışı rapor) ->
                                                         # güncelleme (guncelleme/YYYY-AA) ya da takip (takip/YYYY-AA) dalı -> aylık özet ->
                                                         # damga (notlar/son-aylik-calisma.json). Birleştirmez, göndermez; master değişmez.
  python3 araclar/arsiv-guncelle.py --aylik --kuru       # aylık zincirin yan etkisiz PLANI: ön kontrol + rapor + özet (dal, commit, damga YOK)
  python3 araclar/arsiv-guncelle.py --siki               # rapor modu; GitHub'a ulaşılamadıysa ya da kaynak kontrol edilemediyse çıkış 2
  python3 araclar/arsiv-guncelle.py --help               # bu metin (hiçbir şey çalıştırmaz)

Çıkış kodu: 0 = sorun yok · 1 = erişilemeyen kaynak (rapor modu) ya da hata
            2 = YALNIZ --siki ile: GitHub'a ulaşılamadı ya da bazı kaynaklar kontrol edilemedi (yalnız yerel kontroller yapıldı)
--aylik çıkışı: 0 = tamam/kismi/bekleyen-dal · 1 = basarisiz · 2 = YALNIZ --siki ile kismi. Son satırlar: SONUÇ / NEDEN / DAL / ATLANAN KAYNAKLAR.
Bekleyen guncelleme/* ya da takip/* dalı varken yeni dal açılmaz; salt okuma adımları (rapor, özet) yine çalışır.

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
from ortak import (KAYNAKLAR, KOK, REGISTRY, GhBulunamadi, arsive_cekilir, gh_api, json_oku, json_yaz,  # noqa: E402
                   medya_haric_kumesi, repo_guncel, yerel_agac, yerel_commit)

GECMIS = KOK / "notlar" / "guncelleme-gecmisi.md"
ANA_DAL = "master"
DAMGA = KOK / "notlar" / "son-aylik-calisma.json"  # yerel, git'e girmez (.gitignore); yalnız --aylik yazar
SONUCLAR = ("tamam", "kismi", "basarisiz", "bekleyen-dal")
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
SON_HATA = ""  # _uygula geri alırken hatanın kısa nedeni (--aylik damgası için)
BOLUM_TARAMA = {"arsiv": 0, "fihrist": 0, "katalog": 0, "not": 0}
BOLUM_DEGISEN = {"fihrist": [], "katalog": [], "not": []}
KALDIGI_KAYNAK = None
GECICI_HATA_SAYISI = 0


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


def damga_tarihi(damga):
    """Damgadaki son çalışma tarihi (yeni 'tarih' ya da eski 'son_calisma'); yoksa None."""
    try:
        return date.fromisoformat(str(damga.get("tarih") or damga.get("son_calisma") or "")[:10])
    except ValueError:
        return None


def damga_yaz(sonuc, dal=None, neden="", atlanan=None, ad_degisen=None, ozet_durumu=None, *,
              taranan=None, etkilenen_proje_sayisi=0, toplu_onay_grubu_sayisi=0,
              kaldigi_kaynak=None, gecici_hata_sayisi=0):
    """notlar/son-aylik-calisma.json'u yazar (yerel, git'e girmez). .gitignore'da değilse yazmaz. -> yazıldı mı"""
    if sonuc not in SONUCLAR:
        raise ValueError(f"geçersiz sonuç: {sonuc}")
    if not yoksayiliyor_mu(DAMGA):
        print(f"UYARI: {DAMGA.relative_to(KOK)} .gitignore'da değil; ağacı kirletmemek için yazılmadı (.gitignore satırı eksik).")
        return False
    onceki = damga_oku()
    simdi = datetime.now().astimezone().isoformat(timespec="seconds")
    kayit = {"zaman": simdi, "sonuc": sonuc, "dal": dal, "neden": neden}
    gecmis = [g for g in (onceki.get("gecmis") or []) if isinstance(g, dict)]
    tar = dict(taranan or {})
    damga_durum = "tamamlandi" if (sonuc == "tamam" and gecici_hata_sayisi == 0 and not kaldigi_kaynak) else "yarim_kaldi"
    d = {"surum": 2, "tarih": simdi, "son_tarih": simdi[:10], "sonuc": sonuc, "durum": damga_durum,
         "dal": dal, "neden": neden,
         "atlanan_kaynaklar": sorted(set(atlanan or [])), "ad_degisen": dict(ad_degisen or {}),
         "ozet_durumu": ozet_durumu,
         "son_basarili": simdi if sonuc == "tamam" else onceki.get("son_basarili"),
         "taranan_arsiv": int(tar.get("arsiv", 0)),
         "taranan_fihrist": int(tar.get("fihrist", 0)),
         "taranan_katalog": int(tar.get("katalog", 0)),
         "taranan_not": int(tar.get("not", 0)),
         "etkilenen_proje_sayisi": int(etkilenen_proje_sayisi),
         "toplu_onay_grubu_sayisi": int(toplu_onay_grubu_sayisi),
         "kaldigi_kaynak": kaldigi_kaynak,
         "gecici_hata_sayisi": int(gecici_hata_sayisi),
         "gecmis": ([kayit] + gecmis)[:12]}
    try:
        DAMGA.parent.mkdir(parents=True, exist_ok=True)
        json_yaz(DAMGA, d)
    except OSError as e:
        print(f"UYARI: damga yazılamadı ({type(e).__name__})")
        return False
    return True


def damga_ozet_durumu(durum):
    """Özet üretildikten sonra damgaya özetin durumunu ekler (yeni geçmiş kaydı açmaz)."""
    d = damga_oku()
    if not d or not yoksayiliyor_mu(DAMGA):
        return
    d["ozet_durumu"] = durum
    try:
        json_yaz(DAMGA, d)
    except OSError:
        pass


def _yonlendirme_kontrol(repo, yanit):
    """Commit yanıtındaki html_url üzerinden 301 ad/sahip değişikliğini algılar (yeni kayıt açmaz)."""
    try:
        m = re.search(r"github\.com/([^/]+/[^/]+)/commit/", str(yanit.get("html_url", "")))
        if m:
            bilinen = {repo.lower(), str(repo_guncel(repo)).lower()}
            if m.group(1).lower() not in bilinen:
                ADI_DEGISEN[repo] = m.group(1)
                print(f"~ AD DEĞİŞMİŞ: {repo} -> {m.group(1)} (yeni kaynak DEĞİL; kaynaklar.json'da 'repo'yu yeni adla değiştir, "
                      "eski adı \"eski_adlar\"a yaz; rehber/09)")
    except Exception:  # noqa: BLE001
        pass


def bolumleri_tara(kayitlar, *, kaldigi_kaynak=None, fihrist_kok=None, programlar_veri=None,
                   sorunlu=None, bulunan_kaldi=True):
    """fihrist, katalog (kit + program) ve not (referans) bölümlerini commit bazında tarar.
    programlar.json yazılmaz, kit betiği çalıştırılmaz; 403/429/timeout asla KAYIP sayılmaz."""
    global KALDIGI_KAYNAK, GECICI_HATA_SAYISI
    sorunlu = sorunlu if sorunlu is not None else []
    fihrist_kok = Path(fihrist_kok) if fihrist_kok else (KOK / "fihrist")
    if programlar_veri is None:
        programlar_veri = (json_oku(KOK / "programlar.json", {}) or {}).get("programlar", {})
    degisen_bolum = {"fihrist": [], "katalog": [], "not": []}
    hedefler = []
    gorulen = set()
    for k in kayitlar:
        if not isinstance(k, dict) or not isinstance(k.get("repo"), str):
            continue
        bolum = k.get("bolum")
        if bolum not in ("fihrist", "katalog", "not"):
            continue
        if k.get("tip") in ("KAYIP", "EMEKLI", "T7", "T8"):
            continue
        repo = k["repo"]
        anahtar = (bolum, repo.lower())
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        hedefler.append((bolum, repo, k))

    art_arda = 0
    for i, (bolum, repo, k) in enumerate(hedefler):
        if not bulunan_kaldi:
            if repo.lower() == str(kaldigi_kaynak).lower():
                bulunan_kaldi = True
            else:
                continue
        BOLUM_TARAMA[bolum] += 1
        try:
            yanit = gh_api(f"repos/{repo}/commits/HEAD")
            yeni = yanit["sha"]
        except GhBulunamadi:
            art_arda = 0
            if repo not in sorunlu:
                sorunlu.append(repo)
            print(f"! [{bolum}] {repo}: erişilemiyor (404/410/422; otomatik KAYIP işaretlenmez).")
            continue
        except Exception as e:  # noqa: BLE001
            art_arda += 1
            GECICI_HATA_SAYISI += 1
            if KALDIGI_KAYNAK is None:
                KALDIGI_KAYNAK = repo
            if repo not in ULASILAMAYAN:
                ULASILAMAYAN.append(repo)
            print(f"! [{bolum}] {repo}: geçici hata ({str(e).strip().splitlines()[-1][:100] if str(e).strip() else type(e).__name__})")
            if art_arda >= 3:
                for _, kalan_repo, _ in hedefler[i + 1:]:
                    if kalan_repo not in ULASILAMAYAN:
                        ULASILAMAYAN.append(kalan_repo)
                print(f"UYARI: art arda 3 kaynak kontrol edilemedi ({bolum}); kalanlar atlandı.")
                break
            continue
        art_arda = 0
        _yonlendirme_kontrol(repo, yanit)
        eski = (k.get("son_kontrol") or {}).get("commit") if isinstance(k.get("son_kontrol"), dict) else None
        if bolum == "fihrist" and not eski:
            fd = json_oku(fihrist_kok / (repo.replace("/", "__") + ".json"), {}) or {}
            eski = fd.get("commit")
        elif bolum == "katalog" and not eski and k.get("program"):
            eski = (programlar_veri.get(k["program"]) or {}).get("kutuphane_commit")
        if eski and eski != yeni:
            degisen_bolum[bolum].append({"repo": repo, "tur": k.get("tur"), "eski": eski, "yeni": yeni})
            print(f"~ [{bolum}] {repo}: {eski[:7]} -> {yeni[:7]}")
    return degisen_bolum


def rapor(kaldigi_kaynak=None, tum_bolumler=False):
    """Kaynakları (arsiv, fihrist, katalog, not) kontrol eder. (degisen, sorunlu, ayrinti) döndürür.
    GitHub'a ulaşılamıyorsa kaynak karşılaştırması atlanır (CEVRIMDISI); geçici ağ hatası alan kaynaklar ULASILAMAYAN'a girer."""
    global ADI_DEGISEN, ULASILAMAYAN, CEVRIMDISI, BOLUM_TARAMA, BOLUM_DEGISEN, KALDIGI_KAYNAK, GECICI_HATA_SAYISI
    ADI_DEGISEN, ULASILAMAYAN, CEVRIMDISI = {}, [], False
    BOLUM_TARAMA = {"arsiv": 0, "fihrist": 0, "katalog": 0, "not": 0}
    BOLUM_DEGISEN = {"fihrist": [], "katalog": [], "not": []}
    KALDIGI_KAYNAK = None
    GECICI_HATA_SAYISI = 0
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
    ayar_k = json_oku(KAYNAKLAR)
    repolar = sorted({k["repo"] for k in ayar_k["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4") and arsive_cekilir(k)})
    art_arda = 0
    durdu_art_arda = False
    bulunan_kaldi = not bool(kaldigi_kaynak)
    for i, repo in enumerate(repolar):
        if not bulunan_kaldi:
            if repo.lower() == str(kaldigi_kaynak).lower():
                bulunan_kaldi = True
            else:
                continue
        BOLUM_TARAMA["arsiv"] += 1
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
            GECICI_HATA_SAYISI += 1
            if KALDIGI_KAYNAK is None:
                KALDIGI_KAYNAK = repo
            ULASILAMAYAN.append(repo)
            print(f"! {repo}: şimdilik kontrol edilemedi ({str(e).strip().splitlines()[-1][:120] if str(e).strip() else type(e).__name__})")
            if art_arda >= 3:
                kalan = repolar[i + 1:]
                ULASILAMAYAN.extend(kalan)
                durdu_art_arda = True
                print("UYARI: art arda 3 kaynak kontrol edilemedi; kalanlar atlandı (ağ/hız sınırı).")
                break
            continue
        art_arda = 0
        _yonlendirme_kontrol(repo, yanit)
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
    # Yerel kaynak (T7 kendi/, T8 site/): GitHub'a sorulmaz; kayıtlı sürüm kimliği diskteki içerikten türetilene eşit değilse değişmiştir
    for k in ayar_k["repolar"]:
        if k["tip"] not in ("T7", "T8"):
            continue
        BOLUM_TARAMA["arsiv"] += 1
        yeni = yerel_commit(yerel_agac(KOK / k["yerel"], ayar_k["skill_ici_haric"] + k.get("dosya_haric", []),
                                       tam_haric=medya_haric_kumesi(k))[0])
        eski = mevcut.get(k["repo"])
        if eski != yeni:
            degisen.append(k["repo"])
            ayrinti[k["repo"]] = {"eski": eski, "yeni": yeni, "dosya": 0, "not": f" (yerel kaynak: {k['yerel']}/ klasörü düzenlenmiş)"}
            print(f"~ {k['repo']}: {(eski or '-')[:7]} -> {yeni[:7]}  (yerel kaynak, {k['yerel']}/ düzenlenmiş)")
    if tum_bolumler and not durdu_art_arda:
        BOLUM_DEGISEN = bolumleri_tara(ayar_k["repolar"], kaldigi_kaynak=kaldigi_kaynak,
                                       sorunlu=sorunlu, bulunan_kaldi=bulunan_kaldi)
    if ULASILAMAYAN:
        print(f"Kontrol edilemeyen kaynak: {len(ULASILAMAYAN)} (geçici); sonra tekrar çalıştır.")
    if not degisen and not any(BOLUM_DEGISEN.values()):
        if not ULASILAMAYAN:
            print("Tüm kaynaklar güncel.")
    elif degisen:
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
              "(rehber/07-kategori-inceleme.md)"]
    if ATLANAN:
        satir.append(f"- **Bu ay erişilemeyen (atlanan) kaynaklar** ({len(ATLANAN)}): {', '.join(f'`{x}`' for x in ATLANAN)} "
                     "(arşiv kopyaları korundu; kalıcıysa kaynaklar.json'da 'tip': 'KAYIP' yapmak senin kararın)")
    satir.append("")
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


def kilit_al():
    """Canlı bir güncelleme kilidi varsa durur; yoksa (ya da ölü pid ise) kilidi bu sürece yazar."""
    if KILIT.exists():
        try:
            k = json.loads(KILIT.read_text())
            canli = Path(f"/proc/{k['pid']}").exists() or subprocess.run(["kill", "-0", str(k["pid"])], capture_output=True).returncode == 0
        except Exception:  # noqa: BLE001
            canli = False
        if canli:
            sys.exit(f"DURDU: başka bir güncelleme sürüyor (pid {k['pid']}, {k.get('baslangic')}).")
    KILIT.write_text(json.dumps({"pid": os.getpid(), "baslangic": datetime.now().isoformat(timespec="seconds")}))


def uygula(degisen, ayrinti, dal_modu):
    kirli = kirli_dosyalar()
    if kirli:
        sys.exit(f"DURDU: kütüphanede kaydedilmemiş değişiklik var ({len(kirli)} dosya): {kirli_ozet(kirli)}. "
                 "Önce kaydet (git commit) ya da geri al. Aylık plan için: python3 araclar/arsiv-guncelle.py --aylik --kuru "
                 "(kirli ağaçta salt okuma plan üretir).")
    api_hakki_kontrol()
    onceki = json_oku(REGISTRY)["skiller"]
    dal = git("branch", "--show-current").stdout.strip()
    kilit_al()
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
        if ATLANAN:  # erişilemeyen kaynak zinciri durdurmaz: arşiv kopyası korunur (yalnız --aylik doldurur)
            calistir(sys.executable, "araclar/kaynak-cek.py", "--atla", ",".join(ATLANAN))
        else:
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
        global SON_HATA
        SON_HATA = str(e).strip().splitlines()[-1][:200] if str(e).strip() else type(e).__name__
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


def _kacan_ay_satiri(damga):
    """Damga 35 günden eskiyse 'KAÇAN AY' satırı; damga yoksa bilgi satırı; yoksa None."""
    t = damga_tarihi(damga)
    if t is None:
        return "Aylık çalışma damgası yok (ilk kurulum ya da yeni makine)."
    gun = (date.today() - t).days
    if gun > ESIK_KACAN_GUN:
        return f"KAÇAN AY: son çalışma {gun} gün önce ({t.isoformat()}). Bu koşu kaçan ayı da kapsar."
    return None


def _engeller():
    """Ön kontrol (yalnız okur). -> (engeller, bekleyen, gh_ok, gh_neden, kirli_var). Engel = yazma adımını kapatan durum."""
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
    return engeller, bekleyen, ok, gneden, bool(kirli)


def _liste_raporu():
    """github-skill-listesi.py raporu (ağ ister; hata zinciri durdurmaz)."""
    try:
        r = subprocess.run([sys.executable, str(KOK / "araclar" / "github-skill-listesi.py")], cwd=KOK,
                           capture_output=True, text=True, timeout=300)
        if r.stdout.strip():
            print(r.stdout.rstrip())
        if r.returncode != 0:
            print("UYARI: yıldız listesi kontrolü yapılamadı")
    except (OSError, subprocess.TimeoutExpired):
        print("UYARI: yıldız listesi kontrolü yapılamadı")


def _site_takip_calistir(kuru=False):
    """Site skillerinin (T8, site/) kaynak sitesi değişti mi (araclar/site-takip.py, K-57). Dal açmaz, git'e yazmaz: rapor
    notlar/site-takip.md git dışıdır, aylık özet (4/5) ilk satırını okur. Kuru koşuda --yazmadan. Hata zinciri durdurmaz."""
    arac = KOK / "araclar" / "site-takip.py"
    if not arac.exists():
        print("  BİLGİ: araclar/site-takip.py yok; site takibi atlandı")
        return None
    try:
        r = subprocess.run([sys.executable, str(arac), *(["--yazmadan"] if kuru else [])], cwd=KOK, capture_output=True,
                           text=True, timeout=600, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.TimeoutExpired):
        print("  UYARI: site takibi yapılamadı (zaman aşımı ya da çalışmadı); kaynak KAYIP sayılmaz")
        return None
    satirlar = [s for s in r.stdout.splitlines() if s.startswith(("Site takibi:", "HATA:", "UYARI:", "Değişiklik var", "Site skili yok"))
                or s.lstrip().startswith(("DEĞİŞTİ", "YENİ İÇERİK", "ERİŞİLEMEDİ"))]
    for s in satirlar[:20]:
        print(f"  {s.strip()}")
    if r.returncode not in (0, 1):
        print(f"  UYARI: site takibi çıkış {r.returncode} (kayıt hatası?): python3 araclar/site-takip.py --kayit-denetle")
    return r.returncode


def _dal_geri_al(dal):
    """takip() hatasında: YALNIZ bu koşunun açtığı dalda ise değişiklikleri atar, master'a döner, o dalı siler."""
    if git("branch", "--show-current").stdout.strip() != dal:
        print("UYARI: geri alma yapılamadı (beklenmeyen dal); elle kontrol et")
        return
    git("reset", "-q", "--hard")
    git("clean", "-fdq", "notlar")
    git("switch", "-q", ANA_DAL)
    git("branch", "-D", dal)
    print(f"'{dal}' dalı geri alındı ve silindi; master değişmedi.")


def takip():
    """Kaynaklarda değişiklik yokken: takip/YYYY-AA dalında trend + popüler + konu taraması. -> (sonuc, dal|None, neden)
    Değişiklik yoksa kendi açtığı dalı siler. Hata olursa yalnız kendi dalını geri alır."""
    kilit_al()
    dal = _dal_adi_onizle("takip")
    try:
        calistir("git", "switch", "-q", "-c", dal)
        try:
            basarisiz = 0
            for ad, arg in (("github-trend.py", ["--aday"]), ("populer-tarama.py", []), ("konu-takip.py", [])):
                if subprocess.run([sys.executable, f"araclar/{ad}", *arg], cwd=KOK).returncode:
                    basarisiz += 1
                    print(f"UYARI: {ad} taraması yapılamadı; önceki rapor eski kaldı")
            if basarisiz == 3:
                _dal_geri_al(dal)
                return "kismi", None, "taramalar yapılamadı (ağ?)"
            calistir(sys.executable, "araclar/katalog-uret.py")
            calistir(sys.executable, "araclar/dogrula.py")
            if not git("status", "--porcelain").stdout.strip():
                git("switch", "-q", ANA_DAL)
                git("branch", "-D", dal)
                print("Takip: değişiklik yok (bu koşunun açtığı boş dal silindi).")
                return "tamam", None, ""
            calistir("git", "add", "-A")
            calistir("git", "commit", "-q", "-m", f"Aylık trend + konu takibi ({date.today().isoformat()})")
            calistir("git", "switch", "-q", ANA_DAL)
        except (subprocess.CalledProcessError, SystemExit, Exception) as e:  # noqa: BLE001
            print(f"HATA: takip yarıda kaldı: {e}")
            _dal_geri_al(dal)
            return "basarisiz", None, f"takip yarıda kaldı: {str(e).strip().splitlines()[-1][:150] if str(e).strip() else type(e).__name__}"
    finally:
        KILIT.unlink(missing_ok=True)
    print(f"Takip '{dal}' dalında hazır; master değişmedi.")
    print(f"Onayla:   python3 araclar/arsiv-guncelle.py --birlestir {dal}")
    print(f"Reddet:   git -C ~/Documents/SkillKutuphanesi branch -D {dal}")
    return "tamam", dal, ""


def _ozet_calistir():
    """aylik-ozet.py'yi tam kipte (proje-kullanimi'na --yaz vermeden) çalıştırıp metnini basar. -> özetin durumu ya da None"""
    ozet = KOK / "araclar" / "aylik-ozet.py"
    if not ozet.exists():
        print("UYARI: aylık özet üretilemedi (araclar/aylik-ozet.py yok)")
        return None
    try:
        r = subprocess.run([sys.executable, str(ozet), "--yazmadan", "--ozet-json"], cwd=KOK, capture_output=True, text=True, timeout=900)
    except (OSError, subprocess.TimeoutExpired):
        print("UYARI: aylık özet üretilemedi (zaman aşımı ya da çalışmadı)")
        return None
    try:
        d = json.loads(r.stdout.strip().splitlines()[-1])
        print("\n".join(d["satirlar"]))
        return str(d.get("durum"))
    except (ValueError, KeyError, IndexError, TypeError):
        print(r.stdout.rstrip() or "UYARI: aylık özet üretilemedi")
        return None


def _ozet_sonrasi_temizlik(baslangic_temiz):
    """Özet araçlarının yazdığı izinli rapor dosyalarını geri alır (dalda zaten üretilmiştir); başka kirli yol varsa yalnız uyarır."""
    if not baslangic_temiz or git("branch", "--show-current").stdout.strip() != ANA_DAL:
        return
    kirli = [y for _, y in kirli_dosyalar()]
    if not kirli:
        return
    if all(y in IZINLI_RAPOR_YOLLARI for y in kirli):
        git("checkout", "--", *kirli)
        print(f"Rapor dosyaları özet için üretilmişti; geri alındı: {', '.join(kirli)}")
    else:
        print(f"UYARI: ağaç kirli ({', '.join(kirli[:5])}); sonraki aylık koşu bunu engel sayar.")


def aylik_calistir(siki=False):
    """Aylık zincirin tek komutu. Sıra: ön kontrol, kaynak raporu, güncelleme/takip dalı, aylık özet, damga.
    Birleştirmez, göndermez, dal silmez (yalnız kendi hata geri alması). Damga güncelleme hata verse de yazılır."""
    global ATLANAN
    print(f"AYLIK ZİNCİR — {date.today().isoformat()}")
    pid = _kilit_canli_pid()
    if pid:
        sys.exit(f"DURDU: başka bir güncelleme sürüyor (pid {pid}). Damga yazılmadı.")
    onceki = damga_oku()
    satir = _kacan_ay_satiri(onceki)
    if satir:
        print(satir)
    sonuc, dal_adi, neden, atlanan = "tamam", None, "", []
    ozet_durumu, baslangic_temiz = None, False
    print("\nAdım 1/5 — Ön kontrol")
    engeller, bekleyen, gh_ok, gneden, kirli_var = _engeller()
    baslangic_temiz = not engeller
    for e in engeller:
        print(f"  Engel: {e}")
    if not engeller:
        print("  Engel yok: master'dayız, ağaç temiz, bekleyen dal yok, GitHub'a ulaşılıyor.")
    for b in bekleyen:
        print(f"  Onay bekleyen dal: {b['dal']} ({b['gun']} gün önce hazırlandı)"
              + (" — zaten master'a birleşmiş, silebilirsin" if b["birlesmis"] else ""))
        if b["gun"] > ESIK_DAL_GUN and not b["birlesmis"]:
            print(f"  UYARI: {b['dal']} {ESIK_DAL_GUN} günden eski: birleştir (--birlestir {b['dal']}) ya da sil (git branch -D {b['dal']}).")
    if bekleyen:
        print("  Yeni güncelleme dalı AÇILMAYACAK (önce eski dal: birleştir ya da sil); salt okuma adımları sürüyor.")
    if not gh_ok:
        print("  GitHub'a ulaşılamıyor: yalnız yerel kontroller yapılacak. Kendi terminalinde `gh auth login` çalıştırıp "
              "tarayıcıda onayla; sonra bu komutu yeniden çalıştır.")
    master_sha = git("rev-parse", ANA_DAL).stdout.strip()
    dallar_once = {b["dal"] for b in bekleyen}
    try:
        print("\nAdım 2/5 — Kaynak raporu")
        kaldigi = onceki.get("kaldigi_kaynak") if onceki.get("durum") == "yarim_kaldi" else None
        if kaldigi:
            print(f"  Önceki yarım kalan turdan devam ediliyor: {kaldigi}")
            degisen, sorunlu, ayrinti = rapor(kaldigi_kaynak=kaldigi, tum_bolumler=True)
        else:
            degisen, sorunlu, ayrinti = rapor()
            if not CEVRIMDISI and KALDIGI_KAYNAK is None:
                BOLUM_DEGISEN = bolumleri_tara(json_oku(KAYNAKLAR)["repolar"], sorunlu=sorunlu)
        if gh_ok:
            _liste_raporu()
        print("  Site takibi (siteden alınan skiller, site/):")
        _site_takip_calistir()
        atlanan = list(sorunlu)
        eski_atlanan = set(onceki.get("atlanan_kaynaklar") or [])
        for r in atlanan:
            print(f"  Bu ay erişilemedi: {r}" + (" (geçen ay da erişilemiyordu)" if r in eski_atlanan else "")
                  + ". Arşiv kopyası korunuyor; 'KAYIP' işaretlemek senin kararın (otomatik işaretlenmez).")
        print("\nAdım 3/5 — Güncelleme")
        if bekleyen:
            sonuc = "bekleyen-dal"
            neden = "; ".join(e for e in engeller)
            print("  Atlandı: bekleyen dal var.")
        elif engeller:
            sonuc = "kismi"
            neden = "; ".join(engeller)
            print("  Atlandı: ön kontrol engeli (yukarıda).")
        elif ULASILAMAYAN:
            sonuc = "kismi"
            neden = f"{len(ULASILAMAYAN)} kaynak şimdilik kontrol edilemedi (geçici ağ/hız sınırı): {', '.join(ULASILAMAYAN[:5])}"
            print(f"  Atlandı: {neden}. Sonra tekrar çalıştır.")
        elif degisen and atlanan and not kaynak_cek_atla_var():
            sonuc = "kismi"
            neden = "erişilemeyen kaynak var; kaynak-cek.py --atla yok"
            print(f"  Atlandı: {neden}.")
        else:
            ATLANAN = list(atlanan)
            if degisen:
                print(f"  Kaynaklarda değişiklik var ({len(degisen)}): güncelleme dalı hazırlanıyor.")
                try:
                    uygula(degisen, ayrinti, True)
                except SystemExit as e:
                    sonuc = "basarisiz"
                    neden = (e.code if isinstance(e.code, str) else SON_HATA) or "güncelleme yarıda kaldı"
                    print(f"  Güncelleme tamamlanamadı: {neden}")
                else:
                    yeni = [b["dal"] for b in bekleyen_dallar() if b["dal"] not in dallar_once]
                    dal_adi = yeni[0] if yeni else None
            else:
                print("  Kaynaklarda değişiklik yok: yalnız takip taraması (trend, popüler, konu).")
                try:
                    sonuc, dal_adi, neden = takip()
                except SystemExit as e:
                    sonuc, neden = "basarisiz", str(e.code)
    except Exception as e:  # noqa: BLE001  zincir hiçbir beklenmedik hatada damgasız kalmaz
        sonuc = "basarisiz"
        neden = f"beklenmeyen hata: {type(e).__name__}: {str(e).strip()[:150]}"
        print(f"HATA: {neden}")
    except SystemExit as e:  # rapor() içinden gelen çıkış
        sonuc, neden = "basarisiz", str(e.code)
    # master dışında kaldıysak (yarım hata) ve ağaç temizse geri dön
    if baslangic_temiz and git("branch", "--show-current").stdout.strip() != ANA_DAL and not kirli_dosyalar():
        git("switch", "-q", ANA_DAL)
    if git("rev-parse", ANA_DAL).stdout.strip() != master_sha:
        print("UYARI: master değişmiş görünüyor; kontrol et (bu komut master'a yazmaz).")
    damga_yaz(sonuc, dal_adi, neden, atlanan, ADI_DEGISEN,
              taranan=BOLUM_TARAMA, kaldigi_kaynak=KALDIGI_KAYNAK, gecici_hata_sayisi=GECICI_HATA_SAYISI)
    print("\nAdım 4/5 — Aylık özet (tek sayfa)")
    ozet_durumu = _ozet_calistir()
    _ozet_sonrasi_temizlik(baslangic_temiz)
    print("\nAdım 5/5 — Damga")
    if ozet_durumu:
        damga_ozet_durumu(ozet_durumu)
    print(f"  {DAMGA.relative_to(KOK)}: sonuç {sonuc}" if DAMGA.exists() else "  Damga yazılamadı (yukarıdaki uyarıya bak).")
    print(f"\nSONUÇ: {sonuc}")
    if neden:
        print(f"NEDEN: {neden}")
    if dal_adi:
        print(f"DAL: {dal_adi}")
    if atlanan:
        print(f"ATLANAN KAYNAKLAR: {', '.join(atlanan)}")
    for eski, yeni in ADI_DEGISEN.items():
        print(f"AD DEĞİŞMİŞ: {eski} -> {yeni}")
    return 1 if sonuc == "basarisiz" else 2 if (siki and sonuc == "kismi") else 0


def aylik(kuru, siki=False):
    """Aylık zincir. --kuru: yan etkisiz plan (ön kontrol + rapor + liste raporu + PLAN + hızlı özet; dal, commit, damga yok).
    Kuru olmadan: aylik_calistir()."""
    if not kuru:
        return aylik_calistir(siki)
    print(f"AYLIK ZİNCİR — {date.today().isoformat()} (kuru: hiçbir şey değişmez)")
    pid = _kilit_canli_pid()
    if pid:
        sys.exit(f"DURDU: başka bir güncelleme sürüyor (pid {pid}).")
    satir = _kacan_ay_satiri(damga_oku())
    if satir:
        print(satir)
    engeller, _bekleyen, ok, _gneden, _kirli = _engeller()
    for e in engeller:
        print(f"Ön kontrol: {e}")
    degisen, sorunlu, _ayrinti = rapor()
    if ok:
        _liste_raporu()
    print("Site takibi (yazmadan):")
    _site_takip_calistir(kuru=True)
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
        return aylik("--kuru" in sys.argv, "--siki" in sys.argv)
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
