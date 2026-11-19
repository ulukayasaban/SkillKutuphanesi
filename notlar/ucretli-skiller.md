# Ücretli ve Kısmen Ücretli Skiller

> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.

## 💲 Ücretli (ücret ödemeden hiç kullanılamaz) — 40

| Skill | Kategori | Neden |
|---|---|---|
| `substance-3d-texturing` | 05-3d-webgl | Adobe Substance 3D Painter lisansı/aboneliği |
| `sandbox-migrate-to-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-next` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `sandbox-stable` | 06-devops-guvenlik-performans | Cloudflare Sandbox/Containers Workers Paid planı gerektirir |
| `reverse-any-video` | 04-skill-plugin-yazimi | HyperFrames Pro (ücretli plan) girişi olmadan başlamaz; ekrandaki kişileri HeyGen ile fiyat sormadan yeniden çeker, son render bulutta |
| `style-sampling` | 04-skill-plugin-yazimi | Şablonlar HyperFrames Pro (ücretli plan) özelliğidir; Free planda çekilmez, ücretsiz kullanım yolu yok |
| `create-video` | 01-video-uretim-montaj | HeyGen Video Agent API |
| `pika-h3-flex` | 01-video-uretim-montaj | Pika API anahtarı ve saniye başı ön ödemeli kredi gerekir (480p $0.01/sn'den); ücretsiz yol yok (yalnızca Pika'nın geçici tanıtım kotası) |
| `video-translate` | 01-video-uretim-montaj | HeyGen API |
| `acestep@openmontageinc` | 02-ses-muzik-konusma | Eski OpenMontage kopyası: yalnız RunPod uç noktası (RUNPOD_API_KEY) |
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
| `ideogram4` | 03-ai-gorsel-video-modelleri | Ideogram v4 barındırılan API: görsel başı ücretli API anahtarı gerekir |
| `kling-official` | 03-ai-gorsel-video-modelleri | Kling / fal.ai API |
| `minimax-h3` | 03-ai-gorsel-video-modelleri | MiniMax / fal.ai API |
| `runpod` | 03-ai-gorsel-video-modelleri | RunPod sunucusuz GPU: saniye başı ücretli, ücretsiz katman yok |
| `seedance-2-0` | 03-ai-gorsel-video-modelleri | Seedance (Atlas Cloud / fal.ai / BytePlus) API |
| `seedance-2-5` | 03-ai-gorsel-video-modelleri | Seedance API sağlayıcıları |
| `adaptyv` | 01-yasam-bilimleri-kimya | Adaptyv Bio protein deney hizmeti: ücretli |
| `benchling-integration` | 01-yasam-bilimleri-kimya | Benchling kurumsal lisansı/hesabı gerekir |
| `dnanexus-integration` | 01-yasam-bilimleri-kimya | DNAnexus hesabı/kurum lisansı gerekir |
| `ginkgo-cloud-lab` | 01-yasam-bilimleri-kimya | Ginkgo bulut laboratuvarı: deney siparişi ücretli |
| `labarchive-integration` | 01-yasam-bilimleri-kimya | LabArchives kurumsal hesap gerekir |
| `lambda-labs-gpu-cloud` | 03-veri-bilimi-ml | Lambda GPU kiralama; ücretsiz katman yok, tek işi bu bulutu kullanmak |
| `generate-image` | 04-bilimsel-yazim-literatur | OpenRouter görsel modelleri (OPENROUTER_API_KEY zorunlu), kullanım başına ücret |
| `vast-gpu` | 04-bilimsel-yazim-literatur | Vast.ai GPU kiralama; ücretsiz katman yok, tek işi bu |
| `fictiv` | 05-cad-imalat-robotik | Fictiv imalat siparişi ücretli |

## ½ Kısmen (ücret ödemeden kullanılabilir: ücretsiz katman ya da ücretli servis sadece bir seçenek) — 355

| Skill | Kategori | Neden |
|---|---|---|
| `hallmark` | 01-ui-ux-tasarim-dili | TOGETHER_API_KEY sadece isteğe bağlı karşılaştırma adımı için; tasarım skill'i anahtarsız çalışır |
| `design` | 02-tasarim-sistemi-marka | Logo/görsel üretimi Gemini/MuAPI anahtarı ister; tasarım rehberi ücretsiz |
| `rive-interactive` | 03-animasyon-motion | Rive ücretsiz plan; bazı özellikler ücretli |
| `spline-interactive` | 05-3d-webgl | Spline ücretsiz plan; bazı dışa aktarma/ekip özellikleri ücretli |
| `hatch-pet` | 06-oyun-2d-grafik | Yerel yol ücretsiz; ikincil yedek yol OPENAI_API_KEY ister (ücretli) |
| `frontend-slides` | 07-gorsel-sanat-sunum | Yerel HTML sunum ve PDF ücretsiz; isteğe bağlı Vercel yayını hesap gerektirir (ücretsiz Hobby katmanı var). |
| `sunum-sitesi` | 07-gorsel-sanat-sunum | Site kodu ücretsiz yazılır; görseller ve döngü videoları Higgsfield üzerinden üretilir (kredi harcar). Kendi görsellerinle ücretsiz kullanılabilir. |
| `alloydb-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `api-gateway-backend-security-and-rate-limiting` | 04-mimari-api-veritabani | GCP API Gateway; 'API key' ağ geçidinin kendi kimlik doğrulaması; GCP ücretsiz katman/kota var |
| `api-gateway-mcp-server` | 04-mimari-api-veritabani | GCP API Gateway MCP sunucusu; API anahtarı ağ geçidi kimlik doğrulaması; GCP ücretsiz katman var |
| `api-gateway-openapi-spec-authoring` | 04-mimari-api-veritabani | GCP API Gateway OpenAPI tanımı; 'API key' ağ geçidi kimlik doğrulaması; GCP ücretsiz katman var |
| `api-gateway-troubleshooting` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `apigee-agent-gateway-governance` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `application-design-center-design-deploy` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `application-integration-authoring` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `application-integration-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `application-integration-troubleshooting` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-ai-ml` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-bigframes` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-migration-data-loader` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-migration-metadata-extractor` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-migration-sql-translator` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-migration-validator` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-observability` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-optimization` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-troubleshooting` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigquery-udfs` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `bigtable-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-databases-onboarding` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-sql-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `datalineage-bigquery-asset-impact-analysis` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `datalineage-summary` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `dbt-sf-to-bq-translator` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `firebase-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-agentic-ai-bidirectional-streaming` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-agentic-ai-borderless-data-lakehouse` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-agentic-ai-data-science-workflow` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-agentic-analytics-spark-knowledge-catalog` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-architecture` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-build-deploy-agents` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-guided-gke-ai-migration` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-hybrid-search-alloydb` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-multi-agent-security` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-n-tier-serverless-web-app` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-solution-rag-enterprise-search-gke-sqldb` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-storage-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-storage-bucket-architect` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-storage-diagnostic` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-storage-fuse` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `managed-airflow-dag-authoring` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `managed-airflow-dag-troubleshooting` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `managed-airflow-migrations` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `managed-airflow-recommendations` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `spanner-basics` | 04-mimari-api-veritabani | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `assured-workloads-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `assuredworkloads-environment-assessor` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `assuredworkloads-frameworks-author` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `assuredworkloads-frameworks-navigator` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `basin` | 06-devops-guvenlik-performans | Cloudflare R2/Basin: ücretsiz kota, sonrası kullanım başına |
| `cloud-armor-crs-rule-upgrader` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-build-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-logging-configuration-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-logging-cross-project-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-logging-finops` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-logging-query-generation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-alert-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-chart-generation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-list-time-series-request` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-metric-selection` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-notification-channels-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-monitoring-promql-query` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-network-insights` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-operator` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-operator-setup` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-operator-share-context` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-run-alert-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-run-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloud-trace-querying` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `cloudflare` | 06-devops-guvenlik-performans | Cloudflare ücretsiz plan ile çalışır; bazı ürünler ücretli |
| `cloudflare-email-service` | 06-devops-guvenlik-performans | Cloudflare ücretsiz kota, sonrası ücretli |
| `cloudflare-one` | 06-devops-guvenlik-performans | Cloudflare Zero Trust ücretsiz plan (50 kullanıcıya kadar); kurumsal özellikler ücretli |
| `cloudflare-one-migrations` | 06-devops-guvenlik-performans | Cloudflare Zero Trust ücretsiz plan; kurumsal özellikler ücretli |
| `compute-future-reservations` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `compute-on-demand-reservations` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `compute-spot-capacity-advice` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `compute-vm-creation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `deploy-to-vercel` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; ekip/ticari kullanım ücretli |
| `detection-engineering-coverage-evaluation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `durable-objects` | 06-devops-guvenlik-performans | Workers ücretsiz planında sınırlı; fazlası ücretli |
| `gcloud` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-handle-disruption-gpu-tpu` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-jobset-interruption` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-node-unresponsive-timeout` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-dynamic-slices-monitoring` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-metrics-monitoring` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-mxla-hang` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-partition-overlap` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-performance-degradation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-reservation-stockout` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-slice-mig-stuck-updating` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-vbar-oom` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-ai-troubleshooting-tpu-vm-repair-stuck` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-alert-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-app-onboarding` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-backup-dr` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-batch-hpc` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-cluster-autoscaler` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-cluster-creation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-compute-classes` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-cost-analysis` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-cost-optimization` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-custom-golden-image-discovery` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-golden-path` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-inference` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-manifest-generation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-multitenancy` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-networking` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-node-notready` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-observability` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-platform-security` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-productionize` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-reliability` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-service-networking` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-storage` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-storage-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-upgrades` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-workload-identity` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-workload-scaling` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-workload-scaling-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-workload-security` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gke-workload-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-filestore-auditing` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-filestore-autoscale` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-filestore-log-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-filestore-nfs-browser` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-global-frontend-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-networking-observability` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-recipe-auth` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-recipe-foundation-builder` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-recipe-onboarding` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-scc-query` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-scc-remediation` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-slo-alert-configuration` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-cost-optimization` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-operational-excellence` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-performance-optimization` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-reliability` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-security` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-cloud-waf-sustainability` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `iam-helper-for-policy-management` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `iam-helper-for-policy-simulator` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `iam-helper-for-privileged-access-management` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `iam-helper-for-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `iap-agent-platform-troubleshooting` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `k2` | 06-devops-guvenlik-performans | Cloudflare ürünü: ücretsiz kota + kullanım başına ücret |
| `pathways-workload` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `retrieving-developer-knowledge` | 06-devops-guvenlik-performans | Google geliştirici bilgi API'si; API anahtarı gerekir (DEVELOPERKNOWLEDGE_API_KEY); Google hesabı/kota |
| `secops-cases` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `secops-detection-engineering` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `secops-hunt` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `secops-investigate` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `secops-triage` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `vercel-cli-with-tokens` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; ekip/ticari kullanım ücretli |
| `vercel-optimize` | 06-devops-guvenlik-performans | Vercel Hobby planı ücretsiz; bazı analizler ücretli planlarda |
| `workload-manager-basics` | 06-devops-guvenlik-performans | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `developer-device-platform-basics` | 08-mobil-uygulama | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `developer-device-platform-device-run` | 08-mobil-uygulama | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
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
| `agent-platform-access-audit` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-alert-configuration` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-architecture` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-autorater-customization` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-deploy` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-endpoint-management` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-eval-flywheel` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-inference` | 01-claude-api-mcp | Vertex AI Agent/Model platformu çıkarımı; GCP ücretli ama ücretsiz deneme/kredi var; OPENAI_API_KEY/MiniMax örnek üçüncü taraf model uçları |
| `agent-platform-migrate-from-ai-studio` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-model-registry` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-prompt-management` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-rag-engine-management` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-skill-registry` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-troubleshooting` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-tuning` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `agent-platform-tuning-management` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `claude-api` | 01-claude-api-mcp | Skill kod yazmaya/rehberliğe ücretsiz yardım eder; yazılan kodun Anthropic API çağrıları token bazlı ücretli |
| `claude-opus-4-5-migration` | 01-claude-api-mcp | Kod geçişi ücretsiz yapılır; geçirilen kodun API çağrıları ücretli |
| `connect` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `developing-genkit-dart@google` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `developing-genkit-go` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `developing-genkit-js` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `developing-genkit-python` | 01-claude-api-mcp | Genkit + Gemini API; Gemini ücretsiz katmanı var (AI Studio), üretim ücretli (GEMINI_API_KEY). Genkit kendisi açık kaynak |
| `gemini-agents-api` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `gemini-api` | 01-claude-api-mcp | Gemini API; Google AI Studio ücretsiz katmanı var, üretim/yüksek kota ücretli (GOOGLE_API_KEY) |
| `gemini-interactions-api` | 01-claude-api-mcp | Gemini API etkileşim uçları; AI Studio ücretsiz katmanı var, üretim ücretli (API anahtarı gerekir) |
| `gemini-live-api` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `google-agents-cli-onboarding` | 01-claude-api-mcp | Google Cloud skili; çoğu işlem faturalı bir GCP projesi ister (ücretsiz katman, sandbox ve deneme kredisi ücretsiz başlangıç sağlar, ağır kullanım ücretli) |
| `langsmith-observability` | 01-claude-api-mcp | LangSmith ücretsiz geliştirici katmanı |
| `caveman-setup` | 02-agent-orkestrasyon | Caveman Cloud gateway'e bağlar (CAVE_API_KEY); BYOK ile mevcut LLM anahtarı kullanılır, gateway'in ücretsiz katmanı var; diğer caveman skilleri anahtarsız |
| `context7-cli` | 03-web-arastirma-veri | Çoğu komut girişsiz ve ücretsiz çalışır; `ctx7 setup` ve daha yüksek istek sınırı için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `context7-docs` | 03-web-arastirma-veri | CONTEXT7_API_KEY ister (ücretsiz hesapla alınır); yoğun kullanım için ücretli plan. |
| `context7-mcp` | 03-web-arastirma-veri | Girişsiz ve ücretsiz çalışır (istek sınırı düşük); daha yüksek sınır için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `context7-mcp@upstash` | 03-web-arastirma-veri | Girişsiz ve ücretsiz çalışır (istek sınırı düşük); daha yüksek sınır için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `find-docs` | 03-web-arastirma-veri | Kimlik doğrulamasız ve ücretsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap/API anahtarı, yoğun kullanım için ücretli plan. |
| `graphify` | 03-web-arastirma-veri | Yerel graf çıkarımı ücretsiz; LLM tabanlı çıkarım için isteğe bağlı API anahtarı (ücretli) |
| `nlm-skill` | 03-web-arastirma-veri | nlm komutu ücretsizdir ve Google hesabıyla çalışır; kullanım kotaları Gemini Notebook planına bağlıdır (ücretsiz planda sınırlı) |
| `notebooklm` | 03-web-arastirma-veri | Google hesabı; NotebookLM kullanım kotaları/planları |
| `changelog-video` | 01-video-uretim-montaj | Yerel Whisper; HeyGen sesi isteğe bağlı |
| `cinecode` | 01-video-uretim-montaj | Film kodla üretilir ve ücretsiz çalışır. Seslendirme için Gemini TTS anahtarı (ücretsiz katmanı var) ya da isteğe bağlı ElevenLabs; stok arama için ücretsiz Pixabay anahtarı. Skill ücretli servis, anahtar ve büyük indirmeyi kullanıcı onayı olmadan kullanmaz. |
| `cut-silences` | 01-video-uretim-montaj | Transkript için ElevenLabs Scribe varsayılan sağlayıcıdır (kota/ücret); OpenAI Whisper ve yerel alternatifler ayrıca desteklenir, ücretsiz yol var |
| `edit-video` | 01-video-uretim-montaj | Transkript için ElevenLabs Scribe varsayılan sağlayıcıdır (kota/ücret); OpenAI Whisper ve yerel alternatifler ayrıca desteklenir, ücretsiz yol var |
| `figma` | 01-video-uretim-montaj | FIGMA_TOKEN (ücretsiz planla çalışır); değişkenler (variables) Enterprise ister |
| `hyperframes` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `hyperframes-cli` | 01-video-uretim-montaj | Yerel render ücretsiz; bulut render (HyperFrames OAuth) ücretli plan/kredi ister |
| `media-use` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HyperFrames kredisi/HeyGen isteğe bağlı. 2026-11: skill ücretli çağrıdan önce onay istemiyor (kredi sınırı dosyası var) ve ucuz seçeneğe kendiliğinden geçmiyor; ücretsiz yol açıkça istenmeli; Voice Turbo Free planda ayda 3 dk |
| `moneyprinterturbo-video` | 01-video-uretim-montaj | LLM API anahtarı zorunlu (ücretsiz katmanı olan sağlayıcılar kullanılabilir), Pexels anahtarı ücretsiz, Edge TTS ücretsiz. Üretilmiş video sağlayıcıları (Seedance/Ark, OFox, MiniMax, MuAPI, Infistar, Jalapeno) ücretli görev açar; yalnızca açık onayla. |
| `motion-showreel` | 01-video-uretim-montaj | Çekirdek (kod, kendi müziği) ücretsiz; scripts/kie.mjs (Kie.ai müzik/görsel/video, KIE_API_KEY) ve sfx.mjs (ElevenLabs, ELEVENLABS_API_KEY) ücretli üretim çağrıları yapar, skil onay ister |
| `open-edit` | 01-video-uretim-montaj | VEED barındırılan servisleri (transkript, arka plan silme, AI sunucu, lipsync) ve fal modelleri VEED/fal kredisi ister; render ve yerel araç takımı ücretsiz |
| `openmontage` | 01-video-uretim-montaj | Yerel araçlar ve stok kaynaklar ücretsiz; ElevenLabs, fal.ai gibi ücretli sağlayıcılar isteğe bağlı |
| `parody-short` | 01-video-uretim-montaj | Görsel, klip ve ses kullanıcının Modal uç noktalarında (aylık ücretsiz kota, fazlası ücretli); müzik acemusic ücretsiz anahtarla |
| `provider-refresh-oct23` | 01-video-uretim-montaj | Ücretli sağlayıcı adaptörlerinin (Gemini Omni, Veo, ElevenLabs v4, HeyGen…) güncel API sözleşmeleri; ücretsiz yerel yollar ayrı skillerde |
| `rea-video` | 01-video-uretim-montaj | Çözümleme CLI'ı ücretsiz (yerel); isteğe bağlı görsel model (VLM, REA_VLM_API_KEY) ve önerilen ChatCut yeniden yapım aracı üyelik/kredi ister (ücretli kısım isteğe bağlı) |
| `remotion` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `remotion-best-practices` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-best-practices@calesthio` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-maps` | 01-video-uretim-montaj | Harita karoları Mapbox/MapTiler (ücretsiz kota) ya da ücretsiz OSM kaynakları; Remotion şirket lisansı ayrıca |
| `remotion@openmontageinc` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `session-story` | 01-video-uretim-montaj | İsteğe bağlı Gemini (GEMINI_API_KEY) ile kare özeti; anahtar yoksa yerel çalışır. Not: yerel konuşma geçmişini okur (kullanıcı onayından sonra) |
| `short-form-edit` | 01-video-uretim-montaj | Transkript için ElevenLabs Scribe (varsayılan, alternatifleri var) ve üretilmiş ek görüntüler için isteğe bağlı Kie.ai; ikisi de ücretli servis, ücretsiz yol (yerel transkript, kendi görüntüleri) var |
| `short-form-video` | 01-video-uretim-montaj | Transkript için ElevenLabs Scribe varsayılan sağlayıcıdır (kota/ücret); OpenAI Whisper ve yerel alternatifler ayrıca desteklenir, ücretsiz yol var |
| `synthetic-ui-demo` | 01-video-uretim-montaj | Remotion şablonu yerelde render edilir; anlatıcı sesi ve konuşan kafa isteğe bağlı bulut GPU ya da ElevenLabs ister; Remotion lisansı şirketler için ücretli olabilir |
| `video-toolkit` | 01-video-uretim-montaj | Eski OpenMontage kopyası: açık modelleri kullanıcının Modal/RunPod hesabında çalıştırır; Modal Starter planında aylık ücretsiz işlem kotası var, fazlası ve RunPod ücretli (2026-11-15 yeniden değerlendirildi, önceden ucretli) |
| `video-use` | 01-video-uretim-montaj | ElevenLabs Scribe ücretsiz kotasıyla kullanılabilir; yoğun transkript ücretli. ffmpeg/Manim/PIL yerel ve ücretsiz |
| `video_toolkit` | 01-video-uretim-montaj | Açık modelleri kullanıcının Modal/RunPod hesabında çalıştırır; Modal Starter planında aylık ücretsiz işlem kotası, müzik acemusic ücretsiz anahtarla, ses efekti Openverse ücretsiz; ElevenLabs, Ideogram ve RunPod seçenekleri ücretli |
| `acestep` | 02-ses-muzik-konusma | Varsayılan yol acemusic bulut API'si, ücretsiz anahtarla çalışır; Modal'da kendi barındırma isteğe bağlı (aylık ücretsiz kota, fazlası ücretli) |
| `agents` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planındaki sesli agent dakikalarıyla denenebilir; üretim kullanımı ücretli |
| `azure-speech-to-text` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: faster-whisper |
| `azure-text-to-speech` | 02-ses-muzik-konusma | Azure Speech ücretsiz F0 katmanı (aylık sınırlı, kart ister); fazlası ücretli. Yerel ücretsiz yol: piper |
| `elevenlabs` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planı (aylık sınırlı kota) ile kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Kokoro) |
| `elevenlabs@openmontageinc` | 02-ses-muzik-konusma | ElevenLabs ücretsiz planı (aylık sınırlı kota) ile kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Kokoro) |
| `krillinai-cli` | 02-ses-muzik-konusma | TTS/LLM için MiniMax gibi sağlayıcı anahtarı gerekebilir; yerel yollar (whisper) var |
| `setup-api-key` | 02-ses-muzik-konusma | Sadece anahtar kurulum rehberi; ElevenLabs ücretsiz planıyla da çalışır |
| `sound-effects` | 02-ses-muzik-konusma | ElevenLabs ücretsiz kotasıyla kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Openverse + yerleşik efektler) |
| `sound-effects@barty-bart` | 02-ses-muzik-konusma | ElevenLabs ücretsiz kotasıyla kullanılabilir; fazlası ücretli. Tamamen ücretsiz yol: media-use (Openverse + yerleşik efektler) |
| `speech-to-text` | 02-ses-muzik-konusma | ElevenLabs Scribe ücretsiz kotası var; fazlası ücretli. Tamamen ücretsiz yol: media-use transcribe (Whisper/Parakeet) |
| `3d-asset-generation` | 03-ai-gorsel-video-modelleri | Üretim Atlas Cloud / fal.ai ile ücretli; CC0 Kenney kataloğu ve Blender yolu ücretsiz |
| `antigravity-gorsel` | 03-ai-gorsel-video-modelleri | Antigravity Google hesabıyla ücretsiz kullanılır; görsel üretim kotası hesabın Google planına bağlıdır |
| `comfyui` | 03-ai-gorsel-video-modelleri | Yerel ComfyUI ücretsiz; 'Partner Nodes' Comfy hesabı ve ön ödemeli kredi ister |
| `higgsfield-generate` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `higgsfield-marketplace-cards` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `higgsfield-product-photoshoot` | 03-ai-gorsel-video-modelleri | Higgsfield hesabı gerekir; ücretsiz planın sınırlı kredisi var, çoğu model ve yoğun kullanım ücretli plan ya da kredi ister. |
| `ltx2` | 03-ai-gorsel-video-modelleri | Açık model LTX-2.3 kullanıcının Modal hesabındaki uç noktada çalışır (aylık ücretsiz kota, fazlası ücretli); topluluk lisansı 10M$ altı gelirde ücretsiz |
| `ltx2@openmontageinc` | 03-ai-gorsel-video-modelleri | Açık model LTX-2.3 kullanıcının Modal hesabındaki uç noktada çalışır (aylık ücretsiz kota, fazlası ücretli); topluluk lisansı 10M$ altı gelirde ücretsiz |
| `provider-model-refresh` | 03-ai-gorsel-video-modelleri | Ücretli sağlayıcı adaptörleri; bazı modeller yerel (Qwen Image yerel) |
| `qwen-edit` | 03-ai-gorsel-video-modelleri | Varsayılan Modal uç noktası (aylık ücretsiz kota), RunPod seçeneği ücretli; Qwen-Image-2.1 seçeneği ticari olmayan lisanslı |
| `video-prompt-builder` | 03-ai-gorsel-video-modelleri | Video planı ve istem yazımı ücretsizdir; planın Seedance/Higgsfield'da üretilmesi kredi harcar. |
| `remotion-explainer-video` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `remotion-kinetic-typography` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `remotion-launch-video` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `remotion-logo-animation` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `remotion-motion-graphics` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `remotion-product-demo` | 04-motion-graphics-karakter | Remotion şablonları ücretsiz (MIT); isteğe bağlı snapcn Pro bileşenleri SNAPCN_API_KEY (abonelik) ister. HeyGen yalnız atıf |
| `snapcn` | 04-motion-graphics-karakter | Açık bileşenler ücretsiz (MIT); Pro bileşenler snapcn MCP/SNAPCN_API_KEY (abonelik) ister |
| `image` | 01-satis-pazarlama-musteri | Görsel üretimi için Gemini/Replicate/Ideogram/OpenAI API seçenekleri; Gemini API ücretsiz katmanı var, skill yönlendirme ve optimizasyon da yapar |
| `video` | 01-satis-pazarlama-musteri | AI avatar (HeyGen/Synthesia) ücretli; Remotion gibi programatik yollar ücretsiz. Yöntem seçimi skill'de |
| `trader-broker` | 02-finans-hukuk-ik | Alpaca: ücretsiz kâğıt (paper) hesapla denenir; gerçek hesapta komisyonsuz ama GERÇEK PARA riski — işlem öncesi kullanıcı onayı şart |
| `amazon-a-plus` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `amazon-white-background` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
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
| `multi-angle-set` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `multi-currency` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Open Exchange Rates (ücretsiz kota) |
| `order-fulfillment-workflow` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-management` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: Shippo (ücretsiz plan + etiket başı) |
| `returns-refund-policy` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `revenue-recognition-accounting` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: ücretli plan/servis seçeneği (ücretsiz plan ya da alternatif var) |
| `sale-banner` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `selling-point-infographic` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
| `shipment-tracking` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `shipping-rate-calculator` | 05-e-ticaret-pazaryeri | Entegrasyon kodu ücretsiz yazılır; bağlanan servis: EasyPost (ücretsiz kota + etiket başı) |
| `size-chart` | 05-e-ticaret-pazaryeri | GPT Image API (OpenAI ya da uyumlu) ücretli; agent yerleşik görsel aracıyla ya da istemi elle çalıştırarak ücretsiz kullanılabilir. Önerdiği tryallapi.com aracısına anahtar verme. |
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

Gizli entegrasyon kataloğundaki 0 Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var).
