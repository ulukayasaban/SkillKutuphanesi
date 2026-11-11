#!/usr/bin/env python3
"""Kütüphane dışındaki yedeklerin denetimi (salt okuma).

Hiçbir şeyi silmez, taşımaz, kopyalamaz; dosya içeriği açılmaz (yalnız ad, boyut, izin, tarih okunur);
gizli değer yazdırılmaz. Envanter: yedekler.json (rehber/13-yedek-ve-geri-alma.md).

Çıkış kodu: 0 = araç doğru çalıştı (ne bulursa bulsun); 1 = yalnız --siki ile ve durum "sorun" ise; 2 = kullanım hatası.

Kullanım:
  python3 araclar/yedek-denetim.py              # tablo ve bulgular
  python3 araclar/yedek-denetim.py --kisa       # tek satır / yalnız dikkat-sorun
  python3 araclar/yedek-denetim.py --ozet-json  # tek JSON nesnesi
  python3 araclar/yedek-denetim.py --rapor      # notlar/yedek-durumu.md yazar
"""
import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, GLOBAL_KLASORLER, json_oku  # noqa: E402

VARSAYILAN_KAYIT = KOK / "yedekler.json"
TURLER = ("ayar-dosyasi", "genel-skill-klasoru", "program", "proje", "kutuphane-dali", "git-paketi", "diger")
ZORUNLU = ("kimlik", "yol", "tur", "ne", "tarih", "geri_yukleme", "gizli_icerir")
YAS_UYARI_GUN = 90
YAS_UYARI_GUN_GIZLI = 30
GIT_PAKETI_GUN = 90
BOYUT_TARAMA_SINIRI = 20000
SEVIYE_SIRA = {"sorun": 0, "dikkat": 1, "bilgi": 2}
# Bilinen yedek adı kalıpları: kayıtsız olsa da türü söylenir.
BILINEN_AD_KALIPLARI = [
    (re.compile(r"^genel-klasorler-\d{4}-\d{2}-\d{2}(-\d+)?$"), "genel skill klasörü boşaltma yedeği"),
    (re.compile(r"^geri-yazilan-\d{4}-\d{2}-\d{2}(-\d+)?$"), "geri yazılan genel skill yedeği"),
    (re.compile(r"^ayar-\d{4}-\d{2}-\d{2}(-\d+)?$"), "ayar dosyası yedeği"),
    (re.compile(r"^[\w.]+(?:-[\w.]+)*-\d{4}-\d{2}-\d{2}(-\d+)?$"), "program ya da başka yedek"),
]


def tarama_klasorleri():
    return [Path(p) for p in GLOBAL_KLASORLER.values()] + [Path.home() / ".openmontage"]


def yol_ac(s):
    return Path(str(s)).expanduser()


def kayit_oku(yol):
    try:
        yol = Path(yol)
        if not yol.exists():
            return None, "yedekler.json bulunamadı"
        veri = json_oku(yol)
        if not isinstance(veri, dict) or not isinstance(veri.get("yedekler", []), list):
            return None, "yedekler.json bozuk: beklenen yapı yok"
        return veri, None
    except (ValueError, OSError) as e:
        return None, f"yedekler.json bozuk: {str(e)[:100]}"


def boyut(yol):
    """(bayt, kesildi): yalnız os.scandir ile gezer, dosya açmaz, bağları izlemez."""
    toplam, sayac = 0, 0
    yigin = [str(yol)]
    while yigin:
        d = yigin.pop()
        try:
            with os.scandir(d) as it:
                for e in it:
                    sayac += 1
                    if sayac > BOYUT_TARAMA_SINIRI:
                        return toplam, True
                    try:
                        if e.is_symlink():
                            continue
                        if e.is_dir(follow_symlinks=False):
                            yigin.append(e.path)
                        elif e.is_file(follow_symlinks=False):
                            toplam += e.stat(follow_symlinks=False).st_size
                    except OSError:
                        pass
        except OSError:
            pass
    return toplam, False


