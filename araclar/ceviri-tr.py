#!/usr/bin/env python3
"""Elle Türkçe özeti (ozet_tr) olmayan skillerin description'ını Türkçeye çevirir -> aciklama-tr.json.
Çeviri otomatiktir (claude -p); elle inceleme yerine geçmez, sadece README-SKILLER.md'de gösterilir.
Her çeviri kaynak metnin hash'iyle saklanır: description değişirse çeviri eskir ve yeniden yapılır.

  python3 araclar/ceviri-tr.py              # eksik/eskimiş çevirileri yap
  python3 araclar/ceviri-tr.py --kuru       # kaç skill çevrilecek, yazmadan söyle
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, REGISTRY, json_oku, json_yaz  # noqa: E402

CEVIRI = KOK / "aciklama-tr.json"
ISTEM = """Aşağıdaki JSON nesnesi, AI agent skill'lerinin İngilizce açıklamalarını içeriyor ({{skill_id: açıklama}}).
Her biri için Türkçe iki alan yaz:
- "ne": skill'in ne yaptığı, tek cümle, en fazla 200 karakter.
- "ne_zaman": hangi istekte/durumda kullanılacağı, tek cümle, en fazla 160 karakter.
Kurallar: teknik terimleri, ürün/kütüphane/komut adlarını çevirme (React, Shopify, MCP, CLI...). Pazarlama dili kullanma.
Açıklamada "ne zaman" bilgisi yoksa işten çıkar. Sadece geçerli JSON döndür, başka hiçbir şey yazma:
{{"<skill_id>": {{"ne": "...", "ne_zaman": "..."}}, ...}}

{girdi}"""


def kaynak_metin(s):
    return ((s.get("aciklama_duzeltme") or {}).get("description") or s.get("aciklama") or s["ad"]).strip()[:700]


def ozet(metin):
    return hashlib.sha1(metin.encode()).hexdigest()[:12]


def cevir(parti, model):
    girdi = json.dumps({s["id"]: kaynak_metin(s) for s in parti}, ensure_ascii=False, indent=0)
    for _ in range(3):
        r = subprocess.run(["claude", "-p", ISTEM.format(girdi=girdi), "--model", model, "--max-turns", "1",
                            "--output-format", "json", "--disallowedTools",
                            "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Skill,Task,NotebookEdit"],
                           capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL, cwd="/tmp")
        try:
            cikti = json.loads(r.stdout)
            metin = cikti.get("result", "")
            m = re.search(r"\{.*\}", metin, re.S)
            veri = json.loads(m.group(0))
            return {k: v for k, v in veri.items() if isinstance(v, dict) and v.get("ne")}, cikti.get("total_cost_usd") or 0
        except (ValueError, AttributeError):
            continue
    return {}, 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kuru", action="store_true")
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--parti", type=int, default=60)
    ap.add_argument("--paralel", type=int, default=4)
    a = ap.parse_args()
    skiller = json_oku(REGISTRY)["skiller"]
    mevcut = json_oku(CEVIRI, {})
    eksik = [s for s in skiller if not s.get("ozet_tr")
             and (mevcut.get(s["id"]) or {}).get("kaynak") != ozet(kaynak_metin(s))]
    print(f"Çevrilecek: {len(eksik)} skill ({len(skiller)} içinde; elle özeti olan {sum(1 for s in skiller if s.get('ozet_tr'))})")
    if a.kuru or not eksik:
        return 0
    partiler = [eksik[i:i + a.parti] for i in range(0, len(eksik), a.parti)]
    maliyet = 0
    with ThreadPoolExecutor(a.paralel) as ex:
        for parti, (sonuc, m) in zip(partiler, ex.map(lambda p: cevir(p, a.model), partiler)):
            maliyet += m
            for s in parti:
                if s["id"] in sonuc:
                    mevcut[s["id"]] = {"ne": sonuc[s["id"]]["ne"].strip(), "ne_zaman": (sonuc[s["id"]].get("ne_zaman") or "").strip(),
                                       "kaynak": ozet(kaynak_metin(s))}
            json_yaz(CEVIRI, dict(sorted(mevcut.items())))
            print(f"  parti: {len(sonuc)}/{len(parti)} çevrildi", flush=True)
    kalan = sum(1 for s in skiller if not s.get("ozet_tr") and s["id"] not in mevcut)
    print(f"Bitti · maliyet ≈ ${maliyet:.2f} · çevrilemeyen: {kalan}")
    return 1 if kalan else 0


if __name__ == "__main__":
    sys.exit(main())
