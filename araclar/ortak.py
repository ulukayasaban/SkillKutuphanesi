"""SkillKutuphanesi araçlarının ortak yardımcıları (sadece Python stdlib)."""
import bisect
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ARSIV = KOK / "arsiv"
REGISTRY = KOK / "registry.json"
KAYNAKLAR = KOK / "kaynaklar.json"
KATEGORILER = KOK / "kategoriler.json"
GECICI = KOK / ".gecici"
YAMALAR = KOK / "yamalar"  # kurulan kopyada orijinalin yerine geçen düzeltilmiş dosyalar: yamalar/<skill id>/<yol>
TREND = KOK / "trend.json"

# Claude hesabındaki (claude.ai) skiller Claude Code'a buradan, "anthropic-skills:<ad>" adıyla yüklenir. SADECE OKUNUR.
# Projeye aynı adlı kütüphane skill'i kurulunca agent çoğu zaman hesaptakini seçer; proje .claude/settings.json'da
# skillOverrides {"anthropic-skills:<ad>": "off"} ile hesaptaki o proje için gizlenir (skill-ekle.py hesap_gizle).
HESAP_SKILLERI = Path.home() / ".claude" / "skills" / "synced"
HESAP_ONEK = "anthropic-skills"


def hesap_skilleri() -> dict:
    """Claude hesabından senkronlanan skiller: {ad: klasör}. Yoksa boş."""
    sonuc = {}
    if HESAP_SKILLERI.is_dir():
        for sm in sorted(HESAP_SKILLERI.glob("*/*/SKILL.md")):
            sonuc.setdefault(sm.parent.name, sm.parent)
    return sonuc


# Bilgisayardaki global skill klasörleri: SADECE OKUNUR, asla yazılmaz.
GLOBAL_KLASORLER = {
    "claude": Path.home() / ".claude" / "skills",
    "codex": Path.home() / ".codex" / "skills",
    "agents": Path.home() / ".agents" / "skills",
}


def json_oku(yol, varsayilan=None):
    yol = Path(yol)
    if not yol.exists():
        return varsayilan
    return json.loads(yol.read_text(encoding="utf-8"))


def json_yaz(yol, veri):
    """Atomik yazım: önce geçici dosya, sonra yerine taşı (yarım JSON kalmaz)."""
    yol = Path(yol)
    gecici = yol.with_name(f".{yol.name}.tmp")
    gecici.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(gecici, yol)


class GhBulunamadi(RuntimeError):
    """GitHub 404/422: kaynak yok, private olmuş ya da commit geçmişi yeniden yazılmış."""


def gh_api(yol, deneme=4):
    for i in range(deneme):
        r = subprocess.run(["gh", "api", yol], capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout)
        if "HTTP 404" in r.stderr or "HTTP 422" in r.stderr:
            raise GhBulunamadi(f"{yol}: {r.stderr.strip()[:200]}")
        if "not enabled" in r.stderr or "not available" in r.stderr:  # bu oturumda kapalı uç nokta: beklemek anlamsız
            raise RuntimeError(f"gh api kapalı: {yol}: {r.stderr.strip()[:200]}")
        # hız sınırı: kısa bekleme işe yaramaz; dakikalarca bekleyip yeniden dene (ay-ortası çökme yerine)
        limit = "rate limit" in r.stderr.lower() or "HTTP 403" in r.stderr or "HTTP 429" in r.stderr
        time.sleep(60 * (i + 1) if limit else 2 * (i + 1))
    raise RuntimeError(f"gh api başarısız: {yol}: {r.stderr.strip()}")


API_KAPALI = ("not enabled", "not available", "HTTP 403")


def api_kapali(hata) -> bool:
    """gh api hatası 'bu oturumda repo API'si kapalı' türünden mi? (bulut oturumu: sadece bağlı depo; ya da izin yok)"""
    return any(x in str(hata) for x in API_KAPALI)


def repo_agaci(repo: str, sha: str = None):
    """Reponun dosya ağacı: önce GitHub API (repos/{repo}/git/trees), API kapalıysa git ile (blob'suz sığ fetch; dosya indirilmez).
    Döner: (sha, {"tree": [{"path","type","sha","size"}], "truncated": False, "_kaynak": "api"|"git"})"""
    try:
        if not sha:
            sha = gh_api(f"repos/{repo}/commits/HEAD")["sha"]
        govde = gh_api(f"repos/{repo}/git/trees/{sha}?recursive=1")
        govde["_kaynak"] = "api"
        return sha, govde
    except RuntimeError as e:
        if not api_kapali(e):
            raise
    d = GECICI / "git-agac" / repo.replace("/", "__")
    import shutil
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    komutlar = [["git", "init", "-q"], ["git", "remote", "add", "origin", f"https://github.com/{repo}"],
                ["git", "fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", sha or "HEAD"]]
    for k in komutlar:
        r = subprocess.run(k, cwd=d, capture_output=True, text=True)
        if r.returncode:
            shutil.rmtree(d, ignore_errors=True)
            raise GhBulunamadi(f"{repo}: API kapalı ve git ile de okunamadı: {r.stderr.strip()[-200:]}")
    sha = sha or subprocess.run(["git", "rev-parse", "FETCH_HEAD"], cwd=d, capture_output=True, text=True).stdout.strip()
    agac = []
    # --long KULLANILMAZ: blob'suz klonda boyut için her blob tek tek indirilir (binlerce istek). Boyut None; dosya boyutu
    # sınırı, dosyalar klon_dosyalari_al() ile çekildikten sonra yerelde uygulanır.
    for satir in subprocess.run(["git", "ls-tree", "-r", "FETCH_HEAD"], cwd=d, capture_output=True, text=True).stdout.splitlines():
        meta, yol = satir.split("\t", 1)
        mod, tur, oid = meta.split()
        agac.append({"path": yol, "type": tur, "mode": mod, "sha": oid, "size": None})
    return sha, {"tree": agac, "truncated": False, "_kaynak": "git", "_klon": str(d), "_sha": sha}  # klon kalır: klon_dosyalari_al / klon_temizle


def klon_dosyalari_al(govde, yollar):
    """repo_agaci git modunda seçilen dosyaları indirir: önce dosyaların blob kimlikleri TOPLU olarak çekilir
    (git fetch --stdin, 300'lük partiler; ağ koparsa 4 deneme), sonra çevrimdışı checkout. Böylece binlerce tek tek blob
    isteği (yavaş, proxy'de kopuyor) yerine birkaç pack isteği yapılır.
    Döner: {yol: Path} (klon içindeki dosya). Çağıran kopyalar ve klon_temizle() ile klonu siler."""
    d = Path(govde["_klon"])
    oid = {x["path"]: x["sha"] for x in govde["tree"] if x["type"] == "blob"}
    istenen = sorted({oid[y] for y in yollar if y in oid})
    for i in range(0, len(istenen), 300):
        parti = "\n".join(istenen[i:i + 300]) + "\n"
        for deneme in range(4):
            r = subprocess.run(["git", "fetch", "-q", "--no-tags", "--filter=blob:none", "--stdin", "origin"],
                               cwd=d, input=parti, capture_output=True, text=True)
            if r.returncode == 0:
                break
            time.sleep(3 * (deneme + 1))
        else:
            raise RuntimeError(f"git fetch (blob partisi {i // 300 + 1}) başarısız: {r.stderr.strip()[-300:]}")
    liste = d / ".skill-kutuphanesi-yollar"
    liste.write_text("\n".join(yollar) + "\n", encoding="utf-8")
    # blob fetch'leri FETCH_HEAD'i ezdiği için commit sha'sı kullanılır
    r = subprocess.run(["git", "checkout", "-q", f"--pathspec-from-file={liste}", govde["_sha"]], cwd=d, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"git checkout başarısız: {r.stderr.strip()[-300:]}")
    liste.unlink(missing_ok=True)
    return {y: d / y for y in yollar if (d / y).is_file()}


def klon_temizle(govde):
    import shutil
    if govde and govde.get("_klon"):
        shutil.rmtree(govde["_klon"], ignore_errors=True)


def repo_lisansi(repo: str, agac=None) -> str:
    """Lisans: repo API'si → arama API'si → LICENSE dosyası (raw) → 'belirtilmemiş'."""
    for yol in (f"repos/{repo}", f"search/repositories?q=repo:{repo}"):
        try:
            d = gh_api(yol)
            d = (d.get("items") or [{}])[0] if "items" in d else d
            lis = (d.get("license") or {}).get("spdx_id")
            if lis:
                return lis
            if "items" not in d:
                return "belirtilmemiş"
        except RuntimeError as e:
            if not api_kapali(e):
                raise
    for x in agac or []:
        if re.match(r"^LICEN[SC]E", x["path"], re.I):
            try:
                import urllib.request
                with urllib.request.urlopen(f"https://raw.githubusercontent.com/{repo}/HEAD/{x['path']}", timeout=30) as r:
                    metin = r.read(3000).decode("utf-8", "replace")
            except OSError:
                return "NOASSERTION"
            for k, desen in (("MIT", r"MIT License"), ("Apache-2.0", r"Apache License"), ("AGPL-3.0", r"GNU AFFERO"),
                             ("GPL-3.0", r"GNU GENERAL PUBLIC LICENSE.*Version 3"), ("BSD-3-Clause", r"BSD 3-Clause|Redistribution and use")):
                if re.search(desen, metin, re.S):
                    return k
            return "NOASSERTION"
    return "belirtilmemiş"


def git_blob_hash(veri: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(veri) + veri).hexdigest()


GURULTU = re.compile(r"(^|/)(\.DS_Store|__pycache__|\.git|Thumbs\.db|\.ipynb_checkpoints)(/|$)|\.pyc$")


# İçerik karşılaştırmasında (klasor_hash, kilit) node_modules da sayılmaz: `npm install` skill'i "elle değişmiş" göstermesin.
# GURULTU'ya DEĞİL buraya eklendi: GURULTU genel-bekci ve git-durum'da da kullanılır (onların sayımları değişmesin).
# package-lock.json bilerek sayılmaya devam eder: arşivdeki 18 skill'in klasor_hash'i onu içerir, değişirse projeler "güncelleme var" görür.
ICERIK_GURULTU = re.compile(GURULTU.pattern + r"|(^|/)node_modules(/|$)")


def onemli_dosyalar(klasor: Path):
    """İçerik karşılaştırmasına giren dosyalar: KAYNAK.md ve işletim sistemi/çalışma çöpleri, node_modules hariç."""
    return sorted(p for p in klasor.rglob("*") if p.is_file() and p.name != "KAYNAK.md"
                  and not ICERIK_GURULTU.search(str(p.relative_to(klasor))))


# ------------------------------------------------------------------ yerel (GitHub'sız) kaynak: kendi/ (T7) ve site/ (T8)
# Kullanıcının kendi skilleri kütüphanenin içinde düz bir klasörde durur (kendi/<skill>/; siteden alınanlar site/<skill>/). kaynak-cek.py bu klasörü GitHub
# ağacı gibi okur: aynı biçimde [{path, type, sha, size}] listesi ve 40 haneli bir "commit" (dosya içeriklerinden türetilir).
YEREL_GIZLI_AD = re.compile(r"(^|/)(\.env(\..*)?|auth\.json|token\.json|credentials\.json|[^/]*\.(pem|key|p12|pfx))$", re.I)


def yerel_agac(kok: Path, haric=()):
    """kok altındaki dosyalar: (liste, atlanan_gizli). Bağlar izlenmez; GURULTU/node_modules ve `haric` desenleri (SKILL.md hariç)
    ile gizli görünen dosya adları (.env, *.pem, *.key, auth/token/credentials.json) atlanır. Ağ kullanmaz."""
    sonuc, gizli = [], []
    kok = Path(kok)
    for yol, klasorler, dosyalar in os.walk(kok, followlinks=False):
        klasorler[:] = sorted(d for d in klasorler
                              if not os.path.islink(os.path.join(yol, d)) and not ICERIK_GURULTU.search(d))
        for ad in sorted(dosyalar):
            tam = Path(yol) / ad
            rel = tam.relative_to(kok).as_posix()
            if tam.is_symlink() or ICERIK_GURULTU.search(rel):
                continue
            if YEREL_GIZLI_AD.search(rel):
                gizli.append(rel)
                continue
            if ad.lower() != "skill.md" and any(re.search(d, rel) for d in haric):
                continue
            veri = tam.read_bytes()
            sonuc.append({"path": rel, "type": "blob", "sha": git_blob_hash(veri), "size": len(veri)})
    return sorted(sonuc, key=lambda e: e["path"]), gizli


def yerel_commit(agac) -> str:
    """Yerel ağacın 40 haneli kimliği (dosya yolu + içerik özeti); herhangi bir düzenlemede değişir, git'e bağlı değildir."""
    h = hashlib.sha1()
    for e in sorted(agac, key=lambda e: e["path"]):
        h.update(e["path"].encode() + b"\0" + e["sha"].encode() + b"\n")
    return h.hexdigest()


# Yerel kaynak tipleri (K-57): T7 = kullanıcının KENDİ yazdığı skiller (kendi/), T8 = GitHub'da olmayan, bir web sitesinden alınmış
# skiller (site/<ad>/). İkisi de GitHub'a sorulmaz, KAYIP sayılmaz, kaynak-cek.py ile ağsız çekilir. T8'in her skili için site-takip.json
# kaydı zorunludur (sahip, lisans, site adresi, izlenen dosyaların sha256'sı); site değişikliğini araclar/site-takip.py bildirir.
YEREL_TIPLER = ("T7", "T8")
ARSIVLENEN_TIPLER = ("T1", "T2", "T3", "T4", "T7", "T8")
YEREL_KLASOR = {"T7": "kendi", "T8": "site"}
SITE_TAKIP = "site-takip.json"
LISANSSIZ = ("yok", "NOASSERTION", "belirtilmemiş", "")


def yerel_gelistirici(kayit, bugun=None):
    """Yerel kaynak (T7/T8) için GitHub'sız geliştirici kaydı; ağ kullanılmaz. T7: sahibi kullanıcı, resmî kaynak sayılır.
    T8: kaynak düzeyinde sahip yoktur (skill başına sahip ve lisans site-takip.json'dan gelir: site_gelistirici)."""
    from datetime import date as _d
    bugun = bugun or _d.today().isoformat()
    site = kayit.get("tip") == "T8"
    return {"sahip": "site (skill başına)" if site else "kullanıcı", "sahip_tipi": "kisi", "sahip_url": "",
            "resmi_kaynak": not site, "yildiz": 0, "fork": 0, "acik_issue": 0, "son_guncelleme": bugun,
            "olusturulma": kayit.get("eklendi") or bugun,
            "lisans": "belirtilmemiş" if site else (kayit.get("lisans") or "belirtilmemiş"), "arsivlenmis": False,
            "aciklama": ("Web sitesinden alınan skiller (yerel kaynak site/, GitHub'sız)" if site
                         else "Kullanıcının kendi skilleri (yerel kaynak, GitHub'sız)"), "ana_sayfa": "",
            "katkici": 1, "izleyici": None, "commit_90g": 0, "son_surum": None}


def site_kayitlari(kok) -> dict:
    """site-takip.json -> {skill adı: kayıt}. Dosya yoksa ya da bozuksa boş sözlük (şemayı dogrula/site-takip denetler)."""
    try:
        d = json.loads((Path(kok) / SITE_TAKIP).read_text(encoding="utf-8"))
        return {s["skill"]: s for s in d.get("skiller", []) if isinstance(s, dict) and isinstance(s.get("skill"), str)}
    except (OSError, ValueError, AttributeError, TypeError):
        return {}


def _guven_lis(v):
    return 0 if (v or {}).get("lisans") in LISANSSIZ else 5


def _guven_res(v):
    return 5 if (v or {}).get("resmi_kaynak") else 3 if (v or {}).get("sahip_tipi") == "kurum" else 0


def site_gelistirici(gel, kayit):
    """Site skilinin (T8) geliştirici kaydı: kaynak düzeyindeki kaydın KOPYASI, sahip/lisans/site skill başına site-takip.json'dan.
    Güven puanının lisans ve resmî/kurum parçaları (gelistirici-bilgisi.guven_hesapla ile aynı kural) yeni değere göre düzeltilir.
    `gel` değiştirilmez (aynı kaynağın başka skillerine sızmasın)."""
    if not kayit:
        return gel
    yeni = dict(gel or {})
    yeni.update({"sahip": kayit.get("sahip") or "belirtilmemiş", "sahip_tipi": kayit.get("sahip_tipi") or "kisi",
                 "sahip_url": kayit.get("sahip_url") or "", "lisans": kayit.get("lisans") or "belirtilmemiş",
                 "resmi_kaynak": bool(kayit.get("resmi_kaynak", False)), "ana_sayfa": kayit.get("site") or "",
                 "aciklama": f"Web sitesinden alınan skill: {kayit.get('site') or '?'} (site-takip.json)"})
    gv = (gel or {}).get("guven")
    if gv:
        puan = max(0, gv["puan"] + _guven_lis(yeni) - _guven_lis(gel) + _guven_res(yeni) - _guven_res(gel))
        ayr = [x for x in gv.get("ayrinti", []) if not x.startswith(("lisans ", "resmî/kurum ", "skill başına sahip/lisans"))]
        ayr += [f"lisans {_guven_lis(yeni)}/5", f"resmî/kurum {_guven_res(yeni)}/5"]
        if kayit.get("site"):
            ayr.append("skill başına sahip/lisans: site-takip.json")
        yeni["guven"] = dict(gv, puan=puan, ayrinti=ayr,
                             derece="A" if puan >= 80 else "B" if puan >= 65 else "C" if puan >= 50 else "D")
    return yeni


def klasor_hash(klasor: Path) -> str:
    """Klasör içeriğinin kimliği: (göreli yol, git blob hash) listesinin sha256'sı."""
    h = hashlib.sha256()
    for f in onemli_dosyalar(klasor):
        h.update(str(f.relative_to(klasor)).encode())
        h.update(git_blob_hash(f.read_bytes()).encode())
    return h.hexdigest()


def skill_md_hash(klasor: Path):
    f = klasor / "SKILL.md"
    return git_blob_hash(f.read_bytes()) if f.exists() else None


def frontmatter(metin: str) -> dict:
    """SKILL.md başındaki YAML frontmatter'ı basitçe okur (üst düzey anahtarlar; çok satırlı değerler birleştirilir)."""
    m = re.match(r"^\ufeff?---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", metin, re.S)
    if not m:
        return {}
    sonuc, anahtar, blok = {}, None, []

    def kapat():
        if anahtar is not None:
            sonuc[anahtar] = " ".join(s.strip() for s in blok if s.strip()).strip().strip("'\"")

    for satir in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", satir)
        if km and not satir[:1].isspace():
            kapat()
            anahtar, deger = km.group(1), km.group(2).strip()
            blok = [] if deger in (">", "|", ">-", "|-", ">+", "|+", "") else [deger]
        elif anahtar is not None:
            blok.append(satir)
    kapat()
    return sonuc


# ------------------------------------------------------------------ frontmatter onarımı (kurulumda)
# Claude Code ve Codex skill'i SADECE dosyanın ilk satırında başlayan YAML frontmatter'daki description ile tanır ve
# tetikler. Arşivdeki orijinallere dokunulmaz; bozukluk kurulan kopyada düzeltilir (skill-ekle.py hazirla()).
FM_BASTA = re.compile(r"^(﻿?---[ \t]*(\r?\n))(.*?)(\r?\n---[ \t]*(?:\r?\n|$))", re.S)
FM_YORUM_ARKASINDA = re.compile(r"^(﻿?)((?:\s*<!--.*?-->)+)\s*?\r?\n(---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$))", re.S)
ACIKLAMA_SINIRI = 1024
ONARIM_SURUMU = "1"  # onarım mantığı değişirse artır: kilitteki 'onarim' izi değişir, --guncelle kurulumu yeniler


def _duz_deger_guvensiz(deger: str) -> bool:
    """Tırnaksız (plain) tek satırlık YAML değeri ayrıştırıcıyı bozar mı? (': ' ve ' #' en sık sebep)"""
    if not deger or deger[0] in "'\"|>":
        return False
    return (": " in deger or " #" in deger or deger.endswith(":") or deger[0] in "[]{}&*!%@`,?-"
            or deger.startswith(("- ", "? ")))


def frontmatter_teshis(metin: str) -> list:
    """Skill'in doğru durumda tetiklenmesini engelleyen frontmatter sorunları (YAML kütüphanesi gerektirmez)."""
    s = []
    m = FM_BASTA.match(metin)
    if not m:
        if FM_YORUM_ARKASINDA.match(metin):
            s.append("frontmatter dosya başında değil (önünde HTML yorumu var); araçlar description'ı göremez")
            m = FM_BASTA.match(FM_YORUM_ARKASINDA.sub(lambda x: x.group(1) + x.group(3), metin, count=1))
        else:
            return ["frontmatter yok"]
    satirlar = m.group(3).splitlines()
    for i, satir in enumerate(satirlar):
        dm = re.match(r"^description:[ \t]*(.*)$", satir)
        if not dm:
            continue
        deger = dm.group(1).strip()
        devam = i + 1 < len(satirlar) and satirlar[i + 1][:1].isspace() and satirlar[i + 1].strip()
        if not devam and _duz_deger_guvensiz(deger):
            s.append("description tırnaksız ve ': ' gibi YAML'ı bozan karakter içeriyor; frontmatter ayrıştırılamaz")
        break
    return s


def frontmatter_onar(metin: str, ad: str, aciklama=None):
    """Kurulan kopyanın frontmatter'ını araçların okuyacağı hale getirir. Döner: (yeni metin, yapılanlar).
    - Baştaki HTML yorumundan sonra gelen frontmatter dosyanın başına alınır (yorum korunur, frontmatter'ın altına iner).
    - aciklama verildiyse description onunla değiştirilir/eklenir (frontmatter yoksa oluşturulur).
    - Tırnaksız ve YAML'ı bozan tek satırlık description JSON tırnağıyla yazılır (içerik aynı kalır)."""
    yapilan = []
    nl = "\r\n" if "\r\n" in metin else "\n"
    ym = FM_YORUM_ARKASINDA.match(metin)
    if not FM_BASTA.match(metin) and ym:
        metin = ym.group(1) + ym.group(3) + ym.group(2).strip() + nl + nl + metin[ym.end():].lstrip("\r\n")
        yapilan.append("frontmatter dosya başına alındı")
    m = FM_BASTA.match(metin)
    if not m:
        if aciklama:
            metin = f"---{nl}name: {ad}{nl}description: {json.dumps(aciklama, ensure_ascii=False)}{nl}---{nl}{nl}" + metin
            yapilan.append("frontmatter eklendi")
        return metin, yapilan
    bas, govde, son = m.group(1), m.group(3), m.group(4)
    satirlar = govde.split(nl) if nl in govde else govde.split("\n")
    sira = next((i for i, x in enumerate(satirlar) if re.match(r"^description:", x)), None)
    if sira is not None:
        bitis = sira + 1
        while bitis < len(satirlar) and (satirlar[bitis][:1].isspace() or not satirlar[bitis].strip()):
            bitis += 1
        while bitis > sira + 1 and not satirlar[bitis - 1].strip():  # sondaki boş satırlar description'a ait değil
            bitis -= 1
        if aciklama:
            satirlar[sira:bitis] = [f"description: {json.dumps(aciklama, ensure_ascii=False)}"]
            yapilan.append("description değiştirildi")
        elif bitis == sira + 1:
            deger = satirlar[sira].split(":", 1)[1].strip()
            if _duz_deger_guvensiz(deger):
                satirlar[sira] = f"description: {json.dumps(deger, ensure_ascii=False)}"
                yapilan.append("description tırnaklandı")
    elif aciklama:
        ni = next((i + 1 for i, x in enumerate(satirlar) if re.match(r"^name:", x)), 0)
        satirlar.insert(ni, f"description: {json.dumps(aciklama, ensure_ascii=False)}")
        yapilan.append("description eklendi")
    if any("description" in y for y in yapilan):
        metin = bas + nl.join(satirlar) + son + metin[m.end():]
    return metin, yapilan


_TUM_SKILLER = [None]


def tum_skiller(skiller=None):
    """skiller verilmişse onu döner; verilmemişse registry.json'u süreç başına BİR kez okur (kurulum yolu çağıranları listeyi kendi geçirir)."""
    if skiller is not None:
        return skiller
    if _TUM_SKILLER[0] is None:
        _TUM_SKILLER[0] = (json_oku(REGISTRY) or {}).get("skiller", [])
    return _TUM_SKILLER[0]


def yol_izi(s: dict, skiller=None) -> str:
    """Kurulumda proje içi yola ÇEVRİLECEK kendi sabit yollarının parmak izi (yol_degerlendir(...)['cevrilecek']); çevrilecek yoksa ''.
    Yalnız arşiv verisinden deterministiktir (onek, kardeş kurulu durumu burada YOK: kardeş durumu kilidin 'kardes' alanındadır)."""
    if not s.get("yol") or not (KOK / s["yol"]).is_dir():
        return ""
    cevrilecek = yol_degerlendir(s, tum_skiller(skiller))["cevrilecek"]
    if not cevrilecek:
        return ""
    return hashlib.sha1("\n".join(sorted(f"{b['dosya']}\t{b['ham']}" for b in cevrilecek)).encode()).hexdigest()[:8]


def onarim_izi(s: dict, skiller=None):
    """Kurulan kopyaya uygulanan onarımın izi (frontmatter + yamalar + kendi sabit yollarının çevirisi; kilitte saklanır). Onarım yoksa None.
    Yol bileşeni YALNIZ çevrilecek kendi yolu olan skill'lerde eklenir: öteki skill'lerin izi eskisiyle birebir aynıdır (ONARIM_SURUMU değişmez)."""
    d = (s.get("aciklama_duzeltme") or {}).get("description")
    oto = [y for y in s.get("yapisal_sorunlar", []) if "dosya başında değil" in y or "tırnaksız" in y]
    yama = [f"{rel}:{git_blob_hash((YAMALAR / s['id'] / rel).read_bytes()) if (YAMALAR / s['id'] / rel).exists() else '-'}"
            for rel in sorted(((s.get("yama") or {}).get("dosyalar") or {}))]
    yol = yol_izi(s, skiller)
    if not d and not oto and not yama and not yol:
        return None
    return hashlib.sha1(f"{ONARIM_SURUMU}|{d or ''}|{'|'.join(oto)}|{'|'.join(yama)}{'|yol:' + yol if yol else ''}".encode()).hexdigest()[:12]


