#!/usr/bin/env python3
"""Toplu onay etki raporu aracı (Faz 2, YALNIZ rapor — salt okuma).

Hiçbir projenin kilit.json dosyasına veya skill klasörüne ASLA yazmaz.

Kullanım:
  python3 araclar/toplu-onay-rapor.py
  python3 araclar/toplu-onay-rapor.py --json
  python3 araclar/toplu-onay-rapor.py --ozet-json
  python3 araclar/toplu-onay-rapor.py --girdi-json girdi.json --json
"""
import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ortak  # noqa: E402

ARACLAR_DIZIN = Path(__file__).resolve().parent


def _yukle(dosya_adi, modul_adi):
    spec = importlib.util.spec_from_file_location(modul_adi, ARACLAR_DIZIN / dosya_adi)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _skill_eslestir(ad, kil_kayit, by_id, by_repo_yol):
    sid = kil_kayit.get("id") or ad
    if sid in by_id:
        return by_id[sid]
    repo = kil_kayit.get("repo")
    ky = kil_kayit.get("kaynak_yol", "")
    if repo and (repo, ky) in by_repo_yol:
        return by_repo_yol[(repo, ky)]
    return None


def etki_raporu_hesapla(projeler, registry_skiller, *, onceki_skiller=None, ucret_tablo=None) -> dict:
    """Saf hesaplama: proje listesi ve registry'den toplu onay etki raporu üretir.
    - surum_modu yoksa bellekte 'yalniz_onayli' sayılır.
    - 'dondur' projeler raporda ve toplu gruplarda görünmez.
    - elle_degistirildi, lisans/ücret değişimi ve yalniz_onayli tekil onaya düşer.
    - 'takip' modunda aynı (kaynak, skill_adi, hedef_surum) >= 2 projede tek toplu grupta birleşir.
    """
    ucret_tablo = ucret_tablo or {}
    by_id = {s["id"]: s for s in registry_skiller if isinstance(s, dict) and s.get("id")}
    by_repo_yol = {
        (s["repo"], s.get("kaynak_yol", "")): s
        for s in registry_skiller if isinstance(s, dict) and s.get("repo")
    }
    onceki_by_id = {s["id"]: s for s in (onceki_skiller or []) if isinstance(s, dict) and s.get("id")}

    aday_gruplar = defaultdict(list)
    tekil_onaylar = []
    kaynak_404_uyarilari = []
    etkilenen_projeler = set()
    dondurulan_proje_sayisi = 0

    for p in projeler:
        proje_ad = p["ad"]
        kilit = p.get("kilit") or {}
        surum_modu = kilit.get("surum_modu") or ortak.VARSAYILAN_SURUM_MODU
        if surum_modu == "dondur":
            dondurulan_proje_sayisi += 1
            continue

        elle_kume = set(p.get("elle_degisenler") or ())
        skiller = kilit.get("skiller") or {}
        for ad, kk in sorted(skiller.items()):
            if not isinstance(kk, dict):
                continue
            hedef = _skill_eslestir(ad, kk, by_id, by_repo_yol)
            repo = kk.get("repo") or (hedef.get("repo") if hedef else "?")
            if hedef is None or hedef.get("kaynak_durumu") == "kayip":
                kaynak_404_uyarilari.append({
                    "proje": proje_ad,
                    "kaynak": repo,
                    "skill_adi": ad,
                    "durum": "kaynak_404",
                })
                etkilenen_projeler.add(proje_ad)
                continue

            mevcut_hash = kk.get("klasor_hash")
            hedef_hash = hedef.get("klasor_hash")
            mevcut_commit = kk.get("commit")
            hedef_commit = hedef.get("commit")
            if hedef_hash and mevcut_hash == hedef_hash:
                continue
            if not hedef_hash and hedef_commit and mevcut_commit == hedef_commit:
                continue

            hedef_surum = str(hedef_commit or hedef_hash or "?")
            nedenler = []
            if kk.get("elle_degistirildi") is True or ad in elle_kume:
                nedenler.append("elle_degistirildi")

            onceki_s = onceki_by_id.get(hedef["id"], {})
            eski_lisans = kk.get("lisans") or onceki_s.get("lisans")
            yeni_lisans = hedef.get("lisans")
            if eski_lisans and yeni_lisans and eski_lisans != yeni_lisans:
                nedenler.append(f"lisans_degisti ({eski_lisans} -> {yeni_lisans})")

            eski_ucret = kk.get("ucret") or onceki_s.get("ucret")
            yeni_ucret = (ucret_tablo.get(hedef["id"]) if hedef["id"] in ucret_tablo else None) or hedef.get("ucret")
            if (eski_ucret and yeni_ucret and eski_ucret != yeni_ucret) or yeni_ucret == "ucretli":
                nedenler.append(f"ucret_degisti ({eski_ucret or '?'} -> {yeni_ucret})")

            etkilenen_projeler.add(proje_ad)
            if nedenler or surum_modu == "yalniz_onayli":
                if not nedenler:
                    nedenler.append("yalniz_onayli")
                tekil_onaylar.append({
                    "proje": proje_ad,
                    "kaynak": repo,
                    "skill_adi": ad,
                    "skill_id": hedef["id"],
                    "mevcut_surum": str(mevcut_commit or mevcut_hash or "?"),
                    "hedef_surum": hedef_surum,
                    "surum_modu": surum_modu,
                    "nedenler": nedenler,
                })
                continue

            anahtar = (repo, ad, hedef_surum)
            aday_gruplar[anahtar].append({
                "proje": proje_ad,
                "skill_id": hedef["id"],
                "mevcut_surum": str(mevcut_commit or mevcut_hash or "?"),
            })

    toplu_gruplar = []
    for (repo, ad, hedef_surum), uyeler in sorted(aday_gruplar.items()):
        if len(uyeler) >= 2:
            toplu_gruplar.append({
                "kaynak": repo,
                "skill_adi": ad,
                "skill_id": uyeler[0]["skill_id"],
                "hedef_surum": hedef_surum,
                "projeler": [u["proje"] for u in uyeler],
            })
        else:
            u = uyeler[0]
            tekil_onaylar.append({
                "proje": u["proje"],
                "kaynak": repo,
                "skill_adi": ad,
                "skill_id": u["skill_id"],
                "mevcut_surum": u["mevcut_surum"],
                "hedef_surum": hedef_surum,
                "surum_modu": "takip",
                "nedenler": ["tek_proje"],
            })

    return {
        "toplu_gruplar": toplu_gruplar,
        "tekil_onaylar": tekil_onaylar,
        "kaynak_404_uyarilari": kaynak_404_uyarilari,
        "ozet": {
            "etkilenen_proje_sayisi": len(etkilenen_projeler),
            "toplu_onay_grubu_sayisi": len(toplu_gruplar),
            "tekil_onay_sayisi": len(tekil_onaylar),
            "kaynak_404_sayisi": len(kaynak_404_uyarilari),
            "dondurulan_proje_sayisi": dondurulan_proje_sayisi,
        },
    }


