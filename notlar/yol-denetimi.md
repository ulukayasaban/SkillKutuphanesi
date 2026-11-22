# Yol Denetimi

> `araclar/yol-tara.py` üretir · 2026-11-22 · salt okuma. Skill metinlerindeki sabit genel yol / eklenti kökü / kardeş yol bağımlılıkları. Ayrıntı: `python3 araclar/yol-tara.py --skill <id>`; istisna: `yol-istisnalari.json`.

**2930 skill tarandı** · bulgusu olan: 377 · ön kontrolde UYARI alan: 120

## Bulgu türleri

| Tür | Bulgu | Skill | Doküman sınıfında |
|---|---:|---:|---:|
| eklenti-kardes | 39 | 9 | 0 |
| eklenti-kendi | 35 | 4 | 1 |
| eklenti-kok-anma | 95 | 13 | 18 |
| eklenti-kok-yol | 471 | 48 | 6 |
| genel-baska | 30 | 7 | 8 |
| genel-kalip | 2 | 2 | 1 |
| genel-kendi | 110 | 35 | 72 |
| genele-kopyalar | 63 | 15 | 47 |
| genele-yazar | 208 | 156 | 26 |
| kardes-goreli | 118 | 60 | 4 |
| ornek-metin | 26 | 8 | 4 |
| ortak-dizin | 3 | 2 | 0 |
| skil-disi-yol | 76 | 70 | 0 |

Yalnız sayılan türler (ön kontrolde satır üretmez): ornek-metin, genel-kalip, eklenti-kok-anma, kurulum bandındaki genele-yazar; doküman sınıfı (README, NOTICE, dil klasörleri, atıfsız dosyalar) bulguları da yalnız sayılır. Kapsam dışı (taranmaz): kodda `Path.home() / ".agents" / "skills"` gibi çalışma anında kurulan yollar, öneksiz göreli yollar (`skills/<ad>/…`), `.copilot` gibi başka kök klasörler, Windows yolları.

## Ön kontrol kodları (kaç skilde)

| Seviye | Kod | Skill |
|---|---|---:|
| BİLGİ | genele-yazabilir | 12 |
| BİLGİ | kardes-eksik | 68 |
| BİLGİ | yol-istisna | 8 |
| BİLGİ | yol-yerellestirme | 9 |
| UYARI | eklenti-koku | 39 |
| UYARI | genel-yol | 8 |
| UYARI | genele-yazabilir | 2 |
| UYARI | istisna-eskidi | 1 |
| UYARI | kardes-eksik | 4 |
| UYARI | skil-disi-yol | 69 |

## Sütunlar

| Sütun | Skill |
|---|---:|
| Kurulumda düzelir | 6 |
| Kardeşle düzelir | 58 |
| Paket gerekli | 113 |
| Çözülemez | 6 |
| İstisna | 8 |
| Yalnız sayım (satır yok) | 186 |
| Temiz | 2553 |

## Kurulumda düzelir (6)

