# 07-framework-ozel — Yazılım Geliştirme

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/7**

### next-bundle-optimizer  ·  vercel/next.js @ 1984f67  ·  puan 98 (A)

- **Ne yapar:** Audit and reduce Next.js browser initial-load work. Use for slow route startup, oversized client bundles, duplicate browser dependencies, or features that can wait for interaction.
- **Teknoloji:** next.js, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### next-cache-components-adoption  ·  vercel/next.js @ 1984f67  ·  puan 95 (A)

- **Ne yapar:** Turn on Cache Components in a Next.js app and resolve the blocking routes it surfaces. Use when the user wants to enable, adopt, or migrate to Cache Components, flip the `cacheComponents` flag, work through a flood of blocking-prerender / instant validation errors, run the `cache-components-instant-false` codemod, or decide between opting routes out with `export const instant = false` and fixing t
- **Teknoloji:** html, next.js, node, playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 32.6 KB, yük buyuk)
- **İnceleme:** otomatik

### next-cache-components-optimizer  ·  vercel/next.js @ 1984f67  ·  puan 98 (A)

- **Ne yapar:** Optimize the meaningful UI available immediately from a Next.js route on an initial load (hard navigation) or named client-side navigation (soft navigation). Encode the goal as a failing @next/playwright instant() e2e and work it to green, one verified route and entry point at a time; the shipped test then guards against regression. Use when asked to grow a static shell, fix a slow first paint or 
- **Teknoloji:** next.js, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 22.6 KB, yük orta)
- **İnceleme:** otomatik

### next-dev-loop  ·  vercel/next.js @ 1984f67  ·  puan 98 (A)

- **Ne yapar:** Verify Next.js runtime behavior after editing app code. Use this skill to confirm a change actually works in a running app — not just that it compiles or type-checks. Combines /_next/mcp (Next.js's view) with agent-browser (the browser's view). Requires a running `next dev`.
- **Teknoloji:** next.js, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### next-partial-prefetching-adoption  ·  vercel/next.js @ 1984f67  ·  puan 95 (A)

- **Ne yapar:** Turn on Partial Prefetching in a Next.js app and work through the insights it surfaces. Use when the user wants to enable or adopt Partial Prefetching, flip the `partialPrefetching` flag, opt routes in with `export const prefetch = 'partial'`, audit `Link prefetch={true}` behavior, preserve existing prefetched UI with `instant()` tests, or resolve the instant-link-prefetch-partial and instant-shel
- **Teknoloji:** next.js, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 35 KB (SKILL.md 26.6 KB, yük buyuk)
- **İnceleme:** otomatik

### next-partial-prefetching-optimizer  ·  vercel/next.js @ 1984f67  ·  puan 98 (A)

- **Ne yapar:** Optimize what selected Next.js client navigations include before the click under Partial Prefetching. Use after Cache Components and Partial Prefetching are adopted when the user wants selected URL-specific UI to be instant, wants reusable content to wait for navigation, or needs to choose between default, viewport, and intent prefetching. Requires Next.js 16.3+.
- **Teknoloji:** next.js, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143113, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### playwright-cli  ·  microsoft/playwright @ 66070a1  ·  puan 96 (A)

- **Ne yapar:** Automate browser interactions, test web pages and work with Playwright tests.
- **Teknoloji:** api-anahtari, css, html, node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98217, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 68 KB (SKILL.md 15.3 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik
