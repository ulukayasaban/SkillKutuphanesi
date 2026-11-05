# Örnek görevler ve test sonucu › b-yazilim-gelistirme

[← TEST_RAPORU.md](../../TEST_RAPORU.md) · 2026-11-05 · 404 skill. Örnek görev: elle incelenmiş skillerde Türkçe `kullanim_alani`, diğerlerinde description'daki "Use when …".

| Skill | Sonuç | Örnek görev |
|---|---|---|
| `app-builder` | ✅ | Sıfırdan full-stack uygulama başlatırken yığın seçimi ve iskelet kurulumu; hangi şablonun uygun olduğuna hızlı karar. |
| `architecture@anthropics` | ⚠️ | choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or desig |
| `ask-matt` | ✅ | Ask which skill or flow fits your situation. |
| `brainstorming` | ✅ | Yeni özellik, bileşen veya proje fikrinde gereksinim belirsizken; kodlamaya başlamadan önce ortak anlayış ve yazılı tasarım gerektiğinde. |
| `brainstorming-research-ideas` | ✅ | exploring new problem spaces, pivoting between projects, or seeking novel angles on existing work. |
| `brainstorming@openai` | ✅ | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. |
| `brainstorming@vudovn` | ✅ | ag-kit iş akışı kullanan projelerde; seçenek tablolu, karar odaklı soru listesi tercih edildiğinde. |
| `code-review` | ⚠️ | a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error h |
| `codebase-design` | ✅ | the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or wh |
| `constraint-driven-development` | ✅ | Yazılı kalite çıtası yoksa; agent testleri atlayıp/susturup yeşile ulaşmaya çalışıyorsa; erişilebilirlik, performans veya kapsama eşiği tanımlanacaksa. |
| `debug` | ⚠️ | an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause |
| `deploy-checklist` | ⚠️ | about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or document |
| `diagnosing-bugs` | ✅ | the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| `documentation` | ✅ | "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — AP |
| `domain-modeling` | ✅ | discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. |
| `doubt-driven-development` | ✅ | Yüksek riskli işler (üretim kimlik doğrulama, güvenlik, geri alınamaz migrasyon), tanıdık olmayan kod, planın gizli hata modlarının sınanması. |
| `egm-bootstrap` | ⚠️ | Bootstrap directory README.md files across a repository subtree. |
| `egm-brainstorm` | ⚠️ | Interactive ideation and brainstorming skill for the Elephant & Goldfish Model (EGM). |
| `egm-draft` | ⚠️ | you are ready to write a design doc after aligning on requirements + solution. |
| `egm-drift-report` | ⚠️ | the user asks to detect drift or check for consistency across all design documents or READMEs in a directory. |
| `egm-resolve` | ⚠️ | The Elephant resolution skill. |
| `egm-review` | ⚠️ | Orchestrates the EGM Goldfish Review Protocol. |
| `egm-review-loop` | ⚠️ | reviewing design docs, READMEs, feature specifications, implementation plans, or verifying document completeness and tone. |
| `executing-plans` | ✅ | writing-plans planı hazır ve kullanıcı satır içi yürütmeyi seçtiyse; alt-agent aracı olmayan ortamlarda (ör. bazı Codex kurulumları). |
| `executing-plans@openai` | ✅ | you have a written implementation plan to execute in a separate session with review checkpoints |
| `git-guardrails-claude-code` | ✅ | user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code. |
| `grill-me` | ✅ | A relentless interview to sharpen a plan or design. |
| `grill-with-docs` | ✅ | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `grilling` | ✅ | the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| `handoff` | ✅ | Compact the current conversation into a handoff document for another agent to pick up. |
| `idea-refine` | ✅ | Ürün/özellik fikri henüz bulanıkken, seçenekleri açıp sonra birine indirmek ya da bir planın varsayımlarını sınamak istendiğinde. |
| `implement` | ✅ | Implement a piece of work based on a spec or set of tickets. |
| `implement-spec` | ✅ | Implement the result of /to-spec and /to-tickets in code. |
| `improve-codebase-architecture` | ✅ | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `incident-response` | ⚠️ | "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after |
| `incremental-implementation` | ✅ | Birden çok dosyaya dokunan her özellik/değişiklikte; plandan sıradaki görevi alırken; büyük kod bloğu yazma eğilimi olduğunda. |
| `interview-me` | ✅ | İstek 'kimin için / neden şimdi' bilgisi olmadan geldiğinde; kullanıcı 'beni sorgula', 'emin miyiz?' dediğinde; plan veya spec yazılmadan önce kısa niyet doğrul |
| `karpathy-guidelines` | ✅ | writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. |
| `math-olympiad` | ✅ | Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. |
| `migrate-to-shoehorn` | ✅ | user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. |
| `plan-writing` | ✅ | ag-kit kullanan projelerde veya çok kısa, tek sayfalık plan yeterliyse. |
| `planning-and-task-breakdown` | ✅ | Spec hazır, iş büyük ve dilimlenmesi gerekiyorsa; tahmin/kapsam çıkarma veya paralel iş fırsatı aranırken; superpowers zinciri kullanılmayan projelerde. |
| `pr@mattpocock` | ✅ | opening a PR or asked to write a PR description. |
| `prototype@mattpocock` | ✅ | the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| `replica-architect` | ✅ | the user says "plan the clone", "what stack should I use", "design the database", "write the schema", "plan the API", "architecture for my version of X", or aft |
| `replica-backend` | ✅ | the user says "add login", "set up auth", "wire up the database", "add payments", "connect Stripe", "add Google Calendar", "send emails", "backend for my clone" |
| `replica-brand` | ✅ | the user says "name my app", "rebrand the clone", "make it mine", "pick a name and colours", "logo brief", "brand voice", "check for leftovers", or after /repli |
| `replica-build` | ✅ | the user says "build the clone", "build screen S07", "start building", "rebuild this screen", "implement the booking page", or after /replica-design. |
| `replica-deploy` | ✅ | the user says "deploy it", "ship it", "put it live", "connect my domain", "go to production", "publish the app", or after /replica-launch. |
| `replica-design` | ✅ | the user says "match the design", "rebuild the design system", "get the colours and fonts", "make it look like X", "design tokens for my clone", or after /repli |
| `replica-diff` | ✅ | the user says "how close is my clone", "compare it to the original", "what's missing", "parity check", "diff the screens", "is it ready", or after /replica-test |
| `replica-entrepreneur` | ✅ | the user says "what do people hate about X", "read the reviews", "how do I make mine better", "find the gap", "what features are missing", "how do I position th |
| `replica-launch` | ✅ | the user says "landing page", "pricing", "how much should I charge", "App Store listing", "store screenshots", "launch plan", "Product Hunt", or after /replica- |
| `replica-recon` | ✅ | the user says "clone this app", "reverse engineer X", "how does X work", "map out X", "what screens does X have", "I want to build my own version of X", "copy t |
| `replica-test` | ✅ | the user says "test my clone", "find bugs", "QA this", "click through everything", "write e2e tests", "does it work", or after /replica-build or /replica-backen |
| `research` | ✅ | the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. |
| `retro` | ✅ | Conduct a retrospective on a coding session. |
| `scaffold-exercises` | ✅ | user wants to scaffold exercises, create exercise stubs, or set up a new course section. |
| `setup-matt-pocock-skills` | ✅ | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. |
| `setup-pre-commit` | ✅ | user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing. |
| `siege` | ✅ | Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, independent workers answer them, and the judge keeps a |
| `solo` | ✅ | Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in a notes file so that nothing wr |
| `source-driven-development` | ✅ | Framework/kütüphane sürümüne duyarlı işler; güncelliğini yitirmiş kalıp riski olan hızlı değişen API'ler (Next.js, React 19, Tailwind v4…). |
| `spec-driven-development` | ✅ | Yeni proje/özellik başlarken spec veya PRD yoksa; tek bir isteğin birden çok bağımsız yeteneğe bölünmesi gerektiğinde. |
| `standup` | ⚠️ | preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, formatting work into yesterday/today/blockers, or structuring a few rough |
| `system-design` | ✅ | "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data mo |
| `tdd` | ✅ | the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| `teach` | ✅ | Teach the user a new skill or concept, within this workspace. |
| `tech-debt` | ✅ | "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance  |
| `templates` | ✅ | Sadece şablon dosyaları istenip app-builder'ın orkestrasyon kısmı istenmediğinde. |
| `testing-strategy` | ✅ | "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverag |
| `to-questionnaire` | ✅ | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| `to-spec` | ✅ | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `to-tickets` | ✅ | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edg |
| `triage` | ✅ | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| `wait-what` | ✅ | Stop. |
| `wayfinder` | ⚠️ | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until |
| `wizard` | ✅ | provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover |
| `writing-for-agents` | ✅ | creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| `writing-plans` | ✅ | Çok adımlı bir iş için spec/gereksinim hazırsa, koda dokunmadan önce; alt-agent'lara dağıtılacak görevler gerektiğinde. |
| `writing-plans@openai` | ✅ | you have a spec or requirements for a multi-step task, before touching code |
| `clean-code` | ✅ | Kod yazan agent'lar için kısa, her zaman açık stil ve disiplin kuralı olarak. |
| `code-review-and-quality` | ✅ | Birleştirmeden önce her değişiklikte; kendi, başka agent'ın veya insanın yazdığı diff/PR'ı incelerken (diff satır içi yapıştırılmış olsa da). |
| `code-review-checklist` | ✅ | Hızlı, hafif bir kontrol listesi yeterli olduğunda; ag-kit iş akışı kullanan projelerde. |
| `code-review-graph` | ✅ | 500+ dosyalı depolar, monorepo'lar, modüller arası bağımlılıklı değişiklikler; ölü kod tespiti ve refactor önizlemesi. |
| `code-review@mattpocock` | ✅ | the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\". |
| `code-review@openai` | ✅ | user asks for code review, PR feedback, code quality checks, security issues, or requests fix-review cycles. |
| `code-simplification` | ✅ | Çalışan ama okunması/bakımı zor koda refactor; incelemede biriken karmaşıklık fark edildiğinde; yeni yazılan kodu teslim öncesi toparlamak. |
| `lint-and-validate` | ✅ | TypeScript/JavaScript veya Python projelerinde her değişiklik sonrası otomatik kalite kapısı. |
| `ponytail` | ✅ | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. |
| `ponytail-audit` | ✅ | "audit this codebase", "review the whole repo", "find bloat", "what can I delete", /ponytail-audit. |
| `ponytail-debt` | ✅ | "ponytail debt", "what did ponytail defer", "list the shortcuts", /ponytail-debt. |
| `ponytail-gain` | ✅ | /ponytail-gain, "what does ponytail save", "ponytail impact". |
| `ponytail-help` | ✅ | /ponytail-help, "ponytail help", "how do I use ponytail". |
| `ponytail-review` | ✅ | "review this", "code review", "review the last commit", "review my PR", "is this over-engineered", /ponytail-review. |
| `postgresql-code-review` | ✅ | PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. |
| `pragmatic-review` | ✅ | Aşırı mühendislik, gereksiz soyutlama şüphesi olan değişikliklerde; CI'da otomatik inceleme yorumu üretmek. |
| `receiving-code-review` | ✅ | İnsan veya inceleyici agent'tan geri bildirim geldiğinde, özellikle belirsiz ya da teknik olarak şüpheli öneriler varken. |
| `receiving-code-review@openai` | ✅ | receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and |
| `requesting-code-review` | ✅ | subagent-driven-development'ta her görevden sonra; büyük özellik bitiminde; main'e birleştirmeden önce taze bağlamlı inceleme gerektiğinde. |
| `requesting-code-review@openai` | ✅ | completing tasks, implementing major features, or before merging to verify work meets requirements |
| `simplify-code` | ✅ | Hızlı, kontrol listesi tarzı sadeleştirme; ag-kit iş akışı kullanan projeler. |
| `simplify-codebase` | ✅ | Var olan bir depoda sadeleştirme denetimi veya açıkça yetkilendirilmiş büyük çaplı temizlik; 'nereler gereksiz?' sorusuna kanıtlı yanıt. |
| `sql-code-review` | ✅ | Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL databases (MySQL, PostgreSQL |
| `debugging-and-error-recovery` | ✅ | superpowers zinciri kullanılmayan projelerde hata ayıklama; build/runtime hata tipine göre hazır triyaj listesi istendiğinde. |
| `systematic-debugging` | ✅ | Her hata, test başarısızlığı, build kırılması veya beklenmeyen davranışta düzeltme önermeden önce; özellikle zaman baskısı ve ardışık başarısız düzeltmelerde. |
| `systematic-debugging@heyitsnoah` | ✅ | Tek dosyalık (ek dosyasız) sürüm tercih edildiğinde; claudesidian kasası kullanan projeler. |
| `systematic-debugging@openai` | ✅ | encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `systematic-debugging@vudovn` | ✅ | ag-kit /debug iş akışında veya yalnız kısa bir hatırlatıcı yeterliyse. |
| `tdd-workflow` | ✅ | ag-kit iş akışı kullanan projelerde veya çok kısa bir TDD hatırlatıcısı yeterliyse. |
| `test-driven-development` | ✅ | Mantık yazarken, hata düzeltirken veya davranış değiştirirken; kullanıcı test istemese de kod satır içi verilmiş olsa bile. |
| `test-driven-development@obra` | ✅ | superpowers zinciri (writing-plans → subagent-driven-development / executing-plans) uçtan uca kullanılırken; agent'ın TDD'yi atlama eğilimine karşı en katı disi |
| `test-driven-development@openai` | ✅ | implementing any feature or bugfix, before writing implementation code |
| `test-value` | ✅ | Test paketi yavaş/kararsız olduğunda denetim; commit/PR öncesi test değişikliklerini incelemek; başarısız bir kontrolün gerçek regresyon mu eskimiş assertion mı |
| `testing-patterns` | ✅ | Test çerçevesi ve mock stratejisi seçerken hızlı başvuru; ag-kit kullanan projeler. |
| `verification-before-completion` | ✅ | İş bitti/düzeldi/geçti demeden önce; commit, PR veya alt-agent sonucunu kabul etmeden önce her zaman. |
| `verification-before-completion@openai` | ✅ | about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before maki |
| `verify-changes` | ✅ | Özellik/hata düzeltmesi bittikten sonra somut doğrulama planı ve rapor biçimi gerektiğinde; 'çalışıyor mu?' sorusunda. |
| `api-and-interface-design` | ✅ | REST/GraphQL endpoint'i, modül sınırı veya ön yüz-arka yüz sözleşmesi tasarlarken; herkese açık bir arayüzü değiştirirken. |
| `api-breaking-change-detector` | ✅ | the user asks to check for breaking API changes, verify frontend/backend contract sync, or audit |
| `api-patterns` | ✅ | API stili ve kimlik doğrulama yöntemi seçerken; rate limiting veya sürümleme stratejisi belirlerken. |
| `architecture-blueprint-generator` | ✅ | Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. |
| `architecture@vudovn` | ✅ | Sistem tasarımı, desen seçimi (monolit/mikroservis, katmanlar), önemli kararların ADR olarak kaydı. |
| `database-design` | ✅ | Şema tasarlarken, ORM/veritabanı seçerken, migrasyon planlarken veya yavaş sorgu optimize ederken (Prisma, Drizzle, SQL). |
| `frontend-architecture` | ✅ | React/Next veya Vue kod tabanını yapılandırırken ya da organizasyonunu incelerken: mantık, API çağrısı, durum ve tiplerin nerede yaşayacağı. |
| `frontend-ui-engineering` | ✅ | Arayüz, sayfa veya bileşen yazarken/değiştirirken; erişilebilirlik gereksinimi olduğunda; çıktının 'AI yapımı' değil üretim kalitesinde görünmesi gerektiğinde. |
| `nodejs-best-practices` | ✅ | Node.js backend kurarken veya framework seçerken; mevcut Node servisinin yapısını gözden geçirirken. |
| `python-patterns` | ✅ | Python backend/servis kurarken veya framework seçerken; tip ipucu ve proje yapısı kararlarında. |
| `changelog-generator` | ✅ | Sürüm notları, haftalık/aylık ürün güncellemesi, app store değişiklik metni veya herkese açık changelog sayfası hazırlarken. |
| `deprecation-and-migration` | ✅ | Bir API/özelliği emekliye ayırırken; kullanıcıları yeni sisteme taşırken; üretimde kolon yeniden adlandırma/silme gibi kesintisiz şema değişikliğinde; bakım mı  |
| `finishing-a-development-branch` | ✅ | Tüm testler geçtikten sonra dalı birleştirme/PR/bekletme kararı ve worktree temizliği. |
| `finishing-a-development-branch@openai` | ✅ | implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `git-workflow-and-versioning` | ✅ | Her kod değişikliğinde commit/dal/PR düzeni; karışık çalışma ağacını temiz atomik commit'lere bölmek; sürüm numarası seçmek ve release kesmek. |
| `git-worktrees` | ✅ | Elle worktree yönetimi, PR incelemesi için ayrı checkout veya birleşme sonrası temizlik komutları gerektiğinde. |
| `pr-feedback-quality-gate` | ✅ | Safely track pull request feedback, resolve review comments or merge conflicts, validate fixes, and use a read-only cross-review before committing or pushing fo |
| `pull-request` | ✅ | Kullanıcı açıkça 'PR aç' dediğinde hızlı dal + commit + push + PR. |
| `release-notes-one-pager` | ✅ | Release notes one-page HTML with highlights, Added, Fixed, Breaking changes, Known issues, and Upgrade note. |
| `release@heyitsnoah` | ✅ | package.json ve CHANGELOG.md (Keep a Changelog) kullanan Node projelerinde sürüm kesmek. |
| `using-git-worktrees` | ✅ | Yalıtım gerektiren özellik işine başlarken veya bir uygulama planını yürütmeden önce (superpowers zinciri). |
| `using-git-worktrees@openai` | ✅ | starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native too |
| `agents-sdk` | ✅ | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| `api-monitoring` | ✅ | setting up uptime/error alerts for store APIs, webhooks failing silently, or planning integration SLAs. |
| `basin` | ✅ | streaming data into R2 Iceberg tables, managing catalogs, or querying those tables; also use for requests using the former Data Platform, Pipelines, R2 Data Cat |
| `cf-cli` | ✅ | finding and running Cloudflare commands from the terminal — sign-in and profiles, cf cli search, cf schema, cf deploy/dev/build, resource commands for DNS, zone |
| `ci-cd-and-automation` | ✅ | Build/deploy hattı kurarken veya değiştirirken; kalite kapılarını otomatikleştirirken; test çalıştırıcısını CI'a bağlarken. |
| `claude-security` | ✅ | the user asks to scan, audit or check code with Claude Security, to scan their changes with Claude Security, or to fix or patch Claude Security findings. |
| `cloudflare` | ⚠️ | architecture and product selection, including when the user describes a need without naming a Cloudflare product; then find the relevant skill or documentation. |
| `cloudflare-email-service` | ✅ | Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration. |
| `cloudflare-one` | ✅ | Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. |
| `cloudflare-one-migrations` | ✅ | Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout. |
| `deploy-to-vercel` | ✅ | the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment". |
| `deployment-procedures` | ✅ | Barındırma platformu seçerken veya deploy prosedürü yazarken; ag-kit /deploy iş akışında. |
| `deployments-cicd` | ✅ | deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel. |
| `domain-monitoring` | ✅ | a store needs certificate or domain-renewal alerts, DNS change monitoring, or a website security health check plan. |
| `durable-objects` | ✅ | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| `file-integrity-monitoring` | ✅ | protecting a store (WooCommerce, Magento, custom) from malicious code injection, card skimmers or unauthorized theme/plugin edits. |
| `gateway-workers` | ✅ | Build, debug, or review Cloudflare Workers invoked by the Forward action in Gateway HTTP policies, including the GatewayMiddleware entrypoint, Gateway types, co |
| `k2` | ✅ | stream setup, producing from Workers or HTTP, configuring retention and inputs, and consuming through subscriptions. |
| `localization-testing` | ✅ | launching a store in a new country or language, or auditing translations, currencies and local legal requirements. |
| `nextjs-on-cloudflare` | ✅ | starting a Next.js project on Cloudflare, moving an existing app to Workers, choosing between vinext and OpenNext, or setting up vinext for Workers |
| `observability` | ✅ | instrumenting, debugging, or optimizing application performance and user experience on Vercel. |
| `observability-and-instrumentation` | ✅ | Loglama/metrik/izleme/uyarı eklerken; üretime çıkan her özellikte çalıştığına dair kanıt gerektiğinde; üretim sorunu mevcut veriden anlaşılamıyorsa. |
| `performance-optimization` | ✅ | Performans gereksinimi veya regresyon şüphesi olduğunda; Core Web Vitals/yükleme süresi iyileştirmede; N+1 sorgu düzeltmede; profil çıkarılmış darboğazlarda. |
| `performance-profiling` | ✅ | Lighthouse denetimi çalıştırmak, bundle boyutunu analiz etmek veya DevTools ile çalışma zamanı profili çıkarmak gerektiğinde. |
| `performance-review-writer` | ✅ | : write my performance review, draft self-assessment, peer review, 360 feedback, annual review, mid-year review, upward feedback, write review for colleague, pe |
| `public-status-page` | ✅ | creating or improving a status page, or writing customer-facing incident and outage updates. |
| `red-team-tactics` | ✅ | Yalnız yetkili sızma testi veya kırmızı takım tatbikatında saldırı yüzeyini çerçevelemek ve rapor yapısı kurmak. |
| `reverse-engineer-anything` | ✅ | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA, and build agent environments (AgentEnv bundles) of web  |
| `sandbox-migrate-to-next` | ✅ | Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). |
| `sandbox-next` | ✅ | Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). |
| `sandbox-stable` | ✅ | Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. |
| `security` | ✅ | hardening a Google Play Billing integration against fraud |
| `security-and-hardening` | ✅ | Kullanıcı girdisi, kimlik doğrulama, veri saklama veya dış entegrasyon içeren her özellikte; OWASP Top 10'a karşı giriş akışı denetimi; bağımlılık denetimi. |
| `security-audit` | ✅ | security questions, focused reviews, vulnerability research, security audits, or pen tests |
| `security-diff-scan` | ✅ | Review a pull request, commit, branch diff, or working-tree patch for security vulnerabilities. |
| `security-review` | ✅ | asked to scan code for security vulnerabilities, find bugs, check for SQL injection, XSS, command injection, exposed API keys, hardcoded secrets, insecure depen |
| `security-scan` | ✅ | a standard, single-pass security audit of an entire repository or a scoped path, package, folder, or submodule with no diff to review |
| `server-management` | ✅ | VPS/kendi sunucusunda çalışan uygulamalarda PM2/systemd yapılandırması, izleme ve ölçekleme kararları. |
| `shipping-and-launch` | ✅ | Üretime deploy öncesi 'neler hazır olmalı?' sorusunda; kademeli yayın ve geri alma stratejisi planlarken. |
| `synthetic-monitoring` | ✅ | you need to catch broken checkout or cart flows before customers do. |
| `turnstile-spin` | ✅ | Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify. |
| `vercel-cli-with-tokens` | ✅ | working with Vercel CLI using access tokens rather than interactive login — e.g |
| `vercel-optimize` | ✅ | Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps |
| `vulnerability-scanner` | ✅ | Projede güvenlik taraması, OWASP 2025 uyum kontrolü veya tedarik zinciri (bağımlılık) analizi yaparken. |
| `vulnerability-writeup` | ✅ | one vulnerability or a disclosure campaign; a Codex Security scan is optional. |
| `web-perf` | ✅ | Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores. |
| `workers-best-practices` | ✅ | writing, reviewing, or configuring Workers. |
| `workers-profiling` | ✅ | Profile or debug CPU usage and memory allocation in deployed Cloudflare Workers and Durable Objects. |
| `wrangler` | ✅ | Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, d |
| `bash-linux` | ✅ | macOS/Linux'ta terminal komutları ve bash betikleri yazarken hızlı başvuru. |
| `cardputer-buddy` | ✅ | the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command |
| `m5-onboard` | ⚠️ | the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go". |
| `next-bundle-optimizer` | ✅ | Yavaş route açılışı, şişkin istemci bundle'ı, yinelenen tarayıcı bağımlılıkları, etkileşime ertelenebilecek özellikler veya istemci paketine istemeden giren sun |
| `next-cache-components` | ✅ | implementing partial prerendering, caching strategies, or migrating from older Next.js cache patterns. |
| `next-cache-components-adoption` | ✅ | cacheComponents bayrağını açmak, blocking-prerender/instant doğrulama hatası selini çözmek, 'export const instant = false' ile yerinde düzeltme arasında karar v |
| `next-cache-components-optimizer` | ✅ | Yavaş ilk boyama, anında olmayan gezinme, hangi Suspense sınırının UI'yi engellediğini bulma veya instant() regresyon kapsamı ekleme. |
| `next-dev-loop` | ✅ | next dev çalışırken uygulama kodu düzenlendikten sonra değişikliğin derlenmenin ötesinde çalıştığını doğrulamak. |
| `next-forge` | ✅ | working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages. |
| `next-intl-add-language` | ✅ | Add new language to a Next.js + next-intl application |
| `next-partial-prefetching-adoption` | ✅ | partialPrefetching bayrağını açmak, route'ları 'export const prefetch = partial' ile dahil etmek, prefetch davranışını korurken geçiş yapmak. |
| `next-partial-prefetching-optimizer` | ✅ | URL'ye özgü UI'nin anında gelmesini istemek, yeniden kullanılabilir içeriği gezinmeye bırakmak veya prefetch tetikleyicisi seçmek. |
| `next-upgrade` | ✅ | upgrading Next.js versions, running codemods, or migrating between major releases. |
| `nextjs-react-expert` | ✅ | ag-kit kullanan projelerde veya Cache Components notlarını aynı skillde isteyenlerde React/Next performans incelemesi. |
| `playwright-cli` | ⚠️ | Agent'ın gerçek tarayıcıda sayfayla etkileşmesi, akış doğrulaması, ekran görüntüsü/trace/video alması veya Playwright testleri üretip çalıştırması gerektiğinde. |
| `powershell-windows` | ✅ | Proje Windows'ta çalışıyorsa veya PowerShell betiği yazılıyorsa; agent'ın tipik PowerShell sözdizimi hatalarını önlemek için. |
| `rust-pro` | ✅ | Rust servisi, kütüphanesi veya sistem aracı yazarken; sahiplik/ömür ve async tasarım sorunlarında. |
| `vercel-composition-patterns` | ✅ | refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs |
| `vercel-composition-patterns@calesthio` | ✅ | Çok boolean prop'lu bileşenleri refactor ederken, yeniden kullanılabilir bileşen kütüphanesi veya esnek bileşen API'si tasarlarken. |
| `vercel-react-best-practices` | ✅ | tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements. |
| `vercel-react-best-practices@calesthio` | ✅ | React bileşeni veya Next.js sayfası yazarken/incelerken; veri çekme, bundle ve render performansı sorunlarında. |
| `vercel-react-native-skills` | ✅ | building React Native components, optimizing list performance, implementing animations, or working with native modules |
| `vercel-react-view-transitions` | ✅ | the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, impleme |
| `accessibility` | ✅ | working on accessibility, a11y, WCAG, ARIA, screen readers, keyboard nav, focus order, contrast, alt text, captions, reduced motion, or target sizes; not langua |
| `ad-attribution` | ✅ | running paid acquisition beyond Apple Ads, measuring re-engagement campaigns, designing conversion values, or migrating from SKAdNetwork. |
| `adaptive` | ✅ | Instructions to make or update an app's UI so that it adapts to different Android devices including phones, tablets, foldables, laptops, desktop, TV, Auto, and  |
| `agents-md-generator` | ✅ | missing, bloated, contradictory, or outdated agent instructions, monorepos, services, packages, module context, and portable agent guidance without assuming any |
| `agp-9-upgrade` | ✅ | migrating Kotlin Multiplatform (KMP) projects. |
| `alternative-billing` | ✅ | implementing Google Play's alternative billing programs, external offers and billing choice (PBL 5.2 through 9.1) |
| `android-cli` | ⚠️ | Provides instructions for installing and using the `android` CLI. |
| `android-design-guidelines` | ✅ | building Android apps with Jetpack Compose or XML layouts, implementing Material You, navigation, or accessibility |
| `android-development` | ✅ | building Android apps with Kotlin, Jetpack Compose, MVVM architecture, Hilt dependency injection, Room database, or multi-module projects |
| `android-for-cars-parked-apps` | ✅ | migrating, building, or auditing parked apps for car |
| `android-intent-security` | ✅ | auditing component configurations in AndroidManifest.xml activities, services, receivers) or source code handling incoming Intents (getIntent, getParcelableExtr |
| `android-permissions-security` | ✅ | reviewing AndroidManifest.xml, defining custom permissions, securing Services, Receivers, and Providers, verifying caller signatures and UID using Binder, or im |
| `android-profiler` | ✅ | : recording system traces, CPU call stacks, Vulkan GPU/DRM memory, or Java/native heap profiles; analyzing Perfetto traces for UI jank, frame drops, ANRs, or ap |
| `anr-audit-and-fix` | ✅ | scanning Android code for ANR risks or triaging ANR stack dumps |
| `app-description-writer` | ✅ | writing initial descriptions, improving existing copy, or drafting promotional text and What's New for a major update. |
| `app-store` | ✅ | user needs help with App Store presence, ASO, marketing, or customer communication. |
| `appfunctions` | ✅ | discovering, implementing, documenting, testing, or upgrading AppFunctions in an Android app, including @AppFunctionDeclaration, @AppFunctionSerializable, @AppF |
| `apple-search-ads` | ✅ | user asks about running ads, paid user acquisition, or Apple Search Ads campaigns. |
| `architecture-feature-first` | ✅ | creating a feature, designing folder structure, adding repositories/services/view models, wiring dependency injection, or deciding which layer owns logic. |
| `backend-architecture` | ✅ | building a backend for Google Play Billing receipt verification |
| `billing-response-codes` | ✅ | Use this skill as a reference lookup for every Play Billing Library BillingResponseCode and sub response code, with description, category, and handling guidance |
| `bloc` | ✅ | creating a Cubit or Bloc, modeling state with sealed classes or status enums, wiring BlocBuilder/BlocListener/BlocProvider, writing bloc tests, or choosing betw |
| `camerax` | ✅ | implementing camera features, handling asynchronous recording lifecycles, wiring low-level hardware interop using CameraX, or integrating ML Kit or Media3 effec |
| `cancellations-pauses-winback` | ✅ | implementing cancellations, developer initiated revocations, subscription pauses, and winback offers on Google Play |
| `catalog-management` | ✅ | managing Google Play product and subscription catalogs programmatically with the Google Play Developer API |
| `code-review@evanca` | ✅ | asked to review a PR, MR, branch, or diff, audit changed files, or check code quality. |
| `codex-phone-lab` | ✅ | Codex is asked to create a phone app, prototype an iPhone or Android app, run an app on a physical phone, show a QR code for Expo Go, set up a mobile dev workfl |
| `compose-agent` | ✅ | reading, writing, or reviewing Compose projects. |
| `dart-3-updates` | ✅ | writing switch statements, refactoring if-else chains, creating data classes, choosing records vs classes, destructuring values, or modernizing pre-Dart-3 code. |
| `dart-drift` | ✅ | adding SQLite with package:drift/native.dart, configuring PostgreSQL with drift_postgres and package:postgres, writing type-safe tables, queries, writes, stream |
| `developing-genkit-dart` | ✅ | building AI agents in Dart, implementing Genkit flows or tools, integrating LLMs into Dart or Flutter applications, or using Genkit Dart plugins. |
| `display-glasses-with-jetpack-compose-glimmer` | ✅ | build an Android XR Augmented Experience app with Jetpack Compose Glimmer |
| `eas-app-stores` | ✅ | eas.json setup, release pipelines, signing, app versions and build numbers, store submissions, and listing metadata |
| `eas-hosting` | ✅ | deploying an Expo web app or API routes, setting up EAS Hosting, or configuring hosting environments and domains |
| `eas-observe` | ✅ | anything related to EAS Observe - adding `expo-observe` to an Expo project (AppMetricsRoot/ObserveRoot HOC, markInteractive and ObserveInteractiveMarker, the us |
| `eas-simulator` | ✅ | the user needs a simulator they can't run locally - 'run my app on a cloud simulator', 'use eas simulator to run/install/screenshot my app', 'I'm on Linux/Curso |
| `eas-update` | ✅ | setting up OTA updates, running eas update:configure or eas update, publishing to preview/staging/production channels, explaining branches/channels/runtime vers |
| `eas-update-insights` | ✅ | the user asks how an update is performing, whether a rollout is healthy, how many users are on the embedded build vs OTA, or wants to gate CI on update health. |
| `eas-workflows` | ✅ | the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipelines or deployment automation. |
| `edge-to-edge` | ✅ | migrate your Jetpack Compose app to add adaptive edge-to-edge support and troubleshoot common issues |
| `effective-dart` | ✅ | writing Dart code, reviewing for style, refactoring naming, adding doc comments, structuring imports, or enforcing type annotations. |
| `engage-sdk-integration` | ✅ | adding Engage SDK support, generating publishing code, mapping data classes to entities, or fixing SDK-related errors. |
| `error-handling` | ✅ | designing error handling and retry strategy for the Play Billing Library |
| `expo-animation` | ✅ | animating anything in an Expo app, adding gestures, sheets, screen transitions, press feedback or haptics, or fixing motion that stutters on device |
| `expo-app-clip` | ✅ | the user mentions App Clip, AASA, apple-app-site-association, appclips, smart app banner, or wants to ship a lightweight iOS Clip invoked from a URL alongside t |
| `expo-brownfield` | ✅ | brownfield, embedding a React Native screen in SwiftUI/UIKit or Kotlin, or AAR/XCFramework packaging |
| `expo-data-fetching` | ✅ | implementing or debugging ANY network request, API call, or data fetching |
| `expo-design-system` | ✅ | creating or organizing theme files and design tokens (theme.ts / theme/), extending an existing theme or styling library (NativeWind, Tamagui, Restyle, Unistyle |
| `expo-dev-client` | ✅ | Build and distribute Expo development clients locally or via TestFlight for internal testing. |
| `expo-dom` | ✅ | Use Expo DOM components to run web code in a webview on native and as-is on web. |
| `expo-examples` | ✅ | integrating a third-party library or service into an existing Expo app and you want the canonical, version-matched pattern to adapt, or when scaffolding a new p |
| `expo-migrate-module` | ✅ | converting or incrementally adopting @ExpoModule, @JS, @Event, @SharedObject, or @Record in an existing module |
| `expo-module` | ✅ | building or modifying native modules for Expo |
| `expo-native-ui` | ✅ | Build beautiful, native-feeling Expo screens. |
| `expo-overview` | ⚠️ | Entry point and router for every Expo or EAS task. |
| `expo-project-structure` | ✅ | scaffolding or laying out a new Expo project with Expo Router, or deciding where a file should live in one |
| `expo-router` | ✅ | Navigation and routing for Expo Router. |
| `expo-ui` | ✅ | Build native UI with the @expo/ui package: real SwiftUI on iOS and Jetpack Compose on Android. |
| `expo-upgrade` | ✅ | Guidelines for upgrading Expo SDK versions and fixing dependency issues |
| `expo-web-to-native` | ✅ | the user wants to turn a website into a mobile app, port a Next.js/Vite/CRA React codebase to React Native, reuse web code on native incrementally, or asks how  |
| `firebase-ai` | ✅ | setting up firebase_ai, generating text/chat with Gemini, streaming AI output, building multimodal prompts, or handling AI errors. |
| `firebase-analytics` | ✅ | logging analytics events, setting user properties, configuring default event parameters, building funnels, or adding screen-view tracking. |
| `firebase-app-check` | ✅ | implementing app attestation, configuring App Check providers, setting up debug tokens, enabling backend enforcement, or managing token refresh. |
| `firebase-auth` | ✅ | setting up auth, managing auth state, implementing email/password or social sign-in, handling auth errors, or managing users. |
| `firebase-cloud-firestore` | ✅ | setting up Firestore, designing schemas, doing CRUD, creating listeners, paginating queries, configuring indexes, enabling offline persistence, or writing secur |
| `firebase-cloud-functions` | ✅ | calling callable functions (httpsCallable), passing data to server-side logic, handling function errors/timeouts, configuring regions, or testing with the Emula |
| `firebase-crashlytics` | ✅ | implementing crash reporting, capturing fatal/non-fatal errors, recording isolate/async exceptions, customizing reports, or uploading obfuscated symbols. |
| `firebase-data-connect` | ✅ | setting up Data Connect, writing GraphQL queries/mutations, configuring generated SDKs, handling offline, or applying security rules. |
| `firebase-database` | ✅ | syncing real-time data, structuring JSON trees, reading/writing, creating listeners, enabling offline persistence, managing presence, sharding, or writing secur |
| `firebase-in-app-messaging` | ✅ | running in-app message campaigns, triggering/suppressing messages, configuring opt-in data collection, testing on specific devices, or handling message callback |
| `firebase-messaging` | ✅ | setting up Firebase Cloud Messaging, managing permissions and tokens, handling background/foreground notification taps, or dispatching messages server-side (HTT |
| `firebase-remote-config` | ✅ | implementing feature flags, running A/B tests, setting parameter defaults, fetching/activating config, or enabling real-time config updates. |
| `firebase-storage` | ✅ | setting up Storage, uploading/downloading files, managing metadata, handling errors, or applying security rules. |
| `flutter-adaptive-ui` | ✅ | creating breakpoint-driven layouts, responsive navigation, adaptive dialogs/lists/grids, keyboard/mouse/touch behavior, window-size decisions with MediaQuery or |
| `flutter-animations` | ⚠️ | working with implicit animations such as AnimatedContainer, AnimatedOpacity, AnimatedSwitcher, and TweenAnimationBuilder; explicit animations using AnimationCon |
| `flutter-app-architecture` | ✅ | scaffolding a project, refactoring into layers, creating view models/repositories, configuring dependency injection, or implementing unidirectional data flow (M |
| `flutter-architecture` | ✅ | asked to add a Flutter feature, audit layer dependencies, fix cross-feature imports, migrate to feature-first, choose architecture for a Flutter project, or cre |
| `flutter-best-practices` | ✅ | writing, reviewing, refactoring, or planning Flutter/Dart code — screens, features, project structure, state management, folders, widgets, cubits/blocs, reposit |
| `flutter-change-notifier` | ✅ | setting up ChangeNotifier models, providing them to the widget tree, consuming state with Consumer or Provider.of, or optimizing rebuilds. |
| `flutter-drift` | ✅ | a Flutter task mentions drift, local database storage, SQLite, reactive database streams, CRUD, schemaVersion, build_runner, drift_dev make-migrations, migratio |
| `flutter-duit-bdui` | ✅ | a task mentions DUIT, flutter_duit, backend-driven UI, BDUI, server-driven UI, XDriver, DuitViewHost, DuitRegistry, HTTP or WebSocket transports, custom Duit wi |
| `flutter-errors` | ✅ | hitting layout errors (RenderFlex overflow, unbounded constraints, RenderBox not laid out), scroll errors, or setState-during-build errors. |
| `flutter-internationalization` | ✅ | asked to add l10n or i18n, translate Flutter UI text, configure l10n.yaml, manage ARB translations, migrate away from package:flutter_gen imports, or troublesho |
| `flutter-navigation` | ✅ | working with Navigator, MaterialPageRoute, Router API, go_router, route guards, redirects, ShellRoute or StatefulShellRoute, nested Navigators, passing and retu |
| `flutter-networking` | ✅ | asked to add network requests, investigate network errors, harden API clients, handle auth, or validate Flutter network behavior. |
| `flutter-pre-caching` | ⚠️ | preloading fonts, asset/network images, Lottie/Rive animations, local JSON/config, warming initial API data, or optimizing Flutter Web startup. |
| `flutter-tester` | ✅ | creating, writing, fixing, or reviewing tests in a Flutter project |
| `flutter-testing` | ✅ | adding unit tests, widget tests, integration tests, MethodChannel or plugin mocks, Mockito or mocktail test doubles, golden or accessibility checks, CI test com |
| `flutter-use-column-row-first` | ✅ | building any Flutter screen or component to choose responsive Row, Column, Expanded, Flexible, and Spacer layouts before fixed-size or coordinate-based alternat |
| `flutterfire-configure` | ✅ | adding Firebase to a Flutter project, running flutterfire configure, initializing Firebase in main.dart, or configuring multiple flavors. |
| `generate-images-with-firebase-ai` | ✅ | generating or editing images from Flutter/Dart with Firebase AI Logic and a Gemini image model (Nano Banana), making the first call work, choosing Gemini Develo |
| `glance-appwidget-updates-and-memory` | ✅ | configuring Android 17 (API level 37) compileSdk/targetSdk and AndroidManifest.xml widget receivers, refreshing frozen or stale Glance widget UI after Coroutine |
| `glance-canonical-layouts` | ✅ | create home screen widgets using Jetpack Glance Canonical Layouts from the Android Platform Samples project, or when asked to implement standard widget layout p |
| `iap-finalizer` | ✅ | Take a one-time in-app purchase from MISSING_METADATA to READY_TO_SUBMIT in App Store Connect — set its price schedule and localized display name/description (a |
| `inclusive-design` | ✅ | working on inclusion, i18n/localization, global name/address forms, low-end devices, slow/metered networks, affordability, or first-time/low-confidence users; n |
| `ink-app-builder` | ✅ | implementing stylus or touch drawing surfaces, rendering wet and dry ink strokes, configuring stock brushes (pressure pen, marker, highlighter), implementing ge |
| `ink-custom-brush-builder` | ✅ | configuring custom BrushTip shapes, adding pressure, tilt, speed, or noise sensitivity using BrushBehavior node graphs, creating multi-coat layered brushes, app |
| `integrating-pbl` | ✅ | integrating the Google Play Billing Library client side (adding the dependency, wiring BillingClient, managing its connection lifecycle, and querying product de |
| `ios-accessibility` | ✅ | developers mention: (1) iOS accessibility, VoiceOver, Dynamic Type, or assistive technologies, (2) accessibility labels, traits, hints, or values, (3) automated |
| `ios-code-audit` | ✅ | the user asks for a "code audit", "comprehensive review", "find tech debt", "what should I clean up", or similar broad-scope assessment of a Swift project. |
| `ios-design-guidelines` | ✅ | building, reviewing, or refactoring SwiftUI/UIKit interfaces for iOS |
| `ios-launch-performance` | ✅ | diagnosing iOS app launch performance, startup regressions, first-frame readiness, or early responsiveness |
| `ios-marketing-capture` | ⚠️ | the user wants to automate capture of marketing screenshots for a SwiftUI iOS app across multiple locales, devices, or appearances |
| `ios-perceived-performance` | ✅ | product-level iOS responsiveness and loading/feedback flows, including perceived latency, time to first feedback, progressive rendering, loading states, skeleto |
| `ios-performance-profiling` | ✅ | choosing, running, or interpreting iOS performance profiling workflows, including Instruments traces, signposts, XCTest metrics, MetricKit, Xcode Organizer, han |
| `ipados-design-guidelines` | ✅ | building iPad-optimized interfaces, implementing multitasking, pointer support, keyboard shortcuts, or responsive layouts |
| `jetpack-compose-audit` | ✅ | reviewing a Compose codebase, rating repository quality, inspecting recomposition/state issues, animation issues, or running a Compose audit. |
| `jetpack-compose-performance` | ✅ | analyzing performance bottlenecks of existing code to minimize recomposition overhead and prevent dropped frames and UI lag. |
| `keyword-optimizer` | ✅ | launching a new app, improving search rankings, entering new markets/languages, or safely optimizing ASO for an app with existing traffic. |
| `kotlin-build-kmp-gradle-governance` | ✅ | reviewing or designing Gradle build structure for KMP projects — shared build logic, convention plugins, version catalogs, Android KMP plugin usage, source-set  |
| `kotlin-data-kmp-data-layer` | ✅ | implementing or reviewing KMP data layers, including repositories, data sources, source-of-truth design, API exposure, conflict resolution, error handling, and  |
| `kotlin-kmp-code-review` | ✅ | reviewing implemented Kotlin Multiplatform / Compose Multiplatform code for architecture consistency, business-logic placement, state correctness, concurrency,  |
| `kotlin-kmp-refactor-safety` | ✅ | the task is primarily a refactor, migration, reliability hardening, or architectural cleanup of existing Kotlin Multiplatform code — scope control, behavioral p |
| `kotlin-navigation-compose-multiplatform` | ✅ | designing, implementing, or reviewing navigation in Compose Multiplatform projects — route modeling, back stack ownership, argument passing, NavOptions, conditi |
| `kotlin-platform-app-links-and-deep-links` | ✅ | designing, implementing, or reviewing Android deep links, web links, and App Links in KMP projects — intent-filter design, host verification, manifest scope, an |
| `kotlin-platform-kmp-bridges` | ✅ | designing, implementing, or reviewing platform-specific integrations in KMP projects, including source-set placement, hierarchical sharing, expect/actual usage, |
| `kotlin-project-architecture-review` | ✅ | reviewing KMP architecture, feature proposals, PR structure, layer boundaries, state-holder design, Android entry-point discipline, source-set placement, modula |
| `kotlin-project-bugfix` | ✅ | diagnosing and fixing bugs in a Kotlin Multiplatform project |
| `kotlin-project-feature-implementation` | ✅ | implementing or extending a feature in a Kotlin Multiplatform project |
| `kotlin-project-modularization` | ✅ | designing, reviewing, or refactoring module boundaries in KMP or Android projects — feature, data, app, and common modules, dependency direction, visibility con |
| `kotlin-project-state-management` | ✅ | choosing, implementing, or reviewing state-holder patterns in a KMP project — ViewModel, shared presenter, MVI, or StateFlow-in-common — including effect handli |
| `kotlin-testing-kmp` | ✅ | designing, implementing, or reviewing tests in KMP projects — unit tests, instrumented tests, Compose Multiplatform UI tests, test doubles, test strategy, stabi |
| `kotlin-ui-adaptive-resources` | ✅ | designing, implementing, or reviewing adaptive Compose UI for KMP or Android projects — window-size layouts, adaptive navigation, canonical layouts, multi-windo |
| `kotlin-ui-compose-multiplatform` | ✅ | designing, implementing, or reviewing shared UI in Compose Multiplatform projects, including state-driven architecture, composable decomposition, layout/modifie |
| `leanback-to-compose-tv-migration` | ✅ | Leanback to Compose migrations, including browse screen, settings screen, authentication screen, login screen, or video playback screen migrations, or when repl |
| `litert-lm` | ✅ | creating a chat, summarization, or extraction feature with a .litertlm model from Hugging Face litert-community (Gemma, Qwen, Llama, Phi), including the Gradle  |
| `litert-runtime` | ✅ | any Android LiteRT or .tflite task, including Gradle setup, image classification or vision/audio/embedding helpers, TensorBuffer reuse, CPU memory optimization, |
| `macos-design-guidelines` | ✅ | building macOS apps with SwiftUI or AppKit, implementing menu bars, toolbars, window management, or keyboard shortcuts |
| `marketing-strategy` | ✅ | planning app promotion, launch strategy, user acquisition, or re-engagement campaigns. |
| `media3-cast-integration` | ✅ | adding Cast functionality or migrating from legacy Cast SDK to Media3 Cast. |
| `migrate-xml-views-to-jetpack-compose` | ✅ | you need to migrate an XML View to Jetpack Compose in an Android project |
| `ml-kit-genai-prompt-api` | ✅ | send natural language requests on-device to Gemini Nano, use structured output with Prompt API, implement prefix caching, optimize the current prompt, or apply  |
| `mlkit-agent-api` | ✅ | implementing conversational agents, multi-turn chat with AgentSession in a ViewModel, autonomous tool calling using Android AppFunctions (@AppFunctionDeclaratio |
| `mobile-toolchain-unifier` | ✅ | the user asks to clean, unify, upgrade, or optimize Android SDKs, NDKs, Gradle wrappers, Java/JVM daemons, iOS simulator runtimes, |
| `mockito` | ✅ | generating mocks, stubbing methods, verifying interactions, capturing arguments, or choosing between mocks, fakes, and real objects (Mockito). |
| `mocktail` | ✅ | creating mocks, stubbing methods, verifying interactions, registering fallback values, or choosing between mocks, fakes, and real objects (Mocktail). |
| `navigation-3` | ✅ | Learn how to install and migrate to Jetpack Navigation 3, and how to implement features and patterns such as deep links, multiple backstacks, scenes (dialogs, b |
| `navigation-event` | ✅ | Intercept back gestures and run Predictive Back animations using the NavigationEvent (androidx.navigationevent) library in Compose Android. |
| `one-time-products` | ✅ | implementing, acknowledging, or consuming Google Play one time products (consumables and non consumables) with the Play Billing Library |
| `originality-check` | ✅ | Guideline-4.3 anti-spam / originality gate — score whether an app (and each portfolio addition) is meaningfully distinct in function, content, and metadata befo |
| `owasp-mobile-security-checker` | ✅ | performing security audits, vulnerability assessments, or compliance checks on Flutter or mobile applications |
| `patrol-e2e-testing` | ✅ | writing E2E/integration tests, testing native interactions like permissions or system dialogs, capturing UI regressions, or validating cross-platform behavior ( |
| `payment-recovery` | ✅ | handling failed subscription renewals on Google Play |
| `pbl-v7-to-v8-migration` | ✅ | migrating an Android app from Play Billing Library 7.x to 8.x (latest 8.3.0) |
| `pbl-v7-to-v9-migration` | ✅ | migrating an Android app from Play Billing Library 7.x to 9.x (latest 9.1.0) |
| `pbl-v8-to-v9-migration` | ✅ | migrating an Android app from Play Billing Library 8.x to 9.x (latest 9.1.0) |
| `plan-changes` | ✅ | implementing Google Play subscription upgrades, downgrades, or plan switches with SubscriptionProductReplacementParams (PBL 8.1+) plus SubscriptionUpdateParams. |
| `play-billing-library-version-upgrade` | ✅ | upgrading or migrating an Android project from any legacy Google Play Billing Library (PBL) version to the latest stable version of PBL. |
| `play-developer-api-reference` | ✅ | Use this skill as a quick reference for billing related Google Play Developer API REST endpoints, covering purchases.products, purchases.subscriptionsv2, purcha |
| `play-policy-insights` | ✅ | Automated auditor designed to verify Android applications against Google Play Policy domains. |
| `price-changes` | ✅ | changing subscription prices on Google Play |
| `projected-hardware` | ✅ | building experiences for intelligent eyewear in an Android app and you need to access device hardware like the camera and microphone, handle glasses-specific ru |
| `provider` | ✅ | setting up providers, consuming state, optimizing rebuilds, using ProxyProvider, or migrating from deprecated providers (Provider package). |
| `purchase-flow` | ✅ | implementing the Play Billing purchase flow end to end |
| `r8-analyzer` | ✅ | developers want to optimize their Android app's size, remove redundant or overly broad keep rules, or troubleshoot ProGuard configurations |
| `ratings-mechanics` | ✅ | planning ratings strategy for new markets, considering a ratings reset, setting release options, or diagnosing "why is my rating missing in country X. |
| `rejection-handler` | ✅ | user's app was rejected, is preparing for submission, or needs help with App Review. |
| `restore-credentials` | ✅ | create, sign in with, and delete restore keys, enabling silent user sign-in on new devices after a restore |
| `revenuecat-testing` | ✅ | testing RevenueCat purchases/subscriptions, setting up sandbox testing, debugging a purchase/restore/trial, verifying entitlements or events, checking an app is |
| `review-response-writer` | ✅ | responding to negative reviews, drafting templates for common review types, or improving review management strategy. |
| `riverpod` | ✅ | setting up providers, combining requests, managing state disposal, passing arguments, performing side effects, or testing providers (Riverpod). |
| `rtdn` | ✅ | setting up Real Time Developer Notifications (RTDN) for Google Play |
| `rtdn-reference` | ✅ | . |
| `screenshot-planner` | ✅ | preparing App Store assets, improving screenshot conversion, or drafting screenshot captions for a launch or major update. |
| `setup@revenuecat` | ✅ | configuring Play Console, creating products, enabling service account API access, or setting up RTDN before writing billing code |
| `styles` | ✅ | integrate the Jetpack Compose Styles API into an Android project |
| `subscription-state-diagram` | ✅ | . |
| `subscription-states` | ✅ | mapping a Google Play subscription to the eight states (PENDING, ACTIVE, IN_GRACE_PERIOD, ON_HOLD, PAUSED, CANCELED, EXPIRED, PENDING_PURCHASE_CANCELED) and dec |
| `subscriptions` | ✅ | modeling Google Play subscriptions (the three tier Subscription, Base Plan, Offer hierarchy), choosing a catalog shape, and deciding how to map your paywall to  |
| `swift-code-reviewer` | ✅ | reviewing PRs/MRs (especially AI-generated ones), performing quality audits, validating against original spec, or providing structured feedback with severity le |
| `swift-concurrency` | ✅ | developers mention: (1) Swift Concurrency, async/await, actors, or tasks, (2) "use Swift Concurrency" or "modern concurrency patterns", (3) migrating to Swift 6 |
| `swift-concurrency-performance` | ✅ | reviewing Swift Concurrency performance and responsiveness, including task explosions, actor hopping, MainActor bottlenecks, cancellation, AsyncSequence cleanup |
| `swift-concurrency@tuist` | ✅ | working with async/await, Tasks, actors, MainActor, Sendable, isolation domains, or debugging concurrency compiler errors |
| `swift-expert` | ✅ | Swift specialist for iOS/macOS development with Swift 6.0+, SwiftUI, async/await concurrency, and protocol-oriented design. |
| `swift-runtime-performance` | ✅ | reviewing Swift code for runtime-level performance costs, including heap allocation, ARC traffic, stack vs heap storage, closure capture contexts, method dispat |
| `swift-testing` | ✅ | developers mention: (1) Swift Testing, @Test, #expect, #require, or @Suite, (2) "use Swift Testing" or "modern testing patterns", (3) test doubles, mocks, stubs |
| `swiftdata-pro` | ✅ | reading, writing, or reviewing projects that use SwiftData. |
| `swiftui-design-principles` | ✅ | creating or modifying SwiftUI views, iOS widgets (WidgetKit), or any native Apple UI |
| `swiftui-expert-skill` | ✅ | building new SwiftUI features, refactoring existing views, reviewing code quality, or adopting modern SwiftUI patterns. |
| `swiftui-performance` | ✅ | reviewing or fixing SwiftUI performance issues, including unnecessary invalidation, unstable identity, broad state dependencies, expensive body work, heavy rows |
| `swiftui-ui-patterns` | ✅ | creating or refactoring SwiftUI UI, designing tab architecture with TabView, composing screens with VStack/HStack, managing @State or @Binding, building declara |
| `testing` | ✅ | writing or reviewing Flutter/Dart tests (unit, widget, golden), fixing flaky tests, adding coverage, or choosing between unit and widget tests. |
| `testing-setup` | ✅ | Analyze and create a testing strategy for Android apps - install testing libraries, set up test infrastructure, create harnesses for unit tests, UI tests, scree |
| `testing@revenuecat` | ✅ | testing a Google Play Billing integration |
| `tvos-design-guidelines` | ✅ | building tvOS apps with focus-based navigation, Siri Remote input, or living room viewing experiences |
| `understanding-billing` | ✅ | a developer is new to Google Play Billing or needs to orient themselves before picking an implementation task |
| `verified-email` | ✅ | integrate a secure, OTP-less email verification flow into an Android app |
| `visionos-design-guidelines` | ✅ | building spatial computing apps, implementing eye/hand input, or designing immersive experiences |
| `watchos-design-guidelines` | ✅ | building watchOS apps, complications, or workout features |
| `wear-compose-m3` | ✅ | Guidance for Wear OS Compose Material3 (Wear Compose Material 3 / Wear Compose Material3) watch and wearable apps. |
| `wear-widgets` | ✅ | implementing GlanceWearWidget, GlanceWearWidgetService, WearWidgetDocument, Remote Compose UI primitives (RemoteColumn, RemoteRow, RemoteBox, RemoteText, Remote |
| `web-presence` | ✅ | building a landing page, improving Google visibility for an app, planning a price-drop promotion, or auditing off-store discovery. |
