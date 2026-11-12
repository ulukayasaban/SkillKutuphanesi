#!/usr/bin/env python3
"""yt-dlp ile YouTube araması yapar; başlık, URL, izlenme, süre ve tarih döndürür."""

import argparse
import json
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

YTDLP = shutil.which("yt-dlp")


def flat_search(query, wanted):
    """Hızlı arama: aday videoları toplar (kanal/oynatma listesi sonuçlarını eler)."""
    # Sonuçlar arasında kanal da çıkabildiği için fazladan istiyoruz.
    limit = max(wanted * 3, wanted + 5)
    cmd = [YTDLP, "--flat-playlist", "--dump-json", "--no-warnings",
           f"ytsearch{limit}:{query}"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0 and not proc.stdout.strip():
        sys.exit(f"yt-dlp arama hatası:\n{proc.stderr.strip()}")

    videos, seen = [], set()
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("ie_key") != "Youtube":  # kanal / playlist sonucu
            continue
        vid = entry.get("id")
        if not vid or vid in seen:
            continue
        seen.add(vid)
        videos.append(entry)
        if len(videos) >= wanted:
            break
    return videos


def fetch_details(entry):
    """Tek videonun tam metadatasını çeker (yayın tarihi yalnız burada gelir)."""
    url = entry.get("webpage_url") or f"https://www.youtube.com/watch?v={entry['id']}"
    cmd = [YTDLP, "--dump-json", "--skip-download", "--no-warnings",
           "--no-playlist", url]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    full = {}
    if proc.returncode == 0 and proc.stdout.strip():
        try:
            full = json.loads(proc.stdout.splitlines()[0])
        except json.JSONDecodeError:
            full = {}
    return {
        "baslik": full.get("title") or entry.get("title") or "-",
        "url": url,
        "izlenme": full.get("view_count", entry.get("view_count")),
        "sure_sn": full.get("duration", entry.get("duration")),
        "tarih": full.get("upload_date"),
        "kanal": full.get("channel") or entry.get("channel") or "-",
    }


def fmt_views(n):
    """Turkce binlik ayraci ile: 83712 -> 83.712"""
    if n is None:
        return "-"
    return f"{n:,}".replace(",", ".")


def fmt_duration(sec):
    if not sec:
        return "-"
    sec = int(sec)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fmt_date(d):
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if d and len(d) == 8 else "-"


def main():
    p = argparse.ArgumentParser(description="yt-dlp ile YouTube araması")
    p.add_argument("sorgu", help="Arama sorgusu")
    p.add_argument("-n", "--sayi", type=int, default=10,
                   help="Döndürülecek sonuç sayısı (varsayılan: 10)")
    p.add_argument("--sirala", choices=["ilgi", "izlenme", "tarih"], default="ilgi",
                   help="Sonuç sıralaması (varsayılan: ilgi = YouTube sırası)")
    p.add_argument("--json", action="store_true", help="Ham JSON çıktısı ver")
    args = p.parse_args()

    if not YTDLP:
        sys.exit("yt-dlp bulunamadi. Kurulum: brew install yt-dlp")
    if args.sayi < 1:
        sys.exit("--sayi en az 1 olmali.")

    candidates = flat_search(args.sorgu, args.sayi)
    if not candidates:
        print(f"'{args.sorgu}' icin video bulunamadi.")
        return

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch_details, candidates))

    if args.sirala == "izlenme":
        results.sort(key=lambda r: r["izlenme"] or 0, reverse=True)
    elif args.sirala == "tarih":
        results.sort(key=lambda r: r["tarih"] or "", reverse=True)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f'\nArama: "{args.sorgu}"  —  {len(results)} sonuc  (siralama: {args.sirala})\n')
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['baslik']}")
        print(f"   URL      : {r['url']}")
        print(f"   Kanal    : {r['kanal']}")
        print(f"   Izlenme  : {fmt_views(r['izlenme'])}"
              f"   Sure: {fmt_duration(r['sure_sn'])}"
              f"   Tarih: {fmt_date(r['tarih'])}")
        print()


if __name__ == "__main__":
    main()
