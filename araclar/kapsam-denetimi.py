#!/usr/bin/env python3
"""Kapsam denetimi: yıldızlı repolardaki HER SKILL.md dosyasının ne olduğunu açıklar. Açıklanamayan varsa çıkış kodu 1.

Bağımsız kontrol: arşivi üreten koddan ayrı olarak, her repo için GitHub'dan kayıtlı commit'teki tam dosya ağacını
yeniden çeker ve içindeki tüm SKILL.md (büyük/küçük harf fark etmez) dosyalarını tek tek şunlarla eşleştirir:
  1) registry.json'daki bir skill (ana yol, araç sürümü veya birebir kopya olarak), ya da
  2) gerekçeli bir hariç tutma kararı (ayna / başka AI aracı / test / örnek / şablon).
Ayrıca kütüphane/araç (T5/T6) repolarında sonradan skill eklenmiş mi diye bakar.

Çıktı: notlar/kapsam-denetimi.md
Kullanım: python3 araclar/kapsam-denetimi.py
"""
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, gh_api, json_oku  # noqa: E402

ACIKLAMA = {
    "secildi": "arşivde (ana sürüm)",
    "arac-varyanti": "arşivde (Claude/Codex'e özel sürüm)",
    "ayri-surum": "arşivde (aynı adlı farklı içerik, ayrı skill)",
    "ayna-ayni": "birebir kopya (tek kopya yeter)",
    "ayna-baska-arac": "başka AI aracı (Cursor/Gemini/Kiro…) için kopya",
    "haric": "bilinçli hariç (test/örnek/şablon)",
}


def main():
    reg = json_oku(REGISTRY)
    denetim = reg.get("denetim", {})
    kayitlar = json_oku(KAYNAKLAR)["repolar"]
    arsiv_repolari = sorted({k["repo"] for k in kayitlar if k["tip"] in ("T1", "T2", "T3", "T4")})
    referans_repolari = sorted({k["repo"] for k in kayitlar} - set(arsiv_repolari))
    yol_index = set()
    for s in reg["skiller"]:
        yol_index.add((s["repo"], s["kaynak_yol"]))
        for kk in s.get("kopya_kaynaklar", []):
            r, _, y = kk.partition(":")
            yol_index.add((r, "" if y == "." else y))

    sorunlar, satirlar, toplam = [], [], Counter()
    for repo in arsiv_repolari:
        d = denetim.get(repo)
        if not d:
            sorunlar.append(f"{repo}: denetim kaydı yok (kaynak-cek çalışmamış)")
            continue
        govde = gh_api(f"repos/{repo}/git/trees/{d['commit']}?recursive=1")
        if govde.get("truncated"):
            sorunlar.append(f"{repo}: GitHub ağacı kesik, bağımsız sayım yapılamadı")
        gercek = [e["path"] for e in govde["tree"] if e["type"] == "blob" and e["path"].split("/")[-1].lower() == "skill.md"]
        sayac = Counter()
        for p in gercek:
            karar = d["skill_md"].get(p)
            if karar is None or karar == "dahil-disi":
                sorunlar.append(f"{repo}: AÇIKLANAMAYAN SKILL.md -> {p}")
                sayac["ACIKLANAMAYAN"] += 1
                continue
            tur = karar.split(":")[0]
            sayac[tur] += 1
            if tur in ("secildi", "ayri-surum"):
                klasor = p.rsplit("/", 1)[0] if "/" in p else ""
                if (repo, klasor) not in yol_index:
                    sorunlar.append(f"{repo}: arşive seçildi ama registry'de yok -> {p}")
        for p in d["skill_md"]:
            if p not in gercek:
                sorunlar.append(f"{repo}: denetimde var ama ağaçta yok -> {p}")
        toplam.update(sayac)
        satirlar.append((repo, len(gercek), sayac))

    yeni_skill = []
    for repo in referans_repolari:
        g = gh_api(f"repos/{repo}/git/trees/HEAD?recursive=1")
        n = sum(1 for e in g.get("tree", []) if e["type"] == "blob" and e["path"].split("/")[-1].lower() == "skill.md")
        if n:
            yeni_skill.append((repo, n))
            sorunlar.append(f"{repo}: referans (T5/T6) reposunda {n} SKILL.md var -> kaynaklar.json'a skill kaydı ekle")

    out = ["# Kapsam Denetimi", "",
           f"> `araclar/kapsam-denetimi.py` üretir · {date.today().isoformat()} · Bağımsız kontrol: her repo için "
           "GitHub'daki tam dosya ağacı yeniden çekilip içindeki tüm SKILL.md dosyaları tek tek açıklandı.", "",
           f"**Sonuç: {'✅ Açıklanamayan skill yok' if not sorunlar else f'❌ {len(sorunlar)} sorun'}** · "
           f"Taranan SKILL.md: {sum(n for _, n, _ in satirlar)} · Arşivdeki skill kaydı: {len(reg['skiller'])} · "
           f"Bileşen (komut/agent): {len(reg.get('bilesenler', []))}", "",
           "| Karar | Sayı | Anlamı |", "|---|---|---|"]
    for k, v in toplam.most_common():
        out.append(f"| {k} | {v} | {ACIKLAMA.get(k, '')} |")
    out += ["", "## Repo bazında", "", "| Repo | SKILL.md | Dağılım |", "|---|---|---|"]
    for repo, n, s in satirlar:
        out.append(f"| {repo} | {n} | " + ", ".join(f"{k} {v}" for k, v in s.most_common()) + " |")
    out += ["", "## Referans repoları (T5/T6)", "",
            f"{len(referans_repolari)} repo tarandı; " +
            ("içlerinde skill yok." if not yeni_skill else "skill bulunanlar: " + ", ".join(f"{r} ({n})" for r, n in yeni_skill))]
    hariclar = defaultdict(list)
    for repo, d in denetim.items():
        for p, k in d["skill_md"].items():
            if k.startswith("haric"):
                hariclar[repo].append(f"`{p}` ({k.split(':', 1)[1]})")
    if hariclar:
        out += ["", "## Bilinçli hariç tutulanlar (gerekçeli)", ""]
        for repo, l in hariclar.items():
            out.append(f"- **{repo}**: " + ", ".join(l[:20]) + (f" … (+{len(l) - 20})" if len(l) > 20 else ""))
    if sorunlar:
        out += ["", "## Sorunlar", ""] + [f"- {x}" for x in sorunlar]
    (KOK / "notlar" / "kapsam-denetimi.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    for x in sorunlar:
        print("SORUN:", x)
    print(f"Taranan SKILL.md: {sum(n for _, n, _ in satirlar)} · sorun: {len(sorunlar)} · dağılım: {dict(toplam)}")
    sys.exit(1 if sorunlar else 0)


if __name__ == "__main__":
    main()
