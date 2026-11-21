#!/usr/bin/env python3
"""Maliyet ve performans ölçüm aracı (0 token, sadece Python stdlib).

Kullanım:
  python3 araclar/olcum.py --disk
  python3 araclar/olcum.py --ozet
  python3 araclar/olcum.py --dogrula
  python3 araclar/olcum.py --yaz --tur yeni_repo --islenen-repo 1 --sure-sn 12.4 --token-veya-kota 0 --onay-sayisi 0 --hata-tekrar 0 --kuru
"""
import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ortak import KOK  # noqa: E402

OLCUM_DOSYA = KOK / "olcum.jsonl"
OLCUM_TURLERI = ("yeni_repo", "aylik_takip")
DISK_KLASORLERI = ("arsiv", "fihrist", ".git")
IZINLI_ANAHTARLAR = frozenset({
    "tarih", "tur", "islenen_repo", "sure_sn", "token_veya_kota",
    "disk_mb", "disk_fark_mb", "onay_sayisi", "hata_tekrar", "not",
})
ZORUNLU_TAM_SAYILAR = ("islenen_repo", "token_veya_kota", "onay_sayisi", "hata_tekrar")
ZORUNLU_SAYILAR = ("sure_sn", "disk_mb")


def _tarih_gecerli(deger) -> bool:
    if not isinstance(deger, str) or not deger:
        return False
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", deger):
        try:
            date.fromisoformat(deger)
            return True
        except ValueError:
            return False
    try:
        datetime.fromisoformat(deger)
        return True
    except ValueError:
        return False


def _tam_sayi_mi(deger) -> bool:
    return isinstance(deger, int) and not isinstance(deger, bool) and deger >= 0


def _sayi_mi(deger) -> bool:
    return isinstance(deger, (int, float)) and not isinstance(deger, bool) and deger >= 0


def disk_olcum_mb(kok=KOK) -> float:
    """arsiv/, fihrist/ ve .git/ klasörlerinin toplam boyutunu MB olarak döner.
    Symlink hedeflerini izlemez, sabit bağları (hardlink) çift saymaz."""
    kok = Path(kok)
    toplam = 0
    gorulen_inodlar = set()
    for alt in DISK_KLASORLERI:
        hedef = kok / alt
        if not hedef.exists() or hedef.is_symlink():
            continue
        for kok_yol, _, dosyalar in os.walk(hedef, followlinks=False):
            for ad in dosyalar:
                dosya = Path(kok_yol) / ad
                try:
                    st = dosya.lstat()
                except OSError:
                    continue
                if os.path.islink(dosya):
                    continue
                kimlik = (st.st_dev, st.st_ino)
                if kimlik in gorulen_inodlar:
                    continue
                gorulen_inodlar.add(kimlik)
                toplam += st.st_size
    return round(toplam / (1024 * 1024), 2)


def satir_dogrula(kayit) -> list[str]:
    """Tek bir olcum.jsonl satırının şema hatalarını döndürür (boşsa geçerli)."""
    if not isinstance(kayit, dict):
        return ["satır JSON nesnesi (sözlük) değil"]
    h = []
    if not _tarih_gecerli(kayit.get("tarih")):
        h.append("tarih geçerli YYYY-AA-GG veya ISO-8601 değil")
    if kayit.get("tur") not in OLCUM_TURLERI:
        h.append(f"tur geçersiz: {kayit.get('tur')!r} ({', '.join(OLCUM_TURLERI)})")
    for alan in ZORUNLU_TAM_SAYILAR:
        if not _tam_sayi_mi(kayit.get(alan)):
            h.append(f"{alan} >= 0 tam sayı değil")
    for alan in ZORUNLU_SAYILAR:
        if not _sayi_mi(kayit.get(alan)):
            h.append(f"{alan} >= 0 sayı değil")
    if "disk_fark_mb" in kayit:
        df = kayit["disk_fark_mb"]
        if not (isinstance(df, (int, float)) and not isinstance(df, bool)):
            h.append("disk_fark_mb sayı değil")
    if "not" in kayit and not isinstance(kayit["not"], str):
        h.append("not metin değil")
    yabanci = sorted(k for k in kayit if k not in IZINLI_ANAHTARLAR)
    if yabanci:
        h.append(f"bilinmeyen anahtar: {', '.join(yabanci)}")
    return h


