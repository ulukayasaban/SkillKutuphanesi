#!/usr/bin/env python3
"""Kütüphanenin git durumu (salt okuma).

push etmez, dal silmez, dosya değiştirmez; --uzak yalnız `git fetch origin` yapar.
Söyledikleri: GitHub'a gönderilmemiş commit (push gecikmesi), kirli ağaç, izlenmeyen klasör, artık/bekleyen dal,
.git boyutu, yeni büyük dosya, adı gizli bilgiye benzeyen izlenen dosya, eksik .gitignore koruması,
arsiv/ içinde git'e girmeyen dosya ve (isteğe bağlı) GitHub deposunun hâlâ private olup olmadığı.

Çıkış kodu: 0 = araç doğru çalıştı (ne bulursa bulsun); 1 = yalnız --siki ile ve durum "sorun" ise; 2 = kullanım hatası.

Kullanım:
  python3 araclar/git-durum.py              # insan okuyabilir rapor
  python3 araclar/git-durum.py --kisa       # oturum başı tek satır ("git: temiz" ya da yalnız dikkat/sorun)
  python3 araclar/git-durum.py --ozet-json  # tek JSON nesnesi (aylık özet için)
  python3 araclar/git-durum.py --uzak       # önce git fetch origin (tek ağ işlemi)
  python3 araclar/git-durum.py --rapor      # notlar/git-durumu.md yazar (yalnız bu bayrakla dosya yazılır)
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, GURULTU  # noqa: E402

BEKLENEN_DEPO = "ulukayasaban/SkillKutuphanesi"   # CLAUDE.md kural 5
ANA_DAL = "master"
ESIK_ONDE_COMMIT = 5        # gönderilmemiş commit sayısı: dikkat
ESIK_ONDE_GUN = 7           # en eski gönderilmemiş commit yaşı: dikkat
ESIK_GIT_MB = 300           # .git boyutu: dikkat
ESIK_YENI_DOSYA_MB = 5      # yeni eklenen/izlenmeyen dosya: dikkat
ESIK_BEKLEYEN_DAL_GUN = 45  # guncelleme/* ve takip/* dalı bu kadar gündür bekliyorsa metin güçlenir
ZAMAN_ASIMI = 60            # her git komutu için saniye (fetch 120, gh 20)
BEKLEYEN_DAL_ONEKLERI = ("guncelleme/", "takip/")
GIZLI_AD = re.compile(r"^(?:\.env(?:\..+)?|.*\.(?:pem|key|p12|pfx|keystore|jks)|id_(?:rsa|dsa|ecdsa|ed25519)\b.*|"
                      r"\.npmrc|\.netrc|\.pypirc|\.git-credentials|credentials(?:\..*)?|tokens?(?:\..*)?|secrets?(?:\..*)?|.*\.yedek)$", re.I)
GIZLI_MASKE_SONEKLERI = (".example", ".sample", ".template", ".dist")   # .env.example gizli sayılmaz
KORUMA_PROBLARI = [".env", "ornek.pem", "ornek.key", "yedek/ornek", ".skill-kutuphanesi/yedek/ornek",
                   "notlar/son-aylik-calisma.json", "notlar/aylik-ozet.md"]
SEVIYE_SIRA = {"sorun": 0, "dikkat": 1, "bilgi": 2}
TEK_DEGISIKLIK_ISTISNASI = "notlar/proje-kullanimi.md"   # aylık görev bunu kendisi kaydeder
TARAMA_SINIRI = 20000


def git(depo, *args, zaman=ZAMAN_ASIMI):
    """Salt okuma git (index'i yenilemez). (çıkış kodu, stdout); zaman aşımı ya da hata -> (124, '')."""
    try:
        r = subprocess.run(["git", "--no-optional-locks", "-C", str(depo), *args], capture_output=True, text=True,
                           stdin=subprocess.DEVNULL, timeout=zaman)
        return r.returncode, r.stdout
    except (subprocess.TimeoutExpired, OSError):
        return 124, ""


def origin_depo_adi(url):
    m = re.search(r"github\.com[:/]+([\w.-]+/[\w.-]+?)(?:\.git)?/?$", url or "")
    return m.group(1) if m else None


def _gun(ts):
    return max(0, int((time.time() - ts) // 86400))


def _klasor_boyutu(yol):
    toplam, sayac = 0, 0
    for kok, _, dosyalar in os.walk(yol):
        for d in dosyalar:
            sayac += 1
            if sayac > TARAMA_SINIRI:
                return toplam
            try:
                st = os.lstat(os.path.join(kok, d))
                if not os.path.islink(os.path.join(kok, d)):
                    toplam += st.st_size
            except OSError:
                pass
    return toplam


def bilgi_topla(depo, uzak=False, gh_kullan=True):
    depo = Path(depo)
    b = {"depo": str(depo)}
    kod, c = git(depo, "rev-parse", "--is-inside-work-tree")
    b["depo_var"] = kod == 0 and c.strip() == "true"
    if not b["depo_var"]:
        return b
    b["dal"] = git(depo, "branch", "--show-current")[1].strip()
    b["origin_url"] = git(depo, "config", "--get", "remote.origin.url")[1].strip()
    b["origin_depo"] = origin_depo_adi(b["origin_url"])
    b["uzak_sonuc"] = None
    b["uzak_hata"] = ""
    if uzak:
        if b["origin_depo"] is None or b["origin_depo"] == BEKLENEN_DEPO:
            try:
                r = subprocess.run(["git", "--no-optional-locks", "-C", str(depo), "fetch", "origin"], capture_output=True,
                                   text=True, stdin=subprocess.DEVNULL, timeout=120)
                b["uzak_sonuc"] = "alindi" if r.returncode == 0 else "hata"
                b["uzak_hata"] = (r.stderr or "")[:160]
            except (subprocess.TimeoutExpired, OSError) as e:
                b["uzak_sonuc"], b["uzak_hata"] = "hata", str(e)[:160]
        else:
            b["uzak_sonuc"] = "reddedildi"
    # ahead / behind
    b["ahead"] = b["behind"] = b["son_uzak_tarih"] = b["en_eski_gun"] = None
    if git(depo, "rev-parse", "--verify", "-q", f"refs/remotes/origin/{ANA_DAL}")[0] == 0:
        kod, c = git(depo, "rev-list", "--left-right", "--count", f"origin/{ANA_DAL}...{ANA_DAL}")
        if kod == 0 and len(c.split()) == 2:
            b["behind"], b["ahead"] = int(c.split()[0]), int(c.split()[1])
        b["son_uzak_tarih"] = git(depo, "log", "-1", "--format=%cs", f"origin/{ANA_DAL}")[1].strip() or None
        if b["ahead"]:
            zamanlar = [int(x) for x in git(depo, "log", f"origin/{ANA_DAL}..{ANA_DAL}", "--format=%ct")[1].split() if x.isdigit()]
            if zamanlar:
                b["en_eski_gun"] = _gun(min(zamanlar))
    # durum
    degisen, izlenmeyen = [], []
    kod, c = git(depo, "status", "--porcelain=v1", "-z")
    alanlar = c.split("\0") if kod == 0 else []
    i = 0
    while i < len(alanlar):
        e = alanlar[i]
        i += 1
        if len(e) < 4:
            continue
        kd, yol = e[:2], e[3:]
        if kd == "??":
            izlenmeyen.append(yol)
        else:
            degisen.append(yol)
            if "R" in kd or "C" in kd:
                i += 1   # sıradaki alan eski yol
    b["degisen"], b["izlenmeyen"] = sorted(degisen), sorted(izlenmeyen)
    # arsiv'de git'e girmeyen
    ark = []
    for s in git(depo, "status", "--ignored", "--porcelain", "arsiv")[1].splitlines():
        if s.startswith("!! "):
            yol = s[3:].rstrip("/")
            if not GURULTU.search(yol):
                ark.append(yol)
    b["arsiv_gizli_ignore"] = ark
    # dallar
    dallar = []
    for s in git(depo, "for-each-ref", "--format=%(refname:short)%09%(committerdate:unix)", "refs/heads")[1].splitlines():
        ad, _, ts = s.partition("\t")
        if not ad or ad == ANA_DAL:
            continue
        birlesmis = git(depo, "merge-base", "--is-ancestor", ad, ANA_DAL)[0] == 0
        c = git(depo, "rev-list", "--count", f"{ANA_DAL}..{ad}")[1].strip()
        dallar.append({"ad": ad, "birlesmis": birlesmis, "onde": int(c) if c.isdigit() else 0,
                       "gun": _gun(int(ts)) if ts.isdigit() else 0, "bekleyen": ad.startswith(BEKLEYEN_DAL_ONEKLERI)})
    b["yerel_dallar"] = dallar
    yerel_adlar = {d["ad"] for d in dallar}
    uzak_b = []
    for s in git(depo, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/guncelleme", "refs/remotes/origin/takip")[1].split():
        kisa = s[len("origin/"):] if s.startswith("origin/") else s
        if kisa not in yerel_adlar:
            uzak_b.append(kisa)
    b["uzak_bekleyen"] = sorted(uzak_b)
    # boyut
    boyut_kib = 0
    for s in git(depo, "count-objects", "-v")[1].splitlines():
        k, _, v = s.partition(":")
        if k.strip() in ("size", "size-pack") and v.strip().isdigit():
            boyut_kib += int(v.strip())
    b["git_mb"] = round(boyut_kib / 1024, 1)
    dosyalar = [x for x in git(depo, "ls-files", "-z")[1].split("\0") if x]
    boyutlar = []
    for f in dosyalar:
        try:
            st = os.lstat(depo / f)
            if not os.path.islink(depo / f):
                boyutlar.append((st.st_size, f))
        except OSError:
            pass
    boyutlar.sort(reverse=True)
    b["en_buyuk"] = [(f, round(s / 1048576, 1)) for s, f in boyutlar[:5]]
    esik = ESIK_YENI_DOSYA_MB * 1048576
    yeni = []
    if b["ahead"] is not None:
        for f in git(depo, "diff", "--name-only", "-z", "--diff-filter=A", f"origin/{ANA_DAL}", ANA_DAL)[1].split("\0"):
            if f:
                try:
                    if (depo / f).is_file() and os.lstat(depo / f).st_size >= esik:
                        yeni.append(f)
                except OSError:
                    pass
    for f in izlenmeyen:
        p = depo / f
        try:
            s = _klasor_boyutu(p) if p.is_dir() else os.lstat(p).st_size
        except OSError:
            continue
        if s >= esik:
            yeni.append(f)
    b["yeni_buyuk"] = sorted(set(yeni))
    # gizli adlar
    gizli, gizli_arsiv = [], 0
    for f in dosyalar:
        ad = f.rsplit("/", 1)[-1]
        if GIZLI_AD.match(ad) and not ad.lower().endswith(GIZLI_MASKE_SONEKLERI):
            if f.startswith("arsiv/"):
                gizli_arsiv += 1
            else:
                gizli.append(f)
    b["gizli_adlar"], b["gizli_arsiv_say"] = sorted(gizli), gizli_arsiv
    # koruma
    eksik = []
    for yol in KORUMA_PROBLARI:
        if git(depo, "check-ignore", "-q", "--no-index", "--", yol)[0] == 1:
            eksik.append(yol)
    b["koruma_eksik"] = eksik
    b["stash"] = len([x for x in git(depo, "stash", "list")[1].splitlines() if x.strip()])
    # görünürlük
    b["gorunurluk"] = None
    if gh_kullan and b["origin_depo"] == BEKLENEN_DEPO:
        try:
            r = subprocess.run(["gh", "repo", "view", BEKLENEN_DEPO, "--json", "visibility", "--jq", ".visibility"],
                               capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=20)
            if r.returncode == 0 and r.stdout.strip().lower() in ("private", "public", "internal"):
                b["gorunurluk"] = r.stdout.strip().lower()
        except (subprocess.TimeoutExpired, OSError):
            pass
    b["gh_denendi"] = bool(gh_kullan and b["origin_depo"] == BEKLENEN_DEPO)
    return b


def degerlendir(b):
    f = []

    def ekle(seviye, metin, karar=None):
        f.append({"seviye": seviye, "metin": metin, "karar": karar})
    if not b.get("depo_var"):
        ekle("sorun", f"Kütüphane git deposu değil: {b.get('depo')}")
        return "sorun", f
    od = b.get("origin_depo")
    if od and od != BEKLENEN_DEPO:
        ekle("sorun", f"origin beklenen depo değil ({od}); bu araç yalnız {BEKLENEN_DEPO} ile çalışır, fetch yapılmadı")
    ahead, behind = b.get("ahead"), b.get("behind")
    if ahead and behind:
        ekle("sorun", f"master ile origin/master ayrışmış: {ahead} önde, {behind} geride. Önce sebebi bulunur (GitHub'daki Merge "
                      "düğmesi kullanılmış olabilir, rehber/02); hiçbir şey kendiliğinden birleştirilmez")
    gor = b.get("gorunurluk")
    if gor in ("public", "internal"):
        ekle("sorun", f"GitHub deposu {gor} görünüyor; arsiv/ üçüncü taraf kopyalar içerir, depo private olmalı. Kullanıcıya hemen söyle")
    if b.get("gizli_adlar"):
        ekle("sorun", f"Adı gizli bilgi gibi görünen izlenen dosya: {', '.join(b['gizli_adlar'][:10])}. İçeriğini açma; kullanıcıya söyle (rehber/13)")
    ai = b.get("arsiv_gizli_ignore") or []
    if ai:
        ekle("sorun", f"Skill'in kendi .gitignore'u yüzünden git'e girmeyen arşiv dosyası var ({len(ai)}; ilk: {ai[0]}). "
                      "Düzeltme: git add -f arsiv (klon eksik gelir)")
    dal = b.get("dal")
    if not dal:
        ekle("dikkat", "HEAD bir dala bağlı değil")
    elif dal != ANA_DAL:
        ekle("dikkat", f"Şu an {dal} dalındasın (beklenen: {ANA_DAL})")
    if ahead and not behind:
        gun = b.get("en_eski_gun")
        if ahead >= ESIK_ONDE_COMMIT or (gun is not None and gun > ESIK_ONDE_GUN):
            ekle("dikkat", f"GitHub'a gönderilmemiş {ahead} commit var (en eskisi {gun} gün önce; son bilinen uzak commit "
                           f"{b.get('son_uzak_tarih')}).", f"{ahead} commit GitHub'a gönderilsin mi? (push yalnız sen isteyince yapılır)")
        else:
            ekle("bilgi", f"GitHub'a gönderilmemiş {ahead} commit var (eşiğin altında; en eskisi {gun} gün önce)")
    if behind and not ahead:
        ekle("dikkat", f"GitHub'da {behind} yeni commit var; yerelde yok (git pull gerekir, kullanıcıyla)")
    dg = b.get("degisen") or []
    if dg:
        if dg == [TEK_DEGISIKLIK_ISTISNASI]:
            ekle("bilgi", f"Kaydedilmemiş tek değişiklik {TEK_DEGISIKLIK_ISTISNASI} (aylık görev bunu kendisi kaydeder)")
        else:
            ekle("dikkat", f"Kaydedilmemiş değişiklik: {len(dg)} dosya")
    iz = b.get("izlenmeyen") or []
    if iz:
        liste = ", ".join(iz[:8]) + (f" ... (+{len(iz) - 8})" if len(iz) > 8 else "")
        ekle("dikkat", f"İzlenmeyen klasör/dosya: {liste}", f"{liste} commit edilsin mi?")
    for d in b.get("yerel_dallar", []):
        if d["bekleyen"]:
            uzun = f"; {ESIK_BEKLEYEN_DAL_GUN} günden uzun bekliyor" if d["gun"] > ESIK_BEKLEYEN_DAL_GUN else ""
            ekle("dikkat", f"Bekleyen güncelleme dalı: {d['ad']} ({d['gun']} gündür bekliyor{uzun}); yenisi açılmaz",
                 f"{d['ad']} dalı birleştirilsin mi, reddedilsin mi? (promptlar/08)")
        elif d["birlesmis"]:
            ekle("dikkat", f"Birleşmiş artık dal: {d['ad']} (master'a zaten girmiş)", f"{d['ad']} dalı silinsin mi? (git branch -d, birleşmiş)")
        else:
            ekle("dikkat", f"Birleşmemiş yerel dal: {d['ad']} ({d['onde']} commit master'da yok, son commit {d['gun']} gün önce)",
                 f"{d['ad']} dalı birleştirilsin mi, silinsin mi?")
    if b.get("uzak_bekleyen"):
        ekle("bilgi", f"GitHub'da bekleyen dal (son alıştan): {', '.join(b['uzak_bekleyen'])}")
    if (b.get("git_mb") or 0) > ESIK_GIT_MB:
        ekle("dikkat", f".git klasörü {b['git_mb']} MB (eşik {ESIK_GIT_MB} MB). Büyüme sebebi araştırılır; kullanıcıya sor, kendiliğinden temizleme yapma")
    if b.get("yeni_buyuk"):
        liste = ", ".join(b["yeni_buyuk"][:8])
        ekle("dikkat", f"Yeni büyük dosya (>= {ESIK_YENI_DOSYA_MB} MB): {liste}",
             f"{liste} git'e girsin mi? (büyük medya arsiv'e girecekse önce sor)")
    if b.get("koruma_eksik"):
        ekle("dikkat", f".gitignore koruması eksik: {', '.join(b['koruma_eksik'])} (rehber/13)")
    # bilgi satırları
    if ahead == 0 and behind == 0:
        ekle("bilgi", "GitHub ile eşit: 0 önde, 0 geride")
    elif ahead is None:
        ekle("bilgi", "origin/master bilinmiyor (uzak hiç alınmamış)")
    if b.get("stash"):
        ekle("bilgi", f"Saklanmış değişiklik (stash): {b['stash']}")
    if b.get("en_buyuk"):
        ekle("bilgi", "En büyük 5 izlenen dosya: " + ", ".join(f"{a} {m} MB" for a, m in b["en_buyuk"]))
    ekle("bilgi", f".git boyutu: {b.get('git_mb')} MB")
    if b.get("gizli_arsiv_say"):
        ekle("bilgi", f"arsiv/ içinde adı gizli desenine uyan {b['gizli_arsiv_say']} izlenen üçüncü taraf dosya var (örnek/sabit dosyalar; taranmadı)")
    us = b.get("uzak_sonuc")
    if us == "alindi":
        ekle("bilgi", "Uzak güncellendi (git fetch origin)")
    elif us == "hata":
        ekle("bilgi", "Uzak alınamadı (GitHub oturumu ya da ağ yok): ahead/behind son bilinen duruma göre. "
                      "Oturum için bkz. rehber/13, 'GitHub oturumu bitince'")
    elif us == "reddedildi":
        ekle("sorun", f"origin beklenen depo değil ({od}); bu araç yalnız {BEKLENEN_DEPO} ile çalışır, fetch yapılmadı")
    if gor == "private":
        ekle("bilgi", "Depo görünürlüğü: private")
    elif b.get("gh_denendi"):
        ekle("bilgi", "depo görünürlüğü: denetlenemedi (gh oturumu yok ya da ağ yok)")
    # yinelenen sorun metinlerini ele
    gorulen, tek = set(), []
    for x in f:
        k = (x["seviye"], x["metin"])
        if k not in gorulen:
            gorulen.add(k)
            tek.append(x)
    f = sorted(tek, key=lambda x: SEVIYE_SIRA[x["seviye"]])
    durum = "sorun" if any(x["seviye"] == "sorun" for x in f) else "dikkat" if any(x["seviye"] == "dikkat" for x in f) else "temiz"
    return durum, f


def _kirp(liste, n=10):
    return liste if len(liste) <= n else liste[:n] + [f"... ve {len(liste) - n} satır daha"]


def ozet_json(b, durum, bulgular):
    onemli = [x["metin"] for x in bulgular if x["seviye"] in ("sorun", "dikkat")]
    karar = [x["karar"] for x in bulgular if x["karar"]]
    ahead = b.get("ahead")
    if ahead:
        temiz_satir = f"Git temiz ({ahead} commit GitHub'a gönderilmemiş, eşiğin altında)."
    else:
        temiz_satir = "Git temiz: master GitHub ile aynı, değişiklik yok."
    return {"arac": "git-durum", "durum": durum,
            "satirlar": _kirp(onemli) if onemli else [temiz_satir],
            "karar_bekleyen": karar[:10]}


def kisa_metin(b, durum, bulgular):
    onemli = [x for x in bulgular if x["seviye"] in ("sorun", "dikkat")]
    if not onemli:
        return "git: temiz"
    return "\n".join(("SORUN: " if x["seviye"] == "sorun" else "DİKKAT: ") + x["metin"] for x in onemli)


ETIKET = {"sorun": "SORUN", "dikkat": "DİKKAT", "bilgi": "bilgi"}


def tam_metin(b, durum, bulgular):
    out = [f"Git durumu · {date.today().isoformat()} · dal {b.get('dal') or '-'} · durum: "
           + {"temiz": "TEMİZ", "dikkat": "DİKKAT", "sorun": "SORUN"}[durum]]
    for x in bulgular:
        out.append(f"{ETIKET[x['seviye']]}: {x['metin']}")
    k = [x["karar"] for x in bulgular if x["karar"]]
    if k:
        out += ["", "Karar bekleyenler"] + [f"- {x}" for x in k]
    return "\n".join(out)


def rapor_md(b, durum, bulgular):
    out = ["# Git Durumu", "",
           f"`araclar/git-durum.py` üretir · {date.today().isoformat()} · salt okuma", "",
           "| Seviye | Bulgu |", "|---|---|"]
    out += [f"| {ETIKET[x['seviye']]} | {x['metin'].replace('|', '/')} |" for x in bulgular]
    k = [x["karar"] for x in bulgular if x["karar"]]
    out += ["", "## Karar bekleyenler", ""] + ([f"- {x}" for x in k] if k else ["- yok"])
    out += ["", "## En büyük 5 izlenen dosya", "", "| Dosya | MB |", "|---|---|"]
    out += [f"| {a} | {m} |" for a, m in b.get("en_buyuk", [])]
    return "\n".join(out) + "\n"



def cikti_izinli(hedef):
    """--cikti koruması: araç klasörlerine, ~/Library'ye ve yedek/proje klasörlerine (~/Documents/Claude) yazılmaz."""
    h = os.path.realpath(str(hedef))
    ev = os.path.realpath(str(Path.home()))
    yasak = [os.path.join(ev, d) for d in (".claude", ".agents", ".codex", ".gemini", ".cursor", ".copilot", ".openmontage", ".config", "Library")]
    yasak.append(os.path.join(ev, "Documents", "Claude"))
    return not any(h == y or h.startswith(y + os.sep) for y in yasak)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Git durumu (salt okuma)")
    ap.add_argument("--depo", default=str(KOK))
    ap.add_argument("--uzak", action="store_true", help="önce git fetch origin (tek ağ işlemi)")
    ap.add_argument("--gh-yok", action="store_true", help="depo görünürlüğü denetimini atla")
    ap.add_argument("--kisa", action="store_true", help="tek satır / yalnız dikkat-sorun satırları (gh denetimi yok)")
    ap.add_argument("--ozet-json", action="store_true", help="tek JSON nesnesi yazdır")
    ap.add_argument("--rapor", action="store_true", help="Markdown raporu yaz")
    ap.add_argument("--cikti", default=str(KOK / "notlar" / "git-durumu.md"))
    ap.add_argument("--siki", action="store_true", help="durum sorun ise çıkış kodu 1")
    a = ap.parse_args(argv)
    if a.ozet_json and (a.kisa or a.rapor):
        ap.error("--ozet-json, --kisa ya da --rapor ile birlikte kullanılamaz")
    try:
        b = bilgi_topla(a.depo, uzak=a.uzak, gh_kullan=not (a.gh_yok or a.kisa))
        durum, bulgular = degerlendir(b)
    except Exception as e:  # noqa: BLE001
        if a.ozet_json:
            print(json.dumps({"arac": "git-durum", "durum": "sorun", "satirlar": [f"araç hatası: {str(e)[:120]}"],
                              "karar_bekleyen": []}, ensure_ascii=False))
            return 0
        raise
    if a.ozet_json:
        print(json.dumps(ozet_json(b, durum, bulgular), ensure_ascii=False))
    elif a.kisa:
        print(kisa_metin(b, durum, bulgular))
    else:
        print(tam_metin(b, durum, bulgular))
    if a.rapor:
        hedef = Path(a.cikti)
        if not cikti_izinli(hedef):
            print(f"HATA: --cikti bu yola yazamaz (araç klasörleri ve yedekler korumalı): {hedef}", file=sys.stderr)
            return 2
        yeni = rapor_md(b, durum, bulgular)
        tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
        if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
            hedef.write_text(yeni, encoding="utf-8")
    return 1 if (a.siki and durum == "sorun") else 0


if __name__ == "__main__":
    sys.exit(main())
