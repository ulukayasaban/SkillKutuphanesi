# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-16, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 90A (13) · nextlevelbuilder/ui-ux-pro-max-skill 87A (2) · anthropics/claude-code 85A (1) | `impeccable` 100/A, `design-taste-frontend` 100/B, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 90A (3) · nextlevelbuilder/ui-ux-pro-max-skill 87A (4) · OpenMontageInc/OpenMontage 81A (1) | `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A, `tailwind-design-system` 93/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 90A (7) · OpenMontageInc/OpenMontage 81A (2) · github/awesome-copilot 76B (1) | `gsap-framer-scroll-animation` 99/B, `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 52C (1) · nateherkai/scroll-craft 43D (1) · freshtechbro/claudedesignskills 30D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 61/D, `locomotive-scroll` 61/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | openai/plugins 51C (2) · CloudAI-X/threejs-skills 41D (13) · freshtechbro/claudedesignskills 30D (10) | `threejs-asset-pipeline` 88/D, `threejs-fundamentals` 88/D, `threejs-lighting` 88/D, `threejs-loaders` 88/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 90A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 60C (68) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 90A (14) · nextlevelbuilder/ui-ux-pro-max-skill 87A (1) · OpenMontageInc/OpenMontage 81A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 90A (3) · microsoft/playwright 85A (2) · addyosmani/agent-skills 85A (1) | `playwright-trace` 100/A, `browser-testing-with-devtools` 98/A, `playwright-component-testing` 98/A, `export-download-debugging` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 85A (8) · mattpocock/skills 83A (30) · ruvnet/ruflo 83A (6) | `agent-implementer-sparc-coder` 100/A, `agent-sparc-coordinator` 100/A, `ask-matt` 100/A, `codebase-design` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 87A (6) · addyosmani/agent-skills 85A (2) · tt-a1i/archify 84A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 85A (2) · tt-a1i/archify 84A (1) · ruvnet/ruflo 83A (5) | `test-driven-development` 100/A, `agent-tdd-london-swarm` 100/A, `agent-test-long-runner` 100/A, `test-gaps` 100/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 85A (2) · ruvnet/ruflo 83A (5) · github/awesome-copilot 76B (2) | `api-and-interface-design` 100/A, `ddd-aggregate` 100/A, `ddd-context` 100/A, `ddd-validate` 100/A |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 90A (2) · addyosmani/agent-skills 85A (2) · ruvnet/ruflo 83A (13) | `git-workflow-and-versioning` 100/A, `agent-github-pr-manager` 100/A, `diff-analyze` 100/A, `git-workflow` 100/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 85A (5) · ruvnet/ruflo 83A (22) | `security-and-hardening` 100/A, `agent-performance-analyzer` 100/A, `agent-v3-security-architect` 100/A, `dependency-check` 100/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 85A (1) · anthropics/claude-plugins-official 77B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | google/skills 64C (11) · android/skills 60C (37) · expo/skills 53C (24) | `google-mobile-ads-banner` 99/C, `google-mobile-ads-get-started` 99/C, `google-mobile-ads-interstitial` 99/C, `google-mobile-ads-rewarded` 99/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 90A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 73B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 90A (2) · addyosmani/agent-skills 85A (1) · tt-a1i/archify 84A (1) | `documentation-and-adrs` 100/A, `adr-create` 100/A, `adr-index` 100/A, `adr-reindex` 100/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 90A (1) · anthropics/skills 74B (1) · blader/humanizer 73B (1) | `humanizer` 98/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | obsidianmd/obsidian-skills 74B (5) · ComposioHQ/awesome-claude-skills 64C (2) · AgriciDaniel/claude-obsidian 62C (11) | `defuddle` 92/B, `knap` 92/B, `obsidian-cli` 92/B, `obsidian-bases@kepano` 90/B |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | ruvnet/ruflo 83A (5) · anthropics/claude-plugins-official 77B (4) · anthropics/skills 74B (3) | `chat-format` 100/A, `ruvllm-runtime` 100/A, `build-mcp-app` 100/B, `build-mcp-server` 100/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 90A (2) · JuliusBrussee/caveman 86A (22) · addyosmani/agent-skills 85A (2) | `context-engineering` 100/A, `add-model-descriptions` 100/A, `agent-agentic-payments` 100/A, `agent-app-store` 100/A |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 92A (1) · ruvnet/ruflo 83A (16) · Panniantong/Agent-Reach 80A (1) | `browser` 100/A, `browser-auth-flow` 100/A, `browser-extract` 100/A, `browser-form-fill` 100/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 90A (2) · heygen-com/hyperframes 89A (2) · ruvnet/ruflo 83A (4) | `create-plugin` 100/A, `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 97/A |
| `e-entegrasyon-katalogu/01-uygulama-entegrasyonlari` — Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Co | github/awesome-copilot 76B (460) · openai/plugins 51C (449) | `acreadiness-assess` 99/B, `acreadiness-policy` 99/B, `add-educational-comments` 99/B, `agentic-eval` 99/B |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 84A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 90A (17) · heygen-com/hyperframes 89A (10) · harry0703/MoneyPrinterTurbo 85A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | ruvnet/ruflo 83A (7) · OpenMontageInc/OpenMontage 81A (12) · krillinai/OpenCreator 64C (7) | `music-get` 100/A, `lyria` 100/A, `music` 100/A, `sound-effects` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 81A (16) · digitalsamba/claude-code-video-toolkit 56C (4) · yerel/kendi 17D (1) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 90A (2) · heygen-com/hyperframes 89A (3) · OpenMontageInc/OpenMontage 81A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 80A (48) · anthropics/knowledge-work-plugins 73B (58) · AgriciDaniel/claude-seo 69B (25) | `ab-testing` 100/A, `analytics` 100/A, `aso` 100/A, `attribution` 100/A |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | ruvnet/ruflo 83A (10) · anthropics/knowledge-work-plugins 73B (26) · Jakeschincariol/day-trader-skill 45D (11) | `market-ingest` 100/A, `market-pattern` 100/A, `trader-backtest` 100/A, `trader-cloud-backtest` 100/A |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 73B (69) · Jakeschincariol/founder-skill 37D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 73B (10) · google/skills 64C (2) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 90A (1) · nexscope-ai/eCommerce-Skills 38D (156) · 40RTY-ai/shopify-admin-skills 38D (117) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 81/D, `brand-monitoring` 81/D, `brand-protection-amazon` 81/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 77B (90) · anthropics/knowledge-work-plugins 73B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 77B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 77B (27) · Orchestra-Research/AI-Research-SKILLs 54C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 77B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 67B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 77B (2) · earthtojake/text-to-cad 71B (12) | `fictiv` 97/B, `lab-hardware-cad` 97/B, `bambu-labs` 97/B, `dfam-check` 97/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 430844 | 60637.3 | 362 | 5773 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 92 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 142439 | 19075.5 | 391 | 1481 | 2026-11-03 | 🔥 |
| 3 | nexu-io/open-design | 90 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 105947 | 15944.5 | 451 | 717 | 2026-11-04 |  |
| 4 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143324 | 1179.5 | 4184 | 1549 | 2026-11-04 | 🔥 |
| 5 | heygen-com/hyperframes | 89 A | 15 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/2 | Apache-2.0 | ✓ | 82940 | 10045.3 | 137 | 3163 | 2026-11-12 | 🔥 |
| 6 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 251960 | 1555.6 | 2027 | 134 | 2026-10-14 |  |
| 7 | DietrichGebert/ponytail | 87 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 184540 | 35732.6 | 133 | 163 | 2026-10-29 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 87 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 145229 | 12578.2 | 110 | 81 | 2026-08-13 |  |
| 9 | JuliusBrussee/caveman | 86 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 117512 | 15806.9 | 104 | 1619 | 2026-10-23 |  |
| 10 | addyosmani/agent-skills | 85 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 113281 | 12568.4 | 97 | 392 | 2026-10-31 | 🔥 |
| 11 | anthropics/claude-code | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154554 | 7434.2 | 59 | 247 | 2026-11-04 | 🔥 |
| 12 | harry0703/MoneyPrinterTurbo | 85 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 141094 | 4376.8 | 169 | 554 | 2026-11-07 | 🔥 |
| 13 | microsoft/playwright | 85 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 99306 | 1180.2 | 828 | 733 | 2026-10-14 | 🔥 |
| 14 | tt-a1i/archify | 84 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 93462 | 13215.1 | 92 | 1628 | 2026-10-19 |  |
| 15 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 313295 | 33301.3 | 8 | 133 | 2026-10-29 | 🔥 |
| 16 | pbakaus/impeccable | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 102802 | 8562.1 | 62 | 1203 | 2026-10-26 | 🔥 |
| 17 | ruvnet/ruflo | 83 A | 305 | 02-agent-orkestrasyon (199), 06-devops-guvenlik-performans (22) | 292/8/5 | MIT |  | 81282 | 4644.7 | 95 | 2949 | 2026-11-09 | 🔥 |
| 18 | OpenMontageInc/OpenMontage | 81 A | 54 | 03-ai-gorsel-video-modelleri (16), 02-ses-muzik-konusma (12) | 22/11/21 | AGPL-3.0 |  | 79720 | 10446.1 | 129 | 305 | - | 🔥 |
| 19 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 312440 | 23568.7 | 44 | 7 | 2026-11-03 | 🔥 |
| 20 | Panniantong/Agent-Reach | 80 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 108808 | 12482.1 | 46 | 104 | 2026-11-01 | 🔥 |
| 21 | coreyhaines31/marketingskills | 80 A | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 58521 | 5832.9 | 57 | 961 | 2026-10-30 | 🔥 |
| 22 | Leonxlnx/taste-skill | 79 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 110057 | 12391.6 | 24 | 152 | 2026-11-04 | 🔥 |
| 23 | upstash/context7 | 79 B | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 64385 | 3262.2 | 147 | 253 | 2026-11-06 |  |
| 24 | remotion-dev/remotion | 78 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 70754 | 920.4 | 490 | 5575 | 2026-11-02 | 🔥 |
| 25 | K-Dense-AI/scientific-agent-skills | 77 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 56104 | 4339.9 | 58 | 94 | 2026-10-01 | 🔥 |
| 26 | anthropics/claude-plugins-official | 77 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 46120 | 3883.8 | 42 | 1732 | - | 🔥 |
| 27 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48622 | 292.9 | 639 | 94 | 2026-10-01 |  |
| 28 | GoogleChrome/lighthouse | 76 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31017 | 241.5 | 397 | 192 | 2026-10-27 |  |
| 29 | github/awesome-copilot | 76 B | 469 | 01-uygulama-entegrasyonlari (460), 02-kod-kalitesi-review (2) | 458/10/1 | MIT |  | 40799 | 2371.5 | 578 | 885 | - | 🔥 |
| 30 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 187417 | 13565.4 | 17 | 15 | - | 🔥 |
| 31 | cathrynlavery/diagram-design | 74 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 65003 | 9234.1 | 66 | 397 | - |  |
| 32 | obsidianmd/obsidian-skills | 74 B | 6 | 04-not-alma-bilgi-yonetimi (5), 02-diyagram-dokumantasyon (1) | 6/0/0 | MIT |  | 52786 | 5046.2 | 28 | 43 | 2026-11-11 |  |
| 33 | anthropics/knowledge-work-plugins | 73 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34734 | 3555.3 | 32 | 563 | - | 🔥 |
| 34 | blader/humanizer | 73 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 64838 | 6526.7 | 24 | 60 | 2026-09-28 | 🔥 |
| 35 | earthtojake/text-to-cad | 71 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 25423 | 3715.7 | 32 | 876 | 2026-11-03 | 🔥 |
| 36 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 34907 | 363.2 | 147 | 1009 | - |  |
| 37 | AgriciDaniel/claude-seo | 69 B | 25 | 01-satis-pazarlama-musteri (25) | 25/0/0 | MIT |  | 26654 | 2873.3 | 30 | 209 | 2026-10-22 | 🔥 |
| 38 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20096 | 1951.8 | 42 | 650 | 2026-10-29 |  |
| 39 | google/elephant-goldfish-model | 67 B | 7 | 01-planlama-metodoloji (7) | 7/0/0 | Apache-2.0 |  | 11801 | 5605.5 | 29 | 149 | 2026-10-27 | 🔥 |
| 40 | multica-ai/andrej-karpathy-skills | 67 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 229500 | 23811.6 | 7 | 0 | - | 🔥 |
| 41 | wanshuiyin/Auto-claude-code-research-in-sleep | 67 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 18651 | 2258.9 | 106 | 205 | 2026-09-28 |  |
| 42 | cloudflare/security-audit-skill | 66 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 59355 | 11949.6 | 4 | 3 | - | 🔥 |
| 43 | vercel-labs/agent-skills | 66 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33547 | 2973.3 | 28 | 23 | 2026-10-27 | 🔥 |
| 44 | Nutlope/hallmark | 65 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 47913 | 7175.1 | 10 | 138 | - | 🔥 |
| 45 | ComposioHQ/awesome-claude-skills | 64 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78745 | 6060.4 | 29 | 0 | - |  |
| 46 | krillinai/OpenCreator | 64 C | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14157 | 615.7 | 36 | 458 | 2026-11-03 |  |
| 47 | google/skills | 64 C | 196 | 06-devops-guvenlik-performans (105), 04-mimari-api-veritabani (48) | 20/176/0 | Apache-2.0 |  | 24352 | 3218.7 | 9 | 351 | - | 🔥 |
| 48 | Vincentwei1021/video-shotcraft | 63 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 16988 | 4303.6 | 14 | 44 | 2026-09-01 | 🔥 |
| 49 | AgriciDaniel/claude-obsidian | 62 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16171 | 2204.5 | 11 | 108 | 2026-10-21 |  |
| 50 | Fei-Away/Codex-Dream-Skin | 62 C | 0 | - | 0/0/0 | MIT |  | 15329 | 3758.1 | 23 | 44 | 2026-10-15 |  |
| 51 | dreammis/social-auto-upload | 62 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16118 | 454.5 | 42 | 46 | 2026-10-22 |  |
| 52 | lemomo-ai/lemo-opuscar | 61 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 12273 | 7315.7 | 4 | 80 | 2026-10-12 |  |
| 53 | Donchitos/Claude-Code-Game-Studios | 60 C | 68 | 06-oyun-2d-grafik (68) | 68/0/0 | MIT |  | 35403 | 3885.4 | 1 | 5 | 2026-10-19 | 🔥 |
| 54 | android/skills | 60 C | 37 | 08-mobil-uygulama (37) | 36/1/0 | Apache-2.0 | ✓ | 10337 | 1282.6 | 8 | 36 | 2026-11-04 | 🔥 |
| 55 | browser-use/video-use | 60 C | 2 | 01-video-uretim-montaj (1), 04-motion-graphics-karakter (1) | 1/1/0 | MIT |  | 31088 | 4335.2 | 8 | 5 | - |  |
| 56 | zarazhangrui/frontend-slides | 58 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 31888 | 3319.8 | 9 | 0 | 2026-05-26 |  |
| 57 | cloudflare/skills | 56 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3279 | 292.3 | 48 | 261 | - | 🔥 |
| 58 | digitalsamba/claude-code-video-toolkit | 56 C | 14 | 01-video-uretim-montaj (7), 03-ai-gorsel-video-modelleri (4) | 4/8/2 | MIT |  | 2579 | 229.2 | 17 | 422 | 2026-11-14 |  |
| 59 | zubair-trabzada/geo-seo-claude | 55 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11511 | 1291.3 | 25 | 77 | - |  |
| 60 | AgriciDaniel/claude-ads | 54 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 10746 | 1175.1 | 2 | 43 | 2026-10-16 |  |
| 61 | Orchestra-Research/AI-Research-SKILLs | 54 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14269 | 1147.6 | 17 | 0 | 2026-06-16 |  |
| 62 | WyattBlue/auto-editor | 54 C | 5 | 01-video-uretim-montaj (5) | 5/0/0 | Unlicense |  | 5918 | 75.2 | 17 | 228 | 2026-11-13 |  |
| 63 | vudovn/ag-kit | 54 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8207 | 815.3 | 10 | 8 | 2026-08-31 |  |
| 64 | expo/skills | 53 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4050 | 350.8 | 31 | 45 | - | 🔥 |
| 65 | czlonkowski/n8n-skills | 52 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6589 | 511.0 | 7 | 33 | 2026-10-24 | 🔥 |
| 66 | greensock/gsap-skills | 52 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17884 | 2115.5 | 4 | 0 | - |  |
| 67 | openai/plugins | 51 C | 463 | 01-uygulama-entegrasyonlari (449), 06-devops-guvenlik-performans (5) | 436/27/0 | yok | ✓ | 7752 | 917.0 | 62 | 10 | - |  |
| 68 | darkroomengineering/satus | 50 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.5 | 19 | 152 | 2026-08-28 |  |
| 69 | Leonxlnx/earshot | 49 D | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 3898 | 3703.1 | 1 | 40 | 2026-10-22 |  |
| 70 | Ryze-AI-Adgent/open-seo-mcp-skills | 49 D | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 8815 | 3392.1 | 1 | 16 | - |  |
| 71 | Jakeschincariol/replica-skill | 46 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 7640 | 5278.5 | 1 | 1 | - |  |
| 72 | Jakeschincariol/day-trader-skill | 45 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 5296 | 5296.0 | 1 | 1 | - |  |
| 73 | hardikpandya/stop-slop | 45 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 18619 | 1831.8 | 2 | 0 | - |  |
| 74 | feitangyuan/onetake | 44 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 3959 | 2359.9 | 2 | 21 | 2026-10-08 |  |
| 75 | Jakeschincariol/youtube-agent-skill | 43 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 4562 | 2273.5 | 1 | 1 | - |  |
| 76 | nateherkai/scroll-craft | 43 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4529 | 1600.9 | 1 | 16 | - |  |
| 77 | Jakeschincariol/instagram-agent-skill | 42 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4849 | 2303.3 | 1 | 2 | - |  |
| 78 | yaojingang/yao-meta-skill | 42 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2719 | 359.4 | 3 | 56 | - |  |
| 79 | CloudAI-X/threejs-skills | 41 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3985 | 402.5 | 1 | 20 | - |  |
| 80 | sarpstar/cinecode | 40 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 1614 | 1614.0 | 3 | 7 | - |  |
| 81 | ythx-101/live-panel-skill | 39 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 840 | 580.4 | 4 | 40 | - |  |
| 82 | 40RTY-ai/shopify-admin-skills | 38 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 27.9 | 3 | 13 | 2026-06-17 |  |
| 83 | Jakeschincariol/linkedin-agent-skill | 38 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3205 | 1391.9 | 1 | 1 | - |  |
| 84 | nexscope-ai/eCommerce-Skills | 38 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1332 | 166.6 | 7 | 1 | - |  |
| 85 | Jakeschincariol/founder-skill | 37 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2452 | 1863.5 | 1 | 1 | - |  |
| 86 | kylezantos/design-motion-principles | 36 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1528 | 151.8 | 1 | 0 | 2026-05-21 |  |
| 87 | lottiefiles/motion-design-skill | 36 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 2853 | 348.3 | 1 | 0 | - |  |
| 88 | nexscope-ai/Amazon-Skills | 36 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 834 | 101.0 | 5 | 1 | - |  |
| 89 | heyitsnoah/claudesidian | 35 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2606 | 184.2 | 3 | 0 | 2026-04-11 |  |
| 90 | zanwei/design-dna | 35 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2079 | 265.6 | 3 | 4 | - |  |
| 91 | hamen/compose_skill | 32 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 378 | 53.0 | 3 | 0 | 2026-07-07 |  |
| 92 | xjli360/sealeap-amazon-skills | 32 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 369 | 128.9 | 1 | 15 | - |  |
| 93 | evanca/flutter-ai-rules | 31 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 669 | 35.5 | 1 | 13 | - |  |
| 94 | lemomo-ai/lemo-wake | 31 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 256 | 176.9 | 1 | 15 | 2026-10-05 |  |
| 95 | rshankras/claude-code-apple-skills | 31 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 861 | 68.3 | 2 | 3 | - |  |
| 96 | RevenueCat/play-billing-skills | 30 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 10.9 | 1 | 15 | 2026-10-15 |  |
| 97 | freshtechbro/claudedesignskills | 30 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1248 | 98.0 | 1 | 0 | - |  |
| 98 | tuist/fuckingapproachableswiftconcurrency | 30 D | 0 | - | 0/0/0 | MIT |  | 158 | 14.6 | 15 | 0 | - |  |
| 99 | mercadopago/mercadopago-claude-marketplace | 29 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.7 | 10 | 7 | - |  |
| 100 | moiz-za/etsy-seller-seo-system | 29 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 47 | 7.8 | 2 | 13 | 2026-10-23 |  |
| 101 | twostraws/SwiftData-Agent-Skill | 29 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 463 | 56.3 | 2 | 1 | 2026-03-11 |  |
| 102 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 137 | 78.6 | 1 | 11 | - |  |
| 103 | Livsy90/iOS-Performance-Agent-Skills | 27 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 120 | 20.8 | 2 | 0 | 2026-07-12 |  |
| 104 | OrcaQubits/agentic-commerce-skills-plugins | 27 D | 272 | 05-e-ticaret-pazaryeri (272) | 265/7/0 | MIT |  | 40 | 4.7 | 3 | 11 | 2026-05-13 |  |
| 105 | ehmo/platform-design-skills | 27 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 640 | 67.6 | 1 | 0 | - |  |
| 106 | xianyu110/ecommerce-image-skills | 27 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 144 | 101.8 | 1 | 7 | - |  |
| 107 | finsilabs/awesome-ecommerce-skills | 26 D | 178 | 05-e-ticaret-pazaryeri (178) | 160/18/0 | MIT |  | 63 | 7.7 | 4 | 3 | - |  |
| 108 | ParthJadhav/ios-marketing-capture | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 265 | 36.6 | 1 | 1 | - |  |
| 109 | dpconde/claude-android-skill | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 352 | 31.1 | 1 | 0 | - |  |
| 110 | Lonsdale201/wp-agent-skills | 22 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 3.9 | 3 | 25 | - |  |
| 111 | MADTeacher/mad-agents-skills | 22 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.0 | 2 | 0 | - |  |
| 112 | dadederk/iOS-Accessibility-Agent-Skill | 22 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 176 | 18.1 | 1 | 0 | - |  |
| 113 | leodavincs/kalem | 22 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 106 | 106.0 | 1 | 7 | - |  |
| 114 | Harishwarrior/flutter-claude-skills | 21 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 68 | 5.3 | 2 | 3 | - |  |
| 115 | Shopify/agent-skills | 21 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 101 | 13.4 | 1 | 0 | - |  |
| 116 | Kappaemme-git/codex-phone-lab | 20 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 16.0 | 1 | 0 | - |  |
| 117 | YildizDikme/claude-video-edit | 20 D | 0 | - | 0/0/0 | MIT |  | 33 | 33.0 | 1 | 3 | - |  |
| 118 | oldred-byte/ec-visual-skill | 20 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 104 | 16.2 | 1 | 0 | - |  |
| 119 | Viniciuscarvalho/swift-code-reviewer-skill | 19 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.2 | 5 | 0 | 2026-05-07 |  |
| 120 | avenoxai/avenox-video-kurgu-notlari | 19 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 27 | 27.0 | 1 | 1 | - |  |
| 121 | yohannescodes/apple-app-review-compliance | 18 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 20 | 20.0 | 1 | 4 | - |  |
| 122 | jazzychad/ios-code-audit | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.0 | 1 | 0 | - |  |
| 123 | mmiani/kotlin-kmp-claude-agent-skills | 17 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 90 | 11.7 | 1 | 8 | - |  |
| 124 | Trendyol/trendyol-integration-developer-tool | 16 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.7 | 3 | 0 | - |  |
| 125 | arjitj2/swiftui-design-principles | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 34 | 3.9 | 1 | 0 | - |  |
| 126 | lemomo-ai/codex-radar | 15 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 7.2 | 1 | 8 | - |  |
| 127 | avenoxai/higgsfield-studio | 11 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 14 | 4.8 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 87 A | r186 | `threejs-fundamentals` 88/D, `threejs-geometry` 78/D, `threejs-materials` 78/D, `threejs-lighting` 88/D, `threejs-textures` 80/D, `threejs-loaders` 88/D, `threejs-shaders` 78/D, `threejs-postprocessing` 78/D, `threejs-animation` 80/D, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 80 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `find-docs` 96/B, `tailwind-design-system` 93/A, `web-artifacts-builder` 90/B, `remotion-create` 89/B, `context7-mcp` 88/B | tasarim-teknolojileri.md |
| 3 | d3/d3 | 77 B | v7.9 | `d3-viz` 93/A, `d3-visualization` 97/A, `d3-data-visualization` 71/C, `geospatial-and-cartographic-visualization` 71/C | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 75 B | - | `ffmpeg` 93/A, `video-edit` 100/A, `video-understand` 94/A, `character-animation-qa` 86/A | kutuphaneler.md |
| 5 | ManimCommunity/manim | 72 B | v0.22 | `manim-composer` 94/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 93/A, `remotion-to-hyperframes` 97/A, `manim-video` 84/C | tasarim-teknolojileri.md |
| 6 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 7 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 94/A, `azure-speech-to-text` 94/A, `krillinai-subtitle` 89/C, `whisper` 86/C, `auto-editor-transcribe` 84/C, `twilio-conference-calls` 71/C | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 71 B | v9.8 | `threejs-react-three-fiber` 86/D, `react-three-fiber` 61/D, `react-three-fiber-game` 73/C, `blender-web-pipeline` 61/D, `web3d-integration-patterns` 61/D, `substance-3d-texturing` 53/D, `modern-web-design` 51/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 68 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 94/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 88/B | kutuphaneler.md |
| 10 | 666ghj/MiroFish | 67 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 11 | blender/blender | 67 B | - | `blender-web-pipeline` 61/D, `3d-asset-generation` 94/A, `threejs-loaders` 88/D, `remotion-to-hyperframes` 97/A, `blender` 80/C, `web-3d-asset-pipeline` 73/C | kutuphaneler.md |
| 12 | QwikDev/partytown | 64 C | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 63 C | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 67/D | tasarim-teknolojileri.md |
| 14 | dequelabs/axe-core | 63 C | v4.14 (MPL-2.0) | `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `salesforce-component-standards` 97/B, `scoutqa-test` 97/B, `replica-design` 84/D, `inclusive-design` 79/D, `accessibility` 77/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 15 | librosa/librosa | 63 C | - | `media-use` 100/A | kutuphaneler.md |
| 16 | DavidHDev/react-bits | 62 C | - | `animated-component-libraries` 61/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 17 | paperjs/paper.js | 61 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 18 | darkroomengineering/lenis | 60 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 61/D | tasarim-teknolojileri.md |
| 19 | pmndrs/drei | 60 C | v10.7 | `threejs-react-three-fiber` 86/D | tasarim-teknolojileri.md |
| 20 | airbnb/lottie-web | 59 C | v5.13 | `lottie-animations` 61/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 78/A, `flutter-pre-caching` 77/D, `motion-design` 64/D, `rive-interactive` 61/D | tasarim-teknolojileri.md |
| 21 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 22 | ai/size-limit | 56 C | 14.2 (T5) | `react-doctor` 75/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 55 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 94/A | tasarim-teknolojileri.md |
| 24 | liabru/matter-js | 53 C | 0.20 | `pixijs-2d` 69/D, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 25 | pmndrs/postprocessing | 51 C | v6.39 | `threejs-postprocessing` 78/D, `threejs-shaders` 78/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 26 | rough-stuff/rough | 49 D | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 27 | greensock/GSAP | 48 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 28 | theatre-js/theatre | 46 D | 0.4 (r3f) | `threejs-animation` 80/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 29 | barvian/number-flow | 45 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 30 | opentypejs/opentype.js | 45 D | 2.0 | `svg-character-animation` 94/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 31 | argyleink/open-props | 44 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 32 | figma/code-connect | 44 D | v2.0 | `figma-code-connect` 68/C | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 44 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 41 D | v0.20 | `threejs-world-generation` 93/A, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 35 | JohnHeibel/ClaudeAnimationBase | 40 D | - | `canvas-procedural-animation` 85/A, `algorithmic-art` 81/B, `svg-character-animation` 94/A | tasarim-teknolojileri.md |
| 36 | metafizzy/zdog | 38 D | v1.1 | `svg-character-animation` 94/A, `canvas-procedural-animation` 85/A, `lightweight-3d-effects` 60/D | tasarim-teknolojileri.md |
| 37 | meyda/meyda | 38 D | - | `canvas-procedural-animation` 85/A | kutuphaneler.md |
| 38 | oframe/ogl | 37 D | - | `lightweight-3d-effects` 60/D, `threejs-shaders` 78/D | tasarim-teknolojileri.md |
| 39 | zhuyansen/awesome-claude-video-skills | 37 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 40 | 14islands/r3f-scroll-rig | 34 D | v8.15 | `threejs-react-three-fiber` 86/D, `web3d-integration-patterns` 61/D, `gsap-framer-scroll-animation` 99/B, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `scrollytelling-and-parallax-data-visualization` 71/C, `lottie-animations` 61/D, `barba-js` 61/D | tasarim-teknolojileri.md |
| 41 | linvi/tweetinvi | 33 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 42 | jwagner/simplex-noise.js | 32 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 78/D, `threejs-world-generation` 93/A, `google-docs` 66/C | tasarim-teknolojileri.md |
| 43 | nevertoday/350-layout-compositions | 32 D | - | `design-taste-frontend` 100/B, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 44 | pmndrs/react-three-a11y | 29 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 45 | wj-sidiss/etsy-otomasyon-full-full-surum | 28 D | - | `etsy-seller` 76/D, `etsy-api` 59/D, `etsy-seo` 81/D | kutuphaneler.md |
| 46 | arturitu/the-delegation | 23 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
