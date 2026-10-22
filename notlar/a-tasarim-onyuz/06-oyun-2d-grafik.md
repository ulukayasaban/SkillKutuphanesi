# 06-oyun-2d-grafik — Tasarım ve Ön Yüz

_Oyun geliştirme, PixiJS, 2D grafik_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **12/87**

### 2d-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** 2D oyun ilkeleri: sprite atlas ve animasyon, tilemap katmanları, 2D fizik şekilleri, kamera tipleri ve ekran sarsıntısı, platformer (coyote time, jump buffer) ve top-down kalıpları.
- **Ne zaman:** 2D oyun mekaniği, sprite/tilemap ve kamera kararlarında hızlı hatırlatma. · **Ne zaman değil:** Motorun gerçek API'si veya render kodu için değil; PixiJS için pixijs-2d.
- **Teknoloji:** 2d, sprite, tilemap
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. 2.1 KB'lık özlü kontrol listesi; faydalı ama sığ (tablolar, kod yok). Dikkat: SKILL.md `game-development/2d-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### 3d-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** 3D oyun ilkeleri: render hattı aşamaları, culling/LOD/batching, shader türleri ve ne zaman özel shader yazılır, 3D çarpışma şekilleri, kamera tipleri, ışık türleri ve LOD stratejisi.
- **Ne zaman:** 3D oyun performans ve kamera kararlarında kısa hatırlatma. · **Ne zaman değil:** Three.js/WebGL kodu için threejs-* skill'leri; derin render bilgisi için değil.
- **Teknoloji:** 3d, shader, lod
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. En sığ olanlardan (2.5 KB): ders kitabı özeti, uygulanabilir yönerge yok; threejs-* skill'leri 3D tarafında çok daha somut. Dikkat: SKILL.md `game-development/3d-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### adopt  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Brownfield audit — do existing artifacts actually work? Numbered migration plan. Unlike /project-stage-detect, checks compliance not existence.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 30 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** otomatik

### architecture-decision  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Create an ADR documenting a technical decision: context, alternatives considered, consequences.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik

### architecture-review  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Traceability matrix mapping GDD requirements to ADRs. Finds gaps, cross-ADR conflicts, engine compatibility. PASS/CONCERNS/NOT ASSESSED/FAIL.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### art-bible  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Author the Art Bible — visual identity gating asset production. Run before /map-systems.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 23.6 KB, yük orta)
- **İnceleme:** otomatik

### asset-audit  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 99 (A)

- **Ne yapar:** Audit assets against naming conventions, file size budgets, format standards. Finds orphaned assets, missing references.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.0 KB, yük orta)
- **İnceleme:** otomatik

### asset-spec  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Per-asset visual specs plus AI generation prompts from GDDs and character profiles. After the art bible.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 20.1 KB, yük orta)
- **İnceleme:** otomatik

### balance-check  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Find balance outliers, broken progressions, degenerate strategies, economy imbalances in formulas and data. 'Check game balance'.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### brainstorm  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Guides the user through finding and choosing a game concept. Use when the user wants game ideas, a new concept, a game jam idea, or to explore other directions, including dropping the current idea and starting over.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 5.1 KB, yük kucuk)
- **İnceleme:** otomatik

### bug-report  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Structured bug report from a description, or analyze code for potential bugs. Reproduction steps, severity.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** otomatik

### bug-triage  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Re-evaluate open bugs — priority vs severity, assign to sprints, surface systemic trends. Run when the count grows.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### changelog  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Auto-generate a changelog from git commits and sprint data. Internal and player-facing versions.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik

### code-review@donchitos  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Architectural code review — coding standards, SOLID, testability, performance concerns.
- **Teknoloji:** api-anahtari, git, node, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 14 KB (SKILL.md 13.6 KB, yük orta)
- **İnceleme:** otomatik

### consistency-check  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Scan GDDs against the entity registry for cross-document conflicts. Grep-first approach targets conflicting sections, different stats.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.0 KB, yük orta)
- **İnceleme:** otomatik

### content-audit  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Audit GDD content counts against what's implemented — planned vs built.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.4 KB, yük orta)
- **İnceleme:** otomatik

### create-architecture  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Author the architecture blueprint before code is written. Validates decisions against the pinned engine, flags knowledge gaps.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### create-control-manifest  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Builds a short list of must-do and never-do coding rules per system from accepted ADRs. Use when the user wants programmer rules or a cheat sheet from the ADRs, or needs it regenerated after ADR changes.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.2 KB, yük orta)
- **İnceleme:** otomatik

### create-epics  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Turns the GDDs and architecture into epics, one per architectural module. Use when the user wants to break the game into epics or plan the work before writing stories. Not for splitting one epic into stories.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### create-stories  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Breaks one epic into implementable stories with acceptance criteria. Use when the user wants stories for an epic or the next batch of work to build. Not for turning the whole design into epics.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** otomatik

### day-one-patch  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Day-one launch patch — focused fix for known issues found after gold master. Mini-sprint with QA gate and rollback.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### design-review  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 91 (A)

- **Ne yapar:** Reviews one design document for completeness, internal consistency, implementability, and design standards. Before handing to programmers.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 27.4 KB, yük buyuk)
- **İnceleme:** otomatik

### design-system@donchitos  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Section-by-section GDD authoring for one system — walks through each required section, cross-references dependencies.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 70 KB (SKILL.md 8.7 KB, yük orta)
- **İnceleme:** otomatik

### dev-story  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Implements one story in code with tests, following its ADRs. Use when the user says to build, implement or start working on a story. Not for checking readiness beforehand or closing the story after.
- **Teknoloji:** git, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 17.4 KB, yük orta)
- **İnceleme:** otomatik

### estimate  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 100 (A)

- **Ne yapar:** Estimate task effort from complexity, dependencies, velocity, risk. Structured estimate with confidence levels.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk)
- **İnceleme:** otomatik

### game-art  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun sanatı ilkeleri: sanat stili karar ağacı (pixel, vektör, el boyaması, PBR, low-poly, cel-shaded) ve karşılaştırma matrisi, 2D/3D varlık hattı araç seçenekleri, renk kararları, 12 animasyon ilkesi, çözünürlük ve adlandırma/klasör düzeni.
- **Ne zaman:** Oyunun görsel stilini seçerken ve varlık hattı/adlandırma standardı kurarken. · **Ne zaman değil:** Gerçek sprite/model üretimi için değil (üretim yapmaz, karar çerçevesi verir).
- **Teknoloji:** pixel-art, blender, aseprite
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Stil karar ağacı ve adlandırma düzeni gerçekten işe yarar (4.9 KB), ama sığ bir çerçeve. Dikkat: SKILL.md `game-development/game-art/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-audio  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun sesi ilkeleri: ses kategorileri ve öncelik hiyerarşisi, SFX katmanlama, müzik durum sistemi ve geçiş teknikleri, uyarlanabilir (vertical/horizontal) ses, 3D konumlandırma, platform formatları, mix seviyeleri ve ducking kuralları.
- **Ne zaman:** Oyunda ses mimarisi ve mix dengesi kararlarında. · **Ne zaman değil:** Ses üretmek için değil (elevenlabs/music skill'leri); motora özel ses API'si için değil.
- **Teknoloji:** web-audio, fmod, wwise
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Mix seviyeleri ve ducking tabloları somut (5.2 KB); yine de ilke düzeyinde. Dikkat: SKILL.md `game-development/game-audio/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-design  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun tasarımı ilkeleri: 30 saniyelik çekirdek döngü, GDD bölümleri, oyuncu motivasyon tipleri ve ödül takvimleri, zorluk dengeleme (flow), ilerleme türleri ve tempo.
- **Ne zaman:** GDD yazarken ve çekirdek döngü/zorluk kararlarında. · **Ne zaman değil:** Seviye tasarımı, hikâye veya ekonomi dengeleme derinliği için değil.
- **Teknoloji:** gdd, game-design
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa (2.6 KB) ve sağlam temel, fakat tamamı genel geçer maddeler. Dikkat: SKILL.md `game-development/game-design/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-development  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun geliştirme orkestratörü: oyun döngüsü (sabit zaman adımı), desen seçim matrisi (state machine, pooling, ECS), girdi soyutlama, 60 FPS bütçesi, AI ve çarpışma stratejisi gibi platformdan bağımsız ilkeleri verir ve platforma/boyuta göre 10 alt skill'e (web, mobil, PC, VR/AR, 2D, 3D, tasarım, multiplayer, sanat, ses) yönlendirir.
- **Ne zaman:** Hangi motor/platformla olursa olsun oyun projesine başlarken ilke ve yönlendirme için; alt skill'lerin hepsi tek klasörde gelir. · **Ne zaman değil:** Somut motor/API kodu aramak için değil (içerik ilke ve tablo düzeyinde). Sadece web 2D render kodu için pixijs-2d, 3D web için threejs-* skill'leri.
- **Teknoloji:** game-design, unity, godot, unreal, phaser
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → birincil
- **Boyut:** 35 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kütüphanedeki tek oyun giriş noktası; kısa (4.7 KB) ve alt skill'leri iç içe taşıyor (10 alt klasör, byte aynı). Dikkat: içerik genel ilke tablolarından ibaret, kod/motor özelliği yok; kalite orta. Yönlendirme `game-development/web-games` gibi iç içe yollara dayanır ve alt klasörler ayrı skill olarak otomatik keşfedilmez; ajan o dosyaları açıkça okumalı. Uygun rol yok (oyun rolü tanımlı değil), role eklenmedi.

### gate-check  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Ready to advance between development phases? PASS/CONCERNS/NOT ASSESSED/FAIL with blockers and required artifacts. 'Can we move to production?
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 89 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### hatch-pet  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging.
- **Teknoloji:** api-anahtari, canvas, css, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 160 KB (SKILL.md 23.3 KB, yük orta)
- **İnceleme:** otomatik

### help  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 99 (A)

- **Ne yapar:** What should I do next? Use when stuck or you don't know what to do.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### hotfix  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Emergency fix bypassing normal sprint process — hotfix branch, approvals tracked, backport verified, full audit trail.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.5 KB, yük orta)
- **İnceleme:** otomatik

### launch-checklist  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Launch readiness across every department: code, content, store, marketing, community, infrastructure, legal, go/no-go sign-offs.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### localize  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Localization pipeline — find hardcoded strings, extract string tables, cultural review, VO, RTL, enforce string freeze.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** otomatik

### map-systems  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Decompose a concept into individual systems, map dependencies, prioritize design order, create the systems index.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 22.1 KB, yük orta)
- **İnceleme:** otomatik

### milestone-review  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Milestone progress review — completeness, quality metrics, risk, go/no-go recommendation. At checkpoints or before a deadline.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** otomatik

### mobile-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Mobil oyun ilkeleri: dokunmatik girdi (44pt hedef), pil/ısıl yönetim, performans hedefleri, App Store / Google Play gereklilikleri ve para kazanma modelleri.
- **Ne zaman:** iOS/Android oyun kısıtlarını ve mağaza gerekliliklerini hatırlamak için. · **Ne zaman değil:** Motor veya SDK entegrasyonu için değil.
- **Teknoloji:** ios, android, touch
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa (2.2 KB) kontrol listesi; mağaza gereksinimleri tarih bağımlı ve hızla eskir. Dikkat: SKILL.md `game-development/mobile-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### multiplayer  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Çok oyunculu ilkeleri: mimari seçimi (dedicated, P2P, host), durum/girdi senkronizasyonu, tahmin-enterpolasyon-uzlaştırma ve lag compensation, bant genişliği azaltma, sunucu otoritesi ve hile önleme, eşleştirme.
- **Ne zaman:** Ağ mimarisi ve senkronizasyon stratejisi kararlarında. · **Ne zaman değil:** Belirli ağ kütüphanesi (Photon, Colyseus, Netcode) kullanımı için değil.
- **Teknoloji:** networking, websocket
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. 'İstemciye güvenme' ilkesini ve teknik adları doğru sıralıyor (2.7 KB); uygulama ayrıntısı yok. Dikkat: SKILL.md `game-development/multiplayer/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### onboard  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Onboarding doc for a new contributor or agent — project state, conventions, priorities relevant to the specified role.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, agents); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### patch-notes  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Player-facing patch notes from git history and changelogs. Translates developer language into player communication.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### pc-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** PC/konsol oyun ilkeleri: motor seçimi (Unity 6, Godot 4, Unreal 5) karar ağacı ve karşılaştırması, Steam özellikleri, konsol sertifikasyonu, kontrolcü girdi soyutlama, profilleme araçları ve motora özel ipuçları.
- **Ne zaman:** PC/konsol için motor seçerken ve platform özelliklerini planlarken. · **Ne zaman değil:** Web oyunları için web-games; motor içi kodlama için değil.
- **Teknoloji:** unity, godot, unreal, steam
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Motor karşılaştırma tablosu işe yarar (2.9 KB) ancak lisans/ücret bilgisi tarih bağımlı ve eskimiş olabilir. Dikkat: SKILL.md `game-development/pc-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### perf-profile  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Performance profiling — find bottlenecks, measure against budgets, produce ranked optimization recommendations.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.0 KB, yük orta)
- **İnceleme:** otomatik

### pixijs-2d  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 73 (B)

- **Ne yapar:** PixiJS v8 ile 2D WebGL/WebGPU render rehberi: Application, sprite/texture, Graphics API, ParticleContainer ile on binlerce parçacık, filtreler ve özel shader filtreleri, sprite sheet animasyonu, metin ve performans kalıpları. Başlangıç şablonu, parçacık/sprite üretici betikler ve referans belgeleri içerir.
- **Ne zaman:** Tarayıcıda 2D oyun, parçacık efekti, yoğun sprite sahnesi veya 3D sahne üstü HUD yapılırken. · **Ne zaman değil:** 3D için Three.js/R3F; basit UI animasyonu için GSAP/Motion; tam oyun motoru (fizik, sahne yönetimi) gerekiyorsa Phaser.
- **Teknoloji:** pixi.js, webgl, webgpu, javascript · **Paketler:** pixi.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** pixijs-2d-render → birincil
- **Boyut:** 253 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kütüphanedeki tek somut 2D render rehberi; v8 API'si (async `app.init`, `Graphics.rect().fill()`, `Particle`) doğru ve kod örnekleri çalışır düzende. Dikkat: büyük (20.6 KB SKILL.md, 935 satır; klasör 280 KB). Şablon ve betikler PixiJS'i sürümsüz `https://pixijs.download/release/pixi.js` CDN adresinden yüklüyor (sürüm sabitlenmemiş). 'Related Skills' bölümü var olmayan adlara (threejs-webgl, motion-framer) başvuruyor. Son güncelleme 335 gün önce. Betikler yalnız stdlib python, HTML/JS şablonu üretir; kurulum/anahtar yok. Oyun rolü olmadığı için role eklenmedi.

### playtest-report  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Structured playtest report template, or turn existing playtest notes into structured feedback.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik

### project-stage-detect  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Analyze project state, detect stage, identify gaps, recommend next steps. 'Where are we in development?
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta)
- **İnceleme:** otomatik

### propagate-design-change  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Finds architecture decisions (ADRs) made stale by a changed GDD and walks through resolving each. Use when the user changed a number or rule in a GDD and asks which ADRs or architecture decisions are now out of date.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** otomatik

### prototype  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Concept prototype before GDDs — throwaway HTML, Engine or Paper build, PROCEED/PIVOT/KILL/NOT ASSESSED. After /brainstorm and /setup-engine.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 5.3 KB, yük kucuk)
- **İnceleme:** otomatik

### qa-plan  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** QA test plan for a sprint — classifies stories by Logic/Integration/Visual/UI, covers automated tests, manual cases, smoke scope.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 17.1 KB, yük orta)
- **İnceleme:** otomatik

### quick-design  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Lightweight spec for small changes — tuning adjustments, minor mechanics. Embeds directly into stories; skips full GDD.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.5 KB, yük orta)
- **İnceleme:** otomatik

### regression-suite  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Map test coverage to GDD critical paths, find fixed bugs lacking regression tests, flag drift from new features.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 13.8 KB, yük orta)
- **İnceleme:** otomatik

### release-checklist  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Pre-release checklist — build verification, certification requirements, store metadata, launch readiness.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** otomatik

### retrospective  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Sprint or milestone retrospective from completed work, velocity, blockers. Actionable insights for the next iteration.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### reverse-document  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Generate missing design or architecture docs from existing implementation — works backwards from code and prototypes.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** otomatik

### review-all-gdds  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Holistic cross-GDD review — contradictions between systems, dominant strategies, economic imbalance, cognitive overload, pillar drift.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 39 KB (SKILL.md 7.3 KB, yük kucuk)
- **İnceleme:** otomatik

### scope-check  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 100 (A)

- **Ne yapar:** Scope creep check — current scope versus the original plan. Flags additions, quantifies bloat, recommends cuts. 'Any scope creep?
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik

### security-audit@donchitos  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Security audit — save tampering, cheat vectors, network exploits, data exposure, input validation. Before public or multiplayer release.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 22 KB (SKILL.md 21.8 KB, yük orta)
- **İnceleme:** otomatik

### settings  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** View or change project config — effective merged values, or set locally in project.local.yaml.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, hooks); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 21.0 KB, yük orta)
- **İnceleme:** otomatik

### setup-engine  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Configure engine and version. Pins it in CLAUDE.md; WebSearch fills reference docs when the version is beyond LLM training data.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 86 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** otomatik

### skill-improve  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Improve a skill via a test-fix-retest loop — static checks, targeted fixes, keep or revert on score change.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### skill-test  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 91 (A)

- **Ne yapar:** Validate skill files for structural compliance and behavioral correctness. Four modes: static linter, spec, category rubric, audit.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (, agents); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 28.1 KB, yük buyuk)
- **İnceleme:** otomatik

### smoke-check  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Critical-path smoke gate before QA hand-off — runs the automated suite. A failed check means the build is not QA-ready.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### soak-test  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Soak test protocol for extended play — what to observe and log for slow leaks, fatigue, late-appearing edge cases.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** otomatik

### sprint-plan  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** New or updated sprint plan from the current milestone, completed work, and available capacity.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 19.2 KB, yük orta)
- **İnceleme:** otomatik

### sprint-status  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 99 (A)

- **Ne yapar:** Fast, concise sprint snapshot — burndown and emerging risks for situational awareness. 'How is the sprint going?
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### start@donchitos  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Guides a first-time user through onboarding and picks the right workflow. Use when the user is new, just cloned or installed the studio, has no idea or engine yet, asks where to begin, or wants to bring in an existing game.
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 12 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### story-done  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Closes a finished story: verifies each acceptance criterion, checks for design or ADR deviations and updates its status. Use when the user says a story is done, finished or ready to close.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** otomatik

### story-readiness  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Checks whether a story is ready to implement: clear acceptance criteria, no open questions, valid ADR and dependencies. Use when the user asks if a story, or the sprint's stories, are ready to start or build.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 15.1 KB, yük orta)
- **İnceleme:** otomatik

### team-audio  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the audio team — audio-director, sound-designer, technical-artist, gameplay-programmer — direction through implementation.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 17.2 KB, yük orta)
- **İnceleme:** otomatik

### team-combat  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the combat team — game-designer, gameplay-programmer, ai-programmer, technical-artist, sound-designer, qa-tester — design through implement and validate.
- **Teknoloji:** api-anahtari, node, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 18.7 KB, yük orta)
- **İnceleme:** otomatik

### team-level  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the level team — level-designer, narrative-director, world-builder, art-director, systems-designer, qa-tester — for complete area creation.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 18.7 KB, yük orta)
- **İnceleme:** otomatik

### team-live-ops  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the live-ops team — live-ops-designer, economy-designer, analytics-engineer, community-manager, writer — for a season or live event.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 16.6 KB, yük orta)
- **İnceleme:** otomatik

### team-narrative  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the narrative team — narrative-director, writer, world-builder, level-designer — for story, world lore, narrative-driven levels.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** otomatik

### team-polish  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the polish team — performance-analyst, technical-artist, sound-designer, qa-tester — to optimize and harden a feature or area.
- **Teknoloji:** api-anahtari, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 17.9 KB, yük orta)
- **İnceleme:** otomatik

### team-qa  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 91 (A)

- **Ne yapar:** Orchestrate the QA team through a full testing cycle — qa-lead strategy and test plan, qa-tester case writing, execution, sign-off.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 25.5 KB, yük buyuk)
- **İnceleme:** otomatik

### team-release  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the release team — release-manager, qa-lead, devops-engineer, producer — to execute a release from candidate to deployment.
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 22.0 KB, yük orta)
- **İnceleme:** otomatik

### team-ui  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Orchestrate the UI team through the UX pipeline — authoring, visual design, implementation, review, polish. Uses /ux-design, /ux-review, studio templates.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 22.2 KB, yük orta)
- **İnceleme:** otomatik

### tech-debt@donchitos  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Track, categorize and prioritize technical debt across the codebase — scans for debt indicators, maintains a register.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 10 KB (SKILL.md 9.9 KB, yük orta)
- **İnceleme:** otomatik

### test-evidence-review  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Quality review of test files and evidence — goes beyond existence, evaluates assertion coverage. ADEQUATE/INCOMPLETE/MISSING/NOT ASSESSED per story.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### test-flakiness  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Find flaky tests from CI logs — aggregates pass rates, spots intermittent failures, recommends quarantine. After multiple runs.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** otomatik

### test-helpers  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Generate engine-specific test helper libraries — assertion utilities, factory functions, mocks in the engine's test folder. Reduces boilerplate.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 17.5 KB, yük orta)
- **İnceleme:** otomatik

### test-setup  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 96 (A)

- **Ne yapar:** Scaffold the test framework and CI — tests/ directory, engine test runner, GitHub Actions workflow. Once, before the first sprint.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** otomatik

### ux-design  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Section-by-section UX spec authoring for a screen, flow or HUD. Reads the player journey to provide context; also project-wide accessibility.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 48 KB (SKILL.md 9.5 KB, yük orta)
- **İnceleme:** otomatik

### ux-review  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 99 (A)

- **Ne yapar:** Validate a UX spec, HUD design or pattern library — accessibility, GDD alignment, readiness. APPROVED / NOT ASSESSED / NEEDS REVISION / MAJOR REVISION NEEDED.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta)
- **İnceleme:** otomatik

### vertical-slice  ·  Donchitos/Claude-Code-Game-Studios @ 05ad7c8  ·  puan 94 (A)

- **Ne yapar:** Pre-production validation — end-to-end build to confirm the full loop is achievable before committing to Production. After GDDs, architecture, UX specs.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, model, user-invocable (Codex bunları yok sayar)
- **Geliştirici:** Donchitos (kisi, ★27158, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 20.8 KB, yük orta)
- **İnceleme:** otomatik

### vr-ar  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** VR/AR ilkeleri: platformlar (Quest, PCVR, WebXR, ARKit/ARCore), hareket hastalığı önleme ve konfor ayarları, kare hızı hedefleri, kontrolcü/el takibi etkileşimi, ölçek ve derinlik ipuçları.
- **Ne zaman:** VR/AR projesinde konfor ve performans hedeflerini belirlerken. · **Ne zaman değil:** WebXR kodu için aframe-webxr (05); cihaza özel SDK için değil.
- **Teknoloji:** webxr, quest, arkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. İlkeler doğru ama çok kısa (2.3 KB); cihaz metrikleri hızla eskir. Başlık 2D grafik kategorisine uymuyor (VR/AR 3D) ama oyun ailesi için kalabilir. Dikkat: SKILL.md `game-development/vr-ar/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### web-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Tarayıcı oyunu ilkeleri: çatı seçimi (Phaser, PixiJS, Three.js, Babylon.js), WebGPU benimseme durumu, tarayıcı kısıtları ve optimizasyon sırası, varlık sıkıştırma (KTX2, Draco, Opus), PWA ve Web Audio kuralları.
- **Ne zaman:** Web tabanlı oyun için çatı ve varlık/performans stratejisi seçerken. · **Ne zaman değil:** Kod örneği arıyorsan değil; PixiJS için pixijs-2d, 3D için threejs-*.
- **Teknoloji:** phaser, pixi.js, three.js, webgpu, pwa
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Web oyunu için en uygulanabilir ilke seti (3.0 KB); tarayıcı destek yüzdeleri (~%73 WebGPU) tarih bağımlı. Dikkat: SKILL.md `game-development/web-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.
