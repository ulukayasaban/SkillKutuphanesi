# Roller ve Profiller

> `araclar/katalog-uret.py` üretir (roller/*.json, profiller/*.json). Kullanım: `skill-ekle.py <proje> --profil <ad>` veya `--rol <ad>`.

## Profiller (21)

| Profil | Ne için | Roller |
|---|---|---|
| `3d-urun-sergisi` | 3D ürün tanıtımı / interaktif sergi | `ui-tasarimci`, `3d-gelistirici`, `scroll-deneyim`, `qa-erisilebilirlik` |
| `ai-uygulama` | Claude API / MCP kullanan uygulama | `ai-entegrasyon`, `frontend-muhendis`, `kod-inceleyici` |
| `ai-video-uretimi` | AI ile üretilmiş video (model seçimi, seslendirme, kurgu) | `ai-medya-uretici`, `video-kompozisyon`, `video-kurgu-render`, `ses-tasarimci` |
| `backend-api-servisi` | Backend / API servisi geliştirme | `backend-muhendis`, `kod-inceleyici` |
| `dashboard-saas` | Panel / SaaS uygulama arayüzü | `ui-tasarimci`, `tasarim-sistemi`, `frontend-muhendis`, `qa-erisilebilirlik` |
| `egitim-explainer` | Eğitim / açıklayıcı video | `motion-graphics-sanatcisi`, `ses-tasarimci`, `video-kompozisyon`, `video-kurgu-render` |
| `kurumsal-site` | Çok sayfalı kurumsal web sitesi | `ui-tasarimci`, `tasarim-sistemi`, `frontend-muhendis`, `qa-erisilebilirlik`, `icerik-pazarlama` |
| `landing-page` | Tek sayfalık tanıtım / ürün sayfası | `ui-tasarimci`, `motion-gelistirici`, `frontend-muhendis`, `qa-erisilebilirlik`, `icerik-pazarlama` |
| `marka-sunum` | Marka kimliği, sunum ve görsel materyal | `tasarim-sistemi`, `dokuman-yazari` |
| `mevcut-kod-iyilestirme` | Var olan kod tabanını inceleme ve sadeleştirme | `kod-inceleyici`, `planlayici`, `agent-orkestra` |
| `nextjs-web-uygulamasi` | Next.js web uygulaması | `nextjs-uzmani`, `ui-tasarimci`, `qa-erisilebilirlik` |
| `obsidian-bilgi-sistemi` | Obsidian not alma ve bilgi yönetimi sistemi | `bilgi-yoneticisi` |
| `oyun-gelistirme` | Oyun geliştirme (web, mobil, PC) | `oyun-gelistirici`, `qa-erisilebilirlik` |
| `rapor-dokuman` | Rapor, Word/Excel/PowerPoint/PDF çıktısı | `dokuman-yazari` |
| `scroll-hikaye-sitesi` | Scroll ile anlatılan hikâye / kampanya sitesi | `ui-tasarimci`, `scroll-deneyim`, `motion-gelistirici`, `qa-erisilebilirlik` |
| `skill-plugin-gelistirme` | Agent skill'i, Claude Code eklentisi, hook ve MCP entegrasyonu geliştirme | `skill-gelistirici`, `kod-inceleyici` |
| `sosyal-medya-icerik` | Kısa sosyal medya videoları ve görselleri | `ai-medya-uretici`, `video-kompozisyon`, `video-kurgu-render`, `icerik-pazarlama` |
| `tasarim-sistemi` | Design system / bileşen kütüphanesi kurulumu | `tasarim-sistemi`, `ui-tasarimci` |
| `urun-tanitim-videosu` | Ürün/özellik tanıtım videosu | `video-kompozisyon`, `video-kurgu-render`, `motion-graphics-sanatcisi`, `ses-tasarimci` |
| `webgl-gorsel-efekt` | WebGL / Three.js görsel efektli site | `3d-gelistirici`, `webgl-efekt-sanatcisi`, `qa-erisilebilirlik` |
| `yayin-devops` | CI/CD, yayın ve operasyon kurulumu | `devops-muhendis`, `kod-inceleyici` |

## Roller (25)

| Rol | Görevi | Çekirdek | Opsiyonel (`--opsiyonel`) | Yük |
|---|---|---|---|---|
| `3d-gelistirici` | Three.js / React Three Fiber sahnelerini kuran agent. | threejs-fundamentals, threejs-react-three-fiber, threejs-performance | threejs-materials, threejs-lighting, threejs-loaders | 6 skill, 148 KB |
| `agent-orkestra` | Yazılı bir planı alt-agent'lara dağıtıp yürüten, bağlamı yöneten koordinatör agent. | subagent-driven-development, dispatching-parallel-agents, context-engineering | context-compression, batch-operations | 5 skill, 48 KB |
| `ai-entegrasyon` | Claude API, MCP sunucusu ve web verisi entegrasyonlarını kuran agent. | claude-api, mcp-builder | mcp-builder@vudovn, agent-reach, connect | 5 skill, 134 KB |
| `ai-medya-uretici` | AI ile görsel ve video üreten agent (Kling, Seedance, Flux, Gemini Omni…). | ai-video-gen, seedance-2-0, flux-best-practices | bfl-api, gemini-omni, seedance-2-5, kling-official, minimax-h3, atlas-cloud, provider-model-refresh, comfyui, avatar-video | 12 skill, 99 KB |
| `backend-muhendis` | API, veritabanı ve sunucu tarafı iş mantığını yazan arka yüz mühendisi (Node.js/Python). | api-and-interface-design, database-design, security-and-hardening, test-driven-development, git-workflow-and-versioning, verification-before-completion | architecture, api-patterns, nodejs-best-practices, python-patterns, deprecation-and-migration, observability-and-instrumentation | 12 skill, 115 KB |
| `bilgi-yoneticisi` | Obsidian tabanlı not alma ve bilgi yönetimini kuran agent. | obsidian-markdown, obsidian-bases, json-canvas, daily-review, inbox-processor | research-assistant, thinking-partner, add-frontmatter, file-organizer, download-attachment, notebooklm, doc-coauthoring | 12 skill, 96 KB |
| `devops-muhendis` | CI/CD, deploy, izleme ve güvenlik taramasını kuran altyapı agent'ı. | ci-cd-and-automation, shipping-and-launch, observability-and-instrumentation, security-and-hardening | deployment-procedures, vulnerability-scanner, performance-optimization, git-workflow-and-versioning | 8 skill, 96 KB |
| `dokuman-yazari` | Rapor, sunum, diyagram ve teknik doküman hazırlayan agent. | docx, pptx, pdf, xlsx, archify, doc-coauthoring | documentation-and-adrs, beautiful-mermaid, internal-comms, de-ai-ify, discernment-nudge, slides | 12 skill, 108 KB |
| `frontend-muhendis` | Uygulama kodunu yazan ön yüz mühendisi (React/Next.js). | frontend-ui-engineering, frontend-design, frontend-architecture, test-driven-development, verification-before-completion | vercel-react-best-practices, next-dev-loop, tailwind-patterns, react-doctor, playwright-cli, d3-viz, web-artifacts-builder | 12 skill, 113 KB |
| `icerik-pazarlama` | Blog/makale, sosyal medya metni ve SEO/GEO odaklı web içeriği hazırlayan agent. | content-research-writer, de-ai-ify, seo-fundamentals | geo-fundamentals, twitter-algorithm-optimizer, agent-reach, notebooklm | 7 skill, 59 KB |
| `kod-inceleyici` | Kod inceleme, sadeleştirme ve test değeri kontrolü yapan agent. | code-review-and-quality, code-simplification, simplify-codebase, test-value, systematic-debugging, security-and-hardening | test-driven-development, constraint-driven-development, pragmatic-review, performance-optimization, requesting-code-review | 11 skill, 143 KB |
| `motion-gelistirici` | Animasyon ve mikro-etkileşimleri yazan agent (GSAP / Motion). | gsap-core, gsap-timeline, gsap-react, gsap-performance | gsap-plugins, gsap-utils, motion-framer, lottie-animations | 8 skill, 100 KB |
| `motion-graphics-sanatcisi` | Motion graphics, kinetik tipografi, geçiş ve açıklayıcı animasyon yapan agent. | hyperframes, motion-doctrine, visual-style, cut-the-curve | hyperframes-registry, seam-craft, oversized-cursor, manim-composer, manimce-best-practices, svg-character-animation | 10 skill, 71 KB |
| `nextjs-uzmani` | Next.js (App Router) uygulamalarını geliştiren, performansını ve yapısını iyileştiren agent. | nextjs-react-expert, next-dev-loop, vercel-react-best-practices, vercel-composition-patterns | next-bundle-optimizer, next-cache-components-optimizer, next-partial-prefetching-optimizer, react-doctor, tailwind-design-system | 9 skill, 97 KB |
| `oyun-gelistirici` | Oyun tasarımı ve geliştirmesini yapan agent (web, 2D, mobil, PC, çok oyunculu). | game-development, game-design, web-games, pixijs-2d | 2d-games, 3d-games, game-art, game-audio, multiplayer, mobile-games, pc-games, vr-ar | 12 skill, 56 KB |
| `planlayici` | İşi planlayan ve alt-agent'lara bölen orkestra agent'ı. | brainstorming, writing-plans, subagent-driven-development, requesting-code-review, verification-before-completion, using-git-worktrees | interview-me, spec-driven-development, executing-plans, finishing-a-development-branch, dispatching-parallel-agents, doubt-driven-development | 12 skill, 131 KB |
| `qa-erisilebilirlik` | Görsel QA, erişilebilirlik ve performans kontrolü yapan agent. | webapp-testing, playwright-cli | browser-testing-with-devtools, performance-optimization, impeccable, web-design-guidelines, playwright-trace, playwright-component-testing | 8 skill, 78 KB |
| `scroll-deneyim` | Scroll ile ilerleyen hikâye, pinlenen bölümler ve smooth scroll deneyimini kuran agent. | scroll-craft, gsap-scrolltrigger | locomotive-scroll, barba-js, scroll-reveal-libraries | 5 skill, 90 KB |
| `ses-tasarimci` | Seslendirme, müzik, ses efekti ve transkript işlerini yapan agent. | media-use, elevenlabs, speech-to-text, music, sound-effects | setup-api-key, lyria, text-to-speech, azure-text-to-speech, azure-speech-to-text, fish-audio-tts, dashscope | 12 skill, 73 KB |
| `skill-gelistirici` | Agent skill'i, Claude Code eklentisi, hook, slash komut ve alt-agent tanımı yazan agent. | skill-creator, writing-skills, plugin-structure | hook-development, command-development, agent-development, mcp-integration, writing-hookify-rules, plugin-settings | 9 skill, 139 KB |
| `tasarim-sistemi` | Design token, tema ve marka kimliğini kuran agent. | design-system, brand | theme-factory, banner-design, design-spec, design, tailwind-design-system | 7 skill, 64 KB |
| `ui-tasarimci` | Görsel dil, layout, tipografi ve renk kararlarını veren tasarımcı agent. Arayüzün 'AI şablonu' gibi görünmemesini sağlar. | design-taste-frontend, ui-ux-pro-max, impeccable | design-dna, frontend-design, ui-styling, mobile-design, design-spec, canvas-design | 9 skill, 127 KB |
| `video-kompozisyon` | HyperFrames ile videonun sahnelerini, kompozisyonunu ve medyasını kuran agent. | hyperframes, hyperframes-registry, media-use | captions-overlay, figma, slideshow, remotion-to-hyperframes | 7 skill, 37 KB |
| `video-kurgu-render` | HyperFrames projesini kontrol eden, zaman çizelgesini düzenleyen, render alan ve hazır videoları kurgulayan agent. | hyperframes, hyperframes-cli, video-edit, ffmpeg | media-use, playwright-recording, video-understand | 7 skill, 51 KB |
| `webgl-efekt-sanatcisi` | Three.js ile shader, post-processing ve özel geometri efektleri yapan agent (3d-gelistirici ile birlikte çalışır). | threejs-shaders, threejs-postprocessing, threejs-geometry | threejs-interaction, threejs-asset-pipeline, lightweight-3d-effects | 6 skill, 139 KB |
