# 04-skill-plugin-yazimi — AI ve Otomasyon

_Skill yazma, plugin/hook/komut geliştirme_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/14**

### academy-guide  ·  anthropics/skills @ dbd4588  ·  puan 86 (A)

- **Ne yapar:** Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Claude Academy (academy.claude.com), Anthropic's learning hub. Trigger on: "how do I", "how can I", "getting started with", "what can Claude do", "teach me", "learn to use"; questions about artifacts, projects, skills, plugin
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182672, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 7.6 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### agent-development  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 69 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** otomatik

### command-development  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in com
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 150 KB (SKILL.md 18.5 KB, yük orta)
- **İnceleme:** otomatik

### hook-development  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### plugin-settings  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown 
- **Teknoloji:** api-anahtari, git, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### plugin-structure  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code pl
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 73 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik

### skill-creator  ·  anthropics/skills @ dbd4588  ·  puan 83 (A)

- **Ne yapar:** Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- **Teknoloji:** api-anahtari, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182672, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih
- **Boyut:** 220 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** otomatik

### skill-creator@freshtechbro  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **Teknoloji:** api-anahtari, html, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1102, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 41 KB (SKILL.md 11.3 KB, yük orta)
- **İnceleme:** otomatik

### skill-development  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.
- **Teknoloji:** api-anahtari, html, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 34 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** otomatik

### skill-share  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 88 (A)

- **Ne yapar:** A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### skillify  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Auto-create new skills from repetitive workflows. When you notice yourself doing the same multi-step process repeatedly, extract it into a reusable SKILL.md that any agent can use.
- **Teknoloji:** tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### template-skill  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 88 (A)

- **Ne yapar:** Replace with description of the skill and when Claude should use it.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77588, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 0 KB (SKILL.md 0.1 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-hookify-rules  ·  anthropics/claude-code @ d014fc0  ·  puan 74 (B)

- **Ne yapar:** This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
- **Teknoloji:** api-anahtari, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152692, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** otomatik

### writing-skills  ·  obra/superpowers @ b739a8a  ·  puan 86 (A)

- **Ne yapar:** Use when creating new skills, editing existing skills, or verifying skills work before deployment
- **Teknoloji:** api-anahtari, git, node, python, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★302965, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 105 KB (SKILL.md 26.0 KB, yük buyuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik
