#!/usr/bin/env python3
"""Yeni repo giriş motoru (Faz 2, 0 token kural kapısı).

Kullanım:
  python3 araclar/yeni-repo.py --girdi-json girdi.json --kuru
  python3 araclar/yeni-repo.py --girdi-json girdi.json --uygula
  python3 araclar/yeni-repo.py --kuyruk-ozet
"""
import argparse
import importlib.util
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ortak  # noqa: E402

ARACLAR_DIZIN = Path(__file__).resolve().parent


def _yukle(dosya_adi, modul_adi):
    spec = importlib.util.spec_from_file_location(modul_adi, ARACLAR_DIZIN / dosya_adi)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SALDIRGAN_ETIKETLER = frozenset({
    "red-team", "redteam", "pentest", "penetration-testing", "offensive-security",
    "exploit-framework", "c2-framework", "post-exploitation", "adversary-emulation",
    "malware-development", "phishing-framework",
})
GUCLU_SALDIRI_ISARETLERI = (
    "reverse shell", "command and control", "c2 server", "privilege escalation",
    "credential dump", "lateral movement", "bypass edr", "bypass av", "ransomware",
    "keylogger", "metasploit", "cobalt strike", "mimikatz", "sliver c2", "sqlmap",
    "phishing kit", "offensive security", "red team", "penetration testing",
    "auto-exploit", "active exploit",
)
ZAYIF_ISARETLER = ("exploit", "payload", "shellcode", "bruteforce", "recon")
GRI_GUVENLIK_ISARETLERI = (
    "reverse engineering", "decompile", "ghidra", "ida pro", "frida",
    "mitmproxy", "local proxy", "traffic intercept",
)
GRI_BETIK_DESEN = re.compile(r"(?i)\b(?:curl|wget)\b[^\n|]{0,120}\|\s*(?:sh|bash|zsh)\b")
SAVUNMA_ISARETLERI = (
    "hardening", "security audit", "vulnerability scan", "dependency check",
    "owasp", "sast", "dast", "secret scan", "compliance", "defensive",
    "code security review", "cve fix", "security best practices", "devsecops",
)
KISITLI_LISANS_ONEKLERI = ("AGPL", "SSPL", "BSL", "BUSL", "ELASTIC", "COMMONS-CLAUSE")
MEDYA_ESIK_MB = 0.2


def on_kapi_kontrol(kok=ortak.KOK, ana_dal="master") -> tuple[bool, str]:
    """Ön-kapı: git status --short boş ve aktif dal ana_dal (master) değil olmalı."""
    kok = Path(kok)
    r = subprocess.run(["git", "status", "--short"], cwd=kok, capture_output=True, text=True)
    if r.returncode != 0:
        return False, "git deposu okunamadı"
    if r.stdout.strip():
        return False, f"çalışma ağacı kirli ({len(r.stdout.strip().splitlines())} değişiklik); işlem durdu"
    dal = subprocess.run(["git", "branch", "--show-current"], cwd=kok, capture_output=True, text=True).stdout.strip()
    if dal == ana_dal:
        return False, f"{ana_dal} dalına doğrudan yazılmaz; faz/çalışma dalına geç"
    return True, "temiz"


def liste_farki(liste_repolari, kaynaklar, konu_durum, yonlendirmeler=None, kayip_404=None) -> dict:
    """GitHub listesi ile mevcut kaynaklar.json ve konu-takip.json farkını çıkarır."""
    yonlendirmeler = yonlendirmeler or {}
    kayip_404_kume = {r.lower() for r in (kayip_404 or ())}
    bilinen_kaynak = set()
    for k in (kaynaklar or {}).get("repolar", []):
        if isinstance(k, dict) and isinstance(k.get("repo"), str):
            bilinen_kaynak.add(k["repo"].lower())
            for eski in (k.get("eski_adlar") or []):
                bilinen_kaynak.add(str(eski).lower())

    degerlendirilen = {r.lower() for r in ((konu_durum or {}).get("degerlendirilen") or {})}
    kuyruk = {r.lower() for r in ((konu_durum or {}).get("kuyruk") or {})}

    yeni, degisen, yonlendirilen_301, kesin_404 = [], [], {}, []
    for repo in liste_repolari:
        rl = repo.lower()
        if rl in kayip_404_kume:
            kesin_404.append(repo)
            continue
        if repo in yonlendirmeler or rl in {k.lower() for k in yonlendirmeler}:
            hedef = yonlendirmeler.get(repo) or next(v for k, v in yonlendirmeler.items() if k.lower() == rl)
            yonlendirilen_301[repo] = hedef
            continue
        if rl in bilinen_kaynak:
            degisen.append(repo)
        elif rl not in degerlendirilen and rl not in kuyruk:
            yeni.append(repo)
    return {
        "yeni": yeni,
        "degisen": degisen,
        "yonlendirilen_301": yonlendirilen_301,
        "kesin_404": kesin_404,
    }


def guvenlik_siniflandir(repo, aciklama, agac, icerikler, konular=None) -> tuple[str, list[str]]:
    """K-58 güçlü işaret kontrolü + savunma istisnası + gri_guvenlik ayrımı.
    Döner: ('K-58' | 'gri_guvenlik' | 'temiz', kanitlar)."""
    etiketler = {str(t).strip().lower() for t in (konular or []) if isinstance(t, str)}
    saldirgan_etiketler = sorted(etiketler & SALDIRGAN_ETIKETLER)

    metin_parcalari = [str(repo or ""), str(aciklama or "")]
    for y in sorted((icerikler or {}).keys())[:10]:
        metin_parcalari.append(str(icerikler[y] or "")[:4000])
    metin = "\n".join(metin_parcalari).lower()

    guclu = [p for p in GUCLU_SALDIRI_ISARETLERI if re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", metin)]
    if saldirgan_etiketler or len(set(guclu)) >= 2:
        kanitlar = [f"etiket:{e}" for e in saldirgan_etiketler] + sorted(set(guclu))
        return "K-58", kanitlar

    gri = [p for p in GRI_GUVENLIK_ISARETLERI if p in metin]
    if GRI_BETIK_DESEN.search(metin):
        gri.append("curl/wget|sh")
    savunma = [p for p in SAVUNMA_ISARETLERI if p in metin]
    zayif = [p for p in ZAYIF_ISARETLER if re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", metin)]

    if len(set(guclu)) == 1:
        return "gri_guvenlik", sorted(set(guclu))
    if gri:
        return "gri_guvenlik", sorted(set(gri))
    if zayif and not savunma:
        return "gri_guvenlik", sorted(set(zayif))
    return "temiz", []


def _cjk_orani(metin: str) -> float:
    harfler = [c for c in metin if not c.isspace()]
    if not harfler:
        return 0.0
    cjk = sum(1 for c in harfler if "\u4e00" <= c <= "\u9fff" or "\u3040" <= c <= "\u30ff")
    return cjk / len(harfler)


def _lisans_kisitli_mi(lisans: str | None) -> bool:
    if not lisans:
        return True
    s = str(lisans).strip().upper()
    if s in ("YOK", "BELİRTİLMEMİŞ", "BELIRTILMEMIS", "NONE", "NOASSERTION", "OTHER", ""):
        return True
    return any(s.startswith(p) for p in KISITLI_LISANS_ONEKLERI)


def _skill_adlari_agactan(agac, icerikler) -> list[str]:
    tb = _yukle("tur-belirle.py", "tur_belirle_yr")
    adlar = []
    for d in tb.skil_klasorleri(agac):
        yol = f"{d}/SKILL.md" if d else "SKILL.md"
        metin = (icerikler or {}).get(yol, "")
        fm = ortak.frontmatter(metin) if metin else {}
        ad = fm.get("name") if isinstance(fm.get("name"), str) and fm["name"].strip() else (Path(d).name if d else "")
        if ad:
            adlar.append(ad.strip())
    return adlar


def hafif_kapi_degerlendir(repo, meta, agac, icerikler, kaynaklar, registry, kendi_adlari=None, bugun=None) -> dict:
    """Yeni repo için 10 sıralı Hafif Kapı kuralını çalıştırır (0 token, ağsız, yazmaz)."""
    bugun = bugun or date.today().isoformat()
    meta = meta or {}
    aciklama = str(meta.get("aciklama") or meta.get("description") or "").strip()
    lisans = meta.get("lisans") or meta.get("license")
    push_tarihi = meta.get("son_push") or meta.get("pushed_at")
    sha = str(meta.get("commit") or meta.get("sha") or "")
    konular = meta.get("konular") or meta.get("topics") or []
    alt_tur = meta.get("alt_tur")

    # 1. Saldırgan güvenlik / K-58 (boyut/çakışma çalıştırmadan otomatik ret)
    guv_durum, guv_kanit = guvenlik_siniflandir(repo, aciklama, agac, icerikler, konular)
    if guv_durum == "K-58":
        return {
            "repo": repo, "karar": "REDDET_K58", "neden": "K-58",
            "ayrinti": "Güçlü saldırgan güvenlik işareti: " + ", ".join(guv_kanit),
        }

    # 2. Lisans yok veya kısıtlı
    tb = _yukle("tur-belirle.py", "tur_belirle_yr")
    skil_lisans_var = any(
        re.fullmatch(r"LICEN[SC]E(\.\w+)?", x["path"].rsplit("/", 1)[-1], re.I)
        and any(x["path"].startswith(d + "/") for d in tb.skil_klasorleri(agac) if d)
        for x in agac if x.get("type") == "blob"
    )
    if _lisans_kisitli_mi(lisans) and not skil_lisans_var:
        return {
            "repo": repo, "karar": "KUYRUK", "neden": "lisans_yok",
            "ayrinti": f"Lisans eksik veya kısıtlı ({lisans or 'yok'})",
        }

    # 3. Gri alan güvenlik
    if guv_durum == "gri_guvenlik":
        return {
            "repo": repo, "karar": "KUYRUK", "neden": "gri_guvenlik",
            "ayrinti": "Gri alan güvenlik işareti: " + ", ".join(guv_kanit),
        }

    # 4. Açıklama boş, CJK ağırlıklı veya SKILL.md yok (CLAUDE.md / DESIGN.md)
    dosya_yollari = [x["path"] for x in agac if x.get("type") == "blob"]
    skill_md_sayisi = len(tb.skil_klasorleri(agac))
    standart_disi = [p for p in dosya_yollari if p.rsplit("/", 1)[-1].upper() in ("CLAUDE.MD", "DESIGN.MD")]
    if not aciklama or _cjk_orani(aciklama) >= 0.30 or (skill_md_sayisi == 0 and standart_disi):
        sebep = "açıklama boş" if not aciklama else ("çok dilli/CJK açıklama" if _cjk_orani(aciklama) >= 0.30 else "SKILL.md yok (CLAUDE.md/DESIGN.md)")
        return {
            "repo": repo, "karar": "KUYRUK", "neden": "aciklama_veya_skill_yok",
            "ayrinti": sebep,
        }

    # 5. Tür sırası (tur-belirle.py)
    tk = tb.tur_karari(agac, icerikler, lisans, push_tarihi=push_tarihi, bugun=date.fromisoformat(bugun))
    if tk["durum"] == "EKLENMEZ":
        return {"repo": repo, "karar": "KUYRUK", "neden": "lisans_yok", "ayrinti": tk["gerekce"]}
    if tk["tur"] == "repo-ici":
        return {"repo": repo, "karar": "KUYRUK", "neden": "tur_aday", "ayrinti": "Yeni repo-ici skill alınmaz"}
    if tk["durum"] == "ADAY":
        return {"repo": repo, "karar": "KUYRUK", "neden": "tur_aday", "ayrinti": f"{tk['tur']} ADAY: {tk['gerekce']}"}

    tur, bolum = tk["tur"], tk["bolum"]

    # 6. Arşivlenecek KESİN türlerde ad çakışması ve medya dışlama
    medya_haric = {}
    ne_indirir = None
    if bolum == "arsiv":
        mevcut_adlar = {s["ad"].lower() for s in (registry or {}).get("skiller", []) if isinstance(s, dict) and s.get("ad")}
        yerel_adlar = {a.lower() for a in (kendi_adlari or ())}
        yeni_adlar = _skill_adlari_agactan(agac, icerikler)
        cakisan = [a for a in yeni_adlar if a.lower() in mevcut_adlar or a.lower() in yerel_adlar]
        if cakisan:
            return {
                "repo": repo, "karar": "KUYRUK", "neden": "ad_cakismasi",
                "ayrinti": f"Mevcut/yerel skill ile ad çakışması: {', '.join(cakisan)}",
            }
        esik_bayt = int(MEDYA_ESIK_MB * 1024 * 1024)
        for x in agac:
            if x.get("type") == "blob" and ortak.medya_mi(x["path"]) and not ortak.medya_haric_korunur_mu(x["path"]):
                if (x.get("size") or 0) > esik_bayt:
                    medya_haric[x["path"]] = "medya-esik-ustu"
        if medya_haric:
            ne_indirir = f"büyük medya/model hariç tutuldu ({len(medya_haric)} dosya)"

    # 7. Onaysız KESİN kayıt taslağı
    kayit = {
        "repo": repo,
        "tur": tur,
        "bolum": bolum,
        "tur_gerekce": tk["gerekce"],
        "eklendi": bugun,
        "onay": {"kim": "kural", "tarih": bugun, "commit": sha},
    }
    if tur == "referans":
        kayit["alt_tur"] = alt_tur if alt_tur in ortak.REFERANS_ALT_TURLERI else "kutuphane"
    if medya_haric:
        kayit["medya_haric"] = medya_haric
    if ne_indirir:
        kayit["ne_indirir"] = ne_indirir
    return {"repo": repo, "karar": "OTOMATIK_KAYIT", "kayit": kayit, "uyarilar": tk["uyarilar"]}


def otomatik_isle(kok, girdiler, *, uygula=False, bugun=None, on_kapi=True, ana_dal="master") -> dict:
    """Yeni repo listesini işler. uygula=True iken ön-kapıdan geçerse kaynaklar.json ve konu-takip.json yazar."""
    kok = Path(kok)
    bugun = bugun or date.today().isoformat()
    if uygula and on_kapi:
        ok, neden = on_kapi_kontrol(kok, ana_dal=ana_dal)
        if not ok:
            raise RuntimeError(f"Ön-kapı engeli: {neden}")

    kaynak_yol = kok / "kaynaklar.json"
    reg_yol = kok / "registry.json"
    kt_yol = kok / "konu-takip.json"
    kaynaklar = ortak.json_oku(kaynak_yol, {"repolar": []}) or {"repolar": []}
    registry = ortak.json_oku(reg_yol, {"skiller": []}) or {"skiller": []}
    konu_durum = ortak.json_oku(kt_yol, {"degerlendirilen": {}, "konular": {}, "izlenen": {}}) or {}
    kt = _yukle("konu-takip.py", "konu_takip_yr")

    kendi_klasor = kok / "kendi"
    kendi_adlari = {p.parent.name for p in kendi_klasor.rglob("SKILL.md")} if kendi_klasor.is_dir() else set()

    otomatik, reddedilen_k58, kuyruk = [], [], []
    mevcut_repolar = {k["repo"].lower() for k in kaynaklar.get("repolar", []) if isinstance(k, dict) and k.get("repo")}

    for item in girdiler:
        repo = item["repo"]
        sonuc = hafif_kapi_degerlendir(
            repo, item.get("meta"), item.get("agac", []), item.get("icerikler", {}),
            kaynaklar, registry, kendi_adlari=kendi_adlari, bugun=bugun,
        )
        if sonuc["karar"] == "REDDET_K58":
            reddedilen_k58.append(sonuc)
            kt.kuyruga_ekle(konu_durum, repo, "K-58", sonuc["ayrinti"], bugun=bugun)
        elif sonuc["karar"] == "KUYRUK":
            kuyruk.append(sonuc)
            kt.kuyruga_ekle(konu_durum, repo, sonuc["neden"], sonuc["ayrinti"], bugun=bugun)
        elif sonuc["karar"] == "OTOMATIK_KAYIT":
            otomatik.append(sonuc)
            if repo.lower() not in mevcut_repolar:
                kaynaklar.setdefault("repolar", []).append(sonuc["kayit"])
                mevcut_repolar.add(repo.lower())

    if uygula:
        ortak.json_yaz(kaynak_yol, kaynaklar)
        ortak.json_yaz(kt_yol, konu_durum)

    ozet = kt.kuyruk_ozeti(konu_durum)
    return {
        "uygulandi": bool(uygula),
        "otomatik": otomatik,
        "reddedilen_k58": reddedilen_k58,
        "kuyruk": kuyruk,
        "kuyruk_ozeti": ozet,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Yeni repo giriş akışı (Faz 2, varsayılan --kuru)")
    ap.add_argument("--kok", default=str(ortak.KOK), help="Kütüphane kök klasörü")
    ap.add_argument("--girdi-json", default=None, help="Çevrimdışı repo girdi JSON dosyası")
    ap.add_argument("--kuru", action="store_true", help="Hiçbir dosya yazmadan kuru rapor üret (varsayılan)")
    ap.add_argument("--uygula", action="store_true", help="Ön-kapı temizse KESİN kayıtları ve kuyruğu yaz")
    ap.add_argument("--json", action="store_true", help="Çıktıyı JSON olarak yazdır")
    ap.add_argument("--kuyruk-ozet", action="store_true", help="Yalnız konu-takip.json kuyruk özetini yazdır")
    ap.add_argument("--ana-dal", default="master", help="Doğrudan yazılması engellenen ana dal (varsayılan: master)")
    a = ap.parse_args(argv)

    kok = Path(a.kok)
    if a.kuyruk_ozet:
        kt = _yukle("konu-takip.py", "konu_takip_yr")
        oz = kt.kuyruk_ozeti(ortak.json_oku(kok / "konu-takip.json", {}) or {})
        print(json.dumps(oz, ensure_ascii=False) if a.json else oz["mesaj"])
        return 0

    if not a.girdi_json:
        ap.error("--girdi-json veya --kuyruk-ozet verilmelidir (gerçek ağ taraması Faz 3'tedir)")

    girdiler = json.loads(Path(a.girdi_json).read_text(encoding="utf-8"))
    if isinstance(girdiler, dict):
        girdiler = girdiler.get("repolar", [])
    sonuc = otomatik_isle(kok, girdiler, uygula=bool(a.uygula and not a.kuru), ana_dal=a.ana_dal)
    if a.json:
        print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    else:
        print(f"Otomatik (kim=kural): {len(sonuc['otomatik'])} · K-58 ret: {len(sonuc['reddedilen_k58'])} · Kuyruk: {len(sonuc['kuyruk'])}")
        print(sonuc["kuyruk_ozeti"]["mesaj"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
