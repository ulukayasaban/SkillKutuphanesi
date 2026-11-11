#!/usr/bin/env python3
"""Program denetimi (salt okuma): programlar.json'daki her program için, kaynak kopyalı kartta kütüphanedeki sürümü
GitHub'daki en son sürümle karşılaştırır ve kopya klasörünün var olduğunu kontrol eder; yerinde (kopyasız) kartta
karttaki, kurulu ve son değeri karşılaştırır.

İki kart türü var: 'kaynak' (varsayılan; kaynak kopyası kütüphanede) ve 'yerinde' (kopya yok; program bu bilgisayarda kurulu:
npm-global paket ya da git-checkout). 'yerinde' kartta üç değer bakılır: karttaki, kurulu (şimdi), son (GitHub/npm). Kurulu değer
sadece dosya okuyarak (package.json, salt okuma git, dist-info/METADATA) bulunur; npm, pip, venv python, programın kendisi ÇALIŞMAZ.
Hiçbir şey kurmaz, indirmez, güncellemez; program komutlarını çalıştırmaz; anahtar/oturum dosyalarını açmaz.
Ağ hatası denetimi düşürmez ("öğrenilemedi" yazar). Çıkış kodu her zaman 0 (aylık zinciri durdurmaz).

Çıktı: notlar/program-denetimi.md
Kullanım: python3 araclar/program-denetim.py
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, gh_api, json_oku  # noqa: E402


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


def yol_ac(yol):
    """'~/x' -> mutlak yol."""
    return Path(str(yol)).expanduser()


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
    except Exception:  # noqa: BLE001  ağ/ayrıştırma: denetim düşmez
        return None
    return v if isinstance(v, str) and v.strip() else None


def git_okuma(yol, *args):
    """Salt okuma git (rev-parse/status); çıktı ya da None. İndeksi bile yenilemez (--no-optional-locks)."""
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
    except Exception:  # noqa: BLE001
        return None, None
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


def main(argv=None):
    ap = argparse.ArgumentParser(description="Program denetimi (salt okuma)")
    ap.add_argument("--kart", default=str(KOK / "programlar.json"), help="programlar.json yolu (testler için)")
    ap.add_argument("--cikti", default=str(KOK / "notlar" / "program-denetimi.md"), help="rapor dosyası")
    a = ap.parse_args(argv)
    kart = json_oku(Path(a.kart), {"programlar": {}})["programlar"]
    satirlar, yerinde = [], []
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
            print(f"{ad}: karttaki {kisa(r['kart'], r['tur'])} · kurulu {kisa(r['kurulu'], r['tur'])} · son {kisa(r['son'], r['tur'])} · {r['durum']}{ek}")
            if r["pin"]:
                print(f"  sabit sürümler: {r['pin']} uyuyor" + "".join(f"\n  - {f}" for f in r["pin_fark"]))
            continue
        kopya = KOK / p.get("kaynak_kopyasi", "")
        kopya_var = bool(p.get("kaynak_kopyasi")) and kopya.is_dir() and any(kopya.iterdir())
        try:
            son = gh_api(f"repos/{p['repo']}/releases/latest")["tag_name"]
        except Exception as e:  # noqa: BLE001  ağ/404: denetim düşmez
            son = None
            print(f"UYARI: {ad}: son sürüm öğrenilemedi ({str(e)[:100]})")
        d = durum(p.get("kutuphane_surumu"), son)
        satirlar.append((ad, p["repo"], p.get("kutuphane_surumu"), son or "?", d, "var" if kopya_var else "YOK"))
        print(f"{ad}: kütüphane {p.get('kutuphane_surumu')} · GitHub {son or '?'} · {d} · kaynak kopyası {'var' if kopya_var else 'YOK'}")
    out = ["# Program Denetimi", "",
           f"> `araclar/program-denetim.py` üretir · {date.today().isoformat()} · salt okuma; güncelleme kullanıcı onayıyla "
           "`rehber/11-program-yonetimi.md` adımlarıyla yapılır.", "",
           "| Program | Repo | Kütüphanedeki sürüm | GitHub son sürüm | Durum | Kaynak kopyası |", "|---|---|---|---|---|---|"]
    out += [f"| {a} | {r} | {k} | {s} | {d} | {v} |" for a, r, k, s, d, v in satirlar]
    if yerinde:
        out += ["", "## Yerinde izlenen programlar (kaynak kopyası yok)", "",
                "| Program | Tür | Karttaki | Kurulu | Son | Durum | Yerel değişiklik | Sabit sürümler |", "|---|---|---|---|---|---|---|---|"]
        out += [yerinde_satir(r) for r in yerinde]
        for r in yerinde:
            for f in r["pin_fark"]:
                out.append(f"- {r['ad']} · sabit sürüm farkı: {f}")
    hedef, yeni = Path(a.cikti), "\n".join(out) + "\n"
    tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
    if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
        hedef.write_text(yeni, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
