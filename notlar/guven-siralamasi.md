# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-10-31, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

## 0. Bu dosyayı nasıl kullanırsın (karar kuralları)

İki ayrı puan var, ikisine birden bak:
- **Skill puanı** (0–100, A/B/C/D) — skill'in kendisi: bakım, lisans, Codex uyumu, bağlam yükü, yapı, elle kalite, trend + kaynağın GitHub güveninin 30 puanı.
- **Kaynak güveni** (0–100, A/B/C/D, `#sıra`) — skill'in geldiği GitHub reposunun etkileşimi: yıldız, yıldız hızı, katkıcı, son 90 gün commit, fork, izleyici, son sürüm, lisans; resmî üretici sadece 5 puan. Derece GÖRELİ (kütüphanedeki skill kaynakları arasındaki yer).

| Durum | Karar |
|---|---|
| Skill puanı ≥ 65 **ve** kaynak güveni A/B | Doğrudan aday |
| Skill puanı ≥ 65, kaynak güveni C | Aday; aynı işi yapan A/B kaynaklı skill varsa onu seç |
| Kaynak güveni D | Derece GÖRELİDİR: D = topluluk etkileşimi az (yeni/küçük repo), kalitesiz demek değil. Skill puanı ≥ 80 ise SKILL.md'yi okuyup "düşük topluluk güveni" diye işaretleyerek aday; < 80 ise sadece benzersiz bir iş yapıyorsa |
| Skill puanı < 50 ya da `kalite 1` (yönlendirme) | Alma |
| Aynı işi yapan iki aday | Önce skill puanı, eşitse kaynak güveni (sıra) yüksek olan; 🔥 trend eşitlikte öne geçirir |
| Projede bir referans kütüphanesi kullanılıyor (bölüm 3) | O kütüphanenin "ilgili skiller"i öncelikli aday; skill'in anlattığı sürüm projedekine uymalı |
| Ücret: 💲 ücretli | Ücret ödemeden kullanılamaz; sadece açıkça gerekiyorsa ve kullanıcıya belirterek |
| Lisans `yok`/`NOASSERTION` | Ticari projede kullanıcıya işaretle |

Skill kurulumu SADECE `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> … --kuru` → onay → `--evet`. Bir skill'in ayrıntısı: `KATALOG.md`, `registry.json` (id ile), SKILL.md (`registry.json` → `yol`).

## 1. Kategoriye göre en güvenilir kaynaklar ve en iyi skiller

| Kategori | En güvenilir kaynaklar (güven · o kategorideki skill) | En yüksek puanlı skiller (`id` puan/kaynak derecesi) |
|---|---|---|
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 88A (18) · nextlevelbuilder/ui-ux-pro-max-skill 85A (2) · anthropics/claude-code 83A (1) | `impeccable` 100/B, `design-taste-frontend` 100/B, `user-research` 100/B, `accessibility-review` 99/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 88A (17) · nextlevelbuilder/ui-ux-pro-max-skill 85A (4) · anthropics/skills 73B (2) | `tailwind-design-system` 96/B, `brand-extract` 94/A, `brandkit` 94/A, `stitch-design-taste` 94/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 88A (8) · calesthio/OpenMontage 73B (2) · greensock/gsap-skills 52C (7) | `emilkowalski-motion` 96/A, `motion-lab` 96/A, `animate` 94/A, `gpt-taste` 94/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 52C (1) · nateherkai/scroll-craft 46D (1) · freshtechbro/claudedesignskills 32D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 62/D, `locomotive-scroll` 62/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | nexu-io/open-design 88A (2) · CloudAI-X/threejs-skills 43D (13) · freshtechbro/claudedesignskills 32D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 88A (1) · pixijs/pixijs 75B (26) · Donchitos/Claude-Code-Game-Studios 57C (69) | `estimate` 97/C, `scope-check` 97/C, `asset-audit` 95/C, `help` 95/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 88A (17) · nextlevelbuilder/ui-ux-pro-max-skill 85A (1) · anthropics/claude-plugins-official 75B (1) | `playground` 100/B, `card-twitter` 96/A, `card-xiaohongshu` 96/A, `deck-guizang-editorial` 96/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 88A (7) · microsoft/playwright 83A (2) · addyosmani/agent-skills 83A (1) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 96/A, `impeccable-design-polish` 96/A, `agent-browser` 94/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 83A (8) · obra/superpowers 80A (3) · anthropics/claude-plugins-official 75B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `documentation` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 85A (6) · addyosmani/agent-skills 83A (2) · tt-a1i/archify 82A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 83A (2) · tt-a1i/archify 82A (1) · obra/superpowers 80A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 83A (2) · vudovn/ag-kit 56C (6) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `frontend-architecture` 83/C, `api-patterns` 76/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 88A (2) · addyosmani/agent-skills 83A (2) · obra/superpowers 80A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 93A (1) · addyosmani/agent-skills 83A (5) · anthropics/claude-plugins-official 75B (1) | `reverse-engineer-anything` 100/A, `security-and-hardening` 100/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 83A (1) · anthropics/claude-plugins-official 75B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 63C (33) · expo/skills 55C (24) · evanca/flutter-ai-rules 34D (35) | `agp-9-upgrade` 99/C, `android-profiler` 99/C, `anr-audit-and-fix` 99/C, `appfunctions` 99/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 88A (6) · anthropics/skills 73B (4) · anthropics/knowledge-work-plugins 71B (1) | `view-pdf` 100/B, `article-magazine` 96/A, `doc-kami-parchment` 96/A, `resume-modern` 96/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 88A (2) · addyosmani/agent-skills 83A (1) · tt-a1i/archify 82A (1) | `documentation-and-adrs` 100/A, `beautiful-mermaid` 97/B, `d3-visualization` 96/A, `data-report` 96/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 88A (5) · anthropics/skills 73B (1) · vercel-labs/agent-skills 64C (1) | `research-decision-room` 96/A, `writing-guidelines` 87/C, `yt-audit` 84/D, `yt-chapters` 84/D |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 61C (2) · heyitsnoah/claudesidian 36D (13) | `add-frontmatter` 72/D, `json-canvas` 70/D, `obsidian-bases` 70/D, `obsidian-markdown` 69/D |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 75B (4) · anthropics/skills 73B (3) · ComposioHQ/awesome-claude-skills 61C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-integration` 95/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 88A (3) · addyosmani/agent-skills 83A (2) · obra/superpowers 80A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 90A (1) · Panniantong/Agent-Reach 79B (1) · teng-lin/notebooklm-py 67B (1) | `graphify` 97/A, `agent-reach` 97/B, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 88A (2) · obra/superpowers 80A (1) · anthropics/claude-plugins-official 75B (7) | `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 96/A, `od-next-media-inputs` 96/A |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 82A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 88A (20) · heygen-com/hyperframes 86A (10) · remotion-dev/remotion 76B (13) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | nexu-io/open-design 88A (4) · calesthio/OpenMontage 73B (14) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | nexu-io/open-design 88A (22) · calesthio/OpenMontage 73B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 88A (2) · heygen-com/hyperframes 86A (3) · calesthio/OpenMontage 73B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `manim-composer` 97/B |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 71B (58) | `account-research` 100/B, `brand-voice-enforcement` 100/B, `call-prep` 100/B, `compose-outreach` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 71B (26) · Jakeschincariol/day-trader-skill 44D (11) | `interview-prep` 100/B, `journal-entry-prep` 100/B, `org-planning` 100/B, `recruiting-pipeline` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 71B (69) · Jakeschincariol/founder-skill 40D (11) | `brand-style` 100/B, `build-agent` 100/B, `call-list` 100/B, `close-month` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 71B (10) | `data-context-extractor` 100/B, `analyze` 99/B, `create-viz` 99/B, `data-visualization` 99/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 88A (1) · nexscope-ai/eCommerce-Skills 40D (156) · 40RTY-ai/shopify-admin-skills 39D (117) | `ecommerce-image-workflow` 94/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 76B (90) · anthropics/knowledge-work-plugins 71B (6) | `13c-metabolic-flux` 100/B, `adaptyv` 100/B, `aeon` 100/B, `alphagenome` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 76B (19) | `astropy` 100/B, `cantera` 100/B, `cirq` 100/B, `fluidsim` 100/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 76B (27) | `dask` 100/B, `exploratory-data-analysis` 100/B, `get-available-resources` 100/B, `hugging-science` 100/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 76B (37) | `autoskill` 100/B, `bgpt-paper-search` 100/B, `citation-management` 100/B, `consciousness-council` 100/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 76B (2) · earthtojake/text-to-cad 69B (12) | `fictiv` 100/B, `lab-hardware-cad` 100/B, `bambu-labs` 100/B, `dfam-check` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 93 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 413040 | 62782.1 | 354 | 5564 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 90 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 139598 | 20112.7 | 378 | 1333 | 2026-10-30 | 🔥 |
| 3 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143229 | 1183.8 | 4180 | 1547 | 2026-10-30 | 🔥 |
| 4 | react/react | 89 A | 0 | - | 0/0/0 | MIT | ✓ | 251804 | 1559.7 | 2028 | 137 | 2026-10-14 |  |
| 5 | nexu-io/open-design | 88 A | 139 | 03-ai-gorsel-video-modelleri (22), 01-video-uretim-montaj (20) | 112/5/22 | Apache-2.0 |  | 105084 | 17175.0 | 451 | 787 | 2026-10-22 |  |
| 6 | heygen-com/hyperframes | 86 A | 13 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 9/4/0 | Apache-2.0 | ✓ | 76157 | 9851.8 | 125 | 2985 | 2026-10-31 | 🔥 |
| 7 | DietrichGebert/ponytail | 85 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 181082 | 39041.8 | 133 | 163 | 2026-10-29 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 85 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143117 | 12987.3 | 106 | 79 | 2026-08-13 |  |
| 9 | addyosmani/agent-skills | 83 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112036 | 13201.1 | 96 | 383 | 2026-10-29 | 🔥 |
| 10 | anthropics/claude-code | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 153995 | 7599.8 | 59 | 243 | 2026-10-31 | 🔥 |
| 11 | microsoft/playwright | 83 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 98919 | 1183.0 | 827 | 730 | 2026-10-14 |  |
| 12 | tt-a1i/archify | 82 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 91911 | 14040.7 | 92 | 1635 | 2026-10-19 |  |
| 13 | obra/superpowers | 80 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 309563 | 24317.1 | 44 | 6 | 2026-10-21 | 🔥 |
| 14 | Panniantong/Agent-Reach | 79 B | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 106920 | 13053.7 | 38 | 110 | 2026-10-23 | 🔥 |
| 15 | pbakaus/impeccable | 79 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 97358 | 8480.5 | 61 | 1226 | 2026-10-26 | 🔥 |
| 16 | K-Dense-AI/scientific-agent-skills | 76 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55440 | 4470.5 | 58 | 95 | 2026-10-01 | 🔥 |
| 17 | Leonxlnx/taste-skill | 76 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 106476 | 12743.6 | 24 | 103 | 2026-10-24 | 🔥 |
| 18 | remotion-dev/remotion | 76 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 69197 | 906.3 | 478 | 5454 | 2026-10-26 | 🔥 |
| 19 | GoogleChrome/lighthouse | 75 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30986 | 242.2 | 397 | 184 | 2026-10-27 |  |
| 20 | anthropics/claude-plugins-official | 75 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45472 | 4006.8 | 42 | 1889 | - | 🔥 |
| 21 | pixijs/pixijs | 75 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48602 | 293.7 | 639 | 94 | 2026-10-01 |  |
| 22 | anthropics/skills | 73 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 185499 | 13958.3 | 17 | 15 | - |  |
| 23 | calesthio/OpenMontage | 73 B | 56 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/12/22 | AGPL-3.0 |  | 73578 | 10355.4 | 76 | 169 | - | 🔥 |
| 24 | anthropics/knowledge-work-plugins | 71 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34080 | 3686.9 | 32 | 605 | - | 🔥 |
| 25 | motiondivision/motion | 70 B | 0 | - | 0/0/0 | MIT | ✓ | 34686 | 362.9 | 147 | 1002 | - |  |
| 26 | earthtojake/text-to-cad | 69 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24387 | 3861.3 | 30 | 904 | 2026-10-30 | 🔥 |
| 27 | multica-ai/andrej-karpathy-skills | 67 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 227000 | 24912.6 | 7 | 0 | - |  |
| 28 | teng-lin/notebooklm-py | 67 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20017 | 2048.9 | 42 | 701 | 2026-10-29 |  |
| 29 | cloudflare/security-audit-skill | 64 C | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 54370 | 12243.3 | 4 | 3 | - | 🔥 |
| 30 | vercel-labs/agent-skills | 64 C | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33274 | 3093.4 | 28 | 23 | 2026-10-27 | 🔥 |
| 31 | android/skills | 63 C | 33 | 08-mobil-uygulama (33) | 32/1/0 | Apache-2.0 | ✓ | 10113 | 1342.5 | 8 | 39 | 2026-10-29 | 🔥 |
| 32 | Fei-Away/Codex-Dream-Skin | 62 C | 0 | - | 0/0/0 | MIT |  | 15263 | 4296.3 | 23 | 46 | 2026-10-15 |  |
| 33 | ComposioHQ/awesome-claude-skills | 61 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78372 | 6286.3 | 29 | 0 | - |  |
| 34 | lemomo-ai/lemo-opuscar | 61 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 9842 | 8548.5 | 4 | 72 | 2026-10-12 |  |
| 35 | cloudflare/skills | 58 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3226 | 301.8 | 48 | 254 | - | 🔥 |
| 36 | Donchitos/Claude-Code-Game-Studios | 57 C | 69 | 06-oyun-2d-grafik (69) | 69/0/0 | MIT |  | 30526 | 3555.5 | 1 | 5 | 2026-10-19 | 🔥 |
| 37 | vudovn/ag-kit | 56 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 860.1 | 10 | 8 | 2026-08-31 |  |
| 38 | czlonkowski/n8n-skills | 55 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6555 | 530.0 | 7 | 35 | 2026-10-24 | 🔥 |
| 39 | expo/skills | 55 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 3930 | 356.6 | 31 | 51 | - | 🔥 |
| 40 | darkroomengineering/satus | 52 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 210 | 2026-08-28 |  |
| 41 | greensock/gsap-skills | 52 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17604 | 2220.6 | 4 | 0 | - |  |
| 42 | Jakeschincariol/replica-skill | 48 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 6696 | 6696.0 | 1 | 1 | - |  |
| 43 | nateherkai/scroll-craft | 46 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4287 | 1861.8 | 1 | 16 | - |  |
| 44 | Jakeschincariol/youtube-agent-skill | 45 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3894 | 2630.6 | 1 | 1 | - |  |
| 45 | Jakeschincariol/day-trader-skill | 44 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 3704 | 3704.0 | 1 | 1 | - |  |
| 46 | Jakeschincariol/instagram-agent-skill | 44 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 3977 | 2518.8 | 1 | 2 | - |  |
| 47 | yaojingang/yao-meta-skill | 44 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2718 | 386.1 | 3 | 56 | - |  |
| 48 | CloudAI-X/threejs-skills | 43 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3875 | 413.3 | 1 | 20 | - |  |
| 49 | ythx-101/live-panel-skill | 41 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 827 | 827.0 | 4 | 40 | - |  |
| 50 | Jakeschincariol/founder-skill | 40 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2247 | 2247.0 | 1 | 1 | - |  |
| 51 | Jakeschincariol/linkedin-agent-skill | 40 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 2962 | 1667.5 | 1 | 1 | - |  |
| 52 | nexscope-ai/eCommerce-Skills | 40 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1304 | 174.6 | 7 | 1 | - |  |
| 53 | 40RTY-ai/shopify-admin-skills | 39 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 30.1 | 3 | 13 | 2026-06-17 |  |
| 54 | nexscope-ai/Amazon-Skills | 38 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 820 | 106.1 | 5 | 1 | - |  |
| 55 | zanwei/design-dna | 37 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2055 | 281.4 | 3 | 4 | - |  |
| 56 | heyitsnoah/claudesidian | 36 D | 18 | 04-not-alma-bilgi-yonetimi (13), 05-git-pr-surum (3) | 17/1/0 | MIT |  | 2607 | 191.4 | 3 | 0 | 2026-04-11 |  |
| 57 | evanca/flutter-ai-rules | 34 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 665 | 36.3 | 1 | 15 | - |  |
| 58 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 271 | 05-e-ticaret-pazaryeri (271) | 264/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 59 | hamen/compose_skill | 33 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 376 | 56.9 | 3 | 0 | 2026-07-07 |  |
| 60 | xjli360/sealeap-amazon-skills | 33 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 340 | 145.6 | 1 | 15 | - |  |
| 61 | freshtechbro/claudedesignskills | 32 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1190 | 97.5 | 1 | 0 | - |  |
| 62 | lemomo-ai/lemo-wake | 32 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 221 | 221.0 | 1 | 15 | 2026-10-05 |  |
| 63 | mercadopago/mercadopago-claude-marketplace | 32 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.9 | 10 | 15 | - |  |
| 64 | aldefy/compose-skill | 31 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | NOASSERTION |  | 598 | 74.2 | 5 | 0 | 2026-07-08 |  |
| 65 | Livsy90/iOS-Performance-Agent-Skills | 28 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 119 | 22.8 | 2 | 0 | 2026-07-12 |  |
| 66 | finsilabs/awesome-ecommerce-skills | 28 D | 175 | 05-e-ticaret-pazaryeri (175) | 157/18/0 | MIT |  | 60 | 7.8 | 4 | 3 | - |  |
| 67 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 115 | 94.5 | 1 | 11 | - |  |
| 68 | dpconde/claude-android-skill | 27 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 350 | 32.4 | 1 | 0 | - |  |
| 69 | Lonsdale201/wp-agent-skills | 23 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.3 | 3 | 29 | - |  |
| 70 | buluslan/ecommerce-competitor-analyzer | 23 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.7 | 1 | 3 | 2026-01-29 |  |
| 71 | dadederk/iOS-Accessibility-Agent-Skill | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 175 | 19.1 | 1 | 0 | - |  |
| 72 | Shopify/agent-skills | 22 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 99 | 14.1 | 1 | 0 | - |  |
| 73 | oldred-byte/ec-visual-skill | 22 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 17.2 | 1 | 0 | - |  |
| 74 | magendooro/magento-claude-skills | 19 D | 10 | 05-e-ticaret-pazaryeri (10) | 10/0/0 | MIT |  | 15 | 2.1 | 1 | 0 | - |  |
| 75 | mmiani/kotlin-kmp-claude-agent-skills | 19 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.4 | 1 | 8 | - |  |
| 76 | Trendyol/trendyol-integration-developer-tool | 17 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.9 | 3 | 0 | - |  |
| 77 | lemomo-ai/codex-radar | 17 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 8.0 | 1 | 8 | - |  |
| 78 | J-DTurner/etsy-api-skill | 14 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.7 | 1 | 0 | - |  |
| 79 | itsncki-design/app-store-submission-auditor | 13 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 34 | 4.6 | 1 | 0 | 2026-03-19 |  |
| 80 | vagabond911/aso-auditor | 13 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 33 | 4.9 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 86 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 79 B | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `web-artifacts-builder` 80/B, `saleor-storefront` 80/D, `nextjs-react` 78/D, `spree-admin-customization` 78/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 73 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | ManimCommunity/manim | 71 B | v0.22 | `manim-composer` 97/B, `manimce-best-practices` 100/B, `manimgl-best-practices` 96/B, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 5 | VoltAgent/awesome-design-md | 71 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 6 | d3/d3 | 71 B | v7.9 | `d3-viz` 96/B, `d3-visualization` 96/A | tasarim-teknolojileri.md |
| 7 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/B, `video-understand` 97/B, `azure-speech-to-text` 97/B | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 70 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 62/D, `blender-web-pipeline` 62/D, `web3d-integration-patterns` 62/D, `substance-3d-texturing` 54/D, `modern-web-design` 52/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 67 B | - | `latex-posters` 100/B, `scientific-writing` 100/B, `manim-composer` 97/B, `sympy` 100/B, `scientific-slides` 100/B, `venue-templates` 100/B, `manimce-best-practices` 100/B | kutuphaneler.md |
| 10 | blender/blender | 66 B | - | `blender-web-pipeline` 62/D, `3d-asset-generation` 97/B, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A | kutuphaneler.md |
| 11 | QwikDev/partytown | 65 B | v1.0 (T5) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 12 | dequelabs/axe-core | 65 B | v4.14 (MPL-2.0) | `accessibility-review` 99/B, `frontend-ui-engineering` 98/A, `replica-design` 84/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D, `platform-design` 66/A | tasarim-teknolojileri.md |
| 13 | 666ghj/MiroFish | 64 C | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 14 | librosa/librosa | 64 C | - | `media-use` 100/A | kutuphaneler.md |
| 15 | Tonejs/Tone.js | 63 C | 15.1 | `sound-effects` 100/B, `music` 100/B | tasarim-teknolojileri.md |
| 16 | DavidHDev/react-bits | 61 C | - | `animated-component-libraries` 62/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 17 | paperjs/paper.js | 61 C | v0.16 | `algorithmic-art` 71/B, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 18 | pmndrs/drei | 61 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 19 | darkroomengineering/lenis | 60 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 62/D | tasarim-teknolojileri.md |
| 20 | fontsource/fontsource | 60 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 21 | airbnb/lottie-web | 58 C | v5.13 | `lottie-animations` 62/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 78/D, `rive-interactive` 62/D | tasarim-teknolojileri.md |
| 22 | ai/size-limit | 57 C | 14.2 (T5) | `react-doctor` 76/C, `nextjs-react-expert` 75/C | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 55 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 97/B | tasarim-teknolojileri.md |
| 24 | liabru/matter-js | 52 C | 0.20 | `pixijs-2d` 70/D, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 25 | opentypejs/opentype.js | 52 C | 2.0 | `svg-character-animation` 97/B, `hyperframes` 100/A, `pixijs-scene-text` 90/B | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 51 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `relion` 100/B, `frame-logo-outro` 96/A, `threejs` 66/A | tasarim-teknolojileri.md |
| 27 | rough-stuff/rough | 48 D | v3.1 | `hand-drawn-diagrams` 66/A | tasarim-teknolojileri.md |
| 28 | barvian/number-flow | 47 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 47 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | figma/code-connect | 46 D | v2.0 | `figma-code-connect-components` 66/A | tasarim-teknolojileri.md |
| 31 | argyleink/open-props | 45 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 32 | greensock/GSAP | 45 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 44 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 42 D | v0.20 | `threejs-world-generation` 96/B, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 35 | metafizzy/zdog | 40 D | v1.1 | `svg-character-animation` 97/B, `canvas-procedural-animation` 89/B, `lightweight-3d-effects` 61/D | tasarim-teknolojileri.md |
| 36 | meyda/meyda | 39 D | - | `canvas-procedural-animation` 89/B | kutuphaneler.md |
| 37 | oframe/ogl | 39 D | - | `lightweight-3d-effects` 61/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 38 | zhuyansen/awesome-claude-video-skills | 38 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 39 | 14islands/r3f-scroll-rig | 35 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 62/D, `gpt-taste` 94/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 62/D, `barba-js` 62/D, `locomotive-scroll` 62/D, `scroll-reveal-libraries` 62/D | tasarim-teknolojileri.md |
| 40 | jwagner/simplex-noise.js | 34 D | 4.0 | `algorithmic-art` 71/B, `threejs-shaders` 79/D, `threejs-world-generation` 96/B | tasarim-teknolojileri.md |
| 41 | linvi/tweetinvi | 34 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 42 | nevertoday/350-layout-compositions | 33 D | - | `design-taste-frontend` 100/B, `canvas-design` 79/B, `slides` 82/A | tasarim-teknolojileri.md |
| 43 | pmndrs/react-three-a11y | 31 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 44 | arturitu/the-delegation | 24 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 45 | bytefer/awesome-nextjs | 23 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 46 | gchahal1982/pixeljury | 21 D | v0.1.5 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 47 | darkroomengineering/react-lenis | 13 D | v0.0.37 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 48 | haticesahin/SanalFuar | 12 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
