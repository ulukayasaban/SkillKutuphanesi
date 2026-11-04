# Örnek görevler ve test sonucu › d-ai-otomasyon

[← TEST_RAPORU.md](../../TEST_RAPORU.md) · 2026-11-04 · 83 skill. Örnek görev: elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki "Use when …".

| Skill | Sonuç | Örnek görev |
|---|---|---|
| `academy-guide` | ⚠️ | Claude öğrenmeye yönelik destek/eğitim asistanları; ekibe Claude yaygınlaştırma soruları. |
| `build-mcp-app` | ✅ | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP |
| `build-mcp-server` | ✅ | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Cl |
| `build-mcpb` | ✅ | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP",  |
| `claude-api` | ✅ | Claude çağıran her kod: yeni LLM özelliği, agent/araç tanımı, model geçişi, maliyet optimizasyonu, eval kurma, SDK sürüm yükseltme. |
| `claude-opus-4-5-migration` | ✅ | Yalnızca hedef özellikle Opus 4.5 ise (eski kod tabanlarını tam bu sürüme sabitlemek). |
| `connect` | ✅ | Kendi uygulamasında/agent'ında harici servislere eylem yaptırmak isteyen projeler (Composio kullanmayı kabul ederek). |
| `connect-apps` | ✅ | Claude Code kullanıcısının kendi oturumundan harici uygulamalara eylem yaptırması. |
| `langsmith-fetch` | ✅ | LangSmith izlemesi açık LangChain/LangGraph agent projelerinde hata ayıklama ve performans analizi. |
| `mcp-builder` | ✅ | Harici bir API/servisi agent'lara açan yeni MCP sunucusu yazmak ve değerlendirmek. |
| `mcp-builder@composiohq` | ✅ | Eski sürümdeki daha ayrıntılı 'ajan merkezli tasarım ilkeleri' bölümü özellikle istenirse. |
| `mcp-builder@vudovn` | ✅ | MCP sunucu/istemcisini güncel spesifikasyona taşımak, güvenlik/birlikte çalışabilirlik incelemesi, şema tasarımı. |
| `mcp-integration` | ✅ | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol",  |
| `mcp-integration@anthropics` | ✅ | Bir Claude Code eklentisine hazır MCP sunucusu eklemek/yapılandırmak. |
| `batch-operations` | ✅ | Kod tabanında desen tabanlı toplu değişiklik: fonksiyon yeniden adlandırma, API geçişi, sürüm numarası güncelleme. |
| `behavioral-modes` | ✅ | ag-kit ailesini kuran projelerde agent'ın tonunu/yaklaşımını göreve göre değiştirmek. |
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
| `memory-system` | ✅ | Harness'in yerleşik belleği olmayan ortamlarda (ya da projeye taşınabilir, git'te tutulan bellek istendiğinde) tercih ve kararları saklamak. |
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
| `session-report` | ✅ | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. |
| `subagent-driven-development` | ✅ | Bağımsız görevlere bölünmüş bir planı tek oturumda yüksek kaliteyle uygulamak. |
| `using-agent-skills` | ✅ | agent-skills ailesinden birden çok skill kurulu projelerde oturum başında doğru skill'i seçmek. |
| `using-n8n-mcp-skills` | ✅ | building, editing, validating, testing, or debugging an n8n workflow through the n8n-mcp MCP server — designing a flow, configuring a node, writing an expressio |
| `using-superpowers` | ✅ | superpowers ailesinin (brainstorming, writing-plans, systematic-debugging, subagent-driven-development…) birlikte kurulduğu projeler. |
| `agent-reach` | ✅ | Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. |
| `graphify` | ⚠️ | any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be tre |
| `notebooklm` | ✅ | Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. |
| `agent-development` | ✅ | . |
| `agent-development@anthropics` | ✅ | Claude Code projesine/eklentisine özel alt-agent tanımı yazmak ya da mevcut agent'ın tetiklenmesini düzeltmek. |
| `command-development` | ✅ | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command fr |
| `command-development@anthropics` | ✅ | Ekipte tekrar eden istemleri Claude Code slash komutuna çevirmek. |
| `cowork-plugin-customizer` | ✅ | : customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, m |
| `create-cowork-plugin` | ✅ | users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin |
| `hook-development` | ✅ | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks",  |
| `hook-development@anthropics` | ✅ | Tehlikeli komutu engelleme, düzenleme sonrası otomatik format/test, oturum başında bağlam yükleme gibi olay tabanlı Claude Code otomasyonu. |
| `library-curator` | ✅ | the user asks to reuse an image they captured/uploaded earlier, "pull a logo/screenshot from my library", or to find and drop a stored asset into the page being |
| `od-next-media-inputs` | ⚠️ | Prepare required media inputs within an existing OD Next plan. |
| `plugin-settings` | ✅ | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state |
| `plugin-settings@anthropics` | ✅ | Proje başına açılıp kapatılabilen ya da yapılandırılabilen bir Claude Code eklentisi yazarken. |
| `plugin-structure` | ✅ | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plu |
| `plugin-structure@anthropics` | ✅ | Yeni Claude Code eklentisi iskeleti kurmak, bileşenleri düzenlemek, marketplace'e hazırlamak. |
| `reverse-any-video` | ✅ | reverse, recreate, replicate or copy a video. |
| `skill-creator` | ✅ | Yeni skill yazmak ya da mevcut skill'i ölçülebilir biçimde iyileştirmek (tetikleme doğruluğu dahil). |
| `skill-creator@anthropics` | ✅ | users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, o |
| `skill-creator@composiohq` | ⚠️ | Ölçüm/eval istemeden, basit iskelet + paketleme akışı yeterliyse. |
| `skill-creator@freshtechbro` | ⚠️ | Güncel sürüme erişilemiyorsa yedek. |
| `skill-creator@heyitsnoah` | ✅ | claudesidian kasası içinde skill geliştirirken (kasa bu kopyayı bekler). |
| `skill-development` | ⚠️ | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill co |
| `skill-development@anthropics` | ⚠️ | Bir Claude Code eklentisinin içine skill eklemek (plugin-dev akışı içinde). |
| `skill-share` | ✅ | Ekipte skill paylaşımını Slack bildirimiyle otomatikleştirmek (Composio Rube bağlıysa). |
| `skillify` | ✅ | 'Bunu skill yap' dendiğinde ya da aynı iş 3+ kez tekrarlandığında hızlı skill çıkarımı. |
| `template-skill` | ✅ | Yok — yeni skill için skill-creator'ın init/şablonları daha iyi. |
| `writing-hookify-rules` | ✅ | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on ho |
| `writing-hookify-rules@anthropics` | ✅ | Kod yazmadan 'tehlikeli rm uyarısı', 'console.log engelle' gibi hızlı koruma kuralları eklemek (hookify kuruluysa). |
| `writing-skills` | ⚠️ | Agent davranışını değiştiren süreç/disiplin skillerini yazmak ve gerçekten işe yaradığını kanıtlamak. |
| `yao-meta-skill` | ✅ | migration/release/package, routing, evals/tests, install/trust checks, 优化已有 skill, 补 trigger 评测 |
