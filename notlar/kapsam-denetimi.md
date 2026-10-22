# Kapsam Denetimi

> `araclar/kapsam-denetimi.py` üretir · 2026-10-22 · Bağımsız kontrol: her repo için GitHub'daki tam dosya ağacı yeniden çekilip içindeki tüm SKILL.md dosyaları tek tek açıklandı.

**Sonuç: ✅ Açıklanamayan skill yok** · Taranan SKILL.md: 2616 · Arşivdeki skill kaydı: 1982 · Bileşen (komut/agent): 210

| Karar | Sayı | Anlamı |
|---|---|---|
| secildi | 1984 | arşivde (ana sürüm) |
| haric | 473 | bilinçli hariç (test/örnek/şablon) |
| ayna-ayni | 123 | birebir kopya (tek kopya yeter) |
| ayna-baska-arac | 26 | başka AI aracı (Cursor/Gemini/Kiro…) için kopya |
| ayri-surum | 6 | arşivde (aynı adlı farklı içerik, ayrı skill) |
| arac-varyanti | 4 | arşivde (Claude/Codex'e özel sürüm) |

## Repo bazında

| Repo | SKILL.md | Dağılım |
|---|---|---|
| CloudAI-X/threejs-skills | 13 | secildi 13 |
| ComposioHQ/awesome-claude-skills | 864 | secildi 864 |
| DietrichGebert/ponytail | 12 | ayna-baska-arac 6, secildi 6 |
| Donchitos/Claude-Code-Game-Studios | 74 | secildi 74 |
| Fei-Away/Codex-Dream-Skin | 2 | haric 2 |
| GoogleChrome/lighthouse | 3 | secildi 3 |
| Graphify-Labs/graphify | 1 | secildi 1 |
| K-Dense-AI/scientific-agent-skills | 177 | secildi 177 |
| Leonxlnx/taste-skill | 1 | secildi 1 |
| Panniantong/Agent-Reach | 1 | secildi 1 |
| addyosmani/agent-skills | 25 | secildi 25 |
| android/skills | 33 | secildi 33 |
| anthropics/claude-code | 10 | secildi 10 |
| anthropics/claude-plugins-official | 33 | secildi 25, haric 8 |
| anthropics/knowledge-work-plugins | 252 | secildi 189, haric 57, ayri-surum 6 |
| anthropics/skills | 20 | secildi 19, haric 1 |
| calesthio/OpenMontage | 139 | secildi 79, ayna-ayni 46, haric 12, arac-varyanti 2 |
| cloudflare/security-audit-skill | 1 | secildi 1 |
| cloudflare/skills | 19 | secildi 19 |
| czlonkowski/n8n-skills | 15 | secildi 15 |
| darkroomengineering/satus | 1 | secildi 1 |
| earthtojake/text-to-cad | 13 | secildi 12, haric 1 |
| expo/skills | 25 | secildi 24, haric 1 |
| freshtechbro/claudedesignskills | 90 | ayna-ayni 66, secildi 23, ayna-baska-arac 1 |
| greensock/gsap-skills | 8 | secildi 8 |
| heygen-com/hyperframes | 26 | secildi 13, haric 7, ayna-ayni 6 |
| heyitsnoah/claudesidian | 20 | secildi 20 |
| lemomo-ai/codex-radar | 1 | secildi 1 |
| lemomo-ai/lemo-opuscar | 2 | secildi 2 |
| lemomo-ai/lemo-wake | 3 | secildi 3 |
| microsoft/playwright | 9 | secildi 9 |
| motiondivision/motion | 2 | secildi 2 |
| multica-ai/andrej-karpathy-skills | 1 | secildi 1 |
| nateherkai/scroll-craft | 1 | secildi 1 |
| nextlevelbuilder/ui-ux-pro-max-skill | 13 | secildi 7, ayna-ayni 5, ayna-baska-arac 1 |
| nexu-io/open-design | 549 | haric 380, secildi 169 |
| obra/superpowers | 15 | secildi 15 |
| pbakaus/impeccable | 25 | ayna-baska-arac 18, haric 4, arac-varyanti 2, secildi 1 |
| react/react | 14 | secildi 14 |
| teng-lin/notebooklm-py | 1 | secildi 1 |
| tt-a1i/archify | 5 | secildi 5 |
| vercel-labs/agent-skills | 9 | secildi 9 |
| vercel/next.js | 27 | secildi 27 |
| vudovn/ag-kit | 58 | secildi 58 |
| yaojingang/yao-meta-skill | 1 | secildi 1 |
| ythx-101/live-panel-skill | 1 | secildi 1 |
| zanwei/design-dna | 1 | secildi 1 |

## Referans repoları (T5/T6)

27 repo tarandı; içlerinde skill yok.

## Bilinçli hariç tutulanlar (gerekçeli)

- **anthropics/skills**: `template/SKILL.md` (^template/)
- **pbakaus/impeccable**: `tests/oracle/workspaces/ctx-pin/.agents/skills/impeccable/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.claude/skills/audit/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.claude/skills/impeccable/SKILL.md` ((^|/)tests?/), `tests/oracle/workspaces/ctx-pin/.cursor/skills/impeccable/SKILL.md` ((^|/)tests?/)
- **heygen-com/hyperframes**: `registry/blocks/canopy-part-title/SKILL.md` (^registry/blocks/), `registry/blocks/code-slice-hero/SKILL.md` (^registry/blocks/), `registry/blocks/cuboid-carousel/SKILL.md` (^registry/blocks/), `registry/blocks/frost-sequence-camera-orbit/SKILL.md` (^registry/blocks/), `registry/blocks/glass-shard-title/SKILL.md` (^registry/blocks/), `registry/blocks/orbit-card/SKILL.md` (^registry/blocks/), `registry/blocks/wireframe-portal-title/SKILL.md` (^registry/blocks/)
- **Fei-Away/Codex-Dream-Skin**: `macos/SKILL.md` (^(macos|windows)/), `windows/SKILL.md` (^(macos|windows)/)
- **anthropics/claude-plugins-official**: `external_plugins/discord/skills/access/SKILL.md` (^external_plugins/), `external_plugins/discord/skills/configure/SKILL.md` (^external_plugins/), `external_plugins/imessage/skills/access/SKILL.md` (^external_plugins/), `external_plugins/imessage/skills/configure/SKILL.md` (^external_plugins/), `external_plugins/telegram/skills/access/SKILL.md` (^external_plugins/), `external_plugins/telegram/skills/configure/SKILL.md` (^external_plugins/), `plugins/example-plugin/skills/example-command/SKILL.md` (^plugins/example-plugin/), `plugins/example-plugin/skills/example-skill/SKILL.md` (^plugins/example-plugin/)
- **nexu-io/open-design**: `.claude/skills/od-contribute/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `apps/daemon/tests/fixtures/plugin-fixtures/sample-plugin/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/aster-atelier/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/audio-jingle/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/blog-post/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/clinical-case-report/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/contact-widget/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/critique/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/dashboard/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/dating-web/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/dcf-valuation/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/digital-eguide/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/docs-page/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/email-marketing/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/eng-runbook/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/finance-report/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/flowai-live-dashboard-template/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/gamified-app/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/github-dashboard/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/), `design-templates/guizang-ppt/SKILL.md` (^(plugins|design-templates|tools|docs|apps|\.claude)/) … (+360)
- **calesthio/OpenMontage**: `.agents/skills/hyperframes-animation/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes-cli/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes-core/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes-creative/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes-media/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes-registry/SKILL.md` (arsivden-cikarildi), `.agents/skills/hyperframes/SKILL.md` (arsivden-cikarildi), `.agents/skills/media-use/SKILL.md` (arsivden-cikarildi), `.agents/skills/motion-graphics/SKILL.md` (arsivden-cikarildi), `.agents/skills/music-to-video/SKILL.md` (arsivden-cikarildi), `.agents/skills/remotion-to-hyperframes/SKILL.md` (arsivden-cikarildi), `.agents/skills/website-to-video/SKILL.md` (arsivden-cikarildi)
- **expo/skills**: `.claude/skills/expo-skill-eval/SKILL.md` (^\.claude/)
- **anthropics/knowledge-work-plugins**: `partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/contact-center/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/contact-center/android/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/contact-center/web/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/debug-zoom/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/general/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/android/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/electron/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/ios/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/linux/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/macos/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md` (^partner-built/zoom-plugin/), `partner-built/zoom-plugin/skills/meeting-sdk/unreal/SKILL.md` (^partner-built/zoom-plugin/) … (+37)
- **earthtojake/text-to-cad**: `apps/web/skills/smui/SKILL.md` (^apps/)
