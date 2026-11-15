#!/usr/bin/env python3
"""Aylık özet: rapor araçlarını `--ozet-json` ile toplar, kendi kontrollerini ekler, kullanıcıya kısa düz Türkçe özet verir.

  python3 araclar/aylik-ozet.py                # TAM: araçları koşturur, notlar/aylik-ozet.md yazar, kısa özeti basar
  python3 araclar/aylik-ozet.py --hizli        # UCUZ (oturum başı): ağ yok, yazma yok, <= 15 satır (takma ad: --oturum)
  python3 araclar/aylik-ozet.py --yazmadan     # TAM ama proje-kullanimi'na --yaz VERMEZ (zincir içi kullanım için)
  python3 araclar/aylik-ozet.py --ozet-json    # stdout'a tek JSON nesnesi {arac, durum, satirlar, karar_bekleyen}
  python3 araclar/aylik-ozet.py --siki         # durum 'sorun' ise çıkış 1 (varsayılan her zaman 0)

--hizli salt okur, hiçbir dosya yazmaz. TAM mod rapor dosyalarını yeniler: notlar/aylik-ozet.md (.gitignore'da olmalı, yoksa yazılmaz) ve
altındaki araçların kendi rapor dosyaları (notlar/proje-kullanimi.md, notlar/proje-durumu.md). Yalnız kütüphane içine yazar.
--ozet-json yalnız çıktı biçimini değiştirir, yazma davranışını değil: tam modda --ozet-json de notlar/aylik-ozet.md yazar ve
proje-kullanimi'na --yaz verir (--yazmadan ile verilmez), program-denetim ağ işi yapar. Yazmasız ve ağsız çağrı için yalnız --hizli.
Git'e hiçbir yazma komutu göndermez. Bir araç yoksa ya da çökerse o araç 'dikkat' olur, özet çalışmaya devam eder.
Gizli test bayrakları: --kok --cikti --zaman-asimi --gorev-yolu --paralel --arac-listesi-json
"""
import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path

ESIK_CALISMA = 35
ESIK_CALISMA_SORUN = 70
ESIK_RAPOR = 45
ESIK_DAL = 45
SATIR_SINIRI = 300
ADAY_GOSTER = 5
HIZLI_ZAMAN_ASIMI = 20
IZINLI_RAPOR_YOLLARI = ("notlar/proje-durumu.md", "notlar/program-denetimi.md")
RAPOR_NOTLARI = IZINLI_RAPOR_YOLLARI + ("notlar/proje-kullanimi.md", "notlar/yol-denetimi.md")
CANLI_GOREV = Path.home() / ".claude" / "scheduled-tasks" / "skill-kutuphanesi-aylik-guncelleme" / "SKILL.md"
SIRA = {"temiz": 0, "dikkat": 1, "sorun": 2}

# ortak.OZET_ARACLARI (P8) yoksa kullanılan sabit yedek
ORTAK_YEDEK = [("git-durum", []), ("yedek-denetim", []), ("genel-bekci", []), ("program-denetim", []),
               ("proje-kullanimi", ["--saglik"])]
# P4'e özgü, ağsız, yazmaz. konu-takip --bekleyenler üç aday kaynağını (konu takibi, trend, popüler) birlikte özetler.
EK_TAM = [("skill-ekle", ["--araclar"]), ("konu-takip", ["--bekleyenler"])]
HIZLI_ADLAR = {"genel-bekci", "git-durum", "yedek-denetim"}


def kirp(metin, sinir=SATIR_SINIRI):
    metin = " ".join(str(metin).split())
    return metin if len(metin) <= sinir else metin[:sinir - 1] + "…"


