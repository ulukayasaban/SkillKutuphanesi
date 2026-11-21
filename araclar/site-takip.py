#!/usr/bin/env python3
"""Site takibi: GitHub'da olmayan, bir web sitesinden alınmış skillerin (yerel kaynak `yerel/site`, tip T8, klasör `site/<ad>/`)
kaynak sitesi değişti mi? Kayıt `site-takip.json` (skill başına sahip, lisans, site ve izlenen dosyaların sha256'sı; K-57).

  python3 araclar/site-takip.py                 # tüm site skilleri: her adres için AYNI / DEĞİŞTİ / YENİ İÇERİK / ERİŞİLEMEDİ
  python3 araclar/site-takip.py --skill stil    # yalnız bir skill (rapor dosyası yazılmaz: rapor her zaman bütün site skilleri)
  python3 araclar/site-takip.py --yazmadan      # rapor dosyası yazılmaz, yalnız ekrana basar
  python3 araclar/site-takip.py --indir         # değişen/yeni dosyaları kütüphane DIŞINA indirir:
                                                #   ~/Documents/Claude/deneme/site-takip-<tarih>/<skill>/
  python3 araclar/site-takip.py --siki          # DEĞİŞTİ ya da YENİ İÇERİK varsa çıkış 1
  python3 araclar/site-takip.py --kayit-denetle # yalnız kayıt şeması ve zorunluluklar (ağsız)

Rapor `notlar/site-takip.md` (git'e girmez; ilk satırındaki yorum JSON'unu aylik-ozet.py okur). Yalnız GET, zaman aşımlı, genel bir
User-Agent; istekte kullanıcı bilgisi yoktur. `site/`, `kendi/` ve `arsiv/` içine HİÇ yazmaz; `site-takip.json`'u değiştirmez.
Skilin güncellenmesi her seferinde kullanıcı onayıyla, rehber/03 B3 adımlarıyla elle yapılır. Ağ yoksa ya da site düştüyse sonuç
ERİŞİLEMEDİ olur; kaynak KAYIP sayılmaz. Çıkış: 0 (dört sonucun hepsi), 1 (--siki ve değişiklik), 2 (kayıt hatası).
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, SITE_TAKIP  # noqa: E402

RAPOR = KOK / "notlar" / "site-takip.md"
USER_AGENT = "Mozilla/5.0 (compatible; site-takip/1.0)"
AZAMI_BAYT = 20 * 1024 * 1024
AZAMI_YONLENDIRME = 5
DURUMLAR = ("AYNI", "DEĞİŞTİ", "YENİ İÇERİK", "ERİŞİLEMEDİ")
TURLER = ("asil", "yonlendirme")
KARSILASTIRMALAR = ("tam", "onek")
SKILL_ALANLARI = ("skill", "kaynak", "yerel", "site", "sahip", "sahip_tipi", "sahip_url", "lisans", "resmi_kaynak", "kayit_tarihi",
                  "not", "dosyalar")
DOSYA_ALANLARI = ("ad", "url", "tur", "bayt", "sha256", "karsilastirma", "yerel_dosya", "etkiler", "not")
ZORUNLU_SKILL = ("skill", "kaynak", "yerel", "site", "sahip", "lisans", "dosyalar")
ZORUNLU_DOSYA = ("ad", "url", "tur", "bayt", "sha256")


# ------------------------------------------------------------------ kayıt şeması (dogrula.py da bunu kullanır)
def _sha(veri: bytes) -> str:
    return hashlib.sha256(veri).hexdigest()


def kayit_denetle(veri, kok=KOK, kaynaklar=None):
    """site-takip.json şeması ve zorunlulukları -> (hatalar, uyarilar). Ağ kullanmaz.
    HATA: yapı bozuk; site/<ad>/SKILL.md'nin kaydı yok; kayıt kendi/ altındaki bir skili gösteriyor (yanlış yer: site skili site/'ye).
    UYARI: bilinmeyen alan; kayıttaki skill site/ altında yok; yerel kopya kayıttaki özetle uyuşmuyor."""
    kok = Path(kok)
    h, u = [], []
    if kaynaklar is None:
        try:
            kaynaklar = json.loads((kok / "kaynaklar.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            kaynaklar = {}
    site_kaynak = [k for k in (kaynaklar.get("repolar") or []) if isinstance(k, dict) and k.get("tur") == "site"]
    site_kok = {k.get("yerel") or "site" for k in site_kaynak} or {"site"}
    diskte = sorted({p.parent.name: p for d in site_kok for p in (kok / d).glob("*/SKILL.md")})
    if veri is None:
        if diskte:
            h.append(f"{SITE_TAKIP} yok ama site skili var ({', '.join(diskte)}): her site/<ad>/ için takip kaydı zorunlu (rehber/03 B3)")
        return h, u
    if not isinstance(veri, dict) or veri.get("surum") != 1 or not isinstance(veri.get("skiller"), list):
        return [f"{SITE_TAKIP}: 'surum': 1 ve 'skiller' listesi olmalı"], u
    gorulen = set()
    for i, s in enumerate(veri["skiller"], 1):
        if not isinstance(s, dict):
            h.append(f"{SITE_TAKIP}: skill kaydı {i} sözlük değil")
            continue
        ad = s.get("skill")
        etiket = f"{SITE_TAKIP}: {ad or i}"
        eksik = [a for a in ZORUNLU_SKILL if not s.get(a)]
        if eksik:
            h.append(f"{etiket}: eksik alan: {', '.join(eksik)}")
        yabanci = [a for a in s if a not in SKILL_ALANLARI and not a.startswith("_")]
        if yabanci:
            u.append(f"{etiket}: bilinmeyen alan: {', '.join(yabanci)}")
        if ad in gorulen:
            h.append(f"{etiket}: skill iki kez kayıtlı")
        gorulen.add(ad)
        yerel = str(s.get("yerel") or "")
        if yerel.startswith("kendi/") or yerel == "kendi":
            h.append(f"{etiket}: kayıt kendi/ altındaki bir skili gösteriyor ({yerel}); siteden alınan skill site/<ad>/ altında durur, "
                     "kendi/ yalnız kullanıcının kendi yazdığı skiller içindir (K-57)")
        elif yerel and not any(yerel == f"{d}/{ad}" for d in site_kok):
            h.append(f"{etiket}: 'yerel' {yerel!r} olmalı: site/{ad}")
        if s.get("kaynak") and s["kaynak"] not in {k.get("repo") for k in site_kaynak}:
            h.append(f"{etiket}: kaynak {s['kaynak']!r} kaynaklar.json'da site kaydı değil")
        if s.get("site") and not str(s["site"]).startswith("https://"):
            h.append(f"{etiket}: site https:// ile başlamalı")
        if "resmi_kaynak" in s and not isinstance(s["resmi_kaynak"], bool):
            u.append(f"{etiket}: resmi_kaynak true/false olmalı")
        if s.get("sahip_tipi") and s["sahip_tipi"] not in ("kisi", "kurum"):
            u.append(f"{etiket}: sahip_tipi 'kisi' ya da 'kurum' olmalı")
        klasor = kok / yerel if yerel else None
        if klasor is not None and not (klasor / "SKILL.md").is_file():
            u.append(f"{etiket}: {yerel}/SKILL.md yok (skill taşındı ya da çıkarıldı mı? kayıt artık kalmasın)")
        dosyalar = s.get("dosyalar")
        if not isinstance(dosyalar, list) or not dosyalar:
            h.append(f"{etiket}: 'dosyalar' boş olmayan liste olmalı")
            continue
        adlar = set()
        for f in dosyalar:
            if not isinstance(f, dict):
                h.append(f"{etiket}: dosya kaydı sözlük değil")
                continue
            fe = f"{etiket}/{f.get('ad', '?')}"
            eksik = [a for a in ZORUNLU_DOSYA if a not in f]
            if eksik:
                h.append(f"{fe}: eksik alan: {', '.join(eksik)}")
            yabanci = [a for a in f if a not in DOSYA_ALANLARI]
            if yabanci:
                u.append(f"{fe}: bilinmeyen alan: {', '.join(yabanci)}")
            if f.get("ad") in adlar:
                h.append(f"{fe}: dosya adı tekrarlanıyor")
            adlar.add(f.get("ad"))
            if "url" in f and not str(f["url"]).startswith("https://"):
                h.append(f"{fe}: url https:// ile başlamalı")
            if "tur" in f and f["tur"] not in TURLER:
                h.append(f"{fe}: tur {', '.join(TURLER)} olmalı")
            if "sha256" in f and not re.fullmatch(r"[0-9a-f]{64}", str(f["sha256"])):
                h.append(f"{fe}: sha256 64 haneli küçük harf onaltılık olmalı")
            if "bayt" in f and (isinstance(f["bayt"], bool) or not isinstance(f["bayt"], int) or f["bayt"] < 0):
                h.append(f"{fe}: bayt sıfır ya da pozitif tam sayı olmalı")
            kar = f.get("karsilastirma", "tam")
            if kar not in KARSILASTIRMALAR:
                h.append(f"{fe}: karsilastirma {', '.join(KARSILASTIRMALAR)} olmalı")
            yd = f.get("yerel_dosya")
            if kar == "onek" and not yd:
                h.append(f"{fe}: karsilastirma 'onek' için yerel_dosya gerekir")
            if f.get("tur") == "yonlendirme" and yd:
                u.append(f"{fe}: yönlendirme kaydında yerel_dosya olmaz")
            if yd:
                if ".." in Path(yd).parts or Path(yd).is_absolute():
                    h.append(f"{fe}: yerel_dosya skill klasörüne göreli olmalı")
                elif klasor is not None and (klasor / yd).is_file():
                    if yerel_ozeti(klasor / yd, kar, f.get("bayt")) != f.get("sha256"):
                        u.append(f"{fe}: yerel kopya {yerel}/{yd} kayıttaki özetle uyuşmuyor (dosya elle mi değişti, kayıt mı eski?)")
                elif klasor is not None and (klasor / "SKILL.md").is_file():
                    u.append(f"{fe}: yerel_dosya yok: {yerel}/{yd}")
    for ad in diskte:
        if ad not in gorulen:
            h.append(f"site/{ad}: {SITE_TAKIP} kaydı yok; her site skili için takip kaydı zorunlu (rehber/03 B3)")
    return h, u


def yerel_ozeti(dosya: Path, karsilastirma, bayt):
    veri = Path(dosya).read_bytes()
    return _sha(veri[:bayt] if karsilastirma == "onek" and isinstance(bayt, int) else veri)


def kayit_oku(kok=KOK):
    """-> (veri | None, okuma_hatasi | '')"""
    f = Path(kok) / SITE_TAKIP
    if not f.is_file():
        return None, ""
    try:
        return json.loads(f.read_text(encoding="utf-8")), ""
    except (OSError, ValueError) as e:
        return None, f"{SITE_TAKIP} okunamadı: {str(e)[:100]}"


# ------------------------------------------------------------------ HTTP (yalnız GET)
class _Takipsiz(urllib.request.HTTPRedirectHandler):
    """Yönlendirmeyi kendiliğinden izleme: 3xx yanıtı olduğu gibi görülür (yönlendirme kaydı bunu bilmek ister)."""
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401
        return None


_ACICI = urllib.request.build_opener(_Takipsiz)


def _ac(istek, zaman_asimi):
    """Tek nokta: testler bunu sahte HTTP ile değiştirir."""
    return _ACICI.open(istek, timeout=zaman_asimi)


def getir(url, zaman_asimi):
    """Tek GET -> {"kod": int|None, "govde": bytes|None, "konum": str|None, "hata": str}. Hata gövdesi de okunur (özet için)."""
    istek = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with _ac(istek, zaman_asimi) as y:
            govde = y.read(AZAMI_BAYT + 1)
            return {"kod": getattr(y, "status", None) or y.getcode(), "govde": govde, "konum": None, "hata": ""}
    except urllib.error.HTTPError as e:
        try:
            govde = e.read(AZAMI_BAYT + 1)
        except Exception:  # noqa: BLE001
            govde = b""
        konum = e.headers.get("Location") if e.headers else None
        return {"kod": e.code, "govde": govde, "konum": urllib.parse.urljoin(url, konum) if konum else None, "hata": f"HTTP {e.code}"}
    except (urllib.error.URLError, OSError, ValueError) as e:
        neden = getattr(e, "reason", e)
        return {"kod": None, "govde": None, "konum": None, "hata": f"{type(e).__name__}: {str(neden)[:120]}"}


def dosya_kontrol(f, zaman_asimi, yonlendirme_ozetleri=()):
    """Bir izlenen adres -> sonuç sözlüğü {durum, kod, bayt, sha256, not, govde}."""
    url, tur = f["url"], f.get("tur", "asil")
    notlar = []
    y = getir(url, zaman_asimi)
    if tur == "asil":
        atlama = 0
        while y["kod"] in (301, 302, 303, 307, 308) and y["konum"] and atlama < AZAMI_YONLENDIRME:
            notlar.append(f"yönlendiriliyor: {y['konum']}")
            y = getir(y["konum"], zaman_asimi)
            atlama += 1
    kod, govde = y["kod"], y["govde"]
    sonuc = {"kod": kod, "bayt": len(govde) if govde is not None else None, "sha256": _sha(govde) if govde is not None else None,
             "govde": govde}
    if kod is None:
        return dict(sonuc, durum="ERİŞİLEMEDİ", not_="; ".join(notlar + [y["hata"] or "yanıt yok"]))
    if govde is not None and len(govde) > AZAMI_BAYT:
        return dict(sonuc, durum="DEĞİŞTİ", not_="; ".join(notlar + [f"yanıt {AZAMI_BAYT // 1048576} MB'tan büyük"]), govde=None)
    ayni = sonuc["sha256"] == f["sha256"]
    if tur == "yonlendirme":
        if ayni:
            return dict(sonuc, durum="AYNI", not_="yönlendirme, gerçek dosya değil (gövde kayıttakiyle aynı)")
        if 300 <= kod < 400:
            return dict(sonuc, durum="AYNI", not_=f"yönlendirme, gerçek dosya değil (HTTP {kod} → {y['konum'] or '?'})")
        if 200 <= kod < 300:
            return dict(sonuc, durum="YENİ İÇERİK", not_="yönlendirme yerine gerçek içerik geldi: yeni dosya olabilir")
        return dict(sonuc, durum="ERİŞİLEMEDİ", not_=f"HTTP {kod}")
    if 200 <= kod < 300:
        if ayni:
            return dict(sonuc, durum="AYNI", not_="; ".join(notlar))
        if sonuc["sha256"] in yonlendirme_ozetleri:
            return dict(sonuc, durum="DEĞİŞTİ", not_="; ".join(notlar + ["dosya artık yönlendirme sayfası: kaldırılmış olabilir"]))
        return dict(sonuc, durum="DEĞİŞTİ", not_="; ".join(notlar))
    if 300 <= kod < 400:
        return dict(sonuc, durum="ERİŞİLEMEDİ", not_="; ".join(notlar + [f"çok fazla yönlendirme (HTTP {kod})"]))
    ek = " (dosya kaldırılmış olabilir; kaynak KAYIP sayılmaz)" if kod in (404, 410) else ""
    if ayni:  # bazı siteler gerçek dosyayı hata koduyla verir: gövde aynıysa dosya aynıdır
        return dict(sonuc, durum="AYNI", not_=f"HTTP {kod} ama gövde kayıttakiyle aynı")
    return dict(sonuc, durum="ERİŞİLEMEDİ", not_=f"HTTP {kod}{ek}")


# ------------------------------------------------------------------ çalıştırma ve rapor
def skill_kontrol(s, kok, zaman_asimi):
    yon = {f["sha256"] for f in s["dosyalar"] if f.get("tur") == "yonlendirme"}
    klasor = Path(kok) / s["yerel"]
    satirlar = []
    for f in s["dosyalar"]:
        r = dosya_kontrol(f, zaman_asimi, yon)
        yerel = "-"
        if f.get("yerel_dosya"):
            yd = klasor / f["yerel_dosya"]
            if not yd.is_file():
                yerel = "YOK"
            else:
                yerel = "uyumlu" if yerel_ozeti(yd, f.get("karsilastirma", "tam"), f.get("bayt")) == f["sha256"] else "FARKLI"
        satirlar.append({"ad": f["ad"], "url": f["url"], "tur": f.get("tur", "asil"), "durum": r["durum"], "kod": r["kod"],
                         "bayt_kayit": f.get("bayt"), "bayt": r["bayt"], "sha256": r["sha256"], "not": r["not_"],
                         "yerel": yerel, "yerel_dosya": f.get("yerel_dosya"), "karsilastirma": f.get("karsilastirma", "tam"),
                         "etkiler": f.get("etkiler") or [], "govde": r["govde"]})
    return satirlar


def sayilar(satirlar):
    return {d: sum(1 for x in satirlar if x["durum"] == d) for d in DURUMLAR}


def _git_yoksayiyor(yol, kok):
    """notlar/site-takip.md .gitignore'da mı? Git deposu değilse (test) True."""
    try:
        r = subprocess.run(["git", "-C", str(kok), "check-ignore", "-q", str(yol)], capture_output=True, timeout=10)
        return r.returncode != 1
    except (OSError, subprocess.SubprocessError):
        return True


def rapor_metni(sonuclar, kayit, zaman):
    tum = [x for _, ss in sonuclar for x in ss]
    say = sayilar(tum)
    degisen = [f"{ad}: {x['ad']} {x['durum']}" for ad, ss in sonuclar for x in ss if x["durum"] in ("DEĞİŞTİ", "YENİ İÇERİK")]
    erisilemeyen = [f"{ad}: {x['ad']}" for ad, ss in sonuclar for x in ss if x["durum"] == "ERİŞİLEMEDİ"]
    meta = {"zaman": zaman, "sayilar": say, "skiller": {ad: sayilar(ss) for ad, ss in sonuclar}, "degisen": degisen,
            "erisilemeyen": erisilemeyen}
    s = [f"<!-- site-takip: {json.dumps(meta, ensure_ascii=False)} -->", "# Site takibi", "",
         f"> `araclar/site-takip.py` üretir · {zaman[:10]} · git'e girmez (yerel rapor) · kayıt `{SITE_TAKIP}` · "
         "güncelleme yalnız kullanıcı onayıyla, rehber/03 B3", "",
         f"**Özet:** AYNI {say['AYNI']} · DEĞİŞTİ {say['DEĞİŞTİ']} · YENİ İÇERİK {say['YENİ İÇERİK']} · ERİŞİLEMEDİ {say['ERİŞİLEMEDİ']}", ""]
    for ad, ss in sonuclar:
        k = kayit.get(ad, {})
        s += [f"## {ad} — {k.get('site', '?')}", "",
              f"Sahip: {k.get('sahip', '?')} · lisans: {k.get('lisans', '?')} · klasör: `{k.get('yerel', '?')}` · kayıt tarihi: {k.get('kayit_tarihi', '?')}", "",
              "| Dosya | Tür | Durum | HTTP | Bayt (kayıt → site) | Yerel kopya | Not |", "|---|---|---|---|---|---|---|"]
        for x in ss:
            yerel = x["yerel"] if x["yerel"] == "-" else f"{x['yerel']} (`{x['yerel_dosya']}`, {x['karsilastirma']})"
            s.append(f"| {x['ad']} | {x['tur']} | **{x['durum']}** | {x['kod'] or '-'} | {x['bayt_kayit']} → {x['bayt'] if x['bayt'] is not None else '-'} | "
                     f"{yerel} | {(x['not'] or '').replace('|', '/')} |")
        ds = [x for x in ss if x["durum"] in ("DEĞİŞTİ", "YENİ İÇERİK")]
        if ds:
            s += ["", "Sitede görülen yeni özetler (kullanıcı onaylayıp skili güncelledikten SONRA site-takip.json'a yazılır):", "",
                  "| Dosya | Bayt | sha256 | Etkilenebilecek yerel dosyalar |", "|---|---|---|---|"]
            s += [f"| {x['ad']} | {x['bayt']} | `{x['sha256']}` | {', '.join(x['etkiler']) or (x['yerel_dosya'] or '-')} |" for x in ds]
        if any(x["yerel"] in ("FARKLI", "YOK") for x in ss):
            s += ["", "UYARI: yerel kopya kayıttaki özetle uyuşmuyor (site/ elle değişti ya da kayıt eski); site-takip.json ile site/ eşitlenmeli."]
        s.append("")
    s += ["## Ne yapılır", "",
          "- **AYNI:** bir şey yapılmaz. Yönlendirme satırları sitenin ana sayfaya yönlendiren adresleridir, gerçek dosya değildir.",
          "- **DEĞİŞTİ / YENİ İÇERİK:** kullanıcıya sorulur. Onay gelirse `python3 araclar/site-takip.py --indir` ile dosyalar kütüphane "
          "dışına iner, farkı okunur, skill rehber/03 B3 adımlarıyla elle güncellenir, sonra site-takip.json özetleri yenilenir.",
          "- **ERİŞİLEMEDİ:** ağ ya da site geçici olarak yanıt vermedi. Kaynak KAYIP sayılmaz; sonraki ay yeniden denenir.", ""]
    return "\n".join(s), meta


def indir(sonuclar, kok, bugun):
    """DEĞİŞTİ / YENİ İÇERİK dosyalarını ~/Documents/Claude/deneme/site-takip-<tarih>[-n]/<skill>/ altına yazar (yeni, boş klasör).
    Kütüphanenin içine asla yazmaz; dosyalar çalıştırılmaz. -> (klasör | None, mesaj)"""
    secilen = [(ad, x) for ad, ss in sonuclar for x in ss if x["durum"] in ("DEĞİŞTİ", "YENİ İÇERİK") and x["govde"] is not None]
    if not secilen:
        return None, "İndirilecek değişen dosya yok."
    taban = Path.home() / "Documents" / "Claude" / "deneme"
    hedef, n = taban / f"site-takip-{bugun}", 2
    while hedef.exists():
        hedef, n = taban / f"site-takip-{bugun}-{n}", n + 1
    kok_r = os.path.realpath(str(kok))
    h_r = os.path.realpath(str(hedef.parent))
    if h_r == kok_r or h_r.startswith(kok_r + os.sep):
        return None, f"DURDU: indirme klasörü kütüphanenin içinde olamaz ({hedef})"
    ozet = []
    for ad, x in secilen:
        klasor = hedef / re.sub(r"[^\w.-]", "_", ad)
        klasor.mkdir(parents=True, exist_ok=True)
        yol = urllib.parse.urlparse(x["url"]).path
        dosya_adi = re.sub(r"[^\w.-]", "_", Path(yol).name or "index.html")
        if (klasor / dosya_adi).exists():
            dosya_adi = re.sub(r"[^\w.-]", "_", x["ad"]) + "--" + dosya_adi
        (klasor / dosya_adi).write_bytes(x["govde"])
        ozet.append({"skill": ad, "ad": x["ad"], "url": x["url"], "durum": x["durum"], "bayt": x["bayt"], "sha256": x["sha256"],
                     "dosya": f"{klasor.name}/{dosya_adi}"})
    (hedef / "OZETLER.json").write_text(json.dumps(ozet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return hedef, f"{len(ozet)} dosya indirildi: {hedef} (kütüphane dışında; çalıştırma, yalnız oku)"


def calistir(argv=None, kok=None):
    ap = argparse.ArgumentParser(description="Site skillerinin kaynak sitesi değişti mi (yalnız GET)")
    ap.add_argument("--skill")
    ap.add_argument("--yazmadan", action="store_true")
    ap.add_argument("--indir", action="store_true")
    ap.add_argument("--siki", action="store_true")
    ap.add_argument("--kayit-denetle", action="store_true")
    a = ap.parse_args(argv)
    kok = Path(kok or KOK)
    veri, okuma = kayit_oku(kok)
    if okuma:
        print(f"HATA: {okuma}")
        return 2
    h, u = kayit_denetle(veri, kok)
    for x in h:
        print(f"HATA: {x}")
    for x in u:
        print(f"UYARI: {x}")
    if a.kayit_denetle:
        print(f"Kayıt denetimi: {len(h)} hata, {len(u)} uyarı")
        return 2 if h else 0
    if h:
        print("Kayıt hatalı: takip yapılmadı (site-takip.json'u düzelt).")
        return 2
    if veri is None or not veri["skiller"]:
        print("Site skili yok: takip edilecek bir şey yok.")
        return 0
    skiller = [s for s in veri["skiller"] if not a.skill or s["skill"] == a.skill]
    if a.skill and not skiller:
        print(f"HATA: {a.skill} site-takip.json'da yok")
        return 2
    zaman_asimi = veri.get("zaman_asimi_sn") if isinstance(veri.get("zaman_asimi_sn"), (int, float)) else 30
    kayit = {s["skill"]: s for s in skiller}
    sonuclar = []
    for s in skiller:
        print(f"{s['skill']}: {s['site']} ({len(s['dosyalar'])} adres)")
        ss = skill_kontrol(s, kok, zaman_asimi)
        for x in ss:
            print(f"  {x['durum']:<12} {x['ad']:<16} HTTP {x['kod'] or '-'}  {x['bayt'] if x['bayt'] is not None else '-'} bayt"
                  + (f"  yerel {x['yerel']}" if x["yerel"] != "-" else "") + (f"  ({x['not']})" if x["not"] else ""))
        sonuclar.append((s["skill"], ss))
    zaman = datetime.now().astimezone().isoformat(timespec="seconds")
    metin, meta = rapor_metni(sonuclar, kayit, zaman)
    say = meta["sayilar"]
    print(f"Site takibi: AYNI {say['AYNI']} · DEĞİŞTİ {say['DEĞİŞTİ']} · YENİ İÇERİK {say['YENİ İÇERİK']} · ERİŞİLEMEDİ {say['ERİŞİLEMEDİ']}")
    if not a.yazmadan and not a.skill:
        rapor = kok / "notlar" / "site-takip.md"
        if _git_yoksayiyor(rapor, kok):
            rapor.parent.mkdir(parents=True, exist_ok=True)
            rapor.write_text(metin + "\n", encoding="utf-8")
            print(f"Rapor: {rapor.relative_to(kok)}")
        else:
            print("UYARI: notlar/site-takip.md .gitignore'da değil; ağacı kirletmemek için yazılmadı")
    if a.indir:
        _, mesaj = indir(sonuclar, kok, date.today().isoformat())
        print(mesaj)
    if say["DEĞİŞTİ"] or say["YENİ İÇERİK"]:
        print("Değişiklik var: skill kendiliğinden güncellenmez; kullanıcıya sor (rehber/03 B3).")
    return 1 if a.siki and (say["DEĞİŞTİ"] or say["YENİ İÇERİK"]) else 0


def rapor_oku(kok=KOK):
    """notlar/site-takip.md ilk satırındaki yorum JSON'u (aylik-ozet.py ağsız okur). Yoksa ya da bozuksa None."""
    try:
        with open(Path(kok) / "notlar" / "site-takip.md", encoding="utf-8") as f:
            ilk = f.readline().strip()
        m = re.match(r"<!-- site-takip: (\{.*\}) -->$", ilk)
        return json.loads(m.group(1)) if m else None
    except (OSError, ValueError):
        return None


if __name__ == "__main__":
    sys.exit(calistir())
