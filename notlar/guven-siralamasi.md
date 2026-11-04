# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-02, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 88A (13) · nextlevelbuilder/ui-ux-pro-max-skill 86A (2) · anthropics/claude-code 83A (1) | `impeccable` 100/A, `design-taste-frontend` 100/B, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 88A (3) · nextlevelbuilder/ui-ux-pro-max-skill 86A (4) · anthropics/skills 74B (2) | `tailwind-design-system` 96/B, `brand-extract` 94/A, `brandkit` 94/A, `stitch-design-taste` 94/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 88A (7) · calesthio/OpenMontage 73B (2) · greensock/gsap-skills 54C (7) | `emilkowalski-motion` 96/A, `motion-lab` 96/A, `animate` 94/A, `gpt-taste` 94/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 54C (1) · nateherkai/scroll-craft 48D (1) · freshtechbro/claudedesignskills 34D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 62/D, `locomotive-scroll` 62/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 44D (13) · freshtechbro/claudedesignskills 34D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 88A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 59C (69) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 88A (14) · nextlevelbuilder/ui-ux-pro-max-skill 86A (1) · anthropics/claude-plugins-official 75B (1) | `playground` 100/B, `card-twitter` 96/A, `card-xiaohongshu` 96/A, `deck-guizang-editorial` 96/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 88A (3) · microsoft/playwright 84A (2) · addyosmani/agent-skills 84A (1) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 96/A, `impeccable-design-polish` 96/A, `agent-browser` 94/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 84A (8) · obra/superpowers 81A (3) · anthropics/claude-plugins-official 75B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `code-review` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 84A (2) · tt-a1i/archify 82A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 84A (2) · tt-a1i/archify 82A (1) · obra/superpowers 81A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 84A (2) · vudovn/ag-kit 57C (6) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `frontend-architecture` 83/C, `api-patterns` 76/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 93A (1) · addyosmani/agent-skills 84A (5) · anthropics/claude-plugins-official 75B (1) | `security-and-hardening` 100/A, `reverse-engineer-anything` 99/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 84A (1) · anthropics/claude-plugins-official 75B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 64C (37) · expo/skills 56C (24) · hamen/compose_skill 36D (2) | `agp-9-upgrade` 99/C, `android-profiler` 99/C, `anr-audit-and-fix` 99/C, `appfunctions` 99/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 88A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 72B (1) | `view-pdf` 100/B, `docx` 98/B, `pptx` 97/B, `xlsx` 97/B |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (1) · tt-a1i/archify 82A (1) | `documentation-and-adrs` 100/A, `doc-coauthoring` 97/B, `beautiful-mermaid` 97/B, `d3-visualization` 96/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 88A (1) · anthropics/skills 74B (1) · vercel-labs/agent-skills 66B (1) | `research-decision-room` 96/A, `internal-comms` 90/B, `writing-guidelines` 84/B, `ig-caption` 84/D |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 63C (2) · heyitsnoah/claudesidian 38D (13) | `add-frontmatter` 72/D, `json-canvas` 70/D, `obsidian-bases` 70/D, `file-organizer` 69/C |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 75B (4) · anthropics/skills 74B (3) · ComposioHQ/awesome-claude-skills 63C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-builder` 97/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 91A (1) · Panniantong/Agent-Reach 80A (1) · teng-lin/notebooklm-py 69B (1) | `agent-reach` 98/A, `graphify` 97/A, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 88A (2) · heygen-com/hyperframes 86A (1) · obra/superpowers 81A (1) | `reverse-any-video` 100/A, `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 96/A |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 82A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 88A (18) · heygen-com/hyperframes 86A (10) · remotion-dev/remotion 77B (13) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | calesthio/OpenMontage 73B (14) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | calesthio/OpenMontage 73B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 88A (2) · heygen-com/hyperframes 86A (3) · calesthio/OpenMontage 73B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `manim-composer` 97/B |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 72B (58) | `account-context` 100/B, `account-plan` 100/B, `account-research` 100/B, `account-tiering` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 72B (26) · Jakeschincariol/day-trader-skill 47D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 72B (69) · Jakeschincariol/founder-skill 41D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 72B (10) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 88A (1) · nexscope-ai/eCommerce-Skills 42D (156) · 40RTY-ai/shopify-admin-skills 42D (117) | `ecommerce-image-workflow` 94/A, `amazon-review-checker` 83/D, `brand-monitoring` 83/D, `brand-protection-amazon` 83/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 76B (90) · anthropics/knowledge-work-plugins 72B (6) | `instrument-data-to-allotrope` 100/B, `nextflow-development` 100/B, `scientific-problem-selection` 100/B, `scvi-tools` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 76B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 76B (27) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 76B (37) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 76B (2) · earthtojake/text-to-cad 70B (12) | `bambu-labs` 100/B, `dfam-check` 100/B, `dfm` 100/B, `gcode` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 93 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 419002 | 63057.7 | 356 | 5619 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 91 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 140568 | 20062.3 | 382 | 1385 | 2026-11-01 | 🔥 |
| 3 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143460 | 1185.1 | 4180 | 1526 | 2026-10-31 | 🔥 |
| 4 | react/react | 89 A | 0 | - | 0/0/0 | MIT | ✓ | 252077 | 1560.7 | 2027 | 137 | 2026-10-14 |  |
| 5 | nexu-io/open-design | 88 A | 74 | 01-video-uretim-montaj (18), 07-gorsel-sanat-sunum (14) | 73/1/0 | Apache-2.0 |  | 105353 | 17035.8 | 451 | 780 | 2026-10-22 |  |
| 6 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 182163 | 38725.6 | 133 | 163 | 2026-10-29 | 🔥 |
| 7 | heygen-com/hyperframes | 86 A | 14 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/1 | Apache-2.0 | ✓ | 77137 | 9894.4 | 125 | 3039 | 2026-11-02 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 86 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143857 | 12977.0 | 107 | 80 | 2026-08-13 |  |
| 9 | addyosmani/agent-skills | 84 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112570 | 13162.0 | 97 | 412 | 2026-10-31 | 🔥 |
| 10 | microsoft/playwright | 84 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 99065 | 1183.8 | 827 | 729 | 2026-10-14 |  |
| 11 | anthropics/claude-code | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154176 | 7584.1 | 59 | 243 | 2026-10-31 | 🔥 |
| 12 | tt-a1i/archify | 82 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 92406 | 13975.8 | 92 | 1632 | 2026-10-19 |  |
| 13 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 310663 | 24278.0 | 44 | 6 | 2026-10-21 | 🔥 |
| 14 | Panniantong/Agent-Reach | 80 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 107638 | 13036.6 | 46 | 138 | 2026-11-01 | 🔥 |
| 15 | pbakaus/impeccable | 80 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 99404 | 8609.3 | 62 | 1207 | 2026-10-26 | 🔥 |
| 16 | Leonxlnx/taste-skill | 78 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 107836 | 12805.5 | 24 | 103 | 2026-10-24 | 🔥 |
| 17 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48612 | 293.6 | 639 | 94 | 2026-10-01 |  |
| 18 | remotion-dev/remotion | 77 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 69773 | 913.1 | 479 | 5481 | 2026-10-26 | 🔥 |
| 19 | GoogleChrome/lighthouse | 76 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30996 | 242.2 | 397 | 185 | 2026-10-27 |  |
| 20 | K-Dense-AI/scientific-agent-skills | 76 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55677 | 4465.9 | 58 | 94 | 2026-10-01 | 🔥 |
| 21 | anthropics/claude-plugins-official | 75 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45728 | 4006.1 | 42 | 1851 | - | 🔥 |
| 22 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 186390 | 13956.3 | 17 | 15 | - | 🔥 |
| 23 | calesthio/OpenMontage | 73 B | 57 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/13/22 | AGPL-3.0 |  | 74392 | 10373.9 | 76 | 162 | - | 🔥 |
| 24 | anthropics/knowledge-work-plugins | 72 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34376 | 3692.7 | 32 | 597 | - | 🔥 |
| 25 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 34780 | 363.6 | 147 | 1002 | - |  |
| 26 | earthtojake/text-to-cad | 70 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24772 | 3881.8 | 31 | 903 | 2026-10-30 | 🔥 |
| 27 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20059 | 2039.4 | 42 | 692 | 2026-10-29 |  |
| 28 | multica-ai/andrej-karpathy-skills | 68 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 228018 | 24845.0 | 7 | 0 | - | 🔥 |
| 29 | vercel-labs/agent-skills | 66 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33361 | 3082.6 | 28 | 23 | 2026-10-27 | 🔥 |
| 30 | cloudflare/security-audit-skill | 65 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 56433 | 12522.4 | 4 | 3 | - | 🔥 |
| 31 | Fei-Away/Codex-Dream-Skin | 64 C | 0 | - | 0/0/0 | MIT |  | 15289 | 4225.3 | 23 | 46 | 2026-10-15 |  |
| 32 | android/skills | 64 C | 37 | 08-mobil-uygulama (37) | 36/1/0 | Apache-2.0 | ✓ | 10235 | 1346.9 | 8 | 38 | 2026-10-29 | 🔥 |
| 33 | ComposioHQ/awesome-claude-skills | 63 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78523 | 6265.4 | 29 | 0 | - |  |
| 34 | lemomo-ai/lemo-opuscar | 63 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 10618 | 8724.0 | 4 | 80 | 2026-10-12 |  |
| 35 | Donchitos/Claude-Code-Game-Studios | 59 C | 69 | 06-oyun-2d-grafik (69) | 69/0/0 | MIT |  | 32364 | 3740.9 | 1 | 5 | 2026-10-19 | 🔥 |
| 36 | cloudflare/skills | 59 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3247 | 301.9 | 48 | 256 | - | 🔥 |
| 37 | czlonkowski/n8n-skills | 57 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6564 | 527.9 | 7 | 35 | 2026-10-24 | 🔥 |
| 38 | vudovn/ag-kit | 57 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 854.2 | 10 | 8 | 2026-08-31 |  |
| 39 | expo/skills | 56 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4011 | 361.8 | 31 | 52 | - | 🔥 |
| 40 | darkroomengineering/satus | 54 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 195 | 2026-08-28 |  |
| 41 | greensock/gsap-skills | 54 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17696 | 2213.8 | 4 | 0 | - |  |
| 42 | Jakeschincariol/replica-skill | 49 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 6998 | 6998.0 | 1 | 1 | - |  |
| 43 | nateherkai/scroll-craft | 48 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4370 | 1845.1 | 1 | 16 | - |  |
| 44 | Jakeschincariol/day-trader-skill | 47 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 4327 | 4327.0 | 1 | 1 | - |  |
| 45 | Jakeschincariol/instagram-agent-skill | 46 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4356 | 2648.4 | 1 | 2 | - |  |
| 46 | Jakeschincariol/youtube-agent-skill | 46 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 4169 | 2696.5 | 1 | 1 | - |  |
| 47 | yaojingang/yao-meta-skill | 46 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2719 | 382.7 | 3 | 56 | - |  |
| 48 | CloudAI-X/threejs-skills | 44 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3908 | 413.9 | 1 | 20 | - |  |
| 49 | ythx-101/live-panel-skill | 43 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 833 | 833.0 | 4 | 40 | - |  |
| 50 | 40RTY-ai/shopify-admin-skills | 42 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 29.8 | 3 | 13 | 2026-06-17 |  |
| 51 | Jakeschincariol/linkedin-agent-skill | 42 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3035 | 1647.6 | 1 | 1 | - |  |
| 52 | nexscope-ai/eCommerce-Skills | 42 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1312 | 174.2 | 7 | 1 | - |  |
| 53 | Jakeschincariol/founder-skill | 41 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2324 | 2324.0 | 1 | 1 | - |  |
| 54 | nexscope-ai/Amazon-Skills | 40 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 822 | 105.4 | 5 | 1 | - |  |
| 55 | zanwei/design-dna | 39 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2064 | 280.1 | 3 | 4 | - |  |
| 56 | heyitsnoah/claudesidian | 38 D | 18 | 04-not-alma-bilgi-yonetimi (13), 05-git-pr-surum (3) | 17/1/0 | MIT |  | 2607 | 190.5 | 3 | 0 | 2026-04-11 |  |
| 57 | hamen/compose_skill | 36 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 378 | 56.6 | 3 | 0 | 2026-07-07 |  |
| 58 | xjli360/sealeap-amazon-skills | 36 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 342 | 142.4 | 1 | 15 | - |  |
| 59 | evanca/flutter-ai-rules | 35 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 668 | 36.3 | 1 | 14 | - |  |
| 60 | lemomo-ai/lemo-wake | 35 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 233 | 233.0 | 1 | 15 | 2026-10-05 |  |
| 61 | OrcaQubits/agentic-commerce-skills-plugins | 34 D | 272 | 05-e-ticaret-pazaryeri (272) | 265/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 62 | freshtechbro/claudedesignskills | 34 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1212 | 98.8 | 1 | 0 | - |  |
| 63 | mercadopago/mercadopago-claude-marketplace | 33 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.9 | 10 | 15 | - |  |
| 64 | tuist/fuckingapproachableswiftconcurrency | 33 D | 0 | - | 0/0/0 | MIT |  | 158 | 15.2 | 15 | 0 | - |  |
| 65 | Livsy90/iOS-Performance-Agent-Skills | 30 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 120 | 22.7 | 2 | 0 | 2026-07-12 |  |
| 66 | dpconde/claude-android-skill | 30 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 350 | 32.2 | 1 | 0 | - |  |
| 67 | xjli360/sealeap-ecommerce-skills | 30 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 119 | 92.8 | 1 | 11 | - |  |
| 68 | ParthJadhav/ios-marketing-capture | 29 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 265 | 39.1 | 1 | 1 | - |  |
| 69 | finsilabs/awesome-ecommerce-skills | 29 D | 178 | 05-e-ticaret-pazaryeri (178) | 160/18/0 | MIT |  | 61 | 7.9 | 4 | 3 | - |  |
| 70 | Viniciuscarvalho/swift-code-reviewer-skill | 26 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.5 | 5 | 0 | 2026-05-07 |  |
| 71 | MADTeacher/mad-agents-skills | 25 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.5 | 2 | 0 | - |  |
| 72 | dadederk/iOS-Accessibility-Agent-Skill | 25 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 176 | 19.0 | 1 | 0 | - |  |
| 73 | Kappaemme-git/codex-phone-lab | 24 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 17.4 | 1 | 0 | - |  |
| 74 | Lonsdale201/wp-agent-skills | 24 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.2 | 3 | 29 | - |  |
| 75 | Shopify/agent-skills | 24 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 100 | 14.1 | 1 | 0 | - |  |
| 76 | Harishwarrior/flutter-claude-skills | 23 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 68 | 5.5 | 2 | 3 | - |  |
| 77 | buluslan/ecommerce-competitor-analyzer | 23 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.7 | 1 | 3 | 2026-01-29 |  |
| 78 | oldred-byte/ec-visual-skill | 23 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 17.0 | 1 | 0 | - |  |
| 79 | mmiani/kotlin-kmp-claude-agent-skills | 20 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.3 | 1 | 8 | - |  |
| 80 | jazzychad/ios-code-audit | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.6 | 1 | 0 | - |  |
| 81 | Trendyol/trendyol-integration-developer-tool | 18 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.9 | 3 | 0 | - |  |
| 82 | arjitj2/swiftui-design-principles | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 33 | 4.0 | 1 | 0 | - |  |
| 83 | lemomo-ai/codex-radar | 17 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 7.9 | 1 | 8 | - |  |
| 84 | J-DTurner/etsy-api-skill | 15 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.6 | 1 | 0 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 87 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 79 B | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `remotion-create` 91/B, `web-artifacts-builder` 90/B, `saleor-storefront` 80/D, `nextjs-react` 78/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 74 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | ManimCommunity/manim | 72 B | v0.22 | `manim-composer` 97/B, `manimce-best-practices` 100/B, `manimgl-best-practices` 96/B, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 5 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 80/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 6 | d3/d3 | 72 B | v7.9 | `d3-viz` 96/B, `d3-visualization` 96/A | tasarim-teknolojileri.md |
| 7 | openai/whisper | 72 B | - | `media-use` 100/A, `speech-to-text` 100/B, `video-understand` 97/B, `azure-speech-to-text` 97/B | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 72 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 62/D, `blender-web-pipeline` 62/D, `web3d-integration-patterns` 62/D, `substance-3d-texturing` 54/D, `modern-web-design` 52/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 69 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 97/B, `manimce-best-practices` 100/B, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B | kutuphaneler.md |
| 10 | blender/blender | 67 B | - | `blender-web-pipeline` 62/D, `3d-asset-generation` 97/B, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A | kutuphaneler.md |
| 11 | QwikDev/partytown | 66 B | v1.0 (T5) | `shopify-hydrogen` 48/D | tasarim-teknolojileri.md |
| 12 | dequelabs/axe-core | 66 B | v4.14 (MPL-2.0) | `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 85/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 77/D | tasarim-teknolojileri.md |
| 13 | librosa/librosa | 66 B | - | `media-use` 100/A | kutuphaneler.md |
| 14 | 666ghj/MiroFish | 65 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 15 | Tonejs/Tone.js | 64 C | 15.1 | `sound-effects` 100/B, `music` 100/B | tasarim-teknolojileri.md |
| 16 | pmndrs/drei | 63 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 17 | DavidHDev/react-bits | 62 C | - | `animated-component-libraries` 62/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 18 | darkroomengineering/lenis | 62 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 62/D | tasarim-teknolojileri.md |
| 19 | paperjs/paper.js | 62 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 20 | fontsource/fontsource | 61 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 21 | ai/size-limit | 59 C | 14.2 (T5) | `react-doctor` 76/C, `nextjs-react-expert` 75/C | tasarim-teknolojileri.md |
| 22 | airbnb/lottie-web | 59 C | v5.13 | `lottie-animations` 62/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 78/D, `rive-interactive` 62/D | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 57 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 97/B | tasarim-teknolojileri.md |
| 24 | pmndrs/postprocessing | 55 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `relion` 97/B, `frame-logo-outro` 96/A | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 70/D, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 26 | opentypejs/opentype.js | 54 C | 2.0 | `svg-character-animation` 97/B, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 27 | rough-stuff/rough | 50 C | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 28 | barvian/number-flow | 49 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 29 | theatre-js/theatre | 49 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 30 | figma/code-connect | 48 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 31 | argyleink/open-props | 47 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 32 | greensock/GSAP | 47 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 33 | seek-oss/capsize | 47 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 44 D | v0.20 | `threejs-world-generation` 96/B, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 35 | metafizzy/zdog | 42 D | v1.1 | `svg-character-animation` 97/B, `canvas-procedural-animation` 89/B, `lightweight-3d-effects` 61/D | tasarim-teknolojileri.md |
| 36 | oframe/ogl | 42 D | - | `lightweight-3d-effects` 61/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 37 | meyda/meyda | 41 D | - | `canvas-procedural-animation` 89/B | kutuphaneler.md |
| 38 | zhuyansen/awesome-claude-video-skills | 40 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 39 | 14islands/r3f-scroll-rig | 37 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 62/D, `gpt-taste` 94/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 62/D, `barba-js` 62/D, `locomotive-scroll` 62/D, `scroll-reveal-libraries` 62/D | tasarim-teknolojileri.md |
| 40 | linvi/tweetinvi | 36 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 41 | jwagner/simplex-noise.js | 35 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 79/D, `threejs-world-generation` 96/B | tasarim-teknolojileri.md |
| 42 | nevertoday/350-layout-compositions | 35 D | - | `design-taste-frontend` 100/B, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 43 | pmndrs/react-three-a11y | 33 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 44 | arturitu/the-delegation | 27 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