def git(kok, *args):
    try:
        return subprocess.run(["git", *args], cwd=kok, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return subprocess.CompletedProcess(args, 128, "", "git çalışmadı")


def kirli_yollar(kok):
    """git status --porcelain -z -> {yol}. Depo değilse boş küme."""
    r = git(kok, "status", "--porcelain", "-z")
    if r.returncode != 0:
        return set()
    parca, sonuc, i = r.stdout.split("\0"), set(), 0
    while i < len(parca):
        p = parca[i]
        i += 1
        if len(p) < 4:
            continue
        if "R" in p[:2] or "C" in p[:2]:
            i += 1
        sonuc.add(p[3:])
    return sonuc


def sonuc_eki(sonuc):
    """Damgada sonuç alanı yoksa ': ?' yazma (sonuç kaydı henüz tutulmuyor)."""
    return f": {sonuc}" if sonuc else ""


def dikkat_sebebi(k):
    """Dikkat/sorun olan kontrolün asıl sebebi: aday sayısı, ilk karar maddesi, yoksa ilk satır."""
    if k.get("tam_liste"):
        n = sum(len(g) for g in k["tam_liste"] if g)
        if n:
            return f"{n} aday karar bekliyor"
    if k["karar_bekleyen"]:
        return k["karar_bekleyen"][0]
    for x in k["satirlar"]:
        if re.search(r"YENİ SÜRÜM|geride|UYARI|SORUN|HATA", x):
            return x
    return k["satirlar"][0] if k["satirlar"] else "-"


def kontrol(ad, durum, satirlar, karar=None, dikkat=None, calisti=True):
    return {"ad": ad, "durum": durum, "satirlar": [kirp(x) for x in satirlar], "karar_bekleyen": [kirp(x) for x in (karar or [])],
            "dikkat_satirlar": [kirp(x) for x in (dikkat if dikkat is not None else (satirlar[:2] if durum != "temiz" else []))],
            "calisti": calisti}


# ------------------------------------------------------------------ araç listesi ve koşturma
def arac_listesi(kok, hizli, yaz, liste_json=None):
    if liste_json:
        ham = json.loads(Path(liste_json).read_text(encoding="utf-8"))
        tam = [(a[0], list(a[1])) for a in ham]
    else:
        ortak = None
        try:
            yol = Path(kok) / "araclar" / "ortak.py"
            spec = importlib.util.spec_from_file_location("ortak_aylik", yol)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            ortak = list(getattr(m, "OZET_ARACLARI"))
        except Exception:  # noqa: BLE001  ortak yok / liste yok -> sabit yedek
            ortak = None
        if ortak:
            ortak = [(a, []) if isinstance(a, str) else (a[0], list(a[1])) for a in ortak]
        tam = []
        for ad, bay in (ortak or ORTAK_YEDEK) + EK_TAM:
            if (ad, bay) not in tam:
                tam.append((ad, bay))
    sonuc = []
    for ad, bay in tam:
        if hizli and not (ad in HIZLI_ADLAR or ad == "konu-takip"):  # skill-ekle --araclar sürüm komutu çalıştırır: yalnız tam kip
            continue
        bay = list(bay)
        if ad == "proje-kullanimi" and yaz and not hizli:
            bay.append("--yaz")
        if hizli and ad == "git-durum" and "--gh-yok" not in bay:
            bay.append("--gh-yok")  # GitHub'a hiç gitme
        sonuc.append((ad, bay))
    return sonuc


def json_ayikla(metin):
    metin = (metin or "").strip()
    adaylar = [metin] + [s for s in reversed(metin.splitlines()) if s.lstrip().startswith("{")]
    for a in adaylar:
        try:
            d = json.loads(a)
            if isinstance(d, dict):
                return d
        except ValueError:
            continue
    return None


def sema_gecerli(d):
    return (isinstance(d, dict) and isinstance(d.get("arac"), str) and d.get("durum") in SIRA
            and isinstance(d.get("satirlar"), list) and isinstance(d.get("karar_bekleyen"), list)
            and all(isinstance(x, str) for x in d["satirlar"] + d["karar_bekleyen"]))


def arac_kos(kok, ad, bayraklar, zaman_asimi):
    dosya = Path(kok) / "araclar" / f"{ad}.py"
    if not dosya.exists():
        return kontrol(ad, "dikkat", [f"{ad}: araç kütüphanede yok (atlandı)"], calisti=False)
    komut = [sys.executable, str(dosya), *bayraklar, "--ozet-json"]
    try:
        r = subprocess.run(komut, cwd=kok, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=zaman_asimi)
    except subprocess.TimeoutExpired:
        return kontrol(ad, "dikkat", [f"{ad}: zaman aşımı ({zaman_asimi} sn)"], calisti=False)
    except OSError as e:
        return kontrol(ad, "dikkat", [f"{ad}: çalışmadı ({type(e).__name__})"], calisti=False)
    d = json_ayikla(r.stdout)
    if d is None:
        son = (r.stderr or "").strip().splitlines()
        return kontrol(ad, "dikkat", [f"{ad}: çalışmadı (çıkış {r.returncode}): {kirp(son[-1] if son else 'çıktı yok', 200)}"],
                       calisti=False)
    if not sema_gecerli(d):
        return kontrol(ad, "dikkat", [f"{ad}: çıktı biçimi bozuk"], calisti=False)
    return kontrol(ad, d["durum"], d["satirlar"], d["karar_bekleyen"])


def araclari_kos(kok, liste, zaman_asimi, paralel):
    """-> (kontroller sırayla, {ad: (baslangic, bitis)})"""
    pencere, sonuc = {}, {}

    def is_(ad, bay):
        t0 = time.time()
        try:
            k = arac_kos(kok, ad, bay, zaman_asimi)
        except Exception as e:  # noqa: BLE001
            k = kontrol(ad, "dikkat", [f"{ad}: beklenmeyen hata ({type(e).__name__})"], calisti=False)
        pencere[ad] = (t0, time.time())
        return k

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, paralel)) as ex:
        vadeli = [ex.submit(is_, ad, bay) for ad, bay in liste]
        for (ad, _), f in zip(liste, vadeli):
            sonuc[ad] = f.result()
    return [sonuc[ad] for ad, _ in liste], pencere


