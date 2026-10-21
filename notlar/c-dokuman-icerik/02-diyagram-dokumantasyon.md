# 02-diyagram-dokumantasyon — Doküman ve İçerik

_Diyagram, teknik dokümantasyon, ADR, ortak yazım_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/6**

### archify  ·  tt-a1i/archify @ 25cf370  ·  puan 89 (A)

- **Ne yapar:** Create validated architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree, timeline, and waterfall diagrams as explorable standalone HTML with dark/light themes, motion and image/SVG/WebM export. Accept requirements or Mermaid; inspect repository evidence for code-backed diagrams. Use when visualizing systems, API calls, pipelines, schemas, histories, timings, or everyday ste
- **Teknoloji:** canvas, css, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86907, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7616 KB (SKILL.md 18.4 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### beautiful-mermaid  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram.
- **Teknoloji:** css, html, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 19 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### doc-coauthoring  ·  anthropics/skills @ dbd4588  ·  puan 86 (A)

- **Ne yapar:** Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or 
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182672, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** otomatik

### documentation-and-adrs  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109198, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### documentation-templates  ·  vudovn/ag-kit @ 549ba3d  ·  puan 87 (A)

- **Ne yapar:** Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### json-canvas  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or when the user mentions Canvas files in Obsidian.
- **Teknoloji:** canvas, node, obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** otomatik
