#!/usr/bin/env python3
"""Fihrist üretir ya da yeniler (dev koleksiyon: bolum fihrist). notlar/plan-tur-surecleri.md bölüm 3 ve 5.5; biçim: fihrist/README.md.

  python3 araclar/fihrist-uret.py owner/ad [--kuru]

Repo İNDİRİLMEZ: GitHub ağacından SKILL.md yolları bulunur, her SKILL.md'nin yalnız başı okunur (frontmatter `name` ve `description`).
Skil seçimi kaynak kaydındaki `dahil` / `haric` / `dahil_degil` ve kaynaklar.json `konum_haric` desenlerine uyar (kaynak-cek.py ile aynı işlev);
araç sürümü aynaları (.claude/.agents/başka araç kopyaları) ve birebir kopyalar tek skil sayılır. Kayıt yoksa (A4'ten önce) hepsi alınır.
`yol` skilin klasör yoludur ('' = kök SKILL.md; registry.json `kaynak_yol` ile aynı). Açıklama 300 karakterde kesilir.
--kuru: yalnız özet basar, dosya yazmaz. Var olan fihrist yenilenirse eklenen / silinen / adı değişen skiller raporlanır ve
`inceleme` notları (aynı `yol` için) korunur. Aynı skil registry.json'da (arşivde) varsa `arsivde: true` işaretlenir.
Çıkış kodu: 0 tamam · 2 kullanım hatası / repo okunamadı / hiç skil bulunamadı.
"""
import argparse
import importlib.util
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ortak  # noqa: E402

ACIKLAMA_SINIRI = 300
OKUMA_BAYT = 8000          # frontmatter dosyanın başındadır
PARALEL = 16
FIHRIST = ortak.KOK / "fihrist"


def _kaynak_cek():
    spec = importlib.util.spec_from_file_location("kaynak_cek_fihrist", Path(__file__).resolve().parent / "kaynak-cek.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def dosya_adi(repo):
    return repo.replace("/", "__") + ".json"


def aciklama_kisalt(metin, sinir=ACIKLAMA_SINIRI):
    """Boşlukları tek aralığa indirir; sınırı aşarsa sınır karakterde keser (son karakter …)."""
    m = re.sub(r"\s+", " ", metin or "").strip()
    return m if len(m) <= sinir else m[:sinir - 1].rstrip() + "…"


def skil_girdisi(yol, metin, repo):
    """(klasör yolu, SKILL.md metni | None) -> {ad, aciklama, yol}. Metin yoksa ad klasör adından gelir, açıklama boş kalır."""
    fm = ortak.frontmatter(metin) if metin else {}
    ad = (fm.get("name") or "").strip() or (yol.rsplit("/", 1)[-1] if yol else repo.split("/")[1])
    return {"ad": ad, "aciklama": aciklama_kisalt(fm.get("description", "")), "yol": yol}


def skil_klasorleri_sec(kayitlar, agac, ayar, repo):
    """Kaynak kaydındaki (birden çok olabilir) dahil/haric kurallarıyla seçilen skil klasörleri: {yol: SKILL.md yolu}.
    Kayıt yoksa kuralsız bir kayıt varsayılır."""
    kc = _kaynak_cek()
    sec = {}
    for k in (kayitlar or [{"repo": repo}]):
        secilen, _ = kc.skill_klasorlerini_sec(k, agac, ayar)
        for b in secilen.values():
            sec[b["yol"]] = None
    md = {}
    for e in agac:
        if e["type"] == "blob" and e["path"].rsplit("/", 1)[-1].lower() == "skill.md":
            md.setdefault(e["path"].rpartition("/")[0], e["path"])
    return {y: md[y] for y in sorted(sec) if y in md}


def fihrist_kur(repo, sha, tarih, girdiler, eski=None, arsivde=()):
    """Saf işlev. girdiler: [{ad, aciklama, yol}]; eski: var olan fihrist sözlüğü (inceleme notları aynı yol için korunur);
    arsivde: arşivde de bulunan skil yolları kümesi. Döner: yeni fihrist sözlüğü."""
    eski_inceleme = {x["yol"]: x["inceleme"] for x in (eski or {}).get("skiller", []) if isinstance(x, dict) and "inceleme" in x}
    skiller = []
    for g in sorted(girdiler, key=lambda x: x["yol"]):
        x = {"ad": g["ad"], "aciklama": g["aciklama"], "yol": g["yol"]}
        if g["yol"] in arsivde:
            x["arsivde"] = True
        if g["yol"] in eski_inceleme:
            x["inceleme"] = eski_inceleme[g["yol"]]
        skiller.append(x)
    return {"repo": repo, "commit": sha, "tarih": tarih, "skil_sayisi": len(skiller), "skiller": skiller}


def fark_hesapla(eski, yeni):
    """Eski ve yeni fihrist arasındaki fark: eklenen, silinen (yol, ad), ad_degisen (yol, eski ad, yeni ad), inceleme_kaybolan (silinen skilin notu)."""
    e = {x["yol"]: x for x in (eski or {}).get("skiller", [])}
    y = {x["yol"]: x for x in yeni["skiller"]}
    return {
        "eklenen": [(p, y[p]["ad"]) for p in y if p not in e],
        "silinen": [(p, e[p]["ad"]) for p in e if p not in y],
        "ad_degisen": [(p, e[p]["ad"], y[p]["ad"]) for p in y if p in e and e[p]["ad"] != y[p]["ad"]],
        "inceleme_kaybolan": [p for p in e if p not in y and "inceleme" in e[p]],
    }


def ozet_satirlari(repo, yeni, eski, fark, okunamayan=0, kuru=False):
    s = [f"{repo}: {yeni['skil_sayisi']} skil · commit {yeni['commit'][:9]}" + ("  (--kuru: dosya yazılmadı)" if kuru else "")]
    if okunamayan:
        s.append(f"  UYARI: {okunamayan} SKILL.md okunamadı (ad klasör adından, açıklama boş)")
    if eski is None:
        s.append("  yeni fihrist")
        return s
    s.append(f"  önceki fihrist: {eski.get('skil_sayisi', len(eski.get('skiller', [])))} skil · commit {str(eski.get('commit', ''))[:9]} · {eski.get('tarih', '')}")
    for etiket, anahtar in (("eklenen", "eklenen"), ("silinen", "silinen")):
        for p, ad in fark[anahtar][:20]:
            s.append(f"  {etiket}: {ad}  ({p or '.'})")
        if len(fark[anahtar]) > 20:
            s.append(f"  {etiket}: ... +{len(fark[anahtar]) - 20}")
    for p, a, b in fark["ad_degisen"][:20]:
        s.append(f"  adı değişen: {a} -> {b}  ({p or '.'})")
    for p in fark["inceleme_kaybolan"]:
        s.append(f"  UYARI: silinen skilin inceleme notu düştü: {p or '.'}")
    if not (fark["eklenen"] or fark["silinen"] or fark["ad_degisen"]):
        s.append("  fark yok")
    return s


def icerik_oku(repo, sha, govde, yollar):
    """Ağ. {klasör yolu: SKILL.md metni (ilk OKUMA_BAYT bayt)}; okunamayan yol sözlükte yoktur. git modunda önce toplu klon (klon_dosyalari_al),
    API modunda paralel ham_metin."""
    sonuc = {}
    if govde.get("_kaynak") == "git":
        dosyalar = ortak.klon_dosyalari_al(govde, list(yollar.values()))  # klonu çağıran (main) siler
        for klasor, yol in yollar.items():
            f = dosyalar.get(yol)
            if f:
                sonuc[klasor] = f.read_bytes()[:OKUMA_BAYT].decode("utf-8", "replace")
        return sonuc
    with ThreadPoolExecutor(PARALEL) as ex:
        metinler = list(ex.map(lambda yol: ortak.ham_metin(repo, yol, sha, OKUMA_BAYT), yollar.values()))
    for (klasor, _), m in zip(yollar.items(), metinler):
        if m is not None:
            sonuc[klasor] = m
    return sonuc


def arsivde_yollari(repo):
    reg = ortak.json_oku(ortak.REGISTRY, {"skiller": []}) or {}
    return {s.get("kaynak_yol", "") for s in reg.get("skiller", []) if str(s.get("repo", "")).lower() == repo.lower()}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fihrist üret / yenile (dosya indirmez)")
    ap.add_argument("repo", help="owner/ad")
    ap.add_argument("--kuru", action="store_true", help="yalnız özet; dosya yazma")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", a.repo):
        print("repo 'owner/ad' biçiminde olmalı", file=sys.stderr)
        return 2
    ayar = ortak.json_oku(ortak.KAYNAKLAR)
    kayitlar = [k for k in ayar["repolar"] if k["repo"].lower() == a.repo.lower()]
    govde = None
    try:
        sha, govde = ortak.repo_agaci(a.repo)
        if govde.get("truncated"):
            print("UYARI: GitHub ağacı kesik; fihrist eksik olabilir", file=sys.stderr)
        yollar = skil_klasorleri_sec(kayitlar, govde["tree"], ayar, a.repo)
        if not yollar:
            print(f"HATA: {a.repo}: seçilen SKILL.md yok (kaynak kaydındaki dahil/haric kurallarını kontrol et)", file=sys.stderr)
            return 2
        metinler = icerik_oku(a.repo, sha, govde, yollar)
    except (RuntimeError, OSError) as e:
        print(f"HATA: {a.repo} okunamadı: {e}", file=sys.stderr)
        return 2
    finally:
        ortak.klon_temizle(govde)
    girdiler = [skil_girdisi(y, metinler.get(y), a.repo) for y in yollar]
    hedef = FIHRIST / dosya_adi(a.repo)
    eski = ortak.json_oku(hedef)
    yeni = fihrist_kur(a.repo, sha, date.today().isoformat(), girdiler, eski, arsivde_yollari(a.repo) & set(yollar))
    for satir in ozet_satirlari(a.repo, yeni, eski, fark_hesapla(eski, yeni), len(yollar) - len(metinler), a.kuru):
        print(satir)
    if not a.kuru:
        FIHRIST.mkdir(exist_ok=True)
        ortak.json_yaz(hedef, yeni)
        print(f"yazıldı: fihrist/{hedef.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
