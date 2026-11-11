#!/usr/bin/env python3
"""Verilen repoları yıldızlar ve GitHub'daki skill listesine ('Yapay Zeka Skillleri', kaynaklar.json -> github_skill_listesi)
ekler. Sadece GitHub hesabındaki yıldız/liste değişir; kütüphaneye (kaynaklar.json, arsiv) hiçbir şey eklenmez —
ekleme ayrıca rehber/03-yeni-skill-ekleme.md adımlarıyla (çakışma + ücret kontrolü) yapılır.
Bu araç, "kütüphanede olmayan bir repoyu yıldızla + skill listesine ekle" işinin TEK aracıdır (tek repo ya da --dosya ile toplu).
Yazmadan önce kendi onay sorusunu sorar (e). Etkileşimsiz kabukta input() EOF verir ve hiçbir şey yazılmadan durur; kullanıcı sohbette
"evet" dedikten sonra ajan: printf 'e\n' | python3 araclar/listeye-ekle.py owner/ad

  python3 araclar/listeye-ekle.py owner/ad [owner/ad …]
  python3 araclar/listeye-ekle.py --dosya notlar/populer-aday-2026-11.txt          # satır başına bir repo (# yorum)
  python3 araclar/listeye-ekle.py --dosya notlar/populer-degerlendirme-2026-11.md   # .md: içindeki `owner/ad` adları

Gereksinim: kendi bilgisayarında gh oturumu + 'user' izni (gh auth refresh -h github.com -s user). Bulut oturumlarında
çalışmaz (user/starred ve GraphQL kapalı). Repodaki diğer liste üyelikleri korunur.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, json_oku  # noqa: E402

_spec = importlib.util.spec_from_file_location("gsl", Path(__file__).parent / "github-skill-listesi.py")
gsl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gsl)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    var = {r["repo"].lower() for r in json_oku(KAYNAKLAR)["repolar"]}
    if args[0] == "--dosya":
        metin = Path(KOK, args[1]).read_text(encoding="utf-8")
        if args[1].endswith(".txt"):  # satır başına bir repo; # yorum
            repolar = [l.split("#")[0].strip() for l in metin.splitlines()]
            repolar = [r for r in repolar if r]
        else:
            repolar = sorted(set(re.findall(r"`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`", metin)))
            repolar = [r for r in repolar if not r.endswith((".md", ".py", ".json", ".sh"))]
        repolar = [r for r in repolar if r.lower() not in var]  # kütüphanedekiler zaten listede olmalı (--duzenle)
        print(f"{args[1]} içinde kütüphanede olmayan {len(repolar)} repo bulundu:\n  " + ", ".join(repolar))
    else:
        repolar = [a.strip("/") for a in args]
    kotu = [r for r in repolar if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", r)]
    if kotu:
        sys.exit(f"geçersiz repo adı: {', '.join(kotu)}")
    slug = json_oku(KAYNAKLAR).get("github_skill_listesi", "yapay-zeka-skillleri")
    try:
        listeler = gsl.listeler()
    except RuntimeError as e:
        sys.exit("DURDU: GitHub listeleri okunamadı (GraphQL kapalı ya da gh oturumu yok). Bu aracı kendi bilgisayarında çalıştır.\n"
                 + str(e)[:300])
    hedef = next((l for l in listeler if l["slug"] == slug), None)
    if not hedef:
        sys.exit(f"DURDU: '{slug}' adlı liste yok (kaynaklar.json -> github_skill_listesi). Mevcut listeler: "
                 + ", ".join(f"{l['name']} ({l['slug']})" for l in listeler))
    try:  # hedefin açıklaması: yazmadan önce doğru listeyi gösterip onay almak için
        acik = next((l.get("description") or "" for l in gsl.gql("query{viewer{lists(first:50){nodes{slug description}}}}")
                     ["data"]["viewer"]["lists"]["nodes"] if l["slug"] == slug), "")
    except (RuntimeError, KeyError):
        acik = ""
    print(f"\nHedef liste: **{hedef['name']}** (slug: {hedef['slug']}, {len([x for x in hedef['items']['nodes'] if x])} öğe)"
          + (f"\n  \"{acik[:160]}\"" if acik else "") + "\nDiğer listelere dokunulmaz. "
          f"{len(repolar)} repo yıldızlanıp bu listeye eklenecek. Devam için e:")
    if input().strip().lower() not in ("e", "evet", "y"):
        print("iptal; hiçbir şey değişmedi")
        return 2
    uyelik = {}
    for l in listeler:
        for x in l["items"]["nodes"]:
            if x:
                uyelik.setdefault(x["nameWithOwner"].lower(), set()).add(l["id"])
    hata = 0
    for r in repolar:
        y = subprocess.run(["gh", "api", "-X", "PUT", f"user/starred/{r}"], capture_output=True, text=True)
        if y.returncode:
            hata += 1
            print(f"  ✗ {r}: yıldızlanamadı: {y.stderr.strip()[:160]}")
            continue
        rid = json.loads(subprocess.run(["gh", "api", f"repos/{r}", "--jq", "{id:.node_id}"], capture_output=True, text=True).stdout)["id"]
        if hedef["id"] in uyelik.get(r.lower(), set()):
            print(f"  = {r}: zaten '{hedef['name']}' listesinde (yıldız tazelendi)")
            continue
        try:
            gsl.gql("mutation($item:ID!,$l:[ID!]!){updateUserListsForItem(input:{itemId:$item,listIds:$l}){lists{name}}}",
                    item=rid, l=sorted(uyelik.get(r.lower(), set()) | {hedef["id"]}))
            print(f"  ✓ {r} -> yıldızlandı, '{hedef['name']}' listesine eklendi")
        except RuntimeError as e:
            hata += 1
            if "INSUFFICIENT_SCOPES" in str(e):
                sys.exit("DURDU: gh oturumunda 'user' izni yok:  gh auth refresh -h github.com -s user  (sonra tekrar çalıştır)")
            print(f"  ✗ {r}: listeye eklenemedi: {str(e)[:160]}")
    print(f"\nBitti: {len(repolar) - hata} tamam · {hata} hata. Sonraki adım: python3 araclar/github-skill-listesi.py "
          "(YENİ repoları gösterir) → rehber/03 ile kütüphaneye ekleme (çakışma + ücret kontrolü).")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
