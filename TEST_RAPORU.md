# Skill Test Raporu

Tarih: 2026-11-22 · Araç: `python3 araclar/skill-calistir.py` · Kütüphaneyi ve global skill klasörlerini değiştirmez.

## Nasıl test edildi
Her skill (Claude ve Codex sürümü ayrı ayrı) **gerçek kurulum yoluyla** (`skill-ekle.py` → `hazirla()`: ad eşitleme, frontmatter/description onarımı) geçici bir projeye kuruldu ve şunlar sınandı:

| Adım | Ne bakılır | Sonuç türü |
|---|---|---|
| Yükleme | Frontmatter ilk satırda, YAML ayrışıyor, `name` = klasör adı, `description` 40–1024 karakter | HATA |
| Betik | `.py` derlenir (çalıştırılmaz), `.sh` → `bash -n`, `.js/.mjs/.cjs` → `node --check`, `.json` ayrıştırılır | HATA |
| Bağlantı | SKILL.md'nin göreli bağlantıları ve `scripts/…` gibi paket içi yollar kurulan kopyada var mı | UYARI |
| Örnek görev | Elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki "Use when …" | rapora yazılır |
| Agent (örneklem) | Skill boş projeye kurulur, `claude -p` örnek görevle **sadece okuma araçlarıyla** çalıştırılır; Skill aracıyla bu skill'i yükledi mi | tetiklendi / tetiklenmedi |

**Neden her skill gerçek agent'la değil:** 3815 skill × bir agent oturumu saatler ve ciddi API maliyeti demek; üstelik skillerin çoğu dış servis, API anahtarı ya da kullanıcı projesi ister. Bu yüzden tüm skiller otomatik kontrolden, kategorilerden seçilen bir örneklem de gerçek agent'tan geçti.

## Özet
| | Sayı |
|---|---|
| Test edilen skill | 2930 |
| ✅ Geçti | 2655 |
| ⚠️ Uyarı (çalışır, eksik dosya bağlantısı var) | 272 |
| ❌ Hata | 3 |
| Sözdizimi denetlenen dosya | py 1785 · sh 134 · js 747 · json 1420 |

## 🔧 Bulunan ve düzeltilen hatalar
Hepsi **kurulan kopyada** düzeltilir; `arsiv/` altındaki orijinaller değişmez. Bu düzeltmeler olmadan aşağıdaki skiller ❌ çıkıyordu.

| Hata | Skill | Düzeltme |
|---|---|---|
| Betik çalışmıyor: f-string içinde JSX süslü parantezleri kaçırılmamış: betik SyntaxError veriyordu ({{ }} ile düzeltildi) | `react-three-fiber` | `yamalar/react-three-fiber/` (scripts/component_generator.py); yamalı betik örnek görevle çalıştırıldı, üretilen TSX derlendi |
| Betik çalışmıyor: Durum klasörü ev dizinine (~/etsy-listings) değil proje köküne (./etsy-listings, ETSY_LISTINGS_DIR ile değiştirilebilir) yazılır; kaynak repoda skill klasörü dışında kalan 4 şablon bootstrap.py içine gömüldü (yoksa betik 'Templates dir not found' ile duruyordu); 2026-11-07b: SCHEMA.md ve scripts/README.md'deki yol metinleri de düzeltildi | `etsy-seller` | `yamalar/etsy-seller/` (SKILL.md, references/playbooks/system-laws.md, references/playbooks/listing-health-score.md, scripts/bootstrap.py, references/data-model/SCHEMA.md, scripts/README.md); yamalı betik örnek görevle çalıştırıldı, üretilen TSX derlendi |
| Kaynaktaki git symlink'leri arşive düz metin olarak gelmiş (12 dosya, ör. `remotion-maps` → `../remotion-maps`): SKILL.md'deki alt-skill bağlantıları ölüydü | `remotion-best-practices` | Kurulumda taslak silinir, bağlantılar kardeş skill'e çevrilir; kardeş kurulmazsa ön kontrol `kardes-eksik` uyarır |
| Kaynaktaki git symlink'leri arşive düz metin olarak gelmiş (1 dosya, ör. `remotion-maps` → `../remotion-maps`): SKILL.md'deki alt-skill bağlantıları ölüydü | `remotion-markup` | Kurulumda taslak silinir, bağlantılar kardeş skill'e çevrilir; kardeş kurulmazsa ön kontrol `kardes-eksik` uyarır |
| Claude hesabındaki aynı adlı skill (`anthropic-skills:<ad>`) kütüphane sürümünün yerine seçiliyordu (agent testinde `docx`). Bu makinede ad çakışması: `docs`, `docx`, `pdf`, `pptx`, `skill-creator`, `xlsx`, `youtube-arama` | 7 skill | Kurulumda proje `.claude/settings.json` → `skillOverrides` ile hesaptaki o projede `off`; ön kontrol `hesap-cakismasi` bildirir, `--dogrula` denetler. Düzeltmeden sonra `docx` agent testi ✅ |
| Description yok / çok kısa / 1024'ten uzun: agent skill'i doğru durumda seçemiyordu | 59 skill | `registry.json` → `aciklama_duzeltme` (`notlar/tetiklenme-denetimi.md`) |
| Frontmatter HTML yorumunun arkasında ya da description YAML'ı bozuyor | 20 skill | Kurulumda kendiliğinden |

## ❌ Hatalar
| Skill | Kategori | Hata |
|---|---|---|
| `ios-to-android` | b-yazilim-gelistirme/08-mobil-uygulama | description 1027 karakter > 1024 (Codex yüklemez) |
| `agent-platform-agent-registry` | d-ai-otomasyon/01-claude-api-mcp | scripts/quick-add-gcp-service.sh: bash -n: /Users/sabanulukaya/Documents/SkillKutuphanesi/.gecici/skill-test-7d6ulx10/agent-platform-agent-registry/ana/agent-platform-agent-registry/scripts/quick-add-gcp-service.sh: line 66: `  elif [[ -v CLOU |
| `earshot` | g-video-ses-medya/02-ses-muzik-konusma | description 1327 karakter > 1024 (Codex yüklemez) |

## ⚠️ Uyarılar (272)
Skill yüklenir ve çalışır; SKILL.md'nin andığı bazı dosyalar pakette yok (çoğu kaynak repoda da yok ya da kullanıcının projesindeki bir dosyayı gösteriyor).

<details><summary>Liste</summary>

| Skill | Uyarı |
|---|---|
| `accessibility-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `design-critique` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `design-handoff` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `design-system@anthropics` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `research-synthesis` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `ui-styling` | SKILL.md'nin andığı 1 dosya pakette yok: assets/design-tokens.json |
| `ui-ux-pro-max@nexu-io` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/search.py |
| `ux-copy` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `web-clone` | SKILL.md'nin andığı 1 dosya pakette yok: assets/fonts/fonts.css |
| `brand` | SKILL.md'nin andığı 2 dosya pakette yok: assets/design-tokens.css, assets/design-tokens.json |
| `design` | SKILL.md'nin andığı 1 dosya pakette yok: assets/design-tokens.json |
| `design-system@nextlevelbuilder` | SKILL.md'nin andığı 3 dosya pakette yok: assets/css/slide-animations.css, assets/design-tokens.css, assets/design-tokens.json |
| `animated-component-libraries` | SKILL.md'nin andığı 1 dosya pakette yok: lib/utils.ts |
| `scroll-reveal-libraries` | SKILL.md'nin andığı 1 dosya pakette yok: references/integration_patterns.md |
| `lightweight-3d-effects` | SKILL.md'nin andığı 1 dosya pakette yok: illo |
| `react-three-fiber` | SKILL.md'nin andığı 2 dosya pakette yok: references/drei_helpers.md, references/hooks_guide.md |
| `hatch-pet` | SKILL.md'nin andığı 1 dosya pakette yok: references/canonical-base.png |
| `localize` | SKILL.md'nin andığı 1 dosya pakette yok: assets/data/strings/strings-en.json |
| `map-systems` | SKILL.md'nin andığı 1 dosya pakette yok: templates/systems-index.md |
| `reverse-document` | SKILL.md'nin andığı 3 dosya pakette yok: templates/architecture-doc-from-code.md, templates/concept-doc-from-prototype.md, templates/design-doc-from-implementation.md |
| `slides` | SKILL.md'nin andığı 1 dosya pakette yok: assets/design-tokens.json |
| `architecture@anthropics` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `code-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `debug` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `deploy-checklist` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `egm-bootstrap` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, ./child/${target_filename} |
| `egm-brainstorm` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/codex.md |
| `egm-draft` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, resources/execution_instructions.md |
| `egm-drift-report` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/codex.md |
| `egm-lite` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/codex.md |
| `egm-resolve` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, [RelativePath] |
| `egm-review` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, resources/document_standards/zoom-out-standard.md |
| `egm-review-loop` | SKILL.md'nin andığı 3 dosya pakette yok: ../../docs/codex.md, resources/document_standards/feature-spec-standard.md, resources/document_standards/implementation-readiness-standard.md |
| `incident-response` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `standup` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `wayfinder` | SKILL.md'nin andığı 1 dosya pakette yok: link |
| `cloud-monitoring-alert-configuration` | SKILL.md'nin andığı 3 dosya pakette yok: references/app_hub_labels.md, references/promql_templates.md, references/service_metrics.md |
| `cloudflare` | SKILL.md'nin andığı 1 dosya pakette yok: references/mcp.md |
| `m5-onboard` | SKILL.md'nin andığı 9 dosya pakette yok: references/hardware_signatures.md, references/uiflow2_nvs.md, scripts/detect.py, scripts/fetch_firmware.py |
| `playwright-cli` | SKILL.md'nin andığı 1 dosya pakette yok: .playwright-cli/page-2026-02-14T19-22-42-679Z.yml |
| `android-cli` | SKILL.md'nin andığı 1 dosya pakette yok: path/to/screenshot |
| `expo-overview` | SKILL.md'nin andığı 1 dosya pakette yok: references/native-ios.md |
| `flutter-animations` | SKILL.md'nin andığı 1 dosya pakette yok: lib/main.dart |
| `flutter-pre-caching` | SKILL.md'nin andığı 2 dosya pakette yok: assets/assets/images/logo.png, assets/images/logo.png |
| `ios-marketing-capture` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/capture-marketing.sh |
| `documentation-templates` | SKILL.md'nin andığı 2 dosya pakette yok: ./docs/api.md, ./docs/architecture.md |
| `obsidian-bases@agricidaniel` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/native-conformance.md |
| `obsidian-markdown` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `obsidian-markdown@heyitsnoah` | SKILL.md'nin andığı 2 dosya pakette yok: Note%20Name.md, obsidian://open |
| `obsidian-markdown@kepano` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `save` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/workflow-acceptance.md |
| `wiki` | SKILL.md'nin andığı 3 dosya pakette yok: ../../docs/capacity-and-recovery.md, ../../docs/native-conformance.md, ../../docs/upstream-references.md |
| `wiki-ingest` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/workflow-acceptance.md, url |
| `wiki-mode` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/wiki-mode.py |
| `wiki-retrieve` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/prefix-providers.md, ../../docs/retrieval-evaluation.md |
| `academy-guide` | SKILL.md'nin andığı 1 dosya pakette yok: URL |
| `agent-platform-access-audit` | SKILL.md'nin andığı 1 dosya pakette yok: ... |
| `graphify` | SKILL.md'nin andığı 8 dosya pakette yok: references/add-watch.md, references/exports.md, references/extraction-spec.md, references/github-and-merge.md |
| `od-next-media-inputs` | SKILL.md'nin andığı 1 dosya pakette yok: assets/stock/credits.json |
| `skill-creator@freshtechbro` | SKILL.md'nin andığı 9 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, references/api_docs.md |
| `skill-development` | SKILL.md'nin andığı 16 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, examples/script.sh |
| `skill-development@anthropics` | SKILL.md'nin andığı 16 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, examples/script.sh |
| `writing-skills` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/tool.sh |
| `caption-qa` | SKILL.md'nin andığı 1 dosya pakette yok: \d{1,3} |
| `add-sfx` | SKILL.md'nin andığı 1 dosya pakette yok: ./packages/remotion-media |
| `archify-review` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../CONTRIBUTING.md, ../../../REVIEWING.md |
| `archify-tuning` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../CONTRIBUTING.md |
| `deploy-release-test` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../contributing/core/testing.md |
| `gate-tests` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../test/lib/gate/README.md |
| `interactivity-best-practices` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../packages/docs/docs/studio/interactivity-best-practices.mdx, ../../../packages/docs/docs/studio/make-component-interactive.mdx |
| `playwright-bisect-chromium` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../AGENTS.md, ../../../utils/bisect-chromium.mjs |
| `playwright-dev` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../AGENTS.md |
| `playwright-release-notes` | SKILL.md'nin andığı 3 dosya pakette yok: ./images/foo.png, ./test-parallel.md, [^(]/$ |
| `playwright-triage` | SKILL.md'nin andığı 3 dosya pakette yok: ../../../.github/actions/run-agent/guides/triage.md, ../../../.github/workflows/triage.yml, ../../../AGENTS.md |
| `pr-status-triage` | SKILL.md'nin andığı 2 dosya pakette yok: scripts/pr-status/results/index.md, scripts/pr-status/results/thread-N.md |
| `pr@remotion-dev` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../packages/docs/docs/contributing/elements.mdx |
| `remotion-new-markup` | SKILL.md'nin andığı 3 dosya pakette yok: ../../../packages/skills/skills/remotion-interactivity/timeline-structure.md, ../../../packages/skills/skills/remotion-markup/connected-compositions.md, ../../../packages/skills/skills/remotion-markup/video-editing.md |
| `scaffold-element` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../packages/docs/docs/contributing/elements.mdx, ../../../packages/docs/docs/elements.mdx |
| `studio-checklist` | SKILL.md'nin andığı 10 dosya pakette yok: ../../../packages/browser-studio/e2e/browser-studio.test.ts, ../../../packages/docs/docs/ai/webmcp.mdx, ../../../packages/studio/src/components/ActionTooltip.tsx, ../../../packages/studio/src/components/InspectorPanel/optimistic-composition-metadata.ts |
| `studio-dev` | SKILL.md'nin andığı 10 dosya pakette yok: ../../../packages/browser-studio/e2e/browser-studio.test.ts, ../../../packages/docs/docs/ai/webmcp.mdx, ../../../packages/studio/src/components/ActionTooltip.tsx, ../../../packages/studio/src/components/InspectorPanel/optimistic-composition-metadata.ts |
| `studio-diagnostics` | SKILL.md'nin andığı 6 dosya pakette yok: ../../../packages/core/src/buffering.tsx, ../../../packages/core/src/playback-diagnostics.ts, ../../../packages/core/src/use-buffer-state.ts, ../../../packages/docs/docs/ai/webmcp.mdx |
| `update-ffmpeg` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../packages/compositor/ffmpeg/README.md |
| `update-trace-engine` | SKILL.md'nin andığı 3 dosya pakette yok: scripts/trace/copy-build-trace-engine-for-publish.sh, scripts/trace/prep-trace-engine-package.sh, scripts/trace/test/test-trace-engine.mjs |
| `brag` | SKILL.md'nin andığı 4 dosya pakette yok: references/format.md, references/look.md, references/motion.md, references/story.md |
| `captions-overlay` | SKILL.md'nin andığı 1 dosya pakette yok: references/captions.md |
| `cut-silences` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/validate-beat-sync.mjs<br>[codex] SKILL.md'nin andığı 1 dosya pakette yok: scripts/validate-beat-sync.mjs |
| `moviepy` | SKILL.md'nin andığı 3 dosya pakette yok: examples/data-viz-chart/README.md, examples/data-viz-chart/build.py, examples/quick-spot/build.py |
| `parody-short` | SKILL.md'nin andığı 1 dosya pakette yok: lib/components/LivingPhoto.tsx |
| `prod-by-claude` | SKILL.md'nin andığı 1 dosya pakette yok: assets/bgm.wav |
| `remotion-best-practices@calesthio` | SKILL.md'nin andığı 1 dosya pakette yok: ./rules/sound-effects.md |
| `short-form-edit` | SKILL.md'nin andığı 4 dosya pakette yok: assets/edit-decisions.json, assets/footage-ledger.json, assets/plan.json, assets/transcript.json<br>[codex] SKILL.md'nin andığı 4 dosya pakette yok: assets/edit-decisions.json, assets/footage-ledger.json, assets/plan.json, assets/transcript.json |
| `short-form-video` | SKILL.md'nin andığı 2 dosya pakette yok: references/captions.md, scripts/transcribe-elevenlabs.mjs |
| `style-library` | SKILL.md'nin andığı 1 dosya pakette yok: assets/source.mp4 |
| `synthetic-screen-recording` | SKILL.md'nin andığı 1 dosya pakette yok: lib/verify_scene_pacing.py |
| `synthetic-ui-demo` | SKILL.md'nin andığı 2 dosya pakette yok: lib/components/cues.ts, templates/ds-release-notes/src/scenes/FreeCustomLink.tsx |
| `tiktok-upload` | SKILL.md'nin andığı 2 dosya pakette yok: examples/get_tk_cookie.py, examples/upload_video_to_tiktok.py |
| `video-design` | SKILL.md'nin andığı 1 dosya pakette yok: lib/components/DataChart.tsx |
| `video_toolkit` | SKILL.md'nin andığı 2 dosya pakette yok: lib/components/DataChart.tsx, templates/howto/README.md |
| `xueqiu-upload` | SKILL.md'nin andığı 1 dosya pakette yok: images/chart.png |
| `zhihu-upload` | SKILL.md'nin andığı 1 dosya pakette yok: images/1.png |
| `elevenlabs` | SKILL.md'nin andığı 2 dosya pakette yok: assets/voices/library-shortlist.json, templates/howto/scripts/accent.py |
| `elevenlabs@openmontageinc` | [codex] SKILL.md'nin andığı 1 dosya pakette yok: ../provider-refresh-oct23/SKILL.md |
| `text-to-speech` | [codex] SKILL.md'nin andığı 1 dosya pakette yok: ../provider-refresh-oct23/SKILL.md |
| `blender` | SKILL.md'nin andığı 12 dosya pakette yok: examples/blender-disk-panic/spec.json, examples/blender-in-remotion/src/Video.tsx, examples/blender-product-shot/spec.json, lib/blender/cameras.py |
| `manimgl-best-practices` | SKILL.md'nin andığı 5 dosya pakette yok: examples/3d_visualization.py, examples/basic_animations.py, examples/graph_plotting.py, examples/math_visualization.py |
| `account-research` | SKILL.md'nin andığı 1 dosya pakette yok: references/my-company-context.md |
| `ads-landing` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/fetch_page.py |
| `brand-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `call-prep` | SKILL.md'nin andığı 1 dosya pakette yok: references/my-company-context.md |
| `campaign-plan` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `competitive-brief` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `compose-outreach` | SKILL.md'nin andığı 1 dosya pakette yok: references/my-company-context.md |
| `customer-escalation` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `customer-research` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `draft-content` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `draft-response` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `email-sequence` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `geo-llmstxt` | SKILL.md'nin andığı 1 dosya pakette yok: URL |
| `kb-article` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `link-building` | SKILL.md'nin andığı 6 dosya pakette yok: ../../tools/integrations/ahrefs.md, ../../tools/integrations/dataforseo.md, ../../tools/integrations/exa.md, ../../tools/integrations/firecrawl.md |
| `performance-report` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `seo-audit` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `seo-geo` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `ticket-triage` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `brief` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `comp-analysis` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `compliance-check` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `draft-offer` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `financial-statements` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `journal-entry` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `legal-response` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `onboarding` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `people-report` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `performance-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `policy-lookup` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `review-contract` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `signature-request` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `sox-testing` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `triage-nda` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `vendor-check` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `ad-manager` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `ap-processor` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `build-connector` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/connector-neutrality.md |
| `capacity-plan` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `change-request` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `competitive-brief@anthropics` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `crm-autopilot` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `digest` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `grant-rfp-writer` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `hiring-screener` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `inbox-manager` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `inventory-planner` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `invoice-chase` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `lead-triage@anthropics` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `metrics-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `outreach-composer` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `process-doc` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `proposal-builder` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `review-reputation` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `roadmap-update` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `runbook` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `search` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `search-strategy` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `seo-ai-visibility` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `slack-messaging` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `social-content-engine` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `source-management` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `speed-to-lead` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `sprint-planning` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `stakeholder-update` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `start@anthropics` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `status-report` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `synthesize-research` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `ticket-deflector` | SKILL.md'nin andığı 1 dosya pakette yok: ../../shared/voice-profile.md |
| `update` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `vendor-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `write-spec` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `analyze` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `build-dashboard` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `create-viz` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `explore-data` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `validate-data` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `write-query` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `ecommerce-competitor-analyzer` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/detect-platform.js |
| `mp-test-setup` | SKILL.md'nin andığı 1 dosya pakette yok: references/products.md |
| `shopify-admin-agentic-llms-txt` | SKILL.md'nin andığı 1 dosya pakette yok: assets/llms.txt |
| `shopify-hydrogen` | SKILL.md'nin andığı 4 dosya pakette yok: docs/api/hydrogen/latest/customer/createcustomeraccount, docs/api/hydrogen/latest/utilities/createcustomeraccountclient, docs/api/hydrogen/latest/utilities/createstorefrontclient, docs/api/hydrogen/utilities/createstorefrontclient<br>[codex] SKILL.md'nin andığı 4 dosya pakette yok: docs/api/hydrogen/latest/customer/createcustomeraccount, docs/api/hydrogen/latest/utilities/createcustomeraccountclient, docs/api/hydrogen/latest/utilities/createstorefrontclient, docs/api/hydrogen/utilities/createstorefrontclient |
| `storefront-theming` | SKILL.md'nin andığı 1 dosya pakette yok: assets/base.css |
| `wc-product-search-select` | SKILL.md'nin andığı 4 dosya pakette yok: class-wc-admin-assets.php, class-wc-ajax.php, class-wc-product-data-store-cpt.php, wc-enhanced-select.js |
| `wc-variation-gallery` | SKILL.md'nin andığı 1 dosya pakette yok: templates/single-product/add-to-cart/variable.php |
| `wc-variations-data` | SKILL.md'nin andığı 4 dosya pakette yok: class-wc-product-variable-data-store-cpt.php, class-wc-product-variable.php, class-wc-product-variation.php, wc-product-functions.php |
| `bulk-rnaseq` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/run_enrichment.py |
| `start` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `autoresearch` | SKILL.md'nin andığı 1 dosya pakette yok: references/citation-workflow.md |
| `blip-2-vision-language` | SKILL.md'nin andığı 3 dosya pakette yok: image, query, raw_image |
| `constitutional-ai` | SKILL.md'nin andığı 3 dosya pakette yok: references/constitution-design.md, references/cot-critique.md, references/rlaif-comparison.md |
| `guidance` | SKILL.md'nin andığı 1 dosya pakette yok: lm["action_input"] |
| `llamaguard` | SKILL.md'nin andığı 3 dosya pakette yok: references/benchmarks.md, references/custom-categories.md, references/deployment.md |
| `mamba-architecture` | SKILL.md'nin andığı 3 dosya pakette yok: references/mamba2-details.md, references/performance.md, references/selective-ssm.md |
| `moe-training` | SKILL.md'nin andığı 1 dosya pakette yok: expert_input |
| `nemo-guardrails` | SKILL.md'nin andığı 3 dosya pakette yok: references/colang-guide.md, references/integrations.md, references/performance.md |
| `optimizing-attention-flash` | SKILL.md'nin andığı 2 dosya pakette yok: references/advanced-features.md, references/algorithm.md |
| `ray-train` | SKILL.md'nin andığı 2 dosya pakette yok: references/custom-loops.md, references/hyperparameter-tuning.md |
| `segment-anything-model` | SKILL.md'nin andığı 2 dosya pakette yok: checkpoint="sam_vit_b_01ec64.pth", checkpoint="sam_vit_h_4b8939.pth" |
| `speculative-decoding` | SKILL.md'nin andığı 1 dosya pakette yok: references/draft_model.md |
| `verl-rl-training` | SKILL.md'nin andığı 1 dosya pakette yok: references/multi-turn.md |
| `alphaxiv` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/integration-contract.md |
| `arxiv` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/wiki-helper-resolution.md |
| `auto-paper-improvement-loop` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md |
| `auto-review-loop` | SKILL.md'nin andığı 6 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `auto-review-loop-llm` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `auto-review-loop-minimax` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `citation-audit` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md |
| `citation-crosscheck` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/acceptance-gate.md, ../shared-references/external-cadence.md, ../shared-references/fan-out-pattern.md, ../shared-references/integration-contract.md |
| `claims-drafting` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `deepxiv` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/wiki-helper-resolution.md |
| `dse-loop` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/external-cadence.md |
| `exa-search` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `exa-search@wanshuiyin` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/wiki-helper-resolution.md |
| `experiment-audit` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md |
| `experiment-bridge` | SKILL.md'nin andığı 6 dosya pakette yok: ../shared-references/compute-env-contract.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `experiment-plan` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `experiment-queue` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/external-cadence.md |
| `figure-spec` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/reviewer-backends.md |
| `firecrawl-search` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/citation-discipline.md, ../shared-references/integration-contract.md, ../shared-references/wiki-helper-resolution.md |
| `gemini-search` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `grant-proposal` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
| `idea-creator` | SKILL.md'nin andığı 10 dosya pakette yok: ../shared-references/acceptance-gate.md, ../shared-references/citation-discipline.md, ../shared-references/fan-out-pattern.md, ../shared-references/injection-hygiene.md |
| `idea-discovery` | SKILL.md'nin andığı 7 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-composition.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md |
| `idea-discovery-robot` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
| `interview-cheatsheet` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `invention-structuring` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `keenable-search` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/integration-contract.md |
| `kill-argument` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/fan-out-pattern.md, ../shared-references/reviewer-backends.md |
| `lean-formalize` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/fan-out-pattern.md, ../shared-references/reviewer-backends.md, ../shared-references/reviewer-routing.md |
| `meta-apply` | SKILL.md'nin andığı 5 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/review-scope-limits.md, ../shared-references/review-tracing.md, ../shared-references/reviewer-backends.md |
| `meta-optimize` | SKILL.md'nin andığı 8 dosya pakette yok: ../../templates/claude-hooks/corpus_write_guard.json, ../shared-references/acceptance-gate.md, ../shared-references/capture-antipatterns.md, ../shared-references/output-language.md |
| `monitor-experiment` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/external-cadence.md |
| `novelty-check` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/citation-discipline.md, ../shared-references/integration-contract.md, ../shared-references/reviewer-backends.md |
| `openalex` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/integration-contract.md |
| `paper-claim-audit` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md |
| `paper-figure` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `paper-illustration-image2` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/reviewer-backends.md |
| `paper-plan` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
| `paper-poster-html` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `paper-slides` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `paper-talk` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `paper-write` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `paper-writing` | SKILL.md'nin andığı 5 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `parallel-web` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `patent-novelty-check` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `patent-pipeline` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `patent-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `pixel-art` | SKILL.md'nin andığı 1 dosya pakette yok: filename.svg |
| `proof-checker` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/fan-out-pattern.md, ../shared-references/reviewer-backends.md |
| `rebuttal` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `render-html` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/reviewer-backends.md, url |
| `research-implement-feature` | SKILL.md'nin andığı 11 dosya pakette yok: ../shared-references/acceptance-gate.md, ../shared-references/capture-antipatterns.md, ../shared-references/effort-contract.md, ../shared-references/injection-hygiene.md |
| `research-lit` | SKILL.md'nin andığı 5 dosya pakette yok: ../shared-references/citation-discipline.md, ../shared-references/fan-out-pattern.md, ../shared-references/integration-contract.md, ../shared-references/output-composition.md |
| `research-pipeline` | SKILL.md'nin andığı 7 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md |
| `research-refine` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
| `research-refine-pipeline` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
| `research-review` | SKILL.md'nin andığı 3 dosya pakette yok: ../shared-references/external-cadence.md, ../shared-references/output-composition.md, ../shared-references/reviewer-backends.md |
| `research-wiki` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/capture-antipatterns.md, ../shared-references/integration-contract.md |
| `resubmit-pipeline` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `result-to-claim` | SKILL.md'nin andığı 4 dosya pakette yok: ../shared-references/evidence-precheck.md, ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md, ../shared-references/wiki-helper-resolution.md |
| `semantic-scholar` | SKILL.md'nin andığı 2 dosya pakette yok: ../shared-references/integration-contract.md, ../shared-references/wiki-helper-resolution.md |
| `slides-polish` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `specification-writing` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/reviewer-backends.md |
| `training-check` | SKILL.md'nin andığı 3 dosya pakette yok: ../../tools/watchdog.py, ../shared-references/external-cadence.md, ../shared-references/reviewer-backends.md |
| `wiki-enrich` | SKILL.md'nin andığı 1 dosya pakette yok: ../shared-references/output-language.md |
| `sendcutsend` | SKILL.md'nin andığı 1 dosya pakette yok: references/manufacturing-sheet-metal.md |

</details>

## Tüm skiller ve örnek görevleri
2930 skill'in tek tek sonucu ve örnek görevi, alana göre: [a-tasarim-onyuz](notlar/skill-ornek-gorevler/a-tasarim-onyuz.md) (273) · [b-yazilim-gelistirme](notlar/skill-ornek-gorevler/b-yazilim-gelistirme.md) (567) · [c-dokuman-icerik](notlar/skill-ornek-gorevler/c-dokuman-icerik.md) (106) · [d-ai-otomasyon](notlar/skill-ornek-gorevler/d-ai-otomasyon.md) (160) · [e-entegrasyon-katalogu](notlar/skill-ornek-gorevler/e-entegrasyon-katalogu.md) (1) · [f-repo-ici](notlar/skill-ornek-gorevler/f-repo-ici.md) (122) · [g-video-ses-medya](notlar/skill-ornek-gorevler/g-video-ses-medya.md) (208) · [h-is-alanlari](notlar/skill-ornek-gorevler/h-is-alanlari.md) (1110) · [i-bilim-muhendislik](notlar/skill-ornek-gorevler/i-bilim-muhendislik.md) (383)
