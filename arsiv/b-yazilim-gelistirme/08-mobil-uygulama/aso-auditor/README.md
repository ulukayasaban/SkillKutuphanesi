# ASO Auditor — Claude Skill

Hello

A production-grade App Store Optimization audit skill for Claude. Paste any App Store or Google Play URL and get a fully scored, interactive audit report — rendered inline in Claude with no setup required.

---

## What it does

Drop a Play Store or App Store URL into Claude and receive:

- **Dual-platform scoring** across 7 pillars, 155 points max, normalized to 0–100%
- **Interactive HTML report** rendered inline in Claude — collapsible pillar checklist, live score simulation (toggle checkboxes to simulate fixes), opportunities table, keyword testing lab, and 90-day roadmap
- **Per-criterion recommendations** in three strategy variants: copy-only (low effort), design + copy (medium), and structural/code (high)
- **Visual analysis** — prompts you to upload screenshots and icon before scoring Pillars 2 and 5; uses actual images rather than assumptions
- **Crawling fallbacks** — when the Play Store or App Store doesn't return a full page, Claude asks for the missing fields one-by-one rather than hallucinating

---

## Scoring framework

| Pillar | What it covers | Max pts |
|--------|----------------|---------|
| P1 | Title + Subtitle (iOS) / Title + Short Description (Android) | 25 |
| P2 | App icon | 20 |
| P3 | Keywords & metadata | 25 |
| P4 | Description | 25 |
| P5 | Screenshots | 25 |
| P6 | App preview video | 20 |
| P7 | Ratings & reviews | 15 |
| **Total** | | **155** |

`Optimization Grade = (Raw Score / 155) × 100`

iOS and Android are scored separately. A platform divergence of > 15pp triggers a warning.

---

## Live score simulation

The interactive report has two score states:

- **Audit score** — frozen at the moment of audit, never changes when you interact with the report
- **Live score** — updates in real time as you toggle checkboxes, so you can simulate "what would my score be if I fixed X?"

The platform toggle (🍎 iOS / 🤖 Android) lives inside the Live score card, switching which platform the checklist and live score reflect. For single-platform audits (iOS-only or Android-only), a static badge replaces the toggle.

---

## Known crawling limitations

| Platform | Limitation | How it's handled |
|----------|-----------|-----------------|
| iOS App Store | Preview videos are served as `blob:` URLs — invisible to any crawler | Skill always asks the user to confirm video presence before scoring Pillar 6 |
| Google Play | Short description is frequently missing from crawler responses | Manual input fallback prompts for it before scoring |
| Both | Screenshots and icons cannot be fetched as images | Skill asks you to upload them before scoring Pillars 2 and 5 |

---

## Installation

