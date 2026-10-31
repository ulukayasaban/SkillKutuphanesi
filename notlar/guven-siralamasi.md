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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 89A (13) · nextlevelbuilder/ui-ux-pro-max-skill 86A (2) · anthropics/claude-code 84A (1) | `impeccable` 100/A, `design-taste-frontend` 100/B, `accessibility-review` 100/B, `design-critique` 100/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 89A (3) · nextlevelbuilder/ui-ux-pro-max-skill 86A (4) · anthropics/skills 75B (2) | `tailwind-design-system` 96/B, `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 89A (7) · calesthio/OpenMontage 74B (2) · greensock/gsap-skills 55C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 55C (1) · nateherkai/scroll-craft 49D (1) · freshtechbro/claudedesignskills 36D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 79/D, `barba-js` 62/D, `locomotive-scroll` 62/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 46D (13) · freshtechbro/claudedesignskills 36D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 89A (1) · pixijs/pixijs 77B (26) · Donchitos/Claude-Code-Game-Studios 59C (69) | `estimate` 98/C, `scope-check` 98/C, `asset-audit` 96/C, `help` 96/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 89A (14) · nextlevelbuilder/ui-ux-pro-max-skill 86A (1) · anthropics/claude-plugins-official 76B (1) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 89A (3) · microsoft/playwright 85A (2) · addyosmani/agent-skills 84A (1) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 97/A, `impeccable-design-polish` 97/A, `agent-browser` 95/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 84A (8) · obra/superpowers 82A (3) · anthropics/claude-plugins-official 76B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `code-review` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 84A (2) · tt-a1i/archify 83A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 84A (2) · tt-a1i/archify 83A (1) · obra/superpowers 82A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 84A (2) · vudovn/ag-kit 59C (6) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `frontend-architecture` 84/C, `api-patterns` 77/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 82A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 94A (1) · addyosmani/agent-skills 84A (5) · anthropics/claude-plugins-official 76B (1) | `reverse-engineer-anything` 100/A, `security-and-hardening` 100/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 90A (6) · microsoft/playwright 85A (1) · anthropics/claude-plugins-official 76B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 66B (33) · expo/skills 58C (24) · evanca/flutter-ai-rules 38D (35) | `agp-9-upgrade` 100/B, `android-profiler` 100/B, `anr-audit-and-fix` 100/B, `appfunctions` 100/B |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 89A (3) · anthropics/skills 75B (4) · anthropics/knowledge-work-plugins 73B (1) | `view-pdf` 100/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A, `resume-modern` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (1) · tt-a1i/archify 83A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `beautiful-mermaid` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 89A (1) · anthropics/skills 75B (1) · vercel-labs/agent-skills 67B (1) | `research-decision-room` 97/A, `writing-guidelines` 88/B, `yt-audit` 84/D, `yt-chapters` 84/D |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 63C (2) · heyitsnoah/claudesidian 40D (13) | `add-frontmatter` 72/D, `json-canvas` 71/D, `obsidian-bases` 71/D, `obsidian-markdown` 70/D |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 76B (4) · anthropics/skills 75B (3) · ComposioHQ/awesome-claude-skills 63C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-integration` 96/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 82A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 91A (1) · Panniantong/Agent-Reach 80A (1) · teng-lin/notebooklm-py 70B (1) | `graphify` 97/A, `agent-reach` 97/A, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 89A (2) · obra/superpowers 82A (1) · anthropics/claude-plugins-official 76B (7) | `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 97/A, `od-next-media-inputs` 97/A |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 83A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 89A (18) · heygen-com/hyperframes 87A (10) · remotion-dev/remotion 78B (13) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | calesthio/OpenMontage 74B (14) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | calesthio/OpenMontage 74B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 89A (2) · heygen-com/hyperframes 87A (3) · calesthio/OpenMontage 74B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 73B (58) | `account-context` 100/B, `account-plan` 100/B, `account-research` 100/B, `account-tiering` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 73B (26) · Jakeschincariol/day-trader-skill 47D (11) | `audit-support` 100/B, `brief` 100/B, `close-management` 100/B, `comp-analysis` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 73B (69) · Jakeschincariol/founder-skill 43D (11) | `brand-style` 100/B, `build-agent` 100/B, `business-pulse` 100/B, `call-list` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 73B (10) | `analyze` 100/B, `create-viz` 100/B, `data-context-extractor` 100/B, `data-visualization` 100/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 89A (1) · nexscope-ai/eCommerce-Skills 44D (156) · 40RTY-ai/shopify-admin-skills 43D (117) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 83/D, `brand-monitoring` 83/D, `brand-protection-amazon` 83/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 77B (90) · anthropics/knowledge-work-plugins 73B (6) | `13c-metabolic-flux` 100/B, `adaptyv` 100/B, `aeon` 100/B, `alphagenome` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 77B (19) | `astropy` 100/B, `cantera` 100/B, `cirq` 100/B, `fluidsim` 100/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 77B (27) | `dask` 100/B, `exploratory-data-analysis` 100/B, `get-available-resources` 100/B, `hugging-science` 100/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 77B (37) | `autoskill` 100/B, `bgpt-paper-search` 100/B, `citation-management` 100/B, `consciousness-council` 100/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 77B (2) · earthtojake/text-to-cad 71B (12) | `fictiv` 100/B, `lab-hardware-cad` 100/B, `bambu-labs` 100/B, `dfam-check` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 94 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 413560 | 62861.1 | 355 | 5575 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 91 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 139684 | 20125.1 | 378 | 1333 | 2026-10-30 | 🔥 |
| 3 | vercel/next.js | 90 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143252 | 1184.0 | 4180 | 1548 | 2026-10-31 | 🔥 |
| 4 | nexu-io/open-design | 89 A | 74 | 01-video-uretim-montaj (18), 07-gorsel-sanat-sunum (14) | 73/1/0 | Apache-2.0 |  | 105114 | 17179.9 | 451 | 787 | 2026-10-22 |  |
| 5 | react/react | 89 A | 0 | - | 0/0/0 | MIT | ✓ | 251827 | 1559.8 | 2028 | 138 | 2026-10-14 |  |
| 6 | heygen-com/hyperframes | 87 A | 13 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 9/4/0 | Apache-2.0 | ✓ | 76226 | 9860.7 | 125 | 2985 | 2026-10-31 | 🔥 |
| 7 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 181184 | 39063.8 | 133 | 163 | 2026-10-29 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 86 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143178 | 12992.9 | 106 | 79 | 2026-08-13 |  |
| 9 | microsoft/playwright | 85 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 98926 | 1183.1 | 827 | 730 | 2026-10-14 |  |
| 10 | addyosmani/agent-skills | 84 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112071 | 13205.3 | 97 | 416 | 2026-10-31 | 🔥 |
| 11 | anthropics/claude-code | 84 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154010 | 7600.5 | 59 | 243 | 2026-10-31 | 🔥 |
| 12 | tt-a1i/archify | 83 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 91956 | 14047.5 | 92 | 1635 | 2026-10-19 |  |
| 13 | obra/superpowers | 82 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 309660 | 24324.7 | 44 | 6 | 2026-10-21 | 🔥 |
| 14 | Panniantong/Agent-Reach | 80 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 107001 | 13063.6 | 38 | 110 | 2026-10-23 | 🔥 |
| 15 | pbakaus/impeccable | 80 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 97551 | 8497.3 | 62 | 1227 | 2026-10-26 | 🔥 |
| 16 | Leonxlnx/taste-skill | 78 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 106570 | 12754.8 | 24 | 103 | 2026-10-24 | 🔥 |
| 17 | remotion-dev/remotion | 78 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 69242 | 906.9 | 479 | 5477 | 2026-10-26 | 🔥 |
| 18 | GoogleChrome/lighthouse | 77 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30988 | 242.2 | 397 | 184 | 2026-10-27 |  |
| 19 | K-Dense-AI/scientific-agent-skills | 77 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55463 | 4472.3 | 58 | 95 | 2026-10-01 | 🔥 |
| 20 | pixijs/pixijs | 77 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48602 | 293.7 | 639 | 94 | 2026-10-01 |  |
| 21 | anthropics/claude-plugins-official | 76 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45489 | 4008.3 | 42 | 1889 | - | 🔥 |
| 22 | anthropics/skills | 75 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 185604 | 13966.2 | 17 | 15 | - |  |
| 23 | calesthio/OpenMontage | 74 B | 56 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/12/22 | AGPL-3.0 |  | 73673 | 10368.8 | 76 | 169 | - | 🔥 |
| 24 | anthropics/knowledge-work-plugins | 73 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34101 | 3689.2 | 32 | 605 | - | 🔥 |
| 25 | motiondivision/motion | 72 B | 0 | - | 0/0/0 | MIT | ✓ | 34691 | 362.9 | 147 | 1002 | - |  |
| 26 | earthtojake/text-to-cad | 71 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24404 | 3864.0 | 30 | 904 | 2026-10-30 | 🔥 |
| 27 | teng-lin/notebooklm-py | 70 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20019 | 2049.1 | 42 | 701 | 2026-10-29 |  |
| 28 | multica-ai/andrej-karpathy-skills | 68 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 227090 | 24922.5 | 7 | 0 | - |  |
| 29 | vercel-labs/agent-skills | 67 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33279 | 3093.8 | 28 | 23 | 2026-10-27 | 🔥 |
| 30 | android/skills | 66 B | 33 | 08-mobil-uygulama (33) | 32/1/0 | Apache-2.0 | ✓ | 10127 | 1344.4 | 8 | 39 | 2026-10-29 | 🔥 |
| 31 | cloudflare/security-audit-skill | 66 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 54582 | 12291.1 | 4 | 3 | - | 🔥 |
| 32 | Fei-Away/Codex-Dream-Skin | 65 B | 0 | - | 0/0/0 | MIT |  | 15263 | 4296.3 | 23 | 46 | 2026-10-15 |  |
| 33 | lemomo-ai/lemo-opuscar | 64 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 9902 | 8600.6 | 4 | 72 | 2026-10-12 |  |
| 34 | ComposioHQ/awesome-claude-skills | 63 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78386 | 6287.4 | 29 | 0 | - |  |
| 35 | cloudflare/skills | 61 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3226 | 301.8 | 48 | 254 | - | 🔥 |
| 36 | Donchitos/Claude-Code-Game-Studios | 59 C | 69 | 06-oyun-2d-grafik (69) | 69/0/0 | MIT |  | 30601 | 3564.3 | 1 | 5 | 2026-10-19 | 🔥 |
| 37 | vudovn/ag-kit | 59 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 860.1 | 10 | 8 | 2026-08-31 |  |
| 38 | czlonkowski/n8n-skills | 58 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6554 | 529.9 | 7 | 35 | 2026-10-24 | 🔥 |
| 39 | expo/skills | 58 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 3961 | 359.4 | 31 | 51 | - | 🔥 |
| 40 | darkroomengineering/satus | 56 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 210 | 2026-08-28 |  |
| 41 | greensock/gsap-skills | 55 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17608 | 2221.1 | 4 | 0 | - |  |
| 42 | Jakeschincariol/replica-skill | 50 C | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 6714 | 6714.0 | 1 | 1 | - |  |
| 43 | nateherkai/scroll-craft | 49 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4294 | 1864.8 | 1 | 16 | - |  |
| 44 | Jakeschincariol/youtube-agent-skill | 48 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3915 | 2644.8 | 1 | 1 | - |  |
| 45 | yaojingang/yao-meta-skill | 48 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2718 | 386.1 | 3 | 56 | - |  |
| 46 | Jakeschincariol/day-trader-skill | 47 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 3762 | 3762.0 | 1 | 1 | - |  |
| 47 | Jakeschincariol/instagram-agent-skill | 47 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4012 | 2540.9 | 1 | 2 | - |  |
| 48 | CloudAI-X/threejs-skills | 46 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3878 | 413.7 | 1 | 20 | - |  |
| 49 | ythx-101/live-panel-skill | 45 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 828 | 828.0 | 4 | 40 | - |  |
| 50 | Jakeschincariol/linkedin-agent-skill | 44 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 2965 | 1669.2 | 1 | 1 | - |  |
| 51 | nexscope-ai/eCommerce-Skills | 44 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1304 | 174.6 | 7 | 1 | - |  |
| 52 | 40RTY-ai/shopify-admin-skills | 43 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 200 | 30.0 | 3 | 13 | 2026-06-17 |  |
| 53 | Jakeschincariol/founder-skill | 43 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2255 | 2255.0 | 1 | 1 | - |  |
| 54 | nexscope-ai/Amazon-Skills | 42 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 820 | 106.1 | 5 | 1 | - |  |
| 55 | zanwei/design-dna | 41 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2056 | 281.5 | 3 | 4 | - |  |
| 56 | heyitsnoah/claudesidian | 40 D | 18 | 04-not-alma-bilgi-yonetimi (13), 05-git-pr-surum (3) | 17/1/0 | MIT |  | 2607 | 191.4 | 3 | 0 | 2026-04-11 |  |
| 57 | evanca/flutter-ai-rules | 38 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 665 | 36.3 | 1 | 15 | - |  |
| 58 | hamen/compose_skill | 38 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 376 | 56.9 | 3 | 0 | 2026-07-07 |  |
| 59 | xjli360/sealeap-amazon-skills | 38 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 339 | 145.1 | 1 | 15 | - |  |
| 60 | lemomo-ai/lemo-wake | 37 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 221 | 221.0 | 1 | 15 | 2026-10-05 |  |
| 61 | OrcaQubits/agentic-commerce-skills-plugins | 36 D | 271 | 05-e-ticaret-pazaryeri (271) | 264/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 62 | freshtechbro/claudedesignskills | 36 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1191 | 97.6 | 1 | 0 | - |  |
| 63 | tuist/fuckingapproachableswiftconcurrency | 35 D | 0 | - | 0/0/0 | MIT |  | 158 | 15.3 | 15 | 0 | - |  |
| 64 | mercadopago/mercadopago-claude-marketplace | 34 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.9 | 10 | 15 | - |  |
| 65 | Livsy90/iOS-Performance-Agent-Skills | 32 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 119 | 22.8 | 2 | 0 | 2026-07-12 |  |
| 66 | dpconde/claude-android-skill | 32 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 349 | 32.3 | 1 | 0 | - |  |
| 67 | xjli360/sealeap-ecommerce-skills | 32 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 115 | 94.5 | 1 | 11 | - |  |
| 68 | ParthJadhav/ios-marketing-capture | 31 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 266 | 39.6 | 1 | 1 | - |  |
| 69 | finsilabs/awesome-ecommerce-skills | 31 D | 175 | 05-e-ticaret-pazaryeri (175) | 157/18/0 | MIT |  | 60 | 7.8 | 4 | 3 | - |  |
| 70 | Viniciuscarvalho/swift-code-reviewer-skill | 28 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.5 | 5 | 0 | 2026-05-07 |  |
| 71 | MADTeacher/mad-agents-skills | 27 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.6 | 2 | 0 | - |  |
| 72 | dadederk/iOS-Accessibility-Agent-Skill | 27 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 175 | 19.1 | 1 | 0 | - |  |
| 73 | Kappaemme-git/codex-phone-lab | 26 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 17.6 | 1 | 0 | - |  |
| 74 | Shopify/agent-skills | 26 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 99 | 14.1 | 1 | 0 | - |  |
| 75 | buluslan/ecommerce-competitor-analyzer | 26 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.7 | 1 | 3 | 2026-01-29 |  |
| 76 | Harishwarrior/flutter-claude-skills | 25 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 68 | 5.5 | 2 | 3 | - |  |
| 77 | Lonsdale201/wp-agent-skills | 25 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.3 | 3 | 29 | - |  |
| 78 | oldred-byte/ec-visual-skill | 25 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 17.2 | 1 | 0 | - |  |
| 79 | mmiani/kotlin-kmp-claude-agent-skills | 22 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.4 | 1 | 8 | - |  |
| 80 | jazzychad/ios-code-audit | 21 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.6 | 1 | 0 | - |  |
| 81 | magendooro/magento-claude-skills | 21 D | 10 | 05-e-ticaret-pazaryeri (10) | 10/0/0 | MIT |  | 15 | 2.1 | 1 | 0 | - |  |
| 82 | arjitj2/swiftui-design-principles | 19 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 33 | 4.0 | 1 | 0 | - |  |
| 83 | lemomo-ai/codex-radar | 19 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 8.0 | 1 | 8 | - |  |
| 84 | Trendyol/trendyol-integration-developer-tool | 18 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.9 | 3 | 0 | - |  |
| 85 | J-DTurner/etsy-api-skill | 15 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.7 | 1 | 0 | - |  |
| 86 | vagabond911/aso-auditor | 15 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 33 | 4.9 | 1 | 1 | - |  |
| 87 | itsncki-design/app-store-submission-auditor | 14 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 34 | 4.6 | 1 | 0 | 2026-03-19 |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 88 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 80 A | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 77/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `saleor-storefront` 81/D, `web-artifacts-builder` 80/B, `nextjs-react` 79/D, `spree-admin-customization` 79/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 74 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | ManimCommunity/manim | 73 B | v0.22 | `manim-composer` 97/B, `manimce-best-practices` 100/B, `manimgl-best-practices` 96/B, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 5 | d3/d3 | 73 B | v7.9 | `d3-viz` 96/B, `d3-visualization` 97/A | tasarim-teknolojileri.md |
| 6 | openai/whisper | 73 B | - | `media-use` 100/A, `speech-to-text` 100/B, `video-understand` 97/B, `azure-speech-to-text` 97/B | kutuphaneler.md |
| 7 | pmndrs/react-three-fiber | 73 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 62/D, `blender-web-pipeline` 62/D, `web3d-integration-patterns` 62/D, `substance-3d-texturing` 54/D, `modern-web-design` 53/D | tasarim-teknolojileri.md |
| 8 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 80/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 9 | KaTeX/KaTeX | 70 B | - | `latex-posters` 100/B, `scientific-writing` 100/B, `manim-composer` 97/B, `sympy` 100/B, `scientific-slides` 100/B, `venue-templates` 100/B, `manimce-best-practices` 100/B | kutuphaneler.md |
| 10 | QwikDev/partytown | 68 B | v1.0 (T5) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 11 | blender/blender | 68 B | - | `blender-web-pipeline` 62/D, `3d-asset-generation` 97/B, `threejs-loaders` 89/D, `remotion-to-hyperframes` 97/A | kutuphaneler.md |
| 12 | dequelabs/axe-core | 68 B | v4.14 (MPL-2.0) | `accessibility-review` 100/B, `frontend-ui-engineering` 98/A, `replica-design` 85/C, `inclusive-design` 81/D, `accessibility` 79/D, `accessibility-commerce` 77/D | tasarim-teknolojileri.md |
| 13 | librosa/librosa | 67 B | - | `media-use` 100/A | kutuphaneler.md |
| 14 | 666ghj/MiroFish | 66 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 15 | Tonejs/Tone.js | 66 B | 15.1 | `sound-effects` 100/B, `music` 100/B | tasarim-teknolojileri.md |
| 16 | paperjs/paper.js | 64 C | v0.16 | `algorithmic-art` 71/B, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 17 | pmndrs/drei | 64 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 18 | DavidHDev/react-bits | 63 C | - | `animated-component-libraries` 62/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 19 | darkroomengineering/lenis | 63 C | v1.3 | `scroll-craft` 79/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 62/D | tasarim-teknolojileri.md |
| 20 | fontsource/fontsource | 63 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 21 | ai/size-limit | 61 C | 14.2 (T5) | `nextjs-react-expert` 76/C, `react-doctor` 76/C | tasarim-teknolojileri.md |
| 22 | airbnb/lottie-web | 61 C | v5.13 | `lottie-animations` 62/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 79/D, `rive-interactive` 62/D | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 58 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 97/B | tasarim-teknolojileri.md |
| 24 | liabru/matter-js | 55 C | 0.20 | `pixijs-2d` 70/D, `canvas-procedural-animation` 89/B | tasarim-teknolojileri.md |
| 25 | opentypejs/opentype.js | 55 C | 2.0 | `svg-character-animation` 97/B, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 26 | pmndrs/postprocessing | 55 C | v6.39 | `threejs-postprocessing` 79/D, `threejs-shaders` 79/D, `relion` 100/B, `frame-logo-outro` 97/A | tasarim-teknolojileri.md |
| 27 | barvian/number-flow | 51 C | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 28 | rough-stuff/rough | 51 C | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 29 | figma/code-connect | 50 C | v2.0 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 30 | theatre-js/theatre | 50 C | 0.4 (r3f) | `threejs-animation` 81/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 31 | seek-oss/capsize | 49 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 32 | argyleink/open-props | 48 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | greensock/GSAP | 48 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 46 D | v0.20 | `threejs-world-generation` 96/B, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 35 | metafizzy/zdog | 43 D | v1.1 | `svg-character-animation` 97/B, `canvas-procedural-animation` 89/B, `lightweight-3d-effects` 61/D | tasarim-teknolojileri.md |
| 36 | meyda/meyda | 43 D | - | `canvas-procedural-animation` 89/B | kutuphaneler.md |
| 37 | oframe/ogl | 43 D | - | `lightweight-3d-effects` 61/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 38 | zhuyansen/awesome-claude-video-skills | 42 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 39 | 14islands/r3f-scroll-rig | 39 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 62/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 62/D, `barba-js` 62/D, `locomotive-scroll` 62/D, `scroll-reveal-libraries` 62/D | tasarim-teknolojileri.md |
| 40 | jwagner/simplex-noise.js | 37 D | 4.0 | `algorithmic-art` 71/B, `threejs-shaders` 79/D, `threejs-world-generation` 96/B | tasarim-teknolojileri.md |
| 41 | linvi/tweetinvi | 37 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 42 | nevertoday/350-layout-compositions | 37 D | - | `design-taste-frontend` 100/B, `canvas-design` 79/B, `slides` 82/A | tasarim-teknolojileri.md |
| 43 | pmndrs/react-three-a11y | 35 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 44 | arturitu/the-delegation | 29 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
