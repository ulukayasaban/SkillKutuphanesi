# Ücretli ve Kısmen Ücretli Skiller

> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.

## 💲 Ücretli (ücret ödemeden hiç kullanılamaz) — 33

| Skill | Kategori | Neden |
|---|---|---|
| `substance-3d-texturing` | 05-3d-webgl | Adobe Substance 3D Painter lisansı/aboneliği |
| `sandbox-migrate-to-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-stable` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `create-video` | 01-video-uretim-montaj | HeyGen Video Agent API |
| `video-toolkit` | 01-video-uretim-montaj | Açık modelleri bulut GPU'da (Modal/RunPod) çalıştırır; GPU kullanımı ücretli |
| `video-translate` | 01-video-uretim-montaj | HeyGen API |
| `acestep` | 02-ses-muzik-konusma | RunPod uç noktası (RUNPOD_API_KEY) |
| `dashscope` | 02-ses-muzik-konusma | Alibaba Cloud DashScope API |
| `doubao-tts` | 02-ses-muzik-konusma | Volcengine Doubao API |
| `fish-audio-tts` | 02-ses-muzik-konusma | fish.audio API |
| `lyria` | 02-ses-muzik-konusma | Google Lyria (Gemini/Vertex API) |
| `music` | 02-ses-muzik-konusma | ElevenLabs Music API. Ücretsiz yol: media-use (yerel MusicGen) |
| `text-to-speech` | 02-ses-muzik-konusma | HeyGen Starfish TTS (HEYGEN_API_KEY). Ücretsiz yol: media-use (Kokoro) |
| `ai-video-gen` | 03-ai-gorsel-video-modelleri | HeyGen / fal.ai / Kling / Gemini API ağ geçitleri |
| `atlas-cloud` | 03-ai-gorsel-video-modelleri | Atlas Cloud API (ATLASCLOUD_API_KEY) |
| `avatar-video` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `bfl-api` | 03-ai-gorsel-video-modelleri | Black Forest Labs FLUX API (BFL_API_KEY) |
| `faceswap` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `gemini-omni` | 03-ai-gorsel-video-modelleri | Gemini API / fal.ai (video üretimi ücretli kotada) |
| `grok-media` | 03-ai-gorsel-video-modelleri | xAI API |
| `heygen` | 03-ai-gorsel-video-modelleri | HeyGen API (kullanımdan kaldırıldı; create-video / avatar-video) |
| `kling-official` | 03-ai-gorsel-video-modelleri | Kling / fal.ai API |
| `minimax-h3` | 03-ai-gorsel-video-modelleri | MiniMax / fal.ai API |
| `seedance-2-0` | 03-ai-gorsel-video-modelleri | Seedance (Atlas Cloud / fal.ai / BytePlus) API |
| `seedance-2-5` | 03-ai-gorsel-video-modelleri | Seedance API sağlayıcıları |
| `adaptyv` | 01-yasam-bilimleri-kimya | Adaptyv Bio protein deney hizmeti: ücretli |
| `benchling-integration` | 01-yasam-bilimleri-kimya | Benchling kurumsal lisansı/hesabı gerekir |
| `dnanexus-integration` | 01-yasam-bilimleri-kimya | DNAnexus hesabı/kurum lisansı gerekir |
| `ginkgo-cloud-lab` | 01-yasam-bilimleri-kimya | Ginkgo bulut laboratuvarı: deney siparişi ücretli |
| `labarchive-integration` | 01-yasam-bilimleri-kimya | LabArchives kurumsal hesap gerekir |
| `generate-image` | 04-bilimsel-yazim-literatur | OpenRouter görsel modelleri (OPENROUTER_API_KEY zorunlu), kullanım başına ücret |
| `fictiv` | 05-cad-imalat-robotik | Fictiv imalat siparişi ücretli |

## ½ Kısmen (ücret ödemeden kullanılabilir: ücretsiz katman ya da ücretli servis sadece bir seçenek) — 104

| Skill | Kategori | Neden |
|---|---|---|
| `design` | 02-tasarim-sistemi-marka | Logo/görsel üretimi Gemini/MuAPI anahtarı ister; tasarım rehberi ücretsiz |
| `rive-interactive` | 03-animasyon-motion | Rive ücretsiz plan; bazı özellikler ücretli |
| `spline-interactive` | 05-3d-webgl | Spline ücretsiz plan; bazı dışa aktarma/ekip özellikleri ücretli |
| `hatch-pet` | 06-oyun-2d-grafik | Yerel yol ücretsiz; ikincil yedek yol OPENAI_API_KEY ister (ücretli) |
| `basin` | 06-devops-guvenlik-performans | Cloudflare R2/Basin: ücretsiz kota, sonrası kullanım başına |
| `cloudflare` | 06-devops-guvenlik-performans | Cloudflare ücretsiz plan ile çalışır; bazı ürünler ücretli |
| `cloudflare-email-service` | 06-devops-guvenlik-performans | Cloudflare ücretsiz kota, sonrası ücretli |
| `cloudflare-one` | 06-devops-guvenlik-performans | Cloudflare Zero Trust ücretsiz plan (50 kullanıcıya kadar); kurumsal özellikler ücretli |
| `cloudflare-one-migrations` | 06-devops-guvenlik-performans | Cloudflare Zero Trust ücretsiz plan; kurumsal özellikler ücretli |
| `deploy-to-vercel` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; ekip/ticari kullanım ücretli |
| `durable-objects` | 06-devops-guvenlik-performans | Workers ücretsiz planında sınırlı; fazlası ücretli |
| `k2` | 06-devops-guvenlik-performans | Cloudflare ürünü: ücretsiz kota + kullanım başına ücret |
| `vercel-cli-with-tokens` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; ekip/ticari kullanım ücretli |
| `vercel-optimize` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; bazı analizler ücretli planlarda |
| `eas-app-stores` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-hosting` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-observe` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-simulator` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-update` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-update-insights` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `eas-workflows` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `expo-app-clip` | 08-mobil-uygulama | Expo Application Services: ücretsiz EAS planı (sınırlı derleme/kullanıcı) ile kullanılabilir; fazlası ücretli |
| `expo-dev-client` | 08-mobil-uygulama | Yerel derleme ücretsiz; EAS bulut derlemesi ücretsiz planla sınırlı |
| `play-billing-library-version-upgrade` | 08-mobil-uygulama | Kod geçişi ücretsiz; Play Console geliştirici hesabı tek seferlik ücretli |
| `init-bootstrap` | 04-not-alma-bilgi-yonetimi | Gemini API anahtarı isteğe bağlı (ücretsiz katman var) |
| `claude-api` | 01-claude-api-mcp | Skill kod yazmaya/rehberliğe ücretsiz yardım eder; yazılan kodun Anthropic API çağrıları token bazlı ücretli |
| `claude-opus-4-5-migration` | 01-claude-api-mcp | Kod geçişi ücretsiz yapılır; geçirilen kodun API çağrıları ücretli |
| `connect` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `connect-apps` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `langsmith-fetch` | 01-claude-api-mcp | LangSmith hesabı (ücretsiz katman var) |
| `graphify` | 03-web-arastirma-veri | Yerel graf çıkarımı ücretsiz; LLM tabanlı çıkarım için isteğe bağlı API anahtarı (ücretli) |
| `notebooklm` | 03-web-arastirma-veri | Google hesabı; NotebookLM kullanım kotaları/planları |
| `changelog-video` | 01-video-uretim-montaj | Yerel Whisper; HeyGen sesi isteğe bağlı |
| `figma` | 01-video-uretim-montaj | FIGMA_TOKEN (ücretsiz planla çalışır); değişkenler (variables) Enterprise ister |
| `hyperframes` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `media-use` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HeyGen isteğe bağlı ve ücretli çağrıdan önce onay ister |
| `remotion` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `remotion-best-practices` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-best-practices@calesthio` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-maps` | 01-video-uretim-montaj | Harita karoları Mapbox/MapTiler (ücretsiz kota) ya da ücretsiz OSM kaynakları; Remotion şirket lisansı ayrıca |
| `agents` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planındaki sesli agent dakikalarıyla denenebilir; üretim kullanımı ücretli |
| `azure-speech-to-text` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: faster-whisper |
| `azure-text-to-speech` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: piper |
| `elevenlabs` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planı (aylık sınırlı kota) ile kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Kokoro) |
| `setup-api-key` | 02-ses-muzik-konusma | Sadece anahtar kurulum rehberi; ElevenLabs ücretsiz planıyla da çalışır |
| `sound-effects` | 02-ses-muzik-konusma | ElevenLabs ücretsiz kotasıyla kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Openverse + yerleşik efektler) |
| `speech-to-text` | 02-ses-muzik-konusma | ElevenLabs Scribe ücretsiz kotası var; fazlası ücretli. Tamamen ücretsiz yol: media-use transcribe (Whisper/Parakeet) |
| `3d-asset-generation` | 03-ai-gorsel-video-modelleri | Üretim Atlas Cloud / fal.ai ile ücretli; CC0 Kenney kataloğu ve Blender yolu ücretsiz |
| `comfyui` | 03-ai-gorsel-video-modelleri | Yerel ComfyUI ücretsiz; 'Partner Nodes' Comfy hesabı ve ön ödemeli kredi ister |
| `ltx2` | 03-ai-gorsel-video-modelleri | Açık model (topluluk lisansı: 10M$ altı gelirde ücretsiz); büyük GPU ya da bulut GPU gerekir |
| `provider-model-refresh` | 03-ai-gorsel-video-modelleri | Ücretli sağlayıcı adaptörleri; bazı modeller yerel (Qwen Image yerel) |
| `trader-broker` | 02-finans-hukuk-ik | Alpaca: ücretsiz kâğıt (paper) hesapla denenir; gerçek hesapta komisyonsuz ama GERÇEK PARA riski — işlem öncesi kullanıcı onayı şart |
| `acp-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Stripe (işlem başı ücret, test modu ücretsiz), ACP/Stripe (işlem başı) |
| `ap2-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Google API (ücretsiz kota) |
| `b2b-commerce` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `cross-sell-upsell-engine` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Rebuy (ücretli Shopify uygulaması) |
| `customer-lifetime-value` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `customer-segmentation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `ecommerce-competitor-analyzer` | 05-e-ticaret-pazaryeri | Gemini API (ücretsiz kota) + Olostep kazıma API'si (ücretsiz deneme, sonrası ücretli) |
| `email-service-integration` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: SendGrid (ücretsiz kota) |
| `free-shipping-thresholds` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `invoice-generation-automation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: PDFMonkey (ücretsiz kota) |
| `loyalty-points-system` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `mp-commerce-checkout` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-integrate` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-review` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-test-setup` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-webhooks` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mpp-service-discovery` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `mpp-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `multi-currency` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Open Exchange Rates (ücretsiz kota) |
| `nlweb-llm-providers` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: LLM API'leri (ücretli; yerel model seçeneği) |
| `nlweb-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Qdrant (yerel ücretsiz / bulut ücretli), LLM API'leri (ücretli; yerel model seçeneği) |
| `order-fulfillment-workflow` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-management` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-refund-policy` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `revenue-recognition-accounting` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `shipment-tracking` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `shipping-rate-calculator` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `spree-payments` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Stripe (işlem başı ücret, test modu ücretsiz) |
| `tax-calculation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: TaxJar (ücretli abonelik; ücretsiz deneme) |
| `tax-compliance-automation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: TaxJar (ücretli abonelik; ücretsiz deneme) |
| `volume-pricing` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `alphagenome` | 01-yasam-bilimleri-kimya | AlphaGenome API ticari olmayan kullanım için ücretsiz |
| `esm` | 01-yasam-bilimleri-kimya | Açık ağırlıklarla yerel çalışır; EvolutionaryScale Forge API isteğe bağlı |
| `genomic-intelligence` | 01-yasam-bilimleri-kimya | GI REST API anahtarı; ücretsiz/ücretli katmanlar |
| `latchbio-integration` | 01-yasam-bilimleri-kimya | Latch hesabı: ücretsiz katman, hesaplama ücretli |
| `rowan` | 01-yasam-bilimleri-kimya | Rowan hesabı: ücretsiz kredi, sonrası ücretli |
| `tamarind` | 01-yasam-bilimleri-kimya | Tamarind Bio hesabı: ücretsiz katman, sonrası ücretli |
| `modal` | 03-veri-bilimi-ml | Modal: aylık ücretsiz kredi, sonrası kullanım başına |
| `autoskill` | 04-bilimsel-yazim-literatur | İsteğe bağlı Anthropic/Foundry API (ücretli) |
| `bgpt-paper-search` | 04-bilimsel-yazim-literatur | BGPT API anahtarı; ücretsiz/ücretli katmanlar |
| `database-lookup` | 04-bilimsel-yazim-literatur | Çoğu kamu veritabanı anahtarı ücretsiz; bazı sağlayıcılar (Alpha Vantage vb.) ücretli katmanlı |
| `exa-search` | 04-bilimsel-yazim-literatur | Exa API ücretsiz kota (aylık sınırlı); fazlası ücretli |
| `hypogenic` | 04-bilimsel-yazim-literatur | LLM API (Anthropic/OpenAI) kullanım başına ücretli; yerel model de kullanılabilir |
| `infographics` | 04-bilimsel-yazim-literatur | İnceleme ücretsiz; görsel üretimi OpenRouter (ücretli, anahtar isteğe bağlı) |
| `latex-posters` | 04-bilimsel-yazim-literatur | LaTeX yerel ve ücretsiz; isteğe bağlı AI şemaları OpenRouter (ücretli) |
| `literature-review` | 04-bilimsel-yazim-literatur | Temel tarama ücretsiz (DOI/açık kaynaklar); Parallel/OpenRouter isteğe bağlı ücretli |
| `paperclip` | 04-bilimsel-yazim-literatur | GXL Paperclip CLI; anahtar isteğe bağlı, kapsamlı kullanım ücretli olabilir |
| `parallel-web` | 04-bilimsel-yazim-literatur | Parallel API ücretsiz başlangıç kredisi; sonrası ücretli |
| `research-grants` | 04-bilimsel-yazim-literatur | Rehber ücretsiz; isteğe bağlı görseller OpenRouter (ücretli) |
| `research-lookup` | 04-bilimsel-yazim-literatur | Parallel CLI: ücretsiz başlangıç kredisi, sonrası ücretli |
| `scientific-schematics` | 04-bilimsel-yazim-literatur | AI şema üretimi OpenRouter (ücretli); elle şema yolu ücretsiz |
| `scientific-slides` | 04-bilimsel-yazim-literatur | Slayt yerel; isteğe bağlı AI görsel OpenRouter (ücretli) |

## ? Sınıflandırılmamış — 3

| Skill | Kategori | Neden |
|---|---|---|
| `reverse-any-video` | 04-skill-plugin-yazimi | ücretli servis izi: HeyGen, paid plan -> ucret-siniflandirma.json'a ekle |
| `hyperframes-cli` | 01-video-uretim-montaj | ücretli servis izi: paid plan -> ucret-siniflandirma.json'a ekle |
| `provider-refresh-oct23` | 01-video-uretim-montaj | ücretli servis izi: ElevenLabs, elevenlabs, heygen -> ucret-siniflandirma.json'a ekle |

Gizli entegrasyon kataloğundaki 832 Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var).
