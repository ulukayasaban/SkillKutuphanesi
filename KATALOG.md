# Skill Kataloğu

> `araclar/katalog-uret.py` üretir — elle düzenleme. Kaynak: `registry.json`.

Toplam **362** skill (+878 gizli: entegrasyon `KATALOG-entegrasyon.md`, repo-içi `notlar/referans/repo-ici-skiller.md`).

**İşaretler:** ⭐ tercih edilen · `alt` aynı isimli alternatif sürüm · Codex: ✅ tam uyumlu, 🟡 Claude araç adları geçiyor ama çalışır, 🔵 konusu Claude Code'a özel · Yük: S/M/L (agent bağlamına etkisi) · globalde: bilgisayardaki genel klasörde aynı isimli skill (ayni/farkli)

## İçindekiler

- **Tasarım ve Ön Yüz** (109)
  - [01-ui-ux-tasarim-dili](#01-ui-ux-tasarim-dili) — 15 skill · Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi
  - [02-tasarim-sistemi-marka](#02-tasarim-sistemi-marka) — 8 skill · Design token, tema, marka kimliği, banner/logo
  - [03-animasyon-motion](#03-animasyon-motion) — 17 skill · GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim
  - [04-scroll-deneyimi](#04-scroll-deneyimi) — 6 skill · Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri
  - [05-3d-webgl](#05-3d-webgl) — 34 skill · Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader
  - [06-oyun-2d-grafik](#06-oyun-2d-grafik) — 12 skill · Oyun geliştirme, PixiJS, 2D grafik
  - [07-gorsel-sanat-sunum](#07-gorsel-sanat-sunum) — 10 skill · Poster/canvas tasarımı, generative art, slayt, GIF
  - [08-onyuz-test-kalite](#08-onyuz-test-kalite) — 7 skill · Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı
- **Yazılım Geliştirme** (78)
  - [01-planlama-metodoloji](#01-planlama-metodoloji) — 15 skill · Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini
  - [02-kod-kalitesi-review](#02-kod-kalitesi-review) — 13 skill · Code review, sadeleştirme, temiz kod
  - [03-test-hata-ayiklama](#03-test-hata-ayiklama) — 11 skill · TDD, hata ayıklama, doğrulama
  - [04-mimari-api-veritabani](#04-mimari-api-veritabani) — 14 skill · Mimari, API/arayüz tasarımı, veritabanı, backend
  - [05-git-pr-surum](#05-git-pr-surum) — 8 skill · Git, worktree, PR, sürüm/release, changelog
  - [06-devops-guvenlik-performans](#06-devops-guvenlik-performans) — 10 skill · CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans
  - [07-framework-ozel](#07-framework-ozel) — 7 skill · Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)
- **Doküman ve İçerik** (43)
  - [01-ofis-dokumanlari](#01-ofis-dokumanlari) — 8 skill · Word, Excel, PowerPoint, PDF üretme/düzenleme
  - [02-diyagram-dokumantasyon](#02-diyagram-dokumantasyon) — 6 skill · Diyagram, teknik dokümantasyon, ADR, ortak yazım
  - [03-yazi-iletisim-icerik](#03-yazi-iletisim-icerik) — 15 skill · Yazı, iletişim, pazarlama/içerik, kariyer
  - [04-not-alma-bilgi-yonetimi](#04-not-alma-bilgi-yonetimi) — 14 skill · Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni
- **AI ve Otomasyon** (42)
  - [01-claude-api-mcp](#01-claude-api-mcp) — 9 skill · Claude API, MCP sunucusu, model geçişi
  - [02-agent-orkestrasyon](#02-agent-orkestrasyon) — 14 skill · Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları
  - [03-web-arastirma-veri](#03-web-arastirma-veri) — 3 skill · Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma
  - [04-skill-plugin-yazimi](#04-skill-plugin-yazimi) — 16 skill · Skill yazma, plugin/hook/komut geliştirme
- **Video, Ses ve AI Medya Üretimi** (90)
  - [01-video-uretim-montaj](#01-video-uretim-montaj) — 45 skill · Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg
  - [02-ses-muzik-konusma](#02-ses-muzik-konusma) — 14 skill · Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi
  - [03-ai-gorsel-video-modelleri](#03-ai-gorsel-video-modelleri) — 17 skill · AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu
  - [04-motion-graphics-karakter](#04-motion-graphics-karakter) — 14 skill · Motion graphics, Manim, karakter animasyonu/rig, görsel stil

## Tasarım ve Ön Yüz

### 01-ui-ux-tasarim-dili

_Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi_ · not: `notlar/a-tasarim-onyuz/01-ui-ux-tasarim-dili.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `design` | ⭐ | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corpor… | api-anahtari, css, html, playwright, python | 🟡 | 88 A | M 284KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `design-dna` | ⭐ | Extract, define, and apply design DNA across three dimensions: design system (tokens), design style (qualitative feel), and visual effects (… | api-anahtari, canvas, css, gsap, html | ✅ | 84 A | M 709KB | claude:farkli | zanwei/design-dna |
| `design-spec` | ⭐ | How to author a DESIGN.md file — the machine-readable design-token + human-rationale format that must exist before any UI is built. YAML fro… | api-anahtari, node, tailwind | ✅ | 89 A | S 21KB | - | vudovn/ag-kit |
| `design-taste-frontend` | ⭐ | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love,… | api-anahtari, css, html, next.js, node | ✅ | 88 A | L 2363KB | - | Leonxlnx/taste-skill |
| `frontend-design` | ⭐ | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typog… | api-anahtari, css | ✅ | 86 A | M 9KB | - | anthropics/claude-code |
| `frontend-design@anthropics` | alt | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typog… | api-anahtari, css | ✅ | 86 A | M 19KB | - | anthropics/skills |
| `frontend-design@vudovn` | alt | Anti-slop frontend design for web UI — landing pages, portfolios, marketing/product sites, and redesigns. Reads the brief, infers the right … | api-anahtari, canvas, css, git, gsap | ✅ | 84 A | L 161KB | - | vudovn/ag-kit |
| `impeccable` | ⭐ | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend inte… | api-anahtari, css, node | ✅ | 91 A | M 2138KB | - | pbakaus/impeccable |
| `mobile-design` | ⭐ | Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Te… | api-anahtari, python, react, typescript | ✅ | 87 A | M 216KB | - | vudovn/ag-kit |
| `modern-web-design` | ⭐ | Modern web design trends, principles, and implementation patterns for 2024-2025. Use this skill when designing websites, creating interactiv… | api-anahtari, canvas, css, gsap, html | ✅ | 65 B | L 151KB | - | freshtechbro/claudedesignskills |
| `tailwind-patterns` | ⭐ | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. | api-anahtari, css, react, tailwind, vue | ✅ | 89 A | S 7KB | - | vudovn/ag-kit |
| `ui-styling` | ⭐ | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, a… | api-anahtari, canvas, css, html, next.js | ✅ | 93 A | M 5627KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `ui-ux-pro-max` | ⭐ | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces,… | api-anahtari, css, gsap, html, next.js | 🟡 | 88 A | M 3499KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `web-design-guidelines` | ⭐ | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX"… |  | ✅ | 89 A | S 2KB | claude:farkli | vudovn/ag-kit |
| `web-design-guidelines@calesthio` | alt | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX"… |  | ✅ | 92 A | S 1KB | claude:ayni | calesthio/OpenMontage |

### 02-tasarim-sistemi-marka

_Design token, tema, marka kimliği, banner/logo_ · not: `notlar/a-tasarim-onyuz/02-tasarim-sistemi-marka.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `banner-design` | ⭐ | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or … | canvas, css, html | 🟡 | 90 A | S 12KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand` | ⭐ | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, market… | api-anahtari, css, node, tailwind | ✅ | 95 A | S 106KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand-guidelines` | ⭐ | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use… | python | ✅ | 88 A | S 13KB | - | anthropics/skills |
| `brand-guidelines@composiohq` | alt | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use… | python | ✅ | 88 A | S 13KB | - | ComposioHQ/awesome-claude-skills |
| `design-system` | ⭐ | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacin… | api-anahtari, canvas, css, html, node | ✅ | 95 A | S 178KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `tailwind-design-system` | ⭐ | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component… | api-anahtari, css, react, tailwind, typescript | ✅ | 90 A | M 22KB | claude:ayni | calesthio/OpenMontage |
| `theme-factory` | ⭐ | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set t… | html | ✅ | 88 A | S 141KB | - | anthropics/skills |
| `theme-factory@composiohq` | alt | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set t… | html | ✅ | 88 A | S 141KB | - | ComposioHQ/awesome-claude-skills |

### 03-animasyon-motion

_GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim_ · not: `notlar/a-tasarim-onyuz/03-animasyon-motion.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `animated-component-libraries` | ⭐ | Pre-built animated React component collections combining Magic UI (150+ TypeScript/Tailwind/Motion components) and React Bits (90+ minimal-d… | css, gsap, motion, node, python | ✅ | 68 B | M 89KB | - | freshtechbro/claudedesignskills |
| `animejs` | ⭐ | Versatile JavaScript animation engine for DOM, CSS, SVG, and JavaScript objects. Use when creating timeline-based animations, stagger effect… | css, gsap, python, react, vue | ✅ | 68 B | M 62KB | - | freshtechbro/claudedesignskills |
| `framer-motion` | ⭐ | Use when implementing Disney's 12 animation principles with Framer Motion in React applications | motion, react | ✅ | 92 A | S 3KB | claude:ayni | calesthio/OpenMontage |
| `gsap-core` | ⭐ | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, pref… | css, gsap, react, svelte, vue | ✅ | 95 A | M 14KB | claude:ayni | greensock/gsap-skills |
| `gsap-frameworks` | ⭐ | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wa… | gsap, react, svelte, typescript, vue | ✅ | 95 A | M 10KB | claude:farkli | greensock/gsap-skills |
| `gsap-frameworks@calesthio` | alt | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wa… | gsap, react, svelte, vue | ✅ | 92 A | S 6KB | claude:ayni | calesthio/OpenMontage |
| `gsap-performance` | ⭐ | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations,… | css, gsap | ✅ | 97 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-plugins` | ⭐ | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, Scramble… | api-anahtari, canvas, css, gsap, html | ✅ | 95 A | M 21KB | claude:farkli | greensock/gsap-skills |
| `gsap-plugins@calesthio` | alt | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, Scramble… | canvas, css, gsap, html, react | ✅ | 90 A | M 20KB | claude:farkli | calesthio/OpenMontage |
| `gsap-react` | ⭐ | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks … | gsap, next.js, node, react, svelte | ✅ | 97 A | S 6KB | claude:ayni | greensock/gsap-skills |
| `gsap-timeline` | ⭐ | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing k… | gsap, react | ✅ | 97 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-utils` | ⭐ | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks abou… | css, gsap, react | ✅ | 95 A | M 12KB | claude:ayni | greensock/gsap-skills |
| `lottie-animations` | ⭐ | After Effects animation rendering for web and React applications. Use this skill when implementing Lottie animations, JSON vector animations… | canvas, gsap, html, lottie, motion | ✅ | 68 B | M 64KB | - | freshtechbro/claudedesignskills |
| `lottie-bodymovin` | ⭐ | Use when implementing Disney's 12 animation principles with Lottie animations exported from After Effects | lottie, react | ✅ | 92 A | S 4KB | claude:ayni | calesthio/OpenMontage |
| `motion-framer` | ⭐ | Modern animation library for React and JavaScript. Create smooth, production-ready animations with motion components, variants, gestures (ho… | css, gsap, html, motion, next.js | ✅ | 68 B | M 159KB | - | freshtechbro/claudedesignskills |
| `react-spring-physics` | ⭐ | Physics-based animation library combining React Spring (spring dynamics, gesture integration, 60fps animations) and Popmotion (low-level com… | canvas, gsap, python, r3f, react | ✅ | 68 B | M 71KB | - | freshtechbro/claudedesignskills |
| `rive-interactive` | ⭐ | State machine-based vector animation with runtime interactivity and web integration. Use this skill when creating interactive animations, st… | gsap, lottie, motion, node, python | ✅ | 68 B | M 26KB | - | freshtechbro/claudedesignskills |

### 04-scroll-deneyimi

_Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri_ · not: `notlar/a-tasarim-onyuz/04-scroll-deneyimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `barba-js` | ⭐ | Page transitions library for creating fluid, smooth transitions between website pages. Use this skill when implementing page transitions, cr… | css, gsap, html, node, python | ✅ | 68 B | M 129KB | - | freshtechbro/claudedesignskills |
| `gsap-scrolltrigger` | ⭐ | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based a… | gsap, node, react | ✅ | 95 A | M 18KB | claude:ayni | greensock/gsap-skills |
| `gsap-scrolltrigger@freshtechbro` | alt | Comprehensive skill for GSAP (GreenSock Animation Platform) and ScrollTrigger plugin. Use this skill when creating web animations, scroll-dr… | canvas, css, gsap, html, python | ✅ | 68 B | M 159KB | claude:farkli | freshtechbro/claudedesignskills |
| `locomotive-scroll` | ⭐ | Comprehensive skill for Locomotive Scroll smooth scrolling library with parallax effects, viewport detection, and scroll-driven animations. … | css, gsap, html, node, python | ✅ | 68 B | M 81KB | - | freshtechbro/claudedesignskills |
| `scroll-craft` | ⭐ | Build premium scroll-driven landing pages for service, product, food, and drink brands. Plan the visitor journey, page grammar, emotional pe… | api-anahtari, canvas, css, ffmpeg, git | 🟡 | 80 A | M 380KB | - | nateherkai/scroll-craft |
| `scroll-reveal-libraries` | ⭐ | Simple scroll-triggered reveal animations using AOS (Animate On Scroll). Use this skill when building marketing pages, landing pages, or con… | css, gsap, html, next.js, node | ✅ | 68 B | M 94KB | - | freshtechbro/claudedesignskills |

### 05-3d-webgl

_Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader_ · not: `notlar/a-tasarim-onyuz/05-3d-webgl.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `aframe-webxr` | ⭐ | Declarative web framework for building browser-based 3D, VR, and AR experiences using HTML and entity-component architecture. Use this skill… | canvas, gsap, html, node, r3f | ✅ | 65 B | L 176KB | - | freshtechbro/claudedesignskills |
| `babylonjs-engine` | ⭐ | Comprehensive skill for Babylon.js 3D web rendering engine. Use this skill when building real-time 3D experiences, browser-based games, inte… | canvas, gsap, node, r3f, react | ✅ | 65 B | L 153KB | - | freshtechbro/claudedesignskills |
| `blender-web-pipeline` | ⭐ | Blender to web export workflows for 3D models and animations. Use this skill when exporting Blender models to glTF for web, optimizing 3D as… | node, python, r3f, react, three.js | ✅ | 68 B | M 27KB | - | freshtechbro/claudedesignskills |
| `lightweight-3d-effects` | ⭐ | Lightweight 3D effects for decorative elements and micro-interactions using Zdog, Vanta.js, and Vanilla-Tilt.js. Use this skill when adding … | canvas, css, gsap, html, node | ✅ | 66 B | M 179KB | - | freshtechbro/claudedesignskills |
| `playcanvas-engine` | ⭐ | Lightweight WebGL/WebGPU game engine with entity-component architecture and visual editor integration. Use this skill when building browser-… | canvas, html, node, r3f, react | ✅ | 68 B | M 183KB | - | freshtechbro/claudedesignskills |
| `react-three-fiber` | ⭐ | Build declarative 3D scenes with React Three Fiber (R3F) - a React renderer for Three.js. Use when building interactive 3D experiences in Re… | canvas, gsap, html, motion, next.js | ✅ | 68 B | M 105KB | - | freshtechbro/claudedesignskills |
| `spline-interactive` | ⭐ | Browser-based 3D design tool with visual editor, animation, and web export. Use this skill when creating 3D scenes without code, designing i… | canvas, gsap, motion, next.js, node | ✅ | 68 B | M 54KB | - | freshtechbro/claudedesignskills |
| `substance-3d-texturing` | ⭐ | Comprehensive skill for Adobe Substance 3D Painter texturing and material creation workflow. Use this skill when creating PBR materials, exp… | python, r3f, react, three.js, webgl | ✅ | 68 B | M 126KB | - | freshtechbro/claudedesignskills |
| `threejs-animation` | ⭐ | Keyframe, skeletal and morph-target animation, procedural motion and clip blending, on WebGL or with WebGPU and TSL. Use when animating obje… | canvas, node, three.js, webgl | ✅ | 85 A | M 21KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-animation@calesthio` | alt | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF anima… | three.js, webgl | ✅ | 90 A | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-asset-pipeline` | ⭐ | Shrinking glTF assets for three.js with gltf-transform: inspect, validate and optimize commands, Draco, meshopt and quantization, KTX2, WebP… | canvas, node, r3f, react, three.js | ✅ | 85 A | M 18KB | - | CloudAI-X/threejs-skills |
| `threejs-fundamentals` | ⭐ | Three.js scene setup: scenes and fog, cameras, the renderer and tone mapping, the animation loop, object hierarchies, transforms, core math … | canvas, css, html, node, r3f | ✅ | 85 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-fundamentals@calesthio` | alt | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configurin… | canvas, three.js, webgl | ✅ | 90 A | M 11KB | claude:ayni | calesthio/OpenMontage |
| `threejs-geometry` | ⭐ | Creating and shaping three.js geometry: built-in shapes, 3D text, vertex buffers and attributes, merging, instancing, batching, point clouds… | canvas, css, node, three.js, webgl | ✅ | 82 A | L 25KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-geometry@calesthio` | alt | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertice… | three.js, webgl | ✅ | 90 A | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-interaction` | ⭐ | Picking with raycasting, camera controls, transform gizmos, drag, hover and box selection for three.js, identical under WebGL and WebGPU. Us… | canvas, css, r3f, react, three.js | ✅ | 85 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-interaction@calesthio` | alt | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection… | canvas, css, html, three.js, webgl | ✅ | 90 A | M 16KB | claude:ayni | calesthio/OpenMontage |
| `threejs-lighting` | ⭐ | Light types and physical units, shadow maps, HDR environment lighting, light probes, and lighting performance, on WebGL or with WebGPU and T… | canvas, node, three.js, webgl | ✅ | 85 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-lighting@calesthio` | alt | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing l… | three.js, webgl | ✅ | 90 A | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-loaders` | ⭐ | Loading three.js assets: glTF with Draco, meshopt and KTX2 compression, other model formats, textures, HDR and EXR environments, progress, c… | canvas, html, node, three.js, webgl | ✅ | 85 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-loaders@calesthio` | alt | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing… | node, three.js, webgl | ✅ | 90 A | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-materials` | ⭐ | Choosing and configuring three.js materials - unlit, diffuse, specular, PBR, toon, point and line materials - shared properties like blendin… | canvas, node, three.js, webgl | ✅ | 82 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-materials@calesthio` | alt | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating cust… | three.js, webgl | ✅ | 90 A | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-performance` | ⭐ | Measuring and optimizing three.js speed: render statistics, memory counters, fewer draw calls via merging, instancing, batching and LOD, fil… | canvas, three.js, webgl | ✅ | 82 A | L 25KB | - | CloudAI-X/threejs-skills |
| `threejs-postprocessing` | ⭐ | Three.js post-processing: composer pass chains, built-in renderer effects, and the WebGPU/TSL node pipeline — bloom, depth of field, ambient… | canvas, css, node, three.js, webgl | ✅ | 82 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-postprocessing@calesthio` | alt | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creatin… | node, three.js, webgl | ✅ | 90 A | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-react-three-fiber` | ⭐ | Building three.js scenes from React with React Three Fiber and drei: renderer setup, the scene graph as JSX, frame-loop, state and loading h… | canvas, html, node, r3f, react | ✅ | 82 A | L 29KB | - | CloudAI-X/threejs-skills |
| `threejs-shaders` | ⭐ | Custom GLSL vertex and fragment shaders: uniforms, varyings, shader chunks, extending built-in materials, instanced attributes, plus the sam… | canvas, node, three.js, webgl | ✅ | 82 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-shaders@calesthio` | alt | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing frag… | three.js, webgl | ✅ | 90 A | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-textures` | ⭐ | Three.js textures: image loading, color spaces, UV channels and transforms, texture types from canvas to HDR and KTX2, render targets, textu… | canvas, html, node, three.js, webgl | ✅ | 85 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-textures@calesthio` | alt | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, H… | canvas, three.js, webgl | ✅ | 90 A | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-webgl` | ⭐ | Comprehensive skill for Three.js 3D web development. Use this skill when building interactive 3D scenes, WebGL/WebGPU applications, product … | canvas, gsap, html, python, r3f | ✅ | 68 B | M 62KB | - | freshtechbro/claudedesignskills |
| `threejs-world-generation` | ⭐ | Build deterministic, editable, free-viewpoint Three.js worlds from text or structured briefs. Use for cinematic 3D terrain, semantic regions… | ffmpeg, python, three.js | ✅ | 90 A | M 16KB | claude:ayni | calesthio/OpenMontage |
| `web3d-integration-patterns` | ⭐ | Meta-skill for combining Three.js, GSAP ScrollTrigger, React Three Fiber, Motion, and React Spring for complex 3D web experiences. Use when … | canvas, gsap, html, motion, python | ✅ | 68 B | M 21KB | - | freshtechbro/claudedesignskills |

### 06-oyun-2d-grafik

_Oyun geliştirme, PixiJS, 2D grafik_ · not: `notlar/a-tasarim-onyuz/06-oyun-2d-grafik.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `2d-games` | ⭐ | 2D game development principles. Sprites, tilemaps, physics, camera. |  | ✅ | 89 A | S 2KB | - | vudovn/ag-kit |
| `3d-games` | ⭐ | 3D game development principles. Rendering, shaders, physics, cameras. | webgl | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `game-art` | ⭐ | Game art principles. Visual style selection, asset pipeline, animation workflow. |  | ✅ | 89 A | S 5KB | - | vudovn/ag-kit |
| `game-audio` | ⭐ | Game audio principles. Sound design, music integration, adaptive audio systems. |  | ✅ | 89 A | S 5KB | - | vudovn/ag-kit |
| `game-design` | ⭐ | Game design principles. GDD structure, balancing, player psychology, progression. |  | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `game-development` | ⭐ | Game development orchestrator. Routes to platform-specific skills based on project needs. | webgl | ✅ | 89 A | S 35KB | - | vudovn/ag-kit |
| `mobile-games` | ⭐ | Mobile game development principles. Touch input, battery, performance, app stores. |  | ✅ | 89 A | S 2KB | - | vudovn/ag-kit |
| `multiplayer` | ⭐ | Multiplayer game development principles. Architecture, networking, synchronization. |  | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `pc-games` | ⭐ | PC and console game development principles. Engine selection, platform features, optimization strategies. | webgl | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `pixijs-2d` | ⭐ | Fast, lightweight 2D rendering engine for creating interactive graphics, particle effects, and canvas-based applications using WebGL/WebGPU.… | canvas, gsap, r3f, react, three.js | ✅ | 68 B | M 253KB | - | freshtechbro/claudedesignskills |
| `vr-ar` | ⭐ | VR/AR development principles. Comfort, interaction, performance requirements. |  | ✅ | 89 A | S 2KB | - | vudovn/ag-kit |
| `web-games` | ⭐ | Web browser game development principles. Framework selection, WebGPU, optimization, PWA. | canvas, three.js, webgl | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |

### 07-gorsel-sanat-sunum

_Poster/canvas tasarımı, generative art, slayt, GIF_ · not: `notlar/a-tasarim-onyuz/07-gorsel-sanat-sunum.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `algorithmic-art` | ⭐ | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art … | canvas, html, next.js | ✅ | 86 A | M 58KB | - | anthropics/skills |
| `artifacts-builder` | ⭐ | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | css, html, node, playwright, react | ✅ | 88 A | S 45KB | - | ComposioHQ/awesome-claude-skills |
| `canvas-design` | ⭐ | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a pos… | canvas | ✅ | 86 A | M 5424KB | - | anthropics/skills |
| `canvas-design@composiohq` | alt | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a pos… | canvas | ✅ | 86 A | M 5424KB | - | ComposioHQ/awesome-claude-skills |
| `d3-viz` | ⭐ | Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geogr… | canvas, html, node, react, svelte | ✅ | 90 A | M 80KB | claude:ayni | calesthio/OpenMontage |
| `image-enhancer` | ⭐ | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for pr… |  | ✅ | 88 A | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `slack-gif-creator` | ⭐ | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use … | python | ✅ | 88 A | S 43KB | - | anthropics/skills |
| `slack-gif-creator@composiohq` | alt | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill… | python | ✅ | 86 A | M 208KB | - | ComposioHQ/awesome-claude-skills |
| `slides` | ⭐ | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. | api-anahtari, html | ✅ | 95 A | S 19KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `web-artifacts-builder` | ⭐ | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | css, html, node, playwright, react | ✅ | 88 A | S 45KB | - | anthropics/skills |

### 08-onyuz-test-kalite

_Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı_ · not: `notlar/a-tasarim-onyuz/08-onyuz-test-kalite.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `browser-testing-with-devtools` | ⭐ | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect… | api-anahtari, css, html, node, react | ✅ | 91 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `playwright-component-testing` | ⭐ | Set up component testing with Playwright using a story gallery — scaffold stories and a gallery dev page driven by the built-in mount fixtur… | css, html, next.js, node, playwright | ✅ | 98 A | M 38KB | - | microsoft/playwright |
| `playwright-trace` | ⭐ | Inspect Playwright trace files from the command line — list actions, view requests, console, errors, snapshots and screenshots. | html, node, playwright | ✅ | 100 A | S 5KB | - | microsoft/playwright |
| `react-doctor` | ⭐ | Use when finishing a feature, fixing a bug, before committing React code, or when the user types `/doctor`, asks to scan, triage, or clean u… | node, react | ✅ | 92 A | S 3KB | - | darkroomengineering/satus |
| `webapp-testing` | ⭐ | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI be… | css, html, node, playwright, python | ✅ | 88 A | S 22KB | - | anthropics/skills |
| `webapp-testing@composiohq` | alt | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI be… | css, html, node, playwright, python | ✅ | 88 A | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `webapp-testing@vudovn` | alt | Web application testing principles. E2E, Playwright, deep audit strategies. | playwright, python, typescript | ✅ | 89 A | S 10KB | - | vudovn/ag-kit |

## Yazılım Geliştirme

### 01-planlama-metodoloji

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_ · not: `notlar/b-yazilim-gelistirme/01-planlama-metodoloji.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `app-builder` | ⭐ | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tec… | next.js, node, python, react, vue | ✅ | 89 A | S 63KB | - | vudovn/ag-kit |
| `brainstorming` | ⭐ | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning a… | react | ✅ | 91 A | M 72KB | - | obra/superpowers |
| `brainstorming@vudovn` | alt | Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress… |  | ✅ | 89 A | S 17KB | - | vudovn/ag-kit |
| `constraint-driven-development` | ⭐ | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matt… | git, node, python | ✅ | 91 A | M 31KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `doubt-driven-development` | ⭐ | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examine… | api-anahtari | ✅ | 91 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `executing-plans` | ⭐ | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or… | git, node | ✅ | 89 A | M 23KB | - | obra/superpowers |
| `idea-refine` | ⭐ | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, whe… |  | 🟡 | 86 A | M 40KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `incremental-implementation` | ⭐ | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or w… | git, node, typescript | ✅ | 91 A | M 9KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `interview-me` | ⭐ | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview un… | react | ✅ | 91 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `plan-writing` | ⭐ | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any… | node, python, react, tailwind, typescript | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `planning-and-task-breakdown` | ⭐ | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a t… | typescript | ✅ | 91 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `source-driven-development` | ⭐ | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before im… | api-anahtari, css, html, next.js, node | ✅ | 91 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `spec-driven-development` | ⭐ | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when draft… | node, react | ✅ | 91 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `templates` | ⭐ | Project scaffolding templates for new applications. Use when creating new projects from scratch. Contains 13 templates for various tech stac… | next.js, node, python, react, vue | ✅ | 89 A | S 43KB | - | vudovn/ag-kit |
| `writing-plans` | ⭐ | Use when you have a spec or requirements for a multi-step task, before touching code | git, python | ✅ | 91 A | M 10KB | - | obra/superpowers |

### 02-kod-kalitesi-review

_Code review, sadeleştirme, temiz kod_ · not: `notlar/b-yazilim-gelistirme/02-kod-kalitesi-review.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `archify-review` | ⭐ | Review Archify issues, PRs, or code through value, cost, and impact to support evidence-based maintenance decisions. Use for issue triage, c… |  | ✅ | 91 A | S 2KB | - | tt-a1i/archify |
| `archify-tuning` | ⭐ | Improve Archify diagram accuracy, visual quality and complete authoring speed with fewer repairs. Use for generation experiments or evaluati… | node | ✅ | 89 A | M 57KB | - | tt-a1i/archify |
| `clean-code` | ⭐ | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments | playwright, python, typescript | ✅ | 89 A | S 7KB | - | vudovn/ag-kit |
| `code-review-and-quality` | ⭐ | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use … | node, typescript | ✅ | 91 A | M 20KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `code-review-checklist` | ⭐ | Code review guidelines covering code quality, security, and best practices. | typescript | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `code-review-graph` | ⭐ | Token-efficient code review using Tree-sitter AST graphs and MCP. Cuts AI token usage on large codebases by computing the blast radius of ch… | api-anahtari, git, next.js, node, python | ✅ | 87 A | M 11KB | - | vudovn/ag-kit |
| `code-simplification` | ⭐ | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, mai… | git, python, react, typescript | ✅ | 91 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `lint-and-validate` | ⭐ | Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and proje… | node, python, typescript | ✅ | 89 A | S 16KB | - | vudovn/ag-kit |
| `pragmatic-review` | ⭐ | Interactive pragmatic code review focusing on YAGNI and KISS principles. Use when the user asks for a code review, wants to check for over-e… | git, html, typescript | ✅ | 70 B | M 11KB | - | heyitsnoah/claudesidian |
| `receiving-code-review` | ⭐ | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable -… |  | ✅ | 93 A | S 6KB | - | obra/superpowers |
| `requesting-code-review` | ⭐ | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | git | ✅ | 93 A | S 9KB | - | obra/superpowers |
| `simplify-code` | ⭐ | Reduce complexity of over-engineered code. Identify unnecessary abstractions, remove dead code, flatten deep nesting, and simplify logic whi… | git, node, typescript | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `simplify-codebase` | ⭐ | Simplification audit or authorized codebase simplification whose stated objective is to remove accidental complexity. Use for evidence-backe… |  | ✅ | 93 A | S 27KB | - | tt-a1i/archify |

### 03-test-hata-ayiklama

_TDD, hata ayıklama, doğrulama_ · not: `notlar/b-yazilim-gelistirme/03-test-hata-ayiklama.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `debugging-and-error-recovery` | ⭐ | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match exp… | git, node, typescript | ✅ | 91 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `systematic-debugging` | ⭐ | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | git | ✅ | 91 A | M 40KB | - | obra/superpowers |
| `systematic-debugging@heyitsnoah` | alt | ALWAYS use before attempting any fix. Never jump to solutions - investigate root cause first. Use when encountering any technical issue, bug… | git, node, typescript | ✅ | 70 B | M 13KB | - | heyitsnoah/claudesidian |
| `systematic-debugging@vudovn` | alt | 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues. | git, typescript | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `tdd-workflow` | ⭐ | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |  | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `test-driven-development` | ⭐ | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. … | api-anahtari, css, html, node, playwright | ✅ | 91 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `test-driven-development@obra` | alt | Use when implementing any feature or bugfix, before writing implementation code | node, typescript | ✅ | 91 A | M 17KB | claude:farkli,agents:farkli | obra/superpowers |
| `test-value` | ⭐ | Improve test value and feedback cost when auditing slow, flaky, redundant or brittle tests; choosing tests during implementation; or reviewi… |  | ✅ | 91 A | M 19KB | - | tt-a1i/archify |
| `testing-patterns` | ⭐ | Testing patterns and principles. Unit, integration, mocking strategies. |  | ✅ | 89 A | S 10KB | - | vudovn/ag-kit |
| `verification-before-completion` | ⭐ | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and … |  | ✅ | 93 A | S 4KB | - | obra/superpowers |
| `verify-changes` | ⭐ | Prove code works by running it, not just checking it exists. Verification through execution rather than inspection. Use after writing or mod… | node, python | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |

### 04-mimari-api-veritabani

_Mimari, API/arayüz tasarımı, veritabanı, backend_ · not: `notlar/b-yazilim-gelistirme/04-mimari-api-veritabani.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `api-and-interface-design` | ⭐ | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or Graph… | typescript | ✅ | 91 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `api-patterns` | ⭐ | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. | api-anahtari, python, typescript | ✅ | 89 A | S 20KB | - | vudovn/ag-kit |
| `architecture` | ⭐ | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisi… |  | ✅ | 89 A | S 12KB | - | vudovn/ag-kit |
| `bash-linux` | ⭐ | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. | node | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `database-design` | ⭐ | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |  | ✅ | 89 A | S 13KB | - | vudovn/ag-kit |
| `frontend-architecture` | ⭐ | How to organize frontend code — separation of concerns (UI / logic / data / type), file responsibility, state tiers, API services, schema va… | api-anahtari, next.js, react, tailwind, typescript | ✅ | 85 A | M 8KB | - | vudovn/ag-kit |
| `frontend-ui-engineering` | ⭐ | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components,… | api-anahtari, css, react, tailwind, typescript | ✅ | 91 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `nextjs-react-expert` | ⭐ | React and Next.js performance optimization from Vercel Engineering. Use when building React components, optimizing performance, eliminating … | next.js, python, react, typescript | ✅ | 87 A | M 111KB | - | vudovn/ag-kit |
| `nodejs-best-practices` | ⭐ | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not c… | next.js, node, playwright, react, typescript | ✅ | 87 A | M 8KB | - | vudovn/ag-kit |
| `powershell-windows` | ⭐ | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. | api-anahtari | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `python-patterns` | ⭐ | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not… | api-anahtari, python | ✅ | 87 A | M 9KB | - | vudovn/ag-kit |
| `rust-pro` | ⭐ | Master modern Rust (2024 edition) with async patterns, advanced type system features, and production-ready systems programming. Expert in th… |  | ✅ | 89 A | S 8KB | - | vudovn/ag-kit |
| `vercel-composition-patterns` | ⭐ | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component librarie… | react | ✅ | 92 A | S 49KB | claude:ayni | calesthio/OpenMontage |
| `vercel-react-best-practices` | ⭐ | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refacto… | css, next.js, react | ✅ | 92 A | S 207KB | claude:ayni | calesthio/OpenMontage |

### 05-git-pr-surum

_Git, worktree, PR, sürüm/release, changelog_ · not: `notlar/b-yazilim-gelistirme/05-git-pr-surum.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `changelog-generator` | ⭐ | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical … | git | ✅ | 88 A | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `deprecation-and-migration` | ⭐ | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to ano… | node, typescript | ✅ | 91 A | M 12KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `finishing-a-development-branch` | ⭐ | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | git, node | ✅ | 93 A | S 8KB | - | obra/superpowers |
| `git-workflow-and-versioning` | ⭐ | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitt… | api-anahtari, git, next.js, node, typescript | ✅ | 91 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `git-worktrees` | ⭐ | Work with git worktrees for isolated parallel development. Use when starting feature work in isolation, when need separate workspace without… | git, node | ✅ | 72 B | S 4KB | - | heyitsnoah/claudesidian |
| `pull-request` | ⭐ | Create a new feature branch, commit changes, push to GitHub, and open a pull request — all in one command. Use when the user asks to open a … | git | ✅ | 72 B | S 5KB | - | heyitsnoah/claudesidian |
| `release` | ⭐ | Automatically bump version, update changelog, commit, tag, and push a new release based on recent changes. Use when the user wants to cut a … | git | ✅ | 72 B | S 6KB | - | heyitsnoah/claudesidian |
| `using-git-worktrees` | ⭐ | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated wo… | git, node, python | ✅ | 93 A | S 7KB | - | obra/superpowers |

### 06-devops-guvenlik-performans

_CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans_ · not: `notlar/b-yazilim-gelistirme/06-devops-guvenlik-performans.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `ci-cd-and-automation` | ⭐ | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates… | api-anahtari, node, playwright, typescript | ✅ | 91 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `deployment-procedures` | ⭐ | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, no… | docker, git | ✅ | 89 A | S 6KB | - | vudovn/ag-kit |
| `observability-and-instrumentation` | ⭐ | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shippin… | api-anahtari, node, typescript | ✅ | 91 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-optimization` | ⭐ | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspec… | css, git, node, react | ✅ | 91 A | M 26KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-profiling` | ⭐ | Performance profiling principles. Measurement, analysis, and optimization techniques. | python | ✅ | 89 A | S 13KB | - | vudovn/ag-kit |
| `red-team-tactics` | ⭐ | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. | api-anahtari | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `security-and-hardening` | ⭐ | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data… | api-anahtari, git, html, node | ✅ | 91 A | M 30KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `server-management` | ⭐ | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not comm… | docker, node | ✅ | 89 A | S 4KB | - | vudovn/ag-kit |
| `shipping-and-launch` | ⭐ | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when… | git, node, react, typescript | ✅ | 91 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `vulnerability-scanner` | ⭐ | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. | api-anahtari, python | ✅ | 89 A | S 35KB | - | vudovn/ag-kit |

### 07-framework-ozel

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_ · not: `notlar/b-yazilim-gelistirme/07-framework-ozel.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `next-bundle-optimizer` | ⭐ | Audit and reduce Next.js browser initial-load work. Use for slow route startup, oversized client bundles, duplicate browser dependencies, or… | next.js, node | ✅ | 98 A | M 15KB | - | vercel/next.js |
| `next-cache-components-adoption` | ⭐ | Turn on Cache Components in a Next.js app and resolve the blocking routes it surfaces. Use when the user wants to enable, adopt, or migrate … | html, next.js, node, playwright, react | ✅ | 95 A | L 40KB | - | vercel/next.js |
| `next-cache-components-optimizer` | ⭐ | Optimize the meaningful UI available immediately from a Next.js route on an initial load (hard navigation) or named client-side navigation (… | next.js, node, playwright, typescript | ✅ | 98 A | M 50KB | - | vercel/next.js |
| `next-dev-loop` | ⭐ | Verify Next.js runtime behavior after editing app code. Use this skill to confirm a change actually works in a running app — not just that i… | next.js, node, react | ✅ | 98 A | M 9KB | - | vercel/next.js |
| `next-partial-prefetching-adoption` | ⭐ | Turn on Partial Prefetching in a Next.js app and work through the insights it surfaces. Use when the user wants to enable or adopt Partial P… | next.js, node, playwright, typescript | ✅ | 95 A | L 35KB | - | vercel/next.js |
| `next-partial-prefetching-optimizer` | ⭐ | Optimize what selected Next.js client navigations include before the click under Partial Prefetching. Use after Cache Components and Partial… | next.js, playwright | ✅ | 98 A | M 26KB | - | vercel/next.js |
| `playwright-cli` | ⭐ | Automate browser interactions, test web pages and work with Playwright tests. | api-anahtari, css, html, node, playwright | ✅ | 96 A | M 68KB | - | microsoft/playwright |

## Doküman ve İçerik

### 01-ofis-dokumanlari

_Word, Excel, PowerPoint, PDF üretme/düzenleme_ · not: `notlar/c-dokuman-icerik/01-ofis-dokumanlari.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `docx` | ⭐ | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Tr… | node, python | ✅ | 88 A | S 1102KB | - | anthropics/skills |
| `docx@composiohq` | alt | Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extract… | node, python, typescript | ✅ | 86 A | M 1158KB | - | ComposioHQ/awesome-claude-skills |
| `pdf` | ⭐ | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining o… | canvas, python | ✅ | 86 A | M 57KB | - | anthropics/skills |
| `pdf@composiohq` | alt | Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms. W… | canvas, python | ✅ | 88 A | S 63KB | - | ComposioHQ/awesome-claude-skills |
| `pptx` | ⭐ | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch… | canvas, node, python, react | ✅ | 86 A | M 1112KB | - | anthropics/skills |
| `pptx@composiohq` | alt | Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for: (1) Creating new presentations… | html, node, playwright, python, react | ✅ | 83 A | L 1201KB | - | ComposioHQ/awesome-claude-skills |
| `xlsx` | ⭐ | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or… | html, python | ✅ | 86 A | M 1077KB | - | anthropics/skills |
| `xlsx@composiohq` | alt | Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. When Clau… | python | ✅ | 86 A | M 18KB | - | ComposioHQ/awesome-claude-skills |

### 02-diyagram-dokumantasyon

_Diyagram, teknik dokümantasyon, ADR, ortak yazım_ · not: `notlar/c-dokuman-icerik/02-diyagram-dokumantasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `archify` | ⭐ | Create validated architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree, timeline, and waterfall diagrams as explora… | canvas, css, html, node | ✅ | 89 A | M 7616KB | - | tt-a1i/archify |
| `beautiful-mermaid` | ⭐ | Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram. | css, html, node, typescript | ✅ | 92 A | S 19KB | claude:ayni | calesthio/OpenMontage |
| `doc-coauthoring` | ⭐ | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical s… |  | ✅ | 86 A | M 15KB | - | anthropics/skills |
| `documentation-and-adrs` | ⭐ | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, w… | git, node, typescript | ✅ | 91 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `documentation-templates` | ⭐ | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. | typescript | ✅ | 87 A | S 3KB | - | vudovn/ag-kit |
| `json-canvas` | ⭐ | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual… | canvas, node, obsidian | ✅ | 70 B | M 14KB | - | heyitsnoah/claudesidian |

### 03-yazi-iletisim-icerik

_Yazı, iletişim, pazarlama/içerik, kariyer_ · not: `notlar/c-dokuman-icerik/03-yazi-iletisim-icerik.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `competitive-ads-extractor` | ⭐ | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative app… |  | ✅ | 88 A | S 8KB | - | ComposioHQ/awesome-claude-skills |
| `content-research-writer` | ⭐ | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real… |  | ✅ | 86 A | M 14KB | - | ComposioHQ/awesome-claude-skills |
| `de-ai-ify` | ⭐ | Remove AI-generated jargon and restore human voice to text. Use when the user asks to de-AI-ify, humanize, remove AI tone, or make text soun… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |
| `developer-growth-analysis` | ⭐ | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant lea… | api-anahtari, css, node, react, typescript | ✅ | 86 A | M 15KB | - | ComposioHQ/awesome-claude-skills |
| `domain-name-brainstormer` | ⭐ | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours… |  | ✅ | 88 A | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `geo-fundamentals` | ⭐ | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). | html, python | ✅ | 89 A | S 14KB | - | vudovn/ag-kit |
| `i18n-localization` | ⭐ | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. | css, next.js, python, react | ✅ | 89 A | S 12KB | - | vudovn/ag-kit |
| `internal-comms` | ⭐ | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use … |  | ✅ | 88 A | S 22KB | - | anthropics/skills |
| `internal-comms@composiohq` | alt | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use … |  | ✅ | 88 A | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `lead-research-assistant` | ⭐ | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionab… |  | ✅ | 88 A | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `meeting-insights-analyzer` | ⭐ | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when… |  | ✅ | 86 A | M 10KB | - | ComposioHQ/awesome-claude-skills |
| `raffle-winner-picker` | ⭐ | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with … |  | ✅ | 88 A | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `seo-fundamentals` | ⭐ | SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles. |  | ✅ | 89 A | S 9KB | - | vudovn/ag-kit |
| `tailored-resume-generator` | ⭐ | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview … | python, react | ✅ | 86 A | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `twitter-algorithm-optimizer` | ⭐ | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engage… |  | ✅ | 86 A | M 13KB | - | ComposioHQ/awesome-claude-skills |

### 04-not-alma-bilgi-yonetimi

_Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni_ · not: `notlar/c-dokuman-icerik/04-not-alma-bilgi-yonetimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `add-frontmatter` | ⭐ | Add or update YAML frontmatter properties to enhance Obsidian note organization. Use when the user asks to add, fix, normalize, or improve f… | obsidian | ✅ | 72 B | S 4KB | - | heyitsnoah/claudesidian |
| `daily-review` | ⭐ | Conduct an end-of-day review to capture progress and set up tomorrow. Use when the user asks for a daily review, end of day wrap-up, EOD not… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |
| `download-attachment` | ⭐ | Download files from URLs to the Obsidian attachments folder and organize them with descriptive names. Use when the user provides URLs to dow… | git, obsidian | ✅ | 72 B | S 3KB | - | heyitsnoah/claudesidian |
| `file-organizer` | ⭐ | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structur… |  | ✅ | 86 A | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `inbox-processor` | ⭐ | Help organize and process items in the 00_Inbox folder according to the PARA method. Use when the user asks to process, clear, sort, triage,… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |
| `init-bootstrap` | ⭐ | Interactive setup wizard that helps new users create a personalized CLAUDE.md file based on their Obsidian workflow preferences. Use when th… | api-anahtari, git, node, obsidian | ✅ | 67 B | L 30KB | - | heyitsnoah/claudesidian |
| `install-claudesidian-command` | ⭐ | Install claudesidian shell command to launch Claude Code from anywhere. Use when the user wants to install a shell alias/launcher for their … | obsidian | 🟡 | 65 B | M 10KB | - | heyitsnoah/claudesidian |
| `invoice-organizer` | ⭐ | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consiste… |  | ✅ | 86 A | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `obsidian-bases` | ⭐ | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating datab… | html, obsidian | ✅ | 70 B | M 16KB | - | heyitsnoah/claudesidian |
| `obsidian-markdown` | ⭐ | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when workin… | css, html, obsidian, python | ✅ | 68 B | M 11KB | - | heyitsnoah/claudesidian |
| `research-assistant` | ⭐ | Conduct thorough research on topics by searching the vault and synthesizing findings. Use when the user asks to research a topic, dig into s… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |
| `thinking-partner` | ⭐ | Act as a collaborative thinking partner for exploring complex problems through questioning, not solutioning. Use when the user wants to thin… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |
| `upgrade` | ⭐ | Intelligently upgrade claudesidian with new features while preserving user customizations using AI-powered semantic analysis. Use when the u… | api-anahtari, git, obsidian, python | 🟡 | 65 B | M 11KB | - | heyitsnoah/claudesidian |
| `weekly-synthesis` | ⭐ | Create a comprehensive synthesis of the week's work and thinking. Use when the user asks for a weekly review, weekly synthesis, week-in-revi… |  | ✅ | 72 B | S 2KB | - | heyitsnoah/claudesidian |

## AI ve Otomasyon

### 01-claude-api-mcp

_Claude API, MCP sunucusu, model geçişi_ · not: `notlar/d-ai-otomasyon/01-claude-api-mcp.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `claude-api` | ⭐ | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model … | api-anahtari, html, python, three.js, typescript | 🟡 | 76 B | L 2031KB | - | anthropics/skills |
| `claude-opus-4-5-migration` | ⭐ | Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants to update their codebase, prom… | python | ✅ | 88 A | S 12KB | - | anthropics/claude-code |
| `connect` | ⭐ | Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Noti… | api-anahtari, node, python, typescript | ✅ | 88 A | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `connect-apps` | ⭐ | Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, … | api-anahtari | 🟡 | 83 A | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `langsmith-fetch` | ⭐ | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating er… | api-anahtari, node, python | ✅ | 86 A | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder` | ⭐ | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-design… | node, python, typescript | ✅ | 86 A | M 119KB | - | anthropics/skills |
| `mcp-builder@composiohq` | alt | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-design… | api-anahtari, node, python, typescript | ✅ | 86 A | M 144KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder@vudovn` | alt | MCP (Model Context Protocol) server and client engineering. Protocol design, schemas, transports, extensions, security, and migration. |  | ✅ | 87 A | M 10KB | - | vudovn/ag-kit |
| `mcp-integration` | ⭐ | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model… | api-anahtari, git, node, python | 🔵 | 74 B | M 46KB | - | anthropics/claude-code |

### 02-agent-orkestrasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_ · not: `notlar/d-ai-otomasyon/02-agent-orkestrasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `batch-operations` | ⭐ | Apply operations across multiple files simultaneously. Pattern-based bulk modifications, search-and-replace across codebases, consistent cha… | git, node, typescript | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `behavioral-modes` | ⭐ | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. | node, typescript | ✅ | 89 A | S 6KB | - | vudovn/ag-kit |
| `context-compression` | ⭐ | Manage and compress conversation context in long sessions. Detect when context is growing large, summarize completed work phases, archive ol… | api-anahtari, next.js, typescript | ✅ | 89 A | S 5KB | - | vudovn/ag-kit |
| `context-engineering` | ⭐ | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when yo… | api-anahtari, css, git, node, react | ✅ | 91 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `coordinator-mode` | ⭐ | Advanced multi-agent orchestration with parallel workers, synthesis protocols, and coordinator lifecycle. Use when complex tasks require mul… | api-anahtari, typescript | ✅ | 89 A | S 8KB | - | vudovn/ag-kit |
| `diagnosing-superpowers` | ⭐ | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a… | api-anahtari | ✅ | 93 A | S 41KB | - | obra/superpowers |
| `discernment-nudge` | ⭐ | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, p… | html | ✅ | 86 A | M 21KB | - | anthropics/skills |
| `dispatching-parallel-agents` | ⭐ | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | typescript | ✅ | 93 A | S 6KB | - | obra/superpowers |
| `intelligent-routing` | ⭐ | Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the best specialist agent(s) withou… | api-anahtari, css, docker, html, node | ✅ | 87 A | M 11KB | - | vudovn/ag-kit |
| `memory-system` | ⭐ | Persistent cross-session memory management. Enables agents to remember user preferences, project conventions, and past decisions across diff… | api-anahtari, git, node, tailwind | ✅ | 89 A | S 6KB | - | vudovn/ag-kit |
| `parallel-agents` | ⭐ | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analys… | react | ✅ | 89 A | S 6KB | - | vudovn/ag-kit |
| `subagent-driven-development` | ⭐ | Use when executing implementation plans with independent tasks in the current session | api-anahtari, git | ✅ | 86 A | L 58KB | - | obra/superpowers |
| `using-agent-skills` | ⭐ | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of … | git | ✅ | 91 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `using-superpowers` | ⭐ | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarif… | git | ✅ | 93 A | S 20KB | - | obra/superpowers |

### 03-web-arastirma-veri

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_ · not: `notlar/d-ai-otomasyon/03-web-arastirma-veri.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `agent-reach` | ⭐ | MUST USE when user wants to 调研/research/搜索/search/查/找/look up anything on the internet — e.g. 全网调研 X / 帮我调研一下 X / 查一下 X / 搜搜 X / 看看大家怎么评价 X … | api-anahtari | ✅ | 91 A | M 46KB | - | Panniantong/Agent-Reach |
| `notebooklm` | ⭐ | Install, authenticate, troubleshoot, and operate Gemini Notebook through the notebooklm-py CLI or typed async Python API. Use for notebook a… | api-anahtari, python | ✅ | 88 A | M 16KB | claude:farkli | teng-lin/notebooklm-py |
| `youtube-downloader` | ⭐ | Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube v… | python | ✅ | 88 A | S 7KB | - | ComposioHQ/awesome-claude-skills |

### 04-skill-plugin-yazimi

_Skill yazma, plugin/hook/komut geliştirme_ · not: `notlar/d-ai-otomasyon/04-skill-plugin-yazimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `academy-guide` | ⭐ | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching cour… |  | ✅ | 86 A | S 19KB | - | anthropics/skills |
| `agent-development` | ⭐ | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use des… |  | 🔵 | 74 B | M 69KB | - | anthropics/claude-code |
| `command-development` | ⭐ | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command argumen… | git, node, typescript | 🔵 | 74 B | M 150KB | - | anthropics/claude-code |
| `hook-development` | ⭐ | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement p… | react | 🔵 | 74 B | M 63KB | - | anthropics/claude-code |
| `plugin-settings` | ⭐ | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md f… | api-anahtari, git, typescript | 🔵 | 74 B | M 43KB | - | anthropics/claude-code |
| `plugin-structure` | ⭐ | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin comp… | api-anahtari, node, python | 🔵 | 74 B | M 73KB | - | anthropics/claude-code |
| `skill-creator` | ⭐ | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, ed… | api-anahtari, html, node, python | ✅ | 83 A | L 220KB | - | anthropics/skills |
| `skill-creator@composiohq` | alt | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that exte… | api-anahtari, html, python, react | ✅ | 86 A | M 38KB | - | ComposioHQ/awesome-claude-skills |
| `skill-creator@freshtechbro` | alt | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that exte… | api-anahtari, html, python, react | ✅ | 68 B | M 41KB | - | freshtechbro/claudedesignskills |
| `skill-creator@heyitsnoah` | alt | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, ed… | api-anahtari, html, node, python | ✅ | 67 B | L 221KB | - | heyitsnoah/claudesidian |
| `skill-development` | ⭐ | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description"… | api-anahtari, html, python, react | 🔵 | 74 B | M 34KB | - | anthropics/claude-code |
| `skill-share` | ⭐ | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery… | python | ✅ | 88 A | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `skillify` | ⭐ | Auto-create new skills from repetitive workflows. When you notice yourself doing the same multi-step process repeatedly, extract it into a r… | tailwind | ✅ | 89 A | S 3KB | - | vudovn/ag-kit |
| `template-skill` | ⭐ | Replace with description of the skill and when Claude should use it. |  | ✅ | 88 A | S 0KB | - | ComposioHQ/awesome-claude-skills |
| `writing-hookify-rules` | ⭐ | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or … | api-anahtari, python, typescript | 🔵 | 74 B | M 8KB | - | anthropics/claude-code |
| `writing-skills` | ⭐ | Use when creating new skills, editing existing skills, or verifying skills work before deployment | api-anahtari, git, node, python, react | ✅ | 86 A | L 105KB | - | obra/superpowers |

## Video, Ses ve AI Medya Üretimi

### 01-video-uretim-montaj

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_ · not: `notlar/g-video-ses-medya/01-video-uretim-montaj.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `captions-overlay` | ⭐ | Overlay doctrine for the embedded-captions workflow — the caption MODEL (drop / rail / embed) and the rule that captions are an OVERLAY comp… | canvas | ✅ | 94 A | S 6KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `changelog-video` | ⭐ | Turn a weekly changelog .md into a finished branded changelog video (square 1080, ~45-60s, Annie VO, animated brand background, mock-UI visu… | api-anahtari, ffmpeg, gsap, html, node | ✅ | 92 A | M 521KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `create-video` | ⭐ birincil | HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Ö… | heygen, api-anahtari, rest-api | ✅ | 87 A | S 92KB | claude:ayni | calesthio/OpenMontage |
| `embedded-captions` | ⭐ | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cin… | canvas, css, ffmpeg, gsap, html | 🟡 | 82 A | L 3421KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `faceless-explainer` | ⭐ | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the … | api-anahtari, canvas, html, node | 🟡 | 82 A | L 284KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `ffmpeg` | ⭐ tamamlayıcı | FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar… | ffmpeg | ✅ | 86 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `figma` | ⭐ | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion … | api-anahtari, css, gsap, html, motion | 🟡 | 85 A | M 23KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `general-video` | ⭐ | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or … | api-anahtari, canvas, css, html, node | 🟡 | 85 A | M 36KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes` | ⭐ | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, incl… | api-anahtari, canvas, css, gsap, html | 🟡 | 87 A | M 156KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-animation` | ⭐ | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techni… | canvas, css, gsap, html, lottie | 🟡 | 87 A | M 1240KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-animation@calesthio` | alt tamamlayıcı | HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri ve GSAP, Lottie, T… | hyperframes, gsap, html, css, lottie, three.js | ✅ | 95 A | S 2521KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-audio` | ⭐ | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume auto… | ffmpeg, gsap, html, node, typescript | 🟡 | 84 A | L 100KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-cli` | ⭐ | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present… | api-anahtari, canvas, docker, ffmpeg, html | 🟡 | 84 A | L 128KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-cli@calesthio` | alt tamamlayıcı | HyperFrames CLI geliştirme döngüsü: init, add, lint, validate, inspect, preview, render, AWS Lambda render ve sorun giderme. Render öncesi l… | hyperframes, node, ffmpeg, docker, aws-lambda | ✅ | 86 A | M 54KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-core` | ⭐ | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="… | canvas, css, gsap, html, lottie | 🟡 | 87 A | M 98KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-core@calesthio` | alt birincil | HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönetti… | hyperframes, html, gsap | ✅ | 95 A | S 78KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-creative` | ⭐ | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narratio… | api-anahtari, css, gsap, html, python | 🟡 | 89 A | S 1176KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-creative@calesthio` | alt tamamlayıcı | HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, s… | hyperframes, html, css | ✅ | 95 A | S 1000KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-keyframes` | ⭐ | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, … | canvas, css, gsap, node, three.js | 🟡 | 87 A | M 23KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-media` | ⭐ tamamlayıcı | Tek ses motoru (scripts/audio.mjs) ile HyperFrames için TTS (HeyGen/ElevenLabs/Kokoro), arka plan müziği, ses efekti, Whisper transkripsiyon… | hyperframes, node, heygen, elevenlabs, whisper | ✅ | 86 A | M 1396KB | claude:ayni | calesthio/OpenMontage |
| `hyperframes-registry` | ⭐ | Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever… | canvas, css, gsap, html, node | 🟡 | 87 A | M 79KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-registry@calesthio` | alt tamamlayıcı | HyperFrames kayıt defterindeki hazır blok ve bileşenleri 'hyperframes add' ile kurar ve ana kompozisyona bağlar; yeni blok/bileşen yazıp üst… | hyperframes, html, node | ✅ | 87 A | S 49KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-studio` | ⭐ | Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose i… | canvas, css, html, typescript | 🟡 | 87 A | M 11KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes@calesthio` | alt birincil | HTML'den video render eden HyperFrames'in giriş ve yönlendirme skill'i: alt skillerin (core, animation, creative, media, cli, registry) hari… | hyperframes, html, gsap, node | ✅ | 94 A | M 20KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `media-use` | ⭐ | Agent Media OS for a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or … | api-anahtari, css, node, webgl | 🟡 | 87 A | M 1806KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `media-use@calesthio` | alt birincil | BGM, ses efekti, görsel ve ikon ihtiyacını tek 'resolve' komutuyla HeyGen kataloğunda arayıp indirir, yerelde dondurur ve manifest'e kaydede… | node, heygen, api-anahtari | ✅ | 87 A | S 66KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `music-to-video` | ⭐ | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric vide… | canvas, gsap, html, node, python | 🟡 | 87 A | M 6081KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `music-to-video@calesthio` | alt tamamlayıcı | Bir müzik parçasından vuruşa senkron HyperFrames videosu üretir: parçayı tek analizörle (beatgrid) çözümler, kareleri planlar, her kareyi ay… | hyperframes, python, html, gsap | ✅ | 86 A | M 6053KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `oversized-cursor` | ⭐ | House-style oversized macOS cursor technique for HyperFrames launch videos. Load whenever a scene involves cursors or a pointer-led action, … | css, gsap | ✅ | 94 A | S 6KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `playwright-recording` | ⭐ birincil | Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün tur… | playwright, typescript, node | ✅ | 86 A | M 20KB | claude:ayni | calesthio/OpenMontage |
| `pr-to-video` | ⭐ | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feat… | api-anahtari, canvas, html, node | 🟡 | 84 A | L 358KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `product-launch-video` | ⭐ | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, … | api-anahtari, canvas, ffmpeg, html, node | 🟡 | 84 A | L 341KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `remotion` | ⭐ alternatif | claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch,… | remotion, react, typescript | ✅ | 71 B | S 16KB | claude:ayni | calesthio/OpenMontage |
| `remotion-best-practices` | ⭐ alternatif | Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile m… | remotion, react, typescript | ✅ | 94 A | S 112KB | claude:farkli,agents:farkli | calesthio/OpenMontage |
| `remotion-to-hyperframes` | ⭐ | Port an existing Remotion (React) composition''s source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a… | css, gsap, html, lottie, node | 🟡 | 87 A | M 176KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `remotion-to-hyperframes@calesthio` | alt tamamlayıcı | Mevcut bir Remotion (React) kompozisyonunu HyperFrames HTML'ine taşır; eşlenebilen kalıpları çevirir, useState/useEffect gibi uyumsuz kalıpl… | remotion, hyperframes, react, html, gsap | ✅ | 86 A | M 168KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `slideshow` | ⭐ | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot … | api-anahtari, canvas, css, gsap, html | 🟡 | 84 A | L 76KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `synthetic-screen-recording` | ⭐ alternatif | Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter ka… | remotion, react, typescript | ✅ | 78 B | M 10KB | claude:ayni | calesthio/OpenMontage |
| `talking-head-recut` | ⭐ | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data… | api-anahtari, canvas, css, ffmpeg, gsap | 🟡 | 84 A | L 509KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `video-download` | ⭐ birincil | yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonları… | yt-dlp, ffmpeg | ✅ | 87 A | S 3KB | claude:ayni | calesthio/OpenMontage |
| `video-edit` | ⭐ birincil | ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, form… | ffmpeg | ✅ | 95 A | S 12KB | claude:ayni | calesthio/OpenMontage |
| `video-toolkit` | ⭐ alternatif | claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan ka… | remotion, python, node, modal, runpod | ✅ | 70 B | M 15KB | claude:ayni | calesthio/OpenMontage |
| `video-translate` | ⭐ birincil | HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve w… | heygen, api-anahtari, rest-api | ✅ | 86 A | M 11KB | claude:ayni | calesthio/OpenMontage |
| `video-understand` | ⭐ birincil | ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gere… | ffmpeg, python, whisper | ✅ | 87 A | S 27KB | claude:ayni | calesthio/OpenMontage |
| `website-to-video` | ⭐ tamamlayıcı | Bir web sitesini headless Chrome ile yakalayıp marka varlıklarıyla HyperFrames videosuna (site turu, vitrin, sosyal klip) dönüştüren 7 adıml… | hyperframes, html, node, chrome-headless | ✅ | 85 A | M 1541KB | claude:ayni | calesthio/OpenMontage |

### 02-ses-muzik-konusma

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_ · not: `notlar/g-video-ses-medya/02-ses-muzik-konusma.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `acestep` | ⭐ alternatif | ACE-Step 1.5 açık kaynak modeliyle RunPod üzerinde enstrümantal müzik, sözlü şarkı, cover/stil aktarımı ve stem ayırma yapar; sahne ön ayarl… | python, runpod, ffmpeg | ✅ | 70 B | M 9KB | claude:ayni | calesthio/OpenMontage |
| `agents` | ⭐ birincil | ElevenLabs Agents Platform ile gerçek zamanlı sesli yapay zekâ ajanı (asistan, müşteri hizmetleri botu, etkileşimli karakter) kurar; CLI, Py… | elevenlabs, python, typescript, api-anahtari | ✅ | 86 A | M 64KB | claude:ayni | calesthio/OpenMontage |
| `azure-speech-to-text` | ⭐ alternatif | Azure AI Speech Fast Transcription REST API ile ses/videoyu kelime zaman damgalı, konuşmacı ayrımlı yazıya döker; OpenMontage'da azure_stt a… | azure, python, api-anahtari | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `azure-text-to-speech` | ⭐ alternatif | Azure nöral TTS ile SSML prozodi ve konuşma stili kontrollü çok dilli seslendirme üretir; OpenMontage'da azure_tts aracı olarak tts_selector… | azure, python, ssml, api-anahtari | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `dashscope` | ⭐ alternatif | Alibaba DashScope (Bailian) entegrasyonu: Qwen-Image ile görsel üretimi, Qwen-TTS ile seslendirme ve kelime zaman damgalı Qwen-ASR transkrip… | dashscope, python, api-anahtari | ✅ | 79 B | S 6KB | claude:ayni | calesthio/OpenMontage |
| `doubao-tts` | ⭐ alternatif | Volcengine Doubao Speech 2.0 ile Mandarin ve çok dilli seslendirme üretir; asenkron uç noktadan karakter düzeyinde zaman damgası alıp altyaz… | volcengine, python, api-anahtari | ✅ | 79 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `elevenlabs` | ⭐ birincil | ElevenLabs ile seslendirme, ses klonlama, ses efekti ve müzik üretimini tek skillde toplar; model seçimi, stile göre ses ayarları, duraklama… | elevenlabs, python, ffmpeg, api-anahtari | ✅ | 94 A | M 16KB | claude:farkli | calesthio/OpenMontage |
| `fish-audio-tts` | ⭐ alternatif | fish.audio S1/S2 modelleriyle duygu etiketli ([laugh], [whispers]) çok dilli seslendirme ve reference_id ile klonlanmış sesleri yeniden kull… | fish-audio, python, api-anahtari | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `lyria` | ⭐ alternatif | Google Lyria 3 ile Gemini Interactions API üzerinden müzik üretir ve doğrular; Clip/Pro/RealTime model seçimi, yapılandırılmış prompt sözleş… | google-gemini, api-anahtari | ✅ | 94 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `music` | ⭐ birincil | ElevenLabs Music API ile metin isteminden enstrümantal parça, sözlü şarkı, jingle üretir; bölüm bazlı ince kontrol için kompozisyon planı ol… | elevenlabs, python, typescript, api-anahtari | ✅ | 95 A | S 10KB | claude:ayni | calesthio/OpenMontage |
| `setup-api-key` | ⭐ birincil | ElevenLabs API anahtarını kurar: önce mevcut ELEVENLABS_API_KEY'i bulup doğrular, yoksa kullanıcıyı adım adım anahtar oluşturmaya yönlendiri… | elevenlabs, api-anahtari | ✅ | 79 B | S 3KB | claude:ayni | calesthio/OpenMontage |
| `sound-effects` | ⭐ birincil | ElevenLabs ile metin tarifinden ses efekti, ambiyans, döngü ve UI sesi üretir; süre, prompt etkisi ve döngü parametrelerini açıklar. | elevenlabs, python, typescript, api-anahtari | ✅ | 95 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `speech-to-text` | ⭐ birincil | ElevenLabs Scribe v2 ile 90+ dilde kelime zaman damgalı, konuşmacı ayrımlı transkripsiyon yapar; anahtar terim ipucu, dil tespiti ve gerçek … | elevenlabs, python, typescript, api-anahtari | ✅ | 94 A | M 40KB | claude:ayni | calesthio/OpenMontage |
| `text-to-speech` | ⭐ alternatif | HeyGen'in Starfish TTS modeliyle bağımsız ses dosyası üretir; ses listeleme, hız/perde kontrolü ve MCP araçlarını tercih etme kuralını içeri… | heygen, api-anahtari, rest-api | ✅ | 86 A | M 10KB | claude:ayni | calesthio/OpenMontage |

### 03-ai-gorsel-video-modelleri

_AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu_ · not: `notlar/g-video-ses-medya/03-ai-gorsel-video-modelleri.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `3d-asset-generation` | ⭐ birincil | OpenMontage dünyaları için üretim kalitesinde 3D varlık üretir/yönlendirir: Atlas Tripo, fal Hunyuan 3D, SAM 3D ve CC0 kataloglar arasından … | blender, three.js, atlas-cloud, fal-ai, api-anahtari | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `ai-video-gen` | ⭐ birincil | Metinden ve görselden AI video üretimini fal.ai, HeyGen ve Gemini API ağ geçitleri üzerinden yönetir; Seedance 2.0'ı premium varsayılan saya… | fal-ai, heygen, google-gemini, api-anahtari | ✅ | 86 A | M 11KB | claude:farkli | calesthio/OpenMontage |
| `atlas-cloud` | ⭐ alternatif | Atlas Cloud ağ geçidiyle tek anahtarla Seedance 2.5/2.0, Gemini Omni, MiniMax H3, Seedream 5, GPT Image 2, Nano Banana 2 görsel/video üretim… | atlas-cloud, python, api-anahtari | ✅ | 87 A | S 5KB | claude:ayni | calesthio/OpenMontage |
| `avatar-video` | ⭐ tamamlayıcı | HeyGen v2 API ile avatar, ses, metin, sahne ve arka plan üzerinde tam kontrollü avatar videosu üretir; çok sahneli, şeffaf WebM ve Remotion … | heygen, api-anahtari, rest-api | ✅ | 87 A | S 177KB | claude:ayni | calesthio/OpenMontage |
| `bfl-api` | ⭐ tamamlayıcı | Black Forest Labs FLUX API entegrasyon rehberi: uç noktalar, bölgesel sunucular, fiyatlar, asenkron sorgulama, hız sınırı, hata yönetimi ve … | bfl-flux, python, typescript, api-anahtari | ✅ | 94 A | M 79KB | claude:ayni | calesthio/OpenMontage |
| `comfyui` | ⭐ birincil | OpenMontage'da ComfyUI iş akışlarıyla (comfyui_image/video/music) yerel üretim: sunucu sözleşmesi, API formatlı iş akışı, output_node seçimi… | comfyui, python, gpu | ✅ | 86 A | M 8KB | claude:ayni | calesthio/OpenMontage |
| `faceswap` | ⭐ birincil | HeyGen FaceswapNode iş akışıyla kaynak görseldeki yüzü hedef videoya aktarır; iş gönderme, durum sorgulama ve TypeScript/Python örnekleri iç… | heygen, api-anahtari, rest-api | ✅ | 79 B | S 7KB | claude:ayni | calesthio/OpenMontage |
| `flux-best-practices` | ⭐ birincil | BFL FLUX görsel modelleri için kapsamlı prompt rehberi: prompt yapısı, model seçimi (klein/pro/max/flex), T2I, I2I, JSON yapılandırılmış pro… | bfl-flux | ✅ | 95 A | S 122KB | claude:ayni | calesthio/OpenMontage |
| `gemini-omni` | ⭐ alternatif | Google Gemini Omni Flash ile 3-10 sn 720p sesli video üretimi ve aynı klibi doğal dille durum korumalı (interaction_id) düzenleme; referans … | google-gemini, api-anahtari | ✅ | 94 A | M 8KB | claude:ayni | calesthio/OpenMontage |
| `grok-media` | ⭐ alternatif | xAI Grok görsel ve video üretimi rehberi: kimlik doğrulama, uç noktalar, görsel düzenleme/birleştirme, referans görselli video, asenkron sor… | xai-grok, api-anahtari | ✅ | 79 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `heygen` | ⭐ alternatif | [KULLANIMDAN KALKMIŞ] HeyGen Video Agent ve v2 avatar iş akışlarını birleştiren eski skill; yerini create-video ve avatar-video aldı, geriye… | heygen, api-anahtari | ✅ | 71 B | S 225KB | claude:ayni | calesthio/OpenMontage |
| `kling-official` | ⭐ alternatif | Kling resmi doğrudan API'si (KLING_API_KEY) için OpenMontage sağlayıcı kuralları: fal.ai Kling'den ayrımı, klasik/turbo görev protokolleri, … | kling, python, api-anahtari | ✅ | 86 A | M 9KB | claude:ayni | calesthio/OpenMontage |
| `ltx2` | ⭐ alternatif | LTX-2.3 22B modeliyle Modal (A100) üzerinde ~5 sn metinden/görselden video üretir; kare sayısı kuralı, çözünürlükler ve sinematik prompt reh… | ltx, modal, python | ✅ | 71 B | S 7KB | claude:ayni | calesthio/OpenMontage |
| `minimax-h3` | ⭐ alternatif | MiniMax H3 (Hailuo 3.0) videosunu resmi API, fal.ai, Runway, ComfyUI Partner Node veya yerel açık ağırlıklarla üretir; rotalar arası model k… | minimax, comfyui, api-anahtari | ✅ | 87 A | S 2KB | claude:ayni | calesthio/OpenMontage |
| `provider-model-refresh` | ⭐ birincil | Eylül 2026 görsel, video, konuşma ve Avatar V adaptörleri (GPT Image 2.5, Gemini 3 Pro Image, Ideogram 4.5, Wan 3.0, LTX-2.5, Eleven v4, Lyr… | openmontage, python, api-anahtari | ✅ | 87 A | S 5KB | - | calesthio/OpenMontage |
| `seedance-2-0` | ⭐ tamamlayıcı | ByteDance Seedance 2.0 için yetkili prompt ve parametre rehberi: tek geçişte senkron ses, tek üretimde çoklu çekim, yönetmen düzeyi kamera k… | seedance, fal-ai, api-anahtari | ✅ | 94 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `seedance-2-5` | ⭐ alternatif | Seedance 2.5 ile 4-30 sn sinematik video: fal.ai, Volcengine Ark, Runway, ComfyUI rotaları; bölümlü prompt sözleşmesi, 'Hard cut' çoklu çeki… | seedance, fal-ai, api-anahtari | ✅ | 94 A | M 23KB | claude:ayni | calesthio/OpenMontage |

### 04-motion-graphics-karakter

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_ · not: `notlar/g-video-ses-medya/04-motion-graphics-karakter.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `canvas-procedural-animation` | ⭐ alternatif | p5.js/Canvas ile karakter destekleyici prosedürel hareket: parçacık, hava efekti, yaprak, squash/stretch ve basit yürüme döngüleri; zaman/ka… | p5js, canvas, javascript | ✅ | 79 B | S 1KB | claude:ayni | calesthio/OpenMontage |
| `character-animation-qa` | ⭐ tamamlayıcı | Karakter animasyonunu sunmadan önce katmanlı kontrol: şema doğrulama, varlık kontrolü, Playwright ile tarayıcı önizleme ve ekran görüntüsü, … | playwright, ffmpeg | ✅ | 79 B | S 2KB | claude:ayni | calesthio/OpenMontage |
| `character-rigging` | ⭐ tamamlayıcı | Yerel 2D karakter animasyonu için veri güdümlü rig paketi: parçalar, pivotlar, katman sırası, kısıtlar ve görünümler; her karakteri jenerik … | svg, gsap, remotion | ✅ | 79 B | S 2KB | claude:ayni | calesthio/OpenMontage |
| `cut-the-curve` | ⭐ | The technique catalog: five velocity-matched SEAMS (zoom-through, INVERSE zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut) p… | canvas, css, gsap | ✅ | 92 A | M 28KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `manim-composer` | ⭐ tamamlayıcı | Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını so… | manim | ✅ | 87 A | S 22KB | claude:ayni | calesthio/OpenMontage |
| `manimce-best-practices` | ⭐ birincil | Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve y… | manim, python, latex | ✅ | 95 A | S 206KB | claude:ayni | calesthio/OpenMontage |
| `manimgl-best-practices` | ⭐ alternatif | ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşi… | manim, python, opengl, latex | ✅ | 86 A | S 729KB | claude:ayni | calesthio/OpenMontage |
| `motion-doctrine` | ⭐ | GATEWAY — load FIRST before composing any HyperFrames animation or video. The high-level motion law that makes a multi-scene video feel like… | html, node | ✅ | 92 A | M 44KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `motion-graphics` | ⭐ | Use when creating a short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, lo… | api-anahtari, ffmpeg, gsap, html, node | 🟡 | 85 A | M 113KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `motion-graphics@calesthio` | alt birincil | Hareketin mesaj olduğu kısa (~10-30 sn), anlatımsız motion graphic üretimi: kinetik tipografi, sayı sayacı, grafik, logo sting, lower-third,… | hyperframes, html, gsap, ffmpeg | ✅ | 86 A | M 108KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `pose-library-design` | ⭐ tamamlayıcı | Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekle… | gsap, remotion | ✅ | 79 B | S 1KB | claude:ayni | calesthio/OpenMontage |
| `seam-craft` | ⭐ | Render-correctness doctrine for scene-to-scene seams in HyperFrames launch videos — the prerequisites that make transitions composite correc… | api-anahtari, canvas, gsap, html, typescript | ✅ | 94 A | S 5KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `svg-character-animation` | ⭐ birincil | SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pi… | svg, gsap, remotion, hyperframes | ✅ | 87 A | S 2KB | claude:ayni | calesthio/OpenMontage |
| `visual-style` | ⭐ birincil | Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper… | markdown, html | ✅ | 87 A | S 81KB | claude:ayni | calesthio/OpenMontage |