def mb(bayt):
    return f"{bayt / 1048576:.1f}"


def _gevsek_izin_var(yol):
    """Gizli içerikli yedekte grup/diğer okuyabiliyor mu (POSIX). Windows'ta sessizce False."""
    try:
        yol = Path(yol)
        yigin = [str(yol)]
        sayac = 0
        while yigin:
            d = yigin.pop()
            if os.path.islink(d):
                continue
            sayac += 1
            if sayac > BOYUT_TARAMA_SINIRI:
                break
            st = os.lstat(d)
            if os.path.isdir(d):
                with os.scandir(d) as it:
                    yigin += [e.path for e in it]
            elif st.st_mode & 0o077:
                return True
    except (OSError, AttributeError):
        pass
    return False


def _tarih(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _icinde(yol, ust):
    try:
        Path(os.path.realpath(yol)).relative_to(os.path.realpath(ust))
        return True
    except ValueError:
        return False


def kayit_hatalari(k, goruldu):
    hatalar = []
    if not isinstance(k, dict):
        return ["kayıt bir nesne değil"]
    for a in ZORUNLU:
        if not k.get(a) or not isinstance(k.get(a), str):
            hatalar.append(a)
    if "tur" not in hatalar and k["tur"] not in TURLER:
        hatalar.append("tur")
    if "tarih" not in hatalar and _tarih(k["tarih"]) is None:
        hatalar.append("tarih")
    if "gizli_icerir" not in hatalar and k["gizli_icerir"] not in ("evet", "hayir"):
        hatalar.append("gizli_icerir")
    for a in ("silme_gun", "yas_uyari_gun"):
        if a in k and (not isinstance(k[a], int) or isinstance(k[a], bool)):
            hatalar.append(a)
    if "beklenen" in k and not (isinstance(k["beklenen"], list) and all(isinstance(x, str) for x in k["beklenen"])):
        hatalar.append("beklenen")
    return hatalar


def kayit_denetle(k, kok, bugun, kutuphane, kok_var=True):
    """Tek kayıt için bulgular: [{seviye, metin, karar}]. Şema hatası varsa yalnız onu söyler."""
    f = []
    kim = k.get("kimlik", "?")

    def ekle(s, m, karar=None):
        f.append({"seviye": s, "metin": m, "karar": karar})
    yol = yol_ac(k["yol"])
    tarih = _tarih(k["tarih"])
    yas = (bugun - tarih).days
    gizli = k["gizli_icerir"] == "evet"
    sg, so = k.get("silme_gun"), k.get("silme_olay")
    olay_tamam = k.get("silme_olay_tamam") is True
    if _icinde(yol, kutuphane):
        ekle("sorun", f"{kim}: yedek yanlış yerde (kütüphane içinde); gizli ya da yanlış yüklenebilir, taşınması için kullanıcıya sor")
    elif any(_icinde(yol, t) for t in tarama_klasorleri()):
        ekle("sorun", f"{kim}: yedek yanlış yerde (skill taranan klasör içinde); gizli ya da yanlış yüklenebilir, taşınması için kullanıcıya sor")
    var = yol.exists()
    if kok_var and not var:
        ekle("sorun", f"{kim}: yedek yok ({k['yol']})")
    if var:
        eksik = [a for a in k.get("beklenen", []) if not os.path.lexists(yol / a)]
        if k.get("kayit") and k["kayit"] not in k.get("beklenen", []) and not os.path.lexists(yol / k["kayit"]):
            ekle("sorun", f"{kim}: kayıt dosyası yok: {k['kayit']}")
        if eksik:
            ekle("sorun", f"{kim}: beklenen öğe eksik: {', '.join(eksik)}")
        if gizli:
            if _gevsek_izin_var(yol):
                ekle("dikkat", f"{kim}: gizli içerikli ama izinleri gevşek (chmod 600 önerilir; kullanıcıya sor)")
            if sg is None and so is None:
                ekle("dikkat", f"{kim}: gizli içerikli ama silme zamanı tanımsız (kayda silme_gun ekle)")
    hazir = (sg is not None or so is not None) and (sg is None or yas >= sg) and (so is None or olay_tamam)
    if hazir:
        neden = " ve ".join(([f"{yas} gün oldu, eşik {sg}"] if sg is not None else []) + ([f"olay tamam: {so}"] if so else []))
        mut = str(Path(os.path.expanduser(str(k["yol"]))).resolve())
        ekle("dikkat", f"{kim}: SİLİNEBİLİR ({neden}). Silme komutu (yalnız kullanıcı onaylarsa; kalıcıdır, geri alınamaz): "
                       f"rm -r -- '{mut}' ; ya da Çöp Sepeti'ne taşı: mv -- '{mut}' ~/.Trash/",
             f"{kim} yedeği silinsin mi? Kalıcı silinir, geri alınamaz ({k['ne']}); istersen Çöp Sepeti'ne taşırım")
    else:
        if so and not olay_tamam:
            ekle("bilgi", f"{kim}: silme olayı bekleniyor: {so}")
        if sg is not None and yas < sg:
            ekle("bilgi", f"{kim}: {sg - yas} gün sonra silinebilir" + (" (gizli içerikli)" if gizli else ""))
        esik = k.get("yas_uyari_gun") or (YAS_UYARI_GUN_GIZLI if gizli else YAS_UYARI_GUN)
        if yas > esik and so is None:
            ekle("dikkat", f"{kim}: {yas} gündür duruyor; hâlâ gerekli mi?", f"{kim} yedeği hâlâ gerekli mi?")
    return f


def kayitsizlar(kok, kayitlar):
    """Kök altında kaydı olmayan doğrudan çocuklar: [(ad, bayt, tür_metni|None)]."""
    kayitli = set()
    for k in kayitlar:
        try:
            kayitli.add(os.path.realpath(yol_ac(k["yol"])))
        except (KeyError, TypeError):
            pass
    sonuc = []
    try:
        adlar = sorted(os.listdir(kok))
    except OSError:
        return []
    for ad in adlar:
        if ad.startswith("."):
            continue
        p = Path(kok) / ad
        if os.path.realpath(p) in kayitli:
            continue
        tur = next((t for r, t in BILINEN_AD_KALIPLARI if r.match(ad)), None)
        b, _ = boyut(p) if p.is_dir() and not p.is_symlink() else (_dosya_boyutu(p), False)
        sonuc.append((ad, b, tur))
    return sonuc


def _dosya_boyutu(p):
    try:
        return os.lstat(p).st_size
    except OSError:
        return 0


def degerlendir(veri, hata, kok_arg, kutuphane, bugun):
    """-> (durum, bulgular, satirlar_tablo, kayit_sayisi)"""
    f, tablo = [], []
    if veri is None:
        f.append({"seviye": "sorun", "metin": f"yedekler.json bulunamadı ya da bozuk: {hata[:100]}", "karar": None})
        return "sorun", f, tablo, 0
    kok = yol_ac(kok_arg or veri.get("kok") or "~/Documents/Claude/yedek")
    kayitlar = [k for k in veri.get("yedekler", []) if not (isinstance(k, dict) and k.get("durum") == "silindi")]
    kok_var = kok.is_dir()
    if not kok_var:
        f.append({"seviye": "dikkat", "metin": f"yedek klasörü yok ({kok}); yeni makine olabilir", "karar": None})
    goruldu = set()
    for k in kayitlar:
        h = kayit_hatalari(k, goruldu)
        kim = k.get("kimlik", "?") if isinstance(k, dict) else "?"
        if not h and k["kimlik"] in goruldu:
            f.append({"seviye": "sorun", "metin": f"kimlik tekrar ediyor: {kim}", "karar": None})
            continue
        if h:
            f.append({"seviye": "sorun", "metin": f"{kim}: kayıtta eksik ya da hatalı alan: {', '.join(h)}", "karar": None})
            continue
        goruldu.add(k["kimlik"])
        bul = kayit_denetle(k, kok, bugun, kutuphane, kok_var=kok_var)
        f += bul
        yas = (bugun - _tarih(k["tarih"])).days
        sg = k.get("silme_gun")
        durum_k = "SİLİNEBİLİR" if any("SİLİNEBİLİR" in x["metin"] for x in bul) else (
            "SORUN" if any(x["seviye"] == "sorun" for x in bul) else "tutuluyor")
        silme = " + ".join(([f"{sg} gün"] if sg is not None else []) + (["olay"] if k.get("silme_olay") else []))
        tablo.append((k["kimlik"], k["tur"], k["tarih"], yas, k["gizli_icerir"], durum_k, silme or "-"))
    if kok_var:
        for ad, b, tur in kayitsizlar(kok, [k for k in kayitlar if isinstance(k, dict)]):
            t = f"{tur}; " if tur else "tanınmayan ad; "
            f.append({"seviye": "dikkat", "metin": f"kayıtsız yedek: {ad} ({t}{mb(b)} MB)", "karar": f"{ad} yedeği kayda alınsın mı?"})
    if veri.get("ikinci_kopya_iste") is True:
        paketler = [k for k in kayitlar if isinstance(k, dict) and k.get("tur") == "git-paketi" and _tarih(k.get("tarih"))]
        en_yeni = max((_tarih(k["tarih"]) for k in paketler), default=None)
        if en_yeni is None or (bugun - en_yeni).days > GIT_PAKETI_GUN:
            f.append({"seviye": "dikkat", "metin": f"Kütüphanenin GitHub dışında ikinci kopyası (git bundle) yok ya da {GIT_PAKETI_GUN} günden eski",
                      "karar": None})
    f.sort(key=lambda x: SEVIYE_SIRA[x["seviye"]])
    durum = "sorun" if any(x["seviye"] == "sorun" for x in f) else "dikkat" if any(x["seviye"] == "dikkat" for x in f) else "temiz"
    return durum, f, tablo, len(kayitlar)


def _kirp(liste, n=10):
    return liste if len(liste) <= n else liste[:n] + [f"... ve {len(liste) - n} satır daha"]


def ozet_json(durum, bulgular, n):
    onemli = [x["metin"] for x in bulgular if x["seviye"] in ("sorun", "dikkat")]
    karar = [x["karar"] for x in bulgular if x["karar"]]
    if onemli:
        satirlar = _kirp(onemli)
    else:
        satirlar = [f"{n} yedek kayıtlı, hepsi yerinde; silinecek yedek yok."] + [x["metin"] for x in bulgular if x["seviye"] == "bilgi"][:5]
    return {"arac": "yedek-denetim", "durum": durum, "satirlar": satirlar, "karar_bekleyen": karar[:10]}


ETIKET = {"sorun": "SORUN", "dikkat": "DİKKAT", "bilgi": "bilgi"}
DURUM_ETIKET = {"temiz": "TEMİZ", "dikkat": "DİKKAT", "sorun": "SORUN"}


def tablo_satirlari(tablo):
    out = ["| Yedek | Tür | Tarih | Yaş (gün) | Gizli | Durum | Silme |", "|---|---|---|---|---|---|---|"]
    out += [f"| {a} | {t} | {d} | {y} | {g} | {s} | {sl} |" for a, t, d, y, g, s, sl in tablo]
    return out


def tam_metin(durum, bulgular, tablo, n, bugun):
    out = [f"Yedek durumu · {bugun.isoformat()} · {n} kayıt · durum: {DURUM_ETIKET[durum]}", ""]
    out += tablo_satirlari(tablo) + [""]
    out += [f"{ETIKET[x['seviye']]}: {x['metin']}" for x in bulgular]
    if not any(x["seviye"] in ("sorun", "dikkat") for x in bulgular):
        out.append(f"{n} yedek kayıtlı, hepsi yerinde; silinecek yedek yok.")
    k = [x["karar"] for x in bulgular if x["karar"]]
    if k:
        out += ["", "Karar bekleyenler"] + [f"- {x}" for x in k]
    return "\n".join(out)


def rapor_md(durum, bulgular, tablo, n, bugun):
    out = ["# Yedek Durumu", "", f"`araclar/yedek-denetim.py` üretir · {bugun.isoformat()} · salt okuma", ""]
    out += tablo_satirlari(tablo) + ["", "## Bulgular", ""]
    out += [f"- {ETIKET[x['seviye']]}: {x['metin']}" for x in bulgular] or ["- yok"]
    k = [x["karar"] for x in bulgular if x["karar"]]
    out += ["", "## Karar bekleyenler", ""] + ([f"- {x}" for x in k] if k else ["- yok"])
    return "\n".join(out) + "\n"



def cikti_izinli(hedef):
    """--cikti koruması: araç klasörlerine, ~/Library'ye ve yedek/proje klasörlerine (~/Documents/Claude) yazılmaz."""
    h = os.path.realpath(str(hedef))
    ev = os.path.realpath(str(Path.home()))
    yasak = [os.path.join(ev, d) for d in (".claude", ".agents", ".codex", ".gemini", ".cursor", ".copilot", ".openmontage", ".config", "Library")]
    yasak.append(os.path.join(ev, "Documents", "Claude"))
    return not any(h == y or h.startswith(y + os.sep) for y in yasak)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Yedek envanteri denetimi (salt okuma, silmez)")
    ap.add_argument("--kayit", default=str(VARSAYILAN_KAYIT))
    ap.add_argument("--kok", default=None, help="yedek kökü (dosyadaki 'kok' yerine; testler için)")
    ap.add_argument("--kutuphane", default=str(KOK), help="'yedek kütüphane içinde mi' denetimi için kütüphane yolu")
    ap.add_argument("--bugun", default=None, help="YYYY-AA-GG (test için)")
    ap.add_argument("--kisa", action="store_true")
    ap.add_argument("--ozet-json", action="store_true")
    ap.add_argument("--rapor", action="store_true")
    ap.add_argument("--cikti", default=str(KOK / "notlar" / "yedek-durumu.md"))
    ap.add_argument("--siki", action="store_true", help="durum sorun ise çıkış kodu 1")
    a = ap.parse_args(argv)
    if a.ozet_json and (a.kisa or a.rapor):
        ap.error("--ozet-json, --kisa ya da --rapor ile birlikte kullanılamaz")
    bugun = _tarih(a.bugun) if a.bugun else date.today()
    if bugun is None:
        ap.error("--bugun YYYY-AA-GG olmalı")
    try:
        veri, hata = kayit_oku(a.kayit)
        durum, bulgular, tablo, n = degerlendir(veri, hata, a.kok, Path(a.kutuphane), bugun)
    except Exception as e:  # noqa: BLE001
        if a.ozet_json:
            print(json.dumps({"arac": "yedek-denetim", "durum": "sorun", "satirlar": [f"araç hatası: {str(e)[:120]}"],
                              "karar_bekleyen": []}, ensure_ascii=False))
            return 0
        raise
    if a.ozet_json:
        print(json.dumps(ozet_json(durum, bulgular, n), ensure_ascii=False))
    elif a.kisa:
        onemli = [x for x in bulgular if x["seviye"] in ("sorun", "dikkat")]
        print("\n".join(f"{ETIKET[x['seviye']]}: {x['metin']}" for x in onemli) if onemli else "yedek: temiz")
    else:
        print(tam_metin(durum, bulgular, tablo, n, bugun))
    if a.rapor:
        hedef = Path(a.cikti)
        if not cikti_izinli(hedef):
            print(f"HATA: --cikti bu yola yazamaz (araç klasörleri ve yedekler korumalı): {hedef}", file=sys.stderr)
            return 2
        yeni = rapor_md(durum, bulgular, tablo, n, bugun)
        tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
        if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
            hedef.write_text(yeni, encoding="utf-8")
    return 1 if (a.siki and durum == "sorun") else 0


if __name__ == "__main__":
    sys.exit(main())
