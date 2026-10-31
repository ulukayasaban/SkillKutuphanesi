# T5 — Diğer Kütüphane ve Araçlar (referans)

> Kodları indirilmez. Tasarım teknolojileri ayrı dosyada: `tasarim-teknolojileri.md` (T6).

| Repo | Ne işe yarar | Ne zaman | İlgili skill / rol |
|---|---|---|---|
| vercel/next.js | React tabanlı full-stack framework (App Router, Server Components, Cache Components) | Web sitesi/uygulama iskeleti | `next-dev-loop`, `next-bundle-optimizer`, `next-cache-components-*`, `next-partial-prefetching-*` · frontend-muhendis |
| react/react | UI kütüphanesi (v19: Actions, `use`, React Compiler) | Tüm React projeleri | `frontend-ui-engineering`, `react-doctor` |
| microsoft/playwright | Tarayıcı testi ve otomasyon | E2E test, görsel regresyon | `playwright-cli`, `webapp-testing` · qa-erisilebilirlik |
| GoogleChrome/lighthouse | Performans/a11y/SEO denetimi | Yayın öncesi kontrol, CI bütçesi | `performance-optimization` · qa-erisilebilirlik |
| QwikDev/partytown | 3. parti script'leri web worker'a taşır | Analytics yüklü pazarlama siteleri | performans |
| ai/size-limit | JS paket boyutu bütçesi (CI) | Ağır animasyon/3D kütüphanesi olan projeler | `gsap-performance`, `threejs-performance` |
| FFmpeg/FFmpeg | Video/ses dönüştürme | Video arka plan, sıkıştırma, GIF→MP4 | `ffmpeg` skill'i (OpenMontage kaynaklı, arşivde) |
| anthropics/claude-code | Claude Code CLI; repodaki plugin skilleri arşivde (T2) | Claude Code plugin/hook geliştirme | `plugin-structure`, `hook-development`… |
| arturitu/the-delegation | (skill içermiyor) proje referansı | – | – |
| linvi/tweetinvi | C# Twitter/X API kütüphanesi | .NET ile X entegrasyonu | – |
| zhuyansen/awesome-claude-video-skills | (skill içermiyor) Claude Code/Codex ile video yapan 300+ skill reposunun türe göre, güvenlik notlu keşif listesi | Yeni video skilli ararken; aday repoyu kütüphaneye eklemeden önce `rehber/03` çakışma + ücret kontrolü | video-kompozisyon, video-kurgu-render |
| Fei-Away/Codex-Dream-Skin | Codex Desktop'a duvar kağıdı/tema giydiren macOS/Windows uygulaması (MIT, 15 bin ★). İçindeki tek SKILL.md uygulamanın kurulum girişi | Sadece kişisel görünüm için; kurulumu kendin yap. Resmî değil, paketler imzasız, arayüze CDP ile CSS enjekte eder; README'de API aracı sponsor reklamı var | – (kütüphaneye skill olarak alınmadı) |
| KaTeX/KaTeX | Hızlı LaTeX matematik dizgisi (web) | Bilimsel/eğitim içerikte formül | `latex-posters`, `scientific-writing`, `manim-composer` |
| openai/whisper | Açık kaynak konuşma tanıma (STT) modeli, yerel | Ücretsiz transkripsiyon/altyazı | `media-use` (yerel transkripsiyon), `speech-to-text` (ElevenLabs, kısmen), `video-understand` |
| librosa/librosa | Python ses/müzik analizi (tempo, beat, spektrum) | Müziğe senkron video, ses analizi | `music-to-video`, `media-use` |
| meyda/meyda | Tarayıcı/Node ses özelliği çıkarımı (RMS, spektral) | Sese tepki veren görsel | `canvas-procedural-animation` |
| blender/blender | 3D modelleme/render (açık kaynak) | 3D varlık, web için GLB hazırlama | `blender-web-pipeline`, `3d-asset-generation`, `threejs-loaders` |
| 666ghj/MiroFish | Sürü zekâsı (çok ajanlı) tahmin/simülasyon motoru (AGPL-3.0) | Senaryo/tahmin deneyleri ("Yapay Zeka araçları" listesi) | – |
