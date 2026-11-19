#!/usr/bin/env python3
"""Antigravity (agy) akışını okunur canlı günlüğe çevirir.

Kullanım:
  agy -p "..." --output-format stream-json ... | python3 araclar/neon-izle.py --sonuc <dosya.json> [--ham <ham.jsonl>]

Her adımı tek satır yazar (saat, ne yaptığı, süre); Neon'un ara açıklamalarını kısaltarak gösterir.
Son "result" olayını --sonuc dosyasına JSON olarak yazar ({"status", "response", "conversation_id"}).
Yalnız standart girdiyi okur; kütüphane dosyalarına dokunmaz.
"""
import argparse
import json
import sys
import time

ARAC_ADI = {
    "read_file": "okuyor", "view_file": "okuyor", "list_dir": "klasöre bakıyor", "list_directory": "klasöre bakıyor",
    "grep_search": "arıyor", "find_by_name": "dosya arıyor", "run_command": "komut", "write_to_file": "yazıyor",
    "replace_file_content": "düzenliyor", "multi_replace_file_content": "düzenliyor", "edit_file": "düzenliyor",
    "command_status": "komutu bekliyor", "send_command_input": "komuta girdi",
}
PARAM = ("CommandLine", "Path", "AbsolutePath", "TargetFile", "DirectoryPath", "SearchPath", "Query", "Pattern")


def saat():
    return time.strftime("%H:%M:%S")


def kisalt(m, n=160):
    m = " ".join(str(m).split())
    return m if len(m) <= n else m[: n - 1] + "…"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sonuc", required=True)
    ap.add_argument("--ham")
    a = ap.parse_args()
    ham = open(a.ham, "a", encoding="utf-8") if a.ham else None
    metin, toplam, sonuc = {}, 0, None
    for satir in sys.stdin:
        if ham:
            ham.write(satir)
            ham.flush()
        try:
            o = json.loads(satir)
        except ValueError:
            if satir.strip():
                print(f"{saat()}  · {kisalt(satir)}", flush=True)
            continue
        ev = o.get("event")
        if ev == "init":
            i = o.get("init", {})
            print(f"{saat()}  ▶ Neon başladı · model {i.get('model')} · konuşma {o.get('conversation_id')}", flush=True)
        elif ev == "step_update":
            s = o["step_update"]
            no, tur, durum = s.get("step_index"), s.get("step_type"), s.get("state")
            if s.get("usage"):
                toplam += s["usage"].get("total_tokens", 0)
            if tur == "tool":
                ad = s.get("tool_name", "?")
                p = (s.get("tool_info") or {}).get("parameters") or {}
                hedef = next((p[k] for k in PARAM if k in p), "")
                if durum == "ACTIVE":
                    print(f"{saat()}  #{no} {ARAC_ADI.get(ad, ad)}: {kisalt(hedef, 140)}", flush=True)
                elif durum == "DONE" and (s.get("duration_seconds") or 0) > 20:
                    print(f"{saat()}  #{no}   bitti ({s['duration_seconds']:.0f} sn)", flush=True)
                elif durum not in ("ACTIVE", "DONE"):
                    print(f"{saat()}  #{no} {ad}: {durum}", flush=True)
            elif tur == "agent_response":
                metin[no] = metin.get(no, "") + (s.get("text_delta") or "")
                if durum == "DONE" and metin.get(no, "").strip():
                    print(f"{saat()}  💬 {kisalt(metin.pop(no), 300)}", flush=True)
        elif ev == "result":
            sonuc = o.get("result", {})
            print(f"{saat()}  ■ Neon bitti · durum {sonuc.get('status')} · toplam {toplam:,} token", flush=True)
    with open(a.sonuc, "w", encoding="utf-8") as f:
        json.dump(sonuc or {"status": "SONUC_YOK"}, f, ensure_ascii=False)
    return 0 if sonuc and sonuc.get("status") == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
