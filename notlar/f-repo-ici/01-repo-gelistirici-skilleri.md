# 01-repo-gelistirici-skilleri — Repo-İçi Geliştirici Skilleri (varsayılan listede gizli)

_Next.js, React, Playwright, Lighthouse, Motion repolarına KATKI yapanlar için iç süreç skilleri; kendi projelerinde nadiren gerekir_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **2/48**

### archify-review  ·  tt-a1i/archify @ 25cf370  ·  puan 91 (A)

- **Ne yapar:** Archify reposunun iç bakım skilli: issue, PR veya kodu değer, maliyet ve etki üzerinden değerlendirip kanıta dayalı bakım kararı verdirir; depo kökündeki REVIEWING.md ve CONTRIBUTING.md'ye yönlendirir.
- **Ne zaman:** Yalnız tt-a1i/archify reposuna katkı yaparken issue triyajı ve PR değerlendirmesi. · **Ne zaman değil:** Kendi projelerinde genel code review (code-review-and-quality); bağlantı verdiği REVIEWING.md/CONTRIBUTING.md arşivde yok.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-inceleme → alternatif
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. metadata.internal: true; değer/maliyet/etki çerçevesi kısa ve genel, asıl kurallar repo kökündeki belgelerde (kırık bağlantı). Repo-içi skill olduğu için f-repo-ici'ye taşındı.

### archify-tuning  ·  tt-a1i/archify @ 25cf370  ·  puan 89 (A)

- **Ne yapar:** Archify diyagram üretecinin doğruluk, görsel kalite ve üretim hızını deneylerle iyileştirmek için iç ayar skilli: ölçüler, ajan iz (trace) toplama, sabit girdiyle tekrar oynatma ve ekran görüntüsü karşılaştırma betikleri (Node 22.13+, Chrome) içerir.
- **Ne zaman:** Yalnız Archify reposunda yerleşim/yönlendirme/doğrulama kurallarını değiştirirken deney turu yürütmek. · **Ne zaman değil:** Archify dışındaki her proje; kod incelemesi için değil.
- **Teknoloji:** node, chromium · **Paketler:** node>=22.13, Chrome/Chromium
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★86998, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** archify-ic-surec → alternatif
- **Boyut:** 57 KB (SKILL.md 8.9 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Archify'ın kendi geliştirme döngüsüne özel (metadata.internal), kategori olarak da code review değil; CONTRIBUTING.md bağlantısı kırık, betikler repo yapısına bağlı. f-repo-ici'ye taşındı.

### authoring-skills  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** How to create and maintain agent skills in .agents/skills/. Use when creating a new SKILL.md, writing skill descriptions, choosing frontmatter fields, or deciding what content belongs in a skill vs AGENTS.md. Covers the supported spec fields, description writing, naming conventions, and the relationship between always-loaded AGENTS.md and on-demand skills.
- **Teknoloji:** next.js, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** otomatik

### backport-pr  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Backport a merged Next.js pull request from canary to an LTS release branch (releases/lts/active or releases/lts/maintenance). Use when the user asks to backport, cherry-pick, or open a backport PR from a PR number to an older Next.js version. Covers finding the merged PR commit, creating a backport branch from the target release branch, cherry-picking from canary, validating, and opening the PR w
- **Teknoloji:** git, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### compiler-commit  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you want to verify compiler changes and commit with the correct convention. Runs tests, lint, and format, then commits with the [compiler] or [rust-compiler] prefix.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** otomatik

### compiler-orchestrator  ·  react/react @ ab0d927  ·  puan 98 (A)

- **Ne yapar:** Orchestrate the Rust compiler port end-to-end. Discovers the current frontier, fixes failing passes, ports new passes, reviews, and commits in a loop.
- **Teknoloji:** node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik

### compiler-port  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Port a compiler pass from TypeScript to Rust. Gathers context, plans the port, implements in a subagent with test-fix loop, then reviews.
- **Teknoloji:** react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### compiler-review  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Review Rust port code for port fidelity, convention compliance, and error handling. Compares against the original TypeScript source.
- **Teknoloji:** git, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### compiler-verify  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you need to run all compiler checks (tests, lint, format) before committing. Detects whether TS or Rust code changed and runs the appropriate checks.
- **Teknoloji:** git, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### create-pr  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Create Git branches, commits, pushes, and GitHub pull requests for Next.js. Use when the user asks to create a branch, commit current changes, open a PR or draft PR, publish a pull request, or recover from gh pr create / PR template issues. Covers .github/pull_request_template.md, --body formatting, <agent-name>/ branch names, and Codex app git directives.
- **Teknoloji:** git, next.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### dce-edge  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** DCE-safe require() patterns and edge runtime constraints. Use when writing conditional require() calls, guarding Node-only imports (node:stream etc.), or editing define-env-plugin.ts / app-render / stream-utils for edge builds. Covers if/else branching for webpack DCE, TypeScript definite assignment, the NEXT_RUNTIME vs real feature flag distinction, and forcing flags false for edge in define-env.
- **Teknoloji:** node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### deploy-release-test  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Validate a commit-specific Next.js preview package and manually trigger the entire Next.js deployment test suite through the test_e2e_deploy_release.yml GitHub Actions workflow. Use only when asked to run the full deploy test suite or this workflow specifically from an internal vercel/next.js PR branch. Do not use for focused deployment-test sanity checks; run the relevant tests locally with pnpm 
- **Teknoloji:** next.js, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### docs-diagrams  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Draw diagrams for the Next.js docs in the style of the ones already published there: the light/dark PNGs an mdx references with `<Image srcLight="/docs/light/<name>.png" srcDark="/docs/dark/<name>.png">`. Use when a guide or API reference needs a new diagram or an existing one needs a change. Hand-written SVG from a primitives library, rendered by headless Chrome at 2x. No AI image generation.
- **Teknoloji:** api-anahtari, canvas, css, html, next.js, node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 59 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### extract-errors  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when adding new error messages to React, or seeing "unknown error code" warnings.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 0 KB (SKILL.md 0.3 KB, yük kucuk)
- **İnceleme:** otomatik

### feature-flags  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when feature flag tests fail, flags need updating, understanding @gate pragmas, debugging channel-specific test failures, or adding new flags to React.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### fix  ·  motiondivision/motion @ a03a6da  ·  puan 98 (A)

- **Ne yapar:** Take a GitHub issue, an open PR, or a plan file from plans/ and drive it to a merge-ready PR — reproduce with a failing test first, implement the fix (bugs) or feature (plans), verify against the repo's gates, and open or update the PR. Use when asked to fix an issue, implement or execute a plan, finish or land an open PR, or work through plans/issues/.
- **Teknoloji:** git, motion, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiondivision (kurum, resmî, ★34417, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** otomatik

### fix@react  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you have lint errors, formatting issues, or before committing code to ensure it passes CI.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 0 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### flags  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you need to check feature flag states, compare channels, or debug why a feature behaves differently across release channels.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** otomatik

### flags@vercel  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** How to add or modify Next.js experimental feature flags end-to-end. Use when editing config-shared.ts, config-schema.ts, define-env-plugin.ts, next-server.ts, export/worker.ts, or module.compiled.js. Covers type declaration, zod schema, build-time injection, runtime env plumbing, and the decision between runtime env-var branching vs separate bundle variants.
- **Teknoloji:** next.js, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### flow  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you need to run Flow type checking, or when seeing Flow type errors in React code.
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.9 KB, yük kucuk)
- **İnceleme:** otomatik

### gate-tests  ·  vercel/next.js @ 691ec2a  ·  puan 96 (A)

- **Ne yapar:** How to use the `@gate` / `@force-gate` test directives instead of `it.skip` or fake-green skip patterns. Use when a test is known-failing under some test-matrix dimension (dev mode, a bundler, an experimental flag like cacheComponents), when converting `if (isNextDev) return` guards or env-var `describe.skip` branches, when adding a condition to test/lib/gate/conditions.ts, or when keying a fixtur
- **Teknoloji:** react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### gh-stack  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Manages stacked PRs and splits multi-part work into reviewable branches with gh-stack. Use for stack creation, viewing, edits, push, submit, sync, rebase, merge, or checkout; when asked to split or isolate work for review; whenever a user mentions a stack, branch layers, dependent PRs, or gh stack; or when a stack is checked out.
- **Teknoloji:** git, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 9.1 KB, yük orta)
- **İnceleme:** otomatik

### improve  ·  motiondivision/motion @ a03a6da  ·  puan 96 (A)

