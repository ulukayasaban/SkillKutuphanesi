# Skill Test Raporu

Tarih: 2026-11-04 · Araç: `python3 araclar/skill-calistir.py` --ajan · Kütüphaneyi ve global skill klasörlerini değiştirmez.

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
| Test edilen skill | 5250 |
| ✅ Geçti | 4912 |
| ⚠️ Uyarı (çalışır, eksik dosya bağlantısı var) | 338 |
| ❌ Hata | 0 |
| Sözdizimi denetlenen dosya | py 2035 · sh 115 · js 608 · json 1405 |

## Gerçek agent testi (örneklem: 43 skill · model: varsayılan · tetiklenen 43/43 · maliyet ≈ $8.05 (12 koşu kayıtlı; diğerleri ≈ $0.67/koşu))
| Skill | Örnek görev | Sonuç | Yüklenen |
|---|---|---|---|
| `gsap-scrolltrigger` | Sayfayı kaydırırken ürün görseli pinlensin ve scroll ile birlikte dönsün (scrub). GSAP ScrollTrigger kodu yaz. | ✅ tetiklendi | gsap-scrolltrigger |
| `gsap-performance` | GSAP ile yaptığım 200 kartlık animasyon mobilde takılıyor, jank var. Nasıl optimize ederim? | ✅ tetiklendi | gsap-performance |
| `threejs-asset-pipeline` | Three.js sahneme 80 MB'lık bir GLB model yükleyeceğim; yüklemeden önce nasıl sıkıştırıp doğrularım (Draco/KTX2)? | ✅ tetiklendi | threejs-asset-pipeline |
| `2d-games` | Basit bir 2D platform oyunu yapıyorum; tilemap, sprite animasyonu ve takip eden kamera için hangi yapıyı kurmalıyım? | ✅ tetiklendi | 2d-games |
| `browser-testing-with-devtools` | Çalışan sayfamda konsol hataları ve yavaş ağ istekleri var; Chrome DevTools ile nasıl teşhis edip doğrularım? | ✅ tetiklendi | browser-testing-with-devtools |
| `brainstorming` | Uygulamama bir 'ekip davet etme' özelliği eklemek istiyorum ama gereksinimler net değil. Kod yazmadan önce birlikte netleştirelim. | ✅ tetiklendi | brainstorming |
| `code-review-and-quality` | Şu PR'daki değişiklikleri birleştirmeden önce incele: kalite, okunabilirlik ve olası hatalar açısından değerlendir. | ✅ tetiklendi | code-review-and-quality |
| `d3-viz` | D3 ile zoom ve sürükleme destekli force-directed bir ağ grafiği çiz: düğümler kişiler, kenarlar ilişkiler. | ✅ tetiklendi | d3-viz |
| `tailwind-design-system` | Tailwind v4 projemde Button, Input ve Card için token tabanlı bir bileşen sistemi kur; varyantlar CVA ile olsun. | ✅ tetiklendi | tailwind-design-system |
| `systematic-debugging` | Testlerim CI'da ara sıra kırılıyor, yerelde geçiyor. Düzeltme önermeden önce sebebini sistematik olarak bulalım. | ✅ tetiklendi | systematic-debugging |
| `finishing-a-development-branch` | Bu dalda tüm testler geçti. Şimdi dalı nasıl bitireyim: birleştirme mi, PR mı, worktree temizliği? | ✅ tetiklendi | finishing-a-development-branch |
| `security-and-hardening` | Kullanıcı kayıt ve giriş akışı yazdım; OWASP Top 10'a göre güvenlik açıklarını gözden geçir ve sertleştir. | ✅ tetiklendi | security-and-hardening |
| `next-cache-components-adoption` | Next.js projemde cacheComponents bayrağını açınca blocking-prerender hataları yağıyor. Nasıl geçiş yaparım? | ✅ tetiklendi | next-cache-components-adoption |
| `design-taste-frontend` | Bir yapay zeka not uygulaması için landing page tasarla; sıradan şablon gibi durmasın, karakterli olsun. | ✅ tetiklendi | design-taste-frontend<br><sub>ilk deneme: zaman aşımı (görev: Bir yapay zeka not uygulaması için landing page tasarla; sıradan şablo)</sub> |
| `api-and-interface-design` | Sipariş servisi için REST API tasarla: endpoint'ler, hata biçimi, sayfalama ve sürümleme kuralları. | ✅ tetiklendi | api-and-interface-design |
| `internal-comms` | Yönetime bu haftanın durum güncellemesini yaz: neler bitti, riskler, gelecek hafta. | ✅ tetiklendi | internal-comms |
| `add-frontmatter` | Obsidian kasamdaki notlara etiket ve özellik (frontmatter) ekleyerek Bases görünümleri için düzenle. | ✅ tetiklendi | add-frontmatter |
| `documentation-and-adrs` | Veritabanını PostgreSQL'den SQLite'a geçirme kararımızı belgeleyen bir mimari karar kaydı (ADR) yaz. | ✅ tetiklendi | documentation-and-adrs |
| `mcp-builder` | Şirketimizin iç REST API'sini Claude'a açan bir MCP sunucusu yazmak istiyorum. Nereden başlamalıyım? | ✅ tetiklendi | mcp-builder |
| `agent-reach` | Şu YouTube videosunun altyazısını çıkar ve özetle: https://www.youtube.com/watch?v=dQw4w9WgXcQ | ✅ tetiklendi | agent-reach<br><sub>ilk deneme: tetiklenmedi (görev: Şu YouTube videosunun altyazısını al ve konuyla ilgili X ile Reddit'te)</sub> |
| `docx` | Müşteriye gönderilecek 3 sayfalık bir hizmet sözleşmesini Word (.docx) dosyası olarak hazırla. | ✅ tetiklendi | docx |
| `context-engineering` | Agent'ımın çıktı kalitesi düştü; CLAUDE.md kural dosyasını ve bağlam yapısını nasıl düzenlemeliyim? | ✅ tetiklendi | context-engineering |
| `elevenlabs` | Tanıtım videom için Türkçe bir seslendirme (TTS) üret. | ✅ tetiklendi | elevenlabs |
| `writing-skills` | Agent'ların kod yazmadan önce test yazmasını sağlayan yeni bir skill yazmak istiyorum; işe yaradığını nasıl kanıtlarım? | ✅ tetiklendi | writing-skills |
| `captions-overlay` | Konuşan kafa videoma altyazı ekleyeceğim; yerleşim, kelime vurgusu ve okunabilirlik için ne yapmalıyım? | ✅ tetiklendi | captions-overlay |
| `flux-best-practices` | FLUX ile bir ürün fotoğrafı üreteceğim; iyi sonuç veren prompt nasıl yazılır? | ✅ tetiklendi | flux-best-practices |
| `cut-the-curve` | Kinetik tipografi videomda metin girişleri ve geçişler için easing eğrilerini nasıl seçmeliyim? | ✅ tetiklendi | cut-the-curve |
| `remotion-render` | Remotion projemdeki videoyu MP4 olarak dışa aktarmam gerek. Render komutunu ve ayarlarını söyle. | ✅ tetiklendi | remotion-render |
| `etsy-seller-guide` | Etsy mağazamdaki el yapımı mumların listing başlıklarını ve etiketlerini SEO için iyileştir. | ✅ tetiklendi | etsy-seller-guide |
| `character-rigging` | 2D karakterim için parçaları, pivot noktaları ve katman sırası olan yeniden kullanılabilir bir rig paketi kur. | ✅ tetiklendi | character-rigging |
| `react-three-fiber` | React Three Fiber ile tıklanınca dönen etkileşimli bir küp bileşeni oluştur. | ✅ tetiklendi | react-three-fiber |
| `claude-api` | Python'da Anthropic SDK ile streaming yanıt veren ve bir araç (tool) çağırabilen basit bir sohbet botu yaz. | ✅ tetiklendi | claude-api |
| `shopify-liquid` | Shopify temama ürün sayfasında gösterilecek özel bir Liquid section yaz; schema ayarları da olsun. | ✅ tetiklendi | shopify-liquid |
| `api-monitoring` | Shopify mağazamın webhook'ları bazen sessizce başarısız oluyor; API ve webhook izleme ile alarm sistemi kur. | ✅ tetiklendi | api-monitoring |
| `sealeap-amazon-asin-lifecycle-ad-planning` | Amazon'daki ürünlerimin (ASIN) hangi yaşam döngüsü aşamasında olduğuna göre reklam stratejisi planla: yeni ürün, büyüme, olgunluk, düşüş. | ✅ tetiklendi | sealeap-amazon-asin-lifecycle-ad-planning |
| `sealeap-ebay-brand-ip-triage` | eBay'de markamın görsellerini kopyalayan sahte ürün ilanları var; VeRO şikayeti için kanıtları nasıl hazırlarım? | ✅ tetiklendi | sealeap-ebay-brand-ip-triage |
| `web-clone` | Şu sitenin aynısını klonlamak istiyorum, Three.js efektleri dahil: https://example.com | ✅ tetiklendi | web-clone |
| `motion-lab` | Web sayfamdaki bileşen için uygun bir hover ve metin animasyonu efekti seçip uyarla. | ✅ tetiklendi | motion-lab |
| `obsidian-markdown@kepano` | Obsidian notlarımda callout, wikilink ve embed sözdizimini doğru kullanarak bir proje notu yaz. | ✅ tetiklendi | obsidian-markdown |
| `seo-audit@agricidaniel` | Sitemin teknik SEO denetimini yap: Core Web Vitals, indeksleme, schema ve E-E-A-T açısından. | ✅ tetiklendi | seo-audit |
| `egm-brainstorm` | Yeni bir özellik için spec yazmadan önce Google EGM yöntemiyle beyin fırtınası yap. | ✅ tetiklendi | egm-brainstorm (Read) |
| `humanizer` | Şu blog yazısındaki yapay zeka yazım izlerini temizle, daha insani olsun. | ✅ tetiklendi | humanizer |
| `video-shotcraft` | Remotion ile ürünüm için 20 saniyelik sinematik bir tanıtım videosu kurgula. | ✅ tetiklendi | video-shotcraft |

