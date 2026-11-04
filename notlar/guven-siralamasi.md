# Güven ve Referans Rehberi (agent için)

> Otomatik üretilir (`araclar/katalog-uret.py`, veri: `gelistiriciler.json` 2026-11-04, `registry.json`). **ELLE DÜZENLEME** — her güncellemede yeniden yazılır. Kütüphane: `~/Documents/SkillKutuphanesi` (salt okunur kullan).

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
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 89A (13) · nextlevelbuilder/ui-ux-pro-max-skill 86A (2) · anthropics/claude-code 83A (1) | `impeccable` 100/A, `design-taste-frontend` 100/B, `user-research` 100/B, `accessibility-review` 99/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 89A (3) · nextlevelbuilder/ui-ux-pro-max-skill 86A (4) · anthropics/skills 74B (2) | `tailwind-design-system` 96/B, `brand-extract` 95/A, `brandkit` 95/A, `stitch-design-taste` 95/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 89A (7) · calesthio/OpenMontage 74B (2) · greensock/gsap-skills 52C (7) | `emilkowalski-motion` 97/A, `motion-lab` 97/A, `animate` 95/A, `gpt-taste` 95/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 52C (1) · nateherkai/scroll-craft 44D (1) · freshtechbro/claudedesignskills 30D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 61/D, `locomotive-scroll` 61/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | CloudAI-X/threejs-skills 40D (13) · freshtechbro/claudedesignskills 30D (10) · openai/plugins 28D (2) | `threejs-asset-pipeline` 88/D, `threejs-fundamentals` 88/D, `threejs-lighting` 88/D, `threejs-loaders` 88/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 89A (1) · pixijs/pixijs 76B (26) · Donchitos/Claude-Code-Game-Studios 58C (68) | `estimate` 97/C, `scope-check` 97/C, `hatch-pet` 95/A, `asset-audit` 95/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 89A (14) · nextlevelbuilder/ui-ux-pro-max-skill 86A (1) · anthropics/skills 74B (4) | `playground` 100/B, `card-twitter` 97/A, `card-xiaohongshu` 97/A, `deck-guizang-editorial` 97/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 89A (3) · addyosmani/agent-skills 84A (1) · microsoft/playwright 83A (2) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 97/A, `impeccable-design-polish` 97/A, `agent-browser` 95/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 84A (8) · obra/superpowers 81A (3) · anthropics/claude-plugins-official 74B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `documentation` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 84A (2) · tt-a1i/archify 83A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 84A (2) · tt-a1i/archify 83A (1) · obra/superpowers 81A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 84A (2) · vudovn/ag-kit 53C (6) · github/awesome-copilot 42D (2) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `api-breaking-change-detector` 83/D, `frontend-architecture` 82/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | morluto/rea 93A (1) · addyosmani/agent-skills 84A (5) · anthropics/claude-plugins-official 74B (1) | `security-and-hardening` 100/A, `reverse-engineer-anything` 99/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 89A (6) · microsoft/playwright 83A (1) · anthropics/claude-plugins-official 74B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 60C (37) · expo/skills 52C (24) · hamen/compose_skill 33D (2) | `agp-9-upgrade` 98/C, `android-profiler` 98/C, `anr-audit-and-fix` 98/C, `appfunctions` 98/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 89A (3) · anthropics/skills 74B (4) · anthropics/knowledge-work-plugins 71B (1) | `view-pdf` 100/B, `docx` 98/B, `article-magazine` 97/A, `doc-kami-parchment` 97/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (1) · tt-a1i/archify 83A (1) | `documentation-and-adrs` 100/A, `d3-visualization` 97/A, `data-report` 97/A, `beautiful-mermaid` 97/B |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 89A (1) · anthropics/skills 74B (1) · vercel-labs/agent-skills 65B (1) | `research-decision-room` 97/A, `internal-comms` 90/B, `humanizer` 88/D, `writing-guidelines` 84/B |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 63C (2) · kepano/obsidian-skills 41D (5) · AgriciDaniel/claude-obsidian 34D (11) | `defuddle` 82/D, `knap` 82/D, `obsidian-cli` 82/D, `obsidian-bases@kepano` 80/D |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 74B (4) · anthropics/skills 74B (3) · ComposioHQ/awesome-claude-skills 63C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-builder` 97/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 89A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 91A (1) · Panniantong/Agent-Reach 80A (1) · teng-lin/notebooklm-py 67B (1) | `agent-reach` 98/A, `graphify` 97/A, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 89A (2) · heygen-com/hyperframes 87A (1) · obra/superpowers 81A (1) | `reverse-any-video` 100/A, `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 97/A |
| `e-entegrasyon-katalogu/01-uygulama-entegrasyonlari` — Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Co | github/awesome-copilot 42D (460) · openai/plugins 28D (449) | `acreadiness-assess` 83/D, `acreadiness-policy` 83/D, `add-educational-comments` 83/D, `agentic-eval` 83/D |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 83A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 89A (18) · heygen-com/hyperframes 87A (10) · remotion-dev/remotion 77B (13) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | calesthio/OpenMontage 74B (14) · krillinai/OpenCreator 31D (7) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | calesthio/OpenMontage 74B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 89A (2) · heygen-com/hyperframes 87A (3) · calesthio/OpenMontage 74B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `huashu-art-motion` 97/A |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 71B (58) · coreyhaines31/marketingskills 44D (48) · AgriciDaniel/claude-seo 37D (25) | `account-research` 100/B, `brand-voice-enforcement` 100/B, `call-prep` 100/B, `compose-outreach` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 71B (26) · Jakeschincariol/day-trader-skill 43D (11) | `interview-prep` 100/B, `journal-entry-prep` 100/B, `org-planning` 100/B, `recruiting-pipeline` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 71B (69) · Jakeschincariol/founder-skill 37D (11) | `brand-style` 100/B, `build-agent` 100/B, `call-list` 100/B, `close-month` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 71B (10) | `data-context-extractor` 100/B, `analyze` 99/B, `create-viz` 99/B, `data-visualization` 99/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 89A (1) · nexscope-ai/eCommerce-Skills 39D (156) · 40RTY-ai/shopify-admin-skills 39D (117) | `ecommerce-image-workflow` 95/A, `amazon-review-checker` 82/D, `brand-monitoring` 82/D, `brand-protection-amazon` 82/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 76B (90) · anthropics/knowledge-work-plugins 71B (6) | `scvi-tools` 100/B, `single-cell-rna-qc` 100/B, `cellprofiler` 99/B, `nwb-conversion` 99/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 76B (19) | `pennylane` 99/B, `pybamm` 99/B, `astropy` 97/B, `cantera` 97/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 76B (27) · Orchestra-Research/AI-Research-SKILLs 34D (95) | `vaex` 99/B, `dask` 97/B, `exploratory-data-analysis` 97/B, `get-available-resources` 97/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 76B (37) · wanshuiyin/Auto-claude-code-research-in-sleep 35D (86) | `bgpt-paper-search` 99/B, `autoskill` 97/B, `citation-management` 97/B, `consciousness-council` 97/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 76B (2) · earthtojake/text-to-cad 69B (12) | `bambu-labs` 100/B, `dfam-check` 100/B, `dfm` 100/B, `gcode` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | morluto/rea | 93 A | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT |  | 419002 | 62439.5 | 356 | 5619 | 2026-10-25 | 🔥 |
| 2 | Graphify-Labs/graphify | 91 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 140568 | 19875.7 | 382 | 1385 | 2026-11-01 | 🔥 |
| 3 | nexu-io/open-design | 89 A | 74 | 01-video-uretim-montaj (18), 07-gorsel-sanat-sunum (14) | 73/1/0 | Apache-2.0 |  | 105353 | 16856.5 | 451 | 780 | 2026-10-22 |  |
| 4 | vercel/next.js | 89 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143460 | 1184.5 | 4180 | 1526 | 2026-10-31 | 🔥 |
| 5 | react/react | 88 A | 0 | - | 0/0/0 | MIT | ✓ | 252077 | 1560.1 | 2027 | 137 | 2026-10-14 |  |
| 6 | heygen-com/hyperframes | 87 A | 14 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 8/5/1 | Apache-2.0 | ✓ | 77137 | 9811.6 | 125 | 3039 | 2026-11-02 | 🔥 |
| 7 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 182163 | 38191.4 | 133 | 163 | 2026-10-29 | 🔥 |
| 8 | nextlevelbuilder/ui-ux-pro-max-skill | 86 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143857 | 12900.5 | 107 | 80 | 2026-08-13 |  |
| 9 | addyosmani/agent-skills | 84 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112570 | 13061.6 | 97 | 412 | 2026-10-31 | 🔥 |
| 10 | anthropics/claude-code | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 154176 | 7559.6 | 59 | 243 | 2026-10-31 | 🔥 |
| 11 | microsoft/playwright | 83 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 99065 | 1182.9 | 827 | 729 | 2026-10-14 |  |
| 12 | tt-a1i/archify | 83 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 92406 | 13838.1 | 92 | 1632 | 2026-10-19 |  |
| 13 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 310663 | 24153.8 | 44 | 6 | 2026-10-21 | 🔥 |
| 14 | pbakaus/impeccable | 81 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 99404 | 8560.6 | 62 | 1207 | 2026-10-26 | 🔥 |
| 15 | Panniantong/Agent-Reach | 80 A | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 107638 | 12933.6 | 46 | 138 | 2026-11-01 | 🔥 |
| 16 | Leonxlnx/taste-skill | 78 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 107836 | 12706.3 | 24 | 103 | 2026-10-24 | 🔥 |
| 17 | remotion-dev/remotion | 77 B | 13 | 01-video-uretim-montaj (13) | 11/2/0 | NOASSERTION | ✓ | 69773 | 912.3 | 479 | 5481 | 2026-10-26 | 🔥 |
| 18 | K-Dense-AI/scientific-agent-skills | 76 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55677 | 4442.5 | 58 | 94 | 2026-10-01 | 🔥 |
| 19 | pixijs/pixijs | 76 B | 26 | 06-oyun-2d-grafik (26) | 26/0/0 | MIT | ✓ | 48612 | 293.5 | 639 | 94 | 2026-10-01 |  |
| 20 | GoogleChrome/lighthouse | 75 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30996 | 242.0 | 397 | 185 | 2026-10-27 |  |
| 21 | anthropics/claude-plugins-official | 74 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45728 | 3983.2 | 42 | 1851 | - | 🔥 |
| 22 | anthropics/skills | 74 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 186390 | 13887.9 | 17 | 15 | - | 🔥 |
| 23 | calesthio/OpenMontage | 74 B | 57 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/13/22 | AGPL-3.0 |  | 74392 | 10279.6 | 76 | 162 | - | 🔥 |
| 24 | anthropics/knowledge-work-plugins | 71 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34376 | 3666.8 | 32 | 597 | - | 🔥 |
| 25 | earthtojake/text-to-cad | 69 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24772 | 3842.2 | 31 | 903 | 2026-10-30 | 🔥 |
| 26 | motiondivision/motion | 68 B | 0 | - | 0/0/0 | MIT | ✓ | 34780 | 363.3 | 147 | 1002 | - |  |
| 27 | multica-ai/andrej-karpathy-skills | 68 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 228018 | 24668.1 | 7 | 0 | - | 🔥 |
| 28 | teng-lin/notebooklm-py | 67 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20059 | 2025.9 | 42 | 692 | 2026-10-29 |  |
| 29 | cloudflare/security-audit-skill | 65 B | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 56433 | 12342.2 | 4 | 3 | - | 🔥 |
| 30 | vercel-labs/agent-skills | 65 B | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33361 | 3064.0 | 28 | 23 | 2026-10-27 | 🔥 |
| 31 | ComposioHQ/awesome-claude-skills | 63 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78523 | 6232.6 | 29 | 0 | - |  |
| 32 | Fei-Away/Codex-Dream-Skin | 61 C | 0 | - | 0/0/0 | MIT |  | 15289 | 4149.9 | 23 | 46 | 2026-10-15 |  |
| 33 | android/skills | 60 C | 37 | 08-mobil-uygulama (37) | 36/1/0 | Apache-2.0 | ✓ | 10235 | 1335.4 | 8 | 38 | 2026-10-29 | 🔥 |
| 34 | lemomo-ai/lemo-opuscar | 60 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 10618 | 8276.6 | 4 | 80 | 2026-10-12 |  |
| 35 | Donchitos/Claude-Code-Game-Studios | 58 C | 68 | 06-oyun-2d-grafik (68) | 68/0/0 | MIT |  | 32364 | 3712.7 | 1 | 5 | 2026-10-19 | 🔥 |
| 36 | cloudflare/skills | 55 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3247 | 300.0 | 48 | 256 | - | 🔥 |
| 37 | mattpocock/skills | 54 C | 30 | 01-planlama-metodoloji (30) | 30/0/0 | MIT |  | 313013 | 34728.4 | None | None | - | 🔥 |
| 38 | vudovn/ag-kit | 53 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 848.4 | 10 | 8 | 2026-08-31 |  |
| 39 | czlonkowski/n8n-skills | 52 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6564 | 525.1 | 7 | 35 | 2026-10-24 | 🔥 |
| 40 | expo/skills | 52 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 4011 | 359.7 | 31 | 52 | - | 🔥 |
| 41 | greensock/gsap-skills | 52 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17696 | 2195.7 | 4 | 0 | - |  |
| 42 | darkroomengineering/satus | 51 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 195 | 2026-08-28 |  |
| 43 | JuliusBrussee/caveman | 49 D | 22 | 02-agent-orkestrasyon (22) | 21/1/0 | Apache-2.0 |  | 117484 | 16689.3 | None | None | - |  |
| 44 | Jakeschincariol/replica-skill | 45 D | 11 | 01-planlama-metodoloji (11) | 11/0/0 | MIT |  | 6998 | 6648.1 | 1 | 1 | - |  |
| 45 | nateherkai/scroll-craft | 44 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4370 | 1795.2 | 1 | 16 | - |  |
| 46 | cathrynlavery/diagram-design | 44 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 64968 | 9777.4 | None | None | - |  |
| 47 | coreyhaines31/marketingskills | 44 D | 48 | 01-satis-pazarlama-musteri (48) | 46/2/0 | MIT |  | 58500 | 6069.6 | None | None | - | 🔥 |
| 48 | Jakeschincariol/day-trader-skill | 43 D | 11 | 02-finans-hukuk-ik (11) | 10/1/0 | MIT |  | 4327 | 4327.0 | 1 | 1 | - |  |
| 49 | blader/humanizer | 43 D | 1 | 03-yazi-iletisim-icerik (1) | 1/0/0 | MIT |  | 64788 | 6791.6 | None | None | - | 🔥 |
| 50 | Jakeschincariol/instagram-agent-skill | 42 D | 13 | 03-yazi-iletisim-icerik (13) | 13/0/0 | MIT |  | 4356 | 2546.6 | 1 | 2 | - |  |
| 51 | Jakeschincariol/youtube-agent-skill | 42 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 4169 | 2586.5 | 1 | 1 | - |  |
| 52 | yaojingang/yao-meta-skill | 42 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2719 | 379.2 | 3 | 56 | - |  |
| 53 | github/awesome-copilot | 42 D | 469 | 01-uygulama-entegrasyonlari (460), 02-kod-kalitesi-review (2) | 458/10/1 | MIT |  | 40795 | 2426.9 | None | None | - |  |
| 54 | Nutlope/hallmark | 41 D | 1 | 01-ui-ux-tasarim-dili (1) | 0/1/0 | MIT |  | 47794 | 7607.0 | None | None | - | 🔥 |
| 55 | kepano/obsidian-skills | 41 D | 6 | 04-not-alma-bilgi-yonetimi (5), 02-diyagram-dokumantasyon (1) | 6/0/0 | MIT |  | 50748 | 5041.6 | None | None | - |  |
| 56 | CloudAI-X/threejs-skills | 40 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3908 | 411.1 | 1 | 20 | - |  |
| 57 | ythx-101/live-panel-skill | 40 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 833 | 791.4 | 4 | 40 | - |  |
| 58 | 40RTY-ai/shopify-admin-skills | 39 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 29.5 | 3 | 13 | 2026-06-17 |  |
| 59 | nexscope-ai/eCommerce-Skills | 39 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1312 | 172.7 | 7 | 1 | - |  |
| 60 | Jakeschincariol/linkedin-agent-skill | 38 D | 11 | 03-yazi-iletisim-icerik (11) | 11/0/0 | MIT |  | 3035 | 1590.8 | 1 | 1 | - |  |
| 61 | Jakeschincariol/founder-skill | 37 D | 11 | 03-operasyon-urun-isletme (11) | 11/0/0 | MIT |  | 2324 | 2324.0 | 1 | 1 | - |  |
| 62 | nexscope-ai/Amazon-Skills | 37 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 822 | 104.6 | 5 | 1 | - |  |
| 63 | AgriciDaniel/claude-seo | 37 D | 25 | 01-satis-pazarlama-musteri (25) | 25/0/0 | MIT |  | 26601 | 2995.1 | None | None | - | 🔥 |
| 64 | Vincentwei1021/video-shotcraft | 37 D | 1 | 01-video-uretim-montaj (1) | 1/0/0 | Apache-2.0 |  | 16948 | 4770.5 | None | None | - |  |
| 65 | google/elephant-goldfish-model | 37 D | 7 | 01-planlama-metodoloji (7) | 7/0/0 | Apache-2.0 |  | 11664 | 6819.0 | None | None | - |  |
| 66 | zanwei/design-dna | 35 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2064 | 277.6 | 3 | 4 | - |  |
| 67 | wanshuiyin/Auto-claude-code-research-in-sleep | 35 D | 86 | 04-bilimsel-yazim-literatur (86) | 76/9/1 | MIT |  | 18644 | 2371.5 | None | None | - |  |
| 68 | heyitsnoah/claudesidian | 34 D | 15 | 04-not-alma-bilgi-yonetimi (10), 05-git-pr-surum (3) | 14/1/0 | MIT |  | 2607 | 189.6 | 3 | 0 | 2026-04-11 |  |
| 69 | AgriciDaniel/claude-obsidian | 34 D | 11 | 04-not-alma-bilgi-yonetimi (11) | 11/0/0 | MIT |  | 16164 | 2328.8 | None | None | - |  |
| 70 | Orchestra-Research/AI-Research-SKILLs | 34 D | 97 | 03-veri-bilimi-ml (95), 01-planlama-metodoloji (1) | 82/14/1 | MIT |  | 14267 | 1185.0 | None | None | - |  |
| 71 | Ryze-AI-Adgent/open-seo-mcp-skills | 34 D | 7 | 01-satis-pazarlama-musteri (7) | 7/0/0 | MIT |  | 8802 | 3993.7 | None | None | - |  |
| 72 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 272 | 05-e-ticaret-pazaryeri (272) | 265/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 73 | hamen/compose_skill | 33 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 378 | 56.1 | 3 | 0 | 2026-07-07 |  |
| 74 | xjli360/sealeap-amazon-skills | 33 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 342 | 138.6 | 1 | 15 | - |  |
| 75 | evanca/flutter-ai-rules | 32 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 668 | 36.2 | 1 | 14 | - |  |
| 76 | lemomo-ai/lemo-wake | 32 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 233 | 221.4 | 1 | 15 | 2026-10-05 |  |
| 77 | mercadopago/mercadopago-claude-marketplace | 32 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.8 | 10 | 15 | - |  |
| 78 | dreammis/social-auto-upload | 32 D | 18 | 01-video-uretim-montaj (18) | 18/0/0 | MIT |  | 16117 | 459.6 | None | None | - |  |
| 79 | zubair-trabzada/geo-seo-claude | 32 D | 16 | 01-satis-pazarlama-musteri (16) | 16/0/0 | MIT |  | 11508 | 1350.7 | None | None | - |  |
| 80 | tuist/fuckingapproachableswiftconcurrency | 31 D | 0 | - | 0/0/0 | MIT |  | 158 | 15.2 | 15 | 0 | - |  |
| 81 | AgriciDaniel/claude-ads | 31 D | 34 | 01-satis-pazarlama-musteri (34) | 34/0/0 | MIT |  | 10738 | 1227.2 | None | None | - |  |
| 82 | krillinai/OpenCreator | 31 D | 7 | 02-ses-muzik-konusma (7) | 6/1/0 | Apache-2.0 |  | 14154 | 626.3 | None | None | - |  |
| 83 | freshtechbro/claudedesignskills | 30 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1212 | 98.3 | 1 | 0 | - |  |
| 84 | Livsy90/iOS-Performance-Agent-Skills | 28 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 120 | 22.4 | 2 | 0 | 2026-07-12 |  |
| 85 | finsilabs/awesome-ecommerce-skills | 28 D | 178 | 05-e-ticaret-pazaryeri (178) | 160/18/0 | MIT |  | 61 | 7.8 | 4 | 3 | - |  |
| 86 | xjli360/sealeap-ecommerce-skills | 28 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 119 | 88.2 | 1 | 11 | - |  |
| 87 | openai/plugins | 28 D | 463 | 01-uygulama-entegrasyonlari (449), 06-devops-guvenlik-performans (5) | 436/27/0 | yok | ✓ | 7753 | 962.0 | None | None | - |  |
| 88 | dpconde/claude-android-skill | 27 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 350 | 32.0 | 1 | 0 | - |  |
| 89 | ParthJadhav/ios-marketing-capture | 26 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 265 | 38.7 | 1 | 1 | - |  |
| 90 | Lonsdale201/wp-agent-skills | 23 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.2 | 3 | 29 | - |  |
| 91 | MADTeacher/mad-agents-skills | 23 D | 11 | 08-mobil-uygulama (11) | 11/0/0 | MIT |  | 111 | 11.4 | 2 | 0 | - |  |
| 92 | dadederk/iOS-Accessibility-Agent-Skill | 23 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 176 | 18.9 | 1 | 0 | - |  |
| 93 | Kappaemme-git/codex-phone-lab | 22 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 95 | 17.2 | 1 | 0 | - |  |
| 94 | Shopify/agent-skills | 22 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 100 | 14.0 | 1 | 0 | - |  |
| 95 | buluslan/ecommerce-competitor-analyzer | 22 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.6 | 1 | 3 | 2026-01-29 |  |
| 96 | Harishwarrior/flutter-claude-skills | 21 D | 3 | 08-mobil-uygulama (3) | 3/0/0 | MIT |  | 68 | 5.5 | 2 | 3 | - |  |
| 97 | oldred-byte/ec-visual-skill | 21 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 16.8 | 1 | 0 | - |  |
| 98 | Viniciuscarvalho/swift-code-reviewer-skill | 20 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 39 | 4.4 | 5 | 0 | 2026-05-07 |  |
| 99 | jazzychad/ios-code-audit | 18 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 41 | 7.5 | 1 | 0 | - |  |
| 100 | mmiani/kotlin-kmp-claude-agent-skills | 18 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.2 | 1 | 8 | - |  |
| 101 | Trendyol/trendyol-integration-developer-tool | 17 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.8 | 3 | 0 | - |  |
| 102 | arjitj2/swiftui-design-principles | 17 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 33 | 4.0 | 1 | 0 | - |  |
| 103 | lemomo-ai/codex-radar | 16 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 7.8 | 1 | 8 | - |  |
| 104 | J-DTurner/etsy-api-skill | 14 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.6 | 1 | 0 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 86 A | r186 | `threejs-fundamentals` 88/D, `threejs-geometry` 78/D, `threejs-materials` 78/D, `threejs-lighting` 88/D, `threejs-textures` 80/D, `threejs-loaders` 88/D, `threejs-shaders` 78/D, `threejs-postprocessing` 78/D, `threejs-animation` 80/D, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 79 B | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `web-artifacts-builder` 90/B, `remotion-create` 89/B, `saleor-storefront` 80/D, `nextjs-react` 78/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 73 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | VoltAgent/awesome-design-md | 72 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 5 | ManimCommunity/manim | 71 B | v0.22 | `manim-composer` 97/B, `manimce-best-practices` 100/B, `manimgl-best-practices` 96/B, `remotion-to-hyperframes` 97/A | tasarim-teknolojileri.md |
| 6 | d3/d3 | 71 B | v7.9 | `d3-viz` 96/B, `d3-visualization` 97/A, `d3-data-visualization` 64/D, `geospatial-and-cartographic-visualization` 64/D | tasarim-teknolojileri.md |
| 7 | openai/whisper | 71 B | - | `media-use` 100/A, `speech-to-text` 100/B, `video-understand` 97/B, `azure-speech-to-text` 97/B, `whisper` 80/D, `krillinai-subtitle` 79/D, `twilio-conference-calls` 64/D, `subtitles` 59/D | kutuphaneler.md |
| 8 | pmndrs/react-three-fiber | 70 B | v9.8 | `threejs-react-three-fiber` 86/D, `react-three-fiber` 61/D, `react-three-fiber-game` 66/D, `blender-web-pipeline` 61/D, `web3d-integration-patterns` 61/D, `substance-3d-texturing` 53/D, `modern-web-design` 51/D | tasarim-teknolojileri.md |
| 9 | 666ghj/MiroFish | 66 B | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 10 | KaTeX/KaTeX | 66 B | - | `latex-posters` 97/B, `scientific-writing` 97/B, `manim-composer` 97/B, `manimce-best-practices` 100/B, `sympy` 97/B, `scientific-slides` 97/B, `venue-templates` 97/B, `paper-compile` 78/D | kutuphaneler.md |
| 11 | blender/blender | 65 B | - | `blender-web-pipeline` 61/D, `3d-asset-generation` 97/B, `threejs-loaders` 88/D, `remotion-to-hyperframes` 97/A, `web-3d-asset-pipeline` 66/D | kutuphaneler.md |
| 12 | QwikDev/partytown | 63 C | v1.0 (T5) | `shopify-hydrogen` 49/D | tasarim-teknolojileri.md |
| 13 | Tonejs/Tone.js | 62 C | 15.1 | `sound-effects` 100/B, `music` 100/B | tasarim-teknolojileri.md |
| 14 | dequelabs/axe-core | 62 C | v4.14 (MPL-2.0) | `accessibility-review` 99/B, `frontend-ui-engineering` 98/A, `replica-design` 84/D, `salesforce-component-standards` 81/D, `scoutqa-test` 81/D, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D | tasarim-teknolojileri.md |
| 15 | librosa/librosa | 62 C | - | `media-use` 100/A | kutuphaneler.md |
| 16 | DavidHDev/react-bits | 61 C | - | `animated-component-libraries` 61/D, `frontend-ui-engineering` 98/A | tasarim-teknolojileri.md |
| 17 | paperjs/paper.js | 60 C | v0.16 | `algorithmic-art` 81/B, `canvas-procedural-animation` 88/B | tasarim-teknolojileri.md |
| 18 | darkroomengineering/lenis | 59 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 61/D | tasarim-teknolojileri.md |
| 19 | pmndrs/drei | 59 C | v10.7 | `threejs-react-three-fiber` 86/D | tasarim-teknolojileri.md |
| 20 | airbnb/lottie-web | 58 C | v5.13 | `lottie-animations` 61/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 78/D, `rive-interactive` 61/D | tasarim-teknolojileri.md |
| 21 | fontsource/fontsource | 57 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 22 | ai/size-limit | 56 C | 14.2 (T5) | `react-doctor` 75/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 23 | motion-canvas/motion-canvas | 54 C | v3.17 | `remotion-to-hyperframes` 97/A, `hyperframes` 100/A, `manim-composer` 97/B | tasarim-teknolojileri.md |
| 24 | liabru/matter-js | 52 C | 0.20 | `pixijs-2d` 69/D, `canvas-procedural-animation` 88/B | tasarim-teknolojileri.md |
| 25 | pmndrs/postprocessing | 51 C | v6.39 | `threejs-postprocessing` 78/D, `threejs-shaders` 78/D, `frame-logo-outro` 97/A, `relion` 97/B | tasarim-teknolojileri.md |
| 26 | rough-stuff/rough | 48 D | v3.1 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 27 | greensock/GSAP | 46 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 28 | barvian/number-flow | 45 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 29 | opentypejs/opentype.js | 45 D | 2.0 | `svg-character-animation` 97/B, `hyperframes` 100/A, `pixijs-scene-text` 91/B | tasarim-teknolojileri.md |
| 30 | theatre-js/theatre | 45 D | 0.4 (r3f) | `threejs-animation` 80/D, `gsap-timeline` 87/C | tasarim-teknolojileri.md |
| 31 | figma/code-connect | 44 D | v2.0 | `figma-code-connect` 61/D | tasarim-teknolojileri.md |
| 32 | seek-oss/capsize | 44 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 33 | argyleink/open-props | 43 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 34 | pmndrs/cannon-es | 41 D | v0.20 | `threejs-world-generation` 96/B, `threejs-interaction` 80/D | tasarim-teknolojileri.md |
| 35 | metafizzy/zdog | 38 D | v1.1 | `svg-character-animation` 97/B, `canvas-procedural-animation` 88/B, `lightweight-3d-effects` 60/D | tasarim-teknolojileri.md |
| 36 | meyda/meyda | 38 D | - | `canvas-procedural-animation` 88/B | kutuphaneler.md |
| 37 | oframe/ogl | 37 D | - | `lightweight-3d-effects` 60/D, `threejs-shaders` 78/D | tasarim-teknolojileri.md |
| 38 | zhuyansen/awesome-claude-video-skills | 36 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 39 | 14islands/r3f-scroll-rig | 34 D | v8.15 | `threejs-react-three-fiber` 86/D, `web3d-integration-patterns` 61/D, `gpt-taste` 95/A, `gsap-scrolltrigger` 86/C, `gsap-framer-scroll-animation` 83/D, `scrollytelling-and-parallax-data-visualization` 64/D, `lottie-animations` 61/D, `barba-js` 61/D | tasarim-teknolojileri.md |
| 40 | linvi/tweetinvi | 33 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 41 | jwagner/simplex-noise.js | 32 D | 4.0 | `algorithmic-art` 81/B, `threejs-shaders` 78/D, `threejs-world-generation` 96/B, `google-docs` 59/D | tasarim-teknolojileri.md |
| 42 | nevertoday/350-layout-compositions | 31 D | - | `design-taste-frontend` 100/B, `canvas-design` 89/B, `slides` 82/A | tasarim-teknolojileri.md |
| 43 | pmndrs/react-three-a11y | 31 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 44 | arturitu/the-delegation | 23 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
