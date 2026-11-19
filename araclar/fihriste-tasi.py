#!/usr/bin/env python3
"""Var olan arşivli bir kaynağı (dev koleksiyon) fihriste taşır. Ağ KULLANMAZ.

Ön koşul: `fihrist/<owner>__<ad>.json` dosyası önceden `araclar/fihrist-uret.py` ile üretilmiş olmalıdır;
yoksa araç durur ve hiçbir dosyaya dokunmaz.

  python3 araclar/fihriste-tasi.py owner/ad --kuru [--arsivde-tut YOL ...]
  python3 araclar/fihriste-tasi.py owner/ad --evet [--arsivde-tut YOL ...]

--kuru (varsayılan): yalnız rapor basar, hiçbir dosyayı değiştirmez:
  - çıkacak skil ve bileşen sayısı, arşivde kalacaklar, açılacak yer
  - etkilenen rol, profil ve projeler (canlı proje kilitleri ya da notlar/proje-kullanimi.md)
  - fihriste taşınacak inceleme notu ve Türkçe açıklama sayısı
  - çıplak ad / tercih el değişimi (başka kaynaktaki aynı adlı skil tercihi alırsa)
  - kullanılan ama `arsivde_tut` listesinde olmayan skil varsa HATA verir ve durur.

--evet (yalnız kullanıcı onayıyla):
  (a) registry inceleme alanlarını ve aciklama-tr.json karşılığını fihrist öğesinin `inceleme` alanına taşır,
  (b) `arsivde_tut` dışındaki skilleri ve reponun tüm bileşenlerini `arsiv/` ve `registry.json`'dan çıkarır
      (araclar/kaynak-cikar.py işlevlerini yeniden kullanır),
  (c) `kaynaklar.json` kaydına `tur: dev-koleksiyon`, `bolum: fihrist` ve varsa `arsivde_tut` yazar,
  (d) çıkarılan skillerin `ucret-siniflandirma.json`, `aciklama-tr.json`, `yol-istisnalari.json` satırlarını temizler,
  (e) çıplak ad / tercih el değişimini ve katalog yenileme komutlarını raporlar.

Çıkış kodu: 0 tamam · 1 taşıma engeli / HATA (kullanılan skil arsivde_tut'ta değil vb.) · 2 kullanım hatası / ön koşul eksik.
"""
import argparse
import copy
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ARAC_KLASORU = Path(__file__).resolve().parent
sys.path.insert(0, str(ARAC_KLASORU))
import ortak  # noqa: E402

