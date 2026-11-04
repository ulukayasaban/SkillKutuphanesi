#!/usr/bin/env python3
"""Skill geliştiricisi (repo sahibi) bilgilerini GitHub'dan çeker -> gelistiriciler.json

Toplanan: sahip adı/tipi (kurum/kişi), yıldız, fork, izleyici, açık issue, son güncelleme, oluşturulma, lisans,
arşivlenmiş mi, açıklama, ana sayfa, katkıcı sayısı, son 90 gün commit sayısı, son sürüm (release) tarihi.

GÜVEN PUANI (0-100, 'guven'): GitHub etkileşimlerinin kütüphanedeki TÜM kaynaklar içindeki yüzdelik sırası:
  yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 ·
  son 180 günde sürüm 5 · lisans açık 5 · resmî üretici 5 (kurum 3)  [arşivlenmiş repo: puan yarıya iner]
  Derece: A ≥80 · B ≥65 · C ≥50 · D <50 — GÖRELİ: kütüphanedeki skill kaynakları (T1-T4) arasındaki yeri;
  'sira' = bu kaynaklar içindeki sırası (1 = en güvenilir). Referans kütüphaneleri (T5/T6) havuza girmez.
  Resmî olmak tek başına belirleyici değil (sadece 5 puan); topluluk etkileşimi ağırlıklı.
arsiv-yerlestir.py bu dosyayı okuyup her skill'e 'gelistirici' ve 'degerlendirme' ekler (güven = değerlendirmenin 30 puanı).

Kullanım: python3 araclar/gelistirici-bilgisi.py [--repo owner/ad …]   (--repo: sadece o repolar yenilenir)
"""
import re
import subprocess
import time
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KAYNAKLAR, KOK, api_kapali, gh_api, json_oku, json_yaz  # noqa: E402

# Teknolojinin kendi üreticisi olan kurumlar (resmî kaynak)
RESMI = {"anthropics", "greensock", "vercel", "microsoft", "pmndrs", "mrdoob", "motiondivision",
         "darkroomengineering", "tailwindlabs", "figma", "GoogleChrome", "dequelabs", "airbnb", "react",
         "FFmpeg", "QwikDev", "ComposioHQ", "heygen-com", "android", "expo", "vercel-labs", "cloudflare", "Shopify",
         "mercadopago", "Trendyol", "remotion-dev", "openai"}
# Ayrıca: sahip adı = repo adı (pixijs/pixijs, d3/d3, KaTeX/KaTeX, blender/blender…) teknolojinin kendi üreticisi sayılır (kural: resmi_mi)


def resmi_mi(repo, sahip_login):
    return sahip_login in RESMI or sahip_login.lower() == repo.split("/")[1].lower()


def gh_dene(komut, deneme=3):
    """gh çağrısı: geçici ağ/hız sınırı hatasında yeniden dener. Başarısızsa None (çağıran önceki değeri korur)."""
    for i in range(deneme):
        r = subprocess.run(komut, capture_output=True, text=True)
        if r.returncode == 0:
            return r
        if api_kapali(r.stderr):  # repo API'si bu oturumda kapalı: yeniden denemek anlamsız
            return None
        time.sleep(3 * (i + 1) if "rate limit" not in r.stderr.lower() else 60 * (i + 1))
    return None


def katkici_sayisi(repo):
    r = gh_dene(["gh", "api", "-i", f"repos/{repo}/contributors?per_page=1&anon=true"])
    if r is None:
        return None
    m = re.search(r'page=(\d+)>; rel="last"', r.stdout)
    return int(m.group(1)) if m else 1


def say(yol):
    """Sayfalı GitHub listesinin eleman sayısı (per_page=1 + Link başlığındaki son sayfa)."""
    r = gh_dene(["gh", "api", "-i", yol])
    if r is None:
        return None
    m = re.search(r'page=(\d+)>; rel="last"', r.stdout)
    return int(m.group(1)) if m else (0 if r.stdout.rstrip().endswith("[]") else 1)


def son_surum(repo):
    """Son sürüm tarihi; sürüm yoksa None, ÇAĞRI BAŞARISIZSA "?" (çağıran önceki değeri korur)."""
    r = gh_dene(["gh", "api", f"repos/{repo}/releases?per_page=1", "--jq", ".[0].published_at // empty"])
    if r is None:
        return "?"
    return r.stdout.strip()[:10] or None


def yuzdelik(degerler, x):
    """x, değerlerin yüzde kaçından büyük ya da eşit (0-1). None = 0."""
    d = [v for v in degerler if v is not None]
    if x is None or not d:
        return 0.0
    return sum(1 for v in d if v <= x) / len(d)


def guven_hesapla(sonuc, havuz, referans):
    """havuz: karşılaştırmanın yapıldığı skill kaynakları (T1-T4). Dev referans kütüphaneleri (React, three.js…)
    yüzdelikleri şişirmesin diye havuza girmez; onların puanı da bu havuza göre hesaplanır."""
    bugun = date.today()
    for v in sonuc.values():
        ay = max(1.0, (bugun - date.fromisoformat(v["olusturulma"])).days / 30.4)
        v["yildiz_hizi"] = round(v["yildiz"] / ay, 1)
    olc = {"yildiz": 25, "yildiz_hizi": 15, "katkici": 15, "commit_90g": 15, "fork": 10, "izleyici": 5}
    hepsi = {k: [sonuc[r].get(k) for r in havuz if r in sonuc] for k in olc}
    for v in sonuc.values():
        p, ay = 0.0, []
        for k, w in olc.items():
            q = yuzdelik(hepsi[k], v.get(k))
            p += w * q
            ay.append(f"{k} {v.get(k)} (%{round(q * 100)}) → {w * q:.1f}/{w}")
        sr = v.get("son_surum")
        s5 = 5 if sr and (bugun - date.fromisoformat(sr)).days <= 180 else 0
        lis = 5 if v["lisans"] not in ("yok", "NOASSERTION") else 0
        res = 5 if v["resmi_kaynak"] else 3 if v["sahip_tipi"] == "kurum" else 0
        p += s5 + lis + res
        ay += [f"son 180 günde sürüm {s5}/5", f"lisans {lis}/5", f"resmî/kurum {res}/5"]
        if v["arsivlenmis"]:
            p /= 2
            ay.append("arşivlenmiş repo: ×0.5")
        v["guven"] = {"puan": round(p), "ayrinti": ay}
    sirali = sorted((r for r in sonuc if r in havuz), key=lambda r: -sonuc[r]["guven"]["puan"])
    for i, r in enumerate(sirali, 1):
        sonuc[r]["guven"]["sira"], sonuc[r]["guven"]["toplam"] = i, len(sirali)
    # Referans kütüphaneleri (T5/T6: three.js, React, GSAP…) kendi aralarında sıralanır ("referans_sira")
    ref = sorted((r for r in sonuc if r not in havuz and r in referans), key=lambda r: -sonuc[r]["guven"]["puan"])
    for i, r in enumerate(ref, 1):
        g = sonuc[r]["guven"]
        g["sira"], g["toplam"] = None, len(sirali)
        g["referans_sira"], g["referans_toplam"] = i, len(ref)
    for v in sonuc.values():
        g = v["guven"]
        g["derece"] = "A" if g["puan"] >= 80 else "B" if g["puan"] >= 65 else "C" if g["puan"] >= 50 else "D"


def main():
    repolar = sorted({k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]})
    onceki = json_oku(KOK / "gelistiriciler.json", {"repolar": {}})["repolar"]
    secili = [a for a in sys.argv[1:] if "/" in a]  # --repo owner/ad …: sadece bunlar yenilenir, diğerleri önceki değerden
    sonuc = {r: onceki[r] for r in repolar if secili and r not in secili and r in onceki}
    if secili:
        repolar = [r for r in repolar if r in secili]
    for repo in repolar:
        try:
            try:
                d = gh_api(f"repos/{repo}")
            except RuntimeError as e:  # repo API'si kapalı (bulut oturumu) -> arama API'si aynı temel alanları verir
                if not any(x in str(e) for x in ("not enabled", "not available", "HTTP 403")):
                    raise
                d = (gh_api(f"search/repositories?q=repo:{repo}").get("items") or [None])[0]
                if not d:
                    raise RuntimeError(f"{repo} aramada bulunamadı") from e
                d.setdefault("subscribers_count", None)
                print(f"  {repo}: repo API'si kapalı, arama API'sinden temel bilgi alındı (katkıcı/commit/sürüm eski değerden)")
        except Exception as e:  # noqa: BLE001  ağ kesintisi / silinmiş repo: önceki bilgiyle devam
            if repo in onceki:
                sonuc[repo] = onceki[repo]
                print(f"UYARI: {repo} okunamadı, önceki bilgi kullanıldı ({str(e)[:80]})")
            else:
                print(f"UYARI: {repo} okunamadı ve önceki bilgi yok ({str(e)[:80]})")
            continue
        sahip = d["owner"]
        sonuc[repo] = {
            "sahip": sahip["login"],
            "sahip_tipi": "kurum" if sahip["type"] == "Organization" else "kisi",
            "sahip_url": sahip["html_url"],
            "resmi_kaynak": resmi_mi(repo, sahip["login"]),
            "yildiz": d["stargazers_count"], "fork": d["forks_count"], "acik_issue": d["open_issues_count"],
            "son_guncelleme": d["pushed_at"][:10], "olusturulma": d["created_at"][:10],
            "lisans": (d.get("license") or {}).get("spdx_id") or "yok",
            "arsivlenmis": d["archived"], "aciklama": d.get("description") or "",
            "ana_sayfa": d.get("homepage") or "", "katkici": katkici_sayisi(repo),
            "izleyici": d.get("subscribers_count"),
            "commit_90g": say(f"repos/{repo}/commits?per_page=1&since={date.fromordinal(date.today().toordinal() - 90)}T00:00:00Z"),
            "son_surum": son_surum(repo),
        }
        eski = onceki.get(repo) or {}
        for alan in ("katkici", "commit_90g", "izleyici", "son_surum"):  # geçici ağ hatası puanı sessizce düşürmesin
            if sonuc[repo].get(alan) in (None, "?"):
                sonuc[repo][alan] = eski.get(alan) if sonuc[repo].get(alan) == "?" or eski.get(alan) is not None else None
        print(f"{repo:42s} ★{d['stargazers_count']:>7}  {sonuc[repo]['sahip_tipi']:5s}  {sonuc[repo]['son_guncelleme']}")
    havuz = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T1", "T2", "T3", "T4")}
    referans = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T5", "T6")}
    guven_hesapla(sonuc, havuz, referans)
    print("\nGüven sıralaması (ilk 15):")
    for r in sorted((r for r in sonuc if sonuc[r]["guven"]["sira"]), key=lambda r: sonuc[r]["guven"]["sira"])[:15]:
        g = sonuc[r]["guven"]
        print(f"  #{g['sira']:<3} {r:44s} {g['puan']:3d} ({g['derece']})")
    json_yaz(KOK / "gelistiriciler.json", {"guncelleme": date.today().isoformat(), "repolar": sonuc})
    # notlar/guven-siralamasi.md'yi katalog-uret.py üretir (skill sayıları/kategoriler arsiv-yerlestir'den sonra kesinleşir)


if __name__ == "__main__":
    main()
