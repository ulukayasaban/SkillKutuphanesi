#!/usr/bin/env python3
"""Kaynak türü ÖNERİSİ (yalnız okur; repo indirilmez, hiçbir dosya yazılmaz). notlar/plan-tur-surecleri.md bölüm 4.

  python3 araclar/tur-belirle.py owner/ad [--json]

Kod yalnız mekanik olanları karar verir: lisans yok, SKILL.md sayısı, 200 sınırı. Yargı isteyenler (kit, ürün+skil / repo-içi,
program, riskli) "AJAN KARAR VERİR" diye işaretlenir. Karar sırası: lisans yok (ne kökte ne skil klasörlerinde) -> EKLENMEZ; SKILL.md 0 -> referans; >=200 ->
dev-koleksiyon; skillerin yarısından fazlası köke bağlı -> kit ADAYI; skil dışı kaynak kodu çok -> urun-skil / repo-ici ADAYI;
1 SKILL.md -> tek-skil; birden çok -> koleksiyon.
Çıkış kodu: 0 öneri üretildi · 1 EKLENMEZ · 2 kullanım hatası / repo okunamadı.
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ortak  # noqa: E402

BOLUM = {"koleksiyon": "arsiv", "tek-skil": "arsiv", "urun-skil": "arsiv", "repo-ici": "arsiv", "dev-koleksiyon": "fihrist",
         "kit": "katalog", "program": "katalog", "referans": "not"}
DEV_SINIRI = 200
KOK_ORANI = 0.5            # skillerin bundan FAZLASI köke bağlıysa kit adayı
KOD_ORANI = 0.6            # skil dışı kod dosyası oranı (ve en az KOD_AZAMI dosya) -> ürün adayı
KOD_AZAMI = 20
ICERIK_ORNEK = 40          # içeriği okunan SKILL.md sayısı üst sınırı (büyük repolarda örnekleme)
BAKIMSIZ_AY = 12
KOD_UZANTILARI = frozenset(".py .js .jsx .ts .tsx .mjs .go .rs .java .kt .c .cc .cpp .h .hpp .rb .php .swift .cs .scala .lua .dart".split())
KOK_DEGIL = frozenset({"skills", "skill", ".claude", ".agents", ".codex", ".github", ".claude-plugin", "node_modules"})


def skil_klasorleri(agac):
    """SKILL.md içeren klasörler (kök için '')."""
    d = []
    for x in agac:
        if x["type"] == "blob" and x["path"].rsplit("/", 1)[-1].lower() == "skill.md":
            d.append(x["path"].rpartition("/")[0])
    return sorted(set(d))


def kok_atifi(skil_dizin, metin, agac):
    """Bu SKILL.md'nin skil klasörü DIŞINDA kalan bir yere atıf yapıp yapmadığı: (bool, kanıt).
    (a) `../` ile üst dizine çıkma; (b) kökteki bir klasör adıyla başlayan yol (ve bu ad skilin kendi klasöründe yoksa)."""
    if re.search(r"(?<![\w.])\.\./[\w.-]", metin):
        return True, "../"
    ust = {x["path"].split("/")[0] for x in agac if "/" in x["path"]} - KOK_DEGIL
    yerel = {x["path"][len(skil_dizin) + 1:].split("/")[0] for x in agac
             if skil_dizin and x["path"].startswith(skil_dizin + "/") and "/" in x["path"][len(skil_dizin) + 1:]}
    for m in re.finditer(r"(?<![\w/.:@~-])([\w.-]+)/[\w.-]+", metin):
        ad = m.group(1)
        if ad in ust and ad not in yerel and not (skil_dizin == ad or skil_dizin.startswith(ad + "/")):
            return True, f"{ad}/"
    return False, ""


def kod_orani(agac, dizinler):
    """(skil dışı kod dosyası, toplam kod dosyası). Kökte SKILL.md varsa her şey skil içindedir."""
    kodlar = [x["path"] for x in agac if x["type"] == "blob" and Path(x["path"]).suffix.lower() in KOD_UZANTILARI
              and "node_modules/" not in x["path"]]
    if "" in dizinler:
        return 0, len(kodlar)
    ic = [p for p in kodlar if any(p.startswith(d + "/") for d in dizinler)]
    return len(kodlar) - len(ic), len(kodlar)


def tur_karari(agac, icerikler, lisans, push_tarihi=None, bugun=None):
    """Saf karar işlevi (ağ yok). agac: GitHub ağaç girdileri; icerikler: {SKILL.md yolu: metin} (örnek olabilir);
    lisans: SPDX / 'belirtilmemiş' / 'NOASSERTION'. Döner: sözlük
    {tur, bolum, durum ('KESIN' | 'ADAY' | 'EKLENMEZ'), gerekce, ajan_karar: [...], uyarilar, isaretler: {...}}."""
    bugun = bugun or date.today()
    dizinler = skil_klasorleri(agac)
    n = len(dizinler)
    dosyalar = [x for x in agac if x["type"] == "blob"]
    medya = [x for x in dosyalar if ortak.medya_mi(x["path"])]
    yollar = [x["path"] for x in dosyalar]
    dis_kod, tum_kod = kod_orani(agac, dizinler)
    bagli = []
    for yol, metin in icerikler.items():
        evet, kanit = kok_atifi(yol.rpartition("/")[0], metin, agac)
        if evet:
            bagli.append((yol, kanit))
    bakimsiz = None
    if push_tarihi:
        try:
            t = datetime.fromisoformat(push_tarihi.replace("Z", "+00:00")).date()
            bakimsiz = (bugun - t).days > BAKIMSIZ_AY * 30
        except ValueError:
            pass
    isaretler = {
        "skill_md_sayisi": n,
        "skill_md_yollari": dizinler[:8] + (["..."] if n > 8 else []),
        "claude_plugin": any(p.startswith(".claude-plugin/") for p in yollar),
        "kok_package_json": "package.json" in yollar,
        "kok_pyproject": "pyproject.toml" in yollar,
        "kok_requirements": "requirements.txt" in yollar,
        "medya_dosya_sayisi": len(medya),
        "medya_mb": round(sum(x.get("size") or 0 for x in medya) / 1048576, 1),
        "toplam_mb": round(sum(x.get("size") or 0 for x in dosyalar) / 1048576, 1),
        "kod_dosyasi_skil_disi": dis_kod,
        "kod_dosyasi_toplam": tum_kod,
        "koke_bagli_skil": len(bagli),
        "icerigi_okunan_skil": len(icerikler),
        "koke_bagli_ornek": [f"{y} ({k})" for y, k in bagli[:3]],
        "skil_klasorunde_lisans_dosyasi": sum(1 for x in dosyalar if re.fullmatch(r"LICEN[SC]E(\.\w+)?", x["path"].rsplit("/", 1)[-1], re.I)
                                              and any(x["path"].startswith(d + "/") for d in dizinler if d)),
        "lisans": lisans,
        "son_push": push_tarihi,
        "bakimsiz": bakimsiz,
    }
    ajan = ["program mı / riskli mi (K-58): ajan bakar"]
    uyari = []
    if bakimsiz:
        uyari.append(f"bakımsız: son push {BAKIMSIZ_AY} aydan eski")
    if lisans in ("NOASSERTION", "OTHER"):
        ajan.append(f"lisans belirsiz ({lisans}): LICENSE dosyasını ajan okur ve karar verir")

    def sonuc(tur, durum, gerekce, ek=None):
        return {"tur": tur, "bolum": BOLUM.get(tur), "durum": durum, "gerekce": gerekce,
                "ajan_karar": (ek or []) + ajan, "uyarilar": uyari, "isaretler": isaretler}

    isaretler["lisans_skil_basina"] = False
    if lisans in (None, "", "belirtilmemiş", "none", "None"):
        if not isaretler["skil_klasorunde_lisans_dosyasi"]:
            return sonuc(None, "EKLENMEZ", "EKLENMEZ: lisans yok (ne kökte ne skil klasörlerinde)")
        # Kökte lisans yok ama skil klasörlerinde LICENSE var: normal tür önerisi üretilir, lisans skil başına bakılır.
        isaretler["lisans_skil_basina"] = True
        ajan.append(f"lisans skil başına: kökte lisans yok, {isaretler['skil_klasorunde_lisans_dosyasi']} LICENSE dosyası skil klasörlerinde; "
                    "her skilin lisansını ajan okur (lisanssız skil alınmaz) ve kayda skil başına yazar")
        uyari.append("kök lisansı yok: lisans skil başına")
    if n == 0:
        return sonuc("referans", "KESIN", "SKILL.md yok: bilinmeye değer bir araçsa referans, değilse alınmaz")
    if n >= DEV_SINIRI:
        return sonuc("dev-koleksiyon", "KESIN", f"{n} SKILL.md (>= {DEV_SINIRI}): fihrist")
    if icerikler and len(bagli) > KOK_ORANI * len(icerikler):
        return sonuc("kit", "ADAY", f"okunan {len(icerikler)} skilin {len(bagli)} tanesi skil klasörü dışına/köke atıf yapıyor",
                     ["kit mi? AJAN KARAR VERİR (skiller kök klasörlere, ayarlara, betiklere mi bağlı; tek başına kurulur mu)"])
    if tum_kod and dis_kod >= KOD_AZAMI and dis_kod / tum_kod >= KOD_ORANI:
        return sonuc("urun-skil", "ADAY", f"skil dışı {dis_kod}/{tum_kod} kod dosyası: asıl iş bir yazılım",
                     ["urun-skil mi repo-ici mi? AJAN KARAR VERİR (skiller yazılımın kullanıcıları için mi: urun-skil; "
                      "geliştiricileri için mi: repo-ici, alınmaz)"])
    if n == 1:
        return sonuc("tek-skil", "KESIN", "1 SKILL.md")
    return sonuc("koleksiyon", "KESIN", f"{n} bağımsız SKILL.md")


def repo_oku(repo):
    """Ağ: (agac, icerikler, lisans, push_tarihi, sha). Dosya İNDİRİLMEZ; yalnız ağaç listesi ve en çok ICERIK_ORNEK SKILL.md metni."""
    sha, govde = ortak.repo_agaci(repo)
    agac = govde["tree"]
    lisans = ortak.repo_lisansi(repo, agac)
    try:
        push = ortak.gh_api(f"repos/{repo}").get("pushed_at")
    except RuntimeError:
        push = None
    yollar = sorted(x["path"] for x in agac if x["type"] == "blob" and x["path"].rsplit("/", 1)[-1].lower() == "skill.md")
    adim = max(1, len(yollar) // ICERIK_ORNEK)
    ornek = yollar[::adim][:ICERIK_ORNEK]
    with ThreadPoolExecutor(8) as ex:
        metinler = list(ex.map(lambda y: ortak.ham_metin(repo, y, sha, 60_000), ornek))
    icerikler = {y: m for y, m in zip(ornek, metinler) if m}
    ortak.klon_temizle(govde)
    return agac, icerikler, lisans, push, sha


def yaz(repo, r, sha):
    i = r["isaretler"]
    ev = lambda b: "var" if b else "yok"  # noqa: E731
    print(f"{repo}  (commit {str(sha)[:9]})")
    if r["durum"] == "EKLENMEZ":
        print(f"  ÖNERİ: {r['gerekce']}")
    else:
        print(f"  ÖNERİ: tür {r['tur']} ({r['durum']})  ·  bölüm {r['bolum']}")
        print(f"  gerekçe: {r['gerekce']}")
    print("  işaretler:")
    print(f"    SKILL.md: {i['skill_md_sayisi']}  {', '.join(i['skill_md_yollari'])}")
    print(f"    .claude-plugin: {ev(i['claude_plugin'])}  ·  kök package.json: {ev(i['kok_package_json'])}"
          f"  ·  pyproject.toml: {ev(i['kok_pyproject'])}  ·  requirements.txt: {ev(i['kok_requirements'])}")
    print(f"    medya: {i['medya_dosya_sayisi']} dosya, {i['medya_mb']} MB  ·  repo (dosya toplamı): {i['toplam_mb']} MB")
    print(f"    kod dosyası: skil dışı {i['kod_dosyasi_skil_disi']} / toplam {i['kod_dosyasi_toplam']}")
    print(f"    köke bağlı skil: {i['koke_bagli_skil']} / okunan {i['icerigi_okunan_skil']}  {'; '.join(i['koke_bagli_ornek'])}")
    print(f"    alt klasörlerdeki LICENSE dosyası: {i['skil_klasorunde_lisans_dosyasi']}")
    print(f"    lisans: {i['lisans']}" + ("  (skil başına)" if i.get("lisans_skil_basina") else "") + f"  ·  son push: {i['son_push']}" + ("  ·  BAKIMSIZ" if i["bakimsiz"] else ""))
    for u in r["uyarilar"]:
        print(f"  UYARI: {u}")
    for a in r["ajan_karar"]:
        print(f"  AJAN KARAR VERİR: {a}")


def main():
    ap = argparse.ArgumentParser(description="Kaynak türü önerisi (yalnız okur)")
    ap.add_argument("repo", help="owner/ad")
    ap.add_argument("--json", action="store_true", help="tek JSON nesnesi yaz")
    a = ap.parse_args()
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", a.repo):
        print("repo 'owner/ad' biçiminde olmalı", file=sys.stderr)
        return 2
    try:
        agac, icerikler, lisans, push, sha = repo_oku(a.repo)
    except (RuntimeError, OSError) as e:
        print(f"HATA: {a.repo} okunamadı: {e}", file=sys.stderr)
        return 2
    r = tur_karari(agac, icerikler, lisans, push)
    r["repo"], r["commit"] = a.repo, sha
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        yaz(a.repo, r, sha)
    return 1 if r["durum"] == "EKLENMEZ" else 0


if __name__ == "__main__":
    sys.exit(main())
