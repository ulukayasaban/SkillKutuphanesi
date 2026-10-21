# T6 — Tasarım Teknolojileri: Ne İşe Yarar, Nasıl Çalışır

> Kaynak tipi **T6**: yıldızladığın tasarım kütüphaneleri. Kodları arşive indirilmez (çoğu yüzlerce MB); bu kartlar
> agent'a ve sana "bu teknoloji nasıl çalışır, ne zaman seçilir, hangi skill öğretir" bilgisini verir.
> Sürümler: 2026-10-21 itibarıyla GitHub'daki son sürüm. Güncelleme: `araclar/arsiv-guncelle.py` raporu.

**Kart düzeni:** Ne işe yarar → Nasıl çalışır (temel mantık) → Kurulum → Ne zaman seç / seçme → Performans & erişilebilirlik → Skill & rol eşleşmesi

---

## 1. Animasyon

### GSAP — `greensock/GSAP` · 3.15 · gsap.com
- **Ne işe yarar:** Web'in en yaygın profesyonel animasyon motoru; DOM, SVG, canvas, WebGL nesnelerinin herhangi bir sayısal özelliğini canlandırır.
- **Nasıl çalışır:** `gsap.to/from/fromTo(hedef, {özellikler, duration, ease})` bir **tween** üretir. Tween'ler `gsap.timeline()` içinde sıraya dizilir (`"<"`, `"+=0.2"` gibi konum parametreleriyle). Tek bir `requestAnimationFrame` döngüsü (ticker) tüm animasyonları senkronize eder. Eklentiler `gsap.registerPlugin()` ile eklenir: ScrollTrigger (scroll'a bağlama), SplitText (harf/kelime bölme), Flip (layout geçişi), MorphSVG, Draggable, Observer. 3.13'ten beri tüm eklentiler ücretsiz.
- **Kurulum:** `npm i gsap` · React: `npm i @gsap/react` → `useGSAP()` hook'u (temizliği otomatik yapar).
- **Seç:** Karmaşık sıralı animasyon, scroll hikâyesi, SVG/text efektleri, framework bağımsız iş. **Seçme:** Basit hover/fade (CSS yeter), React state'e bağlı layout animasyonu (Motion daha doğal).
- **Performans / a11y:** `transform` ve `opacity` canlandır (layout tetiklemez); `gsap.matchMedia()` ile `prefers-reduced-motion` ve breakpoint'e göre farklı animasyon.
- **Skill:** `gsap-core`, `gsap-timeline`, `gsap-plugins`, `gsap-utils`, `gsap-react`, `gsap-frameworks`, `gsap-performance`, `gsap-scrolltrigger` · **Rol:** motion-gelistirici, scroll-deneyim

### Motion (eski Framer Motion) — `motiondivision/motion` · v14.5 · motion.dev
- **Ne işe yarar:** React (ve vanilla JS) için bildirimsel animasyon kütüphanesi.
- **Nasıl çalışır:** `<motion.div animate={{x:100}} />` gibi bileşen prop'larıyla çalışır. Durum değişince otomatik canlandırır. `layout` prop'u ile FLIP tabanlı layout animasyonu, `AnimatePresence` ile çıkış animasyonu, `useScroll`/`useTransform` ile scroll'a bağlı değerler. Varsayılan geçiş **spring** fiziği. Mümkün olduğunda Web Animations API ile donanım hızlandırmalı çalışır.
- **Kurulum:** `npm i motion` → `import { motion } from "motion/react"`.
- **Seç:** React uygulamasında state/route geçişleri, liste ekleme-çıkarma, paylaşılan eleman geçişi. **Seçme:** Uzun, zaman çizelgeli sinematik sekanslar (GSAP timeline daha güçlü).
- **Performans / a11y:** `useReducedMotion()`; `MotionConfig reducedMotion="user"`.
- **Skill:** `motion-framer` (freshtechbro), `animated-component-libraries` · **Rol:** motion-gelistirici, frontend-muhendis

