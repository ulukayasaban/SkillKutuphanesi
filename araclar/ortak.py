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
        time.sleep(2 * (i + 1))
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
    gun = (date.fromisoformat(trend["son_tarama"]) - date.fromisoformat(g["son"])).days
    seviye = "trendde" if g["son"] == trend["son_tarama"] else "yakinda" if gun <= 90 else "gecmiste"
    return {"seviye": seviye, "son": g["son"], "ilk": g["ilk"], "gorulme": g["gorulme"],
            "en_iyi": g.get("en_iyi", {})}
