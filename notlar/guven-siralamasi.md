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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 90A (13) · nextlevelbuilder/ui-ux-pro-max-skill 87A (2) · anthropics/claude-code 85A (1) | `impeccable` 100/A, `design-taste-frontend` 100/A, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 90A (3) · nextlevelbuilder/ui-ux-pro-max-skill 87A (4) · OpenMontageInc/OpenMontage 81A (1) | `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A, `tailwind-design-system` 93/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 90A (7) · OpenMontageInc/OpenMontage 81A (2) · greensock/gsap-skills 52C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 52C (1) · nateherkai/scroll-craft 43D (1) · freshtechbro/claudedesignskills 30D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 57/D, `locomotive-scroll` 57/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 42D (13) · freshtechbro/claudedesignskills 30D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 90A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 61C (72) | `estimate` 98/C, `scope-check` 98/C, `test-setup` 98/C, `asset-audit` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 90A (14) · nextlevelbuilder/ui-ux-pro-max-skill 87A (1) · OpenMontageInc/OpenMontage 81A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 90A (3) · microsoft/playwright 86A (2) · addyosmani/agent-skills 86A (1) | `playwright-trace` 100/A, `browser-testing-with-devtools` 98/A, `playwright-component-testing` 98/A, `export-download-debugging` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 86A (9) · mattpocock/skills 83A (30) · obra/superpowers 80A (3) | `accessibility-engineering` 100/A, `ask-matt` 100/A, `codebase-design` 100/A, `diagnosing-bugs` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 86A (2) · tt-a1i/archify 85A (1) | `code-review-and-quality` 100/A, `code-simplification` 100/A, `ponytail` 100/A, `ponytail-audit` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 86A (2) · tt-a1i/archify 85A (1) · obra/superpowers 80A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 86A (2) · google/skills 65B (53) · vudovn/ag-kit 54C (6) | `api-and-interface-design` 100/A, `alloydb-basics` 100/B, `bigquery-basics` 100/B, `bigquery-bigframes` 100/B |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 90A (2) · addyosmani/agent-skills 86A (2) · obra/superpowers 80A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 86A (5) · anthropics/claude-plugins-official 77B (1) | `security-and-hardening` 100/A, `cloud-operator-share-context` 100/B, `cloud-run-alert-configuration` 100/B, `cloud-trace-querying` 100/B |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 86A (1) · anthropics/claude-plugins-official 77B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | google/skills 65B (11) · android/skills 62C (38) · expo/skills 53C (24) | `google-mobile-ads-banner` 100/B, `google-mobile-ads-get-started` 100/B, `google-mobile-ads-interstitial` 100/B, `google-mobile-ads-rewarded` 100/B |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 90A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 74B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 90A (2) · addyosmani/agent-skills 86A (1) · tt-a1i/archify 85A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `doc-coauthoring` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 90A (1) · blader/humanizer 75B (1) · anthropics/skills 74B (1) | `humanizer` 98/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | obsidianmd/obsidian-skills 75B (6) · ComposioHQ/awesome-claude-skills 64C (1) · AgriciDaniel/claude-obsidian 62C (11) | `defuddle` 92/B, `knap` 92/B, `obsidian-cli` 92/B, `obsidian-headless` 92/B |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 77B (4) · anthropics/skills 74B (3) · google/skills 65B (25) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `agent-platform-endpoint-management` 100/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 90A (2) · JuliusBrussee/caveman 87A (22) · addyosmani/agent-skills 86A (2) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 93A (1) · Panniantong/Agent-Reach 82A (1) · upstash/context7 80A (4) | `agent-reach` 95/A, `find-docs` 95/A, `graphify` 94/A, `context7-cli` 88/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | heygen-com/hyperframes 91A (2) · nexu-io/open-design 90A (2) · obra/superpowers 80A (1) | `writing-skills` 100/A, `agent-development` 100/B, `breakdown-diagnosis` 100/B, `breakdown-to-next-report` 100/B |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | heygen-com/hyperframes 91A (10) · nexu-io/open-design 90A (17) · harry0703/MoneyPrinterTurbo 86A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | OpenMontageInc/OpenMontage 81A (12) · krillinai/OpenCreator 65B (7) · Leonxlnx/earshot 59C (2) | `lyria` 100/A, `music` 100/A, `sound-effects` 100/A, `speech-to-text` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 81A (16) · digitalsamba/claude-code-video-toolkit 57C (4) · yerel/kendi 17D (1) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | heygen-com/hyperframes 91A (3) · nexu-io/open-design 90A (2) · OpenMontageInc/OpenMontage 81A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 81A (48) · anthropics/knowledge-work-plugins 74B (58) · AgriciDaniel/claude-seo 73B (28) | `ab-testing` 100/A, `analytics` 100/A, `aso` 100/A, `attribution` 100/A |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 74B (26) · Jakeschincariol/day-trader-skill 48D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 74B (69) · Jakeschincariol/founder-skill 40D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 74B (10) · google/skills 65B (2) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 90A (1) · nexscope-ai/eCommerce-Skills 39D (156) · nexscope-ai/Amazon-Skills 37D (52) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 77B (90) · anthropics/knowledge-work-plugins 74B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 77B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 77B (27) · Orchestra-Research/AI-Research-SKILLs 56C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 77B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 67B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 77B (2) · earthtojake/text-to-cad 72B (17) | `bambu-labs` 98/B, `dfam-check` 98/B, `dfm` 98/B, `engineering-drawing` 98/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 472728 | 64733.9 | 445 | 8676 | 2026-11-20 | 🔥 |
| 2 | Graphify-Labs/graphify | 93 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 151595 | 19778.9 | 431 | 1637 | 2026-11-21 | 🔥 |
| 3 | heygen-com/hyperframes | 91 A | 15 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/2 | Apache-2.0 | ✓ | 87822 | 10388.3 | 154 | 3731 | 2026-11-21 | 🔥 |
| 4 | nexu-io/open-design | 90 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 108838 | 15907.1 | 456 | 497 | 2026-11-19 |  |
| 5 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143633 | 1180.1 | 4194 | 1621 | 2026-11-20 | 🔥 |
| 6 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 252852 | 1559.2 | 2028 | 160 | 2026-10-14 |  |
| 7 | JuliusBrussee/caveman | 87 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 121971 | 15982.4 | 116 | 1634 | 2026-11-08 |  |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 87 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 152496 | 12985.7 | 120 | 92 | 2026-08-13 |  |
| 9 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 196330 | 36616.1 | 133 | 159 | 2026-10-29 | 🔥 |
| 10 | addyosmani/agent-skills | 86 A | 26 | 01-planlama-metodoloji (9), 06-devops-guvenlik-performans (5) | 26/0/0 | MIT |  | 119573 | 12982.2 | 105 | 404 | 2026-11-18 | 🔥 |
| 11 | harry0703/MoneyPrinterTurbo | 86 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 144983 | 4470.1 | 178 | 522 | 2026-11-07 | 🔥 |
| 12 | microsoft/playwright | 86 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 100741 | 1194.4 | 833 | 794 | 2026-11-13 | 🔥 |
| 13 | anthropics/claude-code | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 156567 | 7460.2 | 59 | 364 | 2026-11-20 | 🔥 |
| 14 | tt-a1i/archify | 85 A | 3 | 02-kod-kalitesi-review (1), 03-test-hata-ayiklama (1) | 3/0/0 | Apache-2.0 |  | 98573 | 13559.4 | 92 | 1622 | 2026-11-08 |  |
| 15 | pbakaus/impeccable | 84 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 114513 | 9383.3 | 67 | 2182 | 2026-11-18 | 🔥 |
| 16 | ruvnet/ruflo | 84 A | 0 | - | 0/0/0 | MIT |  | 82225 | 4646.2 | 104 | 3221 | 2026-11-21 |  |
| 17 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 329737 | 34328.8 | 10 | 105 | 2026-10-29 | 🔥 |
| 18 | Panniantong/Agent-Reach | 82 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 113756 | 12760.8 | 55 | 161 | 2026-11-01 | 🔥 |
| 19 | OpenMontageInc/OpenMontage | 81 A | 53 | 03-ai-gorsel-video-modelleri (16), 02-ses-muzik-konusma (12) | 21/11/21 | AGPL-3.0 |  | 82109 | 10487.9 | 129 | 277 | - | 🔥 |
| 20 | coreyhaines31/marketingskills | 81 A | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 61873 | 6048.0 | 93 | 1170 | 2026-11-20 | 🔥 |
| 21 | Leonxlnx/taste-skill | 80 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 119726 | 13187.2 | 27 | 161 | 2026-11-07 | 🔥 |
| 22 | obra/superpowers | 80 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 323687 | 24058.9 | 44 | 6 | 2026-11-03 | 🔥 |
| 23 | remotion-dev/remotion | 80 A | 13 | 01-video-uretim-montaj (13) | 10/3/0 | NOASSERTION | ✓ | 74755 | 969.9 | 512 | 6864 | 2026-11-18 | 🔥 |
| 24 | upstash/context7 | 80 A | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 65240 | 3272.8 | 148 | 329 | 2026-11-17 |  |
| 25 | GoogleChrome/lighthouse | 77 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31180 | 242.4 | 401 | 235 | 2026-10-27 |  |
| 26 | K-Dense-AI/scientific-agent-skills | 77 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 58028 | 4421.2 | 58 | 69 | 2026-10-01 | 🔥 |
| 27 | anthropics/claude-plugins-official | 77 B | 47 | 04-skill-plugin-yazimi (31), 02-agent-orkestrasyon (5) | 47/0/0 | Apache-2.0 | ✓ | 47910 | 3968.6 | 49 | 1454 | - | 🔥 |
| 28 | github/awesome-copilot | 77 B | 0 | - | 0/0/0 | MIT |  | 41428 | 2380.7 | 600 | 1126 | - |  |
| 29 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48870 | 294.0 | 653 | 114 | 2026-11-11 |  |
| 30 | ayghri/i-have-adhd | 75 B | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 61888 | 9748.2 | 53 | 79 | 2026-10-19 |  |
| 31 | blader/humanizer | 75 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 71966 | 7103.1 | 31 | 71 | 2026-11-10 | 🔥 |
| 32 | obsidianmd/obsidian-skills | 75 B | 7 | 04-not-alma-bilgi-yonetimi (6), 02-diyagram-dokumantasyon (1) | 7/0/0 | MIT |  | 53381 | 5008.6 | 28 | 47 | 2026-11-20 |  |
| 33 | anthropics/knowledge-work-plugins | 74 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 36650 | 3677.1 | 32 | 418 | - | 🔥 |
| 34 | anthropics/skills | 74 B | 17 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 16/1/0 | yok | ✓ | 198456 | 14162.1 | 17 | 12 | - | 🔥 |
| 35 | cathrynlavery/diagram-design | 74 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 69771 | 9641.1 | 75 | 344 | - |  |
| 36 | AgriciDaniel/claude-seo | 73 B | 28 | 01-satis-pazarlama-musteri (28) | 28/0/0 | MIT |  | 31389 | 3313.3 | 53 | 472 | 2026-11-15 | 🔥 |
| 37 | google/elephant-goldfish-model | 73 B | 8 | 01-planlama-metodoloji (8) | 8/0/0 | Apache-2.0 |  | 21913 | 9516.5 | 39 | 213 | 2026-11-06 | 🔥 |
| 38 | earthtojake/text-to-cad | 72 B | 17 | 05-cad-imalat-robotik (17) | 17/0/0 | MIT |  | 27069 | 3845.3 | 34 | 519 | 2026-11-21 | 🔥 |
| 39 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 35427 | 367.8 | 147 | 1339 | - |  |
| 40 | latent-spaces/brag | 69 B | 2 | 01-video-uretim-montaj (2) | 2/0/0 | MIT |  | 22155 | 4235.9 | 20 | 58 | 2026-11-15 |  |
| 41 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20324 | 1936.8 | 44 | 401 | 2026-10-29 |  |
| 42 | cloudflare/security-audit-skill | 68 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 76674 | 14846.4 | 4 | 3 | - | 🔥 |
| 43 | JuneYaooo/rea-video | 67 B | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 11785 | 11785.0 | 21 | 180 | 2026-11-11 |  |
| 44 | Nutlope/hallmark | 67 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 59042 | 8587.9 | 12 | 147 | - | 🔥 |
| 45 | vercel-labs/agent-skills | 67 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 34668 | 3019.8 | 29 | 20 | 2026-11-20 | 🔥 |
| 46 | wanshuiyin/Auto-claude-code-research-in-sleep | 67 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 19553 | 2312.9 | 108 | 187 | 2026-09-28 |  |
| 47 | Vincentwei1021/video-shotcraft | 66 B | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 21966 | 5299.7 | 17 | 58 | 2026-09-01 | 🔥 |
| 48 | multica-ai/andrej-karpathy-skills | 66 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 234915 | 23884.3 | 7 | 0 | - | 🔥 |
| 49 | google/skills | 65 B | 217 | 06-devops-guvenlik-performans (118), 04-mimari-api-veritabani (53) | 41/176/0 | Apache-2.0 |  | 24518 | 3158.3 | 9 | 369 | - | 🔥 |
| 50 | krillinai/OpenCreator | 65 B | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14457 | 623.4 | 37 | 501 | 2026-11-18 |  |
| 51 | ComposioHQ/awesome-claude-skills | 64 C | 4 | 03-yazi-iletisim-icerik (2), 04-not-alma-bilgi-yonetimi (1) | 3/1/0 | yok | ✓ | 80007 | 6065.4 | 29 | 0 | - |  |
| 52 | kajisho5/ffmpeg-skill | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 9254 | 3516.5 | 12 | 684 | 2026-11-21 | 🔥 |
| 53 | lemomo-ai/lemo-opuscar | 63 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 19502 | 10401.1 | 10 | 147 | 2026-11-12 |  |
| 54 | AgriciDaniel/claude-obsidian | 62 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16674 | 2213.5 | 11 | 108 | 2026-10-21 |  |
| 55 | android/skills | 62 C | 38 | 08-mobil-uygulama (38) | 37/1/0 | Apache-2.0 | ✓ | 10690 | 1294.7 | 8 | 37 | 2026-11-15 | 🔥 |
| 56 | Donchitos/Claude-Code-Game-Studios | 61 C | 72 | 06-oyun-2d-grafik (72) | 72/0/0 | MIT |  | 40507 | 4351.3 | 1 | 6 | 2026-11-09 | 🔥 |
| 57 | dreammis/social-auto-upload | 61 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16759 | 470.0 | 42 | 18 | 2026-10-22 |  |
| 58 | jacob-bd/gemini-notebook-mcp-cli | 61 C | 0 | - | 0/0/0 | MIT |  | 6552 | 596.3 | 72 | 239 | 2026-11-14 |  |
| 59 | browser-use/video-use | 60 C | 2 | 01-video-uretim-montaj (1), 04-motion-graphics-karakter (1) | 1/1/0 | MIT |  | 31399 | 4261.3 | 8 | 5 | - |  |
| 60 | Leonxlnx/earshot | 59 C | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 5473 | 4378.4 | 8 | 189 | 2026-11-20 |  |
| 61 | zarazhangrui/frontend-slides | 59 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 32731 | 3339.0 | 9 | 0 | 2026-05-26 |  |
| 62 | digitalsamba/claude-code-video-toolkit | 57 C | 14 | 01-video-uretim-montaj (7), 03-ai-gorsel-video-modelleri (4) | 4/8/2 | MIT |  | 2697 | 235.6 | 17 | 503 | 2026-11-14 |  |
| 63 | zubair-trabzada/geo-seo-claude | 57 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11806 | 1295.7 | 25 | 59 | - |  |
| 64 | Orchestra-Research/AI-Research-SKILLs | 56 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14723 | 1165.6 | 17 | 0 | 2026-06-16 |  |
| 65 | cloudflare/skills | 56 C | 22 | 06-devops-guvenlik-performans (22) | 12/7/3 | Apache-2.0 | ✓ | 3422 | 299.8 | 50 | 272 | - | 🔥 |
| 66 | AgriciDaniel/claude-ads | 55 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 11216 | 1200.6 | 2 | 43 | 2026-10-16 |  |
| 67 | WyattBlue/auto-editor | 55 C | 5 | 01-video-uretim-montaj (5) | 5/0/0 | Unlicense |  | 6043 | 76.6 | 17 | 308 | 2026-11-13 |  |
| 68 | vudovn/ag-kit | 54 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8227 | 801.6 | 10 | 8 | 2026-08-31 |  |
| 69 | czlonkowski/n8n-skills | 53 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6690 | 511.0 | 7 | 33 | 2026-10-24 | 🔥 |
| 70 | expo/skills | 53 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4205 | 358.1 | 31 | 43 | - | 🔥 |
| 71 | openai/plugins | 53 C | 0 | - | 0/0/0 | yok | ✓ | 8051 | 930.6 | 63 | 13 | - |  |
| 72 | greensock/gsap-skills | 52 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 18874 | 2181.6 | 4 | 0 | - |  |
| 73 | darkroomengineering/satus | 51 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1023 | 16.6 | 19 | 180 | 2026-08-28 |  |
| 74 | Ryze-AI-Adgent/open-seo-mcp-skills | 50 C | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 10633 | 3802.9 | 1 | 16 | - |  |
| 75 | Jakeschincariol/day-trader-skill | 48 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 9048 | 8335.1 | 1 | 1 | - |  |
| 76 | Jakeschincariol/replica-skill | 48 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 10248 | 6230.8 | 1 | 1 | - |  |
| 77 | veedstudio/open-edit | 47 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 1845 | 456.0 | 3 | 15 | 2026-08-03 |  |
| 78 | feitangyuan/onetake | 46 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 4302 | 2294.4 | 3 | 22 | 2026-10-08 |  |
| 79 | Jakeschincariol/youtube-agent-skill | 45 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 6777 | 3074.9 | 1 | 1 | - |  |
| 80 | hardikpandya/stop-slop | 45 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 19111 | 1844.4 | 2 | 0 | - |  |
| 81 | Jakeschincariol/instagram-agent-skill | 44 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 7955 | 3454.7 | 1 | 2 | - |  |
| 82 | sarpstar/cinecode | 44 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 2838 | 2838.0 | 3 | 9 | - |  |
| 83 | nateherkai/scroll-craft | 43 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 5322 | 1758.6 | 1 | 8 | - |  |
| 84 | CloudAI-X/threejs-skills | 42 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 4335 | 429.3 | 1 | 20 | - |  |
| 85 | shadcn-labs/snapcn | 42 D | 7 | 04-motion-graphics-karakter (7) | 0/7/0 | MIT |  | 670 | 168.3 | 3 | 281 | - |  |
| 86 | lottiefiles/motion-design-skill | 41 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 3518 | 419.4 | 2 | 5 | - |  |
| 87 | Jakeschincariol/founder-skill | 40 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 4538 | 2999.0 | 1 | 1 | - |  |
| 88 | yaojingang/yao-meta-skill | 40 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2740 | 352.9 | 4 | 10 | - |  |
| 89 | ythx-101/live-panel-skill | 40 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 875 | 532.0 | 4 | 41 | - |  |
| 90 | AbubakrChan/product-launch-motion | 39 D | 1 | 04-motion-graphics-karakter (1) | 1/0/0 | MIT |  | 518 | 133.5 | 2 | 44 | 2026-10-12 |  |
| 91 | Jakeschincariol/linkedin-agent-skill | 39 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3810 | 1524.0 | 1 | 1 | - |  |
| 92 | nexscope-ai/eCommerce-Skills | 39 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1483 | 181.1 | 7 | 3 | - |  |
| 93 | nexscope-ai/Amazon-Skills | 37 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 882 | 104.3 | 5 | 3 | - |  |
| 94 | heygen-com/hyperframes-community-skills | 36 D | 7 | 01-video-uretim-montaj (7) | 6/1/0 | Apache-2.0 | ✓ | 286 | 97.7 | 3 | 11 | - |  |
| 95 | 40RTY-ai/shopify-admin-skills | 35 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 205 | 27.7 | 3 | 4 | 2026-06-17 |  |
| 96 | Barty-Bart/motion-graphics | 35 D | 5 | 04-motion-graphics-karakter (5) | 5/0/0 | NOASSERTION |  | 1428 | 748.5 | 4 | 10 | - |  |
| 97 | heyitsnoah/claudesidian | 35 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2615 | 182.3 | 3 | 0 | 2026-04-11 |  |
| 98 | nateherkai/herk-edit-kit | 35 D | 10 | 01-video-uretim-montaj (10) | 5/5/0 | NOASSERTION |  | 3046 | 424.8 | 1 | 13 | - |  |
| 99 | rshankras/claude-code-apple-skills | 35 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 905 | 70.7 | 4 | 11 | - |  |
| 100 | zanwei/design-dna | 35 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2143 | 267.0 | 3 | 3 | - |  |
| 101 | echris6/motion-video-kit | 35 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 1438 | 780.6 | 1 | 7 | - |  |
| 102 | evanca/flutter-ai-rules | 33 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 674 | 35.4 | 2 | 15 | - |  |
| 103 | OrcaQubits/agentic-commerce-skills-plugins | 32 D | 2 | 05-e-ticaret-pazaryeri (2) | 2/0/0 | MIT |  | 40 | 4.6 | 3 | 16 | 2026-11-13 |  |
| 104 | RevenueCat/play-billing-skills | 31 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 10.5 | 1 | 28 | 2026-10-15 |  |
| 105 | hamen/compose_skill | 31 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 380 | 51.8 | 3 | 0 | 2026-07-07 |  |
| 106 | kylezantos/design-motion-principles | 31 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1626 | 158.4 | 1 | 0 | 2026-05-21 |  |
| 107 | lemomo-ai/lemo-wake | 31 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 375 | 228.0 | 1 | 15 | 2026-10-05 |  |
| 108 | xjli360/sealeap-amazon-skills | 31 D | 0 | - | 0/0/0 | MIT |  | 444 | 145.1 | 1 | 9 | - |  |
| 109 | freshtechbro/claudedesignskills | 30 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1426 | 110.3 | 1 | 0 | - |  |
| 110 | mercadopago/mercadopago-claude-marketplace | 29 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 33 | 3.7 | 10 | 7 | - |  |
| 111 | tuist/fuckingapproachableswiftconcurrency | 29 D | 0 | - | 0/0/0 | MIT |  | 159 | 14.4 | 15 | 0 | - |  |
| 112 | tuzhechen2005/opus-video-skills | 29 D | 2 | 04-motion-graphics-karakter (2) | 2/0/0 | NOASSERTION |  | 553 | 294.9 | 3 | 9 | - |  |
| 113 | moiz-za/etsy-seller-seo-system | 28 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 54 | 8.7 | 2 | 13 | 2026-10-23 |  |
| 114 | wj-sidiss/etsy-otomasyon-full-full-surum | 28 D | 0 | - | 0/0/0 | MIT |  | 57 | 57.0 | 1 | 8 | 2026-11-01 |  |
| 115 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 172 | 88.6 | 1 | 11 | - |  |
| 116 | twostraws/SwiftData-Agent-Skill | 27 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 472 | 56.1 | 2 | 1 | 2026-03-11 |  |
| 117 | xianyu110/ecommerce-image-skills | 27 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 190 | 117.9 | 1 | 7 | - |  |
| 118 | Livsy90/iOS-Performance-Agent-Skills | 26 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 121 | 20.3 | 2 | 0 | 2026-07-12 |  |
| 119 | ehmo/platform-design-skills | 26 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 648 | 67.0 | 1 | 0 | - |  |
| 120 | finsilabs/awesome-ecommerce-skills | 26 D | 179 | 05-e-ticaret-pazaryeri (179) | 161/18/0 | MIT |  | 67 | 8.0 | 4 | 3 | - |  |
| 121 | sirioberati/YouTube-AI-Video-Editing-System | 26 D | 0 | - | 0/0/0 | MIT |  | 167 | 158.7 | 1 | 4 | - |  |
| 122 | dpconde/claude-android-skill | 24 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 362 | 31.4 | 1 | 0 | - |  |
| 123 | ParthJadhav/ios-marketing-capture | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 266 | 35.8 | 1 | 1 | - |  |
| 124 | Lonsdale201/wp-agent-skills | 22 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 3.8 | 3 | 20 | - |  |
| 125 | MADTeacher/mad-agents-skills | 21 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 114 | 11.0 | 2 | 0 | - |  |
| 126 | YildizDikme/claude-video-edit | 21 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 57 | 57.0 | 1 | 3 | - |  |
| 127 | dadederk/iOS-Accessibility-Agent-Skill | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 177 | 17.9 | 1 | 0 | - |  |
| 128 | leodavincs/kalem | 21 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 119 | 119.0 | 1 | 7 | - |  |
| 129 | Harishwarrior/flutter-claude-skills | 20 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 69 | 5.3 | 2 | 3 | - |  |
| 130 | Shopify/agent-skills | 20 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 112 | 14.5 | 1 | 0 | - |  |
| 131 | Kappaemme-git/codex-phone-lab | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 96 | 15.7 | 1 | 0 | - |  |
| 132 | oldred-byte/ec-visual-skill | 19 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 117 | 17.7 | 1 | 0 | - |  |
| 133 | Viniciuscarvalho/swift-code-reviewer-skill | 18 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.2 | 5 | 0 | 2026-05-07 |  |
| 134 | avenoxai/avenox-video-kurgu-notlari | 17 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 30 | 30.0 | 1 | 1 | - |  |
| 135 | yohannescodes/apple-app-review-compliance | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 23 | 19.4 | 1 | 4 | - |  |
| 136 | Trendyol/trendyol-integration-developer-tool | 16 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 13 | 2.0 | 3 | 0 | - |  |
| 137 | jazzychad/ios-code-audit | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 6.7 | 1 | 0 | - |  |
| 138 | arjitj2/swiftui-design-principles | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 34 | 3.8 | 1 | 0 | - |  |
| 139 | lemomo-ai/codex-radar | 14 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 40 | 7.2 | 1 | 8 | - |  |
| 140 | mmiani/kotlin-kmp-claude-agent-skills | 13 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 93 | 11.8 | 1 | 0 | - |  |
| 141 | avenoxai/higgsfield-studio | 10 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 17 | 5.4 | 1 | 2 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 88 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 81 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `find-docs` 95/A, `tailwind-design-system` 93/A, `remotion-create` 90/A, `web-artifacts-builder` 90/B, `context7-mcp` 88/A | tasarim-teknolojileri.md |
| 3 | d3/d3 | 77 B | v7.9 | `d3-viz` 93/A, `d3-visualization` 97/A | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 75 B | - | `ffmpeg` 93/A, `video-understand` 94/A, `ffmpeg-skill` 94/C, `character-animation-qa` 86/A, `product-launch-motion` 72/D, `kinetic-reel` 72/D, `cut-mistakes` 65/D, `cut-silences` 65/D | kutuphaneler.md |
| 5 | ManimCommunity/manim | 73 B | v0.22 | `manim-composer` 94/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 93/A, `remotion-to-hyperframes` 97/A, `manim-video` 84/C | tasarim-teknolojileri.md |
| 6 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/A | tasarim-teknolojileri.md |
| 7 | pmndrs/react-three-fiber | 72 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 57/D, `blender-web-pipeline` 57/D, `web3d-integration-patterns` 57/D, `substance-3d-texturing` 49/D, `modern-web-design` 47/D | tasarim-teknolojileri.md |
| 8 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 94/A, `azure-speech-to-text` 94/A, `krillinai-subtitle` 90/B, `whisper` 87/C, `auto-editor-transcribe` 84/C, `ajanla-video-kurgu` 69/D | kutuphaneler.md |
| 9 | blender/blender | 68 B | - | `blender-web-pipeline` 57/D, `3d-asset-generation` 94/A, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A, `render` 96/B, `blender` 80/C | kutuphaneler.md |
| 10 | KaTeX/KaTeX | 67 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 94/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 88/B | kutuphaneler.md |
| 11 | 666ghj/MiroFish | 66 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 12 | QwikDev/partytown | 65 B | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 64 C | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 68/D | tasarim-teknolojileri.md |
| 14 | dequelabs/axe-core | 64 C | v4.14 (MPL-2.0) | `accessibility-engineering` 100/A, `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 84/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 15 | librosa/librosa | 64 C | - | `media-use` 100/A | kutuphaneler.md |
| 16 | DavidHDev/react-bits | 63 C | - | `animated-component-libraries` 57/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 17 | darkroomengineering/lenis | 63 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 57/D | tasarim-teknolojileri.md |
| 18 | paperjs/paper.js | 62 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 19 | Fei-Away/Codex-Dream-Skin | 61 C | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 20 | airbnb/lottie-web | 60 C | v5.13 | `lottie-animations` 57/D, `remotion-to-hyperframes` 97/A, `motion-design` 80/D, `lottie-bodymovin` 78/A, `flutter-pre-caching` 78/D, `rive-interactive` 57/D | tasarim-teknolojileri.md |
| 21 | pmndrs/drei | 60 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 22 | fontsource/fontsource | 58 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 23 | ai/size-limit | 56 C | 14.2 (T5) | `react-doctor` 75/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 24 | motion-canvas/motion-canvas | 56 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 94/A | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 53 C | 0.20 | `pixijs-2d` 65/D, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 52 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 27 | rough-stuff/rough | 49 D | v3.1 | `camera-3d-captions` 79/D, `day-in-my-life` 73/D | tasarim-teknolojileri.md |
| 28 | greensock/GSAP | 48 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 47 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | barvian/number-flow | 45 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 31 | opentypejs/opentype.js | 45 D | 2.0 | `svg-character-animation` 94/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 32 | figma/code-connect | 44 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 44 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | argyleink/open-props | 43 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 35 | JohnHeibel/ClaudeAnimationBase | 42 D | - | `canvas-procedural-animation` 85/A, `algorithmic-art` 81/B, `svg-character-animation` 94/A | tasarim-teknolojileri.md |
| 36 | pmndrs/cannon-es | 41 D | v0.20 | `threejs-world-generation` 93/A, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 37 | zhuyansen/awesome-claude-video-skills | 40 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 38 | metafizzy/zdog | 39 D | v1.1 | `svg-character-animation` 94/A, `canvas-procedural-animation` 85/A, `lightweight-3d-effects` 56/D | tasarim-teknolojileri.md |
| 39 | meyda/meyda | 38 D | - | `canvas-procedural-animation` 85/A | kutuphaneler.md |
| 40 | oframe/ogl | 37 D | - | `lightweight-3d-effects` 56/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 41 | 14islands/r3f-scroll-rig | 34 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 57/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 57/D, `barba-js` 57/D, `locomotive-scroll` 57/D, `scroll-reveal-libraries` 57/D | tasarim-teknolojileri.md |
| 42 | jwagner/simplex-noise.js | 33 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 79/D, `threejs-world-generation` 93/A | tasarim-teknolojileri.md |
| 43 | linvi/tweetinvi | 33 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 44 | nevertoday/350-layout-compositions | 32 D | - | `design-taste-frontend` 100/A, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 45 | pmndrs/react-three-a11y | 28 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 46 | arturitu/the-delegation | 23 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
