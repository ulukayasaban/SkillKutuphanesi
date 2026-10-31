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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 88A (13) · nextlevelbuilder/ui-ux-pro-max-skill 86A (2) · anthropics/claude-code 83A (1) | `impeccable` 100/A, `design-taste-frontend` 100/B, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 88A (3) · nextlevelbuilder/ui-ux-pro-max-skill 86A (4) · anthropics/skills 74B (2) | `tailwind-design-system` 96/B, `brand-extract` 94/A, `brandkit` 94/A, `stitch-design-taste` 94/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 88A (7) · calesthio/OpenMontage 74B (2) · greensock/gsap-skills 54C (7) | `emilkowalski-motion` 96/A, `motion-lab` 96/A, `animate` 94/A, `gpt-taste` 94/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 54C (1) · nateherkai/scroll-craft 48D (1) · freshtechbro/claudedesignskills 35D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 62/D, `locomotive-scroll` 62/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 45D (13) · freshtechbro/claudedesignskills 35D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 88A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 59C (69) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 88A (14) · nextlevelbuilder/ui-ux-pro-max-skill 86A (1) · anthropics/claude-plugins-official 76B (1) | `playground` 100/B, `card-twitter` 96/A, `card-xiaohongshu` 96/A, `deck-guizang-editorial` 96/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 88A (3) · microsoft/playwright 84A (2) · addyosmani/agent-skills 84A (1) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 96/A, `impeccable-design-polish` 96/A, `agent-browser` 94/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 84A (8) · obra/superpowers 82A (3) · anthropics/claude-plugins-official 76B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `code-review` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 84A (2) · obra/superpowers 82A (2) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 84A (2) · obra/superpowers 82A (2) · tt-a1i/archify 82A (1) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 84A (2) · vudovn/ag-kit 58C (6) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `frontend-architecture` 83/C, `api-patterns` 76/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 82A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 93A (1) · addyosmani/agent-skills 84A (5) · anthropics/claude-plugins-official 76B (1) | `reverse-engineer-anything` 100/A, `security-and-hardening` 100/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 84A (1) · anthropics/claude-plugins-official 76B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 64C (33) · expo/skills 57C (24) · hamen/compose_skill 37D (2) | `agp-9-upgrade` 99/C, `android-profiler` 99/C, `anr-audit-and-fix` 99/C, `appfunctions` 99/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 88A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 72B (1) | `view-pdf` 100/B, `article-magazine` 96/A, `doc-kami-parchment` 96/A, `resume-modern` 96/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (1) · tt-a1i/archify 82A (1) | `documentation-and-adrs` 100/A, `beautiful-mermaid` 97/B, `d3-visualization` 96/A, `data-report` 96/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 88A (1) · anthropics/skills 74B (1) · vercel-labs/agent-skills 66B (1) | `research-decision-room` 96/A, `writing-guidelines` 88/B, `yt-audit` 84/D, `yt-chapters` 84/D |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 63C (2) · heyitsnoah/claudesidian 38D (13) | `add-frontmatter` 72/D, `json-canvas` 70/D, `obsidian-bases` 70/D, `file-organizer` 69/C |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 76B (4) · anthropics/skills 74B (3) · ComposioHQ/awesome-claude-skills 63C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-integration` 96/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 82A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 91A (1) · Panniantong/Agent-Reach 79B (1) · teng-lin/notebooklm-py 69B (1) | `graphify` 97/A, `agent-reach` 97/B, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 88A (2) · obra/superpowers 82A (1) · anthropics/claude-plugins-official 76B (7) | `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 96/A, `od-next-media-inputs` 96/A |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 82A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 88A (18) · heygen-com/hyperframes 86A (10) · remotion-dev/remotion 77B (13) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | calesthio/OpenMontage 74B (14) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | calesthio/OpenMontage 74B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 88A (2) · heygen-com/hyperframes 86A (3) · calesthio/OpenMontage 74B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `manim-composer` 97/B |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 72B (58) | `account-context` 100/B, `account-plan` 100/B, `account-research` 100/B, `account-tiering` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 72B (26) · Jakeschincariol/day-trader-skill 46D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 72B (69) · Jakeschincariol/founder-skill 42D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 72B (10) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 88A (1) · nexscope-ai/eCommerce-Skills 43D (156) · nexscope-ai/Amazon-Skills 41D (52) | `ecommerce-image-workflow` 94/A, `amazon-review-checker` 83/D, `brand-monitoring` 83/D, `brand-protection-amazon` 83/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 77B (90) · anthropics/knowledge-work-plugins 72B (6) | `13c-metabolic-flux` 100/B, `adaptyv` 100/B, `aeon` 100/B, `alphagenome` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 77B (19) | `astropy` 100/B, `cantera` 100/B, `cirq` 100/B, `fluidsim` 100/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 77B (27) | `dask` 100/B, `exploratory-data-analysis` 100/B, `get-available-resources` 100/B, `hugging-science` 100/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 77B (37) | `autoskill` 100/B, `bgpt-paper-search` 100/B, `citation-management` 100/B, `consciousness-council` 100/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 77B (2) · earthtojake/text-to-cad 70B (12) | `fictiv` 100/B, `lab-hardware-cad` 100/B, `bambu-labs` 100/B, `dfam-check` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 93 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 413111 | 62792.9 | 354 | 5566 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 91 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 139606 | 20113.9 | 378 | 1333 | 2026-10-30 | 🔥 |
| 3 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143229 | 1183.8 | 4180 | 1547 | 2026-10-30 | 🔥 |
| 4 | react/react | 89 A | 0 | - | 0/0/0 | MIT | ✓ | 251804 | 1559.7 | 2028 | 137 | 2026-10-14 |  |
| 5 | nexu-io/open-design | 88 A | 74 | 01-video-uretim-montaj (18), 07-gorsel-sanat-sunum (14) | 73/1/0 | Apache-2.0 |  | 105085 | 17175.2 | 451 | 787 | 2026-10-22 |  |
| 6 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 181095 | 39044.6 | 133 | 163 | 2026-10-29 | 🔥 |
| 7 | heygen-com/hyperframes | 86 A | 13 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 9/4/0 | Apache-2.0 | ✓ | 76165 | 9852.8 | 125 | 2985 | 2026-10-31 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 86 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143127 | 12988.2 | 106 | 79 | 2026-08-13 |  |
| 9 | addyosmani/agent-skills | 84 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112040 | 13201.6 | 96 | 416 | 2026-10-31 | 🔥 |
| 10 | microsoft/playwright | 84 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 98921 | 1183.0 | 827 | 730 | 2026-10-14 |  |
| 11 | anthropics/claude-code | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 153997 | 7599.9 | 59 | 243 | 2026-10-31 | 🔥 |
| 12 | obra/superpowers | 82 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 309572 | 24317.8 | 44 | 6 | 2026-10-21 | 🔥 |
| 13 | tt-a1i/archify | 82 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 91917 | 14041.6 | 92 | 1635 | 2026-10-19 |  |
| 14 | pbakaus/impeccable | 80 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 97389 | 8483.2 | 61 | 1227 | 2026-10-26 | 🔥 |
| 15 | Panniantong/Agent-Reach | 79 B | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 106932 | 13055.2 | 38 | 110 | 2026-10-23 | 🔥 |
| 16 | K-Dense-AI/scientific-agent-skills | 77 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55442 | 4470.7 | 58 | 95 | 2026-10-01 | 🔥 |
| 17 | Leonxlnx/taste-skill | 77 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 106487 | 12744.9 | 24 | 103 | 2026-10-24 | 🔥 |
| 18 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48602 | 293.7 | 639 | 94 | 2026-10-01 |  |
| 19 | remotion-dev/remotion | 77 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 69205 | 906.4 | 478 | 5454 | 2026-10-26 | 🔥 |
| 20 | GoogleChrome/lighthouse | 76 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30987 | 242.2 | 397 | 184 | 2026-10-27 |  |
| 21 | anthropics/claude-plugins-official | 76 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45473 | 4006.9 | 42 | 1889 | - | 🔥 |
| 22 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 185515 | 13959.5 | 17 | 15 | - |  |
| 23 | calesthio/OpenMontage | 74 B | 56 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/12/22 | AGPL-3.0 |  | 73594 | 10357.7 | 76 | 169 | - | 🔥 |
| 24 | anthropics/knowledge-work-plugins | 72 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34085 | 3687.5 | 32 | 605 | - | 🔥 |
| 25 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 34687 | 362.9 | 147 | 1002 | - |  |
| 26 | earthtojake/text-to-cad | 70 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24391 | 3861.9 | 30 | 904 | 2026-10-30 | 🔥 |
| 27 | teng-lin/notebooklm-py | 69 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20017 | 2048.9 | 42 | 701 | 2026-10-29 |  |
| 28 | multica-ai/andrej-karpathy-skills | 68 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 227011 | 24913.8 | 7 | 0 | - |  |
| 29 | vercel-labs/agent-skills | 66 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33275 | 3093.5 | 28 | 23 | 2026-10-27 | 🔥 |
| 30 | cloudflare/security-audit-skill | 65 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 54405 | 12251.2 | 4 | 3 | - | 🔥 |
| 31 | Fei-Away/Codex-Dream-Skin | 64 C | 0 | - | 0/0/0 | MIT |  | 15263 | 4296.3 | 23 | 46 | 2026-10-15 |  |
| 32 | android/skills | 64 C | 33 | 08-mobil-uygulama (33) | 32/1/0 | Apache-2.0 | ✓ | 10114 | 1342.6 | 8 | 39 | 2026-10-29 | 🔥 |
| 33 | ComposioHQ/awesome-claude-skills | 63 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78374 | 6286.5 | 29 | 0 | - |  |
| 34 | lemomo-ai/lemo-opuscar | 63 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 9853 | 8558.0 | 4 | 72 | 2026-10-12 |  |
| 35 | Donchitos/Claude-Code-Game-Studios | 59 C | 69 | 06-oyun-2d-grafik (69) | 69/0/0 | MIT |  | 30533 | 3556.3 | 1 | 5 | 2026-10-19 | 🔥 |
| 36 | cloudflare/skills | 59 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3226 | 301.8 | 48 | 254 | - | 🔥 |
| 37 | vudovn/ag-kit | 58 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 860.1 | 10 | 8 | 2026-08-31 |  |
| 38 | czlonkowski/n8n-skills | 57 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6555 | 530.0 | 7 | 35 | 2026-10-24 | 🔥 |
| 39 | expo/skills | 57 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 3936 | 357.2 | 31 | 51 | - | 🔥 |
| 40 | darkroomengineering/satus | 54 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 210 | 2026-08-28 |  |
| 41 | greensock/gsap-skills | 54 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17605 | 2220.7 | 4 | 0 | - |  |
| 42 | Jakeschincariol/replica-skill | 50 C | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 6695 | 6695.0 | 1 | 1 | - |  |
| 43 | nateherkai/scroll-craft | 48 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4287 | 1861.8 | 1 | 16 | - |  |
| 44 | Jakeschincariol/youtube-agent-skill | 47 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3896 | 2632.0 | 1 | 1 | - |  |
| 45 | Jakeschincariol/day-trader-skill | 46 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 3709 | 3709.0 | 1 | 1 | - |  |
| 46 | Jakeschincariol/instagram-agent-skill | 46 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 3979 | 2520.0 | 1 | 2 | - |  |
| 47 | yaojingang/yao-meta-skill | 46 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2718 | 386.1 | 3 | 56 | - |  |
| 48 | CloudAI-X/threejs-skills | 45 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3875 | 413.3 | 1 | 20 | - |  |
| 49 | ythx-101/live-panel-skill | 44 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 827 | 827.0 | 4 | 40 | - |  |
| 50 | Jakeschincariol/linkedin-agent-skill | 43 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 2962 | 1667.5 | 1 | 1 | - |  |
| 51 | nexscope-ai/eCommerce-Skills | 43 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1304 | 174.6 | 7 | 1 | - |  |
| 52 | Jakeschincariol/founder-skill | 42 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2248 | 2248.0 | 1 | 1 | - |  |
| 53 | nexscope-ai/Amazon-Skills | 41 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 820 | 106.1 | 5 | 1 | - |  |
| 54 | zanwei/design-dna | 40 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2055 | 281.4 | 3 | 4 | - |  |
| 55 | heyitsnoah/claudesidian | 38 D | 18 | 04-not-alma-bilgi-yonetimi (13), 05-git-pr-surum (3) | 17/1/0 | MIT |  | 2607 | 191.4 | 3 | 0 | 2026-04-11 |  |
| 56 | hamen/compose_skill | 37 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 376 | 56.9 | 3 | 0 | 2026-07-07 |  |
| 57 | OrcaQubits/agentic-commerce-skills-plugins | 36 D | 271 | 05-e-ticaret-pazaryeri (271) | 264/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 58 | evanca/flutter-ai-rules | 36 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 665 | 36.3 | 1 | 15 | - |  |
| 59 | lemomo-ai/lemo-wake | 36 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 221 | 221.0 | 1 | 15 | 2026-10-05 |  |
| 60 | freshtechbro/claudedesignskills | 35 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1190 | 97.5 | 1 | 0 | - |  |
| 61 | tuist/fuckingapproachableswiftconcurrency | 35 D | 0 | - | 0/0/0 | MIT |  | 158 | 15.3 | 15 | 0 | - |  |
| 62 | mercadopago/mercadopago-claude-marketplace | 34 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.9 | 10 | 15 | - |  |
| 63 | Livsy90/iOS-Performance-Agent-Skills | 33 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 119 | 22.8 | 2 | 0 | 2026-07-12 |  |
| 64 | xjli360/sealeap-ecommerce-skills | 32 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 115 | 94.5 | 1 | 11 | - |  |
| 65 | ParthJadhav/ios-marketing-capture | 31 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 266 | 39.6 | 1 | 1 | - |  |
| 66 | finsilabs/awesome-ecommerce-skills | 31 D | 175 | 05-e-ticaret-pazaryeri (175) | 157/18/0 | MIT |  | 60 | 7.8 | 4 | 3 | - |  |
| 67 | Viniciuscarvalho/swift-code-reviewer-skill | 28 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.5 | 5 | 0 | 2026-05-07 |  |
| 68 | dadederk/iOS-Accessibility-Agent-Skill | 28 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 175 | 19.1 | 1 | 0 | - |  |
| 69 | MADTeacher/mad-agents-skills | 27 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.6 | 2 | 0 | - |  |
| 70 | Shopify/agent-skills | 27 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 99 | 14.1 | 1 | 0 | - |  |
| 71 | Kappaemme-git/codex-phone-lab | 26 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 17.6 | 1 | 0 | - |  |
| 72 | buluslan/ecommerce-competitor-analyzer | 26 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.7 | 1 | 3 | 2026-01-29 |  |
| 73 | oldred-byte/ec-visual-skill | 25 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 17.2 | 1 | 0 | - |  |
| 74 | Lonsdale201/wp-agent-skills | 24 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.3 | 3 | 29 | - |  |
| 75 | Harishwarrior/flutter-claude-skills | 23 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 67 | 5.5 | 2 | 0 | - |  |
| 76 | mmiani/kotlin-kmp-claude-agent-skills | 22 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.4 | 1 | 8 | - |  |
| 77 | jazzychad/ios-code-audit | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.6 | 1 | 0 | - |  |
| 78 | magendooro/magento-claude-skills | 21 D | 10 | 05-e-ticaret-pazaryeri (10) | 10/0/0 | MIT |  | 15 | 2.1 | 1 | 0 | - |  |
| 79 | arjitj2/swiftui-design-principles | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 33 | 4.0 | 1 | 0 | - |  |
| 80 | lemomo-ai/codex-radar | 19 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 8.0 | 1 | 8 | - |  |
| 81 | Trendyol/trendyol-integration-developer-tool | 18 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.9 | 3 | 0 | - |  |
| 82 | J-DTurner/etsy-api-skill | 15 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.7 | 1 | 0 | - |  |
| 83 | itsncki-design/app-store-submission-auditor | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 34 | 4.6 | 1 | 0 | 2026-03-19 |  |
| 84 | vagabond911/aso-auditor | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 33 | 4.9 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 87 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 80 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `saleor-storefront` 81/D, `web-artifacts-builder` 80/B, `nextjs-react` 79/D, `spree-admin-customization` 79/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 74 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | d3/d3 | 73 B | v7.9 | `d3-viz` 96/B, `d3-visualization` 96/A | tasarim-teknolojileri.md |
| 5 | openai/whisper | 73 B | - | `media-use` 100/A, `speech-to-text` 100/B, `video-understand` 97/B, `azure-speech-to-text` 97/B | kutuphaneler.md |
| 6 | ManimCommunity/manim | 72 B | v0.22 | `manim-composer` 97/B, `manimce-best-practices` 100/B, `manimgl-best-practices` 96/B, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 7 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 80/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 8 | pmndrs/react-three-fiber | 72 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 62/D, `blender-web-pipeline` 62/D, `web3d-integration-patterns` 62/D, `substance-3d-texturing` 54/D, `modern-web-design` 52/D | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 69 B | - | `latex-posters` 100/B, `scientific-writing` 100/B, `manim-composer` 97/B, `sympy` 100/B, `scientific-slides` 100/B, `venue-templates` 100/B, `manimce-best-practices` 100/B | kutuphaneler.md |
| 10 | QwikDev/partytown | 67 B | v1.0 (T5) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 11 | blender/blender | 67 B | - | `blender-web-pipeline` 62/D, `3d-asset-generation` 97/B, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A | kutuphaneler.md |
| 12 | dequelabs/axe-core | 67 B | v4.14 (MPL-2.0) | `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 85/C, `inclusive-design` 81/D, `accessibility` 79/D, `accessibility-commerce` 77/D | tasarim-teknolojileri.md |
| 13 | 666ghj/MiroFish | 66 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 14 | librosa/librosa | 66 B | - | `media-use` 100/A | kutuphaneler.md |
| 15 | Tonejs/Tone.js | 65 B | 15.1 | `sound-effects` 100/B, `music` 100/B | tasarim-teknolojileri.md |
| 16 | pmndrs/drei | 64 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 17 | paperjs/paper.js | 63 C | v0.16 | `algorithmic-art` 71/B, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 18 | DavidHDev/react-bits | 62 C | - | `animated-component-libraries` 62/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 19 | darkroomengineering/lenis | 62 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 62/D | tasarim-teknolojileri.md |
| 20 | fontsource/fontsource | 62 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 21 | ai/size-limit | 60 C | 14.2 (T5) | `react-doctor` 76/C, `nextjs-react-expert` 75/C | tasarim-teknolojileri.md |
| 22 | airbnb/lottie-web | 60 C | v5.13 | `lottie-animations` 62/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 79/D, `rive-interactive` 62/D | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 57 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 97/B | tasarim-teknolojileri.md |
| 24 | opentypejs/opentype.js | 55 C | 2.0 | `svg-character-animation` 97/B, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 25 | liabru/matter-js | 54 C | 0.20 | `pixijs-2d` 70/D, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 54 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `relion` 100/B, `frame-logo-outro` 96/A | tasarim-teknolojileri.md |
| 27 | barvian/number-flow | 50 C | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 28 | rough-stuff/rough | 50 C | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 29 | figma/code-connect | 49 D | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 30 | theatre-js/theatre | 49 D | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 31 | argyleink/open-props | 48 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 32 | seek-oss/capsize | 48 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | greensock/GSAP | 47 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 45 D | v0.20 | `threejs-world-generation` 96/B, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 35 | metafizzy/zdog | 43 D | v1.1 | `svg-character-animation` 97/B, `canvas-procedural-animation` 89/B, `lightweight-3d-effects` 61/D | tasarim-teknolojileri.md |
| 36 | meyda/meyda | 42 D | - | `canvas-procedural-animation` 89/B | kutuphaneler.md |
| 37 | oframe/ogl | 42 D | - | `lightweight-3d-effects` 61/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 38 | zhuyansen/awesome-claude-video-skills | 40 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 39 | 14islands/r3f-scroll-rig | 38 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 62/D, `gpt-taste` 94/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 62/D, `barba-js` 62/D, `locomotive-scroll` 62/D, `scroll-reveal-libraries` 62/D | tasarim-teknolojileri.md |
| 40 | jwagner/simplex-noise.js | 36 D | 4.0 | `algorithmic-art` 71/B, `threejs-shaders` 79/D, `threejs-world-generation` 96/B | tasarim-teknolojileri.md |
| 41 | linvi/tweetinvi | 36 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 42 | nevertoday/350-layout-compositions | 36 D | - | `design-taste-frontend` 100/B, `canvas-design` 79/B, `slides` 82/A | tasarim-teknolojileri.md |
| 43 | pmndrs/react-three-a11y | 35 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 44 | arturitu/the-delegation | 27 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