# ------------------------------------------------------------------ kendi kontrollerimiz
def tarih_oku(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def json_oku(yol, varsayilan=None):
    try:
        return json.loads(Path(yol).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return varsayilan


def metin_oku(yol, satir_sayisi=None):
    try:
        t = Path(yol).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    return "\n".join(t.splitlines()[:satir_sayisi]) if satir_sayisi else t


def damga_kontrol(kok, bugun):
    damga = json_oku(Path(kok) / "notlar" / "son-aylik-calisma.json", {})
    if not isinstance(damga, dict):
        damga = {}
    satir, karar, durum, dikkat = [], [], "temiz", []
    soru = "Aylık çalışmayı şimdi yapayım mı? (python3 -u araclar/arsiv-guncelle.py --aylik; önce plan görmek istersen: --aylik --kuru)"
    son = tarih_oku(damga.get("tarih") or damga.get("son_calisma"))  # 'tarih' yeni damga, 'son_calisma' eski biçim
    sonuc = damga.get("sonuc") or damga.get("son_sonuc")
    neden = damga.get("neden") or damga.get("son_neden")
    kayit_yedegi = False
    if son is None:
        t = metin_oku(Path(kok) / "notlar" / "guncelleme-gecmisi.md", 60) or ""
        tarihler = [tarih_oku(m) for m in re.findall(r"^## (\d{4}-\d{2}-\d{2})", t, re.M)]
        tarihler = [x for x in tarihler if x]
        if tarihler:
            son, kayit_yedegi = max(tarihler), True
    if son is None:
        satir.append("Aylık çalışma damgası yok (ilk kurulum ya da yeni makine); şimdilik guncelleme-gecmisi.md tarihine bakılır")
    else:
        gun = (bugun - son).days
        if kayit_yedegi:
            satir.append(f"Aylık çalışma damgası yok; son kayıtlı güncelleme {son.isoformat()} ({gun} gün önce)")
        if gun > ESIK_CALISMA:
            durum = "sorun" if gun > ESIK_CALISMA_SORUN else "dikkat"
            satir.append(f"Aylık çalışma {gun} gündür yapılmadı (son: {son.isoformat()}) — kaçan ay var")
            dikkat.append(satir[-1])
            karar.append(soru)
        elif not kayit_yedegi:
            satir.append(f"Son aylık çalışma {son.isoformat()} ({gun} gün önce){sonuc_eki(sonuc)}")
    if sonuc in ("kismi", "basarisiz", "bekleyen-dal", "hata", "durduruldu"):
        durum = max(durum, "dikkat", key=SIRA.get)
        satir.append(f"Son çalışma yarım kaldı: {sonuc} — {neden or 'neden yazılmamış'}")
        dikkat.append(satir[-1])
        sb = tarih_oku(damga.get("son_basarili"))
        if sb and (bugun - sb).days > ESIK_CALISMA:
            satir.append(f"Son başarılı çalışma {(bugun - sb).days} gün önce")
    atlanan = [x for x in (damga.get("atlanan_kaynaklar") or []) if isinstance(x, str)]
    if atlanan:
        kaynaklar = json_oku(Path(kok) / "kaynaklar.json", {}) or {}
        kayip = {k.get("repo") for k in kaynaklar.get("repolar", []) if isinstance(k, dict) and k.get("tip") == "KAYIP"}
        for repo in atlanan:
            if repo in kayip:
                satir.append(f"KAYIP işaretli kaynak: {repo}")
            else:
                satir.append(f"Erişilemeyen kaynak: {repo} (kalıcıysa kaynaklar.json'da tip KAYIP yapılması senin kararın)")
                karar.append(f"{repo} kaynakta erişilemiyor: KAYIP olarak işaretlensin mi? "
                             f"(rehber/03 E3; kaynak-cikar.py --repo {repo} --kuru)")
    ad_deg = damga.get("ad_degisen") if isinstance(damga.get("ad_degisen"), dict) else {}
    for eski, yeni in ad_deg.items():
        satir.append(f"Adı değişen kaynak: {eski} → {yeni}")
        karar.append(f"Adı değişen kaynak: {eski} → {yeni}; kaynaklar.json düzeltilsin mi?")
    k = kontrol("aylik-calisma", durum, satir, karar, dikkat)
    k["son"], k["son_sonuc"] = son, sonuc if damga else None
    k["damga_var"] = bool(damga)
    return k


def dal_kontrol(kok, bugun):
    if git(kok, "rev-parse", "--git-dir").returncode != 0:
        return kontrol("bekleyen-dallar", "temiz", ["git deposu değil"])
    adlar = git(kok, "branch", "--list", "guncelleme/*", "takip/*", "--format=%(refname:short)").stdout.split()
    satir, karar, dikkat, durum = [], [], [], "temiz"
    if not adlar:
        satir.append("Bekleyen güncelleme ya da takip dalı yok")
    for dal in adlar:
        ct = git(kok, "log", "-1", "--format=%ct", dal).stdout.strip()
        gun = (bugun - date.fromtimestamp(int(ct))).days if ct.isdigit() else 0
        birlesmis = git(kok, "merge-base", "--is-ancestor", dal, "master").returncode == 0
        satir.append(f"Bekleyen dal {dal} ({gun} gün önce hazırlandı)")
        if birlesmis:
            satir.append(f"{dal} zaten master'a birleşmiş; silebilirsin (git branch -d {dal})")
            continue
        karar.append(f"{dal} dalı onayını bekliyor: incelenip birleştirilsin mi? (promptlar/08)")
        if gun > ESIK_DAL:
            durum = "dikkat"
            satir.append(f"{dal} {ESIK_DAL} günden eski; birleştir ya da sil")
            dikkat.append(satir[-1])
        if dal.startswith("guncelleme/"):
            g = git(kok, "show", f"{dal}:notlar/guncelleme-gecmisi.md").stdout.splitlines()[:80]
            g = "\n".join(g)
            for desen, cumle in ((r"\*\*Karar bekleyen yeni skiller\*\* \((\d+)",
                                  "{dal}: {n} yeni skill karar bekliyor (kaynaklar.json 'dahil'/'haric')"),
                                 (r"\*\*Yeniden incelenecek\*\* \((\d+)\)", "{dal}: {n} skill yeniden incelenecek (rehber/07)")):
                m = re.search(desen, g)
                if m and int(m.group(1)) > 0:
                    karar.append(cumle.format(dal=dal, n=m.group(1)))
    return kontrol("bekleyen-dallar", durum, satir, karar, dikkat)


def rapor_yasi(kok, bugun):
    kok = Path(kok)
    kaynaklar = []  # (ad, tarih|None, var_mi)
    t = json_oku(kok / "trend.json", {}) or {}
    kaynaklar.append(("github-trend", tarih_oku(t.get("son_tarama")) if isinstance(t, dict) else None, (kok / "trend.json").exists()))
    kt = json_oku(kok / "konu-takip.json", {}) or {}
    tarihler = [tarih_oku(v.get("son_tarama")) for v in (kt.get("konular") or {}).values() if isinstance(v, dict)] if isinstance(kt, dict) else []
    tarihler = [x for x in tarihler if x]
    if tarihler:
        kt_tarih = max(tarihler)
    else:
        m = re.search(r"Son tarama: (\d{4}-\d{2}-\d{2})", metin_oku(kok / "notlar" / "konu-takip.md") or "")
        kt_tarih = tarih_oku(m.group(1)) if m else None
    kaynaklar.append(("konu-takip", kt_tarih, (kok / "konu-takip.json").exists() or (kok / "notlar" / "konu-takip.md").exists()))
    for ad, yol in (("populer-skiller", "notlar/populer-skiller.md"), ("program-denetimi", "notlar/program-denetimi.md"),
                    ("yol-denetimi", "notlar/yol-denetimi.md")):
        t3 = (metin_oku(kok / yol, 3) or "").splitlines()
        m = re.search(r"\d{4}-\d{2}-\d{2}", t3[2] if len(t3) >= 3 else "")
        kaynaklar.append((ad, tarih_oku(m.group(0)) if m else None, (kok / yol).exists()))
    durum_yol = kok / "notlar" / "hf-om-gecisi" / "DURUM.md"
    if durum_yol.exists():
        m = re.search(r"Son güncelleme: (\d{4}-\d{2}-\d{2})", metin_oku(durum_yol, 20) or "")
        kaynaklar.append(("DURUM.md", tarih_oku(m.group(1)) if m else None, True))
    satir, dikkat, durum, tablo = [], [], "temiz", []
    for ad, tarih, var in kaynaklar:
        if not var:
            continue
        if tarih is None:
            satir.append(f"{ad}: tarih okunamadı")
            tablo.append((ad, "-", "-", "tarih okunamadı"))
            continue
        gun = (bugun - tarih).days
        if gun > ESIK_RAPOR:
            durum = "dikkat"
            dikkat.append(f"{ad} {gun} gün eski")
            satir.append(f"{ad}: {gun} gün eski ({tarih.isoformat()})")
            tablo.append((ad, tarih.isoformat(), gun, "dikkat"))
        else:
            satir.append(f"{ad}: {tarih.isoformat()} ({gun} gün önce)")
            tablo.append((ad, tarih.isoformat(), gun, "temiz"))
    k = kontrol("rapor-yasi", durum, satir, None, dikkat)
    k["tablo"] = tablo
    return k


def md_bolum(metin, baslik_oneki):
    """'## <baslik_oneki>...' bölümünün satırları (sonraki '## ' başlığına kadar)."""
    if metin is None:
        return None
    sonuc, icerde = [], False
    for s in metin.splitlines():
        if s.startswith("## "):
            if icerde:
                break
            icerde = s[3:].strip().lower().startswith(baslik_oneki.lower())
            continue
        if icerde:
            sonuc.append(s)
    return sonuc if icerde or sonuc else None


def kararlar_oku(kok):
    """notlar/kararlar.md -> (kutular, susturma_ifadeleri[(ifade, bitis|None)])"""
    t = metin_oku(Path(kok) / "notlar" / "kararlar.md")
    kutular, ifadeler = [], []
    try:
        for s in md_bolum(t, "Karar bekleyenler") or []:
            m = re.match(r"^\s*[-*]\s*\[ \]\s+(.+)$", s)
            if m:
                kutular.append(kirp(m.group(1)))
        for s in md_bolum(t, "Kabul edilen bekleyenler") or []:
            m = re.match(r"^\s*[-*]\s+(.+)$", s)
            if not m:
                continue
            govde, bitis = m.group(1).strip(), None
            if "|" in govde:
                govde, _, b = govde.rpartition("|")
                bitis, govde = tarih_oku(b.strip()), govde.strip()
            if len(govde) >= 8:
                ifadeler.append((govde.lower(), bitis))
    except Exception:  # noqa: BLE001
        pass
    return kutular, ifadeler


def sustur(kararlar, ifadeler, bugun):
    """5b: kabul edilen ifadeyi içeren kararlar çıkarılır. -> (kalan, susturulan_sayisi)"""
    aktif = [i for i, b in ifadeler if b is None or bugun <= b]
    kalan, say = [], 0
    for k in kararlar:
        if any(i in k.lower() for i in aktif):
            say += 1
        else:
            kalan.append(k)
    return kalan, say


def bekleyen_notlar(kok, kontroller, calisan_adlar):
    """Aday sayıları: birincil yol araç çıktısı (konu-takip --bekleyenler); regex yalnız araç çalışmadıysa yedek."""
    kok = Path(kok)
    karar, satir = [], []
    kt = next((k for k in kontroller if k["ad"] == "konu-takip"), None)
    if kt is not None and kt["calisti"]:
        gruplar = {"konu takibi": [], "trend": [], "popüler": [], "izlenen": []}
        for c in kt["karar_bekleyen"]:
            ad = c.split(" (")[0]
            if "izlenen, vadesi geldi" in c:
                gruplar["izlenen"].append(ad)
            elif re.search(r"\(trend, \d+ skill\)", c):
                gruplar["trend"].append(ad)
            elif c.endswith(", popüler)"):
                gruplar["popüler"].append(ad)
            else:
                gruplar["konu takibi"].append(ad)
        for g, adlar in gruplar.items():
            if adlar:
                ek = f" (… +{len(adlar) - ADAY_GOSTER} daha; tam liste: notlar/aylik-ozet.md)" if len(adlar) > ADAY_GOSTER else ""
                karar.append(f"{g}: en az {len(adlar)} aday karar bekliyor; ilk {min(ADAY_GOSTER, len(adlar))}: "
                             f"{', '.join(adlar[:ADAY_GOSTER])}{ek} (kapatmak: konu-takip.py --karar owner/ad eklendi|reddedildi|izle)")
        kt["karar_bekleyen"] = []  # aday satırları yukarıda tek satıra indirildi
        kt["tam_liste"] = [c for c in gruplar.values()]
    elif "konu-takip" in calisan_adlar:
        # YEDEK: araç çalışmadı; rapor dosyalarını regex ile oku (biçim değişirse "okunamadı", çökme yok)
        satir.append("konu-takip: yedek okuma (araç çalışmadı)")
        try:
            t = metin_oku(kok / "notlar" / "konu-takip.md")
            if t is not None:
                n = sum(int(x) for x in re.findall(r"\*\*odaklı aday: (\d+)\*\*", t))
                if n:
                    karar.append(f"{n} odaklı aday repo karar bekliyor (notlar/konu-takip.md)")
        except Exception:  # noqa: BLE001
            satir.append("okunamadı: notlar/konu-takip.md")
        try:
            t = metin_oku(kok / "notlar" / "populer-skiller.md")
            m = re.search(r"^## Yeni adaylar \((\d+)\)", t or "", re.M)
            if m and int(m.group(1)) > 0:
                karar.append(f"{m.group(1)} yeni aday repo (notlar/populer-skiller.md)")
        except Exception:  # noqa: BLE001
            satir.append("okunamadı: notlar/populer-skiller.md")
        try:
            t = metin_oku(kok / "notlar" / "github-trend.md")
            b = md_bolum(t, "Son taramada trend'de olup kütüphanede olmayan repolar")
            if b:
                n = 0
                for s in b:
                    m = re.match(r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", s)
                    if m and int(m.group(2)) > 0:
                        n += 1
                if n:
                    karar.append(f"{n} trend aday repo (SKILL.md içeren; notlar/github-trend.md)")
        except Exception:  # noqa: BLE001
            satir.append("okunamadı: notlar/github-trend.md")
    pd = next((k for k in kontroller if k["ad"] == "program-denetim"), None)
    if pd is not None and not pd["calisti"] and "program-denetim" in calisan_adlar:
        try:
            for s in (metin_oku(kok / "notlar" / "program-denetimi.md") or "").splitlines():
                if s.startswith("|") and "YENİ SÜRÜM VAR" in s:
                    ad = s.strip("|").split("|")[0].strip()
                    if ad:
                        karar.append(f"{ad}: yeni sürüm var, güncelleme onayı bekliyor (rehber/11)")
            satir.append("program-denetim: yedek okuma (araç çalışmadı)")
        except Exception:  # noqa: BLE001
            satir.append("okunamadı: notlar/program-denetimi.md")
    k = kontrol("bekleyen-notlar", "temiz", satir, karar)
    return k


def gorev_kopyasi_kontrol(kok, gorev_yolu):
    """Canlı zamanlanmış görev metni ile kütüphane kopyası (zamanlanmis/aylik-guncelleme.SKILL.md): salt okuma karşılaştırma.
    Aynı -> temiz; farklı ya da canlı dosya yok -> dikkat. Kütüphane kopyası yoksa (bu paket öncesi) sessiz geçer."""
    kopya = Path(kok) / "zamanlanmis" / "aylik-guncelleme.SKILL.md"
    canli = Path(gorev_yolu)
    if not kopya.exists():
        return kontrol("zamanlanmis-gorev", "temiz", [], calisti=True)
    if not canli.exists():
        return kontrol("zamanlanmis-gorev", "dikkat", [f"Canlı zamanlanmış görev dosyası bulunamadı ({canli.name}); görev kurulu olmayabilir "
                                                       "(kütüphane kopyası: zamanlanmis/aylik-guncelleme.SKILL.md)"])
    try:
        h1 = hashlib.sha256(kopya.read_bytes()).hexdigest()
        h2 = hashlib.sha256(canli.read_bytes()).hexdigest()
    except OSError:
        return kontrol("zamanlanmis-gorev", "dikkat", ["Zamanlanmış görev dosyaları okunamadı"])
    if h1 == h2:
        return kontrol("zamanlanmis-gorev", "temiz", ["Zamanlanmış görev metni kütüphane kopyasıyla aynı"])
    return kontrol("zamanlanmis-gorev", "dikkat",
                   ["Zamanlanmış görev metni kütüphane kopyasından farklı; güncellemek için onay gerekir (rehber/02 'Zamanlanmış görev metni')"],
                   ["Zamanlanmış görev metni güncellensin mi?"])


def yerel_git(kok):
    """git-durum.py yoksa hızlı mod yedeği: kirli sayı ve gönderilmemiş commit sayısı (ağ yok)."""
    if git(kok, "rev-parse", "--git-dir").returncode != 0:
        return kontrol("yerel-git", "temiz", ["git deposu değil"])
    satir, durum = [], "temiz"
    n = len(kirli_yollar(kok))
    if n:
        satir.append(f"Kaydedilmemiş değişiklik: {n} dosya")
        durum = "dikkat"
    r = git(kok, "rev-list", "--left-right", "--count", "origin/master...master")
    if r.returncode == 0 and len(r.stdout.split()) == 2:
        onde = int(r.stdout.split()[1])
        if onde:
            satir.append(f"Uzaktan {onde} commit önde (gönderilmedi)")
            durum = "dikkat"
    return kontrol("yerel-git", durum, satir or ["Git temiz"])


def tam_ozet_oku(cikti, bugun):
    """--hizli: son tam özetin ilk satırındaki yorum JSON'u."""
    t = metin_oku(cikti, 1) or ""
    m = re.match(r"<!-- aylik-ozet: (\{.*\}) -->", t.strip())
    if not m:
        return kontrol("tam-ozet", "temiz", ["Tam özet henüz üretilmedi (python3 araclar/aylik-ozet.py)"])
    try:
        d = json.loads(m.group(1))
        z = datetime.fromisoformat(d["zaman"]).date()
    except (ValueError, KeyError, TypeError):
        return kontrol("tam-ozet", "temiz", ["Son tam özet okunamadı"])
    gun = (bugun - z).days
    satir = f"Son tam özet: {z.isoformat()} ({gun} gün önce) durum {d.get('durum', '?')}"
    return kontrol("tam-ozet", "dikkat" if gun > ESIK_DAL else "temiz", [satir + ("; 45 günden eski" if gun > ESIK_DAL else "")],
                   dikkat=[satir] if gun > ESIK_DAL else [])


def site_takip_kontrol(kok, bugun):
    """notlar/site-takip.md ilk satırındaki yorum JSON'u (araclar/site-takip.py yazar; ağsız okunur, K-57).
    DEĞİŞTİ / YENİ İÇERİK varsa karar; ERİŞİLEMEDİ varsa dikkat (kaynak KAYIP sayılmaz); rapor 45 günden eskiyse dikkat."""
    yol = Path(kok) / "notlar" / "site-takip.md"
    if not (Path(kok) / "site-takip.json").exists() and not yol.exists():
        return kontrol("site-takip", "temiz", ["Site skili yok"])
    ilk = (metin_oku(yol, 1) or "").strip()
    m = re.match(r"<!-- site-takip: (\{.*\}) -->$", ilk)
    if not m:
        return kontrol("site-takip", "temiz", ["Site takibi raporu henüz yok (python3 araclar/site-takip.py; aylık zincir de çalıştırır)"])
    try:
        d = json.loads(m.group(1))
        z = datetime.fromisoformat(d["zaman"]).date()
        say = d["sayilar"]
        degisti, yeni, erisilemedi = int(say.get("DEĞİŞTİ", 0)), int(say.get("YENİ İÇERİK", 0)), int(say.get("ERİŞİLEMEDİ", 0))
    except (ValueError, KeyError, TypeError):
        return kontrol("site-takip", "temiz", ["Site takibi raporu okunamadı (notlar/site-takip.md)"])
    gun = (bugun - z).days
    satir = (f"Site takibi {z.isoformat()} ({gun} gün önce): DEĞİŞTİ {degisti} · YENİ İÇERİK {yeni} · "
             f"ERİŞİLEMEDİ {erisilemedi} · AYNI {say.get('AYNI', 0)}")
    karar, dikkat = [], []
    if degisti or yeni:
        adlar = ", ".join((d.get("degisen") or [])[:ADAY_GOSTER])
        karar.append(f"Site takibi ({z.isoformat()}): {degisti} dosya değişti, {yeni} yeni içerik ({adlar}); siteden alınan skill "
                     "güncellensin mi? (notlar/site-takip.md, rehber/03 B3; onaysız güncellenmez)")
    if erisilemedi:
        dikkat.append(f"site takibi: {erisilemedi} adrese ulaşılamadı ({', '.join((d.get('erisilemeyen') or [])[:3])}); "
                      "geçici olabilir, sonraki ay yeniden denenir (kaynak KAYIP sayılmaz)")
    if gun > ESIK_RAPOR:
        dikkat.append(f"site takibi raporu {gun} gün eski (python3 araclar/site-takip.py)")
    return kontrol("site-takip", "dikkat" if dikkat else "temiz", [satir] + dikkat, karar, dikkat)


# ------------------------------------------------------------------ birleştirme ve çıktılar
def birlestir(kontroller, bugun, kok, hizli):
    karar_ham, say_sustur = [], 0
    sira = ["aylik-calisma", "bekleyen-dallar"]
    s = sorted(kontroller, key=lambda k: (sira.index(k["ad"]) if k["ad"] in sira else 2 if k["ad"] != "bekleyen-notlar" else 3))
    for k in s:
        for c in k["karar_bekleyen"]:
            if c not in karar_ham:
                karar_ham.append(c)
    kutular, ifadeler = kararlar_oku(kok)
    karar, say_sustur = sustur(karar_ham, ifadeler, bugun)
    for c in kutular:
        if c not in karar:
            karar.append(c)
    durum = max([k["durum"] for k in kontroller] + (["dikkat"] if karar else ["temiz"]), key=SIRA.get)
    return durum, karar, say_sustur


def ozet_metni(kontroller, durum, karar, bugun, hizli, damga_k, sustur_say):
    ad = {"temiz": "TEMİZ", "dikkat": "DİKKAT", "sorun": "SORUN"}[durum]
    dikkatler = [f"{k['ad']} ({k['durum']}): {x}" for k in kontroller if k["durum"] != "temiz" for x in ([dikkat_sebebi(k)] if k["dikkat_satirlar"] else [])]
    if hizli and durum == "temiz" and not karar and not dikkatler:
        son = damga_k.get("son")
        if son:
            return [f"Aylık özet (hızlı): her şey yolunda · son aylık çalışma {(bugun - son).days} gün önce ({damga_k.get('son_sonuc') or 'kayıtlı'})."]
        return ["Aylık özet (hızlı): her şey yolunda · aylık çalışma damgası yok (ilk kurulum ya da yeni makine)."]
    bas = f"Aylık özet (hızlı kontrol) — {bugun.isoformat()} · durum: {ad}" if hizli else f"Aylık özet — {bugun.isoformat()} · durum: {ad}"
    satir = [bas]
    son = damga_k.get("son")
    if damga_k.get("damga_var") and son:
        satir.append(f"Aylık çalışma: son çalışma {son.isoformat()} ({(bugun - son).days} gün önce){sonuc_eki(damga_k.get('son_sonuc'))}.")
    elif son:
        satir.append(f"Aylık çalışma: son kayıtlı güncelleme {son.isoformat()} ({(bugun - son).days} gün önce).")
    else:
        satir.append("Aylık çalışma: damga yok (ilk kurulum ya da yeni makine).")
    kn, dn = (3, 3) if hizli else (10, 8)
    if karar:
        satir.append(f"Senin kararını bekleyen {len(karar)} şey:")
        satir += [f"  {i}. {kirp(c)}" for i, c in enumerate(karar[:kn], 1)]
        if len(karar) > kn:
            satir.append(f"  … +{len(karar) - kn} daha: " + ("tamamı için python3 araclar/aylik-ozet.py" if hizli else "notlar/aylik-ozet.md"))
    else:
        satir.append("Senin kararını bekleyen bir şey yok.")
    if dikkatler:
        satir.append("Dikkat gerektirenler:")
        satir += [f"  • {kirp(x)}" for x in dikkatler[:dn]]
        if len(dikkatler) > dn:
            satir.append(f"  … +{len(dikkatler) - dn} daha: " + ("tamamı için python3 araclar/aylik-ozet.py" if hizli else "notlar/aylik-ozet.md"))
    else:
        satir.append("Dikkat gerektiren bir şey yok.")
    satir.append("Tam özet için: python3 araclar/aylik-ozet.py" if hizli else "Ayrıntı: notlar/aylik-ozet.md")
    return satir


def md_metni(kontroller, durum, karar, bugun, damga_k, sustur_say, zaman):
    ad = {"temiz": "TEMİZ", "dikkat": "DİKKAT", "sorun": "SORUN"}[durum]
    meta = {"zaman": zaman, "mod": "tam", "durum": durum, "araclar": {k["ad"]: k["durum"] for k in kontroller},
            "karar_sayisi": len(karar)}
    s = [f"<!-- aylik-ozet: {json.dumps(meta, ensure_ascii=False)} -->", "# Aylık Özet", "",
         f"> `araclar/aylik-ozet.py` üretir · {bugun.isoformat()} · tam modda rapor dosyalarını yeniler · git'e girmez (yerel). "
         "Hızlı kontrol: `python3 araclar/aylik-ozet.py --hizli`", "", f"## Durum: {ad}", "",
         f"## Senin kararını bekleyenler ({len(karar)})"]
    s += [f"{i}. {c}" for i, c in enumerate(karar, 1)] or ["Yok."]
    if sustur_say:
        s.append(f"\n({sustur_say} karar 'kabul edildi' listesi nedeniyle susturuldu: notlar/kararlar.md)")
    s += ["", "## Aylık çalışma"]
    son = damga_k.get("son")
    s.append(f"Son çalışma {son.isoformat()} ({(bugun - son).days} gün önce){sonuc_eki(damga_k.get('son_sonuc'))}" if son
             else "Damga yok (ilk kurulum ya da yeni makine).")
    s += ["", "## Kontroller", "| Kontrol | Durum | Özet |", "|---|---|---|"]
    for k in kontroller:
        s.append(f"| {k['ad']} | {k['durum']} | {(dikkat_sebebi(k) if k['durum'] != 'temiz' else (k['satirlar'][0] if k['satirlar'] else '-')).replace('|', '/')} |")
    for k in kontroller:
        s += ["", f"### {k['ad']}"] + [f"- {x}" for x in k["satirlar"]] + [f"- karar: {x}" for x in k["karar_bekleyen"]]
        for g in k.get("tam_liste") or []:
            if g:
                s.append(f"- tam aday listesi: {', '.join(g)}")
    ry = next((k for k in kontroller if k["ad"] == "rapor-yasi"), None)
    if ry:
        s += ["", "## Rapor yaşları", "| Rapor | Son tarih | Gün | Durum |", "|---|---|---|---|"]
        s += [f"| {a} | {t} | {g} | {d} |" for a, t, g, d in ry.get("tablo", [])]
    return "\n".join(s) + "\n"


def md_yaz(kok, cikti, metin):
    """0.1: dosya .gitignore'da değilse YAZMAZ. -> (yazildi, uyari)"""
    h = os.path.realpath(str(cikti))
    ev = os.path.realpath(str(Path.home()))
    yasak = [os.path.join(ev, d) for d in (".claude", ".agents", ".codex", ".gemini", ".cursor", ".copilot", ".openmontage", ".config", "Library")]
    yasak.append(os.path.join(ev, "Documents", "Claude"))
    if any(h == y or h.startswith(y + os.sep) for y in yasak):
        return False, "UYARI: --cikti araç klasörlerine ya da yedeklere yazamaz; aylık özet yazılmadı"
    r = git(kok, "check-ignore", "-q", str(cikti))
    if r.returncode == 1:
        return False, f"UYARI: {Path(cikti).relative_to(kok) if Path(cikti).is_relative_to(kok) else cikti} .gitignore'da değil; " \
                      "ağacı kirletmemek için yazılmadı (.gitignore satırı eksik)"
    try:
        Path(cikti).parent.mkdir(parents=True, exist_ok=True)
        Path(cikti).write_text(metin, encoding="utf-8")
    except OSError as e:
        return False, f"UYARI: aylık özet dosyası yazılamadı ({type(e).__name__})"
    return True, ""


def calis(a):
    kok = Path(a.kok).resolve()
    bugun = date.today()
    hizli = a.hizli or a.oturum
    cikti = Path(a.cikti) if a.cikti else kok / "notlar" / "aylik-ozet.md"
    zaman_asimi = HIZLI_ZAMAN_ASIMI if hizli else a.zaman_asimi
    liste = arac_listesi(kok, hizli, yaz=not a.yazmadan, liste_json=a.arac_listesi_json)
    once = kirli_yollar(kok)
    kontroller, pencere = araclari_kos(kok, liste, zaman_asimi, a.paralel)
    sonra = kirli_yollar(kok)
    # sözleşme: --ozet-json araçları yalnız izinli rapor yollarını yazabilir
    ihlaller = sorted(y for y in (sonra - once) if y not in IZINLI_RAPOR_YOLLARI)
    ihlal_k = []
    for yol in ihlaller:
        try:
            mt = (kok / yol).stat().st_mtime
        except OSError:
            mt = None
        supheli = [ad for ad, (t0, t1) in pencere.items() if mt is not None and t0 <= mt <= t1]  # çalışma penceresi yazma anını kapsayan araçlar
        if not supheli and mt is not None and pencere:  # saat inceliği: en yakın pencere
            supheli = [min(pencere, key=lambda ad: min(abs(mt - pencere[ad][0]), abs(mt - pencere[ad][1])))]
        supheli = supheli or [ad for ad, _ in liste]
        satir = f"UYARI: {', '.join(supheli)} --ozet-json ile dosya yazdı: {yol} (sözleşme ihlali)"
        for k in kontroller:
            if k["ad"] in supheli and len(supheli) <= 2:
                k["satirlar"].insert(0, satir)
                k["dikkat_satirlar"].insert(0, satir)
                if k["durum"] == "temiz":
                    k["durum"] = "dikkat"
        ihlal_k.append(satir)
    extra = []
    dk = damga_kontrol(kok, bugun)
    extra += [dk, dal_kontrol(kok, bugun), site_takip_kontrol(kok, bugun)]
    if hizli:
        if not any(k["ad"] == "git-durum" and k["calisti"] for k in kontroller):
            extra.append(yerel_git(kok))
        extra.append(tam_ozet_oku(cikti, bugun))
    else:
        extra.append(rapor_yasi(kok, bugun))
        extra.append(gorev_kopyasi_kontrol(kok, a.gorev_yolu))
        if not a.yazmadan:
            yeni = sonra
            if yeni and all(y in RAPOR_NOTLARI for y in yeni):
                adlar = " ".join(sorted(yeni))
                extra.append(kontrol("rapor-dosyalari", "dikkat", [f"Rapor dosyaları yenilendi: {adlar}"],
                                     [f"Rapor dosyaları yenilendi ({', '.join(sorted(yeni))}): kaydedilsin mi? "
                                      f"(git add {adlar} && git commit; onayınla)"]))
            elif yeni:
                extra.append(kontrol("rapor-dosyalari", "temiz", [f"Kütüphanede kaydedilmemiş değişiklik: {len(yeni)} dosya"]))
    if ihlal_k and not any(k["durum"] != "temiz" and any("sözleşme ihlali" in x for x in k["satirlar"]) for k in kontroller):
        extra.append(kontrol("sozlesme", "dikkat", ihlal_k))
    tum = kontroller + extra
    tum.append(bekleyen_notlar(kok, tum, {ad for ad, _ in liste}))
    durum, karar, sustur_say = birlestir(tum, bugun, kok, hizli)
    satirlar = ozet_metni(tum, durum, karar, bugun, hizli, dk, sustur_say)
    yazma_uyari = ""
    if not hizli:
        zaman = datetime.now().astimezone().isoformat(timespec="seconds")
        ok, yazma_uyari = md_yaz(kok, cikti, md_metni(tum, durum, karar, bugun, dk, sustur_say, zaman))
        if yazma_uyari:
            tum.append(kontrol("ozet-dosyasi", "dikkat", [yazma_uyari]))
            durum = max(durum, "dikkat", key=SIRA.get)
            satirlar = ozet_metni(tum, durum, karar, bugun, hizli, dk, sustur_say)
    return durum, satirlar, karar


def main(argv=None):
    ap = argparse.ArgumentParser(description="Aylık özet (salt okuma)")
    ap.add_argument("--hizli", action="store_true", help="ucuz oturum başı kontrolü: ağ yok, yazma yok, <= 15 satır")
    ap.add_argument("--oturum", action="store_true", help="--hizli takma adı")
    ap.add_argument("--yazmadan", action="store_true", help="tam mod ama proje-kullanimi'na --yaz verme")
    ap.add_argument("--ozet-json", action="store_true", help="stdout'a tek JSON nesnesi")
    ap.add_argument("--siki", action="store_true", help="durum 'sorun' ise çıkış kodu 1")
    ap.add_argument("--kok", default=str(Path(__file__).resolve().parent.parent), help=argparse.SUPPRESS)
    ap.add_argument("--cikti", default=None, help=argparse.SUPPRESS)
    ap.add_argument("--zaman-asimi", type=int, default=180, help=argparse.SUPPRESS)
    ap.add_argument("--gorev-yolu", default=str(CANLI_GOREV), help=argparse.SUPPRESS)
    ap.add_argument("--paralel", type=int, default=4, help=argparse.SUPPRESS)
    ap.add_argument("--arac-listesi-json", default=None, help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    try:
        durum, satirlar, karar = calis(a)
    except Exception as e:  # noqa: BLE001  hiçbir koşulda Traceback basılmaz
        durum, satirlar, karar = "dikkat", [f"UYARI: aylık özet tamamlanamadı: {type(e).__name__}: {kirp(e, 150)}"], []
    if a.ozet_json:
        print(json.dumps({"arac": "aylik-ozet", "durum": durum, "satirlar": satirlar, "karar_bekleyen": karar}, ensure_ascii=False))
    else:
        print("\n".join(satirlar))
    return 1 if a.siki and durum == "sorun" else 0


if __name__ == "__main__":
    sys.exit(main())
