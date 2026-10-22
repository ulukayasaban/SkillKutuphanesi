#!/usr/bin/env python3
"""Konu takibi: belirli alanlardaki (ör. e-ticaret/Etsy, mobil) YENİ skill repolarını GitHub'da düzenli arar.
Sadece okur ve raporlar; kaynak EKLEMEZ, yıldız/liste değiştirmez.

  python3 araclar/konu-takip.py                # tüm konuları tara -> konu-takip.json + notlar/konu-takip.md
  python3 araclar/konu-takip.py --konu e-ticaret
  python3 araclar/konu-takip.py --rapor        # taramadan rapor
  python3 araclar/konu-takip.py --karar owner/ad reddedildi "neden"   # adayı değerlendirildi olarak işaretle
                                                                     # (eklendi | reddedildi | izle)

Konular ve arama sorguları: kaynaklar.json -> "takip_konulari". Her sorgu GitHub kod aramasında
"<sorgu> filename:SKILL.md" olarak aranır. Kütüphanede olan ve 'degerlendirilen' listesindeki repolar aday sayılmaz.
Aylık güncelleme (arsiv-guncelle.py --uygula) bunu otomatik çalıştırır. Aday eklemek: rehber/03-yeni-skill-ekleme.md.
"""
import json
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, TREND, json_oku, json_yaz, trend_durumu  # noqa: E402

DURUM = KOK / "konu-takip.json"
RAPOR = KOK / "notlar" / "konu-takip.md"


def kod_ara(sorgu):
    for i in range(4):  # GitHub kod araması sık sık 504/ikincil hız sınırı verir
        r = subprocess.run(["gh", "search", "code", f"{sorgu} filename:SKILL.md", "--limit", "100",
                            "--json", "repository,path"], capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout or "[]")
        time.sleep(8 * (i + 1))
    print(f"  ! arama yapılamadı: {sorgu}")
    return None


