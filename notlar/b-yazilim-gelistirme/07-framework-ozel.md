# 07-framework-ozel — Yazılım Geliştirme

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **6/13**

### bash-linux  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** macOS/Linux Bash kalıpları: komut zincirleme operatörleri, dosya işlemleri, süreç yönetimi (port tutan süreci bulma/öldürme), metin işleme (grep/sed/awk/cut/sort), ortam değişkenleri, ağ komutları, hata işlemeli betik şablonu ve sık desenler.
- **Ne zaman:** macOS/Linux'ta terminal komutları ve bash betikleri yazarken hızlı başvuru. · **Ne zaman değil:** Windows/PowerShell ortamı (powershell-windows); model zaten bu komutları bildiği için deneyimli kullanımda düşük katkı.
- **Teknoloji:** bash
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kabuk-komutlari → birincil
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV / opsiyonel. Doğru ama temel komut tablosu; 'sed -i' gibi macOS/GNU farkı olan komutlarda uyarı yok. Araç rehberi olarak 07-framework-ozel'e taşındı.

### nextjs-react-expert  ·  vudovn/ag-kit @ 549ba3d  ·  puan 87 (A)

- **Ne yapar:** Vercel'in React/Next.js performans kurallarının ag-kit uyarlaması: 58 kural etki sırasına göre 8 dosyada, ek olarak Next.js 16 Cache Components bölümü; hızlı karar ağacı, performans inceleme kontrol listesi ve react_performance_checker.py denetim betiği.
- **Ne zaman:** ag-kit kullanan projelerde veya Cache Components notlarını aynı skillde isteyenlerde React/Next performans incelemesi. · **Ne zaman değil:** vercel-react-best-practices kuruluysa (aynı kurallar); React dışı projeler.
- **Teknoloji:** react, next.js, python · **Paketler:** python3 (react_performance_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-performans → alternatif
- **Boyut:** 111 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kurallar özgün kaynaktan geliyor ve denetim betiği bir artı, ama kural sayısı özgünden geride (58/65) ve tek dosyalarda toplu (her dosya 250-350 satır). 07-framework-ozel'e taşındı.

### powershell-windows  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Windows PowerShell tuzakları ve kalıpları: mantıksal operatörlerde cmdlet'i paranteze alma, betiklerde Unicode/emoji yasağı, null kontrolleri, karmaşık string enterpolasyonu, ErrorActionPreference ve try/catch, Join-Path ile yol işlemleri.
- **Ne zaman:** Proje Windows'ta çalışıyorsa veya PowerShell betiği yazılıyorsa; agent'ın tipik PowerShell sözdizimi hatalarını önlemek için. · **Ne zaman değil:** macOS/Linux ortamı (bash-linux).
- **Teknoloji:** powershell, windows
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kabuk-komutlari → alternatif
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (Windows ortamında kullanılır). Kısa ve agent'ların gerçekten yaptığı hatalara odaklı (parantez, Unicode). Araç rehberi olarak 07-framework-ozel'e taşındı.

### rust-pro  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** Modern Rust (2024 sürümü) uzman persona tanımı: async (Tokio), axum, sahiplik/ömür, tip sistemi ve trait'ler, performans ve sistem programlama, hata işleme yeteneklerini listeler; dört adımlı kısa talimat (kısıtları netleştir, runtime/crate seç, testle uygula, profille).
- **Ne zaman:** Rust servisi, kütüphanesi veya sistem aracı yazarken; sahiplik/ömür ve async tasarım sorunlarında. · **Ne zaman değil:** Hızlı betik veya dinamik runtime gerektiğinde; Rust yığına alınamıyorsa.
- **Teknoloji:** rust, tokio, axum · **Paketler:** rust toolchain (cargo)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** rust-gelistirme → birincil
- **Boyut:** 8 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: TUT (yalnız Rust projelerinde --skill ile). İçerik çoğunlukla yetenek listesi (anahtar kelime yığını); somut kural veya örnek az, modelin zaten bildiğini tekrar ediyor. Dil rehberi olduğu için 07-framework-ozel'e taşındı.

### vercel-composition-patterns  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Vercel'in ölçeklenen React kompozisyon desenleri: boolean prop çoğalmasını compound component, state lifting ve iç yapıyı birleştirme ile önleme; durum yönetimi (context arayüzü, implementasyonu ayırma), uygulama desenleri ve React 19 API değişiklikleri (forwardRef'siz ref vb.). Kurallar ayrı dosyalarda.
- **Ne zaman:** Çok boolean prop'lu bileşenleri refactor ederken, yeniden kullanılabilir bileşen kütüphanesi veya esnek bileşen API'si tasarlarken. · **Ne zaman değil:** Performans optimizasyonu (vercel-react-best-practices); React dışı projeler.
- **Teknoloji:** react
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** react-kompozisyon → birincil · **Roller:** frontend-muhendis · **Globalde:** claude:ayni
- **Boyut:** 49 KB (SKILL.md 3.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). Kısa SKILL.md (3 KB) ve kural dosyaları ile bağlam dostu; React 19 notları güncel. OpenMontage'a gömülü Vercel kopyası. 07-framework-ozel'e taşındı.

### vercel-react-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Vercel Engineering'in React/Next.js performans kuralları: etkiye göre 8 kategoride 65 kural (şelaleleri kaldırma, bundle boyutu, sunucu tarafı performans, istemci veri çekme, yeniden render, render performansı, JS performansı, ileri desenler); her kural ayrı dosyada iyi/kötü örnekle, tam derlenmiş AGENTS.md ile.
- **Ne zaman:** React bileşeni veya Next.js sayfası yazarken/incelerken; veri çekme, bundle ve render performansı sorunlarında. · **Ne zaman değil:** React dışı projeler; Next.js 16 Cache Components geçişi (next-cache-components-* skilleri); bileşen API tasarımı (vercel-composition-patterns).
- **Teknoloji:** react, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** react-performans → birincil · **Roller:** frontend-muhendis · **Globalde:** claude:ayni
- **Boyut:** 207 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, react-performans grubunun birincili. Gerekçe: Vercel'in özgün kural seti, kural başına dosya ile seçici okuma (SKILL.md 7 KB, toplam 207 KB); nextjs-react-expert aynı kuralların ag-kit uyarlaması. Bu kopya OpenMontage'a gömülü (upstream vercel-labs/agent-skills arşivde yok); güncellemeler OpenMontage üzerinden gelir. Dil/framework rehberi olduğu için 07-framework-ozel'e taşındı.

### next-bundle-optimizer  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Audit and reduce Next.js browser initial-load work. Use for slow route startup, oversized client bundles, duplicate browser dependencies, or features that can wait for interaction.
- **Teknoloji:** next.js, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### next-cache-components-adoption  ·  vercel/next.js @ 691ec2a  ·  puan 95 (A)

- **Ne yapar:** Turn on Cache Components in a Next.js app and resolve the blocking routes it surfaces. Use when the user wants to enable, adopt, or migrate to Cache Components, flip the `cacheComponents` flag, work through a flood of blocking-prerender / instant validation errors, run the `cache-components-instant-false` codemod, or decide between opting routes out with `export const instant = false` and fixing t
- **Teknoloji:** html, next.js, node, playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 32.6 KB, yük buyuk)
- **İnceleme:** otomatik

### next-cache-components-optimizer  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Optimize the meaningful UI available immediately from a Next.js route on an initial load (hard navigation) or named client-side navigation (soft navigation). Encode the goal as a failing @next/playwright instant() e2e and work it to green, one verified route and entry point at a time; the shipped test then guards against regression. Use when asked to grow a static shell, fix a slow first paint or 
- **Teknoloji:** next.js, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 22.6 KB, yük orta)
- **İnceleme:** otomatik

### next-dev-loop  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Verify Next.js runtime behavior after editing app code. Use this skill to confirm a change actually works in a running app — not just that it compiles or type-checks. Combines /_next/mcp (Next.js's view) with agent-browser (the browser's view). Requires a running `next dev`.
- **Teknoloji:** next.js, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** otomatik

### next-partial-prefetching-adoption  ·  vercel/next.js @ 691ec2a  ·  puan 95 (A)

- **Ne yapar:** Turn on Partial Prefetching in a Next.js app and work through the insights it surfaces. Use when the user wants to enable or adopt Partial Prefetching, flip the `partialPrefetching` flag, opt routes in with `export const prefetch = 'partial'`, audit `Link prefetch={true}` behavior, preserve existing prefetched UI with `instant()` tests, or resolve the instant-link-prefetch-partial and instant-shel
- **Teknoloji:** next.js, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 35 KB (SKILL.md 26.6 KB, yük buyuk)
- **İnceleme:** otomatik

### next-partial-prefetching-optimizer  ·  vercel/next.js @ 691ec2a  ·  puan 98 (A)

- **Ne yapar:** Optimize what selected Next.js client navigations include before the click under Partial Prefetching. Use after Cache Components and Partial Prefetching are adopted when the user wants selected URL-specific UI to be instant, wants reusable content to wait for navigation, or needs to choose between default, viewport, and intent prefetching. Requires Next.js 16.3+.
- **Teknoloji:** next.js, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### playwright-cli  ·  microsoft/playwright @ 66070a1  ·  puan 96 (A)

- **Ne yapar:** Automate browser interactions, test web pages and work with Playwright tests.
- **Teknoloji:** api-anahtari, css, html, node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 68 KB (SKILL.md 15.3 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik
