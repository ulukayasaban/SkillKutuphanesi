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
    Path(yol).write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def gh_api(yol, deneme=4):
    for i in range(deneme):
        r = subprocess.run(["gh", "api", yol], capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout)
        time.sleep(2 * (i + 1))
    raise RuntimeError(f"gh api başarısız: {yol}: {r.stderr.strip()}")


def git_blob_hash(veri: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(veri) + veri).hexdigest()


def klasor_hash(klasor: Path) -> str:
    """Klasör içeriğinin kimliği: (göreli yol, git blob hash) listesinin sha256'sı."""
    h = hashlib.sha256()
    for f in sorted(p for p in klasor.rglob("*") if p.is_file() and p.name != "KAYNAK.md"):
        h.update(str(f.relative_to(klasor)).encode())
        h.update(git_blob_hash(f.read_bytes()).encode())
    return h.hexdigest()


def skill_md_hash(klasor: Path):
    f = klasor / "SKILL.md"
    return git_blob_hash(f.read_bytes()) if f.exists() else None


def frontmatter(metin: str) -> dict:
    """SKILL.md başındaki YAML frontmatter'ı basitçe okur (name, description vb.)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", metin, re.S)
    if not m:
        return {}
    sonuc, anahtar, blok = {}, None, []
    for satir in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", satir)
        if km and not satir.startswith(" "):
            if anahtar and blok:
                sonuc[anahtar] = " ".join(s.strip() for s in blok).strip()
            anahtar, deger = km.group(1), km.group(2).strip()
            if deger in (">", "|", ">-", "|-", ""):
                blok = []
            else:
                sonuc[anahtar] = deger.strip("'\"")
                blok = []
                if not deger:
                    blok = []
        elif anahtar is not None:
            blok.append(satir)
    if anahtar and blok:
        sonuc[anahtar] = " ".join(s.strip() for s in blok).strip()
    return sonuc


def boyut(klasor: Path) -> int:
    return sum(p.stat().st_size for p in klasor.rglob("*") if p.is_file())


def global_durum(ad: str, sm_hash: str) -> dict:
    """Aynı isimli skill global klasörlerde var mı, içerik aynı mı? (salt okuma)"""
    durum = {}
    for arac, klasor in GLOBAL_KLASORLER.items():
        f = klasor / ad / "SKILL.md"
        if f.exists():
            try:
                durum[arac] = "ayni" if git_blob_hash(f.read_bytes()) == sm_hash else "farkli"
            except OSError:
                durum[arac] = "okunamadi"
    return durum
