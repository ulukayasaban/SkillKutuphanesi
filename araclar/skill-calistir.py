#!/usr/bin/env python3
"""Skill çalıştırma testi: her skill'i GERÇEK kurulum yoluyla geçici bir projeye kurar ve agent'ın onu kullanabildiğini sınar.
Kütüphaneyi, arşivi ve global skill klasörlerini değiştirmez. Sonuç: TEST_RAPORU.md (+ .gecici/skill-test.json).

  python3 araclar/skill-calistir.py                 # tüm skiller: kurulum + yükleme + bağlantı + betik sözdizimi
  python3 araclar/skill-calistir.py --skill a b     # sadece bu skiller
  python3 araclar/skill-calistir.py --ajan araclar/ornek-gorevler.json  # + gerçek Claude Code ile örnek görev
      (sonuçlar .gecici/skill-test.json'da birikir; --ajan olmadan çalışınca son agent sonuçları raporda kalır)

Her skill için (Claude ve Codex sürümü ayrı ayrı):
  1. kurulum   skill-ekle.py hazirla() ile kopyalanır (ad eşitleme, frontmatter/description onarımı dahil)
  2. yukleme   frontmatter ilk satırda mı, YAML ayrışıyor mu, name == klasör adı mı, description 40..1024 mü
  3. baglanti  SKILL.md'nin göreli bağlantıları ve `scripts/…` gibi paket içi yollar kurulan kopyada var mı
  4. betik     .py derlenir (çalıştırılmaz), .sh `bash -n`, .js/.mjs/.cjs `node --check`, .json ayrıştırılır
  5. ornek     skill'in örnek görevi (kullanim_alani ya da description'daki "Use when") rapora yazılır
--ajan: verilen örnek görevler için skill geçici projeye kurulur ve `claude -p` sadece okuma araçlarıyla çalıştırılır;
Skill aracıyla bu skill'i yükleyip yüklemediğine bakılır (dosya yazamaz, komut çalıştıramaz).
"""
import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import ACIKLAMA_SINIRI, FM_BASTA, GECICI, KOK, REGISTRY, frontmatter, json_oku, json_yaz  # noqa: E402

try:
    import yaml
except ImportError:
    yaml = None

_spec = importlib.util.spec_from_file_location("skill_ekle", KOK / "araclar" / "skill-ekle.py")
se = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(se)

RAPOR = KOK / "TEST_RAPORU.md"
ORNEKLER = KOK / "notlar" / "skill-ornek-gorevler"  # alan başına bir sayfa
SONUC = GECICI / "skill-test.json"
PAKET_YOLU = re.compile(r"`((?:scripts|references|reference|assets|templates|examples|bin|lib|resources)/[\w./-]+\.\w{1,5})`")
ATLA = re.compile(r"(^|/)(node_modules|\.git|__pycache__|\.venv|venv|dist|build)(/|$)")


def ornek_gorev(s):
    """Skill'in örnek görevi: elle incelenmişse Türkçe kullanim_alani, değilse description'daki 'Use when …' cümlesi."""
    if s.get("kullanim_alani"):
        return s["kullanim_alani"].strip()
    d = (s.get("aciklama_duzeltme") or {}).get("description") or s.get("aciklama") or ""
    m = re.search(r"(?:Use (?:this skill )?(?:whenever|when|for|to)|Trigger(?:s)? (?:on|when|with)|TRIGGER[^:]*:?)\s*(.+?)(?:\.\s|$)", d, re.I | re.S)
    if m:
        return m.group(1).strip()[:300]
    return (re.split(r"(?<=[.!?])\s", d.strip(), maxsplit=1)[0] if d else s["ad"])[:300]


def yukleme_kontrol(sm: Path, ad: str):
    """Claude Code / Codex yükleyicisinin gördüğü gibi okur."""
    metin = sm.read_text(encoding="utf-8", errors="replace")
    m = FM_BASTA.match(metin)
    if not m:
        return ["HATA", "frontmatter ilk satırda başlamıyor; skill yüklenmez"], {}
    try:
        fm = yaml.safe_load(m.group(3)) if yaml else frontmatter(metin)
    except yaml.YAMLError as e:
        return ["HATA", "frontmatter YAML ayrışmıyor: " + str(e).splitlines()[0]], {}
    if not isinstance(fm, dict):
        return ["HATA", "frontmatter bir anahtar/değer listesi değil"], {}
    sorun = []
    if str(fm.get("name", "")).strip() != ad:
        sorun += ["HATA", f"name ({fm.get('name')!r}) klasör adıyla ({ad}) aynı değil"]
    d = fm.get("description")
    if not isinstance(d, str) or not d.strip():
        sorun += ["HATA", "description yok"]
    elif len(d) > ACIKLAMA_SINIRI:
        sorun += ["HATA", f"description {len(d)} karakter > {ACIKLAMA_SINIRI} (Codex yüklemez)"]
    elif len(d.strip()) < 40:
        sorun += ["UYARI", f"description çok kısa ({len(d.strip())} karakter)"]
    return sorun, fm


def baglanti_kontrol(kopya: Path, kardesler=()):
    """Kardeş skill bağlantıları (../<kardeş>/…) sayılmaz: onlar kurulumda kardeşle birlikte çözülür (ön kontrol uyarır)."""
    metin = (kopya / "SKILL.md").read_text(encoding="utf-8", errors="replace")
    eksik = set()
    for hedef in re.findall(r"\]\(([^)\s]+)\)", metin):
        if re.match(r"^(https?:|#|mailto:|<|\$|\{|/)", hedef) or "*" in hedef:
            continue
        yol = hedef.split("#")[0].split("?")[0]
        if yol.startswith("../") and yol[3:].split("/")[0] in kardesler:
            continue
        if yol and not (kopya / yol).exists() and not (kopya / yol).resolve().exists():
            eksik.add(yol)
    for yol in PAKET_YOLU.findall(metin):
        if "<" not in yol and not (kopya / yol).exists():
            eksik.add(yol)
    return sorted(eksik)


def betik_kontrol(kopya: Path):
    """Betikleri ÇALIŞTIRMADAN sözdizimi açısından sınar. Döner: (sayılar, [(dosya, hata)])"""
    say, hatalar = Counter(), []
    for f in sorted(kopya.rglob("*")):
        if not f.is_file() or f.is_symlink() or ATLA.search(str(f.relative_to(kopya))):
            continue
        rel = str(f.relative_to(kopya))
        uz = f.suffix.lower()
        try:
            if uz == ".py":
                say["py"] += 1
                kaynak = f.read_bytes()
                try:
                    compile(kaynak, rel, "exec", dont_inherit=True)
                except SyntaxError as e:
                    ipucu = " (Python 2 sözdizimi)" if re.search(rb"^\s*print [^(=]", kaynak, re.M) else ""
                    hatalar.append((rel, f"Python sözdizimi: {e.msg} (satır {e.lineno}){ipucu}"))
            elif uz == ".sh":
                say["sh"] += 1
                r = subprocess.run(["bash", "-n", str(f)], capture_output=True, text=True, timeout=30)
                if r.returncode:
                    hatalar.append((rel, "bash -n: " + r.stderr.strip().splitlines()[-1][:200]))
            elif uz in (".js", ".mjs", ".cjs"):
                say["js"] += 1
                r = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True, timeout=30)
                if r.returncode:
                    satir = [x for x in r.stderr.splitlines() if "Error" in x]
                    hatalar.append((rel, "node --check: " + (satir[0] if satir else r.stderr.strip()[:200])[:200]))
            elif uz == ".json":
                say["json"] += 1
                metin = f.read_text(encoding="utf-8-sig", errors="replace")
                if f.name not in ("tsconfig.json", "jsconfig.json") and not f.name.endswith((".jsonc", "devcontainer.json")):
                    json.loads(metin)
        except json.JSONDecodeError as e:
            hatalar.append((rel, f"JSON: {e.msg} (satır {e.lineno})"))
        except (subprocess.TimeoutExpired, OSError) as e:
            hatalar.append((rel, f"denenemedi: {e}"))
    return dict(say), hatalar


def skill_test(s, kok: Path):
    ad = s["ad"]
    sonuc = {"id": s["id"], "ad": ad, "kategori": s["kategori"], "gizli": s["gizli"], "ornek_gorev": ornek_gorev(s),
             "hatalar": [], "uyarilar": [], "betik": {}}
    surumler = {"ana": s["yol"], **{k: v for k, v in (s.get("varyantlar") or {}).items() if v}}
    for arac, yol in surumler.items():
        hedef = kok / s["id"].replace("@", "_") / arac / ad
        etiket = "" if arac == "ana" else f"[{arac}] "
        try:
            se.hazirla(KOK / yol, hedef, s, ad)
        except Exception as e:  # kurulum yolu bozuksa diğer kontroller anlamsız
            sonuc["hatalar"].append(f"{etiket}kurulum başarısız: {type(e).__name__}: {e}")
            continue
        sorun, _ = yukleme_kontrol(hedef / "SKILL.md", ad)
        for i in range(0, len(sorun), 2):
            (sonuc["hatalar"] if sorun[i] == "HATA" else sonuc["uyarilar"]).append(etiket + sorun[i + 1])
        eksik = baglanti_kontrol(hedef, s.get("kardes_bagimliliklari") or {})
        if eksik:
            sonuc["uyarilar"].append(f"{etiket}SKILL.md'nin andığı {len(eksik)} dosya pakette yok: {', '.join(eksik[:4])}")
        say, hatalar = betik_kontrol(hedef)
        if arac == "ana":
            sonuc["betik"] = say
        for rel, h in hatalar:
            sonuc["hatalar"].append(f"{etiket}{rel}: {h}")
        shutil.rmtree(hedef.parent, ignore_errors=True)
    sonuc["durum"] = "HATA" if sonuc["hatalar"] else "UYARI" if sonuc["uyarilar"] else "GECTI"
    return sonuc


# ------------------------------------------------------------------ gerçek agent ile örnek görev
def ajan_test(s, gorev, model, zaman_asimi=240):
    """Skill'i boş bir geçici projeye kurar, claude -p'ye örnek görevi verir; Skill aracıyla yüklendi mi?"""
    with tempfile.TemporaryDirectory(prefix="skill-ajan-") as t:
        proje = Path(t)
        subprocess.run(["git", "init", "-q"], cwd=proje)
        se.hazirla(KOK / (s.get("varyantlar") or {}).get("claude", s["yol"]), proje / ".claude" / "skills" / s["ad"], s, s["ad"])
        komut = ["claude", "-p", gorev, "--output-format", "stream-json", "--verbose", "--max-turns", "4",
                 "--allowedTools", "Skill,Read,Glob,Grep", "--disallowedTools", "Bash,Write,Edit,NotebookEdit,WebFetch,WebSearch"]
        if model:
            komut += ["--model", model]
        zaman_doldu = False
        try:
            r = subprocess.run(komut, cwd=proje, capture_output=True, text=True, timeout=zaman_asimi, stdin=subprocess.DEVNULL)
            cikti, kod, hata_metni = r.stdout, r.returncode, r.stderr
        except subprocess.TimeoutExpired as e:  # skill yüklenip uzun bir işe girişmiş olabilir: o ana kadarki çıktı okunur
            cikti = e.stdout.decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
            kod, hata_metni, zaman_doldu = 0, "", True
        yuklenen, gorunur, maliyet = [], False, None
        for satir in cikti.splitlines():
            try:
                o = json.loads(satir)
            except ValueError:
                continue
            if o.get("type") == "system" and o.get("subtype") == "init":
                gorunur = s["ad"] in (o.get("skills") or []) or s["ad"] in json.dumps(o.get("slash_commands") or [])
            if o.get("type") == "assistant":
                for c in o["message"].get("content", []):
                    if c.get("type") == "tool_use" and c.get("name") == "Skill":
                        yuklenen.append(str(c.get("input", {}).get("skill") or c.get("input", {}).get("command")))
                    if c.get("type") == "tool_use" and c.get("name") == "Read" and f"skills/{s['ad']}/SKILL.md" in json.dumps(c.get("input")):
                        yuklenen.append(s["ad"] + " (Read)")
            if o.get("type") == "result":
                maliyet = o.get("total_cost_usd")
        return {"id": s["id"], "gorev": gorev, "gorunur": gorunur, "yuklenen": yuklenen,
                "tetiklendi": any(y.split(" ")[0] == s["ad"] for y in yuklenen),  # eklenti:ad başka bir skill'dir
                "maliyet": maliyet, "zaman_doldu": zaman_doldu,
                "hata": ("zaman aşımı" if zaman_doldu else None) if kod == 0 else hata_metni.strip()[-300:]}


# ------------------------------------------------------------------ rapor
def duzeltilenler():
    """Bulunup kurulum aşamasında düzeltilen hatalar (registry + arşivden hesaplanır; arşiv değişmez)."""
    from ortak import symlink_taslaklari
    skiller = json_oku(REGISTRY)["skiller"]
    yamali = [s for s in skiller if s.get("yama")]
    taslakli = [(s, symlink_taslaklari(KOK / s["yol"])) for s in skiller]
    taslakli = [(s, t) for s, t in taslakli if t]
    duz = [s for s in skiller if s.get("aciklama_duzeltme")]
    oto = [s for s in skiller if any("dosya başında değil" in y or "tırnaksız" in y for y in s.get("yapisal_sorunlar", []))]
    m = ["## 🔧 Bulunan ve düzeltilen hatalar\nHepsi **kurulan kopyada** düzeltilir; `arsiv/` altındaki orijinaller değişmez. "
         "Bu düzeltmeler olmadan aşağıdaki skiller ❌ çıkıyordu.\n\n| Hata | Skill | Düzeltme |\n|---|---|---|\n"]
    for s in yamali:
        m.append(f"| Betik çalışmıyor: {s['yama'].get('neden', '')} | `{s['id']}` | `yamalar/{s['id']}/` "
                 f"({', '.join(s['yama']['dosyalar'])}); yamalı betik örnek görevle çalıştırıldı, üretilen TSX derlendi |\n")
    for s, t in taslakli:
        m.append(f"| Kaynaktaki git symlink'leri arşive düz metin olarak gelmiş ({len(t)} dosya, ör. `{next(iter(t))}` → "
                 f"`../{next(iter(t))}`): SKILL.md'deki alt-skill bağlantıları ölüydü | `{s['id']}` | Kurulumda taslak silinir, "
                 "bağlantılar kardeş skill'e çevrilir; kardeş kurulmazsa ön kontrol `kardes-eksik` uyarır |\n")
    m.append(f"| Description yok / çok kısa / 1024'ten uzun: agent skill'i doğru durumda seçemiyordu | {len(duz)} skill | "
             "`registry.json` → `aciklama_duzeltme` (`notlar/tetiklenme-denetimi.md`) |\n")
    m.append(f"| Frontmatter HTML yorumunun arkasında ya da description YAML'ı bozuyor | {len(oto)} skill | Kurulumda kendiliğinden |\n\n")
    return "".join(m)


def rapor_yaz(sonuclar, ajan, model):
    say = Counter(x["durum"] for x in sonuclar)
    betik = Counter()
    for x in sonuclar:
        betik.update(x["betik"])
    ust = (f"# Skill Test Raporu\n\nTarih: {date.today()} · Araç: `python3 araclar/skill-calistir.py`"
           f"{' --ajan' if ajan else ''} · Kütüphaneyi ve global skill klasörlerini değiştirmez.\n\n"
           "## Nasıl test edildi\n"
           "Her skill (Claude ve Codex sürümü ayrı ayrı) **gerçek kurulum yoluyla** (`skill-ekle.py` → `hazirla()`: ad eşitleme, "
           "frontmatter/description onarımı) geçici bir projeye kuruldu ve şunlar sınandı:\n\n"
           "| Adım | Ne bakılır | Sonuç türü |\n|---|---|---|\n"
           "| Yükleme | Frontmatter ilk satırda, YAML ayrışıyor, `name` = klasör adı, `description` 40–1024 karakter | HATA |\n"
           "| Betik | `.py` derlenir (çalıştırılmaz), `.sh` → `bash -n`, `.js/.mjs/.cjs` → `node --check`, `.json` ayrıştırılır | HATA |\n"
           "| Bağlantı | SKILL.md'nin göreli bağlantıları ve `scripts/…` gibi paket içi yollar kurulan kopyada var mı | UYARI |\n"
           "| Örnek görev | Elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki \"Use when …\" | rapora yazılır |\n"
           "| Agent (örneklem) | Skill boş projeye kurulur, `claude -p` örnek görevle **sadece okuma araçlarıyla** çalıştırılır; "
           "Skill aracıyla bu skill'i yükledi mi | tetiklendi / tetiklenmedi |\n\n"
           "**Neden her skill gerçek agent'la değil:** 3815 skill × bir agent oturumu saatler ve ciddi API maliyeti demek; "
           "üstelik skillerin çoğu dış servis, API anahtarı ya da kullanıcı projesi ister. Bu yüzden tüm skiller otomatik "
           "kontrolden, kategorilerden seçilen bir örneklem de gerçek agent'tan geçti.\n\n")
    ozet = (f"## Özet\n| | Sayı |\n|---|---|\n| Test edilen skill | {len(sonuclar)} |\n| ✅ Geçti | {say['GECTI']} |\n"
            f"| ⚠️ Uyarı (çalışır, eksik dosya bağlantısı var) | {say['UYARI']} |\n| ❌ Hata | {say['HATA']} |\n"
            f"| Sözdizimi denetlenen dosya | py {betik['py']} · sh {betik['sh']} · js {betik['js']} · json {betik['json']} |\n\n")
    bolum = []
    if ajan:
        for x in ajan:
            x["tetiklendi"] = any(y.split(" ")[0] == x["id"].split("@")[0] for y in x.get("yuklenen") or [])
            baska = [y for y in x.get("yuklenen") or [] if ":" in y and y.split(":")[-1] == x["id"].split("@")[0]]
            if not x["tetiklendi"] and baska:
                x["hata"] = f"ortamdaki aynı adlı eklenti skill'i seçildi ({', '.join(baska)}); kurulan skill değil"
        tet = sum(1 for a in ajan if a["tetiklendi"])
        bilinen = [a["maliyet"] for a in ajan if a.get("maliyet") is not None]
        mal = sum(bilinen)
        bolum.append(f"## Gerçek agent testi (örneklem: {len(ajan)} skill · model: {model or 'varsayılan'} · "
                     f"tetiklenen {tet}/{len(ajan)} · maliyet ≈ ${mal:.2f}"
                     f"{f' ({len(bilinen)} koşu kayıtlı; diğerleri ≈ ${mal / len(bilinen):.2f}/koşu)' if bilinen and len(bilinen) < len(ajan) else ''})\n"
                     "| Skill | Örnek görev | Sonuç | Yüklenen |\n|---|---|---|---|\n" +
                     "".join(f"| `{a['id']}` | {a['gorev'][:140].replace('|', '/')} | "
                             f"{'✅ tetiklendi' if a['tetiklendi'] else '❌ ' + (a.get('hata') or 'tetiklenmedi')[:80].replace('|', '/')} | "
                             f"{', '.join(a.get('yuklenen') or []) or '-'}"
                             f"{'<br><sub>ilk deneme: ' + ('zaman aşımı' if (a['ilk_deneme'].get('hata') == 'zaman aşımı') else 'tetiklenmedi') + ' (görev: ' + a['ilk_deneme']['gorev'][:70].replace('|', '/') + ')</sub>' if a.get('ilk_deneme') else ''} |\n"
                             for a in ajan) + "\n")
    bolum.append(duzeltilenler())
    hatali = [x for x in sonuclar if x["durum"] == "HATA"]
    if hatali:
        bolum.append("## ❌ Hatalar\n| Skill | Kategori | Hata |\n|---|---|---|\n" + "".join(
            f"| `{x['id']}` | {x['kategori']} | {'<br>'.join(h.replace('|', '/') for h in x['hatalar'][:6])}"
            f"{' …(+%d)' % (len(x['hatalar']) - 6) if len(x['hatalar']) > 6 else ''} |\n" for x in hatali) + "\n")
    uyar = [x for x in sonuclar if x["durum"] == "UYARI"]
    if uyar:
        bolum.append(f"## ⚠️ Uyarılar ({len(uyar)})\nSkill yüklenir ve çalışır; SKILL.md'nin andığı bazı dosyalar pakette yok "
                     "(çoğu kaynak repoda da yok ya da kullanıcının projesindeki bir dosyayı gösteriyor).\n\n"
                     "<details><summary>Liste</summary>\n\n| Skill | Uyarı |\n|---|---|\n" + "".join(
                         f"| `{x['id']}` | {'<br>'.join(u.replace('|', '/') for u in x['uyarilar'][:3])} |\n" for x in uyar)
                     + "\n</details>\n\n")
    shutil.rmtree(ORNEKLER, ignore_errors=True)
    ORNEKLER.mkdir(parents=True)
    alanlar = {}
    for x in sonuclar:
        alanlar.setdefault(x["kategori"].split("/")[0], []).append(x)
    for alan, liste in sorted(alanlar.items()):
        (ORNEKLER / f"{alan}.md").write_text(
            f"# Örnek görevler ve test sonucu › {alan}\n\n[← TEST_RAPORU.md](../../TEST_RAPORU.md) · {date.today()} · "
            f"{len(liste)} skill. Örnek görev: elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki "
            "\"Use when …\".\n\n| Skill | Sonuç | Örnek görev |\n|---|---|---|\n" + "".join(
                f"| `{x['id']}` | {'✅' if x['durum'] == 'GECTI' else '⚠️' if x['durum'] == 'UYARI' else '❌'} | "
                f"{x['ornek_gorev'][:160].replace('|', '/').replace(chr(10), ' ')} |\n" for x in liste), encoding="utf-8")
    bolum.append(f"## Tüm skiller ve örnek görevleri\n{len(sonuclar)} skill'in tek tek sonucu ve örnek görevi, alana göre: " +
                 " · ".join(f"[{a}](notlar/skill-ornek-gorevler/{a}.md) ({len(l)})" for a, l in sorted(alanlar.items())) + "\n")
    RAPOR.write_text(ust + ozet + "".join(bolum), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Skill çalıştırma testi (kütüphaneyi değiştirmez)")
    ap.add_argument("--skill", nargs="+", help="sadece bu skill id'leri")
    ap.add_argument("--ajan", help="örnek görev dosyası (JSON: {skill_id: görev}) -> gerçek claude -p testi")
    ap.add_argument("--model", help="--ajan için model (varsayılan: claude CLI varsayılanı)")
    ap.add_argument("--is-parcacigi", type=int, default=8)
    ap.add_argument("--ajan-paralel", type=int, default=4, help="aynı anda kaç claude -p oturumu")
    a = ap.parse_args()
    skiller = json_oku(REGISTRY)["skiller"]
    if a.skill:
        skiller = [s for s in skiller if s["id"] in a.skill]
    GECICI.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skill-test-", dir=GECICI) as t:
        with ThreadPoolExecutor(a.is_parcacigi) as ex:
            sonuclar = list(ex.map(lambda s: skill_test(s, Path(t)), skiller))
    ajan = [] if a.ajan else (json_oku(SONUC, {}) or {}).get("ajan", [])  # --ajan yoksa son agent sonuçları raporda kalır
    if a.ajan:
        ids = {s["id"]: s for s in json_oku(REGISTRY)["skiller"]}
        def tek(is_):
            r = ajan_test(ids[is_[0]], is_[1], a.model)
            print(("  ✅ " if r["tetiklendi"] else "  ❌ ") + is_[0], r.get("yuklenen"), r.get("hata") or "", flush=True)
            return r
        with ThreadPoolExecutor(a.ajan_paralel) as ex:
            yeni = list(ex.map(tek, json_oku(a.ajan).items()))
        # önceki agent sonuçlarıyla birleştir (aynı skill yeniden denendiyse son sonuç geçerli, ilk deneme notlanır)
        onceki = {x["id"]: x for x in (json_oku(SONUC, {}) or {}).get("ajan", [])}
        for r in yeni:
            o = onceki.get(r["id"])
            if o and (o.get("tetiklendi") != r["tetiklendi"] or o.get("gorev") != r["gorev"]):
                r["ilk_deneme"] = {"gorev": o.get("gorev"), "tetiklendi": o.get("tetiklendi"), "hata": o.get("hata")}
            onceki[r["id"]] = r
        ajan = list(onceki.values())
    json_yaz(SONUC, {"tarih": str(date.today()), "sonuclar": sonuclar, "ajan": ajan})
    if not a.skill:
        rapor_yaz(sonuclar, ajan, a.model)
    say = Counter(x["durum"] for x in sonuclar)
    print(f"{len(sonuclar)} skill · ✅ {say['GECTI']} · ⚠️ {say['UYARI']} · ❌ {say['HATA']}"
          + (f" · agent: {sum(x['tetiklendi'] for x in ajan)}/{len(ajan)} tetiklendi" if ajan else ""))
    for x in sonuclar:
        if x["durum"] == "HATA" and a.skill:
            print("HATA", x["id"], x["hatalar"])
    return 1 if say["HATA"] else 0


if __name__ == "__main__":
    sys.exit(main())
