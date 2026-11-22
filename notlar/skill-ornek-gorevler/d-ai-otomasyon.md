# Örnek görevler ve test sonucu › d-ai-otomasyon

[← TEST_RAPORU.md](../../TEST_RAPORU.md) · 2026-11-22 · 160 skill. Örnek görev: elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki "Use when …".

| Skill | Sonuç | Örnek görev |
|---|---|---|
| `academy-guide` | ⚠️ | Claude öğrenmeye yönelik destek/eğitim asistanları; ekibe Claude yaygınlaştırma soruları. |
| `agent-platform-access-audit` | ⚠️ | investigating what resources or services an agent accessed, identifying top originating principals the agent is acting as, or triaging PERMISSION_DENIED errors  |
| `agent-platform-agent-registry` | ❌ | registering, discovering, searching, filtering, or governing agents, MCP servers, endpoints, skills, AI applications, or management boundaries in Google Cloud A |
| `agent-platform-alert-configuration` | ✅ | analyzing, writing, or deploying alerting policies to monitor agent latency, error rates, token usage, and quality metrics |
| `agent-platform-architecture` | ✅ | designing multi-project hierarchies (Host, Central Governance Hub, Runtime Spoke, Tool/MCP Spoke), configuring Agent Gateway, authoring Agent Connectivity Templ |
| `agent-platform-autorater-customization` | ✅ | a user wants a metric tailored to their agent, wants to turn failing trajectories into rubrics, says an existing autorater grades their agent wrong, or wants an |
| `agent-platform-deploy` | ✅ | asked to actively deploy a model, list the Model Garden CATALOG of available models, check if a specific model is deployable (`gcloud ai model-garden models lis |
| `agent-platform-endpoint-management` | ✅ | you need to create, list, describe, update, or delete serving endpoints for model deployment on Agent Platform |
| `agent-platform-eval-flywheel` | ✅ | generating synthetic user scenarios, evaluating an agent or model, building an eval dataset, picking or writing evaluation metrics, analyzing failures, comparin |
| `agent-platform-inference` | ✅ | asked to perform inference, ask a model a question, run a test prompt, execute chat completions, or generate code for calling Gemini or OpenMaaS models, authent |
| `agent-platform-migrate-from-ai-studio` | ✅ | moving applications to Google Cloud, to leverage Cloud credits, or to unify inferencing with other Cloud infrastructure (IAM, billing, telemetry). |
| `agent-platform-model-registry` | ✅ | you need to upload, list, describe, update, or delete machine learning models (and their versions) in the Agent Platform Model Registry |
| `agent-platform-prompt-management` | ✅ | you need to create, list, retrieve, version, or delete managed prompts in Agent Platform |
| `agent-platform-rag-engine-management` | ✅ | listing RAG corpora or files, inspecting a corpus, retrieving contexts, or generating content grounded in a RAG corpus |
| `agent-platform-skill-registry` | ✅ | enable agents to register functionality or discover new capabilities. |
| `agent-platform-troubleshooting` | ✅ | agent requests fail with 401/403/404/498/500/503 or Code 13, Egress request is not authorized, HTTP CONNECT fails with 404, Agent Runtime crashes on startup, or |
| `agent-platform-tuning` | ✅ | you need to fine-tune open models or Gemini models using Agent Platform infrastructure |
| `agent-platform-tuning-management` | ✅ | fine-tuning models (use `agent-platform-tuning`), deploying models to endpoints (use `agent-platform-deploy`), or managing serving endpoints (use `agent-platfor |
| `build-mcp-app` | ✅ | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP |
| `build-mcp-server` | ✅ | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Cl |
| `build-mcpb` | ✅ | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP",  |
| `claude-api` | ✅ | Claude çağıran her kod: yeni LLM özelliği, agent/araç tanımı, model geçişi, maliyet optimizasyonu, eval kurma, SDK sürüm yükseltme. |
| `claude-opus-4-5-migration` | ✅ | Yalnızca hedef özellikle Opus 4.5 ise (eski kod tabanlarını tam bu sürüme sabitlemek). |
| `connect` | ✅ | Kendi uygulamasında/agent'ında harici servislere eylem yaptırmak isteyen projeler (Composio kullanmayı kabul ederek). |
| `developing-genkit-dart@google` | ✅ | the user asks to build AI agents in Dart, use Genkit flows, or integrate LLMs into Dart/Flutter applications |
| `developing-genkit-go` | ✅ | the user asks to build AI features, agents, flows, or tools in Go using Genkit, or when working with Genkit Go code involving generation, prompts, streaming, to |
| `developing-genkit-js` | ✅ | the user asks about Genkit, AI agents, flows, or tools in JavaScript/TypeScript, or when encountering Genkit errors, validation issues, type errors, or API prob |
| `developing-genkit-python` | ✅ | building AI agents, flows, tools, structured outputs, or FastAPI routes in Python, upgrading from Genkit 0.12, or debugging Genkit imports, config errors, or tr |
| `gemini-agents-api` | ✅ | the user wants to programmatically create, configure, list, update, or delete stateful, server-managed Agent resources (including mounting files, skills, and to |
| `gemini-api` | ✅ | Google Cloud AI workloads: text/multimodal generation, structured JSON, function calling, Search grounding, code execution, URL context, Nano Banana images, Gem |
| `gemini-interactions-api` | ✅ | the user wants to use the stateful, server-managed Interactions API for multi-turn conversations, background execution, streaming, structured output, and functi |
| `gemini-live-api` | ✅ | scaffolding a LiveAPI client or demo UI/backend (GA v1 WebSockets, isolated Python venv, ADC bearer token refresh, transparent session resumption, ClientMessage |
| `google-agents-cli-onboarding` | ✅ | Onboarding entrypoint for agents-cli in Agent Platform. |
| `langsmith-observability` | ✅ | debugging LLM applications, evaluating model outputs against datasets, monitoring production systems, or building systematic testing pipelines for AI applicatio |
| `mcp-builder` | ✅ | Harici bir API/servisi agent'lara açan yeni MCP sunucusu yazmak ve değerlendirmek. |
| `mcp-builder@vudovn` | ✅ | MCP sunucu/istemcisini güncel spesifikasyona taşımak, güvenlik/birlikte çalışabilirlik incelemesi, şema tasarımı. |
| `mcp-integration` | ✅ | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol",  |
| `mcp-integration@anthropics` | ✅ | Bir Claude Code eklentisine hazır MCP sunucusu eklemek/yapılandırmak. |
| `batch-operations` | ✅ | Kod tabanında desen tabanlı toplu değişiklik: fonksiyon yeniden adlandırma, API geçişi, sürüm numarası güncelleme. |
| `behavioral-modes` | ✅ | ag-kit ailesini kuran projelerde agent'ın tonunu/yaklaşımını göreve göre değiştirmek. |
| `cavecrew` | ✅ | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or  |
| `caveman` | ✅ | /caveman, "caveman mode", "talk like caveman", "be brief", "less tokens" |
| `caveman-commit` | ✅ | "write a commit", "commit message", /commit or /caveman-commit. |
| `caveman-compress` | ✅ | /caveman-compress. |
| `caveman-discover` | ✅ | "discover workflows" or breaking LLM spend down by workflow. |
| `caveman-evidence-review` | ✅ | asked what Caveman found or where LLM spend goes. |
| `caveman-explore` | ✅ | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. |
| `caveman-help` | ✅ | /caveman-help or "caveman help". |
| `caveman-learn` | ✅ | asked to lower an agent's token cost, what caveman has saved, to trim a heavy CLAUDE.md, or to offload re-pasted context into cavemem. |
| `caveman-manage` | ✅ | asked to start, approve, cancel, promote or roll back a Caveman experiment. |
| `caveman-optimize` | ✅ | asked to inspect or evaluate a Caveman optimization report |
| `caveman-review` | ✅ | /caveman-review, "review this PR", or "review the diff". |
| `caveman-setup` | ✅ | "set up caveman" or adding LLM spend observability. |
| `caveman-stats` | ✅ | /caveman-stats. |
| `claude-automation-recommender` | ✅ | user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude C |
| `claude-md-improver` | ✅ | user asks to check, audit, update, improve, or fix CLAUDE.md files |
| `codex-radar` | ✅ | the user asks to run Codex Radar, score how they work with Codex, analyze Codex collaboration, or generate a Codex Radar report |
| `context-compression` | ✅ | 20+ turluk oturumlar, agent tekrar etmeye başladığında, iş aşaması değişiminde. |
| `context-engineering` | ✅ | Yeni oturum/proje kurulumu, kural dosyası yazımı, agent çıktı kalitesi düştüğünde, kod tabanının farklı bölümüne geçerken. |
| `coordinator-mode` | ✅ | Birden çok alanı kapsayan büyük görevde agent'ın kendisi kod yazmadan işçi alt-agent'ları yönetmesi. |
| `creative-director` | ✅ | AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calibrated against Cannes |
| `diagnosing-superpowers` | ✅ | superpowers skill ailesiyle çalışan oturumların neden yanlış gittiğini incelemek, bakımcılara hata raporu hazırlamak. |
| `discernment-nudge` | ✅ | Tavsiye, plan, tahmin, veri yorumu gibi kullanıcının harekete geçeceği çıktılar üreten sohbet/asistan agent'ları. |
| `dispatching-parallel-agents` | ✅ | Birbirinden bağımsız birden çok hata/araştırma işini paralel yürütmek. |
| `full-output-enforcement` | ✅ | Overrides default LLM truncation behavior. |
| `intelligent-routing` | ✅ | ag-kit'in uzman agent tanımlarının kurulu olduğu projelerde. |
| `investigate-first` | ✅ | unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses. |
| `lean-build` | ✅ | new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop condition matter. |
| `megacave` | ✅ | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. |
| `memory-system` | ✅ | Harness'in yerleşik belleği olmayan ortamlarda (ya da projeye taşınabilir, git'te tutulan bellek istendiğinde) tercih ve kararları saklamak. |
| `migration` | ✅ | schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation proof. |
| `n8n-agents` | ✅ | building or editing any @n8n/n8n-nodes-langchain.* AI node — an AI Agent, LLM chain, Text Classifier, or Information Extractor — and whenever the user mentions  |
| `n8n-binary-and-data` | ✅ | working with files, images, PDFs, attachments, uploads or downloads, base64, vision/multimodal input, or when an AI agent needs a file as tool input or output — |
| `n8n-code-javascript` | ✅ | a Code node is already in the workflow (editing it, fixing an error, choosing its mode, making it faster), or when a new one is justified: no native node fits ( |
| `n8n-code-python` | ✅ | the user explicitly wants Python in a Code node, when migrating old Pyodide/"Python (Beta)" code that used _input/_json/_node/_now, or when a Python Code node f |
| `n8n-code-tool` | ✅ | building a Code Tool attached to an AI Agent, writing code that an LLM will invoke, parsing the `query` input, returning a string result, defining an input sche |
| `n8n-error-handling` | ✅ | building any webhook/API workflow, a scheduled or unattended workflow, or any path where a silent failure would drop user-visible work — and whenever the user m |
| `n8n-expression-syntax` | ✅ | writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, mapping data between nodes, or referencing webho |
| `n8n-mcp-tools-expert` | ✅ | searching for nodes, validating configurations, accessing templates, managing workflows, organizing workflows into folders, managing credentials, auditing insta |
| `n8n-multi-instance` | ✅ | an n8n-mcp account targets more than one n8n instance — i.e |
| `n8n-node-configuration` | ✅ | configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration p |
| `n8n-self-hosting` | ✅ | the user wants to self-host, install, provision, or deploy n8n on their own server/VPS (Hetzner, DigitalOcean, AWS EC2, bare metal) — single/regular mode or que |
| `n8n-subworkflows` | ✅ | extracting shared logic, building anything multi-step or reused across workflows, or any workflow over ~10 nodes — and whenever the user mentions sub-workflows, |
| `n8n-validation-expert` | ✅ | encountering validation errors, validation warnings, false positives, operator structure issues, or need help understanding validation results |
| `n8n-workflow-patterns` | ✅ | building new workflows, designing workflow structure, choosing workflow patterns, planning workflow architecture, or asking about webhook processing, HTTP API i |
| `parallel-agents` | ✅ | Güvenlik/izolasyon kuralları önemli olan çok agent'lı işler; delegasyon bütçesi ve izleme gerektiğinde. |
| `project-artifact` | ✅ | a piece of work spans several workstreams and you want a shareable overview kept current |
| `receipts` | ✅ | the user asks for "receipts", an "impact report", "usage report", wants to "show my Claude Code activity", "prove the value of Claude Code", or runs `/receip |
| `safe-refactor` | ✅ | extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits. |
| `session-report` | ✅ | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. |
| `subagent-driven-development` | ✅ | Bağımsız görevlere bölünmüş bir planı tek oturumda yüksek kaliteyle uygulamak. |
| `surgical-patch` | ✅ | regression proof, preserved surrounding behavior, and task-relevant tests matter. |
| `ultracave` | ✅ | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. |
| `using-agent-skills` | ✅ | agent-skills ailesinden birden çok skill kurulu projelerde oturum başında doğru skill'i seçmek. |
| `using-n8n-mcp-skills` | ✅ | building, editing, validating, testing, or debugging an n8n workflow through the n8n-mcp MCP server — designing a flow, configuring a node, writing an expressio |
| `using-superpowers` | ✅ | superpowers ailesinin (brainstorming, writing-plans, systematic-debugging, subagent-driven-development…) birlikte kurulduğu projeler. |
| `verify-and-stop` | ✅ | validation-only tasks, completion checks, focused gate runs, and last-mile proof. |
| `agent-reach` | ✅ | Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. |
| `context7-cli` | ✅ | Context7'yi bir araca kurmak ya da ctx7 komutlarını doğrudan kullanmak. |
| `context7-docs` | ✅ | pi aracıyla ya da API anahtarlı doğrudan Context7 kullanımı. |
| `context7-mcp` | ✅ | Context7 MCP sunucusu kurulu ortamlarda kütüphane dokümanı getirme. |
| `context7-mcp@upstash` | ✅ | Çıplak adlı context7-mcp yerine daha ayrıntılı tetikleme açıklaması isteniyorsa. |
| `context7-mcp@upstash-2` | ✅ | This skill should be used when the user asks about libraries, frameworks, API references, or needs code examples. |
| `find-docs` | ✅ | Modelin eğitim verisi eskimiş olabilecek her kütüphane sorusu: kurulum, yapılandırma, sürüm geçişi, API sözdizimi. |
| `graphify` | ⚠️ | any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be tre |
| `nlm-skill` | ✅ | nlm ile Gemini Notebook'u komut satırından ya da MCP ile otomatikleştirmek, kaynaklara dayalı içerik üretmek. |
| `notebooklm` | ✅ | Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. |
| `youtube-arama` | ✅ | YouTube'dan gerçek video listesi ve metadata gerektiğinde: konu araştırması, rakip kanal incelemesi, içerik fikri için izlenme karşılaştırması. |
| `agent-development` | ✅ | . |
| `agent-development@anthropics` | ✅ | Claude Code projesine/eklentisine özel alt-agent tanımı yazmak ya da mevcut agent'ın tetiklenmesini düzeltmek. |
| `breakdown-diagnosis` | ✅ | When a machine goes down, reads the sensor window before the failure, the asset's maintenance history including the free-text close-out notes technicians actual |
| `breakdown-to-next-report` | ✅ | someone says \"run the breakdown chain,\" \"a machine went down,\" \"diagnose this and get it into the report,\" or \"breakdown to next report.\ |
| `climb` | ✅ | a champion wants to help someone move up a step. |
| `command-development` | ✅ | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command fr |
| `command-development@anthropics` | ✅ | Ekipte tekrar eden istemleri Claude Code slash komutuna çevirmek. |
| `cowork-plugin-customizer` | ✅ | : customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, m |
| `create-cowork-plugin` | ✅ | users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin |
| `custom-connector` | ✅ | Gets the plugin talking to a manufacturing system that has no vendor MCP, working down a seven-tier access ladder in order — vendor MCP, community MCP, a scoped |
| `customer-inquiry-intake` | ✅ | Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal export, a phone photo of a marked-up print, or a forw |
| `daily-production-report` | ✅ | Produces the morning production report: output against plan by line, cell and product; OEE with availability, performance and quality shown separately; the down |
| `data-consolidate` | ✅ | Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor M3), sales orders, production work orders, purcha |
| `design-space-explore` | ✅ | Generates a batch of CAD variants directly in Autodesk Fusion by applying changed parameters to an engineer's existing model, never designing from scratch and n |
| `faq` | ✅ | a champion keeps answering the same questions. |
| `hackathon` | ✅ | a champion wants to run a hack day or a shorter hack session. |
| `hook-development` | ✅ | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks",  |
| `hook-development@anthropics` | ✅ | Tehlikeli komutu engelleme, düzenleme sonrası otomatik format/test, oturum başında bağlam yükleme gibi olay tabanlı Claude Code otomasyonu. |
| `i-have-adhd` | ✅ | Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estima |
| `inspection-to-capa` | ✅ | someone says \"run the CAPA chain,\" \"take this nonconformance through to an 8D,\" \"inspection to CAPA,\" or asks for the full corrective-action workflow. |
| `library-curator` | ✅ | the user asks to reuse an image they captured/uploaded earlier, "pull a logo/screenshot from my library", or to find and drop a stored asset into the page being |
| `maturity` | ✅ | a champion wants to know where their org or team stands, or to compare with an earlier report. |
| `morning-plant-pulse` | ✅ | someone says \"run the morning pulse,\" \"do the overnight report,\" \"morning plant pulse,\" \"u |
| `ncr-writeup` | ✅ | Writes the nonconformance report: what was found and measured, the specific requirement it violates cited to its document and locator, how many parts are actual |
| `od-next-media-inputs` | ⚠️ | Prepare required media inputs within an existing OD Next plan. |
| `office-hours` | ✅ | a champion wants a regular time for teammates to bring problems. |
| `onboarding@anthropics` | ✅ | Sets the plugin up for one plant on first run. |
| `patterns` | ✅ | a champion wants to know what the team should reuse or learn from. |
| `plugin-settings` | ✅ | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state |
| `plugin-settings@anthropics` | ✅ | Proje başına açılıp kapatılabilen ya da yapılandırılabilen bir Claude Code eklentisi yazarken. |
| `plugin-structure` | ✅ | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plu |
| `plugin-structure@anthropics` | ✅ | Yeni Claude Code eklentisi iskeleti kurmak, bileşenleri düzenlemek, marketplace'e hazırlamak. |
| `quote-build` | ✅ | some |
| `reverse-any-video` | ✅ | Bir videoyu kopyalayıp/yeniden yapıp düzenlenebilir proje olarak elde etmek; elinde hakkı olan bir videonun kare kare eşi gerekiyorsa. |
| `rfq-to-quote` | ✅ | Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the plant can build, drafts the questions back, returns |
| `root-cause-capa` | ✅ | someone says \"why did this happ |
| `routines` | ✅ | a champion wants work like a weekly patterns digest, a stale guidance check, or a monthly lead update to happen without kicking it off by hand. |
| `skill-creator` | ✅ | Yeni skill yazmak ya da mevcut skill'i ölçülebilir biçimde iyileştirmek (tetikleme doğruluğu dahil). |
| `skill-creator@anthropics` | ✅ | users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, o |
| `skill-creator@freshtechbro` | ⚠️ | Güncel sürüme erişilemiyorsa yedek. |
| `skill-creator@heyitsnoah` | ✅ | claudesidian kasası içinde skill geliştirirken (kasa bu kopyayı bekler). |
| `skill-development` | ⚠️ | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill co |
| `skill-development@anthropics` | ⚠️ | Bir Claude Code eklentisinin içine skill eklemek (plugin-dev akışı içinde). |
| `skillify` | ✅ | 'Bunu skill yap' dendiğinde ya da aynı iş 3+ kez tekrarlandığında hızlı skill çıkarımı. |
| `style-sampling` | ✅ | Kanıtlanmış bir seri stilinde (açıklayıcı, finans, bilim, marka, true-crime) bölüm yapmak; 'şu stilde bir bölüm' istekleri. |
| `supplier-escape-to-alternate-source` | ✅ | someone says \"run the supplier escape chain,\" \"a supplier caused this, find us an alternate,\" \"supplier escape to alternate source,\" or asks to source aro |
| `supplier-quote-request` | ✅ | Builds the RFQ package that goes out to suppliers — drawing and specification at the verified current revision, the demand picture, the quality clause list, com |
| `trade-study-report` | ✅ | Turns a filled-in trade study matrix and its analysis results into a scored comparison and a decision memo, with every score cited to its source. |
| `writing-hookify-rules` | ✅ | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on ho |
| `writing-hookify-rules@anthropics` | ✅ | Kod yazmadan 'tehlikeli rm uyarısı', 'console.log engelle' gibi hızlı koruma kuralları eklemek (hookify kuruluysa). |
| `writing-skills` | ⚠️ | Agent davranışını değiştiren süreç/disiplin skillerini yazmak ve gerçekten işe yaradığını kanıtlamak. |
| `yao-meta-skill` | ✅ | migration/release/package, routing, evals/tests, install/trust checks, 优化已有 skill, 补 trigger 评测 |
