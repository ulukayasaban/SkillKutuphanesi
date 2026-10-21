#!/usr/bin/env python3
"""Tutarlılık kontrolü. Hata varsa çıkış kodu 1.

- Her registry kaydının klasörü + SKILL.md + KAYNAK.md var mı
- Arşivde registry'de olmayan klasör var mı
- 'tercih' durumunda aynı isimden iki kayıt var mı
- Roller/profiller var olan skillere/rollere mi bakıyor
- Bir rol aynı örtüşme grubundan en fazla 1 birincil + 1 tamamlayıcı alıyor mu
- Kaynaklar.json yıldızlı repoların hepsini kapsıyor mu (--github ile)
"""
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import ARSIV, KAYNAKLAR, KOK, REGISTRY, json_oku  # noqa: E402


def main():
    hatalar, uyarilar = [], []
    skiller = json_oku(REGISTRY)["skiller"]
    ids = {s["id"]: s for s in skiller}
    for s in skiller:
        k = KOK / s["yol"]
        if not (k / "SKILL.md").exists():
            hatalar.append(f"SKILL.md yok: {s['yol']}")
        if not (k / "KAYNAK.md").exists():
            hatalar.append(f"KAYNAK.md yok: {s['yol']}")
    kayitli = {str((KOK / s["yol"]).resolve()) for s in skiller}
    for sm in ARSIV.rglob("KAYNAK.md"):
        if str(sm.parent.resolve()) not in kayitli:
            hatalar.append(f"registry'de olmayan klasör: {sm.parent.relative_to(KOK)}")
    for ad, n in Counter(s["ad"] for s in skiller if s["durum"] == "tercih").items():
        if n > 1:
            hatalar.append(f"aynı isimde birden fazla 'tercih': {ad}")
    for f in sorted((KOK / "roller").glob("*.json")):
        r = json_oku(f)
        for x in r["cekirdek"] + r.get("opsiyonel", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"rol {f.stem}: skill yok -> {x}")
        gruplar = Counter()
        for x in r["cekirdek"]:
            s = ids.get(x)
            if s and s.get("ortusme_grubu"):
                gruplar[(s["ortusme_grubu"], s.get("ortusme_rolu"))] += 1
        for (g, rol), n in gruplar.items():
            if rol == "birincil" and n > 1:
                uyarilar.append(f"rol {f.stem}: '{g}' grubundan {n} birincil skill")
    roller = {f.stem for f in (KOK / "roller").glob("*.json")}
    for f in sorted((KOK / "profiller").glob("*.json")):
        p = json_oku(f)
        for r in p["roller"]:
            if r not in roller:
                hatalar.append(f"profil {f.stem}: rol yok -> {r}")
        for x in p.get("ek_skiller", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"profil {f.stem}: skill yok -> {x}")
    if "--github" in sys.argv:
        r = subprocess.run(["gh", "api", "graphql", "--paginate", "-f",
                            "query=query($endCursor:String){viewer{starredRepositories(first:100,after:$endCursor)"
                            "{pageInfo{hasNextPage endCursor} nodes{nameWithOwner}}}}",
                            "--jq", ".data.viewer.starredRepositories.nodes[].nameWithOwner"],
                           capture_output=True, text=True)
        tanimli = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
        for repo in r.stdout.split():
            if repo not in tanimli:
                uyarilar.append(f"yıldızlı ama kaynaklar.json'da yok: {repo}")
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    print(f"{len(skiller)} skill · {len(hatalar)} hata · {len(uyarilar)} uyarı")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
