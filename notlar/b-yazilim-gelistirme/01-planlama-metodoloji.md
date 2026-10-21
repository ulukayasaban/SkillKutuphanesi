# 01-planlama-metodoloji — Yazılım Geliştirme

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/15**

### app-builder  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents.
- **Teknoloji:** next.js, node, python, react, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### brainstorming  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of it (a talk, a business, a renovation).
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★302965, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 9.8 KB, yük orta)
- **İnceleme:** otomatik

### brainstorming@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error handling.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 17 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### constraint-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane default thresholds when they have no number in mind, records everything in CONSTRAINTS.md, and watches the diff for a weakened bar — new @ts-ignore or eslint-disable suppressions, skipped or deleted tests, assertions stripped out, unimplement
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 31 KB (SKILL.md 20.5 KB, yük orta)
- **İnceleme:** otomatik

### doubt-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding, when stress-testing a plan for hidden failure modes, when correctness matters more than speed, when working in unfamiliar code, when stakes are high (production auth, security-sensitive logic, a high-stakes migration, irreversible operatio
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### executing-plans  ·  obra/superpowers @ b739a8a  ·  puan 89 (A)

- **Ne yapar:** Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★302965, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 19.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### idea-refine  ·  addyosmani/agent-skills @ aeac41d  ·  puan 86 (A)

- **Ne yapar:** Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-test assumptions before committing to a plan, or when you want to expand options before converging on one. Triggers on "ideate", "refine this idea", or "stress-test my plan".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 40 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### incremental-implementation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling a change out behind a feature flag, when you're about to write a large amount of code at once, or when a task feels too big to land in one step.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 9 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** otomatik

### interview-me  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence about the underlying intent. Use when an ask is underspecified ("build me X" without "for whom" or "why now"), when the user explicitly invokes ("interview me", "grill me", "are we sure?", "stress-test my thinking"), or when you catch yours
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 15 KB (SKILL.md 14.7 KB, yük orta)
- **İnceleme:** otomatik

### plan-writing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work.
- **Teknoloji:** node, python, react, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** otomatik

### planning-and-task-breakdown  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** otomatik

### source-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before implementing it, or when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters.
- **Teknoloji:** api-anahtari, css, html, next.js, node, python, react, svelte, tailwind, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 9.8 KB, yük orta)
- **İnceleme:** otomatik

### spec-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document with objectives and scope, or when requirements are unclear, ambiguous, or only exist as a vague idea. Use when a single requirement spans several independently testable capabilities and needs decomposing into a capability ma
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta)
- **İnceleme:** otomatik

### templates  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Project scaffolding templates for new applications. Use when creating new projects from scratch. Contains 13 templates for various tech stacks.
- **Teknoloji:** next.js, node, python, react, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-plans  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** Use when you have a spec or requirements for a multi-step task, before touching code
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★302965, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik
