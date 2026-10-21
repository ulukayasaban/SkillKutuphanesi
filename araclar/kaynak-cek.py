#!/usr/bin/env python3
"""Aşama 1: kaynaklar.json'daki repolardan skill klasörlerini sabit commit'ten indirir.

Repo klonlanmaz; git geçmişi, demo videoları, örnek/test klasörleri inmez.
Repodaki HER SKILL.md için bir karar kaydedilir (denetim): hiçbir skill sessizce atlanmaz.

Kararlar:
  secildi            -> arşive ana sürüm olarak girer
  arac-varyanti      -> aynı skill'in Claude (.claude/skills) veya Codex (.agents|.codex/skills) için uyarlanmış sürümü; ayrıca saklanır
  ayri-surum         -> aynı klasör adı, farklı içerik, ayna değil -> ayrı skill olarak saklanır
  ayna-ayni          -> başka bir yoldaki birebir kopyası (tek kopya yeter)
  ayna-baska-arac    -> Cursor/Gemini/Kiro vb. başka bir AI aracı için uyarlanmış kopya (Claude/Codex'i ilgilendirmez)
  haric:<desen>      -> test/örnek/şablon gibi bilinçli hariç
  dahil-disi         -> bu kayıt kapsamı dışında (aynı reponun başka bir kaydı ele alır)

Çıktı: .gecici/cekilen/<kimlik>/... + .gecici/cekilen/manifest.json
Kullanım:
  python3 araclar/kaynak-cek.py                  # tümü
  python3 araclar/kaynak-cek.py --repo owner/ad  # tek repo
"""
import argparse
import re
import shutil
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GECICI, KAYNAKLAR, frontmatter, gh_api, json_oku, json_yaz  # noqa: E402

ARSIVLENEN_TIPLER = ("T1", "T2", "T3", "T4")
YOL_ONCELIGI = [r"^skills/", r"^plugin/skills/", r"^plugins/[^/]+/skills/", r"^\.claude/skills/",
                r"^\.agents/skills/", r"^\.codex/skills/"]
CLAUDE_YOL = r"^(.*/)?\.claude/skills/"
CODEX_YOL = r"^(.*/)?\.(agents|codex)/skills/"
BILESEN_DESEN = r"(^|/)(commands|agents)/[^/]+\.md$"
KARAR_GUCU = {"secildi": 5, "arac-varyanti": 5, "ayri-surum": 5, "ayna-ayni": 4, "ayna-baska-arac": 3, "haric": 2, "dahil-disi": 1}


def yol_puani(d):
    for i, p in enumerate(YOL_ONCELIGI):
        if re.match(p, d + "/"):
            return i
    return len(YOL_ONCELIGI)


def ilk_eslesen(desenler, metin):
    return next((p for p in desenler if re.search(p, metin)), None)


def is_skill_md(yol):
    return yol.split("/")[-1].lower() == "skill.md"


def skill_klasorlerini_sec(kayit, agac, ayar):
    """(secilenler, denetim) döndürür. denetim: her SKILL.md yolu -> karar."""
    konum_haric, repo_haric = ayar["konum_haric"], kayit.get("haric", [])
    blob_sha = {e["path"]: e["sha"] for e in agac if e["type"] == "blob"}
    denetim, adaylar = {}, []
    for e in agac:
        if e["type"] != "blob" or not is_skill_md(e["path"]):
            continue
        d = e["path"].rsplit("/", 1)[0] if "/" in e["path"] else ""
        kontrol = (d + "/") if d else e["path"]
        if kayit.get("dahil") and not ilk_eslesen(kayit["dahil"], kontrol):
            denetim[e["path"]] = "dahil-disi"
            continue
        if kayit.get("dahil_degil") and ilk_eslesen(kayit["dahil_degil"], kontrol):
            denetim[e["path"]] = "dahil-disi"
            continue
        ust = (d.rsplit("/", 1)[0] + "/") if "/" in d else ""
        h = ilk_eslesen(repo_haric, kontrol) or ilk_eslesen(konum_haric, ust)
        if d and h:
            denetim[e["path"]] = f"haric:{h}"
            continue
        adaylar.append((d, e["path"]))

    gruplar = {}
    for d, tam in adaylar:
        ad = d.split("/")[-1] if d else kayit["repo"].split("/")[1]
        gruplar.setdefault(ad, []).append((d, tam))

    secilen = {}
    for ad, yollar in gruplar.items():
        def tur(d):
            if ilk_eslesen(ayar["ayna_klasorler"], d + "/"):
                return "baska-arac"
            if re.match(CLAUDE_YOL, d + "/"):
                return "claude"
            if re.match(CODEX_YOL, d + "/"):
                return "codex"
            return "genel"
        siniflanmis = [(d, tam, tur(d), blob_sha[tam]) for d, tam in yollar]
        ana_havuz = [x for x in siniflanmis if x[2] != "baska-arac"] or siniflanmis
        ana_havuz.sort(key=lambda x: (yol_puani(x[0]), x[0].count("/"), x[0]))
        ana = ana_havuz[0]
        kayitli_sha = {ana[3]: ana[0]}
        secilen[ad] = {"yol": ana[0], "varyantlar": {}, "aynalar": [], "ust": None}
        denetim[ana[1]] = "secildi"
        for arac in ("claude", "codex"):
            v = next((x for x in sorted(siniflanmis, key=lambda x: (x[0].count("/"), x[0]))
                      if x[2] == arac and x[3] != ana[3]), None)
            if v and v[3] not in kayitli_sha:
                secilen[ad]["varyantlar"][arac] = v[0]
                kayitli_sha[v[3]] = v[0]
                denetim[v[1]] = f"arac-varyanti:{arac}"
            elif v:
                secilen[ad]["varyantlar"][arac] = kayitli_sha[v[3]]
        sira = 2
        for d, tam, t, sha in siniflanmis:
            if tam in denetim:
                continue
            if sha in kayitli_sha:
                denetim[tam] = f"ayna-ayni:{kayitli_sha[sha] or '.'}"
                secilen[ad]["aynalar"].append(d)
            elif t == "baska-arac":
                denetim[tam] = "ayna-baska-arac"
                secilen[ad]["aynalar"].append(d)
            else:  # farklı içerik, ayna değil: kaybetme, ayrı sürüm olarak sakla
                yeni = f"{ad}~{sira}"
                sira += 1
                secilen[yeni] = {"yol": d, "varyantlar": {}, "aynalar": [], "ust": None, "asil_ad": ad}
                kayitli_sha[sha] = d
                denetim[tam] = f"ayri-surum:{yeni}"
    # iç içe skiller: ayrı skill olarak da kurulabilsin, üst skill'i not et
    yollar = {b["yol"]: a for a, b in secilen.items()}
    for ad, b in secilen.items():
        ust = [y for y in yollar if y != b["yol"] and (y == "" or b["yol"].startswith(y + "/"))]
        if ust:
            b["ust"] = yollar[max(ust, key=len)]
    return secilen, denetim


def dosyalari_listele(kayit, agac, d, ayar):
    haric = ayar["skill_ici_haric"]
    sinir = ayar["max_dosya_mb"] * 1024 * 1024
    sonuc, atlanan = [], []
    for e in agac:
        if e["type"] != "blob":
            continue
        if d:
            if not e["path"].startswith(d + "/"):
                continue
            rel = e["path"][len(d) + 1:]
        else:
            rel = e["path"]
            if kayit.get("kok_dosyalari") and rel not in kayit["kok_dosyalari"]:
                continue
        if not is_skill_md(rel) and (ilk_eslesen(haric, rel) or e.get("size", 0) > sinir):
            atlanan.append(rel)
            continue
        sonuc.append((e["path"], "SKILL.md" if is_skill_md(rel) and "/" not in rel else rel))
    return sonuc, atlanan


def bilesenleri_bul(kayit, agac, secilen, ayar):
    """Skill klasörü dışındaki komut/agent tanımları (.claude/commands, plugins/*/agents …)."""
    skill_yollari = [b["yol"] for b in secilen.values()]
    sonuc = []
    for e in agac:
        p = e["path"]
        if e["type"] != "blob" or not re.search(BILESEN_DESEN, p):
            continue
        if any(y == "" or p.startswith(y + "/") for y in skill_yollari):
            continue
        if re.search(r"^(\.github|docs?|tests?)/|(^|/)tests?/", p) or ilk_eslesen(ayar["ayna_klasorler"], p):
            continue
        if kayit.get("dahil") and not ilk_eslesen(kayit["dahil"], p):
            continue
        sonuc.append(p)
    return sonuc


def indir(url, hedef):
    hedef.parent.mkdir(parents=True, exist_ok=True)
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                hedef.write_bytes(r.read())
            return True
        except Exception:  # noqa: BLE001
            if i == 3:
                return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo")
    a = ap.parse_args()
    ayar = json_oku(KAYNAKLAR)
    cikis = GECICI / "cekilen"
    cikis.mkdir(parents=True, exist_ok=True)
    manifest = json_oku(cikis / "manifest.json", {"kayitlar": [], "denetim": {}, "bilesenler": []})
    kayitlar = [k for k in ayar["repolar"] if k["tip"] in ARSIVLENEN_TIPLER]
    if a.repo:
        kayitlar = [k for k in kayitlar if k["repo"] == a.repo]
        manifest["kayitlar"] = [m for m in manifest["kayitlar"] if m["repo"] != a.repo]
        manifest["bilesenler"] = [m for m in manifest.get("bilesenler", []) if m["repo"] != a.repo]
        manifest.setdefault("denetim", {}).pop(a.repo, None)
    else:
        manifest = {"kayitlar": [], "denetim": {}, "bilesenler": []}

    toplam_hata = 0
    for kayit in kayitlar:
        repo = kayit["repo"]
        kimlik = kayit.get("kimlik") or repo.replace("/", "__")
        sha = gh_api(f"repos/{repo}/commits/HEAD")["sha"]
        lisans = (gh_api(f"repos/{repo}").get("license") or {}).get("spdx_id") or "belirtilmemiş"
        govde = gh_api(f"repos/{repo}/git/trees/{sha}?recursive=1")
        if govde.get("truncated"):
            sys.exit(f"HATA: {repo} dosya ağacı GitHub tarafından kesildi; eksik skill riski. Bu repo için sparse clone gerekir.")
        agac = govde["tree"]
        secilen, denetim = skill_klasorlerini_sec(kayit, agac, ayar)
        md = manifest["denetim"].setdefault(repo, {"commit": sha, "skill_md": {}})
        for yol, karar in denetim.items():  # aynı reponun birden fazla kaydı varsa en "güçlü" karar kalır
            onceki = md["skill_md"].get(yol)
            if onceki is None or KARAR_GUCU.get(karar.split(":")[0], 0) > KARAR_GUCU.get(onceki.split(":")[0], 0):
                md["skill_md"][yol] = karar
        hedef_kok = cikis / kimlik
        shutil.rmtree(hedef_kok, ignore_errors=True)
        isler, beklenen = [], {}
        for ad, bilgi in secilen.items():
            yollar = {"ana": bilgi["yol"], **bilgi["varyantlar"]}
            bilgi["atlanan"] = []
            for tur, d in yollar.items():
                if tur != "ana" and d == bilgi["yol"]:
                    continue
                alt = ad if tur == "ana" else f"_varyant/{ad}/{tur}"
                dosyalar, atlanan = dosyalari_listele(kayit, agac, d, ayar)
                if tur == "ana":
                    bilgi["atlanan"] = atlanan
                beklenen[alt] = len(dosyalar)
                for tam, rel in dosyalar:
                    url = f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(tam)}"
                    isler.append((url, hedef_kok / alt / rel))
        bilesenler = bilesenleri_bul(kayit, agac, secilen, ayar)
        for p in bilesenler:
            isler.append((f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(p)}",
                          hedef_kok / "_bilesen" / p))
            manifest["bilesenler"].append({"repo": repo, "kimlik": kimlik, "commit": sha, "yol": p,
                                          "yerel": str((hedef_kok / "_bilesen" / p).relative_to(GECICI))})
        with ThreadPoolExecutor(16) as ex:
            sonuclar = list(ex.map(lambda x: indir(*x), isler))
        hatali = sum(1 for s in sonuclar if not s)
        toplam_hata += hatali
        for ad, bilgi in secilen.items():
            sm = hedef_kok / ad / "SKILL.md"
            fm = frontmatter(sm.read_text(encoding="utf-8", errors="replace")) if sm.exists() else {}
            gercek = sum(1 for p in (hedef_kok / ad).rglob("*") if p.is_file()) if (hedef_kok / ad).exists() else 0
            varyantlar = {}
            for arac, d in bilgi["varyantlar"].items():
                yerel = hedef_kok / "_varyant" / ad / arac
                varyantlar[arac] = str(yerel.relative_to(GECICI)) if yerel.exists() else None
            manifest["kayitlar"].append({
                "repo": repo, "tip": kayit["tip"], "oncelik": kayit.get("oncelik", 5), "kimlik": kimlik,
                "commit": sha, "lisans": lisans, "klasor_adi": ad, "kaynak_yol": bilgi["yol"],
                "asil_ad": bilgi.get("asil_ad"), "ust_skill": bilgi["ust"],
                "aynalar": bilgi["aynalar"], "atlanan_dosyalar": bilgi["atlanan"],
                "varyantlar": varyantlar, "varyant_yollari": bilgi["varyantlar"],
                "ad": fm.get("name") or bilgi.get("asil_ad") or ad, "aciklama": fm.get("description", ""),
                "bagimlilik": kayit.get("bagimlilik"),
                "beklenen_dosya": beklenen.get(ad, 0), "inen_dosya": gercek,
                "yerel": str((hedef_kok / ad).relative_to(GECICI)),
            })
        print(f"{repo:42s} {kayit['tip']} {sha[:7]}  skill={len(secilen):4d}  dosya={len(isler):5d}  "
              f"bilesen={len(bilesenler):3d}  hata={hatali}")
    json_yaz(cikis / "manifest.json", manifest)
    print(f"Toplam kayıt: {len(manifest['kayitlar'])} · indirme hatası: {toplam_hata}")
    if toplam_hata:
        sys.exit("HATA: bazı dosyalar inmedi; tekrar çalıştır.")


if __name__ == "__main__":
    main()
