# 07-framework-ozel — Yazılım Geliştirme

_Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme)_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **13/19**

### bash-linux  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** macOS/Linux Bash kalıpları: komut zincirleme operatörleri, dosya işlemleri, süreç yönetimi (port tutan süreci bulma/öldürme), metin işleme (grep/sed/awk/cut/sort), ortam değişkenleri, ağ komutları, hata işlemeli betik şablonu ve sık desenler.
- **Ne zaman:** macOS/Linux'ta terminal komutları ve bash betikleri yazarken hızlı başvuru. · **Ne zaman değil:** Windows/PowerShell ortamı (powershell-windows); model zaten bu komutları bildiği için deneyimli kullanımda düşük katkı.
- **Teknoloji:** bash
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kabuk-komutlari → birincil
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV / opsiyonel. Doğru ama temel komut tablosu; 'sed -i' gibi macOS/GNU farkı olan komutlarda uyarı yok. Araç rehberi olarak 07-framework-ozel'e taşındı.

### cardputer-buddy  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 100 (A)

- **Ne yapar:** Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /m
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45489, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** otomatik

### m5-onboard  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 100 (A)

- **Ne yapar:** End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45489, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 23.4 KB, yük orta)
- **İnceleme:** otomatik

### next-bundle-optimizer  ·  vercel/next.js @ 13ae649  ·  puan 99 (A)

- **Ne yapar:** Next.js'te tarayıcının ilk yükleme işini denetler ve azaltır: varsayılan 'audit' kipinde next analyze ile anlık görüntü alıp dışa aktarır, modül grafiğinden aday bölmeleri (topluluk → min-cut) kanıtla açıklar; 'fix' kipi yalnız açık istekle tek değişikliği doğrulayarak uygular ve rapor verip durur.
- **Ne zaman:** Yavaş route açılışı, şişkin istemci bundle'ı, yinelenen tarayıcı bağımlılıkları veya etkileşime ertelenebilecek özellikler. · **Ne zaman değil:** Next.js dışı projeler; statik App Shell sorunları (next-cache-components-optimizer) ve prefetch işleri (next-partial-prefetching-optimizer); next analyze içermeyen eski Next sürümleri.
- **Teknoloji:** next.js, node · **Paketler:** next (next analyze içeren sürüm)
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-bundle → birincil
- **Boyut:** 15 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel, --skill ile). Audit/fix ayrımı ve 'ölçülmüş tek değişiklik' kuralı sağlam. Not: Codex sandbox'ı port açmayı engellediği için capture sandbox dışında çalışmalı (skill bunu belirtiyor); diğer next-* skillerini npx skills add ile kurmayı önerir.

### next-cache-components-adoption  ·  vercel/next.js @ 13ae649  ·  puan 100 (A)

- **Ne yapar:** Next.js uygulamasında Cache Components'i açar ve ortaya çıkan engelleyici route'ları çözerek build'i geçirir: App Router ve app dizinini doğrular, artımlı (cache-components-instant-false codemod ile önce opt-out) ya da doğrudan stratejiyi seçtirir, sonra opt-out'ları özellik özellik tarayıcıda veya build ile doğrulayarak kaldırır.
- **Ne zaman:** cacheComponents bayrağını açmak, blocking-prerender/instant doğrulama hatası selini çözmek, 'export const instant = false' ile yerinde düzeltme arasında karar vermek. · **Ne zaman değil:** Yalnız pages/ dizinli projeler (önce App Router geçişi); Cache Components zaten benimsenmişse (optimizer); çalıştırılamayan uygulama.
- **Teknoloji:** next.js, react, typescript, playwright · **Paketler:** next>=16 (App Router)
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-cache-components → birincil
- **Boyut:** 40 KB (SKILL.md 32.6 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (opsiyonel), nextjs-cache-components grubunun birincili. Next.js ekibinin geçiş rehberi; önkoşul kontrolleri (src/app gölgelemesi, import anında DB okuma) çok titiz. 33 KB SKILL.md, yalnız geçiş işinde kurulmalı.

### next-cache-components-optimizer  ·  vercel/next.js @ 13ae649  ·  puan 100 (A)

- **Ne yapar:** Cache Components benimsenmiş Next.js 16.3+ uygulamasında bir route'un ilk yüklemede veya istemci geçişinde anında gösterdiği anlamlı UI'yi (statik kabuk) büyütür: hedefi başarısız bir @next/playwright instant() e2e testine çevirir, üretim benzeri rig'de RED → düzeltme → GREEN döngüsünü, eşitlik ve fark kontrollerini yürütür; geçen test regresyon koruması olarak kalır.
- **Ne zaman:** Yavaş ilk boyama, anında olmayan gezinme, hangi Suspense sınırının UI'yi engellediğini bulma veya instant() regresyon kapsamı ekleme. · **Ne zaman değil:** Cache Components henüz açılmadıysa (önce adoption skilli); Next.js 16.3 altı.
- **Teknoloji:** next.js, playwright, typescript · **Paketler:** next>=16.3, @next/playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-cache-components → tamamlayıcı
- **Boyut:** 50 KB (SKILL.md 22.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (opsiyonel), tamamlayıcı. Test güdümlü optimizasyonun örnek uygulaması (boş geçemeyen RED kapısı, eşitlik kontrolü); rig ve test şablonları dahil.

### next-dev-loop  ·  vercel/next.js @ 13ae649  ·  puan 100 (A)

- **Ne yapar:** Vercel'in Next.js düzenle-doğrula döngüsü: kod değişikliğinden sonra uygulamanın çalışma anında gerçekten çalıştığını iki görünümle kanıtlar — Next.js'in kendi /_next/mcp uç noktası (route, RSC, server action, sunucu logları, derleme hataları) ve gerçek Chrome süren agent-browser CLI (DOM, konsol, ağ, React fiber, vitals). Ön kontrol, döngü, tuzaklar ve kapanış adımları içerir.
- **Ne zaman:** next dev çalışırken uygulama kodu düzenlendikten sonra değişikliğin derlenmenin ötesinde çalıştığını doğrulamak. · **Ne zaman değil:** Next.js 16.3+ (Turbopack) ve agent-browser >= 0.31.1 yoksa (skill bu durumda durur); Next.js dışı projeler.
- **Teknoloji:** next.js, react, node, turbopack · **Paketler:** next>=16.3 (Turbopack), agent-browser>=0.31.1 (npm -g)
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-calisma-dogrulama → birincil · **Roller:** frontend-muhendis
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, nextjs-calisma-dogrulama grubunun birincili. Next.js ekibinin resmî skilli; iki bağımsız görünümle çapraz doğrulama ve sürüm tabanı açıkça belirtilmiş. Sert bağımlılıklar (16.3+, agent-browser) nedeniyle frontend-muhendis'te opsiyonel kalır.

### next-partial-prefetching-adoption  ·  vercel/next.js @ 13ae649  ·  puan 100 (A)

- **Ne yapar:** Next.js'te Partial Prefetching'i açar ve ortaya çıkan içgörüleri çözer: önce <Link prefetch={true}> gezinmelerini denetler, mevcut prefetch davranışını bayrak kapalıyken geçen instant() testleriyle sabitler (koruma kapısı), hedefleri benimser, bayrağı açar, URL-veri içgörülerini next dev'de tarar ve doğrular.
- **Ne zaman:** partialPrefetching bayrağını açmak, route'ları 'export const prefetch = partial' ile dahil etmek, prefetch davranışını korurken geçiş yapmak. · **Ne zaman değil:** Cache Components benimsenmemişse; Next.js 16.3 altı; seçili gezinmeleri ince ayar (optimizer).
- **Teknoloji:** next.js, playwright, typescript · **Paketler:** next>=16.3, @next/playwright
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-partial-prefetching → birincil
- **Boyut:** 35 KB (SKILL.md 26.6 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (opsiyonel), nextjs-partial-prefetching grubunun birincili. Önce koruma testi sonra geçiş kuralı davranış kaybını engelliyor; resmî ve güncel.

### next-partial-prefetching-optimizer  ·  vercel/next.js @ 13ae649  ·  puan 100 (A)

- **Ne yapar:** Partial Prefetching altında seçili istemci gezinmelerinin tıklamadan önce neyi içereceğini optimize eder: her kaynak link/hedef için prefetch edilen ve yalnız gezinmede gelen UI'yi ve tetikleyiciyi (varsayılan, viewport, intent) instant() testine çevirir, mevcut davranışı kanıtlar, en küçük değişikliği yapar ve farkı doğrular.
- **Ne zaman:** URL'ye özgü UI'nin anında gelmesini istemek, yeniden kullanılabilir içeriği gezinmeye bırakmak veya prefetch tetikleyicisi seçmek. · **Ne zaman değil:** Cache Components veya Partial Prefetching benimsenmemişse (adoption skilleri); App Shell commit edemiyorsa (önce cache-components-optimizer).
- **Teknoloji:** next.js, playwright · **Paketler:** next>=16.3, @next/playwright
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143252, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** nextjs-partial-prefetching → tamamlayıcı
- **Boyut:** 26 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (opsiyonel), tamamlayıcı. Bağlantı başına sözleşme yaklaşımı ve gözetimsiz çalışma kuralı net; adoption skilliyle birlikte kurulmalı.

### nextjs-react-expert  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Vercel'in React/Next.js performans kurallarının ag-kit uyarlaması: 58 kural etki sırasına göre 8 dosyada, ek olarak Next.js 16 Cache Components bölümü; hızlı karar ağacı, performans inceleme kontrol listesi ve react_performance_checker.py denetim betiği.
- **Ne zaman:** ag-kit kullanan projelerde veya Cache Components notlarını aynı skillde isteyenlerde React/Next performans incelemesi. · **Ne zaman değil:** vercel-react-best-practices kuruluysa (aynı kurallar); React dışı projeler.
- **Teknoloji:** react, next.js, python · **Paketler:** python3 (react_performance_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-performans → alternatif
- **Boyut:** 111 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kurallar özgün kaynaktan geliyor ve denetim betiği bir artı, ama kural sayısı özgünden geride (58/65) ve tek dosyalarda toplu (her dosya 250-350 satır). 07-framework-ozel'e taşındı.

### playwright-cli  ·  microsoft/playwright @ 66070a1  ·  puan 87 (A)

- **Ne yapar:** Microsoft'un playwright-cli aracıyla tarayıcı otomasyonu: aç/git, snapshot'taki ref'lerle tıklama/yazma/doldurma/sürükleme/yükleme, metin arama, eval, sekmeler, depolama durumu, emülasyon, ağ (istek taklidi), DevTools, izleme (trace), video kaydı, oturum yönetimi ve Playwright test üretimi; ayrıntılar ek başvuru dosyalarında.
- **Ne zaman:** Agent'ın gerçek tarayıcıda sayfayla etkileşmesi, akış doğrulaması, ekran görüntüsü/trace/video alması veya Playwright testleri üretip çalıştırması gerektiğinde. · **Ne zaman değil:** Playwright MCP sunucusu zaten kullanılıyorsa (aynı iş); playwright-cli kurulmamışsa.
- **Teknoloji:** playwright, node · **Paketler:** @playwright/cli (playwright-cli), Playwright tarayıcıları
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98926, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** tarayici-otomasyonu → birincil · **Roller:** frontend-muhendis, qa-erisilebilirlik
- **Boyut:** 68 KB (SKILL.md 15.3 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tarayici-otomasyonu grubunun birincili. Resmî (microsoft/playwright) ve kapsamlı; snapshot ref modeli token dostu. Kırık bağlantı: .playwright-cli/page-*.yml örnek çıktı yolu (çalışma anında üretilen dosya, işlevi etkilemez). a-tasarim/08'deki tarayıcı test skilleriyle örtüşme o kategorinin incelemesinde ele alınmalı.

### powershell-windows  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Windows PowerShell tuzakları ve kalıpları: mantıksal operatörlerde cmdlet'i paranteze alma, betiklerde Unicode/emoji yasağı, null kontrolleri, karmaşık string enterpolasyonu, ErrorActionPreference ve try/catch, Join-Path ile yol işlemleri.
- **Ne zaman:** Proje Windows'ta çalışıyorsa veya PowerShell betiği yazılıyorsa; agent'ın tipik PowerShell sözdizimi hatalarını önlemek için. · **Ne zaman değil:** macOS/Linux ortamı (bash-linux).
- **Teknoloji:** powershell, windows
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kabuk-komutlari → alternatif
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (Windows ortamında kullanılır). Kısa ve agent'ların gerçekten yaptığı hatalara odaklı (parantez, Unicode). Araç rehberi olarak 07-framework-ozel'e taşındı.

### rust-pro  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** Modern Rust (2024 sürümü) uzman persona tanımı: async (Tokio), axum, sahiplik/ömür, tip sistemi ve trait'ler, performans ve sistem programlama, hata işleme yeteneklerini listeler; dört adımlı kısa talimat (kısıtları netleştir, runtime/crate seç, testle uygula, profille).
- **Ne zaman:** Rust servisi, kütüphanesi veya sistem aracı yazarken; sahiplik/ömür ve async tasarım sorunlarında. · **Ne zaman değil:** Hızlı betik veya dinamik runtime gerektiğinde; Rust yığına alınamıyorsa.
- **Teknoloji:** rust, tokio, axum · **Paketler:** rust toolchain (cargo)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** rust-gelistirme → birincil
- **Boyut:** 8 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: TUT (yalnız Rust projelerinde --skill ile). İçerik çoğunlukla yetenek listesi (anahtar kelime yığını); somut kural veya örnek az, modelin zaten bildiğini tekrar ediyor. Dil rehberi olduğu için 07-framework-ozel'e taşındı.

### vercel-composition-patterns  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 88 (A)

- **Ne yapar:** React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers on tasks involving compound components, render props, context providers, or component architecture. Includes React 19 API changes.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33279, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** react-kompozisyon → birincil · **Globalde:** claude:farkli
- **Boyut:** 49 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik
- **Not:** Vercel'in resmî kaynağı (OpenMontage kopyalarının güncel aslı).

### vercel-composition-patterns@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Vercel'in ölçeklenen React kompozisyon desenleri: boolean prop çoğalmasını compound component, state lifting ve iç yapıyı birleştirme ile önleme; durum yönetimi (context arayüzü, implementasyonu ayırma), uygulama desenleri ve React 19 API değişiklikleri (forwardRef'siz ref vb.). Kurallar ayrı dosyalarda.
- **Ne zaman:** Çok boolean prop'lu bileşenleri refactor ederken, yeniden kullanılabilir bileşen kütüphanesi veya esnek bileşen API'si tasarlarken. · **Ne zaman değil:** Performans optimizasyonu (vercel-react-best-practices); React dışı projeler.
- **Teknoloji:** react
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73673, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** react-kompozisyon → alternatif · **Globalde:** claude:ayni
- **Boyut:** 49 KB (SKILL.md 3.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). Kısa SKILL.md (3 KB) ve kural dosyaları ile bağlam dostu; React 19 notları güncel. OpenMontage'a gömülü Vercel kopyası. 07-framework-ozel'e taşındı.
- **Not:** Ön kontroldeki 'OpenMontage kurulumu gerekir' uyarısı bu skill için geçersiz: kaynaklar.json'daki repo düzeyi bağımlılık notundan geliyor; içerik saf React kompozisyon kuralları, OpenMontage araçlarını çağırmaz.

### vercel-react-best-practices  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 88 (A)

- **Ne yapar:** React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
- **Teknoloji:** css, next.js, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33279, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** react-performans → birincil · **Globalde:** claude:farkli
- **Boyut:** 225 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik
- **Not:** Vercel'in resmî kaynağı (OpenMontage kopyalarının güncel aslı).

### vercel-react-best-practices@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Vercel Engineering'in React/Next.js performans kuralları: etkiye göre 8 kategoride 65 kural (şelaleleri kaldırma, bundle boyutu, sunucu tarafı performans, istemci veri çekme, yeniden render, render performansı, JS performansı, ileri desenler); her kural ayrı dosyada iyi/kötü örnekle, tam derlenmiş AGENTS.md ile.
- **Ne zaman:** React bileşeni veya Next.js sayfası yazarken/incelerken; veri çekme, bundle ve render performansı sorunlarında. · **Ne zaman değil:** React dışı projeler; Next.js 16 Cache Components geçişi (next-cache-components-* skilleri); bileşen API tasarımı (vercel-composition-patterns).
- **Teknoloji:** react, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73673, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** react-performans → alternatif · **Roller:** frontend-muhendis · **Globalde:** claude:ayni
- **Boyut:** 207 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, react-performans grubunun birincili. Gerekçe: Vercel'in özgün kural seti, kural başına dosya ile seçici okuma (SKILL.md 7 KB, toplam 207 KB); nextjs-react-expert aynı kuralların ag-kit uyarlaması. Bu kopya OpenMontage'a gömülü (upstream vercel-labs/agent-skills arşivde yok); güncellemeler OpenMontage üzerinden gelir. Dil/framework rehberi olduğu için 07-framework-ozel'e taşındı.
- **Not:** Ön kontroldeki 'OpenMontage kurulumu gerekir' uyarısı bu skill için geçersiz: kaynaklar.json'daki repo düzeyi bağımlılık notundan geliyor; içerik saf React/Next.js kuralları, OpenMontage araçlarını çağırmaz.

### vercel-react-native-skills  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 88 (A)

- **Ne yapar:** React Native and Expo best practices for building performant mobile apps. Use when building React Native components, optimizing list performance, implementing animations, or working with native modules. Triggers on tasks involving React Native, Expo, mobile performance, or native platform APIs.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33279, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 155 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### vercel-react-view-transitions  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 86 (A)

- **Ne yapar:** Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) n
- **Teknoloji:** css, next.js, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33279, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 119 KB (SKILL.md 14.1 KB, yük orta)
- **İnceleme:** otomatik
