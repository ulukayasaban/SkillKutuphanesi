#!/usr/bin/env python3
"""Program denetimi (salt okuma): programlar.json'daki her program için, kaynak kopyalı kartta kütüphanedeki sürümü
GitHub'daki en son sürümle karşılaştırır ve kopya klasörünün var olduğunu kontrol eder; yerinde (kopyasız) kartta
karttaki, kurulu ve son değeri karşılaştırır.

İki kart türü var: 'kaynak' (varsayılan; kaynak kopyası kütüphanede) ve 'yerinde' (kopya yok; program bu bilgisayarda kurulu:
npm-global paket ya da git-checkout). 'yerinde' kartta üç değer bakılır: karttaki, kurulu (şimdi), son (GitHub/npm). Kurulu değer
sadece dosya okuyarak (package.json, salt okuma git, dist-info/METADATA) bulunur; npm, pip, venv python, programın kendisi ÇALIŞMAZ.
Hiçbir şey kurmaz, indirmez, güncellemez; program komutlarını çalıştırmaz; anahtar/oturum dosyalarını açmaz (yalnız var/yok bakar).
Ağ hatası denetimi düşürmez ("öğrenilemedi" yazar; 404 ile ağ hatası ayrı sınıflanır).

Kullanım:
  python3 araclar/program-denetim.py                          # rapor (notlar/program-denetimi.md), çıkış 0
  python3 araclar/program-denetim.py --ozet-json [--siki]     # aynı koşu, stdout'a tek JSON nesnesi; HİÇBİR dosya yazmaz
  python3 araclar/program-denetim.py --sema [--ozet-json] [--siki]   # kart şeması denetimi
  python3 araclar/program-denetim.py --oncesi AD [--hedef SÜRÜM_YA_DA_SHA] [--cevrimdisi] [--tedarik] [--ozet-json] [--siki]
  (bağlar) Bir ya da daha çok projede programla gelen skill bağı varsa (projelerin kilit.json 'dis_skiller'; skill-ekle.py --program-skill)
  rapor ve --oncesi 'bağlar' satırları ekler: hedef şimdi var mı; git-checkout'ta hedef commit yerel depodaysa güncellemeden sonra
  kırılacak bağlar (UYARI 'bağ kırılacak'). Bağ yoksa çıktı değişmez. Kırık bağ yalnız güncelleme dışı görünümde HATA; HAZIR DEĞİL sebebi olmaz.
  python3 araclar/program-denetim.py --iskelet {kaynak|npm-global|git-checkout}   # boş kart iskeleti
  python3 araclar/program-denetim.py --pin-listesi AD         # venv'deki paket==sürüm listesi
  ortak: --kart PATH --cikti PATH --ev DIZIN --yedek-koku DIZIN --kok DIZIN
Çıkış kodu: 0 araç doğru çalıştı (ne bulursa bulsun); 1 yalnız --siki ile ve sonuç 'sorun'/'HAZIR DEĞİL' ise; 2 kullanım hatası.
"""
import argparse
import contextlib
import json
import os
import re
import shutil
import subprocess
import sys
import types
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, GhBulunamadi, api_kapali, gh_api, json_oku, repo_guncel, repo_takma_adlari  # noqa: E402


def surum_ayikla(etiket):
    """'v0.5.0' / '0.5.0' -> (0, 5); anlaşılmazsa None. Sondaki sıfırlar atılır: '1.2' ile '1.2.0' aynı sayılır."""
    m = re.fullmatch(r"v?(\d+(?:\.\d+)*)", (etiket or "").strip())
    if not m:
        return None
    t = tuple(int(x) for x in m.group(1).split("."))
    while len(t) > 1 and t[-1] == 0:
        t = t[:-1]
    return t


def durum(kutuphane, son):
    a, b = surum_ayikla(kutuphane), surum_ayikla(son)
    if not a or not b:
        return "öğrenilemedi"
    return "güncel" if a >= b else "YENİ SÜRÜM VAR"



YERINDE_TURLER = ("npm-global", "git-checkout")


_EV = None  # --ev: '~' bu klasöre çevrilir (testler gerçek ev klasörüne bakmasın)
_SON_HATA = {}  # ("npm", paket) / ("git", repo) -> "404" | "ag" | "kapali" (son çağrının nasıl başarısız olduğu)


def yol_ac(yol, ev=None):
    """'~/x' -> mutlak yol. ev (ya da --ev) verilirse '~' o klasöre çevrilir."""
    ev = ev if ev is not None else _EV
    s = str(yol)
    if ev is not None and (s == "~" or s.startswith("~/")):
        return Path(ev) / s[2:]
    return Path(s).expanduser()


def _kapali(e):
    return api_kapali(e) or "gh api kapalı" in str(e)


def npm_kurulu_surum(yol):
    """<yol>/package.json içindeki 'version'; dosya yok/bozuksa None (program bu bilgisayarda yok)."""
    try:
        v = json.loads((yol_ac(yol) / "package.json").read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError):
        return None
    return v if isinstance(v, str) and v.strip() else None


def npm_son_surum(paket, zaman_asimi=8):
    """npm kayıt defterinden son sürüm (npm komutu yok, sadece urllib); hata olursa None."""
    try:
        with urllib.request.urlopen(f"https://registry.npmjs.org/{paket}/latest", timeout=zaman_asimi) as r:
            v = json.loads(r.read().decode("utf-8")).get("version")
    except urllib.error.HTTPError as e:
        _SON_HATA[("npm", paket)] = "404" if getattr(e, "code", None) == 404 else "ag"
        return None
    except Exception:  # noqa: BLE001  ağ/ayrıştırma: denetim düşmez
        _SON_HATA[("npm", paket)] = "ag"
        return None
    if isinstance(v, str) and v.strip():
        _SON_HATA.pop(("npm", paket), None)
        return v
    _SON_HATA[("npm", paket)] = "ag"
    return None


def npm_integrity(paket, surum, zaman_asimi=8):
    """npm kayıt defterinden bir sürümün dist.integrity değeri (salt okuma GET); alınamazsa None."""
    try:
        with urllib.request.urlopen(f"https://registry.npmjs.org/{paket}/{surum}", timeout=zaman_asimi) as r:
            v = (json.loads(r.read().decode("utf-8")).get("dist") or {}).get("integrity")
    except urllib.error.HTTPError as e:
        _SON_HATA[("npm-integrity", paket)] = "404" if getattr(e, "code", None) == 404 else "ag"
        return None
    except Exception:  # noqa: BLE001
        _SON_HATA[("npm-integrity", paket)] = "ag"
        return None
    return v if isinstance(v, str) and v.strip() else None


def git_okuma(yol, *args):
    """Salt okuma git (rev-parse/status/cat-file -e); çıktı ya da None. İndeksi bile yenilemez (--no-optional-locks).
    cat-file -e başarıda boş çıktı verir (''), yokluğunda None döner."""
    try:
        r = subprocess.run(["git", "--no-optional-locks", "-C", str(yol_ac(yol)), *args],
                           capture_output=True, text=True, timeout=60, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout if r.returncode == 0 else None


def porcelain_say(metin):
    """'git status --porcelain' çıktısı -> (değişen izlenen dosya sayısı, izlenmeyen yol sayısı)."""
    degisen = izlenmeyen = 0
    for satir in (metin or "").splitlines():
        if not satir.strip():
            continue
        if satir.startswith("??"):
            izlenmeyen += 1
        elif not satir.startswith("!!"):
            degisen += 1
    return degisen, izlenmeyen


def git_kurulu(yol):
    """(commit, değişen, izlenmeyen); yol bir deponun kökü değilse ya da yoksa (None, 0, 0).
    'git status' başarısız olursa değişen/izlenmeyen None döner (temiz sayılmaz)."""
    top = git_okuma(yol, "rev-parse", "--show-toplevel")
    if not top or os.path.realpath(top.strip()) != os.path.realpath(str(yol_ac(yol))):
        return None, 0, 0  # yol yok, depo değil ya da üst klasördeki başka bir depo
    sha = git_okuma(yol, "rev-parse", "HEAD")
    if not sha or not sha.strip():
        return None, 0, 0
    st = git_okuma(yol, "status", "--porcelain")
    if st is None:
        return sha.strip(), None, None
    d, i = porcelain_say(st)
    return sha.strip(), d, i


def git_son(repo, dal, kurulu=None):
    """(son commit sha, kurulu commit'ten kaç commit ileride); GitHub API, git fetch yok. Hata: (None, None).
    Karşılaştırma bulunamazsa (kurulu commit GitHub'da yok) geride None kalır."""
    try:
        sha = gh_api(f"repos/{repo}/commits/{dal}", deneme=2)["sha"]
    except Exception as e:  # noqa: BLE001
        _SON_HATA[("git", repo)] = "404" if isinstance(e, GhBulunamadi) else "kapali" if _kapali(e) else "ag"
        return None, None
    _SON_HATA.pop(("git", repo), None)
    geride = None
    if kurulu and kurulu != sha:
        try:
            geride = int(gh_api(f"repos/{repo}/compare/{kurulu}...{dal}", deneme=2)["ahead_by"])
        except Exception:  # noqa: BLE001
            geride = None
    elif kurulu == sha:
        geride = 0
    return sha, geride


def sha_esit(a, b):
    """Tam sha ya da en az 7 haneli önek eşleşmesi."""
    a, b = (a or "").strip().lower(), (b or "").strip().lower()
    return bool(a) and bool(b) and min(len(a), len(b)) >= 7 and (a.startswith(b) or b.startswith(a))


def ham_surum(v):
    """Karşılaştırma için düz metin: boşluk ve baştaki 'v' atılır ('v1.2.0-beta.1' -> '1.2.0-beta.1')."""
    return (v or "").strip().lstrip("vV")


def yerinde_durum(tur, kart, kurulu, son, geride=None):
    """'yerinde' kartın durum sözcüğü. Sıra: kurulu yok -> kart eski -> son bilinmiyor -> yeni sürüm / güncel.
    npm-global'de önce düz metinle kart eşitliği, sonra sürüm sayıyla; git-checkout'ta commit eşitliğiyle.
    git'te geride == 0 ise (kurulu commit GitHub dalından geri değil) sha farklı olsa da 'güncel'."""
    if not kurulu:
        return "bu bilgisayarda kurulu değil"
    if tur == "git-checkout":
        if not sha_esit(kart, kurulu):
            return "KART ESKİ"
        if not son:
            return "öğrenilemedi"
        return "güncel" if sha_esit(kurulu, son) or geride == 0 else "YENİ SÜRÜM VAR"
    kk, uu = surum_ayikla(kart), surum_ayikla(kurulu)
    if ham_surum(kart) != ham_surum(kurulu) and (kk is None or uu is None or kk != uu):
        return "KART ESKİ"
    u, s = surum_ayikla(kurulu), surum_ayikla(son)
    if not u or not s:
        return "öğrenilemedi"  # ön-sürüm ya da bozuk metin: sayıyla karşılaştırılamaz
    return "güncel" if u >= s else "YENİ SÜRÜM VAR"


def paket_adi(ad):
    """PEP 503 normal ad: büyük/küçük harf ve -_. ayrımı yok."""
    return re.sub(r"[-_.]+", "-", str(ad)).lower()


def _surum_anahtar(v):
    """Sıralama için baştaki sayılar: '2.0.0rc1' -> (2, 0, 0); sayı yoksa ()."""
    m = re.match(r"\d+(?:\.\d+)*", v or "")
    return tuple(int(x) for x in m.group(0).split(".")) if m else ()


def dist_info_oku(venv):
    """venv'in site-packages/*.dist-info/METADATA dosyalarından {normal ad: sürüm}. Sadece dosya okur; pip/python çalışmaz."""
    kok = yol_ac(venv)
    sonuc = {}
    siteler = list(kok.glob("lib/python*/site-packages")) + list(kok.glob("Lib/site-packages")) + list(kok.glob("lib64/python*/site-packages"))
    for site in siteler:
        for di in sorted(site.glob("*.dist-info")):
            ad = surum = None
            try:
                with open(di / "METADATA", encoding="utf-8", errors="replace") as f:
                    for satir in f:
                        if not satir.strip():
                            break  # başlık bölümü bitti
                        if satir.startswith("Name:"):
                            ad = satir[5:].strip()
                        elif satir.startswith("Version:"):
                            surum = satir[8:].strip()
            except OSError:
                continue
            if ad and surum:
                n = paket_adi(ad)
                if n not in sonuc or _surum_anahtar(surum) > _surum_anahtar(sonuc[n]):
                    sonuc[n] = surum  # aynı paketin iki kaydı varsa en yüksek sürüm (sıradan bağımsız)
    return sonuc


_KISIT = re.compile(r"\s*(==|!=|>=|<=|>|<)\s*(\d+(?:\.\d+)*)\s*")


def kisit_uyar(kisit, surum):
    """Sabit sürüm metni kurulu sürümle uyuşuyor mu? '1.2.3' / '==1.2.3' tam eşleşme; '>=1,<2' gibi kısıtlar sayıyla.
    True / False; metin anlaşılmazsa None."""
    if surum is None:
        return False
    metin = str(kisit).strip()
    tam = re.fullmatch(r"(?:==)?\s*(\S+)", metin)
    if tam and not re.search(r"[<>!,~]", tam.group(1)):  # işleç yok: tam sürüm metni
        t = tam.group(1)
        if t == surum:
            return True
        a, b = surum_ayikla(t), surum_ayikla(surum)
        return a is not None and b is not None and a == b
    v = surum_ayikla(surum)
    parcalar = [x for x in metin.split(",") if x.strip()]
    if not v or not parcalar:
        return None
    for x in parcalar:
        m = _KISIT.fullmatch(x)
        if not m:
            return None
        op, hedef = m.group(1), surum_ayikla(m.group(2))
        ok = {"==": v == hedef, "!=": v != hedef, ">=": v >= hedef, "<=": v <= hedef, ">": v > hedef, "<": v < hedef}[op]
        if not ok:
            return False
    return True


def pin_karsilastir(sabit, kurulu):
    """sabit {paket: sürüm/kısıt}, kurulu {normal ad: sürüm} -> (uyan sayısı, [farklar]).
    Fark metni: 'paket: karttaki X, kurulu Y' / 'kurulu değil' / 'kısıt anlaşılmadı'."""
    uyan, farklar = 0, []
    for paket, kisit in sorted(sabit.items()):
        s = kurulu.get(paket_adi(paket))
        r = kisit_uyar(kisit, s)
        if r:
            uyan += 1
        elif s is None:
            farklar.append(f"{paket}: karttaki {kisit}, kurulu değil")
        elif r is None:
            farklar.append(f"{paket}: kısıt anlaşılmadı ({kisit}), kurulu {s}")
        else:
            farklar.append(f"{paket}: karttaki {kisit}, kurulu {s}")
    return uyan, farklar


def yerinde_denetle(ad, p):
    """Bir 'yerinde' kart için sözlük döner (ağa ve diske sadece okumaya gider)."""
    y = p.get("yerinde") or {}
    tur, yol = y.get("tur"), y.get("yol", "")
    r = {"ad": ad, "tur": tur, "kart": p.get("kutuphane_commit") if tur == "git-checkout" else p.get("kutuphane_surumu"),
         "kurulu": None, "son": None, "geride": None, "degisen": 0, "izlenmeyen": 0, "pin": None, "pin_fark": []}
    if tur == "npm-global":
        r["kurulu"] = npm_kurulu_surum(yol)
        r["son"] = npm_son_surum(y.get("paket", "")) if r["kurulu"] else None
    elif tur == "git-checkout":
        r["kurulu"], r["degisen"], r["izlenmeyen"] = git_kurulu(yol)
        if r["kurulu"]:
            if p.get("repo"):
                r["son"], r["geride"] = git_son(p["repo"], y.get("dal", "main"), r["kurulu"])
    r["durum"] = yerinde_durum(tur, r["kart"], r["kurulu"], r["son"], r["geride"])
    if r["kurulu"] and r["son"] is None:  # son sürüm alınamadı: 404 mü (repo/paket yok), ağ mı?
        anahtar = ("npm", y.get("paket", "")) if tur == "npm-global" else ("git", p.get("repo"))
        r["son_hata"] = _SON_HATA.get(anahtar)
        if r["son_hata"] == "404" and tur == "git-checkout" and p.get("repo"):
            try:
                r["repo_durum"] = repo_durumu(p["repo"])
            except Exception:  # noqa: BLE001
                pass
    sabit = p.get("sabit_surumler")
    if isinstance(sabit, dict) and sabit and r["kurulu"] and p.get("venv"):
        uyan, fark = pin_karsilastir(sabit, dist_info_oku(yol_ac(yol) / p["venv"]))
        r["pin"], r["pin_fark"] = f"{uyan}/{len(sabit)}", fark
    return r


def kisa(v, tur):
    """Tabloda commit'i 8 haneye kısalt; sürüm olduğu gibi."""
    return (v or "?")[:8] if tur == "git-checkout" and v else (v or "?")


def yerel_metin(r):
    """Git deposundaki yerel değişiklik özeti; git dışında '-'; status okunamadıysa 'öğrenilemedi'."""
    if r["tur"] != "git-checkout" or not r["kurulu"]:
        return "-"
    if r["degisen"] is None or r["izlenmeyen"] is None:
        return "öğrenilemedi"
    return f"{r['degisen']} değişen, {r['izlenmeyen']} izlenmeyen" if r["degisen"] or r["izlenmeyen"] else "temiz"


def yerinde_satir(r):
    t = r["tur"]
    yerel = yerel_metin(r)
    son = kisa(r["son"], t) + (f" ({r['geride']} geride)" if r["geride"] else "")
    return f"| {r['ad']} | {t} | {kisa(r['kart'], t)} | {kisa(r['kurulu'], t) if r['kurulu'] else '-'} | {son} | {r['durum']} | {yerel} | {r['pin'] or '-'} |"




# ============================================================ ağ sınıflaması (404 / ağ / kapalı)

def repo_durumu(repo, gh=None, kaynaklar=None):
    """GitHub'da repo durumu: ("var", None) | ("taşınmış", yeni_ad) | ("kayıp", None) | ("kapalı", None) | ("ağ", None).
    Salt okuma GET. 404'te kaynaklar.json kaydındaki eski adlar denenir."""
    gh = gh or gh_api
    try:
        d = gh(f"repos/{repo}", deneme=2)
        tam = d.get("full_name") if isinstance(d, dict) else None
        if tam and tam.lower() != str(repo).lower():
            return ("taşınmış", tam)
        return ("var", None)
    except GhBulunamadi:
        if kaynaklar is None:
            kaynaklar = json_oku(KOK / "kaynaklar.json", {}) or {}
        eskiler = []
        for k in (kaynaklar.get("repolar") or []):
            adlar = [str(k.get("repo", "")).lower()] + [str(e).lower() for e in (k.get("eski_adlar") or [])]
            if str(repo).lower() in adlar:
                eskiler += [x for x in [k.get("repo")] + list(k.get("eski_adlar") or []) if x and x.lower() != str(repo).lower()]
        for e in eskiler:
            try:
                d = gh(f"repos/{e}", deneme=2)
                return ("taşınmış", (d.get("full_name") if isinstance(d, dict) else None) or e)
            except Exception:  # noqa: BLE001
                continue
        return ("kayıp", None)
    except Exception as e:  # noqa: BLE001
        return ("kapalı", None) if _kapali(e) else ("ağ", None)


def kart_eski_ad(p):
    """Kart eski (taşınmış) repo adını taşıyorsa yeni adı, yoksa None."""
    yeni = repo_takma_adlari().get(str(p.get("repo", "")).lower())
    return yeni if yeni and yeni.lower() != str(p.get("repo", "")).lower() else None


def origin_durumu(yol, p, ev=None):
    """Klonun origin adresi: 'güncel' | 'eski-ad' (kaynaklar.json eski_adlar) | 'farklı' (| None okunamadı)."""
    url = git_okuma(yol_ac(yol, ev), "remote", "get-url", "origin")
    if not url:
        return None
    m = re.search(r"github\.com[:/]+([^/\s]+/[^/\s]+?)(?:\.git)?\s*$", url.strip())
    ad = (m.group(1) if m else "").lower()
    if ad == str(p.get("repo", "")).lower():
        return "güncel"
    eskiler = [e for e, yeni in repo_takma_adlari().items() if yeni.lower() == str(p.get("repo", "")).lower()]
    return "eski-ad" if ad in eskiler else "farklı"


def git_karsilastir(repo, kurulu, dal):
    """GitHub compare: (ahead_by, [dosya yolları], kesik_mi). Hata yukarı fırlar (çağıran yakalar)."""
    d = gh_api(f"repos/{repo}/compare/{kurulu}...{dal}", deneme=2)
    dosyalar = [f.get("filename", "") for f in (d.get("files") or []) if isinstance(f, dict)]
    return int(d["ahead_by"]), dosyalar, len(d.get("files") or []) >= 300


# ============================================================ kart şeması

ARAC_ANAHTARLARI = ("claude-code", "codex", "antigravity", "cursor", "vscode-copilot")
ARAC_ISTEGE_BAGLI = ("gemini-cli", "copilot-cli")
GIRIS_DURUMLARI = ("yerinde", "program-klasoru", "proje-skili", "karar-bekliyor", "yok")
YASAK_ADLAR = (".env", "token.json", "credentials.json", "auth.json")
YER_TUTUCU = "<DOLDUR>"
UCRETLER = ("ucretsiz", "kismen", "ucretli")
DISARIYA_TURLER = ("veri", "program", "skill", "bag", "ayar", "cikti", "onbellek", "anahtar")
YAMA_TURLER = ("izlenen", "izlenmeyen", "venv")
OZET_TURLER = ("sha256", "npm-integrity", "git-commit", "yok")
CEKIRDEK_ALANLAR = ("giris_yolu", "kurulum", "geri_alma", "cikarma", "yedek", "ortam_anahtarlari")
ISTEGE_BAGLI_ALANLAR = ("disariya_yazar", "tedarik_dogrulama", "kirici_surum", "gizli_dosyalar", "yerel_yamalar")
_HEX40 = re.compile(r"[0-9a-f]{40}")
_GIZLI = re.compile(r"sk-[A-Za-z0-9_-]{20}|ghp_[A-Za-z0-9]{20}|AKIA[A-Z0-9]{16}|-----BEGIN")


def _dolu(v):
    return isinstance(v, str) and YER_TUTUCU in v


def _kart_metinleri(v, yol=""):
    """Kartın tüm metin değerleri: (alan yolu, metin)."""
    if isinstance(v, str):
        yield yol, v
    elif isinstance(v, dict):
        for k, x in v.items():
            yield from _kart_metinleri(x, f"{yol}.{k}" if yol else str(k))
    elif isinstance(v, (list, tuple)):
        for i, x in enumerate(v):
            yield from _kart_metinleri(x, f"{yol}[{i}]")


def proje_adlari(kok=KOK):
    """projeler.json'dan proje adları (kart metninde geçmemeli: kütüphane kuralı 6); dosya yoksa boş."""
    try:
        d = json_oku(Path(kok) / "projeler.json", {}) or {}
    except (OSError, ValueError):
        return set()
    adlar = set((d.get("notlar") or {}).keys())
    adlar |= {Path(str(x)).name for x in (d.get("ek_projeler") or [])}
    return {a for a in adlar if len(a) >= 4}


def sema_denetle(kart, kok=KOK, kaynaklar=None, ev=None, sadece=None):
    """Kart şeması denetimi. kart: programlar.json'un tamamı ({'sema':2,'programlar':{...}}) ya da yalnız programlar sözlüğü.
    Dönen: [(seviye 'HATA'|'UYARI', kart adı, alan yolu, mesaj)]. Çekirdek alan eksikliği HATA; isteğe bağlı alanın yokluğu
    sessizdir, varsa ama geçersizse UYARI. '<DOLDUR>' içeren değerlerde yalnız 'doldurulmamış' bildirilir."""
    kok = Path(kok)
    sonuc = []
    if isinstance(kart, dict) and "programlar" in kart:
        if kart.get("sema") != 2 and sadece is None:
            sonuc.append(("UYARI", "programlar.json", "sema", "sürüm işareti yok ya da 2 değil"))
        programlar = kart["programlar"]
    else:
        programlar = kart
    if not isinstance(programlar, dict):
        return sonuc + [("HATA", "programlar.json", "programlar", "sözlük değil")]
    if kaynaklar is None:
        try:
            kaynaklar = json_oku(kok / "kaynaklar.json", {}) or {}
        except (OSError, ValueError):
            kaynaklar = {}
    projeler = proje_adlari(kok)
    for ad, p in sorted(programlar.items()):
        if sadece is not None and ad != sadece:
            continue
        try:
            sonuc += _kart_sema(ad, p, kok, kaynaklar, projeler, ev)
        except Exception as e:  # noqa: BLE001  bozuk kart denetimi düşürmez
            sonuc.append(("HATA", ad, "-", f"kart okunamadı ({type(e).__name__})"))
    return sonuc


def _kart_sema(ad, p, kok, kaynaklar, projeler, ev=None):
    s = []
    H = lambda alan, m: s.append(("HATA", ad, alan, m))  # noqa: E731
    U = lambda alan, m: s.append(("UYARI", ad, alan, m))  # noqa: E731
    if not isinstance(p, dict):
        H("-", "kart sözlük değil")
        return s
    taslak = _dolu(ad) or _dolu(p.get("ad"))

    def metin_ok(alan, v, zorunlu=True, sev=H):
        """Boş olmayan metin; '<DOLDUR>' ise sessiz geçer (doldurulmamış ayrıca bildirilir)."""
        if _dolu(v):
            return False
        if not isinstance(v, str) or not v.strip():
            if zorunlu:
                sev(alan, "boş olmayan metin olmalı")
            return False
        return True

    def liste_ok(alan, v, bos_olur=False, sev=H):
        if not isinstance(v, list):
            sev(alan, "liste olmalı")
            return False
        if not v and not bos_olur:
            sev(alan, "boş olmamalı")
            return False
        return True

    def enum_ok(alan, v, secenekler, sev=H):
        if _dolu(v):
            return False
        if v not in secenekler:
            sev(alan, f"geçersiz değer {v!r}; beklenen: {', '.join(secenekler)}")
            return False
        return True

    # genel: doldurulmamış, gizli değer, proje adı
    for yol, m in _kart_metinleri(p):
        if YER_TUTUCU in m:
            H(yol, "doldurulmamış")
        if _GIZLI.search(m):
            H(yol, "gizli değer gibi bir metin (değer yazdırılmıyor)")
        for pa in projeler:
            if re.search(r"(?<![\w])" + re.escape(pa) + r"(?![\w])", m):
                U(yol, "kütüphane kuralı 6: kartta proje adı olmamalı")
                break
    if p.get("ad") != ad and not _dolu(p.get("ad")):
        H("ad", f"kart anahtarı ({ad}) ile ad ({p.get('ad')!r}) aynı olmalı")
    for alan in ("repo", "tur", "lisans", "ne_yapar", "veri_yeri", "ag"):
        metin_ok(alan, p.get(alan))
    enum_ok("ucret", p.get("ucret"), UCRETLER)
    if not isinstance(p.get("kendini_gunceller"), bool):
        H("kendini_gunceller", "doğru/yanlış (bool) olmalı")
    liste_ok("skilleri", p.get("skilleri"), bos_olur=True)
    if "skill_koku" in p:
        sk = p["skill_koku"]
        if not isinstance(sk, str):
            H("skill_koku", "metin olmalı (boş metin = programın skili yok)")
        elif sk.strip() and not _dolu(sk):
            if not (os.path.isabs(sk) or sk.startswith("~/")):
                H("skill_koku", "mutlak yol ya da ~/ ile başlamalı")
            elif p.get("kopya", "kaynak") == "yerinde" and not yol_ac(sk, ev).is_dir():
                U("skill_koku", "bu bilgisayarda yok (program kurulu mu?)")
    if liste_ok("asla", p.get("asla")):
        pass
    if liste_ok("guncelleme_adimlari", p.get("guncelleme_adimlari")):
        if not any("program-denetim.py --oncesi" in str(x) for x in p["guncelleme_adimlari"]):
            H("guncelleme_adimlari", "'program-denetim.py --oncesi' adımı yok")

    # tür ve sürüm alanları
    kopya = p.get("kopya", "kaynak")
    yerinde = kopya == "yerinde"
    if kopya not in ("kaynak", "yerinde"):
        H("kopya", f"geçersiz değer {kopya!r}; beklenen: kaynak, yerinde")
    y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
    tur = y.get("tur")
    if yerinde:
        if not y:
            H("yerinde", "yerinde kartta 'yerinde' alanı olmalı")
        else:
            enum_ok("yerinde.tur", tur, YERINDE_TURLER)
            metin_ok("yerinde.yol", y.get("yol"))
            if tur == "npm-global":
                metin_ok("yerinde.paket", y.get("paket"))
                metin_ok("kutuphane_surumu", p.get("kutuphane_surumu"))
            elif tur == "git-checkout":
                metin_ok("yerinde.dal", y.get("dal"))
        if "kaynak_kopyasi" in p:
            H("kaynak_kopyasi", "yerinde kartta kaynak_kopyasi olmamalı")
        if tur == "npm-global":
            pass
        elif tur == "git-checkout" and not _dolu(p.get("kutuphane_commit")):
            if not _HEX40.fullmatch(str(p.get("kutuphane_commit", ""))):
                H("kutuphane_commit", "40 haneli tam sha olmalı")
    else:
        metin_ok("kutuphane_surumu", p.get("kutuphane_surumu"))
        kc = p.get("kutuphane_commit")
        if not _dolu(kc) and not _HEX40.fullmatch(str(kc or "")):
            H("kutuphane_commit", "40 haneli tam sha olmalı")
        kk = p.get("kaynak_kopyasi")
        if metin_ok("kaynak_kopyasi", kk) and not taslak:
            d = kok / str(kk)
            if not (d.is_dir() and any(d.iterdir())):
                H("kaynak_kopyasi", f"klasör yok ya da boş: {kk}")
    if ("venv" in p) != ("sabit_surumler" in p):
        H("venv", "venv ve sabit_surumler birlikte olmalı")
    if "sabit_surumler" in p and not isinstance(p["sabit_surumler"], dict):
        H("sabit_surumler", "sözlük olmalı")

    # KAYNAK.md ve kaynaklar.json tutarlılığı
    if not taslak:
        km = kok / "programlar" / ad / "KAYNAK.md"
        try:
            metin = km.read_text(encoding="utf-8")
        except OSError:
            metin = None
            H("KAYNAK.md", f"yok: programlar/{ad}/KAYNAK.md")
        if metin is not None:
            gerekli = [str(p[a]) for a in ("kutuphane_surumu", "kutuphane_commit") if isinstance(p.get(a), str) and p.get(a).strip() and not _dolu(p.get(a))]
            if not gerekli or any(g not in metin for g in gerekli):
                H("KAYNAK.md", "KAYNAK.md kartla uyuşmuyor (kayıtlı sürüm/commit metni bulunamadı)")
        repo = str(p.get("repo", "")).lower()
        kayit = None
        for k in (kaynaklar.get("repolar") or []):
            if k.get("program") == ad and (str(k.get("repo", "")).lower() == repo or repo in [str(e).lower() for e in (k.get("eski_adlar") or [])]):
                kayit = k
        if kayit is None and not _dolu(p.get("repo")):
            H("repo", "kaynaklar.json'da bu repo için program kaydı yok")

    # ---- çekirdek alanlar
    gy = p.get("giris_yolu")
    if gy is None:
        H("giris_yolu", "eksik (çekirdek alan)")
    elif not isinstance(gy, dict):
        H("giris_yolu", "sözlük olmalı")
    else:
        metin_ok("giris_yolu.kural", gy.get("kural"))

        def _giris(alan, g):
            if not isinstance(g, dict):
                H(alan, "sözlük olmalı")
                return
            enum_ok(f"{alan}.durum", g.get("durum"), GIRIS_DURUMLARI)
            if not isinstance(g.get("yol", ""), str):
                H(f"{alan}.yol", "metin olmalı")
            if not isinstance(g.get("nasil", ""), str) or ("nasil" not in g):
                H(f"{alan}.nasil", "metin olmalı")
        araclar = gy.get("araclar")
        if "hepsi" in gy:
            _giris("giris_yolu.hepsi", gy["hepsi"])
        elif isinstance(araclar, dict):
            for k in ARAC_ANAHTARLARI:
                if k not in araclar:
                    H("giris_yolu.araclar", f"araç eksik: {k} ('hepsi' de yok)")
        else:
            H("giris_yolu", "'hepsi' ya da 'araclar' olmalı")
        if isinstance(araclar, dict):
            for k, g in araclar.items():
                if k not in ARAC_ANAHTARLARI + ARAC_ISTEGE_BAGLI:
                    H(f"giris_yolu.araclar.{k}", "bilinmeyen araç anahtarı; beklenen: " + ", ".join(ARAC_ANAHTARLARI + ARAC_ISTEGE_BAGLI))
                else:
                    _giris(f"giris_yolu.araclar.{k}", g)
        elif araclar is not None:
            H("giris_yolu.araclar", "sözlük olmalı")

    ku = p.get("kurulum")
    if ku is None:
        H("kurulum", "eksik (çekirdek alan)")
    elif not isinstance(ku, dict):
        H("kurulum", "sözlük olmalı")
    else:
        liste_ok("kurulum.adimlar", ku.get("adimlar"))
        liste_ok("kurulum.dogrulama", ku.get("dogrulama"))

    ga = p.get("geri_alma")
    if ga is None:
        H("geri_alma", "eksik (çekirdek alan)")
    elif not isinstance(ga, dict):
        H("geri_alma", "sözlük olmalı")
    else:
        liste_ok("geri_alma.ne_zaman", ga.get("ne_zaman"))
        liste_ok("geri_alma.adimlar", ga.get("adimlar"))
        liste_ok("geri_alma.dogrulama", ga.get("dogrulama"), bos_olur=True)
        metin_ok("geri_alma.sinir", ga.get("sinir"))

    ci = p.get("cikarma")
    if ci is None:
        H("cikarma", "eksik (çekirdek alan)")
    elif not isinstance(ci, dict):
        H("cikarma", "sözlük olmalı")
    else:
        liste_ok("cikarma.makineden", ci.get("makineden"))
        liste_ok("cikarma.dokunulmaz", ci.get("dokunulmaz"), bos_olur=True)

    ye = p.get("yedek")
    if ye is None:
        if yerinde:
            H("yedek", "eksik (çekirdek alan)")
    elif not isinstance(ye, dict):
        H("yedek", "sözlük olmalı")
    else:
        metin_ok("yedek.kok", ye.get("kok"))
        tg = ye.get("tazelik_gun")
        if not isinstance(tg, int) or isinstance(tg, bool) or not 1 <= tg <= 30:
            H("yedek.tazelik_gun", "1-30 arası tam sayı olmalı")
        if liste_ok("yedek.zorunlu", ye.get("zorunlu")) and "KAYIT.json" not in ye["zorunlu"]:
            H("yedek.zorunlu", "'KAYIT.json' listede olmalı")
        liste_ok("yedek.yasak_adlar", ye.get("yasak_adlar"), bos_olur=True)

    oa = p.get("ortam_anahtarlari")
    if oa is None:
        H("ortam_anahtarlari", "eksik (çekirdek alan)")
    elif not isinstance(oa, list):
        H("ortam_anahtarlari", "liste olmalı")
    else:
        for i, e in enumerate(oa):
            al = f"ortam_anahtarlari[{i}]"
            if not isinstance(e, dict):
                H(al, "sözlük olmalı")
                continue
            metin_ok(f"{al}.ad", e.get("ad"))
            if not isinstance(e.get("gerekli"), bool):
                H(f"{al}.gerekli", "doğru/yanlış (bool) olmalı")
            if not isinstance(e.get("nerede"), list):
                H(f"{al}.nerede", "liste olmalı")

    # ---- isteğe bağlı alanlar: yok = sessiz; var ama geçersiz = UYARI
    if "disariya_yazar" in p:
        dy = p["disariya_yazar"]
        if not isinstance(dy, list):
            U("disariya_yazar", "liste olmalı")
        else:
            for i, e in enumerate(dy):
                al = f"disariya_yazar[{i}]"
                if not isinstance(e, dict) or not isinstance(e.get("yol"), str):
                    U(al, "yol içeren sözlük olmalı")
                    continue
                enum_ok(f"{al}.tur", e.get("tur"), DISARIYA_TURLER, sev=U)
                for b in ("yedeklenir", "dogrulandi"):
                    if not isinstance(e.get(b), bool):
                        U(f"{al}.{b}", "doğru/yanlış (bool) olmalı")
    if "gizli_dosyalar" in p:
        gd = p["gizli_dosyalar"]
        if not isinstance(gd, list) or not all(isinstance(x, str) for x in gd):
            U("gizli_dosyalar", "yol listesi olmalı")
    if "yerel_yamalar" in p:
        yy = p["yerel_yamalar"]
        if not isinstance(yy, dict) or not isinstance(yy.get("bilinen"), list):
            U("yerel_yamalar", "'bilinen' listesi olan sözlük olmalı")
        else:
            for i, e in enumerate(yy["bilinen"]):
                al = f"yerel_yamalar.bilinen[{i}]"
                if not isinstance(e, dict) or not isinstance(e.get("yol"), str):
                    U(al, "yol içeren sözlük olmalı")
                    continue
                enum_ok(f"{al}.tur", e.get("tur"), YAMA_TURLER, sev=U)
                enum_ok(f"{al}.yedek", e.get("yedek"), ("kopya", "liste"), sev=U)
    if "kirici_surum" in p:
        ks = p["kirici_surum"]
        if not isinstance(ks, dict):
            U("kirici_surum", "sözlük olmalı")
        else:
            if tur == "git-checkout":
                if not isinstance(ks.get("esik_commit"), int) or isinstance(ks.get("esik_commit"), bool):
                    U("kirici_surum.esik_commit", "tam sayı olmalı")
            else:
                enum_ok("kirici_surum.surum_hatti", ks.get("surum_hatti"), ("major", "minor"), sev=U)
            if "izle_dosyalar" in ks and not isinstance(ks["izle_dosyalar"], list):
                U("kirici_surum.izle_dosyalar", "liste olmalı")
    if "tedarik_dogrulama" in p:
        td = p["tedarik_dogrulama"]
        if not isinstance(td, dict) or not isinstance(td.get("ozet"), dict):
            U("tedarik_dogrulama", "'ozet' sözlüğü olan sözlük olmalı")
        else:
            oz = td["ozet"]
            if enum_ok("tedarik_dogrulama.ozet.tur", oz.get("tur"), OZET_TURLER, sev=U) and oz.get("tur") == "git-commit":
                dg = oz.get("deger", "")
                if not _dolu(dg):
                    if not _HEX40.fullmatch(str(dg)):
                        U("tedarik_dogrulama.ozet.deger", "git-commit için 40 haneli sha olmalı")
                    elif p.get("kutuphane_commit") and dg != p.get("kutuphane_commit"):
                        U("tedarik_dogrulama.ozet.deger", "kutuphane_commit ile aynı olmalı")
    return s


def sema_satiri(b):
    seviye, kart, alan, m = b
    return f"{seviye}: {kart}: {alan}: {m}"


# ============================================================ kart iskeleti

def iskelet(tur):
    """Yeni program için eksiksiz kart iskeleti; doldurulacak her değer '<DOLDUR>'."""
    D = YER_TUTUCU
    k = {
        "ad": D, "repo": D, "tur": D, "lisans": D, "ucret": D, "ne_yapar": D, "veri_yeri": D, "ag": D,
        "kendini_gunceller": False, "skilleri": [],
        "giris_yolu": {"kural": D, "kilavuz": "", "calistirma": "", "karar": "",
                       "hepsi": {"durum": D, "yol": "", "nasil": D}},
        "kurulum": {"adimlar": [D], "dogrulama": [D], "yapma": []},
        "guncelleme_adimlari": ["program-denetim.py --oncesi <program adı> çalıştırılır; 'HAZIR' demeden devam edilmez", D],
        "geri_alma": {"ne_zaman": [D], "adimlar": [D], "dogrulama": [D], "sinir": D},
        "cikarma": {"makineden": [D], "dokunulmaz": [D]},
        "yedek": {"kok": "~/Documents/Claude/yedek", "tazelik_gun": 3, "zorunlu": ["KAYIT.json"], "yasak_adlar": []},
        "ortam_anahtarlari": [],
        "asla": [D],
    }
    if tur == "kaynak":
        k.update({"kutuphane_surumu": D, "kutuphane_commit": D, "kaynak_kopyasi": D, "surum_kaynagi": D})
    elif tur == "npm-global":
        k.update({"kopya": "yerinde", "yerinde": {"tur": "npm-global", "yol": D, "paket": D},
                  "kutuphane_surumu": D, "surum_kaynagi": D})
    elif tur == "git-checkout":
        k.update({"kopya": "yerinde", "yerinde": {"tur": "git-checkout", "yol": D, "dal": "main"},
                  "kutuphane_commit": D, "surum_kaynagi": D})
    else:
        raise ValueError(f"bilinmeyen tür: {tur}")
    return k


# ============================================================ ön kontrol (--oncesi): salt okuma, hiçbir şey yazmaz

def _ctx(ev=None, kok=None, yedek_koku=None, cevrimdisi=False, bugun=None, environ=None, hedef=None, tedarik=False):
    ev = Path(ev) if ev is not None else Path.home()
    return types.SimpleNamespace(
        ev=ev, kok=Path(kok) if kok is not None else KOK,
        yedek_koku=Path(yedek_koku) if yedek_koku is not None else ev / "Documents" / "Claude" / "yedek",
        cevrimdisi=cevrimdisi, bugun=bugun or date.today(), environ=os.environ if environ is None else environ,
        hedef=hedef, tedarik=tedarik)


def _goster(yol, ctx):
    """Yolu kullanıcıya '~/...' biçiminde göster (gerçek ev klasörünü değil)."""
    s = str(yol)
    ev = str(ctx.ev)
    return "~" + s[len(ev):] if s.startswith(ev + os.sep) or s == ev else s


def yedek_kontrol(ad, p, ctx, kurulu):
    """Kontrol 1: yedek klasörü var mı, taze mi, KAYIT.json doğru mu, zorunlu içerik var mı, yasak dosya yok mu."""
    ye = p.get("yedek") if isinstance(p.get("yedek"), dict) else {}
    tazelik = ye.get("tazelik_gun") if isinstance(ye.get("tazelik_gun"), int) else 3
    zorunlu = [x for x in (ye.get("zorunlu") or ["KAYIT.json"]) if isinstance(x, str)]
    yasak = set(YASAK_ADLAR) | {x for x in (ye.get("yasak_adlar") or []) if isinstance(x, str)}
    kok = ctx.yedek_koku
    desen = re.compile(r"^" + re.escape(ad) + r"-(\d{4}-\d{2}-\d{2})(?:-(\d+))?$")
    adaylar = []
    try:
        for d in kok.iterdir():
            m = desen.match(d.name)
            if m and d.is_dir():
                adaylar.append((m.group(1), int(m.group(2) or 1), d))
    except OSError:
        pass
    S = []
    H = lambda m: S.append(("HATA", "yedek", m))  # noqa: E731
    if not adaylar:
        H(f"yedek yok: {_goster(kok, ctx)}/{ad}-<YYYY-AA-GG>/")
        return S
    tarih, _, klasor = max(adaylar)
    try:
        gun = (ctx.bugun - datetime.strptime(tarih, "%Y-%m-%d").date()).days
    except ValueError:
        gun = None
    if gun is None or gun > tazelik or gun < 0:
        H(f"yedek eski ({gun} gün; en çok {tazelik}): {klasor.name}")
    kayit = None
    try:
        kayit = json.loads((klasor / "KAYIT.json").read_text(encoding="utf-8"))
        if not isinstance(kayit, dict):
            raise ValueError("sözlük değil")
    except (OSError, ValueError):
        H("KAYIT.json yok ya da geçersiz")
        kayit = None
    if kayit is not None:
        if kayit.get("tarih") != tarih:
            H(f"KAYIT.json tarihi klasör tarihiyle aynı değil ({kayit.get('tarih')!r} / {tarih})")
        onceki = kayit.get("onceki") if isinstance(kayit.get("onceki"), dict) else {}
        y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
        git = y.get("tur") == "git-checkout"
        yedek_deger = onceki.get("commit" if git else "surum")
        ok = bool(kurulu) and bool(yedek_deger) and (sha_esit(yedek_deger, kurulu) if git else ham_surum(yedek_deger) == ham_surum(kurulu))
        if kurulu and not ok:
            H("yedek başka sürümün (kurulu değil)")
    for z in zorunlu:
        yol = klasor / z
        if z == "KAYIT.json":
            continue
        if yol.is_dir():
            try:
                bos = not any(yol.iterdir())
            except OSError:
                bos = True
            if bos:
                H(f"yedekte yok: {z} (klasör boş)")
        elif not yol.exists():
            H(f"yedekte yok: {z}")
    sayac = 0
    for kk, dizinler, dosyalar in os.walk(klasor):
        for n in list(dizinler) + list(dosyalar):
            sayac += 1
            if n in yasak:
                H(f"yedekte gizli dosya var: {os.path.relpath(os.path.join(kk, n), klasor)}")
        if sayac > 50000:
            break
    if not any(x[0] == "HATA" for x in S):
        S.append(("TAMAM", "yedek", f"yedek geçerli: {klasor.name} ({gun} gün önce)"))
    return S


def _ortam_dosyada(yol, ad):
    """(tanımlı mı, değer ya da None, okunamadı mı). Satırlar yazdırılmaz."""
    try:
        metin = Path(yol).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return False, None, False
    except OSError:
        return False, None, True
    if str(yol).endswith("settings.json"):
        try:
            d = json.loads(metin)
        except ValueError:
            return False, None, True
        env = d.get("env") if isinstance(d, dict) else None
        if isinstance(env, dict) and ad in env:
            return True, str(env[ad]), False
        return False, None, False
    bulunan = None
    for satir in metin.splitlines():
        t = satir.strip()
        if t.startswith("#"):
            continue
        m = re.match(r"(?:export\s+)?" + re.escape(ad) + r"=(.*)$", t)
        if m:
            bulunan = m.group(1).split("#")[0].strip().strip("'\"")
    return (bulunan is not None), bulunan, False


def ortam_say(p, ctx):
    """Karttaki her ortam anahtarı için {ad, say, toplam, eksik, farkli, okunamayan, surecte, gerekli, beklenen}."""
    sonuc = []
    for e in (p.get("ortam_anahtarlari") if isinstance(p.get("ortam_anahtarlari"), list) else []):
        if not isinstance(e, dict) or not isinstance(e.get("ad"), str):
            continue
        ad, beklenen = e["ad"], e.get("beklenen")
        nerede = [x for x in (e.get("nerede") or []) if isinstance(x, str)]
        say, eksik, okunamayan, farkli = 0, [], [], False
        for yol in nerede:
            tanimli, deger, okunamadi = _ortam_dosyada(yol_ac(yol, ctx.ev), ad)
            if okunamadi:
                okunamayan.append(yol)
            if tanimli:
                say += 1
                if beklenen not in (None, "") and deger != str(beklenen):
                    farkli = True
            else:
                eksik.append(yol)
        surecte = ad in ctx.environ
        if surecte and beklenen not in (None, "") and ctx.environ.get(ad) != str(beklenen):
            farkli = True
        sonuc.append({"ad": ad, "say": say, "toplam": len(nerede), "eksik": eksik, "farkli": farkli, "okunamayan": okunamayan,
                      "surecte": surecte, "gerekli": bool(e.get("gerekli")), "beklenen": beklenen})
    return sonuc


def ortam_kontrol(p, ctx):
    """Kontrol 3: ortam anahtarları. Değerler asla yazdırılmaz."""
    S = []
    ol = ortam_say(p, ctx)
    if not ol:
        return [("ATLANDI", "ortam", "kartta ortam anahtarı yok")]
    for o in ol:
        ad = o["ad"]
        for yol in o["okunamayan"]:
            S.append(("UYARI", "ortam", f"{yol}: okunamadı"))
        if o["toplam"] == 0:
            durum_s = "süreç ortamında tanımlı" if o["surecte"] else "tanımlı değil"
            tam = o["surecte"]
            sev = "TAMAM" if tam else ("HATA" if o["gerekli"] else "BİLGİ")
            S.append((sev, "ortam", f"{ad}: {durum_s}" + ("" if tam or o["gerekli"] else " (isteğe bağlı)")))
        elif o["say"] == o["toplam"]:
            S.append(("TAMAM", "ortam", f"{ad}: {o['say']}/{o['toplam']} yerde tanımlı"))
        elif o["say"] == 0 and not o["surecte"]:
            S.append(("HATA" if o["gerekli"] else "BİLGİ", "ortam",
                      f"{ad}: hiçbir yerde tanımlı değil" + ("" if o["gerekli"] else " (isteğe bağlı)")))
        elif o["say"] == 0:
            S.append(("UYARI" if o["gerekli"] else "BİLGİ", "ortam", f"{ad}: yalnız süreç ortamında tanımlı (kalıcı bir yerde değil)"))
        else:
            S.append(("UYARI" if o["gerekli"] else "BİLGİ", "ortam", f"{ad}: {o['say']}/{o['toplam']} yerde tanımlı (eksik: {', '.join(o['eksik'])})"))
        if o["farkli"]:
            S.append(("UYARI", "ortam", f"{ad}: değer beklenenden farklı"))
    return S


def _porcelain_yol(satir):
    """'XY yol' / 'R  eski -> yeni' / tırnaklı yol -> değişen yol (yeni ad)."""
    govde = satir[3:] if len(satir) > 3 else ""
    if satir[:1] in ("R", "C") or (len(satir) > 1 and satir[1:2] in ("R", "C")):
        if " -> " in govde:
            govde = govde.split(" -> ")[-1]
    govde = govde.strip()
    if len(govde) >= 2 and govde.startswith('"') and govde.endswith('"'):
        govde = govde[1:-1]
        govde = re.sub(r'\\(["\\])', r"\1", govde).replace("\\t", "\t").replace("\\n", "\n")
        if re.search(r"\\[0-3][0-7]{2}", govde):
            try:
                govde = re.sub(r"(?:\\[0-3][0-7]{2})+", lambda m: bytes(int(x, 8) for x in re.findall(r"\\([0-3][0-7]{2})", m.group(0))).decode("utf-8", "replace"), govde)
            except ValueError:
                pass
    return govde


def _yama_esles(yol, bilinen):
    for b in bilinen:
        by = b.get("yol") if isinstance(b, dict) else None
        if isinstance(by, str) and (yol == by or (by.endswith("/") and yol.startswith(by)) or (by.endswith("/") and yol + "/" == by)):
            return b
    return None


def yama_kontrol(p, porcelain_metin):
    """Kontrol 4 (git kartı): 'git status --porcelain' çıktısındaki her değişiklik karttaki yerel_yamalar.bilinen listesinde mi?
    porcelain_metin None ise (status okunamadı) HATA."""
    if porcelain_metin is None:
        return [("HATA", "yerel değişiklik", "git status okunamadı; yerel değişiklikler doğrulanamıyor")]
    yy = p.get("yerel_yamalar") if isinstance(p.get("yerel_yamalar"), dict) else {}
    bilinen = [b for b in (yy.get("bilinen") or []) if isinstance(b, dict) and b.get("tur") != "venv"]
    degisen = []
    izl = 0
    for satir in porcelain_metin.splitlines():
        if not satir.strip() or satir.startswith("!!"):
            continue
        if satir.startswith("??"):
            izl += 1
        degisen.append(_porcelain_yol(satir))
    S = []
    kayitsiz = [y for y in degisen if _yama_esles(y, bilinen) is None]
    for y in kayitsiz[:20]:
        S.append(("HATA", "yerel değişiklik", f"kayıtsız yerel değişiklik: {y}"))
    if len(kayitsiz) > 20:
        S.append(("HATA", "yerel değişiklik", f"… ve {len(kayitsiz) - 20} tane daha"))
    if not kayitsiz:
        S.append(("TAMAM", "yerel değişiklik", f"{len(degisen) - izl} değişen, {izl} izlenmeyen; hepsi kartta kayıtlı"))
    for b in bilinen:
        if b.get("tur") in ("izlenen", "izlenmeyen") and not any(_yama_esles(y, [b]) for y in degisen):
            S.append(("BİLGİ", "yerel değişiklik", f"kayıtlı ama değişmemiş: {b['yol']} (yama upstream'e girmiş ya da kaybolmuş olabilir)"))
    return S


def giris_kontrol(p, ctx):
    """Kontrol 6: giriş yolu satırları (yol var mı; karar bekleyen var mı)."""
    gy = p.get("giris_yolu")
    if not isinstance(gy, dict):
        return [("ATLANDI", "giriş yolu", "kartta giriş yolu yok")]
    S = []
    kil = gy.get("kilavuz")
    if isinstance(kil, str) and kil.strip() and not os.path.lexists(yol_ac(kil, ctx.ev)):
        S.append(("UYARI", "giriş yolu", f"kılavuz yok: {kil}"))
    girisler = [("hepsi", gy["hepsi"])] if isinstance(gy.get("hepsi"), dict) else []
    if isinstance(gy.get("araclar"), dict):
        girisler += [(k, v) for k, v in gy["araclar"].items() if isinstance(v, dict)]
    for ac, g in girisler:
        d, yol = g.get("durum"), g.get("yol") or ""
        if d == "karar-bekliyor":
            S.append(("BİLGİ", "giriş yolu", f"{ac}: kullanıcı kararı bekliyor"))
        elif d in ("yerinde", "program-klasoru", "proje-skili") and yol:
            if os.path.lexists(yol_ac(yol, ctx.ev)):
                S.append(("BİLGİ", "giriş yolu", f"{ac}: {d} ({yol} var)"))
            else:
                S.append(("UYARI", "giriş yolu", f"giriş yolu kırık: {ac}: {yol}"))
        else:
            S.append(("BİLGİ", "giriş yolu", f"{ac}: {d}"))
    return S or [("ATLANDI", "giriş yolu", "kartta araç satırı yok")]


def gizli_kontrol(p, ctx):
    """Kontrol 7: anahtar/kimlik dosyaları: yalnız var/yok (os.path.lexists); dosya ASLA açılmaz."""
    gd = p.get("gizli_dosyalar")
    if not isinstance(gd, list):
        return [("BİLGİ", "gizli", "kayıtsız")]
    S = []
    for yol in gd:
        if isinstance(yol, str):
            S.append(("BİLGİ", "gizli", f"anahtar/kimlik dosyası var (açılmaz): {yol}") if os.path.lexists(yol_ac(yol, ctx.ev))
                     else ("UYARI", "gizli", f"yok: {yol}"))
    return S or [("BİLGİ", "gizli", "kayıtlı gizli dosya yok")]


def kirici_adayi(p, kurulu, hedef, geride=None, dosyalar=None):
    """Kırıcı sürüm adayı nedenleri (liste; boşsa aday değil). Salt sayı/yol kuralı; ağ çağırmaz."""
    ks = p.get("kirici_surum") if isinstance(p.get("kirici_surum"), dict) else {}
    nedenler = []
    y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
    if y.get("tur") == "git-checkout":
        esik = ks.get("esik_commit")
        if isinstance(esik, int) and isinstance(geride, int) and geride > esik:
            nedenler.append(f"{geride} commit ileride (eşik {esik})")
        dos = set(dosyalar or [])
        for f in ks.get("izle_dosyalar") or []:
            if f in dos:
                nedenler.append(f"yeni commit'ler izlenen dosyayı değiştiriyor: {f}")
        yy = p.get("yerel_yamalar") if isinstance(p.get("yerel_yamalar"), dict) else {}
        for b in yy.get("bilinen") or []:
            if isinstance(b, dict) and b.get("tur") == "izlenen" and b.get("yol") in dos:
                nedenler.append(f"yeni commit'ler yamalı dosyaya da dokunuyor: {b['yol']}")
        return nedenler
    hat = ks.get("surum_hatti")
    a, b = surum_ayikla(kurulu), surum_ayikla(hedef)
    if hat in ("major", "minor") and a and b:
        a2, b2 = (a + (0, 0, 0))[:2], (b + (0, 0, 0))[:2]
        if hat == "major" and b2[0] > a2[0]:
            nedenler.append(f"major sürüm değişiyor ({kurulu} -> {hedef})")
        elif hat == "minor" and (b2[0] > a2[0] or (b2[0] == a2[0] and b2[1] > a2[1])):
            nedenler.append(f"minor/major sürüm değişiyor ({kurulu} -> {hedef})")
    return nedenler


def _durum_baslik(ad, tur, kart, kurulu, son):
    return (f"Program ön kontrolü: {ad} ({tur}) · karttaki {kisa(kart, tur)} · kurulu {kisa(kurulu, tur) if kurulu else '-'}"
            f" · son {kisa(son, tur) if son else '?'}")


# ============================================================ programla gelen skiller: projelerdeki bağlar (K-28)

_BAG_AD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")
_HEDEF_SHA = re.compile(r"[0-9a-fA-F]{7,40}")
_PK = [None]  # proje-kullanimi.py modülü (tembel; yüklenemezse bağ bilgisi yok sayılır)


def _proje_kullanimi():
    if _PK[0] is None:
        import importlib.util
        yol = Path(__file__).with_name("proje-kullanimi.py")
        spec = importlib.util.spec_from_file_location("_pd_proje_kullanimi", yol)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _PK[0] = m
    return _PK[0]


def dis_bag_kayitlari(kilit):
    """Kilitteki 'dis_skiller' içinden yalnız geçerli program bağları: {ad: kayıt}. Anahtar ad kuralına uymalı ve kaydın
    'ad'ı anahtarla aynı olmalı; kilitten gelen hiçbir değer yol olarak kullanılmaz (hedef karttan türetilir)."""
    d = kilit.get("dis_skiller") if isinstance(kilit, dict) else None
    sonuc = {}
    if not isinstance(d, dict):
        return sonuc
    for k, g in d.items():
        if (isinstance(k, str) and _BAG_AD.fullmatch(k) and isinstance(g, dict) and g.get("ad") == k
                and g.get("tur") == "program-bag" and isinstance(g.get("program"), str)):
            sonuc[k] = g
    return sonuc


def proje_baglari(ctx):
    """Kayıtlı projelerdeki program bağları: [{'proje','skill','program','surum','tur_surum'}]. Okuma yalnız: ctx.kok/projeler.json
    ve her projenin .skill-kutuphanesi/kilit.json dosyası. Dosya yok/bozuksa boş (hata vermez). Çağrı başına bir kez hesaplanır."""
    onbellek = getattr(ctx, "_baglar", None)
    if onbellek is not None:
        return onbellek
    sonuc = []
    try:
        ayar = json_oku(Path(ctx.kok) / "projeler.json", None)
        if isinstance(ayar, dict):
            pk = _proje_kullanimi()
            for yol in pk.projeleri_bul(ayar):
                try:
                    kilit = json_oku(Path(yol) / ".skill-kutuphanesi" / "kilit.json", {}) or {}
                except (OSError, ValueError):
                    continue
                for ad, g in sorted(dis_bag_kayitlari(kilit).items()):
                    sonuc.append({"proje": Path(yol).name, "skill": ad, "program": g["program"],
                                  "surum": g.get("program_surum") if isinstance(g.get("program_surum"), str) else None,
                                  "tur_surum": g.get("program_surum_turu") if isinstance(g.get("program_surum_turu"), str) else None})
    except Exception:  # noqa: BLE001  bağ bilgisi okunamazsa denetim düşmez, satır eklenmez
        sonuc = []
    try:
        ctx._baglar = sonuc
    except AttributeError:
        pass
    return sonuc


def bag_hedefi(p, ctx, skill):
    """Bağın şimdiki hedefi: kartın skill_koku/ad yolu (kilitteki 'hedef' kullanılmaz); kartta skill_koku yoksa None."""
    sk = p.get("skill_koku") if isinstance(p, dict) else None
    if not isinstance(sk, str) or not sk.strip() or _dolu(sk) or not _BAG_AD.fullmatch(skill):
        return None
    return os.path.join(os.path.abspath(str(yol_ac(sk, ctx.ev))), skill)


def bag_hedef_var(hedef):
    return bool(hedef) and os.path.isfile(os.path.join(hedef, "SKILL.md"))


def program_baglari(ad, p, ctx):
    """Bu programın bağları: [(bağ kaydı, hedef yol, hedef var mı)]. Kartta skill_koku yoksa hedef None (var=False)."""
    sonuc = []
    for b in proje_baglari(ctx):
        if b["program"] != ad:
            continue
        h = bag_hedefi(p, ctx, b["skill"])
        sonuc.append((b, h, bag_hedef_var(h)))
    return sonuc


def _bag_ozet(liste):
    projeler = sorted({b["proje"] for b, _, _ in liste})
    skiller = sorted({b["skill"] for b, _, _ in liste})
    ek = f" +{len(skiller) - 8}" if len(skiller) > 8 else ""
    return f"projeler: {', '.join(projeler)}; skiller: {', '.join(skiller[:8])}{ek}"


def bag_simdi(ad, p, ctx, seviye):
    """'bağlar' satırları (şimdiki durum). Bağ yoksa boş. Kırık bağ yalnız 'seviye' ile bildirilir: güncelleme bekleyen ya da
    program kurulu olmayan durumda UYARI, güncellenecek bir şey yokken (güncellemeden sonraki görünüm) HATA.
    Bu satırlar yalnız güncelleme DIŞI durumda HATA olabilir; ana yolda hiçbir zaman HAZIR DEĞİL sebebi olmaz."""
    liste = program_baglari(ad, p, ctx)
    if not liste:
        return []
    kirik = [(b, h) for b, h, var in liste if not var]
    if not kirik:
        return [("TAMAM", "bağlar", f"{len(liste)} bağ, hepsi çözülüyor ({_bag_ozet(liste)})")]
    ipucu = " (program kurulu değilse ya da güncelleme bekleniyorsa: kurulum/güncelleme sonrası bu raporu yeniden çalıştır; sonra skill-ekle.py <proje> --yenile ya da --kaldir <ad>)"
    S = []
    for b, h in kirik[:10]:
        goster = _goster(h, ctx) if h else "kartta skill_koku yok"
        S.append((seviye, "bağlar", f"{b['proje']}: {b['skill']} bağı kırık (hedef yok: {goster})"))
    if len(kirik) > 10:
        S.append((seviye, "bağlar", f"…+{len(kirik) - 10} kırık bağ daha"))
    S.append(("BİLGİ", "bağlar", f"{len(liste)} bağın {len(kirik)} tanesi kırık{ipucu}"))
    return S


def bag_kirilacak(ad, p, ctx, hedef_g, kurulu, git, y):
    """Güncelleme bekleyen ana yolda: hedef sürümde bağların hedefi var mı (salt okuma; ağ yok, fetch yok)."""
    liste = program_baglari(ad, p, ctx)
    if not liste or not hedef_g or hedef_g == kurulu:
        return []
    if not git:
        return [("BİLGİ", "bağlar", "paket indirilmeden hedef sürümdeki skill klasörleri bilinemez; güncellemeden sonra bu raporu yeniden çalıştır: kırık bağ HATA görünür")]
    if not _HEDEF_SHA.fullmatch(str(hedef_g)):
        return [("BİLGİ", "bağlar", "hedef bir commit sha'sı değil; bağların kırılıp kırılmayacağı denetlenmedi")]
    yol = yol_ac(y.get("yol", ""), ctx.ev)
    if git_okuma(yol, "cat-file", "-e", f"{hedef_g}^{{commit}}") is None:
        return [("BİLGİ", "bağlar", "hedef commit yerel depoda yok (git fetch yapılmaz); bağların kırılıp kırılmayacağı bilinmiyor")]
    sk = p.get("skill_koku")
    goreli = os.path.relpath(os.path.abspath(str(yol_ac(sk, ctx.ev))), os.path.abspath(str(yol))) if isinstance(sk, str) and sk.strip() else ".."
    if goreli == ".." or goreli.startswith(".." + os.sep):
        return [("BİLGİ", "bağlar", "skill_koku depo dışında; bağ kırılacak mı bilinmiyor")]
    goreli = goreli.replace(os.sep, "/")
    S, tamam = [], 0
    for b, _, _ in liste:
        klasor = ("" if goreli == "." else goreli + "/") + b["skill"]
        if git_okuma(yol, "cat-file", "-e", f"{hedef_g}:{klasor}/SKILL.md") is None:
            S.append(("UYARI", "bağlar", f"bağ kırılacak: {b['proje']}: {b['skill']} ({hedef_g[:8]} sürümünde {klasor} yok)"))
        else:
            tamam += 1
    if tamam:
        S.append(("TAMAM", "bağlar", f"{tamam} bağın hedefi {hedef_g[:8]} sürümünde de var"))
    return S


def oncesi_denetle(ad, p, ctx):
    """Güncellemeden önce salt okuma ön kontrol. Döner: (satırlar, sonuç); satır = (seviye, kontrol, metin);
    seviye TAMAM|BİLGİ|UYARI|HATA|ATLANDI|BAŞLIK. sonuç: HAZIR | HAZIR DEĞİL | GÜNCELLENECEK BİR ŞEY YOK | KURULU DEĞİL.
    Hiçbir şey yazmaz, indirmez, program/npm/pip çalıştırmaz."""
    S = []
    y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
    yerinde = p.get("kopya", "kaynak") == "yerinde"
    tur = y.get("tur") if yerinde else "kaynak"
    git = tur == "git-checkout"
    kart_surum = p.get("kutuphane_commit") if git else p.get("kutuphane_surumu")
    # --- S1 şema
    try:
        bulgu = sema_denetle({ad: p}, kok=ctx.kok, ev=ctx.ev)
    except Exception as e:  # noqa: BLE001
        bulgu = [("HATA", ad, "-", f"kart okunamadı ({type(e).__name__})")]
    # --- S2 kurulu
    kurulu, git_say = None, (0, 0)
    if tur == "npm-global":
        kurulu = npm_kurulu_surum(y.get("yol", ""))
    elif git:
        kurulu, d_, i_ = git_kurulu(yol_ac(y.get("yol", ""), ctx.ev))
    else:
        kk = ctx.kok / str(p.get("kaynak_kopyasi", ""))
        kurulu = p.get("kutuphane_surumu") if p.get("kaynak_kopyasi") and kk.is_dir() and any(kk.iterdir()) else None
    # --- S4 son
    son, geride, son_hata = None, None, None
    hedef = ctx.hedef
    if kurulu and not ctx.cevrimdisi and not hedef:
        if tur == "npm-global":
            son = npm_son_surum(y.get("paket", ""))
            son_hata = _SON_HATA.get(("npm", y.get("paket", "")))
        elif git:
            son, geride = git_son(p.get("repo", ""), y.get("dal", "main"), kurulu)
            son_hata = _SON_HATA.get(("git", p.get("repo")))
        else:
            try:
                son = gh_api(f"repos/{p['repo']}/releases/latest")["tag_name"]
            except GhBulunamadi:
                son_hata = "404"
            except Exception as e:  # noqa: BLE001
                son_hata = "kapali" if _kapali(e) else "ag"
    hedef_g = hedef or son
    S.append(("BAŞLIK", "", _durum_baslik(ad, tur, kart_surum, kurulu, hedef_g)))
    if any(b[0] == "HATA" for b in bulgu):
        S.append(("HATA", "şema", "çekirdek alanlarda hata: " + "; ".join(f"{b[2]}: {b[3]}" for b in bulgu if b[0] == "HATA")[:300] + " (program-denetim.py --sema)"))
    else:
        S.append(("TAMAM", "şema", "çekirdek alanlar geçerli"))
        ik = sum(1 for b in bulgu if b[0] == "UYARI")
        if ik:
            S.append(("UYARI", "şema", f"isteğe bağlı alanlarda {ik} uyarı (program-denetim.py --sema)"))
    if not kurulu:
        S.append(("BİLGİ", "kurulu", "bu bilgisayarda kurulu değil; kurulum için kartın 'kurulum' alanına bakın"))
        S += bag_simdi(ad, p, ctx, "UYARI")  # kurulu değilken bağlar zaten kırık görünür: HAZIR DEĞİL sebebi olmaz
        return S, "KURULU DEĞİL"
    S.append(("TAMAM", "kurulu", f"kurulu {kisa(kurulu, tur)}"))
    # --- S3 kart
    if tur != "kaynak":
        if yerinde_durum(tur, kart_surum, kurulu, None) == "KART ESKİ":
            S.append(("HATA", "kart", f"kurulu {kisa(kurulu, tur)} karttan farklı: sebebi bulunmadan güncelleme yapılmaz"))
        else:
            S.append(("TAMAM", "kart", "kurulu sürüm karttakiyle aynı"))
    # --- S4 sonuç değerlendirme
    if ctx.cevrimdisi:
        S.append(("ATLANDI", "son", "atlandı: çevrimdışı" + (f" (hedef {hedef})" if hedef else "")))
    elif hedef:
        esit = sha_esit(hedef, kurulu) if git else ham_surum(hedef) == ham_surum(kurulu)
        if esit:
            S.append(("BİLGİ", "son", f"hedef {kisa(hedef, tur)} zaten kurulu"))
            S += bag_simdi(ad, p, ctx, "HATA")
            return S, "GÜNCELLENECEK BİR ŞEY YOK"
        S.append(("BİLGİ", "son", f"{kisa(kurulu, tur)} -> {kisa(hedef, tur)} (hedef elle verildi)"))
    elif not son:
        S.append(("HATA", "son", f"son sürüm bilinmiyor ({son_hata or 'ağ'})"))
    else:
        if git:
            guncel = sha_esit(kurulu, son) or geride == 0
        else:
            u, s_ = surum_ayikla(kurulu), surum_ayikla(son)
            guncel = bool(u and s_ and u >= s_)
        if guncel:
            S.append(("BİLGİ", "son", f"kurulu sürüm son sürüm ({kisa(son, tur)})"))
            S += bag_simdi(ad, p, ctx, "HATA")
            return S, "GÜNCELLENECEK BİR ŞEY YOK"
        S.append(("BİLGİ", "son", f"{kisa(kurulu, tur)} -> {kisa(son, tur)}" + (f" ({geride} geride)" if geride else "") + " (YENİ SÜRÜM VAR)"))
    # --- 8 ana kontrol
    S += bag_simdi(ad, p, ctx, "UYARI")  # güncelleme bekleniyor: kırık bağ UYARI (sonraki görünüm HATA)
    S += yedek_kontrol(ad, p, ctx, kurulu)
    # 2. sabit sürümler
    sabit = p.get("sabit_surumler")
    if isinstance(sabit, dict) and sabit:
        vy = yol_ac(y.get("yol", ""), ctx.ev) / str(p.get("venv", ".venv"))
        if not vy.is_dir():
            S.append(("HATA", "sabit sürümler", "venv yok"))
        else:
            uyan, farklar = pin_karsilastir(sabit, dist_info_oku(vy))
            if farklar:
                for f in farklar:
                    S.append(("HATA", "sabit sürümler", f"sabit sürüm farkı: {f}; düzeltmeden devam edilmez"))
            else:
                S.append(("TAMAM", "sabit sürümler", f"{uyan}/{len(sabit)} tutuyor"))
    else:
        S.append(("ATLANDI", "sabit sürümler", "kartta venv yok"))
    S += ortam_kontrol(p, ctx)
    # 4. yama
    if git:
        st = git_okuma(yol_ac(y.get("yol", ""), ctx.ev), "status", "--porcelain")
        S += yama_kontrol(p, st)
        dal = y.get("dal", "main")
        sym = git_okuma(yol_ac(y.get("yol", ""), ctx.ev), "rev-parse", "--abbrev-ref", "HEAD")
        if sym is not None and sym.strip() and sym.strip() != dal:
            S.append(("UYARI", "yerel değişiklik", f"HEAD '{dal}' dalında değil ('{sym.strip()}': ayrık ya da başka dal)"))
    else:
        S.append(("ATLANDI", "yerel değişiklik", "git klonu değil" if tur != "kaynak" else "kaynak kopyalı kart: git klonu yok"))
    # 5. repo
    if ctx.cevrimdisi:
        S.append(("ATLANDI", "repo", "atlandı: çevrimdışı"))
    else:
        rd, yeni = repo_durumu(p.get("repo", ""))
        if rd == "var":
            S.append(("TAMAM", "repo", f"{p.get('repo')} erişilebilir"))
        elif rd == "kayıp":
            S.append(("HATA", "repo", f"{p.get('repo')} GitHub'da bulunamadı (404): kayıp"))
        elif rd == "taşınmış":
            S.append(("UYARI", "repo", f"kart repo adı eski: yeni ad {yeni} (kaynaklar.json eski_adlar'a bakın)"))
        else:
            S.append(("UYARI", "repo", f"repo durumu öğrenilemedi ({'API kapalı' if rd == 'kapalı' else 'ağ'})"))
    ka = kart_eski_ad(p)
    if ka:
        S.append(("UYARI", "repo", f"kart eski repo adını taşıyor; güncel ad: {ka}"))
    if git:
        od = origin_durumu(y.get("yol", ""), p, ctx.ev)
        if od == "eski-ad":
            S.append(("BİLGİ", "repo", "origin adresi eski adı gösteriyor (GitHub yönlendirir; değiştirmek kullanıcı onayı ister)"))
        elif od == "farklı":
            S.append(("UYARI", "repo", "origin adresi kartın reposundan farklı"))
    S += giris_kontrol(p, ctx)
    S += gizli_kontrol(p, ctx)
    S += bag_kirilacak(ad, p, ctx, hedef_g, kurulu, git, y)
    # 8. kırıcı (+ çakışma)
    ks = p.get("kirici_surum") if isinstance(p.get("kirici_surum"), dict) else None
    dosyalar, kesik, g2 = None, False, geride
    if git and not ctx.cevrimdisi and hedef_g:
        try:
            g2, dosyalar, kesik = git_karsilastir(p.get("repo", ""), kurulu, hedef_g if hedef else y.get("dal", "main"))
        except Exception as e:  # noqa: BLE001
            S.append(("UYARI", "kırıcı", f"commit karşılaştırması alınamadı ({'404' if isinstance(e, GhBulunamadi) else 'ağ'}); çakışma bilinmiyor"))
    if ks is None:
        S.append(("BİLGİ", "kırıcı", "kayıtsız, kırıcı adayı denetlenmedi"))
    if git or ks is not None:
        nedenler = kirici_adayi(p, kurulu, hedef_g, g2, dosyalar) if ks is not None or git else []
        if ks is None:  # kayıtsız kartta yalnız yama çakışması bakılır
            nedenler = [n for n in nedenler if "yamalı" in n]
        deneme = (ks or {}).get("deneme_klasoru", "<deneme klasörü>")
        yamali = [n for n in nedenler if n.startswith("yeni commit'ler yamalı")]
        asil = [n for n in nedenler if n not in yamali]
        if asil:
            S.append(("UYARI", "kırıcı", f"KIRICI ADAYI: {'; '.join(asil)}; önce rehber/11 → 'Kırıcı sürüm' deneme adımları ayrı klasörde ({deneme}) uygulanır"))
        for n in yamali:
            S.append(("UYARI", "kırıcı", n))
        if kesik:
            S.append(("UYARI", "kırıcı", "dosya listesi 300'de kesildi; çakışma tam bilinmiyor"))
        if ks is not None and not nedenler:
            S.append(("BİLGİ", "kırıcı", f"kırıcı adayı değil ({kisa(kurulu, tur)} -> {kisa(hedef_g, tur)})" if hedef_g
                      else "hedef sürüm bilinmiyor (çevrimdışı ya da --hedef yok): kırıcı adayı denetlenemedi"))
        gb = ks.get("deneme_disk_gb") if ks else None
        if nedenler and isinstance(gb, (int, float)):
            try:
                bos = shutil.disk_usage(str(ctx.ev)).free / 1e9
                if bos < gb:
                    S.append(("UYARI", "kırıcı", f"deneme için yer az: boş {bos:.1f} GB, gerekli {gb} GB"))
            except OSError:
                pass
    # --tedarik
    if ctx.tedarik:
        S += tedarik_kontrol(p, ctx, kurulu, hedef_g)
    engel = sum(1 for x in S if x[0] == "HATA")
    return S, ("HAZIR DEĞİL" if engel else "HAZIR")


def tedarik_kontrol(p, ctx, kurulu, hedef):
    td = p.get("tedarik_dogrulama") if isinstance(p.get("tedarik_dogrulama"), dict) else {}
    S = []
    yay = td.get("yayinci") if isinstance(td.get("yayinci"), dict) else {}
    if yay.get("ucuncu_taraf") and yay.get("imza") == "yok":
        S.append(("UYARI", "tedarik", "üçüncü taraf, imzasız: kaynaktan kurulum tercih edilir"))
    oz = td.get("ozet") if isinstance(td.get("ozet"), dict) else {}
    if oz.get("tur") == "npm-integrity":
        if not oz.get("deger"):
            S.append(("BİLGİ", "tedarik", "integrity kayıtsız"))
        elif ctx.cevrimdisi:
            S.append(("ATLANDI", "tedarik", "atlandı: çevrimdışı"))
        else:
            y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
            canli = npm_integrity(y.get("paket", ""), hedef or kurulu)
            if canli is None:
                S.append(("UYARI", "tedarik", "registry integrity alınamadı"))
            elif canli == oz["deger"]:
                S.append(("TAMAM", "tedarik", "registry integrity kayıtla aynı"))
            else:
                S.append(("HATA", "tedarik", "registry integrity kayıttan farklı"))
    return S


def oncesi_yaz(ad, S, sonuc):
    """Ön kontrol çıktısını metin satırlarına çevir."""
    cikti = []
    for sev, kont, metin in S:
        cikti.append(metin if sev == "BAŞLIK" else f"{sev:<7} {kont:<16} {metin}")
    engel = sum(1 for x in S if x[0] == "HATA")
    ek = {"HAZIR": "", "HAZIR DEĞİL": f" ({engel} engel)", "GÜNCELLENECEK BİR ŞEY YOK": " (kurulu sürüm son sürüm)",
          "KURULU DEĞİL": " (bu bilgisayarda yok; kurulum için kartın 'kurulum' alanına bakın)"}[sonuc]
    cikti.append(f"SONUÇ: {sonuc}{ek}")
    cikti.append("Bu araç yalnız okur. Güncelleme için kullanıcıdan bu güncellemeye özel AYRI onay alınır; 'HAZIR' demeden güncelleme başlamaz.")
    return cikti


# ============================================================ rapor ve ana akış

def kart_yukle(yol):
    """(belge, hata metni). Okunamayan/bozuk dosya bir bulgudur, çökme değil."""
    try:
        doc = json_oku(Path(yol), {"programlar": {}})
    except (OSError, ValueError) as e:
        return None, f"programlar.json okunamadı ({type(e).__name__}: {str(e)[:80]})"
    if not isinstance(doc, dict) or not isinstance(doc.get("programlar"), dict):
        return None, "programlar.json okunamadı ('programlar' sözlüğü yok)"
    return doc, None


def _satir_durum(r):
    return r["durum"]


def rapor(a, ctx, doc):
    """Normal koşu: (rapor satırları, bulgular). Mevcut çıktı satırları ve iki tablo aynen korunur; sonuna yeni bloklar eklenir.
    bulgular: {'sorun': [...], 'dikkat': [...], 'satirlar': [...], 'karar': [...]}"""
    kart = doc["programlar"]
    satirlar, yerinde = [], []
    B = {"sorun": [], "dikkat": [], "satirlar": [], "karar": []}
    dikkat_bloku = []
    for ad, p in sorted(kart.items()):
        if p.get("kopya", "kaynak") == "yerinde":
            try:
                r = yerinde_denetle(ad, p)
            except Exception as e:  # noqa: BLE001  bozuk kart denetimi düşürmez (çıkış kodu 0 kalır)
                print(f"UYARI: {ad}: denetim hatası ({str(e)[:100]})")
                y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
                r = {"ad": ad, "tur": y.get("tur"), "kart": p.get("kutuphane_commit") or p.get("kutuphane_surumu"), "kurulu": None,
                     "son": None, "geride": None, "degisen": 0, "izlenmeyen": 0, "pin": None, "pin_fark": [], "durum": "öğrenilemedi"}
            yerinde.append(r)
            yerel = yerel_metin(r)
            ek = f" · yerel: {yerel}" if yerel not in ("-", "temiz") else ""
            rd = (r.get("repo_durum") or ("var", None))[0]
            if rd in ("kayıp", "taşınmış"):
                ek += f" · repo: {'KAYIP' if rd == 'kayıp' else 'TAŞINMIŞ'}"
            print(f"{ad}: karttaki {kisa(r['kart'], r['tur'])} · kurulu {kisa(r['kurulu'], r['tur'])} · son {kisa(r['son'], r['tur'])} · {r['durum']}{ek}")
            if r["pin"]:
                print(f"  sabit sürümler: {r['pin']} uyuyor" + "".join(f"\n  - {f}" for f in r["pin_fark"]))
            # --- özet bulguları
            kirici = []
            if r["kurulu"] and r["son"]:
                try:
                    kirici = kirici_adayi(p, r["kurulu"], r["son"], r["geride"], None)
                except Exception:  # noqa: BLE001
                    kirici = []
            kirici = [n for n in kirici if "yamalı" not in n and "izlenen dosyayı" not in n]
            d = r["durum"]
            geride_m = f"{r['geride']} geride" if r["geride"] else None
            if d == "YENİ SÜRÜM VAR":
                detay = f"kurulu {kisa(r['kurulu'], r['tur'])}, son {kisa(r['son'], r['tur'])}" if not geride_m else geride_m
                B["satirlar"].append(f"{ad}: {d} ({detay})" + (" · kırıcı adayı" if kirici else ""))
                B["dikkat"].append(ad)
                B["karar"].append(f"{ad} {r['geride']} commit güncellemesi: kullanıcı onayı bekliyor" if r["tur"] == "git-checkout" and r["geride"]
                                  else f"{ad} {kisa(r['kurulu'], r['tur'])} -> {kisa(r['son'], r['tur'])} güncellemesi: kullanıcı onayı bekliyor")
            elif d == "KART ESKİ":
                B["satirlar"].append(f"{ad}: KART ESKİ (kurulu {kisa(r['kurulu'], r['tur'])}, kart {kisa(r['kart'], r['tur'])})")
                B["sorun"].append(ad)
                B["karar"].append(f"{ad}: kart eski (kurulu {kisa(r['kurulu'], r['tur'])}, kart {kisa(r['kart'], r['tur'])}): sebebi bulunup karar verilmeli")
            else:
                B["satirlar"].append(f"{ad}: {d}")
                if d == "öğrenilemedi":
                    B["dikkat"].append(ad)
            if r["pin_fark"]:
                B["sorun"].append(f"{ad} sabit sürüm farkı")
                B["satirlar"].append(f"{ad}: sabit sürüm farkı ({len(r['pin_fark'])})")
            if rd == "kayıp":
                B["sorun"].append(f"{ad} repo kayıp")
                dikkat_bloku.append(f"- {ad} · repo GitHub'da bulunamadı (404): KAYIP")
            elif rd == "taşınmış":
                B["dikkat"].append(f"{ad} repo taşınmış")
                dikkat_bloku.append(f"- {ad} · repo taşınmış: yeni ad {r['repo_durum'][1]}")
            if kart_eski_ad(p):
                B["dikkat"].append(f"{ad} kart eski repo adı")
                dikkat_bloku.append(f"- {ad} · kart eski repo adını taşıyor; güncel ad: {kart_eski_ad(p)}")
            for n in kirici:
                dikkat_bloku.append(f"- {ad} · kırıcı adayı: {n}")
            continue
        kopya = ctx.kok / p.get("kaynak_kopyasi", "")
        kopya_var = bool(p.get("kaynak_kopyasi")) and kopya.is_dir() and any(kopya.iterdir())
        d_ek = None
        try:
            son = gh_api(f"repos/{p['repo']}/releases/latest")["tag_name"]
        except GhBulunamadi as e:
            son = None
            rd, yeni = repo_durumu(p.get("repo", ""))
            if rd == "kayıp":
                d_ek = "KAYIP (404)"
                print(f"UYARI: {ad}: repo GitHub'da bulunamadı (404)")
            elif rd == "taşınmış":
                d_ek = f"TAŞINMIŞ -> {yeni}"
                print(f"UYARI: {ad}: repo taşınmış: {yeni}")
            elif rd == "var":
                print(f"UYARI: {ad}: repo'da yayımlanmış release yok")
            else:
                print(f"UYARI: {ad}: son sürüm öğrenilemedi ({str(e)[:100]})")
        except Exception as e:  # noqa: BLE001  ağ/404: denetim düşmez
            son = None
            print(f"UYARI: {ad}: son sürüm öğrenilemedi ({str(e)[:100]})")
        d = d_ek or durum(p.get("kutuphane_surumu"), son)
        satirlar.append((ad, p.get("repo", "?"), p.get("kutuphane_surumu"), son or "?", d, "var" if kopya_var else "YOK"))
        print(f"{ad}: kütüphane {p.get('kutuphane_surumu')} · GitHub {son or '?'} · {d} · kaynak kopyası {'var' if kopya_var else 'YOK'}")
        B["satirlar"].append(f"{ad}: {d}")
        if d == "YENİ SÜRÜM VAR":
            B["dikkat"].append(ad)
            B["karar"].append(f"{ad} {p.get('kutuphane_surumu')} -> {son} güncellemesi: kullanıcı onayı bekliyor")
        elif d.startswith("KAYIP") or not kopya_var:
            B["sorun"].append(f"{ad} {d if d.startswith('KAYIP') else 'kaynak kopyası YOK'}")
        elif d != "güncel":
            B["dikkat"].append(ad)
    # --- programla gelen skillerin projelerdeki bağları (bağ yoksa hiçbir şey eklenmez)
    bag_tablo = []
    for ad, p in sorted(kart.items()):
        try:
            liste = program_baglari(ad, p, ctx)
        except Exception:  # noqa: BLE001
            liste = []
        if not liste:
            continue
        k = sum(1 for _, _, var in liste if not var)
        B["satirlar"].append(f"{ad}: {len(liste)} bağ, {k} kırık")
        for b, h, var in liste:
            bag_tablo.append(f"| {ad} | {b['proje']} | {b['skill']} | {'evet' if var else 'HAYIR'} | "
                             f"{kisa(b['surum'], 'git-checkout' if b['tur_surum'] == 'commit' else 'npm-global') if b['surum'] else '—'} |")
            if not var:
                dikkat_bloku.append(f"- {ad} · bağ kırık: {b['proje']}/{b['skill']} (program kurulu değilse ya da güncelleme sonrasıysa: skill-ekle.py <proje> --yenile)")
        if k:
            B["sorun"].append(f"{ad} {k} kırık bağ")
            B["karar"].append(f"{ad}: {k} kırık bağ -> skill-ekle.py <proje> --yenile ya da --kaldir <ad>")
    out = ["# Program Denetimi", "",
           f"> `araclar/program-denetim.py` üretir · {date.today().isoformat()} · salt okuma; güncelleme kullanıcı onayıyla "
           "`rehber/11-program-yonetimi.md` adımlarıyla yapılır.", "",
           "| Program | Repo | Kütüphanedeki sürüm | GitHub son sürüm | Durum | Kaynak kopyası |", "|---|---|---|---|---|---|"]
    out += [f"| {a_} | {r_} | {k_} | {s_} | {d_} | {v_} |" for a_, r_, k_, s_, d_, v_ in satirlar]
    if yerinde:
        out += ["", "## Yerinde izlenen programlar (kaynak kopyası yok)", "",
                "| Program | Tür | Karttaki | Kurulu | Son | Durum | Yerel değişiklik | Sabit sürümler |", "|---|---|---|---|---|---|---|---|"]
        out += [yerinde_satir(r) for r in yerinde]
        for r in yerinde:
            for f in r["pin_fark"]:
                out.append(f"- {r['ad']} · sabit sürüm farkı: {f}")
    # --- yeni bloklar: kart şeması, ortam anahtarları, dikkat
    try:
        bulgu = sema_denetle(doc, kok=ctx.kok, ev=ctx.ev)
    except Exception as e:  # noqa: BLE001
        bulgu = [("HATA", "programlar.json", "-", f"şema denetimi çalışmadı ({type(e).__name__})")]
    h = sum(1 for b in bulgu if b[0] == "HATA")
    u = len(bulgu) - h
    out += ["", "## Kart şeması", ""]
    out += [f"- {sema_satiri(b)}" for b in bulgu] if bulgu else ["tüm kartlar geçerli"]
    B["satirlar"].append(f"kart şeması: {h} hata" + (f", {u} uyarı" if u else ""))
    if h:
        B["sorun"].append("kart şeması hatası")
    elif u:
        B["dikkat"].append("kart şeması uyarısı")
    ortam_satirlari = []
    for ad, p in sorted(kart.items()):
        if p.get("kopya", "kaynak") != "yerinde" or not isinstance(p.get("ortam_anahtarlari"), list):
            continue
        try:
            for o in ortam_say(p, ctx):
                ortam_satirlari.append(f"{ad} · {o['ad']} · " + (f"{o['say']}/{o['toplam']}" if o["toplam"] else ("süreçte" if o["surecte"] else "tanımlı değil")))
                if o["gerekli"] and o["say"] == 0 and not o["surecte"]:
                    B["sorun"].append(f"{ad} {o['ad']} hiçbir yerde tanımlı değil")
                elif o["gerekli"] and o["toplam"] and o["say"] < o["toplam"]:
                    B["dikkat"].append(f"{ad} {o['ad']} bazı yerlerde eksik")
        except Exception:  # noqa: BLE001
            continue
    if ortam_satirlari:
        out += ["", "## Ortam anahtarları", ""] + [f"- {x}" for x in ortam_satirlari]
    if dikkat_bloku:
        out += ["", "## Dikkat", ""] + dikkat_bloku
    if bag_tablo:
        out += ["", "## Programla gelen skiller (bağlar)", "",
                "| Program | Proje | Skill | Hedef var mı | Bağlandığı sürüm |", "|---|---|---|---|---|"] + bag_tablo
    return out, B, bulgu


def _ozet_durum(B):
    return "sorun" if B["sorun"] else "dikkat" if B["dikkat"] else "temiz"


def main(argv=None):
    global _EV
    ap = argparse.ArgumentParser(description="Program denetimi (salt okuma)")
    ap.add_argument("--kart", default=str(KOK / "programlar.json"), help="programlar.json yolu (testler için)")
    ap.add_argument("--cikti", default=str(KOK / "notlar" / "program-denetimi.md"), help="rapor dosyası")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--sema", action="store_true", help="kart şeması denetimi")
    g.add_argument("--oncesi", metavar="AD", help="güncellemeden önce salt okuma ön kontrol")
    g.add_argument("--iskelet", choices=("kaynak", "npm-global", "git-checkout"), help="yeni program için boş kart iskeleti")
    g.add_argument("--pin-listesi", dest="pin_listesi", metavar="AD", help="venv'deki paket==sürüm listesi")
    ap.add_argument("--hedef", help="--oncesi: hedef sürüm ya da commit (sha en az 7 hane)")
    ap.add_argument("--cevrimdisi", action="store_true", help="ağa hiç gitme")
    ap.add_argument("--tedarik", action="store_true", help="--oncesi: tedarik doğrulaması (registry integrity) da bak")
    ap.add_argument("--ozet-json", dest="ozet_json", action="store_true", help="stdout'a tek JSON nesnesi; dosya yazmaz")
    ap.add_argument("--siki", action="store_true", help="sorun varsa çıkış kodu 1")
    ap.add_argument("--ev", help="'~' yerine bu klasör (testler)")
    ap.add_argument("--yedek-koku", dest="yedek_koku", help="yedek klasörlerinin kökü (varsayılan <ev>/Documents/Claude/yedek)")
    ap.add_argument("--kok", help="kütüphane kökü (testler)")
    a = ap.parse_args(argv)

    if a.iskelet:
        print(json.dumps(iskelet(a.iskelet), ensure_ascii=False, indent=2))
        return 0
    ctx = _ctx(ev=a.ev, kok=a.kok, yedek_koku=a.yedek_koku, cevrimdisi=a.cevrimdisi, hedef=a.hedef, tedarik=a.tedarik)
    eski_ev = _EV
    _EV = Path(a.ev) if a.ev else None
    try:
        doc, hata = kart_yukle(a.kart)
        arac = "program-denetim" + (" --sema" if a.sema else f" --oncesi {a.oncesi}" if a.oncesi else "")
        if hata:
            print(f"HATA: {hata}", file=sys.stderr if a.ozet_json else sys.stdout)
            nesne = {"arac": arac, "durum": "sorun", "satirlar": [f"HATA: {hata}"], "karar_bekleyen": []}
            if a.ozet_json:
                print(json.dumps(nesne, ensure_ascii=False))
            return 1 if a.siki else 0
        kart = doc["programlar"]
        for k in (a.oncesi, a.pin_listesi):
            if k and k not in kart:
                print(f"HATA: program yok: {k}; kartlar: {', '.join(sorted(kart))}", file=sys.stderr)
                return 2
        if a.pin_listesi:
            p = kart[a.pin_listesi]
            y = p.get("yerinde") if isinstance(p.get("yerinde"), dict) else {}
            if not p.get("venv") or not y.get("yol"):
                print(f"HATA: {a.pin_listesi} kartında venv yok", file=sys.stderr)
                return 2
            for n, v in sorted(dist_info_oku(yol_ac(y["yol"]) / p["venv"]).items()):
                print(f"{n}=={v}")
            return 0
        sink = sys.stderr if a.ozet_json else sys.stdout
        with contextlib.redirect_stdout(sink):
            if a.sema:
                bulgu = sema_denetle(doc, kok=ctx.kok, ev=ctx.ev)
                h = sum(1 for b in bulgu if b[0] == "HATA")
                u = len(bulgu) - h
                for b in bulgu:
                    print(sema_satiri(b))
                toplam = f"Kart şeması: {len(kart)} kart, {h} hata, {u} uyarı"
                print(toplam)
                nesne = {"arac": arac, "durum": "sorun" if h else "dikkat" if u else "temiz",
                         "satirlar": [sema_satiri(b) for b in bulgu] or [toplam], "karar_bekleyen": []}
            elif a.oncesi:
                S, sonuc = oncesi_denetle(a.oncesi, kart[a.oncesi], ctx)
                cikti = oncesi_yaz(a.oncesi, S, sonuc)
                print("\n".join(cikti))
                durum_j = "sorun" if sonuc == "HAZIR DEĞİL" else ("dikkat" if sonuc == "HAZIR" and any(x[0] == "UYARI" for x in S) else "temiz")
                nesne = {"arac": arac, "durum": durum_j,
                         "satirlar": [f"{x[0]}: {x[1]}: {x[2]}" for x in S if x[0] not in ("BAŞLIK", "ATLANDI")] + [cikti[-2]],
                         "karar_bekleyen": [f"{a.oncesi} güncellemesi için kullanıcı onayı gerekir"] if sonuc == "HAZIR" else []}
            else:
                out, B, _ = rapor(a, ctx, doc)
                nesne = {"arac": arac, "durum": _ozet_durum(B), "satirlar": B["satirlar"], "karar_bekleyen": B["karar"]}
                if not a.ozet_json:
                    hedef, yeni = Path(a.cikti), "\n".join(out) + "\n"
                    tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
                    if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
                        hedef.write_text(yeni, encoding="utf-8")
        if a.ozet_json:
            print(json.dumps(nesne, ensure_ascii=False))
        if a.siki and nesne["durum"] == "sorun":
            return 1
        return 0
    finally:
        _EV = eski_ev


if __name__ == "__main__":
    sys.exit(main())
