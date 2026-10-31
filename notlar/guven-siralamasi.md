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
| Kaynak güveni D | Sadece benzersiz bir iş yapıyorsa, SKILL.md'yi okuduktan sonra, kullanıcıya "düşük güven" diye işaretleyerek |
| Skill puanı < 50 ya da `kalite 1` (yönlendirme) | Alma |
| Aynı işi yapan iki aday | Önce skill puanı, eşitse kaynak güveni (sıra) yüksek olan; 🔥 trend eşitlikte öne geçirir |
| Projede bir referans kütüphanesi kullanılıyor (bölüm 3) | O kütüphanenin "ilgili skiller"i öncelikli aday; skill'in anlattığı sürüm projedekine uymalı |
| Ücret: 💲 ücretli | Ücret ödemeden kullanılamaz; sadece açıkça gerekiyorsa ve kullanıcıya belirterek |
| Lisans `yok`/`NOASSERTION` | Ticari projede kullanıcıya işaretle |

Skill kurulumu SADECE `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> … --kuru` → onay → `--evet`. Bir skill'in ayrıntısı: `KATALOG.md`, `registry.json` (id ile), SKILL.md (`registry.json` → `yol`).

## 1. Kategoriye göre en güvenilir kaynaklar ve en iyi skiller

| Kategori | En güvenilir kaynaklar (güven · o kategorideki skill) | En yüksek puanlı skiller (`id` puan/kaynak derecesi) |
|---|---|---|
| `a-tasarim-onyuz/01-ui-ux-tasarim-dili` — Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış' | nexu-io/open-design 88A (18) · nextlevelbuilder/ui-ux-pro-max-skill 85A (2) · anthropics/claude-code 83A (1) | `impeccable` 100/B, `design-taste-frontend` 100/B, `user-research` 100/B, `accessibility-review` 99/B |
| `a-tasarim-onyuz/02-tasarim-sistemi-marka` — Design token, tema, marka kimliği, banner/logo | nexu-io/open-design 88A (17) · nextlevelbuilder/ui-ux-pro-max-skill 85A (4) · anthropics/skills 73B (2) | `tailwind-design-system` 96/B, `brand-extract` 94/A, `brandkit` 94/A, `stitch-design-taste` 94/A |
| `a-tasarim-onyuz/03-animasyon-motion` — GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | nexu-io/open-design 88A (8) · calesthio/OpenMontage 72B (2) · greensock/gsap-skills 53C (7) | `emilkowalski-motion` 96/A, `motion-lab` 96/A, `animate` 94/A, `gpt-taste` 94/A |
| `a-tasarim-onyuz/04-scroll-deneyimi` — Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişle | greensock/gsap-skills 53C (1) · nateherkai/scroll-craft 46D (1) · freshtechbro/claudedesignskills 34D (3) | `gsap-scrolltrigger` 86/C, `scroll-craft` 78/D, `barba-js` 62/D, `locomotive-scroll` 62/D |
| `a-tasarim-onyuz/05-3d-webgl` — Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, We | nexu-io/open-design 88A (2) · CloudAI-X/threejs-skills 44D (13) · freshtechbro/claudedesignskills 34D (10) | `threejs-asset-pipeline` 89/D, `threejs-fundamentals` 89/D, `threejs-lighting` 89/D, `threejs-loaders` 89/D |
| `a-tasarim-onyuz/06-oyun-2d-grafik` — Oyun geliştirme, PixiJS, 2D grafik | nexu-io/open-design 88A (1) · Donchitos/Claude-Code-Game-Studios 56C (69) · vudovn/ag-kit 55C (11) | `estimate` 97/C, `scope-check` 97/C, `asset-audit` 95/C, `help` 95/C |
| `a-tasarim-onyuz/07-gorsel-sanat-sunum` — Poster/canvas tasarımı, generative art, slayt, GIF | nexu-io/open-design 88A (17) · nextlevelbuilder/ui-ux-pro-max-skill 85A (1) · anthropics/claude-plugins-official 75B (1) | `playground` 100/B, `card-twitter` 96/A, `card-xiaohongshu` 96/A, `deck-guizang-editorial` 96/A |
| `a-tasarim-onyuz/08-onyuz-test-kalite` — Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığ | nexu-io/open-design 88A (7) · microsoft/playwright 84A (2) · addyosmani/agent-skills 84A (1) | `browser-testing-with-devtools` 98/A, `export-download-debugging` 96/A, `impeccable-design-polish` 96/A, `agent-browser` 94/A |
| `b-yazilim-gelistirme/01-planlama-metodoloji` — Fikir geliştirme, spec, plan yazma, görev bölme, uygulama di | addyosmani/agent-skills 84A (8) · obra/superpowers 81A (3) · anthropics/claude-plugins-official 75B (3) | `brainstorming` 100/A, `writing-plans` 100/A, `math-olympiad` 100/B, `documentation` 100/B |
| `b-yazilim-gelistirme/02-kod-kalitesi-review` — Code review, sadeleştirme, temiz kod | DietrichGebert/ponytail 86A (6) · addyosmani/agent-skills 84A (2) · tt-a1i/archify 82A (1) | `ponytail` 100/A, `ponytail-audit` 100/A, `ponytail-debt` 100/A, `ponytail-gain` 100/A |
| `b-yazilim-gelistirme/03-test-hata-ayiklama` — TDD, hata ayıklama, doğrulama | addyosmani/agent-skills 84A (2) · tt-a1i/archify 82A (1) · obra/superpowers 81A (2) | `test-driven-development` 100/A, `systematic-debugging` 100/A, `verification-before-completion` 100/A, `debugging-and-error-recovery` 98/A |
| `b-yazilim-gelistirme/04-mimari-api-veritabani` — Mimari, API/arayüz tasarımı, veritabanı, backend | addyosmani/agent-skills 84A (2) · vudovn/ag-kit 55C (6) | `api-and-interface-design` 100/A, `frontend-ui-engineering` 98/A, `frontend-architecture` 82/C, `api-patterns` 76/C |
| `b-yazilim-gelistirme/05-git-pr-surum` — Git, worktree, PR, sürüm/release, changelog | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (2) | `git-workflow-and-versioning` 100/A, `finishing-a-development-branch` 100/A, `using-git-worktrees` 100/A, `deprecation-and-migration` 98/A |
| `b-yazilim-gelistirme/06-devops-guvenlik-performans` — CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | addyosmani/agent-skills 84A (5) · anthropics/claude-plugins-official 75B (1) · vercel-labs/agent-skills 64C (3) | `security-and-hardening` 100/A, `ci-cd-and-automation` 98/A, `observability-and-instrumentation` 98/A, `performance-optimization` 98/A |
| `b-yazilim-gelistirme/07-framework-ozel` — Belirli framework/araç rehberleri (Next.js, Playwright CLI,  | vercel/next.js 91A (6) · microsoft/playwright 84A (1) · anthropics/claude-plugins-official 75B (2) | `next-cache-components-adoption` 100/A, `next-cache-components-optimizer` 100/A, `next-dev-loop` 100/A, `next-partial-prefetching-adoption` 100/A |
| `b-yazilim-gelistirme/08-mobil-uygulama` — Android (Jetpack Compose, Play), Expo / React Native, iOS; m | android/skills 63C (33) · expo/skills 56C (24) · evanca/flutter-ai-rules 35D (35) | `agp-9-upgrade` 99/C, `android-profiler` 99/C, `anr-audit-and-fix` 99/C, `appfunctions` 99/C |
| `c-dokuman-icerik/01-ofis-dokumanlari` — Word, Excel, PowerPoint, PDF üretme/düzenleme | nexu-io/open-design 88A (6) · anthropics/skills 73B (4) · anthropics/knowledge-work-plugins 71B (1) | `view-pdf` 100/B, `article-magazine` 96/A, `doc-kami-parchment` 96/A, `resume-modern` 96/A |
| `c-dokuman-icerik/02-diyagram-dokumantasyon` — Diyagram, teknik dokümantasyon, ADR, ortak yazım | nexu-io/open-design 88A (2) · addyosmani/agent-skills 84A (1) · tt-a1i/archify 82A (1) | `documentation-and-adrs` 100/A, `beautiful-mermaid` 97/B, `d3-visualization` 96/A, `data-report` 96/A |
| `c-dokuman-icerik/03-yazi-iletisim-icerik` — Yazı, iletişim, pazarlama/içerik, kariyer | nexu-io/open-design 88A (5) · anthropics/skills 73B (1) · vercel-labs/agent-skills 64C (1) | `research-decision-room` 96/A, `writing-guidelines` 87/C, `internal-comms` 80/B, `geo-fundamentals` 76/C |
| `c-dokuman-icerik/04-not-alma-bilgi-yonetimi` — Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | ComposioHQ/awesome-claude-skills 61C (2) · heyitsnoah/claudesidian 38D (13) | `add-frontmatter` 72/D, `json-canvas` 70/D, `obsidian-bases` 70/D, `obsidian-markdown` 69/D |
| `d-ai-otomasyon/01-claude-api-mcp` — Claude API, MCP sunucusu, model geçişi | anthropics/claude-plugins-official 75B (4) · anthropics/skills 73B (3) · ComposioHQ/awesome-claude-skills 61C (3) | `build-mcp-app` 100/B, `build-mcp-server` 100/B, `build-mcpb` 100/B, `mcp-integration` 95/B |
| `d-ai-otomasyon/02-agent-orkestrasyon` — Alt-agent, paralel agent, bağlam mühendisliği, agent davranı | nexu-io/open-design 88A (3) · addyosmani/agent-skills 84A (2) · obra/superpowers 81A (4) | `context-engineering` 100/A, `dispatching-parallel-agents` 100/A, `subagent-driven-development` 100/A, `claude-md-improver` 100/B |
| `d-ai-otomasyon/03-web-arastirma-veri` — Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | Graphify-Labs/graphify 91A (1) · Panniantong/Agent-Reach 79B (1) · teng-lin/notebooklm-py 68B (1) | `graphify` 97/A, `agent-reach` 97/B, `notebooklm` 85/B |
| `d-ai-otomasyon/04-skill-plugin-yazimi` — Skill yazma, plugin/hook/komut geliştirme | nexu-io/open-design 88A (2) · obra/superpowers 81A (1) · anthropics/claude-plugins-official 75B (7) | `writing-skills` 100/A, `agent-development` 100/B, `library-curator` 96/A, `od-next-media-inputs` 96/A |
| `f-repo-ici/01-repo-gelistirici-skilleri` — Next.js, React, Playwright, Lighthouse, Motion repolarına KA | tt-a1i/archify 82A (2) | `archify-review` 72/A, `archify-tuning` 71/A |
| `g-video-ses-medya/01-video-uretim-montaj` — Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı,  | nexu-io/open-design 88A (20) · heygen-com/hyperframes 86A (10) · calesthio/OpenMontage 72B (11) | `captions-overlay` 100/A, `hyperframes` 100/A, `hyperframes-cli` 100/A, `media-use` 100/A |
| `g-video-ses-medya/02-ses-muzik-konusma` — Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti | nexu-io/open-design 88A (4) · calesthio/OpenMontage 72B (14) | `elevenlabs` 100/B, `lyria` 100/B, `music` 100/B, `sound-effects` 100/B |
| `g-video-ses-medya/03-ai-gorsel-video-modelleri` — AI görsel/video model sağlayıcıları (Kling, Seedance, Flux,  | nexu-io/open-design 88A (22) · calesthio/OpenMontage 72B (17) | `bfl-api` 100/B, `flux-best-practices` 100/B, `gemini-omni` 100/B, `seedance-2-0` 100/B |
| `g-video-ses-medya/04-motion-graphics-karakter` — Motion graphics, Manim, karakter animasyonu/rig, görsel stil | nexu-io/open-design 88A (2) · heygen-com/hyperframes 86A (3) · calesthio/OpenMontage 72B (10) | `cut-the-curve` 100/A, `manimce-best-practices` 100/B, `motion-doctrine` 98/A, `manim-composer` 97/B |
| `h-is-alanlari/01-satis-pazarlama-musteri` — Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışla | anthropics/knowledge-work-plugins 71B (58) | `account-research` 100/B, `brand-voice-enforcement` 100/B, `call-prep` 100/B, `compose-outreach` 100/B |
| `h-is-alanlari/02-finans-hukuk-ik` — Finans/muhasebe, hukuk/sözleşme, insan kaynakları | anthropics/knowledge-work-plugins 71B (26) | `interview-prep` 100/B, `journal-entry-prep` 100/B, `org-planning` 100/B, `recruiting-pipeline` 100/B |
| `h-is-alanlari/03-operasyon-urun-isletme` — Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsa | anthropics/knowledge-work-plugins 71B (69) | `brand-style` 100/B, `build-agent` 100/B, `call-list` 100/B, `close-month` 100/B |
| `h-is-alanlari/04-veri-analizi-raporlama` — İş verisi analizi, SQL, pano/rapor, öngörü | anthropics/knowledge-work-plugins 71B (10) | `data-context-extractor` 100/B, `analyze` 99/B, `create-viz` 99/B, `data-visualization` 99/B |
| `h-is-alanlari/05-e-ticaret-pazaryeri` — E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerc | nexu-io/open-design 88A (1) · nexscope-ai/eCommerce-Skills 42D (156) · nexscope-ai/Amazon-Skills 40D (52) | `ecommerce-image-workflow` 94/A, `amazon-review-checker` 83/D, `brand-monitoring` 83/D, `brand-protection-amazon` 83/D |
| `i-bilim-muhendislik/01-yasam-bilimleri-kimya` — Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, l | K-Dense-AI/scientific-agent-skills 75B (90) · anthropics/knowledge-work-plugins 71B (6) | `13c-metabolic-flux` 100/B, `adaptyv` 100/B, `aeon` 100/B, `alphagenome` 100/B |
| `i-bilim-muhendislik/02-fizik-kuantum-malzeme` — Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | K-Dense-AI/scientific-agent-skills 75B (19) | `astropy` 100/B, `cantera` 100/B, `cirq` 100/B, `fluidsim` 100/B |
| `i-bilim-muhendislik/03-veri-bilimi-ml` — Bilimsel Python, istatistik, makine öğrenmesi, görselleştirm | K-Dense-AI/scientific-agent-skills 75B (27) | `dask` 100/B, `exploratory-data-analysis` 100/B, `get-available-resources` 100/B, `hugging-science` 100/B |
| `i-bilim-muhendislik/04-bilimsel-yazim-literatur` — Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendi | K-Dense-AI/scientific-agent-skills 75B (37) | `autoskill` 100/B, `bgpt-paper-search` 100/B, `citation-management` 100/B, `consciousness-council` 100/B |
| `i-bilim-muhendislik/05-cad-imalat-robotik` — CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı  | K-Dense-AI/scientific-agent-skills 75B (2) · earthtojake/text-to-cad 69B (12) | `fictiv` 100/B, `lab-hardware-cad` 100/B, `bambu-labs` 100/B, `dfam-check` 100/B |

## 2. Skill kaynakları (GitHub güven sıralaması)

| # | Kaynak | Güven | Skill | Ana kategoriler | Ücret (ücretsiz/kısmen/💲) | Lisans | Resmî | ★ | ★/ay | Katkıcı | Commit 90g | Son sürüm | 🔥 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Graphify-Labs/graphify | 91 A | 1 | 03-web-arastirma-veri (1) | 0/1/0 | Apache-2.0 |  | 139554 | 20106.4 | 378 | 1333 | 2026-10-30 | 🔥 |
| 2 | vercel/next.js | 91 A | 6 | 07-framework-ozel (6) | 6/0/0 | MIT | ✓ | 143230 | 1183.8 | 4180 | 1547 | 2026-10-30 | 🔥 |
| 3 | react/react | 90 A | 0 | - | 0/0/0 | MIT | ✓ | 251801 | 1559.6 | 2028 | 137 | 2026-10-14 |  |
| 4 | nexu-io/open-design | 88 A | 139 | 03-ai-gorsel-video-modelleri (22), 01-video-uretim-montaj (20) | 112/5/22 | Apache-2.0 |  | 105071 | 17172.9 | 451 | 787 | 2026-10-22 |  |
| 5 | DietrichGebert/ponytail | 86 A | 6 | 02-kod-kalitesi-review (6) | 6/0/0 | MIT |  | 181045 | 39033.8 | 133 | 163 | 2026-10-29 | 🔥 |
| 6 | heygen-com/hyperframes | 86 A | 13 | 01-video-uretim-montaj (10), 04-motion-graphics-karakter (3) | 9/4/0 | Apache-2.0 | ✓ | 76120 | 9847.0 | 125 | 2984 | 2026-10-31 | 🔥 |
| 7 | nextlevelbuilder/ui-ux-pro-max-skill | 85 A | 7 | 02-tasarim-sistemi-marka (4), 01-ui-ux-tasarim-dili (2) | 6/1/0 | MIT |  | 143087 | 12984.6 | 106 | 79 | 2026-08-13 |  |
| 8 | addyosmani/agent-skills | 84 A | 25 | 01-planlama-metodoloji (8), 06-devops-guvenlik-performans (5) | 25/0/0 | MIT |  | 112026 | 13200.0 | 96 | 383 | 2026-10-29 | 🔥 |
| 9 | microsoft/playwright | 84 A | 3 | 08-onyuz-test-kalite (2), 07-framework-ozel (1) | 3/0/0 | Apache-2.0 | ✓ | 98916 | 1182.9 | 827 | 730 | 2026-10-14 |  |
| 10 | anthropics/claude-code | 83 A | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | yok | ✓ | 153992 | 7599.6 | 59 | 243 | 2026-10-31 | 🔥 |
| 11 | tt-a1i/archify | 82 A | 5 | 01-repo-gelistirici-skilleri (2), 02-kod-kalitesi-review (1) | 5/0/0 | Apache-2.0 |  | 91880 | 14035.9 | 92 | 1635 | 2026-10-19 |  |
| 12 | obra/superpowers | 81 A | 14 | 02-agent-orkestrasyon (4), 01-planlama-metodoloji (3) | 14/0/0 | MIT |  | 309519 | 24313.6 | 44 | 6 | 2026-10-21 | 🔥 |
| 13 | Panniantong/Agent-Reach | 79 B | 1 | 03-web-arastirma-veri (1) | 1/0/0 | MIT |  | 106889 | 13049.9 | 38 | 110 | 2026-10-23 | 🔥 |
| 14 | pbakaus/impeccable | 79 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | Apache-2.0 |  | 97252 | 8471.2 | 61 | 1226 | 2026-10-26 | 🔥 |
| 15 | GoogleChrome/lighthouse | 76 B | 0 | - | 0/0/0 | Apache-2.0 | ✓ | 30986 | 242.2 | 397 | 184 | 2026-10-27 |  |
| 16 | Leonxlnx/taste-skill | 76 B | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 106429 | 12738.0 | 24 | 103 | 2026-10-24 | 🔥 |
| 17 | K-Dense-AI/scientific-agent-skills | 75 B | 175 | 01-yasam-bilimleri-kimya (90), 04-bilimsel-yazim-literatur (37) | 147/21/7 | MIT |  | 55425 | 4469.3 | 58 | 95 | 2026-10-01 | 🔥 |
| 18 | anthropics/claude-plugins-official | 75 B | 23 | 04-skill-plugin-yazimi (7), 02-agent-orkestrasyon (5) | 23/0/0 | Apache-2.0 | ✓ | 45465 | 4006.2 | 42 | 1889 | - | 🔥 |
| 19 | anthropics/skills | 73 B | 18 | 07-gorsel-sanat-sunum (4), 01-ofis-dokumanlari (4) | 17/1/0 | yok | ✓ | 185425 | 13952.8 | 17 | 15 | - |  |
| 20 | calesthio/OpenMontage | 72 B | 57 | 03-ai-gorsel-video-modelleri (17), 02-ses-muzik-konusma (14) | 22/13/22 | AGPL-3.0 |  | 73527 | 10348.2 | 76 | 169 | - | 🔥 |
| 21 | anthropics/knowledge-work-plugins | 71 B | 187 | 03-operasyon-urun-isletme (69), 01-satis-pazarlama-musteri (58) | 187/0/0 | Apache-2.0 | ✓ | 34064 | 3685.2 | 32 | 605 | - | 🔥 |
| 22 | motiondivision/motion | 71 B | 0 | - | 0/0/0 | MIT | ✓ | 34683 | 362.8 | 147 | 1002 | - |  |
| 23 | earthtojake/text-to-cad | 69 B | 12 | 05-cad-imalat-robotik (12) | 12/0/0 | MIT |  | 24373 | 3859.1 | 30 | 904 | 2026-10-30 | 🔥 |
| 24 | multica-ai/andrej-karpathy-skills | 68 B | 1 | 01-planlama-metodoloji (1) | 1/0/0 | yok |  | 226943 | 24906.4 | 7 | 0 | - |  |
| 25 | teng-lin/notebooklm-py | 68 B | 1 | 03-web-arastirma-veri (1) | 0/1/0 | MIT |  | 20014 | 2048.6 | 42 | 701 | 2026-10-29 |  |
| 26 | vercel-labs/agent-skills | 64 C | 9 | 07-framework-ozel (4), 06-devops-guvenlik-performans (3) | 6/3/0 | yok | ✓ | 33272 | 3093.2 | 28 | 23 | 2026-10-27 | 🔥 |
| 27 | android/skills | 63 C | 33 | 08-mobil-uygulama (33) | 32/1/0 | Apache-2.0 | ✓ | 10109 | 1342.0 | 8 | 39 | 2026-10-29 | 🔥 |
| 28 | Fei-Away/Codex-Dream-Skin | 62 C | 0 | - | 0/0/0 | MIT |  | 15264 | 4296.5 | 23 | 46 | 2026-10-15 |  |
| 29 | cloudflare/security-audit-skill | 62 C | 1 | 06-devops-guvenlik-performans (1) | 1/0/0 | MIT | ✓ | 54277 | 12222.4 | 4 | 3 | - | 🔥 |
| 30 | ComposioHQ/awesome-claude-skills | 61 C | 19 | 03-yazi-iletisim-icerik (9), 01-claude-api-mcp (3) | 16/3/0 | yok | ✓ | 78366 | 6285.8 | 29 | 0 | - |  |
| 31 | lemomo-ai/lemo-opuscar | 61 C | 1 | 01-video-uretim-montaj (1) | 1/0/0 | MIT |  | 9809 | 8519.8 | 4 | 72 | 2026-10-12 |  |
| 32 | cloudflare/skills | 60 C | 19 | 06-devops-guvenlik-performans (19) | 9/7/3 | Apache-2.0 | ✓ | 3225 | 301.7 | 48 | 254 | - | 🔥 |
| 33 | Donchitos/Claude-Code-Game-Studios | 56 C | 69 | 06-oyun-2d-grafik (69) | 69/0/0 | MIT |  | 30499 | 3552.4 | 1 | 5 | 2026-10-19 | 🔥 |
| 34 | czlonkowski/n8n-skills | 56 C | 15 | 02-agent-orkestrasyon (15) | 15/0/0 | MIT |  | 6554 | 529.9 | 7 | 35 | 2026-10-24 | 🔥 |
| 35 | expo/skills | 56 C | 24 | 08-mobil-uygulama (24) | 15/9/0 | MIT | ✓ | 3915 | 355.3 | 31 | 51 | - | 🔥 |
| 36 | vudovn/ag-kit | 55 C | 51 | 06-oyun-2d-grafik (11), 02-agent-orkestrasyon (7) | 51/0/0 | MIT |  | 8205 | 860.1 | 10 | 8 | 2026-08-31 |  |
| 37 | darkroomengineering/satus | 54 C | 1 | 08-onyuz-test-kalite (1) | 1/0/0 | MIT | ✓ | 1012 | 16.6 | 19 | 210 | 2026-08-28 |  |
| 38 | greensock/gsap-skills | 53 C | 8 | 03-animasyon-motion (7), 04-scroll-deneyimi (1) | 8/0/0 | MIT | ✓ | 17602 | 2220.3 | 4 | 0 | - |  |
| 39 | nateherkai/scroll-craft | 46 D | 1 | 04-scroll-deneyimi (1) | 1/0/0 | MIT |  | 4277 | 1857.4 | 1 | 16 | - |  |
| 40 | yaojingang/yao-meta-skill | 46 D | 1 | 04-skill-plugin-yazimi (1) | 1/0/0 | MIT |  | 2718 | 386.1 | 3 | 56 | - |  |
| 41 | CloudAI-X/threejs-skills | 44 D | 13 | 05-3d-webgl (13) | 13/0/0 | MIT |  | 3873 | 413.1 | 1 | 20 | - |  |
| 42 | ythx-101/live-panel-skill | 43 D | 1 | 02-diyagram-dokumantasyon (1) | 1/0/0 | MIT |  | 827 | 827.0 | 4 | 40 | - |  |
| 43 | nexscope-ai/eCommerce-Skills | 42 D | 162 | 05-e-ticaret-pazaryeri (156), 06-devops-guvenlik-performans (6) | 162/0/0 | MIT |  | 1304 | 174.6 | 7 | 1 | - |  |
| 44 | nexscope-ai/Amazon-Skills | 40 D | 52 | 05-e-ticaret-pazaryeri (52) | 52/0/0 | MIT |  | 820 | 106.1 | 5 | 1 | - |  |
| 45 | 40RTY-ai/shopify-admin-skills | 39 D | 117 | 05-e-ticaret-pazaryeri (117) | 117/0/0 | MIT |  | 201 | 30.1 | 3 | 13 | 2026-06-17 |  |
| 46 | heyitsnoah/claudesidian | 38 D | 18 | 04-not-alma-bilgi-yonetimi (13), 05-git-pr-surum (3) | 17/1/0 | MIT |  | 2607 | 191.4 | 3 | 0 | 2026-04-11 |  |
| 47 | zanwei/design-dna | 38 D | 1 | 01-ui-ux-tasarim-dili (1) | 1/0/0 | MIT |  | 2055 | 281.4 | 3 | 4 | - |  |
| 48 | evanca/flutter-ai-rules | 35 D | 35 | 08-mobil-uygulama (35) | 35/0/0 | MIT |  | 665 | 36.3 | 1 | 15 | - |  |
| 49 | freshtechbro/claudedesignskills | 34 D | 21 | 05-3d-webgl (10), 03-animasyon-motion (6) | 18/2/1 | MIT |  | 1189 | 97.4 | 1 | 0 | - |  |
| 50 | hamen/compose_skill | 34 D | 2 | 08-mobil-uygulama (2) | 2/0/0 | MIT |  | 376 | 56.9 | 3 | 0 | 2026-07-07 |  |
| 51 | xjli360/sealeap-amazon-skills | 34 D | 602 | 05-e-ticaret-pazaryeri (602) | 602/0/0 | MIT |  | 340 | 145.6 | 1 | 15 | - |  |
| 52 | OrcaQubits/agentic-commerce-skills-plugins | 33 D | 271 | 05-e-ticaret-pazaryeri (271) | 264/7/0 | MIT |  | 40 | 5.0 | 3 | 11 | 2026-05-13 |  |
| 53 | aldefy/compose-skill | 33 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | NOASSERTION |  | 598 | 74.2 | 5 | 0 | 2026-07-08 |  |
| 54 | lemomo-ai/lemo-wake | 33 D | 3 | 04-motion-graphics-karakter (3) | 3/0/0 | NOASSERTION |  | 221 | 221.0 | 1 | 15 | 2026-10-05 |  |
| 55 | mercadopago/mercadopago-claude-marketplace | 33 D | 5 | 05-e-ticaret-pazaryeri (5) | 0/5/0 | Apache-2.0 | ✓ | 32 | 3.9 | 10 | 15 | - |  |
| 56 | Livsy90/iOS-Performance-Agent-Skills | 29 D | 6 | 08-mobil-uygulama (6) | 6/0/0 | MIT |  | 119 | 22.8 | 2 | 0 | 2026-07-12 |  |
| 57 | dpconde/claude-android-skill | 29 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 350 | 32.4 | 1 | 0 | - |  |
| 58 | xjli360/sealeap-ecommerce-skills | 29 D | 195 | 05-e-ticaret-pazaryeri (195) | 195/0/0 | MIT |  | 114 | 93.7 | 1 | 11 | - |  |
| 59 | finsilabs/awesome-ecommerce-skills | 28 D | 175 | 05-e-ticaret-pazaryeri (175) | 157/18/0 | MIT |  | 60 | 7.8 | 4 | 3 | - |  |
| 60 | dadederk/iOS-Accessibility-Agent-Skill | 24 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | MIT |  | 175 | 19.1 | 1 | 0 | - |  |
| 61 | Lonsdale201/wp-agent-skills | 23 D | 31 | 05-e-ticaret-pazaryeri (31) | 31/0/0 | MIT |  | 26 | 4.3 | 3 | 29 | - |  |
| 62 | Shopify/agent-skills | 23 D | 15 | 05-e-ticaret-pazaryeri (15) | 15/0/0 | yok | ✓ | 99 | 14.1 | 1 | 0 | - |  |
| 63 | oldred-byte/ec-visual-skill | 23 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 101 | 17.2 | 1 | 0 | - |  |
| 64 | buluslan/ecommerce-competitor-analyzer | 22 D | 1 | 05-e-ticaret-pazaryeri (1) | 0/1/0 | MIT |  | 61 | 6.7 | 1 | 3 | 2026-01-29 |  |
| 65 | magendooro/magento-claude-skills | 19 D | 10 | 05-e-ticaret-pazaryeri (10) | 10/0/0 | MIT |  | 15 | 2.1 | 1 | 0 | - |  |
| 66 | mmiani/kotlin-kmp-claude-agent-skills | 19 D | 15 | 08-mobil-uygulama (15) | 15/0/0 | NOASSERTION |  | 89 | 12.4 | 1 | 8 | - |  |
| 67 | Trendyol/trendyol-integration-developer-tool | 17 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | yok | ✓ | 11 | 1.9 | 3 | 0 | - |  |
| 68 | lemomo-ai/codex-radar | 17 D | 1 | 02-agent-orkestrasyon (1) | 1/0/0 | NOASSERTION |  | 39 | 8.0 | 1 | 8 | - |  |
| 69 | J-DTurner/etsy-api-skill | 14 D | 1 | 05-e-ticaret-pazaryeri (1) | 1/0/0 | MIT |  | 6 | 0.7 | 1 | 0 | - |  |
| 70 | itsncki-design/app-store-submission-auditor | 13 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 34 | 4.6 | 1 | 0 | 2026-03-19 |  |
| 71 | vagabond911/aso-auditor | 13 D | 1 | 08-mobil-uygulama (1) | 1/0/0 | yok |  | 33 | 4.9 | 1 | 1 | - |  |

## 3. Referans kütüphaneleri (skill içermez) → onları öğreten skiller

Projede bu kütüphaneyi kullanıyorsan buradaki skiller öncelikli adaydır. **Sürüm** sütunu kartın yazıldığı sürümdür: projendeki sürüm çok farklıysa (ana sürüm) skill'in API'sini kontrol et. Kartın tamamı: "Kart" sütunu.

| # | Kütüphane | Güven | Sürüm (kart) | İlgili skiller (`id` puan/kaynak derecesi) | Kart |
|---|---|---|---|---|---|
| 1 | mrdoob/three.js | 87 A | r186 | `threejs-fundamentals` 89/D, `threejs-geometry` 79/D, `threejs-materials` 79/D, `threejs-lighting` 89/D, `threejs-textures` 81/D, `threejs-loaders` 89/D, `threejs-shaders` 79/D, `threejs-postprocessing` 79/D, `threejs-animation` 81/D, `threejs-interaction` 81/D | tasarim-teknolojileri.md |
| 2 | tailwindlabs/tailwindcss | 79 B | v4.3 | `ui-styling` 88/A, `tailwind-patterns` 76/C, `design-system@nextlevelbuilder` 90/A, `tailwind-design-system` 96/B, `web-artifacts-builder` 80/B, `saleor-storefront` 80/D, `nextjs-react` 78/D, `spree-admin-customization` 78/D | tasarim-teknolojileri.md |
| 3 | FFmpeg/FFmpeg | 74 B | - | `ffmpeg` 96/B, `video-edit` 100/B, `video-understand` 97/B, `character-animation-qa` 89/B | kutuphaneler.md |
| 4 | pmndrs/react-three-fiber | 71 B | v9.8 | `threejs-react-three-fiber` 87/D, `react-three-fiber` 62/D, `blender-web-pipeline` 62/D, `web3d-integration-patterns` 62/D, `substance-3d-texturing` 54/D, `modern-web-design` 52/D | tasarim-teknolojileri.md |
| 5 | VoltAgent/awesome-design-md | 70 B | - | `design-dna` 79/D, `design-system@nextlevelbuilder` 90/A, `design-taste-frontend` 100/B | tasarim-teknolojileri.md |
| 6 | QwikDev/partytown | 66 B | v1.0 (T5) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 7 | dequelabs/axe-core | 65 B | v4.14 (MPL-2.0) | `accessibility-review` 99/B, `frontend-ui-engineering` 98/A, `inclusive-design` 80/D, `accessibility` 78/D, `accessibility-commerce` 76/D, `platform-design` 66/A | tasarim-teknolojileri.md |
| 8 | pmndrs/drei | 62 C | v10.7 | `threejs-react-three-fiber` 87/D | tasarim-teknolojileri.md |
| 9 | airbnb/lottie-web | 60 C | v5.13 | `lottie-animations` 62/D, `remotion-to-hyperframes` 97/A, `lottie-bodymovin` 81/B, `flutter-pre-caching` 78/D, `rive-interactive` 62/D | tasarim-teknolojileri.md |
| 10 | darkroomengineering/lenis | 60 C | v1.3 | `scroll-craft` 78/D, `gsap-scrolltrigger` 86/C, `locomotive-scroll` 62/D | tasarim-teknolojileri.md |
| 11 | fontsource/fontsource | 59 C | - | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 12 | ai/size-limit | 58 C | 14.2 (T5) | `react-doctor` 76/C, `nextjs-react-expert` 74/C | tasarim-teknolojileri.md |
| 13 | barvian/number-flow | 48 D | 0.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 14 | figma/code-connect | 47 D | v2.0 | `figma-code-connect-components` 66/A | tasarim-teknolojileri.md |
| 15 | argyleink/open-props | 46 D | v1.6 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 16 | greensock/GSAP | 46 D | 3.15 | `gsap-core` 86/C, `gsap-timeline` 87/C, `gsap-plugins` 86/C, `gsap-utils` 78/C, `gsap-react` 87/C, `gsap-frameworks` 78/C, `gsap-performance` 87/C, `gsap-scrolltrigger` 86/C | tasarim-teknolojileri.md |
| 17 | seek-oss/capsize | 46 D | metrics 4.4 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 18 | oframe/ogl | 40 D | - | `lightweight-3d-effects` 61/D, `threejs-shaders` 79/D | tasarim-teknolojileri.md |
| 19 | zhuyansen/awesome-claude-video-skills | 39 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 20 | 14islands/r3f-scroll-rig | 37 D | v8.15 | `threejs-react-three-fiber` 87/D, `web3d-integration-patterns` 62/D, `gpt-taste` 94/A, `gsap-scrolltrigger` 86/C, `lottie-animations` 62/D, `barba-js` 62/D, `locomotive-scroll` 62/D, `scroll-reveal-libraries` 62/D | tasarim-teknolojileri.md |
| 21 | linvi/tweetinvi | 36 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 22 | nevertoday/350-layout-compositions | 34 D | - | `design-taste-frontend` 100/B, `canvas-design` 79/B, `slides` 82/A | tasarim-teknolojileri.md |
| 23 | pmndrs/react-three-a11y | 32 D | v3.0 (2022, bakımı yavaş) | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 24 | arturitu/the-delegation | 26 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 25 | bytefer/awesome-nextjs | 24 D | - | — (skill eşlemesi yok) | kutuphaneler.md |
| 26 | gchahal1982/pixeljury | 20 D | v0.1.5 | — (skill eşlemesi yok) | tasarim-teknolojileri.md |
| 27 | haticesahin/SanalFuar | 12 D | - | — (skill eşlemesi yok) | kutuphaneler.md |

## 4. Hesap ayrıntısı

Kaynak güveni = her ölçütün skill kaynakları (T1–T4) içindeki yüzdelik sırası × ağırlık: yıldız 25 · yıldız hızı (★/ay) 15 · katkıcı 15 · son 90 gün commit 15 · fork 10 · izleyici 5 · son 180 günde sürüm 5 · açık lisans 5 · resmî üretici 5 (kurum 3); arşivlenmiş repo ×0,5. A ≥80 · B ≥65 · C ≥50 · D <50. Referans kütüphaneleri havuza girmez, kendi aralarında sıralanır. Skill puanının ayrıntısı: `registry.json` → `degerlendirme.ayrinti`. Güncelleme: `gelistirici-bilgisi.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (aylık güncellemede otomatik).
