#!/usr/bin/env python3
"""Program denetimi (salt okuma): programlar.json'daki her program için kütüphanedeki kaynak kopyasının sürümü ile
GitHub'daki en son sürümü karşılaştırır, kaynak kopyasının yerinde olduğunu kontrol eder.

Hiçbir şey kurmaz, indirmez, güncellemez; program komutlarını çalıştırmaz; anahtar/oturum dosyalarını açmaz.
Ağ hatası denetimi düşürmez ("öğrenilemedi" yazar). Çıkış kodu her zaman 0 (aylık zinciri durdurmaz).

Çıktı: notlar/program-denetimi.md
Kullanım: python3 araclar/program-denetim.py
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, gh_api, json_oku  # noqa: E402


def surum_ayikla(etiket):
    """'v0.5.0' / '0.5.0' -> (0, 5, 0); anlaşılmazsa None."""
    m = re.fullmatch(r"v?(\d+(?:\.\d+)*)", (etiket or "").strip())
    return tuple(int(x) for x in m.group(1).split(".")) if m else None


def durum(kutuphane, son):
    a, b = surum_ayikla(kutuphane), surum_ayikla(son)
    if not a or not b:
        return "öğrenilemedi"
    return "güncel" if a >= b else "YENİ SÜRÜM VAR"


def main():
    kart = json_oku(KOK / "programlar.json", {"programlar": {}})["programlar"]
    satirlar = []
    for ad, p in sorted(kart.items()):
        kopya = KOK / p.get("kaynak_kopyasi", "")
        kopya_var = bool(p.get("kaynak_kopyasi")) and kopya.is_dir() and any(kopya.iterdir())
        try:
            son = gh_api(f"repos/{p['repo']}/releases/latest")["tag_name"]
        except Exception as e:  # noqa: BLE001  ağ/404: denetim düşmez
            son = None
            print(f"UYARI: {ad}: son sürüm öğrenilemedi ({str(e)[:100]})")
        d = durum(p.get("kutuphane_surumu"), son)
        satirlar.append((ad, p["repo"], p.get("kutuphane_surumu"), son or "?", d, "var" if kopya_var else "YOK"))
        print(f"{ad}: kütüphane {p.get('kutuphane_surumu')} · GitHub {son or '?'} · {d} · kaynak kopyası {'var' if kopya_var else 'YOK'}")
    out = ["# Program Denetimi", "",
           f"> `araclar/program-denetim.py` üretir · {date.today().isoformat()} · salt okuma; güncelleme kullanıcı onayıyla "
           "`rehber/11-program-yonetimi.md` adımlarıyla yapılır.", "",
           "| Program | Repo | Kütüphanedeki sürüm | GitHub son sürüm | Durum | Kaynak kopyası |", "|---|---|---|---|---|---|"]
    out += [f"| {a} | {r} | {k} | {s} | {d} | {v} |" for a, r, k, s, d, v in satirlar]
    hedef, yeni = KOK / "notlar" / "program-denetimi.md", "\n".join(out) + "\n"
    tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
    if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
        hedef.write_text(yeni, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
