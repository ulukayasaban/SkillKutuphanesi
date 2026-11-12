# Ücretli ve Kısmen Ücretli Skiller

> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.

## 💲 Ücretli (ücret ödemeden hiç kullanılamaz) — 46

| Skill | Kategori | Neden |
|---|---|---|
| `substance-3d-texturing` | 05-3d-webgl | Adobe Substance 3D Painter lisansı/aboneliği |
| `sandbox-migrate-to-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-stable` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `deepseek-chat` | 01-claude-api-mcp | Tek işi DeepSeek API'sini çağırmaktır (DEEPSEEK_API_KEY, kullandıkça öde); anahtar yoksa çalışmaz. |
| `deepseek-reason` | 01-claude-api-mcp | Tek işi DeepSeek API'sini (deepseek-reasoner) çağırmaktır (DEEPSEEK_API_KEY, kullandıkça öde); anahtar yoksa çalışmaz. |
| `gaia-submission` | 02-agent-orkestrasyon | GAIA kıyaslamasını Anthropic API anahtarıyla çalıştırır (kullandıkça öde); anahtarsız yürütülemez. |
| `managed-agent` | 02-agent-orkestrasyon | Anthropic Claude Managed Agents bulut çalışma zamanını kullanır (ANTHROPIC_API_KEY, beta erişimi; kullandıkça öde). |
| `reverse-any-video` | 04-skill-plugin-yazimi | HyperFrames Pro (ücretli plan) girişi olmadan başlamaz; ekrandaki kişileri HeyGen ile fiyat sormadan yeniden çeker, son render bulutta |
| `style-sampling` | 04-skill-plugin-yazimi | Şablonlar HyperFrames Pro (ücretli plan) özelliğidir; Free planda çekilmez, ücretsiz kullanım yolu yok |
| `generate-image@github` | 01-uygulama-entegrasyonlari | OpenRouter görsel modelleri (OPENROUTER_API_KEY zorunlu), kullanım başına ücret |
| `nano-banana-pro-openrouter` | 01-uygulama-entegrasyonlari | Tek işi OpenRouter üzerinden Gemini 3 Pro Image çağırmak; model ücretli, kredisiz anahtar çalışmaz |
| `create-video` | 01-video-uretim-montaj | HeyGen Video Agent API |
| `pika-h3-flex` | 01-video-uretim-montaj | Pika API anahtarı ve saniye başı ön ödemeli kredi gerekir (480p $0.01/sn'den); ücretsiz yol yok (yalnızca Pika'nın geçici tanıtım kotası) |
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
| `higgsfield-soul-id` | 03-ai-gorsel-video-modelleri | Soul karakter eğitimi Higgsfield'ın ücretli planını (Basic ve üstü) ister; ücretsiz planda çalışmaz. |
| `kling-official` | 03-ai-gorsel-video-modelleri | Kling / fal.ai API |
| `minimax-h3` | 03-ai-gorsel-video-modelleri | MiniMax / fal.ai API |
| `seedance-2-0` | 03-ai-gorsel-video-modelleri | Seedance (Atlas Cloud / fal.ai / BytePlus) API |
| `seedance-2-5` | 03-ai-gorsel-video-modelleri | Seedance API sağlayıcıları |
| `trader-cloud-backtest` | 02-finans-hukuk-ik | Ağır işleri Anthropic Managed Agents bulutunda çalıştırır (ANTHROPIC_API_KEY, kullandıkça öde). Ücretsiz yol: yerel `trader-backtest`. |
| `adaptyv` | 01-yasam-bilimleri-kimya | Adaptyv Bio protein deney hizmeti: ücretli |
| `benchling-integration` | 01-yasam-bilimleri-kimya | Benchling kurumsal lisansı/hesabı gerekir |
| `dnanexus-integration` | 01-yasam-bilimleri-kimya | DNAnexus hesabı/kurum lisansı gerekir |
| `ginkgo-cloud-lab` | 01-yasam-bilimleri-kimya | Ginkgo bulut laboratuvarı: deney siparişi ücretli |
| `labarchive-integration` | 01-yasam-bilimleri-kimya | LabArchives kurumsal hesap gerekir |
| `lambda-labs-gpu-cloud` | 03-veri-bilimi-ml | Lambda GPU kiralama; ücretsiz katman yok, tek işi bu bulutu kullanmak |
| `generate-image` | 04-bilimsel-yazim-literatur | OpenRouter görsel modelleri (OPENROUTER_API_KEY zorunlu), kullanım başına ücret |
| `vast-gpu` | 04-bilimsel-yazim-literatur | Vast.ai GPU kiralama; ücretsiz katman yok, tek işi bu |
| `fictiv` | 05-cad-imalat-robotik | Fictiv imalat siparişi ücretli |

