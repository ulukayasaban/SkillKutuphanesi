#!/usr/bin/env python3
"""GitHub Trending takibi: hangi skill repoları trend'e girmiş? (sadece okuma; GitHub'da hiçbir şeyi değiştirmez)

  python3 araclar/github-trend.py            # trending sayfalarını tara, trend.json geçmişine ekle, registry'deki
                                             # 'trend' alanlarını güncelle, rapor yaz
  python3 araclar/github-trend.py --rapor    # taramadan, mevcut trend.json'dan rapor
  python3 araclar/github-trend.py --aday     # + trend'deki ama kütüphanede olmayan repolarda SKILL.md say (aday listesi)

Trending anlık bir listedir; geçmiş sadece tarandıkça birikir (aylık güncellemede otomatik çalışır).
Etkisi: değerlendirme puanına bonus (ortak.TREND_BONUS, arsiv-yerlestir.py) ve skill-ekle --oner sıralamasında
konuya UYGUN skiller arasında öne alma. Trend tek başına bir skill'i öneriye sokmaz.
Çıktı: trend.json, notlar/github-trend.md
"""
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, REGISTRY, TREND, gh_api, json_oku, json_yaz, trend_durumu  # noqa: E402

DONEMLER = {"daily": "bugün", "weekly": "bu hafta", "monthly": "bu ay"}
# Skill repoları çoğunlukla dilsiz ya da Python/TS/JS/Shell olarak görünür; "" = tüm diller
DILLER = ["", "python", "typescript", "javascript", "shell"]


def sayfa(donem, dil):
    url = f"https://github.com/trending/{dil}?since={donem}" if dil else f"https://github.com/trending?since={donem}"
    istek = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 SkillKutuphanesi"})
    for i in range(3):
        try:
            with urllib.request.urlopen(istek, timeout=30) as r:
                return r.read().decode("utf-8", "ignore")
        except OSError:
            time.sleep(3 * (i + 1))
    return ""


def ayristir(html):
    sonuc = []
    for sira, a in enumerate(html.split('<article class="Box-row">')[1:], 1):
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"/\s]+/[^"/\s]+)"', a)
        if not m:
            continue
        st = re.search(r"([\d,]+) stars (today|this week|this month)", a)
        sonuc.append({"repo": m.group(1), "sira": sira, "artis": int(st.group(1).replace(",", "")) if st else 0})
    return sonuc


def tara(trend):
    bugun = date.today().isoformat()
    anlik, hata = {}, 0
    for donem in DONEMLER:
        for dil in DILLER:
            html = sayfa(donem, dil)
            if not html:
                hata += 1
                if hata == 1 and not anlik:  # ilk sayfa bile gelmiyorsa (ağ/proxy engeli) 15 sayfa × 3 deneme beklenmez
                    sys.exit("DURDU: github.com/trending okunamadı (ağ ya da proxy engeli; bulut oturumlarında olağan). "
                             "trend.json'a dokunulmadı. Alternatif: python3 araclar/populer-tarama.py (GitHub REST araması)")
                continue
            for x in ayristir(html):
                k = anlik.setdefault(x["repo"], {})
                if donem not in k or x["artis"] > k[donem]["artis"]:
                    k[donem] = {"artis": x["artis"], "sira": x["sira"], "dil": dil or "tümü"}
            time.sleep(1)
    if not anlik:
        sys.exit("DURDU: trending sayfaları okunamadı (ağ ya da sayfa yapısı değişti). trend.json'a dokunulmadı.")
    gecmis = trend.setdefault("gecmis", {})
    for repo, d in anlik.items():
        g = gecmis.setdefault(repo, {"ilk": bugun, "gorulme": 0, "en_iyi": {}})
        if g.get("son") != bugun:
            g["gorulme"] += 1
        g["son"] = bugun
        for donem, v in d.items():
            if v["artis"] >= g["en_iyi"].get(donem, {}).get("artis", -1):
                g["en_iyi"][donem] = {"artis": v["artis"], "tarih": bugun}
    trend["son_tarama"] = bugun
    trend["son_liste"] = anlik
    trend["taramalar"] = (trend.get("taramalar", []) + [{"tarih": bugun, "repo": len(anlik), "okunamayan_sayfa": hata}])[-60:]
    return anlik, hata


def registry_guncelle(trend):
    """Registry'deki her skill'e kaynağının trend durumunu yazar (arşive dokunmaz)."""
    reg = json_oku(REGISTRY)
    degisen = 0
    for s in reg["skiller"]:
        t = trend_durumu(s["repo"], trend)
        if s.get("trend") != t:
            degisen += 1
            if t:
                s["trend"] = t
            else:
                s.pop("trend", None)
    if degisen:
        json_yaz(REGISTRY, reg)
    return degisen


def aday_skill_sayisi(trend, repolar):
    onbellek = trend.setdefault("skill_sayisi", {})
    for repo in repolar:
        if repo in onbellek and onbellek[repo]["tarih"] == trend["son_tarama"]:
            continue
        try:
            g = gh_api(f"repos/{repo}/git/trees/HEAD?recursive=1")
            n = sum(1 for e in g.get("tree", []) if e["path"].split("/")[-1].lower() == "skill.md")
        except Exception:  # noqa: BLE001  (silinmiş/private repo)
            n = -1
        onbellek[repo] = {"skill": n, "tarih": trend["son_tarama"]}


def rapor(trend, aday_modu):
    kaynak = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
    reg = json_oku(REGISTRY)["skiller"]
    skill_say = {}
    for s in reg:
        skill_say[s["repo"]] = skill_say.get(s["repo"], 0) + 1
    son = trend.get("son_liste", {})

    def ozet(repo):
        d = son.get(repo) or {}
        return ", ".join(f"{DONEMLER[p]} +{v['artis']} (#{v['sira']} {v['dil']})" for p, v in d.items())

    satir = ["# GitHub Trend Takibi", "",
             f"> `araclar/github-trend.py` üretir · son tarama {trend.get('son_tarama', '—')} · "
             f"taranan dönemler: {', '.join(DONEMLER.values())} · diller: {', '.join(d or 'tümü' for d in DILLER)}", "",
             "Trend'e giren kaynakların skilleri değerlendirmede bonus alır (trendde +10, son 90 gün +6, daha eski +2) ve",
             "`skill-ekle.py --oner` sıralamasında konuya uygun skiller arasında öne çıkar. Trend tek başına öneri sebebi değildir.", "",
             "## Kütüphanedeki kaynaklardan trend'e girenler", "", "| Repo | Durum | Skill | Son görülme | İlk | Görülme | Şu an |",
             "|---|---|---|---|---|---|---|"]
    for repo in sorted(kaynak):
        t = trend_durumu(repo, trend)
        if t:
            satir.append(f"| {repo} | {t['seviye']} | {skill_say.get(repo, 0)} | {t['son']} | {t['ilk']} | {t['gorulme']} | {ozet(repo)} |")
    adaylar = sorted((r for r in son if r not in kaynak),
                     key=lambda r: -max(v["artis"] for v in son[r].values()))
    if aday_modu:
        aday_skill_sayisi(trend, adaylar)
    sayi = trend.get("skill_sayisi", {})
    satir += ["", "## Son taramada trend'de olup kütüphanede olmayan repolar", "",
              "Skill içerenler (SKILL.md > 0) aday kaynaktır: `rehber/03-yeni-skill-ekleme.md` (çakışma + ücret kontrolü, kullanıcı onayı).", "",
              "| Repo | SKILL.md | Şu an |", "|---|---|---|"]
    for repo in adaylar:
        n = sayi.get(repo, {}).get("skill")
        if aday_modu and not n:
            continue
        satir.append(f"| {repo} | {'?' if n is None else n} | {ozet(repo)} |")
    (KOK / "notlar" / "github-trend.md").write_text("\n".join(satir) + "\n", encoding="utf-8")
    return [(r, sayi.get(r, {}).get("skill")) for r in adaylar]


def main():
    trend = json_oku(TREND, {"_aciklama": "GitHub Trending geçmişi. araclar/github-trend.py üretir; elle düzenleme."})
    if "--rapor" not in sys.argv:
        anlik, hata = tara(trend)
        print(f"Tarandı: {len(anlik)} trend repo · okunamayan sayfa: {hata}")
    aday = rapor(trend, "--aday" in sys.argv)
    json_yaz(TREND, trend)
    print(f"registry'de trend alanı değişen skill: {registry_guncelle(trend)}")
    kaynak = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
    for repo in sorted(kaynak):
        t = trend_durumu(repo, trend)
        if t:
            print(f"  🔥 {repo}: {t['seviye']} (son {t['son']})")
    if "--aday" in sys.argv:
        print("Aday skill repoları (trend'de, kütüphanede yok):")
        for r, n in aday:
            if n:
                print(f"  + {r}: {n} SKILL.md")
    print("Rapor: notlar/github-trend.md")


if __name__ == "__main__":
    main()
