# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **22/45**

### captions-overlay  ·  heygen-com/hyperframes @ 25126bc  ·  puan 94 (A)

- **Ne yapar:** Overlay doctrine for the embedded-captions workflow — the caption MODEL (drop / rail / embed) and the rule that captions are an OVERLAY composited on top of the film, never a reserved bottom band you shift content up to avoid. Load when adding captions/subtitles to a talking-head or launch video, when deciding whether a phrase should be dropped, ride the verbatim rail, or be promoted to a scarce e
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### changelog-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 92 (A)

- **Ne yapar:** Turn a weekly changelog .md into a finished branded changelog video (square 1080, ~45-60s, Annie VO, animated brand background, mock-UI visualizations, lowkey captions). Use when the user provides a changelog/digest markdown and wants the weekly video, or says "changelog video". Self-contained — fonts, background, lexicon, and scripts ship in this skill.
- **Teknoloji:** api-anahtari, ffmpeg, gsap, html, node, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 521 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### create-video  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-produksiyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### embedded-captions  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded behind the subject, VFX captions, “炸/特效/酷炫字幕,” or a named identity from the 35-style catalog. Route by visual identity, not by backend engine. The quiet `anchor` rail is the default; embed every word only when the user explicitly wants
- **Teknoloji:** canvas, css, ffmpeg, gsap, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 3421 KB (SKILL.md 33.8 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### faceless-explainer  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per scene (typography, abstract graphics, diagrams, data-viz). Use for topic explainers, concept breakdowns, how-tos, listicles. Not a video built from a website (/product-launch-video — promo or tour). Unclear → /hyperframes.
- **Teknoloji:** api-anahtari, canvas, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 284 KB (SKILL.md 30.5 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır. · **Kırık bağlantı:** 13
- **İnceleme:** otomatik

### ffmpeg  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### figma  ·  heygen-com/hyperframes @ 25126bc  ·  puan 85 (A)

- **Ne yapar:** Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not slides) (REST/CLI), connector-assisted motion when available, and shaders from a connector or native export. Use when the user pastes a figma.com link or asks to bring a Figma design, frame, logo, brand, or animation into a video/co
- **Teknoloji:** api-anahtari, css, gsap, html, motion, node, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 23 KB (SKILL.md 17.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### general-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 85 (A)

- **Ne yapar:** Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and sizzle reels, montages, static loops, static title cards, footage remixes, and freeform builds. Use motion-graphics instead for a short unnarrated motion-first unit, including an animated title. Route fresh creation through hyperf
- **Teknoloji:** api-anahtari, canvas, css, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 36 KB (SKILL.md 21.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### hyperframes  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title card, overlay, slideshow or interactive deck, Remotion port, or any HyperFrames HTML composition. Also use it to inspect, diagnose, validate, preview, publish, or batch-render an existing HyperFrames project. Inp
- **Teknoloji:** api-anahtari, canvas, css, gsap, html, node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 156 KB (SKILL.md 24.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-animation  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP 
- **Teknoloji:** canvas, css, gsap, html, lottie, node, react, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1240 KB (SKILL.md 20.2 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-animation@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri ve GSAP, Lottie, Three.js, Anime.js, CSS, WAAPI, TypeGPU çalışma zamanı adaptörleri. Tek duraklatılmış, seek-güvenli zaman çizelgesi ilkesine dayanır.
- **Ne zaman:** HyperFrames kompozisyonunda hareket, geçiş veya sahne koreografisi yazarken. · **Ne zaman değil:** HyperFrames dışı web animasyonu (gsap-* veya framer-motion skilleri daha uygun); Remotion projeleri.
- **Teknoloji:** hyperframes, gsap, html, css, lottie, three.js · **Paketler:** hyperframes (npx), gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 2521 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çok zengin kural/blueprint kütüphanesi (2.5 MB); SKILL.md kısa yönlendirici, ayrıntı isteğe bağlı yükleniyor.

### hyperframes-audio  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover (voiceover carve), effects on a track (EQ, compressor, limiter, gate, saturation, delay, reverb, chorus, phaser, bitcrush), automation envelopes drawn on a track's volume or any effect parameter, or one subm
- **Teknoloji:** ffmpeg, gsap, html, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 100 KB (SKILL.md 25.9 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-cli  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes, single or batch render, publish, cloud, cloudrun, feedback, lambda, doctor, browser, info, upgrade, skills, compositions, timeline, history, clean, docs, benchmark, telemetry, transcribe, auth, tts, and remove-background. Also use when diag
- **Teknoloji:** api-anahtari, canvas, docker, ffmpeg, html, node, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 128 KB (SKILL.md 25.4 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-cli@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HyperFrames CLI geliştirme döngüsü: init, add, lint, validate, inspect, preview, render, AWS Lambda render ve sorun giderme. Render öncesi lint/validate/inspect zorunluluğunu ve --json kullanımını tanımlar.
- **Ne zaman:** HyperFrames projesi kurarken, doğrularken, önizlerken ve render alırken. · **Ne zaman değil:** Kompozisyon HTML'inin içeriği/sözleşmesi için (hyperframes-core); HyperFrames kullanılmayan projelerde.
- **Teknoloji:** hyperframes, node, ffmpeg, docker, aws-lambda · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 54 KB (SKILL.md 9.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik ve ajan dostu. Not: 'init' global skill setini otomatik güncelliyor; kütüphane kuralı gereği bu davranış izlenmeli.

### hyperframes-core  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.
- **Teknoloji:** canvas, css, gsap, html, lottie, node, tailwind, three.js, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 98 KB (SKILL.md 12.6 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-core@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönettiği medya oynatma ve deterministik render kuralları. Kompozisyon HTML'i yazmadan önce okunur.
- **Ne zaman:** Renderlanabilir bir HyperFrames projesi kurarken veya mevcut kompozisyonu düzenlerken. · **Ne zaman değil:** Sadece hareket tarifi arıyorsan (hyperframes-animation); HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 78 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Net teknik sözleşme ve referans dizini; diğer alt skillerin temeli.

### hyperframes-creative  ·  heygen-com/hyperframes @ 25126bc  ·  puan 89 (A)

- **Ne yapar:** Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`.
- **Teknoloji:** api-anahtari, css, gsap, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1176 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-creative@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, sese duyarlı görseller ve marka kararları. 'Web sayfası gibi görünen' jenerik çıktıyı önleyen ev stili kurallarını içerir.
- **Ne zaman:** Çok sahneli veya markalı bir HyperFrames videosunun görsel dilini ve ritmini planlarken. · **Ne zaman değil:** Atomik hareket ve geçişler için (hyperframes-animation); tek satırlık düzenlemelerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1000 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çıktı kalitesini en çok etkileyen alt skill; house-style ve video-composition referansları güçlü.

### hyperframes-keyframes  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2D/3D keyframes; also for GSAP, CSS keyframes, Anime.js, WAAPI, FLIP, paths, masks, SVG morph/draw, text trails, 3D depth, or `hyperframes keyframes` diagnostics. Don't use for broad scene strategy, brand design, media sourcing, captions, or
- **Teknoloji:** canvas, css, gsap, node, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 23 KB (SKILL.md 15.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-media  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Tek ses motoru (scripts/audio.mjs) ile HyperFrames için TTS (HeyGen/ElevenLabs/Kokoro), arka plan müziği, ses efekti, Whisper transkripsiyonu, arka plan silme ve altyazı/karaoke üretimi. HeyGen anahtarı yoksa yerel/ücretsiz yollara düşer.
- **Ne zaman:** HyperFrames kompozisyonuna seslendirme, müzik, efekt veya kelime zamanlı altyazı eklerken. · **Ne zaman değil:** HyperFrames dışı projelerde; belirli bir sağlayıcının ayrıntılı API'si gerekiyorsa (elevenlabs, lyria vb.).
- **Teknoloji:** hyperframes, node, heygen, elevenlabs, whisper · **Paketler:** node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon, ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 1396 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Sağlayıcı zinciri ve yedek yollar iyi tasarlanmış; varsayılanı HeyGen'e bağlı.

### hyperframes-registry  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever a brief, a user, or a storyboard names a look, effect, treatment, or transition such as CRT scanlines, glitch, chromatic aberration, film grain, a shimmer sweep, a chart, a code or terminal window, a map, or a confetti burst — because roughly 400 hosted items
- **Teknoloji:** canvas, css, gsap, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 79 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes-registry@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HyperFrames kayıt defterindeki hazır blok ve bileşenleri 'hyperframes add' ile kurar ve ana kompozisyona bağlar; yeni blok/bileşen yazıp üst projeye katkı akışını da anlatır.
- **Ne zaman:** Hazır grafik/efekt bloklarını (data-chart, grain-overlay…) kompozisyona eklerken. · **Ne zaman değil:** Sıfırdan özel sahne yazarken; HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, node · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 49 KB (SKILL.md 4.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar ama net kapsam; registry ağ erişimi gerektirir.

### hyperframes-studio  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose ideas and "don't change anything" get an answer and a plan, not an edit); for a new film, the plan, storyboard and build order that the HyperFrames launch films follow; and how the timeline should be laid out so it reads well (one caption track, one element kin
- **Teknoloji:** canvas, css, html, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### hyperframes@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** HTML'den video render eden HyperFrames'in giriş ve yönlendirme skill'i: alt skillerin (core, animation, creative, media, cli, registry) haritasını ve 'video yap' isteğini doğru iş akışına yönlendiren tabloyu verir.
- **Ne zaman:** Herhangi bir video/animasyon/motion graphic isteğinde ilk okunacak skill; HyperFrames ile video yazılacaksa. · **Ne zaman değil:** Kullanıcı açıkça Remotion veya başka bir çerçeve istiyorsa; sadece hazır videoyu kesip biçen FFmpeg işlerinde.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** video-kompozisyon-cercevesi → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 20 KB (SKILL.md 16.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Ekosistemin yönlendiricisi, iyi yapılandırılmış. Dikkat: /general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions yönlendirmeleri arşivde yok (OpenMontage c806645'te bulunmuyor).

### media-use  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Agent Media OS for a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block + ledger record (one verb, `resolve`); generate via TTS / music / image models when the catalog misses; produce voiceover, transcription, captions, and background removal through one shared audio engine; operate on media (cut / reframe / tran
- **Teknoloji:** api-anahtari, css, node, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1806 KB (SKILL.md 9.6 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### media-use@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** BGM, ses efekti, görsel ve ikon ihtiyacını tek 'resolve' komutuyla HeyGen kataloğunda arayıp indirir, yerelde dondurur ve manifest'e kaydeder; ajana sadece dosya yolunu döndürür.
- **Ne zaman:** Kompozisyona hazır stok müzik, efekt, görsel veya ikon gerektiğinde, bağlamı arama gürültüsüyle doldurmadan. · **Ne zaman değil:** Özgün üretim gerekiyorsa (music, sound-effects, flux); HeyGen anahtarı yoksa katalog araması sınırlı.
- **Teknoloji:** node, heygen, api-anahtari · **Paketler:** node, HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** medya-varlik-temini → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 66 KB (SKILL.md 5.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Bağlam dostu tasarım (tek satır çıktı, önbellek). HeyGen kataloğuna bağımlı.

### music-to-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. The music drives all pacing; any user-supplied images/videos are cut onto the same beat grid, and a complete video needs zero assets. Narrated pieces → the input-matched workflow (see /hyperframes). Unclear → /hyperframes.
- **Teknoloji:** canvas, gsap, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6081 KB (SKILL.md 18.6 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### music-to-video@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Bir müzik parçasından vuruşa senkron HyperFrames videosu üretir: parçayı tek analizörle (beatgrid) çözümler, kareleri planlar, her kareyi ayrı alt ajana yaptırır ve render eder. Şarkı sözü videosu, slayt gösterisi veya kinetik tanıtım bu akıştan çıkar.
- **Ne zaman:** Elinde müzik (veya sesinden yararlanılacak video) olan, ritme oturan klip/lyric video isteklerinde. · **Ne zaman değil:** Anlatımlı veya web sitesinden üretilecek videolarda; müziği olmayan işlerde.
- **Teknoloji:** hyperframes, python, html, gsap · **Paketler:** hyperframes (npx), python3, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-produksiyon, motion-graphics-sanatcisi · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6053 KB (SKILL.md 15.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapılı (gate) iş akışı ve alt ajan dağıtımı olgun; çok ajanlı olduğu için maliyetli/uzun.

### oversized-cursor  ·  heygen-com/hyperframes @ 25126bc  ·  puan 94 (A)

- **Ne yapar:** House-style oversized macOS cursor technique for HyperFrames launch videos. Load whenever a scene involves cursors or a pointer-led action, when kicking off a UI scene, when igniting a morph/transition/typing run with a click, or when a scene reads as static, dead, or stale and needs a cheap high-yield source of motion to carry the viewer's eye and segment them out of the stale state. Covers curso
- **Teknoloji:** css, gsap _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### playwright-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### pr-to-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files: the input is a code change, not a website. Not a product promo (/product-launch-video) or a no-PR topic explainer (/faceless-explainer). Unclear → /hyperframes.
- **Teknoloji:** api-anahtari, canvas, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 358 KB (SKILL.md 33.3 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### product-launch-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants to market, launch, promote, or reveal a product; the default for any commercial URL. Site tours / showcases of a website route here too — the brief carries the show-it-as-is intent. Unclear → /hyperframes.
- **Teknoloji:** api-anahtari, canvas, ffmpeg, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 341 KB (SKILL.md 35.1 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### remotion  ·  calesthio/OpenMontage @ c806645  ·  puan 71 (B)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### remotion-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Roller:** video-produksiyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil.

### remotion-to-hyperframes  ·  heygen-com/hyperframes @ 25126bc  ·  puan 87 (A)

- **Ne yapar:** Port an existing Remotion (React) composition''s source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — one-way, Remotion-only. A passing Remotion mention, reference-only code, or "make something like my Remotion video" is a fresh build (/general-video). Unclear → /hyperframes.
- **Teknoloji:** css, gsap, html, lottie, node, python, react, remotion, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 176 KB (SKILL.md 10.8 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### remotion-to-hyperframes@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Mevcut bir Remotion (React) kompozisyonunu HyperFrames HTML'ine taşır; eşlenebilen kalıpları çevirir, useState/useEffect gibi uyumsuz kalıpları işaretler ve SSIM eşikli test korpusuyla çeviriyi doğrular.
- **Ne zaman:** Kullanıcı açıkça Remotion projesini HyperFrames'e taşımak istediğinde. · **Ne zaman değil:** Yeni kompozisyon yazarken veya Remotion sadece referans olarak geçiyorsa; ters yönde dönüşüm.
- **Teknoloji:** remotion, hyperframes, react, html, gsap · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** video-kompozisyon-cercevesi → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 168 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar kapsamlı ama disiplinli (eval zorunlu). /general-video yönlendirmesi arşivde yok.

### slideshow  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an existing page into a deck. Output is a navigable deck, not a rendered MP4. If the user didn't explicitly ask for a slideshow, confirm before authoring. Unclear → /hyperframes.
- **Teknoloji:** api-anahtari, canvas, css, gsap, html, next.js, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 76 KB (SKILL.md 33.1 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### synthetic-screen-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 78 (B)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### talking-head-recut  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript, on a 16:9 / 9:16 / 4:5 canvas of your choice; the clip plays untouched underneath. Trigger on "graphic overlays", "on-screen graphics", "package / dress up my video". Not plain subt
- **Teknoloji:** api-anahtari, canvas, css, ffmpeg, gsap, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 509 KB (SKILL.md 64.0 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### video-download  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-toolkit  ·  calesthio/OpenMontage @ c806645  ·  puan 70 (B)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-produksiyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### website-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 85 (A)

- **Ne yapar:** Bir web sitesini headless Chrome ile yakalayıp marka varlıklarıyla HyperFrames videosuna (site turu, vitrin, sosyal klip) dönüştüren 7 adımlı, kapılı iş akışı. Varlık denetimi ve 'doğrulamadıklarım' açıklaması zorunludur.
- **Ne zaman:** Portföy/blog/landing sayfasından tanıtım turu veya sosyal medya klibi üretilecekse. · **Ne zaman değil:** Ürün lansman/promosyon videosu, konu anlatımı veya PR videosu (yönlendirdiği skiller arşivde yok).
- **Teknoloji:** hyperframes, html, node, chrome-headless · **Paketler:** hyperframes (npx), node>=22
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 1541 KB (SKILL.md 11.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kalite kapıları güçlü. /product-launch-video ve /faceless-explainer yönlendirmeleri arşivde yok.
