# 04-bilimsel-yazim-literatur — Bilim, Araştırma ve Mühendislik

_Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendirmesi, bilimsel sunum_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/124**

### ablation-planner  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Use when main results pass result-to-claim (claim_supported=yes or partial) and ablation studies are needed for paper submission.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### alphaxiv  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Quick single-paper lookup via AlphaXiv LLM-optimized summaries with tiered source fallback. Use when user says "explain this paper", "summarize paper", pastes an arXiv/AlphaXiv URL, or provides a bare arXiv ID for quick understanding - not for broad literature search.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### analyze-results  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Analyze ML experiment results, compute statistics, generate comparison tables and insights. Use when user says "analyze results", "compare", or needs to interpret experimental data.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** otomatik

### arxiv  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Search, download, and summarize academic papers from arXiv. Use when user says "search arxiv", "download paper", "fetch arxiv", "arxiv search", "get paper pdf", or wants to find and save papers from arXiv to the local paper library.
- **Teknoloji:** git, html, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.1 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### auto-paper-improvement-loop  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Autonomously improve a generated paper via GPT-6-Astra xhigh review → implement fixes → recompile, for 2 rounds. Use when user says \"改论文\", \"improve paper\", \"论文润色循环\", \"auto improve\", or wants to iteratively polish a generated paper.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 42 KB (SKILL.md 41.9 KB, yük buyuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### auto-review-loop  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 79 (B)

- **Ne yapar:** Autonomous multi-round research review loop. In Copilot CLI it defaults to the native complementary rubber-duck subagent with host-event model evidence; elsewhere it uses Codex, while explicit external reviewer overrides remain available. Implements fixes and re-reviews until a policy-approved positive assessment or max rounds is reached.
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 74 KB (SKILL.md 73.8 KB, yük buyuk) · **Kırık bağlantı:** 6
- **İnceleme:** otomatik

### auto-review-loop-llm  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 82 (A)

- **Ne yapar:** Autonomous research review loop using any OpenAI-compatible LLM API. Configure via llm-chat MCP server or environment variables. Trigger with "auto review loop llm" or "llm review".
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### auto-review-loop-minimax  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 82 (A)

- **Ne yapar:** Autonomous multi-round research review loop using MiniMax API. Use when you want to use MiniMax instead of Codex MCP for external review. Trigger with "auto review loop minimax" or "minimax review".
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.7 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### autoskill  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Analyzes user-requested Screenpipe history windows to detect repeated research workflows, match existing scientific skills, and stage new skill drafts or composition recipes for review. Requires a reachable Screenpipe HTTP API, normally on localhost:3030. Detection and embedding inference run locally; the selected LLM receives redacted app/title cluster summaries and matched skill descriptions. Us
- **Teknoloji:** api-anahtari, ffmpeg, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 59 KB (SKILL.md 16.5 KB, yük orta)
- **İnceleme:** otomatik

### bgpt-paper-search  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 99 (A)

- **Ne yapar:** Searches BGPT scientific papers by topic or DOI and retrieves claim-level evidence extracted from full text, including experiments, reported statistics, scope, limitations, and provenance. Use for literature reviews, evidence synthesis, and finding experimental details beyond abstracts.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### citation-audit  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Zero-context verification that every bibliographic entry in the paper is real, correctly attributed, and used in a context the cited paper actually supports — catching hallucinated authors, wrong years, fabricated venues, version mismatches, and wrong-context citations. Use when user says \"审查引用\", \"check citations\", \"citation audit\", \"verify references\", \"引用核对\", or before submission to en
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 31.4 KB, yük buyuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### citation-crosscheck  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Double-blind bibliographic cross-check: one agent extracts each cited entry verbatim from the local .bib, a second independently re-fetches the same paper's record from the web while blind to the .bib, and a third extractor emits a mechanical field-by-field delta to catch dropped/re-ordered authors, wrong years, wrong venues, and bad DOIs/arXiv ids. The main agent (never a shard) assigns the MATCH
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 118 KB (SKILL.md 35.7 KB, yük buyuk) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### citation-management  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be used when you need to find papers, verify citation information, convert DOIs to BibTeX, or ensure reference accuracy in scientific writing.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 293 KB (SKILL.md 16.2 KB, yük orta)
- **İnceleme:** otomatik

### claims-drafting  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Draft patent claims for an invention. Use when user says \"撰写权利要求\", \"draft claims\", \"写权利要求书\", \"claim drafting\", or wants to create patent claims. The core skill of the patent pipeline.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### comm-lit-review  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Communications-domain literature review with Claude-style knowledge-base-first retrieval. Use when the task is about communications, wireless, networking, satellite/NTN, Wi-Fi, cellular, transport protocols, congestion control, routing, scheduling, MAC/PHY, rate adaptation, channel estimation, beamforming, or communication-system research and the user wants papers, related work, a survey, or a lan
- **Teknoloji:** obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta)
- **İnceleme:** otomatik

### consciousness-council  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Structures a multi-perspective council exercise for decisions, research trade-offs, and creative challenges. Simulates thinking archetypes, separates evidence from assumptions and values, and synthesizes a conditional recommendation. Use when the user requests a council, panel, devil's advocate analysis, "mind council", or deliberate comparison of perspectives on a difficult choice.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 13.6 KB, yük orta)
- **İnceleme:** otomatik

### database-lookup  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 94 (A)

- **Ne yapar:** Queries documented public database APIs with explicit endpoints, filters, pagination, and provenance. Used when a scientific, regulatory, financial, or other database-backed fact must be retrieved reproducibly from a named source rather than inferred from general knowledge.
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 397 KB (SKILL.md 26.9 KB, yük buyuk)
- **İnceleme:** otomatik

### deepxiv  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Search and progressively read open-access academic papers through DeepXiv. Use when the user wants layered paper access, section-level reading, trending papers, or DeepXiv-backed literature retrieval.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.5 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### dse-loop  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Autonomous design space exploration loop for computer architecture and EDA. Runs a program, analyzes results, tunes parameters, and iterates until objective is met or timeout. Use when user says \"DSE\", \"design space exploration\", \"sweep parameters\", \"optimize\", \"find best config\", or wants iterative parameter tuning.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 13.8 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### embodiment-description  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Write detailed embodiment descriptions for patent specifications. Use when user says \"撰写实施例\", \"write embodiment\", \"实施例描述\", \"detailed description\", or wants to describe how to practice an invention.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### exa-search  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Searches scientific and technical web content with Exa and extracts page or PDF text from URLs in batches. Supports scholarly discovery with the publication category and academic domain filters. Applies to requests to search the web, look up current research, fetch a page, or extract an article using Exa.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 6.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### exa-search@wanshuiyin  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** AI-powered web search via Exa with content extraction. Use when user says "exa search", "web search with content", "find similar pages", or needs broad web results beyond academic databases (arXiv, Semantic Scholar).
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### experiment-audit  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Audit experiment integrity before claiming results. Uses cross-model review (external reviewer backend) to check for fake ground truth, score normalization fraud, phantom results, and insufficient scope. Use when user says \"审计实验\", \"check experiment integrity\", \"audit results\", \"实验诚实度\", or after experiments complete before writing claims.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.4 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### experiment-bridge  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Workflow 1.5: Bridge between idea discovery and auto review. Reads EXPERIMENT_PLAN.md, implements experiment code, deploys to GPU, collects initial results. Use when user says \"实现实验\", \"implement experiments\", \"bridge\", \"从计划到跑实验\", \"deploy the plan\", or has an experiment plan ready to execute.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 19.6 KB, yük orta) · **Kırık bağlantı:** 5
- **İnceleme:** otomatik

### experiment-plan  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Turn a refined research proposal or method idea into a detailed, claim-driven experiment roadmap. Use after `research-refine`, or when the user asks for a detailed experiment plan, ablation matrix, evaluation protocol, run order, compute budget, or paper-ready validation that supports the core problem, novelty, simplicity, and any LLM / VLM / Diffusion / RL-based contribution.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### experiment-queue  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** SSH job queue for multi-seed/multi-config ML experiments with OOM-aware retry, stale-screen cleanup, and wave-transition race prevention. Use when user says "batch experiments", "队列实验", "run grid", "multi-seed sweep", "auto-chain experiments", or when /run-experiment is insufficient for 10+ jobs that need orchestration.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 39 KB (SKILL.md 19.6 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### experimental-design  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Designs experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking, and laying out treatment combinations so results are interpretable. Use whenever someone is planning a study, asks how to assign subjects/samples to groups, mentions randomization, blocking, stratification, controls, factorial or fractional-factorial designs, design of experiments (DOE), screening 
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 65 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### feishu-notify  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Send notifications to Feishu/Lark. Internal utility used by other skills, or manually via /feishu-notify. Use when user says \"发飞书\", \"notify feishu\", or other skills need to send status updates.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** otomatik

### figure-description  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Process user-provided patent figures and generate formal drawing descriptions. Use when user says \"附图处理\", \"figure description\", \"附图说明\", \"drawings description\", or wants to describe patent figures with reference numerals.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** otomatik

### figure-spec  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate deterministic publication-quality architecture, workflow, and pipeline diagrams from structured JSON (FigureSpec) into editable SVG. Use when user says \"架构图\", \"workflow 图\", \"pipeline 图\", \"确定性矢量图\", \"figure spec\", \"draw architecture\", or needs precise, editable, publication-ready vector diagrams. Preferred over AI illustration for formal architecture/workflow figures.
- **Teknoloji:** api-anahtari, canvas, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 11.8 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### firecrawl-search  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Web search and page scraping via Firecrawl, returning full-page markdown. Use when user says "firecrawl search", "firecrawl scrape" or "/firecrawl-search".
- **Teknoloji:** api-anahtari, git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### formula-derivation  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Structures and derives research formulas when the user wants to 推导公式, build a theory line, organize assumptions, turn scattered equations into a coherent derivation, or rewrite theory notes into a paper-ready formula document. Use when the derivation target is not yet fully fixed, the main object still needs to be chosen, or the user needs a coherent derivation package rather than a finished theor
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### gemini-search  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Search research papers via Gemini for broad literature discovery. Use when user says "gemini search", "gemini papers", "search with gemini", or wants AI-powered literature discovery beyond arXiv/Semantic Scholar indexes.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.1 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### generate-image  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Generates or edits images with AI models through the OpenRouter Image API (Gemini, Seedream, Recraft, GPT-Image, Riverflow). Use for photos, illustrations, artwork, concept art, visual assets, logos, and image editing or compositing from reference images. For flowcharts, circuits, pathways, and other technical diagrams, use the scientific-schematics skill instead.
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 64 KB (SKILL.md 17.4 KB, yük orta)
- **İnceleme:** otomatik

### grant-proposal  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Draft a structured grant proposal from research ideas and literature. Supports KAKENHI (Japan), NSF (US), NSFC (China, including 面上/青年/优青/杰青/海外优青/重点), ERC (EU), DFG (Germany), SNSF (Switzerland), ARC (Australia), NWO (Netherlands), and generic formats. Use when user says \"write grant\", \"grant proposal\", \"申請書\", \"write KAKENHI\", \"科研費\", \"基金申请\", \"写基金\", \"NSF proposal\", or wants to turn 
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 35 KB (SKILL.md 35.3 KB, yük buyuk) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### hypogenic  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted hypothesis generation from labeled text datasets. Use for the `hypogenic` package, its task configs, hypothesis banks, or HypoBench datasets—not for manual hypothesis formulation or scientific validation.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 150 KB (SKILL.md 14.0 KB, yük orta)
- **İnceleme:** otomatik

### hypothesis-generation  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Formulates evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions, measurements, and preregistration-ready analysis plans. Used when turning observations or preliminary findings into transparent, testable research plans without treating hypotheses as facts.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 260 KB (SKILL.md 16.2 KB, yük orta)
- **İnceleme:** otomatik

### idea-creator  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Generate and rank research ideas given a broad direction. Use when user says "找idea", "brainstorm ideas", "generate research ideas", "what can we work on", or wants to explore a research area for publishable directions.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 34.4 KB, yük buyuk) · **Kırık bağlantı:** 10
- **İnceleme:** otomatik

### idea-discovery  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Workflow 1: Full idea discovery pipeline to go from a broad research direction to validated, pilot-tested ideas. Use when user says \"找idea全流程\", \"idea discovery pipeline\", \"从零开始找方向\", or wants the complete idea exploration workflow.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 27.7 KB, yük buyuk) · **Kırık bağlantı:** 6
- **İnceleme:** otomatik

### idea-discovery-robot  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Workflow 1 adaptation for robotics and embodied AI. Orchestrates robotics-aware literature survey, idea generation, novelty check, and critical review to go from a broad robotics direction to benchmark-grounded, simulation-first ideas. Use when user says \"robotics idea discovery\", \"机器人找idea\", \"embodied AI idea\", \"机器人方向探索\", \"sim2real 选题\", or wants ideas for manipulation, locomotion, navig
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.6 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### infographics  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Creates and reviews infographics with Nano Banana 2 via OpenRouter. Use for statistical summaries, timelines, comparisons, processes, and visual explanations with supplied data or optional Sonar research. Supports ten layouts, eight style presets, reference images, and accessible palette starting points.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 154 KB (SKILL.md 15.0 KB, yük orta)
- **İnceleme:** otomatik

### integrity-forensics  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Run the Anti-Autoresearch integrity-forensics sweep (span-anchored evidence ledger → GPT auditors propose findings → a rules-only reporter that lists every proposal with what the auditor said about it) against a paper via a SHA-pinned thin launcher — then convert the verdict into a typed policy gate (BLOCK/WARN/NO_NEW_BLOCKER) and an append-only obligations ledger. Use when user says \"integrity f
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### interview-cheatsheet  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate a long-form Chinese interview-prep cheat sheet on a specific ML/LLM topic — formulas with derivations, from-scratch PyTorch code, comparison tables, and 25 高频面试题 (L1 必会 / L2 进阶 / L3 顶级 lab). Use when the user says '写面试 cheat sheet', '写一份 X 教程', '帮我准备 Y 面试题', '出一份 X 速查', or wants a 600-1000 line Chinese tutorial on a specific ML topic.
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.2 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### invention-structuring  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Structure a raw invention idea into a formal invention disclosure. Use when user says \"构建发明\", \"structure invention\", \"发明构建\", \"invention disclosure\", or wants to formalize a rough idea into a patent-ready structure.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### iso-standards-readiness  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Prepares and structurally reviews readiness evidence for ISO management-system and laboratory-competence standards - ISO 13485 medical device QMS, ISO 14971 device risk management, ISO/IEC 17025 testing and calibration laboratories, and ISO 15189 medical laboratories. Use when organizing declared scope, controlled documents, risk-management files, scope of accreditation, traceability, CAPA, extern
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 267 KB (SKILL.md 17.9 KB, yük orta)
- **İnceleme:** otomatik

### jurisdiction-format  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Compile patent application into jurisdiction-specific filing format. Use when user says \"格式转换\", \"jurisdiction format\", \"国家格式\", \"compile patent\", or wants formatted patent documents for CN/US/EP filing.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik

### keenable-search  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Keyless web search and page fetch via Keenable. Use when user says "keenable search", "web search without an API key", "fetch this page as markdown", or needs broad web results beyond academic databases (arXiv, Semantic Scholar) with no search API key set up.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### kill-argument  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Two-thread adversarial review: a fresh reviewer constructs the strongest 200-word rejection memo, then a second fresh reviewer defends the paper point-by-point and surfaces still-unresolved critical issues. Use when user says \"kill argument\", \"adversarial review\", \"hostile review\", \"rebuttal preparation\", \"reviewer-2 simulation\", or before submitting a theory paper that has already passe
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 25.5 KB, yük buyuk) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### latex-posters  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Creates research posters in LaTeX using beamerposter, tikzposter, or baposter. Use for conference posters, academic presentations, multi-column scientific layouts, figure integration, typography, compilation, and PDF preflight.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 207 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** otomatik

### lean-formalize  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Develop and verify a mathematical proof in Lean, continue an incomplete Lean project, or audit whether it proves the original statement. Connect actual inputs to intermediate lemmas, assemble the target theorem, check its transitive axioms, and provide a reproducible handoff. Use when Lean is requested or a specific proof obligation benefits from formal verification; use proof-writer for ordinary 
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 53 KB (SKILL.md 22.3 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### liteparse  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Local document and PDF parsing that returns spatial text with bounding boxes. Use for extracting text from PDFs, DOCX, Office files, and images; running OCR on scans; producing layout-preserved JSON for RAG; batch-ingesting folders of papers; or rendering pages to PNG for multimodal agents. Distinguishing capabilities are spatial text boxes, Markdown, page raster output, and local parsing with opt
- **Teknoloji:** html, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### literature-review  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Conducts systematic, scoping, and narrative literature reviews using PubMed, arXiv, bioRxiv, Semantic Scholar, and other appropriate sources. Use for research synthesis, reproducible literature searches, screening, citation checking, or preparing Markdown and PDF reviews. Tracks search coverage, records versus studies, and evidence limitations; supports meta-analysis planning but does not supply a
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 128 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** otomatik

### markdown-mermaid-writing  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Writes scientific Markdown documentation and Mermaid diagrams for workflows, relationships, timelines, and schemas. Provides syntax references, document templates, accessibility guidance, and version-aware rendering checks. Use when a user requests Markdown, Mermaid, or a text-based structural diagram; quantitative scientific figures require suitable plotting tools.
- **Teknoloji:** api-anahtari, git, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 288 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### market-research-reports  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Builds evidence-traceable market research reports and assumption-driven market sizing or forecast scenarios. Use for market definition, industry and customer evidence, competitive landscapes, TAM/SAM/SOM reconciliation, forecast sensitivity, and auditable report scaffolds.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 189 KB (SKILL.md 15.0 KB, yük orta)
- **İnceleme:** otomatik

### markitdown  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Converts heterogeneous documents and selected URIs to Markdown with Microsoft MarkItDown for text analysis, search, and LLM/RAG ingestion. Covers safe local conversion, streams, Office/PDF/data formats, batch workflows, plugins, vision OCR, Azure extraction, and the official MCP server.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 110 KB (SKILL.md 11.9 KB, yük orta)
- **İnceleme:** otomatik

### mermaid-diagram  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Generate Mermaid diagrams from user requirements. Supports flowcharts, sequence diagrams, class diagrams, ER diagrams, Gantt charts, and 18 more diagram types.
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### meta-apply  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Privileged applier that LANDS meta-optimize / corpus-audit patches the user approved — the ONLY skill permitted to mutate the skill corpus from a self-modification proposal, with cross-model jury and human approval at landing. Use when the user says \"meta apply\", \"/meta-apply\", \"land the staged patches\", \"应用优化\", after a /meta-optimize run.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.8 KB, yük orta) · **Kırık bağlantı:** 5
- **İnceleme:** otomatik

### meta-optimize  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 82 (A)

- **Ne yapar:** Analyze ARIS usage logs and propose optimizations to SKILL.md files, reviewer prompts, and workflow defaults. Outer-loop harness optimization inspired by Meta-Harness (Lee et al., 2026). Use when user says \"优化技能\", \"meta optimize\", \"improve skills\", \"分析使用记录\", or wants to optimize ARIS's own harness components based on accumulated experience.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 24.3 KB, yük orta) · **Kırık bağlantı:** 7
- **İnceleme:** otomatik

### monitor-experiment  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Monitor running experiments, check progress, collect results. Use when user says "check results", "is it done", "monitor", or wants experiment output.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### novelty-check  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Verify research idea novelty against recent literature. Use when user says "查新", "novelty check", "有没有人做过", "check novelty", or wants to verify a research idea is novel before implementing.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.1 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### open-notebook  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Organizes research with the self-hosted Open Notebook alternative to NotebookLM. Supports source ingestion (PDFs, web pages, audio, video, and Office documents), cited document chat, text and vector search, notes, custom transformations, and multi-speaker podcasts. Use when automating Open Notebook through its REST API or configuring its local or cloud AI providers, including OpenAI, Anthropic, Go
- **Teknoloji:** api-anahtari, docker, next.js, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 66 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** otomatik

### openalex  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Search academic papers via OpenAlex API for open citation data, institutional affiliations, and funding information. Use when user says "openalex search", "search openalex", "open citation graph", or wants comprehensive academic metadata beyond arXiv/Semantic Scholar.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.8 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### overleaf-sync  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Two-way sync between a local paper directory and an Overleaf project, so ARIS audit/edit workflows stay on the local copy while collaborators edit in the Overleaf web UI. Use when user says \"同步 overleaf\", \"overleaf sync\", \"推送到 overleaf\", \"connect overleaf\", \"Overleaf 桥接\", \"pull overleaf\", \"push overleaf\", or wants to bridge their ARIS paper directory with an Overleaf project.
- **Teknoloji:** api-anahtari, git _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** otomatik

### paper-claim-audit  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Zero-context verification that every number, comparison, and scope claim in the paper matches raw result files. Uses a fresh cross-model reviewer with NO prior context to prevent confirmation bias. Use when user says \"审查论文数据\", \"check paper claims\", \"verify numbers\", \"论文数字核对\", or before submission to ensure paper-to-evidence fidelity.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.0 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### paper-compile  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Compile LaTeX paper to PDF, fix errors, and verify output. Use when user says \"编译论文\", \"compile paper\", \"build PDF\", \"生成PDF\", or wants to compile LaTeX into a submission-ready PDF.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.8 KB, yük orta)
- **İnceleme:** otomatik

### paper-figure  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate publication-quality figures and tables from experiment results. Use when user says \"画图\", \"作图\", \"generate figures\", \"paper figures\", or needs plots for a paper.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.4 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### paper-illustration  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 86 (A)

- **Ne yapar:** Generate publication-quality AI illustrations for academic papers using Gemini image generation. Creates architecture diagrams, method illustrations with Claude-supervised iterative refinement loop. Use when user says \"生成图表\", \"画架构图\", \"AI绘图\", \"paper illustration\", \"generate diagram\", or needs visual figures for papers.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 32.5 KB, yük buyuk)
- **İnceleme:** otomatik

### paper-illustration-image2  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate publication-quality academic illustrations through a local Codex app-server bridge that uses Codex native image generation. This is a separate experimental alternative to `paper-illustration`, intended for Claude Code users who want a GPT-image-style renderer without modifying the original skill.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 19.4 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### paper-lookup  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 94 (A)

- **Ne yapar:** Searches 18 scholarly APIs for papers, preprints, citations, open-access full text, repository records, and journal OA status, and returns results with reproducible provenance. Covers PubMed, PMC, Europe PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall, OpenCitations, PubTator3, Zenodo, Figshare, ROR, BioStudies, and DOAJ. Use when searching for papers, citations
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 177 KB (SKILL.md 25.5 KB, yük buyuk)
- **İnceleme:** otomatik

### paper-plan  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate a structured paper outline from review conclusions and experiment results. Use when user says \"写大纲\", \"paper outline\", \"plan the paper\", \"论文规划\", or wants to create a paper plan before writing.
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 21.5 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### paper-poster  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** DEPRECATED — superseded by /paper-poster-html. Kept only as a redirect for muscle memory; do not use for new posters.
- **Teknoloji:** canvas, css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### paper-poster-html  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 82 (A)

- **Ne yapar:** DEFAULT poster pipeline — build an academic conference poster (ICML/NeurIPS/ICLR/CVPR/...) as a single HTML/CSS file with measurement-driven hard gates, real paper figures, a two-hue design-token system, and print-ready PDF via headless Chromium. Use when the user says \"做海报\", \"poster\", \"conference poster\", \"paper poster\", or asks to design/redo a research poster. Supersedes the retired LaT
- **Teknoloji:** canvas, css, html, playwright, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 456 KB (SKILL.md 19.0 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### paper-slides  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Generate conference presentation slides (beamer LaTeX → PDF + editable PPTX) from a compiled paper, with speaker notes and full talk script. Use when user says \"做PPT\", \"做幻灯片\", \"make slides\", \"conference talk\", \"presentation slides\", \"生成slides\", \"写演讲稿\", or wants beamer slides for a conference talk.
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 23.6 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### paper-talk  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** End-to-end conference talk pipeline: paper → slide outline → Beamer + PPTX → per-page polish → assurance checks (claim / citation / anonymity) → final export and report. Default-good for academic conference talks (NeurIPS / ICML / ICLR / VALSE / 投稿 talks). Trigger phrases: \"做 talk\", \"做 PPT 全流程\", \"talk pipeline\", \"end-to-end slides\", \"做演讲\", \"conference talk full workflow\". Use when the 
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 21.2 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### paper-write  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Draft LaTeX paper section by section from an outline. Use when user says \"写论文\", \"write paper\", \"draft LaTeX\", \"开始写\", or wants to generate LaTeX content from a paper plan.
- **Teknoloji:** git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 382 KB (SKILL.md 39.0 KB, yük buyuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### paper-writing  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 79 (B)

- **Ne yapar:** Workflow 3: Full paper writing pipeline that goes from a narrative report to a polished, submission-ready PDF. Use when user says \"写论文全流程\", \"write paper pipeline\", \"从报告到PDF\", \"paper writing\", or wants the complete paper generation workflow.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 51 KB (SKILL.md 51.4 KB, yük buyuk) · **Kırık bağlantı:** 5
- **İnceleme:** otomatik

### paperclip  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Searches and reads biomedical papers, FDA/PMDA/EMA documents, clinical trials, and protein records with the GXL Paperclip CLI and Python SDK. Supports source-scoped search, full-text grep, metadata SQL, map/reduce extraction, figure analysis, optional repositories and claim verification, and line-pinned citations. Use when a task names GXL paperclip, asks to install or authenticate it, or requests
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 70 KB (SKILL.md 12.7 KB, yük orta)
- **İnceleme:** otomatik

### paperzilla  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Reads projects, searches project feeds, and retrieves recommendations and canonical papers in Paperzilla through the pz CLI. Supports recent recommendations, paper details, markdown-based summaries, recommendation feedback, JSON export, and Atom feed URLs.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 9.1 KB, yük orta)
- **İnceleme:** otomatik

### parallel-web  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 95 (A)

- **Ne yapar:** Uses Parallel CLI for web search, URL extraction, deep research, structured data enrichment, entity discovery, and recurring web monitoring. Best for requests that explicitly need current web evidence, academic-source discovery, repeated entity lookups, exhaustive reports, or ongoing change tracking.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 39 KB (SKILL.md 8.7 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### patent-novelty-check  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Assess patent novelty and non-obviousness against prior art. Use when user says \"专利查新\", \"patent novelty\", \"可专利性评估\", \"patentability check\", or wants to evaluate if an invention is patentable.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### patent-pipeline  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Full patent drafting pipeline from invention description to jurisdiction-formatted filing documents. Supports CN (CNIPA), US (USPTO), EP (EPO). Supports invention patents and utility models. Use when user says \"写专利\", \"patent pipeline\", \"专利申请\", \"draft patent\", \"写权利要求书\", or wants to draft a complete patent application.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 14.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### patent-review  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Get an external patent examiner review of a patent application. Use when user says \"专利审查\", \"patent review\", \"审查意见\", \"examiner review\", or wants critical feedback on patent claims and specification.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### peer-review  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Prepares evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Supports authorized review of scientific manuscripts, protocols, preprints, or research proposals; reporting-guideline selection; claim–evidence checks; methods, statistics, reproducibility, ethics, figure/table, and citation critique; or revision-response planning.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 196 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik

### pi-agent  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Builds with and operates Pi, the minimal terminal coding harness. Use for installing Pi, configuring providers/models/settings/environment variables, creating Pi skills/extensions/packages/themes/prompt templates, embedding Pi through the SDK, integrating over RPC or JSON event streams, parsing sessions, running local models through the llama.cpp router, developing custom Pi providers and TUI comp
- **Teknoloji:** api-anahtari, docker, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 270 KB (SKILL.md 8.1 KB, yük orta)
- **İnceleme:** otomatik

### pixel-art  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Generate pixel art SVG illustrations for READMEs, docs, or slides. Use when user says "画像素图", "pixel art", "make an SVG illustration", "README hero image", or wants a cute visual.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### pptx-posters  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Creates and audits editable scientific posters in macro-free PowerPoint (.pptx) from author-approved local content and assets. Used when the requested deliverable is a PowerPoint research/conference poster and exact physical, printer, accessibility, provenance, and package-security checks are required.
- **Teknoloji:** api-anahtari, canvas, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 247 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### prior-art-search  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Search patent databases and academic literature for prior art relevant to an invention. Use when user says \"现有技术检索\", \"prior art search\", \"专利检索\", \"check patents\", or wants to find relevant prior art.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### proof-checker  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Rigorous mathematical proof verification and fixing workflow. Reads a LaTeX proof, identifies gaps via cross-model review (external reviewer backend, ultra reasoning), fixes each gap with full derivations, re-reviews, and generates an audit report. Use when user says "检查证明", "verify proof", "proof check", "审证明", "check this proof", or wants rigorous mathematical verification of a theory paper.
- **Teknoloji:** git, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 55 KB (SKILL.md 55.3 KB, yük buyuk) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### proof-orchestrator  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Manage a stateful, run-directory-based proof project: continuation across runs, run-local source bookkeeping, manual GPT Pro handoff packages when a local attempt stalls, and an optional DeepSeek second opinion as additional evidence only. Use when the user asks for proof-run orchestration, a GPT Pro handoff, or cross-run proof continuation — use /proof-writer for ordinary proof drafting and /proo
- **Teknoloji:** next.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 18.5 KB, yük orta)
- **İnceleme:** otomatik

### proof-writer  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Writes rigorous mathematical proofs for ML/AI theory. Use when asked to prove a theorem, lemma, proposition, or corollary, fill in missing proof steps, formalize a proof sketch, 补全证明, 写证明, 证明某个命题, or determine whether a claimed proof can actually be completed under the stated assumptions.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### pyzotero  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Manages Zotero reference libraries using the pyzotero Python client: retrieves, creates, updates, and deletes items, collections, tags, and attachments via the Zotero Web API v3 or local API. Applies when working with Zotero libraries programmatically, managing bibliographic references, exporting citations, searching library contents, uploading PDF attachments, or building research automation work
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 7.8 KB, yük orta)
- **İnceleme:** otomatik

### qzcli  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Manage GPU compute jobs on the Qizhi (启智) platform using qzcli — a kubectl-style CLI tool. Use when user says "qzcli", "启智平台", "submit job", "stop job", "查计算组", "avail", "list jobs", "batch submit", or needs to manage distributed training jobs on a Qizhi instance.
- **Teknoloji:** docker, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.8 KB, yük kucuk)
- **İnceleme:** otomatik

### rebuttal  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Workflow 4: Submission rebuttal pipeline. Parses external reviews, enforces coverage and grounding, drafts a safe text-only rebuttal under venue limits, and manages follow-up rounds. Use when user says \"rebuttal\", \"reply to reviewers\", \"ICML rebuttal\", \"OpenReview response\", or wants to answer external reviews safely.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 25.1 KB, yük buyuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### render-html  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Render an ARIS Markdown / JSON artifact (IDEA_REPORT, AUTO_REVIEW, KILL_ARGUMENT, PAPER_PLAN, research-wiki state, etc.) into a single-file HTML view designed for human reading. Use when the user says \"渲染 HTML\", \"出一份 HTML 报告\", \"render html\", \"make this readable\", \"export to html\", or wants a polished web-rendered view of a Markdown artifact.
- **Teknoloji:** css, git, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 91 KB (SKILL.md 22.4 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### research-grants  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Supports research proposal preparation and review for NSF, NIH, DOE, DARPA, and Taiwan NSTC, including opportunity-specific requirements, aims, review criteria, budgets, broader impacts, forms, and resubmissions. Use for investigator-authored grant development, compliance matrices, and proposal critiques.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 145 KB (SKILL.md 16.9 KB, yük orta)
- **İnceleme:** otomatik

### research-implement-feature  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 79 (B)

- **Ne yapar:** Build a working artifact from a plain \"implement X for me\" request: a running end-to-end spine first, then one feature per rung, with every under-determined decision written to an assumption ledger BEFORE the code that depends on it and a cross-model sweep for the ones that slipped through undeclared. Use when user says \"给我实现\", \"implement X\", \"帮我做一个能跑的\", \"先搭个原型再加功能\", \"build this feature
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 31.9 KB, yük buyuk) · **Kırık bağlantı:** 10
- **İnceleme:** otomatik

### research-lit  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Search and analyze research papers, find related work, summarize key ideas. Use when user says "find papers", "related work", "literature review", "what does this paper say", or needs to understand academic papers.
- **Teknoloji:** api-anahtari, git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 44.3 KB, yük buyuk) · **Kırık bağlantı:** 5
- **İnceleme:** otomatik

### research-lookup  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Compiles current scholarly evidence for a scientific manuscript or research brief when the user explicitly asks to gather literature, references, background evidence, competing findings, or a manuscript research packet. Uses Parallel Search by default, Parallel Extract for source retrieval, Parallel Research for explicitly deep/exhaustive work, optional explicit Parallel Chat, and optional Perplex
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 102 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### research-pipeline  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Full end-to-end research pipeline: from a broad research direction through idea discovery, experiments, and review all the way to a polished paper PDF. Use when user says \"全流程\", \"full pipeline\", \"从找idea到投稿\", \"end-to-end research\", or wants the complete autonomous research lifecycle.
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 24 KB (SKILL.md 23.7 KB, yük orta) · **Kırık bağlantı:** 6
- **İnceleme:** otomatik

### research-refine  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Turn a vague research direction into a problem-anchored, elegant, frontier-aware, implementation-oriented method plan via iterative GPT-6-Astra review. Use when the user says "refine my approach", "帮我细化方案", "decompose this problem", "打磨idea", "refine research plan", "细化研究方案", or wants a concrete research method that stays simple, focused, and top-venue ready instead of a vague or overbuilt idea.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 33.9 KB, yük buyuk) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### research-refine-pipeline  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Run an end-to-end workflow that chains `research-refine` and `experiment-plan`. Use when the user wants a one-shot pipeline from vague research direction to focused final proposal plus detailed experiment roadmap, or asks to "串起来", build a pipeline, do it end-to-end, or generate both the method and experiment plan together.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.9 KB, yük kucuk) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### research-review  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Get a deep critical review of research from a selected reviewer (Codex by default, Gemini, Grok, Claude Code, or manual). Use when user says "review my research", "help me review", "get external review", or wants critical feedback on research ideas, papers, or experimental results.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.5 KB, yük orta) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### research-wiki  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Persistent research knowledge base that accumulates papers, ideas, experiments, claims, and their relationships across the entire research lifecycle. Inspired by Karpathy's LLM Wiki pattern. Use when user says \"知识库\", \"research wiki\", \"add paper\", \"wiki query\", \"查知识库\", or wants to build/query a persistent field map.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 20.1 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### resubmit-pipeline  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Workflow 5: orchestrate a text-only resubmit of a polished paper to a different venue under hard constraints (no new experiments, no bib edits, no framework changes, never overwrite prior submissions). Use when user says \"resubmit pipeline\", \"重投流程\", \"port paper to <new venue>\", \"resubmit to <venue>\", \"tighten paper for resubmission\", or has a rejected/withdrawn paper to move to a differe
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 33.4 KB, yük buyuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### result-to-claim  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Use when experiments complete to judge what claims the results support, what they don't, and what evidence is still missing. Codex MCP evaluates results against intended claims and routes to next action (pivot, supplement, or confirm). Use after experiments finish — before writing the paper or running ablations.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 17.4 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### run-experiment  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Deploy and run ML experiments on local, remote, Vast.ai, or Modal serverless GPU. Use when user says "run experiment", "deploy to server", "跑实验", or needs to launch training jobs.
- **Teknoloji:** api-anahtari, docker, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.3 KB, yük orta)
- **İnceleme:** otomatik

