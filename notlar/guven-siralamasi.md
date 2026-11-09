# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-09, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 90A (13) · nextlevelbuilder/ui-ux-pro-max-skill 87A (2) · anthropics/claude-code 84A (1) | `impeccable` 100/A, `accessibility-review` 100/B, `design-critique` 100/B, `design-handoff` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 90A (3) · nextlevelbuilder/ui-ux-pro-max-skill 87A (4) · OpenMontageInc/OpenMontage 80A (1) | `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A, `tailwind-design-system` 93/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 90A (7) · OpenMontageInc/OpenMontage 80A (2) · github/awesome-copilot 75B (1) | `gsap-framer-scroll-animation` 100/B, `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 52C (1) · nateherkai/scroll-craft 44D (1) · freshtechbro/claudedesignskills 31D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 61/D, `locomotive-scroll` 61/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | openai/plugins 52C (2) · CloudAI-X/threejs-skills 42D (13) · freshtechbro/claudedesignskills 31D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 90A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 60C (68) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 90A (14) · nextlevelbuilder/ui-ux-pro-max-skill 87A (1) · OpenMontageInc/OpenMontage 80A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 90A (3) · microsoft/playwright 85A (2) · addyosmani/agent-skills 85A (1) | `playwright-trace` 100/A, `playwright-component-testing` 98/A, `export-download-debugging` 97/A, `impeccable-design-polish` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 85A (8) · mattpocock/skills 83A (30) · ruvnet/ruflo 83A (6) | `agent-implementer-sparc-coder` 100/A, `agent-sparc-coordinator` 100/A, `ask-matt` 100/A, `codebase-design` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 87A (6) · addyosmani/agent-skills 85A (2) · tt-a1i/archify 84A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 85A (2) · tt-a1i/archify 84A (1) · ruvnet/ruflo 83A (5) | `test-driven-development` 100/A, `agent-tdd-london-swarm` 100/A, `agent-test-long-runner` 100/A, `agent-tester` 100/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 85A (2) · ruvnet/ruflo 83A (5) · github/awesome-copilot 75B (2) | `api-and-interface-design` 100/A, `ddd-aggregate` 100/A, `ddd-context` 100/A, `ddd-validate` 100/A |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 90A (2) · addyosmani/agent-skills 85A (2) · ruvnet/ruflo 83A (13) | `git-workflow-and-versioning` 100/A, `agent-github-modes` 100/A, `agent-github-pr-manager` 100/A, `agentic-jujutsu` 100/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 85A (5) · ruvnet/ruflo 83A (22) | `reverse-engineer-anything` 100/A, `security-and-hardening` 100/A, `agent-benchmark-suite` 100/A, `agent-performance-analyzer` 100/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 85A (1) · anthropics/claude-plugins-official 76B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 61C (37) · expo/skills 53C (24) · evanca/flutter-ai-rules 33D (35) | `eas-app-stores` 96/C, `eas-observe` 96/C, `eas-workflows` 96/C, `expo-brownfield` 96/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 90A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 72B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 90A (2) · addyosmani/agent-skills 85A (1) · tt-a1i/archify 84A (1) | `documentation-and-adrs` 100/A, `adr-create` 100/A, `adr-index` 100/A, `adr-reindex` 100/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 90A (1) · anthropics/skills 74B (1) · blader/humanizer 73B (1) | `humanizer` 100/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 64C (2) · AgriciDaniel/claude-obsidian 62C (11) · kepano/obsidian-skills 61C (5) | `canvas` 89/C, `think` 89/C, `wiki-cli` 89/C, `wiki-fold` 89/C |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | ruvnet/ruflo 83A (5) · anthropics/claude-plugins-official 76B (4) · anthropics/skills 74B (3) | `chat-format` 100/A, `deepseek-chat` 100/A, `deepseek-reason` 100/A, `llm-config` 100/A |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 90A (2) · JuliusBrussee/caveman 86A (22) · addyosmani/agent-skills 85A (2) | `context-engineering` 100/A, `add-model-descriptions` 100/A, `agent-adaptive-coordinator` 100/A, `agent-agent` 100/A |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 92A (1) · ruvnet/ruflo 83A (16) · Panniantong/Agent-Reach 80A (1) | `browser` 100/A, `browser-auth-flow` 100/A, `browser-extract` 100/A, `browser-form-fill` 100/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 90A (2) · heygen-com/hyperframes 89A (1) · ruvnet/ruflo 83A (4) | `reverse-any-video` 100/A, `create-mod` 100/A, `create-plugin` 100/A, `skill-builder` 100/A |
| `e-entegrasyon-katalogu/01-uygulama-entegrasyonlari` — Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Co | github/awesome-copilot 75B (460) · openai/plugins 52C (449) | `acquire-codebase-knowledge` 100/B, `acreadiness-assess` 100/B, `acreadiness-generate-instructions` 100/B, `acreadiness-policy` 100/B |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 84A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 90A (17) · heygen-com/hyperframes 89A (10) · harry0703/MoneyPrinterTurbo 85A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | ruvnet/ruflo 83A (7) · OpenMontageInc/OpenMontage 80A (14) · krillinai/OpenCreator 64C (7) | `music-connect` 100/A, `music-generate` 100/A, `music-get` 100/A, `music-list` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 80A (17) · avenoxai/higgsfield-studio 12D (5) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 90A (2) · heygen-com/hyperframes 89A (3) · OpenMontageInc/OpenMontage 80A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 79B (48) · anthropics/knowledge-work-plugins 72B (58) · AgriciDaniel/claude-seo 69B (25) | `ab-testing` 100/B, `analytics` 100/B, `aso` 100/B, `attribution` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | ruvnet/ruflo 83A (10) · anthropics/knowledge-work-plugins 72B (26) · Jakeschincariol/day-trader-skill 46D (11) | `market-ingest` 100/A, `market-pattern` 100/A, `trader-backtest` 100/A, `trader-cloud-backtest` 100/A |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 72B (69) · Jakeschincariol/founder-skill 39D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 72B (10) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 90A (1) · nexscope-ai/eCommerce-Skills 39D (156) · 40RTY-ai/shopify-admin-skills 39D (117) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 77B (90) · anthropics/knowledge-work-plugins 72B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 77B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 77B (27) · Orchestra-Research/AI-Research-SKILLs 55C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 77B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 68B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 77B (2) · earthtojake/text-to-cad 71B (12) | `bambu-labs` 100/B, `dfam-check` 100/B, `dfm` 100/B, `gcode` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 430844 | 62668.2 | 362 | 5773 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 92 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 142439 | 19682.5 | 391 | 1481 | 2026-11-03 | 🔥 |
| 3 | nexu-io/open-design | 90 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 105947 | 16516.9 | 451 | 717 | 2026-11-04 |  |
| 4 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143324 | 1181.7 | 4184 | 1549 | 2026-11-04 | 🔥 |
| 5 | heygen-com/hyperframes | 89 A | 14 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/1 | Apache-2.0 | ✓ | 78940 | 9835.1 | 126 | 3031 | 2026-11-04 | 🔥 |
| 6 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 251960 | 1557.8 | 2027 | 134 | 2026-10-14 |  |
| 7 | DietrichGebert/ponytail | 87 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 184540 | 37400.1 | 133 | 163 | 2026-10-29 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 87 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 145229 | 12834.2 | 110 | 81 | 2026-08-13 |  |
| 9 | JuliusBrussee/caveman | 86 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 117512 | 16312.2 | 104 | 1619 | 2026-10-23 |  |
| 10 | addyosmani/agent-skills | 85 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 113281 | 12897.9 | 97 | 392 | 2026-10-31 | 🔥 |
| 11 | harry0703/MoneyPrinterTurbo | 85 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 141094 | 4408.3 | 169 | 554 | 2026-11-07 | 🔥 |
| 12 | microsoft/playwright | 85 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 99306 | 1183.4 | 828 | 733 | 2026-10-14 | 🔥 |
| 13 | anthropics/claude-code | 84 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154554 | 7517.5 | 59 | 247 | 2026-11-04 | 🔥 |
| 14 | tt-a1i/archify | 84 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 93462 | 13659.8 | 92 | 1628 | 2026-10-19 |  |
| 15 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 313295 | 34136.8 | 8 | 133 | 2026-10-29 | 🔥 |
| 16 | ruvnet/ruflo | 83 A | 305 | 02-agent-orkestrasyon (199), 06-devops-guvenlik-performans (22) | 292/8/5 | MIT |  | 81282 | 4706.6 | 95 | 2949 | 2026-11-09 | 🔥 |
| 17 | pbakaus/impeccable | 82 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 102802 | 8729.6 | 62 | 1203 | 2026-10-26 | 🔥 |
| 18 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 312440 | 23985.3 | 44 | 7 | 2026-11-03 | 🔥 |
| 19 | OpenMontageInc/OpenMontage | 80 A | 57 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/13/22 | AGPL-3.0 |  | 78702 | 10633.5 | 129 | 368 | - | 🔥 |
| 20 | Panniantong/Agent-Reach | 80 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 108808 | 12820.8 | 46 | 104 | 2026-11-01 | 🔥 |
| 21 | Leonxlnx/taste-skill | 79 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 110057 | 12721.4 | 24 | 152 | 2026-11-04 | 🔥 |
| 22 | coreyhaines31/marketingskills | 79 B | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 58521 | 5969.9 | 57 | 961 | 2026-10-30 | 🔥 |
| 23 | upstash/context7 | 79 B | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 64385 | 3300.7 | 147 | 253 | 2026-11-06 |  |
| 24 | remotion-dev/remotion | 78 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 70754 | 923.1 | 490 | 5575 | 2026-11-02 | 🔥 |
| 25 | K-Dense-AI/scientific-agent-skills | 77 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 56104 | 4418.6 | 58 | 94 | 2026-10-01 | 🔥 |
| 26 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48622 | 293.3 | 639 | 94 | 2026-10-01 |  |
| 27 | GoogleChrome/lighthouse | 76 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31017 | 241.9 | 397 | 192 | 2026-10-27 |  |
| 28 | anthropics/claude-plugins-official | 76 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 46120 | 3960.6 | 42 | 1732 | - | 🔥 |
| 29 | github/awesome-copilot | 75 B | 469 | 01-uygulama-entegrasyonlari (460), 02-kod-kalitesi-review (2) | 458/10/1 | MIT |  | 40799 | 2403.7 | 578 | 885 | - | 🔥 |
| 30 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 187417 | 13795.3 | 17 | 15 | - | 🔥 |
| 31 | cathrynlavery/diagram-design | 74 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 65003 | 9546.3 | 66 | 397 | - |  |
| 32 | blader/humanizer | 73 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 64838 | 6681.6 | 24 | 60 | 2026-09-28 | 🔥 |
| 33 | anthropics/knowledge-work-plugins | 72 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34734 | 3641.1 | 32 | 563 | - | 🔥 |
| 34 | earthtojake/text-to-cad | 71 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 25423 | 3845.1 | 32 | 876 | 2026-11-03 | 🔥 |
| 35 | motiondivision/motion | 70 B | 0 | - | 0/0/0 | MIT | ✓ | 34907 | 364.0 | 147 | 1009 | - |  |
| 36 | AgriciDaniel/claude-seo | 69 B | 25 | 01-satis-pazarlama-musteri (25) | 25/0/0 | MIT |  | 26654 | 2946.5 | 30 | 209 | 2026-10-22 | 🔥 |
| 37 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20096 | 1996.5 | 42 | 650 | 2026-10-29 |  |
| 38 | google/elephant-goldfish-model | 68 B | 7 | 01-planlama-metodoloji (7) | 7/0/0 | Apache-2.0 |  | 11801 | 6293.9 | 29 | 149 | 2026-10-27 |  |
| 39 | wanshuiyin/Auto-claude-code-research-in-sleep | 68 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 18651 | 2323.7 | 106 | 205 | 2026-09-28 |  |
| 40 | multica-ai/andrej-karpathy-skills | 67 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 229500 | 24394.4 | 7 | 0 | - | 🔥 |
| 41 | cloudflare/security-audit-skill | 66 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 59355 | 12530.5 | 4 | 3 | - | 🔥 |
| 42 | vercel-labs/agent-skills | 66 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33547 | 3035.2 | 28 | 23 | 2026-10-27 | 🔥 |
| 43 | Nutlope/hallmark | 65 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 47913 | 7431.4 | 10 | 138 | - | 🔥 |
| 44 | ComposioHQ/awesome-claude-skills | 64 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78745 | 6169.7 | 29 | 0 | - |  |
| 45 | Vincentwei1021/video-shotcraft | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 16988 | 4570.2 | 14 | 44 | 2026-09-01 | 🔥 |
| 46 | krillinai/OpenCreator | 64 C | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14157 | 621.9 | 36 | 458 | 2026-11-03 |  |
| 47 | AgriciDaniel/claude-obsidian | 62 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16171 | 2275.9 | 11 | 108 | 2026-10-21 |  |
| 48 | Fei-Away/Codex-Dream-Skin | 62 C | 0 | - | 0/0/0 | MIT |  | 15329 | 3982.9 | 23 | 44 | 2026-10-15 |  |
| 49 | dreammis/social-auto-upload | 62 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16118 | 457.5 | 42 | 46 | 2026-10-22 |  |
| 50 | lemomo-ai/lemo-opuscar | 62 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 12273 | 8479.5 | 4 | 80 | 2026-10-12 |  |
| 51 | android/skills | 61 C | 37 | 08-mobil-uygulama (37) | 36/1/0 | Apache-2.0 | ✓ | 10337 | 1320.4 | 8 | 36 | 2026-11-04 | 🔥 |
| 52 | kepano/obsidian-skills | 61 C | 6 | 04-not-alma-bilgi-yonetimi (5), 02-diyagram-dokumantasyon (1) | 6/0/0 | MIT |  | 50753 | 4961.1 | 17 | 3 | - |  |
| 53 | Donchitos/Claude-Code-Game-Studios | 60 C | 68 | 06-oyun-2d-grafik (68) | 68/0/0 | MIT |  | 35403 | 3986.1 | 1 | 5 | 2026-10-19 | 🔥 |
| 54 | zarazhangrui/frontend-slides | 58 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 31888 | 3401.4 | 9 | 0 | 2026-05-26 |  |
| 55 | cloudflare/skills | 57 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3279 | 298.4 | 48 | 261 | - | 🔥 |
| 56 | zubair-trabzada/geo-seo-claude | 56 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11511 | 1325.5 | 25 | 77 | - |  |
| 57 | AgriciDaniel/claude-ads | 55 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 10746 | 1205.5 | 2 | 43 | 2026-10-16 |  |
| 58 | Orchestra-Research/AI-Research-SKILLs | 55 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14269 | 1169.2 | 17 | 0 | 2026-06-16 |  |
| 59 | vudovn/ag-kit | 54 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8207 | 834.4 | 10 | 8 | 2026-08-31 |  |
| 60 | czlonkowski/n8n-skills | 53 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6589 | 520.3 | 7 | 33 | 2026-10-24 | 🔥 |
| 61 | expo/skills | 53 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4050 | 357.9 | 31 | 45 | - | 🔥 |
| 62 | greensock/gsap-skills | 52 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17884 | 2174.7 | 4 | 0 | - |  |
| 63 | openai/plugins | 52 C | 463 | 01-uygulama-entegrasyonlari (449), 06-devops-guvenlik-performans (5) | 436/27/0 | yok | ✓ | 7752 | 942.6 | 62 | 10 | - |  |
| 64 | darkroomengineering/satus | 51 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.5 | 19 | 152 | 2026-08-28 |  |
| 65 | Leonxlnx/earshot | 50 C | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 3898 | 3898.0 | 1 | 40 | 2026-10-22 |  |
| 66 | Ryze-AI-Adgent/open-seo-mcp-skills | 50 C | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 8815 | 3721.9 | 1 | 16 | - |  |
| 67 | Jakeschincariol/replica-skill | 47 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 7640 | 6277.2 | 1 | 1 | - |  |
| 68 | Jakeschincariol/day-trader-skill | 46 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 5296 | 5296.0 | 1 | 1 | - |  |
| 69 | hardikpandya/stop-slop | 46 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 18619 | 1874.2 | 2 | 0 | - |  |
| 70 | feitangyuan/onetake | 45 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 3959 | 2735.3 | 2 | 21 | 2026-10-08 |  |
| 71 | Jakeschincariol/youtube-agent-skill | 44 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 4562 | 2568.2 | 1 | 1 | - |  |
| 72 | nateherkai/scroll-craft | 44 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4529 | 1742.8 | 1 | 16 | - |  |
| 73 | Jakeschincariol/instagram-agent-skill | 43 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4849 | 2586.1 | 1 | 2 | - |  |
| 74 | yaojingang/yao-meta-skill | 43 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2719 | 370.7 | 3 | 56 | - |  |
| 75 | CloudAI-X/threejs-skills | 42 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3985 | 412.1 | 1 | 20 | - |  |
| 76 | sarpstar/cinecode | 41 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 1614 | 1614.0 | 3 | 7 | - |  |
| 77 | ythx-101/live-panel-skill | 40 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 840 | 690.2 | 4 | 40 | - |  |
| 78 | 40RTY-ai/shopify-admin-skills | 39 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 28.8 | 3 | 13 | 2026-06-17 |  |
| 79 | Jakeschincariol/founder-skill | 39 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2452 | 2258.8 | 1 | 1 | - |  |
| 80 | Jakeschincariol/linkedin-agent-skill | 39 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3205 | 1546.5 | 1 | 1 | - |  |
| 81 | nexscope-ai/eCommerce-Skills | 39 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1332 | 171.6 | 7 | 1 | - |  |
| 82 | kylezantos/design-motion-principles | 37 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1528 | 155.4 | 1 | 0 | 2026-05-21 |  |
| 83 | lottiefiles/motion-design-skill | 37 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 2853 | 358.4 | 1 | 0 | - |  |
| 84 | nexscope-ai/Amazon-Skills | 37 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 834 | 103.9 | 5 | 1 | - |  |
| 85 | heyitsnoah/claudesidian | 36 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2606 | 187.3 | 3 | 0 | 2026-04-11 |  |
| 86 | zanwei/design-dna | 36 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2079 | 273.6 | 3 | 4 | - |  |
| 87 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 272 | 05-e-ticaret-pazaryeri (272) | 265/7/0 | MIT |  | 40 | 4.9 | 3 | 11 | 2026-05-13 |  |
| 88 | evanca/flutter-ai-rules | 33 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 669 | 35.9 | 1 | 13 | - |  |
| 89 | hamen/compose_skill | 33 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 378 | 54.7 | 3 | 0 | 2026-07-07 |  |
| 90 | rshankras/claude-code-apple-skills | 33 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 861 | 69.6 | 2 | 3 | - |  |
| 91 | xjli360/sealeap-amazon-skills | 33 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 369 | 140.2 | 1 | 15 | - |  |
| 92 | RevenueCat/play-billing-skills | 32 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 11.4 | 1 | 15 | 2026-10-15 |  |
| 93 | lemomo-ai/lemo-wake | 32 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 256 | 210.3 | 1 | 15 | 2026-10-05 |  |
| 94 | freshtechbro/claudedesignskills | 31 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1248 | 99.8 | 1 | 0 | - |  |
| 95 | tuist/fuckingapproachableswiftconcurrency | 31 D | 0 | - | 0/0/0 | MIT |  | 158 | 14.9 | 15 | 0 | - |  |
| 96 | mercadopago/mercadopago-claude-marketplace | 30 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.8 | 10 | 7 | - |  |
| 97 | moiz-za/etsy-seller-seo-system | 30 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 47 | 8.1 | 2 | 13 | 2026-10-23 |  |
| 98 | twostraws/SwiftData-Agent-Skill | 30 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 463 | 57.9 | 2 | 1 | 2026-03-11 |  |
| 99 | xianyu110/ecommerce-image-skills | 29 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 144 | 121.6 | 1 | 7 | - |  |
| 100 | xjli360/sealeap-ecommerce-skills | 29 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 137 | 90.5 | 1 | 11 | - |  |
| 101 | Livsy90/iOS-Performance-Agent-Skills | 28 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 120 | 21.7 | 2 | 0 | 2026-07-12 |  |
| 102 | ehmo/platform-design-skills | 28 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 640 | 69.2 | 1 | 0 | - |  |
| 103 | finsilabs/awesome-ecommerce-skills | 28 D | 178 | 05-e-ticaret-pazaryeri (178) | 160/18/0 | MIT |  | 63 | 7.9 | 4 | 3 | - |  |
| 104 | dpconde/claude-android-skill | 27 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 352 | 31.8 | 1 | 0 | - |  |
| 105 | ParthJadhav/ios-marketing-capture | 26 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 265 | 37.8 | 1 | 1 | - |  |
| 106 | Lonsdale201/wp-agent-skills | 23 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.1 | 3 | 25 | - |  |
| 107 | MADTeacher/mad-agents-skills | 23 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.2 | 2 | 0 | - |  |
| 108 | dadederk/iOS-Accessibility-Agent-Skill | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 176 | 18.6 | 1 | 0 | - |  |
| 109 | leodavincs/kalem | 23 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 106 | 106.0 | 1 | 7 | - |  |
| 110 | Harishwarrior/flutter-claude-skills | 22 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 68 | 5.4 | 2 | 3 | - |  |
| 111 | Kappaemme-git/codex-phone-lab | 22 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 16.7 | 1 | 0 | - |  |
| 112 | Shopify/agent-skills | 22 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 101 | 13.8 | 1 | 0 | - |  |
| 113 | buluslan/ecommerce-competitor-analyzer | 22 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 62 | 6.6 | 1 | 3 | 2026-01-29 |  |
| 114 | YildizDikme/claude-video-edit | 21 D | 0 | - | 0/0/0 | MIT |  | 33 | 33.0 | 1 | 3 | - |  |
| 115 | oldred-byte/ec-visual-skill | 21 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 104 | 16.8 | 1 | 0 | - |  |
| 116 | Viniciuscarvalho/swift-code-reviewer-skill | 20 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.4 | 5 | 0 | 2026-05-07 |  |
| 117 | yohannescodes/apple-app-review-compliance | 20 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 20 | 20.0 | 1 | 4 | - |  |
| 118 | mmiani/kotlin-kmp-claude-agent-skills | 19 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 90 | 12.1 | 1 | 8 | - |  |
| 119 | jazzychad/ios-code-audit | 18 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.2 | 1 | 0 | - |  |
| 120 | Trendyol/trendyol-integration-developer-tool | 17 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.8 | 3 | 0 | - |  |
| 121 | arjitj2/swiftui-design-principles | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 34 | 4.0 | 1 | 0 | - |  |
| 122 | lemomo-ai/codex-radar | 16 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 7.6 | 1 | 8 | - |  |
| 123 | J-DTurner/etsy-api-skill | 14 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.6 | 1 | 0 | - |  |
| 124 | avenoxai/higgsfield-studio | 12 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 14 | 5.2 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 87 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 80 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `context7-docs` 94/B, `context7-mcp` 94/B, `find-docs` 94/B, `tailwind-design-system` 93/A, `web-artifacts-builder` 90/B | tasarim-teknolojileri.md |
| 3 | d3/d3 | 78 B | v7.9 | `d3-viz` 93/A, `d3-visualization` 97/A, `d3-data-visualization` 72/C, `geospatial-and-cartographic-visualization` 72/C | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 74 B | - | `ffmpeg` 93/A, `video-edit` 100/A, `video-understand` 94/A, `character-animation-qa` 86/A | kutuphaneler.md |
| 5 | ManimCommunity/manim | 72 B | v0.22 | `manim-composer` 94/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 93/A, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 6 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 99/B | tasarim-teknolojileri.md |
| 7 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 94/A, `azure-speech-to-text` 94/A, `krillinai-subtitle` 89/C, `whisper` 86/C, `twilio-conference-calls` 72/C, `subtitles` 67/C | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 71 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 61/D, `react-three-fiber-game` 74/C, `blender-web-pipeline` 61/D, `web3d-integration-patterns` 61/D, `substance-3d-texturing` 53/D, `modern-web-design` 51/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 68 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 94/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 88/B | kutuphaneler.md |
| 10 | 666ghj/MiroFish | 67 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 11 | blender/blender | 67 B | - | `blender-web-pipeline` 61/D, `3d-asset-generation` 94/A, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A, `web-3d-asset-pipeline` 74/C | kutuphaneler.md |
| 12 | QwikDev/partytown | 65 B | v1.0 (T5) | `shopify-hydrogen` 49/D | tasarim-teknolojileri.md |
| 13 | dequelabs/axe-core | 64 C | v4.14 (MPL-2.0) | `salesforce-component-standards` 100/B, `scoutqa-test` 100/B, `accessibility-review` 100/B, `frontend-ui-engineering` 94/A, `replica-design` 84/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 14 | Tonejs/Tone.js | 63 C | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 67/D | tasarim-teknolojileri.md |
| 15 | librosa/librosa | 63 C | - | `media-use` 100/A | kutuphaneler.md |
| 16 | DavidHDev/react-bits | 62 C | - | `animated-component-libraries` 61/D, `frontend-ui-engineering` 94/A | tasarim-teknolojileri.md |
| 17 | darkroomengineering/lenis | 61 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 61/D | tasarim-teknolojileri.md |
| 18 | paperjs/paper.js | 61 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 19 | pmndrs/drei | 60 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 20 | airbnb/lottie-web | 59 C | v5.13 | `lottie-animations` 61/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 78/A, `flutter-pre-caching` 78/D, `motion-design` 72/D, `rive-interactive` 61/D | tasarim-teknolojileri.md |
| 21 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 22 | ai/size-limit | 56 C | 14.2 (T5) | `react-doctor` 75/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 56 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 94/A | tasarim-teknolojileri.md |
| 24 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 69/D, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 25 | pmndrs/postprocessing | 52 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 26 | rough-stuff/rough | 49 D | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 27 | greensock/GSAP | 48 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 28 | theatre-js/theatre | 47 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 29 | barvian/number-flow | 46 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 30 | opentypejs/opentype.js | 46 D | 2.0 | `svg-character-animation` 94/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 31 | figma/code-connect | 45 D | v2.0 | `figma-code-connect` 69/C | tasarim-teknolojileri.md |
| 32 | seek-oss/capsize | 45 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | argyleink/open-props | 44 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | JohnHeibel/ClaudeAnimationBase | 42 D | - | `canvas-procedural-animation` 85/A, `algorithmic-art` 81/B, `svg-character-animation` 94/A | tasarim-teknolojileri.md |
| 35 | pmndrs/cannon-es | 42 D | v0.20 | `threejs-world-generation` 93/A, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 36 | metafizzy/zdog | 39 D | v1.1 | `svg-character-animation` 94/A, `canvas-procedural-animation` 85/A, `lightweight-3d-effects` 60/D | tasarim-teknolojileri.md |
| 37 | meyda/meyda | 39 D | - | `canvas-procedural-animation` 85/A | kutuphaneler.md |
| 38 | oframe/ogl | 38 D | - | `lightweight-3d-effects` 60/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 39 | zhuyansen/awesome-claude-video-skills | 38 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 40 | 14islands/r3f-scroll-rig | 35 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 61/D, `gsap-framer-scroll-animation` 100/B, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `scrollytelling-and-parallax-data-visualization` 72/C, `lottie-animations` 61/D, `barba-js` 61/D | tasarim-teknolojileri.md |
| 41 | linvi/tweetinvi | 34 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 42 | jwagner/simplex-noise.js | 33 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 79/D, `threejs-world-generation` 93/A, `google-docs` 67/C | tasarim-teknolojileri.md |
| 43 | nevertoday/350-layout-compositions | 33 D | - | `design-taste-frontend` 99/B, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 44 | pmndrs/react-three-a11y | 30 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 45 | arturitu/the-delegation | 24 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