def olcum_oku(yol=OLCUM_DOSYA) -> list[dict]:
    """olcum.jsonl satırlarını liste olarak okur; dosya yoksa boş liste döner."""
    yol = Path(yol)
    if not yol.is_file():
        return []
    kayitlar = []
    for no, satir in enumerate(yol.read_text(encoding="utf-8").splitlines(), 1):
        temiz = satir.strip()
        if not temiz:
            continue
        try:
            kayitlar.append(json.loads(temiz))
        except ValueError as e:
            raise ValueError(f"{yol}:{no} geçersiz JSON: {e}") from e
    return kayitlar


def olcum_hazirla(
    *,
    tur: str,
    islenen_repo: int,
    sure_sn: float,
    token_veya_kota: int,
    onay_sayisi: int,
    hata_tekrar: int,
    disk_mb: float = None,
    not_metni: str = None,
    tarih: str = None,
    kok=KOK,
    yol=OLCUM_DOSYA,
) -> dict:
    """Doğrulanmış ölçüm kaydı hazırlar ve disk_fark_mb hesaplar."""
    kok = Path(kok)
    yol = Path(yol)
    olculen_disk = round(float(disk_mb), 2) if disk_mb is not None else disk_olcum_mb(kok)
    oncekiler = olcum_oku(yol) if yol.is_file() else []
    onceki_disk = oncekiler[-1].get("disk_mb") if oncekiler else None
    disk_fark = round(olculen_disk - float(onceki_disk), 2) if isinstance(onceki_disk, (int, float)) and not isinstance(onceki_disk, bool) else 0.0

    kayit = {
        "tarih": tarih or date.today().isoformat(),
        "tur": tur,
        "islenen_repo": islenen_repo,
        "sure_sn": round(float(sure_sn), 2),
        "token_veya_kota": token_veya_kota,
        "disk_mb": olculen_disk,
        "disk_fark_mb": disk_fark,
        "onay_sayisi": onay_sayisi,
        "hata_tekrar": hata_tekrar,
    }
    if not_metni is not None:
        kayit["not"] = not_metni

    hatalar = satir_dogrula(kayit)
    if hatalar:
        raise ValueError("Ölçüm kaydı şeması geçersiz: " + "; ".join(hatalar))
    return kayit


def olcum_yaz(*, kuru: bool = False, yol=OLCUM_DOSYA, **kwargs) -> dict:
    """Ölçüm kaydını doğrular ve kuru=False ise olcum.jsonl sonuna tek satır ekler."""
    yol = Path(yol)
    kayit = olcum_hazirla(yol=yol, **kwargs)
    if not kuru:
        yol.parent.mkdir(parents=True, exist_ok=True)
        with yol.open("a", encoding="utf-8") as f:
            f.write(json.dumps(kayit, ensure_ascii=False) + "\n")
    return kayit


def dosya_dogrula(yol=OLCUM_DOSYA) -> list[str]:
    """Var olan olcum.jsonl dosyasının tüm satırlarını doğrular; hata listesi döner."""
    yol = Path(yol)
    if not yol.is_file():
        return []
    hatalar = []
    for no, satir in enumerate(yol.read_text(encoding="utf-8").splitlines(), 1):
        temiz = satir.strip()
        if not temiz:
            continue
        try:
            obj = json.loads(temiz)
        except ValueError as e:
            hatalar.append(f"satır {no}: JSON ayrışmadı ({e})")
            continue
        for s in satir_dogrula(obj):
            hatalar.append(f"satır {no}: {s}")
    return hatalar


