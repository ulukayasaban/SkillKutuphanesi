#!/usr/bin/env python3
"""GitHub yıldız listeleri ↔ kütüphane eşlemesi. Kütüphanenin TÜM kaynakları (skill repoları + süreçte kullanılan
referans kütüphaneleri T5/T6) TEK listede ('Yapay Zeka Skillleri') durur; başka skill listesi tutulmaz (2026-10-22 kararı).

  python3 araclar/github-skill-listesi.py            # RAPOR (hiçbir şeyi değiştirmez):
                                                     #  - skill listesindeki ama kütüphanede olmayan repolar (= YENİ, eklenecek)
                                                     #  - skill içeren ama skill listesinde olmayan repolar
                                                     #  - birden fazla listede duran skill repoları (kopya)
  python3 araclar/github-skill-listesi.py --duzenle  # skill repolarını sadece skill listesine taşır (başka listelerden çıkarır).
                                                     # GitHub oturumunda 'user' izni gerekir:  gh auth refresh -h github.com -s user
Skill listesinin adı/slug'ı kaynaklar.json -> "github_skill_listesi".
Yıldızlar kaldırılmaz. Kütüphanede olmayan repolar (kişisel yıldızlar) bulundukları listelerde kalır.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, json_oku  # noqa: E402


def gql(sorgu, **degisken):
    komut = ["gh", "api", "graphql", "-f", f"query={sorgu}"]
    for k, v in degisken.items():
        if isinstance(v, list):
            for x in v:
                komut += ["-F", f"{k}[]={x}"]
        else:
            komut += ["-f", f"{k}={v}"]
    r = subprocess.run(komut, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stdout + r.stderr)
    return json.loads(r.stdout)


def listeler():
    """Tüm listeler ve TÜM öğeleri (GitHub sayfa başına en fazla 100 öğe verir: sayfalanır)."""
    d = gql("query{viewer{lists(first:50){nodes{id name slug}}}}")
    sonuc = []
    for l in d["data"]["viewer"]["lists"]["nodes"]:
        ogeler, imlec = [], None
        while True:
            q = ("query($id:ID!,$c:String){node(id:$id){... on UserList{items(first:100,after:$c){pageInfo{hasNextPage endCursor}"
                 " nodes{... on Repository{nameWithOwner id}}}}}}")
            r = gql(q, id=l["id"], **({"c": imlec} if imlec else {}))["data"]["node"]["items"]
            ogeler += r["nodes"]
            if not r["pageInfo"]["hasNextPage"]:
                break
            imlec = r["pageInfo"]["endCursor"]
        sonuc.append({**l, "items": {"nodes": ogeler}})
    return sonuc


def main():
    ayar = json_oku(KAYNAKLAR)
    hedef_slug = ayar.get("github_skill_listesi", "yapay-zeka-skillleri")
    tumu = listeler()
    hedef = next((l for l in tumu if l["slug"] == hedef_slug), None)
    if not hedef:
        sys.exit(f"Skill listesi bulunamadı: '{hedef_slug}'. Mevcut: {', '.join(l['slug'] for l in tumu)}")
    skill_repolari = sorted({k["repo"] for k in ayar["repolar"] if k["tip"] != "KAYIP"})
    uyelik, idler = {}, {}
    for l in tumu:
        for r in l["items"]["nodes"]:
            if r:
                uyelik.setdefault(r["nameWithOwner"], []).append(l["name"])
                idler[r["nameWithOwner"]] = r["id"]
    hedeftekiler = [r["nameWithOwner"] for r in hedef["items"]["nodes"] if r]

    yeni = [r for r in hedeftekiler if r not in {k["repo"] for k in ayar["repolar"]}]
    # Kullanıcının kendi listeleri (kaynaklar.json -> korunan_listeler, ör. 'Yapay Zeka araçları'): üyelik korunur, kopya sayılmaz
    korunan = {l["name"] for l in tumu if l["slug"] in set(ayar.get("korunan_listeler", []))}
    korunan_id = {l["name"]: l["id"] for l in tumu if l["name"] in korunan}
    eksik = [r for r in skill_repolari if hedef["name"] not in uyelik.get(r, [])]
    kopya = [(r, uyelik[r]) for r in skill_repolari if len([x for x in uyelik.get(r, []) if x not in korunan]) > 1]
    print(f"Skill listesi: '{hedef['name']}' ({len(hedeftekiler)} repo) · kütüphanedeki skill kaynağı: {len(skill_repolari)}")
    print(f"\nYENİ (listede var, kütüphanede yok) — {len(yeni)}:" + ("".join(f"\n  + {r}" for r in yeni) or " yok"))
    if yeni:
        print("  -> rehber/03-yeni-skill-ekleme.md (çakışma kontrolü + ücret sınıflandırması dahil)")
    print(f"\nSkill listesinde OLMAYAN skill kaynakları — {len(eksik)}:" + (" " + ", ".join(eksik) if eksik else " yok"))
    print(f"Birden fazla listede duran skill repoları — {len(kopya)}:" + ("".join(f"\n  {r}: {', '.join(l)}" for r, l in kopya) or " yok"))
    diger = [f"{l['name']} ({len([x for x in l['items']['nodes'] if x])})" + (" [korunan]" if l["name"] in korunan else "")
             for l in tumu if l is not hedef]
    print(f"Diğer listeler — {len(diger)}:" + (" " + ", ".join(diger) if diger else " yok"))

    if "--duzenle" not in sys.argv:
        if eksik or kopya:
            print("\nDüzenlemek için: python3 araclar/github-skill-listesi.py --duzenle")
        return 0
    tasinacak = sorted(set(eksik) | {r for r, _ in kopya})
    hata = 0
    for r in tasinacak:
        subprocess.run(["gh", "api", "-X", "PUT", f"user/starred/{r}"], capture_output=True)  # yıldızlı değilse yıldızla
        rid = idler.get(r)
        if not rid:
            rid = json.loads(subprocess.run(["gh", "api", f"repos/{r}", "--jq", "{id:.node_id}"],
                                            capture_output=True, text=True).stdout)["id"]
        try:
            listeler_ = [hedef["id"]] + [korunan_id[n] for n in uyelik.get(r, []) if n in korunan_id]
            gql("mutation($item:ID!,$l:[ID!]!){updateUserListsForItem(input:{itemId:$item,listIds:$l}){lists{name}}}",
                item=rid, l=listeler_)
            print(f"  ✓ {r} -> '{hedef['name']}'" + (f" (+ korunan: {', '.join(n for n in uyelik.get(r, []) if n in korunan_id)})" if any(n in korunan_id for n in uyelik.get(r, [])) else ""))
        except RuntimeError as e:
            hata += 1
            if "INSUFFICIENT_SCOPES" in str(e):
                sys.exit("DURDU: GitHub oturumunda 'user' izni yok. Şunu çalıştırıp tarayıcıda onayla, sonra tekrar dene:\n"
                         "  gh auth refresh -h github.com -s user")
            print(f"  ✗ {r}: {str(e)[:200]}")
    print(f"\nTaşınan: {len(tasinacak) - hata} · hata: {hata}")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
