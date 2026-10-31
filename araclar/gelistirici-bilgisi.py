#!/usr/bin/env python3
"""Skill geliştiricisi (repo sahibi) bilgilerini GitHub'dan çeker -> gelistiriciler.json

Toplanan: sahip adı/tipi (kurum/kişi), yıldız, fork, açık issue, son güncelleme, oluşturulma, lisans,
arşivlenmiş mi, açıklama, ana sayfa, katkıcı sayısı (yaklaşık).
arsiv-yerlestir.py bu dosyayı okuyup her skill'e 'gelistirici' ve 'degerlendirme' ekler.

Kullanım: python3 araclar/gelistirici-bilgisi.py
"""
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, gh_api, json_oku, json_yaz  # noqa: E402

# Teknolojinin kendi üreticisi olan kurumlar (resmî kaynak)
RESMI = {"anthropics", "greensock", "vercel", "microsoft", "pmndrs", "mrdoob", "motiondivision",
         "darkroomengineering", "tailwindlabs", "figma", "GoogleChrome", "dequelabs", "airbnb", "react",
         "FFmpeg", "QwikDev", "ComposioHQ", "heygen-com", "android", "expo", "vercel-labs", "cloudflare", "Shopify",
         "mercadopago", "Trendyol"}


def katkici_sayisi(repo):
    r = subprocess.run(["gh", "api", "-i", f"repos/{repo}/contributors?per_page=1&anon=true"],
                       capture_output=True, text=True)
    m = re.search(r'page=(\d+)>; rel="last"', r.stdout)
    return int(m.group(1)) if m else (1 if r.returncode == 0 else None)


def main():
    repolar = sorted({k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]})
    sonuc = {}
    for repo in repolar:
        d = gh_api(f"repos/{repo}")
        sahip = d["owner"]
        sonuc[repo] = {
            "sahip": sahip["login"],
            "sahip_tipi": "kurum" if sahip["type"] == "Organization" else "kisi",
            "sahip_url": sahip["html_url"],
            "resmi_kaynak": sahip["login"] in RESMI,
            "yildiz": d["stargazers_count"], "fork": d["forks_count"], "acik_issue": d["open_issues_count"],
            "son_guncelleme": d["pushed_at"][:10], "olusturulma": d["created_at"][:10],
            "lisans": (d.get("license") or {}).get("spdx_id") or "yok",
            "arsivlenmis": d["archived"], "aciklama": d.get("description") or "",
            "ana_sayfa": d.get("homepage") or "", "katkici": katkici_sayisi(repo),
        }
        print(f"{repo:42s} ★{d['stargazers_count']:>7}  {sonuc[repo]['sahip_tipi']:5s}  {sonuc[repo]['son_guncelleme']}")
    json_yaz(KOK / "gelistiriciler.json", {"guncelleme": date.today().isoformat(), "repolar": sonuc})


if __name__ == "__main__":
    main()