## 🔧 Bulunan ve düzeltilen hatalar
Hepsi **kurulan kopyada** düzeltilir; `arsiv/` altındaki orijinaller değişmez. Bu düzeltmeler olmadan aşağıdaki skiller ❌ çıkıyordu.

| Hata | Skill | Düzeltme |
|---|---|---|
| Betik çalışmıyor: f-string içinde JSX süslü parantezleri kaçırılmamış: betik SyntaxError veriyordu ({{ }} ile düzeltildi) | `react-three-fiber` | `yamalar/react-three-fiber/` (scripts/component_generator.py); yamalı betik örnek görevle çalıştırıldı, üretilen TSX derlendi |
| Kaynaktaki git symlink'leri arşive düz metin olarak gelmiş (12 dosya, ör. `remotion-license` → `../remotion-license`): SKILL.md'deki alt-skill bağlantıları ölüydü | `remotion-best-practices` | Kurulumda taslak silinir, bağlantılar kardeş skill'e çevrilir; kardeş kurulmazsa ön kontrol `kardes-eksik` uyarır |
| Kaynaktaki git symlink'leri arşive düz metin olarak gelmiş (1 dosya, ör. `remotion-maps` → `../remotion-maps`): SKILL.md'deki alt-skill bağlantıları ölüydü | `remotion-markup` | Kurulumda taslak silinir, bağlantılar kardeş skill'e çevrilir; kardeş kurulmazsa ön kontrol `kardes-eksik` uyarır |
| Claude hesabındaki aynı adlı skill (`anthropic-skills:<ad>`) kütüphane sürümünün yerine seçiliyordu (agent testinde `docx`). Bu makinede ad çakışması: `docs`, `docx`, `pdf`, `pptx`, `skill-creator`, `xlsx` | 6 skill | Kurulumda proje `.claude/settings.json` → `skillOverrides` ile hesaptaki o projede `off`; ön kontrol `hesap-cakismasi` bildirir, `--dogrula` denetler. Düzeltmeden sonra `docx` agent testi ✅ |
| Description yok / çok kısa / 1024'ten uzun: agent skill'i doğru durumda seçemiyordu | 96 skill | `registry.json` → `aciklama_duzeltme` (`notlar/tetiklenme-denetimi.md`) |
| Frontmatter HTML yorumunun arkasında ya da description YAML'ı bozuyor | 21 skill | Kurulumda kendiliğinden |

