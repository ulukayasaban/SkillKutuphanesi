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
TREND = KOK / "trend.json"

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
        # hız sınırı: kısa bekleme işe yaramaz; dakikalarca bekleyip yeniden dene (ay-ortası çökme yerine)
        limit = "rate limit" in r.stderr.lower() or "HTTP 403" in r.stderr or "HTTP 429" in r.stderr
        time.sleep(60 * (i + 1) if limit else 2 * (i + 1))
    raise RuntimeError(f"gh api başarısız: {yol}: {r.stderr.strip()}")


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
    """Kurulan kopyaya uygulanan frontmatter onarımının izi (kilitte saklanır). Onarım yoksa None."""
    d = (s.get("aciklama_duzeltme") or {}).get("description")
    oto = [y for y in s.get("yapisal_sorunlar", []) if "dosya başında değil" in y or "tırnaksız" in y]
    if not d and not oto:
        return None
    return hashlib.sha1(f"{ONARIM_SURUMU}|{d or ''}|{'|'.join(oto)}".encode()).hexdigest()[:12]


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
