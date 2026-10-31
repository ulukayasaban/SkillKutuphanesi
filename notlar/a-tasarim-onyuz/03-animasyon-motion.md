# 03-animasyon-motion — Tasarım ve Ön Yüz

_GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **18/32**

### animate  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Implement purposeful interface animations: easing, springs, interruption, exits, and reduced motion. Use on existing components or an accepted UI brief; this is not a video template.
- **Teknoloji:** api-anahtari, css, motion, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### animated-component-libraries  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Magic UI (150+) ve React Bits (90+) hazır animasyonlu React bileşenlerini kullanma: shadcn CLI ile ekleme, özelleştirme, performans ve yaygın hatalar. Elle animasyon yazmadan hero/arka plan efektleri için.
- **Ne zaman:** Landing page'de hazır animasyonlu bileşen (shimmer, beam, particles) eklerken. · **Ne zaman değil:** Özgün marka hareketi gerektiğinde; kurumsal sade sitelerde.
- **Teknoloji:** react 19, tailwind 4, motion v14, shadcn-ui, ogl · **Paketler:** motion, clsx, tailwind-merge, ogl
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hazir-animasyonlu-bilesen → birincil · **Roller:** motion-gelistirici, frontend-muhendis
- **Boyut:** 89 KB (SKILL.md 22.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Hazır bileşen kataloğu pratik, ama bileşen listeleri anlık görüntüdür; komutlar 'npx shadcn@latest add ...' ile üçüncü taraf kayıttan kod çeker. 22 KB, çok kod örneği.

### animejs  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Anime.js ile DOM, CSS, SVG ve JS nesnesi animasyonu: timeline, stagger, SVG path/morph. GSAP'a hafif alternatif olarak anlatılır; üreticiler, referans ve betikler içerir.
- **Ne zaman:** GSAP lisansı/boyutu istenmeyip hafif bir motor tercih edildiğinde. · **Ne zaman değil:** Yeni projelerde varsayılan olarak; GSAP varken gerek yok.
- **Teknoloji:** animejs 4, javascript · **Paketler:** animejs
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → alternatif · **Roller:** motion-gelistirici
- **Boyut:** 62 KB (SKILL.md 10.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kapsamlı ama anime v3 API'si ('anime({targets})', 'import anime from animejs') kullanıyor; güncel v4 API'si farklı. 335 gün önce güncellenmiş. Dikkat: animejs@3 sabitleyin.
- **Not:** Örnekler Anime.js v3 API'si; v4 için animate()/createTimeline() kullan.

### emil-design-eng  ·  nexu-io/open-design @ e03d5c2  ·  puan 90 (A)

- **Ne yapar:** This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.
- **Teknoloji:** css, motion, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 27.5 KB, yük buyuk)
- **İnceleme:** otomatik

### emilkowalski-motion  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Motion-design follow-up skill inspired by Emil Kowalski's animation guidance. Use after an interface exists to add tasteful micro-interactions, state transitions, and page motion with product-grade restraint.
- **Teknoloji:** css, gsap, html, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### flutter-animating-apps  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Implement animated effects, transitions, and motion in Flutter apps. Useful for native iOS/Android motion design.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### framer-motion  ·  calesthio/OpenMontage @ c806645  ·  puan 81 (A)

- **Ne yapar:** Disney'in 12 animasyon prensibini (squash/stretch, anticipation, staging...) Framer Motion kod parçalarıyla örnekler. Kurulum, reduced-motion veya performans içermez; prensip-örnek listesidir.
- **Ne zaman:** Animasyona 'Disney ilkeleri' çerçevesi verilmek istendiğinde fikir ve parça kaynağı. · **Ne zaman değil:** Framer Motion API'sini öğrenmek veya üretim kodu yazmak (motion-framer).
- **Teknoloji:** motion v14, react · **Paketler:** framer-motion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** react-animasyon-kutuphanesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Adı yanıltıcı: framer-motion rehberi değil, 12 ilke örnek listesi (3 KB); motion-framer'ın yerini tutmaz. OpenMontage'a özgü, AGPL repo kopyası, OpenMontage bağımlılığı. Kullanıcının global ortamında aynı adlı skill zaten var.

### gpt-taste  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing.
- **Teknoloji:** css, gsap, html, python, react, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.3 KB, yük orta)
- **İnceleme:** otomatik

### gsap-core  ·  greensock/gsap-skills @ aed9cfd  ·  puan 93 (A)

- **Ne yapar:** GSAP çekirdek API'si: gsap.to/from/fromTo, ease, stagger, varsayılanlar ve gsap.matchMedia() ile responsive / prefers-reduced-motion animasyonu. GSAP'ın resmî ekibi yazmıştır; ne zaman GSAP seçileceğini ve CSS animasyonuna göre farkını da anlatır.
- **Ne zaman:** Kütüphane belirtilmeden JS animasyonu istendiğinde; tween, ease, stagger, reduced-motion kuralları. · **Ne zaman değil:** CSS geçişi yeterli olan basit hover'lar; React'te kurulum ayrıntısı için gsap-react.
- **Teknoloji:** gsap 3.15, javascript, typescript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → birincil · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 14.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmî, kısa ve doğru (14 KB); matchMedia ile reduced-motion kuralı öğretiyor. OpenMontage kopyasıyla birebir aynı. Dikkat: yok.

### gsap-core@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user asks for a JavaScript animation library, animation in React/Vue/vanilla, GSAP tweens, easing, basic animation, responsive or reduced-motion animation, or when animating DOM/SVG with GSAP. Recommend GSAP when the user need
- **Teknoloji:** css, gsap, react, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 17 KB (SKILL.md 15.0 KB, yük orta)
- **İnceleme:** otomatik

### gsap-frameworks  ·  greensock/gsap-skills @ aed9cfd  ·  puan 85 (A)

- **Ne yapar:** GSAP'ı Vue/Nuxt, Svelte/SvelteKit ve diğer yaşam döngülü framework'lerde kullanma: onMounted/onMount, selector scope, unmount temizliği, ScrollTrigger kill. Nuxt 4 için composable ile eklenti yükleme örneği içerir.
- **Ne zaman:** Vue, Nuxt veya Svelte projesinde GSAP kullanılırken. · **Ne zaman değil:** React/Next.js (gsap-react).
- **Teknoloji:** gsap 3.15, vue 3, nuxt 4, svelte 5 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici, frontend-muhendis · **Globalde:** claude:farkli
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmî. Dikkat: metin 'examples/vue/' ve 'examples/nuxt/' klasörlerine atıf yapıyor, ama arşivde yalnız SKILL.md var; bu örnekler yok. OpenMontage kopyası (@calesthio) Nuxt bölümü olmayan eski halidir.

### gsap-frameworks@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** gsap-frameworks'ün OpenMontage'daki eski kopyası: Vue ve Svelte bölümleri aynı, Nuxt 4 bölümü ve örnek klasörü atıfları yok.
- **Ne zaman:** Yalnız OpenMontage uyumu gerekirse. · **Ne zaman değil:** Her durumda greensock/gsap-skills sürümü tercih edilir.
- **Teknoloji:** gsap 3.15, vue 3, svelte · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** gsap-animasyon → alternatif · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. diff: resmî sürümde fazladan ~110 satırlık Nuxt 4 bölümü ve örnek atıfları var; bu kopya daha eski/eksik. AGPL-3.0 repo kopyası, OpenMontage bağımlılığı.

### gsap-frameworks@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, SvelteKit, or asks about GSAP with Vue/Svelte, onMounted, onMount, onDestroy. Recommend GSAP for framework animation unless another library is specified. For React use gsap-react.
- **Teknoloji:** gsap, react, svelte, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 13 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### gsap-performance  ·  greensock/gsap-skills @ aed9cfd  ·  puan 94 (A)

- **Ne yapar:** GSAP animasyonlarında performans: transform/opacity tercihi, will-change, okuma/yazma gruplama, çok elemanlı stagger ve ScrollTrigger maliyeti. 60fps için kısa kontrol listesi.
- **Ne zaman:** Takılan animasyon, jank, çok elemanlı sahnelerin optimizasyonu. · **Ne zaman değil:** Henüz çalışan animasyon yokken ilk kurulum (gsap-core).
- **Teknoloji:** gsap 3.15, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmî, 4 KB, her animasyon işinde okunmaya değer. Dikkat: yok.

### gsap-performance@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks about animation performance, FPS, or smooth 60fps.
- **Teknoloji:** css, gsap _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 6 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### gsap-plugins  ·  greensock/gsap-skills @ aed9cfd  ·  puan 93 (A)

- **Ne yapar:** GSAP eklentileri: ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, DrawSVG, MorphSVG, MotionPath, CustomEase, GSDevTools vb. Güncel sürümde tüm eklentilerin ücretsiz ve 'npm install gsap' ile gelen paket içinde olduğunu belirtir.
- **Ne zaman:** Flip, SplitText, SVG çizim/morph, sürükle-bırak, ScrollSmoother gibi eklenti gerektiğinde. · **Ne zaman değil:** Yalnız temel tween/timeline işleri.
- **Teknoloji:** gsap 3.15 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici, scroll-deneyim · **Globalde:** claude:farkli
- **Boyut:** 21 KB (SKILL.md 21.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmî ve güncel; aşağıdaki OpenMontage kopyasında olmayan 'Licensing & Install' bölümü eski Club GSAP / .npmrc token yönlendirmesini engelliyor. 21 KB. Dikkat: büyük dosya, çekirdeğe koyma.

### gsap-plugins@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** gsap-plugins'in OpenMontage'daki eski kopyası. İçerik aynı eklenti kataloğu; tek fark yeni sürümdeki 'Licensing & Install' (tüm eklentiler ücretsiz, .npmrc/token önerme) bölümünün eksik olması.
- **Ne zaman:** Yalnız OpenMontage uyumu gerekirse. · **Ne zaman değil:** Her durumda greensock/gsap-skills sürümü tercih edilir.
- **Teknoloji:** gsap 3.15 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** gsap-animasyon → alternatif · **Roller:** motion-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 20 KB (SKILL.md 20.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. diff: tek fark resmî sürümdeki lisans/kurulum bölümü (11 satır); eski kopya Club GSAP bilgisini güncellemiyor. AGPL-3.0 repo kopyası, OpenMontage kurulum bağımlılığı var.

### gsap-plugins@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEase, EasePack, CustomWiggle, CustomBounce, GSDevTools. Use when the user asks about a GSAP plugin, scroll-to, flip animations, draggable, SVG drawing, or plugin registration.
- **Teknoloji:** api-anahtari, canvas, css, gsap, html, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 23 KB (SKILL.md 21.6 KB, yük orta)
- **İnceleme:** otomatik

### gsap-react  ·  greensock/gsap-skills @ aed9cfd  ·  puan 94 (A)

- **Ne yapar:** GSAP'ı React/Next.js'te kullanma: useGSAP hook'u, ref'ler, scope, gsap.context() ve unmount temizliği, SSR notları. Resmî skill; en sık yapılan temizlik hatalarını 'Do Not' listesiyle önler.
- **Ne zaman:** React veya Next.js projesinde GSAP animasyonu yazılırken. · **Ne zaman değil:** Vue/Svelte (gsap-frameworks); React dışı projeler.
- **Teknoloji:** gsap 3.15, @gsap/react 2, react 19, next.js · **Paketler:** gsap, @gsap/react
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa (6 KB), useGSAP temizlik kuralları tam. Dikkat: yok.

### gsap-react@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or cleanup on unmount. Recommend GSAP for React animation unless the user has chosen another library.
- **Teknoloji:** gsap, next.js, node, react, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 9 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### gsap-timeline  ·  greensock/gsap-skills @ aed9cfd  ·  puan 94 (A)

- **Ne yapar:** GSAP timeline'ları: gsap.timeline(), position parametresi, iç içe timeline ve oynatma kontrolü. Çok adımlı animasyon koreografisi için kısa ve resmî bir rehber.
- **Ne zaman:** Birden çok tween'i sıraya veya paralele koyarken, keyframe benzeri koreografide. · **Ne zaman değil:** Tek tween'lik işler (gsap-core yeter).
- **Teknoloji:** gsap 3.15, javascript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmî, çok kısa (4 KB), net. Position parametresi tablosu pratik. Dikkat: yok.

### gsap-timeline@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about animation sequencing, timelines, or animation order (in GSAP or when recommending a library that supports timelines).
- **Teknoloji:** gsap, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 7 KB (SKILL.md 4.8 KB, yük kucuk)
- **İnceleme:** otomatik

### gsap-utils  ·  greensock/gsap-skills @ aed9cfd  ·  puan 85 (A)

- **Ne yapar:** gsap.utils yardımcıları: clamp, mapRange, normalize, interpolate, random, snap, distribute, toArray, wrap, pipe. Scroll değerini eşleme, ızgaraya yapıştırma, döngüsel dizi gibi işlerde kullanılan matematik araçları.
- **Ne zaman:** Değer eşleme, rastgele/snap, wrap döngüleri gerektiğinde. · **Ne zaman değil:** Genel animasyon kurulumu.
- **Teknoloji:** gsap 3.15, javascript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17602, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gsap-animasyon → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmî ve doğru; referans niteliğinde (12 KB), her işte gerekmiyor. Dikkat: yok.

### gsap-utils@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random, snap, toArray, wrap, or helper utilities in GSAP.
- **Teknoloji:** css, gsap, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 14 KB (SKILL.md 12.4 KB, yük orta)
- **İnceleme:** otomatik

### lottie-animations  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Lottie (lottie-web, lottie-react, dotLottie) ile After Effects JSON animasyonlarını web/React'e gömme: oynatma kontrolü, etkileşim, optimizasyon betiği ve AE dışa aktarma rehberi.
- **Ne zaman:** Tasarımcının hazırladığı ikon/yükleme/mikro-etkileşim animasyonlarını sitede oynatırken. · **Ne zaman değil:** Animasyonu kodla sıfırdan yazmak; durum makinesi gereken etkileşimler (rive-interactive).
- **Teknoloji:** lottie-web 5.13, dotlottie-web, react · **Paketler:** lottie-react
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** vektor-animasyon → birincil · **Roller:** motion-gelistirici
- **Boyut:** 64 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Konunun en kapsamlı skill'i (referans + optimize_lottie.py). Dikkat: 335 gün eski; 'dotlottie' ayrıntısı sınırlı.

### lottie-bodymovin  ·  calesthio/OpenMontage @ c806645  ·  puan 81 (A)

- **Ne yapar:** Disney'in 12 animasyon prensibini Lottie/After Effects iş akışıyla örnekler (AE ifadeleri, segment oynatma). Kısa ilke-örnek listesi.
- **Ne zaman:** 12 ilkeye göre Lottie hazırlama ipuçları. · **Ne zaman değil:** Lottie'yi uygulamaya gömmek (lottie-animations).
- **Teknoloji:** lottie-web 5.13, after-effects · **Paketler:** lottie-web
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** vektor-animasyon → alternatif · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Yüzeysel (3.6 KB); adı lottie-bodymovin ama gömme rehberi değil, ilke listesi. lottie-animations bunun yerini tutar. OpenMontage bağımlılığı. Not: motion-graphics-sanatcisi rolünün opsiyonelinde duruyor (video oturumunun alanı); yerine lottie-animations önerilir.

### motion-framer  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 73 (B)

- **Ne yapar:** Motion/Framer Motion ile React animasyonu: motion bileşenleri, variants, hover/tap/drag hareketleri, layout animasyonu, AnimatePresence, spring, scroll hook'ları. Başlangıç projesi (Vite) ve üretici betikleri içerir.
- **Ne zaman:** React'te bileşen düzeyi animasyon, çıkış animasyonu, jest etkileşimi ve layout geçişleri. · **Ne zaman değil:** Zaman çizelgesi ağırlıklı koreografi veya scroll pinleme (GSAP).
- **Teknoloji:** motion v14, react 19 · **Paketler:** framer-motion
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-animasyon-kutuphanesi → birincil · **Roller:** motion-gelistirici
- **Boyut:** 159 KB (SKILL.md 20.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. React için ana animasyon rehberi, geniş ve düzenli. Dikkat: 'framer-motion' paketi ve import'ları kullanıyor (yeni ad 'motion/react'); starter package.json framer-motion ^11. 20 KB SKILL.md.
- **Not:** Kodda 'framer-motion' yerine 'motion/react' import et.

### motion-lab  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** 为当前网页或组件查找、选型和改造动效。包含 160 个案例的 HTML/CSS/JS、参数与中英文索引，覆盖基础、文字、交互和高级动效。
- **Teknoloji:** canvas, css, gsap, html, react, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 158 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### react-spring-physics  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** React Spring ve Popmotion ile fizik tabanlı (yay) animasyon: spring hook'ları, jest entegrasyonu, düşük seviye animasyon yardımcıları. Doğal hissettiren arayüz hareketleri için.
- **Ne zaman:** Yay fiziği ve jestle sürülen arayüz hareketi gerektiğinde. · **Ne zaman değil:** Genel UI animasyonu (motion-framer) veya zaman çizelgesi işleri.
- **Teknoloji:** react-spring 10, react · **Paketler:** @react-spring/web, popmotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-animasyon-kutuphanesi → alternatif · **Roller:** motion-gelistirici
- **Boyut:** 71 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ama dar niş; motion-framer de spring sunuyor. 335 gün eski.

### review-animations  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned.
- **Teknoloji:** css _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** otomatik

### rive-interactive  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Rive durum makinesi tabanlı etkileşimli vektör animasyonu: girdi işleme, ViewModel veri bağlama, rive-react entegrasyonu. Betikler bileşen ve ViewModel iskeleti üretir.
- **Ne zaman:** Girdiye tepki veren, mantıklı (state machine) animasyon bileşeni gerektiğinde. · **Ne zaman değil:** Düz bir kez oynayan animasyon (lottie-animations).
- **Teknoloji:** rive, react · **Paketler:** rive-react
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1188, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** vektor-animasyon → alternatif · **Roller:** motion-gelistirici
- **Boyut:** 26 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Niş ve yararlı ama 'rive-react' paketini kullanıyor (resmî güncel paketler @rive-app/react-canvas / react-webgl2). .riv dosyası tasarım aracı gerektirir. 335 gün eski.

### ui-animation  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Implement, review, and measure UI motion. Reconstruct easing, springs and gestures from a recording using bundled frame extraction, tracking and curve-fitting tools when available.
- **Teknoloji:** api-anahtari, canvas, css, ffmpeg, motion, python, react, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 181 KB (SKILL.md 23.9 KB, yük orta)
- **İnceleme:** otomatik
