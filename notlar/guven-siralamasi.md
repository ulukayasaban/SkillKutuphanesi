# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-22, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 91A (13) · nextlevelbuilder/ui-ux-pro-max-skill 88A (2) · anthropics/claude-code 85A (1) | `impeccable` 100/A, `design-taste-frontend` 100/A, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 91A (3) · nextlevelbuilder/ui-ux-pro-max-skill 88A (4) · OpenMontageInc/OpenMontage 81A (1) | `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A, `tailwind-design-system` 93/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 91A (7) · OpenMontageInc/OpenMontage 81A (2) · greensock/gsap-skills 53C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 53C (1) · nateherkai/scroll-craft 44D (1) · freshtechbro/claudedesignskills 30D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 57/D, `locomotive-scroll` 57/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 41D (13) · freshtechbro/claudedesignskills 30D (10) | `threejs-asset-pipeline` 88/D, `threejs-fundamentals` 88/D, `threejs-lighting` 88/D, `threejs-loaders` 88/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 91A (1) · pixijs/pixijs 78B (26) · Donchitos/Claude-Code-Game-Studios 60C (68) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 91A (14) · nextlevelbuilder/ui-ux-pro-max-skill 88A (1) · OpenMontageInc/OpenMontage 81A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 91A (3) · microsoft/playwright 86A (2) · addyosmani/agent-skills 86A (1) | `playwright-trace` 100/A, `browser-testing-with-devtools` 98/A, `playwright-component-testing` 98/A, `export-download-debugging` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 86A (8) · mattpocock/skills 83A (30) · obra/superpowers 81A (3) | `ask-matt` 100/A, `codebase-design` 100/A, `diagnosing-bugs` 100/A, `domain-modeling` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 87A (6) · addyosmani/agent-skills 86A (2) · tt-a1i/archify 85A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 86A (2) · tt-a1i/archify 85A (1) · obra/superpowers 81A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 86A (2) · google/skills 66B (48) · vudovn/ag-kit 55C (6) | `api-and-interface-design` 100/A, `alloydb-basics` 100/B, `bigquery-basics` 100/B, `bigquery-bigframes` 100/B |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 91A (2) · addyosmani/agent-skills 86A (2) · obra/superpowers 81A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 86A (5) · anthropics/claude-plugins-official 78B (1) | `security-and-hardening` 100/A, `cloud-operator-setup` 100/B, `cloud-operator-share-context` 100/B, `cloud-run-alert-configuration` 100/B |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 86A (1) · anthropics/claude-plugins-official 78B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | google/skills 66B (11) · android/skills 62C (37) · expo/skills 54C (24) | `google-mobile-ads-banner` 100/B, `google-mobile-ads-get-started` 100/B, `google-mobile-ads-interstitial` 100/B, `google-mobile-ads-rewarded` 100/B |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 91A (3) · anthropics/skills 75B (4) · anthropics/knowledge-work-plugins 74B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 91A (2) · addyosmani/agent-skills 86A (1) · tt-a1i/archify 85A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `doc-coauthoring` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 91A (1) · anthropics/skills 75B (1) · blader/humanizer 74B (1) | `humanizer` 98/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | obsidianmd/obsidian-skills 75B (5) · ComposioHQ/awesome-claude-skills 65B (1) · AgriciDaniel/claude-obsidian 63C (11) | `defuddle` 92/B, `knap` 92/B, `obsidian-cli` 92/B, `obsidian-bases@kepano` 90/B |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 78B (4) · anthropics/skills 75B (3) · google/skills 66B (24) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `agent-platform-endpoint-management` 100/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 91A (2) · JuliusBrussee/caveman 87A (22) · addyosmani/agent-skills 86A (2) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 93A (1) · Panniantong/Agent-Reach 81A (1) · upstash/context7 80A (4) | `find-docs` 96/A, `graphify` 94/A, `agent-reach` 94/A, `context7-cli` 88/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 91A (2) · heygen-com/hyperframes 90A (2) · obra/superpowers 81A (1) | `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 97/A, `od-next-media-inputs` 97/A |
| `e-entegrasyon-katalogu/01-uygulama-entegrasyonlari` — Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Co | github/awesome-copilot 77B (1) | `caption-qa` 95/B |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 85A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 91A (17) · heygen-com/hyperframes 90A (10) · harry0703/MoneyPrinterTurbo 86A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | OpenMontageInc/OpenMontage 81A (12) · krillinai/OpenCreator 65B (7) · digitalsamba/claude-code-video-toolkit 57C (2) | `lyria` 100/A, `music` 100/A, `sound-effects` 100/A, `speech-to-text` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 81A (16) · digitalsamba/claude-code-video-toolkit 57C (4) · yerel/kendi 17D (1) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 91A (2) · heygen-com/hyperframes 90A (3) · OpenMontageInc/OpenMontage 81A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 81A (48) · anthropics/knowledge-work-plugins 74B (58) · AgriciDaniel/claude-seo 70B (25) | `ab-testing` 100/A, `analytics` 100/A, `aso` 100/A, `attribution` 100/A |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 74B (26) · Jakeschincariol/day-trader-skill 46D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 74B (69) · Jakeschincariol/founder-skill 38D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 74B (10) · google/skills 66B (2) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 91A (1) · nexscope-ai/eCommerce-Skills 39D (156) · 40RTY-ai/shopify-admin-skills 38D (117) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 78B (90) · anthropics/knowledge-work-plugins 74B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 78B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 78B (27) · Orchestra-Research/AI-Research-SKILLs 56C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 78B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 69B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 78B (2) · earthtojake/text-to-cad 72B (12) | `bambu-labs` 98/B, `dfam-check` 98/B, `dfm` 98/B, `gcode` 98/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 430844 | 58998.5 | 362 | 5773 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 93 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 142439 | 18584.3 | 391 | 1481 | 2026-11-03 | 🔥 |
| 3 | nexu-io/open-design | 91 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 105947 | 15484.6 | 451 | 717 | 2026-11-04 |  |
| 4 | heygen-com/hyperframes | 90 A | 15 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/2 | Apache-2.0 | ✓ | 82940 | 9810.8 | 137 | 3163 | 2026-11-12 | 🔥 |
| 5 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143324 | 1177.6 | 4184 | 1549 | 2026-11-04 | 🔥 |
| 6 | nextlevelbuilder/ui-ux-pro-max-skill | 88 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 145229 | 12366.8 | 110 | 81 | 2026-08-13 |  |
| 7 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 251960 | 1553.7 | 2027 | 134 | 2026-10-14 |  |
| 8 | DietrichGebert/ponytail | 87 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 184540 | 34417.3 | 133 | 163 | 2026-10-29 | 🔥 |
| 9 | JuliusBrussee/caveman | 87 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 117512 | 15398.1 | 104 | 1619 | 2026-10-23 |  |
| 10 | addyosmani/agent-skills | 86 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 113281 | 12299.1 | 97 | 392 | 2026-10-31 | 🔥 |
| 11 | harry0703/MoneyPrinterTurbo | 86 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 141094 | 4350.2 | 169 | 554 | 2026-11-07 | 🔥 |
| 12 | microsoft/playwright | 86 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 99306 | 1177.4 | 828 | 733 | 2026-10-14 | 🔥 |
| 13 | anthropics/claude-code | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154554 | 7364.3 | 59 | 247 | 2026-11-04 | 🔥 |
| 14 | tt-a1i/archify | 85 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 93462 | 12856.3 | 92 | 1628 | 2026-10-19 |  |
| 15 | ruvnet/ruflo | 84 A | 0 | - | 0/0/0 | MIT |  | 81282 | 4592.9 | 95 | 2949 | 2026-11-09 |  |
| 16 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 313295 | 32617.0 | 8 | 133 | 2026-10-29 | 🔥 |
| 17 | pbakaus/impeccable | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 102802 | 8423.7 | 62 | 1203 | 2026-10-26 | 🔥 |
| 18 | OpenMontageInc/OpenMontage | 81 A | 54 | 03-ai-gorsel-video-modelleri (16), 02-ses-muzik-konusma (12) | 22/11/21 | AGPL-3.0 |  | 79720 | 10182.7 | 129 | 305 | - | 🔥 |
| 19 | Panniantong/Agent-Reach | 81 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 108808 | 12205.8 | 46 | 104 | 2026-11-01 | 🔥 |
| 20 | coreyhaines31/marketingskills | 81 A | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 58521 | 5720.4 | 57 | 961 | 2026-10-30 | 🔥 |
| 21 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 312440 | 23222.9 | 44 | 7 | 2026-11-03 | 🔥 |
| 22 | Leonxlnx/taste-skill | 80 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 110057 | 12122.2 | 24 | 152 | 2026-11-04 | 🔥 |
| 23 | upstash/context7 | 80 A | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 64385 | 3229.9 | 147 | 253 | 2026-11-06 |  |
| 24 | remotion-dev/remotion | 79 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 70754 | 918.0 | 490 | 5575 | 2026-11-02 | 🔥 |
| 25 | K-Dense-AI/scientific-agent-skills | 78 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 56104 | 4274.6 | 58 | 94 | 2026-10-01 | 🔥 |
| 26 | anthropics/claude-plugins-official | 78 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 46120 | 3820.3 | 42 | 1732 | - | 🔥 |
| 27 | pixijs/pixijs | 78 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48622 | 292.5 | 639 | 94 | 2026-10-01 |  |
| 28 | GoogleChrome/lighthouse | 77 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31017 | 241.1 | 397 | 192 | 2026-10-27 |  |
| 29 | github/awesome-copilot | 77 B | 1 | 01-uygulama-entegrasyonlari (1) | 0/1/0 | MIT |  | 40799 | 2344.6 | 578 | 885 | - | 🔥 |
| 30 | ayghri/i-have-adhd | 76 B | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 61897 | 9749.6 | 53 | 79 | 2026-10-19 |  |
| 31 | anthropics/skills | 75 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 187417 | 13374.4 | 17 | 15 | - | 🔥 |
| 32 | cathrynlavery/diagram-design | 75 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 65003 | 8982.2 | 66 | 397 | - |  |
| 33 | obsidianmd/obsidian-skills | 75 B | 6 | 04-not-alma-bilgi-yonetimi (5), 02-diyagram-dokumantasyon (1) | 6/0/0 | MIT |  | 52786 | 4952.8 | 28 | 43 | 2026-11-11 |  |
| 34 | anthropics/knowledge-work-plugins | 74 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34734 | 3484.9 | 32 | 563 | - | 🔥 |
| 35 | blader/humanizer | 74 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 64838 | 6399.6 | 24 | 60 | 2026-09-28 | 🔥 |
| 36 | earthtojake/text-to-cad | 72 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 25423 | 3611.5 | 32 | 876 | 2026-11-03 | 🔥 |
| 37 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 34907 | 362.4 | 147 | 1009 | - |  |
| 38 | AgriciDaniel/claude-seo | 70 B | 25 | 01-satis-pazarlama-musteri (25) | 25/0/0 | MIT |  | 26654 | 2813.5 | 30 | 209 | 2026-10-22 | 🔥 |
| 39 | teng-lin/notebooklm-py | 70 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20096 | 1915.1 | 42 | 650 | 2026-10-29 |  |
| 40 | google/elephant-goldfish-model | 69 B | 7 | 01-planlama-metodoloji (7) | 7/0/0 | Apache-2.0 |  | 11801 | 5125.0 | 29 | 149 | 2026-10-27 | 🔥 |
| 41 | latent-spaces/brag | 69 B | 2 | 01-video-uretim-montaj (2) | 2/0/0 | MIT |  | 21811 | 4170.2 | 20 | 58 | 2026-11-15 |  |
| 42 | wanshuiyin/Auto-claude-code-research-in-sleep | 69 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 18651 | 2206.2 | 106 | 205 | 2026-09-28 |  |
| 43 | multica-ai/andrej-karpathy-skills | 67 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 229500 | 23333.8 | 7 | 0 | - | 🔥 |
| 44 | vercel-labs/agent-skills | 67 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33547 | 2922.1 | 28 | 23 | 2026-10-27 | 🔥 |
| 45 | JuneYaooo/rea-video | 66 B | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 10200 | 10200.0 | 17 | 155 | 2026-11-11 |  |
| 46 | Nutlope/hallmark | 66 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 47913 | 6969.2 | 10 | 138 | - | 🔥 |
| 47 | cloudflare/security-audit-skill | 66 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 59355 | 11492.9 | 4 | 3 | - | 🔥 |
| 48 | google/skills | 66 B | 196 | 06-devops-guvenlik-performans (105), 04-mimari-api-veritabani (48) | 20/176/0 | Apache-2.0 |  | 24352 | 3136.9 | 9 | 351 | - | 🔥 |
| 49 | ComposioHQ/awesome-claude-skills | 65 B | 4 | 03-yazi-iletisim-icerik (2), 04-not-alma-bilgi-yonetimi (1) | 3/1/0 | yok | ✓ | 78745 | 5969.7 | 29 | 0 | - |  |
| 50 | krillinai/OpenCreator | 65 B | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14157 | 610.5 | 36 | 458 | 2026-11-03 |  |
| 51 | Vincentwei1021/video-shotcraft | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 16988 | 4098.7 | 14 | 44 | 2026-09-01 | 🔥 |
| 52 | AgriciDaniel/claude-obsidian | 63 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16171 | 2146.7 | 11 | 108 | 2026-10-21 |  |
| 53 | dreammis/social-auto-upload | 63 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16118 | 452.0 | 42 | 46 | 2026-10-22 |  |
| 54 | lemomo-ai/lemo-opuscar | 63 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 12273 | 6545.6 | 4 | 80 | 2026-10-12 |  |
| 55 | android/skills | 62 C | 37 | 08-mobil-uygulama (37) | 36/1/0 | Apache-2.0 | ✓ | 10337 | 1252.0 | 8 | 36 | 2026-11-04 | 🔥 |
| 56 | kajisho5/ffmpeg-skill | 62 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 7677 | 2917.3 | 11 | 590 | 2026-11-15 | 🔥 |
| 57 | browser-use/video-use | 61 C | 2 | 01-video-uretim-montaj (1), 04-motion-graphics-karakter (1) | 1/1/0 | MIT |  | 31088 | 4219.1 | 8 | 5 | - |  |
| 58 | Donchitos/Claude-Code-Game-Studios | 60 C | 68 | 06-oyun-2d-grafik (68) | 68/0/0 | MIT |  | 35403 | 3803.0 | 1 | 5 | 2026-10-19 | 🔥 |
| 59 | zarazhangrui/frontend-slides | 59 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 31888 | 3253.0 | 9 | 0 | 2026-05-26 |  |
| 60 | cloudflare/skills | 57 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3279 | 287.3 | 48 | 261 | - | 🔥 |
| 61 | digitalsamba/claude-code-video-toolkit | 57 C | 14 | 01-video-uretim-montaj (7), 03-ai-gorsel-video-modelleri (4) | 4/8/2 | MIT |  | 2579 | 225.3 | 17 | 422 | 2026-11-14 |  |
| 62 | zubair-trabzada/geo-seo-claude | 57 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11511 | 1263.3 | 25 | 77 | - |  |
| 63 | Orchestra-Research/AI-Research-SKILLs | 56 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14269 | 1129.6 | 17 | 0 | 2026-06-16 |  |
| 64 | AgriciDaniel/claude-ads | 55 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 10746 | 1150.3 | 2 | 43 | 2026-10-16 |  |
| 65 | WyattBlue/auto-editor | 55 C | 5 | 01-video-uretim-montaj (5) | 5/0/0 | Unlicense |  | 5918 | 75.1 | 17 | 228 | 2026-11-13 |  |
| 66 | vudovn/ag-kit | 55 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8207 | 799.7 | 10 | 8 | 2026-08-31 |  |
| 67 | czlonkowski/n8n-skills | 54 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6589 | 503.3 | 7 | 33 | 2026-10-24 | 🔥 |
| 68 | expo/skills | 54 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4050 | 344.9 | 31 | 45 | - | 🔥 |
| 69 | greensock/gsap-skills | 53 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17884 | 2067.2 | 4 | 0 | - |  |
| 70 | openai/plugins | 52 C | 0 | - | 0/0/0 | yok | ✓ | 7752 | 896.0 | 62 | 10 | - |  |
| 71 | darkroomengineering/satus | 51 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.4 | 19 | 152 | 2026-08-28 |  |
| 72 | Leonxlnx/earshot | 50 C | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 3898 | 3118.4 | 1 | 40 | 2026-10-22 |  |
| 73 | Ryze-AI-Adgent/open-seo-mcp-skills | 50 C | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 8815 | 3152.7 | 1 | 16 | - |  |
| 74 | veedstudio/open-edit | 48 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 1838 | 454.3 | 3 | 16 | 2026-08-03 |  |
| 75 | Jakeschincariol/day-trader-skill | 46 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 5296 | 4878.7 | 1 | 1 | - |  |
| 76 | Jakeschincariol/replica-skill | 46 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 7640 | 4645.1 | 1 | 1 | - |  |
| 77 | hardikpandya/stop-slop | 46 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 18619 | 1796.9 | 2 | 0 | - |  |
| 78 | feitangyuan/onetake | 44 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 3959 | 2111.5 | 2 | 21 | 2026-10-08 |  |
| 79 | nateherkai/scroll-craft | 44 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4529 | 1496.5 | 1 | 16 | - |  |
| 80 | Jakeschincariol/instagram-agent-skill | 43 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4849 | 2105.9 | 1 | 2 | - |  |
| 81 | Jakeschincariol/youtube-agent-skill | 43 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 4562 | 2069.9 | 1 | 1 | - |  |
| 82 | shadcn-labs/snapcn | 43 D | 7 | 04-motion-graphics-karakter (7) | 0/7/0 | MIT |  | 652 | 163.8 | 3 | 290 | - |  |
| 83 | yaojingang/yao-meta-skill | 43 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2719 | 350.2 | 3 | 56 | - |  |
| 84 | CloudAI-X/threejs-skills | 41 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3985 | 394.6 | 1 | 20 | - |  |
| 85 | sarpstar/cinecode | 41 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 1614 | 1614.0 | 3 | 7 | - |  |
| 86 | AbubakrChan/product-launch-motion | 40 D | 1 | 04-motion-graphics-karakter (1) | 1/0/0 | MIT |  | 487 | 125.5 | 2 | 44 | 2026-10-12 |  |
| 87 | ythx-101/live-panel-skill | 40 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 840 | 510.7 | 4 | 40 | - |  |
| 88 | Jakeschincariol/linkedin-agent-skill | 39 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3205 | 1282.0 | 1 | 1 | - |  |
| 89 | nexscope-ai/eCommerce-Skills | 39 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1332 | 162.6 | 7 | 1 | - |  |
| 90 | 40RTY-ai/shopify-admin-skills | 38 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 27.2 | 3 | 13 | 2026-06-17 |  |
| 91 | Jakeschincariol/founder-skill | 38 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2452 | 1620.5 | 1 | 1 | - |  |
| 92 | lottiefiles/motion-design-skill | 37 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 2853 | 340.1 | 1 | 0 | - |  |
| 93 | nexscope-ai/Amazon-Skills | 37 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 834 | 98.7 | 5 | 1 | - |  |
| 94 | heygen-com/hyperframes-community-skills | 36 D | 7 | 01-video-uretim-montaj (7) | 6/1/0 | Apache-2.0 | ✓ | 280 | 95.6 | 3 | 11 | - |  |
| 95 | heyitsnoah/claudesidian | 36 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2606 | 181.7 | 3 | 0 | 2026-04-11 |  |
| 96 | zanwei/design-dna | 36 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2079 | 259.0 | 3 | 4 | - |  |
| 97 | Barty-Bart/motion-graphics | 35 D | 5 | 04-motion-graphics-karakter (5) | 5/0/0 | NOASSERTION |  | 1347 | 706.0 | 4 | 10 | - |  |
| 98 | nateherkai/herk-edit-kit | 35 D | 10 | 01-video-uretim-montaj (10) | 5/5/0 | NOASSERTION |  | 2929 | 408.4 | 1 | 13 | - |  |
| 99 | xjli360/sealeap-amazon-skills | 32 D | 0 | - | 0/0/0 | MIT |  | 369 | 120.6 | 1 | 15 | - |  |
| 100 | evanca/flutter-ai-rules | 31 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 669 | 35.1 | 1 | 13 | - |  |
| 101 | hamen/compose_skill | 31 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 378 | 51.5 | 3 | 0 | 2026-07-07 |  |
| 102 | kylezantos/design-motion-principles | 31 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1528 | 148.9 | 1 | 0 | 2026-05-21 |  |
| 103 | rshankras/claude-code-apple-skills | 31 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 861 | 67.3 | 2 | 3 | - |  |
| 104 | RevenueCat/play-billing-skills | 30 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 10.5 | 1 | 15 | 2026-10-15 |  |
| 105 | freshtechbro/claudedesignskills | 30 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1248 | 96.5 | 1 | 0 | - |  |
| 106 | lemomo-ai/lemo-wake | 30 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 256 | 155.6 | 1 | 15 | 2026-10-05 |  |
| 107 | mercadopago/mercadopago-claude-marketplace | 29 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.6 | 10 | 7 | - |  |
| 108 | tuist/fuckingapproachableswiftconcurrency | 29 D | 0 | - | 0/0/0 | MIT |  | 158 | 14.3 | 15 | 0 | - |  |
| 109 | moiz-za/etsy-seller-seo-system | 28 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 47 | 7.6 | 2 | 13 | 2026-10-23 |  |
| 110 | tuzhechen2005/opus-video-skills | 28 D | 2 | 04-motion-graphics-karakter (2) | 2/0/0 | NOASSERTION |  | 525 | 280.0 | 3 | 9 | - |  |
| 111 | twostraws/SwiftData-Agent-Skill | 28 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 463 | 55.0 | 2 | 1 | 2026-03-11 |  |
| 112 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 137 | 70.6 | 1 | 11 | - |  |
| 113 | Livsy90/iOS-Performance-Agent-Skills | 27 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 120 | 20.2 | 2 | 0 | 2026-07-12 |  |
| 114 | OrcaQubits/agentic-commerce-skills-plugins | 27 D | 2 | 05-e-ticaret-pazaryeri (2) | 2/0/0 | MIT |  | 40 | 4.6 | 3 | 11 | 2026-05-13 |  |
| 115 | ehmo/platform-design-skills | 27 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 640 | 66.2 | 1 | 0 | - |  |
| 116 | wj-sidiss/etsy-otomasyon-full-full-surum | 27 D | 0 | - | 0/0/0 | MIT |  | 39 | 39.0 | 1 | 7 | 2026-11-01 |  |
| 117 | finsilabs/awesome-ecommerce-skills | 26 D | 179 | 05-e-ticaret-pazaryeri (179) | 161/18/0 | MIT |  | 63 | 7.5 | 4 | 3 | - |  |
| 118 | xianyu110/ecommerce-image-skills | 26 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 144 | 89.3 | 1 | 7 | - |  |
| 119 | dpconde/claude-android-skill | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 352 | 30.6 | 1 | 0 | - |  |
| 120 | ParthJadhav/ios-marketing-capture | 24 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 265 | 35.6 | 1 | 1 | - |  |
| 121 | Lonsdale201/wp-agent-skills | 22 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 3.8 | 3 | 25 | - |  |
| 122 | MADTeacher/mad-agents-skills | 22 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 10.7 | 2 | 0 | - |  |
| 123 | dadederk/iOS-Accessibility-Agent-Skill | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 176 | 17.8 | 1 | 0 | - |  |
| 124 | leodavincs/kalem | 21 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 106 | 106.0 | 1 | 7 | - |  |
| 125 | Harishwarrior/flutter-claude-skills | 20 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 68 | 5.2 | 2 | 3 | - |  |
| 126 | Kappaemme-git/codex-phone-lab | 20 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 15.5 | 1 | 0 | - |  |
| 127 | Shopify/agent-skills | 20 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 101 | 13.1 | 1 | 0 | - |  |
| 128 | Viniciuscarvalho/swift-code-reviewer-skill | 19 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.2 | 5 | 0 | 2026-05-07 |  |
| 129 | YildizDikme/claude-video-edit | 19 D | 0 | - | 0/0/0 | MIT |  | 33 | 33.0 | 1 | 3 | - |  |
| 130 | oldred-byte/ec-visual-skill | 19 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 104 | 15.7 | 1 | 0 | - |  |
| 131 | avenoxai/avenox-video-kurgu-notlari | 18 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 27 | 27.0 | 1 | 1 | - |  |
| 132 | yohannescodes/apple-app-review-compliance | 18 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 20 | 16.9 | 1 | 4 | - |  |
| 133 | mmiani/kotlin-kmp-claude-agent-skills | 17 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 90 | 11.4 | 1 | 8 | - |  |
| 134 | Trendyol/trendyol-integration-developer-tool | 16 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.7 | 3 | 0 | - |  |
| 135 | jazzychad/ios-code-audit | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 6.7 | 1 | 0 | - |  |
| 136 | arjitj2/swiftui-design-principles | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 34 | 3.8 | 1 | 0 | - |  |
| 137 | lemomo-ai/codex-radar | 14 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 7.0 | 1 | 8 | - |  |
| 138 | avenoxai/higgsfield-studio | 10 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 14 | 4.5 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 88 A | r186 | `threejs-fundamentals` 88/D, `threejs-geometry` 78/D, `threejs-materials` 78/D, `threejs-lighting` 88/D, `threejs-textures` 80/D, `threejs-loaders` 88/D, `threejs-shaders` 78/D, `threejs-postprocessing` 78/D, `threejs-animation` 80/D, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 80 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `find-docs` 96/A, `tailwind-design-system` 93/A, `remotion-create` 90/B, `web-artifacts-builder` 90/B, `context7-mcp` 88/A | tasarim-teknolojileri.md |
| 3 | d3/d3 | 78 B | v7.9 | `d3-viz` 93/A, `d3-visualization` 97/A | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 75 B | - | `ffmpeg` 93/A, `video-edit` 100/A, `video-understand` 94/A, `ffmpeg-skill` 94/C, `character-animation-qa` 86/A, `product-launch-motion` 72/D, `kinetic-reel` 72/D, `cut-mistakes` 65/D | kutuphaneler.md |
| 5 | ManimCommunity/manim | 73 B | v0.22 | `manim-composer` 94/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 93/A, `remotion-to-hyperframes` 97/A, `manim-video` 84/C | tasarim-teknolojileri.md |
| 6 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/A | tasarim-teknolojileri.md |
| 7 | openai/whisper | 72 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 94/A, `azure-speech-to-text` 94/A, `krillinai-subtitle` 90/B, `whisper` 87/C, `auto-editor-transcribe` 84/C, `ajanla-video-kurgu` 69/D | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 72 B | v9.8 | `threejs-react-three-fiber` 86/D, `react-three-fiber` 57/D, `blender-web-pipeline` 57/D, `web3d-integration-patterns` 57/D, `substance-3d-texturing` 49/D, `modern-web-design` 47/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 69 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 94/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 89/B | kutuphaneler.md |
| 10 | blender/blender | 68 B | - | `blender-web-pipeline` 57/D, `3d-asset-generation` 94/A, `threejs-loaders` 88/D, `remotion-to-hyperframes` 97/A, `blender` 80/C | kutuphaneler.md |
| 11 | 666ghj/MiroFish | 67 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 12 | QwikDev/partytown | 65 B | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 64 C | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 67/D | tasarim-teknolojileri.md |
| 14 | dequelabs/axe-core | 64 C | v4.14 (MPL-2.0) | `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 84/D, `inclusive-design` 79/D, `accessibility` 77/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 15 | librosa/librosa | 64 C | - | `media-use` 100/A | kutuphaneler.md |
| 16 | DavidHDev/react-bits | 63 C | - | `animated-component-libraries` 57/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 17 | Fei-Away/Codex-Dream-Skin | 62 C | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 18 | paperjs/paper.js | 62 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 19 | darkroomengineering/lenis | 61 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 57/D | tasarim-teknolojileri.md |
| 20 | airbnb/lottie-web | 60 C | v5.13 | `lottie-animations` 57/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 78/A, `flutter-pre-caching` 77/D, `motion-design` 64/D, `rive-interactive` 57/D | tasarim-teknolojileri.md |
| 21 | pmndrs/drei | 60 C | v10.7 | `threejs-react-three-fiber` 86/D | tasarim-teknolojileri.md |
| 22 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 23 | ai/size-limit | 57 C | 14.2 (T5) | `react-doctor` 75/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 24 | motion-canvas/motion-canvas | 56 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 94/A | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 65/D, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 52 C | v6.39 | `threejs-postprocessing` 78/D, `threejs-shaders` 78/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 27 | greensock/GSAP | 49 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 28 | rough-stuff/rough | 49 D | v3.1 | `camera-3d-captions` 79/D, `day-in-my-life` 73/D | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 47 D | 0.4 (r3f) | `threejs-animation` 80/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | barvian/number-flow | 46 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 31 | opentypejs/opentype.js | 46 D | 2.0 | `svg-character-animation` 94/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 32 | argyleink/open-props | 44 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | figma/code-connect | 44 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | seek-oss/capsize | 44 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 35 | pmndrs/cannon-es | 42 D | v0.20 | `threejs-world-generation` 93/A, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 36 | JohnHeibel/ClaudeAnimationBase | 41 D | - | `canvas-procedural-animation` 85/A, `algorithmic-art` 81/B, `svg-character-animation` 94/A | tasarim-teknolojileri.md |
| 37 | metafizzy/zdog | 39 D | v1.1 | `svg-character-animation` 94/A, `canvas-procedural-animation` 85/A, `lightweight-3d-effects` 56/D | tasarim-teknolojileri.md |
| 38 | meyda/meyda | 39 D | - | `canvas-procedural-animation` 85/A | kutuphaneler.md |
| 39 | oframe/ogl | 38 D | - | `lightweight-3d-effects` 56/D, `threejs-shaders` 78/D | tasarim-teknolojileri.md |
| 40 | zhuyansen/awesome-claude-video-skills | 38 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 41 | 14islands/r3f-scroll-rig | 34 D | v8.15 | `threejs-react-three-fiber` 86/D, `web3d-integration-patterns` 57/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 57/D, `barba-js` 57/D, `locomotive-scroll` 57/D, `scroll-reveal-libraries` 57/D | tasarim-teknolojileri.md |
| 42 | jwagner/simplex-noise.js | 33 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 78/D, `threejs-world-generation` 93/A | tasarim-teknolojileri.md |
| 43 | linvi/tweetinvi | 33 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 44 | nevertoday/350-layout-compositions | 31 D | - | `design-taste-frontend` 100/A, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 45 | pmndrs/react-three-a11y | 29 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 46 | arturitu/the-delegation | 23 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
