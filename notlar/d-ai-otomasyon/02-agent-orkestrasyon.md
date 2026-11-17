# 02-agent-orkestrasyon — AI ve Otomasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **14/269**

### add-model-descriptions  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Add descriptions for new models from the HuggingFace router to chat-ui configuration. Use when new models are released on the router and need descriptions added to prod.yaml and dev.yaml. Triggers on requests like "add new model descriptions", "update models from router", "sync models", or when explicitly invoking /add-model-descriptions.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-adaptive-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for adaptive-coordinator - invoke with $agent-adaptive-coordinator
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-agent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Agent skill for agent - invoke with $agent-agent
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 24.6 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-agentic-payments  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for agentic-payments - invoke with $agent-agentic-payments
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-app-store  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for app-store - invoke with $agent-app-store
- **Teknoloji:** api-anahtari, react, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-arch-system-design  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for arch-system-design - invoke with $agent-arch-system-design
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-architecture@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for architecture - invoke with $agent-architecture
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik
- **Not:** Aynı adlı başka skill: `agent-architecture` (github/awesome-copilot) yapay zekâ AJANI mimarisi tasarlar ve denetler. Bu skill yazılım SİSTEM mimarisi ajanıdır (SPARC mimari aşaması); işler farklı, çıplak ad eski kayıtta kalır.

### agent-authentication  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for authentication - invoke with $agent-authentication
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-automation-smart-agent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for automation-smart-agent - invoke with $agent-automation-smart-agent
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-base-template-generator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for base-template-generator - invoke with $agent-base-template-generator
- **Teknoloji:** react, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-byzantine-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for byzantine-coordinator - invoke with $agent-byzantine-coordinator
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-challenges  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for challenges - invoke with $agent-challenges
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-code-goal-planner  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for code-goal-planner - invoke with $agent-code-goal-planner
- **Teknoloji:** api-anahtari, git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.0 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-coder  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for coder - invoke with $agent-coder
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-collective-intelligence-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for collective-intelligence-coordinator - invoke with $agent-collective-intelligence-coordinator
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-consensus-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for consensus-coordinator - invoke with $agent-consensus-coordinator
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-coordination  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent spawning, lifecycle management, and coordination patterns. Manages 60+ agent types with specialized capabilities. Use when: spawning agents, coordinating multi-agent tasks, managing agent pools. Skip when: single-agent work, no coordination needed.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-coordinator-swarm-init  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for coordinator-swarm-init - invoke with $agent-coordinator-swarm-init
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-crdt-synchronizer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Agent skill for crdt-synchronizer - invoke with $agent-crdt-synchronizer
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 24.6 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-data-ml-model  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for data-ml-model - invoke with $agent-data-ml-model
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-dev-backend-api  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for dev-backend-api - invoke with $agent-dev-backend-api
- **Teknoloji:** api-anahtari, git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.0 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-docs-api-openapi  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for docs-api-openapi - invoke with $agent-docs-api-openapi
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-goal-planner  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for goal-planner - invoke with $agent-goal-planner
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-gossip-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for gossip-coordinator - invoke with $agent-gossip-coordinator
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-hierarchical-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for hierarchical-coordinator - invoke with $agent-hierarchical-coordinator
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-issue-tracker  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Agent skill for issue-tracker - invoke with $agent-issue-tracker
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.3 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-load-balancer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for load-balancer - invoke with $agent-load-balancer
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-matrix-optimizer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for matrix-optimizer - invoke with $agent-matrix-optimizer
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-memory-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for memory-coordinator - invoke with $agent-memory-coordinator
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-mesh-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for mesh-coordinator - invoke with $agent-mesh-coordinator
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-migration-plan  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Agent skill for migration-plan - invoke with $agent-migration-plan
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 18.0 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-multi-repo-swarm  ·  ruvnet/ruflo @ 98ddf41  ·  puan 92 (A)

- **Ne yapar:** Agent skill for multi-repo-swarm - invoke with $agent-multi-repo-swarm
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.6 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### agent-neural-network  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for neural-network - invoke with $agent-neural-network
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-ops-cicd-github  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for ops-cicd-github - invoke with $agent-ops-cicd-github
- **Teknoloji:** api-anahtari, docker, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-orchestrator-task  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Agent skill for orchestrator-task - invoke with $agent-orchestrator-task
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-pagerank-analyzer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for pagerank-analyzer - invoke with $agent-pagerank-analyzer
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-payments  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for payments - invoke with $agent-payments
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-planner  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for planner - invoke with $agent-planner
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-pr-manager  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Agent skill for pr-manager - invoke with $agent-pr-manager
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-production-validator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for production-validator - invoke with $agent-production-validator
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.6 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-project-board-sync  ·  ruvnet/ruflo @ 98ddf41  ·  puan 92 (A)

- **Ne yapar:** Agent skill for project-board-sync - invoke with $agent-project-board-sync
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### agent-pseudocode  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for pseudocode - invoke with $agent-pseudocode
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.3 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-queen-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for queen-coordinator - invoke with $agent-queen-coordinator
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-quorum-manager  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Agent skill for quorum-manager - invoke with $agent-quorum-manager
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 27.4 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-raft-manager  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for raft-manager - invoke with $agent-raft-manager
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-refinement  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for refinement - invoke with $agent-refinement
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-repo-architect  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Agent skill for repo-architect - invoke with $agent-repo-architect
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.2 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-researcher  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for researcher - invoke with $agent-researcher
- **Teknoloji:** git, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-resource-allocator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for resource-allocator - invoke with $agent-resource-allocator
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 19.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-safla-neural  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for safla-neural - invoke with $agent-safla-neural
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-sandbox  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for sandbox - invoke with $agent-sandbox
- **Teknoloji:** api-anahtari, css, html, next.js, node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-scout-explorer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for scout-explorer - invoke with $agent-scout-explorer
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-sona-learning-optimizer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for sona-learning-optimizer - invoke with $agent-sona-learning-optimizer
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-spec-mobile-react-native  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for spec-mobile-react-native - invoke with $agent-spec-mobile-react-native
- **Teknoloji:** git, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-specification  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for specification - invoke with $agent-specification
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-swarm  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for swarm - invoke with $agent-swarm
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-swarm-issue  ·  ruvnet/ruflo @ 98ddf41  ·  puan 92 (A)

- **Ne yapar:** Agent skill for swarm-issue - invoke with $agent-swarm-issue
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### agent-swarm-memory-manager  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for swarm-memory-manager - invoke with $agent-swarm-memory-manager
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-swarm-pr  ·  ruvnet/ruflo @ 98ddf41  ·  puan 92 (A)

- **Ne yapar:** Agent skill for swarm-pr - invoke with $agent-swarm-pr
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### agent-sync-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Agent skill for sync-coordinator - invoke with $agent-sync-coordinator
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-teams-grok  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Run Ruflo-style named Agent Teams on Grok Build using the host-agnostic team bus (scripts/grok-team-bus.mjs). Use when coordinating multi-agent pipelines, feature development with architect→coder→tester→reviewer, or replacing Claude SendMessage.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-topology-optimizer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for topology-optimizer - invoke with $agent-topology-optimizer
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 24.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-trading-predictor  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for trading-predictor - invoke with $agent-trading-predictor
- **Teknoloji:** python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.6 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-user-tools  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for user-tools - invoke with $agent-user-tools
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-v3-integration-architect  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for v3-integration-architect - invoke with $agent-v3-integration-architect
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-v3-memory-specialist  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Agent skill for v3-memory-specialist - invoke with $agent-v3-memory-specialist
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.6 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-v3-queen-coordinator  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for v3-queen-coordinator - invoke with $agent-v3-queen-coordinator
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-worker-specialist  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for worker-specialist - invoke with $agent-worker-specialist
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-workflow  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Agent skill for workflow - invoke with $agent-workflow
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agent-workflow-automation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 92 (A)

