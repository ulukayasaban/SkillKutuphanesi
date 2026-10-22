# Skill Kataloğu

> `araclar/katalog-uret.py` üretir — elle düzenleme. Kaynak: `registry.json`.

Toplam **538** skill (+878 gizli: entegrasyon `KATALOG-entegrasyon.md`, repo-içi `notlar/referans/repo-ici-skiller.md`).

**İşaretler:** ⭐ tercih edilen · `alt` aynı isimli alternatif sürüm · Codex: ✅ tam uyumlu, 🟡 Claude araç adları geçiyor ama çalışır, 🔵 konusu Claude Code'a özel · Yük: S/M/L (agent bağlamına etkisi) · globalde: bilgisayardaki genel klasörde aynı isimli skill (ayni/farkli)

## İçindekiler

- **Tasarım ve Ön Yüz** (201)
  - [01-ui-ux-tasarim-dili](#01-ui-ux-tasarim-dili) — 34 skill · Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi
  - [02-tasarim-sistemi-marka](#02-tasarim-sistemi-marka) — 30 skill · Design token, tema, marka kimliği, banner/logo
  - [03-animasyon-motion](#03-animasyon-motion) — 32 skill · GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim
  - [04-scroll-deneyimi](#04-scroll-deneyimi) — 7 skill · Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri
  - [05-3d-webgl](#05-3d-webgl) — 35 skill · Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader
  - [06-oyun-2d-grafik](#06-oyun-2d-grafik) — 13 skill · Oyun geliştirme, PixiJS, 2D grafik
  - [07-gorsel-sanat-sunum](#07-gorsel-sanat-sunum) — 35 skill · Poster/canvas tasarımı, generative art, slayt, GIF
  - [08-onyuz-test-kalite](#08-onyuz-test-kalite) — 15 skill · Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı
- **Yazılım Geliştirme** (86)
  - [01-planlama-metodoloji](#01-planlama-metodoloji) — 20 skill · Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini
  - [02-kod-kalitesi-review](#02-kod-kalitesi-review) — 11 skill · Code review, sadeleştirme, temiz kod
  - [03-test-hata-ayiklama](#03-test-hata-ayiklama) — 11 skill · TDD, hata ayıklama, doğrulama
  - [04-mimari-api-veritabani](#04-mimari-api-veritabani) — 8 skill · Mimari, API/arayüz tasarımı, veritabanı, backend
  - [05-git-pr-surum](#05-git-pr-surum) — 10 skill · Git, worktree, PR, sürüm/release, changelog
  - [06-devops-guvenlik-performans](#06-devops-guvenlik-performans) — 11 skill · CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans
  - [07-framework-ozel](#07-framework-ozel) — 15 skill · Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)
- **Doküman ve İçerik** (63)
  - [01-ofis-dokumanlari](#01-ofis-dokumanlari) — 17 skill · Word, Excel, PowerPoint, PDF üretme/düzenleme
  - [02-diyagram-dokumantasyon](#02-diyagram-dokumantasyon) — 8 skill · Diyagram, teknik dokümantasyon, ADR, ortak yazım
  - [03-yazi-iletisim-icerik](#03-yazi-iletisim-icerik) — 23 skill · Yazı, iletişim, pazarlama/içerik, kariyer
  - [04-not-alma-bilgi-yonetimi](#04-not-alma-bilgi-yonetimi) — 15 skill · Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni
- **AI ve Otomasyon** (65)
  - [01-claude-api-mcp](#01-claude-api-mcp) — 14 skill · Claude API, MCP sunucusu, model geçişi
  - [02-agent-orkestrasyon](#02-agent-orkestrasyon) — 23 skill · Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları
  - [03-web-arastirma-veri](#03-web-arastirma-veri) — 2 skill · Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma
  - [04-skill-plugin-yazimi](#04-skill-plugin-yazimi) — 26 skill · Skill yazma, plugin/hook/komut geliştirme
- **Video, Ses ve AI Medya Üretimi** (121)
  - [01-video-uretim-montaj](#01-video-uretim-montaj) — 45 skill · Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg
  - [02-ses-muzik-konusma](#02-ses-muzik-konusma) — 18 skill · Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi
  - [03-ai-gorsel-video-modelleri](#03-ai-gorsel-video-modelleri) — 40 skill · AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu
  - [04-motion-graphics-karakter](#04-motion-graphics-karakter) — 18 skill · Motion graphics, Manim, karakter animasyonu/rig, görsel stil

## Tasarım ve Ön Yüz

### 01-ui-ux-tasarim-dili

_Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi_ · not: `notlar/a-tasarim-onyuz/01-ui-ux-tasarim-dili.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `design-brief` | ⭐ | Parse a structured design brief written in I-Lang protocol format into a concrete design spec. Eliminates ambiguity from vague requests like… | api-anahtari, css, html | ücretsiz | ✅ | 28 D | M 13KB | - | nexu-io/open-design |
| `design-dna` | ⭐ birincil | Tasarım DNA'sını üç boyutta çıkarır, tanımlar ve uygular: tasarım sistemi (token), tasarım stili (nitel his) ve görsel efektler (Canvas, Web… | html, css, node, webgl | ücretsiz | ✅ | 82 A | M 709KB | claude:farkli | zanwei/design-dna |
| `design-taste-frontend` | ⭐ birincil | tasteskill v2: 247 seçkin galeri sitesinden damıtılmış 'anti-slop' sanat yönetimi. Betik araştırılmış 20 yönden üçünü dağıtır, seçilen yöne … | html, css, node, chromium | ücretsiz | ✅ | 93 A | L 2363KB | - | Leonxlnx/taste-skill |
| `design-taste-frontend-v1` | ⭐ | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 expe… | canvas, css, gsap, html, motion | ücretsiz | ✅ | 28 D | M 22KB | - | nexu-io/open-design |
| `design-taste-frontend@nexu-io` | alt | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and shi… | api-anahtari, canvas, css, git, gsap | ücretsiz | ✅ | 25 D | L 87KB | - | nexu-io/open-design |
| `faq-page` | ⭐ | A Frequently Asked Questions (FAQ) page with collapsible accordion sections, search functionality, and category filtering. Use when the brie… | api-anahtari, css, html | ücretsiz | ✅ | 30 D | S 21KB | - | nexu-io/open-design |
| `frontend-design@anthropics` | alt alternatif | frontend-design'ın anthropics/skills kopyası: içerik claude-code eklentisindekiyle birebir aynı, ayrıca LICENSE.txt içerir. | html, css | ücretsiz | ✅ | 84 A | M 19KB | - | anthropics/skills |
| `frontend-design@anthropics-2` | ⭐ tamamlayıcı | Anthropic'in kısa tasarım ilkeleri skilli: tasarım stüdyosu yöneticisi gibi konuya özgü, şablon gibi görünmeyen palet/tipografi/düzen kararl… | html, css | ücretsiz | ✅ | 84 A | M 9KB | - | anthropics/claude-code |
| `frontend-design@nexu-io` | alt | Create distinctive, production-grade frontend interfaces with strong visual direction, polished typography, considered layout, and working H… | api-anahtari, css, html, react, svelte | ücretsiz | ✅ | 30 D | S 15KB | - | nexu-io/open-design |
| `frontend-design@vudovn` | alt alternatif | ag-kit'in 'anti-slop' web UI skilli: brief çıkarımı, üç kadranlı (varyans/hareket/yoğunluk) yapılandırma, gerçek tasarım sistemi eşlemesi, t… | html, css, react, next.js, tailwind, python | ücretsiz | ✅ | 74 B | L 161KB | - | vudovn/ag-kit |
| `frontend-dev` | ⭐ | Full-stack frontend with cinematic animations, AI-generated media via MiniMax API, and generative art. Useful for hero pages and showcase si… |  | ½ kısmen | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `frontend-skill` | ⭐ | Create visually strong landing pages, websites, and app UIs with restrained composition. OpenAI's production frontend playbook. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `high-end-visual-design` | ⭐ | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a webs… | css, html, react, tailwind | ücretsiz | ✅ | 28 D | M 12KB | - | nexu-io/open-design |
| `image-to-code` | ⭐ | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply ana… | html | ücretsiz | ✅ | 25 D | L 37KB | - | nexu-io/open-design |
| `imagegen-frontend-mobile` | ⭐ | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-pla… | canvas, html, react | ücretsiz | ✅ | 25 D | L 41KB | - | nexu-io/open-design |
| `imagegen-frontend-web` | ⭐ | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE… | canvas | ücretsiz | ✅ | 25 D | L 38KB | - | nexu-io/open-design |
| `impeccable` | ⭐ birincil | Ön yüz arayüzlerini tasarlama, yeniden tasarlama, eleştirme, denetleme, cilalama ve sağlamlaştırma için komut tabanlı tasarım direktörü: sha… | html, css, node | ücretsiz | ✅ | 95 A | M 2140KB | - | pbakaus/impeccable |
| `industrial-brutalist-ui` | ⭐ | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilit… | css, html | ücretsiz | ✅ | 28 D | M 10KB | - | nexu-io/open-design |
| `login-flow` | ⭐ | Mobile login and authentication flow screens | html | ücretsiz | ✅ | 30 D | S 12KB | - | nexu-io/open-design |
| `minimalist-ui` | ⭐ | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy sha… | canvas, css, html, react, tailwind | ücretsiz | ✅ | 28 D | M 9KB | - | nexu-io/open-design |
| `mobile-design` | ⭐ birincil | iOS ve Android uygulamaları için mobil öncelikli tasarım düşüncesi: dokunma etkileşimi, başparmak bölgesi, platform gelenekleri, performans … | react-native, flutter, python | ücretsiz | ✅ | 84 A | M 216KB | - | vudovn/ag-kit |
| `modern-web-design` | ⭐ alternatif | 2024-2025 web tasarım trendleri ve kalıpları özeti: performans öncelikli tasarım, cesur minimalizm, mikro etkileşim, scrollytelling, imleç U… | html, css, gsap, three.js, react | ücretsiz | ✅ | 55 C | L 151KB | - | freshtechbro/claudedesignskills |
| `redesign-existing-projects` | ⭐ | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design s… | css, html, tailwind | ücretsiz | ✅ | 28 D | M 16KB | - | nexu-io/open-design |
| `reference-design-contract` | ⭐ | Turn vague taste, screenshots, URLs, product notes, or "make it feel like this" references into a grounded DESIGN.md plus an implementation … | api-anahtari, html | ücretsiz | ✅ | 30 D | S 12KB | - | nexu-io/open-design |
| `shadcn-ui` | ⭐ | Build UI components with shadcn/ui. Pairs with the Stitch design loop to ship structured, accessible components quickly. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `swiftui-design` | ⭐ | SwiftUI 前端设计 skill — anti AI-slop rules, design direction advisor, brand asset protocol, and five-dimension review. Works with Claude Code, … |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `ui-skills` | ⭐ | Opinionated, evolving constraints to guide agents when building interfaces. Useful for keeping output coherent across many small UI pieces. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `ui-styling` | ⭐ birincil | shadcn/ui (Radix + Tailwind) bileşenleri, Tailwind yardımcı sınıf stili ve canvas tabanlı görsel tasarımla erişilebilir arayüz kurma: tema/k… | react, tailwind, shadcn-ui, radix, python | ücretsiz | ✅ | 88 A | M 5627KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `ui-ux-pro-max` | ⭐ tamamlayıcı | Yerel aranabilir UI/UX veri tabanı: 79 stil, 192 ürün paleti ve gerekçe profili, 74 font eşleşmesi, 119 UX kuralı, ikonlar, GSAP ön ayarları… | python, html, css, tailwind | ücretsiz | 🟡 | 85 A | M 3499KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `ui-ux-pro-max@nexu-io` | alt | Catalog-only UI/UX Pro Max entry. The full upstream templates, data, and search workflow are not bundled in OpenDesign. | python | ücretsiz | ✅ | 30 D | S 2KB | - | nexu-io/open-design |
| `web-clone` | ⭐ | 网站复刻 / 克隆方法论。USE WHEN 用户说 复刻网站、克隆网站、clone website、抄个站、仿站、 照着这个站做一个、reproduce site、还原某个网页效果、把这个站搬下来改成我的、 复刻某个交互/WebGL/Canvas/Three.js 效果。提供「先… | api-anahtari, canvas, css, git, gsap | ücretsiz | ✅ | 28 D | M 198KB | - | nexu-io/open-design |
| `web-design-guidelines` | ⭐ tamamlayıcı | UI kodunu Vercel'in Web Interface Guidelines kurallarına göre denetler: kuralları her çalıştırmada GitHub'dan (vercel-labs/web-interface-gui… | html, css, react | ücretsiz | ✅ | 85 A | S 2KB | claude:farkli | vudovn/ag-kit |
| `web-design-guidelines@calesthio` | alt alternatif | web-design-guidelines'ın OpenMontage kopyası; ag-kit sürümünün 'İlgili skiller' ve iş akışı bölümleri olmadan aynı içerik. | html, css | ücretsiz | ✅ | 87 A | S 1KB | claude:ayni | calesthio/OpenMontage |
| `web-design-guidelines@nexu-io` | alt | Review UI code for Web Interface Guidelines compliance by the Vercel engineering team. Covers layout, typography, color, motion, and accessi… |  | ücretsiz | ✅ | 30 D | S 10KB | claude:farkli | nexu-io/open-design |

### 02-tasarim-sistemi-marka

_Design token, tema, marka kimliği, banner/logo_ · not: `notlar/a-tasarim-onyuz/02-tasarim-sistemi-marka.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `apple-hig` | ⭐ | Apple Human Interface Guidelines as 14 agent skills covering platforms, foundations, components, patterns, inputs, and technologies for iOS,… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `banner-design` | ⭐ tamamlayıcı | Sosyal medya kapakları, reklam bannerları, web hero görselleri ve baskı bannerları için çok formatlı tasarım akışı. Gereksinimleri sorar, 2-… | html, css | ücretsiz | 🟡 | 78 B | S 12KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand` | ⭐ tamamlayıcı | Marka sesi, görsel kimlik, mesajlaşma çerçeveleri, varlık yönetimi ve tutarlılık denetimi için kapsamlı kılavuz seti. `docs/brand-guidelines… | node, css, markdown | ücretsiz | ✅ | 89 A | S 106KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand-extract` | ⭐ | Extract a complete Brand Kit from a live website by driving the in-app browser. Use when a brand-extraction project opens with a site in the… | api-anahtari, css, html | ücretsiz | ✅ | 28 D | M 68KB | - | nexu-io/open-design |
| `brand-guidelines` | ⭐ tamamlayıcı | Anthropic'in kurumsal renk (koyu #141413, açık #faf9f5, turuncu/mavi/yeşil vurgu) ve tipografi (Poppins başlık, Lora gövde) kurallarını sunu… | python-pptx | ücretsiz | ✅ | 69 B | S 13KB | - | anthropics/skills |
| `brand-guidelines@composiohq` | alt alternatif | anthropics/skills'teki brand-guidelines'ın birebir kopyası: Anthropic renk ve tipografi kurallarını sunum/belgelere uygular. | python-pptx | ücretsiz | ✅ | 69 B | S 13KB | - | ComposioHQ/awesome-claude-skills |
| `brand-guidelines@nexu-io` | alt | Apply Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards. A refe… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `brandkit` | ⭐ | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world prese… | canvas, node | ücretsiz | ✅ | 28 D | M 17KB | - | nexu-io/open-design |
| `color-expert` | ⭐ | Color science expert skill with 286K words of reference material covering OKLCH/OKLAB, palette generation, accessibility/contrast, color nam… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `design` | ⭐ birincil | claudekit birleşik tasarım skilli: marka kimliği, token, UI stili, AI ile logo üretimi (55 stil; Gemini, Atlas Cloud veya MuAPI), 50 teslima… | python, html, css, gemini, api-anahtari | ½ kısmen | 🟡 | 77 B | M 284KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `design-consultation` | ⭐ | Build a complete design system from scratch with creative risks and realistic product mockups. Useful for kickoff workshops and brand-from-z… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `design-md` | ⭐ | Create and manage DESIGN.md files. Useful for capturing design direction, tokens, and visual rules in a single source of truth. | api-anahtari | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `design-spec` | ⭐ tamamlayıcı | DESIGN.md dosyası yazma rehberi: makinece okunur tasarım token'ları (YAML ön bilgi: renk, tipografi, boşluk, köşe, bileşen) ile insan okunur… | markdown, yaml | ücretsiz | ✅ | 85 A | S 21KB | - | vudovn/ag-kit |
| `design-system` | ⭐ birincil | Üç katmanlı (primitive, semantic, component) token mimarisi, CSS değişkenleri, boşluk/tipografi ölçekleri, bileşen durum spesifikasyonları v… | css, node, python, tailwindcss, chart.js | ücretsiz | ✅ | 89 A | S 178KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `figma-code-connect-components` | ⭐ | Connect Figma design components to code components using Code Connect so design-system updates flow into the codebase automatically. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-create-design-system-rules` | ⭐ | Generate project-specific design system rules for Figma-to-code workflows. Useful for capturing tokens, naming, and lint rules in one source… | api-anahtari | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-create-new-file` | ⭐ | Create a new blank Figma Design or FigJam file. Useful as the first step in scripted design-system or workshop workflows. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-generate-design` | ⭐ | Build or update screens in Figma from code or description using design system components. Translate app pages into Figma using design tokens… | api-anahtari | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-generate-library` | ⭐ | Build or update a professional-grade design system library in Figma from a codebase. Useful for keeping the Figma source of truth in sync wi… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-implement-design` | ⭐ | Translate Figma designs into production-ready code with 1:1 visual fidelity. Useful for handing off Figma frames straight to a frontend agen… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `figma-use` | ⭐ | Run Figma Plugin API scripts for canvas writes, inspections, variables, and design-system work. Prerequisite for every other Figma skill in … | canvas | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `platform-design` | ⭐ | 300+ design rules from Apple HIG, Material Design 3, and WCAG 2.2 for cross-platform apps. Useful when shipping a single design across iOS, … |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `stitch-design-taste` | ⭐ | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — s… | api-anahtari, canvas, css | ücretsiz | ✅ | 28 D | M 25KB | - | nexu-io/open-design |
| `stitch-loop` | ⭐ | Iterative design-to-code feedback loop. Critique → adjust → ship cycle for tightening visual fidelity between brief and built UI. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `tailwind-design-system` | ⭐ tamamlayıcı | Tailwind CSS v4 ile (CSS-first `@theme`, OKLCH renk) üretim kalitesinde tasarım sistemi kurma tarifi: semantik token'lar, CVA ile bileşen va… | tailwindcss, react, typescript, radix-ui | ücretsiz | ✅ | 86 A | M 22KB | claude:ayni | calesthio/OpenMontage |
| `tailwind-patterns` | ⭐ tamamlayıcı | Tailwind CSS v4 ilkeleri: CSS-öncelikli @theme yapılandırması, kapsayıcı sorguları, OKLCH renk token mimarisi, karanlık mod, tipografi ölçeğ… | tailwind, css | ücretsiz | ✅ | 77 B | S 7KB | - | vudovn/ag-kit |
| `theme-factory` | ⭐ birincil | 10 hazır renk+yazı tipi temasıyla (Ocean Depths, Midnight Galaxy, Tech Innovation vb.) slayt, belge, rapor veya HTML sayfasını tek seferde s… | html, css, pptx | ücretsiz | ✅ | 77 B | S 141KB | - | anthropics/skills |
| `theme-factory@composiohq` | alt alternatif | anthropics/skills'teki theme-factory'nin birebir kopyası: 10 hazır tema ile slayt/belge/HTML stillendirme. | html, css, pptx | ücretsiz | ✅ | 77 B | S 141KB | - | ComposioHQ/awesome-claude-skills |
| `theme-factory@nexu-io` | alt | Apply professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages. Ships 10 pre-set themes. | html | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `wpds` | ⭐ | WordPress Design System. Apply WordPress's official design tokens, typography, and component patterns to themes and sites. | api-anahtari | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |

### 03-animasyon-motion

_GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim_ · not: `notlar/a-tasarim-onyuz/03-animasyon-motion.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `animate` | ⭐ | Implement purposeful interface animations: easing, springs, interruption, exits, and reduced motion. Use on existing components or an accept… | api-anahtari, css, motion, three.js | ücretsiz | ✅ | 28 D | M 22KB | - | nexu-io/open-design |
| `animated-component-libraries` | ⭐ birincil | Magic UI (150+) ve React Bits (90+) hazır animasyonlu React bileşenlerini kullanma: shadcn CLI ile ekleme, özelleştirme, performans ve yaygı… | react 19, tailwind 4, motion v14, shadcn-ui, ogl | ücretsiz | ✅ | 65 B | M 89KB | - | freshtechbro/claudedesignskills |
| `animejs` | ⭐ alternatif | Anime.js ile DOM, CSS, SVG ve JS nesnesi animasyonu: timeline, stagger, SVG path/morph. GSAP'a hafif alternatif olarak anlatılır; üreticiler… | animejs 4, javascript | ücretsiz | ✅ | 65 B | M 62KB | - | freshtechbro/claudedesignskills |
| `emil-design-eng` | ⭐ | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make softw… | css, motion, node, react | ücretsiz | ✅ | 25 D | L 29KB | - | nexu-io/open-design |
| `emilkowalski-motion` | ⭐ | Motion-design follow-up skill inspired by Emil Kowalski's animation guidance. Use after an interface exists to add tasteful micro-interactio… | css, gsap, html, react | ücretsiz | ✅ | 30 D | S 3KB | - | nexu-io/open-design |
| `flutter-animating-apps` | ⭐ | Implement animated effects, transitions, and motion in Flutter apps. Useful for native iOS/Android motion design. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `framer-motion` | ⭐ alternatif | Disney'in 12 animasyon prensibini (squash/stretch, anticipation, staging...) Framer Motion kod parçalarıyla örnekler. Kurulum, reduced-motio… | motion v14, react | ücretsiz | ✅ | 71 B | S 3KB | claude:ayni | calesthio/OpenMontage |
| `gpt-taste` | ⭐ | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide… | css, gsap, html, python, react | ücretsiz | ✅ | 28 D | M 9KB | - | nexu-io/open-design |
| `gsap-core` | ⭐ birincil | GSAP çekirdek API'si: gsap.to/from/fromTo, ease, stagger, varsayılanlar ve gsap.matchMedia() ile responsive / prefers-reduced-motion animasy… | gsap 3.15, javascript, typescript | ücretsiz | ✅ | 97 A | M 14KB | claude:ayni | greensock/gsap-skills |
| `gsap-core@nexu-io` | alt | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, pref… | css, gsap, react, svelte, vue | ücretsiz | ✅ | 28 D | M 17KB | claude:farkli | nexu-io/open-design |
| `gsap-frameworks` | ⭐ tamamlayıcı | GSAP'ı Vue/Nuxt, Svelte/SvelteKit ve diğer yaşam döngülü framework'lerde kullanma: onMounted/onMount, selector scope, unmount temizliği, Scr… | gsap 3.15, vue 3, nuxt 4, svelte 5 | ücretsiz | ✅ | 89 A | M 10KB | claude:farkli | greensock/gsap-skills |
| `gsap-frameworks@calesthio` | alt alternatif | gsap-frameworks'ün OpenMontage'daki eski kopyası: Vue ve Svelte bölümleri aynı, Nuxt 4 bölümü ve örnek klasörü atıfları yok. | gsap 3.15, vue 3, svelte | ücretsiz | ✅ | 79 B | S 6KB | claude:ayni | calesthio/OpenMontage |
| `gsap-frameworks@nexu-io` | alt | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wa… | gsap, react, svelte, typescript, vue | ücretsiz | ✅ | 28 D | M 13KB | claude:farkli | nexu-io/open-design |
| `gsap-performance` | ⭐ tamamlayıcı | GSAP animasyonlarında performans: transform/opacity tercihi, will-change, okuma/yazma gruplama, çok elemanlı stagger ve ScrollTrigger maliye… | gsap 3.15, css | ücretsiz | ✅ | 98 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-performance@nexu-io` | alt | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations,… | css, gsap | ücretsiz | ✅ | 30 D | S 6KB | claude:farkli | nexu-io/open-design |
| `gsap-plugins` | ⭐ tamamlayıcı | GSAP eklentileri: ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, DrawSVG, MorphSVG, MotionPath… | gsap 3.15 | ücretsiz | ✅ | 97 A | M 21KB | claude:farkli | greensock/gsap-skills |
| `gsap-plugins@calesthio` | alt alternatif | gsap-plugins'in OpenMontage'daki eski kopyası. İçerik aynı eklenti kataloğu; tek fark yeni sürümdeki 'Licensing & Install' (tüm eklentiler ü… | gsap 3.15 | ücretsiz | ✅ | 86 A | M 20KB | claude:farkli | calesthio/OpenMontage |
| `gsap-plugins@nexu-io` | alt | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, Scramble… | api-anahtari, canvas, css, gsap, html | ücretsiz | ✅ | 28 D | M 23KB | claude:farkli | nexu-io/open-design |
| `gsap-react` | ⭐ tamamlayıcı | GSAP'ı React/Next.js'te kullanma: useGSAP hook'u, ref'ler, scope, gsap.context() ve unmount temizliği, SSR notları. Resmî skill; en sık yapı… | gsap 3.15, @gsap/react 2, react 19, next.js | ücretsiz | ✅ | 98 A | S 6KB | claude:ayni | greensock/gsap-skills |
| `gsap-react@nexu-io` | alt | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks … | gsap, next.js, node, react, svelte | ücretsiz | ✅ | 30 D | S 9KB | claude:farkli | nexu-io/open-design |
| `gsap-timeline` | ⭐ tamamlayıcı | GSAP timeline'ları: gsap.timeline(), position parametresi, iç içe timeline ve oynatma kontrolü. Çok adımlı animasyon koreografisi için kısa … | gsap 3.15, javascript | ücretsiz | ✅ | 98 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-timeline@nexu-io` | alt | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing k… | gsap, react | ücretsiz | ✅ | 30 D | S 7KB | claude:farkli | nexu-io/open-design |
| `gsap-utils` | ⭐ tamamlayıcı | gsap.utils yardımcıları: clamp, mapRange, normalize, interpolate, random, snap, distribute, toArray, wrap, pipe. Scroll değerini eşleme, ızg… | gsap 3.15, javascript | ücretsiz | ✅ | 89 A | M 12KB | claude:ayni | greensock/gsap-skills |
| `gsap-utils@nexu-io` | alt | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks abou… | css, gsap, react | ücretsiz | ✅ | 28 D | M 14KB | claude:farkli | nexu-io/open-design |
| `lottie-animations` | ⭐ birincil | Lottie (lottie-web, lottie-react, dotLottie) ile After Effects JSON animasyonlarını web/React'e gömme: oynatma kontrolü, etkileşim, optimiza… | lottie-web 5.13, dotlottie-web, react | ücretsiz | ✅ | 65 B | M 64KB | - | freshtechbro/claudedesignskills |
| `lottie-bodymovin` | ⭐ alternatif | Disney'in 12 animasyon prensibini Lottie/After Effects iş akışıyla örnekler (AE ifadeleri, segment oynatma). Kısa ilke-örnek listesi. | lottie-web 5.13, after-effects | ücretsiz | ✅ | 71 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `motion-framer` | ⭐ birincil | Motion/Framer Motion ile React animasyonu: motion bileşenleri, variants, hover/tap/drag hareketleri, layout animasyonu, AnimatePresence, spr… | motion v14, react 19 | ücretsiz | ✅ | 73 B | M 159KB | - | freshtechbro/claudedesignskills |
| `motion-lab` | ⭐ | 为当前网页或组件查找、选型和改造动效。包含 160 个案例的 HTML/CSS/JS、参数与中英文索引，覆盖基础、文字、交互和高级动效。 | canvas, css, gsap, html, react | ücretsiz | ✅ | 30 D | S 158KB | - | nexu-io/open-design |
| `react-spring-physics` | ⭐ alternatif | React Spring ve Popmotion ile fizik tabanlı (yay) animasyon: spring hook'ları, jest entegrasyonu, düşük seviye animasyon yardımcıları. Doğal… | react-spring 10, react | ücretsiz | ✅ | 65 B | M 71KB | - | freshtechbro/claudedesignskills |
| `review-animations` | ⭐ | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; … | css | ücretsiz | ✅ | 28 D | M 19KB | - | nexu-io/open-design |
| `rive-interactive` | ⭐ alternatif | Rive durum makinesi tabanlı etkileşimli vektör animasyonu: girdi işleme, ViewModel veri bağlama, rive-react entegrasyonu. Betikler bileşen v… | rive, react | ½ kısmen | ✅ | 65 B | M 26KB | - | freshtechbro/claudedesignskills |
| `ui-animation` | ⭐ | Implement, review, and measure UI motion. Reconstruct easing, springs and gestures from a recording using bundled frame extraction, tracking… | api-anahtari, canvas, css, ffmpeg, motion | ücretsiz | ✅ | 28 D | M 181KB | - | nexu-io/open-design |

### 04-scroll-deneyimi

_Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri_ · not: `notlar/a-tasarim-onyuz/04-scroll-deneyimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `barba-js` | ⭐ birincil | Barba.js ile çok sayfalı sitelerde sayfalar arası geçiş animasyonu: hook'lar, router/prefetch/head eklentileri, GSAP entegrasyonu, geçiş kal… | barba 2, gsap 3.15 | ücretsiz | ✅ | 65 B | M 129KB | - | freshtechbro/claudedesignskills |
| `gsap-scrolltrigger` | ⭐ birincil | GSAP ScrollTrigger resmî rehberi: scroll'a bağlı animasyon, pinleme, scrub, tetikleyiciler, refresh ve temizlik. Parallax, pinli bölüm ve sc… | gsap 3.15, scrolltrigger, lenis 1.3 | ücretsiz | ✅ | 97 A | M 18KB | claude:ayni | greensock/gsap-skills |
| `gsap-scrolltrigger@freshtechbro` | alt alternatif | GSAP ve ScrollTrigger için kapsamlı (765 satır) genel rehber: tween, timeline, ScrollTrigger, kalıplar, ease referansı, başlangıç projesi ve… | gsap 3.15, scrolltrigger, three.js, react | ücretsiz | ✅ | 65 B | M 159KB | claude:farkli | freshtechbro/claudedesignskills |
| `gsap-scrolltrigger@nexu-io` | alt | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based a… | gsap, node, react | ücretsiz | ✅ | 28 D | M 20KB | claude:farkli | nexu-io/open-design |
| `locomotive-scroll` | ⭐ birincil | Locomotive Scroll ile yumuşak (smooth) kaydırma, parallax ve viewport algılama; GSAP ScrollTrigger entegrasyon notları ve başlangıç projesi. | locomotive-scroll 4, gsap 3.15 | ücretsiz | ✅ | 65 B | M 81KB | - | freshtechbro/claudedesignskills |
| `scroll-craft` | ⭐ birincil | Premium scroll-driven landing page üretir: brief/röportaj, sayfa grameri, duygu eğrisi, 'imza hamle', çok katmanlı (dimensional) hero, kendi… | html, css, javascript, node, chromium, kie.ai | ücretsiz | 🟡 | 80 A | M 380KB | - | nateherkai/scroll-craft |
| `scroll-reveal-libraries` | ⭐ alternatif | AOS (Animate On Scroll) ile basit scroll reveal animasyonları: data-aos öznitelikleri, yerleşik animasyonlar, özel animasyon, karşılaştırma … | aos, css | ücretsiz | ✅ | 65 B | M 94KB | - | freshtechbro/claudedesignskills |

### 05-3d-webgl

_Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader_ · not: `notlar/a-tasarim-onyuz/05-3d-webgl.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `aframe-webxr` | ⭐ birincil | A-Frame ile HTML tabanlı WebXR/VR/AR deneyimleri: entity-component yapısı, sahne, kameralar, ışık, animasyon, özel bileşenler, VR kontrolcü … | aframe 1.7, webxr, three.js | ücretsiz | ✅ | 63 C | L 176KB | - | freshtechbro/claudedesignskills |
| `babylonjs-engine` | ⭐ birincil | Babylon.js 3D motoru: engine/sahne başlatma, kameralar, ışık, mesh, materyaller, model yükleme, fizik (Havok), animasyon; sahne ve mesh üret… | babylonjs 7, webgl2, webgpu, havok | ücretsiz | ✅ | 63 C | L 153KB | - | freshtechbro/claudedesignskills |
| `blender-web-pipeline` | ⭐ birincil | Blender'dan web için glTF/GLB dışa aktarma: bpy betikleri, toplu işleme, LOD üretimi, model optimizasyonu, Three.js/Babylon.js için hazırlam… | blender 4, bpy, gltf 2.0, python | ücretsiz | ✅ | 65 B | M 27KB | - | freshtechbro/claudedesignskills |
| `lightweight-3d-effects` | ⭐ birincil | Zdog (sözde-3D vektör çizimler), Vanta.js (animasyonlu 3D arka planlar) ve Vanilla-Tilt (paralaks eğim) ile hafif dekoratif 3D efektler; kur… | zdog, vanta, vanilla-tilt, three.js | ücretsiz | ✅ | 64 C | M 179KB | - | freshtechbro/claudedesignskills |
| `playcanvas-engine` | ⭐ birincil | PlayCanvas motoru: Application, entity-component sistemi, güncelleme döngüsü, glTF, materyal, fizik, özel script ve girdi; hazır başlangıç p… | playcanvas 2, webgl2, webgpu | ücretsiz | ✅ | 65 B | M 183KB | - | freshtechbro/claudedesignskills |
| `react-three-fiber` | ⭐ alternatif | React Three Fiber ile deklaratif 3D sahne: Canvas, useFrame/useThree/useLoader, etkileşimli nesneler, glTF yükleme; sahne/bileşen üreten bet… | R3F v8, drei 9, three r172, react 18 | ücretsiz | ✅ | 65 B | M 105KB | - | freshtechbro/claudedesignskills |
| `shader-dev` | ⭐ | GLSL shader techniques for ray marching, fluid simulation, particle systems, and procedural generation. Useful for hero visuals and motion s… | webgl | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `spline-interactive` | ⭐ birincil | Spline: tarayıcı tabanlı görsel 3D tasarım aracı; sahneyi React/web'e @splinetool/react-spline ile gömme, olay yönetimi, nesne kontrolü ve d… | spline, react | ½ kısmen | ✅ | 65 B | M 54KB | - | freshtechbro/claudedesignskills |
| `substance-3d-texturing` | ⭐ tamamlayıcı | Adobe Substance 3D Painter ile PBR materyal/doku üretimi ve web/oyun motoru için dışa aktarma: export preset'leri, toplu dışa aktarma, çözün… | substance-3d-painter, python, pbr | 💲 ücretli | ✅ | 57 C | M 126KB | - | freshtechbro/claudedesignskills |
| `threejs` | ⭐ | Three.js skills for creating 3D elements and interactive experiences in the browser — scenes, materials, controls, and post-processing. | three.js, webgl | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `threejs-animation` | ⭐ birincil | Three.js'te keyframe, iskelet ve morph target animasyonu, AnimationMixer ile klip karıştırma, glTF animasyonlarını oynatma, prosedürel harek… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 83 A | M 21KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-animation@calesthio` | alt alternatif | Three.js keyframe, iskelet ve morph animasyonu ile AnimationMixer kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-asset-pipeline` | ⭐ birincil | gltf-transform ile glTF/GLB varlıklarını küçültme: inspect, validate, optimize, Draco/meshopt/quantization, KTX2, WebP/AVIF dokular, her çık… | three r186, gltf-transform 4, ktx2, draco, meshopt, gltfjsx | ücretsiz | ✅ | 91 A | M 18KB | - | CloudAI-X/threejs-skills |
| `threejs-fundamentals` | ⭐ birincil | Three.js sahne kurulumunun temelleri: sahne ve sis, kameralar, renderer ve tone mapping, animasyon döngüsü, nesne hiyerarşisi, dönüşümler, m… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 91 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-fundamentals@calesthio` | alt alternatif | Three.js sahne kurulumu, kameralar, renderer, Object3D, koordinat sistemi ve matematik sınıflarına kısa giriş (eski sürüm, WebGPU yok). | three.js, webgl | ücretsiz | ✅ | 70 B | M 11KB | claude:ayni | calesthio/OpenMontage |
| `threejs-geometry` | ⭐ birincil | Three.js geometri: yerleşik şekiller, 3D metin, BufferGeometry ve attribute'lar, birleştirme, instancing, batching, nokta bulutu ve çizgiler… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 81 A | L 25KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-geometry@calesthio` | alt alternatif | Three.js yerleşik geometriler, BufferGeometry, instancing ve Points kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-interaction` | ⭐ birincil | Three.js'te raycasting ile seçme, kamera kontrolleri (Orbit, Fly, PointerLock vb.), TransformControls, sürükleme, hover ve kutu seçimi; WebG… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 83 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-interaction@calesthio` | alt alternatif | Three.js raycaster, kontroller, dokunma desteği ve seçim kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 16KB | claude:ayni | calesthio/OpenMontage |
| `threejs-lighting` | ⭐ birincil | Three.js ışık türleri ve fiziksel birimler, gölge haritaları, HDR ortam aydınlatması (IBL), light probe, gölge ayarları ve ışık performansı. | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 91 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-lighting@calesthio` | alt alternatif | Three.js ışık türleri, gölge kurulumu ve ortam aydınlatması kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-loaders` | ⭐ birincil | Three.js varlık yükleme: Draco/meshopt/KTX2 destekli glTF, diğer model biçimleri, dokular, HDR/EXR ortamları, ilerleme, önbellek, klonlama v… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 91 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-loaders@calesthio` | alt alternatif | Three.js GLTF, doku ve HDR yükleme ile LoadingManager kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-materials` | ⭐ birincil | Three.js materyalleri: unlit, diffuse, PBR (Standard/Physical), toon, nokta/çizgi materyalleri, blending/stencil ve WebGPU node materyal/TSL… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-materials@calesthio` | alt alternatif | Three.js materyal türleri (Basic, Phong, Standard, Physical, Toon) kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-performance` | ⭐ birincil | Three.js performans ölçümü ve iyileştirme: render istatistikleri, bellek, draw call azaltma (birleştirme, instancing, batching, LOD), fill r… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 89 A | L 25KB | - | CloudAI-X/threejs-skills |
| `threejs-postprocessing` | ⭐ birincil | Three.js post-processing: composer pass zinciri, bloom, DOF, SSAO, outline, özel ekran efektleri ve WebGPU/TSL node pipeline. | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-postprocessing@calesthio` | alt alternatif | Three.js EffectComposer, bloom, DOF, SSAO, film grain kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-react-three-fiber` | ⭐ birincil | React Three Fiber ve drei ile Three.js sahnesi: renderer kurulumu, JSX sahne grafı, frame-loop, state ve yükleme hook'ları, pointer olayları… | R3F v9, drei 10, three r186, react 19 | ücretsiz | ✅ | 89 A | L 29KB | - | CloudAI-X/threejs-skills |
| `threejs-shaders` | ⭐ birincil | Özel GLSL vertex/fragment shader'lar: uniform, varying, shader chunk, yerleşik materyal genişletme, instanced attribute; WebGPU'da TSL node … | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-shaders@calesthio` | alt alternatif | Three.js GLSL ShaderMaterial, uniform, varying ve yaygın shader kalıpları kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-textures` | ⭐ birincil | Three.js dokuları: yükleme, renk uzayı, UV kanalları/dönüşümleri, canvas'tan HDR ve KTX2'ye doku türleri, render target, atlas, doku belleği… | three r186, webgl2, webgpu, tsl | ücretsiz | ✅ | 83 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-textures@calesthio` | alt alternatif | Three.js doku yükleme, ayarlar, UV, cubemap ve HDR kısa özeti (eski sürüm). | three.js, webgl | ücretsiz | ✅ | 70 B | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-webgl` | ⭐ alternatif | Three.js/WebGL/WebGPU geliştirmesine genel bakış: sahne grafı, temel bileşenler, hazır sahne kalıbı, mesh/ışık/instancing/glTF/gölge örnekle… | three.js, webgl, webgpu, gsap 3.15 | ücretsiz | ✅ | 57 C | M 62KB | - | freshtechbro/claudedesignskills |
| `web3d-integration-patterns` | ⭐ birincil | Three.js, GSAP ScrollTrigger, React Three Fiber, Motion ve React Spring'i birleştirme desenleri: katmanlı ayrım, birleşik React bileşeni, hi… | three.js, R3F v8, gsap 3.15, motion v14, react-spring 10, zustand | ücretsiz | ✅ | 65 B | M 21KB | - | freshtechbro/claudedesignskills |

### 06-oyun-2d-grafik

_Oyun geliştirme, PixiJS, 2D grafik_ · not: `notlar/a-tasarim-onyuz/06-oyun-2d-grafik.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `2d-games` | ⭐ alternatif | 2D oyun ilkeleri: sprite atlas ve animasyon, tilemap katmanları, 2D fizik şekilleri, kamera tipleri ve ekran sarsıntısı, platformer (coyote … | 2d, sprite, tilemap | ücretsiz | ✅ | 77 B | S 2KB | - | vudovn/ag-kit |
| `3d-games` | ⭐ alternatif | 3D oyun ilkeleri: render hattı aşamaları, culling/LOD/batching, shader türleri ve ne zaman özel shader yazılır, 3D çarpışma şekilleri, kamer… | 3d, shader, lod | ücretsiz | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `game-art` | ⭐ alternatif | Oyun sanatı ilkeleri: sanat stili karar ağacı (pixel, vektör, el boyaması, PBR, low-poly, cel-shaded) ve karşılaştırma matrisi, 2D/3D varlık… | pixel-art, blender, aseprite | ücretsiz | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `game-audio` | ⭐ alternatif | Oyun sesi ilkeleri: ses kategorileri ve öncelik hiyerarşisi, SFX katmanlama, müzik durum sistemi ve geçiş teknikleri, uyarlanabilir (vertica… | web-audio, fmod, wwise | ücretsiz | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `game-design` | ⭐ alternatif | Oyun tasarımı ilkeleri: 30 saniyelik çekirdek döngü, GDD bölümleri, oyuncu motivasyon tipleri ve ödül takvimleri, zorluk dengeleme (flow), i… | gdd, game-design | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `game-development` | ⭐ birincil | Oyun geliştirme orkestratörü: oyun döngüsü (sabit zaman adımı), desen seçim matrisi (state machine, pooling, ECS), girdi soyutlama, 60 FPS b… | game-design, unity, godot, unreal, phaser | ücretsiz | ✅ | 77 B | S 35KB | - | vudovn/ag-kit |
| `hatch-pet` | ⭐ | Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, generated images,… | api-anahtari, canvas, css, html, python | ½ kısmen | ✅ | 28 D | M 160KB | - | nexu-io/open-design |
| `mobile-games` | ⭐ alternatif | Mobil oyun ilkeleri: dokunmatik girdi (44pt hedef), pil/ısıl yönetim, performans hedefleri, App Store / Google Play gereklilikleri ve para k… | ios, android, touch | ücretsiz | ✅ | 77 B | S 2KB | - | vudovn/ag-kit |
| `multiplayer` | ⭐ alternatif | Çok oyunculu ilkeleri: mimari seçimi (dedicated, P2P, host), durum/girdi senkronizasyonu, tahmin-enterpolasyon-uzlaştırma ve lag compensatio… | networking, websocket | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `pc-games` | ⭐ alternatif | PC/konsol oyun ilkeleri: motor seçimi (Unity 6, Godot 4, Unreal 5) karar ağacı ve karşılaştırması, Steam özellikleri, konsol sertifikasyonu,… | unity, godot, unreal, steam | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `pixijs-2d` | ⭐ birincil | PixiJS v8 ile 2D WebGL/WebGPU render rehberi: Application, sprite/texture, Graphics API, ParticleContainer ile on binlerce parçacık, filtrel… | pixi.js, webgl, webgpu, javascript | ücretsiz | ✅ | 73 B | M 253KB | - | freshtechbro/claudedesignskills |
| `vr-ar` | ⭐ alternatif | VR/AR ilkeleri: platformlar (Quest, PCVR, WebXR, ARKit/ARCore), hareket hastalığı önleme ve konfor ayarları, kare hızı hedefleri, kontrolcü/… | webxr, quest, arkit | ücretsiz | ✅ | 69 B | S 2KB | - | vudovn/ag-kit |
| `web-games` | ⭐ alternatif | Tarayıcı oyunu ilkeleri: çatı seçimi (Phaser, PixiJS, Three.js, Babylon.js), WebGPU benimseme durumu, tarayıcı kısıtları ve optimizasyon sır… | phaser, pixi.js, three.js, webgpu, pwa | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |

### 07-gorsel-sanat-sunum

_Poster/canvas tasarımı, generative art, slayt, GIF_ · not: `notlar/a-tasarim-onyuz/07-gorsel-sanat-sunum.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `algorithmic-art` | ⭐ birincil | Önce bir 'algoritmik felsefe' (manifesto .md) yazdırıp ardından bunu seed'li rastgelelik ve parametre paneliyle p5.js üretken sanatına (akış… | p5.js, canvas, html, javascript | ücretsiz | ✅ | 76 B | M 58KB | - | anthropics/skills |
| `algorithmic-art@nexu-io` | alt | Create generative art using p5.js with seeded randomness so every render is reproducible. Useful for procedural posters, motion-style stills… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `artifacts-builder` | ⭐ alternatif | React 18 + TypeScript + Vite + Tailwind + shadcn/ui ile karmaşık claude.ai HTML artifact'ı kurar (init-artifact.sh) ve Parcel + html-inline … | react, typescript, vite, tailwind, shadcn-ui, parcel | ücretsiz | ✅ | 69 B | S 45KB | - | ComposioHQ/awesome-claude-skills |
| `artifacts-builder@nexu-io` | alt | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | css, html, react, tailwind | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `canvas-design` | ⭐ birincil | Bir 'tasarım felsefesi' (hareket adı + 4-6 paragraf manifesto) yazdırıp ardından bunu %90 görsel / %10 metin olan özgün PNG veya PDF posteri… | canvas, python, png, pdf | ücretsiz | ✅ | 84 A | M 5424KB | - | anthropics/skills |
| `canvas-design@composiohq` | alt alternatif | Anthropic canvas-design'ın ComposioHQ kopyası; SKILL.md ve font klasörü birebir aynıdır, yalnızca LICENSE.txt farklı (şablon Apache metni, t… | canvas, png, pdf | ücretsiz | ✅ | 68 B | M 5424KB | - | ComposioHQ/awesome-claude-skills |
| `canvas-design@nexu-io` | alt | Create beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, illustrations, and static… | canvas | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `card-twitter` | ⭐ | Twitter quote or data card designed to pair with a post. | html | ücretsiz | ✅ | 30 D | S 5KB | - | nexu-io/open-design |
| `card-xiaohongshu` | ⭐ | Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel. | html | ücretsiz | ✅ | 30 D | S 9KB | - | nexu-io/open-design |
| `d3-viz` | ⭐ birincil | d3.js ile özel, etkileşimli veri görselleştirmeleri (ağ/grafik, hiyerarşi, coğrafi harita, geçişli grafikler) kurmayı anlatır; React ve vani… | d3, svg, react, javascript | ücretsiz | ✅ | 86 A | M 80KB | claude:ayni | calesthio/OpenMontage |
| `deck-guizang-editorial` | ⭐ | Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune). | css, html | ücretsiz | ✅ | 30 D | S 10KB | - | nexu-io/open-design |
| `deck-open-slide-canvas` | ⭐ | Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template. | canvas, html, react, tailwind | ücretsiz | ✅ | 30 D | S 6KB | - | nexu-io/open-design |
| `deck-swiss-international` | ⭐ | 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange). | css, html | ücretsiz | ✅ | 30 D | S 12KB | - | nexu-io/open-design |
| `digits-fintech-swiss-template` | ⭐ | Swiss-grid fintech deck template in black / warm paper / neon-lime contrast. Use when users ask for premium data-story slides with strict mo… | css, html | ücretsiz | ✅ | 30 D | S 20KB | - | nexu-io/open-design |
| `editorial-burgundy-principles-template` | ⭐ | Editorial studio deck template in burgundy / blush / muted-gold palette. Use when users ask for premium manifesto or culture slides with pil… | html | ücretsiz | ✅ | 30 D | S 21KB | - | nexu-io/open-design |
| `field-notes-editorial-template` | ⭐ | Editorial "Field Notes" report template with soft paper background, serif hero typography, rounded pastel insight cards, and a retention cha… | css, html | ücretsiz | ✅ | 30 D | S 23KB | - | nexu-io/open-design |
| `frontend-slides` | ⭐ | Generate animation-rich HTML presentations with visual style previews. Useful for online keynotes, embedded talks, and interactive briefs. | html | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `hand-drawn-diagrams` | ⭐ | Generate hand-drawn Excalidraw diagrams from a prompt — animated SVG, hosted edit link, and PNG export. Works with Claude Code, Codex, Gemin… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `html-ppt-retro-quarterly-review` | ⭐ | Retro Quarterly Review presentation template in a bold blue + orange editorial language. Use when users ask for a high-impact quarterly revi… | api-anahtari, css, html | ücretsiz | ✅ | 30 D | S 29KB | - | nexu-io/open-design |
| `image-enhancer` | ⭐ birincil | Ekran görüntüsü ve görsellerin çözünürlüğünü, keskinliğini ve sıkıştırma artefaktlarını iyileştirmeyi anlatan, betiği olmayan yalnızca yöner… | imagemagick | ücretsiz | ✅ | 69 B | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `image-enhancer@nexu-io` | alt | Improve image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `mockup-device-3d` | ⭐ | Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable composition. | canvas, css, html, tailwind | ücretsiz | ✅ | 30 D | S 14KB | - | nexu-io/open-design |
| `playground` | ⭐ | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, se… | css, git, html | ücretsiz | ✅ | 30 D | S 29KB | - | anthropics/claude-plugins-official |
| `poster-hero` | ⭐ | Vertical poster or Moments-style share image with strong visual impact. | html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `ppt-keynote` | ⭐ | Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation. | html | ücretsiz | ✅ | 30 D | S 10KB | - | nexu-io/open-design |
| `pptx-generator` | ⭐ | Create and edit PowerPoint presentations from scratch with PptxGenJS — MiniMax's production-tested deck pipeline. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `pptx-html-fidelity-audit` | ⭐ | Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missing italic/em,… | canvas, html, python | ücretsiz | ✅ | 28 D | M 57KB | - | nexu-io/open-design |
| `slack-gif-creator` | ⭐ birincil | Slack için animasyonlu GIF üretimi: PIL ile kare çizimi, GIFBuilder, easing fonksiyonları, kare birleştirici ve Slack boyut/FPS/renk sınırla… | python, pillow, imageio, numpy, gif | ücretsiz | ✅ | 77 B | S 43KB | - | anthropics/skills |
| `slack-gif-creator@composiohq` | alt alternatif | Aynı skill'in ComposioHQ'daki daha eski/geniş sürümü: SKILL.md 16,7 KB, ek color_palettes.py, typography.py, visual_effects.py ve templates/… | python, pillow, imageio, numpy, gif | ücretsiz | ✅ | 76 B | M 208KB | - | ComposioHQ/awesome-claude-skills |
| `slack-gif-creator@nexu-io` | alt | Create animated GIFs optimized for Slack with validators for size constraints and composable animation primitives. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `slides` | ⭐ birincil | Chart.js, tasarım token'ları, yerleşim kalıpları ve metin yazım formülleri ile stratejik HTML sunum (pitch deck, pazarlama slaytı) üretir; `… | html, chart.js, css | ücretsiz | ✅ | 81 A | S 19KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `slides@nexu-io` | alt | Create and edit .pptx presentation decks with PptxGenJS. Useful for sales decks, kickoff briefs, and design-system showcases. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `swiss-creative-mode-template` | ⭐ | Swiss-inspired creative-mode presentation template skill with bold editorial typography, high-contrast geometric cards, interactive slide na… | css, html | ücretsiz | ✅ | 30 D | S 20KB | - | nexu-io/open-design |
| `web-artifacts-builder` | ⭐ birincil | React + TypeScript + Vite + Tailwind + shadcn/ui ile çok bileşenli claude.ai HTML artifact'ı kurar ve Parcel/html-inline ile tek dosyalık bu… | react, typescript, vite, tailwind, shadcn-ui, parcel | ücretsiz | ✅ | 85 A | S 45KB | - | anthropics/skills |
| `web-artifacts-builder@nexu-io` | alt | Build complex claude.ai HTML artifacts with React and Tailwind. Anthropic's reference workflow for shipping rich, embeddable artifacts. | html, react, tailwind | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |

### 08-onyuz-test-kalite

_Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı_ · not: `notlar/a-tasarim-onyuz/08-onyuz-test-kalite.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `agent-browser` | ⭐ | Browser automation CLI for AI agents. Use when the user needs to inspect, test, or automate browser behavior: navigating pages, filling form… | api-anahtari, css, html, node | ücretsiz | ✅ | 28 D | M 8KB | - | nexu-io/open-design |
| `browser-testing-with-devtools` | ⭐ birincil | Chrome DevTools MCP ile ajana canlı tarayıcı gözü kazandırır: ekran görüntüsü, DOM, konsol, ağ istekleri, performans izi (LCP/CLS/INP), hesa… | chrome-devtools-mcp, chrome, javascript | ücretsiz | ✅ | 87 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `design-review` | ⭐ | Designer Who Codes: visual audit then fixes with atomic commits and before/after screenshots. Useful for tightening shipped UI before launch… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `export-download-debugging` | ⭐ | Diagnose and fix browser, preview, or Electron export/download failures, especially image export issues involving Save As, Blob/Data URLs, t… |  | ücretsiz | ✅ | 30 D | S 3KB | - | nexu-io/open-design |
| `full-page-screenshot` | ⭐ | Capture full-page screenshots of web pages via Chrome DevTools Protocol with zero dependencies. Useful for portfolios, case studies, and aud… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `impeccable-design-polish` | ⭐ | Follow-up design polish skill inspired by Impeccable. Use after a web or HTML artifact exists to audit, critique, polish, animate, harden, a… | css, gsap, html | ücretsiz | ✅ | 30 D | S 3KB | - | nexu-io/open-design |
| `plan-design-review` | ⭐ | Senior Designer review: rates each design dimension 0-10, explains what a 10 looks like, and flags AI Slop signals. Useful as a gate before … |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `playwright-component-testing` | ⭐ birincil | Playwright ile React/Vue bileşenlerini 'hikâye galerisi' sayfası üzerinden, dahili `mount` fixture'ı ve düz Playwright testleriyle izole tes… | playwright, react, vue, vite, typescript | ücretsiz | ✅ | 91 A | M 38KB | - | microsoft/playwright |
| `playwright-trace` | ⭐ tamamlayıcı | Playwright trace (.zip) dosyalarını komut satırından inceler: eylem listesi, ağ istekleri, konsol, hatalar, DOM/erişilebilirlik anlık görünt… | playwright | ücretsiz | ✅ | 92 A | S 5KB | - | microsoft/playwright |
| `react-doctor` | ⭐ birincil | React kod tabanını güvenlik, performans, doğruluk, erişilebilirlik ve mimari açısından tarayıp 0-100 sağlık puanı veren `react-doctor` CLI'ı… | react, next.js, eslint | ücretsiz | ✅ | 79 B | S 3KB | - | darkroomengineering/satus |
| `screenshot` | ⭐ | Capture desktop, app windows, or pixel regions across OS platforms. Useful for marketing screenshots, design reviews, and bug reports. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `screenshots-marketing` | ⭐ | Generate marketing screenshots with Playwright. Useful for landing-page hero shots, App Store screenshots, and changelog visuals. | playwright | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `webapp-testing` | ⭐ birincil | Yerel web uygulamalarını Python Playwright betikleriyle test etme araç seti: statik/dinamik karar ağacı, `with_server.py` ile bir veya birde… | playwright, python | ücretsiz | ✅ | 85 A | S 22KB | - | anthropics/skills |
| `webapp-testing@composiohq` | alt alternatif | anthropics/skills webapp-testing'in kopyası: Python Playwright ile yerel web uygulaması testi, with_server.py ve örnek betikler. | playwright, python | ücretsiz | ✅ | 85 A | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `webapp-testing@vudovn` | alt alternatif | Web testi ilkeleri (derin denetim, test piramidi, E2E, Playwright kavramları, görsel test, API test, CI) ve hafif `playwright_runner.py` bet… | playwright, python | ücretsiz | ✅ | 77 B | S 10KB | - | vudovn/ag-kit |

## Yazılım Geliştirme

### 01-planlama-metodoloji

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_ · not: `notlar/b-yazilim-gelistirme/01-planlama-metodoloji.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `app-builder` | ⭐ birincil | ag-kit'in uygulama kurma orkestratörü: doğal dil isteğinden proje tipini tespit eder, 2026 varsayılan teknoloji yığınını (Next.js 16, Tailwi… | next.js, react, node, python, vue, flutter, react-native | ücretsiz | ✅ | 77 B | S 63KB | - | vudovn/ag-kit |
| `brainstorming` | ⭐ birincil | superpowers'ın tasarım öncesi skili: uygulamaya geçmeden önce sırayla yaklaşımları ayrı bir mesajda sunup birini seçtirmek, kısa ya da tam t… | node, html | ücretsiz | ✅ | 95 A | M 76KB | - | obra/superpowers |
| `brainstorming@nexu-io` | alt | Transform rough ideas into fully-formed designs through structured questioning and alternative exploration. Useful early in concept work. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `brainstorming@vudovn` | alt alternatif | ag-kit'in Sokratik soru protokolü: belirsiz isteklerde kodlamadan önce en az 3 soru (amaç, kullanıcı, kapsam) sorar, soruları seçenek/artı-e… | dil-bagimsiz | ücretsiz | ✅ | 77 B | S 17KB | - | vudovn/ag-kit |
| `constraint-driven-development` | ⭐ birincil | Projenin kalite çıtasını CONSTRAINTS.md'de yazılı sözleşmeye çevirir: kullanıcıya hangi boyutların önemli olduğunu sorar, sayı yoksa makul v… | git, node, python | ücretsiz | ✅ | 87 A | M 31KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `doubt-driven-development` | ⭐ birincil | Önemsiz olmayan her kararı (iddia → en küçük incelenebilir birim → taze bağlamlı karşıt inceleme → uzlaştırma → dur) döngüsünden geçirir; ge… | api-anahtari | ücretsiz | ✅ | 87 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `executing-plans` | ⭐ birincil | Yazılmış bir planı alt-agent kullanmadan, aynı oturumda görev görev uygular: her görev için brief ve kayıt defteri (ledger) tutar, TDD ile i… | git | ücretsiz | ✅ | 87 A | M 20KB | - | obra/superpowers |
| `idea-refine` | ⭐ alternatif | Ham fikirleri ıraksak (genişlet) ve yakınsak (değerlendir, daralt) düşünme aşamalarıyla keskin bir konsepte çevirir; sonuçta problem tanımı,… | dil-bagimsiz | ücretsiz | 🟡 | 84 A | M 40KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `incremental-implementation` | ⭐ tamamlayıcı | Değişiklikleri ince, doğrulanabilir dilimlerle teslim ettirir: dikey/sözleşme-önce/risk-önce dilimleme, 'önce sadelik' ve kapsam disiplini, … | git | ücretsiz | ✅ | 87 A | M 9KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `interview-me` | ⭐ tamamlayıcı | Kullanıcının gerçekte ne istediğini (yapması gerektiğini düşündüğü şeyi değil) bulmak için tek soruluk turlarla ~%95 güvene kadar görüşme ya… | react | ücretsiz | ✅ | 87 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `karpathy-guidelines` | ⭐ | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make… |  | ücretsiz | ✅ | 30 D | S 2KB | - | multica-ai/andrej-karpathy-skills |
| `math-olympiad` | ⭐ | Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. A… | python | ücretsiz | ✅ | 28 D | M 62KB | - | anthropics/claude-plugins-official |
| `plan-writing` | ⭐ alternatif | ag-kit'in kısa plan yazma rehberi (obra/superpowers'tan uyarlanmış): 5-10 görevlik, her görevin doğrulaması belli, bir sayfayı geçmeyen plan… | node, python, react, tailwind, typescript | ücretsiz | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `planning-and-task-breakdown` | ⭐ alternatif | Spec'i bağımlılık grafiği çıkarıp dikey dilimlere bölerek sıralı, boyutlandırılmış görevlere çevirir; her görev için kabul ölçütü ve doğrula… | typescript | ücretsiz | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `siege` | ⭐ | Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, independent workers answer them, a… | api-anahtari, python | ücretsiz | 🟡 | 20 D | L 104KB | - | anthropics/claude-plugins-official |
| `solo` | ⭐ | Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in a notes fil… | api-anahtari | ücretsiz | 🟡 | 25 D | S 6KB | - | anthropics/claude-plugins-official |
| `source-driven-development` | ⭐ birincil | Her uygulama kararını resmî dokümantasyona dayandırır: yığını ve sürümleri tespit eder, resmî belgeyi çeker (çekilen içeriği talimat değil v… | api-anahtari, css, html, next.js, node | ücretsiz | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `spec-driven-development` | ⭐ birincil | Kodlamadan önce spec yazdırır: kapsam kontrolü (gerekirse yetenek haritasına bölme), amaç/yığın/komutlar/yapı/test stratejisi/sınırlar/başar… | node, react | ücretsiz | ✅ | 87 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `templates` | alt alternatif | 13 proje iskelet şablonunun (Next.js fullstack/SaaS/static, Nuxt, Express, FastAPI, Expo, Flutter, Electron, Chrome MV3, CLI, Turborepo, Ast… | next.js, react, node, python, vue, flutter, react-native | ücretsiz | ✅ | 69 B | S 43KB | - | vudovn/ag-kit |
| `writing-plans` | ⭐ birincil | Spec'ten, kod tabanını hiç görmemiş bir mühendisin uygulayabileceği ayrıntılı uygulama planı yazdırır: dosya yapısı, her görev için dosyalar… | git | ücretsiz | ✅ | 95 A | M 10KB | - | obra/superpowers |

### 02-kod-kalitesi-review

_Code review, sadeleştirme, temiz kod_ · not: `notlar/b-yazilim-gelistirme/02-kod-kalitesi-review.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `clean-code` | ⭐ birincil | ag-kit'in her kod yazımında açık tutulan pragmatik kodlama standardı: SRP/DRY/KISS/YAGNI, isimlendirme kuralları, küçük fonksiyon ve sığ iç … | playwright, python, typescript | ücretsiz | ✅ | 77 B | S 7KB | - | vudovn/ag-kit |
| `code-review-and-quality` | ⭐ birincil | Beş eksenli kod incelemesi yaptırır: doğruluk, okunabilirlik/sadelik, mimari, güvenlik, performans. Önce testleri sonra uygulamayı okur, bul… | node, typescript | ücretsiz | ✅ | 95 A | M 20KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `code-review-checklist` | ⭐ alternatif | Kısa kod inceleme kontrol listesi: doğruluk, güvenlik (enjeksiyon, XSS, gizli anahtar, prompt injection), performans, kod kalitesi, test ve … | typescript | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `code-review-graph` | ⭐ birincil | code-review-graph MCP sunucusunun kullanım rehberi: Tree-sitter ile kod tabanını SQLite'ta AST grafiğine çevirip değişikliğin etki alanını (… | python, tree-sitter, sqlite, mcp | ücretsiz | ✅ | 76 B | M 11KB | - | vudovn/ag-kit |
| `code-simplification` | ⭐ birincil | Davranışı birebir koruyarak kodu açıklık için sadeleştirir: Chesterton'ın çiti (önce neden var olduğunu anla), proje geleneklerine uyma, zek… | typescript, javascript, python, react | ücretsiz | ✅ | 95 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `lint-and-validate` | ⭐ birincil | Her kod değişikliğinden sonra ekosisteme göre lint, tip denetimi ve güvenlik taramasını çalıştırır (Node/TS: eslint, tsc --noEmit, npm audit… | node, typescript, python | ücretsiz | ✅ | 77 B | S 16KB | - | vudovn/ag-kit |
| `pragmatic-review` | ⭐ alternatif | YAGNI ve KISS odaklı etkileşimli kod incelemesi: git durumundan kapsamı seçtirir (commit edilmemiş, dal, dosya, son N commit), aşırı mühendi… | git | ücretsiz | ✅ | 74 B | M 11KB | - | heyitsnoah/claudesidian |
| `receiving-code-review` | ⭐ tamamlayıcı | Gelen kod inceleme geri bildirimine teknik titizlikle yaklaşmayı öğretir: oku, kendi sözlerinle yeniden ifade et, kod tabanında doğrula, değ… | dil-bagimsiz | ücretsiz | ✅ | 88 A | S 6KB | - | obra/superpowers |
| `requesting-code-review` | ⭐ birincil | İş bitince veya birleştirmeden önce, oturum geçmişini değil özenle hazırlanmış bağlamı (açıklama, plan, BASE/HEAD SHA) vererek bir inceleyic… | git | ücretsiz | ✅ | 96 A | S 9KB | - | obra/superpowers |
| `simplify-code` | ⭐ alternatif | Aşırı mühendislik içeren kodu sadeleştirme kontrol listesi: gereksiz soyutlamalar, ölü kod, derin iç içelik, çok parametreli fonksiyonlar ve… | typescript, javascript | ücretsiz | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `simplify-codebase` | ⭐ tamamlayıcı | Kod tabanından kazara karmaşıklığı kanıta dayalı olarak ayıklar: Survey (salt okuma, sıralı bulgular) ve Change (yetkili silme/birleştirme) … | dil-bagimsiz, git | ücretsiz | ✅ | 96 A | S 27KB | - | tt-a1i/archify |

### 03-test-hata-ayiklama

_TDD, hata ayıklama, doğrulama_ · not: `notlar/b-yazilim-gelistirme/03-test-hata-ayiklama.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `debugging-and-error-recovery` | ⭐ alternatif | Kök neden odaklı hata ayıklama: 'hattı durdur' kuralı, yeniden üret → yerelleştir → küçült → kök nedeni düzelt → tekrarı önle → uçtan uca do… | git, node, typescript | ücretsiz | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `systematic-debugging` | ⭐ birincil | superpowers'ın hata ayıklama skilli: 'kök neden bulunmadan düzeltme yok' demir yasasıyla dört faz (kök neden araştırması, desen analizi, hip… | git | ücretsiz | ✅ | 95 A | M 40KB | - | obra/superpowers |
| `systematic-debugging@heyitsnoah` | alt alternatif | obra/superpowers systematic-debugging'in claudesidian'daki kopyası: aynı dört faz ve demir yasa; kök neden izleme, stack trace ekleme, kirle… | git, typescript | ücretsiz | ✅ | 74 B | M 13KB | - | heyitsnoah/claudesidian |
| `systematic-debugging@vudovn` | alt alternatif | ag-kit'in kısaltılmış hata ayıklama şablonu (obra/superpowers'tan uyarlanmış): yeniden üret, izole et, anla (5 Neden), düzelt ve doğrula faz… | git | ücretsiz | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `tdd-workflow` | ⭐ alternatif | ag-kit'in TDD ilke özeti: RED-GREEN-REFACTOR döngüsü, TDD'nin üç yasası, her faz için kurallar, AAA, TDD'nin ne zaman değerli olduğu tablosu… | dil-bagimsiz | ücretsiz | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `test-driven-development` | ⭐ birincil | Kırmızı-yeşil-refactor döngüsüyle geliştirme: önce projenin test yığınını keşfeder, başarısız test yazdırır, minimum kodla geçirtir, sonra t… | api-anahtari, css, html, node, playwright | ücretsiz | ✅ | 95 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `test-driven-development@obra` | alt alternatif | superpowers'ın TDD skilli: 'başarısız test olmadan üretim kodu yok' demir yasası; testten önce yazılan kodu silip baştan başlatır, kırmızıyı… | typescript | ücretsiz | ✅ | 95 A | M 17KB | claude:farkli,agents:farkli | obra/superpowers |
| `test-value` | ⭐ birincil | Testlerin değerini ve geri bildirim maliyetini denetler: yavaş, kararsız, yinelenen veya kırılgan testleri bulur; uygulama sırasında hangi t… | dil-bagimsiz, test-araclari | ücretsiz | ✅ | 95 A | M 19KB | - | tt-a1i/archify |
| `testing-patterns` | ⭐ alternatif | Test ilkeleri özeti: test piramidi, AAA, birim/entegrasyon/E2E seçimi, iyi birim testi özellikleri, mock ne zaman/hangi tür (stub, spy, mock… | python | ücretsiz | ✅ | 77 B | S 10KB | - | vudovn/ag-kit |
| `verification-before-completion` | ⭐ birincil | 'Taze doğrulama kanıtı olmadan tamamlandı iddiası yok' kuralı: bir durum iddia etmeden önce kanıtlayan komutu belirle, tam çalıştır, çıktıyı… | dil-bagimsiz | ücretsiz | ✅ | 96 A | S 4KB | - | obra/superpowers |
| `verify-changes` | ⭐ tamamlayıcı | Kodun çalıştığını incelemeyle değil çalıştırarak kanıtlatır: değişen dosyaları ve beklenen davranışı belirle, değişiklik tipine göre doğrula… | node, python | ücretsiz | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |

### 04-mimari-api-veritabani

_Mimari, API/arayüz tasarımı, veritabanı, backend_ · not: `notlar/b-yazilim-gelistirme/04-mimari-api-veritabani.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `api-and-interface-design` | ⭐ birincil | Kararlı API ve modül arayüzü tasarımı: Hyrum yasası ve tek sürüm kuralı, önce sözleşme, tutarlı hata semantiği, sınırda doğrulama, değiştirm… | typescript, rest, graphql | ücretsiz | ✅ | 95 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `api-patterns` | ⭐ tamamlayıcı | ag-kit'in API tasarım karar rehberi: REST/GraphQL/tRPC seçim ağacı, kaynak isimlendirme ve durum kodları, zarf/hata/sayfalama yanıt biçimler… | rest, graphql, trpc, typescript, python | ücretsiz | ✅ | 77 B | S 20KB | - | vudovn/ag-kit |
| `architecture` | ⭐ birincil | Mimari karar çerçevesi: bağlam keşfi soruları ve proje sınıflandırması, ödünleşim (trade-off) analizi ve ADR şablonları, desen seçimi karar … | dil-bagimsiz | ücretsiz | ✅ | 77 B | S 12KB | - | vudovn/ag-kit |
| `database-design` | ⭐ birincil | Veritabanı tasarım kararları: PostgreSQL/Neon/Turso/SQLite seçimi, Drizzle/Prisma/Kysely ORM seçimi, normalizasyon ve ilişkiler, indeks tipl… | postgresql, sqlite, prisma, drizzle, sql | ücretsiz | ✅ | 77 B | S 13KB | - | vudovn/ag-kit |
| `frontend-architecture` | ⭐ birincil | Ön yüz kodunu ölçeklenir biçimde düzenleme kuralları: UI / mantık (hook, composable) / veri (servis dosyaları) / tip / doğrulama (şema) katm… | react, next.js, vue, typescript, tailwind | ücretsiz | ✅ | 84 A | M 8KB | - | vudovn/ag-kit |
| `frontend-ui-engineering` | ⭐ birincil | Üretim kalitesinde, erişilebilir ve responsive arayüz kurma: bileşen dosya yapısı ve desenleri, durum yönetimi, tasarım sistemine bağlılık v… | react, typescript, css, tailwind | ücretsiz | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `nodejs-best-practices` | ⭐ birincil | Node.js arka yüz karar ilkeleri: Hono/Fastify/NestJS/Express seçim ağacı, yerel TypeScript ve modül sistemi kararları, katmanlı mimari, merk… | node, typescript, express, fastify, hono, nestjs | ücretsiz | ✅ | 76 B | M 8KB | - | vudovn/ag-kit |
| `python-patterns` | ⭐ birincil | Python geliştirme karar ilkeleri: FastAPI/Django/Flask seçim ağacı, async/sync kararı ve kütüphane seçimi, tip ipucu stratejisi ve Pydantic … | python, fastapi, django, flask, pydantic | ücretsiz | ✅ | 76 B | M 9KB | - | vudovn/ag-kit |

### 05-git-pr-surum

_Git, worktree, PR, sürüm/release, changelog_ · not: `notlar/b-yazilim-gelistirme/05-git-pr-surum.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `changelog-generator` | ⭐ tamamlayıcı | Git commit geçmişini tarayıp değişiklikleri kategorilere (yeni özellik, iyileştirme, düzeltme, kırıcı değişiklik, güvenlik) ayırır, iç commi… | git | ücretsiz | ✅ | 77 B | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `deprecation-and-migration` | ⭐ birincil | Eski sistem, API veya özellikleri kaldırma ve kullanıcıları yeni uygulamaya taşıma: 'kod bir yüktür' ve Hyrum yasası ilkeleri, kaldırma kara… | sql | ücretsiz | ✅ | 87 A | M 12KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `finishing-a-development-branch` | ⭐ birincil | Uygulama bittiğinde işi nasıl birleştireceğine karar verdirir: tam test paketini çalıştır (kırmızıysa dur), ortamı (normal repo / worktree /… | git, gh | ücretsiz | ✅ | 96 A | S 8KB | - | obra/superpowers |
| `git-workflow-and-versioning` | ⭐ birincil | Git iş akışı disiplini: trunk tabanlı geliştirme, erken ve sık commit, atomik commit ve açıklayıcı mesajlar, konuları ayırma, değişiklik boy… | git | ücretsiz | ✅ | 95 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `git-worktrees` | ⭐ alternatif | git worktree komut başvurusu: oluşturma (yeni/var olan dal), .worktrees/ dizin düzeni, kurulum sonrası adımlar (bağımlılık, env dosyası), co… | git | ücretsiz | ✅ | 67 B | S 4KB | - | heyitsnoah/claudesidian |
| `pr-feedback-quality-gate` | ⭐ | Safely track pull request feedback, resolve review comments or merge conflicts, validate fixes, and use a read-only cross-review before comm… | git | ücretsiz | ✅ | 30 D | S 2KB | - | nexu-io/open-design |
| `pull-request` | ⭐ alternatif | Tek komutla PR akışı: önkoşulları kontrol eder (git, gh), başlıktan dal adı üretir, değişiklikleri gösterip onay ister, conventional commit … | git, gh | ücretsiz | ✅ | 67 B | S 5KB | - | heyitsnoah/claudesidian |
| `release` | ⭐ birincil | Release akışını otomatikleştirir: son tag'den beri commit'leri analiz edip (BREAKING/feat/fix) sürüm artışını belirler, package.json sürümün… | git, gh, node | ücretsiz | ✅ | 67 B | S 6KB | - | heyitsnoah/claudesidian |
| `release-notes-one-pager` | ⭐ | Release notes one-page HTML with highlights, Added, Fixed, Breaking changes, Known issues, and Upgrade note. Writes explicit "None" style se… | css, html | ücretsiz | ✅ | 30 D | S 41KB | - | nexu-io/open-design |
| `using-git-worktrees` | ⭐ birincil | İşin yalıtılmış bir çalışma alanında yapılmasını sağlar: önce zaten bir worktree içinde olunup olunmadığını (alt modül korumasıyla) tespit e… | git | ücretsiz | ✅ | 96 A | S 7KB | - | obra/superpowers |

### 06-devops-guvenlik-performans

_CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans_ · not: `notlar/b-yazilim-gelistirme/06-devops-guvenlik-performans.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `ci-cd-and-automation` | ⭐ birincil | CI/CD hattı kurulumu: kalite kapısı sırası (lint → tip → birim → build → entegrasyon → E2E → güvenlik), GitHub Actions örnekleri (veritabanl… | github-actions, node, playwright | ücretsiz | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `claude-security` | ⭐ | Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or o… | api-anahtari, git, python | ücretsiz | 🟡 | 25 D | S 133KB | - | anthropics/claude-plugins-official |
| `deployment-procedures` | ⭐ tamamlayıcı | Üretim deploy ilkeleri: platform seçim ağacı (Vercel/Netlify, Railway/Render/Fly, VPS+PM2/Docker, Kubernetes, serverless), deploy öncesi dör… | docker, git | ücretsiz | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `observability-and-instrumentation` | ⭐ birincil | Kodu üretimde görünür ve teşhis edilebilir kılar: önce 'çalışıyor'un tanımı, her soru için doğru sinyal (log, metrik, iz), yapılandırılmış l… | opentelemetry, node, typescript | ücretsiz | ✅ | 87 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-optimization` | ⭐ birincil | Ölçüme dayalı performans iyileştirme: Core Web Vitals hedefleri, önce ölç → darboğazı bul → düzelt → doğrula (tut ya da geri al, geri alınan… | node, react, css | ücretsiz | ✅ | 87 A | M 26KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-profiling` | ⭐ tamamlayıcı | Performans profil çıkarma ilkeleri: Core Web Vitals hedefleri, taban → tespit → düzelt → doğrula süreci, sorun tipine göre araç seçimi (Ligh… | lighthouse, python, node | ücretsiz | ✅ | 77 B | S 13KB | - | vudovn/ag-kit |
| `red-team-tactics` | ⭐ birincil | MITRE ATT&CK tabanlı kırmızı takım ilkeleri: saldırı yaşam döngüsü fazları ve amaçları, pasif/aktif keşif, ilk erişim vektörleri, Windows/Li… | api-anahtari | ücretsiz | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `security-and-hardening` | ⭐ birincil | Kodu güvenlik açıklarına karşı sertleştirir: önce tehdit modeli, 'her zaman yap / önce sor / asla yapma' üç katmanlı sınır sistemi; enjeksiy… | node, html | ücretsiz | ✅ | 95 A | M 30KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `server-management` | ⭐ birincil | Sunucu işletim ilkeleri: süreç yöneticisi seçimi (PM2, systemd, Docker, Kubernetes), izleme metrikleri ve uyarı seviyeleri, izleme aracı seç… | pm2, systemd, docker, node | ücretsiz | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `shipping-and-launch` | ⭐ birincil | Üretime çıkış hazırlığı: kod kalitesi, güvenlik, performans, erişilebilirlik, altyapı ve dokümantasyon için ön yayın kontrol listesi; featur… | git, node, react, typescript | ücretsiz | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `vulnerability-scanner` | ⭐ tamamlayıcı | Güvenlik açığı analizi ilkeleri: varsayılan ihlal, sıfır güven, derinlemesine savunma; OWASP Top 10:2025 (yeni A03 tedarik zinciri), saldırı… | python | ücretsiz | ✅ | 77 B | S 35KB | - | vudovn/ag-kit |

### 07-framework-ozel

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_ · not: `notlar/b-yazilim-gelistirme/07-framework-ozel.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `bash-linux` | ⭐ birincil | macOS/Linux Bash kalıpları: komut zincirleme operatörleri, dosya işlemleri, süreç yönetimi (port tutan süreci bulma/öldürme), metin işleme (… | bash | ücretsiz | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `cardputer-buddy` | ⭐ | Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use… | python | ücretsiz | ✅ | 30 D | S 2KB | - | anthropics/claude-plugins-official |
| `m5-onboard` | ⭐ | End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash U… | git, python | ücretsiz | ✅ | 28 D | M 23KB | - | anthropics/claude-plugins-official |
| `next-bundle-optimizer` | ⭐ birincil | Next.js'te tarayıcının ilk yükleme işini denetler ve azaltır: varsayılan 'audit' kipinde next analyze ile anlık görüntü alıp dışa aktarır, m… | next.js, node | ücretsiz | ✅ | 91 A | M 15KB | - | vercel/next.js |
| `next-cache-components-adoption` | ⭐ birincil | Next.js uygulamasında Cache Components'i açar ve ortaya çıkan engelleyici route'ları çözerek build'i geçirir: App Router ve app dizinini doğ… | next.js, react, typescript, playwright | ücretsiz | ✅ | 97 A | L 40KB | - | vercel/next.js |
| `next-cache-components-optimizer` | ⭐ tamamlayıcı | Cache Components benimsenmiş Next.js 16.3+ uygulamasında bir route'un ilk yüklemede veya istemci geçişinde anında gösterdiği anlamlı UI'yi (… | next.js, playwright, typescript | ücretsiz | ✅ | 99 A | M 50KB | - | vercel/next.js |
| `next-dev-loop` | ⭐ birincil | Vercel'in Next.js düzenle-doğrula döngüsü: kod değişikliğinden sonra uygulamanın çalışma anında gerçekten çalıştığını iki görünümle kanıtlar… | next.js, react, node, turbopack | ücretsiz | ✅ | 99 A | M 9KB | - | vercel/next.js |
| `next-partial-prefetching-adoption` | ⭐ birincil | Next.js'te Partial Prefetching'i açar ve ortaya çıkan içgörüleri çözer: önce <Link prefetch={true}> gezinmelerini denetler, mevcut prefetch … | next.js, playwright, typescript | ücretsiz | ✅ | 97 A | L 35KB | - | vercel/next.js |
| `next-partial-prefetching-optimizer` | ⭐ tamamlayıcı | Partial Prefetching altında seçili istemci gezinmelerinin tıklamadan önce neyi içereceğini optimize eder: her kaynak link/hedef için prefetc… | next.js, playwright | ücretsiz | ✅ | 99 A | M 26KB | - | vercel/next.js |
| `nextjs-react-expert` | ⭐ alternatif | Vercel'in React/Next.js performans kurallarının ag-kit uyarlaması: 58 kural etki sırasına göre 8 dosyada, ek olarak Next.js 16 Cache Compone… | react, next.js, python | ücretsiz | ✅ | 76 B | M 111KB | - | vudovn/ag-kit |
| `playwright-cli` | ⭐ birincil | Microsoft'un playwright-cli aracıyla tarayıcı otomasyonu: aç/git, snapshot'taki ref'lerle tıklama/yazma/doldurma/sürükleme/yükleme, metin ar… | playwright, node | ücretsiz | ✅ | 90 A | M 68KB | - | microsoft/playwright |
| `powershell-windows` | ⭐ alternatif | Windows PowerShell tuzakları ve kalıpları: mantıksal operatörlerde cmdlet'i paranteze alma, betiklerde Unicode/emoji yasağı, null kontroller… | powershell, windows | ücretsiz | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `rust-pro` | ⭐ birincil | Modern Rust (2024 sürümü) uzman persona tanımı: async (Tokio), axum, sahiplik/ömür, tip sistemi ve trait'ler, performans ve sistem programla… | rust, tokio, axum | ücretsiz | ✅ | 69 B | S 8KB | - | vudovn/ag-kit |
| `vercel-composition-patterns` | ⭐ birincil | Vercel'in ölçeklenen React kompozisyon desenleri: boolean prop çoğalmasını compound component, state lifting ve iç yapıyı birleştirme ile ön… | react | ücretsiz | ✅ | 87 A | S 49KB | claude:ayni | calesthio/OpenMontage |
| `vercel-react-best-practices` | ⭐ birincil | Vercel Engineering'in React/Next.js performans kuralları: etkiye göre 8 kategoride 65 kural (şelaleleri kaldırma, bundle boyutu, sunucu tara… | react, next.js | ücretsiz | ✅ | 87 A | S 207KB | claude:ayni | calesthio/OpenMontage |

## Doküman ve İçerik

### 01-ofis-dokumanlari

_Word, Excel, PowerPoint, PDF üretme/düzenleme_ · not: `notlar/c-dokuman-icerik/01-ofis-dokumanlari.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `article-magazine` | ⭐ | Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay. | html | ücretsiz | ✅ | 30 D | S 11KB | - | nexu-io/open-design |
| `doc` | ⭐ | Read, create, and edit .docx documents with formatting and layout fidelity via OpenAI's document skill. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `doc-kami-parchment` | ⭐ | Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography. | canvas, css, html, tailwind | ücretsiz | ✅ | 30 D | S 10KB | - | nexu-io/open-design |
| `docx` | ⭐ birincil | Word (.docx/.dotx) belgelerini oluşturur, okur ve düzenler. Yeni belge için docx-js (npm), mevcut belge için unzip → XML düzenleme → zip akı… | node, python, docx-js, libreoffice | ücretsiz | ✅ | 93 A | S 1102KB | - | anthropics/skills |
| `docx@composiohq` | alt alternatif | Anthropic docx skill'inin ComposioHQ deposundaki eski sürümü. docx-js ile yeni belge, Python 'Document' kütüphanesi (ooxml) ile düzenleme ve… | node, python, docx-js, libreoffice | ücretsiz | ✅ | 76 B | M 1158KB | - | ComposioHQ/awesome-claude-skills |
| `docx@nexu-io` | alt | Create, edit, and analyze Word documents with tracked changes, comments, and formatting. Useful for design briefs, copy docs, and review-rea… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `minimax-docx` | ⭐ | Professional DOCX document creation and editing using OpenXML SDK. Useful for branded reports, polished proposals, and template-based author… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `minimax-pdf` | ⭐ | Generate, fill, and reformat PDFs with a token-based design system and 15 cover styles. Useful for branded PDFs, e-guides, and reports. | api-anahtari | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `pdf` | ⭐ birincil | PDF okuma, metin/tablo çıkarma, birleştirme, bölme, döndürme, filigran, form doldurma, şifreleme ve OCR işlerini Python (pypdf, pdfplumber, … | python | ücretsiz | ✅ | 84 A | M 57KB | - | anthropics/skills |
| `pdf@composiohq` | alt alternatif | Anthropic pdf skill'inin ComposioHQ'daki eski kopyası: pypdf/pdfplumber/reportlab ile PDF okuma, çıkarma, birleştirme/bölme ve form doldurma… | python | ücretsiz | ✅ | 77 B | S 63KB | - | ComposioHQ/awesome-claude-skills |
| `pdf@nexu-io` | alt | Extract text, create PDFs, and handle forms. Useful for press releases, branded one-pagers, and printable design deliverables. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `pptx` | ⭐ birincil | PowerPoint (.pptx/.potx) sunumlarını oluşturur, okur ve düzenler. Yeni deste için pptxgenjs, şablon/düzenleme için XML akışı kullanır; slayt… | node, python, pptxgenjs, libreoffice | ücretsiz | ✅ | 92 A | M 1112KB | - | anthropics/skills |
| `pptx@composiohq` | alt alternatif | Anthropic pptx skill'inin eski sürümü (ComposioHQ). HTML slaytları playwright ile html2pptx dönüştürerek sunum üretir; şablonlu üretimde sla… | node, python, pptxgenjs, playwright, html | ücretsiz | ✅ | 74 B | L 1201KB | - | ComposioHQ/awesome-claude-skills |
| `pptx@nexu-io` | alt | Read, generate, and adjust PowerPoint slides, layouts, and templates. Useful for executive decks, training material, and product reviews. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `resume-modern` | ⭐ | Modern minimal resume, single A4 page, ready for print or PDF export. | html | ücretsiz | ✅ | 30 D | S 11KB | - | nexu-io/open-design |
| `xlsx` | ⭐ birincil | Excel/CSV/TSV dosyalarını openpyxl ve pandas ile oluşturur, okur, düzenler ve temizler. Formül kullanımını zorunlu tutar, LibreOffice ile ye… | python, libreoffice | ücretsiz | ✅ | 92 A | M 1077KB | - | anthropics/skills |
| `xlsx@composiohq` | alt alternatif | Anthropic xlsx skill'inin eski kopyası (ComposioHQ): formül zorunluluğu, finansal model renk/sayı biçimi kuralları, pandas/openpyxl örnekler… | python, libreoffice | ücretsiz | ✅ | 76 B | M 18KB | - | ComposioHQ/awesome-claude-skills |

### 02-diyagram-dokumantasyon

_Diyagram, teknik dokümantasyon, ADR, ortak yazım_ · not: `notlar/c-dokuman-icerik/02-diyagram-dokumantasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `archify` | ⭐ birincil | Mimari, iş akışı, sequence, veri akışı, yaşam döngüsü, ERD, class, ağaç, zaman çizelgesi ve waterfall diyagramlarını doğrulanmış, temalı, an… | node, html, svg | ücretsiz | ✅ | 93 A | M 7616KB | - | tt-a1i/archify |
| `beautiful-mermaid` | ⭐ alternatif | Mermaid diyagramlarını Beautiful Mermaid kütüphanesiyle temalı SVG'ye, ardından tarayıcı ekran görüntüsüyle yüksek çözünürlüklü PNG'ye çevir… | typescript, bun, mermaid, svg | ücretsiz | ✅ | 87 A | S 19KB | claude:ayni | calesthio/OpenMontage |
| `d3-visualization` | ⭐ | Teaches the agent to produce D3 charts and interactive data visualizations. A comprehensive D3.js skill with examples across chart types and… | git | ücretsiz | ✅ | 30 D | S 2KB | - | nexu-io/open-design |
| `data-report` | ⭐ | Turns CSV, Excel, or JSON data into a polished visual report page. | canvas, html | ücretsiz | ✅ | 30 D | S 13KB | - | nexu-io/open-design |
| `doc-coauthoring` | ⭐ tamamlayıcı | Kullanıcıyla birlikte doküman (spec, öneri, karar dokümanı, PRD, RFC) yazmak için üç aşamalı bir süreç yürütür: bağlam toplama, bölüm bölüm … | markdown | ücretsiz | ✅ | 92 A | M 15KB | - | anthropics/skills |
| `documentation-and-adrs` | ⭐ birincil | Kararları ve 'neden'i belgelemeyi öğretir: projedeki mevcut ADR düzenine uyarak ADR yazma, satır içi yorum kuralları, bilinen tuzakları belg… | markdown, typescript | ücretsiz | ✅ | 95 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `documentation-templates` | ⭐ alternatif | README, endpoint bazlı API dokümanı, JSDoc/TSDoc yorumu, Keep-a-Changelog, kısa ADR ve llms.txt gibi AI dostu doküman için hazır şablonlar v… | markdown | ücretsiz | ✅ | 76 B | S 3KB | - | vudovn/ag-kit |
| `live-panel` | ⭐ | Build a terminal-style, always-running animated architecture diagram (a "live panel") from a JSON config and render it to an mp4. Use when t… | canvas, css, ffmpeg, html, python | ücretsiz | ✅ | 28 D | M 1704KB | - | ythx-101/live-panel-skill |

### 03-yazi-iletisim-icerik

_Yazı, iletişim, pazarlama/içerik, kariyer_ · not: `notlar/c-dokuman-icerik/03-yazi-iletisim-icerik.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `ad-creative` | ⭐ | Generate and iterate ad creative including headlines, descriptions, and primary text. Useful for paid social and search ad iteration. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `competitive-ads-extractor` | ⭐ alternatif | Rakiplerin Facebook Ad Library, LinkedIn gibi reklam kütüphanelerindeki reklamlarını toplayıp mesaj, vurgulanan problem, hedef kitle ve krea… | web-arama, tarayici-otomasyonu | ücretsiz | ✅ | 69 B | S 8KB | - | ComposioHQ/awesome-claude-skills |
| `competitive-ads-extractor@nexu-io` | alt | Extract and analyze competitors' ads from ad libraries to understand messaging and creative approaches that resonate. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `content-research-writer` | ⭐ birincil | Blog, makale, bülten gibi içerikleri kullanıcıyla birlikte yazar: taslak/ana hat oluşturma, araştırma ve kaynak gösterme, giriş (hook) iyile… | markdown, web-arama | ücretsiz | ✅ | 76 B | M 14KB | - | ComposioHQ/awesome-claude-skills |
| `copywriting` | ⭐ | Write and rewrite marketing copy for landing pages, homepages, and ads. Useful as a copy chief partner during launches. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `de-ai-ify` | ⭐ tamamlayıcı | Metindeki yapay zekâ kokan kalıpları (aşırı geçiş kelimeleri, klişeler, kaçamak ifadeler, kurumsal jargon, üçlü sıralamalar) temizleyip doğa… | markdown | ücretsiz | ✅ | 75 B | S 2KB | - | heyitsnoah/claudesidian |
| `developer-growth-analysis` | ⭐ alternatif | Son 24-48 saatlik Claude Code sohbet geçmişini (~/.claude/history.jsonl) okuyup kodlama kalıplarını, eksik alanları ve gelişim önerilerini ç… | claude-code, mcp, slack | ücretsiz | ✅ | 68 B | M 15KB | - | ComposioHQ/awesome-claude-skills |
| `domain-name-brainstormer` | ⭐ alternatif | Proje için yaratıcı alan adı fikirleri üretir ve .com/.io/.dev/.ai gibi uzantılarda müsaitlik kontrolü yapılmasını tarif eder; marka açısınd… | web-arama | ücretsiz | ✅ | 69 B | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `domain-name-brainstormer@nexu-io` | alt | Generate creative domain name ideas and check availability across multiple TLDs including .com, .io, .dev, and .ai. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `geo-fundamentals` | ⭐ tamamlayıcı | Generative Engine Optimization: içeriğin ChatGPT, Claude, Perplexity, Gemini gibi AI arama motorlarında kaynak gösterilmesi için ilkeler, al… | html, python | ücretsiz | ✅ | 77 B | S 14KB | - | vudovn/ag-kit |
| `i18n-localization` | ⭐ birincil | Uluslararasılaştırma ve yerelleştirme kalıpları: react-i18next, next-intl, gettext örnekleri, locale dosya yapısı, çoğul/tarih/sayı biçimler… | react, next.js, python | ücretsiz | ✅ | 77 B | S 12KB | - | vudovn/ag-kit |
| `internal-comms` | ⭐ birincil | Şirket içi iletişim metinleri yazar: 3P güncellemeleri (Progress/Plans/Problems), şirket bülteni, SSS cevapları, durum raporu, liderlik ve p… | markdown | ücretsiz | ✅ | 85 A | S 22KB | - | anthropics/skills |
| `internal-comms@composiohq` | alt alternatif | Anthropic internal-comms skill'inin ComposioHQ'daki birebir kopyası: 3P güncellemesi, bülten, SSS ve genel iç iletişim yönergeleri. | markdown | ücretsiz | ✅ | 77 B | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `lead-research-assistant` | ⭐ birincil | Ürünü/kod tabanını analiz edip ideal müşteri profiline uyan şirketleri bulmayı, uygunluk puanıyla sıralamayı ve kişiselleştirilmiş iletişim … | web-arama | ücretsiz | ✅ | 69 B | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `marketing-psychology` | ⭐ | Apply psychological principles and behavioral science to copy and design. Useful for tightening hooks, framing, and pricing presentation. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `meeting-insights-analyzer` | ⭐ birincil | Toplantı transkriptlerinden iletişim kalıplarını çıkarır: çatışmadan kaçınma, konuşma oranı, dolgu kelimeler, dinleme ve kolaylaştırma; zama… | markdown | ücretsiz | ✅ | 76 B | M 10KB | - | ComposioHQ/awesome-claude-skills |
| `paywall-upgrade-cro` | ⭐ | Design and optimize upgrade screens, paywalls, and upsell modals. Useful for SaaS conversion design and pricing-page experiments. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `raffle-winner-picker` | ⭐ alternatif | Liste, CSV/Excel ya da Google Sheets'ten çekiliş/yarışma kazananını rastgele seçer; çoklu kazanan, tekrar engelleme, ağırlıklı seçim ve yede… | python | ücretsiz | ✅ | 69 B | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `research-decision-room` | ⭐ | Turn messy user research notes, interviews, support tickets, surveys, and product context into an evidence-backed decision room: a single HT… | html | ücretsiz | ✅ | 30 D | S 38KB | - | nexu-io/open-design |
| `seo-fundamentals` | ⭐ birincil | SEO temelleri: E-E-A-T, Core Web Vitals hedefleri, teknik SEO (sitemap, robots, canonical), sayfa öğeleri, schema türleri, AI içerik kuralla… | html, python | ücretsiz | ✅ | 77 B | S 9KB | - | vudovn/ag-kit |
| `tailored-resume-generator` | ⭐ birincil | İş ilanını analiz edip anahtar gereksinimleri çıkarır ve adayın deneyimini buna göre yeniden düzenleyen, ATS uyumlu, ilana özel özgeçmiş üre… | markdown | ücretsiz | ✅ | 76 B | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `twitter-algorithm-optimizer` | ⭐ birincil | Twitter/X'in açık kaynak öneri algoritması bileşenlerine (Real-graph, SimClusters, TwHIN, Tweepcred) dayanarak tweet taslaklarını analiz edi… | markdown | ücretsiz | ✅ | 76 B | M 13KB | - | ComposioHQ/awesome-claude-skills |
| `writing-guidelines` | ⭐ | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs … |  | ücretsiz | ✅ | 30 D | S 17KB | - | nexu-io/open-design |

### 04-not-alma-bilgi-yonetimi

_Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni_ · not: `notlar/c-dokuman-icerik/04-not-alma-bilgi-yonetimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `add-frontmatter` | ⭐ tamamlayıcı | Obsidian notlarını (tek dosya ya da klasör) okuyup not türüne göre (toplantı, günlük, referans, proje) YAML frontmatter özellikleri ekler ve… | obsidian, markdown, yaml | ücretsiz | ✅ | 75 B | S 4KB | - | heyitsnoah/claudesidian |
| `daily-review` | ⭐ tamamlayıcı | Gün sonu değerlendirmesi: bugün değişen/oluşan notları bulur, ilerlemeyi, takılan işleri ve içgörüleri çıkarır, yarının ilk 3 önceliğini ve … | obsidian, markdown | ücretsiz | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `download-attachment` | ⭐ alternatif | Verilen URL'lerden dosyaları Obsidian kasasının 05_Attachments klasörüne indirir (yalnızca http/https, dosya adı temizleme, zaman aşımı), iç… | bash, obsidian | ücretsiz | ✅ | 67 B | S 3KB | - | heyitsnoah/claudesidian |
| `file-organizer` | ⭐ birincil | Bilgisayardaki klasörleri (İndirilenler, Belgeler, projeler) analiz eder; kopya dosyaları bulur, mantıklı klasör yapısı önerir ve kullanıcı … | bash | ücretsiz | ✅ | 76 B | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `inbox-processor` | ⭐ tamamlayıcı | Kasanın 00_Inbox klasöründeki notları PARA yöntemine göre (Projects/Areas/Resources/Archive/Sil) sınıflandırır; her not için hedef klasör, g… | obsidian, markdown | ücretsiz | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `init-bootstrap` | ⭐ birincil | Claudesidian kasası için etkileşimli kurulum sihirbazı: klasör adı, bağımlılık kurulumu (pnpm/npm), git durumu, mevcut kasa yapısı ve çalışm… | obsidian, node, git | ½ kısmen | ✅ | 64 C | L 30KB | - | heyitsnoah/claudesidian |
| `install-claudesidian-command` | ⭐ tamamlayıcı | Kabuğa (bash/zsh/fish) `claudesidian` adlı bir alias/fonksiyon ekler: kasa klasörüne geçip `claude --resume` ile oturumu sürdürür ya da yeni… | bash, claude-code | ücretsiz | 🟡 | 63 C | M 10KB | - | heyitsnoah/claudesidian |
| `invoice-organizer` | ⭐ tamamlayıcı | Fatura ve fişleri (PDF, taranmış görsel, e-posta eki) okuyup satıcı, tarih, tutar, fatura no gibi bilgileri çıkarır; `YYYY-AA-GG Satıcı - Fa… | python, pdf | ücretsiz | ✅ | 76 B | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `json-canvas` | ⭐ tamamlayıcı | Obsidian'ın kullandığı JSON Canvas 1.0 (.canvas) dosyalarını oluşturur ve düzenler: text/file/link/group düğümleri, kenarlar, renkler, yerle… | json, obsidian | ücretsiz | ✅ | 74 B | M 14KB | - | heyitsnoah/claudesidian |
| `obsidian-bases` | ⭐ tamamlayıcı | Obsidian Bases (.base) dosyalarını oluşturur ve düzenler: tam YAML şeması, global/görünüm filtreleri, formül sözdizimi ve fonksiyon başvurus… | obsidian, yaml | ücretsiz | ✅ | 74 B | M 16KB | - | heyitsnoah/claudesidian |
| `obsidian-markdown` | ⭐ birincil | Obsidian Flavored Markdown yazımı: wikilink, gömme (embed), callout, özellikler (properties), etiketler, blok referansları, LaTeX matematik … | obsidian, markdown | ücretsiz | ✅ | 73 B | M 11KB | - | heyitsnoah/claudesidian |
| `research-assistant` | ⭐ birincil | Bir konuyu kasadaki notlar üzerinden araştırır: ilgili notları bulup okur, temaları, çelişkileri ve boşlukları çıkarır, wikilink'li bir araş… | obsidian, markdown | ücretsiz | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `thinking-partner` | ⭐ birincil | Karmaşık bir problemi çözüme koşmadan sorularla birlikte düşünme modu: önce sorar, varsayımları yüzeye çıkarır, içgörüleri kaydeder, kasadak… | markdown | ücretsiz | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `upgrade` | ⭐ tamamlayıcı | claudesidian kurulumunu GitHub'daki son sürüme yükseltir: sürüm kontrolü, yedek, upstream çekme, dosya dosya anlamsal karşılaştırma ile kull… | git, bash, obsidian | ücretsiz | 🟡 | 63 C | M 11KB | - | heyitsnoah/claudesidian |
| `weekly-synthesis` | ⭐ birincil | Haftanın notlarını ve çalışmalarını tarayıp tekrar eden temaları, içgörüleri, proje ilerlemesini, ortaya çıkan soruları, enerji denetimini v… | obsidian, markdown | ücretsiz | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |

## AI ve Otomasyon

### 01-claude-api-mcp

_Claude API, MCP sunucusu, model geçişi_ · not: `notlar/d-ai-otomasyon/01-claude-api-mcp.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `academy-guide` | ⭐ birincil | Claude veya bir Claude ürününün nasıl kullanılacağına dair sorulara verilen cevabın sonuna, Claude Academy'den (academy.claude.com) yalnızca… | web-fetch | ücretsiz | ✅ | 84 A | S 19KB | - | anthropics/skills |
| `build-mcp-app` | ⭐ | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components … | css, html, node, python, typescript | ücretsiz | ✅ | 28 D | M 47KB | - | anthropics/claude-plugins-official |
| `build-mcp-server` | ⭐ | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude",… | api-anahtari, node, python, typescript | ücretsiz | ✅ | 28 D | M 49KB | - | anthropics/claude-plugins-official |
| `build-mcpb` | ⭐ | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distr… | node, python, typescript | ücretsiz | ✅ | 30 D | S 18KB | - | anthropics/claude-plugins-official |
| `claude-api` | ⭐ birincil | Claude API / Anthropic SDK için kapsamlı ve güncel başvuru: model kimlikleri ve fiyatlar, adaptive thinking, streaming, araç kullanımı, prom… | anthropic-sdk, python, typescript, go, java, csharp, php, ruby, curl | 💲 ücretli | 🟡 | 86 A | L 2031KB | - | anthropics/skills |
| `claude-opus-4-5-migration` | alt alternatif | Sonnet 4.0/4.5 ve Opus 4.1'den Opus 4.5'e tek seferlik geçiş: platforma göre (Anthropic, Bedrock, Vertex, Azure) model dizgelerini değiştiri… | anthropic-sdk | 💲 ücretli | ✅ | 69 B | S 12KB | - | anthropics/claude-code |
| `connect` | ⭐ birincil | Composio SDK (Python/TS) ile agent'ı Gmail, Slack, GitHub, Notion gibi 1000+ uygulamaya bağlar; e-posta gönderme, issue açma, mesaj atma gib… | composio, python, typescript, oauth | ½ kısmen | ✅ | 77 B | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `connect-apps` | ⭐ alternatif | Claude Code'a `/plugin install composio-toolrouter` ile Composio Tool Router eklentisini kurup 1000+ uygulamada (Gmail, Slack, GitHub, Notio… | composio, claude-code, mcp | ½ kısmen | 🟡 | 66 B | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `langsmith-fetch` | ⭐ birincil | LangChain/LangGraph agent'larını hata ayıklamak için langsmith-fetch CLI ile LangSmith'ten çalışma izlerini (trace) çeker; son etkinlik, bel… | langchain, langgraph, langsmith, python | ½ kısmen | ✅ | 76 B | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder` | ⭐ birincil | Yüksek kaliteli MCP sunucusu geliştirme rehberi: araştırma/planlama (araç adlandırma, bağlam yönetimi, hata mesajları), Python FastMCP veya … | mcp, python, typescript | ücretsiz | ✅ | 92 A | M 119KB | - | anthropics/skills |
| `mcp-builder@composiohq` | alt alternatif | Anthropic mcp-builder'ın ComposioHQ'daki eski sürümü: 'iş akışı odaklı araç tasarımı' ilkeleri, ayrıntılı uygulama planı, dil rehberleri ve … | mcp, python, typescript | ücretsiz | ✅ | 76 B | M 144KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder@vudovn` | alt tamamlayıcı | MCP sunucu ve istemci mühendisliği: kararlı 2026-07-28 spesifikasyonuna göre durumsuz istek modeli, taşıma ve kimlik doğrulama, araç girdi/ç… | mcp, json-schema | ücretsiz | ✅ | 84 A | M 10KB | - | vudovn/ag-kit |
| `mcp-integration` | ⭐ | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model… | api-anahtari, git, node, python | ücretsiz | 🟡 | 23 D | M 45KB | - | anthropics/claude-plugins-official |
| `mcp-integration@anthropics` | alt birincil | Claude Code eklentilerine MCP sunucusu paketleme rehberi: .mcp.json ya da plugin.json içinde mcpServers, stdio/SSE/HTTP/WebSocket sunucu tip… | mcp, claude-code, json | ücretsiz | 🔵 | 76 B | M 46KB | - | anthropics/claude-code |

### 02-agent-orkestrasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_ · not: `notlar/d-ai-otomasyon/02-agent-orkestrasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `batch-operations` | ⭐ birincil | Birçok dosyaya aynı değişikliği güvenle uygulama protokolü: deseni tanımla, önce grep ile etkilenen dosyaları önizle, toplu uygula, sonra do… | bash, git | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `behavioral-modes` | ⭐ alternatif | Görev türüne göre yedi çalışma modu tanımlar (brainstorm, implement, debug, review, teach, ship, orchestrate); her mod için davranış kuralla… | node, typescript | ücretsiz | ✅ | 69 B | S 6KB | - | vudovn/ag-kit |
| `claude-automation-recommender` | ⭐ | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation… | docker, git, next.js, node, playwright | ücretsiz | 🟡 | 23 D | M 42KB | - | anthropics/claude-plugins-official |
| `claude-md-improver` | ⭐ | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for al… | git, node | ücretsiz | ✅ | 30 D | S 15KB | - | anthropics/claude-plugins-official |
| `codex-radar` | ⭐ | Analyze local Codex session history and create an evidence-grounded HTML collaboration report. Use when the user asks to run Codex Radar, sc… | html, node | ücretsiz | ✅ | 28 D | M 179KB | - | lemomo-ai/codex-radar |
| `context-compression` | ⭐ tamamlayıcı | Uzun oturumlarda bağlamı sıkıştırma: büyük araç çıktılarını anlamsal özete indirme (mikro), biten iş aşamalarını özetleme ve oturum kontrol … | api-anahtari, next.js, typescript | ücretsiz | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `context-engineering` | ⭐ birincil | Agent'a doğru bağlamı doğru zamanda verme: kalıcıdan geçiciye bağlam hiyerarşisi (kural dosyaları CLAUDE.md/AGENTS.md, spec, ilgili kaynak d… | markdown | ücretsiz | ✅ | 95 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `coordinator-mode` | ⭐ alternatif | Koordinatör olarak çok agent'lı orkestrasyon: görevi ayrıştır, sınıflandır (araştırma/uygulama/doğrulama), okuma işlerini paralel yazma işle… | api-anahtari, typescript | ücretsiz | ✅ | 85 A | S 8KB | - | vudovn/ag-kit |
| `creative-director` | ⭐ | AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calib… | html | ücretsiz | ✅ | 30 D | S 3KB | - | nexu-io/open-design |
| `diagnosing-superpowers` | ⭐ | Bir superpowers oturumu kötü gittiğinde (tekrar eden iş, yok sayılan plan, tetiklenmeyen skill, pahalılık) diskteki transkriptleri okuyup ka… | bash, jsonl | ücretsiz | ✅ | 88 A | S 41KB | - | obra/superpowers |
| `discernment-nudge` | ⭐ birincil | Kullanıcının üzerine karar vereceği önemli bir cevap ya da taslaktan sonra, cevaptaki belirli noktalara bağlı 2-3 kısa takip sorusu ekler: ö… | html | ücretsiz | ✅ | 84 A | M 21KB | - | anthropics/skills |
| `dispatching-parallel-agents` | ⭐ tamamlayıcı | Bağımsız 2+ problemi (farklı test dosyaları, alt sistemler) her birine izole bağlamlı ayrı bir agent vererek paralel çözme kalıbı: bağımsız … | typescript | ücretsiz | ✅ | 96 A | S 6KB | - | obra/superpowers |
| `enhance-prompt` | ⭐ | Improve prompts with design specs and UI/UX vocabulary. Useful for design-to-code workflows and clarifying requests for visual output. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `full-output-enforcement` | ⭐ | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits clea… | api-anahtari, html | ücretsiz | ✅ | 30 D | S 4KB | - | nexu-io/open-design |
| `intelligent-routing` | ⭐ alternatif | Her kullanıcı isteğini sessizce analiz edip anahtar kelime/alan/karmaşıklığa göre uygun uzman agent'ı (security-auditor, frontend-specialist… | api-anahtari, css, docker, html, node | ücretsiz | ✅ | 68 B | M 11KB | - | vudovn/ag-kit |
| `memory-system` | ⭐ birincil | Oturumlar arası kalıcı bellek: .agents/memory/MEMORY.md indeksi (en fazla 200 satır) ve konu dosyaları (kullanıcı tercihleri, proje kurallar… | markdown | ücretsiz | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `parallel-agents` | ⭐ alternatif | Güvenli paralel agent kullanımı: ne zaman paralelleştirilir/paralelleştirilmez, çalışma ortamından bağımsız yetenek keşfi, güven sınırı, del… | react | ücretsiz | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `project-artifact` | ⭐ | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success… | css, git, html | ücretsiz | ✅ | 28 D | M 46KB | - | anthropics/claude-plugins-official |
| `receipts` | ⭐ | Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying Claude Cod… | api-anahtari, git, html, node | ücretsiz | ✅ | 28 D | M 82KB | - | anthropics/claude-plugins-official |
| `session-report` | ⭐ | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/project… | api-anahtari, css, html, node | ücretsiz | 🟡 | 25 D | S 56KB | - | anthropics/claude-plugins-official |
| `subagent-driven-development` | ⭐ birincil | Yazılı uygulama planını görev başına taze bir uygulayıcı alt-agent göndererek yürütür; her görevden sonra spec uyumu + kod kalitesi inceleme… | git, bash | ücretsiz | ✅ | 95 A | M 56KB | - | obra/superpowers |
| `using-agent-skills` | ⭐ birincil | addyosmani/agent-skills ailesinin meta-skill'i: işin geliştirme aşamasına göre hangi skill'in uygulanacağını gösteren karar ağacı (interview… | git | ücretsiz | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `using-superpowers` | ⭐ alternatif | superpowers ailesinin meta-skill'i: '%1 ihtimal bile varsa skill'i çağır' kuralı, süreç skillerinin önceliği, rasyonalizasyon kırmızı bayrak… | git | ücretsiz | ✅ | 88 A | S 20KB | - | obra/superpowers |

### 03-web-arastirma-veri

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_ · not: `notlar/d-ai-otomasyon/03-web-arastirma-veri.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `agent-reach` | ⭐ birincil | İnternet erişimi için yönlendirici: 16 platformda (web arama/Exa, Twitter/X, Reddit, YouTube, Bilibili, Xiaohongshu, V2EX, LinkedIn, GitHub … | python, cli, web-arama | ücretsiz | ✅ | 87 A | M 46KB | - | Panniantong/Agent-Reach |
| `notebooklm` | ⭐ tamamlayıcı | Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi)… | python, notebooklm, cli | ½ kısmen | ✅ | 85 A | M 16KB | claude:farkli | teng-lin/notebooklm-py |

### 04-skill-plugin-yazimi

_Skill yazma, plugin/hook/komut geliştirme_ · not: `notlar/d-ai-otomasyon/04-skill-plugin-yazimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `agent-development` | ⭐ | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use des… |  | ücretsiz | ✅ | 28 D | M 68KB | - | anthropics/claude-plugins-official |
| `agent-development@anthropics` | alt birincil | Claude Code eklentileri için alt-agent (subagent) yazımı: Markdown + YAML frontmatter yapısı, name/description/model/color/tools alanları, <… | claude-code, markdown, yaml | ücretsiz | 🔵 | 76 B | M 69KB | - | anthropics/claude-code |
| `command-development` | ⭐ | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command argumen… | git, node, typescript | ücretsiz | 🟡 | 23 D | M 151KB | - | anthropics/claude-plugins-official |
| `command-development@anthropics` | alt birincil | Claude Code slash komutu yazımı: komut konumları (proje/kullanıcı/eklenti), YAML frontmatter (description, allowed-tools, model, argument-hi… | claude-code, markdown, yaml | ücretsiz | 🔵 | 76 B | M 150KB | - | anthropics/claude-code |
| `hook-development` | ⭐ | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement p… | react | ücretsiz | 🟡 | 23 D | M 63KB | - | anthropics/claude-plugins-official |
| `hook-development@anthropics` | alt birincil | Claude Code hook'ları: prompt tabanlı (LLM kararlı) ve komut hook'ları, eklenti hooks.json ve settings biçimi, PreToolUse/PostToolUse/Stop/S… | claude-code, bash, json | ücretsiz | 🔵 | 84 A | M 63KB | - | anthropics/claude-code |
| `library-curator` | ⭐ | Search the OD Library (the global asset registry) and apply matching assets into the current project mid-task. Use when the user asks to reu… | api-anahtari, css, html | ücretsiz | ✅ | 30 D | S 2KB | - | nexu-io/open-design |
| `od-next-media-inputs` | ⭐ | Prepare required media inputs within an existing OD Next plan. Reuse capability evidence, acquire and measure assets efficiently, and resolv… |  | ücretsiz | ✅ | 30 D | S 7KB | - | nexu-io/open-design |
| `plugin-settings` | ⭐ | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md f… | api-anahtari, git, typescript | ücretsiz | 🟡 | 23 D | M 43KB | - | anthropics/claude-plugins-official |
| `plugin-settings@anthropics` | alt tamamlayıcı | Claude Code eklentilerinde kullanıcıya özel ayar ve durum saklama kalıbı: proje kökünde `.claude/<eklenti>.local.md` dosyası (YAML frontmatt… | claude-code, yaml, bash | ücretsiz | 🔵 | 76 B | M 43KB | - | anthropics/claude-code |
| `plugin-structure` | ⭐ | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin comp… | api-anahtari, node, python | ücretsiz | 🟡 | 23 D | M 73KB | - | anthropics/claude-plugins-official |
| `plugin-structure@anthropics` | alt birincil | Claude Code eklenti mimarisi: dizin düzeni (.claude-plugin/plugin.json, commands, agents, skills, hooks, .mcp.json), manifest alanları ve bi… | claude-code, json | ücretsiz | 🔵 | 84 A | M 73KB | - | anthropics/claude-code |
| `skill-creator` | ⭐ birincil | Skill oluşturma, iyileştirme ve ölçme: niyet yakalama ve görüşme, SKILL.md yazım rehberi (aşamalı açılım, sürpriz olmama ilkesi), test istem… | python, markdown | ücretsiz | ✅ | 90 A | L 220KB | - | anthropics/skills |
| `skill-creator@anthropics` | alt | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, ed… | api-anahtari, html, node, python | ücretsiz | ✅ | 25 D | L 220KB | - | anthropics/claude-plugins-official |
| `skill-creator@composiohq` | alt alternatif | skill-creator'ın eski sürümü (ComposioHQ): skill anatomisi, aşamalı açılım ilkesi ve 6 adımlı süreç (örnekle anlama, içerik planlama, init_s… | python, markdown | ücretsiz | ✅ | 76 B | M 38KB | - | ComposioHQ/awesome-claude-skills |
| `skill-creator@freshtechbro` | alt alternatif | skill-creator'ın eski sürümünün freshtechbro/claudedesignskills kopyası: skill anatomisi, aşamalı açılım ve init/package betikli 6 adımlı sü… | python, markdown | ücretsiz | ✅ | 57 C | M 41KB | - | freshtechbro/claudedesignskills |
| `skill-creator@heyitsnoah` | alt alternatif | Anthropic skill-creator'ın güncel sürümünün claudesidian içindeki birebir kopyası (eval görüntüleyici, değerlendirici agent'lar, benchmark v… | python, markdown | ücretsiz | ✅ | 64 C | L 221KB | - | heyitsnoah/claudesidian |
| `skill-development` | ⭐ | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description"… | api-anahtari, html, python, react | ücretsiz | 🟡 | 23 D | M 34KB | - | anthropics/claude-plugins-official |
| `skill-development@anthropics` | alt alternatif | Claude Code eklentileri için skill yazım rehberi: skill anatomisi, aşamalı açılım, örnekle anlama → içerik planlama → yapı oluşturma → SKILL… | claude-code, markdown | ücretsiz | 🔵 | 68 B | M 34KB | - | anthropics/claude-code |
| `skill-share` | ⭐ alternatif | Yeni skill iskeleti oluşturur, doğrular, zip paketler ve Rube (Composio) MCP üzerinden Slack kanalına paylaşır. | mcp, slack, composio | ücretsiz | ✅ | 69 B | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `skillify` | ⭐ alternatif | Tekrar eden çok adımlı iş akışlarını yeniden kullanılabilir SKILL.md'ye dönüştürür: kalıbı tanımla, şablondan SKILL.md üret, yerleştir, doğr… | markdown | ücretsiz | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `template-skill` | alt alternatif | Boş skill şablonu: yalnızca name/description yer tutucuları ve 'talimatları buraya yaz' satırı. | markdown | ücretsiz | ✅ | 61 C | S 0KB | - | ComposioHQ/awesome-claude-skills |
| `writing-hookify-rules` | ⭐ | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or … | api-anahtari, python, typescript | ücretsiz | 🟡 | 23 D | M 8KB | - | anthropics/claude-plugins-official |
| `writing-hookify-rules@anthropics` | alt alternatif | hookify eklentisi için kural yazımı: `.claude/hookify.<kural>.local.md` dosyalarında YAML frontmatter (name, enabled, event: bash/file/stop/… | claude-code, yaml, regex | ücretsiz | 🔵 | 76 B | M 8KB | - | anthropics/claude-code |
| `writing-skills` | ⭐ tamamlayıcı | Skill yazımını süreç dokümantasyonuna uygulanmış TDD olarak ele alır: önce alt-agent'larla baskı senaryosu çalıştırıp skill'siz başarısızlığ… | markdown, graphviz | ücretsiz | ✅ | 95 A | M 107KB | - | obra/superpowers |
| `yao-meta-skill` | ⭐ | Create, improve, or evaluate an existing skill from workflows, prompts, SOPs, scripts. Use for migration/release/package, routing, evals/tes… | python | ücretsiz | ✅ | 30 D | S 3172KB | - | yaojingang/yao-meta-skill |

## Video, Ses ve AI Medya Üretimi

### 01-video-uretim-montaj

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_ · not: `notlar/g-video-ses-medya/01-video-uretim-montaj.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `8-bit-orbit-video-template` | ⭐ | Hyperframes-based video template for retro pixel deck motion design. Use when users want a high-fidelity, multi-scene HTML-to-video composit… | css, gsap, html | ücretsiz | ✅ | 30 D | S 20KB | - | nexu-io/open-design |
| `after-hours-editorial-template` | ⭐ | Luxury dark-editorial HyperFrames template for three-page cinematic storyboards, inspired by haute couture title cards and magazine chapter … | css, html | ücretsiz | ✅ | 30 D | S 16KB | - | nexu-io/open-design |
| `captions-overlay` | ⭐ tamamlayıcı | HyperFrames videolarında altyazı doktrini: her cümle drop / rail / embed olarak sınıflanır (embed nadir zirve), altyazı alttan rezerve bir ş… | hyperframes | ücretsiz | ✅ | 88 A | S 6KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `changelog-video` | ⭐ alternatif | Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka… | hyperframes, html, gsap, node, heygen | ½ kısmen | ✅ | 71 B | M 521KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `chat-motion-overlay` | ⭐ | Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat containers, option… | python, remotion, typescript | ücretsiz | ✅ | 30 D | S 1308KB | - | nexu-io/open-design |
| `create-video` | ⭐ birincil | HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Ö… | heygen, api-anahtari, rest-api | 💲 ücretli | ✅ | 87 A | S 92KB | claude:ayni | calesthio/OpenMontage |
| `ffmpeg` | ⭐ tamamlayıcı | FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar… | ffmpeg | ücretsiz | ✅ | 86 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `figma` | ⭐ tamamlayıcı | Figma içeriğini HyperFrames videosuna getirir: asset (SVG/PNG), marka token'ları, frame'leri düzenlenebilir HTML bileşen olarak, connector i… | hyperframes, figma api, gsap | ½ kısmen | 🟡 | 85 A | S 11KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `frame-data-chart-nyt` | ⭐ | NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band). | html | ücretsiz | ✅ | 30 D | S 9KB | - | nexu-io/open-design |
| `frame-flowchart-sticky` | ⭐ | SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel. | css, html | ücretsiz | ✅ | 30 D | S 10KB | - | nexu-io/open-design |
| `frame-glitch-title` | ⭐ | Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes. | css, html | ücretsiz | ✅ | 30 D | S 9KB | - | nexu-io/open-design |
| `frame-light-leak-cinema` | ⭐ | Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards. | css, html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `frame-liquid-bg-hero` | ⭐ | WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters. | canvas, css, html, webgl | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `frame-logo-outro` | ⭐ | Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames. | css, html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `frame-macos-notification` | ⭐ | Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers. | css, html | ücretsiz | ✅ | 30 D | S 7KB | - | nexu-io/open-design |
| `hyperframes` | ⭐ birincil | HyperFrames'in yeni tek giriş skili: HTML'i kare kare render ederek videoya çeviren sistemin render sözleşmesini (12 kural), düzenlenebilirl… | hyperframes, html, gsap, node 22+, ffmpeg | ½ kısmen | 🟡 | 93 A | S 1112KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-cli` | ⭐ tamamlayıcı | HyperFrames CLI'yi işe göre anlatır: init/capture, check, snapshot, timeline düzenleme (move/trim/split…), preview, yerel/bulut render, proj… | hyperframes, node 22+, ffmpeg, chrome | ücretsiz | 🟡 | 93 A | S 120KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-registry` | ⭐ tamamlayıcı | ~450 hazır HyperFrames bloğu ve bileşenini (geçişler, overlay, başlık, kinetik tipografi, altyazı stilleri, grafik, harita, 3D, kamera harek… | hyperframes, html, gsap | ücretsiz | 🟡 | 85 A | S 83KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `lemo-opuscar` | ⭐ birincil | Lemo-Opuscar film stili kütüphanesine giriş skili: 59 hazır stilden birini seçip (ya da kendi stilini oluşturup) video modeli kullanmadan, t… | node, three.js, ffmpeg, python, kokoro tts | ücretsiz | ✅ | 85 A | S 10KB | - | lemomo-ai/lemo-opuscar |
| `lemo-opuscar@lemomo-ai` | alt alternatif | Aynı Lemo-Opuscar skilinin 'dizin/eklenti paketi' sürümü: kütüphanenin yanında paketlenmiş (library/) gelmesini bekler, ~/.lemo-opuscar'a ko… | node, three.js, ffmpeg, python, kokoro tts | ücretsiz | ✅ | 69 B | S 123KB | - | lemomo-ai/lemo-opuscar |
| `media-use` | ⭐ birincil | HyperFrames videosu için her türlü medyayı tek komutla (`media-use resolve`) bulur ya da üretir: müzik, ses efekti, görsel/ikon/logo, seslen… | hyperframes, heygen, ffmpeg, python 3.10+ (kokoro tts) | ½ kısmen | 🟡 | 93 A | S 1842KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `motion-design` | ⭐ | Apply motion craft to an active task: refine a brief, beat map, visual continuity, typography, pacing, and timeline implementation. Use when… | api-anahtari, canvas, css, gsap, html | ücretsiz | ✅ | 28 D | M 24KB | claude:farkli | nexu-io/open-design |
| `oversized-cursor` | ⭐ tamamlayıcı | Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasa… | hyperframes, gsap, css | ücretsiz | ✅ | 88 A | S 6KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `playwright-recording` | ⭐ birincil | Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün tur… | playwright, typescript, node | ücretsiz | ✅ | 86 A | M 20KB | claude:ayni | calesthio/OpenMontage |
| `remotion` | alt | Programmatic video creation with React. Useful for branded explainers, social cuts, dashboards-to-video, and reproducible motion graphics. | react, remotion | ½ kısmen | ✅ | 26 D | S 1KB | claude:farkli | nexu-io/open-design |
| `remotion-best-practices` | ⭐ birincil | Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile m… | remotion, react, typescript | ½ kısmen | ✅ | 94 A | S 112KB | claude:farkli,agents:farkli | calesthio/OpenMontage |
| `remotion-to-hyperframes` | ⭐ tamamlayıcı | Başka araçlarla yapılmış video kodunu ya da çıktısını HyperFrames'e alır ve kare kare karşılaştırarak doğrular: Native (Remotion/HTML/GSAP ç… | hyperframes, remotion, react, python | ücretsiz | 🟡 | 85 A | S 170KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `remotion@calesthio` | ⭐ alternatif | claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch,… | remotion, react, typescript | ½ kısmen | ✅ | 71 B | S 16KB | claude:ayni | calesthio/OpenMontage |
| `slideshow` | ⭐ tamamlayıcı | HyperFrames ile canlı sunulan slayt gösterisi kurar: her slayt bir sahne, JSON adası ile fragment reveal, dallanan hotspot'lar ve konuşmacı … | hyperframes, html, gsap | ücretsiz | 🟡 | 85 A | S 48KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `social-reddit-card` | ⭐ | Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing. | css, html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `social-spotify-card` | ⭐ | Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepages. | css, html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `social-x-post-card` | ⭐ | Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards. | css, html | ücretsiz | ✅ | 30 D | S 8KB | - | nexu-io/open-design |
| `swiss-user-research-video-template` | ⭐ | Swiss-style user-research narrative template in warm-paper editorial aesthetics. Use when users ask for a premium research deck or story-fir… | api-anahtari, css, html | ücretsiz | ✅ | 30 D | S 23KB | - | nexu-io/open-design |
| `synthetic-screen-recording` | ⭐ alternatif | Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter ka… | remotion, react, typescript | ücretsiz | ✅ | 78 B | M 10KB | claude:ayni | calesthio/OpenMontage |
| `vfx-text-cursor` | ⭐ | Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros. | html | ücretsiz | ✅ | 30 D | S 7KB | - | nexu-io/open-design |
| `video-download` | ⭐ birincil | yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonları… | yt-dlp, ffmpeg | ücretsiz | ✅ | 87 A | S 3KB | claude:ayni | calesthio/OpenMontage |
| `video-downloader` | ⭐ | Download videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality opti… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `video-edit` | ⭐ birincil | ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, form… | ffmpeg | ücretsiz | ✅ | 95 A | S 12KB | claude:ayni | calesthio/OpenMontage |
| `video-hyperframes` | ⭐ | Hyperframes / Remotion-compatible continuous frame animation with autoplay support. | html, remotion | ücretsiz | ✅ | 30 D | S 10KB | - | nexu-io/open-design |
| `video-toolkit` | ⭐ alternatif | claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan ka… | remotion, python, node, modal, runpod | 💲 ücretli | ✅ | 70 B | M 15KB | claude:ayni | calesthio/OpenMontage |
| `video-translate` | ⭐ birincil | HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve w… | heygen, api-anahtari, rest-api | 💲 ücretli | ✅ | 86 A | M 11KB | claude:ayni | calesthio/OpenMontage |
| `video-understand` | ⭐ birincil | ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gere… | ffmpeg, python, whisper | ücretsiz | ✅ | 87 A | S 27KB | claude:ayni | calesthio/OpenMontage |
| `weread-year-in-review-video-template` | ⭐ | WeRead-inspired HyperFrames video template for vertical annual reading reports, personal reading dashboards, book-note recaps, and shareable… | html | ücretsiz | ✅ | 30 D | S 33KB | - | nexu-io/open-design |
| `youtube-clipper` | ⭐ | YouTube clip generation and editing with automated workflows — pull source video, slice highlights, add captions, and export. |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `youtube-downloader` | ⭐ alternatif | yt-dlp kullanan download_video.py betiğiyle YouTube videosu indirir: kalite (best…360p), format (mp4/webm/mkv) ve yalnızca ses (MP3) seçenek… | python, yt-dlp, ffmpeg | ücretsiz | ✅ | 77 B | S 7KB | - | ComposioHQ/awesome-claude-skills |

### 02-ses-muzik-konusma

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_ · not: `notlar/g-video-ses-medya/02-ses-muzik-konusma.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `acestep` | ⭐ alternatif | ACE-Step 1.5 açık kaynak modeliyle RunPod üzerinde enstrümantal müzik, sözlü şarkı, cover/stil aktarımı ve stem ayırma yapar; sahne ön ayarl… | python, runpod, ffmpeg | 💲 ücretli | ✅ | 70 B | M 9KB | claude:ayni | calesthio/OpenMontage |
| `agents` | ⭐ birincil | ElevenLabs Agents Platform ile gerçek zamanlı sesli yapay zekâ ajanı (asistan, müşteri hizmetleri botu, etkileşimli karakter) kurar; CLI, Py… | elevenlabs, python, typescript, api-anahtari | 💲 ücretli | ✅ | 86 A | M 64KB | claude:ayni | calesthio/OpenMontage |
| `ai-music-album` | ⭐ | Full-lifecycle AI music album production — concept, lyric drafting, track sequencing, and export. Useful for indie album experiments and bra… |  | ücretsiz | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `azure-speech-to-text` | ⭐ alternatif | Azure AI Speech Fast Transcription REST API ile ses/videoyu kelime zaman damgalı, konuşmacı ayrımlı yazıya döker; OpenMontage'da azure_stt a… | azure, python, api-anahtari | 💲 ücretli | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `azure-text-to-speech` | ⭐ alternatif | Azure nöral TTS ile SSML prozodi ve konuşma stili kontrollü çok dilli seslendirme üretir; OpenMontage'da azure_tts aracı olarak tts_selector… | azure, python, ssml, api-anahtari | 💲 ücretli | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `dashscope` | ⭐ alternatif | Alibaba DashScope (Bailian) entegrasyonu: Qwen-Image ile görsel üretimi, Qwen-TTS ile seslendirme ve kelime zaman damgalı Qwen-ASR transkrip… | dashscope, python, api-anahtari | 💲 ücretli | ✅ | 79 B | S 6KB | claude:ayni | calesthio/OpenMontage |
| `doubao-tts` | ⭐ alternatif | Volcengine Doubao Speech 2.0 ile Mandarin ve çok dilli seslendirme üretir; asenkron uç noktadan karakter düzeyinde zaman damgası alıp altyaz… | volcengine, python, api-anahtari | 💲 ücretli | ✅ | 79 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `elevenlabs` | ⭐ birincil | ElevenLabs ile seslendirme, ses klonlama, ses efekti ve müzik üretimini tek skillde toplar; model seçimi, stile göre ses ayarları, duraklama… | elevenlabs, python, ffmpeg, api-anahtari | 💲 ücretli | ✅ | 94 A | M 16KB | claude:farkli | calesthio/OpenMontage |
| `fish-audio-tts` | ⭐ alternatif | fish.audio S1/S2 modelleriyle duygu etiketli ([laugh], [whispers]) çok dilli seslendirme ve reference_id ile klonlanmış sesleri yeniden kull… | fish-audio, python, api-anahtari | 💲 ücretli | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `lyria` | ⭐ alternatif | Google Lyria 3 ile Gemini Interactions API üzerinden müzik üretir ve doğrular; Clip/Pro/RealTime model seçimi, yapılandırılmış prompt sözleş… | google-gemini, api-anahtari | 💲 ücretli | ✅ | 94 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `music` | ⭐ birincil | ElevenLabs Music API ile metin isteminden enstrümantal parça, sözlü şarkı, jingle üretir; bölüm bazlı ince kontrol için kompozisyon planı ol… | elevenlabs, python, typescript, api-anahtari | 💲 ücretli | ✅ | 95 A | S 10KB | claude:ayni | calesthio/OpenMontage |
| `setup-api-key` | ⭐ birincil | ElevenLabs API anahtarını kurar: önce mevcut ELEVENLABS_API_KEY'i bulup doğrular, yoksa kullanıcıyı adım adım anahtar oluşturmaya yönlendiri… | elevenlabs, api-anahtari | 💲 ücretli | ✅ | 79 B | S 3KB | claude:ayni | calesthio/OpenMontage |
| `sound-effects` | ⭐ birincil | ElevenLabs ile metin tarifinden ses efekti, ambiyans, döngü ve UI sesi üretir; süre, prompt etkisi ve döngü parametrelerini açıklar. | elevenlabs, python, typescript, api-anahtari | 💲 ücretli | ✅ | 95 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `speech` | ⭐ | Generate spoken audio from text using OpenAI's API with built-in voices. Useful for narrated explainers, lecture audio, and quick voiceover … |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `speech-to-text` | ⭐ birincil | ElevenLabs Scribe v2 ile 90+ dilde kelime zaman damgalı, konuşmacı ayrımlı transkripsiyon yapar; anahtar terim ipucu, dil tespiti ve gerçek … | elevenlabs, python, typescript, api-anahtari | 💲 ücretli | ✅ | 94 A | M 40KB | claude:ayni | calesthio/OpenMontage |
| `text-to-speech` | ⭐ alternatif | HeyGen'in Starfish TTS modeliyle bağımsız ses dosyası üretir; ses listeleme, hız/perde kontrolü ve MCP araçlarını tercih etme kuralını içeri… | heygen, api-anahtari, rest-api | 💲 ücretli | ✅ | 86 A | M 10KB | claude:ayni | calesthio/OpenMontage |
| `venice-audio-music` | ⭐ | Music generation queueing, retrieval, and completion endpoints via Venice.ai. Suited for jingles, background loops, and prototype scoring. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `venice-audio-speech` | ⭐ | Text-to-speech models, voices, formats, and streaming via Venice.ai. Useful for narration, voiceover, and conversational agent voices. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |

### 03-ai-gorsel-video-modelleri

_AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu_ · not: `notlar/g-video-ses-medya/03-ai-gorsel-video-modelleri.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `3d-asset-generation` | ⭐ birincil | OpenMontage dünyaları için üretim kalitesinde 3D varlık üretir/yönlendirir: Atlas Tripo, fal Hunyuan 3D, SAM 3D ve CC0 kataloglar arasından … | blender, three.js, atlas-cloud, fal-ai, api-anahtari | ½ kısmen | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `ai-video-gen` | ⭐ birincil | Metinden ve görselden AI video üretimini fal.ai, HeyGen ve Gemini API ağ geçitleri üzerinden yönetir; Seedance 2.0'ı premium varsayılan saya… | fal-ai, heygen, google-gemini, api-anahtari | 💲 ücretli | ✅ | 86 A | M 11KB | claude:farkli | calesthio/OpenMontage |
| `atlas-cloud` | ⭐ alternatif | Atlas Cloud ağ geçidiyle tek anahtarla Seedance 2.5/2.0, Gemini Omni, MiniMax H3, Seedream 5, GPT Image 2, Nano Banana 2 görsel/video üretim… | atlas-cloud, python, api-anahtari | 💲 ücretli | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `avatar-video` | ⭐ tamamlayıcı | HeyGen v2 API ile avatar, ses, metin, sahne ve arka plan üzerinde tam kontrollü avatar videosu üretir; çok sahneli, şeffaf WebM ve Remotion … | heygen, api-anahtari, rest-api | 💲 ücretli | ✅ | 87 A | S 177KB | claude:ayni | calesthio/OpenMontage |
| `bfl-api` | ⭐ tamamlayıcı | Black Forest Labs FLUX API entegrasyon rehberi: uç noktalar, bölgesel sunucular, fiyatlar, asenkron sorgulama, hız sınırı, hata yönetimi ve … | bfl-flux, python, typescript, api-anahtari | 💲 ücretli | ✅ | 94 A | M 79KB | claude:ayni | calesthio/OpenMontage |
| `comfyui` | ⭐ birincil | OpenMontage'da ComfyUI iş akışlarıyla (comfyui_image/video/music) yerel üretim: sunucu sözleşmesi, API formatlı iş akışı, output_node seçimi… | comfyui, python, gpu | ½ kısmen | ✅ | 86 A | M 8KB | claude:ayni | calesthio/OpenMontage |
| `ecommerce-image-workflow` | ⭐ | Reference-product ecommerce image workflow for generating a compact set of product-faithful main, feature, and lifestyle images from real pr… | html | ücretsiz | ✅ | 28 D | M 24KB | - | nexu-io/open-design |
| `faceswap` | ⭐ birincil | HeyGen FaceswapNode iş akışıyla kaynak görseldeki yüzü hedef videoya aktarır; iş gönderme, durum sorgulama ve TypeScript/Python örnekleri iç… | heygen, api-anahtari, rest-api | 💲 ücretli | ✅ | 79 B | S 7KB | claude:ayni | calesthio/OpenMontage |
| `fal-3d` | ⭐ | Generate 3D models from text or images via fal.ai. Useful for game assets, AR previews, product mockups, and concept sculpting. | webgl | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-generate` | ⭐ | Generate images and videos using fal.ai AI models. Production-grade catalogue covering Flux, SDXL, ideogram, and other community-hosted endp… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-image-edit` | ⭐ | AI-powered image editing with style transfer, background removal, object removal, and inpainting via fal.ai hosted models. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-kling-o3` | ⭐ | Generate images and videos with Kling O3 — Kling's most powerful model family — via fal.ai. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-lip-sync` | ⭐ | Create talking head videos and lip sync audio to video via fal.ai. Useful for explainer avatars, multilingual dubbing previews, and social c… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-realtime` | ⭐ | Real-time and streaming AI image generation via fal.ai. Suited for moodboard exploration, draft variations, and rapid creative iteration. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-restore` | ⭐ | Restore and fix image quality — deblur, denoise, fix faces, and restore old documents using fal.ai's hosted restoration models. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-train` | ⭐ | Train custom AI models (LoRA) on fal.ai for personalized image generation tailored to a brand, character, or style. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-tryon` | ⭐ | Virtual try-on — see how clothes look on a person via fal.ai's hosted try-on models. Useful for ecommerce, lookbooks, and styling experiment… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-upscale` | ⭐ | Upscale and enhance image and video resolution using AI super-resolution models hosted on fal.ai. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-video-edit` | ⭐ | Edit existing videos using AI — remix style, upscale, remove background, and add audio via fal.ai's hosted video models. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `fal-vision` | ⭐ | Analyze images — segment objects, detect, run OCR, describe, and answer visual questions via fal.ai vision models. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `flux-best-practices` | ⭐ birincil | BFL FLUX görsel modelleri için kapsamlı prompt rehberi: prompt yapısı, model seçimi (klein/pro/max/flex), T2I, I2I, JSON yapılandırılmış pro… | bfl-flux | ücretsiz | ✅ | 95 A | S 122KB | claude:ayni | calesthio/OpenMontage |
| `gemini-omni` | ⭐ alternatif | Google Gemini Omni Flash ile 3-10 sn 720p sesli video üretimi ve aynı klibi doğal dille durum korumalı (interaction_id) düzenleme; referans … | google-gemini, api-anahtari | 💲 ücretli | ✅ | 94 A | M 8KB | claude:ayni | calesthio/OpenMontage |
| `gif-sticker-maker` | ⭐ | Convert photos into animated GIF stickers in Funko Pop / Pop Mart style via the MiniMax API. Useful for personalized chat stickers and avata… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `grok-media` | ⭐ alternatif | xAI Grok görsel ve video üretimi rehberi: kimlik doğrulama, uç noktalar, görsel düzenleme/birleştirme, referans görselli video, asenkron sor… | xai-grok, api-anahtari | 💲 ücretli | ✅ | 79 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `heygen` | ⭐ alternatif | [KULLANIMDAN KALKMIŞ] HeyGen Video Agent ve v2 avatar iş akışlarını birleştiren eski skill; yerini create-video ve avatar-video aldı, geriye… | heygen, api-anahtari | 💲 ücretli | ✅ | 71 B | S 225KB | claude:ayni | calesthio/OpenMontage |
| `imagegen` | ⭐ | Generate and edit images using OpenAI's Image API for project assets — UI mockups, icons, illustrations, social cards, and visual references… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `imagen` | ⭐ | Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets. |  | ½ kısmen | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `kling-official` | ⭐ alternatif | Kling resmi doğrudan API'si (KLING_API_KEY) için OpenMontage sağlayıcı kuralları: fal.ai Kling'den ayrımı, klasik/turbo görev protokolleri, … | kling, python, api-anahtari | 💲 ücretli | ✅ | 86 A | M 9KB | claude:ayni | calesthio/OpenMontage |
| `ltx2` | ⭐ alternatif | LTX-2.3 22B modeliyle Modal (A100) üzerinde ~5 sn metinden/görselden video üretir; kare sayısı kuralı, çözünürlükler ve sinematik prompt reh… | ltx, modal, python | ½ kısmen | ✅ | 71 B | S 7KB | claude:ayni | calesthio/OpenMontage |
| `minimax-h3` | ⭐ alternatif | MiniMax H3 (Hailuo 3.0) videosunu resmi API, fal.ai, Runway, ComfyUI Partner Node veya yerel açık ağırlıklarla üretir; rotalar arası model k… | minimax, comfyui, api-anahtari | 💲 ücretli | ✅ | 87 A | S 2KB | claude:ayni | calesthio/OpenMontage |
| `nanobanana-ppt` | ⭐ | AI-powered PPT generation with document analysis and styled images via the NanoBanana stack. Combines image generation with structured deck … |  | ½ kısmen | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `pixelbin-media` | ⭐ | Generate and edit images and videos with an 85+ API portfolio and build visually appealing website pages via Pixelbin. |  | ½ kısmen | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `provider-model-refresh` | ⭐ birincil | Eylül 2026 görsel, video, konuşma ve Avatar V adaptörleri (GPT Image 2.5, Gemini 3 Pro Image, Ideogram 4.5, Wan 3.0, LTX-2.5, Eleven v4, Lyr… | openmontage, python, api-anahtari | ½ kısmen | ✅ | 87 A | S 5KB | - | calesthio/OpenMontage |
| `replicate` | ⭐ | Discover, compare, and run AI models using Replicate's API. Strong fit for image, audio, and video generation pipelines that swap models fre… |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `seedance-2-0` | ⭐ tamamlayıcı | ByteDance Seedance 2.0 için yetkili prompt ve parametre rehberi: tek geçişte senkron ses, tek üretimde çoklu çekim, yönetmen düzeyi kamera k… | seedance, fal-ai, api-anahtari | 💲 ücretli | ✅ | 94 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `seedance-2-5` | ⭐ alternatif | Seedance 2.5 ile 4-30 sn sinematik video: fal.ai, Volcengine Ark, Runway, ComfyUI rotaları; bölümlü prompt sözleşmesi, 'Hard cut' çoklu çeki… | seedance, fal-ai, api-anahtari | 💲 ücretli | ✅ | 94 A | M 23KB | claude:ayni | calesthio/OpenMontage |
| `sora` | ⭐ | Generate, remix, and manage short video clips via OpenAI's Sora API. Useful for cinematic shots, b-roll, and rapid concept video iteration. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `venice-image-edit` | ⭐ | Image edits, upscaling, and background removal via the Venice.ai API. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `venice-image-generate` | ⭐ | Image generation endpoints and available styles via the Venice.ai API. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |
| `venice-video` | ⭐ | Video generation and transcription workflows via the Venice.ai API. |  | 💲 ücretli | ✅ | 26 D | S 1KB | - | nexu-io/open-design |

### 04-motion-graphics-karakter

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_ · not: `notlar/g-video-ses-medya/04-motion-graphics-karakter.md`

| Skill | Durum | Ne yapar | Teknoloji | Ücret | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|---|
| `canvas-procedural-animation` | ⭐ alternatif | p5.js/Canvas ile karakter destekleyici prosedürel hareket: parçacık, hava efekti, yaprak, squash/stretch ve basit yürüme döngüleri; zaman/ka… | p5js, canvas, javascript | ücretsiz | ✅ | 79 B | S 1KB | claude:ayni | calesthio/OpenMontage |
| `character-animation-qa` | ⭐ tamamlayıcı | Karakter animasyonunu sunmadan önce katmanlı kontrol: şema doğrulama, varlık kontrolü, Playwright ile tarayıcı önizleme ve ekran görüntüsü, … | playwright, ffmpeg | ücretsiz | ✅ | 79 B | S 2KB | claude:ayni | calesthio/OpenMontage |
| `character-rigging` | ⭐ tamamlayıcı | Yerel 2D karakter animasyonu için veri güdümlü rig paketi: parçalar, pivotlar, katman sırası, kısıtlar ve görünümler; her karakteri jenerik … | svg, gsap, remotion | ücretsiz | ✅ | 79 B | S 2KB | claude:ayni | calesthio/OpenMontage |
| `cut-the-curve` | ⭐ tamamlayıcı | Hız eşlemeli sahne geçişleri kataloğu: zoom-through, ters zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut; ayrıca sahne içi … | gsap, hyperframes | ücretsiz | ✅ | 95 A | M 28KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `huashu-art-motion` | ⭐ | 辅助艺术动画与解说任务：35 种艺术风格配方、9 种解说语法、分镜与确定性 Canvas 绘制工具。按宿主时间轴实现，素材与导出使用宿主能力。 | canvas | ücretsiz | ✅ | 30 D | S 424KB | - | nexu-io/open-design |
| `layers` | ⭐ | Split one image into editable layers (PSD + PNG). 把一张图拆成图层（PSD + PNG）。 | api-anahtari, canvas, python | ücretsiz | ✅ | 28 D | M 31KB | - | lemomo-ai/lemo-wake |
| `manim-composer` | ⭐ tamamlayıcı | Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını so… | manim | ücretsiz | ✅ | 87 A | S 22KB | claude:ayni | calesthio/OpenMontage |
| `manimce-best-practices` | ⭐ birincil | Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve y… | manim, python, latex | ücretsiz | ✅ | 95 A | S 206KB | claude:ayni | calesthio/OpenMontage |
| `manimgl-best-practices` | ⭐ alternatif | ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşi… | manim, python, opengl, latex | ücretsiz | ✅ | 86 A | S 729KB | claude:ayni | calesthio/OpenMontage |
| `motion-doctrine` | ⭐ birincil | Çok sahneli videonun bağımsız slaytlar yığını değil tek kesintisiz kamera hareketi gibi hissettirmesi için üst düzey hareket yasası: vektör … | hyperframes, gsap, node | ücretsiz | ✅ | 87 A | M 44KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `oil-motion` | ⭐ | 处理视频和序列帧，编译滚动、指针、拖动与状态驱动的网页动效；内含本地媒体处理脚本和运行时。新素材生成使用宿主工具。 | api-anahtari, css, ffmpeg, html, python | ücretsiz | ✅ | 28 D | M 318KB | - | nexu-io/open-design |
| `pose-library-design` | ⭐ tamamlayıcı | Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekle… | gsap, remotion | ücretsiz | ✅ | 79 B | S 1KB | claude:ayni | calesthio/OpenMontage |
| `seam-craft` | ⭐ tamamlayıcı | Sahneden sahneye geçişlerin ana zaman çizelgesinde doğru birleşmesi için render önkoşulları: koyu filmlerde kesmede beyaz parlamayı önleyen … | hyperframes, html, css | ücretsiz | ✅ | 80 A | S 5KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `svg-character-animation` | ⭐ birincil | SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pi… | svg, gsap, remotion, hyperframes | ücretsiz | ✅ | 87 A | S 2KB | claude:ayni | calesthio/OpenMontage |
| `threejs-world-generation` | ⭐ birincil | Metinden veya yapılandırılmış özetten belirlenimci, düzenlenebilir Three.js dünyaları: arazi, semantik bölgeler, prosedürel biyomlar, landma… | three.js, hyperframes, openmontage, python, blender | ücretsiz | ✅ | 86 A | M 16KB | claude:ayni | calesthio/OpenMontage |
| `upload` | ⭐ | Share a film to the lemo-wake gallery. 把动图投稿到作品墙。 | api-anahtari, git, python | ücretsiz | ✅ | 30 D | S 21KB | - | lemomo-ai/lemo-wake |
| `visual-style` | ⭐ birincil | Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper… | markdown, html | ücretsiz | ✅ | 87 A | S 81KB | claude:ayni | calesthio/OpenMontage |
| `wake` | ⭐ | Turn one image into a ~5 s looping animation. 把一张图做成约 5 秒的循环动图。 | api-anahtari, canvas, ffmpeg, html, node | ücretsiz | ✅ | 28 D | M 549KB | - | lemomo-ai/lemo-wake |
