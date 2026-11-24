# 01-claude-api-mcp — AI ve Otomasyon

_Claude API, MCP sunucusu, model geçişi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **7/38**

### academy-guide  ·  anthropics/skills @ e4bb5d9  ·  puan 89 (A)

- **Ne yapar:** Claude veya bir Claude ürününün nasıl kullanılacağına dair sorulara verilen cevabın sonuna, Claude Academy'den (academy.claude.com) yalnızca güçlü eşleşme varsa uygun kurs/eğitim/kullanım örneği önerisi ekler. Katalog skill içine gömülü değil; güncel JSON katalog çalışma anında çekilir ve tazeliği kontrol edilir.
- **Ne zaman:** Claude öğrenmeye yönelik destek/eğitim asistanları; ekibe Claude yaygınlaştırma soruları. · **Ne zaman değil:** Kod/proje agent'larında (iş ortasındaki kullanıcıya kurs önermek gürültü); web erişimi yoksa (katalog çekilemez, uydurma yasak). Skill yazımı ile ilgisi yok — kategorisi Claude ürün desteği.
- **Teknoloji:** web-fetch
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★199922, son güncelleme 2026-11-16, lisans yok)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 7.6 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV (projelere gerek yok). Anthropic resmi, uydurmayı engelleyen tazelik kuralları iyi; ama proje agent'ları için kullanım alanı yok.

### agent-platform-access-audit  ·  google/skills @ 4bb21eb  ·  puan 96 (A)

- **Ne yapar:** Audits AI agent data access, blast radius, and blocked policy operations in Google Cloud by querying Cloud Audit Logs via BigQuery. Use when investigating what resources or services an agent accessed, identifying top originating principals the agent is acting as, or triaging PERMISSION_DENIED errors to distinguish VPC Service Controls perimeter violations from IAM permission denials. Don't use for
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 11.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### agent-platform-agent-registry  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Manages Google Cloud Agent Registry (agentregistry.googleapis.com) resources using gcloud CLI and Kubernetes manifests, including agents, MCP servers, endpoints, services, bindings, AI applications, skills and skill revisions, resource-level IAM policies, Cloud Run and GKE automatic workload registration, Cloud Resource Manager management boundaries, 5-endpoint Quick Add for Agent Gateway, and Pyt
- **Teknoloji:** docker, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 123 KB (SKILL.md 33.3 KB, yük buyuk)
- **İnceleme:** otomatik

### agent-platform-alert-configuration  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Configures best-practice alerting policies for AI agents using OpenTelemetry (OTel) metrics, generating output as Terraform (.tf) configuration files. Use when analyzing, writing, or deploying alerting policies to monitor agent latency, error rates, token usage, and quality metrics. Don't use for standard infrastructure monitoring unrelated to AI agents, or when the agent is not instrumented with 
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 306 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-architecture  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Designs, engineers, and validates enterprise Gemini platform architectures. Use when designing multi-project hierarchies (Host, Central Governance Hub, Runtime Spoke, Tool/MCP Spoke), configuring Agent Gateway, authoring Agent Connectivity Templates (ALL_TRAFFIC vs PRIVATE_RANGES_ONLY), deploying Secure Web Proxy (SWP) with Policy-Based Routing (PBR) or Cross-Cloud mTLS Egress Hubs, configuring Pr
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 188 KB (SKILL.md 14.4 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-autorater-customization  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Customizes an autorater (evaluation metric) for an AI agent so its grades match the user's own judgment, starting from the agent's real trajectories. Use when a user wants a metric tailored to their agent, wants to turn failing trajectories into rubrics, says an existing autorater grades their agent wrong, or wants an autorater to agree with human labels (autorater hillclimbing, judge calibration)
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 76 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-deploy  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Deploy open models or custom weights from Model Garden to Agent Platform endpoints, check the status of an in-progress deployment operation, or clean up resources by undeploying models and deleting endpoints. Use when asked to actively deploy a model, list the Model Garden CATALOG of available models, check if a specific model is deployable (`gcloud ai model-garden models list-deployment-config`),
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 48 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-endpoint-management  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Manages Agent Platform serving endpoints. Use when you need to create, list, describe, update, or delete serving endpoints for model deployment on Agent Platform. Also use when troubleshooting endpoint permission, quota, or resource busy errors. Don't use for deploying models to endpoints or for running model evaluations.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### agent-platform-eval-flywheel  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Measures and improves the quality of AI models and agents on Google Cloud using the Eval Quality Flywheel methodology. Use when generating synthetic user scenarios, evaluating an agent or model, building an eval dataset, picking or writing evaluation metrics, analyzing failures, comparing results before and after a fix, or when guidance is needed on Agent Platform eval methodology — including data
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 127 KB (SKILL.md 30.2 KB, yük buyuk)
- **İnceleme:** otomatik

### agent-platform-inference  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Connects to and performs inference with Google Cloud Agent Platform GenAI models, including First-Party Gemini models and Third-Party OpenMaaS models (Llama, DeepSeek, Qwen, etc.). Use when asked to perform inference, ask a model a question, run a test prompt, execute chat completions, or generate code for calling Gemini or OpenMaaS models, authenticate with GenAI SDK, OpenAI SDK, or legacy Agent 
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 37.6 KB, yük buyuk)
- **İnceleme:** otomatik

### agent-platform-migrate-from-ai-studio  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Guides agents and users through migrating from Gemini API in Google AI Studio to Gemini Enterprise Agent Platform (formerly Vertex AI). Use this skill when moving applications to Google Cloud, to leverage Cloud credits, or to unify inferencing with other Cloud infrastructure (IAM, billing, telemetry).
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-model-registry  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Agent Platform Model Registry Management. Use when you need to upload, list, describe, update, or delete machine learning models (and their versions) in the Agent Platform Model Registry. Don't use for model training, model deployment to endpoints, or managing non-Agent Platform models.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-prompt-management  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Manages and orchestrates prompts in Agent Platform. Use when you need to create, list, retrieve, version, or delete managed prompts in Agent Platform. Don't use for model training, model deployment to endpoints, or managing non-Agent Platform prompts.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-rag-engine-management  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Manage and query Agent Platform RAG Engine Corpora and retrieve grounded contexts using the Google GenAI SDK. Use when listing RAG corpora or files, inspecting a corpus, retrieving contexts, or generating content grounded in a RAG corpus. Do not use for standard database queries (use SQL/Spanner skills), Google Workspace RAG, or other RAG products like gRAG.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 10.0 KB, yük orta)
- **İnceleme:** otomatik

### agent-platform-skill-registry  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Interact with the Gemini Enterprise Agent Platform Skill Registry to create and search for available skills. Use this skill to enable agents to register functionality or discover new capabilities.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### agent-platform-troubleshooting  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Troubleshoots Google Cloud Gemini Enterprise Agent Platform issues across Agent Gateway, Agent Connectivity Templates (ACT), Agent Registry, Agent Identity, Identity-Aware Proxy (IAP), Unified Access Policies (UAP), Model Armor, Semantic Governance Policies (SGP), Cloud DNS peering, Private CA TrustConfig, Next-Hop Secure Web Proxy (SWP), Explicit HTTPS Proxy (L4 AuthzPolicy), and Cloud Trace. Use
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 398 KB (SKILL.md 26.2 KB, yük buyuk)
- **İnceleme:** otomatik

### agent-platform-tuning  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Agent Platform Model Tuning. Use when you need to fine-tune open models or Gemini models using Agent Platform infrastructure. Don't use for model training outside Agent Platform, model deployment to endpoints (use `agent-platform-deploy`), or managing serving endpoints (use `agent-platform-endpoint-management`).
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 98 KB (SKILL.md 41.0 KB, yük buyuk)
- **İnceleme:** otomatik

### agent-platform-tuning-management  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Manages GenAI tuning jobs in Agent Platform. Use this to list, get, or cancel ongoing model tuning jobs. Don't use for fine-tuning models (use `agent-platform-tuning`), deploying models to endpoints (use `agent-platform-deploy`), or managing serving endpoints (use `agent-platform-endpoint-management`).
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### build-mcp-app  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model,
- **Teknoloji:** api-anahtari, css, html, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 18.9 KB, yük orta)
- **İnceleme:** otomatik

### build-mcp-server  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP,
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 49 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### build-mcpb  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set 
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### claude-api  ·  anthropics/skills @ e4bb5d9  ·  puan 91 (A)

- **Ne yapar:** Claude API / Anthropic SDK için kapsamlı ve güncel başvuru: model kimlikleri ve fiyatlar, adaptive thinking, streaming, araç kullanımı, prompt caching, compaction, MCP, Managed Agents, Files/Skills API. Dil algılayıp (Python, TS, Go, Java, C#, PHP, Ruby, cURL) ilgili klasörü okutur; migrate, prompt-audit, upgrade, cost-optimize, build-eval, hillclimb alt komutları içerir.
- **Ne zaman:** Claude çağıran her kod: yeni LLM özelliği, agent/araç tanımı, model geçişi, maliyet optimizasyonu, eval kurma, SDK sürüm yükseltme. · **Ne zaman değil:** Projede başka sağlayıcı (OpenAI, Gemini, Ollama…) kullanılıyorsa — skill bunu kendisi kontrol eder. SKILL.md 103 KB: rol bütçesinin büyük kısmını yer; sadece Claude entegrasyonu yapan agent'a ver. Codex'te: WebFetch gibi Claude araç adları geçiyor; Codex'in web/arama aracıyla aynı adımlar uygulanır, içerik ve kod kalıpları aynen geçerli.
- **Teknoloji:** anthropic-sdk, python, typescript, go, java, csharp, php, ruby, curl · **Paketler:** anthropic (pip) veya @anthropic-ai/sdk (npm) — dile göre resmi SDK, ANTHROPIC_API_KEY
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★199922, son güncelleme 2026-11-16, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-api-gecis → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 2031 KB (SKILL.md 102.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic resmi, sürekli güncel (model listesi 2026-10-06), API kayması uyarı tablosu ve dil başına doğrulanmış kalıplar. Tek eksi: SKILL.md 103 KB, klasör 2.2 MB. claude-opus-4-5-migration'ın işini 'migrate' alt komutu güncel modellerle yapıyor.

### claude-opus-4-5-migration  ·  anthropics/claude-code @ 5ed799e  ·  puan 72 (B)

- **Ne yapar:** Sonnet 4.0/4.5 ve Opus 4.1'den Opus 4.5'e tek seferlik geçiş: platforma göre (Anthropic, Bedrock, Vertex, Azure) model dizgelerini değiştirir, desteklenmeyen beta başlığını kaldırır, effort parametresi ekler ve Opus 4.5 davranış farklarına göre (araç aşırı tetikleme, aşırı mühendislik) istem ayarı önerir.
- **Ne zaman:** Yalnızca hedef özellikle Opus 4.5 ise (eski kod tabanlarını tam bu sürüme sabitlemek). · **Ne zaman değil:** Güncel modellere (Opus 5.5, Sonnet 5.5, Fable 5.1) geçişte — claude-api 'migrate' alt komutu kullanılmalı. Haiku 4.5 geçişi kapsam dışı.
- **Teknoloji:** anthropic-sdk
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-api-gecis → alternatif
- **Boyut:** 12 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İyi yazılmış ama eskidi: hedef model Opus 4.5 ve 1M bağlam notu artık geçerli değil. Aynı iş claude-api/shared/model-migration.md'de güncel.

### connect  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 71 (B)

- **Ne yapar:** Composio SDK (Python/TS) ile agent'ı Gmail, Slack, GitHub, Notion gibi 1000+ uygulamaya bağlar; e-posta gönderme, issue açma, mesaj atma gibi gerçek eylemler yaptırır. API anahtarı, OAuth akışı, framework desteği ve sorun giderme anlatılır.
- **Ne zaman:** Kendi uygulamasında/agent'ında harici servislere eylem yaptırmak isteyen projeler (Composio kullanmayı kabul ederek). · **Ne zaman değil:** Üçüncü taraf aracı servise (Composio) veri/OAuth yetkisi vermek istenmiyorsa; tek bir servis için resmi MCP sunucusu varsa. Gerçek e-posta/mesaj gönderir — onaysız çalıştırma.
- **Teknoloji:** composio, python, typescript, oauth · **Paketler:** composio (pip) veya @composio/core (npm), COMPOSIO_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★80247, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** composio-baglanti → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil, Composio grubunda). Kurulum ve kod örnekleri kısa ve çalışır; pazarlama dili yoğun. Araçtan bağımsız (SDK) olduğu için connect-apps'e tercih edildi.

### developing-genkit-dart@google  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance on developing AI-powered applications using the Genkit Dart SDK. Use when the user asks to build AI agents in Dart, use Genkit flows, or integrate LLMs into Dart/Flutter applications. Don't use for Genkit in JavaScript/TypeScript, Go, or Python.
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 155 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik
- **Not:** Aynı ad, iki kaynak: bu kayıt google/skills resmî Google Genkit Dart geliştirme skili (alternatif). Çıplak adı ve tercihi evanca/flutter-ai-rules kaydı taşıyor (durum_elle ile sabit); bu kaynağın önceliği (1) daha yüksek olsa da çıplak ad kendiliğinden el değiştirmez. ad_devral kararı ana oturumun.

### developing-genkit-go  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance on developing AI-powered applications using Genkit in Go. Use when the user asks to build AI features, agents, flows, or tools in Go using Genkit, or when working with Genkit Go code involving generation, prompts, streaming, tool calling, or model providers. Don't use for Genkit in JavaScript/TypeScript, Python, or Dart.
- **Teknoloji:** python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 156 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### developing-genkit-js  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance on developing AI-powered applications using Genkit in Node.js/TypeScript. Use when the user asks about Genkit, AI agents, flows, or tools in JavaScript/TypeScript, or when encountering Genkit errors, validation issues, type errors, or API problems. Don't use for Genkit in Python, Go, or Dart.
- **Teknoloji:** next.js, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 130 KB (SKILL.md 13.1 KB, yük orta)
- **İnceleme:** otomatik

### developing-genkit-python  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance on developing AI-powered applications using Genkit Python (0.13) and migrating Genkit Python 0.12 projects to 0.13. Use when building AI agents, flows, tools, structured outputs, or FastAPI routes in Python, upgrading from Genkit 0.12, or debugging Genkit imports, config errors, or traces. Don't use for Genkit in JavaScript/TypeScript, Go, or Dart.
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 156 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik

### gemini-agents-api  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Manages custom Agent resources on Gemini Enterprise Agent Platform. Use when the user wants to programmatically create, configure, list, update, or delete stateful, server-managed Agent resources (including mounting files, skills, and tools) before executing conversations.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 12.9 KB, yük orta)
- **İnceleme:** otomatik

### gemini-api  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Integrates Gemini models on Gemini platform (formerly Gemini Enterprise Agent Platform and Vertex AI) using the unified Google Gen AI SDK across Python, TypeScript/JavaScript, Go, Java, and C#. Use for Google Cloud AI workloads: text/multimodal generation, structured JSON, function calling, Search grounding, code execution, URL context, Nano Banana images, Gemini Omni and Veo video, TTS, Lyria mus
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 49 KB (SKILL.md 8.3 KB, yük orta)
- **İnceleme:** otomatik

### gemini-interactions-api  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Guides the usage of Gemini Interactions API on Gemini Enterprise Agent Platform. Use when the user wants to use the stateful, server-managed Interactions API for multi-turn conversations, background execution, streaming, structured output, and function calling on the Agent Platform.
- **Teknoloji:** api-anahtari, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 16.7 KB, yük orta)
- **İnceleme:** otomatik

