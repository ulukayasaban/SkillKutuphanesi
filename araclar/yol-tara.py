#!/usr/bin/env python3
"""Sabit yol taraması (salt okuma): skill metinlerinde bilgisayar geneli klasör yolu (~/.claude/skills/<ad>/…), eklenti kökü
(${CLAUDE_PLUGIN_ROOT}/…), kardeş skill yolu (../<kardeş>/…) ve genel klasöre yazma (npx skills -g, cp … ~/.claude/skills) var mı?
Hiçbir şey kurmaz, indirmez, arşive ve registry'ye dokunmaz. Çıkış kodu HER ZAMAN 0 (hata olursa 'UYARI: …' yazar; bayrak hatasında kullanım metni yazılır).
Kapsam dışı: kodda `Path.home() / ".agents" / "skills" / …` gibi kurulan yollar ve öneksiz göreli yollar (skills/<ad>/…) taranmaz.

Kullanım:
  python3 araclar/yol-tara.py                  tüm arşivi tarar -> notlar/yol-denetimi.md (tek yazılan dosya)
  python3 araclar/yol-tara.py --skill <id>     tek skill'in ayrıntısı (stdout; dosya yazmaz): bulgular, ön kontrol satırları, istisna taslağı
  python3 araclar/yol-tara.py --repo owner/ad  repodaki tüm skiller (stdout). Repo registry'de yoksa taze çekilmiş .gecici/cekilen
                                               malzemesini tarar (kaynak-cek.py --repo sonrası, arsiv-yerlestir.py öncesi)
Kural 6: raporda proje adı geçmez; skill'in yolu kendi niteliğidir.
"""
import argparse
import re
import sys
import time
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ortak  # noqa: E402
from ortak import GECICI, KOK, REGISTRY, json_oku  # noqa: E402

SUTUNLAR = (("kurulumda-duzelir", "Kurulumda düzelir", "kurulan kopyada yol proje içi yola çevrilecek"),
            ("kardesle-duzelir", "Kardeşle düzelir", "aynı repodaki kardeş skill de kurulursa yol tutar"),
            ("paket-gerekli", "Paket gerekli", "dosya arşive alınmamış (eklenti kökü / kardeşte ya da kendinde eksik)"),
            ("cozulemez", "Çözülemez", "otomatik çevrilmiyor ya da hedef bulunamıyor: elle bakılmalı"),
            ("istisna", "İstisna", "yol-istisnalari.json kaydıyla kapsanmış"))


def md(x, n=150):
    x = re.sub(r"\s+", " ", str(x)).strip()
    return (x[:n - 1] + "…" if len(x) > n else x).replace("|", "\\|")


def skiller_yukle():
    return json_oku(REGISTRY)["skiller"]


def degerlendir_hepsi(skiller):
    sonuc, hata = {}, 0
    for s in skiller:
        try:
            sonuc[s["id"]] = ortak.yol_degerlendir(s, skiller)
        except Exception as e:  # noqa: BLE001  tek skill raporu düşürmez
            hata += 1
            print(f"UYARI: {s['id']}: taranamadı ({type(e).__name__}: {str(e)[:100]})")
    return sonuc, hata


def rapor_uret(skiller, sonuc):
    by_id = {s["id"]: s for s in skiller}
    tur_bulgu, tur_skill, tur_dokuman = Counter(), Counter(), Counter()
    kod_skill, sutun_say = Counter(), Counter()
    for sid, d in sonuc.items():
        sutun_say[d["sutun"]] += 1
        for t, n in d["sayim"].items():
            tur_bulgu[t] += n
            tur_skill[t] += 1
        for sv, kod in {(sv, kod) for sv, kod, _ in d["satirlar"]}:
            kod_skill[(sv, kod)] += 1
    for s in skiller:  # doküman sınıfı bulgu sayısı: ayrı sayım için tekrar okunur (önbellekten gelir)
        for b in ortak.skill_yol_taramasi(s, skiller):
            if b["sinif"] == "dokuman":
                tur_dokuman[b["tur"]] += 1
    o = ["# Yol Denetimi", "",
         f"> `araclar/yol-tara.py` üretir · {date.today().isoformat()} · salt okuma. Skill metinlerindeki sabit genel yol / eklenti kökü / "
         "kardeş yol bağımlılıkları. Ayrıntı: `python3 araclar/yol-tara.py --skill <id>`; istisna: `yol-istisnalari.json`.", "",
         f"**{len(sonuc)} skill tarandı** · bulgusu olan: {sum(1 for d in sonuc.values() if d['sutun'] != 'temiz')} · "
         f"ön kontrolde UYARI alan: {sum(1 for d in sonuc.values() if any(x[0] == 'UYARI' for x in d['satirlar']))}", "",
         "## Bulgu türleri", "", "| Tür | Bulgu | Skill | Doküman sınıfında |", "|---|---:|---:|---:|"]
    o += [f"| {t} | {tur_bulgu[t]} | {tur_skill[t]} | {tur_dokuman[t]} |" for t in sorted(tur_bulgu)]
    o += ["", "Yalnız sayılan türler (ön kontrolde satır üretmez): ornek-metin, genel-kalip, eklenti-kok-anma, kurulum bandındaki genele-yazar; "
          "doküman sınıfı (README, NOTICE, dil klasörleri, atıfsız dosyalar) bulguları da yalnız sayılır. Kapsam dışı (taranmaz): kodda "
          "`Path.home() / \".agents\" / \"skills\"` gibi çalışma anında kurulan yollar, öneksiz göreli yollar (`skills/<ad>/…`), `.copilot` gibi "
          "başka kök klasörler, Windows yolları.", "",
          "## Ön kontrol kodları (kaç skilde)", "", "| Seviye | Kod | Skill |", "|---|---|---:|"]
    o += [f"| {sv} | {kod} | {n} |" for (sv, kod), n in sorted(kod_skill.items())]
    o += ["", "## Sütunlar", "", "| Sütun | Skill |", "|---|---:|"]
    for k, ad, _ in SUTUNLAR:
        o.append(f"| {ad} | {sutun_say[k]} |")
    o += [f"| Yalnız sayım (satır yok) | {sutun_say['yalniz-sayim']} |", f"| Temiz | {sutun_say['temiz']} |"]
    for k, ad, aciklama in SUTUNLAR:
        uyeler = sorted(sid for sid, d in sonuc.items() if d["sutun"] == k)
        o += ["", f"## {ad} ({len(uyeler)})", "", f"_{aciklama}._", ""]
        if not uyeler:
            o.append("(yok)")
            continue
        o += ["| Skill | Repo | Kodlar | İlk neden |", "|---|---|---|---|"]
        for sid in uyeler:
            satir = sorted(sonuc[sid]["satirlar"], key=lambda x: (x[0] != "UYARI", x[1]))
            kodlar = ", ".join(sorted({x[1] for x in satir}))
            ilk = next(((sv, kod, g) for sv, kod, g in satir if sv == "UYARI"), satir[0] if satir else ("", "", ""))
            o.append(f"| {sid} | {by_id[sid]['repo']} | {kodlar} | {md(ilk[2])} |")
    uyari_genele = sorted(sid for sid, d in sonuc.items() if any(x[1] == "genele-yazabilir" and x[0] == "UYARI" for x in d["satirlar"]))
    o += ["", f"## Genel klasöre dosya kopyalayabilen skiller ({len(uyari_genele)})", "",
          "Ajan dosyasında `cp / ln -s / mkdir -p / git clone … ~/.claude/skills` satırı var (sütunlardan bağımsız bilgi).", "",
          ", ".join(uyari_genele) if uyari_genele else "(yok)"]
    paket = sorted((by_id[sid]["repo"], sid) for sid, d in sonuc.items()
                   if any(x[1] == "eklenti-koku" for x in d["satirlar"]) or d["sutun"] == "paket-gerekli")
    repo_say = Counter(r for r, _ in paket)
    o += ["", "## Sonraki tur adayı: eklenti kökü dosyalarını arşive almak (`ek_dosyalar`)", "",
          "Bu turda YAPILMADI: kök dosyaları (scripts/, docs/, templates/ …) çekmek lisans ve ücret sınıflandırması onayı ister "
          "(`ucret-siniflandirma.json`, `notlar/ucretli-skiller.md`). Aday sayısı repo bazında:", "",
          "| Repo | Skill |", "|---|---:|"]
    o += [f"| {r} | {n} |" for r, n in sorted(repo_say.items())]
    return "\n".join(o) + "\n"


def rapor_yaz(metin):
    hedef = KOK / "notlar" / "yol-denetimi.md"
    tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
    if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(metin):
        hedef.write_text(metin, encoding="utf-8")
        return True
    return False


def bulgu_yaz(b):
    ek = f" alt={b['alt']}" if b.get("alt") else ""
    kd = f" kardes={b['kardes_id']}" if b.get("kardes_id") else ""
    print(f"  [{b['tur']}] {b['dosya']}:{b['satir']} sinif={b['sinif']} engel={b['engel']} var={b['var']} cevrilebilir={b['cevrilebilir']}"
          f" hedef={b['hedef']!r} kalan={b['kalan']!r}{ek}{kd}\n      ham: {b['ham'][:160]}")


def skill_ayrinti(s, skiller):
    print(f"=== {s['id']} ({s['repo']} :: {s.get('kaynak_yol')})")
    bulgular = ortak.skill_yol_taramasi(s, skiller)
    print(f"{len(bulgular)} bulgu · skill adları: {sorted(ortak.skill_adlari(s, skiller))}")
    for b in bulgular:
        bulgu_yaz(b)
    d = ortak.yol_degerlendir(s, skiller)
    print(f"\nÖn kontrol satırları (kurulacak_idler bilinmiyor) · sütun: {d['sutun']} · sayım: {d['sayim']}")
    for sv, kod, g in d["satirlar"]:
        print(f"  {sv} {kod}: {s['id']}: {g}")
    if not d["satirlar"]:
        print("  (satır yok)")
    if d["cevrilecek"]:
        print(f"  kurulumda çevrilecek: {len(d['cevrilecek'])} yol")
    print(f"\nistisna anahtarı: {ortak.istisna_anahtari(s)}")
    for tur in sorted({b["tur"] for b in bulgular}):
        grup = [b for b in bulgular if b["tur"] == tur]
        hedefler = sorted({b["hedef"] for b in grup if b["hedef"]})
        alan, deger = ("hedefler", hedefler) if hedefler and all(b["hedef"] for b in grup) else ("dosyalar", sorted({b["dosya"] for b in grup}))
        kayit = {"tur": tur, alan: deger, "karar": "ornek-metin"}
        h = ortak.bulgu_hash(ortak.istisna_kapsami(kayit, bulgular))
        print(f"  bulgu_hash[{tur}] ({len(grup)} bulgu, {alan}={deger[:4]}{'…' if len(deger) > 4 else ''}) = {h}")
    istisna = (ortak.yol_istisnalari().get(ortak.istisna_anahtari(s)) or {}).get("kayitlar")
    if istisna:
        print(f"  mevcut istisna kaydı: {len(istisna)} kayıt")


def gecici_skiller(repo, kayitlar):
    """Taze çekilmiş (.gecici/cekilen) kayıtlardan, taramaya uygun sahte skill kayıtları: yol mutlak (KOK / yol -> mutlak yol)."""
    sonuc = []
    for k in kayitlar:
        klasor = GECICI / k["yerel"]
        if klasor.is_dir():
            sonuc.append({"id": "gecici:" + k["klasor_adi"], "ad": k.get("ad") or k["klasor_adi"], "klasor_adi": k["klasor_adi"],
                          "kaynak_yol": k.get("kaynak_yol", ""), "repo": k["repo"], "yol": str(klasor), "klasor_hash": "gecici"})
    return sonuc


def repo_ayrinti(repo, skiller):
    repo_k = ortak.repo_guncel(repo).lower()
    secilen = [s for s in skiller if s["repo"].lower() == repo_k]
    if secilen:
        print(f"# {repo}: registry'de {len(secilen)} skill")
        tum = skiller
    else:
        manifest = json_oku(GECICI / "cekilen" / "manifest.json", {"kayitlar": []})
        secilen = gecici_skiller(repo, [k for k in manifest.get("kayitlar", []) if k["repo"].lower() == repo.lower()])
        if not secilen:
            print(f"{repo}: ne registry'de ne de .gecici/cekilen içinde bulundu. Önce: python3 araclar/kaynak-cek.py --repo {repo}")
            return
        print(f"# {repo}: registry'de yok; .gecici/cekilen içindeki {len(secilen)} taze skill taranıyor (arşive girmeden önce)")
        tum = skiller + secilen
    for s in sorted(secilen, key=lambda x: x["id"]):
        skill_ayrinti(s, tum)
        print()


def main():
    ap = argparse.ArgumentParser(description="Sabit yol taraması (salt okuma)")
    ap.add_argument("--skill")
    ap.add_argument("--repo")
    try:
        a = ap.parse_args()
    except SystemExit as e:  # argparse hatası (bilinmeyen bayrak, değersiz --skill): kullanım metni yazıldı, çıkış kodu yine 0
        return 0 if e.code in (0, 2, None) else e.code
    t0 = time.time()
    try:
        skiller = skiller_yukle()
        if a.skill:
            s = next((x for x in skiller if x["id"] == a.skill), None) or next((x for x in skiller if x["ad"] == a.skill and x["durum"] == "tercih"), None)
            if not s:
                print(f"Skill bulunamadı: {a.skill}")
                return 0
            skill_ayrinti(s, skiller)
            return 0
        if a.repo:
            repo_ayrinti(a.repo, skiller)
            return 0
        sonuc, hata = degerlendir_hepsi(skiller)
        yazildi = rapor_yaz(rapor_uret(skiller, sonuc))
        sut = Counter(d["sutun"] for d in sonuc.values())
        uyari = sum(1 for d in sonuc.values() if any(x[0] == "UYARI" for x in d["satirlar"]))
        print(f"{len(sonuc)} skill tarandı · UYARI alan {uyari} · " + " · ".join(f"{k}: {sut[k]}" for k in
              ("kurulumda-duzelir", "kardesle-duzelir", "paket-gerekli", "cozulemez", "istisna", "yalniz-sayim", "temiz"))
              + f" · hata {hata} · notlar/yol-denetimi.md {'güncellendi' if yazildi else 'değişmedi'} · {time.time() - t0:.1f} sn")
    except Exception as e:  # noqa: BLE001  araç aylık zinciri / kurulumu düşürmez
        print(f"UYARI: yol taraması tamamlanamadı: {type(e).__name__}: {str(e)[:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