### scholar-evaluation  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Provides qualitative-first, evidence-traceable developmental review of scholarly works and audit low-stakes research-assessment rubrics with optional local quality controls. Never use for ranking people or consequential decisions.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 165 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### scientific-brainstorming  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation, adversarial review, and decision logs. Use for early-stage research brainstorming or prioritizing candidate directions; hand off empirical validation, study design, ethics or regulatory review, and clinical questions to appropriate experts or skills.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 133 KB (SKILL.md 14.3 KB, yük orta)
- **İnceleme:** otomatik

### scientific-critical-thinking  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Evaluates scientific claims and evidence quality. Applies to experimental design validity, biases and confounders, statistical interpretation, evidence grading frameworks (GRADE, Cochrane Risk of Bias), and teaching critical analysis. Supports evidence appraisal and identifying flaws; formal peer review writing belongs to peer-review.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 130 KB (SKILL.md 12.8 KB, yük orta)
- **İnceleme:** otomatik

### scientific-schematics  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7 Flash for quality review. Refines when the review requests improvement, with at most two generations. Specialized in neural network architectures, system diagrams, flowcharts, biological pathways, and complex scientific visualizations.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 101 KB (SKILL.md 19.8 KB, yük orta)
- **İnceleme:** otomatik

### scientific-slides  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 381 KB (SKILL.md 21.0 KB, yük orta)
- **İnceleme:** otomatik

### scientific-writing  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Drafts, revises, and audits scientific manuscripts or reports with explicit evidence provenance, reporting-guideline coverage, authorship accountability, confidentiality controls, and local consistency checks. Use for manuscript sections, references, declarations, tables, figures, or submission preparation when scientific accuracy and traceability matter.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 176 KB (SKILL.md 14.5 KB, yük orta)
- **İnceleme:** otomatik

### semantic-scholar  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Search published venue papers (IEEE, ACM, Springer, etc.) via Semantic Scholar API. Complements /arxiv (preprints) with citation counts, venue metadata, and TLDR. Use when user says "search semantic scholar", "find IEEE papers", "find journal papers", "venue papers", "citation search", or wants published literature beyond arXiv preprints.
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### serverless-modal  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Run GPU workloads on Modal — training, fine-tuning, inference, batch processing. Zero-config serverless: no SSH, no Docker, auto scale-to-zero. Use when user says \"modal run\", \"modal training\", \"modal inference\", \"deploy to modal\", \"need a GPU\", \"run on modal\", \"serverless GPU\", or needs remote GPU compute.
- **Teknoloji:** api-anahtari, docker, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 12.9 KB, yük orta)
- **İnceleme:** otomatik

### slides-polish  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 84 (A)

- **Ne yapar:** Per-page Codex review + targeted python-pptx / Beamer fixes for academic talk slides. Use AFTER /paper-slides (or any externally generated PPTX/Beamer) when the deck looks 'mostly OK' but the user wants a final pass that aligns visual weight with a reference, bumps PPTX fonts to projector-readable size, kills italic style leaks, fixes text-frame overflow, and catches per-slide layout drift. Trigge
- **Teknoloji:** html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 29.0 KB, yük buyuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### specification-writing  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Write the full patent specification from claims and invention disclosure. Use when user says \"撰写说明书\", \"write specification\", \"写说明书\", \"patent description\", or wants to draft the complete patent specification.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.5 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### system-profile  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Profile a target (script, process, GPU, memory, interconnect) for performance analysis. Use when user says \"profile\", \"benchmark\", \"bottleneck\", or wants performance analysis.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### training-check  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Periodically check WandB metrics during training to catch problems early (NaN, loss divergence, idle GPUs). Avoids wasting GPU hours on broken runs. Use when training is running and you want automated health checks.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### vast-gpu  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Rent, manage, and destroy GPU instances on vast.ai. Use when user says \"rent gpu\", \"vast.ai\", \"rent a server\", \"cloud gpu\", or needs on-demand GPU without owning hardware.
- **Teknoloji:** api-anahtari, docker, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** otomatik

### venue-templates  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Prepares journal manuscripts, conference papers, research posters, and grant documents using venue-specific formatting guidance and bundled LaTeX scaffolds. Supports selecting an official template, checking current page or anonymity rules, adapting academic writing to a venue, or inspecting a submission PDF.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 314 KB (SKILL.md 13.0 KB, yük orta)
- **İnceleme:** otomatik

### web-debug-search  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 89 (A)

- **Ne yapar:** Search GitHub, Stack Exchange, Chinese technical communities, official documentation, and general developer web sources for software errors, compatibility problems, API usage questions, and real-world workarounds. Use for debugging and discovery only; results are not paper-citation evidence.
- **Teknoloji:** node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 14.7 KB, yük orta)
- **İnceleme:** otomatik

### what-if-oracle  ·  K-Dense-AI/scientific-agent-skills @ ec59a29  ·  puan 97 (A)

- **Ne yapar:** Supports structured what-if scenario analysis for research planning, experimental contingencies, and scientific project decisions. Explores favorable, reference, adverse, wild-card, contrarian, and second-order scenarios with explicit assumptions, evidence, and decision triggers. Use to stress-test a research plan under uncertainty; scenario narratives do not estimate causal effects or calibrated 
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** K-Dense-AI (kurum, ★58227, son güncelleme 2026-11-23, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 11.5 KB, yük orta)
- **İnceleme:** otomatik

### wiki-enrich  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 87 (A)

- **Ne yapar:** Fill in the per-paper TODO sections of research-wiki/papers/<slug>.md pages that literature-ingest skills leave as bare scaffolds. Use when user says 'enrich wiki', 'fill paper TODOs', 'wiki body 補完', '把 paper 摘要寫進 wiki', 'research-wiki 自動填', or after a batch ingest that left papers/ as TODO scaffolds.
- **Teknoloji:** git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 16.2 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### writing-systems-papers  ·  wanshuiyin/Auto-claude-code-research-in-sleep @ 4ba94ae  ·  puan 91 (A)

- **Ne yapar:** Paragraph-level structural blueprint for 10-12 page systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. Provides page allocation, paragraph templates, and writing patterns. Use when user says \"写系统论文\", \"systems paper structure\", \"OSDI paper\", \"SOSP paper\", or wants fine-grained structural guidance for a systems conference submission.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** wanshuiyin (kisi, ★19655, son güncelleme 2026-11-19, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** otomatik