## ½ Kısmen (ücret ödemeden kullanılabilir: ücretsiz katman ya da ücretli servis sadece bir seçenek) — 212

| Skill | Kategori | Neden |
|---|---|---|
| `hallmark` | 01-ui-ux-tasarim-dili | TOGETHER_API_KEY sadece isteğe bağlı karşılaştırma adımı için; tasarım skill'i anahtarsız çalışır |
| `design` | 02-tasarim-sistemi-marka | Logo/görsel üretimi Gemini/MuAPI anahtarı ister; tasarım rehberi ücretsiz |
| `rive-interactive` | 03-animasyon-motion | Rive ücretsiz plan; bazı özellikler ücretli |
| `spline-interactive` | 05-3d-webgl | Spline ücretsiz plan; bazı dışa aktarma/ekip özellikleri ücretli |
| `hatch-pet` | 06-oyun-2d-grafik | Yerel yol ücretsiz; ikincil yedek yol OPENAI_API_KEY ister (ücretli) |
| `frontend-slides` | 07-gorsel-sanat-sunum | Yerel HTML sunum ve PDF ücretsiz; isteğe bağlı Vercel yayını hesap gerektirir (ücretsiz Hobby katmanı var). |
| `sunum-sitesi` | 07-gorsel-sanat-sunum | Site kodu ücretsiz yazılır; görseller ve döngü videoları Higgsfield üzerinden üretilir (kredi harcar). Kendi görsellerinle ücretsiz kullanılabilir. |
| `verification-quality` | 02-kod-kalitesi-review | Doğrulama akışı yerel ve ücretsiz çalışır; Datadog'a metrik gönderme (DD_API_KEY) yalnızca isteğe bağlı bir entegrasyon örneğidir. |
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
| `langsmith-observability` | 01-claude-api-mcp | LangSmith ücretsiz geliştirici katmanı |
| `caveman-setup` | 02-agent-orkestrasyon | Caveman Cloud gateway'e bağlar (CAVE_API_KEY); BYOK ile mevcut LLM anahtarı kullanılır, gateway'in ücretsiz katmanı var; diğer caveman skilleri anahtarsız |
| `cost-benchmark` | 02-agent-orkestrasyon | Yerel ölçüm ücretsizdir; Gemini/Sonnet/Opus karşılaştırma tabanları isteğe bağlıdır ve ilgili API anahtarıyla ücretlenir. |
| `cost-openrouter` | 02-agent-orkestrasyon | OpenRouter hesabı ve anahtarı gerekir (hesap ücretsiz); skill yalnızca harcamayı okur, kendisi ücret doğurmaz. |
| `flow-nexus-neural` | 02-agent-orkestrasyon | Flow Nexus bulut hesabı gerekir; eğitim için ücretsiz katman var, büyük işler ücretli katmanda kredi harcar. |
| `flow-nexus-platform` | 02-agent-orkestrasyon | Flow Nexus bulut hesabı gerekir; kredi sistemiyle çalışır, ücretsiz katman var, pro/enterprise ücretlidir. |
| `flow-nexus-swarm` | 02-agent-orkestrasyon | Flow Nexus bulut hesabı gerekir; kredi sistemiyle çalışır, ücretsiz katman var. |
| `intelligence-transfer` | 02-agent-orkestrasyon | Yerel projeler arası kalıp kopyalama ücretsizdir; IPFS pazarına yayımlama Pinata anahtarı ister (Pinata'nın ücretsiz planı var). |
| `browser-intent` | 03-web-arastirma-veri | OpenAI uyumlu bir LLM sağlayıcısı ister: OpenRouter ya da Ollama Cloud (ücretli/kotalı) veya kendi yerel uç noktan (ücretsiz). Sağlayıcı yoksa skill kısıtlı kipte çalışır. |
| `context7-cli` | 03-web-arastirma-veri | Çoğu komut girişsiz ve ücretsiz çalışır; `ctx7 setup` ve daha yüksek istek sınırı için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `context7-docs` | 03-web-arastirma-veri | CONTEXT7_API_KEY ister (ücretsiz hesapla alınır); yoğun kullanım için ücretli plan. |
| `context7-mcp` | 03-web-arastirma-veri | Girişsiz ve ücretsiz çalışır (istek sınırı düşük); daha yüksek sınır için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `context7-mcp@upstash` | 03-web-arastirma-veri | Girişsiz ve ücretsiz çalışır (istek sınırı düşük); daha yüksek sınır için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `find-docs` | 03-web-arastirma-veri | Kimlik doğrulamasız ve ücretsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `graphify` | 03-web-arastirma-veri | Yerel graf çıkarımı ücretsiz; LLM tabanlı çıkarım için isteğe bağlı API anahtarı (ücretli) |
| `notebooklm` | 03-web-arastirma-veri | Google hesabı; NotebookLM kullanım kotaları/planları |
| `agents-sdk@openai` | 01-uygulama-entegrasyonlari | OpenAI Agents SDK rehberi; çalıştırmak için OpenAI API kredisi gerekir, bilgi/kod üretimi ücretsiz |
| `ai-gateway` | 01-uygulama-entegrasyonlari | Vercel AI Gateway rehberi; sağlayıcı anahtarı/kredisi gerekir, ücretsiz katman var |
| `aiq-deploy` | 01-uygulama-entegrasyonlari | NVIDIA AIQ dağıtımı; arama sağlayıcıları (Exa/Serper/Tavily) ücretsiz katman + ücretli |
| `arize-ai-provider-integration` | 01-uygulama-entegrasyonlari | Arize/Phoenix: Phoenix açık kaynak ve yerel çalışır; Arize AX bulutu ücretsiz katman + ücretli |
| `arize-annotation` | 01-uygulama-entegrasyonlari | Arize/Phoenix: Phoenix açık kaynak ve yerel çalışır; Arize AX bulutu ücretsiz katman + ücretli |
| `arize-evaluator` | 01-uygulama-entegrasyonlari | Değerlendirme için LLM API anahtarı (OpenAI/Anthropic) gerekir; Phoenix kendisi ücretsiz |
| `arize-experiment` | 01-uygulama-entegrasyonlari | Deney için LLM API anahtarı gerekir; Phoenix kendisi ücretsiz |
| `arize-instrumentation` | 01-uygulama-entegrasyonlari | Phoenix yerel (ücretsiz) ya da Arize AX (ücretsiz katman) |
| `arize-prompt-optimization` | 01-uygulama-entegrasyonlari | LLM API anahtarı gerekir; Phoenix kendisi ücretsiz |
| `boltz-cli-setup` | 01-uygulama-entegrasyonlari | Boltz CLI kurulum rehberi; API anahtarı isteğe bağlı bulut yolu için |
| `cloudflare@openai` | 01-uygulama-entegrasyonlari | Cloudflare ücretsiz plan ile çalışır; bazı ürünler ücretli |
| `durable-objects@openai` | 01-uygulama-entegrasyonlari | Workers ücretsiz planında sınırlı; fazlası ücretli |
| `email` | 01-uygulama-entegrasyonlari | Resend: aylık ücretsiz kota, fazlası ücretli |
| `expo-api-routes` | 01-uygulama-entegrasyonlari | Örneklerde OpenAI/Weather API anahtarı; Expo API route rehberi anahtarsız kullanılır |
| `expo-dev-client@openai` | 01-uygulama-entegrasyonlari | Yerel derleme ücretsiz; EAS bulut derlemesi ücretsiz planla sınırlı |
| `latchshot-page-capture` | 01-uygulama-entegrasyonlari | Latchshot üçüncü taraf servisi; anahtarsız JPEG demo yolu var, tam kullanım API anahtarı/kota ister |
| `namecheap` | 01-uygulama-entegrasyonlari | Namecheap hesabı ve API erişimi gerekir (hesap ücretsiz, API için bakiye/alan adı şartı); alan adları ücretli |
| `nemoclaw-user-get-started` | 01-uygulama-entegrasyonlari | NVIDIA NemoClaw; NGC kaydı ücretsiz, bulut kullanımı ücretli olabilir |
| `omniverse-cad-to-simready` | 01-uygulama-entegrasyonlari | NVIDIA NGC/NVCF anahtarı: kayıt ücretsiz, bulut işlevleri kotalı |
| `openai-api-troubleshooting` | 01-uygulama-entegrasyonlari | OpenAI API hata ayıklama rehberi; API kullanımı ücretli ama rehber bilgi skill'i |
| `openai-platform-api-key` | 01-uygulama-entegrasyonlari | OpenAI API anahtarı yönetimi rehberi; API kullanımı ücretli |
| `physical-ai-neural-reconstruction` | 01-uygulama-entegrasyonlari | NVIDIA NGC anahtarı: kayıt ücretsiz |
| `pinecone-rag` | 01-uygulama-entegrasyonlari | Pinecone ücretsiz (starter) katmanı var |
| `resemble-detect` | 01-uygulama-entegrasyonlari | Resemble AI API anahtarı gerekir; ücretsiz plan sınırlı kota ile var |
| `subtitles` | 01-uygulama-entegrasyonlari | OpenAI Whisper API ile altyazı; API ücretli, ücretsiz yol: yerel whisper (kütüphanede media-use) |
| `temporal-cloud-setup` | 01-uygulama-entegrasyonlari | Temporal Cloud ücretli (deneme kredisi); Temporal kendi sunucunda ücretsiz |
| `temporal-ops` | 01-uygulama-entegrasyonlari | Temporal Cloud ücretli; açık kaynak Temporal ücretsiz |
| `twilio-agent-connect` | 01-uygulama-entegrasyonlari | Twilio hesabı: deneme kredisi, sonrası kullanım başı ücret |
| `twilio-ai-agent-architect` | 01-uygulama-entegrasyonlari | Twilio + isteğe bağlı ElevenLabs; deneme kredisi/ücretsiz katman |
| `twilio-cli-reference` | 01-uygulama-entegrasyonlari | Twilio/SendGrid hesabı; ücretsiz katman/deneme |
| `twilio-conversation-orchestrator` | 01-uygulama-entegrasyonlari | Twilio + isteğe bağlı ElevenLabs |
| `twilio-iam-auth-setup` | 01-uygulama-entegrasyonlari | Twilio hesabı (deneme kredisi) |
| `twilio-security-api-auth` | 01-uygulama-entegrasyonlari | Twilio hesabı (deneme kredisi) |
| `twilio-sendgrid-account-setup` | 01-uygulama-entegrasyonlari | SendGrid ücretsiz katman (günlük sınırlı e-posta) |
| `twilio-sendgrid-email-send` | 01-uygulama-entegrasyonlari | SendGrid ücretsiz katman |
| `twilio-sendgrid-engagement-quality` | 01-uygulama-entegrasyonlari | SendGrid ücretsiz katman |
| `twilio-sendgrid-inbound-parse` | 01-uygulama-entegrasyonlari | SendGrid ücretsiz katman |
| `twilio-sendgrid-suppressions` | 01-uygulama-entegrasyonlari | SendGrid ücretsiz katman |
| `twilio-voice-conversation-relay` | 01-uygulama-entegrasyonlari | Twilio + isteğe bağlı ElevenLabs |
| `v0-dev` | 01-uygulama-entegrasyonlari | v0 ücretsiz katman; API/SDK için kredi gerekir |
| `vercel-connect` | 01-uygulama-entegrasyonlari | Vercel + Linear entegrasyonu; her ikisinin ücretsiz katmanı var |
| `changelog-video` | 01-video-uretim-montaj | Yerel Whisper; HeyGen sesi isteğe bağlı |
| `cinecode` | 01-video-uretim-montaj | Film kodla üretilir ve ücretsiz çalışır. Seslendirme için Gemini TTS anahtarı (ücretsiz katmanı var) ya da isteğe bağlı ElevenLabs; stok arama için ücretsiz Pixabay anahtarı. Skill ücretli servis, anahtar ve büyük indirmeyi kullanıcı onayı olmadan kullanmaz. |
| `figma` | 01-video-uretim-montaj | FIGMA_TOKEN (ücretsiz planla çalışır); değişkenler (variables) Enterprise ister |
| `hyperframes` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `hyperframes-cli` | 01-video-uretim-montaj | Yerel render ücretsiz; bulut render (HyperFrames OAuth) ücretli plan/kredi ister |
| `hyperframes-cli@openai` | 01-video-uretim-montaj | Yerel render ücretsiz; bulut render (HyperFrames OAuth) ücretli plan/kredi ister |
| `hyperframes-registry@openai` | 01-video-uretim-montaj | HeyGen anılıyor; HyperFrames kendisi açık kaynak (kütüphanede heygen-com/hyperframes ile aynı sınıf) |
| `hyperframes@openai` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `media-use` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HyperFrames kredisi/HeyGen isteğe bağlı. 2026-11: skill ücretli çağrıdan önce onay istemiyor (kredi sınırı dosyası var) ve ucuz seçeneğe kendiliğinden geçmiyor; ücretsiz yol açıkça istenmeli; Voice Turbo Free planda ayda 3 dk |
| `moneyprinterturbo-video` | 01-video-uretim-montaj | LLM API anahtarı zorunlu (ücretsiz katmanı olan sağlayıcılar kullanılabilir), Pexels anahtarı ücretsiz, Edge TTS ücretsiz. Üretilmiş video sağlayıcıları (Seedance/Ark, OFox, MiniMax, MuAPI, Infistar, Jalapeno) ücretli görev açar; yalnızca açık onayla. |
| `provider-refresh-oct23` | 01-video-uretim-montaj | Ücretli sağlayıcı adaptörlerinin (Gemini Omni, Veo, ElevenLabs v4, HeyGen…) güncel API sözleşmeleri; ücretsiz yerel yollar ayrı skillerde |
| `remotion` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `remotion-best-practices` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-best-practices@calesthio` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-best-practices@openai` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-maps` | 01-video-uretim-montaj | Harita karoları Mapbox/MapTiler (ücretsiz kota) ya da ücretsiz OSM kaynakları; Remotion şirket lisansı ayrıca |
| `remotion-maps@openai` | 01-video-uretim-montaj | Harita karoları Mapbox/MapTiler (ücretsiz kota) ya da ücretsiz OSM kaynakları; Remotion şirket lisansı ayrıca |
| `agents` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planındaki sesli agent dakikalarıyla denenebilir; üretim kullanımı ücretli |
| `azure-speech-to-text` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: faster-whisper |
| `azure-text-to-speech` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: piper |
| `elevenlabs` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planı (aylık sınırlı kota) ile kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Kokoro) |
| `krillinai-cli` | 02-ses-muzik-konusma | TTS/LLM için MiniMax gibi sağlayıcı anahtarı gerekebilir; yerel yollar (whisper) var |
| `setup-api-key` | 02-ses-muzik-konusma | Sadece anahtar kurulum rehberi; ElevenLabs ücretsiz planıyla da çalışır |
| `sound-effects` | 02-ses-muzik-konusma | ElevenLabs ücretsiz kotasıyla kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Openverse + yerleşik efektler) |
| `speech-to-text` | 02-ses-muzik-konusma | ElevenLabs Scribe ücretsiz kotası var; fazlası ücretli. Tamamen ücretsiz yol: media-use transcribe (Whisper/Parakeet) |
| `3d-asset-generation` | 03-ai-gorsel-video-modelleri | Üretim Atlas Cloud / fal.ai ile ücretli; CC0 Kenney kataloğu ve Blender yolu ücretsiz |
| `comfyui` | 03-ai-gorsel-video-modelleri | Yerel ComfyUI ücretsiz; 'Partner Nodes' Comfy hesabı ve ön ödemeli kredi ister |
| `higgsfield-generate` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `higgsfield-marketplace-cards` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `higgsfield-product-photoshoot` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `ltx2` | 03-ai-gorsel-video-modelleri | Açık model (topluluk lisansı: 10M$ altı gelirde ücretsiz); büyük GPU ya da bulut GPU gerekir |
| `provider-model-refresh` | 03-ai-gorsel-video-modelleri | Ücretli sağlayıcı adaptörleri; bazı modeller yerel (Qwen Image yerel) |
| `video-prompt-builder` | 03-ai-gorsel-video-modelleri | Video planı ve istem yazımı ücretsizdir; planın Seedance/Higgsfield'da üretilmesi kredi harcar. |
| `image` | 01-satis-pazarlama-musteri | Görsel üretimi için Gemini/Replicate/Ideogram/OpenAI API seçenekleri; Gemini API ücretsiz katmanı var, skill yönlendirme ve optimizasyon da yapar |
| `video` | 01-satis-pazarlama-musteri | AI avatar (HeyGen/Synthesia) ücretli; Remotion gibi programatik yollar ücretsiz. Yöntem seçimi skill'de |
| `trader-broker` | 02-finans-hukuk-ik | Alpaca: ücretsiz kâğıt (paper) hesapla denenir; gerçek hesapta komisyonsuz ama GERÇEK PARA riski — işlem öncesi kullanıcı onayı şart |
| `acp-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Stripe (işlem başı ücret, test modu ücretsiz), ACP/Stripe (işlem başı) |
| `amazon-a-plus` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `amazon-white-background` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `ap2-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Google API (ücretsiz kota) |
| `b2b-commerce` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `batch-background-swap` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `cross-sell-upsell-engine` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Rebuy (ücretli Shopify uygulaması) |
| `customer-lifetime-value` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `customer-segmentation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `ecommerce-competitor-analyzer` | 05-e-ticaret-pazaryeri | Gemini API (ücretsiz kota) + Olostep kazıma API'si (ücretsiz deneme, sonrası ücretli) |
| `ecommerce-listing-suite` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `email-service-integration` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: SendGrid (ücretsiz kota) |
| `free-shipping-thresholds` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `invoice-generation-automation` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: PDFMonkey (ücretsiz kota) |
| `lifestyle-scene` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `loyalty-points-system` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `model-try-on` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `mp-commerce-checkout` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-integrate` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-review` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-test-setup` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mp-webhooks` | 05-e-ticaret-pazaryeri | Entegrasyon ve test ortamı ücretsiz; gerçek ödemelerde Mercado Pago işlem komisyonu |
| `mpp-service-discovery` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `mpp-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `multi-angle-set` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `multi-currency` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Open Exchange Rates (ücretsiz kota) |
| `nlweb-llm-providers` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: LLM API'leri (ücretli; yerel model seçeneği) |
| `nlweb-setup` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Qdrant (yerel ücretsiz / bulut ücretli), LLM API'leri (ücretli; yerel model seçeneği) |
| `order-fulfillment-workflow` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-management` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-refund-policy` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `revenue-recognition-accounting` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `sale-banner` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `selling-point-infographic` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `shipment-tracking` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `shipping-rate-calculator` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `size-chart` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
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
| `academic-plotting` | 03-veri-bilimi-ml | Gemini API isteğe bağlı; matplotlib ile anahtarsız çalışır |
| `dspy` | 03-veri-bilimi-ml | LLM API anahtarı gerekir; yerel model de kullanılabilir |
| `evolving-ai-agents` | 03-veri-bilimi-ml | LLM API anahtarı gerekir; yerel model de kullanılabilir |
| `experiment-tracking-swanlab` | 03-veri-bilimi-ml | SwanLab bireysel kullanımda ücretsiz; kendi sunucunda da çalışır |
| `guidance` | 03-veri-bilimi-ml | LLM API ya da yerel model (llama.cpp/transformers) ile çalışır |
| `langchain` | 03-veri-bilimi-ml | LangChain ücretsiz; LangSmith izleme isteğe bağlı |
| `miles-rl-training` | 03-veri-bilimi-ml | MiniMax anılıyor; eğitim yerel GPU'da yapılır |
| `modal` | 03-veri-bilimi-ml | Modal: aylık ücretsiz kredi, sonrası kullanım başına |
| `modal-serverless-gpu` | 03-veri-bilimi-ml | Modal aylık ücretsiz kredi verir; fazlası ücretli |
| `nemo-evaluator-sdk` | 03-veri-bilimi-ml | NGC kaydı ücretsiz; yargıç LLM için API anahtarı gerekebilir |
| `nnsight-remote-interpretability` | 03-veri-bilimi-ml | NDIF uzak erişim anahtarı araştırmacılara ücretsiz; yerel modelle de çalışır |
| `skypilot-multi-cloud-orchestration` | 03-veri-bilimi-ml | SkyPilot ücretsiz; hedef bulutlar (RunPod vb.) ücretli, yerel küme de desteklenir |
| `verl-rl-training` | 03-veri-bilimi-ml | veRL açık kaynak, yerel GPU'da; volcengine sadece örnek bulut |
| `weights-and-biases` | 03-veri-bilimi-ml | W&B kişisel kullanımda ücretsiz; takım planları ücretli |
| `auto-review-loop-llm` | 04-bilimsel-yazim-literatur | Herhangi bir LLM API anahtarı (MiniMax/DashScope…) gerekir; Claude Code içindeki model de kullanılabilir |
| `auto-review-loop-minimax` | 04-bilimsel-yazim-literatur | MiniMax API anahtarı gerekir (ücretli); aynı işin LLM-bağımsız sürümü auto-review-loop |
| `autoskill` | 04-bilimsel-yazim-literatur | İsteğe bağlı Anthropic/Foundry API (ücretli) |
| `bgpt-paper-search` | 04-bilimsel-yazim-literatur | BGPT API anahtarı; ücretsiz/ücretli katmanlar |
| `database-lookup` | 04-bilimsel-yazim-literatur | Çoğu kamu veritabanı anahtarı ücretsiz; bazı sağlayıcılar (Alpha Vantage vb.) ücretli katmanlı |
| `exa-search` | 04-bilimsel-yazim-literatur | Exa API ücretsiz kota (aylık sınırlı); fazlası ücretli |
| `exa-search@wanshuiyin` | 04-bilimsel-yazim-literatur | Exa API ücretsiz kota (aylık sınırlı); fazlası ücretli |
| `firecrawl-search` | 04-bilimsel-yazim-literatur | Firecrawl ücretsiz kota, fazlası ücretli |
| `gemini-search` | 04-bilimsel-yazim-literatur | Gemini API ücretsiz katmanı |
| `hypogenic` | 04-bilimsel-yazim-literatur | LLM API (Anthropic/OpenAI) kullanım başına ücretli; yerel model de kullanılabilir |
| `infographics` | 04-bilimsel-yazim-literatur | İnceleme ücretsiz; görsel üretimi OpenRouter (ücretli, anahtar isteğe bağlı) |
| `keenable-search` | 04-bilimsel-yazim-literatur | Exa/Keenable ücretsiz kota, fazlası ücretli |
| `latex-posters` | 04-bilimsel-yazim-literatur | LaTeX yerel ve ücretsiz; isteğe bağlı AI şemaları OpenRouter (ücretli) |
| `literature-review` | 04-bilimsel-yazim-literatur | Temel tarama ücretsiz (DOI/açık kaynaklar); Parallel/OpenRouter isteğe bağlı ücretli |
| `paper-illustration` | 04-bilimsel-yazim-literatur | Gemini API ücretsiz katmanı |
| `paper-writing` | 04-bilimsel-yazim-literatur | Gemini API ücretsiz katmanı; anahtarsız da taslak yazar |
| `paperclip` | 04-bilimsel-yazim-literatur | GXL Paperclip CLI; anahtar isteğe bağlı, kapsamlı kullanım ücretli olabilir |
| `parallel-web` | 04-bilimsel-yazim-literatur | Parallel API ücretsiz başlangıç kredisi; sonrası ücretli |
| `proof-checker` | 04-bilimsel-yazim-literatur | MiniMax anılıyor; LLM-bağımsız kullanılabilir |
| `research-grants` | 04-bilimsel-yazim-literatur | Rehber ücretsiz; isteğe bağlı görseller OpenRouter (ücretli) |
| `research-lookup` | 04-bilimsel-yazim-literatur | Parallel CLI: ücretsiz başlangıç kredisi, sonrası ücretli |
| `run-experiment` | 04-bilimsel-yazim-literatur | W&B isteğe bağlı; deney yerelde çalışır |
| `scientific-schematics` | 04-bilimsel-yazim-literatur | AI şema üretimi OpenRouter (ücretli); elle şema yolu ücretsiz |
| `scientific-slides` | 04-bilimsel-yazim-literatur | Slayt yerel; isteğe bağlı AI görsel OpenRouter (ücretli) |

Gizli entegrasyon kataloğundaki 832 Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var).
