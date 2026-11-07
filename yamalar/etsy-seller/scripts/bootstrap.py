#!/usr/bin/env python3
"""
bootstrap.py — One-time state initialization for the etsy-seller skill (v2.0).

Detects whether the project's state folder exists at ./etsy-listings/ (current working directory = project root).
If not, creates it with empty markdown templates: from state-templates/ if present, otherwise from the
copies embedded below (the source repo keeps the templates outside the skill folder).

SkillKutuphanesi patch (2026-11-07): default state dir is the PROJECT, never the home directory; set
ETSY_LISTINGS_DIR or --state-dir to override.

Idempotent — safe to call on every skill invocation. Returns early if state already exists.

Usage:
    python3 bootstrap.py [--state-dir PATH] [--templates-dir PATH] [--quiet]

Default paths:
    state-dir:     $ETSY_LISTINGS_DIR or ./etsy-listings (project root)
    templates-dir: <skill-dir>/../../state-templates/etsy-listings (auto-detected)
"""
import argparse
import os
import shutil
import sys
from pathlib import Path


def find_default_templates_dir(script_dir: Path) -> Path:
    """Locate state-templates, handling two different install layouts.

    Git-clone layout:  repo/skill/scripts/bootstrap.py
                       repo/state-templates/etsy-listings/   ← two levels up

    .skill zip layout: ~/.claude/skills/<name>/scripts/bootstrap.py
                       ~/.claude/skills/<name>/state-templates/etsy-listings/ ← one level up

    Try one level up first (zip layout); fall back to two levels up (repo layout).
    """
    one_up = script_dir.parent / "state-templates" / "etsy-listings"
    if one_up.exists():
        return one_up
    return script_dir.parent.parent / "state-templates" / "etsy-listings"


def find_default_state_dir() -> Path:
    env = os.environ.get("ETSY_LISTINGS_DIR")
    return Path(env).expanduser() if env else Path.cwd() / "etsy-listings"


# Embedded copies of state-templates/etsy-listings/* (used when the folder is not shipped with the skill).
EMBEDDED_TEMPLATES = {
    "keyword-map.md": "# Keyword Map\n\n**Schema version:** 2.0\n**Last updated:** (auto-updated by skill)\n\nThis is the master index of every listing in your database with its primary keyword. The skill reads this file on every REWRITE or CREATE to check whether a candidate primary keyword overlaps with an existing listing's cluster.\n\nWhen you have many listings, this file becomes a quick at-a-glance view of your portfolio's keyword coverage.\n\n---\n\n## Listings\n\n| Listing ID | Short slug | Primary keyword | Cluster words | Secondary keywords | Difficulty | Assigned | Status |\n|---|---|---|---|---|---|---|---|\n\n*The skill appends rows here automatically after every REWRITE or CREATE. The example row below shows the format; it gets removed once you have real listings.*\n\n| L001 | _example-slug_ | _example primary kw_ | _word1;word2;word3_ | _sec phrase 1;sec phrase 2_ | _Medium_ | _YYYY-MM-DD_ | _example_ |\n\n---\n\n## Notes\n\n- Listing IDs (L001, L002, ...) are permanent. They survive title rewrites and re-keywording.\n- Cluster words are semicolon-separated. Used for the keyword reuse check (Phase 5).\n- The skill writes to this file using its Edit/Write tools — no Python scripting needed for ongoing updates.\n- Status values: `active` / `archived` / `paused`.\n",
    "listings/_TEMPLATE_listing.md": "# Listing L### — <short slug>\n\n**Schema version:** 2.0\n**Listing ID:** L###\n**Created:** YYYY-MM-DD\n**Last full edit:** YYYY-MM-DD\n**Last minor edit:** YYYY-MM-DD\n**Listing URL on Etsy:** (paste when known)\n\n---\n\n## Current state\n\n### Title\n<current title text>\n- First 40 chars: \"...\" ✅\n- Word count: X · Char count: X / 140\n\n### Primary keyword\n**<primary keyword>**\n- Difficulty: <Low-Medium / Medium / etc.>\n- Source: autocomplete (×N) + SERP top-10 (×M)\n- Last verified: YYYY-MM-DD\n- Search intent: <Browse / Specific hunt / Gifting / Trend>\n\n### Secondary keywords\n- phrase 1 (autocomplete)\n- phrase 2 (SERP top-10)\n- ...\n\n### Tags (13/13)\n| # | Tag | Chars | Source |\n|---|---|---|---|\n| 1 | <tag> | X | autocomplete |\n| 2 | <tag> | X | SERP top-10 |\n| 3 | <tag> | X | ... |\n| 4 | <tag> | X | ... |\n| 5 | <tag> | X | ... |\n| 6 | <tag> | X | ... |\n| 7 | <tag> | X | ... |\n| 8 | <tag> | X | ... |\n| 9 | <tag> | X | ... |\n| 10 | <tag> | X | ... |\n| 11 | <tag> | X | ... |\n| 12 | <tag> | X | ... |\n| 13 | <tag> | X | ... |\n\n### Attributes\n| Attribute | Value |\n|---|---|\n| Style | <value> |\n| Occasion | <value> |\n| Recipient | <value> |\n| File Type | <value> |\n| Primary Color | <value> |\n| Secondary Color | <value> |\n\n### Category\n<Top Level> > <Mid Level> > <Subcategory>\n\n### Description (full text)\n```\n<paste the full optimized description here>\n```\n\n### Hero image alt text\n<alt text — 100–150 chars, includes primary keyword>\n\n### AI & image compliance (optional)\n- **Item origin:** <human-made / seller-prompted AI / unknown>\n- **Content type:** <physical / digital design / functional instructions / prompt bundle>\n- **Image evidence:** <real unedited photo / content preview / licensed mockup / missing>\n- **AI disclosure in description:** <yes / no / not required>\n- **Gate result:** <PASS / ACTION REQUIRED / BLOCKED> — YYYY-MM-DD\n\n### Pinterest block\n- **Pin title:** <text>\n- **Board name:** <name>\n- **Board description:** <text>\n- **Pin description:** <text> (XXX chars)\n- **Image brief:** <text>\n- **Video brief (5–15 sec storyboard):** <summary>\n\n---\n\n## Indexing spread check (latest)\n\n| Surface | Status |\n|---|---|\n| Title (first 40 chars) | ✅ |\n| Tags (≥3 with cluster) | Tag #X, #Y, #Z ✅ |\n| Attribute echo | Style=\"<value>\" ✅ |\n| Description first 160 | ✅ |\n| Hero alt text | ✅ |\n\n---\n\n## Health score (latest)\n\n**Composite: XX / 100**\n\n| Component | Score |\n|---|---|\n| SEO surface coverage | X / 25 |\n| Evidence quality | X / 20 |\n| Coherence | X / 15 |\n| CTR estimate | X / 15 [* inferred if no SQR] |\n| Conversion estimate | X / 15 [* inferred] |\n| Compliance | X / 10 |\n\n**Suggested next action:** <one-line recommendation>\n\n---\n\n## SQR data (if user pasted any)\n\nLatest import: `sqr-imports/YYYY-MM-DD_L###.md` (if exists)\n\n### Top queries bringing impressions (last 30 days)\n| Query | Impressions | Clicks | Orders | CTR | CVR |\n|---|---|---|---|---|---|\n| <query> | __ | __ | __ | __% | __% |\n\n**Match with current primary:** ✅ / ⚠️ (pivot recommended)\n\n---\n\n## Change history\n\n### YYYY-MM-DD — <Action description, e.g., \"Full rewrite (REWRITE mode)\">\n- Field(s) changed: <list>\n- Reason: <SEO problem / SQR pivot / refresh / etc.>\n- Old → new: <where applicable>\n- Spread check after: ✅\n\n### YYYY-MM-DD — Created (CREATE mode)\n- Initial primary: <phrase>\n- Initial difficulty: <classification>\n\n---\n\n## Iteration check-ins (when user provides post-publish stats)\n\n### Day 7 (YYYY-MM-DD)\n- Impressions: __ · CTR: __% · Orders: __\n- Verdict: <on-track / under-impressions / impressions-but-no-clicks / clicks-but-no-sales>\n- Action: <none / monitor / pivot / fix hero image / etc.>\n\n### Day 14 (YYYY-MM-DD)\n- ...\n\n### Day 30 / 60 / 90 — same structure\n",
    "refresh-schedule.md": "# Refresh Schedule\n\n**Schema version:** 2.0\n**Last updated:** (auto-updated by skill)\n\nThis is when each listing in your database is due for its next refresh. Etsy gradually demotes listings that go untouched for 90+ days; the skill helps you maintain a refresh cadence to prevent this decay.\n\n---\n\n## Cadence rules\n\n- **Minor refresh:** every 90 days. One tag swap, one attribute update, or hero alt text refresh.\n- **Full review:** every 180 days. Re-run Phase 4 keyword research; rewrite if needed.\n\n**Priority levels** are computed against today's date:\n- **P1** = overdue (next minor refresh date already passed)\n- **P2** = within 30 days\n- **P3** = within 90 days\n- **Recent** = touched in last 90 days; skip\n\n---\n\n## Schedule\n\n| Listing ID | Last full edit | Last minor edit | Next minor | Next full review | Priority | Notes |\n|---|---|---|---|---|---|---|\n\n*Example row format (gets removed once you have real listings):*\n\n| L001 | YYYY-MM-DD | YYYY-MM-DD | YYYY-MM-DD | YYYY-MM-DD | P3 | _Initial creation_ |\n\n---\n\n## Notes\n\n- The skill updates dates on every listing touch.\n- To find what to refresh this week, ask the skill: \"What's due for refresh?\" → it scans this file and returns the P1 + P2 listings.\n",
    "sqr-imports/README.md": "# SQR Imports\n\nThis folder stores raw Search Query Report (SQR) data pasted from Etsy Shop Stats.\n\n## How to import SQR data\n\n1. In Etsy: Shop Manager → Stats → click on the listing → \"Search Terms\" tab\n2. Set window to last 30 days\n3. Manually copy the table (Etsy does not offer CSV export)\n4. In your AI chat: paste the table — the skill auto-detects the SQR shape and processes it\n\nThe skill will:\n- Identify the listing it relates to (matches against existing keyword-map entries by title or asks if ambiguous)\n- Compare the SQR queries against your current primary keyword\n- Recommend a pivot if a different query is outperforming\n- Write a new file here: `YYYY-MM-DD_L###.md`\n\n## File naming\n\n```\nYYYY-MM-DD_L###.md\n```\n\nExample: `2026-06-14_L007.md` = SQR for listing L007 imported on June 14, 2026.\n\n## Why keep old imports\n\nThe skill compares current SQR against earlier imports to detect:\n- Keywords gaining traction (rising impressions)\n- Keywords decaying (dropping impressions — often signals competitor entry)\n- New query patterns appearing\n- Lost queries (you fell off page 1)\n\nRetain SQR files for 12 months minimum.\n"
}


def state_exists(state_dir: Path) -> bool:
    """State is considered to exist if keyword-map.md is present."""
    return (state_dir / "keyword-map.md").exists()


def bootstrap(state_dir: Path, templates_dir: Path, verbose: bool = True) -> dict:
    """Create state structure from templates. Idempotent."""
    result = {
        "state_dir": str(state_dir),
        "templates_dir": str(templates_dir),
        "already_existed": False,
        "files_created": [],
        "errors": [],
    }

    if state_exists(state_dir):
        result["already_existed"] = True
        if verbose:
            print(f"[bootstrap] State already exists at {state_dir} — no action.")
        return result

    if not templates_dir.exists():
        # Fall back to the embedded templates
        state_dir.mkdir(parents=True, exist_ok=True)
        if verbose:
            print(f"[bootstrap] Created state dir: {state_dir} (embedded templates)")
        for rel, text in EMBEDDED_TEMPLATES.items():
            target = state_dir / rel
            if target.exists():
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            result["files_created"].append(rel)
        if verbose:
            print(f"[bootstrap] Done. {len(result['files_created'])} entries created.")
            print(f"[bootstrap] Your listings database is ready at: {state_dir}")
        return result

    state_dir.mkdir(parents=True, exist_ok=True)
    if verbose:
        print(f"[bootstrap] Created state dir: {state_dir}")

    # Copy every entry from the template folder, skipping OS/editor junk (.DS_Store, etc.)
    SKIP_NAMES = {".DS_Store", "__pycache__", "Thumbs.db", ".gitkeep"}
    for entry in templates_dir.iterdir():
        if entry.name in SKIP_NAMES or entry.name.startswith("."):
            continue
        target = state_dir / entry.name
        if target.exists():
            continue
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
        result["files_created"].append(str(target.relative_to(state_dir)))
        if verbose:
            print(f"[bootstrap] Copied: {entry.name}")

    if verbose:
        print(f"[bootstrap] Done. {len(result['files_created'])} entries created.")
        print(f"[bootstrap] Your listings database is ready at: {state_dir}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Bootstrap etsy-seller skill state (v2.0).")
    parser.add_argument("--state-dir", type=Path, default=None,
                        help="Where to create state (default: $ETSY_LISTINGS_DIR or ./etsy-listings)")
    parser.add_argument("--templates-dir", type=Path, default=None,
                        help="Source templates (default: ../../state-templates/etsy-listings)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    state_dir = args.state_dir or find_default_state_dir()
    templates_dir = args.templates_dir or find_default_templates_dir(script_dir)

    result = bootstrap(state_dir, templates_dir, verbose=not args.quiet)

    if result["errors"]:
        print(f"[bootstrap] Completed with {len(result['errors'])} error(s):", file=sys.stderr)
        for err in result["errors"]:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