INCELEME_METIN_ALANLARI = (
    "ozet_tr", "kalite_notu", "kullanim_alani", "kullanma",
    "ortusme_grubu", "ortusme_rolu", "zorluk", "uygulama_grubu", "inceleyen",
)
INCELEME_LISTE_ALANLARI = ("teknoloji", "gerekli_paketler", "proje_tipleri")
TARIH_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _modul(ad):
    spec = importlib.util.spec_from_file_location(ad.replace("-", "_") + "_ft", ARAC_KLASORU / f"{ad}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _tarih_gecerli(s):
    if not isinstance(s, str) or not TARIH_RE.fullmatch(s):
        return False
    try:
        date.fromisoformat(s)
        return True
    except ValueError:
        return False


def dosya_adi(repo):
    return repo.replace("/", "__") + ".json"


def bayt_bicim(bayt):
    if bayt >= 1024 * 1024:
        return f"{bayt / (1024 * 1024):.2f} MB"
    if bayt >= 1024:
        return f"{round(bayt / 1024)} KB"
    return f"{bayt} B"


# ------------------------------------------------------------------ saf işlevler (dosya ve ağ yok)
def arsivde_tut_coz(arg_listesi, kayitlar=()):
    """CLI --arsivde-tut argümanları + mevcut kaynak kaydındaki arsivde_tut -> sıralı tekil kaynak_yol listesi."""
    sonuc = set()
    for k in (kayitlar or []):
        if isinstance(k, dict) and isinstance(k.get("arsivde_tut"), list):
            for x in k["arsivde_tut"]:
                if isinstance(x, str):
                    sonuc.add(x)
    for ham in (arg_listesi or []):
        if ham == "":
            sonuc.add("")
            continue
        for parca in ham.split(","):
            p = parca.strip()
            if p or ham == "":
                sonuc.add(p)
    return sorted(sonuc)


def proje_kullanimi_md_coz(metin, repo, eski_adlar=()):
    """notlar/proje-kullanimi.md içinden verilen repodan kurulu skilleri okur (canlı proje kilidi yokken yedek).
    Döner: [{"proje": ad, "skiller": [{"kurulu_ad": ..., "id": ...}]}]."""
    hedefler = {repo.lower()} | {e.lower() for e in (eski_adlar or [])}
    projeler = {}
    mevcut_proje = None
    for satir in (metin or "").splitlines():
        m_baslik = re.match(r"^##\s+(.+?)\s*$", satir)
        if m_baslik:
            ad = m_baslik.group(1)
            if ad.startswith(("Skill →", "Programla gelen")):
                mevcut_proje = None
            else:
                mevcut_proje = ad
            continue
        if not mevcut_proje or not satir.startswith("|"):
            continue
        parcalar = [p.strip() for p in satir.strip().strip("|").split("|")]
        if len(parcalar) < 2 or parcalar[0] in ("Skill", "---") or parcalar[0].startswith("---"):
            continue
        kaynak_sutun = parcalar[1].strip("` ")
        if kaynak_sutun.lower() not in hedefler:
            continue
        sk_col = parcalar[0]
        m_ad = re.match(r"`([^`]+)`(?:\s*\(kimlik\s+`([^`]+)`\))?", sk_col)
        if not m_ad:
            continue
        kurulu_ad = m_ad.group(1)
        sid = m_ad.group(2) or kurulu_ad
        projeler.setdefault(mevcut_proje, []).append({"kurulu_ad": kurulu_ad, "id": sid})
    return [{"proje": ad, "skiller": sk} for ad, sk in sorted(projeler.items())]


def kullanilan_skilleri_bul(repo_skiller, rapor, md_projeler=()):
    """Rol, profil ve projelerde kullanılan repo skillerini kaynak_yol bazında toplar.
    Döner: (kullanilan, eslesmeyen)
      - kullanilan: {kaynak_yol: {"skill": s, "roller": [...], "profiller": [...], "projeler": [...]}}
      - eslesmeyen: repo_skiller ile eşleşmeyen kullanım girdilerinin açıklamaları (sessizce atlanmaz)."""
    id_map = {s["id"]: s for s in repo_skiller}
    tercih_map = {s["ad"]: s for s in repo_skiller if s.get("durum") == "tercih"}
    sonuc = {}
    eslesmeyen = []

    def ekle(s, alan, deger):
        yol = s.get("kaynak_yol", "")
        k = sonuc.setdefault(yol, {"skill": s, "roller": [], "profiller": [], "projeler": []})
        if deger not in k[alan]:
            k[alan].append(deger)

    def esle_girdi(girdi):
        return id_map.get(girdi) or tercih_map.get(girdi)

    for r in rapor.get("roller", []):
        s = esle_girdi(r.get("girdi"))
        if s:
            ekle(s, "roller", f"{r['dosya']} ({r['alan']})")
        else:
            eslesmeyen.append(f"rol {r.get('dosya', '?')} ({r.get('alan', '?')}): '{r.get('girdi', '')}'")
    for pr in rapor.get("profiller", []):
        s = esle_girdi(pr.get("girdi"))
        if s:
            ekle(s, "profiller", f"{pr['dosya']} ({pr['alan']})")
        else:
            eslesmeyen.append(f"profil {pr.get('dosya', '?')} ({pr.get('alan', '?')}): '{pr.get('girdi', '')}'")

    proje_kaynak = rapor.get("projeler", []) if rapor.get("proje_bilgisi") == "var" else list(md_projeler)
    for p in proje_kaynak:
        for x in p.get("skiller", []):
            s = (
                id_map.get(x.get("id"))
                or tercih_map.get(x.get("id"))
                or id_map.get(x.get("kurulu_ad"))
                or tercih_map.get(x.get("kurulu_ad"))
            )
            if s:
                ekle(s, "projeler", f"{p['proje']} ({x['kurulu_ad']})")
            else:
                eslesmeyen.append(
                    f"proje {p.get('proje', '?')}: kurulu_ad='{x.get('kurulu_ad', '')}', id='{x.get('id', '')}'"
                )
    return sonuc, eslesmeyen


def inceleme_kaydi_kur(skill, atr_girdi=None, bugun=None, mevcut_inceleme=None):
    """Registry skil kaydı + aciklama-tr.json girdisi -> fihrist `inceleme` sözlüğü (şema: dogrula.fihrist_hatalari).
    Taşınacak inceleme notu / Türkçe açıklama / mevcut inceleme yoksa None döner."""
    bugun = bugun or date.today().isoformat()
    elle_alan_var = (
        skill.get("inceleme") not in (None, "", "otomatik")
        or any(isinstance(skill.get(a), str) and skill[a].strip() for a in INCELEME_METIN_ALANLARI)
        or any(isinstance(skill.get(a), list) and skill[a] for a in INCELEME_LISTE_ALANLARI)
        or (isinstance(skill.get("kalite"), int) and not isinstance(skill.get("kalite"), bool))
        or (isinstance(skill.get("notlar"), str) and skill["notlar"].strip())
    )
    atr_var = isinstance(atr_girdi, dict) and isinstance(atr_girdi.get("ne"), str) and bool(atr_girdi["ne"].strip())
    if not elle_alan_var and not atr_var:
        return copy.deepcopy(mevcut_inceleme) if isinstance(mevcut_inceleme, dict) else None

    taban = copy.deepcopy(mevcut_inceleme) if isinstance(mevcut_inceleme, dict) else {}
    commit = skill.get("inceleme_commit") or skill.get("commit") or taban.get("commit") or ""
    tarih = (
        skill.get("inceleme_tarihi") if _tarih_gecerli(skill.get("inceleme_tarihi"))
        else taban.get("tarih") if _tarih_gecerli(taban.get("tarih"))
        else skill.get("arsiv_tarihi") if _tarih_gecerli(skill.get("arsiv_tarihi"))
        else bugun
    )
    sonuc = skill.get("inceleme") if (skill.get("inceleme") and skill.get("inceleme") != "otomatik") else (taban.get("sonuc") or skill.get("inceleme") or "otomatik")

    ic = dict(taban)
    ic["commit"] = str(commit)
    ic["tarih"] = tarih
    ic["sonuc"] = str(sonuc)

    not_parcalari = []
    if isinstance(skill.get("notlar"), str) and skill["notlar"].strip():
        not_parcalari.append(skill["notlar"].strip())
    elif isinstance(skill.get("kalite_notu"), str) and skill["kalite_notu"].strip():
        not_parcalari.append(skill["kalite_notu"].strip())
    if not_parcalari:
        ic["not"] = " · ".join(not_parcalari)
    elif "not" in taban and isinstance(taban["not"], str):
        ic["not"] = taban["not"]

    for a in INCELEME_METIN_ALANLARI:
        v = skill.get(a)
        if isinstance(v, str) and v.strip():
            ic[a] = v.strip()
    if isinstance(skill.get("kalite"), int) and not isinstance(skill.get("kalite"), bool) and 1 <= skill["kalite"] <= 5:
        ic["kalite"] = skill["kalite"]
    for a in INCELEME_LISTE_ALANLARI:
        v = skill.get(a)
        if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            ic[a] = list(v)
    if atr_var:
        atr_temiz = {"ne": atr_girdi["ne"].strip()}
        if isinstance(atr_girdi.get("ne_zaman"), str) and atr_girdi["ne_zaman"].strip():
            atr_temiz["ne_zaman"] = atr_girdi["ne_zaman"].strip()
        ic["aciklama_tr"] = atr_temiz
    return ic


def fihriste_inceleme_tasi(fihrist, repo_skiller, tutulan_yollar, aciklama_tr, bugun=None):
    """Saf işlev: çıkarılan skillerin inceleme alanlarını ve aciklama-tr.json karşılıklarını fihrist öğelerine taşır;
    `arsivde: true` işaretini yalnız `tutulan_yollar` için bırakır.
    Döner: (yeni_fihrist, {inceleme_notu, tr_aciklama, fihristte_yok})."""
    bugun = bugun or date.today().isoformat()
    tutulan = set(tutulan_yollar)
    yeni = copy.deepcopy(fihrist)
    yol_oge = {x["yol"]: x for x in yeni.get("skiller", []) if isinstance(x, dict) and isinstance(x.get("yol"), str)}

    for yol, oge in yol_oge.items():
        if yol in tutulan:
            oge["arsivde"] = True
        else:
            oge.pop("arsivde", None)

    inceleme_say = 0
    tr_say = 0
    fihristte_yok = []
    for s in repo_skiller:
        yol = s.get("kaynak_yol", "")
        if yol in tutulan:
            continue
        atr_girdi = (aciklama_tr or {}).get(s["id"])
        elle_var = (
            s.get("inceleme") not in (None, "", "otomatik")
            or any(isinstance(s.get(a), str) and s[a].strip() for a in INCELEME_METIN_ALANLARI)
            or any(isinstance(s.get(a), list) and s[a] for a in INCELEME_LISTE_ALANLARI)
            or (isinstance(s.get("notlar"), str) and s["notlar"].strip())
            or (isinstance(s.get("kalite"), int) and not isinstance(s.get("kalite"), bool))
        )
        tr_var = (
            (isinstance(s.get("ozet_tr"), str) and bool(s["ozet_tr"].strip()))
            or (isinstance(atr_girdi, dict) and isinstance(atr_girdi.get("ne"), str) and bool(atr_girdi["ne"].strip()))
        )
        oge = yol_oge.get(yol)
        if oge is None:
            if elle_var or tr_var:
                fihristte_yok.append(yol)
            continue
        ic = inceleme_kaydi_kur(s, atr_girdi, bugun, oge.get("inceleme"))
        if ic is not None:
            oge["inceleme"] = ic
        if elle_var:
            inceleme_say += 1
        if tr_var:
            tr_say += 1
    return yeni, {"inceleme_notu": inceleme_say, "tr_aciklama": tr_say, "fihristte_yok": sorted(fihristte_yok)}


def _kayit_yola_uyar(kayit, yol):
    """kaynak-cek.py ile aynı kural: arşivlenen kaydın dahil / dahil_degil / haric kuralları bu kaynak_yol'u kabul ediyor mu?"""
    if kayit.get("tip") not in ortak.ARSIVLENEN_TIPLER:
        return False
    kontrol = (yol + "/") if yol else "SKILL.md"
    if kayit.get("dahil") and not any(re.search(p, kontrol) for p in kayit["dahil"]):
        return False
    if kayit.get("dahil_degil") and any(re.search(p, kontrol) for p in kayit["dahil_degil"]):
        return False
    if yol and kayit.get("haric") and any(re.search(p, kontrol) for p in kayit["haric"]):
        return False
    return True


def tutulan_kayit_esle(eslesen, tutulan_yollar, repo_skiller):
    """Saf işlev: her tutulan yolu tip ve dahil/dahil_degil/haric kurallarıyla uygun kaynak kaydına eşler.
    Döner: (atama: {index: [yol, ...]}, uymayan: [yol, ...])."""
    yol_tip = {s.get("kaynak_yol", ""): s.get("tip") for s in repo_skiller}
    atama = {i: [] for i in range(len(eslesen))}
    uymayan = []
    for yol in sorted(set(tutulan_yollar)):
        tip = yol_tip.get(yol)
        adaylar = [
            i for i, k in enumerate(eslesen)
            if (tip is None or k.get("tip") == tip) and _kayit_yola_uyar(k, yol)
        ]
        if not adaylar:
            uymayan.append(yol)
            continue
        # Birden çok aday varsa açık 'dahil' kuralına sahip daha özgül kaydı öncele
        adaylar.sort(key=lambda i: (0 if eslesen[i].get("dahil") else 1, i))
        atama[adaylar[0]].append(yol)
    return atama, uymayan


def kaynak_kaydini_guncelle(kaynaklar, repo, tutulan_yollar, repo_skiller, siki=True):
    """Saf işlev: kaynaklar.json'daki arşivlenen repo kayıt(lar)ına tur='dev-koleksiyon', bolum='fihrist' ve arsivde_tut yazar.
    Çok kayıtlı repoda her tutulan yol tip + dahil/dahil_degil/haric kurallarına göre kendi kaydına yazılır;
    siki=True iken hiçbir kayda uymayan yol varsa ValueError yükseltir."""
    yeni = copy.deepcopy(kaynaklar)
    eslesen = [
        k for k in yeni.get("repolar", [])
        if isinstance(k, dict) and str(k.get("repo", "")).lower() == repo.lower()
        and k.get("tip") in ortak.ARSIVLENEN_TIPLER
    ]
    atama, uymayan = tutulan_kayit_esle(eslesen, tutulan_yollar, repo_skiller)
    if siki and uymayan:
        raise ValueError(f"arsivde_tut yolları {repo} kaynak kayıtlarının kurallarına uymuyor: {', '.join(y or '.' for y in uymayan)}")

    for i, k in enumerate(eslesen):
        k["tur"] = "dev-koleksiyon"
        k["bolum"] = "fihrist"
        kayit_tutulan = sorted(atama.get(i, ()))
        if kayit_tutulan:
            k["arsivde_tut"] = kayit_tutulan
        else:
            k.pop("arsivde_tut", None)
        if isinstance(k.get("skill_bagimlilik"), dict):
            kayit_tutulan_set = set(kayit_tutulan)
            k["skill_bagimlilik"] = {y: m for y, m in k["skill_bagimlilik"].items() if y in kayit_tutulan_set}
            if not k["skill_bagimlilik"]:
                k.pop("skill_bagimlilik", None)
    return yeni


def ucret_temizle(ucret_veri, cikarilan_skiller, kalan_skiller):
    """Saf işlev: çıkarılan skillerin ucret-siniflandirma.json satırlarını temizler; kalan skillerin id/ad anahtarlarını korur."""
    yeni = copy.deepcopy(ucret_veri)
    siniflar = yeni.get("siniflar")
    if not isinstance(siniflar, dict):
        return yeni, []
    korunan = {s["id"] for s in kalan_skiller} | {s["ad"] for s in kalan_skiller if s.get("ad")}
    aday = {s["id"] for s in cikarilan_skiller} | {s["ad"] for s in cikarilan_skiller if s.get("ad")}
    silinecek = sorted(k for k in aday if k in siniflar and k not in korunan)
    for k in silinecek:
        siniflar.pop(k, None)
    return yeni, silinecek


def aciklama_tr_temizle(atr_veri, cikarilan_skiller, kalan_skiller):
    """Saf işlev: çıkarılan skillerin aciklama-tr.json satırlarını temizler (anahtar: skill id); kalanları korur."""
    yeni = copy.deepcopy(atr_veri)
    if not isinstance(yeni, dict):
        return yeni, []
    korunan = {s["id"] for s in kalan_skiller}
    silinecek = sorted({s["id"] for s in cikarilan_skiller if s["id"] in yeni and s["id"] not in korunan})
    for k in silinecek:
        yeni.pop(k, None)
    return yeni, silinecek


def yol_istisna_temizle(yol_veri, cikarilan_skiller, eski_adlar=()):
    """Saf işlev: çıkarılan skillerin yol-istisnalari.json satırlarını temizler (anahtar: repo::kaynak_yol); kalanları korur."""
    yeni = copy.deepcopy(yol_veri)
    ist = yeni.get("istisnalar")
    if not isinstance(ist, dict):
        return yeni, []
    eski_k = {e.lower() for e in (eski_adlar or [])}
    hedef_ciftler = set()
    for s in cikarilan_skiller:
        yol = s.get("kaynak_yol", "")
        hedef_ciftler.add((str(s.get("repo", "")).lower(), yol))
        for e in eski_k:
            hedef_ciftler.add((e, yol))
    silinecek = []
    for anahtar in list(ist):
        if "::" not in anahtar:
            continue
        r, yol = anahtar.split("::", 1)
        if (r.lower(), yol) in hedef_ciftler:
            silinecek.append(anahtar)
            ist.pop(anahtar, None)
    return yeni, sorted(silinecek)


def rapor_metni(plan, uygulandi=False, uygulama_sonucu=None):
    baslik = "FİHRİSTE TAŞIMA UYGULANDI" if uygulandi else "FİHRİSTE TAŞIMA PLANI (--kuru; hiçbir dosya değişmedi)"
    o = [baslik, f"Kaynak: {plan['repo']} · fihrist: fihrist/{plan['fihrist_dosya']}"]
    o.append(
        f"Çıkacak: {len(plan['cikarilan_skiller'])} skil, {len(plan['cikarilan_bilesenler'])} bileşen · "
        f"Arşivde kalacak: {len(plan['tutulan_skiller'])} skil · Açılacak yer: {bayt_bicim(plan['acilan_bayt'])}"
    )
    if plan["tutulan_skiller"]:
        o.append("Arşivde kalacak skiller (arsivde_tut):")
        for s in plan["tutulan_skiller"]:
            o.append(f"  - {s['id']} ({s.get('kaynak_yol') or '.'})")
    else:
        o.append("Arşivde kalacak skil: yok")

    kul = plan["kullanilan"]
    o.append("Etkilenen rol / profil / projeler:")
    if plan["proje_bilgisi"] == "yok":
        o.append("  DURUM: canlı proje kilidi ve notlar/proje-kullanimi.md bulunamadı; proje kullanımı doğrulanamadı (HATA).")
    elif plan["proje_bilgisi"] == "md":
        o.append("  (proje bilgisi: notlar/proje-kullanimi.md)")
    if not kul:
        o.append("  Hiçbir rol, profil ya da projede kullanılmıyor.")
    else:
        for yol, bilgi in sorted(kul.items()):
            parcalar = []
            if bilgi["roller"]:
                parcalar.append("roller: " + ", ".join(bilgi["roller"]))
            if bilgi["profiller"]:
                parcalar.append("profiller: " + ", ".join(bilgi["profiller"]))
            if bilgi["projeler"]:
                parcalar.append("projeler: " + ", ".join(bilgi["projeler"]))
            durum = "KORUNUYOR" if yol in plan["tutulan_yollar"] else "EKSİK (arsivde_tut'ta yok!)"
            o.append(f"  - {bilgi['skill']['id']} ({yol or '.'}) [{durum}] -> " + " | ".join(parcalar))

    oz = plan["inceleme_ozet"]
    o.append(f"Fihriste taşınacak notlar: {oz['inceleme_notu']} inceleme notu, {oz['tr_aciklama']} Türkçe açıklama")
    if oz["fihristte_yok"]:
        yollar_m = ", ".join((y or ".") for y in oz["fihristte_yok"][:10])
        o.append(f"  Fihrist dosyasında karşılığı bulunmayan (taşınamayacak) {len(oz['fihristte_yok'])} yol: {yollar_m}")

    o.append(
        f"Temizlenecek yardımcı kayıtlar: ucret-siniflandirma={len(plan['temizlenecek']['ucret'])}, "
        f"aciklama-tr={len(plan['temizlenecek']['aciklama_tr'])}, yol-istisnalari={len(plan['temizlenecek']['yol_istisna'])}"
    )

    if plan["tercih_degisenler"]:
        o.append("Çıplak ad / tercih el değişimi:")
        for d in plan["tercih_degisenler"]:
            ek = " (çıplak ad boşaldı; kimlikler rehber/09 gereği değişmedi)" if d["ciplak_ad_bosaldi"] else ""
            o.append(f"  - {d['ad']}: {d['eski_id']} ({d['eski_repo']}) -> yeni tercih {d['yeni_id']} ({d['yeni_repo']}){ek}")
    else:
        o.append("Çıplak ad / tercih el değişimi: yok")

    if plan["hatalar"]:
        for h in plan["hatalar"]:
            o.append(f"HATA: {h}")
        if plan["eksik_tutulan"]:
            bayraklar = " ".join('--arsivde-tut ""' if y == "" else f"--arsivde-tut {y}" for y in plan["eksik_tutulan"])
            o.append(f"Öneri: {bayraklar}")
        return "\n".join(o)

    if uygulandi and uygulama_sonucu:
        o.append(
            f"Silinen arşiv öğeleri: {uygulama_sonucu['silinen_skil_klasoru']} skil klasörü, "
            f"{uygulama_sonucu['silinen_varyant_klasoru']} araç sürümü, "
            f"{uygulama_sonucu['silinen_bilesen_dosyasi']} bileşen dosyası ({bayt_bicim(uygulama_sonucu['acilan_bayt'])})"
        )
        o.append("Sonraki adımlar (katalog ve denetim):")
        o.append("  python3 araclar/katalog-uret.py && python3 araclar/skill-readme.py")
        o.append("  python3 araclar/dogrula.py")
        o.append("  python3 araclar/kapsam-denetimi.py")
    else:
        o.append("Katalog notu: uygulamadan sonra katalog dosyalarını yenile: python3 araclar/katalog-uret.py && python3 araclar/skill-readme.py")
    return "\n".join(o)


# ------------------------------------------------------------------ disk işlemleri (ağ yok)
class OnKosulHata(Exception):
    """Ön koşul eksik / hedef bulunamadı: çıkış kodu 2."""


def git_calisma_agaci_kontrol(kok):
    """Git çalışma ağacının temizliğini denetler (salt okuma; --no-optional-locks indeksi değiştirmez).
    Döner: (temiz_mi: bool, neden: str). Git deposu değilse ya da status okunamazsa temiz sayılmaz."""
    try:
        r = subprocess.run(
            ["git", "--no-optional-locks", "status", "--porcelain"],
            cwd=str(kok),
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as e:
        return False, f"git status çalıştırılamadı: {e}"
    if r.returncode != 0:
        err = (r.stderr or r.stdout or "").strip().splitlines()
        detay = err[0] if err else f"çıkış kodu {r.returncode}"
        return False, f"git çalışma ağacı doğrulanamadı ({detay})"
    satirlar = [s for s in r.stdout.splitlines() if s.strip()]
    if satirlar:
        ornek = ", ".join(s.strip() for s in satirlar[:5])
        ek = f" (+{len(satirlar) - 5})" if len(satirlar) > 5 else ""
        return False, f"git çalışma ağacı temiz değil ({len(satirlar)} değişiklik: {ornek}{ek})"
    return True, ""


def _atomik_json_toplu_yaz(yazilacaklar):
    """Hazırlanmış [(hedef_yol, json_metni), ...] çiftlerini iki fazlı atomik olarak yazar:
    1) Önce tüm dosyalar kendi klasörlerindeki geçici dosyalara yazılır ve fsync edilir (hata çıkarsa
       oluşturulan tüm geçici dosyalar silinir, hiçbir hedef dosya değişmez).
    2) Ardından tüm geçici dosyalar os.replace ile atomik olarak hedeflerin yerine taşınır."""
    geciciler = []
    try:
        for hedef, metin in yazilacaklar:
            hedef = Path(hedef)
            hedef.parent.mkdir(parents=True, exist_ok=True)
            fd, gecici_ad = tempfile.mkstemp(prefix=f".{hedef.name}.", suffix=".tmp", dir=str(hedef.parent))
            gecici = Path(gecici_ad)
            geciciler.append((gecici, hedef))
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(metin)
                fh.flush()
                os.fsync(fh.fileno())
    except Exception:
        for gecici, _ in geciciler:
            gecici.unlink(missing_ok=True)
        raise

    try:
        for gecici, hedef in geciciler:
            os.replace(gecici, hedef)
    except Exception as e:
        for gecici, _ in geciciler:
            gecici.unlink(missing_ok=True)
        raise RuntimeError(
            f"JSON atomik yeniden adlandırma sırasında hata ({e}). "
            "Kurtarma: git restore --source=HEAD --staged --worktree ."
        ) from e


def planla(kok, repo, arsivde_tut=None, bugun=None, ayar=None):
    """Salt okuma: taşıma planını hesaplar. Ağ kullanmaz, hiçbir dosyaya yazmaz."""
    kok = Path(kok)
    bugun = bugun or date.today().isoformat()
    kaynaklar = ortak.json_oku(kok / "kaynaklar.json")
    registry = ortak.json_oku(kok / "registry.json")
    if not isinstance(kaynaklar, dict) or not isinstance(registry, dict):
        raise OnKosulHata("kaynaklar.json ya da registry.json okunamadı")

    kcik = _modul("kaynak-cikar")
    dg = _modul("dogrula")
    try:
        rapor = kcik.rapor_uret(kok, "repo", repo, bugun=bugun, ayar=ayar)
    except kcik.HedefHata as e:
        raise OnKosulHata(str(e)) from e

    if rapor["karar"] == "yok":
        raise OnKosulHata(f"Kaynak zaten çıkarılmış: {repo}")
    if rapor["karar"] == "reddedildi":
        raise OnKosulHata(rapor.get("mesaj") or f"Program kaynağı fihriste taşınamaz: {repo}")

    canon = rapor["hedef"]["repo"]
    kayitlar = [k for k in kaynaklar.get("repolar", []) if isinstance(k, dict) and str(k.get("repo", "")).lower() == canon.lower()]
    if not kayitlar:
        raise OnKosulHata(f"kaynaklar.json içinde kayıt bulunamadı: {canon}")

    f_adi = dosya_adi(canon)
    f_yol = kok / "fihrist" / f_adi
    if not f_yol.is_file():
        raise OnKosulHata(f"fihrist/{f_adi} yok; önce üret: python3 araclar/fihrist-uret.py {canon}")
    try:
        fihrist = ortak.json_oku(f_yol)
    except ValueError as e:
        raise OnKosulHata(f"fihrist/{f_adi} ayrıştırılamadı: {e}") from e
    f_hata = dg.fihrist_hatalari(fihrist, canon)
    if f_hata:
        raise OnKosulHata(f"fihrist/{f_adi} şema hatası: {f_hata[0]}")

    repo_skiller = [s for s in registry.get("skiller", []) if str(s.get("repo", "")).lower() == canon.lower()]
    repo_yollar = {s.get("kaynak_yol", "") for s in repo_skiller}
    tutulan_yollar = arsivde_tut_coz(arsivde_tut, kayitlar)
    tutulan_set = set(tutulan_yollar)

    eski_adlar = sorted({e for k in kayitlar for e in k.get("eski_adlar", [])})
    md_projeler = []
    proje_bilgisi = rapor["proje_bilgisi"]
    if proje_bilgisi == "yok":
        pk_md = kok / "notlar" / "proje-kullanimi.md"
        if pk_md.is_file():
            md_projeler = proje_kullanimi_md_coz(pk_md.read_text(encoding="utf-8", errors="replace"), canon, eski_adlar)
            proje_bilgisi = "md"

    kullanilan, eslesmeyen_kullanilan = kullanilan_skilleri_bul(repo_skiller, rapor, md_projeler)
    hatalar = []
    if proje_bilgisi == "yok":
        hatalar.append("proje kullanımı doğrulanamadı (canlı proje kilidi ve notlar/proje-kullanimi.md bulunamadı)")
    for e in eslesmeyen_kullanilan:
        hatalar.append(f"kullanım girdisi {canon} arşiv skilleriyle eşleşmedi: {e}")

    eksik_tutulan = sorted(y for y in kullanilan if y not in tutulan_set)
    for y in eksik_tutulan:
        b = kullanilan[y]
        yerler = b["roller"] + b["profiller"] + b["projeler"]
        hatalar.append(f"kullanılan skil arsivde_tut'ta değil: {b['skill']['id']} ({y or '.'}) -> {', '.join(yerler)}")
    for y in tutulan_yollar:
        if y not in repo_yollar:
            hatalar.append(f"arsivde_tut yolu {canon} arşivinde bulunamadı: {y or '.'}")

    arsivlik_kayitlar = [k for k in kayitlar if k.get("tip") in ortak.ARSIVLENEN_TIPLER]
    _, uymayan_kayit_yollar = tutulan_kayit_esle(
        arsivlik_kayitlar, [y for y in tutulan_yollar if y in repo_yollar], repo_skiller
    )
    for y in uymayan_kayit_yollar:
        hatalar.append(f"arsivde_tut yolu {canon} kaynak kayıtlarının tip/dahil/haric kurallarına uymuyor: {y or '.'}")

    tutulan_skiller = [s for s in repo_skiller if s.get("kaynak_yol", "") in tutulan_set]
    cikarilacak_idler = {s["id"] for s in repo_skiller if s.get("kaynak_yol", "") not in tutulan_set}
    oncelikler = {}
    for k in kaynaklar.get("repolar", []):
        if isinstance(k, dict) and isinstance(k.get("repo"), str):
            r = k["repo"].lower()
            oncelikler[r] = min(oncelikler.get(r, 99), k.get("oncelik", 5))

    yeni_reg, reg_sonuc = kcik.registryden_cikar(
        registry, cikarilacak_idler, bilesen_repolar=[canon], oncelikler=oncelikler, fihrist_tutulan={canon: tutulan_set}
    )
    yeni_reg["guncelleme"] = bugun
    cikarilan_skiller = reg_sonuc["cikarilan_skiller"]
    cikarilan_bilesenler = reg_sonuc["cikarilan_bilesenler"]
    kalan_skiller = yeni_reg["skiller"]
    kalan_bilesenler = yeni_reg.get("bilesenler", [])

    for sh in kcik.arsiv_silme_hatalari(kok, cikarilan_skiller, cikarilan_bilesenler, kalan_skiller, kalan_bilesenler):
        hatalar.append(f"arşiv silme güvenlik engeli: {sh}")

    acilan_bayt = kcik.acilan_bayt_hesapla(kok, cikarilan_skiller, cikarilan_bilesenler)
    aciklama_tr = ortak.json_oku(kok / "aciklama-tr.json", {}) or {}
    ucret_veri = ortak.json_oku(kok / "ucret-siniflandirma.json", None)
    yol_veri = ortak.json_oku(kok / "yol-istisnalari.json", None)

    yeni_fihrist, inceleme_ozet = fihriste_inceleme_tasi(fihrist, repo_skiller, tutulan_set, aciklama_tr, bugun)
    if inceleme_ozet["fihristte_yok"]:
        yollar_m = ", ".join((y or ".") for y in inceleme_ozet["fihristte_yok"][:10])
        fazla = f" (+{len(inceleme_ozet['fihristte_yok']) - 10})" if len(inceleme_ozet["fihristte_yok"]) > 10 else ""
        hatalar.append(
            f"inceleme notu veya Türkçe açıklaması fihristte karşılık bulamayan {len(inceleme_ozet['fihristte_yok'])} yol "
            f"(veri kaybını önlemek için durduruldu; fihristi yenileyin ya da --arsivde-tut ile koruyun): {yollar_m}{fazla}"
        )

    yeni_kaynaklar = kaynak_kaydini_guncelle(kaynaklar, canon, tutulan_yollar, repo_skiller, siki=False)
    yeni_ucret, sil_ucret = ucret_temizle(ucret_veri, cikarilan_skiller, kalan_skiller) if isinstance(ucret_veri, dict) else (None, [])
    yeni_atr, sil_atr = aciklama_tr_temizle(aciklama_tr, cikarilan_skiller, kalan_skiller) if (kok / "aciklama-tr.json").is_file() else (None, [])
    yeni_yol, sil_yol = yol_istisna_temizle(yol_veri, cikarilan_skiller, eski_adlar) if isinstance(yol_veri, dict) else (None, [])

    return {
        "repo": canon,
        "fihrist_dosya": f_adi,
        "fihrist_yol": f_yol,
        "tutulan_yollar": tutulan_yollar,
        "tutulan_skiller": tutulan_skiller,
        "cikarilan_skiller": cikarilan_skiller,
        "cikarilan_bilesenler": cikarilan_bilesenler,
        "acilan_bayt": acilan_bayt,
        "kullanilan": kullanilan,
        "eslesmeyen_kullanilan": eslesmeyen_kullanilan,
        "proje_bilgisi": proje_bilgisi,
        "eksik_tutulan": eksik_tutulan,
        "hatalar": hatalar,
        "tercih_degisenler": reg_sonuc["tercih_degisenler"],
        "inceleme_ozet": inceleme_ozet,
        "temizlenecek": {"ucret": sil_ucret, "aciklama_tr": sil_atr, "yol_istisna": sil_yol},
        "_yeni": {
            "fihrist": yeni_fihrist,
            "registry": yeni_reg,
            "kaynaklar": yeni_kaynaklar,
            "ucret": yeni_ucret,
            "aciklama_tr": yeni_atr,
            "yol_istisna": yeni_yol,
        },
    }


def uygula(kok, plan):
    """Planı diske uygular (--evet).

    Yazma ve silme sırası ile gerekçesi (yarıda kesilme / tutarsızlık koruması):
      0. Ön kapılar: plan['hatalar'] boş olmalı, git çalışma ağacı temiz olmalı ve arşiv silme güvenlik
         denetimi geçmeli; herhangi biri başarısızsa tek bir dosyaya dokunulmadan ValueError ile durulur.
      1. Hazırlama (bellekte): bütün JSON çıktıları (fihrist, registry, kaynaklar ve değişen yardımcı dosyalar)
         diske yazmadan önce serileştirilir; serileştirme hatasında hiçbir dosya değişmez.
      2. Atomik JSON yazımları: tüm JSON'lar önce kendi klasörlerindeki geçici dosyalara yazılıp fsync edilir,
         sonra os.replace ile atomik olarak hedeflerin yerine taşınır (yarım JSON kalmaz; fihristteki inceleme
         ve Türkçe açıklama kayıtları ile yeni registry/kaynaklar güvenle kaydedilir).
      3. Arşiv silme EN SON: kaynak-cikar.arsivden_cikar (kalan skiller ve bileşenler korunan küme olarak
         verilerek) ancak bütün JSON yazımları başarıyla bittikten sonra çağrılır. Böylece herhangi bir JSON
         yazım hatasında arsiv/ klasörleri zarar görmez; beklenmedik bir kesintide temiz git başlangıcına
         (git restore --source=HEAD --staged --worktree .) güvenle dönülebilir.
    """
    if plan["hatalar"]:
        raise ValueError("Hatalı plan uygulanamaz: " + "; ".join(plan["hatalar"]))
    kok = Path(kok)
    temiz, neden = git_calisma_agaci_kontrol(kok)
    if not temiz:
        raise ValueError(f"Taşıma uygulanamadı (--evet öncesi git çalışma ağacı temiz olmalı): {neden}")

    kcik = _modul("kaynak-cikar")
    yeni = plan["_yeni"]
    kalan_skiller = yeni["registry"].get("skiller", [])
    kalan_bilesenler = yeni["registry"].get("bilesenler", [])
    silme_hatalari = kcik.arsiv_silme_hatalari(
        kok, plan["cikarilan_skiller"], plan["cikarilan_bilesenler"], kalan_skiller, kalan_bilesenler
    )
    if silme_hatalari:
        raise ValueError("Arşiv silme güvenlik engeli: " + "; ".join(silme_hatalari))

    # 1. Önce bütün JSON çıktılarını bellekte hazırla ve serileştir (hata çıkarsa diske dokunulmaz).
    hedefler = [
        (plan["fihrist_yol"], yeni["fihrist"]),
        (kok / "registry.json", yeni["registry"]),
        (kok / "kaynaklar.json", yeni["kaynaklar"]),
    ]
    if yeni["ucret"] is not None and plan["temizlenecek"]["ucret"]:
        hedefler.append((kok / "ucret-siniflandirma.json", yeni["ucret"]))
    if yeni["aciklama_tr"] is not None and plan["temizlenecek"]["aciklama_tr"]:
        hedefler.append((kok / "aciklama-tr.json", yeni["aciklama_tr"]))
    if yeni["yol_istisna"] is not None and plan["temizlenecek"]["yol_istisna"]:
        hedefler.append((kok / "yol-istisnalari.json", yeni["yol_istisna"]))
    hazir_jsonlar = [(yol, json.dumps(veri, ensure_ascii=False, indent=2) + "\n") for yol, veri in hedefler]

    # 2. Bütün JSON'ları geçici dosya + atomik yeniden adlandırma (os.replace) ile diske yaz.
    _atomik_json_toplu_yaz(hazir_jsonlar)

    # 3. En son arşiv klasör ve bileşen dosyalarını sil (kalan skiller ve bileşenler korunur).
    return kcik.arsivden_cikar(
        kok,
        plan["cikarilan_skiller"],
        plan["cikarilan_bilesenler"],
        kalan_skiller=kalan_skiller,
        kalan_bilesenler=kalan_bilesenler,
    )


def main(argv=None, kok=None):
    ap = argparse.ArgumentParser(description="Arşivli kaynağı fihriste taşır (ağ kullanmaz)")
    ap.add_argument("repo", help="owner/ad")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--kuru", action="store_true", help="yalnız rapor; dosya değiştirme (varsayılan)")
    g.add_argument("--evet", action="store_true", help="taşıma işlemini uygula (kullanıcı onayıyla)")
    ap.add_argument("--arsivde-tut", action="append", default=None,
                    help="arşivde kalacak skilin kaynak_yol'u (birden çok kez ya da virgülle verilebilir)")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", a.repo):
        print("HATA: repo 'owner/ad' biçiminde olmalı", file=sys.stderr)
        return 2
    kok = Path(kok) if kok is not None else ortak.KOK
    try:
        plan = planla(kok, a.repo, arsivde_tut=a.arsivde_tut)
    except OnKosulHata as e:
        print(f"HATA: {e}", file=sys.stderr)
        return 2
    if plan["hatalar"]:
        print(rapor_metni(plan, uygulandi=False))
        return 1
    if not a.evet:
        print(rapor_metni(plan, uygulandi=False))
        return 0
    temiz, neden = git_calisma_agaci_kontrol(kok)
    if not temiz:
        print(rapor_metni(plan, uygulandi=False))
        print(f"HATA: --evet öncesi git çalışma ağacı temiz olmalı: {neden}")
        return 1
    sonuc = uygula(kok, plan)
    print(rapor_metni(plan, uygulandi=True, uygulama_sonucu=sonuc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