def main(argv=None):
    ap = argparse.ArgumentParser(description="SkillKutuphanesi Faz 1 ölçüm aracı (olcum.jsonl)")
    ap.add_argument("--kok", default=str(KOK), help="Kütüphane kök klasörü")
    ap.add_argument("--dosya", default=None, help="Ölçüm JSONL dosya yolu (varsayılan: <kok>/olcum.jsonl)")
    ap.add_argument("--disk", action="store_true", help="Mevcut arsiv/ + fihrist/ + .git/ boyutunu (MB) yazdır")
    ap.add_argument("--ozet", action="store_true", help="Mevcut ölçüm kayıtlarını özetle")
    ap.add_argument("--dogrula", action="store_true", help="Ölçüm dosyasının şemasını doğrula")
    ap.add_argument("--yaz", action="store_true", help="Yeni ölçüm satırı yaz")
    ap.add_argument("--kuru", action="store_true", help="--yaz ile diske yazmadan üretilecek satırı göster")
    ap.add_argument("--tur", choices=OLCUM_TURLERI, help="Ölçüm türü")
    ap.add_argument("--islenen-repo", type=int, default=0, help="İşlenen repo sayısı")
    ap.add_argument("--sure-sn", type=float, default=0.0, help="Toplam süre (saniye)")
    ap.add_argument("--token-veya-kota", type=int, default=0, help="YZ token veya çağrı sayısı (0 = Python)")
    ap.add_argument("--onay-sayisi", type=int, default=0, help="Kullanıcı onay turu sayısı")
    ap.add_argument("--hata-tekrar", type=int, default=0, help="Başarısız/tekrar adım sayısı")
    ap.add_argument("--disk-mb", type=float, default=None, help="İsteğe bağlı manuel disk boyutu (MB)")
    ap.add_argument("--not", dest="not_metni", default=None, help="İsteğe bağlı açıklama notu")
    ap.add_argument("--tarih", default=None, help="İsteğe bağlı tarih (YYYY-AA-GG)")
    a = ap.parse_args(argv)

    kok = Path(a.kok)
    dosya = Path(a.dosya) if a.dosya else (kok / "olcum.jsonl")

    if a.disk:
        print(f"{disk_olcum_mb(kok):.2f} MB")
        return 0

    if a.dogrula:
        h = dosya_dogrula(dosya)
        for x in h:
            print("HATA:", x)
        if not h:
            print(f"olcum.jsonl temiz ({len(olcum_oku(dosya))} kayıt)")
        return 1 if h else 0

    if a.ozet:
        kayitlar = olcum_oku(dosya)
        if not kayitlar:
            print("Ölçüm kaydı yok.")
            return 0
        print(f"Toplam {len(kayitlar)} kayıt:")
        for k in kayitlar[-10:]:
            print(f"  {k.get('tarih')} | {k.get('tur')} | repo={k.get('islenen_repo')} | "
                  f"{k.get('sure_sn')} sn | token={k.get('token_veya_kota')} | "
                  f"disk={k.get('disk_mb')} MB (fark {k.get('disk_fark_mb', 0):+}) | "
                  f"onay={k.get('onay_sayisi')} | hata={k.get('hata_tekrar')}")
        return 0

    if a.yaz:
        if not a.tur:
            ap.error("--yaz için --tur (yeni_repo | aylik_takip) zorunludur")
        kayit = olcum_yaz(
            kuru=a.kuru,
            yol=dosya,
            kok=kok,
            tur=a.tur,
            islenen_repo=a.islenen_repo,
            sure_sn=a.sure_sn,
            token_veya_kota=a.token_veya_kota,
            onay_sayisi=a.onay_sayisi,
            hata_tekrar=a.hata_tekrar,
            disk_mb=a.disk_mb,
            not_metni=a.not_metni,
            tarih=a.tarih,
        )
        print(json.dumps(kayit, ensure_ascii=False))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
