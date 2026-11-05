#!/usr/bin/env python3
"""Türkçe skill rehberini üretir: README-SKILLER.md (nasıl çağrılır + dizin) ve skiller/<alan>/<kategori>.md
(her skill: ne yapar, ne zaman kullanılır, nasıl çağrılır). Kaynak: registry.json + aciklama-tr.json (otomatik çeviri)
+ kurulacak SKILL.md'nin frontmatter'ı (argument-hint, user-invocable, disable-model-invocation).

  python3 araclar/skill-readme.py
Türkçe metin önceliği: elle inceleme (ozet_tr / kullanim_alani) > aciklama-tr.json (kaynakla eşleşiyorsa) > İngilizce.
"""
import hashlib
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KATEGORILER, KOK, REGISTRY, frontmatter, frontmatter_onar, json_oku  # noqa: E402

CIKTI = KOK / "README-SKILLER.md"
KLASOR = KOK / "skiller"
CEVIRI = KOK / "aciklama-tr.json"
PARCA = 400  # bir sayfadaki en fazla skill (GitHub büyük markdown dosyalarını göstermez)


def temiz(x, n=None):
    x = re.sub(r"\s+", " ", str(x or "")).strip().replace("|", "/")
    return (x[: n - 1].rstrip() + "…") if n and len(x) > n else x


def kaynak_metin(s):
    return ((s.get("aciklama_duzeltme") or {}).get("description") or s.get("aciklama") or s["ad"]).strip()[:700]


def turkce(s, ceviri):
    """(ne yapar, ne zaman, kaynak) — kaynak: 'inceleme' | 'ceviri' | 'ingilizce'"""
    if s.get("ozet_tr"):
        return s["ozet_tr"], s.get("kullanim_alani") or "", "inceleme"
    c = ceviri.get(s["id"]) or {}
    if c.get("ne") and c.get("kaynak") == hashlib.sha1(kaynak_metin(s).encode()).hexdigest()[:12]:
        return c["ne"], c.get("ne_zaman", ""), "ceviri"
    return kaynak_metin(s), "", "ingilizce"


def cagri(s):
    """Kurulan SKILL.md'nin frontmatter'ından çağrı biçimi."""
    f = KOK / s["yol"] / "SKILL.md"
    metin = f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""
    fm = frontmatter(frontmatter_onar(metin, s["ad"], (s.get("aciklama_duzeltme") or {}).get("description"))[0])
    arg = temiz(fm.get("argument-hint", ""), 60)
    elle_yok = str(fm.get("user-invocable", fm.get("user_invocable", "true"))).lower() == "false"
    oto_yok = str(fm.get("disable-model-invocation", "")).lower() == "true"
    slash = f"`/{s['ad']}{(' ' + arg) if arg else ''}`"
    if oto_yok:
        return f"**Sadece elle:** Claude {slash} · Codex `${s['ad']}`"
    if elle_yok:
        return "Otomatik (menüde görünmez; agent gerekince yükler)"
    return f"Otomatik · Claude {slash} · Codex `${s['ad']}`"


def satir(s, ceviri):
    ne, zaman, kaynak = turkce(s, ceviri)
    notlar = []
    if s["durum"] == "alternatif":
        notlar.append("alternatif sürüm")
    if s.get("ucret") == "ucretli":
        notlar.append("💰 ücretli")
    elif s.get("ucret") == "kismen":
        notlar.append("kısmen ücretli")
    if (s.get("uyum") or {}).get("codex") not in (None, "tam"):
        notlar.append("Codex: " + s["uyum"]["codex"])
    if (s.get("trend") or {}).get("durum") == "trendde":
        notlar.append("🔥trend")
    if kaynak == "ingilizce":
        notlar.append("çeviri yok")
    ad = f"`{s['id']}`" + (f"<br><sub>{s['repo']}</sub>")
    return (f"| {ad} | {temiz(ne, 260)} | {temiz(zaman, 200) or '—'} | {cagri(s)} | "
            f"{s['degerlendirme']['puan']} {s['degerlendirme']['not']}{' · ' + ', '.join(notlar) if notlar else ''} |\n")


def main():
    skiller = json_oku(REGISTRY)["skiller"]
    ceviri = json_oku(CEVIRI, {})
    alanlar = json_oku(KATEGORILER)["alanlar"]
    gruplu = defaultdict(list)
    for s in skiller:
        gruplu[s["kategori"]].append(s)
    shutil.rmtree(KLASOR, ignore_errors=True)
    kaynak_say = Counter(turkce(s, ceviri)[2] for s in skiller)
    dizin = []
    for alan, a in alanlar.items():
        alan_say = sum(len(gruplu.get(f"{alan}/{k}", [])) for k in a["kategoriler"])
        if not alan_say:
            continue
        dizin.append(f"\n### {a['baslik']} ({alan_say})\n| Kategori | Kapsam | Skill |\n|---|---|---|\n")
        for kat, aciklama in a["kategoriler"].items():
            liste = sorted(gruplu.get(f"{alan}/{kat}", []), key=lambda s: (s["durum"] != "tercih", -s["degerlendirme"]["puan"], s["id"]))
            if not liste:
                continue
            parcalar = [liste[i:i + PARCA] for i in range(0, len(liste), PARCA)]
            for no, parca in enumerate(parcalar, 1):
                ek = f"-{no}" if len(parcalar) > 1 else ""
                yol = KLASOR / alan / f"{kat}{ek}.md"
                yol.parent.mkdir(parents=True, exist_ok=True)
                gezinme = (" · bölümler: " + " ".join(f"[{i}]({kat}-{i}.md)" if i != no else f"**{i}**"
                                                       for i in range(1, len(parcalar) + 1))) if len(parcalar) > 1 else ""
                yol.write_text(
                    f"# {a['baslik']} › {kat}{f' ({no}/{len(parcalar)})' if ek else ''}\n\n{aciklama}\n\n"
                    f"[← Skill rehberi](../../README-SKILLER.md) · {len(liste)} skill{gezinme} · "
                    "puana göre sıralı (önce tercih edilen sürümler)\n\n"
                    "**Kurulum:** `python3 araclar/skill-ekle.py <proje> --skill <id> --kuru` → raporu gör → `--evet`. "
                    "Çağrı adı projede kurulan klasör adıdır (globalde aynı adlı farklı skill varsa `<ad>--kutuphane`).\n\n"
                    "| Skill | Ne yapar | Ne zaman kullanılır | Nasıl çağrılır | Puan · not |\n|---|---|---|---|---|\n"
                    + "".join(satir(s, ceviri) for s in parca), encoding="utf-8")
            gizli = " (gizli katalog)" if all(s["gizli"] for s in liste) else ""
            bag = (f"[{kat}](skiller/{alan}/{kat}.md)" if len(parcalar) == 1 else
                   f"{kat}: " + " · ".join(f"[{i}](skiller/{alan}/{kat}-{i}.md)" for i in range(1, len(parcalar) + 1)))
            dizin.append(f"| {bag}{gizli} | {temiz(aciklama, 120)} | {len(liste)} |\n")
    ust = f"""# Skill Rehberi (Türkçe)

Bu kütüphanedeki **{len(skiller)} skill'in** ne işe yaradığı ve nasıl çağrıldığı. Kategori sayfaları otomatik üretilir:
`python3 araclar/skill-readme.py`. Test sonuçları: [TEST_RAPORU.md](TEST_RAPORU.md) · kurulum ve araçlar: [README.md](README.md).

## Skill nedir?
Skill, bir agent'a belirli bir işi nasıl yapacağını öğreten klasördür: `SKILL.md` (talimatlar) ve gerekirse betikler,
şablonlar ve referans dosyaları. Agent başta sadece her skill'in **adını ve açıklamasını** (`description`) görür; iş buna
uyunca skill'in tamamını yükler. Bu yüzden skill'in "doğru durumda tetiklenmesi" açıklamasına bağlıdır.

## Nasıl kurulur?
Skiller globale değil, **sadece seçtiğin projeye** kurulur:
```bash
python3 araclar/skill-ekle.py --oner "etsy mağazası seo"                     # ne kullanmalıyım?
python3 araclar/skill-ekle.py ~/Projeler/magaza --skill etsy-seller-guide --kuru   # ön kontrol raporu
python3 araclar/skill-ekle.py ~/Projeler/magaza --skill etsy-seller-guide --evet   # kur
```
Claude Code `.claude/skills/<ad>/`, Codex `.agents/skills/<ad>/` klasöründen okur; araç ikisine de kurar.

## Nasıl çağrılır?
| Yol | Claude Code | Codex |
|---|---|---|
| **Otomatik** (varsayılan) | İsteğin skill'in açıklamasına uyar ("Etsy listing başlıklarımı iyileştir"); agent skill'i kendisi yükler | Aynı |
| **Elle** | `/<skill-adı> [argümanlar]` yaz (ör. `/etsy-seller-guide`) | İstemde `$<skill-adı>` ile an |
| **Adını söyleyerek** | "etsy-seller-guide skill'ini kullanarak …" | Aynı |
| **Agent rolüyle** | Rol kurulduysa (`--rol`) `.claude/agents/<rol>.md` skilleri önyükler | `.codex/agents/<rol>.toml` |

- Tablolardaki **"Sadece elle"** skiller (`disable-model-invocation: true`) otomatik tetiklenmez; adlarıyla çağrılır.
- **"Menüde görünmez"** skiller (`user-invocable: false`) `/` menüsünde çıkmaz; agent gerekince kendisi yükler.
- Argüman alan skillerde `/ad <argüman>` biçimi tabloda yazar (ör. `/design-handoff <Figma URL>`).
- **Claude hesabında aynı adlı skill varsa** (ör. claude.ai'deki `docx`, `pdf`, `xlsx`, `pptx`): Claude Code onu
  `anthropic-skills:<ad>` olarak yükler ve agent çoğu zaman onu seçer. `skill-ekle.py` kurulumda hesaptakini o projede
  gizler (`.claude/settings.json` → `skillOverrides`), böylece kütüphane sürümü kullanılır. Ön kontrol `hesap-cakismasi` der.

## Tablolar nasıl okunur?
- **Ne yapar / Ne zaman:** elle incelenmiş {kaynak_say['inceleme']} skill'de inceleme notu; {kaynak_say['ceviri']} skill'de açıklamanın
  otomatik Türkçe çevirisi (`aciklama-tr.json`, `araclar/ceviri-tr.py`){f"; {kaynak_say['ingilizce']} skill'de henüz İngilizce" if kaynak_say['ingilizce'] else ""}.
- **Puan:** 0–100 otomatik değerlendirme ve derece (A–D): kaynağın bakımı, GitHub güveni, yapı, inceleme notu.
- **Not:** alternatif sürüm, ücretli/kısmen ücretli (`notlar/ucretli-skiller.md`), Codex uyumu, 🔥trend.
- **Gizli katalog:** entegrasyon kataloğu (tek bir uygulama için hazır otomasyon) ve repo-içi (bir projenin kendi
  geliştiricilerine yönelik) skiller; öneri listesinde varsayılan olarak çıkmazlar ama `--skill <id>` ile kurulabilir.

## Dizin
"""
    CIKTI.write_text(ust + "".join(dizin), encoding="utf-8")
    print(f"README-SKILLER.md + skiller/: {len(skiller)} skill · {len(gruplu)} kategori · Türkçe: inceleme {kaynak_say['inceleme']}, "
          f"çeviri {kaynak_say['ceviri']}, İngilizce kalan {kaynak_say['ingilizce']}")


if __name__ == "__main__":
    main()