def repo_bilgisi(repo):
    r = subprocess.run(["gh", "api", f"repos/{repo}", "--jq",
                        "{yildiz:.stargazers_count,lisans:(.license.spdx_id//\"yok\"),son:.pushed_at[:10],"
                        "aciklama:((.description//\"\")[:140]),arsiv:.archived}"], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None


def tara(durum, ayar, secili):
    bugun = date.today().isoformat()
    for k in ayar["takip_konulari"]:
        if secili and k["konu"] != secili:
            continue
        print(f"# {k['konu']}: {len(k['sorgular'])} sorgu")
        hedef = durum.setdefault("konular", {}).setdefault(k["konu"], {"repolar": {}})
        basarisiz = 0
        for q in k["sorgular"]:
            sonuc = kod_ara(q)
            if sonuc is None:
                basarisiz += 1
                continue
            for x in sonuc:
                repo = x["repository"]["nameWithOwner"]
                r = hedef["repolar"].setdefault(repo, {"ilk": bugun, "sorgular": [], "skill_yollari": []})
                r["son"] = bugun
                if q not in r["sorgular"]:
                    r["sorgular"].append(q)
                if x["path"] not in r["skill_yollari"] and len(r["skill_yollari"]) < 50:
                    r["skill_yollari"].append(x["path"])
            time.sleep(2)
        hedef["son_tarama"] = bugun
        hedef["basarisiz_sorgu"] = basarisiz
        # Sadece aday olabileceklerin bilgisini çek (kütüphanede/değerlendirilmiş olanlar hariç)
        bilinen = bilinenler(durum)
        for repo, r in hedef["repolar"].items():
            if repo not in bilinen and r.get("bilgi_tarihi") != bugun:
                bilgi = repo_bilgisi(repo)
                if bilgi:
                    r.update(bilgi)
                    r["bilgi_tarihi"] = bugun


def bilinenler(durum):
    kaynak = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
    return kaynak | set(durum.get("degerlendirilen", {}))


def rapor(durum, ayar):
    kaynak = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
    deg = durum.get("degerlendirilen", {})
    trend = json_oku(TREND, {})
    satir = ["# Konu Takibi — yeni skill repoları", "",
             "> `araclar/konu-takip.py` üretir. Konular/sorgular: `kaynaklar.json` → `takip_konulari`. Adaylar otomatik EKLENMEZ; "
             "uygun olanlar `rehber/03-yeni-skill-ekleme.md` (çakışma + ücret kontrolü, kullanıcı onayı) ile eklenir. "
             "Değerlendirilen repo bir daha aday olarak gösterilmez: `konu-takip.py --karar owner/ad reddedildi \"neden\"`.", ""]
    for k in ayar["takip_konulari"]:
        h = durum.get("konular", {}).get(k["konu"], {})
        repolar = h.get("repolar", {})
        min_y = k.get("min_yildiz", 10)
        tum = [(r, v) for r, v in repolar.items() if r not in kaynak and r not in deg and not v.get("arsiv")
               and v.get("yildiz", 0) >= min_y]
        # Odaklı aday: repo adı/açıklaması konuya odaklı ("odak" regex). Dolaylı: konu kelimesi sadece birkaç SKILL.md'de geçiyor
        od = re.compile(k.get("odak", "."), re.I)
        aday = sorted(((r, v) for r, v in tum if od.search(r + " " + v.get("aciklama", ""))),
                      key=lambda x: (-len(x[1]["sorgular"]), -x[1].get("yildiz", 0)))
        dolayli = len(tum) - len(aday)
        dusuk = sum(1 for r, v in repolar.items() if r not in kaynak and r not in deg and v.get("yildiz", 0) < min_y)
        kutup = sorted(r for r in repolar if r in kaynak)
        satir += [f"## {k['konu']} → `{k['kategori']}`", "",
                  f"Son tarama: {h.get('son_tarama', '—')} · eşleşen repo: {len(repolar)} · kütüphanede: {len(kutup)} · "
                  f"değerlendirilmiş: {sum(1 for r in repolar if r in deg)} · **odaklı aday: {len(aday)}** · dolaylı eşleşme: {dolayli} "
                  f"(★{min_y} altı {dusuk} repo gösterilmez) · başarısız sorgu: {h.get('basarisiz_sorgu', 0)}", "",
                  "| Aday repo | ★ | Lisans | Son | Eşleşen SKILL.md | Sorgular | Trend | Açıklama |", "|---|---|---|---|---|---|---|---|"]
        for r, v in aday[:60]:
            t = trend_durumu(r, trend)
            satir.append(f"| {r} | {v.get('yildiz', '?')} | {v.get('lisans', '?')} | {v.get('son', '?')} | {len(v['skill_yollari'])} | "
                         f"{', '.join(v['sorgular'][:5])} | {t['seviye'] if t else '-'} | {v.get('aciklama', '').replace('|', '/')} |")
        satir.append("")
    satir += ["## Değerlendirilen repolar (aday olarak gösterilmez)", "", "| Repo | Karar | Tarih | Neden |", "|---|---|---|---|"]
    for r, v in sorted(deg.items()):
        satir.append(f"| {r} | {v['karar']} | {v['tarih']} | {v['neden'].replace('|', '/')} |")
    RAPOR.write_text("\n".join(satir) + "\n", encoding="utf-8")


def main():
    ayar = json_oku(KAYNAKLAR)
    durum = json_oku(DURUM, {"_aciklama": "araclar/konu-takip.py üretir. 'degerlendirilen' elle/--karar ile doldurulur."})
    if "--karar" in sys.argv:
        i = sys.argv.index("--karar")
        repo, karar, neden = sys.argv[i + 1], sys.argv[i + 2], " ".join(sys.argv[i + 3:]) or "-"
        if karar not in ("eklendi", "reddedildi", "izle"):
            sys.exit("karar: eklendi | reddedildi | izle")
        durum.setdefault("degerlendirilen", {})[repo] = {"karar": karar, "neden": neden, "tarih": date.today().isoformat()}
        if karar == "izle":  # izle = tekrar aday olarak görünsün
            durum["degerlendirilen"].pop(repo)
            durum.setdefault("izlenen", {})[repo] = {"neden": neden, "tarih": date.today().isoformat()}
    elif "--rapor" not in sys.argv:
        secili = sys.argv[sys.argv.index("--konu") + 1] if "--konu" in sys.argv else None
        tara(durum, ayar, secili)
    json_yaz(DURUM, durum)
    rapor(durum, ayar)
    for k in ayar["takip_konulari"]:
        h = durum.get("konular", {}).get(k["konu"], {})
        kaynak = {x["repo"] for x in ayar["repolar"]}
        od = re.compile(k.get("odak", "."), re.I)
        aday = [r for r, v in h.get("repolar", {}).items() if r not in kaynak and r not in durum.get("degerlendirilen", {})
                and v.get("yildiz", 0) >= k.get("min_yildiz", 10) and not v.get("arsiv") and od.search(r + " " + v.get("aciklama", ""))]
        print(f"{k['konu']}: {len(h.get('repolar', {}))} eşleşen repo · odaklı aday {len(aday)}")
    print(f"Rapor: {RAPOR.relative_to(KOK)}")


if __name__ == "__main__":
    main()