def projeleri_topla(kok=ortak.KOK) -> tuple[list[dict], list[dict]]:
    """Gerçek projeleri ve registry'yi salt okur (hiçbir dosyaya yazmaz)."""
    kok = Path(kok)
    pk = _yukle("proje-kullanimi.py", "pk_tor")
    se = _yukle("skill-ekle.py", "se_tor")
    ayar = ortak.json_oku(kok / "projeler.json", {}) or {}
    reg = ortak.json_oku(kok / "registry.json", {"skiller": []}) or {"skiller": []}
    projeler = []
    for yol in pk.projeleri_bul(ayar):
        f = Path(yol) / ".skill-kutuphanesi" / "kilit.json"
        if not f.is_file():
            continue
        try:
            kilit = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(kilit, dict):
            continue
        elle = set()
        for ad, kk in (kilit.get("skiller") or {}).items():
            try:
                if se.elle_degismis(Path(yol), ad, kk):
                    elle.add(ad)
            except Exception:  # noqa: BLE001
                pass
        projeler.append({"ad": Path(yol).name, "yol": str(yol), "kilit": kilit, "elle_degisenler": elle})
    return projeler, reg.get("skiller", [])


def metin_rapor(sonuc: dict) -> str:
    oz = sonuc["ozet"]
    satir = [
        f"Toplu Onay Etki Raporu (etkilenen proje: {oz['etkilenen_proje_sayisi']} · "
        f"toplu grup: {oz['toplu_onay_grubu_sayisi']} · tekil onay: {oz['tekil_onay_sayisi']} · "
        f"404 uyarı: {oz['kaynak_404_sayisi']})",
    ]
    if sonuc["toplu_gruplar"]:
        satir.append("\nToplu onay grupları:")
        for g in sonuc["toplu_gruplar"]:
            satir.append(f"  - {g['kaynak']} / {g['skill_adi']} -> {g['hedef_surum'][:7]} ({len(g['projeler'])} proje: {', '.join(g['projeler'])})")
    if sonuc["tekil_onaylar"]:
        satir.append("\nTekil onay gerekenler:")
        for x in sonuc["tekil_onaylar"]:
            satir.append(f"  - {x['proje']}: {x['kaynak']} / {x['skill_adi']} [{', '.join(x['nedenler'])}]")
    if sonuc["kaynak_404_uyarilari"]:
        satir.append("\nKaynak 404 uyarıları (yerel kopya korunur):")
        for u in sonuc["kaynak_404_uyarilari"]:
            satir.append(f"  - {u['proje']}: {u['kaynak']} / {u['skill_adi']} (kaynak_404)")
    if not (sonuc["toplu_gruplar"] or sonuc["tekil_onaylar"] or sonuc["kaynak_404_uyarilari"]):
        satir.append("Tüm projeler güncel.")
    return "\n".join(satir)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Toplu onay etki raporu (salt okuma, yazmaz)")
    ap.add_argument("--kok", default=str(ortak.KOK), help="Kütüphane kök klasörü")
    ap.add_argument("--girdi-json", default=None, help="Sahte proje/registry test girdisi JSON")
    ap.add_argument("--json", action="store_true", help="Tam raporu JSON olarak yazdır")
    ap.add_argument("--ozet-json", action="store_true", help="Tek satır --ozet-json sözleşmesi")
    a = ap.parse_args(argv)

    if a.girdi_json:
        g = json.loads(Path(a.girdi_json).read_text(encoding="utf-8"))
        sonuc = etki_raporu_hesapla(
            g.get("projeler", []), g.get("skiller", []),
            onceki_skiller=g.get("onceki_skiller"), ucret_tablo=g.get("ucret_tablo"),
        )
    else:
        projeler, skiller = projeleri_topla(Path(a.kok))
        sonuc = etki_raporu_hesapla(projeler, skiller)

    if a.ozet_json:
        oz = sonuc["ozet"]
        durum = "dikkat" if (oz["toplu_onay_grubu_sayisi"] or oz["tekil_onay_sayisi"] or oz["kaynak_404_sayisi"]) else "temiz"
        print(json.dumps({
            "arac": "toplu-onay-rapor",
            "durum": durum,
            "satirlar": metin_rapor(sonuc).splitlines()[:10],
            "karar_bekleyen": [f"Toplu grup ({len(g['projeler'])}): {g['kaynak']}/{g['skill_adi']}" for g in sonuc["toplu_gruplar"]],
        }, ensure_ascii=False))
    elif a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    else:
        print(metin_rapor(sonuc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
