#!/usr/bin/env python3
"""GitHub'da popüler skill repolarını tarar (sadece okuma; hiçbir şey eklemez) -> notlar/populer-skiller.md

  python3 araclar/populer-tarama.py                 # tara, raporla (sayımlar .gecici/populer-tarama.json'da önbelleklenir)
  python3 araclar/populer-tarama.py --min-yildiz 300 --gun 90
  python3 araclar/populer-tarama.py --karar owner/ad reddedildi "neden"   # konu-takip.py ile aynı karar defteri

Yıldız listesi (GraphQL) ve github.com/trending (HTML) bazı ortamlarda (ör. bulut oturumu, kısıtlı ağ) okunamaz; bu araç
sadece GitHub REST aramasını kullanır: `search/repositories` (skill konulu sorgular) + `search/code filename:SKILL.md repo:X`
(adayda gerçekten skill var mı, kaç tane). Kütüphanedeki, bilerek çıkarılan ve daha önce reddedilen repolar elenir.
Adaylar onaysız eklenmez: uygun olanlar rehber/03-yeni-skill-ekleme.md adımlarıyla (çakışma + ücret kontrolü) eklenir.
"""
import argparse
import json
import re
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GECICI, KAYNAKLAR, KOK, json_oku, json_yaz  # noqa: E402

RAPOR = KOK / "notlar" / "populer-skiller.md"
ONBELLEK = GECICI / "populer-tarama.json"
KARARLAR = KOK / "konu-takip.json"  # konu-takip.py ile ortak 'degerlendirilen' defteri
SORGULAR = ["agent skills SKILL.md", "claude code skills", "codex skills", "awesome agent skills", "topic:agent-skills",
            "topic:claude-skills", "topic:claude-code-skills", "topic:agentskills", "skills claude in:name",
            "skill.md in:readme stars:>200", "skills marketplace agents", "skills registry claude codex cursor",
            "cursor rules skills agent", "gemini cli skills", "copilot agent skills"]
ILGILI = re.compile(r"skill|agent|claude|codex|cursor|copilot|gemini|plugin|prompt", re.I)


def gh(yol, **param):
    komut = ["gh", "api", "-X", "GET", yol]
    for k, v in param.items():
        komut += ["-f", f"{k}={v}"]
    for deneme in range(4):
        r = subprocess.run(komut, capture_output=True, text=True)
        if r.returncode == 0:
            try:
                return json.loads(r.stdout)
            except ValueError:
                return None
        if "rate limit" in r.stderr.lower() or "HTTP 403" in r.stderr or "HTTP 429" in r.stderr:
            time.sleep(65 * (deneme + 1))
        else:
            return None
    return None


def repo_ara(sorgular, gun, min_yildiz):
    bulunan = {}
    tarih = (date.today() - timedelta(days=gun)).isoformat()
    for s in sorgular:
        d = gh("search/repositories", q=f"{s} pushed:>{tarih} stars:>={min_yildiz}", sort="stars", per_page="50")
        for it in (d or {}).get("items", []):
            r = bulunan.setdefault(it["full_name"], {"yildiz": it["stargazers_count"], "son": it["pushed_at"][:10],
                                                      "olusturma": it["created_at"][:10], "lisans": (it.get("license") or {}).get("spdx_id") or "yok",
                                                      "aciklama": re.sub(r"\s+", " ", it.get("description") or "")[:160],
                                                      "konular": it.get("topics") or [], "sorgular": []})
            r["sorgular"].append(s)
        time.sleep(1.5)
    return bulunan


def skill_sayisi(repo, onbellek):
    k = onbellek.get(repo)
    if k and k.get("tarih") == date.today().isoformat():
        return k["skill_md"]
    d = gh("search/code", q=f"filename:SKILL.md repo:{repo}")
    n = d.get("total_count") if isinstance(d, dict) else None
    onbellek[repo] = {"skill_md": n, "tarih": date.today().isoformat()}
    time.sleep(2.2)  # code search: ~30 istek/dk
    return n