This is a [Claude Skill](https://claude.ai) — a structured instruction file that Claude reads before responding to any ASO-related request.

**To install:**

1. Download `SKILL.md` from this repo
2. In Claude, go to **Settings/Customize → Skills** (or your team's skill directory)
3. Upload downloaded `SKILL.md` by clicking on "+ Create Skill"

Once installed, the skill triggers automatically whenever you:
- Paste an App Store URL (`apps.apple.com/...`)
- Paste a Play Store URL (`play.google.com/store/apps/...`)
- Use phrases like "ASO audit", "optimize my app listing", "screenshot review", "app store ranking"

---

## Usage

### Minimal input (both platforms)

```
https://apps.apple.com/us/app/your-app/id123456789
https://play.google.com/store/apps/details?id=com.your.app
App category: Finance
```

### Single platform

```
https://play.google.com/store/apps/details?id=com.your.app
[Android only — no iOS listing]
```

### With optional data

```
https://apps.apple.com/us/app/your-app/id123456789
https://play.google.com/store/apps/details?id=com.your.app
App category: Health & Fitness

[attach: app_store_connect_export.csv]
[attach: screenshots/]
[competitor URLs: https://apps.apple.com/..., https://play.google.com/...]
```

### After the audit

At the end of every audit Claude asks:

> **Would you like to run a competitor comparison or export these recommendations as a Notion-ready task list?**

---

## Sample output

Each audit produces a self-contained interactive widget with:

```
┌─────────────────────────────────────────────────────────────┐
│  InShot — Video Editor & Maker                              │
│  Photo & Video · id997362197 · Audited: 5 Apr 2026          │
│                                                             │
│  ┌── iOS 64% ──┐  ┌── Android 77% ──┐  ┌── Live ─────────┐ │
│  │ 100/155     │  │  120/155        │  │ [🍎][🤖]         │ │
│  │ Needs work  │  │  Well optimized │  │ 65%              │ │
│  └─────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                             │
│  P1 Title + Subtitle    ████░░   15/25                      │
│  P2 App icon            ████████ 20/20                      │
│  P3 Keywords            ████░░░░ 15/25                      │
│  ...                                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Repo structure

```
aso-auditor/
├── SKILL.md              # The skill — install this file
├── README.md             # This file
├── docs/
│   ├── scoring-rubric.md # Full 7-pillar rubric with pass/fail definitions
│   ├── failure-patterns.md # 15 failure patterns with 3-strategy fixes each
│   └── audits/           # Example audit outputs (HTML widgets)
│       ├── inshot-2026-04.html
│       ├── remitly-2026-04.html
│       └── sai-satcharitra-2026-03.html
└── .github/
    └── ISSUE_TEMPLATE/
        └── audit-feedback.md
```

---

## What's in SKILL.md

| Section | Contents |
|---------|----------|
| 1. Skill metadata | Name, version, trigger phrases |
| 2. Input schema | Required / optional inputs, validation rules |
| 3. Pre-audit research protocol | Fetch sequence, mobile URL formats, crawling fallbacks, screenshot upload protocol |
| 4. Scoring rubric | Full 7-pillar table — pass definition, fail definition, source for every sub-criterion |
| 5. Platform delta table | Side-by-side iOS vs Android field limits and rules |
| 6. Interactive HTML report | Complete scaffold with anti-pattern documentation, single-platform layout spec, binary scoring rule |
| 7. Failure pattern library | 15 patterns × 3 strategy variants (copy-only / design / structural) |
| 8. Opportunities table module | P0/P1/P2 priority format, population rules |
| 9. 90-day ASO process roadmap | Fixed milestone timeline |
| 10. Keyword testing lab | Title, subtitle, and short description testing rules and candidate table format |
| 11. Competitor comparison module | Gap table format, competitor scoring instructions |
| 12. Notion export module | Checkbox format, priority labels, effort and owner fields |
| 13. Closing protocol | Mandatory closing CTA — verbatim, every audit |

---

## Key design decisions

**Single source of truth for scoring.** The audit uses a `computeScore(pillars, plat)` function applied to the same `INIT_PILLARS` array for both the frozen baseline and the live simulation. There are no separate score constants that could drift out of sync. This eliminates the double-counting bug that occurs when `Object.values()` is called on an object with a `get total()` getter.

**Binary scoring only.** Every sub-criterion scores its full point value or zero — never fractional. This makes the live simulation meaningful: each checkbox toggle produces a clean, predictable score change.

**Listing reference required.** Every recommendation Claude generates must quote actual text, numbers, or observations from the audited listing. Generic advice is not acceptable when real data is available.

**iOS video detection is impossible from a crawler.** The App Store renders preview videos as `blob:` URLs generated in the browser session. The skill documents this explicitly and always asks the user to confirm video presence rather than auto-failing criterion 6.1.

---

## Changelog

### v1.0.0 — April 2026

- Initial release
- 7-pillar, 155-point scoring framework
- Dual-platform (iOS + Android) and single-platform audit support
- Interactive HTML widget with frozen audit score + live simulation
- Platform toggle inside Live card (not below hero)
- 15 failure patterns × 3 strategy variants each
- iOS blob video detection limitation documented and handled
- Mobile URL locale params (`&hl=en&gl=us`) baked into fetch steps
- Screenshot upload protocol for Pillars 2 and 5
- Manual input fallback for missing crawler fields

---

## Contributing

Issues and PRs welcome. If you run an audit and find a scoring edge case, a crawling gap, or a failure pattern that should be in the library, open an issue with:

- The app URL(s)
- The criterion that scored incorrectly or the pattern that's missing
- What the correct behaviour should be

See `.github/ISSUE_TEMPLATE/audit-feedback.md` for the full template.

---

## License

MIT. Use freely, attribution appreciated.

---

*Built by [Vageesh Kollupuram Velusamy](https://www.advancedappmarketing.com) · Powered by Claude (Anthropic)*
