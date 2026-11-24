# 04-skill-plugin-yazimi — AI ve Otomasyon

_Skill yazma, plugin/hook/komut geliştirme_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **12/187**

### ab-testing-framework  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** A/B and multivariate testing methodology. Design experiments, calculate sample sizes, determine statistical significance, avoid common pitfalls, and interpret results. Platform-agnostic framework applicable to landing pages, emails, ads, pricing, and product features. Use when the user asks about A/B testing, split testing, experiment design, statistical significance, or conversion experiments.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 5.3 KB, yük kucuk)
- **İnceleme:** otomatik

### account-structure-review  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Google and Meta paid media account structure evaluation. Audits campaign/ad set architecture against conversion volume minimums, budget thresholds, and targeting overlap. Identifies over-segmentation, under-segmentation, budget fragmentation, and structural anti-patterns blocking algorithmic learning. Provides consolidation roadmaps with migration plans. Use when inheriting accounts, quarterly hea
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 85 KB (SKILL.md 23.4 KB, yük orta)
- **İnceleme:** otomatik

### aeo-geo-optimizer  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) specialist. Optimize content and websites to appear in AI-generated answers from ChatGPT, Perplexity, Claude, Google AI Overviews, and other LLM-powered search experiences. Use when the user asks about AI search optimization, AEO, GEO, AI Overviews, appearing in AI answers, LLM citations, or optimizing for generative search.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 9.6 KB, yük orta)
- **İnceleme:** otomatik

### agent-development  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 68 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** otomatik

### agent-development@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 80 (A)

- **Ne yapar:** Claude Code eklentileri için alt-agent (subagent) yazımı: Markdown + YAML frontmatter yapısı, name/description/model/color/tools alanları, <example> bloklarıyla tetikleme koşulları, sistem istemi tasarımı, AI destekli üretim ve doğrulama kuralları; doğrulama betiği ve örnekler içerir.
- **Ne zaman:** Claude Code projesine/eklentisine özel alt-agent tanımı yazmak ya da mevcut agent'ın tetiklenmesini düzeltmek. · **Ne zaman değil:** Codex'te frontmatter biçimi geçerli değil: Codex özel agent'ları `.codex/agents/<ad>.toml` dosyasında `name`, `description`, `developer_instructions` (ve isteğe bağlı skills.config) alanlarıyla tanımlanır — bu kütüphanenin skill-ekle.py'si rolleri zaten bu biçimde üretir. Skill'in sistem istemi tasarımı ve 'ne zaman tetiklenmeli' açıklaması yazım ilkeleri Codex'te de geçerli; color/model/tools alanlarını atla.
- **Teknoloji:** claude-code, markdown, yaml
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-alt-agent-tanimi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 69 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi plugin-dev setinden; alan alan doğrulama kuralları ve örnekler net. Claude Code'a özel (Codex için yukarıdaki uyarlama).

### android-benchmark-comparison  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when comparing physical Android benchmark configurations, investigating inconsistent rankings, or selecting an Android default from measured results. Do not use for code-level Compose performance diagnosis without a configuration comparison.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### apple-aso  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Optimize Apple App Store metadata in store.config.json for ASO (App Store Optimization). Use when working with store.config.json, App Store keywords, titles, subtitles, descriptions, or localizing app metadata. Helps maximize app visibility and downloads.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### apple-docs-index  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 78 (B)

- **Ne yapar:** Index of Apple developer documentation for iOS, macOS, and related frameworks. Use when looking up what APIs exist in a framework, browsing available documentation, or deciding what docs to fetch. Covers SwiftUI, UIKit, Core Animation (QuartzCore), XCTest, HealthKit, Combine, SwiftData, and more.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3641 KB (SKILL.md 3.0 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### backgroundtasks  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: BackgroundTasks. Query for BGTaskScheduler, app refresh, background processing.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### baguette  ·  tddworks/baguette @ e0a4cc4  ·  puan 87 (A)

- **Ne yapar:** Drive and inspect iOS simulators with the `baguette` CLI: taps, swipes, buttons, typing, screenshots, the accessibility tree, logs, and the conditions an app runs under (location, network, appearance, push, UserDefaults), without opening Xcode. Use when an agent must act on or verify a running simulator — a UI flow, smoke test or demo, checking a code change on screen — or when the user names `bag
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tddworks (kurum, ★2345, son güncelleme 2026-11-23, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 85 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### baguette-test-app  ·  tddworks/baguette @ e0a4cc4  ·  puan 87 (A)

- **Ne yapar:** Test an iOS app the way a person uses it: read the simulator's screen, decide what's next, click, and check what happened, with the `baguette` CLI. Use when asked to test, QA, verify or walk through an app or a user flow on a simulator, check that a change works on screen, or complete a task inside an app ("sign up and check the receipt"). For the commands themselves, or for driving a simulator wi
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tddworks (kurum, ★2345, son güncelleme 2026-11-23, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.5 KB, yük kucuk)
- **İnceleme:** otomatik

### better-i18n  ·  better-i18n/oss @ 249e1ee  ·  puan 79 (B)

- **Ne yapar:** Guides all better-i18n integration decisions — SDK selection (Next.js, React, Expo, Swift, Flutter, Remix), CDN vs GitHub workflow, AI-powered translation management via MCP tools, CLI health checks (scan, doctor, sync), Content CMS (localized models, entries, custom fields), file format conventions (flat / nested / namespaced), key naming, publish flows, and quality analytics. Use whenever buildi
- **Teknoloji:** next.js, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** better-i18n (kurum, ★21, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 98 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### braze  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Braze customer engagement platform expertise. Audit campaigns, Canvases, segments, messaging channels, and data architecture. Use when the user asks about Braze, customer engagement, push notifications, in-app messaging, cross-channel orchestration, or lifecycle marketing at scale.
- **Teknoloji:** canvas, git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 5.7 KB, yük kucuk)
- **İnceleme:** otomatik

### breakdown-diagnosis  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** When a machine goes down, reads the sensor window before the failure, the asset's maintenance history including the free-text close-out notes technicians actually wrote, photos of what they can see, and the manufacturer's troubleshooting tree — then ranks likely causes, each with its supporting evidence, the specific prior work orders behind it, and the cheapest test that would tell them apart. Su
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 17.4 KB, yük orta)
- **İnceleme:** otomatik

### breakdown-to-next-report  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the sensor window, the maintenance history and its free-text close-out notes, technician photographs and the manufacturer's manual together, ranks likely causes with the cheapest test that tells them apart, then folds the diagnosis and its downtime into the next morning's downtime log and excep
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik

### build-a-baseline  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Stop conclusions drifting between sessions by turning a judgement call into a fixed scoring rule over measured data, with the subjective inputs frozen in a file, the measuring instrument validated against a known-good source, and falsification thresholds written down before the test is run. Use when the user says you keep changing your mind, contradicting yourself, or have no baseline; when the sa
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### business-motion-film  ·  echris6/motion-video-kit @ e4b1c00  ·  puan 79 (B)

- **Ne yapar:** Plan, build and quality-check a premium short commercial for a real business (roofing, property, ecommerce, B2B software) using AI-generated footage, code-built motion (HTML/GSAP), selective Three.js and an independent-critic "Gauntlet" loop. Use when asked to make a launch-style / SaaS-style video, business ad, explainer, sample reel or pitch video, or to review and improve one. Encodes motion pr
- **Teknoloji:** api-anahtari, gsap, html, python, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** echris6 (kisi, ★1455, son güncelleme 2026-10-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 110 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** otomatik

### changelog@chrisbanes  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when updating or reviewing Unreleased changelog entries, reconciling a changelog against Git history and issue or PR evidence, or preparing changelog notes for a specified release.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 7 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** otomatik

### climb  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** Work out where a teammate, the champion, or a team is on the steps of AI adoption, and what to try next. Use when a champion wants to help someone move up a step.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** otomatik

### cold-email-outreach  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Cold email and outreach sequence design with personalization, deliverability optimization, follow-up cadence, and compliance (CAN-SPAM/GDPR). Use when the user asks about cold email, outreach sequences, email prospecting, cold outreach, or email deliverability for outbound.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### combine  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Combine. Query for publishers, subscribers, operators, async data streams.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 150 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### command-development  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in com
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, commands); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 151 KB (SKILL.md 18.8 KB, yük orta)
- **İnceleme:** otomatik

### command-development@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 80 (A)

- **Ne yapar:** Claude Code slash komutu yazımı: komut konumları (proje/kullanıcı/eklenti), YAML frontmatter (description, allowed-tools, model, argument-hint, disable-model-invocation), $ARGUMENTS ve konumsal argümanlar, @dosya başvuruları, satır içi bash çalıştırma, AskUserQuestion ile etkileşim ve organizasyon/namespacing.
- **Ne zaman:** Ekipte tekrar eden istemleri Claude Code slash komutuna çevirmek. · **Ne zaman değil:** Codex'te Claude slash komut biçimi yok: karşılığı `~/.codex/prompts/<ad>.md` özel istem dosyaları (`/prompts:<ad>` ile çağrılır; $ARGUMENTS/$1 yer tutucuları desteklenir) ya da doğrudan bir skill'dir. allowed-tools, model, satır içi `!bash` çalıştırma ve @dosya başvurusu Codex'te çalışmaz — bunları istemin içinde 'şu komutu çalıştır / şu dosyayı oku' talimatına çevir.
- **Teknoloji:** claude-code, markdown, yaml
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-slash-komut → birincil · **Roller:** skill-gelistirici
- **Boyut:** 150 KB (SKILL.md 18.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi, çok sayıda örnek ve referans; SKILL.md 19 KB ve klasör 150 KB ile ağırca. Claude Code'a özel.

### competitor-ads-analyst  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Extract and analyze competitor advertising from public ad libraries (Facebook Ad Library, Google Ads Transparency Center, TikTok, LinkedIn). Identifies messaging patterns, creative formats, pain points targeted, and positioning gaps. Use for competitive intelligence, campaign planning, and creative inspiration.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-animations  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Jetpack Compose motion: visibility enter/exit, animating one property toward a target, color or size transitions, multiple properties from one state, switching composable content, or choosing between AnimatedVisibility, animate*AsState, updateTransition, rememberTransition, AnimatedContent, and Crossfade.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-component-design  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when designing or reviewing reusable Jetpack Compose component APIs with modifier parameters, root layout placement, caller-provided variable content, primitive content parameters, optional content, or boolean shape flags.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-focus-navigation  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Jetpack Compose UI for TV, keyboard, desktop, accessibility focus, D-pad navigation, FocusRequester, focusProperties, key events, or initial focus behavior.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-performance  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when investigating Jetpack Compose recomposition cost, compiler stability reports, skippability, unstable parameters, frame-rate State reads, cross-phase snapshot back-writing, or @ReadOnlyComposable contracts.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-state-and-effects  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Jetpack Compose state ownership, remember state, state hoisting, screen state holders, LaunchedEffect, DisposableEffect, SideEffect, Flow collection, navigation, snackbar, analytics, or focus requests.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** otomatik

### compose-ui-testing-patterns  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Jetpack Compose UI tests, screenshot tests or baseline-recording evidence, previews, semantics assertions, fake image loading, keyboard input, focus assertions, interaction state (hover/pressed/focused), or tests for plain state-driven UI composables.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 7.5 KB, yük kucuk)
- **İnceleme:** otomatik

### content-creator  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Comprehensive content marketing toolkit with brand voice analysis, SEO optimization scripts, content frameworks, social media strategy, and content calendar planning. Use when writing blog posts, creating social media content, analyzing brand voice, optimizing SEO, planning content calendars, or developing content strategy. For deep SEO writing optimization, see the seo-content-writer skill.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### content-pipeline  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** End-to-end content creation workflow that orchestrates research, editorial review, and social distribution agents in sequence. Use when the user wants to create, review, and distribute content through a multi-stage pipeline, or says "/content-pipeline".
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### content-workflow  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** End-to-end content creation pipeline from research through editorial review to social distribution. Orchestrates a 3-stage workflow: research, draft/edit, and distribute. Supports blog posts, LinkedIn, Twitter threads, newsletters, and essays.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### copywriting-frameworks  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Framework-driven copywriting for ads, landing pages, emails, sales pages, and CTAs. Includes AIDA, PAS, BAB, 4Ps, StoryBrand, QUEST, FAB, and more. Use when writing conversion-focused copy, ad creative, headlines, email sequences, sales pages, or when the user mentions copywriting frameworks, persuasive writing, or direct response copy.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### core-animation  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Core Animation (QuartzCore). Query for CALayer, CAAnimation, CABasicAnimation, CAKeyframeAnimation, CASpringAnimation, CATransaction, CAShapeLayer, CAGradientLayer, CAEmitterLayer, CATransform3D, CADisplayLink.
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 215 KB (SKILL.md 4.8 KB, yük kucuk)
- **İnceleme:** otomatik

### corehaptics  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Core Haptics. Query for CHHapticEngine, haptic patterns, tactile feedback.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### cowork-plugin-customizer  ·  anthropics/knowledge-work-plugins @ 0e0fcac  ·  puan 95 (A)

- **Ne yapar:** Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★36794, son güncelleme 2026-11-23, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### create-cowork-plugin  ·  anthropics/knowledge-work-plugins @ 0e0fcac  ·  puan 95 (A)

- **Ne yapar:** Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★36794, son güncelleme 2026-11-23, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 13.0 KB, yük orta)
- **İnceleme:** otomatik

### cro-auditor  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Conversion Rate Optimization auditing for landing pages, signup flows, checkout funnels, forms, and CTAs. Identifies friction points, runs heuristic evaluations, produces prioritized recommendations using ICE/PIE frameworks. Use when the user asks about conversion optimization, funnel analysis, landing page audits, form optimization, CTA testing, or checkout improvement.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### cross-platform-audit  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 56 (C)

- **Ne yapar:** Unified multi-platform paid media audit with parallel execution. Spawns scored audits for Google Ads, Meta Ads, and Microsoft Ads simultaneously, merges results into a budget-weighted aggregate health score (A-F), adds cross-platform analysis (budget allocation, tracking consistency, creative alignment, attribution overlap), and produces a prioritized action plan. Optionally generates a client-rea
- **Teknoloji:** git, html _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### custom-connector  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Gets the plugin talking to a manufacturing system that has no vendor MCP, working down a seven-tier access ladder in order — vendor MCP, community MCP, a scoped API wrapper, a read-only database view, a Zapier bridge, screen automation as a last resort, or a scheduled export contract — and stopping at the highest rung that actually works. States plainly at every rung what the customer gets, what i
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 45 KB (SKILL.md 22.6 KB, yük orta)
- **İnceleme:** otomatik

### customer-inquiry-intake  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal export, a phone photo of a marked-up print, or a forwarded thread where the real requirement is four messages down — and pulls specifications, quantities and dates into one consistent intake form with every field traceable to the file and page it came from. Records how each tolerance was read
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 20.7 KB, yük orta)
- **İnceleme:** otomatik

### customer-journey-mapping  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Map customer journeys from awareness to advocacy. Visualize touchpoints, identify drop-off points, analyze channel interactions, and optimize the end-to-end experience. Use when the user asks about customer journey, funnel mapping, touchpoint analysis, or experience optimization.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### daily-production-report  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Produces the morning production report: output against plan by line, cell and product; OEE with availability, performance and quality shown separately; the downtime log ranked both by minutes and by frequency; scrap and downtime priced in dollars; week-over-week movers; and the exceptions needing a decision today. For each significant exception it drafts a specific reschedule or changeover move wi
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 27.0 KB, yük buyuk)
- **İnceleme:** otomatik

### data-consolidate  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor M3), sales orders, production work orders, purchase orders, inventory, routings and closed-job operation actuals; CMMS assets and maintenance work orders; and the MES, historian, quality and planning files landing in the Microsoft 365 export folder. Keys on part number, production work or
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** otomatik

### data-viz-deck  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Transform audit data, performance reports, and structured analyses into polished visual deliverables. Generates presentation decks (PPTX), interactive HTML dashboards, or styled markdown reports with charts. Includes a customizable design system with forest green accent and warm cream backgrounds. Use when the user has analysis data and needs a visual deliverable.
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### deliver-issue  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when explicitly asked to deliver a named tracker issue and its descendants, including clarification, planning, implementation and reviewed delivery.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 385 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik

### dep-audit  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Cross-repository dependency audit. Scans package manifests for outdated packages, security advisories, version conflicts, and license issues. Produces a prioritized update plan. Supports Node.js, Python, Rust, and Go projects.
- **Teknoloji:** git, node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 7.8 KB, yük kucuk)
- **İnceleme:** otomatik

### design-space-explore  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Generates a batch of CAD variants directly in Autodesk Fusion by applying changed parameters to an engineer's existing model, never designing from scratch and never overwriting the base. Checks first whether the parameters the engineer wants to vary actually drive the model's geometry, and stops rather than generating garbage if they don't. Confirms the variant count with the engineer before gener
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 11.0 KB, yük orta)
- **İnceleme:** otomatik

### email-composer  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Draft professional emails for business and marketing contexts — outreach, client communication, proposals, follow-ups, and internal updates. Includes tone calibration, subject line formulas, and follow-up cadence recommendations.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### eventkit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: EventKit. Query for EKEventStore, EKEvent, EKReminder, calendar access.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 56 KB (SKILL.md 0.6 KB, yük kucuk)
- **İnceleme:** otomatik

### extract-lessons  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Harvest a finished session for anything that would help beyond this one project, decide honestly where each piece belongs, and put it there. Most sessions yield nothing, and saying so is the correct outcome. Separates a project detail from a general trap, routes real findings to the right skill as a pull request, spots when a cluster of homeless lessons means a new skill is needed, and recognises 
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik

### facebook-ads  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Meta Ads (Facebook & Instagram) platform expertise. Audit campaigns, audiences, creative strategy, pixel tracking, and CAPI. Use when the user asks about Facebook Ads, Instagram Ads, Meta Ads, social media advertising, Advantage+ campaigns, or Meta pixel/CAPI setup.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** otomatik

### fact-check  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Re-check stated facts about the App Store, Google Play and app tools against the current official pages, update each fact's status and date, fix broken source links, and report what changed. Works on a project's rules file and docs, or on The Last Mile's own traps and facts (one topic or all of them). Use when the user says "check the facts", "is this still true", "re-verify the traps", "store rul
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### faq  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Turn repeat questions into a pinned FAQ. Use when a champion keeps answering the same questions.
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.1 KB, yük kucuk)
- **İnceleme:** otomatik

### feature-demo  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Build a tap-through demo of a feature so the person can see it before it ships, instead of reading a spec about it. Enumerates the feature's real states, draws them in the app's own colours and fonts, publishes a clickable walkthrough, and annotates each step with the decision behind it. Use when a feature has states nobody can reach by tapping around, when a spec conversation has stalled, when as
- **Teknoloji:** css, html, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### github-readme  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Generate, audit, or update GitHub READMEs with project-type-aware structure, voice calibration, and SEO/AEO discoverability guidance. Three modes: generate (new), audit (check existing), update (patch). Detects repo type and adapts sections, tone, and badges accordingly.
- **Teknoloji:** api-anahtari, docker, git, next.js, node, python, react, svelte, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 36 KB (SKILL.md 11.5 KB, yük orta)
- **İnceleme:** otomatik

### google-ads  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Google Ads platform expertise. Audit campaigns, keywords, audiences, bidding, and conversion tracking. Use when the user asks about Google Ads, PPC, search advertising, Performance Max, Shopping ads, display campaigns, YouTube ads, or paid search optimization.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 68 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### google-analytics  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Analyze Google Analytics data, review website performance metrics, identify traffic patterns, and suggest data-driven improvements. Use when the user asks about analytics, website metrics, traffic analysis, conversion rates, user behavior, or performance optimization.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 57 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### google-tag-manager  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Google Tag Manager expertise. Audit GTM containers, design tag and trigger architecture, debug firing issues, implement consent mode v2, and advise on server-side tagging. Use when the user asks about GTM, tag management, container audits, consent mode, server-side tagging, or tracking implementation.
- **Teknoloji:** api-anahtari, css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 61 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik

### gradle-run  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when planning to execute Gradle through `gradle`, `./gradlew`, or a custom `gradlew*` wrapper script, or diagnosing a Gradle build, recovering a workflow's status, compact workflow ledger, repeated failure fingerprint, check, test, lint, warning, or failure even when no new Gradle run is appropriate.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 151 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### grounded-writing  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when drafting or reviewing public developer documentation, other text the user will publish or send, or a user-owned draft under an explicit editorial review, including review comments, replies, and internal technical reports.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-macos-spm-packaging  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Scaffold, build, and package SwiftPM-based macOS apps without an Xcode project. Use when you need a from-scratch macOS app layout, SwiftPM targets/resources, a custom .app bundle assembly script, or signing/notarization/appcast steps outside Xcode.
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-swift-concurrency  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Swift concurrency patterns — actors, structured concurrency, cancellation, async streams, GCD migration, strict-concurrency diagnostics, common bug patterns. Use when writing, reviewing, or debugging concurrent Swift code.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 53 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-swift-testing  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Swift Testing patterns — structs over classes, async confirmations, parameterized tests, exit tests, attachments, common agent mistakes. Use when writing, reviewing, or migrating Swift Testing code.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-swiftdata  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** SwiftData patterns — autosave, relationships, dangerous predicates, CloudKit constraints, indexing, class inheritance. Use when writing, reviewing, or debugging SwiftData code.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-swiftui-charts  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Swift Charts patterns — marks, axes, selection, styling, composition, Chart3D, accessibility, and Audio Graph. Use when building or improving charts in SwiftUI.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### guide-swiftui-performance-audit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Audit and improve SwiftUI runtime performance from code review and architecture. Use for requests to diagnose slow rendering, janky scrolling, high CPU/memory usage, excessive view updates, or layout thrash in SwiftUI apps, and to provide guidance for user-run Instruments profiling when code review alone is insufficient.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### hackathon  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** Plan a hackathon, either from a team's real backlog or as open-ended creative play with Claude Code. Use when a champion wants to run a hack day or a shorter hack session.
- **Teknoloji:** git, html _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, agents, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.6 KB, yük orta)
- **İnceleme:** otomatik

### healthkit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: HealthKit. Query for HKHealthStore, HKQuantitySample, workouts, health data read/write.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 383 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### hig  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Fact lookup: Apple Human Interface Guidelines corpus (greppable markdown). Query on demand for accessibility and ergonomic minimums (hit-target sizes, Dynamic Type), platform terminology, system component capabilities, and App-Review-relevant conventions. Not design direction.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 619 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** otomatik

### hook-development  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### hook-development@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 88 (A)

- **Ne yapar:** Claude Code hook'ları: prompt tabanlı (LLM kararlı) ve komut hook'ları, eklenti hooks.json ve settings biçimi, PreToolUse/PostToolUse/Stop/SubagentStop/SessionStart/SessionEnd/UserPromptSubmit/PreCompact/Notification olayları, çıktı biçimi, ${CLAUDE_PLUGIN_ROOT}; doğrulama/test betikleri ve örnek hook'lar içerir.
- **Ne zaman:** Tehlikeli komutu engelleme, düzenleme sonrası otomatik format/test, oturum başında bağlam yükleme gibi olay tabanlı Claude Code otomasyonu. · **Ne zaman değil:** Codex'te Claude Code hook olayları ve hooks.json biçimi birebir yok; Codex'in kendi onay/sandbox politikası (`approval_policy`, `sandbox_mode`) ve sürümüne göre sunduğu hook/notify ayarları `~/.codex/config.toml` içinde yapılır. Bu skilldeki betik mantığı Codex'te sandbox kuralı, AGENTS.md talimatı ya da git pre-commit hook'u olarak uygulanabilir; prompt tabanlı hook'ların karşılığı yoktur. Basit 'şunu görünce uyar' kuralları için writing-hookify-rules daha hızlı.
- **Teknoloji:** claude-code, bash, json · **Paketler:** jq (betikler için)
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-hook → birincil · **Roller:** skill-gelistirici
- **Boyut:** 63 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil, hook grubunda). Anthropic resmi; tüm olaylar, girdi/çıktı şemaları ve test betikleri tek yerde. hookify kuralına göre daha güçlü ama daha zahmetli.

### html-report-builder  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Create polished HTML technical reports and multi-page documents for consulting deliverables. Features a professional design system with dark cover pages, warm cream content pages, Switzer + Cartograph CF typography, and a curated component library (KPI cards, data tables, callout boxes, recommendation cards, priority banners). Outputs standalone HTML that prints cleanly to PDF.
- **Teknoloji:** css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 4.8 KB, yük kucuk)
- **İnceleme:** otomatik

### i-have-adhd  ·  ayghri/i-have-adhd @ 1ecea19  ·  puan 93 (A)

- **Ne yapar:** Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estimates, make wins visible. Invoke with /i-have-adhd; stays on until "stop adhd mode".
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ayghri (kisi, ★62154, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** otomatik

### icp-research  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Build detailed ideal customer profiles with pain points, objections, buying triggers, and messaging angles. Includes community research to find where ICPs gather online and extract their exact language. Use when researching audiences, creating buyer personas, or developing targeted messaging.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** otomatik

### implement-with-subagents  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when implementing supplied tickets or plan tasks with solo or worker-owned implementation selected from the task graph, or when reviewing that orchestration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### improve-skill  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Fix a Last Mile skill that did the wrong thing, from inside the project where it went wrong. Decides whether the lesson belongs in the project's rules file or in the skill, makes the smallest change to the skill in The Last Mile repo (never the synced copy), keeps every project detail out because the repo is public, runs the checks and opens a pull request. Also adds a store or build trap other ap
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### inspection-to-capa  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches history at the moment of writing to say whether this has happened before and whether the last fix held, reads sensor and inspection data on one verified timeline, proposes ranked candidate causes with evidence for and against, drafts the 8D, and produces the customer pack behind a redaction d
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### ios-dev  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** Start here for any iOS or SwiftUI task. Coordinates best-practice guides, correctness checks, and full Apple API references. Use before navigating to other Apple skills — for building, reviewing, refactoring, or debugging iOS apps.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### ios-liquid-glass  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Liquid Glass (iOS 26+). Query for glass effects, navigation patterns, GlassEffect modifiers, design principles.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 112 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### klaviyo-analyst  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Klaviyo marketing operations and analyst expertise. Audit flows, segments, campaigns, deliverability, and revenue attribution. Use when the user asks about Klaviyo marketing strategy, email/SMS automation, customer segmentation, flow optimization, or lifecycle marketing. For API integration, SDK, webhook, or developer questions, see the klaviyo-developer skill.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 101 KB (SKILL.md 19.7 KB, yük orta)
- **İnceleme:** otomatik

### klaviyo-developer  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Klaviyo API and developer integration expertise. Event tracking, SDKs, webhooks, rate limits, OAuth, catalog sync, and code patterns. Use when the user asks about Klaviyo API, integrating with Klaviyo, tracking events, building custom integrations, webhook handling, or developer implementation. For marketing strategy, flow optimization, and campaign auditing, see the klaviyo-analyst skill.
- **Teknoloji:** api-anahtari, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 122 KB (SKILL.md 19.3 KB, yük orta)
- **İnceleme:** otomatik

### kotlin-api-design  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when designing or reviewing Kotlin function ownership, member or extension functions, factories, single-field domain types, value classes, data classes, Kotlin Multiplatform expect/actual declarations, or platform service boundaries.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### kotlin-concurrency-and-flow  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Kotlin coroutine scope ownership, raw Thread or Executor work, init launches, non-suspending launch APIs, runBlocking, cancellation, StateFlow, SharedFlow, Channel, stateIn, SharingStarted, state updates, or one-shot events.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### kotlin-control-flow  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when writing or reviewing Kotlin branching and control flow: when expressions, guard conditions, sealed type exhaustiveness, smart casts, nullable branching, early returns, or replacing complex if/else chains.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### landing-page-optimizer  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Landing page audit and optimization for conversion. Covers above-the-fold design, value propositions, CTAs, social proof placement, form design, page speed, and mobile optimization. Use when the user asks about landing page optimization, conversion rate improvement, page audits, or CTA optimization.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### lean-out  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Find the structural clutter in an app that is making every new change land wrong, and rank it by what it would have prevented rather than by taste. Produces a measured audit and a list that can be worked through in pieces, never a big bang refactor. Use when the codebase feels heavy, when the same kind of bug keeps coming back in a new place, when a file has grown past anyone's head, or when the a
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### library-curator  ·  nexu-io/open-design @ e033aad  ·  puan 97 (A)

- **Ne yapar:** Search the OD Library (the global asset registry) and apply matching assets into the current project mid-task. Use when the user asks to reuse an image they captured/uploaded earlier, "pull a logo/screenshot from my library", or to find and drop a stored asset into the page being built.
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★109313, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### linkedin-ads  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** LinkedIn Ads platform expertise. Audit campaigns, optimize targeting (job title, company, seniority, industry), creative strategy, Lead Gen Forms, conversion tracking, and ABM campaigns. Use when the user asks about LinkedIn advertising, B2B paid social, LinkedIn campaign optimization, Lead Gen Forms, Matched Audiences, or professional audience targeting.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### llms-txt  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Generate and maintain llms.txt files for AI discoverability. Scans repos to create curated content maps that help AI answer engines surface your project accurately. Implements the llms.txt specification from Answer.AI.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** otomatik

### looker-studio  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Looker Studio (formerly Google Data Studio) expertise. Build dashboards, design data visualizations, connect data sources, and create marketing reports. Use when the user asks about Looker Studio, Data Studio, marketing dashboards, data visualization, report building, or connecting analytics data sources.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 60 KB (SKILL.md 14.1 KB, yük orta)
- **İnceleme:** otomatik

### mapkit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: MapKit for SwiftUI. Map view, Marker, Annotation, camera positions, map features.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 203 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### market-research  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Generate comprehensive market research reports (50+ pages) in the style of top consulting firms (McKinsey, BCG, Gartner). Professional LaTeX formatting, strategic analysis frameworks (Porter's Five Forces, PESTLE, SWOT, TAM/SAM/SOM, BCG Matrix), and deep research integration.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### maturity  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** Evaluate an organization's AI maturity on the steps of AI adoption and write a polished, shareable HTML report with evidence for each score. Use when a champion wants to know where their org or team stands, or to compare with an earlier report.
- **Teknoloji:** git, html _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** otomatik

### microsoft-ads  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Microsoft Advertising (Bing Ads) platform expertise. Audit campaigns, keywords, audiences, and UET tracking. Use when the user asks about Microsoft Ads, Bing Ads, search advertising on Microsoft, LinkedIn audience targeting, or Performance Max campaigns on Microsoft.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 56 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### mine-community  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Harvest a founder community (a subreddit, a forum, a newsletter archive) for what is actually working in app marketing, pricing, ASO and growth, then filter it honestly and file the few findings worth keeping. Drops milestone and promotional posts, keeps only claims that either converge with an unrelated source or contradict something the project already believes, and ranks the survivors against t
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.5 KB, yük orta)
- **İnceleme:** otomatik

### morning-plant-pulse  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Runs the overnight chain that has the morning production report waiting before anyone asks for it: joins last night's planning, production and maintenance exports, flags the mismatched keys, then computes output against plan, OEE with its three components, downtime ranked two ways, priced losses and the exceptions needing a decision. Stores a record per production day and keeps one Operations Comm
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 221 KB (SKILL.md 21.0 KB, yük orta)
- **İnceleme:** otomatik

### motion-design@howseen-ai  ·  howseen-ai/claude-motion-design @ 3d90d34  ·  puan 70 (B)

- **Ne yapar:** Code-only motion design pipeline (no After Effects) for Raphaël / Howseen: launch films, showreels, product promos, LinkedIn/X videos, meme clips. Use when asked to make a motion design video, a promo/launch film, a showreel, \"remake this video\", a video from a prompt (e.g. \"make a 15s motion graphics video…\"), to change a video's music/SFX, or to prepare memes for posts. Covers the brief → be
- **Teknoloji:** canvas, css, ffmpeg, gsap, html, lottie, motion, next.js, node, playwright, python, react, remotion, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** howseen-ai (kurum, ★894, son güncelleme 2026-10-04, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 72 KB (SKILL.md 33.1 KB, yük buyuk)
- **İnceleme:** otomatik

### ncr-writeup  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Writes the nonconformance report: what was found and measured, the specific requirement it violates cited to its document and locator, how many parts are actually suspect and why that scope rather than a narrower one, and where every one of them physically is across all five locations. Searches prior NCRs and CAPAs at the moment of writing and reports whether the earlier fix held. Where containmen
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** otomatik

### od-next-media-inputs  ·  nexu-io/open-design @ e033aad  ·  puan 97 (A)

- **Ne yapar:** Prepare required media inputs within an existing OD Next plan. Reuse capability evidence, acquire and measure assets efficiently, and resolve asynchronous jobs without removing required content or weakening quality standards.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★109313, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### office-hours  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Set up and run Claude Code office hours, including the calendar event when the champion's own calendar connector allows it. Use when a champion wants a regular time for teammates to bring problems.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### onboarding@anthropics  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Sets the plugin up for one plant on first run. Asks which ERP, CAD, CMMS and document system the plant uses and tests the four supported connectors (Microsoft 365, Oracle NetSuite, Infor M3, Autodesk Fusion), takes a bulk drop of the plant's own documents so it asks only what they don't answer, profiles the export folder, and runs the time interview with a clock-skew check. Also captures vocabular
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 86 KB (SKILL.md 26.5 KB, yük buyuk)
- **İnceleme:** otomatik

### one-time-surface  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Build or check a surface that is meant to appear once and then stop, such as a coach mark, tooltip, tour, primer, upsell card or review ask. Covers the three questions that decide whether it works for real people, not just on your phone, plus the traps that silently take it to zero. Use when adding a hint or one time card, when one is not appearing, when one keeps reappearing, or before shipping a
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### patterns  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** Find patterns worth sharing from recent PRs and repo history, both repeats to fix and good practices worth spreading. Use when a champion wants to know what the team should reuse or learn from.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.7 KB, yük orta)
- **İnceleme:** otomatik

### photosui  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: PhotosUI. Query for PhotosPicker, PHLivePhotoView, photo selection.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 143 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### plugin-settings  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown 
- **Teknoloji:** git, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### plugin-settings@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 80 (A)

- **Ne yapar:** Claude Code eklentilerinde kullanıcıya özel ayar ve durum saklama kalıbı: proje kökünde `.claude/<eklenti>.local.md` dosyası (YAML frontmatter + Markdown gövde); hook betiklerinden, komutlardan ve agent'lardan okuma, frontmatter ayrıştırma teknikleri ve geçici aktif hook, agent durum yönetimi gibi kalıplar.
- **Ne zaman:** Proje başına açılıp kapatılabilen ya da yapılandırılabilen bir Claude Code eklentisi yazarken. · **Ne zaman değil:** Codex'te `.claude/*.local.md` dosyalarını okuyan bir mekanizma yok; aynı kalıp Codex'te skill'in kendisinin okuyacağı bir proje dosyası (örn. `.agents/<ad>.local.md`) olarak elle uygulanabilir, hook entegrasyonu kısmı uygulanamaz.
- **Teknoloji:** claude-code, yaml, bash
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-plugin-yapisi → tamamlayıcı · **Roller:** skill-gelistirici
- **Boyut:** 43 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar ama iyi örneklenmiş bir kalıp; plugin-structure ile birlikte kullanılır.

### plugin-structure  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code pl
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 73 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik

### plugin-structure@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 88 (A)

- **Ne yapar:** Claude Code eklenti mimarisi: dizin düzeni (.claude-plugin/plugin.json, commands, agents, skills, hooks, .mcp.json), manifest alanları ve bileşen yolu yapılandırması, otomatik keşif, ${CLAUDE_PLUGIN_ROOT} ile taşınabilir yollar ve dosya adlandırma kuralları.
- **Ne zaman:** Yeni Claude Code eklentisi iskeleti kurmak, bileşenleri düzenlemek, marketplace'e hazırlamak. · **Ne zaman değil:** Codex'te Claude Code eklenti biçimi (.claude-plugin/plugin.json, ${CLAUDE_PLUGIN_ROOT}) desteklenmez; bileşenler ayrı ayrı kurulur: skiller `.agents/skills/<ad>/SKILL.md`, agent'lar `.codex/agents/<ad>.toml`, MCP sunucuları `~/.codex/config.toml` [mcp_servers], özel istemler `~/.codex/prompts/`. Dizin düzeni ve adlandırma ilkeleri yine yol gösterir.
- **Teknoloji:** claude-code, json
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-plugin-yapisi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 73 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil, eklenti grubunda). plugin-dev ailesinin giriş noktası; diğer plugin-dev skilleri (komut, agent, hook, ayar, MCP) bunu tamamlar.

### port-feature  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Bring a feature you already built in another of your own repos into this project. Reads the source feature end to end (screens, state, data, tests and the source's gotchas), maps it onto this project's architecture and conventions, lists what changes and what stays behind, ports the tests, then proves it works here. Never copies secrets, env values, or the other app's names, copy or branding. Use 
- **Teknoloji:** api-anahtari, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** otomatik

### pricing-strategy  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Pricing model design, competitive positioning, value metric selection, price testing, and pricing page optimization. Use when the user asks about pricing strategy, pricing models, price testing, value-based pricing, or competitive pricing analysis.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### pro-deck-builder  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 59 (C)

- **Ne yapar:** Create polished HTML slide decks and PDF-ready documents for consulting deliverables. Uses the RRBC design system with warm light mode, dark mode cover pages, Lora/Inter/Roboto Mono typography, and data visualization palette. Trigger on 'deck', 'slides', 'presentation', 'pitch deck', 'keynote', 'report', or 'PDF'.
- **Teknoloji:** git, html, node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 55 KB (SKILL.md 24.0 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### pro-report-builder  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Create polished HTML technical reports and multi-page documents for consulting deliverables. Includes a customizable design system with dark cover page, warm cream content pages (8.5x11 portrait), professional typography, and a curated component library (KPI cards, data tables with severity coloring, callout boxes, recommendation cards, priority banners). Trigger on report, audit report, technical
- **Teknoloji:** css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 36 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** otomatik

### product-shots  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Front-door router for the product-shots ecosystem. Clarifies underspecified visual creation requests through a 4-stage state machine, injects platform visual DNA (Amazon + 7 social platforms) and industry visual DNA (7 industries), enforces a unified Negative Constraints prompt patch, then routes to one of five downstream business skills (product-shots-main-image / product-shots-detail-page / prod
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 62 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** otomatik

### product-shots-ad-creative  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Designs high-performing ad creatives across Instagram, Facebook, TikTok, LinkedIn, Google (Display / Demand Gen), YouTube, Pinterest, and X/Twitter — locking platform dimensions, safe zones, text overlay policy, character limits, industry visual DNA, ad objective hierarchy, composition patterns, CTA strategy, and prompt sanitation. Use when the user says "create an ad", "design an ad creative", "m
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 103 KB (SKILL.md 17.0 KB, yük orta)
- **İnceleme:** otomatik

### product-shots-detail-page  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Designs Amazon A+ Content (formerly Enhanced Brand Content) — the 8 module suite that appears below the standard product carousel for Brand Registered sellers. Covers Hero Banner (21:9 / 2388×1024), Pain Points / Selling Points / Technology / Data / How-to-Use / Variants (3:2 / 1536×1024), and Endorsement (21:9), with mobile safe-area rule, 30pt text floor, and cross-module consistency anchored to
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### product-shots-image-gen  ·  motiful/product-shots @ 063c508  ·  puan 67 (B)

- **Ne yapar:** Unified image-generation engine for the product-shots ecosystem. Dispatches to the right model family (OpenAI gpt-image-2 / Gemini gemini-3-pro-image-preview Nano Banana Pro) with one parameterised script for text-to-image and image-to-image. Primary backend: OmniMaaS / Cloubic gateway (https://api.omnimaas.com/v1); also supports any OpenAI-SDK-compatible gateway via fallback env vars. Auto-resize
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 59 KB (SKILL.md 16.7 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### product-shots-main-image  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Designs Amazon-compliant main product images and the 7 secondary image types (Infographic / Multi-angle / Detail Shot / Lifestyle / Variants / What''s in Box / Size Reference) — with platform-mandatory main-image rules, conversion-rate-tuned secondary types per product category, and multi-image consistency anchored to the main image URL. Use when the user says "Amazon main image", "亚马逊主图", "produc
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 11.4 KB, yük orta)
- **İnceleme:** otomatik

### product-shots-multi-angle  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Generates 9 consistent multi-angle fashion-editorial portraits from a single reference image, with locked identity (face/skin/eyes), preserved hairstyle structure, faithful outfit/accessories, and a unified photography style across all frames. Use when the user says "multi-angle", "multi-angle shots", "九连拍", "多角度九连拍", "9-angle portraits", "fashion lookbook", "model consistency series", "consistent
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 12.5 KB, yük orta)
- **İnceleme:** otomatik

### product-shots-social-post  ·  motiful/product-shots @ 063c508  ·  puan 69 (B)

- **Ne yapar:** Designs social-platform-native visuals (Feed, Story, Reel, Carousel formats) for Instagram, TikTok, Facebook, Pinterest, RedNote, LinkedIn, X/Twitter and other social platforms — with platform-correct dimensions, safe zones, industry visual DNA, engagement hooks, and cross-slide consistency. Use when the user says "social post", "Instagram post", "IG post", "TikTok post", "Facebook post", "Pintere
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiful (kurum, ★154, son güncelleme 2026-06-08, lisans MIT)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 12.0 KB, yük orta)
- **İnceleme:** otomatik

### programmatic-seo@thatrebeccarae  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Template-based page generation at scale for SEO. Data-driven content, internal linking architecture, and automated optimization for large-scale content operations. Use when the user asks about programmatic SEO, pSEO, scaled content, template pages, or automated page generation.
- **Teknoloji:** git, next.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 8 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### quote-build  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Produces the make-to-order quote from the intake form, comparable prior jobs and cost history, with every number traced to where it came from — material at the price actually paid on a named purchase order, machine hours per operation from a labelled ladder (current routing, closed-job actuals, the confirmed design, first principles) with setup and run kept apart, setup re-amortized at each quanti
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 58 KB (SKILL.md 28.0 KB, yük buyuk)
- **İnceleme:** otomatik

### reference-hunt  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Find how real, shipped apps solve a given screen or flow, so the design starts from patterns people actually use instead of the AI's average guess. Searches Mobbin when it is connected, otherwise works from the user's own screenshots and App Store listing screenshots. Gives the 3 best patterns in chat, each linked to the real screen and marked seen or unconfirmed, and saves a dated reference card 
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** otomatik

### repo-health  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** One-command GitHub repository health audit. Checks for missing standard files, GitHub configuration, branch protection, documentation quality, and code hygiene. Produces a scored health report with prioritized fix recommendations.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### repo-scaffold  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Initialize GitHub repositories with standard files and configuration. Generates LICENSE, CONTRIBUTING.md, SECURITY.md, issue/PR templates, CI config, and .gitignore. Detects project type and adapts templates accordingly.
- **Teknoloji:** git, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### research-digest  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Generate structured research briefs from RSS feeds and web sources on any topic. Synthesizes multiple sources into actionable analysis with key findings, data points, expert perspectives, and content angles.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### research@namedtoaster  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Answer a question by searching the project's own docs and code first, then official sources, and file the dated, sourced answer where it will be read again. Adds to an existing doc before creating a new one, marks anything unverified, and keeps a one line summary with the headline finding in the rules file's Docs index. Gives a short answer in chat first. Use when the user asks to research, look i
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 7 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### retention-churn-prevention  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Customer retention analysis, churn prediction, cohort analysis, win-back campaigns, and loyalty program design. Use when the user asks about churn, retention, customer lifetime value, cohort analysis, or win-back strategies.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### reverse-any-video  ·  heygen-com/hyperframes @ 925cea1  ·  puan 97 (A)

- **Ne yapar:** Herhangi bir videoyu (motion graphics, konuşan kafa, canlı çekim, AI üretimi) birebir kare karşılaştırmasıyla düzenlenebilir bir HyperFrames projesine yeniden kurar: kesim noktalarını `measure cuts` ile bulur, bileşenleri HTML olarak yeniden yazar, görüntüdeki kişileri HeyGen ile yeniden çeker, bulutta render alıp `diff` ile özgün videoya karşı doğrular ve REVERSE.md yazar.
- **Ne zaman:** Bir videoyu kopyalayıp/yeniden yapıp düzenlenebilir proje olarak elde etmek; elinde hakkı olan bir videonun kare kare eşi gerekiyorsa. · **Ne zaman değil:** Sıfırdan yeni video (hyperframes); yalnızca bir stilin yeni konuya uygulanması (style-sampling ya da hyperframes look.md); Pro plan yoksa (başlamaz).
- **Teknoloji:** hyperframes, html, gsap, ffmpeg, node 22+ · **Paketler:** hyperframes (npx), node>=22, ffmpeg, HyperFrames Pro hesabı, HeyGen (kişi yeniden çekimi)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★89524, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı
- **Boyut:** 23 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — HyperFrames Pro özelliği: plan yoksa `reverse start` reddeder, skill yükseltme bağlantısını verir ve billing komutunu kullanıcıya bıraktırır. Ekrandaki kişileri fiyat söylemeden HeyGen ile yeniden çeker (kredi harcar) ve son render bulutta. Disiplinli doğrulama döngüsü (cuts, frame-range, diff) kaliteli. Başlangıç telemetri işareti (skill adı, hesaba bağlı) var; yalnızca hakkı olunan videolar için. Not: kategori otomatik atamayla yazılım-skill-yazımı altında; içeriği video üretimi.

### rfq-to-quote  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the plant can build, drafts the questions back, returns a provisional bid/no-bid, pulls cost history, routings and closed-job actuals, builds an internal estimating model in Fusion where connected (from the drawing, a prior part's model saved as new, text specs as a ROM only, or a STEP file), d
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 19.1 KB, yük orta)
- **İnceleme:** otomatik

### root-cause-capa  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timeline, runs the pattern checks in code rather than by eye — SPC drift, clustering by lot, shift, operator, machine and tool change, correlation with a maintenance event — then proposes ranked candidate causal chains, each with the evidence for it, the evidence against it, and the test that wou
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 22.2 KB, yük orta)
- **İnceleme:** otomatik

### routines  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** Set up recurring champion routines as Claude Code scheduled tasks. Use when a champion wants work like a weekly patterns digest, a stale guidance check, or a monthly lead update to happen without kicking it off by hand.
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.3 KB, yük orta)
- **İnceleme:** otomatik

### run-project  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when explicitly asked to set up, review or run a project board, select its next eligible ticket, or drain its authorized work.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 686 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### saas-motion-video  ·  tugrawork-creator/saas-motion-kit @ bc7a414  ·  puan 67 (B)

- **Ne yapar:** Make a promo / motion video for a software product with HyperFrames, using the saas-motion-kit 7-stage process (brief → components → theme → storyboard → build → sound → deliver), the clean-or-imaginary component rule, the creative muscle (tone matrix, variety rules, component forge, transition atlas, variety audit) and the 101-theme gallery in docs/. Use when someone asks for a launch video, prod
- **Teknoloji:** css, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tugrawork-creator (kisi, ★295, son güncelleme 2026-10-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### safe-push  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Pre-push hygiene check for GitHub repositories. Scans for PII, secrets, and sensitive data before pushing. Audits commit messages, enforces repo-specific blocklists, and rate-limits pushes to avoid GitHub abuse detection. Use before any git push, especially to public repos.
- **Teknoloji:** api-anahtari, git, html, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** otomatik

### schema-markup-generator  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Generate structured data markup (JSON-LD) for rich results, AI search visibility, and enhanced SERP features. Supports Article, FAQ, HowTo, Product, Review, LocalBusiness, Event, BreadcrumbList, Person, Organization, and more. Use when the user needs schema markup, structured data, rich snippets, JSON-LD, or wants to improve search appearance.
- **Teknoloji:** git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** otomatik

### screen-atlas  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Build a browsable catalogue of every screen in the app, captured from a running build and grouped into the journeys people actually walk, so you can see what each flow does without opening the app. Finds screens nothing navigates to as a side effect. Use when the user says they cannot picture how the app flows, wants a Mobbin for their own app, asks for screenshots of every screen, wants to review
- **Teknoloji:** css, html, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### search-pages  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Build the pages that get an app found in search, picking the topics from real search data and a check of who currently ranks rather than from taste. Puts the blog on the app's own domain, ships schema and a sitemap with the first post, and writes the comparison pages that actually pull traffic instead of the explainer pages that do not. Use when the user wants a blog, SEO, organic traffic, content
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.5 KB, yük orta)
- **İnceleme:** otomatik

### see-it-work  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 71 (B)

- **Ne yapar:** Prove a change to an Expo app or a website works by seeing it, not by trusting a passing test. Picks which layer proves this change (component test, seeded simulator screenshot, smoke case, release build smoke run, browser preview, end to end journey), runs it, and shows the evidence. Use after any UI, navigation, layout, purchase or deep link change, before saying something is fixed or done, and 
- **Teknoloji:** playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### seo-content-writer  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** SEO-optimized content creation with brand voice analysis and platform-specific frameworks. Covers blog posts, social media, email marketing, and landing pages. Includes keyword integration, readability optimization, and performance metrics.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### session-end  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Wrap up a working session automatically. Runs the project's checks, adds manual test items to the release checklist, records new gotchas and decisions, updates the handoff file and docs, checks progress against the current goal, commits only this session's files and pushes. Use when the user says they are done, wrapping up, or asks to end the session.
- **Teknoloji:** api-anahtari, git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### set-goals  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Write or renew the project's 6 week goal in GOALS.md, and close the previous cycle in a few lines drafted from git history. Walks the stages from a working loop on your phone, into the stores, to the first 100 weekly users and beyond, each with a default goal to edit. Use when the user says "set my goal", "new cycle", "what should I focus on", "my goal ended", or when session end has said the curr
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 5.8 KB, yük kucuk)
- **İnceleme:** otomatik

### setup@namedtoaster  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Interview the user one question at a time and write the project's rules file, goals file, handoff file and release checklist. Use when starting a new app, adopting The Last Mile in an existing project, or when the user asks to set up or redo their project rules.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 9 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### shepherd  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when asked to shepherd, babysit, monitor, or poll open pull requests or merge requests, including triaging review feedback, CI failures, and routine follow-up.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 42 KB (SKILL.md 7.8 KB, yük kucuk)
- **İnceleme:** otomatik

### ship  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Take any mobile app, on any stack, from a working build to the App Store and Google Play. Works out the stack, sweeps the code for known rejection traps, fixes what it can, bumps the version, builds and tests the release, writes the store listing and privacy answers, uploads and submits with the user's yes, and handles rejections. Works for Expo, React Native, Flutter, native iOS and Android, Capa
- **Teknoloji:** api-anahtari, git, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 168 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** otomatik

### shopify  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Shopify e-commerce platform marketing expertise. Audit store performance, optimize conversion funnels, configure tracking, and integrate marketing tools. Use when the user asks about Shopify, e-commerce optimization, Shopify analytics, store conversion, product feeds, or Shopify app integrations.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 79 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** otomatik

### shopify-theme-audit  ·  tanujrajputdev/shopify-theme-audit-skill @ df4992f  ·  puan 76 (B)

- **Ne yapar:** Audit a Shopify theme (Online Store 2.0 or 1.0) for performance, Core Web Vitals, accessibility, conversion, third-party app overhead, SEO, AEO and GEO, and return a scored report with file paths, line numbers and working Liquid fixes. Use when the user asks to audit or review a Shopify theme or its Liquid sections and snippets, find out why a store is slow, check for deprecated Shopify APIs, chec
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tanujrajputdev (kisi, ★47, son güncelleme 2026-11-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 213 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik

### skill-creator@anthropics  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 98 (A)

- **Ne yapar:** Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- **Teknoloji:** html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 220 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** otomatik

### skill-creator@anthropics-2  ·  anthropics/skills @ e4bb5d9  ·  puan 95 (A)

- **Ne yapar:** Skill oluşturma, iyileştirme ve ölçme: niyet yakalama ve görüşme, SKILL.md yazım rehberi (aşamalı açılım, sürpriz olmama ilkesi), test istemleriyle skill'li/skill'siz çalıştırma, değerlendirici/karşılaştırıcı/analizci agent'lar, eval görüntüleyici, benchmark ve varyans analizi, açıklama (tetikleme) optimizasyonu ve paketleme betikleri.
- **Ne zaman:** Yeni skill yazmak ya da mevcut skill'i ölçülebilir biçimde iyileştirmek (tetikleme doğruluğu dahil). · **Ne zaman değil:** Claude Code eklentisine özgü yerleşim için skill-development'ı da oku. Eval döngüsü `claude -p` ile alt süreç çalıştırır; Codex'te bu adımlar `codex exec` ile değiştirilmeli ya da test istemleri elle çalıştırılmalı — yazım rehberi ve betiklerin çoğu (quick_validate, package_skill) araçtan bağımsız çalışır.
- **Teknoloji:** python, markdown · **Paketler:** python3, claude CLI (eval döngüsü için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★199922, son güncelleme 2026-11-16, lisans yok)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 220 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Dört sürüm arasında en güncel ve tek ölçme/eval altyapısı olan Anthropic resmi sürüm. heyitsnoah kopyası bununla aynı (yalnızca NOTICE/LICENSE farkı); composiohq ve freshtechbro eski 'init_skill + package' sürümü. writing-skills tamamlayıcı (baskı testi/TDD yaklaşımı).

### skill-creator@freshtechbro  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 49 (D)

- **Ne yapar:** skill-creator'ın eski sürümünün freshtechbro/claudedesignskills kopyası: skill anatomisi, aşamalı açılım ve init/package betikli 6 adımlı süreç.
- **Ne zaman:** Güncel sürüme erişilemiyorsa yedek. · **Ne zaman değil:** Varsayılan olarak kullanma; composiohq kopyasıyla aynı içerik, anthropics/skill-creator güncel.
- **Teknoloji:** python, markdown · **Paketler:** python3
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1442, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 39 KB (SKILL.md 11.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Eski sürümün ikinci kopyası; ek değer yok (MIT lisanslı olması tek fark).

### skill-creator@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 61 (C)

- **Ne yapar:** Anthropic skill-creator'ın güncel sürümünün claudesidian içindeki birebir kopyası (eval görüntüleyici, değerlendirici agent'lar, benchmark ve açıklama optimizasyonu dahil); NOTICE.md ile lisans notu eklenmiş.
- **Ne zaman:** claudesidian kasası içinde skill geliştirirken (kasa bu kopyayı bekler). · **Ne zaman değil:** Diğer projelerde; anthropics/skill-creator ile aynı içerik.
- **Teknoloji:** python, markdown · **Paketler:** python3, claude CLI (eval döngüsü için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2615, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 221 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İçerik resmi sürümle aynı; çift kurulum bağlamı boşa harcar.

### skill-development  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.
- **Teknoloji:** html, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** otomatik

### skill-development@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 72 (B)

- **Ne yapar:** Claude Code eklentileri için skill yazım rehberi: skill anatomisi, aşamalı açılım, örnekle anlama → içerik planlama → yapı oluşturma → SKILL.md düzenleme adımları; eklentideki skills/ dizinine yerleştirme, üçüncü şahıs açıklama ve tetikleme ifadeleri, doğrulama kontrol listesi.
- **Ne zaman:** Bir Claude Code eklentisinin içine skill eklemek (plugin-dev akışı içinde). · **Ne zaman değil:** Bağımsız skill yazımı ve ölçümü için skill-creator birincil. Codex'te: eklenti yerleşimi (plugins/<ad>/skills/) ve ${CLAUDE_PLUGIN_ROOT} geçerli değil — skill'i doğrudan `.agents/skills/<ad>/SKILL.md` olarak yaz; SKILL.md yazım ilkeleri (frontmatter name/description, aşamalı açılım) Codex'te de aynen geçerli.
- **Teknoloji:** claude-code, markdown
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 34 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İçeriğin çoğu eski skill-creator metninden türetilmiş (22 KB); eklentiye özgü kısım ince. writing-skills ve skill-creator varken ek değeri düşük.

### skillify  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Tekrar eden çok adımlı iş akışlarını yeniden kullanılabilir SKILL.md'ye dönüştürür: kalıbı tanımla, şablondan SKILL.md üret, yerleştir, doğrula; adlandırma kuralları ve kalite kontrol listesi.
- **Ne zaman:** 'Bunu skill yap' dendiğinde ya da aynı iş 3+ kez tekrarlandığında hızlı skill çıkarımı. · **Ne zaman değil:** Ölçülebilir, test edilmiş skill gerekiyorsa (skill-creator, writing-skills). Şablon when_to_use/allowed-tools/effort gibi ag-kit/Claude Code'a özgü alanlar üretir; Codex için yalnızca name + description bırak.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa ve pratik 'iş akışından skill' tarifi; doğrulama yüzeysel.

### social-media-strategy  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Platform-specific organic social media strategy, content calendars, engagement tactics, community building, and performance measurement. Use when the user asks about social media strategy, organic social, content calendars, community management, or social media metrics.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 4.8 KB, yük kucuk)
- **İnceleme:** otomatik

### social-preview  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Generate Open Graph social preview images (1280x640) for GitHub repositories. Creates branded OG images that display when repos are shared on Twitter, LinkedIn, and Slack. Supports custom templates, dark/light themes, and automated generation.
- **Teknoloji:** canvas, css, git, html, node, playwright, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### sqlx4k  ·  smyrgeorge/sqlx4k @ 2887585  ·  puan 80 (A)

- **Ne yapar:** Write Kotlin (JVM, Android or Kotlin Multiplatform) database code with sqlx4k, the coroutine-first SQL toolkit for PostgreSQL, MySQL/MariaDB, SQLite and SQLCipher: Gradle setup, @Table entities, @Repository interfaces with compile-time validated @Query methods, transactions, migrations and error handling. Use when a project depends on sqlx4k (io.github.smyrgeorge:sqlx4k-*, the io.github.smyrgeorge
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** smyrgeorge (kisi, ★323, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 10.0 KB, yük orta)
- **İnceleme:** otomatik

### store-listing  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 76 (B)

- **Ne yapar:** Write the App Store and Google Play listing from evidence instead of taste. Picks keywords by checking who already owns each phrase and whether a small app can win it, spends the name and subtitle on one lane, writes the descriptions and the first three screenshot captions, finds a screenshot look to copy from real listings, and keeps a dated keyword file so every later change can be measured. Use
- **Teknoloji:** node, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** otomatik

### storekit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: StoreKit 2. Product, Transaction, subscriptions, StoreView, SubscriptionStoreView.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 390 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### style-sampling  ·  heygen-com/hyperframes @ 925cea1  ·  puan 97 (A)

- **Ne yapar:** Hazır video stil şablonlarından (Collage Explainer, Finance Explainer, Animated Science Explainer, 3D Brand Explainer, 3D True Crime) birini seçip kullanıcının konusunda yeni bölüm üretir: `hyperframes templates pull <slug>` ile şablonu çeker, REMIX.md sürecini izler; storyboard ve taslak onayları kullanıcıya aittir.
- **Ne zaman:** Kanıtlanmış bir seri stilinde (açıklayıcı, finans, bilim, marka, true-crime) bölüm yapmak; 'şu stilde bir bölüm' istekleri. · **Ne zaman değil:** Tek bir videoyu kopyalamak (reverse-any-video); beş şablon dışında bir stil (hyperframes look.md ile); Pro plan yoksa (şablon çekilmez).
- **Teknoloji:** hyperframes, html, gsap, node 22+ · **Paketler:** hyperframes (npx), node>=22, HyperFrames Pro hesabı
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★89524, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı
- **Boyut:** 16 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Şablonlar HyperFrames Pro özelliği (Free planda çekilmez; skill kullanıcıdan billing komutunu kendisinin çalıştırmasını ister). Şablon çekimi kredi harcamaz; üretilen medya media-use kredi kuralına tabi. Yaratıcılara teşekkür notu var; kişi yüzü/sesi/logosu kullanılmaması kuralı net. Başlangıç telemetri işareti (hesaba bağlı) var.

### subagent-delegation  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when the user invokes the subagent delegation playbook, or the user's instructions direct its use when delegating work or deciding whether to delegate.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 5.1 KB, yük kucuk)
- **İnceleme:** otomatik

### supplier-escape-to-alternate-source  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Runs the cross-area chain from a nonconformance traced to purchased material through to an alternate-source RFQ: writes the NCR and its containment, establishes root cause against the supplier rather than the process, records the corrective action, then builds the sourcing package with a response format that makes the returned bids comparable. Use when someone says \"run the supplier escape chain,
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta)
- **İnceleme:** otomatik

### supplier-quote-request  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Builds the RFQ package that goes out to suppliers — drawing and specification at the verified current revision, the demand picture, the quality clause list, commercial terms, and a mandated response format that makes the returned bids comparable by construction. Lists everything missing. Hard stops on a revision mismatch or restricted technical data. Then runs the supplier loop: candidates from th
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 57 KB (SKILL.md 22.5 KB, yük orta)
- **İnceleme:** otomatik

### swift-concurrency@prisma-labs-dev  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Swift Concurrency. async/await, Task, TaskGroup, actors, AsyncSequence, AsyncStream, continuations.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 74 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### swift-testing@prisma-labs-dev  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: Swift Testing framework. @Test, @Suite, #expect, #require, traits, parameterized tests, migrating from XCTest.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 87 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** otomatik

### swiftdata  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: SwiftData. Query for @Model, ModelContext, @Query, schema migrations.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 126 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### swiftui  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: SwiftUI. Query for views, layouts, navigation, @State/@Binding/@Observable, view modifiers, NavigationStack, iOS 26+ features.
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4314 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** otomatik

### sync  ·  namedtoaster/The-Last-Mile @ c31b1cf  ·  puan 78 (B)

- **Ne yapar:** Bring this project's copy of The Last Mile skills up to date, then commit and push it, so the next session on any device has the latest skills. Works from the phone, nothing to run by hand. Use when the user says "sync", "update the skills", "get the latest Last Mile", or a Last Mile change they just made is missing here.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** namedtoaster (kisi, ★41, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** otomatik

### sync-repos  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Manage public/private repository pairs. Verify parity, detect drift, run sync scripts, and validate no sensitive data leaks to the public repo. Use for projects that maintain separate dev and public repositories.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### tech-diagram  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Generate technical architecture diagrams, pipeline flows, layer/stack diagrams, and system illustrations as standalone HTML files. Uses a dark-mode design system with embedded CSS and inline SVG. Use when the user needs architecture diagrams, system illustrations, flow charts, or technical visualizations.
- **Teknoloji:** canvas, css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### technical-seo-audit  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 61 (C)

- **Ne yapar:** Deep technical SEO auditing covering crawlability, indexation, Core Web Vitals, site architecture, canonicalization, structured data validation, and performance optimization. Use when the user asks about technical SEO, site audits, crawl issues, indexation problems, Core Web Vitals, page speed, or site architecture optimization. For content-focused SEO, see the seo-content-writer skill.
- **Teknoloji:** css, git, next.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 8.4 KB, yük orta)
- **İnceleme:** otomatik

### tiktok-ads  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** TikTok Ads platform expertise. Audit campaigns, creative strategy, audience targeting, Spark Ads, TikTok Shop integration, pixel/Events API setup, and performance optimization. Use when the user asks about TikTok advertising, short-form video ads, TikTok Shop, Spark Ads, or social commerce advertising.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** otomatik

### tipkit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: TipKit. Tip protocol, TipView, PopoverTipView, Tips.configure, inline and popover tips.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 62 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik

### to-plan  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when asked for an implementation plan or execution contract for one or more tracker items or an in-chat task, including a read-only review of the next safe step, without drafting or provider access, when the source or contract is incomplete, or a retained approved tracker plan has an existing amendment chain or a changed published integration decision needing durable consumption.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 443 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### trade-study-report  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 100 (A)

- **Ne yapar:** Turns a filled-in trade study matrix and its analysis results into a scored comparison and a decision memo, with every score cited to its source. Runs the sensitivity analysis every time — where the winner flips, which criterion the decision actually rests on, whether an option never wins under any plausible weighting — because a recommendation with no sensitivity check is a spreadsheet, not a dec
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** otomatik

### uikit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: UIKit. Query for UIView, UIViewController, controls, table and collection views, navigation controllers, scenes, Auto Layout, images, colors, gestures, presentation, and SwiftUI hosting.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2434 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik

### usernotifications  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: UserNotifications. Query for local/remote notifications, triggers, notification content.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 73 KB (SKILL.md 0.9 KB, yük kucuk)
- **İnceleme:** otomatik

### using-chrisbanes-skills  ·  chrisbanes/skills @ efeb99d  ·  puan 84 (A)

- **Ne yapar:** Use when routing Kotlin or Jetpack Compose work, or physical Android benchmark evidence that needs a configuration decision, especially when several Kotlin or Compose concerns overlap.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** chrisbanes (kisi, ★1166, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** otomatik

### utm-attribution-strategy  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** UTM parameter strategy, campaign tracking, and marketing attribution modeling. Build consistent UTM taxonomies, configure attribution models, measure cross-channel performance, and connect marketing spend to revenue. Use when the user asks about UTM parameters, campaign tracking, attribution models, marketing measurement, or cross-channel analytics.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### wasted-spend-finder  ·  thatrebeccarae/claude-marketing @ a8a63ec  ·  puan 63 (C)

- **Ne yapar:** Systematic analysis of Google Ads and Meta advertising spend to identify wasted budget. Produces actionable exclusion lists with thematic categorization and statistical validation. Use when onboarding new accounts, performing monthly hygiene, or preparing for budget optimization.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** thatrebeccarae (kisi, ★216, son güncelleme 2026-05-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### widgetkit  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: WidgetKit. Query for widget timelines, entries, providers, home/lock screen widgets.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 70 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-hookify-rules  ·  anthropics/claude-plugins-official @ 73c8cf3  ·  puan 96 (A)

- **Ne yapar:** This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
- **Teknoloji:** api-anahtari, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★48119, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### writing-hookify-rules@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 80 (A)

- **Ne yapar:** hookify eklentisi için kural yazımı: `.claude/hookify.<kural>.local.md` dosyalarında YAML frontmatter (name, enabled, event: bash/file/stop/prompt/all, pattern, action: warn/block) ve Claude'a gösterilecek mesaj; çoklu koşul, olay türü rehberi, regex ipuçları ve tuzaklar.
- **Ne zaman:** Kod yazmadan 'tehlikeli rm uyarısı', 'console.log engelle' gibi hızlı koruma kuralları eklemek (hookify kuruluysa). · **Ne zaman değil:** hookify eklentisi kurulu değilse; karmaşık mantık gerekiyorsa hook-development. Codex'te hookify yok: aynı korumalar Codex'in sandbox/onay politikasıyla (`~/.codex/config.toml`), AGENTS.md'deki yasak komut listesiyle ya da git pre-commit hook'uyla sağlanır; kuralın regex'i ve mesajı bu araçlara aynen taşınabilir.
- **Teknoloji:** claude-code, yaml, regex · **Paketler:** hookify Claude Code eklentisi
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★156944, son güncelleme 2026-11-24, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-hook → alternatif · **Roller:** skill-gelistirici
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif, hook grubunda). Anthropic resmi; kısa ve örnekli. hook-development'ın kod gerektirmeyen hafif alternatifi.

### writing-skills  ·  obra/superpowers @ 22f0b46  ·  puan 100 (A)

- **Ne yapar:** Skill yazımını süreç dokümantasyonuna uygulanmış TDD olarak ele alır: önce alt-agent'larla baskı senaryosu çalıştırıp skill'siz başarısızlığı gözle (RED), skill'i yaz (GREEN), açıkları kapat (REFACTOR). Skill türleri, yapı, keşfedilebilirlik (SDO), ikna ilkeleri ve Anthropic en iyi uygulamaları ekleri içerir.
- **Ne zaman:** Agent davranışını değiştiren süreç/disiplin skillerini yazmak ve gerçekten işe yaradığını kanıtlamak. · **Ne zaman değil:** Basit başvuru/format skilleri için ağır (skill-creator yeterli). superpowers:test-driven-development'ı ön koşul sayar. Codex'te: alt-agent baskı testleri ayrı `codex exec` oturumlarıyla yapılır; skill yolu `~/.agents/skills/` (skill bunu kendisi belirtir).
- **Teknoloji:** markdown, graphviz · **Paketler:** graphviz (isteğe bağlı, render-graphs.js için node)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★325731, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → tamamlayıcı · **Roller:** skill-gelistirici
- **Boyut:** 107 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi: referanslar references/ altına taşındı; description kuralı (sadece 'ne zaman', iş akışını özetleme) daha net anlatılıyor; SKILL.md 300 satır kısaldı. Agent Skills standardıyla uyumlu.

### xcuitest  ·  Prisma-Labs-Dev/apple-skills @ 4986260  ·  puan 80 (A)

- **Ne yapar:** API reference: XCUITest. Query for element queries, waiting patterns, Swift 6 @MainActor, assertions, screenshots, launch arguments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Prisma-Labs-Dev (kurum, ★360, son güncelleme 2026-09-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 192 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### yao-meta-skill  ·  yaojingang/yao-meta-skill @ 49ce5f2  ·  puan 83 (A)

- **Ne yapar:** Create, improve, or evaluate an existing skill from workflows, prompts, SOPs, scripts. Use for migration/release/package, routing, evals/tests, install/trust checks, 优化已有 skill, 补 trigger 评测. Exclude summary/translation/docs, brainstorming, one-off prompts, copy-only edits, outline-only requests.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** yaojingang (kisi, ★2742, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3181 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik
