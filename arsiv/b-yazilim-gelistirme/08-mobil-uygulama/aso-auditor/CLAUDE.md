# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is a **Claude Skill** repository — not a runnable application. The primary artifact is `SKILL.md`, a 1,700+ line instruction file that users upload to Claude to enable production-grade App Store Optimization (ASO) audits. There is no build system, no package manager, and no runtime.

## No Build or Test Commands

There are no build, lint, or test commands. All files are Markdown or HTML. The "product" is the structured instruction set in `SKILL.md`.

## Repository Structure

```
SKILL.md                          # Master skill instruction file (primary artifact)
README.md                         # User-facing overview, installation, usage
docs/
  scoring-rubric.md               # Detailed reference for all 7 scoring pillars
  failure-patterns.md             # 15 ASO failure patterns × 3 fix strategies each
  audits/
    README.md                     # Example audit index
    *.html                        # Example rendered audit widgets
.github/
  ISSUE_TEMPLATE/audit-feedback.md
```

## SKILL.md Architecture

`SKILL.md` is organized into 13 numbered sections:

1. **Metadata** — skill name, version, trigger conditions
2. **Input Schema** — required fields (iOS/Play Store URL, category) and optional fields (ASC/Play Console exports, competitor URLs)
3. **Pre-Audit Research Protocol** — URL normalization, crawling procedure, fallback prompts when data is missing
4. **Scoring Framework** — 7 pillars, 155 total points, normalized to 0–100%
5. **Platform Delta Table** — iOS vs. Android differences for every dimension
6. **Interactive Report Delivery** — pure HTML + vanilla JS widget scaffold with frozen baseline + live simulation mode
7. **Failure Pattern Library** — 15 patterns with copy-only / design+copy / structural fix variants
8. **Opportunities Table** — P0/P1/P2 priority matrix
9. **90-Day Roadmap** — fixed milestone format
10. **Keyword Testing Lab** — title/subtitle/short description variant generator
11. **Competitor Comparison** — gap analysis format
12. **Notion Export** — checkbox task list output format
13. **Closing Protocol** — mandatory CTA at audit end

## Scoring Design Rules

These rules are load-bearing — violating them breaks the interactive widget:

- **Binary scoring only**: Every sub-criterion scores full points or 0. No partial credit. This makes live simulation work (toggling a fix changes score by a fixed known amount).
- **Single source of truth**: All scores must flow from `INIT_PILLARS` array through `computeScore(pillars, plat)`. Never maintain a second score variable — it will drift.
- **No getter double-counting**: Using `get total()` with `Object.values()` causes the getter to be counted as a value. Use plain `const` for frozen baselines.
- **Listing-anchored recommendations**: Every recommendation must quote actual text or data from the audited listing. No generic advice.

## Crawler Limitations (Critical)

These affect scoring logic and must be handled with fallback prompts:

- **iOS preview videos** are blob URLs — invisible to web crawlers. Always ask user to confirm before scoring Pillar 6.
- **Android short description** is frequently missing from crawls. Prompt for manual input.
- **Screenshots and icons** cannot be fetched as images by crawlers. User must upload before scoring Pillars 2 and 5.

## The 7 Pillars (155 pts total)

| # | Pillar | Points |
|---|--------|--------|
| 1 | Title + Subtitle (iOS) / Title + Short Desc (Android) | 25 |
| 2 | App Icon | 20 |
| 3 | Keywords & Metadata | 25 |
| 4 | Description | 25 |
| 5 | Screenshots | 25 |
| 6 | App Preview Video | 20 |
| 7 | Ratings & Reviews | 15 |

Score = (raw points / 155) × 100. Flag divergence > 15 percentage points between iOS and Android scores.

## When Editing SKILL.md

- Scoring criterion changes must be reflected in both `SKILL.md` (Section 4) and `docs/scoring-rubric.md`.
- New failure patterns belong in both `SKILL.md` (Section 7) and `docs/failure-patterns.md`.
- The HTML widget scaffold in Section 6 uses vanilla JS only — no React, no build step, no external dependencies.
