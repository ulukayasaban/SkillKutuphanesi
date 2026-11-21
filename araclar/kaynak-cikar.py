#!/usr/bin/env python3
"""Kaynak çıkarma ETKİ RAPORU (yalnız okuma). Bu sürümde SADECE --kuru vardır; hiçbir dosyayı ve hiçbir GitHub kaydını değiştirmez.
Bir kaynak repo (--repo) ya da bir skill (--skill) için: onu kullanan projeler, roller/profiller, registry, çıplak ad devri,
yıldız/liste, kartlar ve kayıt dosyaları; sonra sıralı adımlar ve geri alma. Uygulayan mod yok: adımları kullanıcı onayıyla ajan elle yapar.

  python3 araclar/kaynak-cikar.py --repo owner/ad --kuru [--neden "gerekçe"] [--json] [--github] [--siki]
  python3 araclar/kaynak-cikar.py --skill <kimlik|ad> --kuru [--neden "gerekçe"] [--json] [--github] [--siki]

--github  : yalnız okuma: repo erişilebilir mi / adı değişmiş mi (gh api repos/..), yıldız durumu, liste üyeliği.
--json    : tek bir JSON nesnesi yazar (başka hiçbir şey yazmaz).
--siki    : karar 'engel' ya da 'reddedildi' ise çıkış kodu 1.
Çıkış kodu: 0 rapor üretildi (karar ne olursa olsun) · 1 yalnız --siki ile engel/reddedildi · 2 kullanım hatası / hedef bulunamadı /
birden çok kayıt / --kuru verilmedi.

Neden uygulayan mod yok: (1) çıkarma nadirdir (defterde 9 tam repo kaydı); elle iş tek JSON kaydı ve birkaç rol satırıdır.
(2) Tehlikeli ve sık atlanan kısım etki kontrolüdür; onu bu araç otomatikleştirir. (3) 181 kayıtlık kaynaklar.json'u yeniden yazmak
ve rol/profil dosyalarını düzenlemek yedek, kuru çalıştırma ve onay işi getirir; kazanılan yazma zahmetinden büyüktür.
(4) Üç ayda ~10'dan fazla çıkarma olursa ya da elle bir adım iki kez yanlış yapılırsa yeniden düşünülür.
Kural 6: proje adları yalnız ekrana yazılır; bu araç hiçbir şey kaydetmez.
"""
import argparse
import copy
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ARAC_KLASORU = Path(__file__).resolve().parent
sys.path.insert(0, str(ARAC_KLASORU))
from ortak import json_oku  # noqa: E402

KAYIT_DOSYALARI = ("kaynaklar.json", "kategori-kurallari.json", "ucret-siniflandirma.json", "gelistiriciler.json", "trend.json",
                   "konu-takip.json", "yol-istisnalari.json", "programlar.json", "projeler.json")
GERI_ALMA = [
    "Commit atılmadıysa: değişiklikleri kullanıcıya göster; onaylarsa: git restore --source=HEAD --staged --worktree .   "
    "sonra: git clean -n -d arsiv   (listeyi göster; silmeden önce yine sor)",
    "Commit atıldıysa (push edilse de edilmese de): git revert <commit>   (tek commit; merge commit ise -m 1). kaynaklar.json, registry, "
    "arşiv, katalog, roller geri gelir. Push yalnız kullanıcı isterse.",
    "Projeden kaldırılan skiller: python3 araclar/skill-ekle.py \"<yol>\" --geri-al <yedek adı>   (kaldırma çıktısı yedek adını yazdı)",
    "GitHub yıldız/liste (git revert kapsamaz): python3 araclar/listeye-ekle.py <owner/ad>   (kullanıcı onayıyla)",
]
PLACEHOLDER_NEDEN = "<NEDEN: kullanıcının onayladığı gerekçe>"


class HedefHata(Exception):
    """Hedef bulunamadı / belirsiz: çıkış kodu 2."""


def _modul(ad):
    """araclar/ klasöründen (kütüphane kökünden DEĞİL) bir aracı tembel yükler; içe aktarma yan etkisizdir."""
    spec = importlib.util.spec_from_file_location(ad.replace("-", "_"), ARAC_KLASORU / f"{ad}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _kisa(yol):
    y = str(yol)
    h = str(Path.home())
    return "~" + y[len(h):] if y.startswith(h) else y


def _acik(yol):
    """'~/…' kısa yolunu komutta çalışacak tam yola çevirir (çift tırnak içinde ~ açılmaz)."""
    return str(Path(yol).expanduser())


def _liste(x):
    if not x:
        return []
    if isinstance(x, str):
        return [x]
    if isinstance(x, dict):
        return list(x)
    return [str(i) for i in x]


def _gh_calistir(args):
    try:
        r = subprocess.run(["gh"] + args, capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout, r.stderr
    except Exception as e:  # noqa: BLE001
        return 99, "", str(e)


def _github_oku(canon, gh, listeler):
    """Salt okuma. Her hata 'okunamadı' olur, çalıştırmayı düşürmez."""
    g = {"erisim": "okunamadı", "yeni_ad": None, "yildiz": "okunamadı", "listeler": "okunamadı"}
    try:
        rc, out, err = gh(["api", f"repos/{canon}", "--jq", ".full_name"])
        if rc == 0 and out.strip():
            tam = out.strip()
            g["erisim"] = f"erişilebilir ({tam})"
            if tam.lower() != canon.lower():
                g["yeni_ad"] = tam
        elif "404" in (out + err):
            g["erisim"] = "404: kaynak kayıp"
    except Exception:  # noqa: BLE001
        pass
    try:
        rc, out, err = gh(["api", f"user/starred/{canon}"])
        if rc == 0:
            g["yildiz"] = "yıldızlı"
        elif "404" in (out + err) or rc == 1:
            g["yildiz"] = "yıldızsız"
    except Exception:  # noqa: BLE001
        pass
    try:
        ls = listeler()
        g["listeler"] = sorted(l["name"] for l in ls
                               if any(x and x.get("nameWithOwner", "").lower() == canon.lower() for x in l["items"]["nodes"]))
    except Exception:  # noqa: BLE001
        pass
    return g


def _satirlar(yol, desenler):
    """Dosyada desenlerden (küçük harf) birini içeren satır numaraları; okunamazsa []."""
    try:
        metin = Path(yol).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    return [i for i, s in enumerate(metin.splitlines(), 1) if any(d in s.lower() for d in desenler)]


def rapor_uret(kok, hedef_turu, hedef, neden=None, github=False, bugun=None, gh=None, listeler=None, ayar=None):
    """Salt okuma. kok: kütüphane kökü (testlerde geçici ağaç). -> rapor sözlüğü. HedefHata: hedef yok/belirsiz.
    ayar: projeler.json yerine verilecek sözlük (testler); None ise kok/projeler.json okunur."""
    kok = Path(kok)
    bugun = bugun or date.today().isoformat()
    kaynaklar = json_oku(kok / "kaynaklar.json", {}) or {}
    registry = json_oku(kok / "registry.json", {}) or {}
    skiller = registry.get("skiller", [])
    kayitlar_k = kaynaklar.get("repolar", [])
    eski = {}
    for k in kayitlar_k:
        for e in k.get("eski_adlar", []):
            eski[e.lower()] = k["repo"]

    def guncel(r):
        return eski.get((r or "").lower(), r or "")

    # ---------------------------------------------------------------- 0. hedef
    notlar = []
    cikarilan = {(_r["repo"] if isinstance(_r, dict) else _r).lower(): _r for _r in kaynaklar.get("arsivden_cikarilan_repolar", [])}
    skill_hedef = None
    if hedef_turu == "repo":
        canon = guncel(hedef)
        kayitlar = [k for k in kayitlar_k if k["repo"].lower() == canon.lower()]
        if kayitlar:
            canon = kayitlar[0]["repo"]
        hedef_skiller = [s for s in skiller if guncel(s["repo"]).lower() == canon.lower()]
        if not kayitlar:
            if canon.lower() in cikarilan:
                c = cikarilan[canon.lower()]
                ek = f" ({c.get('tarih', '?')}, {c.get('neden', '-')}). Geri alma: {c.get('geri_alma', '-')}" if isinstance(c, dict) else ""
                return {"arac": "kaynak-cikar", "mod": "kuru", "hedef": {"tur": "repo", "repo": canon, "eski_adlar": [], "kaynak_tur": None, "bolum": None,
                        "kayit_sayisi": 0, "skill_sayisi": 0, "kayip": False, "program": None},
                        "karar": "yok", "engeller": [], "dikkatler": [], "projeler": [], "proje_bilgisi": "yok", "roller": [],
                        "profiller": [], "registry": {"idler": [], "alternatif_kardesler": [], "ortusme": [], "kopya_kaynaklar": []},
                        "ad_devri": {"bu_kaydin": [], "baska_kayitlarin": []}, "kayitlar": [], "github": None, "defter_taslagi": None,
                        "adimlar": [], "geri_alma": [], "mesaj": "Zaten çıkarılmış" + ek}
            if hedef_skiller:
                notlar.append("orphan: registry'de bu repoya ait skill var ama kaynaklar.json'da kaydı yok")
            else:
                raise HedefHata(f"Bulunamadı: {hedef} (ne kaynaklar.json'da ne registry'de)")
    else:
        sk = next((s for s in skiller if s["id"] == hedef), None)
        if sk is None:
            adaylar = [s for s in skiller if s.get("ad") == hedef]
            if len(adaylar) > 1:
                raise HedefHata("Birden çok kayıt: tam kimliği yaz: --skill <id>\n  " + "\n  ".join(
                    f"{s['id']} ({s.get('durum')}, {s['repo']})" for s in adaylar))
            if not adaylar:
                raise HedefHata(f"Bulunamadı: skill {hedef}")
            sk = adaylar[0]
        skill_hedef = sk
        canon = guncel(sk["repo"])
        kayitlar = [k for k in kayitlar_k if k["repo"].lower() == canon.lower()]
        if kayitlar:
            canon = kayitlar[0]["repo"]
        hedef_skiller = [sk]
        if len([s for s in skiller if guncel(s["repo"]).lower() == canon.lower()]) == 1:
            notlar.append("bu repodaki tek skill: tüm kaynağı çıkarmak için --repo")
    ids = {s["id"] for s in hedef_skiller}
    tercih_adlar = {s.get("ad") for s in hedef_skiller if s.get("durum") == "tercih"}
    kaynak_tur = kayitlar[0].get("tur") if kayitlar else None
    bolum = kayitlar[0].get("bolum") if kayitlar else None
    programlar = sorted({k["program"] for k in kayitlar if k.get("program")})
    eski_adlar = sorted({e for k in kayitlar for e in k.get("eski_adlar", [])})
    hedef_bilgi = {"tur": hedef_turu, "repo": canon, "eski_adlar": eski_adlar, "kaynak_tur": kaynak_tur, "bolum": bolum,
                   "kayit_sayisi": len(kayitlar), "skill_sayisi": len(hedef_skiller),
                   "kayip": any(k.get("durum") == "kayip" for k in kayitlar),
                   "program": programlar[0] if programlar else None}
    if skill_hedef:
        hedef_bilgi.update({"id": skill_hedef["id"], "ad": skill_hedef.get("ad"), "kaynak_yol": skill_hedef.get("kaynak_yol"),
                            "durum": skill_hedef.get("durum"), "kaynak_durumu": skill_hedef.get("kaynak_durumu")})
    if len(set(c for c in (s.get("commit") for s in hedef_skiller) if c)) > 0:
        son_commit = sorted(c for c in (s.get("commit") for s in hedef_skiller) if c)[0]
    else:
        son_commit = ""

    rapor = {"arac": "kaynak-cikar", "mod": "kuru", "hedef": hedef_bilgi, "karar": None, "engeller": [], "dikkatler": [],
             "projeler": [], "proje_bilgisi": "yok", "roller": [], "profiller": [],
             "registry": {"idler": [], "alternatif_kardesler": [], "ortusme": [], "kopya_kaynaklar": []},
             "ad_devri": {"bu_kaydin": [], "baska_kayitlarin": []}, "kayitlar": [], "github": None, "defter_taslagi": None,
             "adimlar": [], "geri_alma": [], "notlar": notlar}

    # programa bağlı kaynak: bu yolla çıkarılmaz
    if programlar:
        rapor["registry"]["sayim"] = {"tercih": sum(1 for s in hedef_skiller if s.get("durum") == "tercih"),
                                      "alternatif": sum(1 for s in hedef_skiller if s.get("durum") != "tercih")}
        rapor["karar"] = "reddedildi"
        rapor["mesaj"] = (f"Bu kaynak bir PROGRAM olarak da izleniyor (kaynaklar.json \"program\": \"{programlar[0]}\"). "
                          "Programı çıkarma rehber/11 → 'Programı çıkarma' bölümündedir; önce oradaki adımlar. Bu araç adım üretmez.")
        return rapor

    dikkat, engel = rapor["dikkatler"], rapor["engeller"]

    # ---------------------------------------------------------------- 1. projeler
    ayar = ayar if ayar is not None else (json_oku(kok / "projeler.json", {}) or {})
    pk = _modul("proje-kullanimi")
    if not pk.projeleri_bul(ayar):
        rapor["proje_bilgisi"] = "yok"
        dikkat.append("projeler: bu bilgisayarda proje bulunamadı, etki BİLİNMİYOR (başka bilgisayar/bulut olabilir)")
    else:
        rapor["proje_bilgisi"] = "var"
        for p in pk.oku(ayar):
            eslesen = []
            for ad, v in (p["kilit"].get("skiller") or {}).items():
                vrepo = guncel(v.get("repo")).lower()
                if hedef_turu == "repo":
                    uyar = vrepo == canon.lower()
                else:
                    uyar = v.get("id", ad) == skill_hedef["id"] or (vrepo, v.get("kaynak_yol")) == (canon.lower(), skill_hedef.get("kaynak_yol"))
                if uyar:
                    eslesen.append({"kurulu_ad": ad, "id": v.get("id", ad), "roller": list(v.get("roller", []))})
            if eslesen:
                rapor["projeler"].append({"proje": p["ad"], "yol": _kisa(p["yol"]), "skiller": eslesen})
        if rapor["projeler"]:
            dikkat.append(f"projeler: {len(rapor['projeler'])} projede kurulu")

    # ---------------------------------------------------------------- 2. roller ve profiller
    def esler(girdi):
        return girdi in ids or girdi in tercih_adlar

    rol_adlari = set()
    for dosya in sorted((kok / "roller").glob("*.json")):
        r = json_oku(dosya, {}) or {}
        for alan in ("cekirdek", "opsiyonel"):
            for g in r.get(alan, []):
                if esler(g):
                    rapor["roller"].append({"dosya": f"roller/{dosya.name}", "alan": alan, "girdi": g})
                    rol_adlari.add(r.get("ad") or dosya.stem)
    for dosya in sorted((kok / "profiller").glob("*.json")):
        pr = json_oku(dosya, {}) or {}
        for g in pr.get("ek_skiller", []):
            if esler(g):
                rapor["profiller"].append({"dosya": f"profiller/{dosya.name}", "alan": "ek_skiller", "girdi": g})
    rapor["etkilenen_profiller"] = sorted(f"profiller/{d.name}" for d in (kok / "profiller").glob("*.json")
                                          if rol_adlari & set((json_oku(d, {}) or {}).get("roller", [])))
    for x in rapor["roller"] + rapor["profiller"]:
        engel.append(f"{x['dosya']}: {x['alan']}: {x['girdi']}")

    # ---------------------------------------------------------------- 3. registry
    reg = rapor["registry"]
    reg["idler"] = sorted(ids)
    reg["sayim"] = {"tercih": sum(1 for s in hedef_skiller if s.get("durum") == "tercih"),
                    "alternatif": sum(1 for s in hedef_skiller if s.get("durum") != "tercih")}
    reg["ilk_30"] = [f"{s['id']} ({s.get('durum')}, {s.get('kaynak_durumu')})" for s in sorted(hedef_skiller, key=lambda x: x["id"])[:30]]
    reg["kopya_kaynaklar"] = sorted({str(c) for s in hedef_skiller for c in _liste(s.get("kopya_kaynaklar"))})
    adlar = {s.get("ad") for s in hedef_skiller}
    reg["alternatif_kardesler"] = sorted(s["id"] for s in skiller if s.get("ad") in adlar and s["id"] not in ids)
    gruplar = {s.get("ortusme_grubu") for s in hedef_skiller if s.get("ortusme_grubu")}
    for gr in sorted(gruplar):
        uyeler = [s["id"] for s in skiller if s.get("ortusme_grubu") == gr]
        reg["ortusme"].append({"grup": gr, "uyeler": uyeler})
        if any(s.get("ortusme_grubu") == gr and s.get("ortusme_rolu") == "birincil" for s in hedef_skiller):
            dikkat.append(f"{gr} grubunun birincil skili gidiyor")
    reg["cocuklar"] = sorted(s["id"] for s in skiller if s.get("ust_skill") in ids and s["id"] not in ids)
    reg["yama_klasorleri"] = sorted(i for i in ids if (kok / "yamalar" / i).is_dir())
    reg["duzeltme_alanlari"] = sorted(s["id"] for s in hedef_skiller if s.get("aciklama_duzeltme") or s.get("yama"))
    if reg["alternatif_kardesler"]:
        dikkat.append("aynı adlı kardeş kayıtlar var; çıkarınca tercih hangisine geçer: python3 araclar/skill-ekle.py --listele --ara <ad>")
    if any(s.get("kaynak_durumu") for s in hedef_skiller):
        dikkat.append("skillerin kaynak_durumu dolu (kaynakta-kaldirildi / kayip)")

    # ---------------------------------------------------------------- 4. çıplak ad devri
    bu = []
    for k in kayitlar:
        for ad in _liste(k.get("ad_devral")):
            bu.append({"ad": ad, "devredilen_kimlikler": sorted(s["id"] for s in skiller if s["id"].startswith(ad + "@"))})
    rapor["ad_devri"]["bu_kaydin"] = bu
    for k in kayitlar_k:
        if k in kayitlar:
            continue
        for ad in _liste(k.get("ad_devral")):
            if ad in adlar:
                rapor["ad_devri"]["baska_kayitlarin"].append({"repo": k["repo"], "ad": ad})
    if bu or rapor["ad_devri"]["baska_kayitlarin"]:
        dikkat.append("çıplak ad devri var (rapor bölüm 4)")

    # ---------------------------------------------------------------- 5. GitHub
    if github and kaynak_tur == "kendi":
        dikkat.append("yerel kaynak (kendi/): GitHub'da yok, --github atlandı; çıkarmak kullanıcının kendi skillerini kütüphaneden düşürür, kendi/ klasörü ayrıca silinmez")
    elif github and kaynak_tur == "site":
        dikkat.append("yerel kaynak (site/): GitHub'da yok, --github atlandı; çıkarmak siteden alınan skilleri kütüphaneden düşürür, "
                      "site/ klasörü ve site-takip.json kaydı ayrıca silinmez (kayıt kalırsa dogrula uyarır)")
    elif github:
        gh = gh or _gh_calistir
        if listeler is None:
            def listeler():
                return _modul("github-skill-listesi").listeler()
        rapor["github"] = _github_oku(canon, gh, listeler)
        if rapor["github"]["yeni_ad"]:
            dikkat.append(f"AD DEĞİŞMİŞ: {rapor['github']['yeni_ad']} (çıkarma değil, rehber/09 'Repo adı değişirse')")
        if hedef_bilgi["kayip"] and rapor["github"]["erisim"].startswith("erişilebilir"):
            dikkat.append("KAYIP işaretli kaynak GitHub'da yeniden erişilebilir (rehber/03 E4)")

    # ---------------------------------------------------------------- 6. kartlar, konular, kayıt dosyaları
    desenler = [canon.lower()] + [e.lower() for e in eski_adlar] if hedef_turu == "repo" else [canon.lower()]
    if hedef_turu == "repo":
        for d in KAYIT_DOSYALARI:
            n = _satirlar(kok / d, desenler)
            if n:
                rapor["kayitlar"].append({"dosya": d, "satir": len(n)})
    else:
        for d, anahtar in (("ucret-siniflandirma.json", skill_hedef["id"]), ("yol-istisnalari.json", f"{canon}::{skill_hedef.get('kaynak_yol', '')}".lower()),
                           ("projeler.json", skill_hedef["id"])):
            n = _satirlar(kok / d, [anahtar.lower()])
            if n:
                rapor["kayitlar"].append({"dosya": d, "satir": len(n)})
    kart = False
    for dosya in sorted((kok / "notlar" / "referans").glob("*.md")) if (kok / "notlar" / "referans").is_dir() else []:
        n = _satirlar(dosya, desenler)
        if n:
            kart = True
            yol = f"notlar/referans/{dosya.name}"
            rapor["kayitlar"].append({"dosya": yol, "satir": len(n), "satirlar": n[:3]})
            dikkat.append(f"T5/T6 kartı: {yol} satır {n[0]}")
    rapor["kart_var"] = kart

    # ---------------------------------------------------------------- 7. karar
    rapor["karar"] = "engel" if engel else ("dikkat" if dikkat or rapor["proje_bilgisi"] == "yok" else "hazir")

    # ---------------------------------------------------------------- defter taslağı
    neden_m = neden or PLACEHOLDER_NEDEN
    onay = {"kim": "kullanıcı", "tarih": bugun, "oturum": "<kısa not>"}
    if hedef_turu == "repo":
        kayit = {"repo": canon, "skill_sayisi": len(hedef_skiller), "neden": neden_m, "tarih": bugun, "onay": onay,
                 "son_commit": son_commit, "geri_alma": f"git revert <commit>; GitHub: python3 araclar/listeye-ekle.py {canon}"}
        rapor["defter_taslagi"] = {"defter": "arsivden_cikarilan_repolar", "kayit": kayit}
    else:
        kayit = {"repo": canon, "kaynak_yol": skill_hedef.get("kaynak_yol", ""), "ad": skill_hedef.get("ad"), "neden": neden_m,
                 "tarih": bugun, "son_commit": skill_hedef.get("commit", ""), "onay": onay}
        rapor["defter_taslagi"] = {"defter": "arsivden_cikarilanlar", "kayit": kayit}

    # ---------------------------------------------------------------- 8. adımlar
    a = ["0. git status --short  -> boş olmalı. Değilse DUR, kullanıcıya söyle.",
         "1. Bu raporu kullanıcıya göster. Ölçüt ve içerik doğrulaması (rehber/03 D0) yapılmadıysa önce onu yap. "
         "Kullanıcının \"evet, çıkar\" cevabını bekle."]
    if rapor["roller"] or rapor["profiller"]:
        a.append("2. " + " | ".join(f"{x['dosya']}: \"{x['girdi']}\"" for x in rapor["roller"] + rapor["profiller"])
                 + " girdisini çıkar ya da yerine geçeni koy (yoksa dogrula HATA verir).")
    if rapor["projeler"]:
        cmds = []
        for p in rapor["projeler"]:
            names = " ".join(x["kurulu_ad"] for x in p["skiller"])
            cmds.append(f"{p['proje']}: python3 araclar/skill-ekle.py \"{_acik(p['yol'])}\" --kaldir {names} --kuru")
        a.append("3. Her proje için kullanıcıya sor, onaylarsa (önce --kuru, sonra --evet): " + " ; ".join(cmds)
                 + ". Çıkarılmazsa projedeki kopya çalışır ama kaynak kütüphanede yoktur (--durum: kaynak-yok).")
    snip = json.dumps(rapor["defter_taslagi"]["kayit"], ensure_ascii=False)
    if hedef_turu == "repo":
        a.append(f"4. kaynaklar.json: \"{canon}\" kaydını repolar'dan SİL (kaydı KAYIP yapıp bırakma: o ayrı bir karar, rehber/03 E) "
                 f"ve arsivden_cikarilan_repolar'a şu kaydı ekle: {snip}")
    else:
        a.append(f"4. kaynaklar.json: kaydı SİLME; arsivden_cikarilanlar'a şu kaydı ekle: {snip}")
    if kart:
        a.append("5. " + " ; ".join(f"{k['dosya']}: satır {k['satirlar'][0]} (kart/satır)" for k in rapor["kayitlar"] if k.get("satirlar"))
                 + " sil.")
    if hedef_turu == "repo":
        fihrist_dosya = kok / "fihrist" / (canon.replace("/", "__") + ".json")
        try:
            kit_var = any(str(x.get("repo", "")).lower() == canon.lower() for x in ((json_oku(kok / "kitler.json", {}) or {}).get("kitler") or []))
        except (AttributeError, TypeError):
            kit_var = False
        if fihrist_dosya.is_file():
            a.append(f"5b. fihrist/{fihrist_dosya.name} dosyasını sil (bolum fihrist kaynağın skil listesi; arşivde dosya yok, dogrula kaynağı olmayan fihristi UYARI sayar).")
        if kit_var:
            a.append(f"5c. kitler.json -> kitler listesinden \"{canon}\" kaydını sil (dogrula kaynağı olmayan kit kaydını UYARI sayar).")
    if hedef_turu == "skill":
        a.append(f"6. python3 araclar/kaynak-cek.py --repo {canon}   Sonra: python3 araclar/arsiv-yerlestir.py   "
                 "(--kayba-izin-ver KULLANMA: defter kaydı güvenlik kilidini zaten geçirir)")
    else:
        a.append("6. .gecici/cekilen/manifest.json yoksa: python3 araclar/kaynak-cek.py   Sonra: python3 araclar/arsiv-yerlestir.py   "
                 "(--kayba-izin-ver KULLANMA: defter kaydı güvenlik kilidini zaten geçirir)")
    a += ["7. python3 araclar/kapsam-denetimi.py   (0 sorun)",
          "8. python3 araclar/katalog-uret.py",
          "9. python3 araclar/dogrula.py   (0 hata; uyarı sayısı 0. adımdaki başlangıçtan fazla olmasın)",
          "10. python3 araclar/test.py",
          f"11. git status --short göster; tek commit: git add -A && git add -f arsiv && git commit -m \"Kaynak çıkarıldı: {canon}\"",
          f"12. GitHub (git dışı, kullanıcının kararı): yıldız/liste kalsın mı? Kaldırılacaksa kullanıcı onayıyla: gh api -X DELETE user/starred/{canon}"]
    rapor["adimlar"] = a
    rapor["geri_alma"] = list(GERI_ALMA)
    return rapor


def metin_uret(r):
    h = r["hedef"]
    if r["karar"] == "yok":
        return r.get("mesaj", "Zaten çıkarılmış.") + "\nKARAR: YOK (zaten çıkarılmış)"
    o = ["KAYNAK ÇIKARMA ETKİ RAPORU (yalnız okuma; hiçbir şey değişmedi)"]
    if h["tur"] == "skill":
        o.append(f"Hedef: skill {h['id']} ({h.get('durum')}) · kaynak {h['repo']} · tür {h.get('kaynak_tur')}/{h.get('bolum')} · kaynak_yol '{h.get('kaynak_yol')}'")
    else:
        sy = r["registry"].get("sayim") or {}
        o.append(f"Hedef: kaynak {h['repo']} · tür {h.get('kaynak_tur')}/{h.get('bolum')} · registry'de {h['skill_sayisi']} skill "
                 f"({sy.get('tercih', 0)} tercih, {sy.get('alternatif', 0)} alternatif)" + (" · KAYIP kaynak" if h["kayip"] else ""))
    for n in r.get("notlar", []):
        o.append(f"Not: {n}")
    if r.get("mesaj"):
        o += [r["mesaj"], "KARAR: REDDEDİLDİ (program)"]
        return "\n".join(o)
    o.append("1. PROJELER" + (f"  ({len(r['projeler'])} projede kullanılıyor)" if r["proje_bilgisi"] == "var" else ""))
    if r["proje_bilgisi"] == "yok":
        o.append("   Bu bilgisayarda proje bulunamadı: etki BİLİNMİYOR (başka bilgisayar/bulut olabilir).")
    elif not r["projeler"]:
        o.append("   Hiçbir projede kullanılmıyor.")
    for p in r["projeler"]:
        for x in p["skiller"]:
            o.append(f"   {p['proje']}: {x['kurulu_ad']} (kimlik {x['id']}; roller: {', '.join(x['roller']) or '—'})")
        o.append(f"   sonra: python3 araclar/skill-ekle.py \"{_acik(p['yol'])}\" --kaldir {' '.join(x['kurulu_ad'] for x in p['skiller'])} --kuru")
    o.append("2. ROLLER VE PROFİLLER")
    for x in r["roller"] + r["profiller"]:
        o.append(f"   ENGEL {x['dosya']}: {x['alan']}: {x['girdi']}")
    if not (r["roller"] or r["profiller"]):
        o.append("   Hiçbir rol/profil bu kaynağa bağlı değil.")
    if r.get("etkilenen_profiller"):
        o.append("   (bilgi) etkilenen rolleri içeren profiller: " + ", ".join(r["etkilenen_profiller"]))
    g = r["registry"]
    o.append(f"3. REGISTRY  {len(g['idler'])} kimlik: " + ", ".join(g.get("ilk_30", [])[:30]))
    if g["kopya_kaynaklar"]:
        o.append("   kopya kaynaklar: " + ", ".join(g["kopya_kaynaklar"]))
    if g["alternatif_kardesler"]:
        o.append("   aynı adlı kardeşler: " + ", ".join(g["alternatif_kardesler"]) +
                 "  (çıkarınca tercih hangisine geçer: python3 araclar/skill-ekle.py --listele --ara <ad>)")
    for og in g["ortusme"]:
        o.append(f"   örtüşme grubu {og['grup']}: {len(og['uyeler'])} üye")
    if g.get("cocuklar"):
        o.append("   alt skiller (ust_skill): " + ", ".join(g["cocuklar"]))
    if g.get("yama_klasorleri"):
        o.append("   yamalar/ klasörü var: " + ", ".join(g["yama_klasorleri"]))
    if g.get("duzeltme_alanlari"):
        o.append("   kayıtla giden düzeltme/yama alanları: " + ", ".join(g["duzeltme_alanlari"]))
    ad = r["ad_devri"]
    o.append("4. ÇIPLAK AD DEVRİ" + ("" if ad["bu_kaydin"] or ad["baska_kayitlarin"] else "  yok"))
    for x in ad["bu_kaydin"]:
        o.append(f"   bu kayıt '{x['ad']}' adını devralmış; çıkarınca çıplak ad boşalır; kimlikler değişmez: {', '.join(x['devredilen_kimlikler']) or '—'}")
    for x in ad["baska_kayitlarin"]:
        o.append(f"   başka kaynak ({x['repo']}) bu adı devralmış: {x['ad']}")
    o.append("5. YILDIZ VE LİSTE")
    if r["github"] is None:
        o.append("   GitHub yıldızı ve liste üyeliği git dışındadır; kullanıcının kararıdır. Kaldırmak: gh api -X DELETE user/starred/"
                 f"{h['repo']} (listeden de çıkar). Geri: python3 araclar/listeye-ekle.py {h['repo']}")
    else:
        gh = r["github"]
        o.append(f"   erişim: {gh['erisim']}" + (f" · AD DEĞİŞMİŞ: {gh['yeni_ad']}" if gh["yeni_ad"] else ""))
        o.append(f"   yıldız: {gh['yildiz']} · listeler: {', '.join(gh['listeler']) if isinstance(gh['listeler'], list) else gh['listeler']}")
    o.append("6. KARTLAR, KONULAR, KAYIT DOSYALARI")
    for k in r["kayitlar"]:
        o.append(f"   {k['dosya']}: {k['satir']} satır" + (f" (satır {', '.join(map(str, k['satirlar']))})" if k.get("satirlar") else ""))
    if not r["kayitlar"]:
        o.append("   (anılan yer yok)")
    if r["karar"] == "engel":
        o.append(f"KARAR: ENGEL ({len(r['engeller'])}) · DİKKAT ({len(r['dikkatler'])})")
    elif r["karar"] == "dikkat":
        o.append(f"KARAR: DİKKAT ({len(r['dikkatler'])})" if r["dikkatler"] else "KARAR: DİKKAT (proje bilgisi yok)")
    else:
        o.append("KARAR: HAZIR (engel ve dikkat yok)")
    for d in r["dikkatler"]:
        o.append(f"   dikkat: {d}")
    o.append("ADIMLAR (sırayla; kullanıcı onayı olmadan 2. adımdan öteye geçme):")
    o += [f"  {x}" for x in r["adimlar"]]
    o += ["GERİ ALMA"] + [f" - {x}" for x in r["geri_alma"]]
    return "\n".join(o)


# ------------------------------------------------------------------ yeniden kullanılabilir skil/bileşen çıkarma yardımcıları
def _yasak_arsiv_kokleri(kok):
    """Asla silinemeyecek ortak arşiv kökleri: arsiv/, arsiv/_varyantlar, arsiv/_bilesenler."""
    arsiv = (Path(kok) / "arsiv").resolve()
    return {
        arsiv,
        (arsiv / "_varyantlar").resolve(),
        (arsiv / "_bilesenler").resolve(),
    }


def _arsiv_ici_yol(kok, goreli):
    """goreli yol (kok / 'arsiv') altındaysa ve ortak köklerden (arsiv/, _varyantlar, _bilesenler)
    biri değilse çözülmüş Path döner; dışındaysa ya da ortak kökse None (güvenlik)."""
    if not goreli or not isinstance(goreli, str):
        return None
    arsiv = (Path(kok) / "arsiv").resolve()
    hedef = (Path(kok) / goreli).resolve()
    if hedef in _yasak_arsiv_kokleri(kok) or arsiv not in hedef.parents:
        return None
    return hedef


def _klasor_bayt(yol):
    if not yol.exists():
        return 0
    if yol.is_file():
        return yol.stat().st_size
    return sum(p.stat().st_size for p in yol.rglob("*") if p.is_file())


def registryden_cikar(registry, cikarilacak_idler, bilesen_repolar=(), oncelikler=None, fihrist_tutulan=None):
    """Saf işlev (verilen sözlüğü değiştirmez): seçilen skill kimliklerini ve verilen repoların bileşenlerini
    registry'den çıkarır. Çıkarılan skill 'tercih' idiyse aynı adlı kalan skillerden en uygunu 'tercih' olur
    (kimlikler rehber/09 gereği değişmez). fihrist_tutulan: {repo: set(kaynak_yol)} verilirse denetim kaydını günceller.
    Döner: (yeni_registry, {cikarilan_skiller, cikarilan_bilesenler, tercih_degisenler})."""
    cikar_set = set(cikarilacak_idler)
    bil_repolar = {r.lower() for r in bilesen_repolar}
    oncelik_map = {k.lower(): v for k, v in (oncelikler or {}).items()}
    cikarilan_skiller, kalan_skiller = [], []
    for s in registry.get("skiller", []):
        if s.get("id") in cikar_set:
            cikarilan_skiller.append(copy.deepcopy(s))
        else:
            kalan_skiller.append(copy.deepcopy(s))
    cikarilan_bilesenler, kalan_bilesenler = [], []
    for b in registry.get("bilesenler", []):
        if str(b.get("repo", "")).lower() in bil_repolar:
            cikarilan_bilesenler.append(copy.deepcopy(b))
        else:
            kalan_bilesenler.append(copy.deepcopy(b))
    tercih_degisenler = []
    etkilenen_adlar = sorted({s["ad"] for s in cikarilan_skiller
                              if s.get("ad") and (s.get("durum") == "tercih" or s.get("id") == s.get("ad"))})
    for ad in etkilenen_adlar:
        kardesler = [k for k in kalan_skiller if k.get("ad") == ad]
        if not kardesler:
            continue
        eski = next((s for s in cikarilan_skiller if s.get("ad") == ad and (s.get("id") == ad or s.get("durum") == "tercih")), None)
        kazanan = next((k for k in kardesler if k.get("durum") == "tercih"), None)
        if kazanan is None:
            kazanan = min(
                kardesler,
                key=lambda k: (
                    bool(k.get("gizli")),
                    0 if (k.get("durum_elle") and k.get("durum") == "tercih")
                    else 2 if (k.get("durum_elle") and k.get("durum") == "alternatif") else 1,
                    oncelik_map.get(str(k.get("repo", "")).lower(), 5),
                    str(k.get("repo", "")),
                    str(k.get("kaynak_yol", "")),
                ),
            )
            kazanan["durum"] = "tercih"
        if eski is not None:
            tercih_degisenler.append({
                "ad": ad,
                "eski_id": eski["id"],
                "eski_repo": eski.get("repo", ""),
                "yeni_id": kazanan["id"],
                "yeni_repo": kazanan.get("repo", ""),
                "ciplak_ad_bosaldi": eski["id"] == ad,
            })
    yeni_reg = copy.deepcopy(registry)
    yeni_reg["skiller"] = kalan_skiller
    if "bilesenler" in yeni_reg or kalan_bilesenler:
        yeni_reg["bilesenler"] = kalan_bilesenler
    if fihrist_tutulan and isinstance(yeni_reg.get("denetim"), dict):
        denetim = yeni_reg["denetim"]
        for repo, tutulan in fihrist_tutulan.items():
            rk = next((k for k in denetim if k.lower() == repo.lower()), None)
            if rk is None:
                continue
            if not tutulan:
                denetim.pop(rk, None)
            elif isinstance(denetim[rk], dict) and isinstance(denetim[rk].get("skill_md"), dict):
                tutulan_set = set(tutulan)
                for p in list(denetim[rk]["skill_md"]):
                    klasor = p.rsplit("/", 1)[0] if "/" in p else ""
                    if klasor not in tutulan_set:
                        denetim[rk]["skill_md"][p] = "fihristte"
    return yeni_reg, {
        "cikarilan_skiller": cikarilan_skiller,
        "cikarilan_bilesenler": cikarilan_bilesenler,
        "tercih_degisenler": tercih_degisenler,
    }


def acilan_bayt_hesapla(kok, cikarilan_skiller, cikarilan_bilesenler):
    """Salt okuma: arşivden çıkarılacak skill klasörleri, araç sürümleri ve bileşen dosyalarının toplam baytı."""
    kok = Path(kok)
    gorulen, toplam = set(), 0
    for s in cikarilan_skiller:
        for yol in [s.get("yol")] + list((s.get("varyantlar") or {}).values()):
            p = _arsiv_ici_yol(kok, yol)
            if p and p not in gorulen and p.exists():
                gorulen.add(p)
                toplam += _klasor_bayt(p)
    for b in cikarilan_bilesenler:
        p = _arsiv_ici_yol(kok, b.get("yol"))
        if p and p not in gorulen and p.exists():
            gorulen.add(p)
            toplam += _klasor_bayt(p)
    return toplam


def _korunan_yollar(kok, kalan_skiller=(), kalan_bilesenler=()):
    """Kalan tüm skillerin (yol + varyantlar) ve kalan bileşenlerin çözülmüş arşiv yolları kümesi."""
    korunan = set()
    for s in (kalan_skiller or ()):
        if not isinstance(s, dict):
            continue
        for yol in [s.get("yol")] + list((s.get("varyantlar") or {}).values()):
            p = _arsiv_ici_yol(kok, yol)
            if p is not None:
                korunan.add(p)
    for b in (kalan_bilesenler or ()):
        if not isinstance(b, dict):
            continue
        p = _arsiv_ici_yol(kok, b.get("yol"))
        if p is not None:
            korunan.add(p)
    return korunan


def _yol_cakisma_nedeni(kok, ham_yol, korunan):
    """Silme hedefi yasak ortak kökse, arsiv/ dışındaysa ya da korunan bir yolla çakışıyorsa neden metni döner; güvenliyse None."""
    p = _arsiv_ici_yol(kok, ham_yol)
    if p is None:
        return f"yasak ortak kök ya da arsiv/ dışı yol silinemez: {ham_yol!r}"
    for k in korunan:
        if p == k:
            return f"kalan bir skil/bileşenle paylaşılan yol silinemez: {ham_yol!r}"
        if p in k.parents:
            return f"kalan bir skil/bileşenin üst klasörü silinemez: {ham_yol!r}"
        if k in p.parents:
            return f"kalan bir klasörün içindeki yol silinemez: {ham_yol!r}"
    return None


def arsiv_silme_hatalari(kok, cikarilan_skiller, cikarilan_bilesenler, kalan_skiller=(), kalan_bilesenler=()):
    """Salt okuma: arsivden_cikar öncesi tüm silme hedeflerini ortak kökler ve kalan skiller/bileşenlere karşı doğrular."""
    kok = Path(kok)
    korunan = _korunan_yollar(kok, kalan_skiller, kalan_bilesenler)
    hatalar = []
    for s in (cikarilan_skiller or ()):
        yol = s.get("yol")
        if yol is not None and yol != "":
            n = _yol_cakisma_nedeni(kok, yol, korunan)
            if n:
                hatalar.append(f"skil {s.get('id', '?')}: {n}")
        for arac, vy in (s.get("varyantlar") or {}).items():
            if vy is not None and vy != "":
                n = _yol_cakisma_nedeni(kok, vy, korunan)
                if n:
                    hatalar.append(f"skil {s.get('id', '?')} varyant({arac}): {n}")
    for b in (cikarilan_bilesenler or ()):
        by = b.get("yol")
        if by is not None and by != "":
            n = _yol_cakisma_nedeni(kok, by, korunan)
            if n:
                hatalar.append(f"bileşen {b.get('ad', '?')}: {n}")
    return hatalar


def _bos_ustleri_sil(baslangic, sinir, korunan=()):
    """baslangic'tan yukarı doğru boş klasörleri siler; sinir (dahil değil) ya da korunan klasörde durur."""
    cur = baslangic.resolve()
    sinir = sinir.resolve()
    korunan_set = set(korunan or ())
    while cur != sinir and sinir in cur.parents and cur not in korunan_set:
        try:
            if cur.is_dir() and not any(cur.iterdir()):
                cur.rmdir()
                cur = cur.parent
            else:
                break
        except OSError:
            break


def arsivden_cikar(kok, cikarilan_skiller, cikarilan_bilesenler, kalan_skiller=(), kalan_bilesenler=()):
    """Seçilen skillerin klasörlerini, araç sürümlerini ve bileşen dosyalarını arsiv/ içinden siler.
    Yalnız (kok / 'arsiv') altındaki güvenli hedeflere dokunur: arsiv/, arsiv/_varyantlar, arsiv/_bilesenler
    ortak kökleri ve kalan skiller/varyantlar/bileşenlerle paylaşılan ya da onları kapsayan yollar hiçbir şey
    silinmeden ValueError ile reddedilir. shutil.rmtree öncesi is_dir() ve symlink kontrolü yapılır."""
    kok = Path(kok)
    arsiv = (kok / "arsiv").resolve()
    hatalar = arsiv_silme_hatalari(kok, cikarilan_skiller, cikarilan_bilesenler, kalan_skiller, kalan_bilesenler)
    if hatalar:
        raise ValueError("Arşiv silme güvenlik engeli: " + "; ".join(hatalar))

    korunan = _korunan_yollar(kok, kalan_skiller, kalan_bilesenler)
    n_skil = n_var = n_bil = bayt = 0
    silinen_yollar = set()
    atlanan = []
    for s in (cikarilan_skiller or ()):
        yol = s.get("yol")
        p = _arsiv_ici_yol(kok, yol)
        ham = (kok / yol) if isinstance(yol, str) and yol else None
        if p and p not in silinen_yollar:
            if ham is not None and ham.is_symlink():
                atlanan.append(str(yol))
            elif p.is_dir():
                bayt += _klasor_bayt(p)
                shutil.rmtree(p)
                silinen_yollar.add(p)
                n_skil += 1
            elif p.exists():
                atlanan.append(str(yol))
        for vy in (s.get("varyantlar") or {}).values():
            vp = _arsiv_ici_yol(kok, vy)
            vham = (kok / vy) if isinstance(vy, str) and vy else None
            if vp and vp not in silinen_yollar:
                if vham is not None and vham.is_symlink():
                    atlanan.append(str(vy))
                elif vp.is_dir():
                    bayt += _klasor_bayt(vp)
                    shutil.rmtree(vp)
                    silinen_yollar.add(vp)
                    n_var += 1
                    _bos_ustleri_sil(vp.parent, arsiv / "_varyantlar", korunan)
                elif vp.exists():
                    atlanan.append(str(vy))
    for b in (cikarilan_bilesenler or ()):
        by = b.get("yol")
        bp = _arsiv_ici_yol(kok, by)
        bham = (kok / by) if isinstance(by, str) and by else None
        if bp and bp not in silinen_yollar:
            if bham is not None and bham.is_symlink():
                atlanan.append(str(by))
            elif bp.is_file():
                bayt += bp.stat().st_size
                bp.unlink()
                silinen_yollar.add(bp)
                n_bil += 1
                _bos_ustleri_sil(bp.parent, arsiv / "_bilesenler", korunan)
            elif bp.exists():
                atlanan.append(str(by))
    return {"silinen_skil_klasoru": n_skil, "silinen_varyant_klasoru": n_var,
            "silinen_bilesen_dosyasi": n_bil, "acilan_bayt": bayt, "atlanan": atlanan}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--repo", help="kaynak repo (güncel ya da eski ad, büyük/küçük harf fark etmez)")
    g.add_argument("--skill", help="skill kimliği ya da çıplak ad")
    ap.add_argument("--kuru", action="store_true", help="ZORUNLU: yalnız etki raporu; hiçbir şey değiştirmez")
    ap.add_argument("--neden", help="defter taslağına yazılacak gerekçe")
    ap.add_argument("--json", action="store_true", help="tek JSON nesnesi yaz")
    ap.add_argument("--github", action="store_true", help="repo/yıldız/liste durumunu GitHub'dan OKU (yazmaz)")
    ap.add_argument("--siki", action="store_true", help="karar engel/reddedildi ise çıkış 1")
    a = ap.parse_args(argv)
    if not a.kuru:
        print("Bu sürümde yalnız --kuru var (etki raporu; hiçbir şey değiştirmez).")
        return 2
    if not (a.repo or a.skill):
        print("--repo ya da --skill ver.")
        return 2
    from ortak import KOK
    try:
        r = rapor_uret(KOK, "repo" if a.repo else "skill", a.repo or a.skill, neden=a.neden, github=a.github)
    except HedefHata as e:
        print(str(e), file=sys.stderr)
        return 2
    print(json.dumps(r, ensure_ascii=False) if a.json else metin_uret(r))
    return 1 if (a.siki and r["karar"] in ("engel", "reddedildi")) else 0


if __name__ == "__main__":
    sys.exit(main())
