# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-24, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 90A (13) · nextlevelbuilder/ui-ux-pro-max-skill 88A (2) · anthropics/claude-code 85A (1) | `impeccable` 100/A, `design-taste-frontend` 100/A, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 90A (3) · nextlevelbuilder/ui-ux-pro-max-skill 88A (4) · OpenMontageInc/OpenMontage 82A (1) | `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A, `tailwind-design-system` 94/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 90A (7) · OpenMontageInc/OpenMontage 82A (2) · greensock/gsap-skills 54C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 54C (1) · nateherkai/scroll-craft 44D (1) · freshtechbro/claudedesignskills 31D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 57/D, `locomotive-scroll` 57/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 43D (13) · freshtechbro/claudedesignskills 31D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 90A (1) · pixijs/pixijs 78B (26) · Donchitos/Claude-Code-Game-Studios 62C (72) | `estimate` 99/C, `scope-check` 99/C, `test-setup` 99/C, `asset-audit` 97/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 90A (14) · nextlevelbuilder/ui-ux-pro-max-skill 88A (1) · OpenMontageInc/OpenMontage 82A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 90A (3) · microsoft/playwright 87A (2) · addyosmani/agent-skills 86A (1) | `playwright-trace` 100/A, `playwright-component-testing` 98/A, `browser-testing-with-devtools` 98/A, `export-download-debugging` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 86A (9) · mattpocock/skills 83A (30) · obra/superpowers 81A (3) | `accessibility-engineering` 100/A, `ask-matt` 100/A, `codebase-design` 100/A, `diagnosing-bugs` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 87A (6) · addyosmani/agent-skills 86A (2) · tt-a1i/archify 86A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 86A (2) · tt-a1i/archify 86A (1) · obra/superpowers 81A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 86A (2) · google/skills 66B (53) · vudovn/ag-kit 56C (6) | `api-and-interface-design` 100/A, `alloydb-basics` 100/B, `bigquery-basics` 100/B, `bigquery-bigframes` 100/B |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 90A (2) · addyosmani/agent-skills 86A (2) · obra/superpowers 81A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 86A (5) · anthropics/claude-plugins-official 78B (1) | `security-and-hardening` 100/A, `cloud-operator-share-context` 100/B, `cloud-run-alert-configuration` 100/B, `cloud-trace-querying` 100/B |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 91A (6) · microsoft/playwright 87A (1) · anthropics/claude-plugins-official 78B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | google/skills 66B (11) · android/skills 64C (38) · expo/skills 55C (24) | `google-mobile-ads-banner` 100/B, `google-mobile-ads-get-started` 100/B, `google-mobile-ads-interstitial` 100/B, `google-mobile-ads-rewarded` 100/B |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 90A (3) · anthropics/knowledge-work-plugins 75B (1) · anthropics/skills 74B (4) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 90A (2) · tt-a1i/archify 86A (1) · addyosmani/agent-skills 86A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `doc-coauthoring` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 90A (1) · blader/humanizer 76B (1) · anthropics/skills 74B (1) | `humanizer` 99/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | obsidianmd/obsidian-skills 76B (6) · ComposioHQ/awesome-claude-skills 65B (1) · AgriciDaniel/claude-obsidian 63C (11) | `defuddle` 93/B, `knap` 93/B, `obsidian-cli` 93/B, `obsidian-headless` 93/B |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 78B (4) · anthropics/skills 74B (3) · google/skills 66B (25) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `agent-platform-endpoint-management` 100/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 90A (2) · JuliusBrussee/caveman 88A (22) · addyosmani/agent-skills 86A (2) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 93A (1) · Panniantong/Agent-Reach 82A (1) · upstash/context7 81A (4) | `agent-reach` 95/A, `find-docs` 95/A, `graphify` 94/A, `context7-cli` 88/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | heygen-com/hyperframes 91A (2) · nexu-io/open-design 90A (2) · obra/superpowers 81A (1) | `writing-skills` 100/A, `agent-development` 100/B, `breakdown-diagnosis` 100/B, `breakdown-to-next-report` 100/B |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | heygen-com/hyperframes 91A (10) · nexu-io/open-design 90A (17) · harry0703/MoneyPrinterTurbo 87A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | OpenMontageInc/OpenMontage 82A (12) · krillinai/OpenCreator 66B (7) · Leonxlnx/earshot 60C (2) | `lyria` 100/A, `music` 100/A, `sound-effects` 100/A, `speech-to-text` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 82A (16) · digitalsamba/claude-code-video-toolkit 59C (4) · yerel/kendi 16D (1) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | heygen-com/hyperframes 91A (3) · nexu-io/open-design 90A (2) · OpenMontageInc/OpenMontage 82A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 82A (48) · anthropics/knowledge-work-plugins 75B (58) · AgriciDaniel/claude-seo 74B (28) | `ab-testing` 100/A, `ad-creative` 100/A, `ai-seo` 100/A, `analytics` 100/A |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 75B (26) · Jakeschincariol/day-trader-skill 49D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 75B (69) · Jakeschincariol/founder-skill 42D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 75B (10) · google/skills 66B (2) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 90A (1) · nexscope-ai/eCommerce-Skills 41D (156) · nexscope-ai/Amazon-Skills 38D (52) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 78B (90) · anthropics/knowledge-work-plugins 75B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 78B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 78B (27) · Orchestra-Research/AI-Research-SKILLs 57C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 78B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 69B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 78B (2) · earthtojake/text-to-cad 73B (17) | `bambu-labs` 98/B, `dfam-check` 98/B, `dfm` 98/B, `engineering-drawing` 98/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 475550 | 64538.9 | 453 | 9334 | 2026-11-20 | 🔥 |
| 2 | Graphify-Labs/graphify | 93 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 152526 | 19731.0 | 432 | 1634 | 2026-11-23 | 🔥 |
| 3 | heygen-com/hyperframes | 91 A | 15 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/2 | Apache-2.0 | ✓ | 88929 | 10438.0 | 155 | 3862 | 2026-11-23 | 🔥 |
| 4 | vercel/next.js | 91 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143619 | 1179.4 | 4196 | 1595 | 2026-11-23 | 🔥 |
| 5 | nexu-io/open-design | 90 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 109169 | 15803.5 | 456 | 451 | 2026-11-19 |  |
| 6 | react/react | 89 A | 0 | - | 0/0/0 | MIT | ✓ | 252814 | 1558.3 | 2028 | 154 | 2026-10-14 |  |
| 7 | JuliusBrussee/caveman | 88 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 122405 | 15902.2 | 116 | 1631 | 2026-11-22 |  |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 88 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 153269 | 12978.8 | 124 | 91 | 2026-08-13 |  |
| 9 | DietrichGebert/ponytail | 87 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 197495 | 36387.0 | 133 | 162 | 2026-10-29 | 🔥 |
| 10 | harry0703/MoneyPrinterTurbo | 87 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 145237 | 4468.8 | 180 | 516 | 2026-11-23 | 🔥 |
| 11 | microsoft/playwright | 87 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 100913 | 1195.5 | 833 | 799 | 2026-11-13 | 🔥 |
| 12 | addyosmani/agent-skills | 86 A | 26 | 01-planlama-metodoloji (9), 06-devops-guvenlik-performans (5) | 26/0/0 | MIT |  | 119994 | 12935.5 | 104 | 402 | 2026-11-18 | 🔥 |
| 13 | tt-a1i/archify | 86 A | 3 | 02-kod-kalitesi-review (1), 03-test-hata-ayiklama (1) | 3/0/0 | Apache-2.0 |  | 99103 | 13510.0 | 108 | 2597 | 2026-11-23 |  |
| 14 | anthropics/claude-code | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 156823 | 7449.1 | 59 | 377 | 2026-11-23 | 🔥 |
| 15 | pbakaus/impeccable | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 115615 | 9422.8 | 67 | 2158 | 2026-11-22 | 🔥 |
| 16 | ruvnet/ruflo | 84 A | 0 | - | 0/0/0 | MIT |  | 82330 | 4634.9 | 104 | 3241 | 2026-11-23 |  |
| 17 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 331357 | 34262.8 | 10 | 102 | 2026-10-29 | 🔥 |
| 18 | OpenMontageInc/OpenMontage | 82 A | 53 | 03-ai-gorsel-video-modelleri (16), 02-ses-muzik-konusma (12) | 21/11/21 | AGPL-3.0 |  | 82708 | 10476.3 | 128 | 277 | - | 🔥 |
| 19 | Panniantong/Agent-Reach | 82 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 114256 | 12723.0 | 56 | 161 | 2026-11-01 | 🔥 |
| 20 | coreyhaines31/marketingskills | 82 A | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 62253 | 6046.3 | 92 | 1176 | 2026-11-23 | 🔥 |
| 21 | Leonxlnx/taste-skill | 81 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 120649 | 13193.3 | 27 | 163 | 2026-11-07 | 🔥 |
| 22 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 325028 | 24041.0 | 44 | 6 | 2026-11-03 | 🔥 |
| 23 | remotion-dev/remotion | 81 A | 13 | 01-video-uretim-montaj (13) | 10/3/0 | NOASSERTION | ✓ | 75207 | 975.0 | 513 | 6731 | 2026-11-23 | 🔥 |
| 24 | upstash/context7 | 81 A | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 65348 | 3267.4 | 148 | 331 | 2026-11-17 |  |
| 25 | garrytan/gbrain | 80 A | 0 | - | 0/0/0 | MIT |  | 33486 | 4369.0 | 140 | 15294 | 2026-11-23 |  |
| 26 | K-Dense-AI/scientific-agent-skills | 78 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 58227 | 4414.2 | 57 | 69 | 2026-10-01 | 🔥 |
| 27 | anthropics/claude-plugins-official | 78 B | 46 | 04-skill-plugin-yazimi (30), 02-agent-orkestrasyon (5) | 46/0/0 | Apache-2.0 | ✓ | 48060 | 3959.4 | 49 | 1446 | - | 🔥 |
| 28 | github/awesome-copilot | 78 B | 0 | - | 0/0/0 | MIT |  | 41486 | 2375.1 | 600 | 1111 | - |  |
| 29 | pixijs/pixijs | 78 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48879 | 294.0 | 653 | 110 | 2026-11-11 |  |
| 30 | GoogleChrome/lighthouse | 77 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31195 | 242.4 | 401 | 231 | 2026-10-27 |  |
| 31 | davila7/claude-code-templates | 77 B | 0 | - | 0/0/0 | MIT |  | 34144 | 2043.3 | 192 | 686 | 2026-10-09 |  |
| 32 | ayghri/i-have-adhd | 76 B | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 62063 | 9675.5 | 53 | 79 | 2026-10-19 |  |
| 33 | blader/humanizer | 76 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 72730 | 7132.2 | 30 | 71 | 2026-11-10 | 🔥 |
| 34 | obsidianmd/obsidian-skills | 76 B | 7 | 04-not-alma-bilgi-yonetimi (6), 02-diyagram-dokumantasyon (1) | 7/0/0 | MIT |  | 53557 | 4994.3 | 28 | 47 | 2026-11-20 |  |
| 35 | anthropics/knowledge-work-plugins | 75 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 36736 | 3661.6 | 32 | 414 | - | 🔥 |
| 36 | cathrynlavery/diagram-design | 75 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 70942 | 9714.6 | 76 | 355 | - |  |
| 37 | google/elephant-goldfish-model | 75 B | 8 | 01-planlama-metodoloji (8) | 8/0/0 | Apache-2.0 |  | 22419 | 9465.8 | 39 | 221 | 2026-11-06 | 🔥 |
| 38 | AgriciDaniel/claude-seo | 74 B | 28 | 01-satis-pazarlama-musteri (28) | 28/0/0 | MIT |  | 31927 | 3346.8 | 52 | 471 | 2026-11-15 | 🔥 |
| 39 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 199461 | 14167.3 | 17 | 12 | - | 🔥 |
| 40 | earthtojake/text-to-cad | 73 B | 17 | 05-cad-imalat-robotik (17) | 17/0/0 | MIT |  | 27238 | 3833.5 | 34 | 495 | 2026-11-23 | 🔥 |
| 41 | motiondivision/motion | 72 B | 0 | - | 0/0/0 | MIT | ✓ | 35493 | 368.3 | 147 | 1370 | - |  |
| 42 | latent-spaces/brag | 70 B | 2 | 01-video-uretim-montaj (2) | 2/0/0 | MIT |  | 22360 | 4222.0 | 20 | 58 | 2026-11-15 |  |
| 43 | teng-lin/notebooklm-py | 70 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20356 | 1927.8 | 44 | 398 | 2026-10-29 |  |
| 44 | JuneYaooo/rea-video | 69 B | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 12660 | 12660.0 | 24 | 200 | 2026-11-11 |  |
| 45 | cloudflare/security-audit-skill | 69 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 77538 | 14824.9 | 4 | 3 | - | 🔥 |
| 46 | wanshuiyin/Auto-claude-code-research-in-sleep | 69 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 19655 | 2307.0 | 108 | 185 | 2026-09-28 |  |
| 47 | Nutlope/hallmark | 68 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 60068 | 8654.3 | 12 | 147 | - | 🔥 |
| 48 | vercel-labs/agent-skills | 68 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 34809 | 3014.8 | 29 | 20 | 2026-11-20 | 🔥 |
| 49 | Vincentwei1021/video-shotcraft | 67 B | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 22280 | 5291.5 | 17 | 54 | 2026-09-01 | 🔥 |
| 50 | multica-ai/andrej-karpathy-skills | 67 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 235311 | 23765.6 | 7 | 0 | - | 🔥 |
| 51 | google/skills | 66 B | 217 | 06-devops-guvenlik-performans (118), 04-mimari-api-veritabani (53) | 41/176/0 | Apache-2.0 |  | 24582 | 3139.9 | 9 | 361 | - | 🔥 |
| 52 | krillinai/OpenCreator | 66 B | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14512 | 624.0 | 37 | 509 | 2026-11-23 |  |
| 53 | ComposioHQ/awesome-claude-skills | 65 B | 4 | 03-yazi-iletisim-icerik (2), 04-not-alma-bilgi-yonetimi (1) | 3/1/0 | yok | ✓ | 80171 | 6047.6 | 29 | 0 | - |  |
| 54 | kajisho5/ffmpeg-skill | 65 B | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 10214 | 3786.7 | 13 | 705 | 2026-11-23 | 🔥 |
| 55 | android/skills | 64 C | 38 | 08-mobil-uygulama (38) | 37/1/0 | Apache-2.0 | ✓ | 10721 | 1288.2 | 8 | 34 | 2026-11-23 | 🔥 |
| 56 | lemomo-ai/lemo-opuscar | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 20300 | 10459.7 | 10 | 148 | 2026-11-12 |  |
| 57 | AgriciDaniel/claude-obsidian | 63 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16720 | 2200.4 | 11 | 98 | 2026-10-21 |  |
| 58 | jacob-bd/gemini-notebook-mcp-cli | 63 C | 0 | - | 0/0/0 | MIT |  | 6562 | 593.7 | 72 | 242 | 2026-11-22 |  |
| 59 | Donchitos/Claude-Code-Game-Studios | 62 C | 72 | 06-oyun-2d-grafik (72) | 72/0/0 | MIT |  | 40723 | 4343.8 | 1 | 6 | 2026-11-09 | 🔥 |
| 60 | dreammis/social-auto-upload | 62 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16865 | 472.1 | 42 | 19 | 2026-10-22 |  |
| 61 | browser-use/video-use | 61 C | 2 | 01-video-uretim-montaj (1), 04-motion-graphics-karakter (1) | 1/1/0 | MIT |  | 31493 | 4236.2 | 8 | 5 | - |  |
| 62 | Leonxlnx/earshot | 60 C | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 5643 | 4288.7 | 8 | 189 | 2026-11-20 |  |
| 63 | digitalsamba/claude-code-video-toolkit | 59 C | 14 | 01-video-uretim-montaj (7), 03-ai-gorsel-video-modelleri (4) | 4/8/2 | MIT |  | 2719 | 236.2 | 17 | 515 | 2026-11-22 |  |
| 64 | tradermonty/claude-trading-skills | 59 C | 0 | - | 0/0/0 | MIT |  | 8032 | 608.9 | 46 | 500 | - |  |
| 65 | cloudflare/skills | 58 C | 22 | 06-devops-guvenlik-performans (22) | 12/7/3 | Apache-2.0 | ✓ | 3439 | 299.6 | 50 | 271 | - | 🔥 |
| 66 | tddworks/baguette | 58 C | 2 | 04-skill-plugin-yazimi (2) | 2/0/0 | Apache-2.0 |  | 2346 | 344.5 | 18 | 577 | 2026-11-22 |  |
| 67 | zubair-trabzada/geo-seo-claude | 58 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11830 | 1289.0 | 25 | 57 | - |  |
| 68 | Orchestra-Research/AI-Research-SKILLs | 57 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14770 | 1163.2 | 17 | 0 | 2026-06-16 |  |
| 69 | AgriciDaniel/claude-ads | 56 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 11278 | 1198.8 | 2 | 42 | 2026-10-16 |  |
| 70 | WyattBlue/auto-editor | 56 C | 5 | 01-video-uretim-montaj (5) | 5/0/0 | Unlicense |  | 6065 | 76.9 | 17 | 330 | 2026-11-23 |  |
| 71 | vudovn/ag-kit | 56 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8225 | 796.3 | 10 | 8 | 2026-08-31 |  |
| 72 | czlonkowski/n8n-skills | 55 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6702 | 509.4 | 7 | 33 | 2026-10-24 | 🔥 |
| 73 | expo/skills | 55 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4224 | 357.7 | 31 | 43 | - | 🔥 |
| 74 | openai/plugins | 55 C | 0 | - | 0/0/0 | yok | ✓ | 8253 | 946.8 | 63 | 13 | - |  |
| 75 | zarazhangrui/frontend-slides | 55 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 32820 | 3325.8 | 9 | 0 | 2026-05-26 |  |
| 76 | greensock/gsap-skills | 54 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 18965 | 2175.6 | 4 | 0 | - |  |
| 77 | Ryze-AI-Adgent/open-seo-mcp-skills | 51 C | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 10649 | 3721.0 | 1 | 16 | - |  |
| 78 | darkroomengineering/satus | 51 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1023 | 16.6 | 19 | 180 | 2026-08-28 |  |
| 79 | wondelai/skills | 51 C | 0 | - | 0/0/0 | MIT |  | 2774 | 282.0 | 3 | 16 | 2026-08-29 |  |
| 80 | Jakeschincariol/day-trader-skill | 49 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 9332 | 8105.5 | 1 | 1 | - |  |
| 81 | Jakeschincariol/replica-skill | 49 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 10446 | 6106.9 | 1 | 1 | - |  |
| 82 | veedstudio/open-edit | 49 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 1853 | 450.6 | 3 | 15 | 2026-08-03 |  |
| 83 | feitangyuan/onetake | 48 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 4414 | 2274.3 | 3 | 22 | 2026-10-08 |  |
| 84 | chrisbanes/skills | 47 D | 20 | 04-skill-plugin-yazimi (19), 05-git-pr-surum (1) | 20/0/0 | Apache-2.0 |  | 1165 | 180.7 | 4 | 152 | 2026-11-23 |  |
| 85 | Jakeschincariol/instagram-agent-skill | 46 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 8644 | 3649.7 | 1 | 2 | - |  |
| 86 | Jakeschincariol/youtube-agent-skill | 46 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 7129 | 3140.9 | 1 | 1 | - |  |
| 87 | hardikpandya/stop-slop | 46 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 19153 | 1836.8 | 2 | 0 | - |  |
| 88 | sarpstar/cinecode | 46 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 2916 | 2916.0 | 3 | 9 | - |  |
| 89 | nateherkai/scroll-craft | 44 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 5383 | 1740.9 | 1 | 8 | - |  |
| 90 | CloudAI-X/threejs-skills | 43 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 4361 | 429.0 | 1 | 20 | - |  |
| 91 | huytieu/COG-second-brain | 43 D | 0 | - | 0/0/0 | MIT |  | 1515 | 113.7 | 6 | 6 | 2026-10-23 |  |
| 92 | shadcn-labs/snapcn | 43 D | 7 | 04-motion-graphics-karakter (7) | 0/7/0 | MIT |  | 687 | 169.8 | 3 | 236 | - |  |
| 93 | Jakeschincariol/founder-skill | 42 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 4777 | 3025.4 | 1 | 1 | - |  |
| 94 | lottiefiles/motion-design-skill | 42 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 3621 | 428.3 | 2 | 5 | - |  |
| 95 | yaojingang/yao-meta-skill | 42 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2742 | 350.2 | 4 | 10 | - |  |
| 96 | nexscope-ai/eCommerce-Skills | 41 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1511 | 183.0 | 7 | 3 | - |  |
| 97 | ythx-101/live-panel-skill | 41 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 879 | 513.9 | 4 | 41 | - |  |
| 98 | AbubakrChan/product-launch-motion | 40 D | 1 | 04-motion-graphics-karakter (1) | 1/0/0 | MIT |  | 529 | 134.0 | 2 | 44 | 2026-10-12 |  |
| 99 | Jakeschincariol/linkedin-agent-skill | 40 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3889 | 1515.7 | 1 | 1 | - |  |
| 100 | howseen-ai/claude-motion-design | 40 D | 0 | - | 0/0/0 | MIT |  | 889 | 466.0 | 1 | 32 | - |  |
| 101 | smyrgeorge/sqlx4k | 40 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 323 | 11.0 | 4 | 242 | 2026-11-01 |  |
| 102 | nexscope-ai/Amazon-Skills | 38 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 889 | 104.3 | 5 | 3 | - |  |
| 103 | Barty-Bart/motion-graphics | 37 D | 5 | 04-motion-graphics-karakter (5) | 5/0/0 | NOASSERTION |  | 1480 | 749.9 | 4 | 10 | - |  |
| 104 | nateherkai/herk-edit-kit | 37 D | 10 | 01-video-uretim-montaj (10) | 5/5/0 | NOASSERTION |  | 3103 | 428.8 | 1 | 13 | - |  |
| 105 | 40RTY-ai/shopify-admin-skills | 36 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 205 | 27.5 | 3 | 4 | 2026-06-17 |  |
| 106 | echris6/motion-video-kit | 36 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 1450 | 760.0 | 1 | 7 | - |  |
| 107 | heyitsnoah/claudesidian | 36 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2614 | 181.4 | 3 | 0 | 2026-04-11 |  |
| 108 | rshankras/claude-code-apple-skills | 36 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 904 | 70.3 | 4 | 11 | - |  |
| 109 | zanwei/design-dna | 36 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2150 | 265.7 | 3 | 3 | - |  |
| 110 | heygen-com/hyperframes-community-skills | 35 D | 7 | 01-video-uretim-montaj (7) | 6/1/0 | Apache-2.0 | ✓ | 292 | 97.5 | 3 | 6 | - |  |
| 111 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 2 | 05-e-ticaret-pazaryeri (2) | 2/0/0 | MIT |  | 41 | 4.7 | 3 | 16 | 2026-11-13 |  |
| 112 | evanca/flutter-ai-rules | 33 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 675 | 35.3 | 2 | 13 | - |  |
| 113 | Prisma-Labs-Dev/apple-skills | 32 D | 27 | 04-skill-plugin-yazimi (27) | 27/0/0 | MIT |  | 359 | 39.3 | 3 | 4 | - |  |
| 114 | hamen/compose_skill | 32 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 380 | 51.3 | 3 | 0 | 2026-07-07 |  |
| 115 | kylezantos/design-motion-principles | 32 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1641 | 158.9 | 1 | 0 | 2026-05-21 |  |
| 116 | lemomo-ai/lemo-wake | 32 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 380 | 222.2 | 1 | 15 | 2026-10-05 |  |
| 117 | xjli360/sealeap-amazon-skills | 32 D | 0 | - | 0/0/0 | MIT |  | 451 | 144.3 | 1 | 9 | - |  |
| 118 | RevenueCat/play-billing-skills | 31 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 10.4 | 1 | 28 | 2026-10-15 |  |
| 119 | better-i18n/oss | 31 D | 1 | 04-skill-plugin-yazimi (1) | 0/1/0 | MIT |  | 21 | 2.2 | 5 | 25 | 2026-10-04 |  |
| 120 | freshtechbro/claudedesignskills | 31 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1438 | 110.7 | 1 | 0 | - |  |
| 121 | tuzhechen2005/opus-video-skills | 30 D | 2 | 04-motion-graphics-karakter (2) | 2/0/0 | NOASSERTION |  | 562 | 289.6 | 3 | 9 | - |  |
| 122 | mercadopago/mercadopago-claude-marketplace | 29 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 33 | 3.7 | 10 | 6 | - |  |
| 123 | tuist/fuckingapproachableswiftconcurrency | 29 D | 0 | - | 0/0/0 | MIT |  | 159 | 14.3 | 15 | 0 | - |  |
| 124 | moiz-za/etsy-seller-seo-system | 28 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 54 | 8.6 | 2 | 13 | 2026-10-23 |  |
| 125 | namedtoaster/The-Last-Mile | 28 D | 19 | 04-skill-plugin-yazimi (18), 02-agent-orkestrasyon (1) | 18/1/0 | MIT |  | 41 | 28.3 | 3 | 146 | - |  |
| 126 | tugrawork-creator/saas-motion-kit | 28 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | NOASSERTION |  | 292 | 147.9 | 1 | 8 | 2026-10-04 |  |
| 127 | twostraws/SwiftData-Agent-Skill | 28 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 472 | 55.6 | 2 | 1 | 2026-03-11 |  |
| 128 | wj-sidiss/etsy-otomasyon-full-full-surum | 28 D | 0 | - | 0/0/0 | MIT |  | 57 | 57.0 | 1 | 8 | 2026-11-01 |  |
| 129 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 173 | 86.2 | 1 | 11 | - |  |
| 130 | ehmo/platform-design-skills | 27 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 651 | 66.9 | 1 | 0 | - |  |
| 131 | sirioberati/YouTube-AI-Video-Editing-System | 27 D | 0 | - | 0/0/0 | MIT |  | 170 | 152.0 | 1 | 4 | - |  |
| 132 | xianyu110/ecommerce-image-skills | 27 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 192 | 114.4 | 1 | 7 | - |  |
| 133 | Livsy90/iOS-Performance-Agent-Skills | 26 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 121 | 20.1 | 2 | 0 | 2026-07-12 |  |
| 134 | finsilabs/awesome-ecommerce-skills | 26 D | 179 | 05-e-ticaret-pazaryeri (179) | 161/18/0 | MIT |  | 67 | 7.9 | 4 | 3 | - |  |
| 135 | dpconde/claude-android-skill | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 363 | 31.3 | 1 | 0 | - |  |
| 136 | thatrebeccarae/claude-marketing | 24 D | 54 | 04-skill-plugin-yazimi (50), 02-tasarim-sistemi-marka (2) | 52/0/2 | MIT |  | 214 | 22.6 | 2 | 0 | - |  |
| 137 | ParthJadhav/ios-marketing-capture | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 266 | 35.5 | 1 | 1 | - |  |
| 138 | Lonsdale201/wp-agent-skills | 22 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 3.8 | 3 | 19 | - |  |
| 139 | MADTeacher/mad-agents-skills | 21 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 114 | 11.0 | 2 | 0 | - |  |
| 140 | YildizDikme/claude-video-edit | 21 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 58 | 58.0 | 1 | 3 | - |  |
| 141 | dadederk/iOS-Accessibility-Agent-Skill | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 177 | 17.8 | 1 | 0 | - |  |
| 142 | leodavincs/kalem | 21 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 120 | 120.0 | 1 | 7 | - |  |
| 143 | Harishwarrior/flutter-claude-skills | 20 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 69 | 5.3 | 2 | 3 | - |  |
| 144 | Shopify/agent-skills | 20 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 111 | 14.2 | 1 | 0 | - |  |
| 145 | tanujrajputdev/shopify-theme-audit-skill | 20 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 46 | 8.2 | 3 | 2 | - |  |
| 146 | Kappaemme-git/codex-phone-lab | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 96 | 15.5 | 1 | 0 | - |  |
| 147 | Viniciuscarvalho/swift-code-reviewer-skill | 19 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.1 | 5 | 0 | 2026-05-07 |  |
| 148 | oldred-byte/ec-visual-skill | 19 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 117 | 17.5 | 1 | 0 | - |  |
| 149 | avenoxai/avenox-video-kurgu-notlari | 17 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 30 | 30.0 | 1 | 1 | - |  |
| 150 | yohannescodes/apple-app-review-compliance | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 23 | 18.4 | 1 | 4 | - |  |
| 151 | Trendyol/trendyol-integration-developer-tool | 16 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 13 | 2.0 | 3 | 0 | - |  |
| 152 | jazzychad/ios-code-audit | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 6.7 | 1 | 0 | - |  |
| 153 | arjitj2/swiftui-design-principles | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 35 | 3.9 | 1 | 0 | - |  |
| 154 | lemomo-ai/codex-radar | 14 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 40 | 7.1 | 1 | 8 | - |  |
| 155 | mmiani/kotlin-kmp-claude-agent-skills | 13 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 94 | 11.8 | 1 | 0 | - |  |
| 156 | avenoxai/higgsfield-studio | 10 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 17 | 5.3 | 1 | 2 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 88 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 82 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `find-docs` 95/A, `tailwind-design-system` 94/A, `remotion-create` 90/A, `web-artifacts-builder` 90/B, `context7-mcp` 88/A | tasarim-teknolojileri.md |
| 3 | d3/d3 | 78 B | v7.9 | `d3-viz` 94/A, `d3-visualization` 97/A | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 76 B | - | `ffmpeg` 94/A, `video-understand` 95/A, `ffmpeg-skill` 95/B, `character-animation-qa` 87/A, `product-launch-motion` 72/D, `kinetic-reel` 72/D, `cut-mistakes` 65/D, `cut-silences` 65/D | kutuphaneler.md |
| 5 | ManimCommunity/manim | 74 B | v0.22 | `manim-composer` 95/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 94/A, `remotion-to-hyperframes` 97/A, `manim-video` 84/C | tasarim-teknolojileri.md |
| 6 | VoltAgent/awesome-design-md | 73 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/A | tasarim-teknolojileri.md |
| 7 | pmndrs/react-three-fiber | 73 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 57/D, `blender-web-pipeline` 57/D, `web3d-integration-patterns` 57/D, `substance-3d-texturing` 49/D, `modern-web-design` 47/D | tasarim-teknolojileri.md |
| 8 | openai/whisper | 72 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 95/A, `azure-speech-to-text` 95/A, `krillinai-subtitle` 90/B, `whisper` 87/C, `auto-editor-transcribe` 84/C, `ajanla-video-kurgu` 69/D | kutuphaneler.md |
| 9 | KaTeX/KaTeX | 69 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 95/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 89/B | kutuphaneler.md |
| 10 | blender/blender | 69 B | - | `blender-web-pipeline` 57/D, `3d-asset-generation` 95/A, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A, `render` 96/B, `blender` 81/C | kutuphaneler.md |
| 11 | 666ghj/MiroFish | 67 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 12 | QwikDev/partytown | 65 B | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 65 B | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 68/D | tasarim-teknolojileri.md |
| 14 | darkroomengineering/lenis | 65 B | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 57/D | tasarim-teknolojileri.md |
| 15 | dequelabs/axe-core | 65 B | v4.14 (MPL-2.0) | `accessibility-engineering` 100/A, `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 85/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 16 | librosa/librosa | 65 B | - | `media-use` 100/A | kutuphaneler.md |
| 17 | DavidHDev/react-bits | 64 C | - | `animated-component-libraries` 57/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 18 | Fei-Away/Codex-Dream-Skin | 62 C | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 19 | paperjs/paper.js | 62 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 86/A | tasarim-teknolojileri.md |
| 20 | airbnb/lottie-web | 61 C | v5.13 | `lottie-animations` 57/D, `remotion-to-hyperframes` 97/A, `motion-design` 81/D, `lottie-bodymovin` 79/A, `flutter-pre-caching` 78/D, `rive-interactive` 57/D | tasarim-teknolojileri.md |
| 21 | pmndrs/drei | 61 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 22 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 23 | ai/size-limit | 57 C | 14.2 (T5) | `nextjs-react-expert` 75/C, `react-doctor` 75/C | tasarim-teknolojileri.md |
| 24 | motion-canvas/motion-canvas | 57 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 95/A | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 65/D, `canvas-procedural-animation` 86/A | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 54 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 27 | rough-stuff/rough | 50 C | v3.1 | `camera-3d-captions` 79/D, `day-in-my-life` 72/D | tasarim-teknolojileri.md |
| 28 | greensock/GSAP | 49 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 48 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | barvian/number-flow | 46 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 31 | opentypejs/opentype.js | 46 D | 2.0 | `svg-character-animation` 95/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 32 | figma/code-connect | 45 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 45 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | argyleink/open-props | 44 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 35 | JohnHeibel/ClaudeAnimationBase | 43 D | - | `canvas-procedural-animation` 86/A, `algorithmic-art` 81/B, `svg-character-animation` 95/A | tasarim-teknolojileri.md |
| 36 | pmndrs/cannon-es | 43 D | v0.20 | `threejs-world-generation` 94/A, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 37 | zhuyansen/awesome-claude-video-skills | 41 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 38 | metafizzy/zdog | 40 D | v1.1 | `svg-character-animation` 95/A, `canvas-procedural-animation` 86/A, `lightweight-3d-effects` 56/D | tasarim-teknolojileri.md |
| 39 | meyda/meyda | 40 D | - | `canvas-procedural-animation` 86/A | kutuphaneler.md |
| 40 | oframe/ogl | 39 D | - | `lightweight-3d-effects` 56/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 41 | 14islands/r3f-scroll-rig | 35 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 57/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 57/D, `barba-js` 57/D, `locomotive-scroll` 57/D, `scroll-reveal-libraries` 57/D | tasarim-teknolojileri.md |
| 42 | jwagner/simplex-noise.js | 34 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 79/D, `threejs-world-generation` 94/A | tasarim-teknolojileri.md |
| 43 | linvi/tweetinvi | 34 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 44 | nevertoday/350-layout-compositions | 33 D | - | `design-taste-frontend` 100/A, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 45 | pmndrs/react-three-a11y | 29 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 46 | arturitu/the-delegation | 24 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
