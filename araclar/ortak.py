"""SkillKutuphanesi araçlarının ortak yardımcıları (sadece Python stdlib)."""
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


def onemli_dosyalar(klasor: Path):
    """İçerik karşılaştırmasına giren dosyalar: KAYNAK.md ve işletim sistemi/çalışma çöpleri hariç."""
    return sorted(p for p in klasor.rglob("*") if p.is_file() and p.name != "KAYNAK.md"
                  and not GURULTU.search(str(p.relative_to(klasor))))


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


def onarim_izi(s: dict):
    """Kurulan kopyaya uygulanan onarımın izi (frontmatter + yamalar; kilitte saklanır). Onarım yoksa None."""
    d = (s.get("aciklama_duzeltme") or {}).get("description")
    oto = [y for y in s.get("yapisal_sorunlar", []) if "dosya başında değil" in y or "tırnaksız" in y]
    yama = [f"{rel}:{git_blob_hash((YAMALAR / s['id'] / rel).read_bytes()) if (YAMALAR / s['id'] / rel).exists() else '-'}"
            for rel in sorted(((s.get("yama") or {}).get("dosyalar") or {}))]
    if not d and not oto and not yama:
        return None
    return hashlib.sha1(f"{ONARIM_SURUMU}|{d or ''}|{'|'.join(oto)}|{'|'.join(yama)}".encode()).hexdigest()[:12]


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