_kurulan kopyada yol proje içi yola çevrilecek._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| ffmpeg-skill | kajisho5/ffmpeg-skill | yol-yerellestirme | 1 sabit yol kurulan kopyada proje içi yola çevrilecek (references/scripts.md:1657 ~/.claude/skills/ffmpeg-skill/mcp/server.py) |
| kinetic-reel | tuzhechen2005/opus-video-skills | yol-yerellestirme | 1 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:22 ~/.claude/skills/kinetic-reel/scripts/new_project.sh) |
| painted-animation | tuzhechen2005/opus-video-skills | yol-yerellestirme | 1 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:17 ~/.claude/skills/painted-animation/scripts/new_project.sh) |
| siege | anthropics/claude-plugins-official | yol-yerellestirme | 3 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:7 ${CLAUDE_PLUGIN_ROOT}/skills/siege/scripts/ledger.py; SKILL.md:73 ${CLAUDE_PLUGIN_R… |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill | yol-yerellestirme | 15 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:42 ${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/scripts/search.py; SKILL.md:80… |
| youtube-arama | yerel/kendi | yol-yerellestirme | 4 sabit yol kurulan kopyada proje içi yola çevrilecek (SKILL.md:13 ~/.claude/skills/youtube-arama/scripts/youtube_search.py; SKILL.md:28 ~/.claude/sk… |

## Kardeşle düzelir (58)

_aynı repodaki kardeş skill de kurulursa yol tutar._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| accessibility-engineering | addyosmani/agent-skills | kardes-eksik | frontend-ui-engineering (frontend-ui-engineering) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:26 ../frontend-ui-engineering/SKILL.md; … |
| add-cli-option | remotion-dev/remotion | kardes-eksik | studio-config-option-lifecycle (studio-config-option-lifecycle) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:80 ../studio-config-option… |
| autoresearch@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:27 ../wiki/references |
| brand-style | anthropics/knowledge-work-plugins | kardes-eksik | smb-onboard (smb-onboard) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:41 ../smb-onboard/reference/website-research.md; SKILL.md:83 ../… |
| breakdown-to-next-report | anthropics/claude-plugins-official | kardes-eksik | breakdown-diagnosis (breakdown-diagnosis) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:206 ../breakdown-diagnosis/SKILL.md |
| build-mcp-app | anthropics/claude-plugins-official | kardes-eksik | build-mcp-server (build-mcp-server) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:59 ../build-mcp-server/references/elicitation.md |
| canva-creator | anthropics/knowledge-work-plugins | kardes-eksik | social-content-engine (social-content-engine) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:69 ../social-content-engine/reference/shopif… |
| canvas | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:20 ../wiki/references |
| daily-production-report | anthropics/claude-plugins-official | kardes-eksik | data-consolidate (data-consolidate) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:239 ../data-consolidate/reference/mismatch-classes.md |
| data-consolidate | anthropics/claude-plugins-official | kardes-eksik | onboarding (onboarding@anthropics) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:159 ../onboarding/reference/erp-scope.md |
| defuddle@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:21 ../wiki/references |
| design-space-explore | anthropics/claude-plugins-official | kardes-eksik | rfq-to-quote (rfq-to-quote) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/cad-adapter.md:81 ../../rfq-to-quote/reference/design-step.md |
| eas-simulator | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: references/run-your-app.md:228 ../../expo-overview/references/launch-… |
| executing-plans | obra/superpowers | kardes-eksik | subagent-driven-development (subagent-driven-development) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:126 ../subagent-driven-developme… |
| expo-dev-client | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:154 ../expo-overview/references/launch-without-dev-menu.md |
| expo-web-to-native | expo/skills | kardes-eksik | expo-overview (expo-overview) kardeş skill gerekli; kurulursa kardeşle düzelir: references/verify-on-device.md:32 ../../expo-overview/references/laun… |
| founder-offer | Jakeschincariol/founder-skill | kardes-eksik | founder-board (founder-board) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:19 ../founder-board/lenses.md |
| founder-pricing | Jakeschincariol/founder-skill | kardes-eksik | founder-cfo (founder-cfo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:58 ${CLAUDE_SKILL_DIR}/../founder-cfo/unit_economics.py |
| gke-cluster-creation | google/skills | kardes-eksik | gke-golden-path (gke-golden-path) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:120 ../gke-golden-path/assets/golden-path-autopilot.yaml |
| growth-pulse | anthropics/knowledge-work-plugins | kardes-eksik | ad-manager (ad-manager) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/data_sources.md:46 ../../ad-manager/SKILL.md |
| hyperframes-cli | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:31 ../hyperframes/references/captions.md; SKILL.md:103 ../hyperf… |
| hypogenic | K-Dense-AI/scientific-agent-skills | kardes-eksik | hypothesis-generation (hypothesis-generation) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:31 ../hypothesis-generation/SKILL.md |
| idea-creator | wanshuiyin/Auto-claude-code-research-in-sleep | kardes-eksik | research-wiki (research-wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:81 ../research-wiki/SKILL.md |
| inspection-to-capa | anthropics/claude-plugins-official | kardes-eksik | ncr-writeup (ncr-writeup) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:187 ../ncr-writeup/SKILL.md |
| marketing-monday | anthropics/knowledge-work-plugins | kardes-eksik | growth-pulse (growth-pulse) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:9 ../growth-pulse/reference/data_sources.md |
| media-use | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: references/local.md:25 ../../hyperframes/references/captions.md |
| monday-brief | anthropics/knowledge-work-plugins | kardes-eksik | report-builder (report-builder) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:28 ../report-builder/reference/saved_reports.md |
| morning-plant-pulse | anthropics/claude-plugins-official | kardes-eksik | daily-production-report (daily-production-report) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:193 ../daily-production-report/SKILL.md;… |
| mp-test-setup | mercadopago/mercadopago-claude-marketplace | kardes-eksik | mp-integrate (mp-integrate) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:120 ${CLAUDE_PLUGIN_ROOT}/skills/mp-integrate/references/produ… |
| obsidian-bases@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:26 ../wiki/references |
| obsidian-markdown@agricidaniel | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:22 ../wiki/references |
| onboarding@anthropics | anthropics/claude-plugins-official | kardes-eksik | custom-connector (custom-connector) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:45 ../custom-connector/reference/known-systems.md; SKI… |
| quote-build | anthropics/claude-plugins-official | kardes-eksik | design-space-explore (design-space-explore) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/hours-ladder.md:128 ../../design-space-explor… |
| react-scan | remotion-dev/remotion | kardes-eksik | studio-perf (studio-perf) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:70 ../studio-perf/SKILL.md |
| remotion-to-hyperframes | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:45 ../hyperframes/references/runtimes.md |
| replica-brand | Jakeschincariol/replica-skill | kardes-eksik | replica-design (replica-design) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:66 ../replica-design/contrast.py |
| replica-deploy | Jakeschincariol/replica-skill | kardes-eksik | replica-brand (replica-brand) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:34 ../replica-brand/sweep.py |
| research-refine-pipeline | wanshuiyin/Auto-claude-code-research-in-sleep | kardes-eksik | experiment-plan (experiment-plan) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:39 ../experiment-plan/SKILL.md |
| rfq-to-quote | anthropics/claude-plugins-official | kardes-eksik | customer-inquiry-intake (customer-inquiry-intake) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:321 ../customer-inquiry-intake/SKILL.md |
| save | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:32 ../wiki/references |
| seo-content-brief | AgriciDaniel/claude-seo | kardes-eksik | seo (seo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:134 ${CLAUDE_PLUGIN_ROOT}/skills/seo/references/quality-gates.md |
| seo-local | AgriciDaniel/claude-seo | kardes-eksik | seo (seo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:61 ${CLAUDE_PLUGIN_ROOT}/skills/seo/references/local-schema-types.md; SKILL.md:1… |
| seo-maps | AgriciDaniel/claude-seo | kardes-eksik | seo (seo) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:54 ${CLAUDE_PLUGIN_ROOT}/skills/seo/references/maps-free-apis.md; SKILL.md:59 ${… |
| skill-development | anthropics/claude-plugins-official | kardes-eksik | agent-development (agent-development) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:610 ../agent-development/ |
| skill-development@anthropics | anthropics/claude-code | kardes-eksik | agent-development (agent-development@anthropics) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:610 ../agent-development/ |
| smb-router | anthropics/knowledge-work-plugins | kardes-eksik | cash-flow-snapshot (cash-flow-snapshot) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/connector-map.md:45 ../../cash-flow-snapshot/refe… |
| style-sampling | heygen-com/hyperframes | kardes-eksik | hyperframes (hyperframes) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:30 ../hyperframes/references/look.md |
| supplier-escape-to-alternate-source | anthropics/claude-plugins-official | kardes-eksik | ncr-writeup (ncr-writeup) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:201 ../ncr-writeup/SKILL.md |
| supplier-quote-request | anthropics/claude-plugins-official | kardes-eksik | onboarding (onboarding@anthropics) kardeş skill gerekli; kurulursa kardeşle düzelir: reference/supplier-loop.md:17 ../../onboarding/reference/config-… |
| update-ffmpeg | remotion-dev/remotion | kardes-eksik | pr (pr@remotion-dev) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:38 ../pr/SKILL.md |
| wiki-cli | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:21 ../wiki/references |
| wiki-fold | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:22 ../wiki/references |
| wiki-ingest | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:23 ../wiki/references |
| wiki-lint | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:20 ../wiki/references |
| wiki-mode | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:24 ../wiki/references |
| wiki-query | AgriciDaniel/claude-obsidian | kardes-eksik | wiki (wiki) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:27 ../wiki/references |
| yt-audit | Jakeschincariol/youtube-agent-skill | kardes-eksik | yt-package (yt-package) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:26 ../yt-package/title.py |
| yt-shorts | Jakeschincariol/youtube-agent-skill | kardes-eksik | yt-script (yt-script) kardeş skill gerekli; kurulursa kardeşle düzelir: SKILL.md:28 ../yt-script/hookscore.py |

## Paket gerekli (113)

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
| claude-security | anthropics/claude-plugins-official | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:21 ${CLAUDE_PLUGIN_ROOT}/scripts/render_report.p… |
| code-review@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| consistency-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| content-audit | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-architecture | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-control-manifest | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-epics | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| create-stories | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| cut | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| design-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| design-system@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| design-taste-frontend | Leonxlnx/taste-skill | eklenti-koku, yol-yerellestirme | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:18 $CLAUDE_PLUGIN_ROOT/scripts/gate.mjs; referen… |
| dev-story | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:11 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| egm-bootstrap | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:11 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-brainstorm | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:16 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-draft | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-drift-report | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-lite | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:17 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-resolve | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-review | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:15 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| egm-review-loop | google/elephant-goldfish-model | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:17 ${CLAUDE_PLUGIN_ROOT}/docs/claude.md |
| gate-check | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| geo | zubair-trabzada/geo-seo-claude | genel-yol | kendi genel klasöründen dosya bekliyor, bu dosyalar arşivde yok: SKILL.md:195 ~/.claude/skills/geo/templates; SKILL.md:205 ~/.claude/skills/geo/templ… |
| geo-report-pdf | zubair-trabzada/geo-seo-claude | kardes-eksik | geo: dosya arşivde yok: SKILL.md:26 ~/.claude/skills/geo/templates/geo-report-template.html; SKILL.md:59 ~/.claude/skills/geo/templates/geo-report-te… |
| geo-schema | zubair-trabzada/geo-seo-claude | kardes-eksik | geo: dosya arşivde yok: SKILL.md:31 ~/.claude/skills/geo/scripts/fetch_page.py |
| geo-update | zubair-trabzada/geo-seo-claude | genele-yazabilir, kardes-eksik | bilgisayar geneli skill/agent klasörüne dosya kopyalıyor: SKILL.md:64 cp -r "$SOURCE_DIR/geo/"* "$CLAUDE_DIR/skills; SKILL.md:69 mkdir -p "$CLAUDE_DI… |
| launch-checklist | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| localize | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| map-systems | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| mcp-integration | anthropics/claude-plugins-official | eklenti-koku, istisna-eskidi | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:30 ${CLAUDE_PLUGIN_ROOT}/servers/db-server; SKIL… |
| milestone-review | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| mp-commerce-checkout | mercadopago/mercadopago-claude-marketplace | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:182 ${CLAUDE_PLUGIN_ROOT}/templates/mp_checkout_… |
| mp-integrate | mercadopago/mercadopago-claude-marketplace | eklenti-koku, yol-yerellestirme | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:111 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve-checko… |
| next-step | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:23 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh; SKILL.md:246 ${CLAUDE_SK… |
| onboard | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| patch-notes | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| perf-profile | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh; SKILL.md:85 ${CLAUDE_SKI… |
| playtest-report | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| project-settings | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:53 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| project-stage-detect | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:24 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| propagate-design-change | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| prototype@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:9 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| qa-plan | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| quick-design | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| regression-suite | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| release-checklist | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:9 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| retrospective | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| reverse-document | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:44 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| review-all-gdds | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| security-audit@donchitos | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| seo | AgriciDaniel/claude-seo | eklenti-koku, genel-yol, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:18 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-agentic | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:46 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-audit@agricidaniel | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:17 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-backlinks | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:21 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-bing | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:35 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-cluster | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:80 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-content | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:146 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SK… |
| seo-dataforseo | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:51 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-drift | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:98 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-ecommerce | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:42 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-flow | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:85 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-geo | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:337 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-google | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:32 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-hreflang | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: references/machine-translation-qa.md:45 ${CLAUDE_PLUGIN_R… |
| seo-images | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:67 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-page | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:22 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-programmatic | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:119 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-schema | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:19 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-shopify | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:47 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-sitemap | AgriciDaniel/claude-seo | eklenti-koku, kardes-eksik | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:24 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo |
| seo-sxo | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:43 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
| seo-technical | AgriciDaniel/claude-seo | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:23 ${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo; SKI… |
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
| write-changelog | Donchitos/Claude-Code-Game-Studios | skil-disi-yol | skill klasörünün dışına çıkan yol, hedef dosya arşive alınmamış: SKILL.md:10 ${CLAUDE_SKILL_DIR}/../../hooks/yaml-helper.sh |
| writing-hookify-rules | anthropics/claude-plugins-official | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:324 ${CLAUDE_PLUGIN_ROOT}/examples |
| writing-hookify-rules@anthropics | anthropics/claude-code | eklenti-koku | eklenti kökündeki dosyalara dayanıyor, arşive alınmamış; düz kurulumda bu adımlar çalışmaz: SKILL.md:324 ${CLAUDE_PLUGIN_ROOT}/examples |

## Çözülemez (6)

_otomatik çevrilmiyor ya da hedef bulunamıyor: elle bakılmalı._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| app-store | rshankras/claude-code-apple-skills | genel-yol | ortak dizine (_shared gibi) dayanıyor: iap-finalizer/SKILL.md:25 ../../_shared/asc-api/asc.py; iap-finalizer/SKILL.md:27 ~/.claude/skills/_shared/asc… |
| edit-video | nateherkai/herk-edit-kit | genel-yol, kardes-eksik | göreli kardeş yolu (../<skill>/…) aynı repoda tek aday olarak çözülemedi, düz kurulumda kırılır: SKILL.md:28 ../hyperframes/SKILL.md (kütüphanede baş… |
| engineering-drawing | earthtojake/text-to-cad | genel-yol | göreli kardeş yolu (../<skill>/…) aynı repoda tek aday olarak çözülemedi, düz kurulumda kırılır: SKILL.md:44 ../PDF/enclosure_drawing.pdf (kütüphaned… |
| graphify | Graphify-Labs/graphify | genel-yol | kendi sabit yolu otomatik çevrilmiyor (betik içinde / kurulum dosyasında / karışık ya da kurulum anlatan dosyada): install.py:553 ~/.claude/skills/gr… |
| hatch-pet | nexu-io/open-design | genel-yol | kendi genel klasörünü bir değişkene atıyor (sonraki betik yolları buna dayanabilir), otomatik çevrilmiyor: SKILL.md:149 ${CODEX_HOME:-$HOME/.codex}/s… |
| iap-finalizer | rshankras/claude-code-apple-skills | genel-yol | ortak dizine (_shared gibi) dayanıyor: SKILL.md:27 ~/.claude/skills/_shared/asc-api/asc.py |

## İstisna (8)

_yol-istisnalari.json kaydıyla kapsanmış._

| Skill | Repo | Kodlar | İlk neden |
|---|---|---|---|
| command-development | anthropics/claude-plugins-official | yol-istisna | 81 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| command-development@anthropics | anthropics/claude-code | yol-istisna | 81 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| create-cowork-plugin | anthropics/knowledge-work-plugins | yol-istisna | 3 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| hook-development | anthropics/claude-plugins-official | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| hook-development@anthropics | anthropics/claude-code | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| mcp-integration@anthropics | anthropics/claude-code | yol-istisna | 12 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| plugin-structure | anthropics/claude-plugins-official | yol-istisna | 21 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |
| plugin-structure@anthropics | anthropics/claude-code | yol-istisna | 21 bulgu istisna kaydıyla kapsandı (eklenti-kok-yol; kayıt: yol-istisnalari.json) |

## Genel klasöre dosya kopyalayabilen skiller (2)

Ajan dosyasında `cp / ln -s / mkdir -p / git clone … ~/.claude/skills` satırı var (sütunlardan bağımsız bilgi).

firebase-basics, geo-update

## Sonraki tur adayı: eklenti kökü dosyalarını arşive almak (`ek_dosyalar`)

Bu turda YAPILMADI: kök dosyaları (scripts/, docs/, templates/ …) çekmek lisans ve ücret sınıflandırması onayı ister (`ucret-siniflandirma.json`, `notlar/ucretli-skiller.md`). Aday sayısı repo bazında:

| Repo | Skill |
|---|---:|
| AgriciDaniel/claude-seo | 22 |
| Donchitos/Claude-Code-Game-Studios | 69 |
| Leonxlnx/taste-skill | 1 |
| Viniciuscarvalho/swift-code-reviewer-skill | 1 |
| anthropics/claude-code | 1 |
| anthropics/claude-plugins-official | 3 |
| anthropics/knowledge-work-plugins | 2 |
| google/elephant-goldfish-model | 8 |
| mercadopago/mercadopago-claude-marketplace | 2 |
| zubair-trabzada/geo-seo-claude | 4 |
