# 02-tasarim-sistemi-marka — Tasarım ve Ön Yüz

_Design token, tema, marka kimliği, banner/logo_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **3/11**

### banner-design  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 56ea9cf  ·  puan 90 (A)

- **Ne yapar:** Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Actions: design, create, generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero, print. Styles: minimalist, gradient, bold typography, photo-based, illustrated, geometric, retro, glassmorph
- **Teknoloji:** canvas, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138431, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### brand  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 56ea9cf  ·  puan 95 (A)

- **Ne yapar:** Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides.
- **Teknoloji:** api-anahtari, css, node, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138431, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 106 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### brand-guidelines  ·  anthropics/skills @ dbd4588  ·  puan 88 (A)

- **Ne yapar:** Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### brand-guidelines@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 88 (A)

- **Ne yapar:** Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif
- **Boyut:** 13 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### design  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 56ea9cf  ·  puan 77 (B)

- **Ne yapar:** claudekit birleşik tasarım skilli: marka kimliği, token, UI stili, AI ile logo üretimi (55 stil; Gemini, Atlas Cloud veya MuAPI), 50 teslimatlı kurumsal kimlik (CIP) maketleri, HTML sunumlar, banner (22 stil), SVG ikon ve sosyal medya görselleri. brand, design-system ve ui-styling kardeş alt skillerine yönlendirir.
- **Ne zaman:** Logo, kurumsal kimlik seti, banner, ikon veya sosyal medya görseli üretimi; marka paketi çıkarma. · **Ne zaman değil:** Web sayfası tasarımı (01 kategorisindeki skiller); API anahtarı olmadan AI logo/ikon üretimi.
- **Teknoloji:** python, html, css, gemini, api-anahtari · **Paketler:** python3, google-genai, pillow, GEMINI_API_KEY veya MUAPI_API_KEY
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138431, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** marka-gorsel-varlik → birincil · **Roller:** tasarim-sistemi
- **Boyut:** 284 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Geniş kapsamlı 'her şey' skilli; marka/banner/logo işleri için 02 kategorisine taşındı. Kardeş skiller (brand, design-system, ui-styling) olmadan eksik çalışır; AI üretimi için ücretli API anahtarı ve pip kurulumu gerekir.

### design-spec  ·  vudovn/ag-kit @ 549ba3d  ·  puan 85 (A)

- **Ne yapar:** DESIGN.md dosyası yazma rehberi: makinece okunur tasarım token'ları (YAML ön bilgi: renk, tipografi, boşluk, köşe, bileşen) ile insan okunur gerekçenin tek gerçek kaynakta birleştiği format; kanonik bölüm sırası, token adlandırma önerileri ve 70+ gerçek DESIGN.md örneği (collection.md). Google Labs DESIGN.md spesifikasyonundan uyarlanmış.
- **Ne zaman:** UI koduna başlamadan önce projenin DESIGN.md'sini oluştururken veya güncellerken. · **Ne zaman değil:** Görsel yön henüz belirsizken (önce design-taste-frontend / design-dna); tek bileşenlik işler.
- **Teknoloji:** markdown, yaml · **Paketler:** @google/design.md (npx, isteğe bağlı linter)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarim-referans-analizi → tamamlayıcı · **Roller:** ui-tasarimci, tasarim-sistemi
- **Boyut:** 21 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Net şema ve gerçek örnek kütüphanesi; impeccable ve design-dna çıktılarıyla uyumlu. Konu itibarıyla tasarım sistemi kategorisine taşındı.

### design-system  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 56ea9cf  ·  puan 95 (A)

- **Ne yapar:** Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strategic slide creation. Use for design tokens, systematic design, brand-compliant presentations.
- **Teknoloji:** api-anahtari, canvas, css, html, node, python, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138431, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 178 KB (SKILL.md 7.3 KB, yük kucuk)
- **İnceleme:** otomatik

### tailwind-design-system  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component libraries, implementing design systems, or standardizing UI patterns.
- **Teknoloji:** api-anahtari, css, react, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 22 KB (SKILL.md 21.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### tailwind-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Tailwind CSS v4 ilkeleri: CSS-öncelikli @theme yapılandırması, kapsayıcı sorguları, OKLCH renk token mimarisi, karanlık mod, tipografi ölçeği, bileşen çıkarma ve anti-kalıplar.
- **Ne zaman:** Tailwind v4 projesinde token mimarisi ve modern CSS kalıpları kurulurken. · **Ne zaman değil:** Tailwind v3 projeleri (yapılandırma farklı); Tailwind kullanılmayan projeler.
- **Teknoloji:** tailwind, css · **Paketler:** tailwindcss>=4
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** shadcn-tailwind-uygulama → tamamlayıcı · **Roller:** frontend-muhendis
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ilke özeti, v3→v4 farkları faydalı; kod örneği derinliği sınırlı. Konu itibarıyla tasarım sistemi kategorisine taşındı (tailwind-design-system ile birlikte değerlendirilmeli).

### theme-factory  ·  anthropics/skills @ dbd4588  ·  puan 88 (A)

- **Ne yapar:** Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 141 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### theme-factory@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 88 (A)

- **Ne yapar:** Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif
- **Boyut:** 141 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik
