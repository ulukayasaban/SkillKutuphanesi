# Skill Kataloğu

> `araclar/katalog-uret.py` üretir — elle düzenleme. Kaynak: `registry.json`.

Toplam **362** skill (+878 gizli: entegrasyon `KATALOG-entegrasyon.md`, repo-içi `notlar/referans/repo-ici-skiller.md`).

**İşaretler:** ⭐ tercih edilen · `alt` aynı isimli alternatif sürüm · Codex: ✅ tam uyumlu, 🟡 Claude araç adları geçiyor ama çalışır, 🔵 konusu Claude Code'a özel · Yük: S/M/L (agent bağlamına etkisi) · globalde: bilgisayardaki genel klasörde aynı isimli skill (ayni/farkli)

## İçindekiler

- **Tasarım ve Ön Yüz** (108)
  - [01-ui-ux-tasarim-dili](#01-ui-ux-tasarim-dili) — 12 skill · Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi
  - [02-tasarim-sistemi-marka](#02-tasarim-sistemi-marka) — 11 skill · Design token, tema, marka kimliği, banner/logo
  - [03-animasyon-motion](#03-animasyon-motion) — 17 skill · GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim
  - [04-scroll-deneyimi](#04-scroll-deneyimi) — 6 skill · Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri
  - [05-3d-webgl](#05-3d-webgl) — 33 skill · Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader
  - [06-oyun-2d-grafik](#06-oyun-2d-grafik) — 12 skill · Oyun geliştirme, PixiJS, 2D grafik
  - [07-gorsel-sanat-sunum](#07-gorsel-sanat-sunum) — 10 skill · Poster/canvas tasarımı, generative art, slayt, GIF
  - [08-onyuz-test-kalite](#08-onyuz-test-kalite) — 7 skill · Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı
- **Yazılım Geliştirme** (76)
  - [01-planlama-metodoloji](#01-planlama-metodoloji) — 15 skill · Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini
  - [02-kod-kalitesi-review](#02-kod-kalitesi-review) — 11 skill · Code review, sadeleştirme, temiz kod
  - [03-test-hata-ayiklama](#03-test-hata-ayiklama) — 11 skill · TDD, hata ayıklama, doğrulama
  - [04-mimari-api-veritabani](#04-mimari-api-veritabani) — 8 skill · Mimari, API/arayüz tasarımı, veritabanı, backend
  - [05-git-pr-surum](#05-git-pr-surum) — 8 skill · Git, worktree, PR, sürüm/release, changelog
  - [06-devops-guvenlik-performans](#06-devops-guvenlik-performans) — 10 skill · CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans
  - [07-framework-ozel](#07-framework-ozel) — 13 skill · Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)
- **Doküman ve İçerik** (43)
  - [01-ofis-dokumanlari](#01-ofis-dokumanlari) — 8 skill · Word, Excel, PowerPoint, PDF üretme/düzenleme
  - [02-diyagram-dokumantasyon](#02-diyagram-dokumantasyon) — 5 skill · Diyagram, teknik dokümantasyon, ADR, ortak yazım
  - [03-yazi-iletisim-icerik](#03-yazi-iletisim-icerik) — 15 skill · Yazı, iletişim, pazarlama/içerik, kariyer
  - [04-not-alma-bilgi-yonetimi](#04-not-alma-bilgi-yonetimi) — 15 skill · Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni
- **AI ve Otomasyon** (41)
  - [01-claude-api-mcp](#01-claude-api-mcp) — 10 skill · Claude API, MCP sunucusu, model geçişi
  - [02-agent-orkestrasyon](#02-agent-orkestrasyon) — 14 skill · Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları
  - [03-web-arastirma-veri](#03-web-arastirma-veri) — 2 skill · Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma
  - [04-skill-plugin-yazimi](#04-skill-plugin-yazimi) — 15 skill · Skill yazma, plugin/hook/komut geliştirme
- **Video, Ses ve AI Medya Üretimi** (92)
  - [01-video-uretim-montaj](#01-video-uretim-montaj) — 46 skill · Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg
  - [02-ses-muzik-konusma](#02-ses-muzik-konusma) — 14 skill · Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi
  - [03-ai-gorsel-video-modelleri](#03-ai-gorsel-video-modelleri) — 17 skill · AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu
  - [04-motion-graphics-karakter](#04-motion-graphics-karakter) — 15 skill · Motion graphics, Manim, karakter animasyonu/rig, görsel stil

## Tasarım ve Ön Yüz

### 01-ui-ux-tasarim-dili

_Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi_ · not: `notlar/a-tasarim-onyuz/01-ui-ux-tasarim-dili.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `design-dna` | ⭐ birincil | Tasarım DNA'sını üç boyutta çıkarır, tanımlar ve uygular: tasarım sistemi (token), tasarım stili (nitel his) ve görsel efektler (Canvas, Web… | html, css, node, webgl | ✅ | 82 A | M 709KB | claude:farkli | zanwei/design-dna |
| `design-taste-frontend` | ⭐ birincil | tasteskill v2: 247 seçkin galeri sitesinden damıtılmış 'anti-slop' sanat yönetimi. Betik araştırılmış 20 yönden üçünü dağıtır, seçilen yöne … | html, css, node, chromium | ✅ | 93 A | L 2363KB | - | Leonxlnx/taste-skill |
| `frontend-design` | ⭐ tamamlayıcı | Anthropic'in kısa tasarım ilkeleri skilli: tasarım stüdyosu yöneticisi gibi konuya özgü, şablon gibi görünmeyen palet/tipografi/düzen kararl… | html, css | ✅ | 84 A | M 9KB | - | anthropics/claude-code |
| `frontend-design@anthropics` | alt alternatif | frontend-design'ın anthropics/skills kopyası: içerik claude-code eklentisindekiyle birebir aynı, ayrıca LICENSE.txt içerir. | html, css | ✅ | 84 A | M 19KB | - | anthropics/skills |
| `frontend-design@vudovn` | alt alternatif | ag-kit'in 'anti-slop' web UI skilli: brief çıkarımı, üç kadranlı (varyans/hareket/yoğunluk) yapılandırma, gerçek tasarım sistemi eşlemesi, t… | html, css, react, next.js, tailwind, python | ✅ | 74 B | L 161KB | - | vudovn/ag-kit |
| `impeccable` | ⭐ birincil | Ön yüz arayüzlerini tasarlama, yeniden tasarlama, eleştirme, denetleme, cilalama ve sağlamlaştırma için komut tabanlı tasarım direktörü: sha… | html, css, node | ✅ | 95 A | M 2140KB | - | pbakaus/impeccable |
| `mobile-design` | ⭐ birincil | iOS ve Android uygulamaları için mobil öncelikli tasarım düşüncesi: dokunma etkileşimi, başparmak bölgesi, platform gelenekleri, performans … | react-native, flutter, python | ✅ | 84 A | M 216KB | - | vudovn/ag-kit |
| `modern-web-design` | ⭐ alternatif | 2024-2025 web tasarım trendleri ve kalıpları özeti: performans öncelikli tasarım, cesur minimalizm, mikro etkileşim, scrollytelling, imleç U… | html, css, gsap, three.js, react | ✅ | 55 C | L 151KB | - | freshtechbro/claudedesignskills |
| `ui-styling` | ⭐ birincil | shadcn/ui (Radix + Tailwind) bileşenleri, Tailwind yardımcı sınıf stili ve canvas tabanlı görsel tasarımla erişilebilir arayüz kurma: tema/k… | react, tailwind, shadcn-ui, radix, python | ✅ | 88 A | M 5627KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `ui-ux-pro-max` | ⭐ tamamlayıcı | Yerel aranabilir UI/UX veri tabanı: 79 stil, 192 ürün paleti ve gerekçe profili, 74 font eşleşmesi, 119 UX kuralı, ikonlar, GSAP ön ayarları… | python, html, css, tailwind | 🟡 | 85 A | M 3499KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `web-design-guidelines` | ⭐ tamamlayıcı | UI kodunu Vercel'in Web Interface Guidelines kurallarına göre denetler: kuralları her çalıştırmada GitHub'dan (vercel-labs/web-interface-gui… | html, css, react | ✅ | 85 A | S 2KB | claude:farkli | vudovn/ag-kit |
| `web-design-guidelines@calesthio` | alt alternatif | web-design-guidelines'ın OpenMontage kopyası; ag-kit sürümünün 'İlgili skiller' ve iş akışı bölümleri olmadan aynı içerik. | html, css | ✅ | 87 A | S 1KB | claude:ayni | calesthio/OpenMontage |

### 02-tasarim-sistemi-marka

_Design token, tema, marka kimliği, banner/logo_ · not: `notlar/a-tasarim-onyuz/02-tasarim-sistemi-marka.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `banner-design` | ⭐ tamamlayıcı | Sosyal medya kapakları, reklam bannerları, web hero görselleri ve baskı bannerları için çok formatlı tasarım akışı. Gereksinimleri sorar, 2-… | html, css | 🟡 | 78 B | S 12KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand` | ⭐ tamamlayıcı | Marka sesi, görsel kimlik, mesajlaşma çerçeveleri, varlık yönetimi ve tutarlılık denetimi için kapsamlı kılavuz seti. `docs/brand-guidelines… | node, css, markdown | ✅ | 89 A | S 106KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `brand-guidelines` | ⭐ tamamlayıcı | Anthropic'in kurumsal renk (koyu #141413, açık #faf9f5, turuncu/mavi/yeşil vurgu) ve tipografi (Poppins başlık, Lora gövde) kurallarını sunu… | python-pptx | ✅ | 69 B | S 13KB | - | anthropics/skills |
| `brand-guidelines@composiohq` | alt alternatif | anthropics/skills'teki brand-guidelines'ın birebir kopyası: Anthropic renk ve tipografi kurallarını sunum/belgelere uygular. | python-pptx | ✅ | 69 B | S 13KB | - | ComposioHQ/awesome-claude-skills |
| `design` | ⭐ birincil | claudekit birleşik tasarım skilli: marka kimliği, token, UI stili, AI ile logo üretimi (55 stil; Gemini, Atlas Cloud veya MuAPI), 50 teslima… | python, html, css, gemini, api-anahtari | 🟡 | 77 B | M 284KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `design-spec` | ⭐ tamamlayıcı | DESIGN.md dosyası yazma rehberi: makinece okunur tasarım token'ları (YAML ön bilgi: renk, tipografi, boşluk, köşe, bileşen) ile insan okunur… | markdown, yaml | ✅ | 85 A | S 21KB | - | vudovn/ag-kit |
| `design-system` | ⭐ birincil | Üç katmanlı (primitive, semantic, component) token mimarisi, CSS değişkenleri, boşluk/tipografi ölçekleri, bileşen durum spesifikasyonları v… | css, node, python, tailwindcss, chart.js | ✅ | 89 A | S 178KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `tailwind-design-system` | ⭐ tamamlayıcı | Tailwind CSS v4 ile (CSS-first `@theme`, OKLCH renk) üretim kalitesinde tasarım sistemi kurma tarifi: semantik token'lar, CVA ile bileşen va… | tailwindcss, react, typescript, radix-ui | ✅ | 86 A | M 22KB | claude:ayni | calesthio/OpenMontage |
| `tailwind-patterns` | ⭐ tamamlayıcı | Tailwind CSS v4 ilkeleri: CSS-öncelikli @theme yapılandırması, kapsayıcı sorguları, OKLCH renk token mimarisi, karanlık mod, tipografi ölçeğ… | tailwind, css | ✅ | 77 B | S 7KB | - | vudovn/ag-kit |
| `theme-factory` | ⭐ birincil | 10 hazır renk+yazı tipi temasıyla (Ocean Depths, Midnight Galaxy, Tech Innovation vb.) slayt, belge, rapor veya HTML sayfasını tek seferde s… | html, css, pptx | ✅ | 77 B | S 141KB | - | anthropics/skills |
| `theme-factory@composiohq` | alt alternatif | anthropics/skills'teki theme-factory'nin birebir kopyası: 10 hazır tema ile slayt/belge/HTML stillendirme. | html, css, pptx | ✅ | 77 B | S 141KB | - | ComposioHQ/awesome-claude-skills |

### 03-animasyon-motion

_GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim_ · not: `notlar/a-tasarim-onyuz/03-animasyon-motion.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `animated-component-libraries` | ⭐ birincil | Magic UI (150+) ve React Bits (90+) hazır animasyonlu React bileşenlerini kullanma: shadcn CLI ile ekleme, özelleştirme, performans ve yaygı… | react 19, tailwind 4, motion v14, shadcn-ui, ogl | ✅ | 65 B | M 89KB | - | freshtechbro/claudedesignskills |
| `animejs` | ⭐ alternatif | Anime.js ile DOM, CSS, SVG ve JS nesnesi animasyonu: timeline, stagger, SVG path/morph. GSAP'a hafif alternatif olarak anlatılır; üreticiler… | animejs 4, javascript | ✅ | 65 B | M 62KB | - | freshtechbro/claudedesignskills |
| `framer-motion` | ⭐ alternatif | Disney'in 12 animasyon prensibini (squash/stretch, anticipation, staging...) Framer Motion kod parçalarıyla örnekler. Kurulum, reduced-motio… | motion v14, react | ✅ | 71 B | S 3KB | claude:ayni | calesthio/OpenMontage |
| `gsap-core` | ⭐ birincil | GSAP çekirdek API'si: gsap.to/from/fromTo, ease, stagger, varsayılanlar ve gsap.matchMedia() ile responsive / prefers-reduced-motion animasy… | gsap 3.15, javascript, typescript | ✅ | 97 A | M 14KB | claude:ayni | greensock/gsap-skills |
| `gsap-frameworks` | ⭐ tamamlayıcı | GSAP'ı Vue/Nuxt, Svelte/SvelteKit ve diğer yaşam döngülü framework'lerde kullanma: onMounted/onMount, selector scope, unmount temizliği, Scr… | gsap 3.15, vue 3, nuxt 4, svelte 5 | ✅ | 89 A | M 10KB | claude:farkli | greensock/gsap-skills |
| `gsap-frameworks@calesthio` | alt alternatif | gsap-frameworks'ün OpenMontage'daki eski kopyası: Vue ve Svelte bölümleri aynı, Nuxt 4 bölümü ve örnek klasörü atıfları yok. | gsap 3.15, vue 3, svelte | ✅ | 79 B | S 6KB | claude:ayni | calesthio/OpenMontage |
| `gsap-performance` | ⭐ tamamlayıcı | GSAP animasyonlarında performans: transform/opacity tercihi, will-change, okuma/yazma gruplama, çok elemanlı stagger ve ScrollTrigger maliye… | gsap 3.15, css | ✅ | 98 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-plugins` | ⭐ tamamlayıcı | GSAP eklentileri: ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, DrawSVG, MorphSVG, MotionPath… | gsap 3.15 | ✅ | 97 A | M 21KB | claude:farkli | greensock/gsap-skills |
| `gsap-plugins@calesthio` | alt alternatif | gsap-plugins'in OpenMontage'daki eski kopyası. İçerik aynı eklenti kataloğu; tek fark yeni sürümdeki 'Licensing & Install' (tüm eklentiler ü… | gsap 3.15 | ✅ | 86 A | M 20KB | claude:farkli | calesthio/OpenMontage |
| `gsap-react` | ⭐ tamamlayıcı | GSAP'ı React/Next.js'te kullanma: useGSAP hook'u, ref'ler, scope, gsap.context() ve unmount temizliği, SSR notları. Resmî skill; en sık yapı… | gsap 3.15, @gsap/react 2, react 19, next.js | ✅ | 98 A | S 6KB | claude:ayni | greensock/gsap-skills |
| `gsap-timeline` | ⭐ tamamlayıcı | GSAP timeline'ları: gsap.timeline(), position parametresi, iç içe timeline ve oynatma kontrolü. Çok adımlı animasyon koreografisi için kısa … | gsap 3.15, javascript | ✅ | 98 A | S 4KB | claude:ayni | greensock/gsap-skills |
| `gsap-utils` | ⭐ tamamlayıcı | gsap.utils yardımcıları: clamp, mapRange, normalize, interpolate, random, snap, distribute, toArray, wrap, pipe. Scroll değerini eşleme, ızg… | gsap 3.15, javascript | ✅ | 89 A | M 12KB | claude:ayni | greensock/gsap-skills |
| `lottie-animations` | ⭐ birincil | Lottie (lottie-web, lottie-react, dotLottie) ile After Effects JSON animasyonlarını web/React'e gömme: oynatma kontrolü, etkileşim, optimiza… | lottie-web 5.13, dotlottie-web, react | ✅ | 65 B | M 64KB | - | freshtechbro/claudedesignskills |
| `lottie-bodymovin` | ⭐ alternatif | Disney'in 12 animasyon prensibini Lottie/After Effects iş akışıyla örnekler (AE ifadeleri, segment oynatma). Kısa ilke-örnek listesi. | lottie-web 5.13, after-effects | ✅ | 71 B | S 4KB | claude:ayni | calesthio/OpenMontage |
| `motion-framer` | ⭐ birincil | Motion/Framer Motion ile React animasyonu: motion bileşenleri, variants, hover/tap/drag hareketleri, layout animasyonu, AnimatePresence, spr… | motion v14, react 19 | ✅ | 73 B | M 159KB | - | freshtechbro/claudedesignskills |
| `react-spring-physics` | ⭐ alternatif | React Spring ve Popmotion ile fizik tabanlı (yay) animasyon: spring hook'ları, jest entegrasyonu, düşük seviye animasyon yardımcıları. Doğal… | react-spring 10, react | ✅ | 65 B | M 71KB | - | freshtechbro/claudedesignskills |
| `rive-interactive` | ⭐ alternatif | Rive durum makinesi tabanlı etkileşimli vektör animasyonu: girdi işleme, ViewModel veri bağlama, rive-react entegrasyonu. Betikler bileşen v… | rive, react | ✅ | 65 B | M 26KB | - | freshtechbro/claudedesignskills |

### 04-scroll-deneyimi

_Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri_ · not: `notlar/a-tasarim-onyuz/04-scroll-deneyimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `barba-js` | ⭐ birincil | Barba.js ile çok sayfalı sitelerde sayfalar arası geçiş animasyonu: hook'lar, router/prefetch/head eklentileri, GSAP entegrasyonu, geçiş kal… | barba 2, gsap 3.15 | ✅ | 65 B | M 129KB | - | freshtechbro/claudedesignskills |
| `gsap-scrolltrigger` | ⭐ birincil | GSAP ScrollTrigger resmî rehberi: scroll'a bağlı animasyon, pinleme, scrub, tetikleyiciler, refresh ve temizlik. Parallax, pinli bölüm ve sc… | gsap 3.15, scrolltrigger, lenis 1.3 | ✅ | 97 A | M 18KB | claude:ayni | greensock/gsap-skills |
| `gsap-scrolltrigger@freshtechbro` | alt alternatif | GSAP ve ScrollTrigger için kapsamlı (765 satır) genel rehber: tween, timeline, ScrollTrigger, kalıplar, ease referansı, başlangıç projesi ve… | gsap 3.15, scrolltrigger, three.js, react | ✅ | 65 B | M 159KB | claude:farkli | freshtechbro/claudedesignskills |
| `locomotive-scroll` | ⭐ birincil | Locomotive Scroll ile yumuşak (smooth) kaydırma, parallax ve viewport algılama; GSAP ScrollTrigger entegrasyon notları ve başlangıç projesi. | locomotive-scroll 4, gsap 3.15 | ✅ | 65 B | M 81KB | - | freshtechbro/claudedesignskills |
| `scroll-craft` | ⭐ birincil | Premium scroll-driven landing page üretir: brief/röportaj, sayfa grameri, duygu eğrisi, 'imza hamle', çok katmanlı (dimensional) hero, kendi… | html, css, javascript, node, chromium, kie.ai | 🟡 | 80 A | M 380KB | - | nateherkai/scroll-craft |
| `scroll-reveal-libraries` | ⭐ alternatif | AOS (Animate On Scroll) ile basit scroll reveal animasyonları: data-aos öznitelikleri, yerleşik animasyonlar, özel animasyon, karşılaştırma … | aos, css | ✅ | 65 B | M 94KB | - | freshtechbro/claudedesignskills |

### 05-3d-webgl

_Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader_ · not: `notlar/a-tasarim-onyuz/05-3d-webgl.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `aframe-webxr` | ⭐ birincil | A-Frame ile HTML tabanlı WebXR/VR/AR deneyimleri: entity-component yapısı, sahne, kameralar, ışık, animasyon, özel bileşenler, VR kontrolcü … | aframe 1.7, webxr, three.js | ✅ | 63 C | L 176KB | - | freshtechbro/claudedesignskills |
| `babylonjs-engine` | ⭐ birincil | Babylon.js 3D motoru: engine/sahne başlatma, kameralar, ışık, mesh, materyaller, model yükleme, fizik (Havok), animasyon; sahne ve mesh üret… | babylonjs 7, webgl2, webgpu, havok | ✅ | 63 C | L 153KB | - | freshtechbro/claudedesignskills |
| `blender-web-pipeline` | ⭐ birincil | Blender'dan web için glTF/GLB dışa aktarma: bpy betikleri, toplu işleme, LOD üretimi, model optimizasyonu, Three.js/Babylon.js için hazırlam… | blender 4, bpy, gltf 2.0, python | ✅ | 65 B | M 27KB | - | freshtechbro/claudedesignskills |
| `lightweight-3d-effects` | ⭐ birincil | Zdog (sözde-3D vektör çizimler), Vanta.js (animasyonlu 3D arka planlar) ve Vanilla-Tilt (paralaks eğim) ile hafif dekoratif 3D efektler; kur… | zdog, vanta, vanilla-tilt, three.js | ✅ | 64 C | M 179KB | - | freshtechbro/claudedesignskills |
| `playcanvas-engine` | ⭐ birincil | PlayCanvas motoru: Application, entity-component sistemi, güncelleme döngüsü, glTF, materyal, fizik, özel script ve girdi; hazır başlangıç p… | playcanvas 2, webgl2, webgpu | ✅ | 65 B | M 183KB | - | freshtechbro/claudedesignskills |
| `react-three-fiber` | ⭐ alternatif | React Three Fiber ile deklaratif 3D sahne: Canvas, useFrame/useThree/useLoader, etkileşimli nesneler, glTF yükleme; sahne/bileşen üreten bet… | R3F v8, drei 9, three r172, react 18 | ✅ | 65 B | M 105KB | - | freshtechbro/claudedesignskills |
| `spline-interactive` | ⭐ birincil | Spline: tarayıcı tabanlı görsel 3D tasarım aracı; sahneyi React/web'e @splinetool/react-spline ile gömme, olay yönetimi, nesne kontrolü ve d… | spline, react | ✅ | 65 B | M 54KB | - | freshtechbro/claudedesignskills |
| `substance-3d-texturing` | ⭐ tamamlayıcı | Adobe Substance 3D Painter ile PBR materyal/doku üretimi ve web/oyun motoru için dışa aktarma: export preset'leri, toplu dışa aktarma, çözün… | substance-3d-painter, python, pbr | ✅ | 57 C | M 126KB | - | freshtechbro/claudedesignskills |
| `threejs-animation` | ⭐ birincil | Three.js'te keyframe, iskelet ve morph target animasyonu, AnimationMixer ile klip karıştırma, glTF animasyonlarını oynatma, prosedürel harek… | three r186, webgl2, webgpu, tsl | ✅ | 83 A | M 21KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-animation@calesthio` | alt alternatif | Three.js keyframe, iskelet ve morph animasyonu ile AnimationMixer kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-asset-pipeline` | ⭐ birincil | gltf-transform ile glTF/GLB varlıklarını küçültme: inspect, validate, optimize, Draco/meshopt/quantization, KTX2, WebP/AVIF dokular, her çık… | three r186, gltf-transform 4, ktx2, draco, meshopt, gltfjsx | ✅ | 91 A | M 18KB | - | CloudAI-X/threejs-skills |
| `threejs-fundamentals` | ⭐ birincil | Three.js sahne kurulumunun temelleri: sahne ve sis, kameralar, renderer ve tone mapping, animasyon döngüsü, nesne hiyerarşisi, dönüşümler, m… | three r186, webgl2, webgpu, tsl | ✅ | 91 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-fundamentals@calesthio` | alt alternatif | Three.js sahne kurulumu, kameralar, renderer, Object3D, koordinat sistemi ve matematik sınıflarına kısa giriş (eski sürüm, WebGPU yok). | three.js, webgl | ✅ | 70 B | M 11KB | claude:ayni | calesthio/OpenMontage |
| `threejs-geometry` | ⭐ birincil | Three.js geometri: yerleşik şekiller, 3D metin, BufferGeometry ve attribute'lar, birleştirme, instancing, batching, nokta bulutu ve çizgiler… | three r186, webgl2, webgpu, tsl | ✅ | 81 A | L 25KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-geometry@calesthio` | alt alternatif | Three.js yerleşik geometriler, BufferGeometry, instancing ve Points kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-interaction` | ⭐ birincil | Three.js'te raycasting ile seçme, kamera kontrolleri (Orbit, Fly, PointerLock vb.), TransformControls, sürükleme, hover ve kutu seçimi; WebG… | three r186, webgl2, webgpu, tsl | ✅ | 83 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-interaction@calesthio` | alt alternatif | Three.js raycaster, kontroller, dokunma desteği ve seçim kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 16KB | claude:ayni | calesthio/OpenMontage |
| `threejs-lighting` | ⭐ birincil | Three.js ışık türleri ve fiziksel birimler, gölge haritaları, HDR ortam aydınlatması (IBL), light probe, gölge ayarları ve ışık performansı. | three r186, webgl2, webgpu, tsl | ✅ | 91 A | M 23KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-lighting@calesthio` | alt alternatif | Three.js ışık türleri, gölge kurulumu ve ortam aydınlatması kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 12KB | claude:ayni | calesthio/OpenMontage |
| `threejs-loaders` | ⭐ birincil | Three.js varlık yükleme: Draco/meshopt/KTX2 destekli glTF, diğer model biçimleri, dokular, HDR/EXR ortamları, ilerleme, önbellek, klonlama v… | three r186, webgl2, webgpu, tsl | ✅ | 91 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-loaders@calesthio` | alt alternatif | Three.js GLTF, doku ve HDR yükleme ile LoadingManager kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-materials` | ⭐ birincil | Three.js materyalleri: unlit, diffuse, PBR (Standard/Physical), toon, nokta/çizgi materyalleri, blending/stencil ve WebGPU node materyal/TSL… | three r186, webgl2, webgpu, tsl | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-materials@calesthio` | alt alternatif | Three.js materyal türleri (Basic, Phong, Standard, Physical, Toon) kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-performance` | ⭐ birincil | Three.js performans ölçümü ve iyileştirme: render istatistikleri, bellek, draw call azaltma (birleştirme, instancing, batching, LOD), fill r… | three r186, webgl2, webgpu, tsl | ✅ | 89 A | L 25KB | - | CloudAI-X/threejs-skills |
| `threejs-postprocessing` | ⭐ birincil | Three.js post-processing: composer pass zinciri, bloom, DOF, SSAO, outline, özel ekran efektleri ve WebGPU/TSL node pipeline. | three r186, webgl2, webgpu, tsl | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-postprocessing@calesthio` | alt alternatif | Three.js EffectComposer, bloom, DOF, SSAO, film grain kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-react-three-fiber` | ⭐ birincil | React Three Fiber ve drei ile Three.js sahnesi: renderer kurulumu, JSX sahne grafı, frame-loop, state ve yükleme hook'ları, pointer olayları… | R3F v9, drei 10, three r186, react 19 | ✅ | 89 A | L 29KB | - | CloudAI-X/threejs-skills |
| `threejs-shaders` | ⭐ birincil | Özel GLSL vertex/fragment shader'lar: uniform, varying, shader chunk, yerleşik materyal genişletme, instanced attribute; WebGPU'da TSL node … | three r186, webgl2, webgpu, tsl | ✅ | 81 A | L 26KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-shaders@calesthio` | alt alternatif | Three.js GLSL ShaderMaterial, uniform, varying ve yaygın shader kalıpları kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 14KB | claude:ayni | calesthio/OpenMontage |
| `threejs-textures` | ⭐ birincil | Three.js dokuları: yükleme, renk uzayı, UV kanalları/dönüşümleri, canvas'tan HDR ve KTX2'ye doku türleri, render target, atlas, doku belleği… | three r186, webgl2, webgpu, tsl | ✅ | 83 A | M 22KB | claude:farkli | CloudAI-X/threejs-skills |
| `threejs-textures@calesthio` | alt alternatif | Three.js doku yükleme, ayarlar, UV, cubemap ve HDR kısa özeti (eski sürüm). | three.js, webgl | ✅ | 70 B | M 13KB | claude:ayni | calesthio/OpenMontage |
| `threejs-webgl` | ⭐ alternatif | Three.js/WebGL/WebGPU geliştirmesine genel bakış: sahne grafı, temel bileşenler, hazır sahne kalıbı, mesh/ışık/instancing/glTF/gölge örnekle… | three.js, webgl, webgpu, gsap 3.15 | ✅ | 57 C | M 62KB | - | freshtechbro/claudedesignskills |
| `web3d-integration-patterns` | ⭐ birincil | Three.js, GSAP ScrollTrigger, React Three Fiber, Motion ve React Spring'i birleştirme desenleri: katmanlı ayrım, birleşik React bileşeni, hi… | three.js, R3F v8, gsap 3.15, motion v14, react-spring 10, zustand | ✅ | 65 B | M 21KB | - | freshtechbro/claudedesignskills |

### 06-oyun-2d-grafik

_Oyun geliştirme, PixiJS, 2D grafik_ · not: `notlar/a-tasarim-onyuz/06-oyun-2d-grafik.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `2d-games` | ⭐ alternatif | 2D oyun ilkeleri: sprite atlas ve animasyon, tilemap katmanları, 2D fizik şekilleri, kamera tipleri ve ekran sarsıntısı, platformer (coyote … | 2d, sprite, tilemap | ✅ | 77 B | S 2KB | - | vudovn/ag-kit |
| `3d-games` | ⭐ alternatif | 3D oyun ilkeleri: render hattı aşamaları, culling/LOD/batching, shader türleri ve ne zaman özel shader yazılır, 3D çarpışma şekilleri, kamer… | 3d, shader, lod | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `game-art` | ⭐ alternatif | Oyun sanatı ilkeleri: sanat stili karar ağacı (pixel, vektör, el boyaması, PBR, low-poly, cel-shaded) ve karşılaştırma matrisi, 2D/3D varlık… | pixel-art, blender, aseprite | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `game-audio` | ⭐ alternatif | Oyun sesi ilkeleri: ses kategorileri ve öncelik hiyerarşisi, SFX katmanlama, müzik durum sistemi ve geçiş teknikleri, uyarlanabilir (vertica… | web-audio, fmod, wwise | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `game-design` | ⭐ alternatif | Oyun tasarımı ilkeleri: 30 saniyelik çekirdek döngü, GDD bölümleri, oyuncu motivasyon tipleri ve ödül takvimleri, zorluk dengeleme (flow), i… | gdd, game-design | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `game-development` | ⭐ birincil | Oyun geliştirme orkestratörü: oyun döngüsü (sabit zaman adımı), desen seçim matrisi (state machine, pooling, ECS), girdi soyutlama, 60 FPS b… | game-design, unity, godot, unreal, phaser | ✅ | 77 B | S 35KB | - | vudovn/ag-kit |
| `mobile-games` | ⭐ alternatif | Mobil oyun ilkeleri: dokunmatik girdi (44pt hedef), pil/ısıl yönetim, performans hedefleri, App Store / Google Play gereklilikleri ve para k… | ios, android, touch | ✅ | 77 B | S 2KB | - | vudovn/ag-kit |
| `multiplayer` | ⭐ alternatif | Çok oyunculu ilkeleri: mimari seçimi (dedicated, P2P, host), durum/girdi senkronizasyonu, tahmin-enterpolasyon-uzlaştırma ve lag compensatio… | networking, websocket | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `pc-games` | ⭐ alternatif | PC/konsol oyun ilkeleri: motor seçimi (Unity 6, Godot 4, Unreal 5) karar ağacı ve karşılaştırması, Steam özellikleri, konsol sertifikasyonu,… | unity, godot, unreal, steam | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `pixijs-2d` | ⭐ birincil | PixiJS v8 ile 2D WebGL/WebGPU render rehberi: Application, sprite/texture, Graphics API, ParticleContainer ile on binlerce parçacık, filtrel… | pixi.js, webgl, webgpu, javascript | ✅ | 73 B | M 253KB | - | freshtechbro/claudedesignskills |
| `vr-ar` | ⭐ alternatif | VR/AR ilkeleri: platformlar (Quest, PCVR, WebXR, ARKit/ARCore), hareket hastalığı önleme ve konfor ayarları, kare hızı hedefleri, kontrolcü/… | webxr, quest, arkit | ✅ | 69 B | S 2KB | - | vudovn/ag-kit |
| `web-games` | ⭐ alternatif | Tarayıcı oyunu ilkeleri: çatı seçimi (Phaser, PixiJS, Three.js, Babylon.js), WebGPU benimseme durumu, tarayıcı kısıtları ve optimizasyon sır… | phaser, pixi.js, three.js, webgpu, pwa | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |

### 07-gorsel-sanat-sunum

_Poster/canvas tasarımı, generative art, slayt, GIF_ · not: `notlar/a-tasarim-onyuz/07-gorsel-sanat-sunum.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `algorithmic-art` | ⭐ birincil | Önce bir 'algoritmik felsefe' (manifesto .md) yazdırıp ardından bunu seed'li rastgelelik ve parametre paneliyle p5.js üretken sanatına (akış… | p5.js, canvas, html, javascript | ✅ | 76 B | M 58KB | - | anthropics/skills |
| `artifacts-builder` | ⭐ alternatif | React 18 + TypeScript + Vite + Tailwind + shadcn/ui ile karmaşık claude.ai HTML artifact'ı kurar (init-artifact.sh) ve Parcel + html-inline … | react, typescript, vite, tailwind, shadcn-ui, parcel | ✅ | 69 B | S 45KB | - | ComposioHQ/awesome-claude-skills |
| `canvas-design` | ⭐ birincil | Bir 'tasarım felsefesi' (hareket adı + 4-6 paragraf manifesto) yazdırıp ardından bunu %90 görsel / %10 metin olan özgün PNG veya PDF posteri… | canvas, python, png, pdf | ✅ | 84 A | M 5424KB | - | anthropics/skills |
| `canvas-design@composiohq` | alt alternatif | Anthropic canvas-design'ın ComposioHQ kopyası; SKILL.md ve font klasörü birebir aynıdır, yalnızca LICENSE.txt farklı (şablon Apache metni, t… | canvas, png, pdf | ✅ | 68 B | M 5424KB | - | ComposioHQ/awesome-claude-skills |
| `d3-viz` | ⭐ birincil | d3.js ile özel, etkileşimli veri görselleştirmeleri (ağ/grafik, hiyerarşi, coğrafi harita, geçişli grafikler) kurmayı anlatır; React ve vani… | d3, svg, react, javascript | ✅ | 86 A | M 80KB | claude:ayni | calesthio/OpenMontage |
| `image-enhancer` | ⭐ birincil | Ekran görüntüsü ve görsellerin çözünürlüğünü, keskinliğini ve sıkıştırma artefaktlarını iyileştirmeyi anlatan, betiği olmayan yalnızca yöner… | imagemagick | ✅ | 69 B | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `slack-gif-creator` | ⭐ birincil | Slack için animasyonlu GIF üretimi: PIL ile kare çizimi, GIFBuilder, easing fonksiyonları, kare birleştirici ve Slack boyut/FPS/renk sınırla… | python, pillow, imageio, numpy, gif | ✅ | 77 B | S 43KB | - | anthropics/skills |
| `slack-gif-creator@composiohq` | alt alternatif | Aynı skill'in ComposioHQ'daki daha eski/geniş sürümü: SKILL.md 16,7 KB, ek color_palettes.py, typography.py, visual_effects.py ve templates/… | python, pillow, imageio, numpy, gif | ✅ | 76 B | M 208KB | - | ComposioHQ/awesome-claude-skills |
| `slides` | ⭐ birincil | Chart.js, tasarım token'ları, yerleşim kalıpları ve metin yazım formülleri ile stratejik HTML sunum (pitch deck, pazarlama slaytı) üretir; `… | html, chart.js, css | ✅ | 81 A | S 19KB | - | nextlevelbuilder/ui-ux-pro-max-skill |
| `web-artifacts-builder` | ⭐ birincil | React + TypeScript + Vite + Tailwind + shadcn/ui ile çok bileşenli claude.ai HTML artifact'ı kurar ve Parcel/html-inline ile tek dosyalık bu… | react, typescript, vite, tailwind, shadcn-ui, parcel | ✅ | 85 A | S 45KB | - | anthropics/skills |

### 08-onyuz-test-kalite

_Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı_ · not: `notlar/a-tasarim-onyuz/08-onyuz-test-kalite.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `browser-testing-with-devtools` | ⭐ birincil | Chrome DevTools MCP ile ajana canlı tarayıcı gözü kazandırır: ekran görüntüsü, DOM, konsol, ağ istekleri, performans izi (LCP/CLS/INP), hesa… | chrome-devtools-mcp, chrome, javascript | ✅ | 87 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `playwright-component-testing` | ⭐ birincil | Playwright ile React/Vue bileşenlerini 'hikâye galerisi' sayfası üzerinden, dahili `mount` fixture'ı ve düz Playwright testleriyle izole tes… | playwright, react, vue, vite, typescript | ✅ | 91 A | M 38KB | - | microsoft/playwright |
| `playwright-trace` | ⭐ tamamlayıcı | Playwright trace (.zip) dosyalarını komut satırından inceler: eylem listesi, ağ istekleri, konsol, hatalar, DOM/erişilebilirlik anlık görünt… | playwright | ✅ | 92 A | S 5KB | - | microsoft/playwright |
| `react-doctor` | ⭐ birincil | React kod tabanını güvenlik, performans, doğruluk, erişilebilirlik ve mimari açısından tarayıp 0-100 sağlık puanı veren `react-doctor` CLI'ı… | react, next.js, eslint | ✅ | 79 B | S 3KB | - | darkroomengineering/satus |
| `webapp-testing` | ⭐ birincil | Yerel web uygulamalarını Python Playwright betikleriyle test etme araç seti: statik/dinamik karar ağacı, `with_server.py` ile bir veya birde… | playwright, python | ✅ | 85 A | S 22KB | - | anthropics/skills |
| `webapp-testing@composiohq` | alt alternatif | anthropics/skills webapp-testing'in kopyası: Python Playwright ile yerel web uygulaması testi, with_server.py ve örnek betikler. | playwright, python | ✅ | 85 A | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `webapp-testing@vudovn` | alt alternatif | Web testi ilkeleri (derin denetim, test piramidi, E2E, Playwright kavramları, görsel test, API test, CI) ve hafif `playwright_runner.py` bet… | playwright, python | ✅ | 77 B | S 10KB | - | vudovn/ag-kit |

## Yazılım Geliştirme

### 01-planlama-metodoloji

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_ · not: `notlar/b-yazilim-gelistirme/01-planlama-metodoloji.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `app-builder` | ⭐ birincil | ag-kit'in uygulama kurma orkestratörü: doğal dil isteğinden proje tipini tespit eder, 2026 varsayılan teknoloji yığınını (Next.js 16, Tailwi… | next.js, react, node, python, vue, flutter, react-native | ✅ | 77 B | S 63KB | - | vudovn/ag-kit |
| `brainstorming` | ⭐ birincil | superpowers'ın tasarım öncesi sohbet skilli: kullanıcının ne istediğini ve nedenini tek seferde tek soruyla açar, gerektiğinde kodu/web'i ke… | node, html | ✅ | 95 A | M 76KB | - | obra/superpowers |
| `brainstorming@vudovn` | alt alternatif | ag-kit'in Sokratik soru protokolü: belirsiz isteklerde kodlamadan önce en az 3 soru (amaç, kullanıcı, kapsam) sorar, soruları seçenek/artı-e… |  | ✅ | 77 B | S 17KB | - | vudovn/ag-kit |
| `constraint-driven-development` | ⭐ birincil | Projenin kalite çıtasını CONSTRAINTS.md'de yazılı sözleşmeye çevirir: kullanıcıya hangi boyutların önemli olduğunu sorar, sayı yoksa makul v… | git, node, python | ✅ | 87 A | M 31KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `doubt-driven-development` | ⭐ birincil | Önemsiz olmayan her kararı (iddia → en küçük incelenebilir birim → taze bağlamlı karşıt inceleme → uzlaştırma → dur) döngüsünden geçirir; ge… | api-anahtari | ✅ | 87 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `executing-plans` | ⭐ birincil | Yazılmış bir planı alt-agent kullanmadan, aynı oturumda görev görev uygular: her görev için brief ve kayıt defteri (ledger) tutar, TDD ile i… | git | ✅ | 87 A | M 20KB | - | obra/superpowers |
| `idea-refine` | ⭐ alternatif | Ham fikirleri ıraksak (genişlet) ve yakınsak (değerlendir, daralt) düşünme aşamalarıyla keskin bir konsepte çevirir; sonuçta problem tanımı,… |  | 🟡 | 84 A | M 40KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `incremental-implementation` | ⭐ tamamlayıcı | Değişiklikleri ince, doğrulanabilir dilimlerle teslim ettirir: dikey/sözleşme-önce/risk-önce dilimleme, 'önce sadelik' ve kapsam disiplini, … | git | ✅ | 87 A | M 9KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `interview-me` | ⭐ tamamlayıcı | Kullanıcının gerçekte ne istediğini (yapması gerektiğini düşündüğü şeyi değil) bulmak için tek soruluk turlarla ~%95 güvene kadar görüşme ya… | react | ✅ | 87 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `plan-writing` | ⭐ alternatif | ag-kit'in kısa plan yazma rehberi (obra/superpowers'tan uyarlanmış): 5-10 görevlik, her görevin doğrulaması belli, bir sayfayı geçmeyen plan… | node, python, react, tailwind, typescript | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `planning-and-task-breakdown` | ⭐ alternatif | Spec'i bağımlılık grafiği çıkarıp dikey dilimlere bölerek sıralı, boyutlandırılmış görevlere çevirir; her görev için kabul ölçütü ve doğrula… | typescript | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `source-driven-development` | ⭐ birincil | Her uygulama kararını resmî dokümantasyona dayandırır: yığını ve sürümleri tespit eder, resmî belgeyi çeker (çekilen içeriği talimat değil v… | api-anahtari, css, html, next.js, node | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `spec-driven-development` | ⭐ birincil | Kodlamadan önce spec yazdırır: kapsam kontrolü (gerekirse yetenek haritasına bölme), amaç/yığın/komutlar/yapı/test stratejisi/sınırlar/başar… | node, react | ✅ | 87 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `templates` | alt alternatif | 13 proje iskelet şablonunun (Next.js fullstack/SaaS/static, Nuxt, Express, FastAPI, Expo, Flutter, Electron, Chrome MV3, CLI, Turborepo, Ast… | next.js, react, node, python, vue, flutter, react-native | ✅ | 69 B | S 43KB | - | vudovn/ag-kit |
| `writing-plans` | ⭐ birincil | Spec'ten, kod tabanını hiç görmemiş bir mühendisin uygulayabileceği ayrıntılı uygulama planı yazdırır: dosya yapısı, her görev için dosyalar… | git | ✅ | 95 A | M 10KB | - | obra/superpowers |

### 02-kod-kalitesi-review

_Code review, sadeleştirme, temiz kod_ · not: `notlar/b-yazilim-gelistirme/02-kod-kalitesi-review.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `clean-code` | ⭐ birincil | ag-kit'in her kod yazımında açık tutulan pragmatik kodlama standardı: SRP/DRY/KISS/YAGNI, isimlendirme kuralları, küçük fonksiyon ve sığ iç … | playwright, python, typescript | ✅ | 77 B | S 7KB | - | vudovn/ag-kit |
| `code-review-and-quality` | ⭐ birincil | Beş eksenli kod incelemesi yaptırır: doğruluk, okunabilirlik/sadelik, mimari, güvenlik, performans. Önce testleri sonra uygulamayı okur, bul… | node, typescript | ✅ | 95 A | M 20KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `code-review-checklist` | ⭐ alternatif | Kısa kod inceleme kontrol listesi: doğruluk, güvenlik (enjeksiyon, XSS, gizli anahtar, prompt injection), performans, kod kalitesi, test ve … | typescript | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `code-review-graph` | ⭐ birincil | code-review-graph MCP sunucusunun kullanım rehberi: Tree-sitter ile kod tabanını SQLite'ta AST grafiğine çevirip değişikliğin etki alanını (… | python, tree-sitter, sqlite, mcp | ✅ | 76 B | M 11KB | - | vudovn/ag-kit |
| `code-simplification` | ⭐ birincil | Davranışı birebir koruyarak kodu açıklık için sadeleştirir: Chesterton'ın çiti (önce neden var olduğunu anla), proje geleneklerine uyma, zek… | typescript, javascript, python, react | ✅ | 95 A | M 13KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `lint-and-validate` | ⭐ birincil | Her kod değişikliğinden sonra ekosisteme göre lint, tip denetimi ve güvenlik taramasını çalıştırır (Node/TS: eslint, tsc --noEmit, npm audit… | node, typescript, python | ✅ | 77 B | S 16KB | - | vudovn/ag-kit |
| `pragmatic-review` | ⭐ alternatif | YAGNI ve KISS odaklı etkileşimli kod incelemesi: git durumundan kapsamı seçtirir (commit edilmemiş, dal, dosya, son N commit), aşırı mühendi… | git | ✅ | 74 B | M 11KB | - | heyitsnoah/claudesidian |
| `receiving-code-review` | ⭐ tamamlayıcı | Gelen kod inceleme geri bildirimine teknik titizlikle yaklaşmayı öğretir: oku, kendi sözlerinle yeniden ifade et, kod tabanında doğrula, değ… |  | ✅ | 88 A | S 6KB | - | obra/superpowers |
| `requesting-code-review` | ⭐ birincil | İş bitince veya birleştirmeden önce, oturum geçmişini değil özenle hazırlanmış bağlamı (açıklama, plan, BASE/HEAD SHA) vererek bir inceleyic… | git | ✅ | 96 A | S 9KB | - | obra/superpowers |
| `simplify-code` | ⭐ alternatif | Aşırı mühendislik içeren kodu sadeleştirme kontrol listesi: gereksiz soyutlamalar, ölü kod, derin iç içelik, çok parametreli fonksiyonlar ve… | typescript, javascript | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `simplify-codebase` | ⭐ tamamlayıcı | Kod tabanından kazara karmaşıklığı kanıta dayalı olarak ayıklar: Survey (salt okuma, sıralı bulgular) ve Change (yetkili silme/birleştirme) … |  | ✅ | 96 A | S 27KB | - | tt-a1i/archify |

### 03-test-hata-ayiklama

_TDD, hata ayıklama, doğrulama_ · not: `notlar/b-yazilim-gelistirme/03-test-hata-ayiklama.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `debugging-and-error-recovery` | ⭐ alternatif | Kök neden odaklı hata ayıklama: 'hattı durdur' kuralı, yeniden üret → yerelleştir → küçült → kök nedeni düzelt → tekrarı önle → uçtan uca do… | git, node, typescript | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `systematic-debugging` | ⭐ birincil | superpowers'ın hata ayıklama skilli: 'kök neden bulunmadan düzeltme yok' demir yasasıyla dört faz (kök neden araştırması, desen analizi, hip… | git | ✅ | 95 A | M 40KB | - | obra/superpowers |
| `systematic-debugging@heyitsnoah` | alt alternatif | obra/superpowers systematic-debugging'in claudesidian'daki kopyası: aynı dört faz ve demir yasa; kök neden izleme, stack trace ekleme, kirle… | git, typescript | ✅ | 74 B | M 13KB | - | heyitsnoah/claudesidian |
| `systematic-debugging@vudovn` | alt alternatif | ag-kit'in kısaltılmış hata ayıklama şablonu (obra/superpowers'tan uyarlanmış): yeniden üret, izole et, anla (5 Neden), düzelt ve doğrula faz… | git | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `tdd-workflow` | ⭐ alternatif | ag-kit'in TDD ilke özeti: RED-GREEN-REFACTOR döngüsü, TDD'nin üç yasası, her faz için kurallar, AAA, TDD'nin ne zaman değerli olduğu tablosu… |  | ✅ | 69 B | S 3KB | - | vudovn/ag-kit |
| `test-driven-development` | ⭐ birincil | Kırmızı-yeşil-refactor döngüsüyle geliştirme: önce projenin test yığınını keşfeder, başarısız test yazdırır, minimum kodla geçirtir, sonra t… | api-anahtari, css, html, node, playwright | ✅ | 95 A | M 16KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `test-driven-development@obra` | alt alternatif | superpowers'ın TDD skilli: 'başarısız test olmadan üretim kodu yok' demir yasası; testten önce yazılan kodu silip baştan başlatır, kırmızıyı… | typescript | ✅ | 95 A | M 17KB | claude:farkli,agents:farkli | obra/superpowers |
| `test-value` | ⭐ birincil | Testlerin değerini ve geri bildirim maliyetini denetler: yavaş, kararsız, yinelenen veya kırılgan testleri bulur; uygulama sırasında hangi t… |  | ✅ | 95 A | M 19KB | - | tt-a1i/archify |
| `testing-patterns` | ⭐ alternatif | Test ilkeleri özeti: test piramidi, AAA, birim/entegrasyon/E2E seçimi, iyi birim testi özellikleri, mock ne zaman/hangi tür (stub, spy, mock… | python | ✅ | 77 B | S 10KB | - | vudovn/ag-kit |
| `verification-before-completion` | ⭐ birincil | 'Taze doğrulama kanıtı olmadan tamamlandı iddiası yok' kuralı: bir durum iddia etmeden önce kanıtlayan komutu belirle, tam çalıştır, çıktıyı… |  | ✅ | 96 A | S 4KB | - | obra/superpowers |
| `verify-changes` | ⭐ tamamlayıcı | Kodun çalıştığını incelemeyle değil çalıştırarak kanıtlatır: değişen dosyaları ve beklenen davranışı belirle, değişiklik tipine göre doğrula… | node, python | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |

### 04-mimari-api-veritabani

_Mimari, API/arayüz tasarımı, veritabanı, backend_ · not: `notlar/b-yazilim-gelistirme/04-mimari-api-veritabani.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `api-and-interface-design` | ⭐ birincil | Kararlı API ve modül arayüzü tasarımı: Hyrum yasası ve tek sürüm kuralı, önce sözleşme, tutarlı hata semantiği, sınırda doğrulama, değiştirm… | typescript, rest, graphql | ✅ | 95 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `api-patterns` | ⭐ tamamlayıcı | ag-kit'in API tasarım karar rehberi: REST/GraphQL/tRPC seçim ağacı, kaynak isimlendirme ve durum kodları, zarf/hata/sayfalama yanıt biçimler… | rest, graphql, trpc, typescript, python | ✅ | 77 B | S 20KB | - | vudovn/ag-kit |
| `architecture` | ⭐ birincil | Mimari karar çerçevesi: bağlam keşfi soruları ve proje sınıflandırması, ödünleşim (trade-off) analizi ve ADR şablonları, desen seçimi karar … |  | ✅ | 77 B | S 12KB | - | vudovn/ag-kit |
| `database-design` | ⭐ birincil | Veritabanı tasarım kararları: PostgreSQL/Neon/Turso/SQLite seçimi, Drizzle/Prisma/Kysely ORM seçimi, normalizasyon ve ilişkiler, indeks tipl… | postgresql, sqlite, prisma, drizzle, sql | ✅ | 77 B | S 13KB | - | vudovn/ag-kit |
| `frontend-architecture` | ⭐ birincil | Ön yüz kodunu ölçeklenir biçimde düzenleme kuralları: UI / mantık (hook, composable) / veri (servis dosyaları) / tip / doğrulama (şema) katm… | react, next.js, vue, typescript, tailwind | ✅ | 84 A | M 8KB | - | vudovn/ag-kit |
| `frontend-ui-engineering` | ⭐ birincil | Üretim kalitesinde, erişilebilir ve responsive arayüz kurma: bileşen dosya yapısı ve desenleri, durum yönetimi, tasarım sistemine bağlılık v… | react, typescript, css, tailwind | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `nodejs-best-practices` | ⭐ birincil | Node.js arka yüz karar ilkeleri: Hono/Fastify/NestJS/Express seçim ağacı, yerel TypeScript ve modül sistemi kararları, katmanlı mimari, merk… | node, typescript, express, fastify, hono, nestjs | ✅ | 76 B | M 8KB | - | vudovn/ag-kit |
| `python-patterns` | ⭐ birincil | Python geliştirme karar ilkeleri: FastAPI/Django/Flask seçim ağacı, async/sync kararı ve kütüphane seçimi, tip ipucu stratejisi ve Pydantic … | python, fastapi, django, flask, pydantic | ✅ | 76 B | M 9KB | - | vudovn/ag-kit |

### 05-git-pr-surum

_Git, worktree, PR, sürüm/release, changelog_ · not: `notlar/b-yazilim-gelistirme/05-git-pr-surum.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `changelog-generator` | ⭐ tamamlayıcı | Git commit geçmişini tarayıp değişiklikleri kategorilere (yeni özellik, iyileştirme, düzeltme, kırıcı değişiklik, güvenlik) ayırır, iç commi… | git | ✅ | 77 B | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `deprecation-and-migration` | ⭐ birincil | Eski sistem, API veya özellikleri kaldırma ve kullanıcıları yeni uygulamaya taşıma: 'kod bir yüktür' ve Hyrum yasası ilkeleri, kaldırma kara… | sql | ✅ | 87 A | M 12KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `finishing-a-development-branch` | ⭐ birincil | Uygulama bittiğinde işi nasıl birleştireceğine karar verdirir: tam test paketini çalıştır (kırmızıysa dur), ortamı (normal repo / worktree /… | git, gh | ✅ | 96 A | S 8KB | - | obra/superpowers |
| `git-workflow-and-versioning` | ⭐ birincil | Git iş akışı disiplini: trunk tabanlı geliştirme, erken ve sık commit, atomik commit ve açıklayıcı mesajlar, konuları ayırma, değişiklik boy… | git | ✅ | 95 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `git-worktrees` | ⭐ alternatif | git worktree komut başvurusu: oluşturma (yeni/var olan dal), .worktrees/ dizin düzeni, kurulum sonrası adımlar (bağımlılık, env dosyası), co… | git | ✅ | 67 B | S 4KB | - | heyitsnoah/claudesidian |
| `pull-request` | ⭐ alternatif | Tek komutla PR akışı: önkoşulları kontrol eder (git, gh), başlıktan dal adı üretir, değişiklikleri gösterip onay ister, conventional commit … | git, gh | ✅ | 67 B | S 5KB | - | heyitsnoah/claudesidian |
| `release` | ⭐ birincil | Release akışını otomatikleştirir: son tag'den beri commit'leri analiz edip (BREAKING/feat/fix) sürüm artışını belirler, package.json sürümün… | git, gh, node | ✅ | 67 B | S 6KB | - | heyitsnoah/claudesidian |
| `using-git-worktrees` | ⭐ birincil | İşin yalıtılmış bir çalışma alanında yapılmasını sağlar: önce zaten bir worktree içinde olunup olunmadığını (alt modül korumasıyla) tespit e… | git | ✅ | 96 A | S 7KB | - | obra/superpowers |

### 06-devops-guvenlik-performans

_CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans_ · not: `notlar/b-yazilim-gelistirme/06-devops-guvenlik-performans.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `ci-cd-and-automation` | ⭐ birincil | CI/CD hattı kurulumu: kalite kapısı sırası (lint → tip → birim → build → entegrasyon → E2E → güvenlik), GitHub Actions örnekleri (veritabanl… | github-actions, node, playwright | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `deployment-procedures` | ⭐ tamamlayıcı | Üretim deploy ilkeleri: platform seçim ağacı (Vercel/Netlify, Railway/Render/Fly, VPS+PM2/Docker, Kubernetes, serverless), deploy öncesi dör… | docker, git | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `observability-and-instrumentation` | ⭐ birincil | Kodu üretimde görünür ve teşhis edilebilir kılar: önce 'çalışıyor'un tanımı, her soru için doğru sinyal (log, metrik, iz), yapılandırılmış l… | opentelemetry, node, typescript | ✅ | 87 A | M 14KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-optimization` | ⭐ birincil | Ölçüme dayalı performans iyileştirme: Core Web Vitals hedefleri, önce ölç → darboğazı bul → düzelt → doğrula (tut ya da geri al, geri alınan… | node, react, css | ✅ | 87 A | M 26KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `performance-profiling` | ⭐ tamamlayıcı | Performans profil çıkarma ilkeleri: Core Web Vitals hedefleri, taban → tespit → düzelt → doğrula süreci, sorun tipine göre araç seçimi (Ligh… | lighthouse, python, node | ✅ | 77 B | S 13KB | - | vudovn/ag-kit |
| `red-team-tactics` | ⭐ birincil | MITRE ATT&CK tabanlı kırmızı takım ilkeleri: saldırı yaşam döngüsü fazları ve amaçları, pasif/aktif keşif, ilk erişim vektörleri, Windows/Li… | api-anahtari | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `security-and-hardening` | ⭐ birincil | Kodu güvenlik açıklarına karşı sertleştirir: önce tehdit modeli, 'her zaman yap / önce sor / asla yapma' üç katmanlı sınır sistemi; enjeksiy… | node, html | ✅ | 95 A | M 30KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `server-management` | ⭐ birincil | Sunucu işletim ilkeleri: süreç yöneticisi seçimi (PM2, systemd, Docker, Kubernetes), izleme metrikleri ve uyarı seviyeleri, izleme aracı seç… | pm2, systemd, docker, node | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `shipping-and-launch` | ⭐ birincil | Üretime çıkış hazırlığı: kod kalitesi, güvenlik, performans, erişilebilirlik, altyapı ve dokümantasyon için ön yayın kontrol listesi; featur… | git, node, react, typescript | ✅ | 87 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `vulnerability-scanner` | ⭐ tamamlayıcı | Güvenlik açığı analizi ilkeleri: varsayılan ihlal, sıfır güven, derinlemesine savunma; OWASP Top 10:2025 (yeni A03 tedarik zinciri), saldırı… | python | ✅ | 77 B | S 35KB | - | vudovn/ag-kit |

### 07-framework-ozel

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_ · not: `notlar/b-yazilim-gelistirme/07-framework-ozel.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `bash-linux` | ⭐ birincil | macOS/Linux Bash kalıpları: komut zincirleme operatörleri, dosya işlemleri, süreç yönetimi (port tutan süreci bulma/öldürme), metin işleme (… | bash | ✅ | 69 B | S 4KB | - | vudovn/ag-kit |
| `next-bundle-optimizer` | ⭐ birincil | Next.js'te tarayıcının ilk yükleme işini denetler ve azaltır: varsayılan 'audit' kipinde next analyze ile anlık görüntü alıp dışa aktarır, m… | next.js, node | ✅ | 91 A | M 15KB | - | vercel/next.js |
| `next-cache-components-adoption` | ⭐ birincil | Next.js uygulamasında Cache Components'i açar ve ortaya çıkan engelleyici route'ları çözerek build'i geçirir: App Router ve app dizinini doğ… | next.js, react, typescript, playwright | ✅ | 97 A | L 40KB | - | vercel/next.js |
| `next-cache-components-optimizer` | ⭐ tamamlayıcı | Cache Components benimsenmiş Next.js 16.3+ uygulamasında bir route'un ilk yüklemede veya istemci geçişinde anında gösterdiği anlamlı UI'yi (… | next.js, playwright, typescript | ✅ | 99 A | M 50KB | - | vercel/next.js |
| `next-dev-loop` | ⭐ birincil | Vercel'in Next.js düzenle-doğrula döngüsü: kod değişikliğinden sonra uygulamanın çalışma anında gerçekten çalıştığını iki görünümle kanıtlar… | next.js, react, node, turbopack | ✅ | 99 A | M 9KB | - | vercel/next.js |
| `next-partial-prefetching-adoption` | ⭐ birincil | Next.js'te Partial Prefetching'i açar ve ortaya çıkan içgörüleri çözer: önce <Link prefetch={true}> gezinmelerini denetler, mevcut prefetch … | next.js, playwright, typescript | ✅ | 97 A | L 35KB | - | vercel/next.js |
| `next-partial-prefetching-optimizer` | ⭐ tamamlayıcı | Partial Prefetching altında seçili istemci gezinmelerinin tıklamadan önce neyi içereceğini optimize eder: her kaynak link/hedef için prefetc… | next.js, playwright | ✅ | 99 A | M 26KB | - | vercel/next.js |
| `nextjs-react-expert` | ⭐ alternatif | Vercel'in React/Next.js performans kurallarının ag-kit uyarlaması: 58 kural etki sırasına göre 8 dosyada, ek olarak Next.js 16 Cache Compone… | react, next.js, python | ✅ | 76 B | M 111KB | - | vudovn/ag-kit |
| `playwright-cli` | ⭐ birincil | Microsoft'un playwright-cli aracıyla tarayıcı otomasyonu: aç/git, snapshot'taki ref'lerle tıklama/yazma/doldurma/sürükleme/yükleme, metin ar… | playwright, node | ✅ | 90 A | M 68KB | - | microsoft/playwright |
| `powershell-windows` | ⭐ alternatif | Windows PowerShell tuzakları ve kalıpları: mantıksal operatörlerde cmdlet'i paranteze alma, betiklerde Unicode/emoji yasağı, null kontroller… | powershell, windows | ✅ | 77 B | S 4KB | - | vudovn/ag-kit |
| `rust-pro` | ⭐ birincil | Modern Rust (2024 sürümü) uzman persona tanımı: async (Tokio), axum, sahiplik/ömür, tip sistemi ve trait'ler, performans ve sistem programla… | rust, tokio, axum | ✅ | 69 B | S 8KB | - | vudovn/ag-kit |
| `vercel-composition-patterns` | ⭐ birincil | Vercel'in ölçeklenen React kompozisyon desenleri: boolean prop çoğalmasını compound component, state lifting ve iç yapıyı birleştirme ile ön… | react | ✅ | 87 A | S 49KB | claude:ayni | calesthio/OpenMontage |
| `vercel-react-best-practices` | ⭐ birincil | Vercel Engineering'in React/Next.js performans kuralları: etkiye göre 8 kategoride 65 kural (şelaleleri kaldırma, bundle boyutu, sunucu tara… | react, next.js | ✅ | 87 A | S 207KB | claude:ayni | calesthio/OpenMontage |

## Doküman ve İçerik

### 01-ofis-dokumanlari

_Word, Excel, PowerPoint, PDF üretme/düzenleme_ · not: `notlar/c-dokuman-icerik/01-ofis-dokumanlari.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `docx` | ⭐ birincil | Word (.docx/.dotx) belgelerini oluşturur, okur ve düzenler. Yeni belge için docx-js (npm), mevcut belge için unzip → XML düzenleme → zip akı… | node, python, docx-js, libreoffice | ✅ | 93 A | S 1102KB | - | anthropics/skills |
| `docx@composiohq` | alt alternatif | Anthropic docx skill'inin ComposioHQ deposundaki eski sürümü. docx-js ile yeni belge, Python 'Document' kütüphanesi (ooxml) ile düzenleme ve… | node, python, docx-js, libreoffice | ✅ | 76 B | M 1158KB | - | ComposioHQ/awesome-claude-skills |
| `pdf` | ⭐ birincil | PDF okuma, metin/tablo çıkarma, birleştirme, bölme, döndürme, filigran, form doldurma, şifreleme ve OCR işlerini Python (pypdf, pdfplumber, … | python | ✅ | 84 A | M 57KB | - | anthropics/skills |
| `pdf@composiohq` | alt alternatif | Anthropic pdf skill'inin ComposioHQ'daki eski kopyası: pypdf/pdfplumber/reportlab ile PDF okuma, çıkarma, birleştirme/bölme ve form doldurma… | python | ✅ | 77 B | S 63KB | - | ComposioHQ/awesome-claude-skills |
| `pptx` | ⭐ birincil | PowerPoint (.pptx/.potx) sunumlarını oluşturur, okur ve düzenler. Yeni deste için pptxgenjs, şablon/düzenleme için XML akışı kullanır; slayt… | node, python, pptxgenjs, libreoffice | ✅ | 92 A | M 1112KB | - | anthropics/skills |
| `pptx@composiohq` | alt alternatif | Anthropic pptx skill'inin eski sürümü (ComposioHQ). HTML slaytları playwright ile html2pptx dönüştürerek sunum üretir; şablonlu üretimde sla… | node, python, pptxgenjs, playwright, html | ✅ | 74 B | L 1201KB | - | ComposioHQ/awesome-claude-skills |
| `xlsx` | ⭐ birincil | Excel/CSV/TSV dosyalarını openpyxl ve pandas ile oluşturur, okur, düzenler ve temizler. Formül kullanımını zorunlu tutar, LibreOffice ile ye… | python, libreoffice | ✅ | 92 A | M 1077KB | - | anthropics/skills |
| `xlsx@composiohq` | alt alternatif | Anthropic xlsx skill'inin eski kopyası (ComposioHQ): formül zorunluluğu, finansal model renk/sayı biçimi kuralları, pandas/openpyxl örnekler… | python, libreoffice | ✅ | 76 B | M 18KB | - | ComposioHQ/awesome-claude-skills |

### 02-diyagram-dokumantasyon

_Diyagram, teknik dokümantasyon, ADR, ortak yazım_ · not: `notlar/c-dokuman-icerik/02-diyagram-dokumantasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `archify` | ⭐ birincil | Mimari, iş akışı, sequence, veri akışı, yaşam döngüsü, ERD, class, ağaç, zaman çizelgesi ve waterfall diyagramlarını doğrulanmış, temalı, an… | node, html, svg | ✅ | 93 A | M 7616KB | - | tt-a1i/archify |
| `beautiful-mermaid` | ⭐ alternatif | Mermaid diyagramlarını Beautiful Mermaid kütüphanesiyle temalı SVG'ye, ardından tarayıcı ekran görüntüsüyle yüksek çözünürlüklü PNG'ye çevir… | typescript, bun, mermaid, svg | ✅ | 87 A | S 19KB | claude:ayni | calesthio/OpenMontage |
| `doc-coauthoring` | ⭐ tamamlayıcı | Kullanıcıyla birlikte doküman (spec, öneri, karar dokümanı, PRD, RFC) yazmak için üç aşamalı bir süreç yürütür: bağlam toplama, bölüm bölüm … | markdown | ✅ | 92 A | M 15KB | - | anthropics/skills |
| `documentation-and-adrs` | ⭐ birincil | Kararları ve 'neden'i belgelemeyi öğretir: projedeki mevcut ADR düzenine uyarak ADR yazma, satır içi yorum kuralları, bilinen tuzakları belg… | markdown, typescript | ✅ | 95 A | M 11KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `documentation-templates` | ⭐ alternatif | README, endpoint bazlı API dokümanı, JSDoc/TSDoc yorumu, Keep-a-Changelog, kısa ADR ve llms.txt gibi AI dostu doküman için hazır şablonlar v… | markdown | ✅ | 76 B | S 3KB | - | vudovn/ag-kit |

### 03-yazi-iletisim-icerik

_Yazı, iletişim, pazarlama/içerik, kariyer_ · not: `notlar/c-dokuman-icerik/03-yazi-iletisim-icerik.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `competitive-ads-extractor` | ⭐ alternatif | Rakiplerin Facebook Ad Library, LinkedIn gibi reklam kütüphanelerindeki reklamlarını toplayıp mesaj, vurgulanan problem, hedef kitle ve krea… | web-arama, tarayici-otomasyonu | ✅ | 69 B | S 8KB | - | ComposioHQ/awesome-claude-skills |
| `content-research-writer` | ⭐ birincil | Blog, makale, bülten gibi içerikleri kullanıcıyla birlikte yazar: taslak/ana hat oluşturma, araştırma ve kaynak gösterme, giriş (hook) iyile… | markdown, web-arama | ✅ | 76 B | M 14KB | - | ComposioHQ/awesome-claude-skills |
| `de-ai-ify` | ⭐ tamamlayıcı | Metindeki yapay zekâ kokan kalıpları (aşırı geçiş kelimeleri, klişeler, kaçamak ifadeler, kurumsal jargon, üçlü sıralamalar) temizleyip doğa… | markdown | ✅ | 75 B | S 2KB | - | heyitsnoah/claudesidian |
| `developer-growth-analysis` | ⭐ alternatif | Son 24-48 saatlik Claude Code sohbet geçmişini (~/.claude/history.jsonl) okuyup kodlama kalıplarını, eksik alanları ve gelişim önerilerini ç… | claude-code, mcp, slack | ✅ | 68 B | M 15KB | - | ComposioHQ/awesome-claude-skills |
| `domain-name-brainstormer` | ⭐ alternatif | Proje için yaratıcı alan adı fikirleri üretir ve .com/.io/.dev/.ai gibi uzantılarda müsaitlik kontrolü yapılmasını tarif eder; marka açısınd… | web-arama | ✅ | 69 B | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `geo-fundamentals` | ⭐ tamamlayıcı | Generative Engine Optimization: içeriğin ChatGPT, Claude, Perplexity, Gemini gibi AI arama motorlarında kaynak gösterilmesi için ilkeler, al… | html, python | ✅ | 77 B | S 14KB | - | vudovn/ag-kit |
| `i18n-localization` | ⭐ birincil | Uluslararasılaştırma ve yerelleştirme kalıpları: react-i18next, next-intl, gettext örnekleri, locale dosya yapısı, çoğul/tarih/sayı biçimler… | react, next.js, python | ✅ | 77 B | S 12KB | - | vudovn/ag-kit |
| `internal-comms` | ⭐ birincil | Şirket içi iletişim metinleri yazar: 3P güncellemeleri (Progress/Plans/Problems), şirket bülteni, SSS cevapları, durum raporu, liderlik ve p… | markdown | ✅ | 85 A | S 22KB | - | anthropics/skills |
| `internal-comms@composiohq` | alt alternatif | Anthropic internal-comms skill'inin ComposioHQ'daki birebir kopyası: 3P güncellemesi, bülten, SSS ve genel iç iletişim yönergeleri. | markdown | ✅ | 77 B | S 22KB | - | ComposioHQ/awesome-claude-skills |
| `lead-research-assistant` | ⭐ birincil | Ürünü/kod tabanını analiz edip ideal müşteri profiline uyan şirketleri bulmayı, uygunluk puanıyla sıralamayı ve kişiselleştirilmiş iletişim … | web-arama | ✅ | 69 B | S 6KB | - | ComposioHQ/awesome-claude-skills |
| `meeting-insights-analyzer` | ⭐ birincil | Toplantı transkriptlerinden iletişim kalıplarını çıkarır: çatışmadan kaçınma, konuşma oranı, dolgu kelimeler, dinleme ve kolaylaştırma; zama… | markdown | ✅ | 76 B | M 10KB | - | ComposioHQ/awesome-claude-skills |
| `raffle-winner-picker` | ⭐ alternatif | Liste, CSV/Excel ya da Google Sheets'ten çekiliş/yarışma kazananını rastgele seçer; çoklu kazanan, tekrar engelleme, ağırlıklı seçim ve yede… | python | ✅ | 69 B | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `seo-fundamentals` | ⭐ birincil | SEO temelleri: E-E-A-T, Core Web Vitals hedefleri, teknik SEO (sitemap, robots, canonical), sayfa öğeleri, schema türleri, AI içerik kuralla… | html, python | ✅ | 77 B | S 9KB | - | vudovn/ag-kit |
| `tailored-resume-generator` | ⭐ birincil | İş ilanını analiz edip anahtar gereksinimleri çıkarır ve adayın deneyimini buna göre yeniden düzenleyen, ATS uyumlu, ilana özel özgeçmiş üre… | markdown | ✅ | 76 B | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `twitter-algorithm-optimizer` | ⭐ birincil | Twitter/X'in açık kaynak öneri algoritması bileşenlerine (Real-graph, SimClusters, TwHIN, Tweepcred) dayanarak tweet taslaklarını analiz edi… | markdown | ✅ | 76 B | M 13KB | - | ComposioHQ/awesome-claude-skills |

### 04-not-alma-bilgi-yonetimi

_Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni_ · not: `notlar/c-dokuman-icerik/04-not-alma-bilgi-yonetimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `add-frontmatter` | ⭐ tamamlayıcı | Obsidian notlarını (tek dosya ya da klasör) okuyup not türüne göre (toplantı, günlük, referans, proje) YAML frontmatter özellikleri ekler ve… | obsidian, markdown, yaml | ✅ | 75 B | S 4KB | - | heyitsnoah/claudesidian |
| `daily-review` | ⭐ tamamlayıcı | Gün sonu değerlendirmesi: bugün değişen/oluşan notları bulur, ilerlemeyi, takılan işleri ve içgörüleri çıkarır, yarının ilk 3 önceliğini ve … | obsidian, markdown | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `download-attachment` | ⭐ alternatif | Verilen URL'lerden dosyaları Obsidian kasasının 05_Attachments klasörüne indirir (yalnızca http/https, dosya adı temizleme, zaman aşımı), iç… | bash, obsidian | ✅ | 67 B | S 3KB | - | heyitsnoah/claudesidian |
| `file-organizer` | ⭐ birincil | Bilgisayardaki klasörleri (İndirilenler, Belgeler, projeler) analiz eder; kopya dosyaları bulur, mantıklı klasör yapısı önerir ve kullanıcı … | bash | ✅ | 76 B | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `inbox-processor` | ⭐ tamamlayıcı | Kasanın 00_Inbox klasöründeki notları PARA yöntemine göre (Projects/Areas/Resources/Archive/Sil) sınıflandırır; her not için hedef klasör, g… | obsidian, markdown | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `init-bootstrap` | ⭐ birincil | Claudesidian kasası için etkileşimli kurulum sihirbazı: klasör adı, bağımlılık kurulumu (pnpm/npm), git durumu, mevcut kasa yapısı ve çalışm… | obsidian, node, git | ✅ | 64 C | L 30KB | - | heyitsnoah/claudesidian |
| `install-claudesidian-command` | ⭐ tamamlayıcı | Kabuğa (bash/zsh/fish) `claudesidian` adlı bir alias/fonksiyon ekler: kasa klasörüne geçip `claude --resume` ile oturumu sürdürür ya da yeni… | bash, claude-code | 🟡 | 63 C | M 10KB | - | heyitsnoah/claudesidian |
| `invoice-organizer` | ⭐ tamamlayıcı | Fatura ve fişleri (PDF, taranmış görsel, e-posta eki) okuyup satıcı, tarih, tutar, fatura no gibi bilgileri çıkarır; `YYYY-AA-GG Satıcı - Fa… | python, pdf | ✅ | 76 B | M 12KB | - | ComposioHQ/awesome-claude-skills |
| `json-canvas` | ⭐ tamamlayıcı | Obsidian'ın kullandığı JSON Canvas 1.0 (.canvas) dosyalarını oluşturur ve düzenler: text/file/link/group düğümleri, kenarlar, renkler, yerle… | json, obsidian | ✅ | 74 B | M 14KB | - | heyitsnoah/claudesidian |
| `obsidian-bases` | ⭐ tamamlayıcı | Obsidian Bases (.base) dosyalarını oluşturur ve düzenler: tam YAML şeması, global/görünüm filtreleri, formül sözdizimi ve fonksiyon başvurus… | obsidian, yaml | ✅ | 74 B | M 16KB | - | heyitsnoah/claudesidian |
| `obsidian-markdown` | ⭐ birincil | Obsidian Flavored Markdown yazımı: wikilink, gömme (embed), callout, özellikler (properties), etiketler, blok referansları, LaTeX matematik … | obsidian, markdown | ✅ | 73 B | M 11KB | - | heyitsnoah/claudesidian |
| `research-assistant` | ⭐ birincil | Bir konuyu kasadaki notlar üzerinden araştırır: ilgili notları bulup okur, temaları, çelişkileri ve boşlukları çıkarır, wikilink'li bir araş… | obsidian, markdown | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `thinking-partner` | ⭐ birincil | Karmaşık bir problemi çözüme koşmadan sorularla birlikte düşünme modu: önce sorar, varsayımları yüzeye çıkarır, içgörüleri kaydeder, kasadak… | markdown | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |
| `upgrade` | ⭐ tamamlayıcı | claudesidian kurulumunu GitHub'daki son sürüme yükseltir: sürüm kontrolü, yedek, upstream çekme, dosya dosya anlamsal karşılaştırma ile kull… | git, bash, obsidian | 🟡 | 63 C | M 11KB | - | heyitsnoah/claudesidian |
| `weekly-synthesis` | ⭐ birincil | Haftanın notlarını ve çalışmalarını tarayıp tekrar eden temaları, içgörüleri, proje ilerlemesini, ortaya çıkan soruları, enerji denetimini v… | obsidian, markdown | ✅ | 67 B | S 2KB | - | heyitsnoah/claudesidian |

## AI ve Otomasyon

### 01-claude-api-mcp

_Claude API, MCP sunucusu, model geçişi_ · not: `notlar/d-ai-otomasyon/01-claude-api-mcp.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `academy-guide` | ⭐ birincil | Claude veya bir Claude ürününün nasıl kullanılacağına dair sorulara verilen cevabın sonuna, Claude Academy'den (academy.claude.com) yalnızca… | web-fetch | ✅ | 84 A | S 19KB | - | anthropics/skills |
| `claude-api` | ⭐ birincil | Claude API / Anthropic SDK için kapsamlı ve güncel başvuru: model kimlikleri ve fiyatlar, adaptive thinking, streaming, araç kullanımı, prom… | anthropic-sdk, python, typescript, go, java, csharp, php, ruby, curl | 🟡 | 86 A | L 2031KB | - | anthropics/skills |
| `claude-opus-4-5-migration` | alt alternatif | Sonnet 4.0/4.5 ve Opus 4.1'den Opus 4.5'e tek seferlik geçiş: platforma göre (Anthropic, Bedrock, Vertex, Azure) model dizgelerini değiştiri… | anthropic-sdk | ✅ | 69 B | S 12KB | - | anthropics/claude-code |
| `connect` | ⭐ birincil | Composio SDK (Python/TS) ile agent'ı Gmail, Slack, GitHub, Notion gibi 1000+ uygulamaya bağlar; e-posta gönderme, issue açma, mesaj atma gib… | composio, python, typescript, oauth | ✅ | 77 B | S 4KB | - | ComposioHQ/awesome-claude-skills |
| `connect-apps` | ⭐ alternatif | Claude Code'a `/plugin install composio-toolrouter` ile Composio Tool Router eklentisini kurup 1000+ uygulamada (Gmail, Slack, GitHub, Notio… | composio, claude-code, mcp | 🟡 | 66 B | S 2KB | - | ComposioHQ/awesome-claude-skills |
| `langsmith-fetch` | ⭐ birincil | LangChain/LangGraph agent'larını hata ayıklamak için langsmith-fetch CLI ile LangSmith'ten çalışma izlerini (trace) çeker; son etkinlik, bel… | langchain, langgraph, langsmith, python | ✅ | 76 B | M 11KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder` | ⭐ birincil | Yüksek kaliteli MCP sunucusu geliştirme rehberi: araştırma/planlama (araç adlandırma, bağlam yönetimi, hata mesajları), Python FastMCP veya … | mcp, python, typescript | ✅ | 92 A | M 119KB | - | anthropics/skills |
| `mcp-builder@composiohq` | alt alternatif | Anthropic mcp-builder'ın ComposioHQ'daki eski sürümü: 'iş akışı odaklı araç tasarımı' ilkeleri, ayrıntılı uygulama planı, dil rehberleri ve … | mcp, python, typescript | ✅ | 76 B | M 144KB | - | ComposioHQ/awesome-claude-skills |
| `mcp-builder@vudovn` | alt tamamlayıcı | MCP sunucu ve istemci mühendisliği: kararlı 2026-07-28 spesifikasyonuna göre durumsuz istek modeli, taşıma ve kimlik doğrulama, araç girdi/ç… | mcp, json-schema | ✅ | 84 A | M 10KB | - | vudovn/ag-kit |
| `mcp-integration` | ⭐ birincil | Claude Code eklentilerine MCP sunucusu paketleme rehberi: .mcp.json ya da plugin.json içinde mcpServers, stdio/SSE/HTTP/WebSocket sunucu tip… | mcp, claude-code, json | 🔵 | 76 B | M 46KB | - | anthropics/claude-code |

### 02-agent-orkestrasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_ · not: `notlar/d-ai-otomasyon/02-agent-orkestrasyon.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `batch-operations` | ⭐ birincil | Birçok dosyaya aynı değişikliği güvenle uygulama protokolü: deseni tanımla, önce grep ile etkilenen dosyaları önizle, toplu uygula, sonra do… | bash, git | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `behavioral-modes` | ⭐ alternatif | Görev türüne göre yedi çalışma modu tanımlar (brainstorm, implement, debug, review, teach, ship, orchestrate); her mod için davranış kuralla… | node, typescript | ✅ | 69 B | S 6KB | - | vudovn/ag-kit |
| `context-compression` | ⭐ tamamlayıcı | Uzun oturumlarda bağlamı sıkıştırma: büyük araç çıktılarını anlamsal özete indirme (mikro), biten iş aşamalarını özetleme ve oturum kontrol … | api-anahtari, next.js, typescript | ✅ | 77 B | S 5KB | - | vudovn/ag-kit |
| `context-engineering` | ⭐ birincil | Agent'a doğru bağlamı doğru zamanda verme: kalıcıdan geçiciye bağlam hiyerarşisi (kural dosyaları CLAUDE.md/AGENTS.md, spec, ilgili kaynak d… | markdown | ✅ | 95 A | M 15KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `coordinator-mode` | ⭐ alternatif | Koordinatör olarak çok agent'lı orkestrasyon: görevi ayrıştır, sınıflandır (araştırma/uygulama/doğrulama), okuma işlerini paralel yazma işle… | api-anahtari, typescript | ✅ | 85 A | S 8KB | - | vudovn/ag-kit |
| `diagnosing-superpowers` | ⭐ tamamlayıcı | Bir superpowers oturumu kötü gittiğinde (tekrar eden iş, yok sayılan plan, tetiklenmeyen skill, pahalılık) diskteki transkriptleri okuyup ka… | bash, jsonl | ✅ | 88 A | S 41KB | - | obra/superpowers |
| `discernment-nudge` | ⭐ birincil | Kullanıcının üzerine karar vereceği önemli bir cevap ya da taslaktan sonra, cevaptaki belirli noktalara bağlı 2-3 kısa takip sorusu ekler: ö… | html | ✅ | 84 A | M 21KB | - | anthropics/skills |
| `dispatching-parallel-agents` | ⭐ tamamlayıcı | Bağımsız 2+ problemi (farklı test dosyaları, alt sistemler) her birine izole bağlamlı ayrı bir agent vererek paralel çözme kalıbı: bağımsız … | typescript | ✅ | 96 A | S 6KB | - | obra/superpowers |
| `intelligent-routing` | ⭐ alternatif | Her kullanıcı isteğini sessizce analiz edip anahtar kelime/alan/karmaşıklığa göre uygun uzman agent'ı (security-auditor, frontend-specialist… | api-anahtari, css, docker, html, node | ✅ | 68 B | M 11KB | - | vudovn/ag-kit |
| `memory-system` | ⭐ birincil | Oturumlar arası kalıcı bellek: .agents/memory/MEMORY.md indeksi (en fazla 200 satır) ve konu dosyaları (kullanıcı tercihleri, proje kurallar… | markdown | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `parallel-agents` | ⭐ alternatif | Güvenli paralel agent kullanımı: ne zaman paralelleştirilir/paralelleştirilmez, çalışma ortamından bağımsız yetenek keşfi, güven sınırı, del… | react | ✅ | 77 B | S 6KB | - | vudovn/ag-kit |
| `subagent-driven-development` | ⭐ birincil | Yazılı uygulama planını görev başına taze bir uygulayıcı alt-agent göndererek yürütür; her görevden sonra spec uyumu + kod kalitesi inceleme… | git, bash | ✅ | 95 A | M 56KB | - | obra/superpowers |
| `using-agent-skills` | ⭐ birincil | addyosmani/agent-skills ailesinin meta-skill'i: işin geliştirme aşamasına göre hangi skill'in uygulanacağını gösteren karar ağacı (interview… | git | ✅ | 87 A | M 10KB | claude:ayni,agents:ayni | addyosmani/agent-skills |
| `using-superpowers` | ⭐ alternatif | superpowers ailesinin meta-skill'i: '%1 ihtimal bile varsa skill'i çağır' kuralı, süreç skillerinin önceliği, rasyonalizasyon kırmızı bayrak… | git | ✅ | 88 A | S 20KB | - | obra/superpowers |

### 03-web-arastirma-veri

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_ · not: `notlar/d-ai-otomasyon/03-web-arastirma-veri.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `agent-reach` | ⭐ birincil | İnternet erişimi için yönlendirici: 16 platformda (web arama/Exa, Twitter/X, Reddit, YouTube, Bilibili, Xiaohongshu, V2EX, LinkedIn, GitHub … | python, cli, web-arama | ✅ | 87 A | M 46KB | - | Panniantong/Agent-Reach |
| `notebooklm` | ⭐ tamamlayıcı | Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi)… | python, notebooklm, cli | ✅ | 85 A | M 16KB | claude:farkli | teng-lin/notebooklm-py |

### 04-skill-plugin-yazimi

_Skill yazma, plugin/hook/komut geliştirme_ · not: `notlar/d-ai-otomasyon/04-skill-plugin-yazimi.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `agent-development` | ⭐ birincil | Claude Code eklentileri için alt-agent (subagent) yazımı: Markdown + YAML frontmatter yapısı, name/description/model/color/tools alanları, <… | claude-code, markdown, yaml | 🔵 | 76 B | M 69KB | - | anthropics/claude-code |
| `command-development` | ⭐ birincil | Claude Code slash komutu yazımı: komut konumları (proje/kullanıcı/eklenti), YAML frontmatter (description, allowed-tools, model, argument-hi… | claude-code, markdown, yaml | 🔵 | 76 B | M 150KB | - | anthropics/claude-code |
| `hook-development` | ⭐ birincil | Claude Code hook'ları: prompt tabanlı (LLM kararlı) ve komut hook'ları, eklenti hooks.json ve settings biçimi, PreToolUse/PostToolUse/Stop/S… | claude-code, bash, json | 🔵 | 84 A | M 63KB | - | anthropics/claude-code |
| `plugin-settings` | ⭐ tamamlayıcı | Claude Code eklentilerinde kullanıcıya özel ayar ve durum saklama kalıbı: proje kökünde `.claude/<eklenti>.local.md` dosyası (YAML frontmatt… | claude-code, yaml, bash | 🔵 | 76 B | M 43KB | - | anthropics/claude-code |
| `plugin-structure` | ⭐ birincil | Claude Code eklenti mimarisi: dizin düzeni (.claude-plugin/plugin.json, commands, agents, skills, hooks, .mcp.json), manifest alanları ve bi… | claude-code, json | 🔵 | 84 A | M 73KB | - | anthropics/claude-code |
| `skill-creator` | ⭐ birincil | Skill oluşturma, iyileştirme ve ölçme: niyet yakalama ve görüşme, SKILL.md yazım rehberi (aşamalı açılım, sürpriz olmama ilkesi), test istem… | python, markdown | ✅ | 90 A | L 220KB | - | anthropics/skills |
| `skill-creator@composiohq` | alt alternatif | skill-creator'ın eski sürümü (ComposioHQ): skill anatomisi, aşamalı açılım ilkesi ve 6 adımlı süreç (örnekle anlama, içerik planlama, init_s… | python, markdown | ✅ | 76 B | M 38KB | - | ComposioHQ/awesome-claude-skills |
| `skill-creator@freshtechbro` | alt alternatif | skill-creator'ın eski sürümünün freshtechbro/claudedesignskills kopyası: skill anatomisi, aşamalı açılım ve init/package betikli 6 adımlı sü… | python, markdown | ✅ | 57 C | M 41KB | - | freshtechbro/claudedesignskills |
| `skill-creator@heyitsnoah` | alt alternatif | Anthropic skill-creator'ın güncel sürümünün claudesidian içindeki birebir kopyası (eval görüntüleyici, değerlendirici agent'lar, benchmark v… | python, markdown | ✅ | 64 C | L 221KB | - | heyitsnoah/claudesidian |
| `skill-development` | ⭐ alternatif | Claude Code eklentileri için skill yazım rehberi: skill anatomisi, aşamalı açılım, örnekle anlama → içerik planlama → yapı oluşturma → SKILL… | claude-code, markdown | 🔵 | 68 B | M 34KB | - | anthropics/claude-code |
| `skill-share` | ⭐ alternatif | Yeni skill iskeleti oluşturur, doğrular, zip paketler ve Rube (Composio) MCP üzerinden Slack kanalına paylaşır. | mcp, slack, composio | ✅ | 69 B | S 3KB | - | ComposioHQ/awesome-claude-skills |
| `skillify` | ⭐ alternatif | Tekrar eden çok adımlı iş akışlarını yeniden kullanılabilir SKILL.md'ye dönüştürür: kalıbı tanımla, şablondan SKILL.md üret, yerleştir, doğr… | markdown | ✅ | 77 B | S 3KB | - | vudovn/ag-kit |
| `template-skill` | alt alternatif | Boş skill şablonu: yalnızca name/description yer tutucuları ve 'talimatları buraya yaz' satırı. | markdown | ✅ | 61 C | S 0KB | - | ComposioHQ/awesome-claude-skills |
| `writing-hookify-rules` | ⭐ alternatif | hookify eklentisi için kural yazımı: `.claude/hookify.<kural>.local.md` dosyalarında YAML frontmatter (name, enabled, event: bash/file/stop/… | claude-code, yaml, regex | 🔵 | 76 B | M 8KB | - | anthropics/claude-code |
| `writing-skills` | ⭐ tamamlayıcı | Skill yazımını süreç dokümantasyonuna uygulanmış TDD olarak ele alır: önce alt-agent'larla baskı senaryosu çalıştırıp skill'siz başarısızlığ… | markdown, graphviz | ✅ | 95 A | M 107KB | - | obra/superpowers |

## Video, Ses ve AI Medya Üretimi

### 01-video-uretim-montaj

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_ · not: `notlar/g-video-ses-medya/01-video-uretim-montaj.md`

| Skill | Durum | Ne yapar | Teknoloji | Codex | Puan | Yük | Globalde | Kaynak |
|---|---|---|---|---|---|---|---|---|
| `captions-overlay` | ⭐ tamamlayıcı | embedded-captions iş akışının üzerine uygulanan overlay doktrini: altyazı modeli (at / ray / göm) ve altyazının filme bindirilen bir katman … | hyperframes, html, css | ✅ | 88 A | S 6KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `changelog-video` | ⭐ alternatif | Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka… | hyperframes, html, gsap, node, heygen | ✅ | 71 B | M 521KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `create-video` | ⭐ birincil | HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Ö… | heygen, api-anahtari, rest-api | ✅ | 87 A | S 92KB | claude:ayni | calesthio/OpenMontage |
| `embedded-captions` | ⭐ 🗄️emekli tamamlayıcı | Tek kişilik konuşan kafa videosuna görüntüyü düzenlemeden altyazı ekler: düz birebir altyazı, öznenin arkasına gömülü sinematik altyazı, VFX… | hyperframes, html, gsap, ffmpeg, whisper, python | 🟡 | 82 A | L 3421KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `faceless-explainer` | ⭐ 🗄️emekli tamamlayıcı | Makale, not, konu veya brief gibi düz metni yüzsüz (faceless) açıklayıcı videoya çevirir: yakalanacak site/görüntü olmadığı için görseller s… | hyperframes, html, gsap, node | 🟡 | 82 A | L 284KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `ffmpeg` | ⭐ tamamlayıcı | FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar… | ffmpeg | ✅ | 86 A | M 17KB | claude:ayni | calesthio/OpenMontage |
| `figma` | ⭐ tamamlayıcı | Figma içeriğini HyperFrames kompozisyonuna aktarır: render edilmiş varlıklar, marka token'ları, bileşenler (REST/CLI), bir SECTION içindeki … | hyperframes, figma-api, node | 🟡 | 85 A | S 11KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `general-video` | ⭐ 🗄️emekli birincil | Uzmanlaşmış bir iş akışına uymayan özel HyperFrames kompozisyonları için genel iş akışı: uzun veya çok sahneli işler, marka/sizzle reel, mon… | hyperframes, html, gsap, node | 🟡 | 84 A | M 36KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes` | ⭐ birincil | HyperFrames ekosisteminin zorunlu giriş noktası: proje durumunu okur, gerekirse niyet görüşmesi yapar, isteği girdi türüne göre tek bir iş a… | hyperframes, html, gsap, node | 🟡 | 93 A | S 1112KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-animation` | ⭐ alternatif | HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri ve GSAP, Lottie, T… | hyperframes, gsap, html, css, lottie, three.js | ✅ | 95 A | S 2521KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-animation@heygen-com-eski` | alt 🗄️emekli tamamlayıcı | HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri, 24 adlı metin efe… | hyperframes, gsap, html, css, lottie, three.js | 🟡 | 92 A | M 1240KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-audio` | ⭐ 🗄️emekli tamamlayıcı | Kompozisyona yerleşmiş sesin miksajı: fade/crossfade, iz kazancı, otomasyon zarfları, seslendirme altında müzik kısma (voiceover carve), EQ/… | hyperframes, html, web-audio, node | 🟡 | 82 A | L 100KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-cli` | ⭐ tamamlayıcı | HyperFrames CLI geliştirme döngüsü: init, add, capture, check (lint dahil), snapshot, preview, render (yerel, HeyGen bulut, AWS Lambda, Clou… | hyperframes, node, ffmpeg, aws-lambda, cloud-run | 🟡 | 85 A | S 120KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-cli@calesthio` | alt alternatif | HyperFrames CLI geliştirme döngüsü: init, add, lint, validate, inspect, preview, render, AWS Lambda render ve sorun giderme. Render öncesi l… | hyperframes, node, ffmpeg, docker, aws-lambda | ✅ | 86 A | M 54KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-core` | ⭐ alternatif | HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönetti… | hyperframes, html, gsap | ✅ | 95 A | S 78KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-core@heygen-com-eski` | alt 🗄️emekli birincil | HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönetti… | hyperframes, html, gsap | 🟡 | 92 A | M 98KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-creative` | ⭐ alternatif | HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, s… | hyperframes, html, css | ✅ | 95 A | S 1000KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-creative@heygen-com-eski` | alt 🗄️emekli tamamlayıcı | HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, s… | hyperframes, html, css | 🟡 | 93 A | S 1176KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-keyframes` | ⭐ 🗄️emekli tamamlayıcı | Seek-güvenli 2D/3D anahtar kare tarifleri: punch-in/out, zoom, yeniden çerçeveleme, Ken Burns, kamera hareketi, whip/match geçişleri, maske,… | hyperframes, gsap, css, svg, three.js | 🟡 | 84 A | M 23KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes-media` | ⭐ alternatif | Tek ses motoru (scripts/audio.mjs) ile HyperFrames için TTS (HeyGen/ElevenLabs/Kokoro), arka plan müziği, ses efekti, Whisper transkripsiyon… | hyperframes, node, heygen, elevenlabs, whisper | ✅ | 78 B | M 1396KB | claude:ayni | calesthio/OpenMontage |
| `hyperframes-registry` | ⭐ tamamlayıcı | HyperFrames kayıt defterindeki ~400 hazır blok ve bileşeni arar, 'hyperframes add' ile kurar ve kompozisyona bağlar; adı geçen bir görünüm/e… | hyperframes, html, node | 🟡 | 85 A | S 83KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `hyperframes-registry@calesthio` | alt alternatif | HyperFrames kayıt defterindeki hazır blok ve bileşenleri 'hyperframes add' ile kurar ve ana kompozisyona bağlar; yeni blok/bileşen yazıp üst… | hyperframes, html, node | ✅ | 87 A | S 49KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `hyperframes-studio` | ⭐ 🗄️emekli tamamlayıcı | HyperFrames Studio'da bir kişiyle birlikte çalışma kuralları: mesaj gerçekten değişiklik istiyor mu önce anla; yeni film için plan→storyboar… | hyperframes, html | 🟡 | 84 A | M 11KB | claude:ayni,codex:ayni,agents:ayni | heygen-com/hyperframes |
| `hyperframes@calesthio` | alt alternatif | HTML'den video render eden HyperFrames'in giriş ve yönlendirme skill'i: alt skillerin (core, animation, creative, media, cli, registry) hari… | hyperframes, html, gsap, node | ✅ | 94 A | M 20KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `media-use` | ⭐ birincil | HyperFrames projesinin medya işletim katmanı: BGM, SFX, görsel, ikon, marka logosu, ses, renk/LUT ihtiyacını tek 'resolve' komutuyla bulup y… | node, heygen, ffmpeg, api-anahtari | 🟡 | 85 A | S 1842KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `media-use@calesthio` | alt alternatif | BGM, ses efekti, görsel ve ikon ihtiyacını tek 'resolve' komutuyla HeyGen kataloğunda arayıp indirir, yerelde dondurur ve manifest'e kaydede… | node, heygen, api-anahtari | ✅ | 87 A | S 66KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `music-to-video` | ⭐ alternatif | Bir müzik parçasından vuruşa senkron HyperFrames videosu üretir: parçayı tek analizörle (beatgrid) çözümler, kareleri planlar, her kareyi ay… | hyperframes, python, html, gsap | ✅ | 86 A | M 6053KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `music-to-video@heygen-com-eski` | alt 🗄️emekli tamamlayıcı | Bir müzik parçasından (ses dosyası, sesi alınacak video veya ruh hali brief'inden üretilen parça) vuruşa senkron video üretir: lyric video, … | hyperframes, html, gsap, node | 🟡 | 84 A | M 6081KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `oversized-cursor` | ⭐ tamamlayıcı | Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasa… | hyperframes, gsap, css | ✅ | 88 A | S 6KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `playwright-recording` | ⭐ birincil | Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün tur… | playwright, typescript, node | ✅ | 86 A | M 20KB | claude:ayni | calesthio/OpenMontage |
| `pr-to-video` | ⭐ 🗄️emekli tamamlayıcı | GitHub pull request'ini (URL, owner/repo#N veya 'bu PR') kod değişikliği açıklayıcı videoya çevirir: changelog, özellik duyurusu, hata düzel… | hyperframes, html, gsap, node, github-cli | 🟡 | 82 A | L 358KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `product-launch-video` | ⭐ 🗄️emekli tamamlayıcı | Ürün/pazarlama URL'si, yapıştırılmış senaryo veya brief'ten ürün lansmanı/tanıtım videosu üretir: SaaS tanıtımları, özellik duyuruları, ürün… | hyperframes, html, gsap, node, playwright | 🟡 | 82 A | L 341KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `remotion` | ⭐ alternatif | claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch,… | remotion, react, typescript | ✅ | 71 B | S 16KB | claude:ayni | calesthio/OpenMontage |
| `remotion-best-practices` | ⭐ alternatif | Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile m… | remotion, react, typescript | ✅ | 94 A | S 112KB | claude:farkli,agents:farkli | calesthio/OpenMontage |
| `remotion-to-hyperframes` | ⭐ tamamlayıcı | Mevcut bir Remotion (React) kompozisyonunun kaynağını HyperFrames HTML'ine taşır; yalnızca açık taşıma isteğinde, tek yönlü. Eşlenebilen kal… | remotion, hyperframes, react, html, gsap | 🟡 | 85 A | S 170KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `remotion-to-hyperframes@calesthio` | alt alternatif | Mevcut bir Remotion (React) kompozisyonunu HyperFrames HTML'ine taşır; eşlenebilen kalıpları çevirir, useState/useEffect gibi uyumsuz kalıpl… | remotion, hyperframes, react, html, gsap | ✅ | 86 A | M 168KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `slideshow` | ⭐ tamamlayıcı | HyperFrames ile gezilebilir sunum/pitch deck yazar: ayrık slaytlar, parça parça açılma (fragment), dallanma, hotspot gezinme ve konuşmacı no… | hyperframes, html, gsap | 🟡 | 85 A | S 48KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `synthetic-screen-recording` | ⭐ alternatif | Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter ka… | remotion, react, typescript | ✅ | 78 B | M 10KB | claude:ayni | calesthio/OpenMontage |
| `talking-head-recut` | ⭐ 🗄️emekli tamamlayıcı | Mevcut konuşan kafa/röportaj/podcast videosunu transkripte senkron tasarlanmış grafik overlay kartlarıyla paketler: kinetik başlık, lower-th… | hyperframes, html, gsap, ffmpeg, whisper | 🟡 | 82 A | L 509KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `video-download` | ⭐ birincil | yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonları… | yt-dlp, ffmpeg | ✅ | 87 A | S 3KB | claude:ayni | calesthio/OpenMontage |
| `video-edit` | ⭐ birincil | ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, form… | ffmpeg | ✅ | 95 A | S 12KB | claude:ayni | calesthio/OpenMontage |
| `video-toolkit` | ⭐ alternatif | claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan ka… | remotion, python, node, modal, runpod | ✅ | 70 B | M 15KB | claude:ayni | calesthio/OpenMontage |
| `video-translate` | ⭐ birincil | HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve w… | heygen, api-anahtari, rest-api | ✅ | 86 A | M 11KB | claude:ayni | calesthio/OpenMontage |
| `video-understand` | ⭐ birincil | ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gere… | ffmpeg, python, whisper | ✅ | 87 A | S 27KB | claude:ayni | calesthio/OpenMontage |
| `website-to-video` | ⭐ alternatif | Bir web sitesini headless Chrome ile yakalayıp marka varlıklarıyla HyperFrames videosuna (site turu, vitrin, sosyal klip) dönüştüren 7 adıml… | hyperframes, html, node, chrome-headless | ✅ | 77 B | M 1541KB | claude:ayni | calesthio/OpenMontage |
| `youtube-downloader` | ⭐ alternatif | yt-dlp kullanan download_video.py betiğiyle YouTube videosu indirir: kalite (best…360p), format (mp4/webm/mkv) ve yalnızca ses (MP3) seçenek… | python, yt-dlp, ffmpeg | ✅ | 77 B | S 7KB | - | ComposioHQ/awesome-claude-skills |

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
| `cut-the-curve` | ⭐ tamamlayıcı | Hız eşlemeli sahne geçişleri kataloğu: zoom-through, ters zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut; ayrıca sahne içi … | gsap, hyperframes | ✅ | 95 A | M 28KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `manim-composer` | ⭐ tamamlayıcı | Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını so… | manim | ✅ | 87 A | S 22KB | claude:ayni | calesthio/OpenMontage |
| `manimce-best-practices` | ⭐ birincil | Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve y… | manim, python, latex | ✅ | 95 A | S 206KB | claude:ayni | calesthio/OpenMontage |
| `manimgl-best-practices` | ⭐ alternatif | ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşi… | manim, python, opengl, latex | ✅ | 86 A | S 729KB | claude:ayni | calesthio/OpenMontage |
| `motion-doctrine` | ⭐ birincil | Çok sahneli videonun bağımsız slaytlar yığını değil tek kesintisiz kamera hareketi gibi hissettirmesi için üst düzey hareket yasası: vektör … | hyperframes, gsap, node | ✅ | 87 A | M 44KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `motion-graphics` | ⭐ alternatif | Hareketin mesaj olduğu kısa (~10-30 sn), anlatımsız motion graphic üretimi: kinetik tipografi, sayı sayacı, grafik, logo sting, lower-third,… | hyperframes, html, gsap, ffmpeg | ✅ | 86 A | M 108KB | claude:farkli,codex:farkli,agents:farkli | calesthio/OpenMontage |
| `motion-graphics@heygen-com-eski` | alt 🗄️emekli tamamlayıcı | Hareketin mesaj olduğu kısa (genelde <10 sn, en çok ~30 sn), anlatımsız motion graphic üretimi: kinetik tipografi, sayaç, grafik, logo sting… | hyperframes, html, gsap, ffmpeg | 🟡 | 84 A | M 113KB | claude:farkli,codex:farkli,agents:farkli | heygen-com/hyperframes |
| `pose-library-design` | ⭐ tamamlayıcı | Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekle… | gsap, remotion | ✅ | 79 B | S 1KB | claude:ayni | calesthio/OpenMontage |
| `seam-craft` | ⭐ tamamlayıcı | Sahneden sahneye geçişlerin ana zaman çizelgesinde doğru birleşmesi için render önkoşulları: koyu filmlerde kesmede beyaz parlamayı önleyen … | hyperframes, html, css | ✅ | 80 A | S 5KB | claude:ayni,codex:ayni,agents:farkli | heygen-com/hyperframes |
| `svg-character-animation` | ⭐ birincil | SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pi… | svg, gsap, remotion, hyperframes | ✅ | 87 A | S 2KB | claude:ayni | calesthio/OpenMontage |
| `threejs-world-generation` | ⭐ birincil | Metinden veya yapılandırılmış özetten belirlenimci, düzenlenebilir Three.js dünyaları: arazi, semantik bölgeler, prosedürel biyomlar, landma… | three.js, hyperframes, openmontage, python, blender | ✅ | 86 A | M 16KB | claude:ayni | calesthio/OpenMontage |
| `visual-style` | ⭐ birincil | Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper… | markdown, html | ✅ | 87 A | S 81KB | claude:ayni | calesthio/OpenMontage |
