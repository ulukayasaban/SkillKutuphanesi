# Bosluklar (2026-11-11)

## 1. Arac tablosu
| Arac | Bu Mac | Proje skill klasoru | Talimat dosyasi | Alt ajan | Ad cakismasi | Symlink | Belirsiz |
|---|---|---|---|---|---|---|---|
| Claude Code | var (CLI 2.1.319) | .claude/skills | CLAUDE.md; AGENTS.md yalniz CLAUDE.md yoksa | .claude/agents/*.md | kurumsal>kisisel>proje | evet | .agents/skills okunmaz (belgede yok) |
| Codex | var (0.167.0) | .agents/skills | AGENTS.md (override), 32 KiB sinir | .codex/agents/*.toml | belgesiz | evet (belge) | ~/.codex/skills hala okunuyor mu |
| Antigravity | var (App 2.29, IDE 2.6) | .agents/skills (.agent eski) | AGENTS.md, GEMINI.md, .agents/rules | .agents/agents/*.md | proje>kullanici (CLI ozel klasor haric) | belgesiz | CLAUDE.md okunmaz varsayilmali; symlink |
| Gemini CLI | yok | .gemini/skills, .agents/skills (alias) | GEMINI.md; AGENTS.md varsayilan degil | .gemini/agents/*.md | proje>kullanici | belgesiz | CLI Antigravity'ye geciyor olabilir |
| Cursor | var (3.25.6) | .agents/skills, .cursor/skills, .claude/skills, .codex/skills | AGENTS.md, .cursor/rules | .cursor/agents, .claude/agents, .codex/agents | skillde belgesiz | belgesiz | CLAUDE.md okunur mu |
| Copilot | VS Code var; CLI yok | .github/skills, .claude/skills, .agents/skills | copilot-instructions.md, AGENTS.md, CLAUDE.md (CLI: GEMINI.md de) | .github/agents/*.agent.md | CLI proje>kisisel | belgesiz | VS Code onceligi |

Tek duzen: gercek klasor .agents/skills + AGENTS.md; Codex, Antigravity, Gemini CLI (alias), Cursor ve Copilot bunu okur. Claude icin ek: .claude/skills (symlink; Windows'ta kopya) ve CLAUDE.md (AGENTS.md'yi gostermeli, yoksa Claude AGENTS.md'yi gormez). Gemini CLI icin ek: GEMINI.md (veya context.fileName). Rol/ajan dosyalari Claude (.claude/agents), Codex (.codex/agents) icin ayri uretilir; digerleri tum skilleri gorur. Cursor/Copilot ek dosya gerektirmez.

## 2-4: bkz. asagi (donus metniyle ayni)