- **Ne yapar:** Survey any codebase as a senior advisor and produce prioritized, self-contained implementation plans for OTHER models/agents to execute. Strictly read-only on source code — never implements, fixes, or refactors anything itself. Use when asked to audit a codebase, find improvement opportunities (bugs, security, performance, test coverage, tech debt, migrations, DX), suggest features or where to tak
- **Teknoloji:** api-anahtari, git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiondivision (kurum, resmî, ★34417, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 39 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** otomatik

### insight-error-page  ·  vercel/next.js @ 691ec2a  ·  puan 96 (A)

- **Ne yapar:** Write or audit an insight-kind error page for the Next.js dev overlay. Use when creating a new `errors/<slug>.mdx` page, auditing an existing one, or checking that a page matches the framework fix cards. Covers page structure, title alignment, FixCard cards with Copy prompt button, code snippets, terminology verification against canonical docs, and Vercel technical writing style.
- **Teknoloji:** html, next.js, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 21.6 KB, yük orta) · **Kırık bağlantı:** 5
- **İnceleme:** otomatik

### lighthouse-verification  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 98 (A)

- **Ne yapar:** Instructions for how to validate changes made to Lighthouse. Must invoke when making changes to Lighthouse.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### next-rspack  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Maintain @next/rspack-core and @next/rspack-binding packages. Use when editing rspack/package.json, rspack/crates/binding/Cargo.toml, rspack/rust-toolchain.toml, or packages/next-rspack/package.json. Covers upgrading @rspack/core npm version, rspack_* crate versions, Rust toolchain version, building and linking for local testing, and NEXT_RSPACK environment variable usage. Does NOT apply to root r
- **Teknoloji:** next.js, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** otomatik

### plan-update  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you need to update a plan document with deep research across all compiler passes. Launches parallel subagents to analyze how a topic affects every compiler phase, then consolidates findings into the plan doc.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** otomatik

### playwright-cherry-pick  ·  microsoft/playwright @ 66070a1  ·  puan 100 (A)

- **Ne yapar:** Cherry-pick a commit or PR from main into a release branch (release-<version>) and retitle it as cherry-pick(#<pr>): <original title>. Use when asked to cherry-pick, backport, or port a change into a release.
- **Teknoloji:** git, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### playwright-dev  ·  microsoft/playwright @ 66070a1  ·  puan 98 (A)

- **Ne yapar:** Explains how to develop Playwright - add APIs, MCP tools, CLI commands, and vendor dependencies.
- **Teknoloji:** node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 95 KB (SKILL.md 1.3 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### playwright-devops  ·  microsoft/playwright @ 66070a1  ·  puan 100 (A)

- **Ne yapar:** DevOps workflows for Playwright - CI failure analysis, workflow debugging, and release operations.
- **Teknoloji:** playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 0.4 KB, yük kucuk)
- **İnceleme:** otomatik

### playwright-release-notes  ·  microsoft/playwright @ 66070a1  ·  puan 96 (A)

- **Ne yapar:** Write the release notes for a Playwright release - the Node.js notes in docs/src/release-notes-js.md together with the Python, Java and .NET translations, and the GitHub markdown for each language's release. Use when asked to write, translate or publish release notes.
- **Teknoloji:** html, node, playwright, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.3 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### playwright-test-results  ·  microsoft/playwright @ 66070a1  ·  puan 98 (A)

- **Ne yapar:** Query Playwright CI test results from the aggregated DuckDB database. Answers questions about flaky tests, failure rates, slow tests, and per-run/SHA/PR results without hunting through GitHub artifacts.
- **Teknoloji:** api-anahtari, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.7 KB, yük orta)
- **İnceleme:** otomatik

### playwright-triage  ·  microsoft/playwright @ 66070a1  ·  puan 96 (A)

- **Ne yapar:** Triage a Playwright bug report by reproducing it from the information in the issue. Use when asked to triage, reproduce, or verify a GitHub issue (a new bug report, or an existing report with a new comment).
- **Teknoloji:** css, node, playwright, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.3 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** otomatik

### pr-status-triage  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Triage CI failures and PR review comments using scripts/pr-status.js. Use when investigating failing CI jobs, flaky tests, or PR review feedback. Covers blocker-first prioritization (build > lint > types > tests), CI env var matching for local reproduction, and the Known Flaky Tests distinction.
- **Teknoloji:** next.js, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### react-sync  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Build local React changes in the bundle variants consumed by Next.js, sync them into a local Next.js checkout, and test the resulting integration. Use when working on React changes that need validation in Next.js, or when asked to run buildForNext, pnpm sync-react, or synchronize a React checkout with Next.js.
- **Teknoloji:** next.js, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### react-vendoring  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** React vendoring and react-server layer boundaries. Use when editing entry-base.ts, $$compiled.internal.d.ts, compiled/react* packages, or taskfile.js copy_vendor_react. Covers the entry-base.ts boundary (all react-server-dom-webpack/* imports must go through it), vendored React channels, type declarations, Turbopack remap to react-server-dom-turbopack, ComponentMod access patterns, and ESLint supp
- **Teknoloji:** next.js, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### router-act  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** How to write end-to-end tests using createRouterAct and LinkAccordion. Use when writing or modifying tests that need to control the timing of internal Next.js requests (like prefetches) or assert on their responses. Covers the act API, fixture patterns, prefetch control via LinkAccordion, fake clocks, and avoiding flaky testing patterns.
- **Teknoloji:** next.js, playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta)
- **İnceleme:** otomatik

### runtime-debug  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Debug and verification workflow for runtime-bundle and module-resolution regressions. Use when diagnosing unexpected module inclusions, bundle size regressions, or CI failures related to NEXT_SKIP_ISOLATE, nft.json traces, or runtime bundle selection (module.compiled.js). Covers CI env mirroring, full stack traces via __NEXT_SHOW_IGNORE_LISTED, route trace inspection, and webpack stats diffing.
- **Teknoloji:** html, next.js, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** otomatik

### rust-port-status  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Show the status of all Rust port plan documents and recent related commits. Use when you need to understand what's been done vs what remains.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### sandbox-bench  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Benchmark React or Next.js changes on Vercel Sandbox VMs with paired A/B statistics: react PR/commit vs base, or Next.js PR/commit vs base, measured end-to-end through the bench/render-pipeline app (rps, latency, p95; TTFB, RSS and document/Flight bytes when the Next side captures them) and, for React changes, through the react repo's flight-ssr-bench fixture (Node AND Edge web-streams paths, Fizz
- **Teknoloji:** api-anahtari, git, next.js, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 160 KB (SKILL.md 16.2 KB, yük orta)
- **İnceleme:** otomatik

### test  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you need to run tests for React core. Supports source, www, stable, and experimental channels.
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### update-ard-port  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 96 (A)

- **Ne yapar:** Sync Lighthouse's Agentic Resource Discovery (ARD) port with upstream ards-project/ard-spec. Invoke when `node core/scripts/update-ard-spec.js --check` reports the ARD spec is out of sync, when the weekly cron CI job fails on it, or when asked to update the ARD conformance script, schema, or discovery rules.
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** otomatik

### update-docs  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user asks to "update documentation for my changes", "check docs for this PR", "what docs need updating", "sync docs with code", "scaffold docs for this feature", "document this feature", "review docs completeness", "add docs for this change", "what documentation is affected", "docs impact", or mentions "docs/", "docs/01-app", "docs/02-pages", "MDX", "documentatio
- **Teknoloji:** git, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 7.4 KB, yük kucuk)
- **İnceleme:** otomatik

### update-trace-engine  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 96 (A)

- **Ne yapar:** Build, validate, publish, and roll @paulirish/trace_engine from devtools-frontend into Lighthouse. Invoke when asked to update or roll the trace_engine package.
- **Teknoloji:** git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** otomatik

### v8-jit  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** V8 JIT optimization patterns for writing high-performance JavaScript in Next.js server internals. Use when writing or reviewing hot-path code in app-render, stream-utils, routing, caching, or any per-request code path. Covers hidden classes / shapes, monomorphic call sites, inline caches, megamorphic deopt, closure allocation, array packing, and profiling with --trace-opt / --trace-deopt.
- **Teknoloji:** next.js, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** otomatik

### verify  ·  react/react @ ab0d927  ·  puan 100 (A)

- **Ne yapar:** Use when you want to validate changes before committing, or when you need to check all React contribution requirements.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### write-api-reference  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Produces API reference documentation for Next.js APIs: functions, components, file conventions, directives, and config options. **Auto-activation:** User asks to write, create, or draft an API reference page. Also triggers on paths like `docs/01-app/03-api-reference/`, or keywords like "API reference", "props", "parameters", "returns", "signature". **Input sources:** Next.js source code, existing 
- **Teknoloji:** html, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta)
- **İnceleme:** otomatik

### write-guide  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Generates technical guides that teach real-world use cases through progressive examples. **Auto-activation:** User asks to write, create, or draft a guide or tutorial. Also use when converting feature documentation, API references, or skill knowledge into step-by-step learning content. **Input sources:** Feature skills, API documentation, existing code examples, or user-provided specifications. **
- **Teknoloji:** next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik
