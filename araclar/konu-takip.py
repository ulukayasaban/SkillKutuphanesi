#!/usr/bin/env python3
"""Konu takibi: belirli alanlardaki (ör. e-ticaret/Etsy, mobil) YENİ skill repolarını GitHub'da düzenli arar.
Sadece okur ve raporlar; kaynak EKLEMEZ, yıldız/liste değiştirmez.

  python3 araclar/konu-takip.py                # tüm konuları tara -> konu-takip.json + notlar/konu-takip.md
  python3 araclar/konu-takip.py --konu e-ticaret
  python3 araclar/konu-takip.py --rapor        # taramadan rapor
  python3 araclar/konu-takip.py --karar owner/ad reddedildi "neden"   # adayı değerlendirildi olarak işaretle
                                                                     # (eklendi | reddedildi | izle)
  python3 araclar/konu-takip.py --bekleyenler [--ozet-json] [--siki]   # kararı bekleyen adayları (konu takibi, trend, popüler) ve
                                       # vadesi gelen izlenenleri özetler: tarama yapmaz, ağ kullanmaz, dosya yazmaz
  python3 araclar/konu-takip.py --kuyruk [--json]                    # Faz 2: konu-takip.json kuyruğunu özetler (ağsız, yazmaz)
  python3 araclar/konu-takip.py --kuyruga-ekle owner/ad neden "not"  # Faz 2: repoyu kuyruğa ekler (K-58 ise reddedildi)

Konular ve arama sorguları: kaynaklar.json -> "takip_konulari". Her sorgu GitHub kod aramasında
"<sorgu> filename:SKILL.md" olarak aranır. Kütüphanede olan ve 'degerlendirilen' listesindeki repolar aday sayılmaz.
Karar anlamları: eklendi = kütüphaneye eklendi; reddedildi = kalıcı, bir daha aday olmaz (yeniden açmak kullanıcı kararı);
izle = "şimdilik değil, durum değişirse bak": yalnız 'izlenen' bölümüne yazılır, aday tablosunda görünmez, 90 gün sonra "zamanı geldi".
Kararı HER ZAMAN buradan yaz (populer-tarama.py --karar kullanma). Eleme büyük/küçük harfe bakmaz.
Aylık güncelleme (arsiv-guncelle.py --uygula) bunu otomatik çalıştırır. Aday eklemek: rehber/03-yeni-skill-ekleme.md.
"""
import json
import re
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import (KAYNAKLAR, KOK, KUYRUK_DURUMLARI, KUYRUK_NEDENLERI, TREND,  # noqa: E402
                   json_oku, json_yaz, trend_durumu)

BILGI_YASI_GUN = 90   # aday repo bilgisi bu kadar günde bir tazelenir
BILGI_SINIRI = 400    # bir turda en çok bu kadar repo bilgisi çekilir
DURUM = KOK / "konu-takip.json"
RAPOR = KOK / "notlar" / "konu-takip.md"
POPULER = KOK / "notlar" / "populer-skiller.md"
IZLE_GUN = 90          # izlenen kaydın 'tekrar bak' süresi (tarih + 90 gün hesaplanır, alan tutulmaz)
BAYAT_GUN = 45         # --bekleyenler: tarama bayatlığı
REPO_DESEN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def kod_ara(sorgu):
    for i in range(4):  # GitHub kod araması sık sık 504/ikincil hız sınırı verir
        r = subprocess.run(["gh", "search", "code", f"{sorgu} filename:SKILL.md", "--limit", "100",
                            "--json", "repository,path"], capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout or "[]")
        time.sleep(8 * (i + 1))
    print(f"  ! arama yapılamadı: {sorgu}")
    return None


def repo_bilgisi(repo):
    r = subprocess.run(["gh", "api", f"repos/{repo}", "--jq",
                        "{yildiz:.stargazers_count,lisans:(.license.spdx_id//\"yok\"),son:.pushed_at[:10],"
                        "aciklama:((.description//\"\")[:140]),arsiv:.archived}"], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None


def tara(durum, ayar, secili):
    bugun = date.today().isoformat()
    for k in ayar["takip_konulari"]:
        if secili and k["konu"] != secili:
            continue
        print(f"# {k['konu']}: {len(k['sorgular'])} sorgu")
        hedef = durum.setdefault("konular", {}).setdefault(k["konu"], {"repolar": {}})
        basarisiz = 0
        for q in k["sorgular"]:
            sonuc = kod_ara(q)
            if sonuc is None:
                basarisiz += 1
                continue
            for x in sonuc:
                repo = x["repository"]["nameWithOwner"]
                r = hedef["repolar"].setdefault(repo, {"ilk": bugun, "sorgular": [], "skill_yollari": []})
                r["son"] = bugun
                if q not in r["sorgular"]:
                    r["sorgular"].append(q)
                if x["path"] not in r["skill_yollari"] and len(r["skill_yollari"]) < 50:
                    r["skill_yollari"].append(x["path"])
            time.sleep(2)
        hedef["son_tarama"] = bugun
        hedef["basarisiz_sorgu"] = basarisiz
        # Sadece aday olabileceklerin bilgisini çek (kütüphanede/değerlendirilmiş olanlar hariç)
        bilinen = bilinenler(durum, ayar)
        # API bütçesi: aday bilgisi en çok 90 günde bir tazelenir ve bir turda en çok BILGI_SINIRI çağrı yapılır
        # (aday havuzu sürekli büyür; sınırsız çağrı aylık güncellemeyi hız sınırına çarptırırdı)
        cagri = 0
        for repo, r in hedef["repolar"].items():
            if repo.lower() in bilinen:
                continue
            taze = r.get("bilgi_tarihi") and r.get("yildiz") is not None and \
                (date.fromisoformat(bugun) - date.fromisoformat(r["bilgi_tarihi"])).days < BILGI_YASI_GUN
            if taze:
                continue
            if cagri >= BILGI_SINIRI:
                break
            cagri += 1
            bilgi = repo_bilgisi(repo)
            if bilgi:
                r.update(bilgi)
                r["bilgi_tarihi"] = bugun


def _repo_adi(x):
    return (x.get("repo") if isinstance(x, dict) else x) or ""


def elenecekler(ayar, durum):
    """-> {'kaynak','cikarilan','karar','izlenen'}: hepsi KÜÇÜK HARFLİ küme.
    kaynak = repolar[*].repo + eski_adlar (T1..T6 ve KAYIP dahil); cikarilan = arsivden_cikarilan_repolar (str ya da {'repo':..});
    karar = durum['degerlendirilen'] anahtarları; izlenen = durum['izlenen'] anahtarları."""
    kaynak = set()
    for k in ayar.get("repolar", []):
        kaynak.add(k["repo"].lower())
        kaynak.update(e.lower() for e in k.get("eski_adlar", []))
    return {"kaynak": kaynak,
            "cikarilan": {_repo_adi(x).lower() for x in ayar.get("arsivden_cikarilan_repolar", []) if _repo_adi(x)},
            "karar": {r.lower() for r in durum.get("degerlendirilen", {})},
            "izlenen": {r.lower() for r in durum.get("izlenen", {})}}


def eleniyor(repo, e, izlenen_dahil=True):
    r = repo.lower()
    return r in e["kaynak"] or r in e["cikarilan"] or r in e["karar"] or (izlenen_dahil and r in e["izlenen"])


def bilinenler(durum, ayar):
    """tara(): bilgisi çekilmeyecek repolar (küçük harf). İzlenenler dahil DEĞİL: bilgileri tazelenmeye devam eder."""
    e = elenecekler(ayar, durum)
    return e["kaynak"] | e["cikarilan"] | e["karar"]


def aday_mi(repo, v, k, e, odakli=True):
    """TEK aday ölçütü (rapor tablosu, özet sayısı ve main çıktısı bunu kullanır): elenmemiş (izlenen dahil), arşivlenmemiş,
    yıldız eşiğini geçmiş; odakli=True ise repo adı/açıklaması konunun 'odak' ifadesine uyan."""
    if eleniyor(repo, e) or v.get("arsiv") or v.get("yildiz", 0) < k.get("min_yildiz", 10):
        return False
    return (not odakli) or bool(re.search(k.get("odak", "."), repo + " " + v.get("aciklama", ""), re.I))


def _gun(x):
    return x if isinstance(x, date) else date.fromisoformat(str(x))


def izlenen_vadesi(kayit, bugun=None):
    """-> (tekrar_bak_tarihi ISO, vade_geldi). Tarih yoksa ya da bozuksa: ('—', False)."""
    try:
        t = _gun(kayit["tarih"]) + timedelta(days=IZLE_GUN)
    except (KeyError, ValueError, TypeError):
        return "—", False
    return t.isoformat(), _gun(bugun or date.today()) >= t


def karar_uygula(durum, ayar, trend, repo, karar, neden, bugun=None):
    """Saf işlev: -> (mesajlar, hata). durum yalnız hata None iken değişir. Dosya yazmaz."""
    bugun = _gun(bugun or date.today()).isoformat()
    if not REPO_DESEN.match(repo or ""):
        return [], f"geçersiz repo adı: {repo} (owner/ad biçimi)"
    if karar not in ("eklendi", "reddedildi", "izle"):
        return [], "karar: eklendi | reddedildi | izle"
    neden = neden or "-"
    deg, izl = durum.get("degerlendirilen", {}), durum.get("izlenen", {})
    key = next((r for r in list(deg) + list(izl) if r.lower() == repo.lower()), None)
    bilinen_yer = key is not None
    if key is None:
        for h in durum.get("konular", {}).values():
            key = next((r for r in h.get("repolar", {}) if r.lower() == repo.lower()), None)
            if key:
                break
    if key is None:
        key = next((r for r in (trend or {}).get("son_liste", {}) if r.lower() == repo.lower()), None)
    bilinen_yer = bilinen_yer or key is not None
    key = key or repo
    mesaj = []
    if not bilinen_yer:
        mesaj.append("UYARI: bu repo hiçbir tarama kaydında yok (yazım hatası olabilir); yine de kaydedildi.")
    e = elenecekler(ayar, durum)
    if repo.lower() in e["kaynak"] and karar in ("reddedildi", "izle"):
        return [], f"kütüphanede olan repoya {karar} verilemez (çıkarmak için kaynak-cikar.py)"
    onceki = deg.get(key)
    if onceki:
        if onceki.get("karar") == "reddedildi" and karar == "izle":
            return [], (f"daha önce REDDEDİLDİ ({onceki.get('tarih', '?')}: {onceki.get('neden', '-')}); yeniden değerlendirmek "
                        "kullanıcı kararıdır (konu-takip.json'dan o kaydı sil)")
        if onceki.get("karar") == "eklendi" and karar in ("reddedildi", "izle"):
            return [], (f"daha önce EKLENDİ ({onceki.get('tarih', '?')}: {onceki.get('neden', '-')}); yeniden değerlendirmek "
                        "kullanıcı kararıdır (konu-takip.json'dan o kaydı sil)")
        if onceki.get("karar") == "reddedildi" and karar == "eklendi":
            mesaj.append("önceki karar reddedildi idi: güncellendi")
    if karar == "izle":
        durum.setdefault("izlenen", {})[key] = {"neden": neden, "tarih": bugun}
    else:
        durum.setdefault("degerlendirilen", {})[key] = {"karar": karar, "neden": neden, "tarih": bugun}
        durum.get("izlenen", {}).pop(key, None)
    mesaj.append(f"{key}: {karar} yazıldı")
    return mesaj, None


def kuyruga_ekle(durum, repo, neden, ayrinti="", bugun=None):
    """Saf işlev: repo'yu konu-takip.json kuyruğuna ekler -> (kayit, hata).
    neden == 'K-58' ise reddedildi + degerlendirilen kaydı açar; diğer nedenlerde 'bekliyor'."""
    if not REPO_DESEN.match(repo or ""):
        return None, f"geçersiz repo adı: {repo} (owner/ad biçimi)"
    if neden not in KUYRUK_NEDENLERI:
        return None, f"geçersiz kuyruk nedeni: {neden!r} ({', '.join(KUYRUK_NEDENLERI)})"
    bugun = _gun(bugun or date.today()).isoformat()
    kuyruk = durum.setdefault("kuyruk", {})
    key = next((r for r in kuyruk if r.lower() == repo.lower()), repo)
    if neden == "K-58":
        kayit = {"repo": key, "durum": "reddedildi", "neden": "K-58", "tarih": bugun, "ayrinti": ayrinti or "K-58 otomatik ret"}
        kuyruk[key] = kayit
        durum.setdefault("degerlendirilen", {})[key] = {"karar": "reddedildi", "neden": "K-58", "tarih": bugun}
        return kayit, None
    kayit = {"repo": key, "durum": "bekliyor", "neden": neden, "tarih": bugun, "ayrinti": str(ayrinti or "")}
    kuyruk[key] = kayit
    return kayit, None


def kuyruk_karar_ver(durum, repo, yeni_durum, aciklama="", bugun=None):
    """Saf işlev: kuyruktaki kaydın durumunu 'karar_verildi' veya 'reddedildi' yapar."""
    if yeni_durum not in KUYRUK_DURUMLARI or yeni_durum == "bekliyor":
        return None, "karar durumu 'karar_verildi' veya 'reddedildi' olmalı"
    kuyruk = durum.get("kuyruk") or {}
    key = next((r for r in kuyruk if r.lower() == (repo or "").lower()), None)
    if not key:
        return None, f"kuyrukta bulunamadı: {repo}"
    bugun = _gun(bugun or date.today()).isoformat()
    kuyruk[key]["durum"] = yeni_durum
    kuyruk[key]["karar_tarihi"] = bugun
    if aciklama:
        kuyruk[key]["ayrinti"] = aciklama
    if yeni_durum == "reddedildi":
        durum.setdefault("degerlendirilen", {})[key] = {
            "karar": "reddedildi", "neden": aciklama or kuyruk[key].get("neden", "reddedildi"), "tarih": bugun
        }
    return kuyruk[key], None


def kuyruk_ozeti(durum) -> dict:
    """Saf işlev: 'bekliyor' durumundaki kuyruk kayıtlarını nedenine göre gruplar ve toplu özet metni üretir."""
    kuyruk = (durum or {}).get("kuyruk") or {}
    bekleyenler_l = [v for v in kuyruk.values() if isinstance(v, dict) and v.get("durum") == "bekliyor"]
    gruplar = {}
    for k in bekleyenler_l:
        gruplar.setdefault(k.get("neden", "tur_aday"), []).append(k)
    satirlar = []
    if not bekleyenler_l:
        mesaj = "Kuyrukta karar bekleyen repo yok."
    else:
        satirlar.append(f"Karar bekleyen {len(bekleyenler_l)} repo (tek toplu onay):")
        for neden in sorted(gruplar):
            repolar = gruplar[neden]
            satirlar.append(f"- {neden} ({len(repolar)}): " + ", ".join(x.get("repo", "?") for x in repolar))
        mesaj = "\n".join(satirlar)
    return {"toplam_bekleyen": len(bekleyenler_l), "gruplar": gruplar, "satirlar": satirlar, "mesaj": mesaj}


def _aralik(tarih, bugun):
    try:
        return (_gun(bugun) - _gun(tarih)).days
    except (ValueError, TypeError):
        return None


def populer_adaylari(metin):
    """notlar/populer-skiller.md -> (rapor tarihi ya da None, [(repo, yildiz)]) ; 'Yeni adaylar' bölümü yoksa liste None."""
    m = re.search(r"· (\d{4}-\d{2}-\d{2}) ·", metin)
    tarih = m.group(1) if m else None
    bas = metin.find("## Yeni adaylar")
    if bas < 0:
        return tarih, None
    son = metin.find("\n## ", bas + 5)
    bolum = metin[bas:son if son > 0 else len(metin)]
    sonuc = []
    for sat in bolum.splitlines():
        r = re.match(r"\| \[([^\]]+)\]\(https://github\.com/", sat)
        if r:
            hucre = [h.strip() for h in sat.split("|")]
            try:
                y = int(hucre[2])
            except (IndexError, ValueError):
                y = 0
            sonuc.append((r.group(1), y))
    return tarih, sonuc


def bekleyenler(ayar, durum, trend, populer_metin, bugun=None):
    """Saf işlev: üç aday kaynağının karar bekleyenlerini özetler -> (durum, satirlar, karar_bekleyen). Dosya okumaz/yazmaz."""
    bugun = _gun(bugun or date.today())
    e = elenecekler(ayar, durum)
    dikkat, satirlar, bekleyen = False, [], []

    def bayat(tarih):
        g = _aralik(tarih, bugun) if tarih else None
        return g, (g is None or g > BAYAT_GUN)

    # 1) konu takibi
    adaylar = []
    for k in ayar.get("takip_konulari", []):
        h = durum.get("konular", {}).get(k["konu"], {})
        liste = sorted(((r, v) for r, v in h.get("repolar", {}).items() if aday_mi(r, v, k, e)),
                       key=lambda x: (-x[1].get("yildiz", 0), x[0]))
        g, eski = bayat(h.get("son_tarama"))
        yas = f"son tarama {h['son_tarama']} ({g} gün önce)" if g is not None else "hiç taranmamış"
        satirlar.append(f"{k['konu']}: {len(liste)} odaklı aday, {yas}")
        dikkat = dikkat or bool(liste) or eski
        adaylar += [(v.get("yildiz", 0), r, k["konu"]) for r, v in liste]
    bekleyen += [f"{r} (★{y}, {kn})" for y, r, kn in sorted(adaylar, key=lambda x: (-x[0], x[1]))[:5]]
    vadeli = sorted(r for r, v in durum.get("izlenen", {}).items() if izlenen_vadesi(v, bugun)[1])
    if durum.get("izlenen"):
        satirlar.append(f"izlenen: {len(durum['izlenen'])} kayıt, {len(vadeli)} tanesinin vadesi geldi")
    if vadeli:
        dikkat = True
        bekleyen += [f"{r} (izlenen, vadesi geldi)" for r in vadeli[:5]]
    # 2) trend
    if not trend or not (trend.get("son_liste") or trend.get("son_tarama")):
        satirlar.append("trend: rapor yok")
        dikkat = True
    else:
        sayi = trend.get("skill_sayisi", {})
        tr = [(r, (sayi.get(r) or {}).get("skill", 0)) for r in trend.get("son_liste", {}) if not eleniyor(r, e)]
        tr = sorted(((r, n) for r, n in tr if n and n > 0), key=lambda x: (-x[1], x[0]))
        g, eski = bayat(trend.get("son_tarama"))
        satirlar.append(f"trend: {len(tr)} aday" + (f", son tarama {trend.get('son_tarama')} ({g} gün önce)" if g is not None else ""))
        dikkat = dikkat or bool(tr) or eski
        bekleyen += [f"{r} (trend, {n} skill)" for r, n in tr[:5]]
    # 3) popüler
    if populer_metin is None:
        satirlar.append("popüler: rapor yok")
        dikkat = True
    else:
        tarih, liste = populer_adaylari(populer_metin)
        if liste is None:
            satirlar.append("popüler: populer-skiller.md okunamadı ('Yeni adaylar' bölümü yok)")
            dikkat = True
        else:
            pa = sorted(((r, y) for r, y in liste if not eleniyor(r, e)), key=lambda x: (-x[1], x[0]))
            g, eski = bayat(tarih)
            satirlar.append(f"popüler: {len(pa)} aday (rapor {tarih or '?'}" + (f", {g} gün)" if g is not None else ")"))
            dikkat = dikkat or bool(pa) or eski
            bekleyen += [f"{r} (★{y}, popüler)" for r, y in pa[:5]]
    return ("dikkat" if dikkat else "temiz"), satirlar, bekleyen


def ozet_yaz(arac, durum, satirlar, bekleyen, json_mod):
    if json_mod:
        print(json.dumps({"arac": arac, "durum": durum, "satirlar": satirlar, "karar_bekleyen": bekleyen}, ensure_ascii=False))
        return
    print(f"{arac}: {durum}")
    for x in satirlar:
        print(f"  {x}")
    if bekleyen:
        print("  Karar bekleyen (en çok 5 ad/kaynak):")
        for x in bekleyen:
            print(f"    - {x}")


def bekleyenler_calistir(json_mod, siki):
    """--bekleyenler: dosya yazmaz, ağ kullanmaz. 'sorun' yalnız kaynaklar.json ya da konu-takip.json okunamazsa."""
    def oku_metin(yol):
        try:
            return Path(yol).read_text(encoding="utf-8")
        except OSError:
            return None
    try:
        ayar = json_oku(KAYNAKLAR)
        durum = json_oku(DURUM, {})
        if not isinstance(ayar, dict) or not isinstance(durum, dict):
            raise ValueError("beklenmeyen biçim")
    except Exception as ex:  # noqa: BLE001
        ozet_yaz("konu-takip", "sorun", [f"kaynaklar.json ya da konu-takip.json okunamadı: {type(ex).__name__}"], [], json_mod)
        return 1 if siki else 0
    try:
        trend = json_oku(TREND, {})
    except Exception:  # noqa: BLE001
        trend = None
    d, satirlar, bekleyen = bekleyenler(ayar, durum, trend, oku_metin(POPULER))
    ozet_yaz("konu-takip", d, satirlar, bekleyen, json_mod)
    return 0


def rapor(durum, ayar):
    e = elenecekler(ayar, durum)
    deg = durum.get("degerlendirilen", {})
    trend = json_oku(TREND, {})
    satir = ["# Konu Takibi — yeni skill repoları", "",
             "> `araclar/konu-takip.py` üretir. Konular/sorgular: `kaynaklar.json` → `takip_konulari`. Adaylar otomatik EKLENMEZ; "
             "uygun olanlar `rehber/03-yeni-skill-ekleme.md` (çakışma + ücret kontrolü, kullanıcı onayı) ile eklenir. "
             "Reddedilen/eklenen repo bir daha aday olarak gösterilmez; izlenen repo ayrı bölümde durur: "
             "`konu-takip.py --karar owner/ad reddedildi|eklendi|izle \"neden\"`.", ""]
    for k in ayar["takip_konulari"]:
        h = durum.get("konular", {}).get(k["konu"], {})
        repolar = h.get("repolar", {})
        min_y = k.get("min_yildiz", 10)
        tum = [(r, v) for r, v in repolar.items() if aday_mi(r, v, k, e, odakli=False)]
        # Odaklı aday: repo adı/açıklaması konuya odaklı ("odak" regex). Dolaylı: konu kelimesi sadece birkaç SKILL.md'de geçiyor
        aday = sorted(((r, v) for r, v in tum if aday_mi(r, v, k, e)),
                      key=lambda x: (-len(x[1]["sorgular"]), -x[1].get("yildiz", 0)))
        dolayli = len(tum) - len(aday)
        dusuk = sum(1 for r, v in repolar.items() if not eleniyor(r, e) and v.get("yildiz", 0) < min_y)
        kutup = sorted(r for r in repolar if r.lower() in e["kaynak"])
        satir += [f"## {k['konu']} → `{k['kategori']}`", "",
                  f"Son tarama: {h.get('son_tarama', '—')} · eşleşen repo: {len(repolar)} · kütüphanede: {len(kutup)} · "
                  f"değerlendirilmiş: {sum(1 for r in repolar if r.lower() in e['karar'])} · **odaklı aday: {len(aday)}** · dolaylı eşleşme: {dolayli} "
                  f"(★{min_y} altı {dusuk} repo gösterilmez) · başarısız sorgu: {h.get('basarisiz_sorgu', 0)}", "",
                  "| Aday repo | ★ | Lisans | Son | Eşleşen SKILL.md | Sorgular | Trend | Açıklama |", "|---|---|---|---|---|---|---|---|"]
        for r, v in aday[:60]:
            t = trend_durumu(r, trend)
            satir.append(f"| {r} | {v.get('yildiz', '?')} | {v.get('lisans', '?')} | {v.get('son', '?')} | {len(v['skill_yollari'])} | "
                         f"{', '.join(v['sorgular'][:5])} | {t['seviye'] if t else '-'} | {v.get('aciklama', '').replace('|', '/')} |")
        satir.append("")
    bugun = date.today()
    satir += ["## İzlenenler (şimdilik değil; durum değişirse bak)", "", "| Repo | Tarih | Tekrar bak | Neden |", "|---|---|---|---|"]
    for r, v in sorted(durum.get("izlenen", {}).items()):
        t, vade = izlenen_vadesi(v, bugun)
        satir.append(f"| {r} | {v.get('tarih', '?')} | {t}{' ⏰ zamanı geldi' if vade else ''} | {str(v.get('neden', '-')).replace('|', '/')} |")
    if not durum.get("izlenen"):
        satir.append("| (yok) | | | |")
    satir += ["", "## Değerlendirilen repolar (aday olarak gösterilmez)", "", "| Repo | Karar | Tarih | Neden |", "|---|---|---|---|"]
    for r, v in sorted(deg.items()):
        satir.append(f"| {r} | {v['karar']} | {v['tarih']} | {v['neden'].replace('|', '/')} |")
    RAPOR.write_text("\n".join(satir) + "\n", encoding="utf-8")


def main():
    if "-h" in sys.argv or "--help" in sys.argv:  # yardım istenince tarama başlatma
        print(__doc__ or "konu-takip.py: kullanım için dosyanın başındaki açıklamaya bakın (-h ağ işi yapmaz, dosya yazmaz).")
        return 0
    if "--bekleyenler" in sys.argv:  # her şeyden ÖNCE: ağ yok, dosya yazmaz
        return bekleyenler_calistir("--ozet-json" in sys.argv, "--siki" in sys.argv)
    if "--kuyruk" in sys.argv:
        durum = json_oku(DURUM, {}) or {}
        oz = kuyruk_ozeti(durum)
        if "--json" in sys.argv:
            print(json.dumps(oz, ensure_ascii=False))
        else:
            print(oz["mesaj"])
        return 0
    ayar = json_oku(KAYNAKLAR)
    durum = json_oku(DURUM, {"_aciklama": "araclar/konu-takip.py üretir. 'degerlendirilen' elle/--karar ile doldurulur."})
    if "--kuyruga-ekle" in sys.argv:
        i = sys.argv.index("--kuyruga-ekle")
        if len(sys.argv) < i + 3:
            print('kullanım: konu-takip.py --kuyruga-ekle owner/ad <neden> ["ayrıntı"]')
            sys.exit(2)
        repo, neden = sys.argv[i + 1], sys.argv[i + 2]
        ayrinti = " ".join(sys.argv[i + 3:])
        kayit, hata = kuyruga_ekle(durum, repo, neden, ayrinti)
        if hata:
            print(hata)
            sys.exit(2)
        json_yaz(DURUM, durum)
        print(f"{kayit['repo']}: kuyruk ({kayit['durum']}, {kayit['neden']})")
        return 0
    if "--karar" in sys.argv:
        i = sys.argv.index("--karar")
        if len(sys.argv) < i + 3:
            print('kullanım: konu-takip.py --karar owner/ad eklendi|reddedildi|izle "neden"')
            sys.exit(2)
        repo, karar, neden = sys.argv[i + 1], sys.argv[i + 2], " ".join(sys.argv[i + 3:]) or "-"
        try:
            trend = json_oku(TREND, {})
        except Exception:  # noqa: BLE001
            trend = {}
        mesajlar, hata = karar_uygula(durum, ayar, trend, repo, karar, neden)
        if hata:
            print(hata)
            sys.exit(2)
        for m in mesajlar:
            print(m)
    elif "--rapor" not in sys.argv:
        secili = sys.argv[sys.argv.index("--konu") + 1] if "--konu" in sys.argv else None
        tara(durum, ayar, secili)
        topl = sum(len(k["sorgular"]) for k in ayar["takip_konulari"] if not secili or k["konu"] == secili)
        bas = sum(durum.get("konular", {}).get(k["konu"], {}).get("basarisiz_sorgu", 0) for k in ayar["takip_konulari"]
                  if not secili or k["konu"] == secili)
        if topl and bas * 2 > topl:  # sorguların yarıdan fazlası başarısız: çağıran (aylık güncelleme) uyarı versin
            json_yaz(DURUM, durum)
            rapor(durum, ayar)
            print(f"UYARI: {bas}/{topl} sorgu başarısız (GitHub kod araması yavaş/hız sınırı); sonuçlar eksik olabilir.")
            sys.exit(1)
    json_yaz(DURUM, durum)
    rapor(durum, ayar)
    for k in ayar["takip_konulari"]:
        h = durum.get("konular", {}).get(k["konu"], {})
        e = elenecekler(ayar, durum)
        aday = [r for r, v in h.get("repolar", {}).items() if aday_mi(r, v, k, e)]
        print(f"{k['konu']}: {len(h.get('repolar', {}))} eşleşen repo · odaklı aday {len(aday)}")
    print(f"Rapor: {RAPOR.relative_to(KOK)}")


if __name__ == "__main__":
    sys.exit(main() or 0)
