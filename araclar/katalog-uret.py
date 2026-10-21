#!/usr/bin/env python3
"""registry.json -> KATALOG.md (+ KATALOG-entegrasyon.md, notlar/teknoloji-secim-rehberi.md). Elle düzenleme yapma."""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KATEGORILER, KOK, REGISTRY, json_oku  # noqa: E402

UYUM = {"tam": "✅", "uyarlanabilir": "🟡", "konu-claude-ozel": "🔵"}
YUK = {"kucuk": "S", "orta": "M", "buyuk": "L"}


def satir(s):
    ozet = (s.get("ozet_tr") or s["aciklama"]).replace("|", "/").replace("\n", " ")
    ozet = ozet[:140] + ("…" if len(ozet) > 140 else "")
    tek = ", ".join(s.get("teknoloji") or s["teknoloji_oto"][:5])
    glob = ",".join(f"{k}:{v}" for k, v in s.get("globalde", {}).items()) or "-"
    durum = "⭐" if s["durum"] == "tercih" else "alt"
    if s.get("kaynak_durumu") == "kaynakta-kaldirildi":
        durum += " 🗄️emekli"
    elif s.get("kaynak_durumu") == "kayip":
        durum += " 🗄️kayıp"
    if s.get("ortusme_rolu"):
        durum += f" {s['ortusme_rolu']}"
    d = s.get("degerlendirme", {})
    return (f"| `{s['id']}` | {durum} | {ozet} | {tek} | {UYUM.get(s['uyum']['codex'], '?')} | "
            f"{d.get('puan', '-')} {d.get('not', '')} | {YUK[s['baglam_yuku']]} {s['boyut_kb']}KB | {glob} | {s['repo']} |")


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
           "**İşaretler:** ⭐ tercih edilen · `alt` aynı isimli alternatif sürüm · Codex: ✅ tam uyumlu, "
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
                    "| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |",
                    "|---|---|---|---|---|---|---|---|---|"]
            out += [satir(s) for s in liste] or ["| – | | | | | | | | |"]
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
    for r, g in sorted(gel.items(), key=lambda x: -x[1]["yildiz"]):
        gl.append(f"| [{r}](https://github.com/{r}) | {g['sahip']} | {g['sahip_tipi']} | {'✅' if g['resmi_kaynak'] else ''} | "
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
    print(f"KATALOG.md: {len(gorunur)} · gizli: {len(gizli)} (repo-içi {len(repo_ici)}) · bileşen: {len(reg.get('bilesenler', []))} · teknoloji: {len(tek)}")


if __name__ == "__main__":
    main()