### Lottie Web — `airbnb/lottie-web` · v5.13
- **Ne işe yarar:** After Effects'te hazırlanıp Bodymovin ile JSON'a aktarılan animasyonları web/mobilde oynatır.
- **Nasıl çalışır:** Animasyon vektör veri olarak JSON'da durur; `lottie.loadAnimation({container, path, renderer:'svg'|'canvas'})` ile çizilir. Kare kare kontrol (`goToAndStop`, `setSpeed`) yapılabilir; scroll'a bağlanabilir.
- **Kurulum:** `npm i lottie-web` (React: `lottie-react`; daha hafif alternatif: `@lottiefiles/dotlottie-web`).
- **Seç:** Tasarımcı hazır After Effects animasyonu verdiyse (ikon, illüstrasyon, onboarding). **Seçme:** Kod ile üretilebilecek basit hareketler.
- **Performans:** Büyük JSON'lar ağırdır; `canvas` renderer çok katmanda daha hızlı.
- **Skill:** `lottie-animations` · **Rol:** motion-gelistirici

### Number Flow — `barvian/number-flow` · 0.6
- **Ne işe yarar:** Sayı değişimlerini (fiyat, sayaç, istatistik) "odometre" gibi canlandıran erişilebilir bileşen.
- **Nasıl çalışır:** Her basamak ayrı bir kolon olarak çizilir; değer değişince sadece değişen basamaklar kayar. `Intl.NumberFormat` ile yerelleştirilmiş format; ekran okuyucuya tek metin olarak okunur.
- **Kurulum:** `npm i @number-flow/react` (Vue/Svelte sürümleri de var).
- **Seç:** Dashboard KPI, fiyat değiştirici, sayaç. **Rol:** frontend-muhendis, motion-gelistirici

---

## 2. Scroll

### Lenis — `darkroomengineering/lenis` · v1.3
- **Ne işe yarar:** Hafif "smooth scroll" kütüphanesi; tarayıcının kendi scroll'unu korur (sticky, anchor, erişilebilirlik bozulmaz).
- **Nasıl çalışır:** Tekerlek/touch girdisini yakalar, hedef scroll konumuna doğru `lerp` (yumuşak yaklaşım) ile her karede `window.scrollTo` yapar. Gerçek scroll konumu değiştiği için `position: sticky` ve ScrollTrigger çalışmaya devam eder. GSAP ile: `lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker.add(t => lenis.raf(t*1000))`.
- **Kurulum:** `npm i lenis` (React: `lenis/react` → `<ReactLenis root />`).
- **Seç:** Premium his isteyen tanıtım siteleri, scroll hikâyesi. **Seçme:** Uzun içerikli doküman/uygulama ekranları (kullanıcı native scroll bekler).
- **a11y:** `prefers-reduced-motion`'da kapat; klavye scroll'u native kalır.
- **Skill:** `scroll-craft` (Lenis + GSAP kurgusu), `gsap-scrolltrigger` · **Rol:** scroll-deneyim

### r3f-scroll-rig — `14islands/r3f-scroll-rig` · v8.15
- **Ne işe yarar:** DOM'daki HTML elemanlarıyla 3D mesh'leri senkron kaydırır (görsel HTML'de yer tutar, 3D sahnede çizilir).
- **Nasıl çalışır:** Tek bir paylaşılan R3F `<Canvas>` sayfanın arkasında sabit durur. `<ScrollScene track={ref}>` her karede takip edilen DOM elemanının konumunu ölçüp 3D nesneyi oraya yerleştirir. Lenis ile entegre çalışır.
- **Seç:** "HTML görsel gibi görünen ama WebGL efektli" galeri/hero (distortion, shader hover). **Skill:** `threejs-react-three-fiber`, `web3d-integration-patterns` · **Rol:** 3d-gelistirici, scroll-deneyim

---

## 3. 3D / WebGL

### Three.js — `mrdoob/three.js` · r186 · threejs.org
- **Ne işe yarar:** Web'de 3D'nin standart kütüphanesi (WebGL2 ve WebGPU renderer).
- **Nasıl çalışır:** **Scene** (sahne ağacı) + **Camera** + **Renderer** üçlüsü. Görünen her nesne `Mesh = Geometry (şekil) + Material (yüzey)`. Işıklar, dokular (texture), yükleyiciler (GLTFLoader), post-processing (EffectComposer) üstüne eklenir. Her karede `renderer.render(scene, camera)`. Yeni: `WebGPURenderer` + TSL (node tabanlı shader dili).
- **Kurulum:** `npm i three`.
- **Seç:** Framework bağımsız 3D, tam kontrol. **Seçme:** React projesi (R3F daha düzenli).
- **Performans:** Draw call sayısını düşür (instancing, birleştirme), texture'ları KTX2/Basis ile sıkıştır, `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`.
- **Skill:** `threejs-fundamentals`, `threejs-geometry`, `threejs-materials`, `threejs-lighting`, `threejs-textures`, `threejs-loaders`, `threejs-shaders`, `threejs-postprocessing`, `threejs-animation`, `threejs-interaction`, `threejs-performance`, `threejs-asset-pipeline` · **Rol:** 3d-gelistirici

### React Three Fiber — `pmndrs/react-three-fiber` · v9.8
- **Ne işe yarar:** Three.js'i React bileşenleriyle yazmayı sağlayan renderer.
- **Nasıl çalışır:** `<Canvas>` içindeki JSX (`<mesh><boxGeometry/><meshStandardMaterial/></mesh>`) doğrudan Three.js nesnelerine dönüşür; React yeniden çizimi değil, Three.js sahne ağacı güncellenir. Her kare mantığı `useFrame((state, delta) => …)` içinde; state değişikliklerini React'e değil ref'lere yaz (performans).
- **Kurulum:** `npm i three @react-three/fiber` (v9 → React 19).
- **Skill:** `threejs-react-three-fiber` (CloudAI-X), `react-three-fiber` (freshtechbro, alternatif) · **Rol:** 3d-gelistirici

### Drei — `pmndrs/drei` · v10.7
- **Ne işe yarar:** R3F için hazır yardımcı bileşenler: `OrbitControls`, `Environment`, `useGLTF`, `Text`, `Html`, `ScrollControls`, `MeshTransmissionMaterial`, `Float`…
- **Nasıl çalışır:** Sık yazılan Three.js kalıplarını tek bileşene sarar; çoğu tembel yüklenir.
- **Seç:** Her R3F projesinde neredeyse varsayılan. **Rol:** 3d-gelistirici

### React Three A11y — `pmndrs/react-three-a11y` · v3.0 (2022, bakımı yavaş)
- **Ne işe yarar:** 3D sahnedeki nesnelere klavye odağı, ekran okuyucu etiketi ve rol verir.
- **Nasıl çalışır:** `<A11y role="button" description="…">` 3D nesneyi sarar, görünmez bir DOM eşleniği üretir. Sürüm eski: R3F v9 ile uyumunu kurulumdan önce kontrol et. **Rol:** 3d-gelistirici, qa-erisilebilirlik

### OGL — `oframe/ogl`
- **Ne işe yarar:** Çok küçük (~30 KB) minimal WebGL kütüphanesi.
- **Nasıl çalışır:** Three.js'e benzer ama soyutlama az; shader'ı kendin yazarsın. Tam ekran shader arka planı, görsel distortion gibi tek efektler için ideal. **Seç:** Paket boyutu kritik, tek efektli sayfa. **Skill:** `lightweight-3d-effects`, `threejs-shaders` (kavramlar ortak) · **Rol:** 3d-gelistirici

---

## 4. Stil, Token ve Tipografi

### Tailwind CSS — `tailwindlabs/tailwindcss` · v4.3
- **Ne işe yarar:** Utility-first CSS framework.
- **Nasıl çalışır:** Sınıf adlarını (`flex gap-4 text-lg`) tarar, sadece kullanılanların CSS'ini üretir. v4'te yapılandırma CSS içinde: `@import "tailwindcss";` + `@theme { --color-brand: …; }` — tema değerleri otomatik CSS değişkeni olur. Oxide motoru (Rust) ile hızlı derleme.
- **Kurulum:** `npm i tailwindcss @tailwindcss/vite` (veya `@tailwindcss/postcss`).
- **Skill:** `ui-styling` (ui-ux-pro-max), `tailwind-patterns` (ag-kit), `design-system` · **Rol:** frontend-muhendis, tasarim-sistemi

### Open Props — `argyleink/open-props` · v1.6
- **Ne işe yarar:** Hazır CSS değişkenleri (renk, boşluk, gölge, easing, gradient) seti — "token kütüphanesi".
- **Nasıl çalışır:** `@import "open-props/style"` → `var(--size-3)`, `var(--ease-spring-3)`… Framework bağımsız; Tailwind kullanmayan projelerde tasarım sistemi tabanı. **Rol:** tasarim-sistemi

### Capsize — `seek-oss/capsize` · metrics 4.4
- **Ne işe yarar:** Yazı tipinin üst/alt boşluklarını (leading trim) kırparak metni piksel hassasiyetinde hizalar.
- **Nasıl çalışır:** Fontun metrik verisinden (cap height, ascent, descent) negatif margin hesaplar; `createStyleObject({ capHeight, lineGap, fontMetrics })`. Böylece "16px boşluk" gerçekten 16px görünür. **Seç:** Tasarım sistemi, sıkı tipografik grid. **Rol:** tasarim-sistemi, ui-tasarimci

### Fontsource — `fontsource/fontsource`
- **Ne işe yarar:** Google Fonts ve açık kaynak fontları npm paketi olarak self-host etme.
- **Nasıl çalışır:** `npm i @fontsource-variable/inter` → `import "@fontsource-variable/inter"`; font dosyaları kendi sunucundan gelir (gizlilik, hız, offline). **Rol:** frontend-muhendis, tasarim-sistemi

---

## 5. Tasarım ↔ Kod Köprüsü ve Başlangıç Şablonu

### Figma Code Connect — `figma/code-connect` · v2.0
- **Ne işe yarar:** Figma'daki bileşeni koddaki gerçek bileşene bağlar; Dev Mode'da hazır kod örneği gösterir, Figma MCP ile agent'lar doğru bileşeni kullanır.
- **Nasıl çalışır:** `*.figma.tsx` dosyasında `figma.connect(Button, "<figma-url>", { props: { variant: figma.enum(…) } })` ile eşleme; `npx figma connect publish` ile yayınlanır. **Seç:** Figma'da tasarım sistemi olan ekipler. **Rol:** tasarim-sistemi, frontend-muhendis

### Satus — `darkroomengineering/satus` · v3.0
- **Ne işe yarar:** Darkroom'un (Lenis'in yapımcısı) Next.js App Router başlangıç şablonu: Lenis, GSAP, Theatre.js, React Three Fiber, Tailwind hazır kurulu.
- **Nasıl çalışır:** Repo şablon olarak kopyalanır; içinde `react-doctor` agent skill'i de var (arşivde `a-tasarim-onyuz/08-onyuz-test-kalite`). **Seç:** Yüksek animasyonlu tanıtım sitesine hızlı başlangıç. **Profil:** scroll-hikaye-sitesi, 3d-urun-sergisi

---

## 6. Kalite, Erişilebilirlik ve Performans

### axe-core — `dequelabs/axe-core` · v4.14 (MPL-2.0)
- **Ne işe yarar:** Otomatik erişilebilirlik (WCAG) denetim motoru.
- **Nasıl çalışır:** Sayfanın DOM'unda kurallar çalıştırır (kontrast, alt metin, ARIA, form etiketleri) ve ihlal listesi döner. Playwright ile: `@axe-core/playwright` → `new AxeBuilder({page}).analyze()`. Otomatik testler sorunların ~%50'sini bulur; klavye/ekran okuyucu testi yine gerekir. **Rol:** qa-erisilebilirlik

### Lighthouse — `GoogleChrome/lighthouse` · v13.5
- **Ne işe yarar:** Performans, erişilebilirlik, SEO, best-practices puanlaması.
- **Nasıl çalışır:** Sayfayı Chrome'da kontrollü (yavaş ağ/CPU) yükler, Core Web Vitals (LCP, CLS, INP/TBT) ölçer. `npx lighthouse <url> --view` veya CI'da `@lhci/cli` ile bütçe. **Rol:** qa-erisilebilirlik

### Playwright — `microsoft/playwright` · v1.64
- **Ne işe yarar:** Chromium/Firefox/WebKit'te uçtan uca test ve tarayıcı otomasyonu.
- **Nasıl çalışır:** Otomatik bekleme (auto-wait) yapan locator'lar (`page.getByRole('button', {name})`), ekran görüntüsü karşılaştırma (`toHaveScreenshot`), trace viewer. Agent'lar için `playwright-cli` skill'i. **Skill:** `playwright-cli`, `playwright-component-testing`, `playwright-trace`, `webapp-testing` · **Rol:** qa-erisilebilirlik

### PixelJury — `gchahal1982/pixeljury` · v0.1.5
- **Ne işe yarar:** AI ile yapılmış ön yüzler için görsel QA CLI'ı: sayfayı render eder, tasarım ve erişilebilirlik sorunlarını bulur, agent'a verilecek düzeltme prompt'u yazar.
- **Nasıl çalışır:** Playwright ile sayfayı farklı viewport'larda açar, kurallara göre ("AI slop" kalıpları, hizalama, kontrast) rapor üretir. `npx pixeljury <url>`. Henüz erken sürüm. **Rol:** qa-erisilebilirlik

### Partytown — `QwikDev/partytown` · v1.0 (T5)
- Üçüncü parti script'leri (analytics, pixel) web worker'a taşıyıp ana thread'i boşaltır; `type="text/partytown"`. Pazarlama sitelerinde INP iyileştirir.

### size-limit — `ai/size-limit` · 14.2 (T5)
- JS paket boyutu bütçesi; CI'da sınır aşılınca PR'ı kırmızıya çevirir. Animasyon/3D kütüphanesi eklenen projelerde önerilir.

---

## Hızlı seçim tablosu

| İhtiyaç | Teknoloji | Skill |
|---|---|---|
| Sıralı, sinematik animasyon | GSAP | gsap-core, gsap-timeline |
| React state/route animasyonu | Motion | motion-framer |
| Scroll hikâyesi | GSAP ScrollTrigger + Lenis | scroll-craft, gsap-scrolltrigger |
| Hazır After Effects animasyonu | Lottie | lottie-animations |
| 3D sahne (React) | R3F + Drei | threejs-react-three-fiber |
| 3D sahne (vanilla) | Three.js | threejs-fundamentals |
| Tek shader efekti, küçük paket | OGL | lightweight-3d-effects |
| HTML + WebGL senkron | r3f-scroll-rig | web3d-integration-patterns |
| Token / stil | Tailwind v4 veya Open Props | design-system, ui-styling |
| Hassas tipografi | Capsize + Fontsource | – |
| Figma ↔ kod | Code Connect | – |
| A11y / performans QA | axe-core, Lighthouse, Playwright, PixelJury | webapp-testing, playwright-cli, audit |