def main():
    if "-h" in sys.argv or "--help" in sys.argv:  # yardım istenince tarama başlatma
        print(__doc__ or "populer-tarama.py: kullanım için dosyanın başındaki açıklamaya bakın (-h ağ işi yapmaz, dosya yazmaz).")
        return 0
    ap = argparse.ArgumentParser(description="GitHub'da popüler skill repoları (salt okuma)")
    ap.add_argument("--min-yildiz", type=int, default=150)
    ap.add_argument("--gun", type=int, default=120, help="son N günde push almış repolar")
    ap.add_argument("--karar", nargs=3, metavar=("REPO", "KARAR", "NEDEN"))
    a = ap.parse_args()
    kararlar = json_oku(KARARLAR, {"degerlendirilen": {}})
    if a.karar:
        repo, karar, neden = a.karar
        if karar not in ("eklendi", "reddedildi", "izle"):
            sys.exit("karar: eklendi | reddedildi | izle")
        kararlar.setdefault("degerlendirilen", {})[repo] = {"karar": karar, "neden": neden, "tarih": date.today().isoformat()}
        json_yaz(KARARLAR, kararlar)
        print(f"kaydedildi: {repo} -> {karar}")
        return 0
    ayar = json_oku(KAYNAKLAR)
    var = {r["repo"].lower() for r in ayar["repolar"]}
    cik = {(x if isinstance(x, str) else x.get("repo", "")).lower() for x in ayar.get("arsivden_cikarilan_repolar", [])}
    degerlendirilen = {k.lower(): v for k, v in kararlar.get("degerlendirilen", {}).items()}
    GECICI.mkdir(exist_ok=True)
    onbellek = json_oku(ONBELLEK, {})
    bulunan = repo_ara(SORGULAR, a.gun, a.min_yildiz)
    aday = {r: v for r, v in bulunan.items() if r.lower() not in var | cik and ILGILI.search(r + " " + v["aciklama"] + " ".join(v["konular"]))}
    print(f"arama: {len(bulunan)} repo · kütüphanede {sum(1 for r in bulunan if r.lower() in var)} · aday {len(aday)}", flush=True)
    for i, r in enumerate(sorted(aday, key=lambda x: -aday[x]["yildiz"]), 1):
        aday[r]["skill_md"] = skill_sayisi(r, onbellek)
        if i % 25 == 0:
            json_yaz(ONBELLEK, onbellek)
            print(f"  {i}/{len(aday)} sayıldı", flush=True)
    json_yaz(ONBELLEK, onbellek)
    skilli = {r: v for r, v in aday.items() if (v["skill_md"] or 0) >= 1}
    yeni = {r: v for r, v in skilli.items() if r.lower() not in degerlendirilen}
    eski = {r: v for r, v in skilli.items() if r.lower() in degerlendirilen}
    kutuphanede = sorted((r, v) for r, v in bulunan.items() if r.lower() in var)

    def satir(r, v):
        return (f"| [{r}](https://github.com/{r}) | {v['yildiz']} | {v['skill_md']} | {v['lisans']} | {v['son']} | {v['olusturma']} | "
                f"{v['aciklama'][:120].replace('|', '/')} |\n")
    m = [f"# Popüler skill repoları (GitHub REST araması)\n\n> `araclar/populer-tarama.py` üretir · {date.today()} · "
         f"{len(SORGULAR)} sorgu · son {a.gun} günde push almış, ★{a.min_yildiz}+ · adayda `SKILL.md` sayısı `search/code` ile sayıldı. "
         "Yıldız listesi ve trending'den bağımsızdır (onlar okunamadığında da çalışır). **Adaylar otomatik eklenmez**; uygun olanlar "
         "`rehber/03-yeni-skill-ekleme.md` ile (çakışma + ücret kontrolü, onay) eklenir. Değerlendirilen repo bir daha çıkmaz: "
         "`--karar owner/ad reddedildi \"neden\"`.\n\n",
         f"## Yeni adaylar ({len(yeni)}) — içinde SKILL.md olan, kütüphanede olmayan, değerlendirilmemiş\n"
         "| Repo | ★ | SKILL.md | Lisans | Son push | Oluşturma | Açıklama |\n|---|---|---|---|---|---|---|\n"
         + "".join(satir(r, v) for r, v in sorted(yeni.items(), key=lambda x: -x[1]["yildiz"])) + "\n",
         f"## Skill içermeyen eşleşmeler ({len(aday) - len(skilli)})\nAramaya takılan ama `SKILL.md` içermeyen repolar (araç, liste, uygulama): "
         + ", ".join(f"`{r}`" for r, _ in sorted(((r, v) for r, v in aday.items() if not v['skill_md']), key=lambda x: -x[1]['yildiz'])[:60]) + "\n\n",
         f"## Daha önce değerlendirilenler ({len(eski)})\n" + "".join(
             f"- `{r}` ★{v['yildiz']} · {degerlendirilen[r.lower()]['karar']}: {degerlendirilen[r.lower()].get('neden', '')}\n"
             for r, v in sorted(eski.items(), key=lambda x: -x[1]['yildiz'])) + "\n",
         f"## Kütüphanedeki kaynaklardan aramada çıkanlar ({len(kutuphanede)})\n"
         + ", ".join(f"`{r}` ★{v['yildiz']}" for r, v in sorted(kutuphanede, key=lambda x: -x[1]['yildiz'])) + "\n"]
    RAPOR.write_text("".join(m), encoding="utf-8")
    print(f"{RAPOR.relative_to(KOK)}: yeni aday {len(yeni)} · skill'siz {len(aday) - len(skilli)} · değerlendirilmiş {len(eski)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
