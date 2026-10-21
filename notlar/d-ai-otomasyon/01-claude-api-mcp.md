# 01-claude-api-mcp — AI ve Otomasyon

_Claude API, MCP sunucusu, model geçişi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/9**

### claude-api  ·  anthropics/skills @ dbd4588  ·  puan 76 (B)

- **Ne yapar:** Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read BEFORE opening the target file; don't skip because it "looks like a one-liner" — whenever: the prompt names Claude/Anthropic in any form (Claude, Anthropic, Fable, Opus, Sonnet, Haiku, `anthropic`, `@anthropic-ai`, `claude-*`, `us.ant
- **Teknoloji:** api-anahtari, html, python, three.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★182672, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 2031 KB (SKILL.md 102.7 KB, yük buyuk)
- **İnceleme:** otomatik

### claude-opus-4-5-migration  ·  anthropics/claude-code @ d014fc0  ·  puan 88 (A)

- **Ne yapar:** Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants to update their codebase, prompts, or API calls to use Opus 4.5. Handles model string updates and prompt adjustments for known Opus 4.5 behavioral differences. Does NOT migrate Haiku 4.5.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### connect  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 88 (A)

- **Ne yapar:** Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### connect-apps  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 83 (A)

- **Ne yapar:** Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### langsmith-fetch  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 86 (A)

- **Ne yapar:** Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed.
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### mcp-builder  ·  anthropics/skills @ dbd4588  ·  puan 86 (A)

- **Ne yapar:** Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182672, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 119 KB (SKILL.md 8.9 KB, yük orta)
- **İnceleme:** otomatik

### mcp-builder@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 86 (A)

- **Ne yapar:** Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif
- **Boyut:** 144 KB (SKILL.md 13.2 KB, yük orta)
- **İnceleme:** otomatik

### mcp-builder@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 87 (A)

- **Ne yapar:** MCP (Model Context Protocol) server and client engineering. Protocol design, schemas, transports, extensions, security, and migration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** otomatik

### mcp-integration  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for 
- **Teknoloji:** api-anahtari, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik
