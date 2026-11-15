#!/usr/bin/env python3
"""registry.json -> KATALOG.md (+ KATALOG-entegrasyon.md, notlar/teknoloji-secim-rehberi.md). Elle düzenleme yapma."""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KATEGORILER, KAYNAKLAR, KOK, REGISTRY, json_oku  # noqa: E402

UYUM = {"tam": "✅", "uyarlanabilir": "🟡", "konu-claude-ozel": "🔵"}
YUK = {"kucuk": "S", "orta": "M", "buyuk": "L"}


def satir(s):
    ozet = (s.get("ozet_tr") or s["aciklama"]).replace("|", "/").replace("\n", " ")
    ozet = ozet[:140] + ("…" if len(ozet) > 140 else "")
    tek = ", ".join(s.get("teknoloji") or s["teknoloji_oto"][:5])
    glob = ",".join(f"{k}:{v}" for k, v in s.get("globalde", {}).items()) or "-"
    durum = "⭐" if s["durum"] == "tercih" else "alt"
    if s.get("ortusme_rolu") == "emekli" and not s.get("kaynak_durumu"):
        durum += " 🗄️eski"
    if s.get("kaynak_durumu") == "kaynakta-kaldirildi":
        durum += " 🗄️emekli"
    elif s.get("kaynak_durumu") == "kayip":
        durum += " 🗄️kayıp"
    if s.get("trend"):
        durum += " 🔥"
    if s.get("ortusme_rolu"):
        durum += f" {s['ortusme_rolu']}"
    d = s.get("degerlendirme", {})
    ucret = {"ucretli": "💲 ücretli", "kismen": "½ kısmen", "belirsiz": "? belirsiz"}.get(s.get("ucret"), "ücretsiz")
    return (f"| `{s['id']}` | {durum} | {ozet} | {tek} | {ucret} | {UYUM.get(s['uyum']['codex'], '?')} | "
            f"{d.get('puan', '-')} {d.get('not', '')} | {YUK[s['baglam_yuku']]} {s['boyut_kb']}KB | {glob} | {s['repo']} |")


# Referans kütüphanesi -> ilgili skill eşlemesi (kartında "Skill:" satırı olmayanlar ya da ek adaylar için).
# Skill'in adı/açıklaması bu deseni içermeli (otomatik teknoloji etiketleri tek başına gürültülü).
REF_DESEN = {"mrdoob/three.js": r"three\.?js|threejs|webgl|webgpu", "pmndrs/react-three-fiber": r"react.three.fiber|\br3f\b",
             "pmndrs/drei": r"\bdrei\b", "tailwindlabs/tailwindcss": r"tailwind", "greensock/GSAP": r"\bgsap\b",
             "FFmpeg/FFmpeg": r"ffmpeg", "airbnb/lottie-web": r"lottie|bodymovin", "darkroomengineering/lenis": r"\blenis\b|smooth.scroll",
             "oframe/ogl": r"\bogl\b", "dequelabs/axe-core": r"axe-core|\baxe\b|wcag|accessibility audit",
             "figma/code-connect": r"code.connect", "QwikDev/partytown": r"partytown|third-party script",
             "ai/size-limit": r"size-limit|bundle size|bundle budget", "fontsource/fontsource": r"fontsource|self-host(ed)? font",
             "seek-oss/capsize": r"capsize|font metric", "barvian/number-flow": r"number.?flow|animated number",
             "argyleink/open-props": r"open.props", "14islands/r3f-scroll-rig": r"scroll.rig|r3f", "pmndrs/react-three-a11y": r"react-three-a11y",
             "vercel/next.js": r"next\.?js", "react/react": r"\breact\b", "microsoft/playwright": r"playwright",
             "GoogleChrome/lighthouse": r"lighthouse|core web vitals", "motion-canvas/motion-canvas": r"motion.canvas",
             "d3/d3": r"\bd3\b", "Tonejs/Tone.js": r"tone\.js|web audio", "ManimCommunity/manim": r"\bmanim",
             "liabru/matter-js": r"matter\.?js|2d physics", "pmndrs/cannon-es": r"cannon|3d physics", "paperjs/paper.js": r"paper\.js",
             "rough-stuff/rough": r"rough\.?js|hand.drawn|sketchy", "jwagner/simplex-noise.js": r"simplex|perlin|noise field",
             "metafizzy/zdog": r"zdog|pseudo.3d", "theatre-js/theatre": r"theatre\.js", "pmndrs/postprocessing": r"post.?processing|bloom",
             "opentypejs/opentype.js": r"opentype|glyph", "DavidHDev/react-bits": r"react.bits", "darkroomengineering/react-lenis": r"\blenis\b",
             "KaTeX/KaTeX": r"katex|latex", "openai/whisper": r"whisper", "librosa/librosa": r"librosa|beat detect",
             "meyda/meyda": r"meyda|audio feature", "blender/blender": r"blender"}


