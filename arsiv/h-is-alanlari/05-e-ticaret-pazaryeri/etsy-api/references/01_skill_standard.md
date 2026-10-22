# `SKILL.md` standard (practical notes)

A skill is a folder that contains an **agent instruction file** named `SKILL.md`.

Common conventions (as documented for Codex-style skills) include:

- **Discovery**: skills are discovered from one or more directories (commonly `~/.codex/skills` for user-scoped skills and `./.codex/skills` for repo-scoped skills).
- **Structure**: a skill folder contains:
  - `SKILL.md` — the authoritative instructions
  - `scripts/` — optional helper code the agent can run (e.g., API wrappers, CLI utilities)
  - `references/` — optional curated reference notes, snippets, “how-to” docs, etc.

This repo is organized like:

```
skills/etsy-api/
  SKILL.md
  scripts/
  references/
```

To use the skill in a Codex-style repo setup, copy `skills/etsy-api` into `.codex/skills/etsy-api`.

## Authoring guidance

When writing a skill, aim for:

- Clear, imperative instructions (“Do X”, “Avoid Y”)
- Explicit environment variables / configuration
- Known constraints (rate limits, required headers, retry behavior)
- “Golden path” examples for the most common operations