def yamalari_uygula(klasor: Path, s: dict) -> list:
    """registry 'yama' kaydındaki dosyaları kurulan kopyada yamalı halleriyle değiştirir. Sadece orijinal dosya yamanın
    yazıldığı sürümle AYNIYSA uygulanır (kaynak güncellendiyse yama atlanır; dogrula.py 'yama eskidi' der).
    Döner: [(yol, 'uygulandi' | 'eskidi' | 'yok')]"""
    sonuc = []
    for rel, orijinal_hash in sorted(((s.get("yama") or {}).get("dosyalar") or {}).items()):
        hedef, yama = klasor / rel, YAMALAR / s["id"] / rel
        if not hedef.is_file() or not yama.is_file():
            sonuc.append((rel, "yok"))
        elif git_blob_hash(hedef.read_bytes()) != orijinal_hash:
            sonuc.append((rel, "eskidi"))
        else:
            hedef.write_bytes(yama.read_bytes())
            sonuc.append((rel, "uygulandi"))
    return sonuc


# Kaynak repodaki git symlink'leri (ör. remotion-best-practices/remotion-create -> ../remotion-create) GitHub API'den düz
# metin dosyası olarak gelir: içinde sadece hedef yol yazar. Skill kökündeki "../<kardeş>" taslakları kardeş skill demektir.
SYMLINK_TASLAK = re.compile(r"^\.\./([\w.@+-]+)/?\s*$")


def symlink_taslaklari(klasor: Path) -> dict:
    """Skill kökündeki symlink taslakları: {dosya adı: kardeş skill adı}."""
    sonuc = {}
    for f in klasor.iterdir():
        if f.is_file() and not f.is_symlink() and f.stat().st_size < 300 and not f.suffix:
            m = SYMLINK_TASLAK.match(f.read_text(encoding="utf-8", errors="replace"))
            if m and m.group(1) == f.name:
                sonuc[f.name] = m.group(1)
    return sonuc


def taslak_baglantilarini_cevir(metin: str, taslaklar, derinlik: int = 0) -> str:
    """Skill kökündeki taslak klasörüne giden bağlantıları (./X/…, X/…) kardeş skill yoluna (../X/…) çevirir."""
    if not taslaklar:
        return metin
    adlar = "|".join(re.escape(a) for a in sorted(taslaklar, key=len, reverse=True))
    geri = "../" * derinlik
    return re.sub(r"(\]\(|`)" + re.escape(geri) + r"(?:\./)?(" + adlar + r")/", lambda m: m.group(1) + geri + "../" + taslaklar[m.group(2)] + "/", metin)


def boyut(klasor: Path) -> int:
    return sum(p.stat().st_size for p in klasor.rglob("*") if p.is_file())


def global_durum(ad: str, ana_hash: str) -> dict:
    """Aynı isimli skill global klasörlerde var mı, TÜM klasör içeriği aynı mı? (salt okuma, anlık)"""
    durum = {}
    for arac, klasor in GLOBAL_KLASORLER.items():
        d = klasor / ad
        if (d / "SKILL.md").exists():
            try:
                durum[arac] = "ayni" if klasor_hash(d.resolve()) == ana_hash else "farkli"
            except OSError:
                durum[arac] = "okunamadi"
    return durum


TREND_BONUS = {"trendde": 10, "yakinda": 6, "gecmiste": 2}  # değerlendirme puanına (0-100) eklenen


def trend_durumu(repo: str, trend: dict):
    """Repo GitHub Trending'de görüldü mü? trendde = son taramada · yakinda = son 90 gün · gecmiste = daha eski."""
    g = (trend or {}).get("gecmis", {}).get(repo)
    if not g:
        return None
    from datetime import date
    # BUGÜNÜN tarihine göre: tarama durursa bonus sönmeli ("trendde" sadece son tarama taze ve repo o taramadaysa)
    bugun = date.today()
    gun = (bugun - date.fromisoformat(g["son"])).days
    taze_tarama = (bugun - date.fromisoformat(trend["son_tarama"])).days <= 14
    seviye = "trendde" if (g["son"] == trend["son_tarama"] and taze_tarama) else "yakinda" if gun <= 90 else "gecmiste"
    return {"seviye": seviye, "son": g["son"], "ilk": g["ilk"], "gorulme": g["gorulme"],
            "en_iyi": g.get("en_iyi", {})}


_TAKMA_ADLAR = None


def repo_takma_adlari():
    """kaynaklar.json -> repolar[].eski_adlar: {eski ad (küçük harf): güncel ad}.
    Repo GitHub'da taşınınca/yeniden adlandırılınca kaynaklar.json'da 'repo' güncellenir, eski ad 'eski_adlar'a yazılır.
    Kurulu projelerin kilit dosyaları eski adı taşımaya devam eder; kaynak eşleşmesi bu haritayla yapılır."""
    harita = {}
    for k in (json_oku(KAYNAKLAR, {}) or {}).get("repolar", []):
        for e in k.get("eski_adlar", []):
            harita[e.lower()] = k["repo"]
    return harita


def repo_guncel(repo):
    """Eski (taşınmış) repo adını güncel ada çevirir; bilinmiyorsa aynen döner."""
    global _TAKMA_ADLAR
    if _TAKMA_ADLAR is None:
        _TAKMA_ADLAR = repo_takma_adlari()
    return _TAKMA_ADLAR.get((repo or "").lower(), repo)


# ------------------------------------------------------------------ sabit yol taraması (salt okuma, ağ yok)
# Bir skill'in metinlerinde "bilgisayar geneli klasör" / "eklenti kökü" / kardeş skill yolları var mı? Kurulum ön kontrolü
# (skill-ekle.py) ve araclar/yol-tara.py bunu kullanır. Kurulan kopyada yol çevirisi (sonraki aşama) BU arayüzü tüketir:
# yol_taramasi() (düşük seviye), skill_yol_taramasi() (kardeş çözümlü), istisna_uygula(), yol_degerlendir() (ön kontrol satırları).
# Prensip: "dar çevir, geniş uyar" — yalnız `cevrilebilir` bulgular otomatik çevrilir; gerisi UYARI/BİLGİ olarak raporlanır.
YOL_ISTISNA = KOK / "yol-istisnalari.json"
YOL_METIN_UZANTI = (".md", ".mdx", ".txt", ".sh", ".bash", ".zsh", ".cmd", ".ps1", ".py", ".js", ".mjs", ".cjs", ".ts",
                    ".json", ".yaml", ".yml", ".toml", "")  # "" = uzantısız dosya
GENEL_KLASOR_ADLARI = {"skill", "skills", "src", "web", "ios", "android", "setup", "main", "app", "core", "docs", "lib", "scripts",
                       "references", "assets", "templates", "bin", "tools", "utils", "common", "shared", "base", "default", "example",
                       "examples", "test", "tests", "plugin", "plugins", "agent", "agents", "cli", "server", "client", "api", "backend",
                       "frontend", "mobile", "desktop", "public", "dist", "build", "config", "data", "resources", "rules", "commands",
                       "hooks", "prompts", "workflows", "general", "generic", "index", "template", "root", "skillset"}
_YOL_KOD_UZANTI = {".py", ".js", ".mjs", ".cjs", ".ts", ".sh", ".bash", ".zsh", ".ps1", ".cmd"}
_YOL_ENGEL_SIRASI = ("dokuman", "kurucu-dosya", "kurulum-komutu", "cok-kok", "kullanim-metni", "ornek-satir", "kalan-bos", "dosya-yok",
                     "karisik-dosya", "betik-ici")
YOL_TARAMA_SINIRLARI = {"dosya_bayt": 2_000_000, "satir_karakter": 20_000, "dosya_bulgu": 2000, "atif_bayt": 262_144}  # dayanıklılık: kötü niyetli/bozuk girdi taramayı kilitlemesin
_YOL_GIZLI_AD = re.compile(r"^(?:id_(?:rsa|dsa|ecdsa|ed25519)\b.*|\.npmrc|\.netrc|\.pypirc|\.git-credentials|credentials(?:\.\w+)?|.*\.(?:p12|pfx|keystore)"
                           r"|.*secrets?\.(?:json|ya?ml|toml|txt))$", re.I)
_YOL_AILESI = {"genel-kendi", "genel-baska", "eklenti-kendi", "eklenti-kardes", "kardes-goreli", "skil-disi-yol"}
_EV = (r"(?:(?:~|\$HOME|\$\{HOME\}|/Users/[\w.-]+|/home/[\w.-]+)/\.(?:claude|agents|codex)"
       r"|\$\{(?:CODEX_HOME|CLAUDE_DIR|CLAUDE_CONFIG_DIR)(?::-[^}\s]*)?\}|\$(?:CODEX_HOME|CLAUDE_DIR)(?!\w))")
_KALAN = r"(?:/[^\s`'\"<>)\]|,;(\\]*)?"
_GENEL = re.compile(r"(?<![\w$./~-])(?P<on>" + _EV + r"/skills)/(?P<ad>[A-Za-z0-9_.@+*-]+)(?P<son>[<>$\[\]{}]?)(?P<k>" + _KALAN + ")")
_EKLENTI = re.compile(r"(?:\$\{CLAUDE_PLUGIN_ROOT\}|\$CLAUDE_PLUGIN_ROOT(?!\w))(?P<k>" + _KALAN + ")")
_EKLENTI_SKILL = re.compile(r"^/?(?:\.(?:claude|agents|codex)/)?skills/(?P<ad>[^/]+)(?P<k>/.*)?$")
_SKIL_DIZIN = re.compile(r"(?:\$\{CLAUDE_SKILL_DIR\}|\$CLAUDE_SKILL_DIR(?!\w))(?P<n>(?:/\.\.(?![\w.-]))+)(?P<k>" + _KALAN + ")")
_GORELI = re.compile(r"(?<![\w./~$}-])(?<!\]\()(?P<n>(?:\.\./)+)(?P<ad>[A-Za-z0-9_.@+-]+)/(?P<k>[^\s`'\"<>)\]|,;(\\]*)")
_YAZAR = re.compile(r"npx\s+(?:-y\s+|--yes\s+)?skills(?:@[\w.-]+)?\s+(?:add|update)\b[^\n]{0,400}?(?:\s-g\b|--global\b)")
_YAZAR_SKILL = re.compile(r"--skill[= ]+[\"']?([^\s\"']+)")
_KOPYA = re.compile(r"(?P<v>\b(?:cp|mv|rsync)\s+\S|\bln\s+-\w*s|\bmkdir\s+-p\b|\bgit\s+clone\b|\binstall\s+-\w)[^\n]{0,300}?"
                    r"(?P<t>" + _EV + r"/(?:skills|agents)\b)")
# genel klasöre yazan öteki kalıplar: --dest/--target/--output <ev>/skills (--root OKUMA kökü olduğundan yok) ve "write|save|copy|create … to <ev>/skills"
_KOPYA2 = re.compile(r"(?P<v>--(?:dest|target|output|out)(?:=|\s+)[\"'`]?)(?P<t>" + _EV + r"/(?:skills|agents)\b)"
                     r"|(?P<v2>\b(?:write|save|copy|create)\b[^\n]{0,60}?\b(?:to|into)\s+[\"'`]?)(?P<t2>" + _EV + r"/(?:skills|agents)\b)", re.I)
_ORNEK_SATIR = re.compile(r"\bin most installs\b|\bfor (?:example|instance)\b|\be\.g\.|\bsuch as\b|\bUnder\s+\S+\s+that is\b|\bor example\b|\börneğin\b|\bmesela\b", re.I)
_KULLANIM_SATIR = re.compile(r"^\s*(?:@?echo|printf|print\(|console\.(?:log|error|warn)|puts|Write-Host|Write-Output|echo\.)\b")
_ALTERNATIF = re.compile(r"\bor\b[^\n]{0,80}(?:~/|\$HOME|\$\{HOME\}|\bPATH\b|/usr/|\./|\.\./)|(?:when|if)\s+(?:it'?s\s+)?(?:installed|running)\s+as\s+(?:a\s+)?plugin", re.I)
_ATAMA = re.compile(r"[A-Za-z_]\w*=[\"']?$")
_KURULUM_KOMUTU = re.compile(r"\bgit\s+clone\b|\bln\s+-\w+|\bmkdir\s+-p\b|\bcp\s+-\w+|\bcurl\b[^\n]*?\s-o\b|\bwget\b[^\n]*?\s-O\b"
                             r"|\brm\s+-\w*r\w*|\bnpx\s+(?:-y\s+|--yes\s+)?skills(?:@[\w.-]+)?\s+(?:add|update)\b")
_KOK_YERLESIM = re.compile(r"\.(?P<a>[a-z][\w-]*)/skills\b|\.config/(?P<b>[a-z][\w-]*)/skills\b|\$\{?(?P<c>CODEX_HOME|CLAUDE_DIR)\}?/skills\b")
_PROJE_ICI = re.compile(r"(?:(?<![\w$}~/])|(?<=\./))\.(?:claude|agents|codex)/skills/[\w@.+*-]")
_KURULUM_BASLIK = re.compile(r"install|kurulum|setup|getting started|quick ?start", re.I)
_DOKUMAN_AD = re.compile(r"^(?:README|NOTICE|CONTRIBUTING|CHANGELOG|LICENSE)|^(?:AGENTS|CLAUDE)\.md$", re.I)
_DIL = ("ar bg bn ca cs da de el es fa fi fr he hi hu id it ja ko ms nl no pl pt ru sv th tr uk vi zh zh-cn zh-tw zh-hans zh-hant pt-br "
        "es-es fr-fr de-de ja-jp ko-kr ru-ru en-us en-gb").split()
_DIL_KLASOR = {d for d in _DIL} | {d.replace("-", "_") for d in _DIL} | {"i18n", "l10n", "locales", "translations", "lang", "languages"}
_DIL_DOSYA = re.compile(r"[._-](?:" + "|".join(sorted((d.replace("-", "[-_]") for d in _DIL), key=len, reverse=True)) + r")\.[A-Za-z]+$", re.I)
_ATIF_PARCA = re.compile(r"[\w@+./-]+")  # doğrusal: yol karakterlerinden oluşan parça (dosya/dizin ayrımı sonradan, regex geri izlemesiz)


def _yol_kes(ham: str) -> str:
    """Yakalanan yol parçasını temizler (baştaki '/' korunur): '…' ve '...' sonrası kesilir; '#bağ', '?sorgu', ':satır' ve sondaki
    .,;:*)'\"`_ ile '/' atılır."""
    k = ham.split("…")[0].split("...")[0]
    k = re.split(r"[#?]", k)[0]
    k = re.sub(r":\d+(?::\d+)?$", "", k)
    return k.rstrip(".,;:*)'\"`_/")


def _kalan_temizle(ham: str) -> str:
    return _yol_kes(ham).strip("/")


def _var_bak(klasor: Path, kalan: str):
    """kalan klasor içinde var mı? True/False; joker ('*' '?') glob ile; değişken/'..' içeriyorsa None. Boş kalan = klasörün kendisi."""
    if not kalan:
        return klasor.is_dir()
    if ".." in kalan.split("/") or any(c in kalan for c in "${}<>[]"):
        return None
    try:
        if any(c in kalan for c in "*?"):
            return any(klasor.glob(kalan))
        return (klasor / kalan).exists()
    except (OSError, ValueError):
        return None


def _satir_haritasi(metin: str):
    return [m.start() for m in re.finditer("\n", metin)]


def _satir_no(yeni_satir, pos):
    import bisect
    return bisect.bisect_left(yeni_satir, pos) + 1


def _satir_metni(metin: str, yeni_satir, pos):
    import bisect
    i = bisect.bisect_left(yeni_satir, pos)
    bas = yeni_satir[i - 1] + 1 if i else 0
    son = yeni_satir[i] if i < len(yeni_satir) else len(metin)
    return metin[bas:son], bas


def _atif_kumesi(klasor: Path, dosyalar):
    """SKILL.md'nin andığı göreli dosya yolları (ve 'dizin/' diye anılan dizinlerin altındakiler). Doğrusal zamanlı (regex geri izlemesi
    yok); SKILL.md 256 KB'dan büyükse atıf çıkarılmaz (kök SKILL.md yine 'ajan' sayılır, öteki dosyalar atıfsız = 'dokuman')."""
    sm = klasor / "SKILL.md"
    try:
        if not sm.is_file() or sm.stat().st_size > YOL_TARAMA_SINIRLARI["atif_bayt"]:
            return set()
        metin = sm.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()
    belirteclar, dizinler = set(), set()
    for tok in _ATIF_PARCA.findall(metin):
        for parca in re.split(r"/{2,}", tok):
            dizin_mi = parca.endswith("/") and len(parca.strip("/")) > 0
            p = parca.strip("/")
            if p.startswith("./"):
                p = p[2:]
            if not p:
                continue
            (dizinler if dizin_mi else belirteclar).add(p.rstrip(".") if not dizin_mi else p)
    sonuc = set()
    for rel in dosyalar:
        parcalar = rel.split("/")
        if rel in belirteclar or any("/".join(parcalar[:i]) in dizinler for i in range(1, len(parcalar))):
            sonuc.add(rel)
    return sonuc


def _dosya_sinifi(rel: str, atiflar, betik: bool) -> str:
    """'ajan' (ajanın okuyup çalıştırdığı), 'kurucu' (install/setup/bootstrap*), 'dokuman' (geri kalan)."""
    parca = rel.split("/")
    ad = parca[-1]
    if ad.lower().startswith(("install", "setup", "bootstrap")):
        return "kurucu"
    if rel == "SKILL.md":
        return "ajan"
    # dil kuralı yalnız metin dosyalarına (.md .mdx .txt) uygulanır: dil kodu adlı (it, no, id …) kod dosyası ya da klasörü sessizleşmez
    metin_dosyasi = ad.lower().endswith((".md", ".mdx", ".txt"))
    if _DOKUMAN_AD.match(ad) or (metin_dosyasi and (any(p.lower() in _DIL_KLASOR for p in parca[:-1]) or _DIL_DOSYA.search(ad))):
        return "dokuman"
    if ad == "SKILL.md":
        return "ajan"
    if any(p.lower() in ("tests", "test", "__tests__", "fixtures") for p in parca[:-1]):
        return "dokuman"  # ajan test dosyası çalıştırmaz
    if len(parca) > 1 and parca[0] in ("scripts", "bin", "templates", "agents"):
        return "ajan"
    if len(parca) == 1 and betik:
        return "ajan"
    return "ajan" if rel in atiflar else "dokuman"


def _ad_norm(ad):
    return (ad or "").strip().lower()


def _hedef_turu(ad: str, son: str, adlar, bilinen, aile):
    """Yakalanan skill adının türü: genel-kalip / ortak-dizin / ornek-metin / '<aile>-kendi' / '<aile>-baska' (aile: genel|eklenti)."""
    ad2 = ad.rstrip(".")
    if not ad2:
        return None, None
    if "*" in ad2 or ad2.endswith("-") or son:
        return "genel-kalip", ad2
    if ad2.startswith("_"):
        return "ortak-dizin", ad2
    d = ad2.lower()
    if d.startswith("."):  # gizli sistem klasörü (.system/…): kütüphanede olması beklenmez ama gerçek bir bağımlılık
        return ("genel-baska" if aile == "genel" else "eklenti-kardes"), ad2
    if d in adlar:
        return f"{aile}-kendi", ad2
    if bilinen is not None and d not in bilinen:
        return "ornek-metin", ad2
    return ("genel-baska" if aile == "genel" else "eklenti-kardes"), ad2


def _yol_dosyalari(klasor: Path) -> list:
    """Yol taramasının okuduğu dosyalar: onemli_dosyalar içinden ≤2 MB, uzantısı YOL_METIN_UZANTI'da; .env*/*.pem/*.key, gizli adlı dosyalar
    ve symlink'ler (klasör dışına işaret edebilir) okunmaz."""
    dosyalar = []
    for f in onemli_dosyalar(klasor):
        if (f.suffix.lower() not in YOL_METIN_UZANTI or f.name.startswith(".env") or f.name.endswith((".pem", ".key"))
                or _YOL_GIZLI_AD.match(f.name) or f.is_symlink()):
            continue
        try:
            if f.stat().st_size <= YOL_TARAMA_SINIRLARI["dosya_bayt"]:
                dosyalar.append(f)
        except OSError:
            continue
    return dosyalar


def yol_dosya_sinifi_haritasi(klasor) -> dict:
    """{göreli dosya: (sınıf 'ajan'|'kurucu'|'dokuman', betik mi)} — yol_taramasi ile AYNI dosya seçimi ve sınıflama (kurulumdaki dar geçiş kullanır)."""
    klasor = Path(klasor)
    dosyalar = _yol_dosyalari(klasor)
    atiflar = _atif_kumesi(klasor, [x.relative_to(klasor).as_posix() for x in dosyalar])
    sonuc = {}
    for f in dosyalar:
        rel = f.relative_to(klasor).as_posix()
        betik = f.suffix.lower() in _YOL_KOD_UZANTI
        if not betik and f.suffix == "":
            try:
                with f.open("rb") as fh:
                    betik = fh.read(2) == b"#!"
            except OSError:
                continue
        sonuc[rel] = (_dosya_sinifi(rel, atiflar, betik), betik)
    return sonuc


def yol_taramasi(klasor, adlar, bilinen_adlar=None) -> list:
    """Bir skill klasöründeki sabit yol bağımlılıkları (SAF: yalnız verilen klasörü okur; ağ yok; arşivde deterministik).
    klasor: skill klasörü · adlar: skill'in KENDİ adları (skill_adlari) · bilinen_adlar: kütüphanedeki tüm skill adları
    (verilirse kütüphanede hiç olmayan hedefler 'ornek-metin' sayılır, UYARI üretmez).

    Taranan dosyalar: onemli_dosyalar(klasor) içinden ≤2 MB, uzantısı YOL_METIN_UZANTI'da, .env*/*.pem/*.key hariç.
    Bulgu sözlüğü: tur, dosya (posix göreli), satir (1'den), ham (dosyadaki metin), hedef (skill adı ya da None), kalan (skill-içi yol,
    '' olabilir), var (True/False/None), sinif ('ajan'|'dokuman'|'kurucu'), engel (otomatik çevrilmeme nedeni ya da None),
    cevrilebilir (bool), engeller (uygulanabilir tüm nedenler, öncelik sırasıyla; ayrıntı için); genele-yazar bulgularında ayrıca
    alt: 'kurulum-bandi' = markdown dosyada "Install/Kurulum…" başlığı altında ve --skill değerleri (varsa) skill'in kendi adlarından biri;
    aksi hâlde (başka skill kuruluyor, betik dosyası, başka başlık) 'ajan-adimi'.
    Türler: genel-kendi, genel-baska, ornek-metin, ortak-dizin, genel-kalip, eklenti-kendi, eklenti-kardes, eklenti-kok-yol,
    eklenti-kok-anma, skil-disi-yol, kardes-goreli, genele-kopyalar, genele-yazar. Ev önekleri: ~ $HOME ${HOME} $CODEX_HOME
    ${CODEX_HOME} $CLAUDE_DIR /Users/<ad> /home/<ad> (~, $HOME, /Users, /home için '.claude|.agents|.codex' klasörü zorunlu).
    engel öncelik sırası: dokuman, kurucu-dosya, kurulum-komutu, cok-kok, kullanim-metni (betikte echo/printf/print satırı: kullanım ipucu),
    ornek-satir ("in most installs", "for example", "e.g." … açıklama satırı), kalan-bos, dosya-yok, karisik-dosya (aynı dosyada proje içi
    .claude/skills yolu VAR ya da dosya bir kurulum tarifi: genele-kopyalar / kurulum komutu içeriyor), betik-ici.
    Ek bayraklar (engel dışı): 'atama' (kalan-bos kendi yolu bir değişkene atanıyor: SKILL_DIR="~/.claude/skills/<ad>"), 'alternatif'
    (satırda "… or ~/…" / "when installed as a plugin" seçenekleri: eklenti-kok-yol ve kendi/başka yolları için).
    Dayanıklılık (YOL_TARAMA_SINIRLARI): dosya başına en çok 2000 bulgu, 20 000 karakterden uzun satırların kuyruğu atılır, SKILL.md atıf
    taraması için 256 KB'a kadar okunur; symlink'ler ve gizli adlı dosyalar (id_rsa*, .npmrc, .netrc, credentials*, *secret*.json …) okunmaz.
    Kapsam dışı: kodda Path.home()/".agents"/"skills" gibi kurulan yollar, öneksiz göreli yollar (skills/<ad>/…) ve .copilot gibi başka kökler.
    cevrilebilir = engel yok ve var True ve kalan boş değil (ve tür bir yol ailesinden). Kardeş türlerinde var burada None kalır:
    skill_yol_taramasi kardeşin arşivine bakarak doldurur."""
    klasor = Path(klasor)
    adlar = {_ad_norm(a) for a in adlar if a}
    bilinen = bilinen_adlar if bilinen_adlar is None or isinstance(bilinen_adlar, frozenset) else frozenset(_ad_norm(a) for a in bilinen_adlar)
    dosyalar = _yol_dosyalari(klasor)
    atiflar, bulgular = None, []
    for f in dosyalar:
        rel = f.relative_to(klasor).as_posix()
        try:
            ham_bayt = f.read_bytes()
            if b"\0" in ham_bayt or not any(k in ham_bayt for k in (b"/skills", b"/agents", b"PLUGIN_ROOT", b"SKILL_DIR", b"../", b"npx")):
                continue
            metin = ham_bayt.decode("utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        sk = YOL_TARAMA_SINIRLARI["satir_karakter"]
        if len(metin) > sk and any(len(x) > sk for x in metin.split("\n")):
            metin = "\n".join(x[:sk] for x in metin.split("\n"))  # aşırı uzun satır (gömülü base64/minify): satır no korunur, kuyruk atılır
        if atiflar is None:
            atiflar = _atif_kumesi(klasor, [x.relative_to(klasor).as_posix() for x in dosyalar])
        betik = f.suffix.lower() in _YOL_KOD_UZANTI or (f.suffix == "" and metin.startswith("#!"))
        sinif = _dosya_sinifi(rel, atiflar, betik)
        derinlik = rel.count("/")
        yeni = _satir_haritasi(metin)
        yerel = []
        satir_onb = {}  # satır başı konumu -> (kurulum komutu başlangıçları, yerleşim kökleri, açıklama/kullanım/alternatif bayrakları)
        kopya_satir = set()

        class _Doldu(Exception):
            pass

        def ekle(pos, tur, ham, hedef=None, kalan="", var=None, alt=None):
            if len(yerel) >= YOL_TARAMA_SINIRLARI["dosya_bulgu"]:
                raise _Doldu
            satir, bas = _satir_metni(metin, yeni, pos)
            b = {"tur": tur, "dosya": rel, "satir": _satir_no(yeni, pos), "ham": ham, "hedef": hedef, "kalan": kalan, "var": var,
                 "sinif": sinif, "engel": None, "cevrilebilir": False, "engeller": []}
            if alt:
                b["alt"] = alt
            if tur in _YOL_AILESI or tur == "eklenti-kok-yol":
                if bas not in satir_onb:
                    satir_onb[bas] = ([m.start() for m in _KURULUM_KOMUTU.finditer(satir)],
                                      len({(m.group("a") or m.group("b") or m.group("c")).lower().replace("codex_home", "codex").replace("claude_dir", "claude")
                                           for m in _KOK_YERLESIM.finditer(satir)}),
                                      bool(_ORNEK_SATIR.search(satir)), bool(betik and _KULLANIM_SATIR.match(satir)), bool(_ALTERNATIF.search(satir)))
                komutlar, kok_say, ornek, kullanim, alternatif = satir_onb[bas]
                if alternatif:
                    b["alternatif"] = True  # "… or ~/x, or ${CLAUDE_PLUGIN_ROOT}/…" gibi: birçok seçenekten biri
            if tur in _YOL_AILESI:
                if any(k < pos - bas for k in komutlar):
                    b["engeller"].append("kurulum-komutu")
                if kok_say >= 2:
                    b["engeller"].append("cok-kok")
                if kullanim:
                    b["engeller"].append("kullanim-metni")
                if ornek:
                    b["engeller"].append("ornek-satir")
                if not kalan:
                    b["engeller"].append("kalan-bos")
                    if _ATAMA.search(satir[:pos - bas]):
                        b["atama"] = True  # SKILL_DIR="~/.claude/skills/<ad>" gibi: sonraki satırlar bu değişkenle betik çalıştırabilir
            yerel.append(b)

        try:
            for m in (_GENEL.finditer(metin) if "/skills/" in metin else ()):
                tur, ad = _hedef_turu(m.group("ad"), m.group("son"), adlar, bilinen, "genel")
                if not tur:
                    continue
                on = metin[m.start():m.start("ad")] + ad
                kalan = "" if tur == "genel-kalip" else _kalan_temizle(m.group("k"))
                ekle(m.start(), tur, on + ("/" + kalan if kalan else ""), ad, kalan, _var_bak(klasor, kalan) if tur == "genel-kendi" else None)
            for m in (_EKLENTI.finditer(metin) if "PLUGIN_ROOT" in metin else ()):
                tam = _yol_kes(m.group("k") or "")
                on = metin[m.start():m.start("k")]
                sm = _EKLENTI_SKILL.match(tam)
                if sm and not sm.group("ad").startswith(".") and not (not sm.group("k") and re.search(r"\.[A-Za-z0-9]{1,5}$", sm.group("ad"))):
                    ad_ham = sm.group("ad")
                    if re.fullmatch(r"[A-Za-z0-9_.@+*-]+", ad_ham):
                        tur, ad = _hedef_turu(ad_ham, "", adlar, bilinen, "eklenti")
                    else:  # <ad> / ${ad} yer tutucusu
                        tur, ad = "genel-kalip", ad_ham
                    kalan = "" if tur == "genel-kalip" else _kalan_temizle(sm.group("k") or "")
                    ekle(m.start(), tur, on + tam, ad, kalan, _var_bak(klasor, kalan) if tur == "eklenti-kendi" else None)
                elif tam.strip("/") in ("skills", ".claude/skills") and metin[m.end("k"):m.end("k") + 1] in ("<", "{", "$", "[", "*"):
                    ekle(m.start(), "genel-kalip", on + tam, None, "")  # skills/<ad>/… yer tutucusu
                else:
                    ekle(m.start(), "eklenti-kok-yol" if tam.strip("/") else "eklenti-kok-anma", on + tam, None, tam.strip("/"))
            for m in (_SKIL_DIZIN.finditer(metin) if "SKILL_DIR" in metin else ()):
                tam = _yol_kes(m.group("k") or "").strip("/")
                hedef, kalan = (tam.partition("/")[0] or None, tam.partition("/")[2]) if m.group("n").count("/..") == 1 else (None, tam)
                ekle(m.start(), "skil-disi-yol", metin[m.start():m.start("k")] + ("/" + tam if tam else ""), hedef, kalan)
            for m in (_GORELI.finditer(metin) if "../" in metin else ()):
                ad = m.group("ad").rstrip(".")
                if m.group("n").count("../") != derinlik + 1 or not ad or _ad_norm(ad) in adlar:
                    continue  # skill içinde kalıyor / daha yukarı çıkıyor / kendi klasörü: kardeş değil
                if bilinen is not None and _ad_norm(ad) not in bilinen and not ad.startswith("_"):
                    continue  # kütüphanede böyle skill yok: gösterge değil, sıradan göreli yol (../node_modules/…) — sayılmaz bile
                kalan = _kalan_temizle("/" + m.group("k"))
                ekle(m.start(), "ortak-dizin" if ad.startswith("_") else "kardes-goreli", metin[m.start():m.start("k")] + kalan, ad, kalan)
            basliklar = None
            for m in (_YAZAR.finditer(metin) if "npx" in metin else ()):
                if basliklar is None:  # başlık konumları dosya başına BİR kez; son başlık bisect ile
                    basliklar = [(x.start(), x.group(1)) for x in re.finditer(r"^#{1,6}[ \t]+(.*)$", metin, re.M)] if not betik else []
                    baslik_pos = [x[0] for x in basliklar]
                import bisect
                i = bisect.bisect_left(baslik_pos, m.start())
                satir_sonu = metin.find("\n", m.start())
                skiller_ = _YAZAR_SKILL.findall(metin[m.start():satir_sonu if satir_sonu >= 0 else len(metin)])
                # kurulum bandı: markdown dosyada, "Install/Kurulum…" başlığı altında ve yalnız kendi skill'ini kuruyorsa (--skill başka bir adı gösteriyorsa gerçek bağımlılık)
                band = bool(i and _KURULUM_BASLIK.search(basliklar[i - 1][1]) and all(_ad_norm(x) in adlar for x in skiller_))
                ekle(m.start(), "genele-yazar", m.group(0), alt="kurulum-bandi" if band else "ajan-adimi")
            for m in (_KOPYA.finditer(metin) if "/skills" in metin or "/agents" in metin else ()):
                kopya_satir.add(_satir_no(yeni, m.start()))
                ekle(m.start(), "genele-kopyalar", metin[m.start("v"):m.end("t")])
            for m in (_KOPYA2.finditer(metin) if "/skills" in metin or "/agents" in metin else ()):
                bas_, son_ = (m.start("v"), m.end("t")) if m.group("v") else (m.start("v2"), m.end("t2"))
                if _satir_no(yeni, bas_) in kopya_satir:
                    continue
                kopya_satir.add(_satir_no(yeni, bas_))
                ekle(bas_, "genele-kopyalar", metin[bas_:son_])
        except _Doldu:
            pass  # bir dosyada en çok dosya_bulgu bulgu: sonrası atlanır (bkz. YOL_TARAMA_SINIRLARI)
        proje_ici = bool(_PROJE_ICI.search(metin)) and any(x["tur"] in ("genel-kendi", "genel-baska") for x in yerel)
        # kurulum anlatan dosya (ln -s / cp / mkdir -p / git clone … genel klasör): aynı dosyadaki sabit yollar kurulum tarifinin parçası, çevrilmez
        kurulum_anlatimi = any(x["tur"] == "genele-kopyalar" or "kurulum-komutu" in x["engeller"] for x in yerel)
        for b in yerel:
            if b["tur"] in _YOL_AILESI:
                b["engeller"] = (["dokuman"] if sinif == "dokuman" else ["kurucu-dosya"] if sinif == "kurucu" else []) + b["engeller"]
                if proje_ici or kurulum_anlatimi:
                    b["engeller"].append("karisik-dosya")
                if betik:
                    b["engeller"].append("betik-ici")
            bulgular.append(b)
    for b in bulgular:
        _engel_hesapla(b)
    bulgular.sort(key=lambda b: (b["dosya"], b["satir"], b["tur"], b["ham"]))
    return bulgular


def _engel_hesapla(b: dict):
    """engel = uygulanabilir nedenlerin öncelik sırasındaki ilki (var False ise 'dosya-yok' da aday); cevrilebilir buna bağlı."""
    nedenler = set(b.get("engeller", []))
    if b["var"] is False and b["tur"] in _YOL_AILESI:
        nedenler.add("dosya-yok")
    b["engel"] = next((n for n in _YOL_ENGEL_SIRASI if n in nedenler), None)
    b["cevrilebilir"] = bool(b["tur"] in _YOL_AILESI and b["engel"] is None and b["var"] is True and b["kalan"])


_SKILLER_INDEKS = [None, 0, None]  # (skiller listesi, uzunluk, indeks): kardeş/bilinen ad aramaları için tek seferlik


def _skill_ham_adlari(s: dict) -> set:
    """Skill'in dışarıdan anılabilen adları (küçük harf): ad (@kaynak eksiz), klasor_adi ve kaynak_yol'un son klasörü (genel klasör adları hariç)."""
    adlar = {_ad_norm(str(s.get("ad", "")).split("@")[0])}
    for x in (s.get("klasor_adi"), Path(s.get("kaynak_yol") or "").name):
        if x and _ad_norm(x) not in GENEL_KLASOR_ADLARI:
            adlar.add(_ad_norm(x))
    adlar.discard("")
    return adlar


def _skiller_indeksi(skiller):
    if _SKILLER_INDEKS[0] is not skiller or _SKILLER_INDEKS[1] != len(skiller):
        repolar, bilinen = {}, set()
        for s in skiller:
            ad = _skill_ham_adlari(s)
            repolar.setdefault(s.get("repo"), []).append((s, ad))
            bilinen |= ad
        _SKILLER_INDEKS[:] = [skiller, len(skiller), (repolar, frozenset(bilinen))]
    return _SKILLER_INDEKS[2]


def skill_adlari(s: dict, skiller=None) -> set:
    """Skill'in KENDİ adları (küçük harf): ad (@kaynak eksiz), klasor_adi ve kaynak_yol'un son klasörü (ikisi de genel klasör adı
    değilse: skill, src, web, setup, main, app, core, docs, lib … GENEL_KLASOR_ADLARI) ve reponun son bileşeni — yalnız AYNI
    repodaki başka hiçbir skill o adı taşımıyorsa (skiller verilmezse repo adı eklenmez)."""
    adlar = _skill_ham_adlari(s)
    if skiller is not None and s.get("repo"):
        repo_ad = _ad_norm(s["repo"].split("/")[-1])
        if repo_ad and repo_ad not in GENEL_KLASOR_ADLARI and not any(
                x["id"] != s["id"] and repo_ad in ad for x, ad in _skiller_indeksi(skiller)[0].get(s["repo"], [])):
            adlar.add(repo_ad)
    return adlar


def _eklenti_koku_yolu(kaynak_yol) -> str:
    """kaynak_yol içindeki eklenti kökü: '.../skills/<ad>' kalıbında 'skills' öncesi (plugins/<p>/skills/x -> plugins/<p>); yoksa ''."""
    p = (kaynak_yol or "").strip("/").split("/")
    return "/".join(p[:p.index("skills")]) if "skills" in p[:-1] else ""


def kardes_coz(s: dict, hedef_ad: str, skiller, ipucu=None):
    """hedef_ad adlı başka skill'i YALNIZ aynı repoda arar (ad @kaynak eksiz, klasor_adi ya da kaynak_yol son klasörü eşleşmesi);
    tam bir aday varsa kaydı döner, yoksa ya da birden çok aday varsa None (sessizce tahmin edilmez).
    ipucu (isteğe bağlı): birden çok aday varsa daraltır — 'ust' (göreli ../<ad> yolu: aday, bu skill'le AYNI üst klasörde olmalı:
    dirname(kaynak_yol) eşit) ya da 'kok' (${CLAUDE_PLUGIN_ROOT}/skills/<ad>: aynı eklenti kökü). Daralınca da tek aday kalmazsa None."""
    h = _ad_norm(hedef_ad)
    adaylar = [x for x, ad in _skiller_indeksi(skiller)[0].get(s.get("repo"), []) if x["id"] != s["id"] and h in ad]
    if len(adaylar) > 1 and ipucu in ("ust", "kok"):
        kay = (lambda x: "/".join((x.get("kaynak_yol") or "").strip("/").split("/")[:-1])) if ipucu == "ust" else (lambda x: _eklenti_koku_yolu(x.get("kaynak_yol")))
        adaylar = [x for x in adaylar if kay(x) == kay(s)]
    return adaylar[0] if len(adaylar) == 1 else None


_YOL_ONBELLEK = {}


def skill_yol_taramasi(s: dict, skiller) -> list:
    """Üst seviye tarama: adlar = skill_adlari, bilinen adlar = tüm skiller. genel-baska / eklenti-kardes / kardes-goreli /
    skil-disi-yol (tek '..') bulgularında kardeşi kardes_coz ile çözer: bulguya 'kardes_id' eklenir ve var = dosya KARDEŞİN ARŞİV
    klasöründe var mı (boş kalan = kardeş klasörü). Sonuç (id, klasor_hash, yol) anahtarıyla ve AYNI skiller listesi (kimlik+uzunluk) için modül sözlüğünde önbelleklenir
    (kardeşin dosyaları aynı süreçte değişirse önbellek bilmez); her çağrıda kopya döner. Çok adaylı adlarda göreli yol (kardes-goreli,
    skil-disi-yol) için aynı üst klasördeki, eklenti-kardes için aynı eklenti kökündeki tek aday seçilir (kardes_coz ipucu)."""
    anahtar = (s["id"], s.get("klasor_hash"), s.get("yol"))  # yol: geçici (taze çekilmiş) skiller birbirinin önbelleğini kullanmasın
    onb = _YOL_ONBELLEK.get(anahtar)
    if onb is None or onb[0] is not skiller or onb[1] != len(skiller):  # kardeş çözümü skiller listesine bağlı: başka/büyüyen liste = yeniden hesapla
        bulgular = yol_taramasi(KOK / s["yol"], skill_adlari(s, skiller), _skiller_indeksi(skiller)[1])
        for b in bulgular:
            if b["tur"] in ("genel-baska", "eklenti-kardes", "kardes-goreli", "skil-disi-yol") and b["hedef"]:
                k = kardes_coz(s, b["hedef"], skiller, {"kardes-goreli": "ust", "skil-disi-yol": "ust", "eklenti-kardes": "kok"}.get(b["tur"]))
                if k:
                    b["kardes_id"] = k["id"]
                    b["var"] = _var_bak(KOK / k["yol"], b["kalan"])
                    _engel_hesapla(b)
        onb = _YOL_ONBELLEK[anahtar] = (skiller, len(skiller), bulgular)
    return [dict(b, engeller=list(b["engeller"])) for b in onb[2]]


# ------------------------------------------------------------------ yol istisnaları (yol-istisnalari.json)
def istisna_anahtari(s: dict) -> str:
    """İstisna kaydının anahtarı: 'repo::kaynak_yol' (skill id'si DEĞİL: id 'ad@kaynak'a dönse de istisna ölmesin)."""
    return f"{s.get('repo')}::{s.get('kaynak_yol')}"


def bulgu_hash(bulgular) -> str:
    """Bulguların kimliği: sıralı (dosya, ham) çiftlerinin sha256'sı (satır numarası hariç: satır kayması istisnayı düşürmesin)."""
    return hashlib.sha256("\n".join(f"{b['dosya']}\t{b['ham']}" for b in sorted(bulgular, key=lambda b: (b["dosya"], b["ham"]))).encode()).hexdigest()


def yol_istisnalari() -> dict:
    """YOL_ISTISNA dosyasındaki {'repo::kaynak_yol': {'ad', 'kayitlar': [...]}} sözlüğü ('istisnalar' alanı). Dosya yoksa ya da bozuksa {}
    (bozukluğu dogrula.py HATA olarak bildirir; kurulum bu yüzden çökmez).
    Kayıt şeması: {tur, hedefler:[…] | dosyalar:[…], karar: 'ornek-metin'|'kabul', neden, tarih, bulgu_hash}."""
    try:
        d = json_oku(YOL_ISTISNA, {}) or {}
    except ValueError:
        return {}
    d = d.get("istisnalar", {}) if isinstance(d, dict) else {}
    return d if isinstance(d, dict) else {}


def _anahtar_norm(anahtar: str) -> str:
    """'repo::kaynak_yol' -> repo güncel adıyla ve küçük harfle ('Owner/Repo' ya da taşınmış eski ad aynı kayda çıkar); kaynak_yol aynen."""
    repo, _, yol = (anahtar or "").partition("::")
    return f"{repo_guncel(repo).lower()}::{yol}"


def istisna_kaydi_gecerli(k) -> bool:
    """Kayıt geçerli mi: tur dolu, karar bilinen, hedefler/dosyalar (varsa) yalnız boş olmayan metinlerden oluşan listeler ve en az biri
    dolu (tür bazlı kör istisna yok; [null] / iç içe liste geçersiz)."""
    if not (isinstance(k, dict) and isinstance(k.get("tur"), str) and k.get("tur") and k.get("karar") in ("ornek-metin", "kabul")):
        return False
    dolu = False
    for a in ("hedefler", "dosyalar"):
        v = k.get(a)
        if v is None or v == []:
            continue
        if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
            return False
        dolu = True
    return dolu


def istisna_kapsami(k: dict, bulgular) -> list:
    """Geçerli bir istisna kaydının kapsadığı bulgular: aynı tür ve hedefi 'hedefler'de ya da dosyası 'dosyalar'da olanlar."""
    h, d = set(k.get("hedefler") or []), set(k.get("dosyalar") or [])
    return [b for b in bulgular if b["tur"] == k["tur"] and (bool(h and b["hedef"] in h) or bool(d and b["dosya"] in d))]


def istisna_uygula(s: dict, bulgular, istisnalar=None):
    """(kalan, istisnali, eskiyen): kalan = istisnasız bulgular, istisnali = bir kayıtla kapsananlar, eskiyen = bulgu_hash'i artık
    tutmayan kayıtlar (bunların bulguları kalan'da KALIR; kullanıcıya 'istisna-eskidi' gösterilir). Geçersiz/bozuk kayıtlar ve bozuk dosya
    yapısı sessizce yok sayılır (çökmez; dogrula.py HATA bildirir). Anahtar eşlemesi yol_istisna_denetimi ile aynıdır."""
    ist = yol_istisnalari() if istisnalar is None else (istisnalar.get("istisnalar", istisnalar) if isinstance(istisnalar, dict) else {})
    ik = _anahtar_norm(istisna_anahtari(s))  # dogrula ile AYNI eşleme (repo güncel adı + küçük harf): doğrulamadan geçen kayıt uygulanmadan ölmesin
    giris = next((v for a, v in ist.items() if isinstance(a, str) and _anahtar_norm(a) == ik), None) if isinstance(ist, dict) else None
    kayitlar = giris.get("kayitlar") if isinstance(giris, dict) else None
    kapsanan_idler, eskiyen = set(), []
    for k in (kayitlar if isinstance(kayitlar, list) else []):
        if not istisna_kaydi_gecerli(k):
            continue
        kap = istisna_kapsami(k, bulgular)
        if k.get("bulgu_hash") and bulgu_hash(kap) == k["bulgu_hash"]:
            kapsanan_idler |= {id(b) for b in kap}
        else:
            eskiyen.append(k)
    return ([b for b in bulgular if id(b) not in kapsanan_idler], [b for b in bulgular if id(b) in kapsanan_idler], eskiyen)


def _yol_ornekleri(bulgular, n=3) -> str:
    gor, sonuc = set(), []
    for b in bulgular:
        x = f"{b['dosya']}:{b['satir']} {b['ham'][:70]}"
        if x not in gor:
            gor.add(x)
            sonuc.append(x)
    return "; ".join(sonuc[:n]) + (f" (+{len(sonuc) - n})" if len(sonuc) > n else "")


def yol_degerlendir(s: dict, skiller, kurulacak_idler=None, istisnalar=None) -> dict:
    """Bulguları ön kontrol satırlarına çeviren TEK yer (yol-tara.py ve sonraki aşamada skill-ekle.py kullanır).
    kurulacak_idler: kurulan / hedef projede kurulu skill kimlikleri kümesi; None = bilinmiyor (rapor kipi).
    Döner:
      satirlar   [(seviye 'UYARI'|'BİLGİ', kod, gövde)]  gövde "ad: " öneki OLMADAN, kısa, en çok 3 örnek. Kodlar:
                 yol-yerellestirme (BİLGİ) · genel-yol (UYARI: a kendi yolu ama dosya arşivde yok, b kendi yolu ama otomatik çevrilmiyor
                 [betik/kurulum dosyası/karışık ya da kurulum anlatan dosya], c çözülemeyen kardeş: başka skill'in genel klasörü YA DA göreli ../<skill>/ yolu,
                 d ortak dizin, e kalan boş kendi yolu bir değişkene atanıyor [SKILL_DIR=…]; echo/printf kullanım ipuçları ve "e.g." açıklama satırları
                 yalnız sayılır) · eklenti-koku (UYARI; satırda "or ~/…" gibi seçenekler varsa BİLGİ) · skil-disi-yol (UYARI) ·
                 kardes-eksik (UYARI: kardeş kurulmuyor ya da kardeşte dosya yok; kurulacak_idler None iken BİLGİ "kardeşle düzelir") ·
                 kardes-yol (BİLGİ: kardeş kuruluyor, yol çevrilecek) · genele-yazabilir (UYARI: ajan dosyasında genele-kopyalar;
                 BİLGİ: yalnız gerçek genele-yazar adımı) · yol-istisna (BİLGİ) · istisna-eskidi (UYARI). 'dokuman' sınıfı dosyalar satır üretmez.
      sayim      {tur: adet} — sayım-yalnız türler dahil, istisnalılar dahil
      cevrilecek istisnasız kendi-yol bulguları (genel-kendi/eklenti-kendi) cevrilebilir=True olanlar
      kardesler  {hedef_ad: {"id", "kurulu" (bool | None), "bulgular"}} yalnız çözülen kardeşler
      satir_kardes  (yalnız satırlardan biri bir kardeşe bağlıysa var) satirlar ile paralel liste: satırın ilgili olduğu kardeş skill kimliği (yoksa None) — kurulum ön kontrolü kardeşi kimliğe göre tekilleştirir
      cevrilecek_kardes  (yalnız varsa) istisnasız kardeş-yol bulguları (genel-baska/eklenti-kardes/skil-disi-yol, kardes_id var) cevrilebilir=True olanlar
      sutun      'temiz'|'yalniz-sayim'|'kurulumda-duzelir'|'kardesle-duzelir'|'paket-gerekli'|'cozulemez'|'istisna'
                 (skil-disi-yol ve eklenti kökü = paket-gerekli: dosyalar arşive alınmamış; öncelik: cozulemez > paket-gerekli > kardesle-duzelir > kurulumda-duzelir > istisna > yalniz-sayim > temiz)"""
    tum = skill_yol_taramasi(s, skiller)
    sayim = {}
    for b in tum:
        sayim[b["tur"]] = sayim.get(b["tur"], 0) + 1
    kalan, istisnali, eskiyen = istisna_uygula(s, tum, istisnalar)
    satir, kardesler, bayrak = [], {}, set()
    satir_kid = []  # satir ile paralel: satırın ilgili olduğu kardeş skill kimliği (yoksa None)

    def ek(sv, kod, govde, kid=None):
        satir.append((sv, kod, govde))
        satir_kid.append(kid)
    aktif = [b for b in kalan if b["sinif"] != "dokuman"]
    satir_engel = ("kurulum-komutu", "cok-kok", "kullanim-metni", "ornek-satir")  # kurulum tarifi / betikteki kullanım ipucu (echo) / "e.g., in most installs" açıklama satırları: bağımlılık değil, yalnız sayılır
    cevrilecek = [b for b in kalan if b["tur"] in ("genel-kendi", "eklenti-kendi") and b["cevrilebilir"]]
    # kardeşin proje içi yoluna GERÇEKTEN çevrilebilecek bulgular (kurulum bunları ve yalnız bunları yazar; ../<kardeş>/ göreli yolları ayrı geçiştir)
    cevrilecek_kardes = [b for b in kalan if b["tur"] in ("genel-baska", "eklenti-kardes", "skil-disi-yol") and b.get("kardes_id") and b["cevrilebilir"]]
    yamali = set((s.get("yama") or {}).get("dosyalar") or {})  # yama dosyanın tamamını değiştirir: kurulumda o dosyada çeviri yapılmaz, ön kontrol de vaat etmesin
    if yamali:
        cevrilecek = [b for b in cevrilecek if b["dosya"] not in yamali]
        cevrilecek_kardes = [b for b in cevrilecek_kardes if b["dosya"] not in yamali]
    # kendi yolları
    a_yok, b_cevrilmez, e_yok, atama = [], [], [], []
    for b in aktif:
        if b["tur"] not in ("genel-kendi", "eklenti-kendi") or b["engel"] in satir_engel or b["cevrilebilir"]:
            continue
        if b["engel"] == "dosya-yok":
            (a_yok if b["tur"] == "genel-kendi" else e_yok).append(b)
        elif b["engel"] == "kalan-bos" and b.get("atama"):
            atama.append(b)
        elif b["engel"] in ("betik-ici", "kurucu-dosya", "karisik-dosya"):
            b_cevrilmez.append(b)
    if cevrilecek:
        ek("BİLGİ", "yol-yerellestirme", f"{len(cevrilecek)} sabit yol kurulan kopyada proje içi yola çevrilecek ({_yol_ornekleri(cevrilecek)})")
        bayrak.add("kurulumda")
    if a_yok:
        ek("UYARI", "genel-yol", f"kendi genel klasöründen dosya bekliyor, bu dosyalar arşivde yok: {_yol_ornekleri(a_yok)}")
        bayrak.add("paket")
    if b_cevrilmez:
        ek("UYARI", "genel-yol", f"kendi sabit yolu otomatik çevrilmiyor (betik içinde / kurulum dosyasında / karışık ya da kurulum anlatan dosyada): {_yol_ornekleri(b_cevrilmez)}")
        bayrak.add("cozulemez")
    if atama:
        ek("UYARI", "genel-yol", f"kendi genel klasörünü bir değişkene atıyor (sonraki betik yolları buna dayanabilir), otomatik çevrilmiyor: {_yol_ornekleri(atama)}")
        bayrak.add("cozulemez")
    if e_yok:
        ek("UYARI", "eklenti-koku", f"eklenti kökündeki kendi klasörüne işaret ediyor ama dosya arşivde yok: {_yol_ornekleri(e_yok)}")
        bayrak.add("paket")
    # kardeş / başka skill yolları
    cozulmeyen, ortak, kok_yol, disi, goreli_cozulmeyen = [], [], [], [], []
    cozulen = {}
    for b in aktif:
        t = b["tur"]
        if t == "ortak-dizin":
            ortak.append(b)
        elif t == "eklenti-kok-yol" and b["sinif"] == "ajan":
            kok_yol.append(b)
        elif t == "skil-disi-yol" and not b.get("kardes_id"):
            disi.append(b)
        elif t in ("genel-baska", "eklenti-kardes", "kardes-goreli", "skil-disi-yol"):
            if b.get("kardes_id"):
                if b["engel"] in satir_engel or (b["engel"] == "kalan-bos" and t != "kardes-goreli"):
                    continue
                cozulen.setdefault(b["hedef"], []).append(b)
            elif t in ("genel-baska",) and b["engel"] not in satir_engel:
                cozulmeyen.append(b)
            elif t == "kardes-goreli":
                goreli_cozulmeyen.append(b)
            elif t == "eklenti-kardes":
                kok_yol.append(b)
    if cozulmeyen:
        adlar = sorted({b["hedef"] for b in cozulmeyen})
        varsa = [a for a in adlar if _ad_norm(a) in _skiller_indeksi(skiller)[1]]
        ek("UYARI", "genel-yol", f"başka skill'in genel klasörüne dayanıyor, aynı repoda tek aday olarak çözülemedi: {_yol_ornekleri(cozulmeyen)}"
           + (f" (kütüphanede başka yerde var: {', '.join(varsa[:3])})" if varsa else " (kütüphanede yok)"))
        bayrak.add("cozulemez")
    if goreli_cozulmeyen:
        adlar = sorted({b["hedef"] for b in goreli_cozulmeyen})
        varsa = [a for a in adlar if _ad_norm(a) in _skiller_indeksi(skiller)[1]]
        ek("UYARI", "genel-yol", f"göreli kardeş yolu (../<skill>/…) aynı repoda tek aday olarak çözülemedi, düz kurulumda kırılır: {_yol_ornekleri(goreli_cozulmeyen)}"
           + (f" (kütüphanede başka yerde var: {', '.join(varsa[:3])})" if varsa else " (kütüphanede yok)"))
        bayrak.add("cozulemez")
    if ortak:
        ek("UYARI", "genel-yol", f"ortak dizine (_shared gibi) dayanıyor: {_yol_ornekleri(ortak)}")
        bayrak.add("cozulemez")
    kok_alt = [b for b in kok_yol if b.get("alternatif")]
    kok_yol = [b for b in kok_yol if not b.get("alternatif")]
    if kok_yol:
        ek("UYARI", "eklenti-koku", f"eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: {_yol_ornekleri(kok_yol)}")
        bayrak.add("paket")
    if kok_alt:
        ek("BİLGİ", "eklenti-koku", f"eklenti kökü yolu başka seçeneklerle birlikte geçiyor (…, or ~/…): düz kurulumda öteki seçenek kullanılabilir: {_yol_ornekleri(kok_alt)}")
    if disi:
        ek("UYARI", "skil-disi-yol", f"skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: {_yol_ornekleri(disi)}")
        bayrak.add("paket")
    for hedef in sorted(cozulen):
        bl = cozulen[hedef]
        kid = bl[0]["kardes_id"]
        kurulu = None if kurulacak_idler is None else kid in kurulacak_idler
        kardesler[hedef] = {"id": kid, "kurulu": kurulu, "bulgular": bl}
        eksik = [b for b in bl if b["var"] is False]
        if eksik:
            ek("UYARI", "kardes-eksik", f"{hedef}: dosya arşivde yok: {_yol_ornekleri(eksik)}", kid)
            bayrak.add("paket")
        tamam = [b for b in bl if b["var"] is not False]
        if not tamam:
            continue
        if kurulu is None:
            ek("BİLGİ", "kardes-eksik", f"{hedef} ({kid}) kardeş skill gerekli; kurulursa kardeşle düzelir: {_yol_ornekleri(tamam)}", kid)
            bayrak.add("kardes")
        elif not kurulu:
            ek("UYARI", "kardes-eksik", f"{hedef} ({kid}) kardeş skill projeye kurulmuyor: {_yol_ornekleri(tamam)}", kid)
            bayrak.add("kardes")
        else:
            ek("BİLGİ", "kardes-yol", f"{hedef} ({kid}) kardeş kuruluyor, {len(tamam)} yol kardeşin proje içi yoluna çevrilecek", kid)
            cevrilmez = [b for b in tamam if b["engel"] in ("betik-ici", "kurucu-dosya", "karisik-dosya")
                         and b["tur"] in ("genel-baska", "eklenti-kardes")]
            if cevrilmez:
                ek("UYARI", "genel-yol", f"{hedef} yolu otomatik çevrilmiyor (betik içinde / kurulum dosyasında / karışık dosyada): {_yol_ornekleri(cevrilmez)}", kid)
                bayrak.add("cozulemez")
    # genele yazma
    kopya = [b for b in aktif if b["tur"] == "genele-kopyalar" and b["sinif"] == "ajan"]
    adim = [b for b in aktif if b["tur"] == "genele-yazar" and b["sinif"] == "ajan" and b.get("alt") == "ajan-adimi"]
    if kopya:
        ek("UYARI", "genele-yazabilir", f"bilgisayar geneli skill/agent klasörüne dosya kopyalıyor: {_yol_ornekleri(kopya + adim)}")
    elif adim:
        ek("BİLGİ", "genele-yazabilir", f"genel kuruluma yazan komut ajan adımı olarak geçiyor: {_yol_ornekleri(adim)}")
    if istisnali:
        ek("BİLGİ", "yol-istisna", f"{len(istisnali)} bulgu istisna kaydıyla kapsandı ({', '.join(sorted({b['tur'] for b in istisnali}))}; kayıt: yol-istisnalari.json)")
    for k in eskiyen:
        ek("UYARI", "istisna-eskidi", f"{k.get('tur')} istisnası artık tutmuyor (dosyalar değişmiş): kaydı yeniden doğrula ya da sil")
    sira = (("cozulemez", "cozulemez"), ("paket", "paket-gerekli"), ("kardes", "kardesle-duzelir"), ("kurulumda", "kurulumda-duzelir"))
    sutun = next((ad for b_, ad in sira if b_ in bayrak), None)
    if not sutun:
        sutun = "istisna" if istisnali else "yalniz-sayim" if tum else "temiz"
    sonuc = {"satirlar": satir, "sayim": sayim, "cevrilecek": cevrilecek, "kardesler": kardesler, "sutun": sutun}
    if any(satir_kid):  # ek anahtarlar YALNIZ doluysa eklenir: kardeşi olmayan skill'in dönüşü eski biçimiyle birebir aynı kalır
        sonuc["satir_kardes"] = satir_kid
    if cevrilecek_kardes:
        sonuc["cevrilecek_kardes"] = cevrilecek_kardes
    return sonuc


# ------------------------------------------------------------------ kurulumda dar geçiş: kendi klasörü .agents/skills/<ad>/… -> .claude/skills/<kurulum adı>/…
_EV_ICI_AGENTS = re.compile(r"(?:(?<![\w$}~/])|(?<=\./)|(?<=\$\{CLAUDE_PROJECT_DIR\}/)|(?<=\$CLAUDE_PROJECT_DIR/))(?P<on>\.agents/skills)/(?P<ad>[A-Za-z0-9_.@+-]+)(?P<k>" + _KALAN + ")")


def ev_ici_kendi_cevir(metin: str, adlar, yeni_ad: str, hedef_onek: str, arsiv, betik: bool = False):
    """Proje içi (öneksiz) '.agents/skills/<kendi ad>/<kalan>' (ya da ./, ${CLAUDE_PROJECT_DIR}/, $CLAUDE_PROJECT_DIR/ önekli) yollarını '<hedef_onek>/<yeni_ad>/<kalan>' yapar. Satır kuralları yol_taramasi ile aynıdır:
    kalan boş ya da arşivde (arsiv klasörü) yoksa, satırda kurulum komutu (yoldan önce) / iki ya da daha çok yerleşim kökü / açıklama (e.g., for example)
    varsa çevrilmez. Döner: (yeni metin, çevrilen sayısı)."""
    arsiv = Path(arsiv)
    adlar = {_ad_norm(a) for a in adlar if a}
    yeni_satir = _satir_haritasi(metin)
    degisim, onbellek = [], {}  # onbellek: satır başı -> (kurulum komutu konumları, yerleşim kökü sayısı, örnek satırı mı); satır başına tek tarama
    for m in _EV_ICI_AGENTS.finditer(metin):
        ad = m.group("ad")
        if ad.endswith(".") or _ad_norm(ad) not in adlar:
            continue
        kalan = _kalan_temizle(m.group("k") or "")
        if not kalan or _var_bak(arsiv, kalan) is not True:
            continue
        i = bisect.bisect_left(yeni_satir, m.start())
        bas = yeni_satir[i - 1] + 1 if i else 0
        son = yeni_satir[i] if i < len(yeni_satir) else len(metin)
        if son - bas > YOL_TARAMA_SINIRLARI["satir_karakter"]:
            continue  # yol_taramasi ile aynı sınır: aşırı uzun (gömülü/minify) satırda çevirme yapılmaz
        poz = m.start() - bas
        bilgi = onbellek.get(bas)
        if bilgi is None:
            satir = metin[bas:son]
            kokler = {(x.group("a") or x.group("b") or x.group("c")).lower().replace("codex_home", "codex").replace("claude_dir", "claude")
                      for x in _KOK_YERLESIM.finditer(satir)}
            bilgi = onbellek[bas] = ([k.start() for k in _KURULUM_KOMUTU.finditer(satir)], len(kokler),
                                     bool(_ORNEK_SATIR.search(satir)), bool(betik and _KULLANIM_SATIR.match(satir)))
        if any(k < poz for k in bilgi[0]) or bilgi[1] >= 2 or bilgi[2] or bilgi[3]:
            continue
        degisim.append((m.start("on"), m.end("ad"), f"{hedef_onek}/{yeni_ad}"))
    for bas_, son_, yeni in reversed(degisim):
        metin = metin[:bas_] + yeni + metin[son_:]
    return metin, len(degisim)


def yol_istisna_denetimi(skiller):
    """yol-istisnalari.json denetimi (dogrula.py ve testler aynı kuralı kullanır). Döner: (hatalar, uyarılar) — dosya yoksa ([], []).
    HATA: bozuk JSON, 'istisnalar' sözlük değil, kayıt geçersiz (bilinmeyen karar, boş hedefler+dosyalar, tur yok), bulgu_hash yok.
    UYARI: anahtar ('repo::kaynak_yol', repo eski_adlar ile güncellenerek) registry'de hiçbir skill'e uymuyor; bulgu_hash artık tutmuyor."""
    if not YOL_ISTISNA.exists():
        return [], []
    hatalar, uyarilar = [], []
    try:
        veri = json.loads(YOL_ISTISNA.read_text(encoding="utf-8"))
        ist = veri.get("istisnalar") if isinstance(veri, dict) else None
        if not isinstance(ist, dict):
            return [f"{YOL_ISTISNA.name}: 'istisnalar' sözlük olmalı"], []
    except ValueError as e:
        return [f"{YOL_ISTISNA.name}: geçerli JSON değil ({str(e)[:80]})"], []
    skiller_k = {}
    for s in skiller:
        skiller_k.setdefault(_anahtar_norm(istisna_anahtari(s)), []).append(s)
    for anahtar, giris in sorted(ist.items()):
        uyan = skiller_k.get(_anahtar_norm(anahtar), [])
        kayitlar = giris.get("kayitlar") if isinstance(giris, dict) else None
        if not isinstance(kayitlar, list) or not kayitlar:
            hatalar.append(f"{YOL_ISTISNA.name}: {anahtar}: 'kayitlar' boş ya da liste değil")
            continue
        if not uyan:
            uyarilar.append(f"{YOL_ISTISNA.name}: {anahtar} registry'deki hiçbir skill'e uymuyor (skill kaldırılmış / repo taşınmış?): kaydı sil ya da güncelle")
        for i, k in enumerate(kayitlar):
            if not istisna_kaydi_gecerli(k):
                hatalar.append(f"{YOL_ISTISNA.name}: {anahtar} kayıt {i + 1} geçersiz (tur, karar 'ornek-metin'|'kabul', boş olmayan hedefler ya da dosyalar gerekli)")
            elif not k.get("bulgu_hash"):
                hatalar.append(f"{YOL_ISTISNA.name}: {anahtar} kayıt {i + 1} ({k['tur']}): bulgu_hash yok")
            elif uyan and not any(bulgu_hash(istisna_kapsami(k, skill_yol_taramasi(s, skiller))) == k["bulgu_hash"] for s in uyan):
                uyarilar.append(f"{YOL_ISTISNA.name}: {anahtar} kayıt {i + 1} ({k['tur']}): bulgu_hash tutmuyor (skill dosyaları değişmiş): "
                                f"python3 araclar/yol-tara.py --skill {uyan[0]['id']} ile yeniden doğrula")
    return hatalar, uyarilar


# --- P8: genel klasör izi, rapor araçları, rapor yaşı ---------------------------------------
GENEL_ATLA = ("synced", ".system", "skills-cursor")  # Claude hesap senkronu / Codex ve Cursor'ın kendi yerleşikleri
GENEL_TEST_KLASORLERI = list(GLOBAL_KLASORLER.values()) + [  # testin önce/sonra izi: yalnız kütüphane araçlarının yazabileceği klasörler
    Path.home() / ".openmontage" / ".agents" / "skills",
]
GENEL_TEST_ATLA = GENEL_ATLA + (".DS_Store", ".git", ".cache", "__pycache__", "node_modules")  # kendiliğinden değişen üst düzey girdiler
GENEL_IZLEME_KLASORLERI = GENEL_TEST_KLASORLERI + [  # bekçi: diğer yapay zeka araçlarının klasörleri de
    Path.home() / ".cursor" / "skills",
    Path.home() / ".gemini" / "skills",
    Path.home() / ".gemini" / "antigravity" / "skills",
    Path.home() / ".copilot" / "skills",
]


def genel_izleri(klasorler=None, atla=None) -> dict:
    """{'<klasör>/<ad>': mtime_ns}: kütüphane araçları bu klasörlere yazmamalı. Yalnız okur."""
    iz = {}
    atla = GENEL_ATLA if atla is None else atla
    for g in (GENEL_IZLEME_KLASORLERI if klasorler is None else klasorler):
        g = Path(g)
        if g.is_dir():
            for p in sorted(g.iterdir()):
                if p.name not in atla:
                    iz[f"{g}/{p.name}"] = p.lstat().st_mtime_ns
    return iz


def genel_parmak_izi(klasorler=None, atla=None) -> str:
    return hashlib.sha256(json.dumps(genel_izleri(klasorler, atla), sort_keys=True).encode()).hexdigest()


def genel_fark(once: dict, sonra: dict) -> list:
    return sorted(set(once) ^ set(sonra) | {k for k in set(once) & set(sonra) if once[k] != sonra[k]})


OZET_DURUMLAR = ("temiz", "dikkat", "sorun")
OZET_ARACLARI = [  # (araç dosyası adı, ekstra bayraklar); her biri --ozet-json destekler; duman ve aylik-ozet (P4) aynı listeyi kullanır
    ("git-durum", []), ("yedek-denetim", []), ("genel-bekci", []),
    ("program-denetim", []), ("proje-kullanimi", ["--saglik"]),
    ("skill-ekle", ["--araclar"]),
    ("konu-takip", ["--bekleyenler"]),
]


def ozet_json_gecerli(metin: str):
    """stdout tam olarak tek JSON nesnesi mi? -> (nesne ya da None, hata metni)."""
    try:
        o = json.loads(metin)
    except ValueError as e:
        return None, f"JSON değil: {str(e)[:80]}"
    if not isinstance(o, dict) or not {"arac", "durum", "satirlar", "karar_bekleyen"} <= set(o):
        return None, "arac/durum/satirlar/karar_bekleyen anahtarları eksik"
    if o["durum"] not in OZET_DURUMLAR or not isinstance(o["arac"], str):
        return None, f"durum geçersiz: {o['durum']!r}"
    if not all(isinstance(o[k], list) and all(isinstance(x, str) for x in o[k]) for k in ("satirlar", "karar_bekleyen")):
        return None, "satirlar/karar_bekleyen metin listesi değil"
    return o, ""


RAPOR_YASI = [  # (yol, eşik gün, yenileme komutu): aylik-ozet tam modda gösterebilir; dogrula.py KULLANMAZ
    ("notlar/github-trend.md", 45, "python3 araclar/github-trend.py --aday"),
    ("notlar/populer-skiller.md", 45, "python3 araclar/populer-tarama.py"),
    ("notlar/konu-takip.md", 45, "python3 araclar/konu-takip.py"),
    ("notlar/program-denetimi.md", 45, "python3 araclar/program-denetim.py"),
    ("notlar/kapsam-denetimi.md", 45, "python3 araclar/kapsam-denetimi.py"),
    ("TEST_RAPORU.md", 45, "aylık güncelleme yeniler (python3 araclar/skill-calistir.py)"),
    ("notlar/proje-durumu.md", 45, "python3 araclar/proje-kullanimi.py --saglik --yaz"),
    ("notlar/genel-bekci.md", 45, "python3 araclar/genel-bekci.py"),
    ("notlar/hf-om-gecisi/DURUM.md", 45, "kütüphane oturumu 'Son güncelleme' satırını yeniler"),
]


def rapor_yasi_satirlari(kok=None, bugun=None, tablo=None) -> list:
    """Bayat raporların düz cümleleri (yoksa []). Yalnız okur. Tarih: dosyanın ilk 8 satırındaki ilk YYYY-AA-GG;
    yoksa 'git log -1 --format=%cs -- <dosya>' (klonda mtime sıfırlanır, kullanılmaz); ikisi de yoksa atlanır."""
    from datetime import date
    kok = Path(kok or KOK)
    bugun = bugun or date.today()
    cikti = []
    for yol, esik, komut in (RAPOR_YASI if tablo is None else tablo):
        f = kok / yol
        if not f.is_file():
            continue
        m = re.search(r"\d{4}-\d{2}-\d{2}", "\n".join(f.read_text(encoding="utf-8", errors="replace").splitlines()[:8]))
        gun = m.group(0) if m else ""
        if not gun:
            try:
                gun = subprocess.run(["git", "log", "-1", "--format=%cs", "--", yol], cwd=kok, capture_output=True,
                                     text=True, timeout=10).stdout.strip()
            except (OSError, subprocess.SubprocessError):
                gun = ""
        try:
            yas = (bugun - date.fromisoformat(gun)).days
        except ValueError:
            continue
        if yas > esik:
            cikti.append(f"{yol} {yas} gün önce üretilmiş (eşik {esik}); yenile: {komut}")
    return cikti


# ================================================================== programla gelen skiller: klasör adı eşlemesi (kart alanı skill_klasorleri)
# Kart: "skill_klasorleri": {"<skill adı>": "<skill_koku altındaki klasör adı>"}. Alan yoksa ya da ad eşlemede yoksa klasör adı skill adıdır.
# Üç araç (skill-ekle, program-denetim, proje-kullanimi) hedefi AYNI kuralla hesaplar: skill_koku / program_skill_klasoru(kart, ad).
SKILL_AD_DESENI = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")   # fullmatch ile kullanılır


def klasor_adi_gecerli(v):
    """skill_koku altındaki TEK parça klasör adı: boş, '.', '..', '/', '\\', mutlak yol, NUL ve geçersiz karakter olamaz."""
    return isinstance(v, str) and bool(SKILL_AD_DESENI.fullmatch(v)) and v not in (".", "..")


def skill_klasorleri_hatalari(kart):
    """Kartın skill_klasorleri alanındaki hatalar: [(alan yolu, mesaj)]. Alan yoksa boş."""
    if not isinstance(kart, dict) or "skill_klasorleri" not in kart:
        return []
    sk = kart["skill_klasorleri"]
    if not isinstance(sk, dict):
        return [("skill_klasorleri", "sözlük olmalı (skill adı -> klasör adı)")]
    out = []
    for a, k in sk.items():
        if not (isinstance(a, str) and SKILL_AD_DESENI.fullmatch(a)):
            out.append((f"skill_klasorleri.{a}", "anahtar geçerli bir skill adı olmalı"))
        if not klasor_adi_gecerli(k):
            out.append((f"skill_klasorleri.{a}", "değer tek parça klasör adı olmalı (boş, '..', '/' ve mutlak yol olamaz)"))
    # iki skill aynı klasöre ya da bir skill adı başka bir skilin klasörüne denk gelirse belirsizlik doğar
    gecerli = [(a, k) for a, k in sk.items() if isinstance(a, str) and klasor_adi_gecerli(k)]
    klasorler = [k for _, k in gecerli]
    for k in sorted({x for x in klasorler if klasorler.count(x) > 1}):
        out.append(("skill_klasorleri", f"iki skill aynı klasöre eşlenmiş: {k}"))
    return out


def program_skill_klasorleri(kart):
    """Geçerli eşlemeler: {skill adı: klasör adı}. Geçersiz girdi yok sayılır (şema denetimi bildirir)."""
    sk = kart.get("skill_klasorleri") if isinstance(kart, dict) else None
    if not isinstance(sk, dict):
        return {}
    return {a: k for a, k in sk.items() if isinstance(a, str) and SKILL_AD_DESENI.fullmatch(a) and klasor_adi_gecerli(k)}


def program_skill_klasoru(kart, ad):
    """Skill adının skill_koku altındaki klasör adı: eşlemede varsa eşlenen ad, yoksa skill adının kendisi."""
    return program_skill_klasorleri(kart).get(ad, ad)


def program_skill_ham_klasoru_mu(kart, ad):
    """True: `ad` eşlenmiş bir klasörün HAM adı (skill adı değil). Örn. nlm: 'data' (skill adı 'nlm-skill')."""
    m = program_skill_klasorleri(kart)
    return ad not in m and ad in m.values()


def program_klasor_skill_adi(kart, klasor):
    """Klasör adının skill adı (ters eşleme); eşleme yoksa klasör adı."""
    for a, k in program_skill_klasorleri(kart).items():
        if k == klasor:
            return a
    return klasor


# --- tür ve boyut araçları için ortak yardımcılar (tur-belirle.py, boyut-hesapla.py) ---
MEDYA_UZANTILARI = frozenset(
    # video, ses, görsel, yazı tipi
    ".mp4 .mov .webm .mkv .avi .m4v .mp3 .wav .ogg .flac .m4a .aac .png .jpg .jpeg .gif .webp .bmp .tif .tiff .ico .psd .svgz "
    ".heic .avif .ttf .otf .woff .woff2 .eot "
    # model ağırlığı, arşiv ve ikili
    ".safetensors .ckpt .pt .pth .onnx .gguf .bin .h5 .npz .npy .pkl .zip .tar .gz .tgz .bz2 .xz .7z .rar .whl .jar "
    ".so .dylib .dll .exe .a .o .wasm .pdf .glb .gltf .fbx .blend .obj .db .sqlite".split())


def medya_mi(yol: str) -> bool:
    """Medya ya da ikili dosya mı (uzantıya göre)? Kütüphane boyutu hesabında ayrı toplanır."""
    return Path(yol).suffix.lower() in MEDYA_UZANTILARI


def ham_metin(repo: str, yol: str, ref: str = "HEAD", azami: int = 200_000):
    """Reponun bir dosyasını raw.githubusercontent.com'dan okur (en çok `azami` bayt, zaman aşımı 15 sn). Okunamazsa None."""
    import urllib.parse
    import urllib.request
    url = f"https://raw.githubusercontent.com/{repo}/{ref}/{urllib.parse.quote(yol)}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "skill-kutuphanesi"}), timeout=15) as r:
            return r.read(azami).decode("utf-8", "replace")
    except (OSError, ValueError):
        return None
