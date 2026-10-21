# Repo-İçi Geliştirici Skilleri (gizli)

> Bu skiller ilgili repoya katkı yapanlar içindir. Arama: `skill-ekle.py --listele --gizli --kategori f-repo-ici`

| Skill | Repo | Ne yapar |
|---|---|---|
| `authoring-skills` | vercel/next.js | How to create and maintain agent skills in .agents/skills/. Use when creating a new SKILL.md, writing skill de |
| `backport-pr` | vercel/next.js | Backport a merged Next.js pull request from canary to an LTS release branch (releases/lts/active or releases/l |
| `compiler-commit` | react/react | Use when you want to verify compiler changes and commit with the correct convention. Runs tests, lint, and for |
| `compiler-orchestrator` | react/react | Orchestrate the Rust compiler port end-to-end. Discovers the current frontier, fixes failing passes, ports new |
| `compiler-port` | react/react | Port a compiler pass from TypeScript to Rust. Gathers context, plans the port, implements in a subagent with t |
| `compiler-review` | react/react | Review Rust port code for port fidelity, convention compliance, and error handling. Compares against the origi |
| `compiler-verify` | react/react | Use when you need to run all compiler checks (tests, lint, format) before committing. Detects whether TS or Ru |
| `create-pr` | vercel/next.js | Create Git branches, commits, pushes, and GitHub pull requests for Next.js. Use when the user asks to create a |
| `dce-edge` | vercel/next.js | DCE-safe require() patterns and edge runtime constraints. Use when writing conditional require() calls, guardi |
| `deploy-release-test` | vercel/next.js | Validate a commit-specific Next.js preview package and manually trigger the entire Next.js deployment test sui |
| `docs-diagrams` | vercel/next.js | Draw diagrams for the Next.js docs in the style of the ones already published there: the light/dark PNGs an md |
| `extract-errors` | react/react | Use when adding new error messages to React, or seeing "unknown error code" warnings. |
| `feature-flags` | react/react | Use when feature flag tests fail, flags need updating, understanding @gate pragmas, debugging channel-specific |
| `fix` | motiondivision/motion | Take a GitHub issue, an open PR, or a plan file from plans/ and drive it to a merge-ready PR — reproduce with  |
| `fix@react` | react/react | Use when you have lint errors, formatting issues, or before committing code to ensure it passes CI. |
| `flags` | react/react | Use when you need to check feature flag states, compare channels, or debug why a feature behaves differently a |
| `flags@vercel` | vercel/next.js | How to add or modify Next.js experimental feature flags end-to-end. Use when editing config-shared.ts, config- |
| `flow` | react/react | Use when you need to run Flow type checking, or when seeing Flow type errors in React code. |
| `gate-tests` | vercel/next.js | How to use the `@gate` / `@force-gate` test directives instead of `it.skip` or fake-green skip patterns. Use w |
| `gh-stack` | vercel/next.js | Manages stacked PRs and splits multi-part work into reviewable branches with gh-stack. Use for stack creation, |
| `improve` | motiondivision/motion | Survey any codebase as a senior advisor and produce prioritized, self-contained implementation plans for OTHER |
| `insight-error-page` | vercel/next.js | Write or audit an insight-kind error page for the Next.js dev overlay. Use when creating a new `errors/<slug>. |
| `lighthouse-verification` | GoogleChrome/lighthouse | Instructions for how to validate changes made to Lighthouse. Must invoke when making changes to Lighthouse. |
| `next-rspack` | vercel/next.js | Maintain @next/rspack-core and @next/rspack-binding packages. Use when editing rspack/package.json, rspack/cra |
| `plan-update` | react/react | Use when you need to update a plan document with deep research across all compiler passes. Launches parallel s |
| `playwright-cherry-pick` | microsoft/playwright | Cherry-pick a commit or PR from main into a release branch (release-<version>) and retitle it as cherry-pick(# |
| `playwright-dev` | microsoft/playwright | Explains how to develop Playwright - add APIs, MCP tools, CLI commands, and vendor dependencies. |
| `playwright-devops` | microsoft/playwright | DevOps workflows for Playwright - CI failure analysis, workflow debugging, and release operations. |
| `playwright-release-notes` | microsoft/playwright | Write the release notes for a Playwright release - the Node.js notes in docs/src/release-notes-js.md together  |
| `playwright-test-results` | microsoft/playwright | Query Playwright CI test results from the aggregated DuckDB database. Answers questions about flaky tests, fai |
| `playwright-triage` | microsoft/playwright | Triage a Playwright bug report by reproducing it from the information in the issue. Use when asked to triage,  |
| `pr-status-triage` | vercel/next.js | Triage CI failures and PR review comments using scripts/pr-status.js. Use when investigating failing CI jobs,  |
| `react-sync` | vercel/next.js | Build local React changes in the bundle variants consumed by Next.js, sync them into a local Next.js checkout, |
| `react-vendoring` | vercel/next.js | React vendoring and react-server layer boundaries. Use when editing entry-base.ts, $$compiled.internal.d.ts, c |
| `router-act` | vercel/next.js | How to write end-to-end tests using createRouterAct and LinkAccordion. Use when writing or modifying tests tha |
| `runtime-debug` | vercel/next.js | Debug and verification workflow for runtime-bundle and module-resolution regressions. Use when diagnosing unex |
| `rust-port-status` | react/react | Show the status of all Rust port plan documents and recent related commits. Use when you need to understand wh |
| `sandbox-bench` | vercel/next.js | Benchmark React or Next.js changes on Vercel Sandbox VMs with paired A/B statistics: react PR/commit vs base,  |
| `test` | react/react | Use when you need to run tests for React core. Supports source, www, stable, and experimental channels. |
| `update-ard-port` | GoogleChrome/lighthouse | Sync Lighthouse's Agentic Resource Discovery (ARD) port with upstream ards-project/ard-spec. Invoke when `node |
| `update-docs` | vercel/next.js | This skill should be used when the user asks to "update documentation for my changes", "check docs for this PR |
| `update-trace-engine` | GoogleChrome/lighthouse | Build, validate, publish, and roll @paulirish/trace_engine from devtools-frontend into Lighthouse. Invoke when |
| `v8-jit` | vercel/next.js | V8 JIT optimization patterns for writing high-performance JavaScript in Next.js server internals. Use when wri |
| `verify` | react/react | Use when you want to validate changes before committing, or when you need to check all React contribution requ |
| `write-api-reference` | vercel/next.js | Produces API reference documentation for Next.js APIs: functions, components, file conventions, directives, an |
| `write-guide` | vercel/next.js | Generates technical guides that teach real-world use cases through progressive examples. **Auto-activation:**  |
