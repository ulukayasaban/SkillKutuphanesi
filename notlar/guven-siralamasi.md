# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-25, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 90A (7) · OpenMontageInc/OpenMontage 81A (2) · greensock/gsap-skills 54C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 54C (1) · nateherkai/scroll-craft 44D (1) · freshtechbro/claudedesignskills 31D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 57/D, `locomotive-scroll` 57/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 43D (13) · freshtechbro/claudedesignskills 31D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 90A (1) · pixijs/pixijs 78B (26) · Donchitos/Claude-Code-Game-Studios 62C (72) | `estimate` 99/C, `scope-check` 99/C, `test-setup` 99/C, `asset-audit` 97/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 90A (14) · nextlevelbuilder/ui-ux-pro-max-skill 87A (1) · OpenMontageInc/OpenMontage 81A (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 90A (3) · microsoft/playwright 87A (2) · addyosmani/agent-skills 85A (1) | `playwright-trace` 100/A, `playwright-component-testing` 98/A, `browser-testing-with-devtools` 98/A, `export-download-debugging` 97/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 85A (9) · mattpocock/skills 83A (30) · obra/superpowers 80A (3) | `accessibility-engineering` 100/A, `ask-matt` 100/A, `codebase-design` 100/A, `diagnosing-bugs` 100/A |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · tt-a1i/archify 86A (1) · addyosmani/agent-skills 85A (2) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | tt-a1i/archify 86A (1) · addyosmani/agent-skills 85A (2) · obra/superpowers 80A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 85A (2) · google/skills 66B (53) · vudovn/ag-kit 55C (6) | `api-and-interface-design` 100/A, `alloydb-basics` 100/B, `bigquery-basics` 100/B, `bigquery-bigframes` 100/B |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 90A (2) · addyosmani/agent-skills 85A (2) · obra/superpowers 80A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 85A (5) · anthropics/claude-plugins-official 78B (1) | `security-and-hardening` 100/A, `cloud-operator-share-context` 100/B, `cloud-run-alert-configuration` 100/B, `cloud-trace-querying` 100/B |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 87A (1) · anthropics/claude-plugins-official 78B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | google/skills 66B (11) · android/skills 64C (38) · expo/skills 55C (24) | `google-mobile-ads-banner` 100/B, `google-mobile-ads-get-started` 100/B, `google-mobile-ads-interstitial` 100/B, `google-mobile-ads-rewarded` 100/B |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 90A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 74B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 90A (2) · tt-a1i/archify 86A (1) · addyosmani/agent-skills 85A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `doc-coauthoring` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 90A (1) · blader/humanizer 76B (1) · anthropics/skills 74B (1) | `humanizer` 99/B, `research-decision-room` 97/A, `internal-comms` 90/B, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | obsidianmd/obsidian-skills 75B (6) · ComposioHQ/awesome-claude-skills 65B (1) · AgriciDaniel/claude-obsidian 63C (11) | `defuddle` 92/B, `knap` 92/B, `obsidian-cli` 92/B, `obsidian-headless` 92/B |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 78B (4) · anthropics/skills 74B (3) · google/skills 66B (25) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `agent-platform-endpoint-management` 100/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 90A (2) · JuliusBrussee/caveman 87A (22) · addyosmani/agent-skills 85A (2) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 93A (1) · Panniantong/Agent-Reach 82A (1) · upstash/context7 80A (4) | `agent-reach` 95/A, `find-docs` 95/A, `graphify` 94/A, `context7-cli` 88/A |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | heygen-com/hyperframes 91A (2) · nexu-io/open-design 90A (2) · obra/superpowers 80A (1) | `writing-skills` 100/A, `agent-development` 100/B, `breakdown-diagnosis` 100/B, `breakdown-to-next-report` 100/B |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | heygen-com/hyperframes 91A (10) · nexu-io/open-design 90A (17) · harry0703/MoneyPrinterTurbo 86A (1) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | OpenMontageInc/OpenMontage 81A (12) · krillinai/OpenCreator 66B (7) · Leonxlnx/earshot 60C (2) | `lyria` 100/A, `music` 100/A, `sound-effects` 100/A, `speech-to-text` 100/A |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | OpenMontageInc/OpenMontage 81A (16) · digitalsamba/claude-code-video-toolkit 59C (4) · yerel/kendi 17D (1) | `bfl-api` 100/A, `flux-best-practices` 100/A, `gemini-omni` 100/A, `seedance-2-0` 100/A |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | heygen-com/hyperframes 91A (3) · nexu-io/open-design 90A (2) · OpenMontageInc/OpenMontage 81A (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/A, `motion-doctrine` 99/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | coreyhaines31/marketingskills 82A (48) · anthropics/knowledge-work-plugins 74B (58) · AgriciDaniel/claude-seo 74B (28) | `ab-testing` 100/A, `ad-creative` 100/A, `ai-seo` 100/A, `analytics` 100/A |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 74B (26) · Jakeschincariol/day-trader-skill 49D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 74B (69) · Jakeschincariol/founder-skill 42D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 74B (10) · google/skills 66B (2) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 90A (1) · nexscope-ai/eCommerce-Skills 41D (156) · nexscope-ai/Amazon-Skills 38D (52) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 78B (90) · anthropics/knowledge-work-plugins 74B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 78B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 78B (27) · Orchestra-Research/AI-Research-SKILLs 57C (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 78B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 68B (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 78B (2) · earthtojake/text-to-cad 72B (17) | `bambu-labs` 98/B, `dfam-check` 98/B, `dfm` 98/B, `engineering-drawing` 98/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 476996 | 64447.5 | 458 | 9469 | 2026-11-20 | 🔥 |
| 2 | Graphify-Labs/graphify | 93 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 152966 | 19704.1 | 436 | 1655 | 2026-11-24 | 🔥 |
| 3 | affaan-m/ECC | 93 A | 0 | - | 0/0/0 | MIT |  | 310158 | 30317.7 | 547 | 2557 | 2026-10-01 |  |
| 4 | heygen-com/hyperframes | 91 A | 15 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/2 | Apache-2.0 | ✓ | 89524 | 10467.4 | 155 | 3960 | 2026-11-24 | 🔥 |
| 5 | nexu-io/open-design | 90 A | 73 | 01-video-uretim-montaj (17), 07-gorsel-sanat-sunum (14) | 72/1/0 | Apache-2.0 |  | 109313 | 15749.4 | 456 | 435 | 2026-11-19 |  |
| 6 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143684 | 1179.6 | 4196 | 1600 | 2026-11-23 | 🔥 |
| 7 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 252865 | 1558.3 | 2028 | 151 | 2026-10-14 |  |
| 8 | JuliusBrussee/caveman | 87 A | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 122631 | 15863.8 | 116 | 1632 | 2026-11-22 |  |
| 9 | microsoft/playwright | 87 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 100988 | 1196.0 | 833 | 808 | 2026-11-13 | 🔥 |
| 10 | nextlevelbuilder/ui-ux-pro-max-skill | 87 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 153719 | 12980.7 | 126 | 93 | 2026-08-13 |  |
| 11 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 198027 | 36265.2 | 133 | 162 | 2026-10-29 | 🔥 |
| 12 | harry0703/MoneyPrinterTurbo | 86 A | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 145481 | 4471.8 | 180 | 499 | 2026-11-23 | 🔥 |
| 13 | tt-a1i/archify | 86 A | 3 | 02-kod-kalitesi-review (1), 03-test-hata-ayiklama (1) | 3/0/0 | Apache-2.0 |  | 99504 | 13504.1 | 108 | 2621 | 2026-11-24 |  |
| 14 | addyosmani/agent-skills | 85 A | 26 | 01-planlama-metodoloji (9), 06-devops-guvenlik-performans (5) | 26/0/0 | MIT |  | 120187 | 12910.5 | 106 | 440 | 2026-11-24 | 🔥 |
| 15 | anthropics/claude-code | 85 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 156944 | 7443.2 | 59 | 403 | 2026-11-23 | 🔥 |
| 16 | pbakaus/impeccable | 84 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 116236 | 9448.1 | 67 | 2154 | 2026-11-24 | 🔥 |
| 17 | ruvnet/ruflo | 84 A | 0 | - | 0/0/0 | MIT |  | 82370 | 4628.6 | 105 | 3250 | 2026-11-24 |  |
| 18 | mattpocock/skills | 83 A | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 332135 | 34226.8 | 10 | 107 | 2026-10-29 | 🔥 |
| 19 | Panniantong/Agent-Reach | 82 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 114497 | 12703.3 | 56 | 164 | 2026-11-01 | 🔥 |
| 20 | coreyhaines31/marketingskills | 82 A | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 62450 | 6046.1 | 92 | 1173 | 2026-11-23 | 🔥 |
| 21 | Leonxlnx/taste-skill | 81 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 121079 | 13192.8 | 27 | 164 | 2026-11-07 | 🔥 |
| 22 | OpenMontageInc/OpenMontage | 81 A | 53 | 03-ai-gorsel-video-modelleri (16), 02-ses-muzik-konusma (12) | 21/11/21 | AGPL-3.0 |  | 83050 | 10476.0 | 128 | 272 | - | 🔥 |
| 23 | garrytan/gbrain | 80 A | 0 | - | 0/0/0 | MIT |  | 33537 | 4356.9 | 140 | 15326 | 2026-11-24 |  |
| 24 | obra/superpowers | 80 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 325731 | 24034.5 | 44 | 6 | 2026-11-03 | 🔥 |
| 25 | remotion-dev/remotion | 80 A | 13 | 01-video-uretim-montaj (13) | 10/3/0 | NOASSERTION | ✓ | 75459 | 977.8 | 515 | 6717 | 2026-11-24 | 🔥 |
| 26 | upstash/context7 | 80 A | 4 | 03-web-arastirma-veri (4) | 0/4/0 | MIT |  | 65407 | 3265.0 | 148 | 338 | 2026-11-24 |  |
| 27 | K-Dense-AI/scientific-agent-skills | 78 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 58356 | 4413.0 | 57 | 69 | 2026-10-01 | 🔥 |
| 28 | anthropics/claude-plugins-official | 78 B | 46 | 04-skill-plugin-yazimi (30), 02-agent-orkestrasyon (5) | 46/0/0 | Apache-2.0 | ✓ | 48119 | 3953.6 | 49 | 1456 | - | 🔥 |
| 29 | github/awesome-copilot | 78 B | 0 | - | 0/0/0 | MIT |  | 41524 | 2372.8 | 600 | 1104 | - |  |
| 30 | pixijs/pixijs | 78 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48889 | 294.0 | 653 | 102 | 2026-11-11 |  |
| 31 | GoogleChrome/lighthouse | 77 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 31199 | 242.3 | 400 | 231 | 2026-10-27 |  |
| 32 | ayghri/i-have-adhd | 76 B | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 62154 | 9640.2 | 53 | 77 | 2026-10-19 |  |
| 33 | blader/humanizer | 76 B | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 73145 | 7149.9 | 30 | 70 | 2026-11-10 | 🔥 |
| 34 | davila7/claude-code-templates | 76 B | 0 | - | 0/0/0 | MIT |  | 34175 | 2041.1 | 200 | 702 | 2026-10-09 |  |
| 35 | cathrynlavery/diagram-design | 75 B | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 71933 | 9806.1 | 76 | 357 | - |  |
| 36 | google/elephant-goldfish-model | 75 B | 8 | 01-planlama-metodoloji (8) | 8/0/0 | Apache-2.0 |  | 22650 | 9432.3 | 39 | 222 | 2026-11-06 | 🔥 |
| 37 | obsidianmd/obsidian-skills | 75 B | 7 | 04-not-alma-bilgi-yonetimi (6), 02-diyagram-dokumantasyon (1) | 7/0/0 | MIT |  | 53648 | 4987.5 | 28 | 47 | 2026-11-20 |  |
| 38 | AgriciDaniel/claude-seo | 74 B | 28 | 01-satis-pazarlama-musteri (28) | 28/0/0 | MIT |  | 32164 | 3360.1 | 52 | 466 | 2026-11-15 | 🔥 |
| 39 | anthropics/knowledge-work-plugins | 74 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 36794 | 3655.4 | 32 | 411 | - | 🔥 |
| 40 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 199922 | 14167.0 | 17 | 12 | - | 🔥 |
| 41 | earthtojake/text-to-cad | 72 B | 17 | 05-cad-imalat-robotik (17) | 17/0/0 | MIT |  | 27354 | 3832.1 | 34 | 487 | 2026-11-23 | 🔥 |
| 42 | motiondivision/motion | 72 B | 0 | - | 0/0/0 | MIT | ✓ | 35530 | 368.5 | 147 | 1390 | - |  |
| 43 | latent-spaces/brag | 70 B | 2 | 01-video-uretim-montaj (2) | 2/0/0 | MIT |  | 22477 | 4217.9 | 20 | 58 | 2026-11-15 |  |
| 44 | JuneYaooo/rea-video | 69 B | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 12985 | 12985.0 | 25 | 215 | 2026-11-11 |  |
| 45 | cloudflare/security-audit-skill | 69 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 77929 | 14806.5 | 4 | 3 | - | 🔥 |
| 46 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20366 | 1922.8 | 45 | 400 | 2026-10-29 |  |
| 47 | vercel-labs/agent-skills | 68 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 34869 | 3011.4 | 29 | 20 | 2026-11-20 | 🔥 |
| 48 | wanshuiyin/Auto-claude-code-research-in-sleep | 68 B | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 19782 | 2313.0 | 108 | 174 | 2026-09-28 |  |
| 49 | Nutlope/hallmark | 67 B | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 60525 | 8679.1 | 12 | 147 | - | 🔥 |
| 50 | Vincentwei1021/video-shotcraft | 67 B | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 22437 | 5287.5 | 17 | 54 | 2026-09-01 | 🔥 |
| 51 | google/skills | 66 B | 217 | 06-devops-guvenlik-performans (118), 04-mimari-api-veritabani (53) | 41/176/0 | Apache-2.0 |  | 24613 | 3130.7 | 9 | 365 | - | 🔥 |
| 52 | kajisho5/ffmpeg-skill | 66 B | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 10640 | 3897.1 | 17 | 966 | 2026-11-23 | 🔥 |
| 53 | krillinai/OpenCreator | 66 B | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14527 | 623.8 | 37 | 509 | 2026-11-23 |  |
| 54 | multica-ai/andrej-karpathy-skills | 66 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 235505 | 23706.5 | 7 | 0 | - | 🔥 |
| 55 | ComposioHQ/awesome-claude-skills | 65 B | 4 | 03-yazi-iletisim-icerik (2), 04-not-alma-bilgi-yonetimi (1) | 3/1/0 | yok | ✓ | 80247 | 6038.4 | 29 | 0 | - |  |
| 56 | android/skills | 64 C | 38 | 08-mobil-uygulama (38) | 37/1/0 | Apache-2.0 | ✓ | 10743 | 1285.8 | 8 | 34 | 2026-11-23 | 🔥 |
| 57 | lemomo-ai/lemo-opuscar | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 20656 | 10465.7 | 10 | 148 | 2026-11-12 |  |
| 58 | AgriciDaniel/claude-obsidian | 63 C | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16736 | 2193.0 | 11 | 95 | 2026-10-21 |  |
| 59 | Donchitos/Claude-Code-Game-Studios | 62 C | 72 | 06-oyun-2d-grafik (72) | 72/0/0 | MIT |  | 40822 | 4339.1 | 1 | 6 | 2026-11-09 | 🔥 |
| 60 | dreammis/social-auto-upload | 62 C | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16938 | 473.7 | 42 | 18 | 2026-10-22 |  |
| 61 | jacob-bd/gemini-notebook-mcp-cli | 62 C | 0 | - | 0/0/0 | MIT |  | 6567 | 592.4 | 72 | 233 | 2026-11-22 |  |
| 62 | browser-use/video-use | 61 C | 2 | 01-video-uretim-montaj (1), 04-motion-graphics-karakter (1) | 1/1/0 | MIT |  | 31528 | 4222.3 | 8 | 5 | - |  |
| 63 | Leonxlnx/earshot | 60 C | 2 | 02-ses-muzik-konusma (2) | 2/0/0 | MIT |  | 5719 | 4240.4 | 8 | 189 | 2026-11-20 |  |
| 64 | digitalsamba/claude-code-video-toolkit | 59 C | 14 | 01-video-uretim-montaj (7), 03-ai-gorsel-video-modelleri (4) | 4/8/2 | MIT |  | 2749 | 238.1 | 17 | 522 | 2026-11-22 |  |
| 65 | tradermonty/claude-trading-skills | 59 C | 0 | - | 0/0/0 | MIT |  | 8280 | 626.1 | 46 | 500 | - |  |
| 66 | cloudflare/skills | 58 C | 22 | 06-devops-guvenlik-performans (22) | 12/7/3 | Apache-2.0 | ✓ | 3447 | 299.4 | 51 | 273 | - | 🔥 |
| 67 | tddworks/baguette | 58 C | 2 | 04-skill-plugin-yazimi (2) | 2/0/0 | Apache-2.0 |  | 2345 | 342.7 | 18 | 574 | 2026-11-22 |  |
| 68 | zubair-trabzada/geo-seo-claude | 58 C | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11847 | 1286.2 | 25 | 56 | - |  |
| 69 | Orchestra-Research/AI-Research-SKILLs | 57 C | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14802 | 1162.7 | 17 | 0 | 2026-06-16 |  |
| 70 | AgriciDaniel/claude-ads | 56 C | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 11301 | 1197.0 | 2 | 39 | 2026-10-16 |  |
| 71 | WyattBlue/auto-editor | 56 C | 5 | 01-video-uretim-montaj (5) | 5/0/0 | Unlicense |  | 6102 | 77.3 | 17 | 341 | 2026-11-23 |  |
| 72 | czlonkowski/n8n-skills | 55 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6707 | 508.5 | 7 | 33 | 2026-10-24 | 🔥 |
| 73 | expo/skills | 55 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4227 | 356.9 | 31 | 41 | - | 🔥 |
| 74 | vudovn/ag-kit | 55 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8225 | 793.8 | 10 | 8 | 2026-08-31 |  |
| 75 | zarazhangrui/frontend-slides | 55 C | 1 | 07-gorsel-sanat-sunum (1) | 0/1/0 | MIT |  | 32850 | 3317.7 | 9 | 0 | 2026-05-26 |  |
| 76 | greensock/gsap-skills | 54 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 19013 | 2172.9 | 4 | 0 | - |  |
| 77 | openai/plugins | 54 C | 0 | - | 0/0/0 | yok | ✓ | 8338 | 952.9 | 63 | 11 | - |  |
| 78 | darkroomengineering/satus | 52 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1023 | 16.6 | 19 | 178 | 2026-08-28 |  |
| 79 | Ryze-AI-Adgent/open-seo-mcp-skills | 51 C | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 10658 | 3681.9 | 1 | 16 | - |  |
| 80 | wondelai/skills | 51 C | 0 | - | 0/0/0 | MIT |  | 2780 | 281.7 | 3 | 16 | 2026-08-29 |  |
| 81 | Jakeschincariol/day-trader-skill | 49 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 9478 | 8003.6 | 1 | 1 | - |  |
| 82 | veedstudio/open-edit | 49 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | Apache-2.0 |  | 1854 | 447.3 | 3 | 16 | 2026-08-03 |  |
| 83 | Jakeschincariol/replica-skill | 48 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 10552 | 6052.5 | 1 | 1 | - |  |
| 84 | feitangyuan/onetake | 48 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | NOASSERTION |  | 4458 | 2258.7 | 3 | 22 | 2026-10-08 |  |
| 85 | chrisbanes/skills | 47 D | 20 | 04-skill-plugin-yazimi (19), 05-git-pr-surum (1) | 20/0/0 | Apache-2.0 |  | 1166 | 179.9 | 4 | 160 | 2026-11-24 |  |
| 86 | Jakeschincariol/instagram-agent-skill | 46 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 8958 | 3730.5 | 1 | 2 | - |  |
| 87 | Jakeschincariol/youtube-agent-skill | 46 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 7300 | 3170.3 | 1 | 1 | - |  |
| 88 | hardikpandya/stop-slop | 46 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 19184 | 1833.9 | 2 | 0 | - |  |
| 89 | sarpstar/cinecode | 46 D | 1 | 01-video-uretim-montaj (1) | 0/1/0 | MIT |  | 2938 | 2938.0 | 3 | 9 | - |  |
| 90 | nateherkai/scroll-craft | 44 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 5426 | 1736.3 | 1 | 8 | - |  |
| 91 | CloudAI-X/threejs-skills | 43 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 4379 | 429.4 | 1 | 20 | - |  |
| 92 | huytieu/COG-second-brain | 43 D | 0 | - | 0/0/0 | MIT |  | 1516 | 113.5 | 6 | 6 | 2026-10-23 |  |
| 93 | lottiefiles/motion-design-skill | 43 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 3650 | 430.1 | 2 | 5 | - |  |
| 94 | shadcn-labs/snapcn | 43 D | 7 | 04-motion-graphics-karakter (7) | 0/7/0 | MIT |  | 699 | 171.4 | 3 | 224 | - |  |
| 95 | Jakeschincariol/founder-skill | 42 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 4868 | 3020.1 | 1 | 1 | - |  |
| 96 | yaojingang/yao-meta-skill | 42 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2742 | 348.8 | 4 | 10 | - |  |
| 97 | nexscope-ai/eCommerce-Skills | 41 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1522 | 183.6 | 7 | 2 | - |  |
| 98 | ythx-101/live-panel-skill | 41 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 880 | 504.8 | 4 | 41 | - |  |
| 99 | AbubakrChan/product-launch-motion | 40 D | 1 | 04-motion-graphics-karakter (1) | 1/0/0 | MIT |  | 534 | 134.2 | 2 | 44 | 2026-10-12 |  |
| 100 | Jakeschincariol/linkedin-agent-skill | 40 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3946 | 1518.5 | 1 | 1 | - |  |
| 101 | howseen-ai/claude-motion-design | 40 D | 0 | - | 0/0/0 | MIT |  | 894 | 460.6 | 1 | 32 | - |  |
| 102 | smyrgeorge/sqlx4k | 40 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 323 | 11.0 | 4 | 242 | 2026-11-01 |  |
| 103 | nexscope-ai/Amazon-Skills | 38 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 899 | 105.1 | 5 | 2 | - |  |
| 104 | Barty-Bart/motion-graphics | 37 D | 5 | 04-motion-graphics-karakter (5) | 5/0/0 | NOASSERTION |  | 1510 | 752.5 | 4 | 10 | - |  |
| 105 | echris6/motion-video-kit | 37 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 1455 | 749.7 | 1 | 7 | - |  |
| 106 | nateherkai/herk-edit-kit | 37 D | 10 | 01-video-uretim-montaj (10) | 5/5/0 | NOASSERTION |  | 3138 | 431.7 | 1 | 13 | - |  |
| 107 | rshankras/claude-code-apple-skills | 37 D | 13 | 08-mobil-uygulama (13) | 13/0/0 | MIT |  | 909 | 70.5 | 4 | 11 | - |  |
| 108 | zanwei/design-dna | 37 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2153 | 265.0 | 3 | 3 | - |  |
| 109 | 40RTY-ai/shopify-admin-skills | 36 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 205 | 27.3 | 3 | 4 | 2026-06-17 |  |
| 110 | heyitsnoah/claudesidian | 36 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2615 | 181.1 | 3 | 0 | 2026-04-11 |  |
| 111 | heygen-com/hyperframes-community-skills | 35 D | 7 | 01-video-uretim-montaj (7) | 6/1/0 | Apache-2.0 | ✓ | 293 | 96.8 | 3 | 6 | - |  |
| 112 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 2 | 05-e-ticaret-pazaryeri (2) | 2/0/0 | MIT |  | 41 | 4.7 | 3 | 16 | 2026-11-13 |  |
| 113 | evanca/flutter-ai-rules | 33 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 675 | 35.3 | 2 | 12 | - |  |
| 114 | Prisma-Labs-Dev/apple-skills | 32 D | 27 | 04-skill-plugin-yazimi (27) | 27/0/0 | MIT |  | 360 | 39.2 | 3 | 4 | - |  |
| 115 | hamen/compose_skill | 32 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 380 | 51.1 | 3 | 0 | 2026-07-07 |  |
| 116 | kylezantos/design-motion-principles | 32 D | 1 | 03-animasyon-motion (1) | 1/0/0 | MIT |  | 1648 | 159.0 | 1 | 0 | 2026-05-21 |  |
| 117 | lemomo-ai/lemo-wake | 32 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 389 | 223.1 | 1 | 15 | 2026-10-05 |  |
| 118 | xjli360/sealeap-amazon-skills | 32 D | 0 | - | 0/0/0 | MIT |  | 452 | 143.1 | 1 | 9 | - |  |
| 119 | RevenueCat/play-billing-skills | 31 D | 23 | 08-mobil-uygulama (22), 06-devops-guvenlik-performans (1) | 23/0/0 | Apache-2.0 |  | 60 | 10.4 | 1 | 28 | 2026-10-15 |  |
| 120 | better-i18n/oss | 31 D | 1 | 04-skill-plugin-yazimi (1) | 0/1/0 | MIT |  | 21 | 2.1 | 5 | 25 | 2026-10-04 |  |
| 121 | freshtechbro/claudedesignskills | 31 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1442 | 110.7 | 1 | 0 | - |  |
| 122 | tuzhechen2005/opus-video-skills | 30 D | 2 | 04-motion-graphics-karakter (2) | 2/0/0 | NOASSERTION |  | 564 | 285.8 | 3 | 9 | - |  |
| 123 | tugrawork-creator/saas-motion-kit | 29 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | NOASSERTION |  | 295 | 147.0 | 1 | 8 | 2026-10-04 |  |
| 124 | tuist/fuckingapproachableswiftconcurrency | 29 D | 0 | - | 0/0/0 | MIT |  | 159 | 14.3 | 15 | 0 | - |  |
| 125 | mercadopago/mercadopago-claude-marketplace | 28 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 33 | 3.7 | 10 | 3 | - |  |
| 126 | moiz-za/etsy-seller-seo-system | 28 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 55 | 8.7 | 2 | 13 | 2026-10-23 |  |
| 127 | namedtoaster/The-Last-Mile | 28 D | 19 | 04-skill-plugin-yazimi (18), 02-agent-orkestrasyon (1) | 18/1/0 | MIT |  | 41 | 27.7 | 3 | 146 | - |  |
| 128 | twostraws/SwiftData-Agent-Skill | 28 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 475 | 55.8 | 2 | 1 | 2026-03-11 |  |
| 129 | wj-sidiss/etsy-otomasyon-full-full-surum | 28 D | 0 | - | 0/0/0 | MIT |  | 57 | 57.0 | 1 | 8 | 2026-11-01 |  |
| 130 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 178 | 87.3 | 1 | 11 | - |  |
| 131 | ehmo/platform-design-skills | 27 D | 7 | 08-mobil-uygulama (7) | 7/0/0 | MIT |  | 651 | 66.6 | 1 | 0 | - |  |
| 132 | sirioberati/YouTube-AI-Video-Editing-System | 27 D | 0 | - | 0/0/0 | MIT |  | 171 | 148.5 | 1 | 4 | - |  |
| 133 | xianyu110/ecommerce-image-skills | 27 D | 10 | 05-e-ticaret-pazaryeri (10) | 0/10/0 | MIT |  | 194 | 113.4 | 1 | 7 | - |  |
| 134 | Livsy90/iOS-Performance-Agent-Skills | 26 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 121 | 20.0 | 2 | 0 | 2026-07-12 |  |
| 135 | finsilabs/awesome-ecommerce-skills | 26 D | 179 | 05-e-ticaret-pazaryeri (179) | 161/18/0 | MIT |  | 67 | 7.9 | 4 | 3 | - |  |
| 136 | dpconde/claude-android-skill | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 363 | 31.3 | 1 | 0 | - |  |
| 137 | motiful/product-shots | 25 D | 7 | 04-skill-plugin-yazimi (7) | 6/0/1 | MIT |  | 154 | 27.1 | 1 | 0 | - |  |
| 138 | thatrebeccarae/claude-marketing | 25 D | 54 | 04-skill-plugin-yazimi (50), 02-tasarim-sistemi-marka (2) | 52/0/2 | MIT |  | 216 | 22.7 | 2 | 0 | - |  |
| 139 | ParthJadhav/ios-marketing-capture | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 266 | 35.3 | 1 | 1 | - |  |
| 140 | Lonsdale201/wp-agent-skills | 22 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 3.8 | 3 | 19 | - |  |
| 141 | MADTeacher/mad-agents-skills | 21 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 114 | 10.9 | 2 | 0 | - |  |
| 142 | YildizDikme/claude-video-edit | 21 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 59 | 59.0 | 1 | 3 | - |  |
| 143 | dadederk/iOS-Accessibility-Agent-Skill | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 177 | 17.7 | 1 | 0 | - |  |
| 144 | leodavincs/kalem | 21 D | 2 | 01-video-uretim-montaj (2) | 2/0/0 | NOASSERTION |  | 123 | 123.0 | 1 | 7 | - |  |
| 145 | Harishwarrior/flutter-claude-skills | 20 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 71 | 5.4 | 2 | 3 | - |  |
| 146 | Shopify/agent-skills | 20 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 111 | 14.2 | 1 | 0 | - |  |
| 147 | tanujrajputdev/shopify-theme-audit-skill | 20 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 47 | 8.4 | 3 | 2 | - |  |
| 148 | Kappaemme-git/codex-phone-lab | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 96 | 15.4 | 1 | 0 | - |  |
| 149 | Viniciuscarvalho/swift-code-reviewer-skill | 19 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.1 | 5 | 0 | 2026-05-07 |  |
| 150 | oldred-byte/ec-visual-skill | 19 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 119 | 17.7 | 1 | 0 | - |  |
| 151 | avenoxai/avenox-video-kurgu-notlari | 17 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 30 | 30.0 | 1 | 1 | - |  |
| 152 | yohannescodes/apple-app-review-compliance | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 23 | 17.9 | 1 | 4 | - |  |
| 153 | Trendyol/trendyol-integration-developer-tool | 16 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 13 | 2.0 | 3 | 0 | - |  |
| 154 | jazzychad/ios-code-audit | 16 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 6.6 | 1 | 0 | - |  |
| 155 | arjitj2/swiftui-design-principles | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 36 | 4.0 | 1 | 0 | - |  |
| 156 | lemomo-ai/codex-radar | 14 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 40 | 7.0 | 1 | 8 | - |  |
| 157 | mmiani/kotlin-kmp-claude-agent-skills | 13 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 95 | 11.9 | 1 | 0 | - |  |
| 158 | avenoxai/higgsfield-studio | 10 D | 6 | 03-ai-gorsel-video-modelleri (5), 07-gorsel-sanat-sunum (1) | 0/5/1 | yok |  | 18 | 5.6 | 1 | 2 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 88 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 82 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `find-docs` 95/A, `tailwind-design-system` 93/A, `remotion-create` 90/A, `web-artifacts-builder` 90/B, `context7-mcp` 88/A | tasarim-teknolojileri.md |
| 3 | d3/d3 | 78 B | v7.9 | `d3-viz` 93/A, `d3-visualization` 97/A | tasarim-teknolojileri.md |
| 4 | FFmpeg/FFmpeg | 76 B | - | `ffmpeg` 93/A, `ffmpeg-skill` 95/B, `video-understand` 94/A, `character-animation-qa` 86/A, `product-launch-motion` 72/D, `kinetic-reel` 72/D, `cut-mistakes` 65/D, `cut-silences` 65/D | kutuphaneler.md |
| 5 | ManimCommunity/manim | 74 B | v0.22 | `manim-composer` 94/A, `manimce-best-practices` 100/A, `manimgl-best-practices` 93/A, `remotion-to-hyperframes` 97/A, `manim-video` 84/C | tasarim-teknolojileri.md |
| 6 | pmndrs/react-three-fiber | 73 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 57/D, `blender-web-pipeline` 57/D, `web3d-integration-patterns` 57/D, `substance-3d-texturing` 49/D, `modern-web-design` 47/D | tasarim-teknolojileri.md |
| 7 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/A | tasarim-teknolojileri.md |
| 8 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/A, `video-understand` 94/A, `azure-speech-to-text` 94/A, `krillinai-subtitle` 90/B, `whisper` 87/C, `auto-editor-transcribe` 84/C, `ajanla-video-kurgu` 69/D | kutuphaneler.md |
| 9 | blender/blender | 69 B | - | `blender-web-pipeline` 57/D, `3d-asset-generation` 94/A, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A, `render` 96/B, `blender` 81/C | kutuphaneler.md |
| 10 | KaTeX/KaTeX | 68 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 94/A, `manimce-best-practices` 100/A, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 88/B | kutuphaneler.md |
| 11 | 666ghj/MiroFish | 67 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 12 | QwikDev/partytown | 65 B | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 65 B | 15.1 | `sound-effects` 100/A, `music` 100/A, `cinecode` 68/D | tasarim-teknolojileri.md |
| 14 | darkroomengineering/lenis | 65 B | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 57/D | tasarim-teknolojileri.md |
| 15 | dequelabs/axe-core | 65 B | v4.14 (MPL-2.0) | `accessibility-engineering` 100/A, `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 84/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 16 | librosa/librosa | 65 B | - | `media-use` 100/A | kutuphaneler.md |
| 17 | DavidHDev/react-bits | 64 C | - | `animated-component-libraries` 57/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 18 | Fei-Away/Codex-Dream-Skin | 62 C | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 19 | paperjs/paper.js | 62 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 20 | pmndrs/drei | 61 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 21 | airbnb/lottie-web | 60 C | v5.13 | `lottie-animations` 57/D, `remotion-to-hyperframes` 97/A, `motion-design` 81/D, `lottie-bodymovin` 78/A, `flutter-pre-caching` 78/D, `rive-interactive` 57/D | tasarim-teknolojileri.md |
| 22 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 23 | ai/size-limit | 57 C | 14.2 (T5) | `react-doctor` 76/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 24 | motion-canvas/motion-canvas | 57 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 94/A | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 65/D, `canvas-procedural-animation` 85/A | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 53 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 27 | rough-stuff/rough | 50 C | v3.1 | `camera-3d-captions` 79/D, `day-in-my-life` 72/D | tasarim-teknolojileri.md |
| 28 | greensock/GSAP | 49 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 48 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | barvian/number-flow | 46 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 31 | opentypejs/opentype.js | 46 D | 2.0 | `svg-character-animation` 94/A, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 32 | figma/code-connect | 45 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 45 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | argyleink/open-props | 44 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 35 | JohnHeibel/ClaudeAnimationBase | 43 D | - | `canvas-procedural-animation` 85/A, `algorithmic-art` 81/B, `svg-character-animation` 94/A | tasarim-teknolojileri.md |
| 36 | pmndrs/cannon-es | 43 D | v0.20 | `threejs-world-generation` 93/A, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 37 | zhuyansen/awesome-claude-video-skills | 41 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 38 | metafizzy/zdog | 40 D | v1.1 | `svg-character-animation` 94/A, `canvas-procedural-animation` 85/A, `lightweight-3d-effects` 56/D | tasarim-teknolojileri.md |
| 39 | meyda/meyda | 40 D | - | `canvas-procedural-animation` 85/A | kutuphaneler.md |
| 40 | oframe/ogl | 39 D | - | `lightweight-3d-effects` 56/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 41 | nevertoday/350-layout-compositions | 36 D | - | `design-taste-frontend` 100/A, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 42 | 14islands/r3f-scroll-rig | 35 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 57/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 57/D, `barba-js` 57/D, `locomotive-scroll` 57/D, `scroll-reveal-libraries` 57/D | tasarim-teknolojileri.md |
| 43 | jwagner/simplex-noise.js | 34 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 79/D, `threejs-world-generation` 93/A | tasarim-teknolojileri.md |
| 44 | linvi/tweetinvi | 34 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 45 | pmndrs/react-three-a11y | 29 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 46 | arturitu/the-delegation | 24 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
