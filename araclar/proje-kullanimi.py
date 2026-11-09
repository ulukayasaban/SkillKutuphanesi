#!/usr/bin/env python3
"""Hangi proje hangi skili kullanıyor? Proje bilgisinin TEK yeri: kütüphane kayıtlarına (registry.json inceleme alanları,
kaynaklar.json notları, kategori/referans kartları) proje adı yazılmaz; proje ↔ skill eşlemesi buradan okunur.

  python3 araclar/proje-kullanimi.py                 # projeleri tara -> notlar/proje-kullanimi.md (hiçbir projeyi değiştirmez)
  python3 araclar/proje-kullanimi.py --skill <id>    # bu skili/kaynağı kullanan projeler (ör. silmeden / tercih değiştirmeden önce)
  python3 araclar/proje-kullanimi.py --repo owner/ad

Kaynak: her projenin `.skill-kutuphanesi/kilit.json` dosyası (skill-ekle.py yazar) ve varsa `elle-kurulan.json`.
Projeler `projeler.json` -> `tarama_kokleri` altında bir seviye aranır; başka yerdeki projeler `ek_projeler` listesine yazılır.
Projeye özel elle notlar (ör. "şu tarihten beri bu sürüm kullanılıyor") `projeler.json` -> `notlar` -> <proje> -> <skill id>.
"""
import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, REGISTRY, json_oku  # noqa: E402

AYAR = KOK / "projeler.json"
RAPOR = KOK / "notlar" / "proje-kullanimi.md"


def projeleri_bul(ayar):
    yollar = []
    for kok in ayar.get("tarama_kokleri", []):
        kok = Path(kok).expanduser()
        if kok.is_dir():
            yollar += sorted(p.parent.parent for p in kok.glob("*/.skill-kutuphanesi/kilit.json"))
    yollar += [Path(p).expanduser() for p in ayar.get("ek_projeler", [])]
    gorulen, sonuc = set(), []
    for y in yollar:
        y = y.resolve()
        if y in gorulen or y == KOK or not (y / ".skill-kutuphanesi" / "kilit.json").exists():
            continue
        gorulen.add(y)
        sonuc.append(y)
    return sonuc


def oku(ayar):
    projeler = []
    for yol in projeleri_bul(ayar):
        kilit = json_oku(yol / ".skill-kutuphanesi" / "kilit.json", {}) or {}
        elle = json_oku(yol / ".skill-kutuphanesi" / "elle-kurulan.json", None)
        if isinstance(elle, dict):
            elle = elle.get("skiller", elle)
        projeler.append({"ad": yol.name, "yol": yol, "kilit": kilit, "elle": sorted(elle) if elle else []})
    return projeler


def kisa_yol(yol):
    try:
        return "~/" + str(yol.relative_to(Path.home()))
    except ValueError:
        return str(yol)


def rapor_yaz(projeler, ayar, registry):
    """registry: {(repo, kaynak_yol): güncel kimlik}. Kilit yazıldıktan sonra tercih değiştiyse kimlik kaymış olabilir."""
    registry_idler = set(registry.values())
    notlar = ayar.get("notlar", {})
    s = ["# Proje kullanımı — hangi proje hangi skili kullanıyor",
         "",
         f"> `araclar/proje-kullanimi.py` üretir ({date.today().isoformat()}); elle düzenleme. Kaynak: projelerin "
         "`.skill-kutuphanesi/kilit.json` dosyaları. Elle notlar `projeler.json` → `notlar`.",
         "> Proje bilgisi yalnızca burada tutulur; skill ve kaynak kayıtlarına proje adı yazılmaz.",
         "",
         "| Proje | Yol | Skill | Araç | Blok | Son işlem |",
         "|---|---|---|---|---|---|"]
    for p in projeler:
        k = p["kilit"]
        s.append(f"| [{p['ad']}](#{p['ad'].lower().replace(' ', '-')}) | `{kisa_yol(p['yol'])}` | {len(k.get('skiller', {}))} | "
                 f"{', '.join(k.get('araclar', [])) or '—'} | {k.get('blok') or 'tam'} | {k.get('guncelleme') or '—'} |")
    kullanan = {}
    for p in projeler:
        k = p["kilit"]
        s += ["", f"## {p['ad']}", ""]
        if k.get("profil") or k.get("roller"):
            s.append(f"Profil: {k.get('profil') or '—'} · Roller: {', '.join(k.get('roller', [])) or '—'}")
            s.append("")
        s += ["| Skill | Kaynak | Commit | Roller | Not |", "|---|---|---|---|---|"]
        pn = notlar.get(p["ad"], {})
        for ad, v in sorted(k.get("skiller", {}).items()):
            sid = v.get("id", ad)
            guncel = registry.get((v.get("repo"), v.get("kaynak_yol")))
            ek = pn.get(sid, "") or pn.get(guncel or "", "")
            if guncel is None and sid not in registry_idler:
                ek = ("kütüphanede artık yok · " + ek).rstrip(" ·")
            elif guncel and guncel != sid:
                ek = (f"kütüphanede şimdi `{guncel}` · " + ek).rstrip(" ·")
            kullanan.setdefault(guncel or sid, []).append(p["ad"])
            kurulu = f"`{ad}`" if ad == sid else f"`{ad}` (kimlik `{sid}`)"
            s.append(f"| {kurulu} | {v.get('repo', '?')} | `{str(v.get('commit', ''))[:7]}` | "
                     f"{', '.join(v.get('roller', [])) or '—'} | {ek} |")
        if p["elle"]:
            s += ["", "Kütüphane dışı, elle kurulan: " + ", ".join(f"`{a}`" for a in p["elle"])]
    s += ["", "## Skill → projeler (birden fazla projede kullanılanlar)", "", "| Skill | Projeler |", "|---|---|"]
    for sid, pl in sorted(kullanan.items(), key=lambda x: (-len(x[1]), x[0])):
        if len(pl) > 1:
            s.append(f"| `{sid}` | {', '.join(pl)} |")
    s.append("")
    RAPOR.write_text("\n".join(s), encoding="utf-8")
    return kullanan


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skill", help="bu skill kimliğini kullanan projeleri yaz")
    ap.add_argument("--repo", help="bu kaynaktan (owner/ad) skill kullanan projeleri yaz")
    a = ap.parse_args()
    ayar = json_oku(AYAR, {}) or {}
    projeler = oku(ayar)
    if a.skill or a.repo:
        bulundu = False
        for p in projeler:
            for ad, v in sorted(p["kilit"].get("skiller", {}).items()):
                if (a.skill and v.get("id", ad) == a.skill) or (a.repo and v.get("repo", "").lower() == a.repo.lower()):
                    print(f"{p['ad']}: {v.get('id', ad)} ({v.get('repo')}@{str(v.get('commit', ''))[:7]})")
                    bulundu = True
        if not bulundu:
            print("Hiçbir projede kullanılmıyor.")
        return
    reg = json_oku(REGISTRY, {}) or {}
    esleme = {(x.get("repo"), x.get("kaynak_yol")): x["id"] for x in reg.get("skiller", [])}
    kullanan = rapor_yaz(projeler, ayar, esleme)
    print(f"{len(projeler)} proje · {len(kullanan)} farklı skill kullanımda · rapor: {RAPOR.relative_to(KOK)}")
    for p in projeler:
        print(f"  {p['ad']}: {len(p['kilit'].get('skiller', {}))} skill")
    bilinmeyen = sorted(set(ayar.get("notlar", {})) - {p["ad"] for p in projeler})
    if bilinmeyen:
        print("UYARI: projeler.json notlarında olup bulunamayan proje: " + ", ".join(bilinmeyen))


if __name__ == "__main__":
    main()
