#!/usr/bin/env python3
"""Kütüphanenin KENDİ ajanları: tek kaynak ajanlar/kutuphane-*.md -> Claude ve Codex ajan dosyaları.

  python3 araclar/ajan-uret.py             # .claude/agents/*.md ve .codex/agents/*.toml dosyalarını kaynaktan yeniden üretir
  python3 araclar/ajan-uret.py --kontrol   # yazmaz; kaynak hatalıysa ya da üretilen dosyalar eskiyse çıkış 1
  python3 araclar/ajan-uret.py --kok YOL   # başka kök (testler)
  python3 araclar/ajan-uret.py --help      # bu metin (hiçbir şey çalıştırmaz)

Kaynak: ajanlar/ORTAK.md (her ajanın ortak kuralları) ve ajanlar/kutuphane-<ad>.md (başlık bloğu + görev tanımı).
Başlık bloğu (--- arasında, 'anahtar: değer' satırları): name (dosya adıyla aynı), description (tek satır),
model (inherit | sonnet | opus | haiku | fable | claude-... tam kimlik), effort (low | medium | high | xhigh | max),
tools (isteğe bağlı; yalnız Claude; virgülle ayrılmış araç adları).
Üretilen dosyalar elle düzenlenmez; ilk satırlarındaki işaret bunu söyler. Codex dosyasına model yazılmaz (Codex kendi modelini kullanır).
Bu araç yalnız kütüphane klasörünün içine yazar; projelere, genel klasörlere ve ayar dosyalarına dokunmaz. Rehber: rehber/15-ajanlar.md
"""
import argparse
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ISARET = "ajan-uret.py üretti; elle düzenleme. Kaynak:"
MODELLER = ("inherit", "sonnet", "opus", "haiku", "fable")
CABALAR = ("low", "medium", "high", "xhigh", "max")
AD_DESENI = re.compile(r"kutuphane-[a-z][a-z0-9-]{1,40}")
ALANLAR = ("name", "description", "model", "effort", "tools")
# Görev tanımlarında anılan ve var olması gereken kütüphane dosyaları (ters tırnak içinde)
ATIF = re.compile(r"`((?:rehber|promptlar|araclar|zamanlanmis|kendi|notlar|ajanlar)/[A-Za-z0-9_./-]+\.(?:md|py|json))`")


def _oku(f):
    return f.read_text(encoding="utf-8")


def kaynak_ayir(metin):
    """'---' başlık bloğu + gövde -> (alanlar sözlüğü, gövde). Blok yoksa ({}, metin)."""
    m = re.match(r"---\n(.*?)\n---\n?(.*)\Z", metin, re.S)
    if not m:
        return {}, metin
    alan = {}
    for satir in m.group(1).splitlines():
        if not satir.strip():
            continue
        k, ayir, v = satir.partition(":")
        if ayir:
            alan[k.strip()] = v.strip()
    return alan, m.group(2).lstrip("\n")


def kaynaklar(kok):
    """ajanlar/kutuphane-*.md -> [(ad, alanlar, gövde, dosya)], ada göre sıralı."""
    d = Path(kok) / "ajanlar"
    out = []
    for f in sorted(d.glob("kutuphane-*.md")):
        alan, govde = kaynak_ayir(_oku(f))
        out.append((f.stem, alan, govde, f))
    return out


def kaynak_hatalari(kok):
    """Kaynak dosyalarındaki hatalar: [mesaj]. ajanlar/ klasörü yoksa boş (ajan kurulmamış kök)."""
    kok = Path(kok)
    d = kok / "ajanlar"
    if not d.is_dir():
        return []
    h = []
    if not (d / "ORTAK.md").is_file():
        h.append("ajanlar/ORTAK.md yok (ortak kurallar)")
    liste = kaynaklar(kok)
    if not liste:
        h.append("ajanlar/ içinde kutuphane-*.md yok")
    for ad, alan, govde, f in liste:
        rel = f"ajanlar/{f.name}"
        if not AD_DESENI.fullmatch(ad):
            h.append(f"{rel}: dosya adı 'kutuphane-<ad>.md' biçiminde olmalı (küçük harf, rakam, tire)")
        if alan.get("name") != ad:
            h.append(f"{rel}: name alanı dosya adıyla aynı olmalı ({ad})")
        if not alan.get("description"):
            h.append(f"{rel}: description boş (tek satır; aracın ajanı ne zaman seçeceğini söyler)")
        model = alan.get("model", "")
        if model not in MODELLER and not re.fullmatch(r"claude-[a-z0-9.-]+", model):
            h.append(f"{rel}: model geçersiz ({model or 'boş'}); {', '.join(MODELLER)} ya da claude-... tam kimlik")
        if alan.get("effort") not in CABALAR:
            h.append(f"{rel}: effort geçersiz ({alan.get('effort') or 'boş'}); {', '.join(CABALAR)}")
        for k in alan:
            if k not in ALANLAR:
                h.append(f"{rel}: bilinmeyen başlık alanı '{k}' ({', '.join(ALANLAR)})")
        if "tools" in alan and not re.fullmatch(r"[A-Za-z]+(?:\s*,\s*[A-Za-z]+)*", alan["tools"]):
            h.append(f"{rel}: tools virgülle ayrılmış araç adları olmalı (ör. Read, Grep, Glob, Bash)")
        if not govde.strip():
            h.append(f"{rel}: görev tanımı boş")
    for f in sorted(d.glob("*.md")):
        for yol in sorted(set(ATIF.findall(_oku(f)))):
            if not (kok / yol).is_file():
                h.append(f"ajanlar/{f.name}: olmayan dosyaya işaret ediyor: {yol}")
    return h


def _talimat(kok, ad, govde):
    ortak = _oku(Path(kok) / "ajanlar" / "ORTAK.md").strip()
    return (f"Sen SkillKutuphanesi'nin `{ad}` ajanısın. Aşağıda önce bütün kütüphane ajanlarının ortak kuralları, sonra senin görev "
            f"tanımın var. Kesin kurallar `CLAUDE.md` / `AGENTS.md` dosyasındadır; orada yazanla çelişen bir şey görürsen dur ve raporla.\n\n"
            f"{ortak}\n\n---\n\n{govde.strip()}\n")


def claude_metni(kok, ad, alan, govde):
    bas = ["---", f"name: {ad}", f"description: {json.dumps(alan['description'], ensure_ascii=False)}",
           f"model: {alan['model']}", f"effort: {alan['effort']}"]
    if alan.get("tools"):
        bas.append(f"tools: {alan['tools']}")
    bas.append("---")
    return "\n".join(bas) + f"\n<!-- {ISARET} ajanlar/{ad}.md ve ajanlar/ORTAK.md -->\n\n" + _talimat(kok, ad, govde)


def codex_metni(kok, ad, alan, govde):
    s = lambda v: json.dumps(v, ensure_ascii=False)  # noqa: E731  (JSON dizgisi geçerli bir TOML temel dizgisidir)
    return "\n".join([f"# {ISARET} ajanlar/{ad}.md ve ajanlar/ORTAK.md", f"name = {s(ad)}", f"description = {s(alan['description'])}",
                      f"model_reasoning_effort = {s(alan['effort'])}", f"developer_instructions = {s(_talimat(kok, ad, govde))}"]) + "\n"


def beklenen(kok):
    """Üretilmesi gereken dosyalar: {göreli yol: metin}. Kaynak hatalıysa boş."""
    kok = Path(kok)
    if kaynak_hatalari(kok) or not (kok / "ajanlar").is_dir():
        return {}
    out = {}
    for ad, alan, govde, _f in kaynaklar(kok):
        out[f".claude/agents/{ad}.md"] = claude_metni(kok, ad, alan, govde)
        out[f".codex/agents/{ad}.toml"] = codex_metni(kok, ad, alan, govde)
    return out


def uretilmis_fazlalar(kok, hedef):
    """Bu aracın ürettiği ama kaynağı kalmamış dosyalar (işaret satırı var, beklenenler arasında yok)."""
    kok = Path(kok)
    out = []
    for klasor, desen in ((kok / ".claude" / "agents", "kutuphane-*.md"), (kok / ".codex" / "agents", "kutuphane-*.toml")):
        for f in sorted(klasor.glob(desen)) if klasor.is_dir() else []:
            rel = str(f.relative_to(kok))
            if rel not in hedef and ISARET in _oku(f):
                out.append(rel)
    return out


def ajan_denetimi(kok=KOK):
    """dogrula.py için: (hatalar, uyarilar). ajanlar/ yoksa ikisi de boş."""
    kok = Path(kok)
    if not (kok / "ajanlar").is_dir():
        return [], []
    h = [f"ajan: {x}" for x in kaynak_hatalari(kok)]
    if h:
        return h, []
    hedef = beklenen(kok)
    for rel, metin in sorted(hedef.items()):
        f = kok / rel
        if not f.is_file():
            h.append(f"ajan: {rel} yok -> python3 araclar/ajan-uret.py")
        elif _oku(f) != metin:
            h.append(f"ajan: {rel} kaynakla aynı değil (elle düzenlenmiş ya da kaynak değişmiş) -> python3 araclar/ajan-uret.py")
    for rel in uretilmis_fazlalar(kok, hedef):
        h.append(f"ajan: {rel} kaynağı kalmamış üretilmiş dosya -> python3 araclar/ajan-uret.py")
    return h, []


def uret(kok=KOK):
    """Dosyaları yazar; kaynağı kalmamış üretilmiş dosyaları siler. Döner: (yazılan, silinen, hatalar)."""
    kok = Path(kok)
    h = kaynak_hatalari(kok)
    if h or not (kok / "ajanlar").is_dir():
        return [], [], h or ["ajanlar/ klasörü yok"]
    hedef = beklenen(kok)
    yazilan = []
    for rel, metin in sorted(hedef.items()):
        f = kok / rel
        if not f.is_file() or _oku(f) != metin:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(metin, encoding="utf-8")
            yazilan.append(rel)
    silinen = uretilmis_fazlalar(kok, hedef)
    for rel in silinen:
        (kok / rel).unlink()
    return yazilan, silinen, []


def main():
    ap = argparse.ArgumentParser(description="Kütüphanenin kendi ajan dosyalarını ajanlar/ kaynağından üretir.")
    ap.add_argument("--kontrol", action="store_true", help="yazma; kaynak hatalıysa ya da üretilen dosyalar eskiyse çıkış 1")
    ap.add_argument("--kok", default=str(KOK), help="kütüphane kökü (testler için)")
    a = ap.parse_args()
    kok = Path(a.kok)
    if a.kontrol:
        h, _u = ajan_denetimi(kok)
        for x in h:
            print("HATA:", x)
        print(f"Ajanlar: {len(kaynaklar(kok))} kaynak · {len(h)} hata")
        return 1 if h else 0
    yazilan, silinen, h = uret(kok)
    for x in h:
        print("HATA:", x)
    if h:
        return 1
    for rel in yazilan:
        print("yazıldı:", rel)
    for rel in silinen:
        print("silindi (kaynağı yok):", rel)
    print(f"Ajanlar: {len(kaynaklar(kok))} kaynak · {len(yazilan)} dosya yazıldı · {len(silinen)} silindi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
