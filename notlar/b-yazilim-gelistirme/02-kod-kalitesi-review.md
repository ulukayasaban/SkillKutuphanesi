# 02-kod-kalitesi-review — Yazılım Geliştirme

_Code review, sadeleştirme, temiz kod_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/13**

### archify-review  ·  tt-a1i/archify @ 25cf370  ·  puan 91 (A)

- **Ne yapar:** Review Archify issues, PRs, or code through value, cost, and impact to support evidence-based maintenance decisions. Use for issue triage, change reviews, and code quality assessments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### archify-tuning  ·  tt-a1i/archify @ 25cf370  ·  puan 89 (A)

- **Ne yapar:** Improve Archify diagram accuracy, visual quality and complete authoring speed with fewer repairs. Use for generation experiments or evaluating changes to layout, routing, diagnostics, authoring instructions and acceptance rules against actual diagrams and agent traces.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 57 KB (SKILL.md 8.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### clean-code  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments
- **Teknoloji:** playwright, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### code-review-and-quality  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 20 KB (SKILL.md 20.5 KB, yük orta)
- **İnceleme:** otomatik

### code-review-checklist  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Code review guidelines covering code quality, security, and best practices.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### code-review-graph  ·  vudovn/ag-kit @ 549ba3d  ·  puan 87 (A)

- **Ne yapar:** Token-efficient code review using Tree-sitter AST graphs and MCP. Cuts AI token usage on large codebases by computing the blast radius of changes instead of reading entire codebases. Uses a SQLite graph database for structural analysis.
- **Teknoloji:** api-anahtari, git, next.js, node, python, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** otomatik

### code-simplification  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulated unnecessary complexity.
- **Teknoloji:** git, python, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 13 KB (SKILL.md 13.2 KB, yük orta)
- **İnceleme:** otomatik

### lint-and-validate  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and project standards. Triggers on keywords: lint, format, check, validate, types, static analysis.
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** otomatik

### pragmatic-review  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** Interactive pragmatic code review focusing on YAGNI and KISS principles. Use when the user asks for a code review, wants to check for over-engineering, or wants a YAGNI/KISS-focused review of changes.
- **Teknoloji:** git, html, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** otomatik

### receiving-code-review  ·  obra/superpowers @ b739a8a  ·  puan 93 (A)

- **Ne yapar:** Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### requesting-code-review  ·  obra/superpowers @ b739a8a  ·  puan 93 (A)

- **Ne yapar:** Use when completing tasks, implementing major features, or before merging to verify work meets requirements
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### simplify-code  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Reduce complexity of over-engineered code. Identify unnecessary abstractions, remove dead code, flatten deep nesting, and simplify logic while preserving behavior.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### simplify-codebase  ·  tt-a1i/archify @ 25cf370  ·  puan 93 (A)

- **Ne yapar:** Simplification audit or authorized codebase simplification whose stated objective is to remove accidental complexity. Use for evidence-backed deletion or consolidation of dead code, duplicate state, redundant APIs or layers, ownerless abstractions, obsolete compatibility or design records, and over-engineering in any language; also use for 代码简化 or 熵回收. Do not use for general code review, onboardin
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** otomatik
