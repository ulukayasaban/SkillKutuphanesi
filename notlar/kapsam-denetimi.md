# Kapsam Denetimi

> `araclar/kapsam-denetimi.py` üretir · 2026-10-22 · Bağımsız kontrol: her repo için GitHub'daki tam dosya ağacı yeniden çekilip içindeki tüm SKILL.md dosyaları tek tek açıklandı.

**Sonuç: ✅ Açıklanamayan skill yok** · Taranan SKILL.md: 1392 · Arşivdeki skill kaydı: 1240 · Bileşen (komut/agent): 67

| Karar | Sayı | Anlamı |
|---|---|---|
| secildi | 1233 | arşivde (ana sürüm) |
| ayna-ayni | 123 | birebir kopya (tek kopya yeter) |
| ayna-baska-arac | 20 | başka AI aracı (Cursor/Gemini/Kiro…) için kopya |
| haric | 12 | bilinçli hariç (test/örnek/şablon) |
| arac-varyanti | 4 | arşivde (Claude/Codex'e özel sürüm) |

## Repo bazında

| Repo | SKILL.md | Dağılım |
|---|---|---|
| CloudAI-X/threejs-skills | 13 | secildi 13 |
| ComposioHQ/awesome-claude-skills | 864 | secildi 864 |
| GoogleChrome/lighthouse | 3 | secildi 3 |
| Leonxlnx/taste-skill | 1 | secildi 1 |
| Panniantong/Agent-Reach | 1 | secildi 1 |
| addyosmani/agent-skills | 25 | secildi 25 |
| anthropics/claude-code | 10 | secildi 10 |
| anthropics/skills | 20 | secildi 19, haric 1 |
| calesthio/OpenMontage | 139 | secildi 91, ayna-ayni 46, arac-varyanti 2 |
| darkroomengineering/satus | 1 | secildi 1 |
| freshtechbro/claudedesignskills | 90 | ayna-ayni 66, secildi 23, ayna-baska-arac 1 |
| greensock/gsap-skills | 8 | secildi 8 |
| heygen-com/hyperframes | 26 | secildi 13, haric 7, ayna-ayni 6 |
| heyitsnoah/claudesidian | 20 | secildi 20 |
| microsoft/playwright | 9 | secildi 9 |
| motiondivision/motion | 2 | secildi 2 |
| nateherkai/scroll-craft | 1 | secildi 1 |
| nextlevelbuilder/ui-ux-pro-max-skill | 13 | secildi 7, ayna-ayni 5, ayna-baska-arac 1 |
| obra/superpowers | 15 | secildi 15 |
| pbakaus/impeccable | 25 | ayna-baska-arac 18, haric 4, arac-varyanti 2, secildi 1 |
| react/react | 14 | secildi 14 |
| teng-lin/notebooklm-py | 1 | secildi 1 |
| tt-a1i/archify | 5 | secildi 5 |
| vercel/next.js | 27 | secildi 27 |
| vudovn/ag-kit | 58 | secildi 58 |
| zanwei/design-dna | 1 | secildi 1 |

## Referans repoları (T5/T6)

24 repo tarandı; içlerinde skill yok.

## Bilinçli hariç tutulanlar (gerekçeli)

- **anthropics/skills**: `template/SKILL.md` (^template/)
- **pbakaus/impeccable**: `tests/oracle/workspaces/ctx-pin/.agents/skills/impeccable/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.claude/skills/audit/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.claude/skills/impeccable/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.cursor/skills/impeccable/SKILL.md` ((^|/)tests?/)
- **heygen-com/hyperframes**: `registry/blocks/canopy-part-title/SKILL.md` (^registry/blocks/), `registry/blocks/code-slice-hero/SKILL.md` (^registry/blocks/), `registry/blocks/cuboid-carousel/SKILL.md` (^registry/blocks/), `registry/blocks/frost-sequence-camera-orbit/SKILL.md` (^registry/blocks/), `registry/blocks/glass-shard-title/SKILL.md` (^registry/blocks/), `registry/blocks/orbit-card/SKILL.md` (^registry/blocks/), `registry/blocks/wireframe-portal-title/SKILL.md` (^registry/blocks/)
