# Yol Denetimi

> `araclar/yol-tara.py` üretir · 2026-11-11 · salt okuma. Skill metinlerindeki sabit genel yol / eklenti kökü / kardeş yol bağımlılıkları. Ayrıntı: `python3 araclar/yol-tara.py --skill <id>`; istisna: `yol-istisnalari.json`.

**5649 skill tarandı** · bulgusu olan: 431 · ön kontrolde UYARI alan: 125

## Bulgu türleri

| Tür | Bulgu | Skill | Doküman sınıfında |
|---|---:|---:|---:|
| eklenti-kardes | 15 | 6 | 0 |
| eklenti-kendi | 29 | 3 | 1 |
| eklenti-kok-anma | 95 | 14 | 18 |
| eklenti-kok-yol | 459 | 53 | 6 |
| genel-baska | 35 | 10 | 11 |
| genel-kalip | 2 | 2 | 1 |
| genel-kendi | 108 | 31 | 70 |
| genele-kopyalar | 64 | 18 | 43 |
| genele-yazar | 206 | 157 | 26 |
| kardes-goreli | 406 | 111 | 50 |
| ornek-metin | 30 | 12 | 4 |
| ortak-dizin | 3 | 2 | 0 |
| skil-disi-yol | 75 | 69 | 0 |

Yalnız sayılan türler (ön kontrolde satır üretmez): ornek-metin, genel-kalip, eklenti-kok-anma, kurulum bandındaki genele-yazar; doküman sınıfı (README, NOTICE, dil klasörleri, atıfsız dosyalar) bulguları da yalnız sayılır. Kapsam dışı (taranmaz): kodda `Path.home() / ".agents" / "skills"` gibi çalışma anında kurulan yollar, öneksiz göreli yollar (`skills/<ad>/…`), `.copilot` gibi başka kök klasörler, Windows yolları.

## Ön kontrol kodları (kaç skilde)

| Seviye | Kod | Skill |
|---|---|---:|
| BİLGİ | eklenti-koku | 1 |
| BİLGİ | genele-yazabilir | 13 |
| BİLGİ | kardes-eksik | 112 |
| BİLGİ | yol-istisna | 10 |
| BİLGİ | yol-yerellestirme | 5 |
| UYARI | eklenti-koku | 42 |
| UYARI | genel-yol | 9 |
| UYARI | genele-yazabilir | 5 |
| UYARI | kardes-eksik | 4 |
| UYARI | skil-disi-yol | 68 |

## Sütunlar

| Sütun | Skill |
|---|---:|
| Kurulumda düzelir | 3 |
| Kardeşle düzelir | 103 |
| Paket gerekli | 115 |
| Çözülemez | 7 |
| İstisna | 10 |
| Yalnız sayım (satır yok) | 193 |
| Temiz | 5218 |

## Kurulumda düzelir (3)

_kurulan kopyada yol proje içi yola çevrilecek._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| code-tour | github/awesome-copilot | yol-yerellestirme | 3 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:23 ~/.agents/skills/code-tour/scripts/validate_tour.py; SKILL.md:24 ~/.agents/skills/… |
| siege | anthropics/claude-plugins-official | yol-yerellestirme | 3 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:7 ${CLAUDE_PLUGIN_ROOT}/skills/siege/scripts/ledger.py; SKILL.md:73 ${CLAUDE_PLUGIN_R… |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill | yol-yerellestirme | 11 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:42 ${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py; SKILL.md:78… |

## Kardeşle düzelir (103)

_aynı repodaki kardeş skill de kurulursa yol tutar._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| accessibility-and-inclusive-visualization | openai/plugins | kardes-eksik | dashboards-and-real-time-visualization (dashboards-and-real-time-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/keyboard… |
| add-cli-option | remotion-dev/remotion | kardes-eksik | studio-config-option-lifecycle (studio-config-option-lifecycle) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:80 ../studio-config-option… |
| aiq-research | openai/plugins | kardes-eksik | aiq-deploy (aiq-deploy) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:263 ../aiq-deploy/SKILL.md |
| android-performance | openai/plugins | kardes-eksik | android-emulator-qa (android-emulator-qa) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:8 ../android-emulator-qa/SKILL.md |
| autoresearch@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:27 ../wiki/references |
| brand-style | anthropics/knowledge-work-plugins | kardes-eksik | smb-onboard (smb-onboard) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:41 ../smb-onboard/reference/website-research.md; SKILL.md:83 ../… |
| build-mcp-app | anthropics/claude-plugins-official | kardes-eksik | build-mcp-server (build-mcp-server) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:59 ../build-mcp-server/references/elicitation.md |
| build-zoom-contact-center-app | openai/plugins | kardes-eksik | cobrowse-sdk (zoom-cobrowse-sdk) kardeş skill gerekli; kurulursa kardeşle düzelir: web/SKILL.md:42 ../../cobrowse-sdk/SKILL.md |
| build-zoom-meeting-sdk-app | openai/plugins | kardes-eksik | oauth (zoom-oauth) kardeş skill gerekli; kurulursa kardeşle düzelir: android/SKILL.md:28 ../../oauth/SKILL.md |
| build-zoom-video-sdk-app | openai/plugins | kardes-eksik | meeting-sdk (build-zoom-meeting-sdk-app) kardeş skill gerekli; kurulursa kardeşle düzelir: web/SKILL.md:12 ../../meeting-sdk/web/component-view/SKILL… |
| build-zoom-virtual-agent | openai/plugins | kardes-eksik | contact-center (build-zoom-contact-center-app) kardeş skill gerekli; kurulursa kardeşle düzelir: android/SKILL.md:34 ../../contact-center/android/SKI… |
| canva-creator | anthropics/knowledge-work-plugins | kardes-eksik | social-content-engine (social-content-engine) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:69 ../social-content-engine/reference/shopif… |
| canvas | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:20 ../wiki/references |
| canvas2d-data-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/re… |
| catalyst-calendar | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| company-tearsheet | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| comps-valuation | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| d3-data-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/d3… |
| dashboards-and-real-time-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/in… |
| data-visualization@openai | openai/plugins | kardes-eksik | canvas2d-data-visualization (canvas2d-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/default-stack-selection.md:64 … |
| dcf-model-builder | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| deck-report-qc | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| defuddle@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:21 ../wiki/references |
| earnings-deep-dive | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| earnings-preview | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| eas-simulator | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: references/run-your-app.md:222 ../../expo-overview/references/launch-… |
| economic-impact-report | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| equity-model-update | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| evaluate-skill | openai/plugins | kardes-eksik | improve-skill (improve-skill) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:21 ../improve-skill/SKILL.md |
| event-driven-analyzer | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| executing-plans | obra/superpowers | kardes-eksik | subagent-driven-development (subagent-driven-development) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:126 ../subagent-driven-developme… |
| executing-plans@openai | openai/plugins | kardes-eksik | using-superpowers (using-superpowers@openai) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:14 ../using-superpowers/references |
| expo-dev-client | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:154 ../expo-overview/references/launch-without-dev-menu.md |
| expo-web-to-native | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: references/verify-on-device.md:32 ../../expo-overview/references/laun… |
| financials-normalizer | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| finding-discovery | openai/plugins | kardes-eksik | attack-path-analysis (attack-path-analysis) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:117 ../attack-path-analysis/references/severit… |
| founder-offer | Jakeschincariol/founder-skill | kardes-eksik | founder-board (founder-board) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:19 ../founder-board/lenses.md |
| founder-pricing | Jakeschincariol/founder-skill | kardes-eksik | founder-cfo (founder-cfo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:58 ${CLAUDE_SKILL_DIR}/../founder-cfo/unit_economics.py |
| game-playtest | openai/plugins | kardes-eksik | game-ui-frontend (game-ui-frontend) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:74 ../game-ui-frontend/SKILL.md |
| game-studio | openai/plugins | kardes-eksik | game-playtest (game-playtest) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:50 ../game-playtest/SKILL.md |
| game-ui-frontend | openai/plugins | kardes-eksik | react-three-fiber-game (react-three-fiber-game) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:111 ../react-three-fiber-game/SKILL.md |
| geospatial-and-cartographic-visualization | openai/plugins | kardes-eksik | d3-data-visualization (d3-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/deckgl-d3-geo-stack-selection.md:30 ../../… |
| grammar-of-graphics-and-declarative-visualization | openai/plugins | kardes-eksik | canvas2d-data-visualization (canvas2d-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/when-to-stay-declarative.md:27… |
| growth-pulse | anthropics/knowledge-work-plugins | kardes-eksik | ad-manager (ad-manager) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/data_sources.md:46 ../../ad-manager/SKILL.md |
| hyperframes-cli | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:97 ../hyperframes/references/motion.md; references/preview-rende… |
| hypogenic | K-Dense-AI/scientific-agent-skills | kardes-eksik | hypothesis-generation (hypothesis-generation) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:31 ../hypothesis-generation/SKILL.md |
| idea-creator | wanshuiyin/Auto-claude-code-research-in-sleep | kardes-eksik | research-wiki (research-wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:81 ../research-wiki/SKILL.md |
| idea-generation | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| initiating-coverage | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| ios-ettrace-performance | openai/plugins | kardes-eksik | ios-debugger-agent (ios-debugger-agent) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:8 ../ios-debugger-agent/SKILL.md |
| ios-memgraph-leaks | openai/plugins | kardes-eksik | ios-debugger-agent (ios-debugger-agent) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:8 ../ios-debugger-agent/SKILL.md |
| long-short-pitch | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| marketing-monday | anthropics/knowledge-work-plugins | kardes-eksik | growth-pulse (growth-pulse) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:9 ../growth-pulse/reference/data_sources.md |
| media-use | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: references/local.md:25 ../../hyperframes/references/captions.md |
| meeting-prep | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| memo-builder | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| model-audit-tieout | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| monday-brief | anthropics/knowledge-work-plugins | kardes-eksik | report-builder (report-builder) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:28 ../report-builder/reference/saved_reports.md |
| mp-test-setup | mercadopago/mercadopago-claude-marketplace | kardes-eksik | mp-integrate (mp-integrate) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:120 ${CLAUDE_PLUGIN_ROOT}/skills/mp-integrate/references/produ… |
| node-link-and-diagram-layout | openai/plugins | kardes-eksik | canvas2d-data-visualization (canvas2d-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:144 ../canvas2d-data-visualizati… |
| obsidian-bases@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:26 ../wiki/references |
| obsidian-markdown@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:22 ../wiki/references |
| phaser-2d-game | openai/plugins | kardes-eksik | game-ui-frontend (game-ui-frontend) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:86 ../game-ui-frontend/SKILL.md |
| plugin-eval | openai/plugins | kardes-eksik | evaluate-plugin (evaluate-plugin) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:74 ../evaluate-plugin/SKILL.md |
| portfolio-risk-management | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| public-equity-investing | openai/plugins | kardes-eksik | user-context (user-context@openai) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:159 ../user-context/SKILL.md |
| react-and-nextjs-data-visualization | openai/plugins | kardes-eksik | d3-data-visualization (d3-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/d3-canvas-and-grammar-in-react.md:27 ../..… |
| react-scan | remotion-dev/remotion | kardes-eksik | studio-perf (studio-perf) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:63 ../studio-perf/SKILL.md |
| react-three-fiber-game | openai/plugins | kardes-eksik | game-ui-frontend (game-ui-frontend) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:80 ../game-ui-frontend/SKILL.md |
| remotion-to-hyperframes | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:43 ../hyperframes/references/runtimes.md |
| replica-brand | Jakeschincariol/replica-skill | kardes-eksik | replica-design (replica-design) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:66 ../replica-design/contrast.py |
| replica-deploy | Jakeschincariol/replica-skill | kardes-eksik | replica-brand (replica-brand) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:34 ../replica-brand/sweep.py |
| reports-pdfs-and-slide-automation | openai/plugins | kardes-eksik | data-visualization (data-visualization@openai) kardeş skill gerekli; kurulursa kardeşle düzelir: references/document-embedding-and-regeneration.md:25… |
| research-refine-pipeline | wanshuiyin/Auto-claude-code-research-in-sleep | kardes-eksik | experiment-plan (experiment-plan) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:39 ../experiment-plan/SKILL.md |
| save | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:32 ../wiki/references |
| scenario-sensitivity-generator | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| scrollytelling-and-parallax-data-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:75 .… |
| seo-local | AgriciDaniel/claude-seo | kardes-eksik | seo (seo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:61 ../seo/references/local-schema-types.md; SKILL.md:165 ../seo/references/local… |
| seo-maps | AgriciDaniel/claude-seo | kardes-eksik | seo (seo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:54 ../seo/references/maps-free-apis.md; SKILL.md:59 ../seo/references/maps-api-e… |
| skill-development | anthropics/claude-plugins-official | kardes-eksik | agent-development (agent-development) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:610 ../agent-development/ |
| skill-development@anthropics | anthropics/claude-code | kardes-eksik | agent-development (agent-development@anthropics) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:610 ../agent-development/ |
| smb-router | anthropics/knowledge-work-plugins | kardes-eksik | cash-flow-snapshot (cash-flow-snapshot) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/connector-map.md:45 ../../cash-flow-snapshot/refe… |
| sprite-pipeline | openai/plugins | kardes-eksik | game-studio (game-studio) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../game-studio/SKILL.md |
| statistical-and-uncertainty-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/mi… |
| subagent-driven-development@openai | openai/plugins | kardes-eksik | requesting-code-review (requesting-code-review@openai) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:88 ../requesting-code-review/code-r… |
| testing-data-visualizations | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:140 … |
| thesis-tracker | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| three-statement-model-builder | openai/plugins | kardes-eksik | public-equity-investing (public-equity-investing) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:12 ../public-equity-investing/SKILL.md |
| three-webgl-game | openai/plugins | kardes-eksik | game-ui-frontend (game-ui-frontend) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:116 ../game-ui-frontend/SKILL.md |
| threejs-data-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/pa… |
| typescript-data-visualization-engineering | openai/plugins | kardes-eksik | canvas2d-data-visualization (canvas2d-data-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/library-selection-for-builders… |
| ui-toolkit | openai/plugins | kardes-eksik | video-sdk (build-zoom-video-sdk-app) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:24 ../video-sdk/web/SKILL.md |
| uml-and-software-architecture-visualization | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:115 … |
| update-ffmpeg | remotion-dev/remotion | kardes-eksik | pr (pr@remotion-dev) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:38 ../pr/SKILL.md |
| visualization-strategy-and-critique | openai/plugins | kardes-eksik | accessibility-and-inclusive-visualization (accessibility-and-inclusive-visualization) kardeş skill gerekli; kurulursa kardeşle düzelir: references/cr… |
| wiki-cli | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:21 ../wiki/references |
| wiki-fold | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:22 ../wiki/references |
| wiki-ingest | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:23 ../wiki/references |
| wiki-lint | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:20 ../wiki/references |
| wiki-mode | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:24 ../wiki/references |
| wiki-query | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:27 ../wiki/references |
| yt-audit | Jakeschincariol/youtube-agent-skill | kardes-eksik | yt-package (yt-package) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:26 ../yt-package/title.py |
| yt-shorts | Jakeschincariol/youtube-agent-skill | kardes-eksik | yt-script (yt-script) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:28 ../yt-script/hookscore.py |

## Paket gerekli (115)

_dosya arşive alınmamış (eklenti kökü / kardeşte ya da kendinde eksik)._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| adopt | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| architecture-decision | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| architecture-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| art-bible | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| asset-spec | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| balance-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| brainstorm | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| bug-report | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| bug-triage | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| changelog | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| claude-security | anthropics/claude-plugins-official | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:21 ${CLAUDE_PLUGIN_ROOT}/scripts/render_report.p… |
| code-review@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| consistency-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| content-audit | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| cost-advise | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:11 ${CLAUDE_PLUGIN_ROOT}/scripts/advise.mjs |
| cost-ledger | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/scripts/ledger.mjs; SKI… |
| cost-local | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:11 ${CLAUDE_PLUGIN_ROOT}/scripts/local-cost.mjs |
| cost-openrouter | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:13 ${CLAUDE_PLUGIN_ROOT}/scripts/openrouter.mjs;… |
| create-architecture | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-control-manifest | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-epics | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-stories | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| design-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| design-system@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| dev-story | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:11 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| egm-bootstrap | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:11 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-brainstorm | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:16 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-draft | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-drift-report | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-resolve | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-review | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-review-loop | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:17 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| gate-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| geo | zubair-trabzada/geo-seo-claude | genel-yol | kendi genel klasöründen dosya bekliyor, bu dosyalar arşivde yok: SKILL.md:195 ~/.claude/skills/geo/templates; SKILL.md:205 ~/.claude/skills/geo/templ… |
| geo-report-pdf | zubair-trabzada/geo-seo-claude | kardes-eksik | geo: dosya arşivde yok: SKILL.md:26 ~/.claude/skills/geo/templates/geo-report-template.html; SKILL.md:59 ~/.claude/skills/geo/templates/geo-report-te… |
| geo-schema | zubair-trabzada/geo-seo-claude | kardes-eksik | geo: dosya arşivde yok: SKILL.md:31 ~/.claude/skills/geo/scripts/fetch_page.py |
| geo-update | zubair-trabzada/geo-seo-claude | genele-yazabilir, kardes-eksik | bilgisayar geneli skill/agent klasörüne dosya kopyalıyor: SKILL.md:64 cp -r "$SOURCE_DIR/geo/"* "$CLAUDE_DIR/skills; SKILL.md:69 mkdir -p "$CLAUDE_DI… |
| help | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:20 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh; SKILL.md:205 ${CLAUDE_SK… |
| launch-checklist | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| localize | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| map-systems | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| milestone-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| monitor-stream | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:9 ${CLAUDE_PLUGIN_ROOT}/scripts/swarm-watch.mjs |
| mp-commerce-checkout | mercadopago/mercadopago-claude-marketplace | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:182 ${CLAUDE_PLUGIN_ROOT}/templates/mp_checkout_… |
| mp-integrate | mercadopago/mercadopago-claude-marketplace | eklenti-koku, yol-yerellestirme | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:111 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve-checko… |
| onboard | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| patch-notes | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| perf-profile | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh; SKILL.md:85 ${CLAUDE_SKI… |
| playtest-report | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| project-stage-detect | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:24 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| propagate-design-change | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| prototype@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| qa-plan | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| quick-design | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| readiness-audit | OrcaQubits/agentic-commerce-skills-plugins | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:37 ${CLAUDE_PLUGIN_ROOT}/scripts/readiness_audit… |
| readiness-quick-check | OrcaQubits/agentic-commerce-skills-plugins | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:22 ${CLAUDE_PLUGIN_ROOT}/scripts/readiness_audit… |
| regression-suite | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| release-checklist | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:9 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| retrospective | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| reverse-document | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:40 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| review-all-gdds | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| ruos-host-run | ruvnet/ruflo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:16 ${CLAUDE_PLUGIN_ROOT}/scripts/cli.mjs |
| security-audit@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| seo | AgriciDaniel/claude-seo | eklenti-koku, genel-yol, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:18 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-agentic | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:46 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-audit@agricidaniel | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:17 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-backlinks | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:21 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-cluster | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:80 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-content | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:146 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SK… |
| seo-dataforseo | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:51 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-drift | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:98 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-ecommerce | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:42 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-flow | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:85 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-geo | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:335 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-google | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:32 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-hreflang | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: references/machine-translation-qa.md:45 ${CLAUDE_PLUGIN_R… |
| seo-images | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:109 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SK… |
| seo-page | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:23 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-programmatic | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:119 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-schema | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:19 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-sitemap | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:23 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-sxo | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:43 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-technical | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:23 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| settings | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:53 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| setup-engine | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:14 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| skill-improve | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| skill-test | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| smoke-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| soak-test | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| sprint-plan | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| sprint-status | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh; SKILL.md:49 ${CLAUDE_SKI… |
| start@anthropics | anthropics/knowledge-work-plugins | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:26 ${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html |
| story-done | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:11 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| story-readiness | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| swift-code-reviewer | Viniciuscarvalho/swift-code-reviewer-skill | kardes-eksik, yol-yerellestirme | swiftui-ui-patterns: dosya arşivde yok: references/swiftui-review-checklist.md:932 ~/.claude/skills/swiftui-ui-patterns/references/navigation.md |
| task-management | anthropics/knowledge-work-plugins | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:23 ${CLAUDE_PLUGIN_ROOT}/skills/dashboard.html |
| team-audio | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:29 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-combat | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:29 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-level | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:29 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-live-ops | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:29 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-narrative | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:28 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-polish | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:28 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-qa | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:26 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-release | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:30 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| team-ui | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:28 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| tech-debt@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| test-evidence-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| test-flakiness | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| test-helpers | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| test-setup | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| ux-design | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| ux-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| vertical-slice | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| writing-hookify-rules | anthropics/claude-plugins-official | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:324 ${CLAUDE_PLUGIN_ROOT}/examples |
| writing-hookify-rules@anthropics | anthropics/claude-code | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:324 ${CLAUDE_PLUGIN_ROOT}/examples |

## Çözülemez (7)

_otomatik çevrilmiyor ya da hedef bulunamıyor: elle bakılmalı._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| app-store | rshankras/claude-code-apple-skills | genel-yol | ortak dizine (_shared gibi) dayanıyor: iap-finalizer/SKILL.md:25 ../../_shared/asc-api/asc.py; iap-finalizer/SKILL.md:27 ~/.claude/skills/_shared/asc… |
| graphify | Graphify-Labs/graphify | genel-yol | kendi sabit yolu otomatik çevrilmiyor (betik içinde / kurulum dosyasında / karışık ya da kurulum anlatan dosyada): install.py:578 ~/.claude/skills/gr… |
| hatch-pet | nexu-io/open-design | genel-yol | kendi genel klasörünü bir değişkene atıyor (sonraki betik yolları buna dayanabilir), otomatik çevrilmiyor: SKILL.md:149 ${CODEX_HOME:-$HOME/.codex}/s… |
| iap-finalizer | rshankras/claude-code-apple-skills | genel-yol | ortak dizine (_shared gibi) dayanıyor: SKILL.md:27 ~/.claude/skills/_shared/asc-api/asc.py |
| improve-skill | openai/plugins | genel-yol | başka skill'in genel klasörüne dayanıyor, aynı repoda tek aday olarak çözülemedi: SKILL.md:14 /Users/benlesh/.codex/skills/skill-creator/SKILL.md (kü… |
| ponder | github/awesome-copilot | eklenti-koku, genel-yol, genele-yazabilir | kendi sabit yolu otomatik çevrilmiyor (betik içinde / kurulum dosyasında / karışık ya da kurulum anlatan dosyada): references/harness-notes.md:66 ~/.… |
| v3-core-implementation | ruvnet/ruflo | genel-yol | göreli kardeş yolu (../<skill>/…) aynı repoda tek aday olarak çözülemedi, düz kurulumda kırılır: SKILL.md:177 ../events/task-assigned.event (kütüphan… |

## İstisna (10)

_yol-istisnalari.json kaydıyla kapsanmış._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| cli-mastery | github/awesome-copilot | yol-istisna | 1 bulgu istisna kaydıyla kapsandı (genele-kopyalar; kayıt: yol-istisnalari.json) |
| command-development | anthropics/claude-plugins-official | yol-istisna | 81 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| command-development@anthropics | anthropics/claude-code | yol-istisna | 81 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| create-cowork-plugin | anthropics/knowledge-work-plugins | yol-istisna | 3 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| hook-development | anthropics/claude-plugins-official | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| hook-development@anthropics | anthropics/claude-code | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| mcp-integration | anthropics/claude-plugins-official | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| mcp-integration@anthropics | anthropics/claude-code | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| plugin-structure | anthropics/claude-plugins-official | yol-istisna | 21 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| plugin-structure@anthropics | anthropics/claude-code | yol-istisna | 21 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |

## Genel klasöre dosya kopyalayabilen skiller (5)

Ajan dosyasında `cp / ln -s / mkdir -p / git clone … ~/.claude/skills` satırı var (sütunlardan bağımsız bilgi).

agent-skill-stack, create-data-context, geo-update, ponder, skill-builder

## Sonraki tur adayı: eklenti kökü dosyalarını arşive almak (`ek_dosyalar`)

Bu turda YAPILMADI: kök dosyaları (scripts/, docs/, templates/ …) çekmek lisans ve ücret sınıflandırması onayı ister (`ucret-siniflandirma.json`, `notlar/ucretli-skiller.md`). Aday sayısı repo bazında:

| Repo | Skill |
|---|---:|
| AgriciDaniel/claude-seo | 20 |
| Donchitos/Claude-Code-Game-Studios | 68 |
| OrcaQubits/agentic-commerce-skills-plugins | 2 |
| Viniciuscarvalho/swift-code-reviewer-skill | 1 |
| anthropics/claude-code | 1 |
| anthropics/claude-plugins-official | 2 |
| anthropics/knowledge-work-plugins | 2 |
| github/awesome-copilot | 1 |
| google/elephant-goldfish-model | 7 |
| mercadopago/mercadopago-claude-marketplace | 2 |
| ruvnet/ruflo | 6 |
| zubair-trabzada/geo-seo-claude | 4 |