## ⚠️ Uyarılar (338)
Skill yüklenir ve çalışır; SKILL.md'nin andığı bazı dosyalar pakette yok (çoğu kaynak repoda da yok ya da kullanıcının projesindeki bir dosyayı gösteriyor).

<details><summary>Liste</summary>

| Skill | Uyarı |
|---|---|
| `accessibility-review` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `audit` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
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
| `egm-resolve` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, [RelativePath] |
| `egm-review` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/codex.md, resources/document_standards/zoom-out-standard.md |
| `egm-review-loop` | SKILL.md'nin andığı 3 dosya pakette yok: ../../docs/codex.md, resources/document_standards/feature-spec-standard.md, resources/document_standards/implementation-readiness-standard.md |
| `incident-response` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `standup` | SKILL.md'nin andığı 1 dosya pakette yok: ../../CONNECTORS.md |
| `wayfinder` | SKILL.md'nin andığı 1 dosya pakette yok: link |
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
| `obsidian-markdown@heyitsnoah` | SKILL.md'nin andığı 2 dosya pakette yok: Note%20Name.md, obsidian://open |
| `obsidian-markdown@kepano` | SKILL.md'nin andığı 1 dosya pakette yok: url |
| `save` | SKILL.md'nin andığı 1 dosya pakette yok: ../../docs/workflow-acceptance.md |
| `wiki` | SKILL.md'nin andığı 3 dosya pakette yok: ../../docs/capacity-and-recovery.md, ../../docs/native-conformance.md, ../../docs/upstream-references.md |
| `wiki-ingest` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/workflow-acceptance.md, url |
| `wiki-mode` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/wiki-mode.py |
| `wiki-retrieve` | SKILL.md'nin andığı 2 dosya pakette yok: ../../docs/prefix-providers.md, ../../docs/retrieval-evaluation.md |
| `academy-guide` | SKILL.md'nin andığı 1 dosya pakette yok: URL |
| `graphify` | SKILL.md'nin andığı 8 dosya pakette yok: references/add-watch.md, references/exports.md, references/extraction-spec.md, references/github-and-merge.md |
| `od-next-media-inputs` | SKILL.md'nin andığı 1 dosya pakette yok: assets/stock/credits.json |
| `skill-creator@composiohq` | SKILL.md'nin andığı 9 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, references/api_docs.md |
| `skill-creator@freshtechbro` | SKILL.md'nin andığı 9 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, references/api_docs.md |
| `skill-development` | SKILL.md'nin andığı 16 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, examples/script.sh |
| `skill-development@anthropics` | SKILL.md'nin andığı 16 dosya pakette yok: assets/font.ttf, assets/logo.png, assets/slides.pptx, examples/script.sh |
| `writing-skills` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/tool.sh |
| `agents-sdk@openai` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/generate_diagrams.py |
| `assess-patch-risk` | SKILL.md'nin andığı 1 dosya pakette yok: ../../schemas/patch-risk-assessment.schema.json |
| `build-report` | SKILL.md'nin andığı 1 dosya pakette yok: ../../assets/demo-product-growth.csv |
| `canva-resize-for-social-media` | SKILL.md'nin andığı 1 dosya pakette yok: edit_url |
| `caption-qa` | SKILL.md'nin andığı 1 dosya pakette yok: \d{1,3} |
| `create-data-context` | SKILL.md'nin andığı 1 dosya pakette yok: references/source-inventory.md |
| `create-llms` | SKILL.md'nin andığı 12 dosya pakette yok: CODE_OF_CONDUCT.md, CONTRIBUTING.md, README.md, docs/architecture.md |
| `d365-solution-blueprint` | SKILL.md'nin andığı 1 dosya pakette yok: references/firm-standards.md |
| `debug-zoom` | SKILL.md'nin andığı 1 dosya pakette yok: ../../README.md |
| `design-qa` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `expo-ui-jetpack-compose` | SKILL.md'nin andığı 1 dosya pakette yok: assets/icons/wifi.xml |
| `gdpr-compliant` | SKILL.md'nin andığı 2 dosya pakette yok: references/operations.md, references/security.md |
| `get-context` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `google-docs` | SKILL.md'nin andığı 1 dosya pakette yok: plugin://documents@openai-primary-runtime |
| `google-drive` | SKILL.md'nin andığı 1 dosya pakette yok: plugin://spreadsheets@openai-primary-runtime |
| `google-sheets` | SKILL.md'nin andığı 1 dosya pakette yok: plugin://spreadsheets@openai-primary-runtime |
| `google-slides` | SKILL.md'nin andığı 1 dosya pakette yok: plugin://presentations@openai-primary-runtime |
| `ideate` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `image-to-code@openai` | SKILL.md'nin andığı 2 dosya pakette yok: ../../references/critical-overrides.md, ../../references/local-prototype-preflight.md |
| `index` | SKILL.md'nin andığı 2 dosya pakette yok: ../../.app.json, ../../assets/demo-product-growth.csv |
| `index@openai` | SKILL.md'nin andığı 2 dosya pakette yok: ../../references/communication-protocol.md, ../../references/critical-overrides.md |
| `md-to-docx` | SKILL.md'nin andığı 2 dosya pakette yok: diagrams/high-level-architecture.drawio.png, path |
| `microsoft-skill-creator` | SKILL.md'nin andığı 1 dosya pakette yok: sample_codes/getting-started/hello-kernel.cs |
| `mixpanel-headless-setup` | SKILL.md'nin andığı 2 dosya pakette yok: ../mixpanelyst/references/analytical-frameworks.md, ../mixpanelyst/references/python-api.md |
| `ngs-amplicon-microbiome` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-analysis-router` | SKILL.md'nin andığı 2 dosya pakette yok: references/intake-schema.json, references/pipeline-registry.json |
| `ngs-atacseq-peaks-qc` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-chip-cutrun-peaks-qc` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-dna-germline-variants` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-dna-somatic-variants` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-dna-umi-panel-variants` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-dna-variant-calling` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-scrna-seq` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `ngs-shotgun-metagenomics` | SKILL.md'nin andığı 1 dosya pakette yok: resources/resource_plan.json |
| `omniverse-cad-to-simready` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/run.py |
| `omniverse-usd-performance-tuning` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/optimization-report.schema.json |
| `physical-ai-infrastructure-setup-and-resilient-scaling` | SKILL.md'nin andığı 2 dosya pakette yok: scripts/preflight.sh, scripts/scan_transcript_secrets.py |
| `plan-zoom-integration` | SKILL.md'nin andığı 1 dosya pakette yok: ../../README.md |
| `plan-zoom-product` | SKILL.md'nin andığı 1 dosya pakette yok: ../../README.md |
| `pr-address-feedback` | SKILL.md'nin andığı 2 dosya pakette yok: COMMENT_URL, url |
| `pr-screenshots` | SKILL.md'nin andığı 3 dosya pakette yok: url, url-to-after-image, url-to-before-image |
| `qdrant-vertical-scaling` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../qdrant-monitoring/SKILL.md |
| `quality-playbook` | SKILL.md'nin andığı 3 dosya pakette yok: bin/reference_docs_ingest.py, bin/run_playbook.py, references/filename.md |
| `research@openai` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `screen-recording` | SKILL.md'nin andığı 1 dosya pakette yok: page |
| `share` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `shopify-hydrogen@openai` | SKILL.md'nin andığı 4 dosya pakette yok: docs/api/hydrogen/latest/customer/createcustomeraccount, docs/api/hydrogen/latest/utilities/createcustomeraccountclient, docs/api/hydrogen/latest/utilities/createstorefrontclient, docs/api/hydrogen/utilities/createstorefrontclient |
| `swiftui-patterns` | SKILL.md'nin andığı 1 dosya pakette yok: references/run-button-bootstrap.md |
| `track-findings` | SKILL.md'nin andığı 3 dosya pakette yok: app://asdk_app_69a089a326dc8191b32a3f2553f5be2c, app://asdk_app_6a83901dde988191b3f3cefdcc19acfa, app://connector_76869538009648d5b282a4bb21c3d157 |
| `update-avm-modules-in-bicep` | SKILL.md'nin andığı 1 dosya pakette yok: link |
| `update-llms` | SKILL.md'nin andığı 12 dosya pakette yok: CODE_OF_CONDUCT.md, CONTRIBUTING.md, README.md, docs/architecture.md |
| `update-markdown-file-index` | SKILL.md'nin andığı 2 dosya pakette yok: path/to/filename.ext, path/to/filename2.ext |
| `url-to-code` | SKILL.md'nin andığı 2 dosya pakette yok: ../../references/critical-overrides.md, ../../references/local-prototype-preflight.md |
| `user-context` | SKILL.md'nin andığı 1 dosya pakette yok: ../../references/critical-overrides.md |
| `zoom-contact-center-android` | SKILL.md'nin andığı 2 dosya pakette yok: ../../rest-api/SKILL.md, ../../zoom-apps-sdk/SKILL.md |
| `zoom-contact-center-ios` | SKILL.md'nin andığı 2 dosya pakette yok: ../../oauth/SKILL.md, ../../zoom-apps-sdk/SKILL.md |
| `zoom-contact-center-web` | SKILL.md'nin andığı 3 dosya pakette yok: ../../cobrowse-sdk/SKILL.md, ../../oauth/SKILL.md, ../../zoom-apps-sdk/SKILL.md |
| `zoom-meeting-sdk-android` | SKILL.md'nin andığı 3 dosya pakette yok: ../../oauth/SKILL.md, ../SKILL.md, ../references/signature-playbook.md |
| `zoom-meeting-sdk-electron` | SKILL.md'nin andığı 3 dosya pakette yok: ../../general/SKILL.md, ../../oauth/SKILL.md, ../SKILL.md |
| `zoom-meeting-sdk-ios` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-meeting-sdk-linux` | SKILL.md'nin andığı 4 dosya pakette yok: ../references/ai-companion.md, ../references/authorization.md, ../references/bot-authentication.md, ../references/breakout-rooms.md |
| `zoom-meeting-sdk-macos` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-meeting-sdk-react-native` | SKILL.md'nin andığı 3 dosya pakette yok: ../../general/SKILL.md, ../../oauth/SKILL.md, ../SKILL.md |
| `zoom-meeting-sdk-unreal` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-meeting-sdk-web` | SKILL.md'nin andığı 4 dosya pakette yok: ../../general/use-cases/custom-meeting-ui-web.md, ../../general/use-cases/probe-sdk-preflight-readiness-gate.md, ../../oauth/SKILL.md, ../../probe-sdk/SKILL.md |
| `zoom-meeting-sdk-web-client-view` | SKILL.md'nin andığı 4 dosya pakette yok: ../SKILL.md, ../concepts/sharedarraybuffer.md, ../troubleshooting/common-issues.md, ../troubleshooting/error-codes.md |
| `zoom-meeting-sdk-web-component-view` | SKILL.md'nin andığı 4 dosya pakette yok: ../SKILL.md, ../concepts/sharedarraybuffer.md, ../troubleshooting/common-issues.md, ../troubleshooting/error-codes.md |
| `zoom-meeting-sdk-windows` | SKILL.md'nin andığı 5 dosya pakette yok: ../../oauth/SKILL.md, ../references/ai-companion.md, ../references/authorization.md, ../references/bot-authentication.md |
| `zoom-video-sdk-android` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-video-sdk-flutter` | SKILL.md'nin andığı 3 dosya pakette yok: ../../general/SKILL.md, ../../oauth/SKILL.md, ../SKILL.md |
| `zoom-video-sdk-ios` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-video-sdk-macos` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-video-sdk-react-native` | SKILL.md'nin andığı 3 dosya pakette yok: ../../general/SKILL.md, ../../oauth/SKILL.md, ../SKILL.md |
| `zoom-video-sdk-unity` | SKILL.md'nin andığı 1 dosya pakette yok: ../SKILL.md |
| `zoom-video-sdk-web` | SKILL.md'nin andığı 3 dosya pakette yok: ../../general/use-cases/probe-sdk-preflight-readiness-gate.md, ../../meeting-sdk/web/component-view/SKILL.md, ../../probe-sdk/SKILL.md |
| `zoom-virtual-agent-android` | SKILL.md'nin andığı 2 dosya pakette yok: ../../contact-center/android/SKILL.md, ../SKILL.md |
| `zoom-virtual-agent-ios` | SKILL.md'nin andığı 2 dosya pakette yok: ../../contact-center/ios/SKILL.md, ../SKILL.md |
| `zoom-virtual-agent-web` | SKILL.md'nin andığı 4 dosya pakette yok: ../../contact-center/web/SKILL.md, ../../oauth/SKILL.md, ../../rest-api/SKILL.md, ../SKILL.md |
| `add-sfx` | SKILL.md'nin andığı 1 dosya pakette yok: ./packages/remotion-media |
| `archify-review` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../CONTRIBUTING.md, ../../../REVIEWING.md |
| `archify-tuning` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../CONTRIBUTING.md |
| `deploy-release-test` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../contributing/core/testing.md |
| `gate-tests` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../test/lib/gate/README.md |
| `interactivity-best-practices` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../packages/docs/docs/studio/interactivity-best-practices.mdx, ../../../packages/docs/docs/studio/make-component-interactive.mdx |
| `playwright-dev` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../AGENTS.md |
| `playwright-devops` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../.github/workflows/bots.md |
| `playwright-release-notes` | SKILL.md'nin andığı 4 dosya pakette yok: ./getting-started-mcp.md, ./images/foo.png, ./test-parallel.md, [^(]/$ |
| `playwright-triage` | SKILL.md'nin andığı 3 dosya pakette yok: ../../../.github/actions/run-agent/guides/triage.md, ../../../.github/workflows/triage.yml, ../../../AGENTS.md |
| `pr-status-triage` | SKILL.md'nin andığı 2 dosya pakette yok: scripts/pr-status/results/index.md, scripts/pr-status/results/thread-N.md |
| `pr@remotion-dev` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../packages/docs/docs/contributing/elements.mdx |
| `remotion-new-markup` | SKILL.md'nin andığı 3 dosya pakette yok: ../../../packages/skills/skills/remotion-interactivity/timeline-structure.md, ../../../packages/skills/skills/remotion-markup/connected-compositions.md, ../../../packages/skills/skills/remotion-markup/video-editing.md |
| `scaffold-element` | SKILL.md'nin andığı 2 dosya pakette yok: ../../../packages/docs/docs/contributing/elements.mdx, ../../../packages/docs/docs/elements.mdx |
| `studio-dev` | SKILL.md'nin andığı 10 dosya pakette yok: ../../../packages/browser-studio/e2e/browser-studio.test.ts, ../../../packages/docs/docs/ai/webmcp.mdx, ../../../packages/studio/src/components/ActionTooltip.tsx, ../../../packages/studio/src/components/InspectorPanel/optimistic-composition-metadata.ts |
| `update-ffmpeg` | SKILL.md'nin andığı 1 dosya pakette yok: ../../../packages/compositor/ffmpeg/README.md |
| `update-trace-engine` | SKILL.md'nin andığı 3 dosya pakette yok: scripts/trace/copy-build-trace-engine-for-publish.sh, scripts/trace/prep-trace-engine-package.sh, scripts/trace/test/test-trace-engine.mjs |
| `captions-overlay` | SKILL.md'nin andığı 1 dosya pakette yok: references/captions.md |
| `remotion-best-practices@calesthio` | SKILL.md'nin andığı 1 dosya pakette yok: ./rules/sound-effects.md |
| `synthetic-screen-recording` | SKILL.md'nin andığı 1 dosya pakette yok: lib/verify_scene_pacing.py |
| `tiktok-upload` | SKILL.md'nin andığı 2 dosya pakette yok: examples/get_tk_cookie.py, examples/upload_video_to_tiktok.py |
| `xueqiu-upload` | SKILL.md'nin andığı 1 dosya pakette yok: images/chart.png |
| `zhihu-upload` | SKILL.md'nin andığı 1 dosya pakette yok: images/1.png |
| `elevenlabs` | [codex] SKILL.md'nin andığı 1 dosya pakette yok: ../provider-refresh-oct23/SKILL.md |
| `text-to-speech` | [codex] SKILL.md'nin andığı 1 dosya pakette yok: ../provider-refresh-oct23/SKILL.md |
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
| `bc-checkout` | SKILL.md'nin andığı 1 dosya pakette yok: templates/pages/checkout.html |
| `bc-stencil` | SKILL.md'nin andığı 1 dosya pakette yok: assets/js/app.js |
| `ecommerce-competitor-analyzer` | SKILL.md'nin andığı 1 dosya pakette yok: scripts/detect-platform.js |
| `mp-test-setup` | SKILL.md'nin andığı 1 dosya pakette yok: references/products.md |
| `saleor-apps` | SKILL.md'nin andığı 1 dosya pakette yok: lib/saleor-client.ts |
| `shopify-admin-agentic-llms-txt` | SKILL.md'nin andığı 1 dosya pakette yok: assets/llms.txt |
| `shopify-hydrogen` | SKILL.md'nin andığı 4 dosya pakette yok: docs/api/hydrogen/latest/customer/createcustomeraccount, docs/api/hydrogen/latest/utilities/createcustomeraccountclient, docs/api/hydrogen/latest/utilities/createstorefrontclient, docs/api/hydrogen/utilities/createstorefrontclient<br>[codex] SKILL.md'nin andığı 4 dosya pakette yok: docs/api/hydrogen/latest/customer/createcustomeraccount, docs/api/hydrogen/latest/utilities/createcustomeraccountclient, docs/api/hydrogen/latest/utilities/createstorefrontclient, docs/api/hydrogen/utilities/createstorefrontclient |
| `spree-dev-patterns` | SKILL.md'nin andığı 1 dosya pakette yok: lib/spree/dependencies.rb |
| `spree-events-webhooks` | SKILL.md'nin andığı 2 dosya pakette yok: lib/spree/event.rb, lib/spree/subscriber.rb |
| `spree-extensions` | SKILL.md'nin andığı 1 dosya pakette yok: lib/spree/dependencies.rb |
| `storefront-theming` | SKILL.md'nin andığı 1 dosya pakette yok: assets/base.css |
| `wc-product-search-select` | SKILL.md'nin andığı 4 dosya pakette yok: class-wc-admin-assets.php, class-wc-ajax.php, class-wc-product-data-store-cpt.php, wc-enhanced-select.js |
| `wc-variation-gallery` | SKILL.md'nin andığı 1 dosya pakette yok: templates/single-product/add-to-cart/variable.php |
| `wc-variations-data` | SKILL.md'nin andığı 4 dosya pakette yok: class-wc-product-variable-data-store-cpt.php, class-wc-product-variable.php, class-wc-product-variation.php, wc-product-functions.php |
| `woo-testing` | SKILL.md'nin andığı 1 dosya pakette yok: bin/install-wp-tests.sh |
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
| `experiment-bridge` | SKILL.md'nin andığı 5 dosya pakette yok: ../shared-references/output-language.md, ../shared-references/output-manifest.md, ../shared-references/output-versioning.md, ../shared-references/reviewer-backends.md |
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

</details>

## Tüm skiller ve örnek görevleri
5250 skill'in tek tek sonucu ve örnek görevi, alana göre: [a-tasarim-onyuz](notlar/skill-ornek-gorevler/a-tasarim-onyuz.md) (277) · [b-yazilim-gelistirme](notlar/skill-ornek-gorevler/b-yazilim-gelistirme.md) (358) · [c-dokuman-icerik](notlar/skill-ornek-gorevler/c-dokuman-icerik.md) (112) · [d-ai-otomasyon](notlar/skill-ornek-gorevler/d-ai-otomasyon.md) (112) · [e-entegrasyon-katalogu](notlar/skill-ornek-gorevler/e-entegrasyon-katalogu.md) (1781) · [f-repo-ici](notlar/skill-ornek-gorevler/f-repo-ici.md) (114) · [g-video-ses-medya](notlar/skill-ornek-gorevler/g-video-ses-medya.md) (146) · [h-is-alanlari](notlar/skill-ornek-gorevler/h-is-alanlari.md) (1972) · [i-bilim-muhendislik](notlar/skill-ornek-gorevler/i-bilim-muhendislik.md) (378)
