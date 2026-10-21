# 03-test-hata-ayiklama — Yazılım Geliştirme

_TDD, hata ayıklama, doğrulama_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/11**

### debugging-and-error-recovery  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you encounter any unexpected error. Use when you need to figure out what broke and why — a systematic approach to finding and fixing the root cause rather than guessing.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### systematic-debugging  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### systematic-debugging@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** ALWAYS use before attempting any fix. Never jump to solutions - investigate root cause first. Use when encountering any technical issue, bug, test failure, or unexpected behavior.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 13 KB (SKILL.md 12.9 KB, yük orta)
- **İnceleme:** otomatik

### systematic-debugging@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues.
- **Teknoloji:** git, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### tdd-workflow  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### test-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing functionality. Use when asked to add tests to a function, fix a bug in it or change its behavior, even when the code is pasted inline and the request
- **Teknoloji:** api-anahtari, css, html, node, playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### test-driven-development@obra  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** Use when implementing any feature or bugfix, before writing implementation code
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 17 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** otomatik

### test-value  ·  tt-a1i/archify @ 25cf370  ·  puan 91 (A)

- **Ne yapar:** Improve test value and feedback cost when auditing slow, flaky, redundant or brittle tests; choosing tests during implementation; or reviewing test changes before a commit or PR. Keep ordinary implementation and pre-commit use scoped to the affected behavior, not a repository-wide audit.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** otomatik

### testing-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Testing patterns and principles. Unit, integration, mocking strategies.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** otomatik

### verification-before-completion  ·  obra/superpowers @ b739a8a  ·  puan 93 (A)

- **Ne yapar:** Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### verify-changes  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Prove code works by running it, not just checking it exists. Verification through execution rather than inspection. Use after writing or modifying code to ensure it actually functions correctly.
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik
