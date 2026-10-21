# 03-animasyon-motion — Tasarım ve Ön Yüz

_GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **17/17**

### animated-component-libraries  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Hazır animasyonlu React bileşen koleksiyonları: Magic UI (Tailwind + Motion, shadcn uyumlu) ve React Bits (az bağımlılıklı, bazıları OGL/WebGL). Bileşen seçimi, kurulum, özelleştirme ve prop üreteci betikleri.
- **Ne zaman:** Landing page/pazarlama sitesinde hızlıca hazır animasyonlu hero, metin efekti, arka plan veya bento grid eklemek. · **Ne zaman değil:** Özgün, markaya özel hareket dili gereken projeler (hazır bileşenler 'şablon' görünür); React dışı yığınlar.
- **Teknoloji:** react 19, tailwind 4, motion v14, shadcn-ui, ogl · **Paketler:** motion, tailwindcss, shadcn (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hazir-animasyonlu-bilesen → birincil · **Roller:** motion-gelistirici, frontend-muhendis
- **Boyut:** 89 KB (SKILL.md 22.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Hazır bileşen için kategoride tek skill. Magic UI örnekleri güncel ('motion/react'); React Bits bölümü hâlâ 'npm install framer-motion' diyor. Kopyala-yapıştır akışı yerine shadcn CLI kayıtları tercih edilmeli.

### animejs  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Anime.js ile DOM/CSS/SVG/JS nesnesi animasyonu: timeline, stagger, keyframe, SVG yol ve morph animasyonları; Python ile animasyon/timeline kod üreteci betikleri içerir.
- **Ne zaman:** Projede zaten Anime.js varsa veya çok hafif bir GSAP alternatifi isteniyorsa (kodu v4'e uyarlayarak). · **Ne zaman değil:** Yeni projelerde varsayılan olarak (gsap-core birincil); örnekler Anime.js v3 API'siyle yazıldığı için doğrudan kopyalanmamalı.
- **Teknoloji:** animejs 4, javascript · **Paketler:** animejs
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → alternatif
- **Boyut:** 62 KB (SKILL.md 10.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. Güncel değil: tüm örnekler v3 API'si (import anime from 'animejs'; anime({targets…})). Anime.js v4 (2025) adlandırılmış export'lara geçti: import { animate, createTimeline, stagger } from 'animejs'; animate(hedef, {…}). npm'den bugün kurulan sürümle örnekler çalışmaz.
- **Not:** Örnekler Anime.js v3 API'si; v4 için animate()/createTimeline() kullan.

### framer-motion  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Disney'in 12 animasyon ilkesini (squash & stretch, anticipation, staging, follow-through, easing, arcs…) Framer Motion örnekleriyle gösteren kısa ilke kartı (3 KB).
- **Ne zaman:** Motion ile yazılan animasyonlara 'canlılık' ilkeleri eklemek; animasyon eleştirisi. · **Ne zaman değil:** Motion API'sini öğrenmek (motion-framer); React dışı projeler.
- **Teknoloji:** motion v14, react · **Paketler:** motion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** react-animasyonu → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Çok kısa ve ucuz; API öğretmez, ilke uygular. Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### gsap-core  ·  greensock/gsap-skills @ aed9cfd  ·  puan 95 (A)

- **Ne yapar:** GreenSock'un resmî GSAP çekirdek skilli: gsap.to/from/fromTo, easing, duration, stagger, defaults ve gsap.matchMedia() ile responsive ve prefers-reduced-motion uyumlu animasyon. Ne zaman GSAP önerileceğini ve temel hataları (transform kısaltmaları, autoAlpha, immediateRender) anlatır.
- **Ne zaman:** DOM/SVG animasyonu yazılan her projede GSAP temel API'si; vanilla, React, Vue veya Svelte fark etmez. · **Ne zaman değil:** Sadece basit hover/fade (CSS yeter); React state'e bağlı layout/çıkış animasyonları (motion-framer daha doğal).
- **Teknoloji:** gsap 3.15, javascript, typescript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → birincil · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 14.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. dom-animasyon-motoru grubunun birincili: resmî kaynak, GSAP 3.13+ (tüm eklentiler ücretsiz) dönemine güncel, kısa (14 KB). OpenMontage'daki gsap-core birebir aynı kopya (arşivde tek kayıt).

### gsap-frameworks  ·  greensock/gsap-skills @ aed9cfd  ·  puan 95 (A)

- **Ne yapar:** Resmî GSAP skilli Vue, Nuxt 4, Svelte/SvelteKit ve diğer React dışı çatılar için: yaşam döngüsü (onMounted/onMount), seçici kapsamı, unmount'ta gsap.context().revert() ile temizlik, Nuxt'ta eklenti kaydı ve tembel yükleme.
- **Ne zaman:** Vue/Nuxt veya Svelte/SvelteKit projesinde GSAP kullanılırken. · **Ne zaman değil:** React projeleri (gsap-react); vanilla JS (gsap-core yeter).
- **Teknoloji:** gsap 3.15, vue 3, nuxt 4, svelte 5 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Birincil sürüm: OpenMontage kopyasında olmayan Nuxt 4 bölümü var. Not: SKILL.md'nin andığı examples/vue ve examples/nuxt klasörleri arşive alınmamış (skill klasörü dışında); metin onlarsız da yeterli.

### gsap-frameworks@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** gsap-frameworks skillinin OpenMontage'daki eski kopyası: Vue ve Svelte kalıpları aynı, Nuxt 4 bölümü yok.
- **Ne zaman:** Yalnızca OpenMontage içi tutarlılık gerektiğinde. · **Ne zaman değil:** Normalde: greensock sürümü (gsap-frameworks) daha kapsamlı.
- **Teknoloji:** gsap 3.15, vue 3, svelte · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** dom-animasyon-motoru → alternatif · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kaynağın eski kopyası (Nuxt 4 eksik). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### gsap-performance  ·  greensock/gsap-skills @ aed9cfd  ·  puan 97 (A)

- **Ne yapar:** Resmî GSAP performans skilli: transform/opacity tercih et, layout thrashing'den kaçın, will-change'i ölçülü kullan, quickTo/quickSetter ve toplu güncelleme ile 60 fps hedefle.
- **Ne zaman:** Takılan (jank) animasyonları düzeltme, mobilde FPS sorunları, çok sayıda eleman canlandırma. · **Ne zaman değil:** Genel performans optimizasyonu (bundle, LCP vb.); GSAP dışı kütüphaneler.
- **Teknoloji:** gsap 3.15, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. 4 KB ile en ucuz bağlam; resmî, güncel, her motion rolüne çekirdek olarak uygun.

### gsap-plugins  ·  greensock/gsap-skills @ aed9cfd  ·  puan 95 (A)

- **Ne yapar:** Resmî GSAP eklentileri skilli: kayıt (registerPlugin), ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, DrawSVG/MorphSVG/MotionPath, CustomEase ve GSDevTools. Tüm eklentilerin artık ücretsiz ve public npm paketinde olduğunu açıkça yazar.
- **Ne zaman:** SplitText metin animasyonu, Flip layout geçişi, Draggable, SVG çizim/morph, smooth scroll (ScrollSmoother) gibi eklenti gerektiren işler. · **Ne zaman değil:** Eklenti gerektirmeyen temel animasyonlar; scroll tetikleyicileri (gsap-scrolltrigger).
- **Teknoloji:** gsap 3.15 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici, scroll-deneyim · **Globalde:** claude:farkli
- **Boyut:** 21 KB (SKILL.md 21.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Birincil sürüm: OpenMontage kopyasında olmayan 'Licensing & Install' bölümü var (eski Club GSAP .npmrc/token talimatlarını önler).

### gsap-plugins@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** gsap-plugins skillinin OpenMontage'daki eski anlık görüntüsü: aynı eklenti anlatımı, fakat eklentilerin ücretsiz olduğunu ve token/özel registry kullanılmaması gerektiğini anlatan lisans bölümü yok.
- **Ne zaman:** Yalnızca OpenMontage içinde zaten kurulu kopyayla tutarlılık gerektiğinde. · **Ne zaman değil:** Normalde: greensock/gsap-skills sürümü (gsap-plugins) daha güncel.
- **Teknoloji:** gsap 3.15 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** dom-animasyon-motoru → alternatif · **Globalde:** claude:farkli
- **Boyut:** 20 KB (SKILL.md 20.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kaynağın eski kopyası; lisans/kurulum bölümü eksik. Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### gsap-react  ·  greensock/gsap-skills @ aed9cfd  ·  puan 97 (A)

- **Ne yapar:** Resmî GSAP + React skilli: @gsap/react paketinin useGSAP() hook'u, scope ile seçici sınırlama, contextSafe ile olay işleyicileri, SSR/Next.js ve otomatik temizlik.
- **Ne zaman:** React veya Next.js projesinde GSAP kullanılırken (bileşen ömrü, temizlik, StrictMode). · **Ne zaman değil:** React dışı projeler (Vue/Svelte için gsap-frameworks); GSAP kullanılmayan React animasyonları (motion-framer).
- **Teknoloji:** gsap 3.15, @gsap/react 2, react 19, next.js · **Paketler:** gsap, @gsap/react
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. useGSAP kalıbını doğru öğretiyor (gsap.context elle yönetimi yerine). Resmî, güncel; OpenMontage kopyası aynı.

### gsap-timeline  ·  greensock/gsap-skills @ aed9cfd  ·  puan 97 (A)

- **Ne yapar:** Resmî GSAP timeline skilli: gsap.timeline() ile sıralama, konum parametreleri ('<', '+=0.2', etiketler), iç içe timeline'lar ve oynatma kontrolü (play/pause/reverse/seek).
- **Ne zaman:** Birden fazla adımlı, sıralı veya örtüşen animasyon koreografisi (hero girişleri, intro sekansları). · **Ne zaman değil:** Tek tween'lik basit animasyonlar; scroll'a bağlı zamanlama (gsap-scrolltrigger ile birlikte kullan).
- **Teknoloji:** gsap 3.15, javascript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa (4 KB), resmî ve güncel; gsap-core'un doğal tamamlayıcısı. OpenMontage kopyası birebir aynı.

### gsap-utils  ·  greensock/gsap-skills @ aed9cfd  ·  puan 95 (A)

- **Ne yapar:** Resmî GSAP yardımcıları skilli: gsap.utils içindeki clamp, mapRange, normalize, interpolate, snap, wrap, distribute, toArray, random, pipe gibi fonksiyonlar ve kullanım örnekleri.
- **Ne zaman:** Değer eşleme/kırpma, rastgele dağıtım, stagger hesapları, imleç/scroll'a bağlı değer dönüşümleri. · **Ne zaman değil:** Temel tween/timeline yazımı (gsap-core yeter).
- **Teknoloji:** gsap 3.15, javascript · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dom-animasyon-motoru → tamamlayıcı · **Roller:** motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmî ve doğru; ama her projede gerekmez, opsiyonel tut.

### lottie-animations  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** After Effects/Bodymovin JSON animasyonlarını web ve React'te oynatma: lottie-web, @lottiefiles/dotlottie-web ve dotlottie-react, lottie-react; oynatma kontrolü, etkileşim, scroll'a bağlama ve performans. JSON küçültme ve React bileşeni üretme betikleri içerir.
- **Ne zaman:** Tasarımcının hazırladığı After Effects animasyonu (ikon, illüstrasyon, onboarding, yükleme) siteye konacaksa. · **Ne zaman değil:** Kodla kolayca üretilebilecek basit hareketler; durum makinesi gereken etkileşimli animasyon (rive-interactive).
- **Teknoloji:** lottie-web 5.13, dotlottie-web, react · **Paketler:** @lottiefiles/dotlottie-web, @lottiefiles/dotlottie-react, lottie-web
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarimci-animasyonu → birincil · **Roller:** motion-gelistirici
- **Boyut:** 64 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Seçim gerekçesi: dotLottie'yi (modern, küçük dosya) önerir, kurulum/oynatma/performans kapsamı tam; lottie-bodymovin yalnızca ilke kartı.

### lottie-bodymovin  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Disney'in 12 animasyon ilkesini After Effects'te kurup Bodymovin/Lottie ile dışa aktarma ve playSegments/setSpeed ile çalışma zamanında uygulama üzerine kısa ilke kartı.
- **Ne zaman:** Lottie animasyonu tasarlanırken/eleştirilirken ilke rehberi olarak. · **Ne zaman değil:** Lottie kurulumu ve oynatıcı seçimi (lottie-animations).
- **Teknoloji:** lottie-web 5.13, after-effects · **Paketler:** lottie-web
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tasarimci-animasyonu → tamamlayıcı · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Kısa (4 KB), işlevsel ama derinliği az. Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### motion-framer  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Motion (eski Framer Motion) ile React animasyonu: motion bileşenleri, variants, hover/tap/drag jestleri, layout animasyonu, AnimatePresence çıkış animasyonu, spring fiziği ve useScroll/useTransform ile scroll'a bağlı değerler. Vite başlangıç projesi ve varyant üreteci betikleri içerir.
- **Ne zaman:** React uygulamasında state/route geçişleri, mikro etkileşim, liste ekleme-çıkarma, paylaşılan eleman geçişi. · **Ne zaman değil:** Uzun sinematik sekanslar ve scroll hikâyesi (GSAP timeline/ScrollTrigger daha güçlü); React dışı projeler.
- **Teknoloji:** motion v14, react 19 · **Paketler:** motion
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-animasyonu → birincil · **Roller:** motion-gelistirici, frontend-muhendis
- **Boyut:** 159 KB (SKILL.md 20.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). react-animasyonu grubunda en kapsamlı Motion skilli; seçim gerekçesi: tam API kapsamı (layout, AnimatePresence, jestler, scroll). Dikkat: örnekler eski paket adını kullanıyor (import from 'framer-motion'); güncel kurulum npm i motion + import { motion } from 'motion/react'. Başlangıç projesi React 18 / framer-motion 11.
- **Not:** Kodda 'framer-motion' yerine 'motion/react' import et.

### react-spring-physics  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** React Spring (@react-spring/web, @react-spring/three) ile yay fiziği tabanlı animasyon: useSpring, useTrail, useTransition, jestlerle sürükleme; düşük seviye yardımcılar için Popmotion. Yay parametresi hesaplayıcı betikler içerir.
- **Ne zaman:** Projede react-spring zaten varsa; fiziksel olarak kesintisiz, jest tabanlı arayüzler; R3F sahnesinde @react-spring/three. · **Ne zaman değil:** Yeni React projelerinde varsayılan (motion-framer yay fiziğini de kapsar); Popmotion kısmı (kütüphane Motion'a devredildi, bakımsız).
- **Teknoloji:** react-spring 10, react · **Paketler:** @react-spring/web, @use-gesture/react
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-animasyonu → alternatif
- **Boyut:** 71 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. react-spring kısmı geçerli; Popmotion artık ayrı geliştirilmiyor (Motion'a katıldı). freshtechbro 2025-11'den beri güncellenmedi.

### rive-interactive  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Rive ile durum makinesi tabanlı etkileşimli vektör animasyonu: state machine girdileri, ViewModel veri bağlama, React entegrasyonu ve olay dinleme. ViewModel ve bileşen üreteci betikleri içerir.
- **Ne zaman:** Girdiye/duruma göre tepki veren animasyon (etkileşimli buton, karakter, onboarding) gerektiğinde; Lottie yetmediğinde. · **Ne zaman değil:** Tek yönlü oynatılan basit animasyon (lottie-animations); Rive editörüne erişim yoksa.
- **Teknoloji:** rive, react · **Paketler:** @rive-app/react-canvas
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarimci-animasyonu → alternatif
- **Boyut:** 26 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. ViewModel veri bağlama gibi yeni API'leri kapsıyor; ama import'lar eski 'rive-react' paket adını kullanıyor (güncel: @rive-app/react-canvas veya @rive-app/react-webgl2).