def ref_kartlari():
    """notlar/referans kartlarından: repo -> (sürüm, [skill adları], kart dosyası)."""
    kart = {}
    t6 = (KOK / "notlar" / "referans" / "tasarim-teknolojileri.md").read_text(encoding="utf-8")
    for blok in re.split(r"\n(?=### )", t6):
        m = re.match(r"### (.+?) — `([^`]+/[^`]+)`(?: · ([^·\n]+))?", blok)
        if m:
            sk = []
            for satir in blok.splitlines():
                if "**Skill:**" in satir:
                    sk += re.findall(r"`([a-z0-9][a-z0-9._@-]*)`", satir.split("**Skill:**", 1)[1].split("**Rol:**")[0])
            surum = (m.group(3) or "").strip()
            surum = surum if re.match(r"^(v?\d|r\d|metrics)", surum) else ""  # başlıkta sürüm yerine lisans/tarih olabilir
            kart[m.group(2)] = (surum, sk, "notlar/referans/tasarim-teknolojileri.md")
    t5 = (KOK / "notlar" / "referans" / "kutuphaneler.md").read_text(encoding="utf-8")
    for satir in t5.splitlines():
        h = [x.strip() for x in satir.strip("|").split("|")]
        if len(h) >= 4 and "/" in h[0] and not h[0].startswith("-") and h[0] != "Repo":
            kart.setdefault(h[0], ("", re.findall(r"`([a-z0-9][a-z0-9._@-]*)`", h[-1]), "notlar/referans/kutuphaneler.md"))
    return kart


def guven_raporu(skiller):
    """notlar/guven-siralamasi.md: başka bir projenin agent'ının DOĞRUDAN kullanacağı güven + referans rehberi."""
    gel = json_oku(KOK / "gelistiriciler.json", {"repolar": {}})["repolar"]
    tip = {}
    for k in json_oku(KAYNAKLAR)["repolar"]:
        tip.setdefault(k["repo"], k["tip"])
    kat_ad = {f"{a}/{c}": d for a, v in json_oku(KATEGORILER)["alanlar"].items() for c, d in v["kategoriler"].items()}
    gor = [s for s in skiller if not s.get("gizli") and s["durum"] == "tercih"]
    by_ad = {s["ad"]: s for s in gor}
    by_id = {s["id"]: s for s in skiller}
    repo_sk = defaultdict(list)
    for s in gor:
        repo_sk[s["repo"]].append(s)

    def gv(repo):
        return (gel.get(repo) or {}).get("guven") or {}

    def sk_etiket(s):
        g = gv(s["repo"])
        return f"`{s['id']}` {s['degerlendirme']['puan']}/{g.get('derece', '?')}"

    tarih = json_oku(KOK / "gelistiriciler.json", {}).get("guncelleme", "?")
    o = ["# Güven ve Referans Rehberi (agent için)", "",
         f"> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` {tarih}, `registry.json`). **ELLE DÜZENLEME** — "
         "her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).", "",
         "## 0. Bu dosyayı nasıl kullanırsın (karar kuralları)", "",
         "İki ayrı puan var, ikisine birden bak:",
         "- **Skill puanı** (0–100, A/B/C/D) — skill'in kendisi: bakım, lisans, Codex uyumu, bağlam yükü, yapı, elle kalite, trend + kaynağın GitHub güveninin 30 puanı.",
         "- **Kaynak güveni** (0–100, A/B/C/D, `#sıra`) — skill'in geldiği GitHub reposunun etkileşimi: yıldız, yıldız hızı, katkıcı, "
         "son 90 gün commit, fork, izleyici, son sürüm, lisans; resmî üretici sadece 5 puan. Derece GÖRELİ (kütüphanedeki skill kaynakları arasındaki yer).", "",
         "| Durum | Karar |", "|---|---|",
         "| Skill puanı ≥ 65 **ve** kaynak güveni A/B | Doğrudan aday |",
         "| Skill puanı ≥ 65, kaynak güveni C | Aday; aynı işi yapan A/B kaynaklı skill varsa onu seç |",
         "| Kaynak güveni D | Derece GÖRELİDİR: D = topluluk etkileşimi az (yeni/küçük repo), kalitesiz demek değil. Skill puanı ≥ 80 ise SKILL.md'yi okuyup \"düşük topluluk güveni\" diye işaretleyerek aday; < 80 ise sadece benzersiz bir iş yapıyorsa |",
         "| Skill puanı < 50 ya da `kalite 1` (yönlendirme) | Alma |",
         "| Aynı işi yapan iki aday | Önce skill puanı, eşitse kaynak güveni (sıra) yüksek olan; 🔥 trend eşitlikte öne geçirir |",
         "| Projede bir referans kütüphanesi kullanılıyor (bölüm 3) | O kütüphanenin \"ilgili skiller\"i öncelikli aday; skill'in anlattığı sürüm projedekine uymalı |",
         "| Ücret: 💲 ücretli | Ücret ödemeden kullanılamaz; sadece açıkça gerekiyorsa ve kullanıcıya belirterek |",
         "| Lisans `yok`/`NOASSERTION` | Ticari projede kullanıcıya işaretle |", "",
         "Skill kurulumu SADECE `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> … --kuru` → onay → `--evet`. "
         "Bir skill'in ayrıntısı: `KATALOG.md`, `registry.json` (id ile), SKILL.md (`registry.json` → `yol`).", ""]
    # 1. Kategori -> en güvenilir kaynaklar ve skiller
    o += ["## 1. Kategoriye göre en güvenilir kaynaklar ve en iyi skiller", "",
          "| Kategori | En güvenilir kaynaklar (güven · o kategorideki skill) | En yüksek puanlı skiller (`id` puan/kaynak derecesi) |", "|---|---|---|"]
    kat_sk = defaultdict(list)
    for s in gor:
        kat_sk[s["kategori"]].append(s)
    for k in sorted(kat_sk):
        l = kat_sk[k]
        rc = Counter(s["repo"] for s in l)
        kay = sorted(rc, key=lambda r: (-(gv(r).get("puan") or 0), -rc[r]))[:3]
        kays = " · ".join(f"{r} {gv(r).get('puan', '?')}{gv(r).get('derece', '')} ({rc[r]})" for r in kay)
        en = sorted(l, key=lambda s: (-s["degerlendirme"]["puan"], -(gv(s["repo"]).get("puan") or 0)))[:4]
        o.append(f"| `{k}` — {kat_ad.get(k, '')[:60]} | {kays} | {', '.join(sk_etiket(s) for s in en)} |")
    # 2. Skill kaynakları
    o += ["", "## 2. Skill kaynakları (GitHub güven sıralaması)", "",
          "| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    havuz = [r for r in gel if gv(r).get("sira")]
    for r in sorted(havuz, key=lambda r: gv(r)["sira"]):
        v, g, l = gel[r], gv(r), repo_sk.get(r, [])
        kc = Counter(s["kategori"].split("/")[1] for s in l).most_common(2)
        uc = Counter(s["ucret"] for s in l)
        tr = "🔥" if any(s.get("trend") for s in l) else ""
        o.append(f"| {g['sira']} | {r} | {g['puan']} {g['derece']} | {len(l)} | {', '.join(f'{a} ({n})' for a, n in kc) or '-'} | "
                 f"{uc.get('ucretsiz', 0)}/{uc.get('kismen', 0)}/{uc.get('ucretli', 0)} | {v['lisans']} | {'✓' if v['resmi_kaynak'] else ''} | "
                 f"{v['yildiz']} | {v.get('yildiz_hizi', '')} | {v.get('katkici', '')} | {v.get('commit_90g', '')} | {v.get('son_surum') or '-'} | {tr} |")
    # 3. Referans kütüphaneleri -> ilgili skiller
    kart = ref_kartlari()
    o += ["", "## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller", "",
          "Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: "
          "projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: \"Kart\" sütunu.", "",
          "| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |", "|---|---|---|---|---|---|"]
    ref = [r for r in gel if gv(r).get("referans_sira")]
    for r in sorted(ref, key=lambda r: gv(r)["referans_sira"]):
        g = gv(r)
        surum, adlar, dosya = kart.get(r, ("", [], ""))
        sk = []
        for a in adlar:
            s = by_id.get(a) or by_ad.get(a)
            if s and s not in sk and not s.get("gizli"):
                sk.append(s)
        desen = REF_DESEN.get(r)
        if desen:
            d = re.compile(desen, re.I)
            ek = sorted((s for s in gor if s not in sk and d.search(s["id"] + " " + s["aciklama"])),
                        key=lambda s: (-s["degerlendirme"]["puan"], -(gv(s["repo"]).get("puan") or 0)))
            sk += ek[: max(0, 8 - len(sk))]
        o.append(f"| {g['referans_sira']} | {r} | {g['puan']} {g['derece']} | {surum or '-'} | "
                 f"{', '.join(sk_etiket(s) for s in sk[:10]) or '— (skill eşlemesi yok)'} | {dosya.replace('notlar/referans/', '') or '-'} |")
    o += ["", "## 4. Hesap ayrıntısı", "",
          "Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · "
          "katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); "
          "arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. "
          "Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` "
          "(aylık güncellemede otomatik)."]
    (KOK / "notlar" / "guven-siralamasi.md").write_text("\n".join(o) + "\n", encoding="utf-8")


def main():
    skiller = json_oku(REGISTRY)["skiller"]
    kat = json_oku(KATEGORILER)["alanlar"]
    gorunur = [s for s in skiller if not s.get("gizli")]
    gizli = [s for s in skiller if s.get("gizli")]
    alan_say = defaultdict(int)
    for s in gorunur:
        alan_say[s["alan"]] += 1

    out = ["# Skill Kataloğu", "",
           "> `araclar/katalog-uret.py` üretir — elle düzenleme. Kaynak: `registry.json`.", "",
           f"Toplam **{len(gorunur)}** skill (+{len(gizli)} gizli: entegrasyon `KATALOG-entegrasyon.md`, repo-içi `notlar/referans/repo-ici-skiller.md`).", "",
           "**İşaretler:** ⭐ tercih edilen · `alt` aynı isimli alternatif sürüm · 🔥 kaynağı GitHub Trending'e girmiş (notlar/github-trend.md) · Codex: ✅ tam uyumlu, "
           "🟡 Claude araç adları geçiyor ama çalışır, 🔵 konusu Claude Code'a özel · Yük: S/M/L (agent bağlamına etkisi) · "
           "globalde: bilgisayardaki genel klasörde aynı isimli skill (ayni/farkli)", "",
           "## İçindekiler", ""]
    for a, v in kat.items():
        if a in ("e-entegrasyon-katalogu", "f-repo-ici"):
            continue
        out.append(f"- **{v['baslik']}** ({alan_say[a]})")
        for k, acik in v["kategoriler"].items():
            n = sum(1 for s in gorunur if s["kategori"] == f"{a}/{k}")
            out.append(f"  - [{k}](#{k}) — {n} skill · {acik}")
    for a, v in kat.items():
        if a in ("e-entegrasyon-katalogu", "f-repo-ici"):
            continue
        out += ["", f"## {v['baslik']}"]
        for k, acik in v["kategoriler"].items():
            liste = [s for s in gorunur if s["kategori"] == f"{a}/{k}"]
            out += ["", f"### {k}", "", f"_{acik}_ · not: `notlar/{a}/{k}.md`", "",
                    "| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |",
                    "|---|---|---|---|---|---|---|---|---|---|"]
            out += [satir(s) for s in liste] or ["| – | | | | | | | | | |"]
    (KOK / "KATALOG.md").write_text("\n".join(out) + "\n", encoding="utf-8")

    ent = ["# Entegrasyon Kataloğu (Composio)", "",
           "> Varsayılan listede gizli. Rube MCP (rube.app) bağlantısı ve uygulama başına Composio hesabı bağlantısı gerekir (COMPOSIO_API_KEY değil). Arama: "
           "`skill-ekle.py --listele --gizli --ara drive`. İnceleme raporu: `notlar/referans/composio-inceleme.md`", ""]
    t4 = [s for s in gizli if s["tip"] == "T4"]
    gruplar = defaultdict(list)
    for s in t4:
        gruplar[s.get("uygulama_grubu") or "diger"].append(s)
    sira = sorted(gruplar, key=lambda g: (g == "diger", -len(gruplar[g])))
    ent += ["## Gruplar", ""] + [f"- [{g}](#{g}) — {len(gruplar[g])}" for g in sira]
    for g in sira:
        ent += ["", f"## {g}", "", "| Skill | İnceleme | Ne yapar |", "|---|---|---|"]
        ent += [f"| `{s['id']}` | {s.get('inceleme', 'otomatik')} | {(s.get('ozet_tr') or s['aciklama'])[:140].replace('|', '/')} |"
                for s in gruplar[g]]
    (KOK / "KATALOG-entegrasyon.md").write_text("\n".join(ent) + "\n", encoding="utf-8")

    reg = json_oku(REGISTRY)
    repo_ici = [s for s in gizli if s["tip"] == "T3"]
    ri = ["# Repo-İçi Geliştirici Skilleri (gizli)", "", "> Bu skiller ilgili repoya katkı yapanlar içindir. "
          "Arama: `skill-ekle.py --listele --gizli --kategori f-repo-ici`", "", "| Skill | Repo | Ne yapar |", "|---|---|---|"]
    ri += [f"| `{s['id']}` | {s['repo']} | {s['aciklama'][:110].replace('|', '/')} |" for s in repo_ici]
    (KOK / "notlar" / "referans" / "repo-ici-skiller.md").write_text("\n".join(ri) + "\n", encoding="utf-8")
    bl = ["# Skill Olmayan Bileşenler (komut / agent tanımları)", "",
          "> Skillerle birlikte gelen slash command ve alt-agent dosyaları. Arşivde: `arsiv/_bilesenler/`. Otomatik kurulmaz; "
          "gerekirse Claude için `.claude/commands/` ya da `.claude/agents/` içine elle kopyalanır.", "",
          "| Tür | Ad | Repo | Yol |", "|---|---|---|---|"]
    bl += [f"| {b['tur']} | `{b['ad']}` | {b['repo']} | `{b['kaynak_yol']}` |" for b in reg.get("bilesenler", [])]
    (KOK / "notlar" / "referans" / "bilesenler.md").write_text("\n".join(bl) + "\n", encoding="utf-8")
    gel = json_oku(KOK / "gelistiriciler.json", {"repolar": {}})["repolar"]
    say = defaultdict(int)
    for s in skiller:
        say[s["repo"]] += 1
    gl = ["# Skill Geliştiricileri", "", "> `araclar/gelistirici-bilgisi.py` ile GitHub'dan alınır. Puanlama: `rehber/06-degerlendirme-ve-gelistirici.md`.", "",
          "| Repo | Sahip | Tip | Resmî | ★ | Katkıcı | Son güncelleme | Lisans | Arşivdeki skill |", "|---|---|---|---|---|---|---|---|---|"]
    yerel_repolar = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T7", "T8")}  # yerel kaynak (kendi/, site/): GitHub bağlantısı yok
    for r, g in sorted(gel.items(), key=lambda x: -x[1]["yildiz"]):
        gl.append(f"| {r if r in yerel_repolar else f'[{r}](https://github.com/{r})'} | {g['sahip']} | {g['sahip_tipi']} | {'✅' if g['resmi_kaynak'] else ''} | "
                  f"{g['yildiz']} | {g.get('katkici') or '-'} | {g['son_guncelleme']} | {g['lisans']} | {say.get(r, 0)} |")
    (KOK / "notlar" / "gelistiriciler.md").write_text("\n".join(gl) + "\n", encoding="utf-8")

    # Kategori notları: her skill için kart (registry'den üretilir; elle bilgi registry'ye yazılır)
    for a, v in kat.items():
        for k, acik in v["kategoriler"].items():
            liste = [s for s in skiller if s["kategori"] == f"{a}/{k}"]
            if not liste or a in ("e-entegrasyon-katalogu",):
                continue
            incelenen = sum(1 for s in liste if s.get("inceleme") == "incelendi")
            md = [f"# {k} — {v['baslik']}", "", f"_{acik}_", "",
                  f"> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır "
                  f"(bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **{incelenen}/{len(liste)}**", ""]
            for s in liste:
                g, d = s.get("gelistirici") or {}, s["degerlendirme"]
                md += [f"### {s['id']}  ·  {s['repo']} @ {s['commit'][:7]}  ·  puan {d['puan']} ({d['not']})", "",
                       f"- **Ne yapar:** {s.get('ozet_tr') or s['aciklama'][:400]}"]
                if s.get("kullanim_alani") or s.get("kullanma"):
                    md.append(f"- **Ne zaman:** {s.get('kullanim_alani', '-')} · **Ne zaman değil:** {s.get('kullanma', '-')}")
                md += [f"- **Teknoloji:** {', '.join(s.get('teknoloji') or s['teknoloji_oto']) or '-'}"
                       + (" _(otomatik tespit)_" if not s.get("teknoloji") else "")
                       + (f" · **Paketler:** {', '.join(s['gerekli_paketler'])}" if s.get("gerekli_paketler") else ""),
                       f"- **Claude / Codex:** {s['uyum']['claude']} / {s['uyum']['codex']}" + (f" — {s['uyum']['not']}" if s['uyum'].get('not') else ""),
                       f"- **Geliştirici:** {g.get('sahip', '?')} ({g.get('sahip_tipi', '?')}{', resmî' if g.get('resmi_kaynak') else ''}, "
                       f"★{g.get('yildiz', '?')}, son güncelleme {g.get('son_guncelleme', '?')}, lisans {g.get('lisans', s['lisans'])})",
                       f"- **Durum:** {s['durum']}" + (f" · **Örtüşme:** {s['ortusme_grubu']} → {s.get('ortusme_rolu', '?')}" if s.get('ortusme_grubu') else "")
                       + (f" · **Roller:** {', '.join(s['roller'])}" if s.get("roller") else "")
                       + (f" · **Globalde:** {', '.join(f'{x}:{y}' for x, y in s['globalde'].items())}" if s.get("globalde") else ""),
                       f"- **Boyut:** {s['boyut_kb']} KB (SKILL.md {s['skill_md_kb']} KB, yük {s['baglam_yuku']})"
                       + (f" · **Bağımlılık:** {s['bagimlilik']}" if s.get("bagimlilik") else "")
                       + (f" · **Kırık bağlantı:** {len(s['kirik_baglantilar'])}" if s.get("kirik_baglantilar") else ""),
                       f"- **İnceleme:** {s.get('inceleme', 'otomatik')}" + (f" · kalite {s['kalite']}/5 — {s.get('kalite_notu', '')}" if s.get("kalite") else "")]
                if s.get("notlar"):
                    md.append(f"- **Not:** {s['notlar']}")
                md.append("")
            yol = KOK / "notlar" / a / f"{k}.md"
            yol.parent.mkdir(parents=True, exist_ok=True)
            yol.write_text("\n".join(md), encoding="utf-8")

    # Roller ve profiller özeti (roller/*.json ve profiller/*.json'dan üretilir)
    import glob as _g
    rl = {Path(p).stem: json_oku(p) for p in sorted(_g.glob(str(KOK / "roller" / "*.json")))}
    pr = {Path(p).stem: json_oku(p) for p in sorted(_g.glob(str(KOK / "profiller" / "*.json")))}
    kb = {s["id"]: s["skill_md_kb"] for s in skiller}
    out2 = ["# Roller ve Profiller", "",
            "> `araclar/katalog-uret.py` üretir (roller/*.json, profiller/*.json). Kullanım: "
            "`skill-ekle.py <proje> --profil <ad>` veya `--rol <ad>`.", "",
            f"## Profiller ({len(pr)})", "", "| Profil | Ne için | Roller |", "|---|---|---|"]
    out2 += [f"| `{a}` | {p['baslik']} | {', '.join(f'`{r}`' for r in p['roller'])} |" for a, p in pr.items()]
    out2 += ["", f"## Roller ({len(rl)})", "", "| Rol | Görevi | Çekirdek | Opsiyonel (`--opsiyonel`) | Yük |", "|---|---|---|---|---|"]
    for a, r in rl.items():
        tum = r["cekirdek"] + r.get("opsiyonel", [])
        out2.append(f"| `{a}` | {r['aciklama']} | {', '.join(r['cekirdek'])} | {', '.join(r.get('opsiyonel', []))} | "
                    f"{len(tum)} skill, {sum(kb.get(x, 0) for x in tum):.0f} KB |")
    kullanilan = {x for p in pr.values() for x in p["roller"]}
    kayip = sorted(set(rl) - kullanilan)
    if kayip:
        out2 += ["", f"Hiçbir profilde olmayan roller (yalnız `--rol` ile): {', '.join(kayip)}"]
    (KOK / "notlar" / "roller-ve-profiller.md").write_text("\n".join(out2) + "\n", encoding="utf-8")

    # Ücretli / kısmen ücretli skiller
    uc = ["# Ücretli ve Kısmen Ücretli Skiller", "",
          "> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; "
          "ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.", ""]
    for sinif, baslik in (("ucretli", "💲 Ücretli (ücret ödemeden hiç kullanılamaz)"),
                          ("kismen", "½ Kısmen (ücret ödemeden kullanılabilir: ücretsiz katman ya da ücretli servis sadece bir seçenek)"),
                          ("belirsiz", "? Sınıflandırılmamış")):
        liste = sorted((s for s in gorunur if s.get("ucret") == sinif), key=lambda s: (s["kategori"], s["id"]))
        if not liste:
            continue
        uc += [f"## {baslik} — {len(liste)}", "", "| Skill | Kategori | Neden |", "|---|---|---|"]
        uc += [f"| `{s['id']}` | {s['kategori'].split('/')[1]} | {s.get('ucret_notu', '').replace('|', '/')} |" for s in liste]
        uc.append("")
    gizli_k = sum(1 for s in gizli if s.get("ucret") == "kismen")
    uc += [f"Gizli entegrasyon kataloğundaki {gizli_k} Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var)."]
    (KOK / "notlar" / "ucretli-skiller.md").write_text("\n".join(uc) + "\n", encoding="utf-8")

    tek = defaultdict(list)
    for s in gorunur:
        if s["durum"] != "tercih":
            continue
        for t in s.get("teknoloji") or s["teknoloji_oto"]:
            tek[t].append(s["id"])
    rehber = ["# Teknolojiye Göre Skill Rehberi", "",
              "> Otomatik üretilir. Teknoloji etiketleri inceleme sırasında elle düzeltilir (`teknoloji` alanı); "
              "henüz incelenmemiş skillerde otomatik tespit (`teknoloji_oto`) kullanılır.", ""]
    for t in sorted(tek, key=lambda x: -len(tek[x])):
        rehber += [f"## {t} ({len(tek[t])})", "", ", ".join(f"`{x}`" for x in sorted(tek[t])), ""]
    (KOK / "notlar" / "teknoloji-secim-rehberi.md").write_text("\n".join(rehber), encoding="utf-8")
    guven_raporu(skiller)
    print(f"KATALOG.md: {len(gorunur)} · gizli: {len(gizli)} (repo-içi {len(repo_ici)}) · bileşen: {len(reg.get('bilesenler', []))} · teknoloji: {len(tek)}")


if __name__ == "__main__":
    main()