### gemini-live-api  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Builds, integrates, and troubleshoots Gemini Enterprise Agent Platform Live API (BidiGenerateContent) WebSocket clients and sessions. Use when scaffolding a LiveAPI client or demo UI/backend (GA v1 WebSockets, isolated Python venv, ADC bearer token refresh, transparent session resumption, ClientMessage and ServerMessage JSON protos, tool responses, context_update, interrupt and transcription handl
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 124 KB (SKILL.md 26.9 KB, yük buyuk)
- **İnceleme:** otomatik

### google-agents-cli-onboarding  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Onboarding entrypoint for agents-cli in Agent Platform. It should be used when the user wants to "create a new agent", "develop an agent", "build an agent using ADK", "run the agent locally", "debug agent code", "test an agent", "evaluate an agent", "deploy an agent", "publish an agent", "monitor an agent", or needs the ADK (Agent Development Kit) development lifecycle.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### langsmith-observability  ·  Orchestra-Research/AI-Research-SKILLs @ 773a529  ·  puan 85 (A)

- **Ne yapar:** LLM observability platform for tracing, evaluation, and monitoring. Use when debugging LLM applications, evaluating model outputs against datasets, monitoring production systems, or building systematic testing pipelines for AI applications.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Orchestra-Research (kurum, ★14802, son güncelleme 2026-10-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### mcp-builder  ·  anthropics/skills @ e4bb5d9  ·  puan 97 (A)

- **Ne yapar:** Yüksek kaliteli MCP sunucusu geliştirme rehberi: araştırma/planlama (araç adlandırma, bağlam yönetimi, hata mesajları), Python FastMCP veya TypeScript MCP SDK v2 (@modelcontextprotocol/server; v1 yalnızca mevcut projeler için, codemod ile geçiş) ile uygulama, MCP Inspector ile test ve 10 soruluk değerlendirme (eval) seti; değerlendirmeyi çalıştıran evaluation.py betiği içerir.
- **Ne zaman:** Harici bir API/servisi agent'lara açan yeni MCP sunucusu yazmak ve değerlendirmek. · **Ne zaman değil:** Mevcut bir MCP sunucusunu Claude Code eklentisine bağlamak (mcp-integration); protokol sürüm geçişi/güvenlik denetimi ağırlıklı işler (mcp-builder@vudovn daha güncel).
- **Teknoloji:** mcp, python, typescript · **Paketler:** mcp / fastmcp (pip) veya @modelcontextprotocol/server + zod (npm, SDK v2; eski projelerde @modelcontextprotocol/sdk v1), @modelcontextprotocol/inspector, anthropic (eval betiği için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★199922, son güncelleme 2026-11-16, lisans yok)
- **Durum:** tercih · **Örtüşme:** mcp-sunucu-gelistirme → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 155 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic resmi, ComposioHQ kopyasından daha güncel ve kısa; dil rehberleri ve eval betiği tek pakette. vudovn sürümü spec/güvenlik tarafını tamamlıyor; birincil bu çünkü uçtan uca iş akışı ve değerlendirme aracı içeriyor.

### mcp-builder@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 82 (A)

- **Ne yapar:** MCP sunucu ve istemci mühendisliği: kararlı 2026-07-28 spesifikasyonuna göre durumsuz istek modeli, taşıma ve kimlik doğrulama, araç girdi/çıktı şemaları, $ref güvenliği, araç/kaynak/istem tasarımı, güvenlik gereksinimleri, eklentiler (Tasks, Skills over MCP, MCP Apps), eski sürümlerden geçiş ve test matrisi.
- **Ne zaman:** MCP sunucu/istemcisini güncel spesifikasyona taşımak, güvenlik/birlikte çalışabilirlik incelemesi, şema tasarımı. · **Ne zaman değil:** Sıfırdan sunucu yazıp değerlendirme seti kurmak için anthropics/mcp-builder ile birlikte kullan (tek başına iş akışı/kod iskeleti vermez). allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** mcp, json-schema
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** mcp-sunucu-gelistirme → tamamlayıcı · **Roller:** ai-entegrasyon
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Üç sürüm içinde en güncel spesifikasyon bilgisi ve güvenlik kontrol listesi; MIT, 10 KB. İş akışı ve eval aracı olmadığı için birincil değil.

### mcp-integration  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for 
- **Teknoloji:** api-anahtari, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### mcp-integration@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 80 (A)

- **Ne yapar:** Claude Code eklentilerine MCP sunucusu paketleme rehberi: .mcp.json ya da plugin.json içinde mcpServers, stdio/SSE/HTTP/WebSocket sunucu tipleri, ${CLAUDE_PLUGIN_ROOT} ve ortam değişkeni genişletme, MCP araç adlandırması (mcp__eklenti__sunucu__araç), yaşam döngüsü ve OAuth/token kimlik doğrulama kalıpları.
- **Ne zaman:** Bir Claude Code eklentisine hazır MCP sunucusu eklemek/yapılandırmak. · **Ne zaman değil:** MCP sunucusunun kendisini yazmak için (mcp-builder). Codex'te eklenti paketleme yok: MCP sunucusu `~/.codex/config.toml` dosyasında `[mcp_servers.<ad>]` tablosuyla (command, args, env ya da url) tanımlanır; .mcp.json ve ${CLAUDE_PLUGIN_ROOT} kullanılmaz. Sunucu tipleri, kimlik doğrulama ve güvenlik bölümleri Codex'te de geçerli, plugin.json kısımlarını atla.
- **Teknoloji:** mcp, claude-code, json
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-plugin-mcp → birincil · **Roller:** skill-gelistirici
- **Boyut:** 46 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi plugin-dev setinin parçası; örnek ve referans dosyaları zengin. Claude Code eklentisine özgü; Codex için yukarıdaki uyarlama gerekir.