- **Ne yapar:** Agent skill for workflow-automation - invoke with $agent-workflow-automation
- **Teknoloji:** docker, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### agentdb-advanced  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Master advanced AgentDB features including QUIC synchronization, multi-database management, custom distance metrics, hybrid search, and distributed systems integration. Use when building distributed AI systems, multi-agent coordination, or advanced vector search applications.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agentdb-learning  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Create and train AI learning plugins with AgentDB's 9 reinforcement learning algorithms. Includes Decision Transformer, Q-Learning, SARSA, Actor-Critic, and more. Use when building self-learning agents, implementing RL, or optimizing agent behavior through experience.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.6 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agentdb-memory-patterns  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Implement persistent memory patterns for AI agents using AgentDB. Includes session memory, long-term storage, pattern learning, and context management. Use when building stateful agents, chat systems, or intelligent assistants.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agentdb-optimization  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Optimize AgentDB performance with quantization (4-32x memory reduction), HNSW indexing (150x faster search), caching, and batch operations. Use when optimizing memory usage, improving search speed, or scaling to millions of vectors.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agentdb-query  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Query AgentDB through the controller bridge -- semantic routing, hierarchical recall, causal graphs, context synthesis, pattern store/search
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agentdb-vector-search  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Implement semantic vector search with AgentDB for intelligent document retrieval, similarity matching, and context-aware querying. Use when building RAG systems, semantic search engines, or intelligent knowledge bases.
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.8 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### agntcy-status  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Show AGNTCY/SLIM/CASA integration status: whether the SLIM runtime is installed, an endpoint configured, which transport is default, and what the agntcy mod saw this session. Use when the user asks whether AGNTCY is configured. Read-only; no network call.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### analyze-app  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Statically inspect a local JavaScript or Electron app you are authorized to study and explain how a feature works with file+line evidence. Use when the user wants to understand or reimplement a feature from an app whose source they have. Parses only; never executes the target.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### autopilot-loop  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run an autonomous /loop iteration -- check progress, work on next task, schedule next wake
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### autopilot-predict  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Use learned patterns and current state to predict the optimal next action
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### batch-operations  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Birçok dosyaya aynı değişikliği güvenle uygulama protokolü: deseni tanımla, önce grep ile etkilenen dosyaları önizle, toplu uygula, sonra doğrula (sayım, derleme, test). Yeniden adlandırma, import ekleme, sürüm güncelleme gibi yaygın kalıplar ve güvenlik kuralları içerir.
- **Ne zaman:** Kod tabanında desen tabanlı toplu değişiklik: fonksiyon yeniden adlandırma, API geçişi, sürüm numarası güncelleme. · **Ne zaman değil:** Tek dosya düzenlemesi ya da her dosyada ayrı yargı gerektiren değişiklik (alt-agent'lara böl). allowed-tools/effort frontmatter alanları Claude Code'a özgü; Codex yok sayar, protokol aynen geçerli.
- **Teknoloji:** bash, git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Roller:** agent-orkestra
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru 'önizle → uygula → doğrula' disiplini; içerik genel bilgi düzeyinde. Aslında yazılım geliştirme konusu ama alt-agent'a bölme kararıyla bağlantılı.

### behavioral-modes  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** Görev türüne göre yedi çalışma modu tanımlar (brainstorm, implement, debug, review, teach, ship, orchestrate); her mod için davranış kuralları ve çıktı biçimi verir.
- **Ne zaman:** ag-kit ailesini kuran projelerde agent'ın tonunu/yaklaşımını göreve göre değiştirmek. · **Ne zaman değil:** Diğer ailelerle (superpowers, agent-skills) birlikte — süreç skilleri zaten bu davranışları tanımlıyor ve çakışır; IMPLEMENT modu kütüphanede olmayan 'clean-code' skill'ine atıf yapıyor. allowed-tools Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Genel istem metni; ag-kit'in diğer skillerine bağımlı, ek değeri düşük.

### cavecrew  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or using `Explore`. Their output is compressed, so main context lasts longer.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Terse caveman voice: answer first, fluff gone, every technical fact kept. Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less tokens". Stays on until "stop caveman" or "normal mode".
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-commit  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Write a Conventional Commits message compressed to intent only. Use for "write a commit", "commit message", /commit or /caveman-commit.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-compress  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. Sends the file's text to the configured model provider. Trigger: /caveman-compress.
- **Teknoloji:** api-anahtari, css, docker, git, html, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 94 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-discover  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. Use for "discover workflows" or breaking LLM spend down by workflow.
- **Teknoloji:** api-anahtari, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-evidence-review  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. Use when asked what Caveman found or where LLM spend goes.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-explore  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it when the exact file or symbol is already named. Returns path:line citations only; its reads stay out of main context.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: model (Codex bunları yok sayar)
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-help  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Quick-reference card for the three caveman skills and their commands. Trigger: /caveman-help or "caveman help".
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-learn  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 94 (A)

- **Ne yapar:** Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. Use when asked to lower an agent's token cost, what caveman has saved, to trim a heavy CLAUDE.md, or to offload re-pasted context into cavemem.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### caveman-manage  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use when asked to start, approve, cancel, promote or roll back a Caveman experiment.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-optimize  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. Use when asked to inspect or evaluate a Caveman optimization report. Needs explicit approval.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-review  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### caveman-setup  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 94 (A)

- **Ne yapar:** Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change. Use for "set up caveman" or adding LLM spend observability.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** otomatik

### caveman-stats  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. Trigger: /caveman-stats.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### claims  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Claims-based authorization for agents and operations. Grant, revoke, and verify permissions for secure multi-agent coordination. Use when: permission management, access control, secure operations, authorization checks. Skip when: open access, no security requirements, single-agent local work.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### claude-automation-recommender  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 96 (A)

- **Ne yapar:** Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.
- **Teknoloji:** docker, git, next.js, node, playwright, react, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (agents, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 42 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### claude-md-improver  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### codex-radar  ·  lemomo-ai/codex-radar @ c388223  ·  puan 60 (C)

- **Ne yapar:** Analyze local Codex session history and create an evidence-grounded HTML collaboration report. Use when the user asks to run Codex Radar, score how they work with Codex, analyze Codex collaboration, or generate a Codex Radar report. Do not use for Claude Code history, generic code review, or workspace usage analytics.
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★39, son güncelleme 2026-09-20, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 179 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** otomatik

### cognitive-pattern  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Define and manage cognitive patterns for agent reasoning and decision-making
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### connect-chatcut-desktop  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Install, open, connect, or repair ChatCut Desktop when the chatcut_desktop MCP tools are missing or unavailable. Do not use from a managed agent already running inside ChatCut Desktop, or when chatcut_desktop tools are already available.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** otomatik

### connect-recommend  ·  openai/plugins @ b767f8f  ·  puan 67 (B)

- **Ne yapar:** Use this skill when the user asks about Stripe Connect configuration, charge patterns, Dashboard access, or how to get started with Connect, is building a marketplace, platform, multi-vendor store, gig platform, or subscription platform, needs to pay out sellers, vendors, or providers, mentions split payments, revenue sharing, multi-party payments, or similar payment distribution concepts, provide
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** tercih
- **Boyut:** 140 KB (SKILL.md 20.7 KB, yük orta)
- **İnceleme:** otomatik

### context-compression  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Uzun oturumlarda bağlamı sıkıştırma: büyük araç çıktılarını anlamsal özete indirme (mikro), biten iş aşamalarını özetleme ve oturum kontrol noktası yazma; kararları ve değişen dosyaları koruma protokolü.
- **Ne zaman:** 20+ turluk oturumlar, agent tekrar etmeye başladığında, iş aşaması değişiminde. · **Ne zaman değil:** Kısa oturumlarda; harness otomatik sıkıştırma yapıyorsa (Claude Code/Codex compaction) çoğu zaman gereksiz — yalnızca elle kontrol noktası yazımı için. allowed-tools/effort Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** api-anahtari, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → tamamlayıcı · **Roller:** agent-orkestra
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Üç seviyeli sıkıştırma ve kontrol noktası şablonu kullanışlı; token kazancı rakamları tahmini.

### context-engineering  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Agent'a doğru bağlamı doğru zamanda verme: kalıcıdan geçiciye bağlam hiyerarşisi (kural dosyaları CLAUDE.md/AGENTS.md, spec, ilgili kaynak dosyalar, hata çıktısı, konuşma), yeniden başlatılabilir oturum sınırları ve bağlam paketleme stratejileri.
- **Ne zaman:** Yeni oturum/proje kurulumu, kural dosyası yazımı, agent çıktı kalitesi düştüğünde, kod tabanının farklı bölümüne geçerken. · **Ne zaman değil:** Tek seferlik küçük sorularda gereksiz.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★113281, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → birincil · **Roller:** agent-orkestra
- **Boyut:** 15 KB (SKILL.md 15.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). addyosmani; araçtan bağımsız (CLAUDE.md ve AGENTS.md'yi birlikte anıyor), somut kural dosyası şablonu ve oturum sınırı önerileri. Bağlam grubunda birincil. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### coordinate-ruflo-swarm  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Coordinate work across a RuFlo AI-agent swarm by discovering channels, reading signed updates, checking claims, and choosing safe next actions. Use for multi-agent status, handoffs, ownership conflicts, or shared-work planning.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### coordinate-team-work  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Creates, assigns, and updates tasks in an AI team run so work has one owner and one deliverable each. Use when the user asks to break down, assign, claim, block, or complete tasks in a run. Changes recorded task state only.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### coordinator-mode  ·  vudovn/ag-kit @ 549ba3d  ·  puan 84 (A)

- **Ne yapar:** Koordinatör olarak çok agent'lı orkestrasyon: görevi ayrıştır, sınıflandır (araştırma/uygulama/doğrulama), okuma işlerini paralel yazma işlerini sıralı dağıt, izle, sentezle ve doğrula. 'Anlamayı devretme' kuralı, işçi istem şablonları ve fork kuralları içerir.
- **Ne zaman:** Birden çok alanı kapsayan büyük görevde agent'ın kendisi kod yazmadan işçi alt-agent'ları yönetmesi. · **Ne zaman değil:** Tek alanlı işlerde; yazılı bir uygulama planı varsa subagent-driven-development daha disiplinli. allowed-tools içinde Claude Code'un 'Agent' aracı geçiyor; Codex'te alt-agent desteği olan sürümde aynı akış, yoksa işçi görevleri ayrı Codex oturumları/`codex exec` çağrılarıyla çalıştırılır.
- **Teknoloji:** api-anahtari, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İşçi istemi yazma rehberi ve eşzamanlılık kuralları güçlü; ama plan tabanlı inceleme döngüsü yok. Orkestrasyon grubunda birincil subagent-driven-development.

### cost-advise  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Optimisation findings from your own Claude Code and Codex logs — low cache hit ratio, 1-hour cache writes that did not pay back, sub-agents on a top-tier model, Codex reasoning share, bloated sessions — each with evidence and a what-if saving. Use when asked how to cut spend or why it is high.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-anomaly  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** MAD-based outlier detection on session spend: lists anomalous sessions with modified-z scores, with an optional --alert-on-outliers exit code for CI. Use when asked which individual session is the cost outlier; cost-burn covers the aggregate trend.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-benchmark  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run the corpus benchmark — booster locally, optional Gemini/Sonnet/Opus baselines — and persist a verifiable measured-vs-claimed table
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-booster-edit  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Apply a simple code transform via agent-booster's WASM engine — sub-millisecond, deterministic, $0 (no LLM call). Companion to cost-booster-route.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-booster-route  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Route tasks through hooks_route, partition by Agent Booster availability, and report Tier 1 bypass utilization with $0 cost
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-budget-check  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Read accumulated cost-tracking spend + budget config, compute utilization, emit 50/75/90/100% alert ladder
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-burn  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Burn-rate trend over time with optional drift-alert exit code. Bins session spend into buckets, surfaces window-over-window delta, and can exit 1 when latest bucket exceeds prior mean by a configurable %. Distinct from `cost-trend` (benchmark drift); this tracks PRODUCTION spend trajectory.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-compact-context  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Wrap getTokenOptimizer().getCompactContext() to retrieve compacted ReasoningBank context for cost-analysis queries; report bridge-reported tokensSaved
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-conversation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Per-conversation cost view — list every session in cost-tracking with started-at, message count, top model, and total cost
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-counterfactual  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Multi-baseline counterfactual cost analysis. Compares actual session spend to hypothetical always-haiku / always-sonnet / always-opus routing baselines. Answers "is the routing earning its keep?" Negative savings flag over-escalation; positive savings quantify the router's win.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-diff  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Snapshot delta between two cost-summary JSON outputs. PR-level cost regression detection — answers "what changed between these two specific snapshots?". Pairs with cost-summary's stable JSON contract.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-export  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Export cost-tracking telemetry in Prometheus textfile or webhook JSON formats — for external observability (Grafana, Datadog, custom dashboards)
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-federation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Consumer-side wiring for ADR-097 Phase 3 federation_spend events — per-peer rolling windows + suspension-threshold check
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-health  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Composite CI gate — runs cost-budget-check + cost-burn + cost-anomaly + cost-projection in parallel and surfaces a single combined health status with max exit code. The operationally-useful entry point — one shell-out covers all four alert ladders.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-ledger  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** One cost view across Claude Code, Codex and Grok on this machine — spend, tokens, cache hit ratio per provider and model, with unpriced models flagged. Use when asked "what did I spend", "how much did Codex cost", or to compare providers. Local logs only, nothing is sent.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-local  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Cost per million tokens on hardware you own (Ollama, llama.cpp, vLLM, LM Studio) from watts, electricity price, hardware price and measured tokens/second, and the utilisation at which local beats a hosted model. Use for local-vs-API break-even questions.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-openrouter  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** OpenRouter real spend — key limit and usage today/week/month, one request's billed cost by generation id, account credits. Use when asked what OpenRouter charged or whether a key is near its limit. Network and API key: asks first.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-optimize  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Analyze token usage patterns and recommend cost optimizations with estimated savings
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-projection  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Forward-looking spend extrapolation. Computes a USD-per-day rate from the recent measurement window, projects to 7d/30d/90d/365d horizons, and surfaces "days until budget exhausted" when a budget is configured. Predictive counterpart to `cost-budget-check` (reactive).
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-report  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Generate a cost report showing token usage and USD costs by agent and model
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-session  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Per-message cost breakdown within a single session. The drill-down companion to cost-anomaly — when an outlier session is flagged, this surfaces the specific expensive messages so operators can see whether the cost came from output tokens, cache writes, or model escalations.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### cost-summary  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Single-shot programmatic dump of all cost data — total spend, per-tier, top session, budget status, federation aggregate. JSON or markdown.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-track  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Auto-capture per-session token usage from the Claude Code session jsonl and persist to the cost-tracking namespace
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cost-trend  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Read every docs/benchmarks/runs/*.json and surface drift in win rate, latency, escalation rate, and LLM-baseline cost over time
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### creative-director  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calibrated against Cannes/D&AD/HumanKind, 5-phase process from brief to presentation.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### cron-schedule  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Schedule persistent background workers via CronCreate
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### cross-host-federation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Join and operate a signed cross-host agentbbs federation and coordinate work claims across nodes. Use when connecting ruflo agents across machines, sharing tasks or results between hosts, or standing up a federation hub; skip for single-host work.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### daa-agent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Create and adapt Dynamic Agentic Architecture agents that learn and evolve
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### diagnosing-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 98 (A)

- **Ne yapar:** Bir superpowers oturumu kötü gittiğinde (tekrar eden iş, yok sayılan plan, tetiklenmeyen skill, pahalılık) diskteki transkriptleri okuyup kanıta dayalı rapor çıkarır; her bulgu path:line ile alıntılanır. Oturum bulma, gizli veri karartma ve GitHub issue paketi rehberleri içerir.
- **Ne zaman:** superpowers skill ailesiyle çalışan oturumların neden yanlış gittiğini incelemek, bakımcılara hata raporu hazırlamak. · **Ne zaman değil:** superpowers kullanılmıyorsa; genel kod hata ayıklaması için (systematic-debugging).
- **Teknoloji:** bash, jsonl
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★312440, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (dar). Kanıt disiplini ve redaksiyon politikası örnek alınacak düzeyde; çok harness'li (Claude Code, Codex vb.) oturum keşfi var. Yalnızca superpowers kullanıcıları için.

### discernment-nudge  ·  anthropics/skills @ ca45fc4  ·  puan 89 (A)

- **Ne yapar:** Kullanıcının üzerine karar vereceği önemli bir cevap ya da taslaktan sonra, cevaptaki belirli noktalara bağlı 2-3 kısa takip sorusu ekler: önemli olguları doğrulama, varsayımları sorgulama, eksik bağlamı fark etme. Konuşma başına en fazla bir kez; basit sorularda, kodda ve yaratıcı yazıda devreye girmez.
- **Ne zaman:** Tavsiye, plan, tahmin, veri yorumu gibi kullanıcının harekete geçeceği çıktılar üreten sohbet/asistan agent'ları. · **Ne zaman değil:** Kod yazan agent'larda (skill zaten kapsam dışı sayar); otomatik iş hatlarında (kullanıcı yokken soru eklemek gürültü).
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Roller:** dokuman-yazari
- **Boyut:** 21 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi; ne zaman kullanılmayacağı ve çıktı biçimi çok net. Orkestrasyon değil 'cevap kalitesi' skill'i; rapor/tavsiye üreten rollere opsiyonel.

### discover-plugins  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Discover and recommend ruflo plugins based on your workflow, installed MCP tools, and current task
- **Teknoloji:** api-anahtari, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### dispatching-parallel-agents  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Bağımsız 2+ problemi (farklı test dosyaları, alt sistemler) her birine izole bağlamlı ayrı bir agent vererek paralel çözme kalıbı: bağımsız alanları belirle, odaklı görev istemi yaz, paralel dağıt, sonuçları incele ve birleştir.
- **Ne zaman:** Birbirinden bağımsız birden çok hata/araştırma işini paralel yürütmek. · **Ne zaman değil:** Görevler ortak durum paylaşıyor ya da aynı dosyalara yazıyorsa; tek kök nedenli hatalarda. Codex'te alt-agent yoksa paralel `codex exec` süreçleri ya da ayrı worktree'lerle uygulanır.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★312440, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → tamamlayıcı · **Roller:** agent-orkestra, planlayici
- **Boyut:** 6 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (tamamlayıcı). superpowers; kısa (6 KB), karar ağacı ve istem yapısı net. subagent-driven-development ile birlikte kullanılır.

### dispatching-parallel-agents@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 6 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### embeddings  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Vector embeddings with HNSW indexing, sql.js persistence, and hyperbolic support. 75x faster with agentic-flow integration. Use when: semantic search, pattern matching, similarity queries, knowledge retrieval. Skip when: exact text matching, simple lookups, no semantic understanding needed.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### fast-code-edits  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Apply code edits locally in milliseconds with no LLM call: deterministic codemods (var-to-const, remove-console, add-logging) via hooks_codemod, and snippet merges into large files via hooks_fast-apply (agent-booster). Use for mechanical transforms across many files, or when you already have the replacement code for one function in a big file. Skip when the change needs reasoning; route that to a 
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-audit  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Review the signed coordination evidence visible through RuFlo Federation. Use to inspect recent messages, channel activity, and work-claim history for inconsistencies or follow-up without changing shared state.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-audit@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Query federation audit logs with compliance filtering
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-init  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Guide a user through connecting to RuFlo Federation with the public x.ruv.io MCP service. Use for onboarding, connection details, available channels, or an explicitly requested gateway presence announcement.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-init@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Initialize federation on this node — generate keypair and configure peers
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 0.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-status  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Summarize the observable health and activity of the public RuFlo Federation gateway. Use when the user asks whether the federation is active, what channels or claims exist, or what agents are currently coordinating.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### federation-status@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Show federation health — peers, sessions, trust levels, and message metrics. Use when the user asks "is federation healthy?", "show peers", "federation status", or wants to inspect cross-installation agent connectivity.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### flow-nexus-neural  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Train and deploy neural networks in distributed E2B sandboxes with Flow Nexus
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### flow-nexus-platform  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Comprehensive Flow Nexus platform management - authentication, sandboxes, app deployment, payments, and challenges
- **Teknoloji:** api-anahtari, css, docker, git, html, next.js, node, python, react, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 24.9 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### flow-nexus-swarm  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Cloud-based AI swarm deployment and event-driven workflow automation with Flow Nexus platform
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.2 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### full-output-enforcement  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output.
- **Teknoloji:** api-anahtari, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### gaia-architecture-comparison  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Side-by-side comparison of ruflo vs HAL vs other GAIA harnesses — capability gaps, design decisions, and improvement roadmap
- **Teknoloji:** api-anahtari, html, node, playwright, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### gaia-debugging  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Diagnose why a GAIA question failed — extract trace, classify failure mode, and propose a fix. Use when a GAIA benchmark run reports a failed/incorrect task_id and you need to root-cause it before resubmitting.
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### gaia-submission  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Walk through a complete GAIA benchmark→submit flow — from key resolution through HAL-compatible package generation
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### generate-console-theme  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Generate a data-only animated theme preset for Ruflo Console Theme Studio. Use when the user requests a new console color palette, cyberpunk theme, or variation of Orbital globe, stars, and swarm animation in Claude or Codex.
- **Teknoloji:** api-anahtari, css _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### graph-mincut  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Find the weakest boundary in a dependency or knowledge graph with an exact minimum cut (@ruvector/mincut-wasm via ruvector). Use when the user asks where to split a module, which files are loosely coupled, what cluster a node belongs to, or how to partition work between agents. Skip for shortest paths or simple neighbour lookups (use agentdb_graph-query k-hop).
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### harness-bench  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Create (`bench create {repo}`) or verify (`bench verify {suite.json}`) a @metaharness/darwin bench suite, the fixed corpus `harness-evolve --bench` scores variants against. Use when preparing an evolution benchmark. Degrades gracefully without darwin.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-drift-from-history  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** One-command drift detection: run a fresh metaharness audit, diff it against the latest stored audit by ADR-152 similarity, and alert when the distance crosses `--threshold`. Use when checking whether a harness has drifted since its last audit.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-evolve  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run `@metaharness/darwin evolve {repo}`: mutate a harness's seven policy surfaces, sandbox-score each variant and promote only measured wins. Use when evolving a harness against its tests or a bench suite. Degrades gracefully without darwin (ADR-150/153).
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-genome  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** 7-section repo readiness report from `metaharness genome {path}`. Returns repo_type / agent_topology / risk_score / mcp_surface / test_confidence / publish_readiness. Pure-read; degrades gracefully (ADR-150).
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-gepa  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Load, validate or render a GEPA genome, or classify failure modes in a run transcript, via @metaharness/darwin/gepa. Use when inspecting or auditing a genome; use harness-evolve for sandbox-scored evolution. Degrades gracefully without darwin.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-learn  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run a GEPA learning cycle via `metaharness learn`, optimizing a harness genome against a SWE-bench-style slice. Use when training a harness genome. $0 dry-run by default; `--run` opts into spend. Needs a metaharness checkout (--repo or $METAHARNESS_REPO).
- **Teknoloji:** docker, git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-mcp-scan  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Static security scan of a harness's declared MCP surface via `harness mcp-scan {path}`. Reads `.mcp/servers.json` + `.harness/claims.json`. Pure-read, no dispatch. Exits 1 on findings at or above `--fail-on` severity.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-mint  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Scaffold a custom AI agent harness via `metaharness new {name} --template {id} --host {id}`. Use when the user wants a new standalone harness. Dry-run unless --confirm is passed, and refuses to write inside the calling repo.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-oia-audit  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Composite Phase-2 audit worker (ADR-150). Bundles harness oia-manifest + threat-model + mcp-scan into one timestamped audit record stored in the `metaharness-audit` memory namespace. Designed for cron-scheduled drift detection.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-score  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** 5-dimension harness readiness scorecard from `metaharness score {path}` (harnessFit, compileConfidence, taskCoverage, toolSafety, memoryUsefulness, plus cost per run). Use when rating a repo as an agent harness. Pure-read; degrades gracefully without MetaHarness.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-security-bench  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run `@metaharness/darwin security bench` (Darwin Shield): evolve a security-detection harness on a 10-vuln/9-decoy corpus and grade TPR/FPR/patch/repro against four baselines. Use when benchmarking security-harness detection. Degrades gracefully without darwin.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### harness-similarity  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Weighted similarity (ADR-152) between two harness fingerprints (genome + score JSON): an overall score in [0,1] plus per-component breakdown. Use when comparing two harnesses or detecting drift between them. Pure TypeScript; needs no @metaharness package.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### harness-threat-model  ·  ruvnet/ruflo @ 98ddf41  ·  puan 97 (A)

- **Ne yapar:** Enterprise-review-grade threat model from `harness threat-model {path}`. Categorizes MCP-surface threats; emits `worst: 'clean'|'low'|'medium'|'high'` + per-threat findings. Pure-read.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### hive-mind  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Byzantine fault-tolerant consensus and distributed coordination. Queen-led hierarchical swarm management with multiple consensus strategies. Use when: distributed coordination, fault-tolerant operations, multi-agent consensus, collective decision making. Skip when: single-agent tasks, simple operations, local-only work.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### hive-mind-advanced  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Advanced Hive Mind collective intelligence system for queen-led multi-agent coordination with consensus mechanisms and persistent memory
- **Teknoloji:** api-anahtari, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.2 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### hooks-automation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Automated coordination, formatting, and learning from Claude Code operations using intelligent hooks with MCP integration. Includes pre/post task hooks, session management, Git integration, memory coordination, and neural pattern training for enhanced development workflows.
- **Teknoloji:** api-anahtari, docker, git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: claude, codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 30 KB (SKILL.md 30.1 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### init-project  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Initialize a new Ruflo project with MCP tools, hooks, and agent configuration. Use when setting up Ruflo in a fresh repo, or when the user says "init ruflo", "set up ruflo", or asks how to bootstrap the MCP server, hooks, and agent configs from scratch.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### injection-defense  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Screen untrusted text (web pages, issue bodies, tool output, other agents' messages) for prompt injection, jailbreaks and PII before acting on it, using ruflo AIDefence. Use before passing fetched or user-supplied content to an agent, before storing it in memory, or when a message asks you to ignore instructions. Skip for text you wrote yourself.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### intelligence-route  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Route tasks via the 3-tier model selector and learned patterns; emits a routing rationale via hooks_explain
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### intelligence-transfer  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Copy learned patterns from another local project, or browse, download and publish patterns through the IPFS pattern marketplace. Use when a new project should start with patterns an older one already learned, or when sharing patterns with a peer.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### intelligent-routing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 66 (B)

- **Ne yapar:** Her kullanıcı isteğini sessizce analiz edip anahtar kelime/alan/karmaşıklığa göre uygun uzman agent'ı (security-auditor, frontend-specialist, orchestrator…) otomatik seçen yönlendirme kuralları.
- **Ne zaman:** ag-kit'in uzman agent tanımlarının kurulu olduğu projelerde. · **Ne zaman değil:** ag-kit agent'ları (security-auditor, backend-specialist vb.) kurulu değilse — bu kütüphanede yoklar, rol sistemi zaten skill-ekle.py ile kuruluyor. 'Her zaman aktif' talimatı bağlamı ve davranışı etkiler. allowed-tools Claude Code'a özgü.
- **Teknoloji:** api-anahtari, css, docker, html, node, playwright, react, tailwind, vue _(otomatik tespit)_ · **Paketler:** ag-kit agent tanımları
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Var olmayan agent adlarına bağımlı; bu kütüphanenin rol sistemiyle çakışır.

### investigate-first  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### kg-extract  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Extract entities and relations from source files to build a knowledge graph
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### kg-traverse  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Pathfinder traversal of the knowledge graph starting from a seed entity
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### launch-ai-team  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Plans and creates an AI team for a goal, with roles, a run that carries a unit budget, and bounded tasks. Use when the user asks to start, set up or staff a team, or to split a larger goal across roles. Records coordination state only; nothing is executed.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### lean-build  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Build feature work with high overbuilding risk. Use for new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop condition matter.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** otomatik

### loop-worker  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run Ruflo background workers using Claude Code native /loop scheduling
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### lora-learning  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Train and use ruflo's on-device learning: MicroLoRA adapters on @ruvector/learning-wasm (microsecond-scale WASM adaptation), trajectory recording and pattern learning. Use when the user wants ruflo to learn from successful tasks, adapt routing to a project, or check whether WASM learning is active. Skip for one-off tasks with no feedback signal.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### manage-team-lifecycle  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Pauses, resumes, or completes an AI team, or marks a run complete, while keeping its evidence. Use when the user asks to pause, stop, resume, wrap up, or close a team or run. Changes coordination state only and deletes nothing.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### managed-agent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run an Anthropic Claude Managed Agent — a cloud agent harness (container + filesystem + tools), the cloud counterpart of the local wasm-agent runtime
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### managed-workflow  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Discover and run bounded remote dynamic workflows with Ruflo mod policy, worker inspection and independent acceptance gates
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### megacave  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. Invoke only with /megacave or /caveman wenyan. Stays on until "stop caveman" or "normal mode".
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### memory-bridge  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Bridge Claude Code auto-memory into AgentDB with ONNX embeddings, deduplicate, and enable unified cross-project search
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### memory-management@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** AgentDB memory system with HNSW vector search. Provides 150x-12,500x faster pattern retrieval, persistent storage, and semantic search capabilities for learning and knowledge management. Use when: need to store successful patterns, searching for similar solutions, semantic lookup of past work, learning from previous tasks, sharing knowledge between agents, building knowledge base. Skip when: no le
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 4 KB (SKILL.md 3.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik
- **Not:** Aynı adlı başka skill: `memory-management` (anthropics/knowledge-work-plugins) CLAUDE.md + memory/ ile çalışma belleği kurar. Bu skill AgentDB vektör belleğidir ve `npx @claude-flow/cli memory` ister; işler farklı.

### memory-search  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Search Ruflo memory with semantic retrieval, keyword/semantic union, or optional SmartRetrieval reranking
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### memory-system  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Oturumlar arası kalıcı bellek: .agents/memory/MEMORY.md indeksi (en fazla 200 satır) ve konu dosyaları (kullanıcı tercihleri, proje kuralları, teknik kararlar, geri bildirim); kaydetme, hatırlama, arama işlemleri ve neyin kaydedilmeyeceği kuralları.
- **Ne zaman:** Harness'in yerleşik belleği olmayan ortamlarda (ya da projeye taşınabilir, git'te tutulan bellek istendiğinde) tercih ve kararları saklamak. · **Ne zaman değil:** Claude Code'un yerleşik auto-memory'si veya claude-mem gibi bir bellek eklentisi zaten kullanılıyorsa (çift kayıt olur); gizli bilgi saklamak için. Codex'te uygundur — AGENTS.md'ye 'oturum başında .agents/memory/MEMORY.md oku' satırı eklenmeli.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel). İndeks + konu dosyası yapısı sağlam ve Claude Code belleğine benzer; harness belleğiyle çakışma riski var.

### migration  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation proof.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### monitor-ai-team  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Reports an AI team's progress, blockers, task ownership, and recorded budget. Use when the user asks for status, what is blocked, who owns what, or how much of the budget is recorded as used. Read-only.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### monitor-stream  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Stream live swarm events using the Monitor tool for real-time observability
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### n8n-agents  ·  czlonkowski/n8n-skills @ e037563  ·  puan 87 (A)

- **Ne yapar:** Design n8n AI agents the right way. Use when building or editing any @n8n/n8n-nodes-langchain.* AI node — an AI Agent, LLM chain, Text Classifier, or Information Extractor — and whenever the user mentions AI agents, LLM with tools, tool calling, $fromAI, system prompts, agent memory, sessionId, structured/JSON output, output parser, RAG, vector store, a chat assistant/bot, or human-in-the-loop rev
- **Teknoloji:** api-anahtari, canvas, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 124 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** otomatik

### n8n-binary-and-data  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Handle files and binary data in n8n correctly. Use when working with files, images, PDFs, attachments, uploads or downloads, base64, vision/multimodal input, or when an AI agent needs a file as tool input or output — and whenever the user mentions $binary, binaryPropertyName, "read the PDF", "attach the file", "send the image", Merge losing binary, or a CDN for chat images. Covers the $binary vs $
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 61 KB (SKILL.md 15.5 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-javascript  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Write, review, or debug JavaScript in an n8n Code node. Use when a Code node is already in the workflow (editing it, fixing an error, choosing its mode, making it faster), or when a new one is justified: no native node fits (check the job-to-node table in using-n8n-mcp-skills first) and the job is on the closed list — loops or recursion no node expresses, state across runs, parsing no node handles
- **Teknoloji:** api-anahtari, canvas, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 134 KB (SKILL.md 22.4 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-python  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Write Python in n8n Code nodes (native Python, `language` pythonNative, n8n 2.x). Use when the user explicitly wants Python in a Code node, when migrating old Pyodide/"Python (Beta)" code that used _input/_json/_node/_now, or when a Python Code node fails with NameError, "Security violations detected", "Import of standard library module … is disallowed", "__build_class__ not found", "A 'json' prop
- **Teknoloji:** html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-tool  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Write JavaScript or Python for the n8n Custom Code Tool (@n8n/n8n-nodes-langchain.toolCode) — the AI-agent-callable tool, NOT the workflow Code node. Use when building a Code Tool attached to an AI Agent, writing code that an LLM will invoke, parsing the `query` input, returning a string result, defining an input schema for structured arguments (specifyInputSchema, jsonSchemaExample, DynamicStruct
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 36 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### n8n-error-handling  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Wire n8n error handling so failures are loud, structured, and recoverable. Use when building any webhook/API workflow, a scheduled or unattended workflow, or any path where a silent failure would drop user-visible work — and whenever the user mentions error handling, onError, continueErrorOutput, error branches/outputs, retries, retryOnFail, Respond to Webhook status codes, 4xx/5xx, Error Trigger,
- **Teknoloji:** api-anahtari, canvas, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** otomatik

### n8n-expression-syntax  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, mapping data between nodes, or referencing webhook data in workflows. Use this skill whenever configuring node fields that reference data from previous nodes — expressions are how n8n passes data between nodes, and getting th
- **Teknoloji:** api-anahtari, canvas, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 22.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-mcp-tools-expert  ·  czlonkowski/n8n-skills @ e037563  ·  puan 87 (A)

- **Ne yapar:** Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, organizing workflows into folders, managing credentials, auditing instance security, or using any n8n-mcp tool. Provides tool selection guidance, parameter formats, and common patterns. IMPORTANT — Always consult this skill before calling any n8n-m
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 107 KB (SKILL.md 30.0 KB, yük buyuk)
- **İnceleme:** otomatik

### n8n-multi-instance  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Use when an n8n-mcp account targets more than one n8n instance — i.e. the `n8n_instances` tool is available, the user mentions multiple n8n instances or environments (prod vs staging, several teams or clients), several agents or chats work on one account in parallel, a workflow / datatable / credential / execution call returns an unexpected NOT_FOUND or reads data you don't recognize, or a call is
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 14.5 KB, yük orta)
- **İnceleme:** otomatik

### n8n-node-configuration  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration patterns by node type — including the native nodes that replace Code (Summarize, Aggregate, Split Out, Merge, Compare Datasets, Remove Duplicates, Sort, Limit, Date & Time, HTTP Request p
- **Teknoloji:** api-anahtari, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 108 KB (SKILL.md 19.7 KB, yük orta)
- **İnceleme:** otomatik

### n8n-self-hosting  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Deploy a production self-hosted n8n end-to-end to a fresh Linux VM over SSH, using Docker Compose behind a Caddy reverse proxy with automatic HTTPS. Use whenever the user wants to self-host, install, provision, or deploy n8n on their own server/VPS (Hetzner, DigitalOcean, AWS EC2, bare metal) — single/regular mode or queue mode with workers — or to update, back up, restore, or harden such an insta
- **Teknoloji:** api-anahtari, docker, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** otomatik

### n8n-subworkflows  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Build reusable, composable n8n sub-workflows. Use when extracting shared logic, building anything multi-step or reused across workflows, or any workflow over ~10 nodes — and whenever the user mentions sub-workflows, Execute Workflow, reuse, shared/common logic, modular workflows, "Define Below" inputs, waitForSubWorkflow, mode each vs all, or exposing a workflow as an agent tool. Covers typed sub-
- **Teknoloji:** api-anahtari, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 19.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-validation-expert  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Interpret validation errors and guide fixing them. Use when encountering validation errors, validation warnings, false positives, operator structure issues, or need help understanding validation results. Also use when asking about validation profiles, error types, the validation loop process, or auto-fix capabilities. Consult this skill whenever a validate_node or validate_workflow call returns er
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 91 KB (SKILL.md 22.4 KB, yük orta)
- **İnceleme:** otomatik

### n8n-workflow-patterns  ·  czlonkowski/n8n-skills @ e037563  ·  puan 90 (A)

- **Ne yapar:** Proven workflow architectural patterns from real n8n workflows. Use when building new workflows, designing workflow structure, choosing workflow patterns, planning workflow architecture, or asking about webhook processing, HTTP API integration, database operations, AI agent workflows, batch processing, or scheduled tasks. Always consult this skill when the user asks to create, build, or design an 
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 101 KB (SKILL.md 21.5 KB, yük orta)
- **İnceleme:** otomatik

### nested-subagents  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Spawn nested sub-agents (agents that spawn sub-agents, up to depth=5) via Claude Code's native Task tool — for context-managed deep delegation
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### neural-train  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Train SONA + MicroLoRA neural patterns from successful task completions; runs the DISTILL + CONSOLIDATE phases of the 4-step pipeline
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### neural-training  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Neural pattern training with SONA (Self-Optimizing Neural Architecture), MoE (Mixture of Experts), and EWC++ for knowledge consolidation. Use when: pattern learning, model optimization, knowledge transfer, adaptive routing. Skip when: simple tasks, no learning required, one-off operations.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### open-federation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Coordinate with the open ruflo swarm federation at x.ruv.io (signed Nostr, membership-gated) and ask Seraphina — the swarm queen / primary coordinator — for guidance. Use when: seeing who is online across the internet, reading/assigning work, checking or issuing claims across hosts, onboarding a new node or user, opening a public or private coordination channel, or deciding what the swarm should d
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### parallel-agents  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Güvenli paralel agent kullanımı: ne zaman paralelleştirilir/paralelleştirilmez, çalışma ortamından bağımsız yetenek keşfi, güven sınırı, delegasyon bütçesi, izolasyon politikası (worktree/sandbox), delegasyon şablonu, ilerleme yok tespiti ve sentez protokolü. Google Antigravity öncelikli yazılmış.
- **Ne zaman:** Güvenlik/izolasyon kuralları önemli olan çok agent'lı işler; delegasyon bütçesi ve izleme gerektiğinde. · **Ne zaman değil:** Claude Code/Codex'te Antigravity'ye özgü kısımlar uygulanamaz — genel kurallar geçerli. Plan yürütmek için subagent-driven-development, basit paralel hata ayıklama için dispatching-parallel-agents. allowed-tools/effort Claude Code'a özgü.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Güvenlik ve izolasyon bölümleri iyi; Antigravity odaklı olması diğer harness'lerde gürültü yaratıyor.

### pod-sales  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run one dry-run tick of the sales business-pod (ADR-164): validate templates/sales.json, reserve budget, post a summary envelope to the \"sales\" room and print a status line for /loop. Use when a person or a /loop asks for the next sales-pod tick.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### project-artifact  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a
- **Teknoloji:** css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 19.9 KB, yük orta)
- **İnceleme:** otomatik

### publish-ruflo-update  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Prepare and publish a concise, gateway-attributed RuFlo federation update when the user explicitly asks to announce status, tasks, results, or help. Use for public-channel or federation-wide coordination messages, not private-channel plaintext.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### reasoningbank-agentdb  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Implement ReasoningBank adaptive learning with AgentDB's 150x faster vector database. Includes trajectory tracking, verdict judgment, memory distillation, and pattern recognition. Use when building self-learning agents, optimizing decision-making, or implementing experience replay systems.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### reasoningbank-intelligence  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Implement adaptive learning with ReasoningBank for pattern recognition, strategy optimization, and continuous improvement. Use when building self-learning agents, optimizing workflows, or implementing meta-cognitive systems.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### receipts  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying Claude Code usage/spend to a manager, self-review, or "what have I been using this for" check-ins. Mines ~/.claude/projects locally (no extra API calls beyond one final write-up), cross-references local git history, and writes a markdown report plus a self-contained HTM
- **Teknoloji:** api-anahtari, git, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### remember-team-context  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Stores approved context for one AI team and searches it later, with provenance. Use when the user asks to remember a decision, constraint, or fact for the team, or to recall what the team already knows. Memory is separate for each team and tenant.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### review-team-deliverables  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Checks an AI team run against its acceptance criteria using the evidence bundle. Use when the user asks whether the work is done or correct, or before completing a run. Separates verified evidence from agent claims.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ruflo  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Ruflo is a multi-agent orchestration platform for AI coding agents (Claude Code, Cursor, Codex, Copilot, Gemini, Amp, +12 more). Use this skill when the user wants to (1) install/init ruflo in a project, (2) run multi-agent swarms with hierarchical coordination, (3) use ruflo's 314+ MCP tools for memory, routing, hooks, sub-agents, or workflows, (4) check ruflo status/version/doctor health, or (5)
- **Teknoloji:** api-anahtari, git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ruflo-doctor  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run health checks on the Ruflo installation and fix common issues
- **Teknoloji:** api-anahtari, git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ruflo-status  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Diagnose Ruflo health, then report system, MCP server, and active-agent status without changing the installation
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ruos-host-run  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** Run a ruflo swarm agent on the user's own ruOS cloud desktop through the fleet MCP, stream its output and record it in swarm state. Use when the user wants an agent to run on a ruOS desktop or places a swarm agent on a remote ruOS host.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### rvf-manage  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Manage RVF (Ruflo Vector Format) files for portable agent memory and cross-platform transfer
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### safe-refactor  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### session-persist  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Persist and restore agent sessions across conversations with state snapshots
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### session-report  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 98 (A)

- **Ne yapar:** Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.
- **Teknoloji:** api-anahtari, css, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 56 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### stream-chain  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Stream-JSON chaining for multi-agent pipelines, data transformation, and sequential workflows
- **Teknoloji:** api-anahtari, git, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### subagent-driven-development  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Yazılı uygulama planını görev başına taze bir uygulayıcı alt-agent göndererek yürütür; her görevden sonra spec uyumu + kod kalitesi incelemesi, düzeltme döngüsü ve sonda tüm dal incelemesi yapar. Rol başına model seçimi, karar defteri (ledger), kesintisiz yürütme kuralları ve görev özeti/inceleme paketi betikleri içerir.
- **Ne zaman:** Bağımsız görevlere bölünmüş bir planı tek oturumda yüksek kaliteyle uygulamak. · **Ne zaman değil:** Plan yoksa (önce writing-plans/planning-and-task-breakdown); görevler sıkı bağımlıysa; küçük tek dosyalık işlerde. Codex'te alt-agent desteği yoksa her görev için ayrı `codex exec` çağrısı ya da executing-plans ile sıralı yürütme kullanılır.
- **Teknoloji:** git, bash
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★312440, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → birincil · **Roller:** agent-orkestra, planlayici
- **Boyut:** 56 KB (SKILL.md 19.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi: düzeltme döngüsü ve final inceleme ayrıntıları references/fix-loop.md ve references/final-review.md dosyalarına taşındı; SKILL.md 260 satır kısaldı, akış diyagramı sadeleşti. Davranış aynı, bağlam yükü azaldı.

### subagent-driven-development@openai  ·  openai/plugins @ b767f8f  ·  puan 69 (B)

- **Ne yapar:** Use when executing implementation plans with independent tasks in the current session
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 55 KB (SKILL.md 31.6 KB, yük buyuk)
- **İnceleme:** otomatik

### sublinear-core  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Personalized PageRank, local forward/backward push and sparse diagonally dominant solves with the zero-dependency @ruvnet/sublinear-core. Use for relevance around a few nodes of a large graph or a few entries of A⁻¹b; for ruflo's own knowledge graph use agentdb_graph-pathfinder.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### sublinear-solver  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Solve large sparse diagonally dominant linear systems (Mx = b) and estimate single solution entries without a full solve, using sublinear-time-solver. Use for Laplacian or graph systems, influence estimates, or when only a few entries of the solution are needed. Skip for small graphs or plain PageRank: ruflo's built-in power iteration is much faster there.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### surgical-patch  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matter.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.6 KB, yük kucuk)
- **İnceleme:** otomatik

### swarm-advanced  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Advanced swarm orchestration patterns for research, development, testing, and complex distributed workflows
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: claude, codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 23.1 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### swarm-init  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Initialize a multi-agent swarm with anti-drift configuration. Use when starting a complex multi-file task that needs 3+ coordinated agents (feature implementation, refactor across modules, security audit). Skip for single-file edits or quick questions.
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### swarm-orchestration  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Orchestrate multi-agent swarms with agentic-flow for parallel task execution, dynamic topology, and intelligent coordination. Use when scaling beyond single agents, implementing complex workflows, or building distributed AI systems.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### swarm-orchestration@ruvnet  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Multi-agent swarm coordination for complex tasks. Use when: 3+ files need changes, new features, refactoring. Skip when: single file edits, simple fixes, documentation.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### triage-ruflo-work  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Triage a RuFlo swarm without changing coordination state by inspecting channels, signed updates, and work claims. Use to identify blockers, collisions, stale work, or the best next task before anyone publishes or claims work.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ultracave  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Caveman at maximum compression: fragments, one word when one word is enough, each fact once. Invoke only with /ultracave or /caveman ultra. Stays on until "stop caveman" or "normal mode".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### using-agent-skills  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** addyosmani/agent-skills ailesinin meta-skill'i: işin geliştirme aşamasına göre hangi skill'in uygulanacağını gösteren karar ağacı (interview-me, spec, plan, incremental-implementation, test, review, ship…) ve temel çalışma davranışları (varsayımları açığa çıkar, karışıklığı yönet, sadeliği koru, kapsamı koru, doğrula).
- **Ne zaman:** agent-skills ailesinden birden çok skill kurulu projelerde oturum başında doğru skill'i seçmek. · **Ne zaman değil:** Ailenin skilleri kurulu değilse karar ağacındaki adlar boşa düşer; superpowers ailesi kullanılıyorsa using-superpowers ile birlikte kurma (iki meta-skill çakışır).
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★113281, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → birincil
- **Boyut:** 10 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil, meta grubunda). Zorlayıcı dil kullanmadan net yönlendirme yapıyor; çalışma davranışları bölümü aileden bağımsız da değerli.

### using-n8n-mcp-skills  ·  czlonkowski/n8n-skills @ e037563  ·  puan 85 (A)

- **Ne yapar:** Use when building, editing, validating, testing, or debugging an n8n workflow through the n8n-mcp MCP server — designing a flow, configuring a node, writing an expression or Code node, wiring credentials, or fixing one that misbehaves. The entry-point skill for the n8n-mcp-skills pack: it routes you to the right specialist skill, gives working knowledge of every n8n-mcp tool from turn one, and sta
- **Teknoloji:** api-anahtari, canvas, docker, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** czlonkowski (kisi, ★6589, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 17.2 KB, yük orta)
- **İnceleme:** otomatik

### using-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 98 (A)

- **Ne yapar:** superpowers ailesinin meta-skill'i: '%1 ihtimal bile varsa skill'i çağır' kuralı, süreç skillerinin önceliği, rasyonalizasyon kırmızı bayrakları ve Claude Code, Codex, Pi, Antigravity, Gemini, Hermes, Muse için araç eşleme dosyaları.
- **Ne zaman:** superpowers ailesinin (brainstorming, writing-plans, systematic-debugging, subagent-driven-development…) birlikte kurulduğu projeler. · **Ne zaman değil:** Aile kurulu değilse; agent-skills ailesinin meta-skill'iyle birlikte. Çok agresif tetikleme dili küçük işlerde gereksiz süreç yükü yaratabilir. Codex'te references/codex-tools.md araç eşlemesini kullanır — ek uyarlama gerekmez.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★312440, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 20 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (meta grubunda). Çok harness'li araç eşlemesi en güçlü yanı; aile dışında kullanılmaz. superpowers ailesi seçilen projede birincil olur.

### using-superpowers@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 17 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik

### v3-cli-modernization  ·  ruvnet/ruflo @ 98ddf41  ·  puan 96 (A)

- **Ne yapar:** CLI modernization and hooks system enhancement for claude-flow v3. Implements interactive prompts, command decomposition, enhanced hooks integration, and intelligent workflow automation.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 25.1 KB, yük buyuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-core-implementation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Core module implementation for claude-flow v3. Implements DDD domains, clean architecture patterns, dependency injection, and modular TypeScript codebase with comprehensive testing.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 21.5 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-ddd-architecture  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Domain-Driven Design architecture for claude-flow v3. Implements modular, bounded context architecture with clean separation of concerns and microkernel pattern.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-integration-deep  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Deep agentic-flow@alpha integration implementing ADR-001. Eliminates 10,000+ duplicate lines by building claude-flow as specialized extension rather than parallel implementation.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-mcp-optimization  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** MCP server optimization and transport layer enhancement for claude-flow v3. Implements connection pooling, load balancing, tool registry optimization, and performance monitoring for sub-100ms response times.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 20.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-memory-unification  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Unify 6+ memory systems into AgentDB with HNSW indexing for 150x-12,500x search improvements. Implements ADR-006 (Unified Memory Service) and ADR-009 (Hybrid Memory Backend).
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### v3-swarm-coordination  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** 15-agent hierarchical mesh coordination for v3 implementation. Orchestrates parallel execution across security, core, and integration domains following 10 ADRs with 14-week timeline.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.9 KB, yük orta) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-cluster  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Cluster code by graph community detection via npx ruvector@0.3.13 hooks graph-cluster (spectral / Louvain)
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-embed  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Generate embeddings via npx ruvector@0.3.13 embed text (ONNX all-MiniLM-L6-v2, 384-dim), normalize, and store in HNSW index
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-hyperbolic  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Place hierarchical data in the Poincare ball using depth for the radius and npx ruvector@0.3.13 embed text for direction (a unit-norm text embedding alone has no depth)
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-quantization  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Semantic vector search and 1-bit RaBitQ quantization over ruflo memory. Use when the user needs similarity search over stored patterns or embeddings, wants to shrink a large embedding store (~32x smaller), or asks why recall is low. Skip for exact key lookups (use memory_retrieve) or tiny stores (<1k entries), where plain search is already exact.
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-search  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Vector search via embeddings_* (large-scale HNSW) and ruvllm_hnsw_* (WASM router for ≤11 hot patterns), with RaBitQ 1-bit quantization for 32× memory reduction
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### vector-setup  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** First-run setup for ruvector@0.3.13 — installs ONNX/Brain/SONA add-ons, registers the MCP server, and verifies the install via `doctor`
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### verify-and-stop  ·  JuliusBrussee/caveman @ 2e068f7  ·  puan 96 (A)

- **Ne yapar:** Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proof.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuliusBrussee (kisi, ★117512, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### wasm-agent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Create and manage sandboxed WASM agents for isolated code execution
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### wasm-gallery  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Browse, publish, and install WASM agents from the community gallery
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### witness  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Sign, verify and track fix-marker regressions over time with an Ed25519 witness manifest. Use when registering fixes or checking a release for regressed fixes. The default seed proves integrity only; set RUFLO_WITNESS_SEED/RUFLO_WITNESS_PUBLIC_KEY for authorship.
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### worker-integration  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Worker-Agent integration for intelligent task dispatch and performance tracking
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar) · Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### workflow-automation  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Workflow creation, execution, and template management. Automates complex multi-step processes with agent coordination. Use when: automating processes, creating reusable workflows, orchestrating multi-step tasks. Skip when: simple single-step tasks, ad-hoc operations.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### workflow-create  ·  ruvnet/ruflo @ 98ddf41  ·  puan 94 (A)

- **Ne yapar:** Author a workflow — either an MCP workflow template (persisted, lifecycle) or a native .claude/workflows/*.js orchestration script (agent/parallel/pipeline fan-out)
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### workflow-run  ·  ruvnet/ruflo @ 98ddf41  ·  puan 99 (A)

- **Ne yapar:** Run a workflow — drive an MCP workflow lifecycle (execute/pause/resume/cancel) or invoke + resume a native .claude/workflows/*.js orchestration via the Workflow tool
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik
