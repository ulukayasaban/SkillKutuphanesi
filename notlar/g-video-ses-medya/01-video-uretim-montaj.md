# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/22**

### create-video  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Create videos from a text prompt using HeyGen's Video Agent. Use when: (1) Creating a video from a description or idea, (2) Generating explainer, demo, or marketing videos from a prompt, (3) Making a video without specifying exact avatars, voices, or scenes, (4) Quick video prototyping or drafts, (5) One-shot prompt-to-video generation, (6) User says "make me a video" or "create a video about X".
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### ffmpeg  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Video and audio processing with FFmpeg. Use for format conversion, resizing, compression, audio extraction, and preparing assets for Remotion. Triggers include converting GIF to MP4, resizing video, extracting audio, compressing files, or any media transformation task.
- **Teknoloji:** ffmpeg, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, title card, overlay, or any composition. HyperFrames renders video from HTML; this is the entry skill and the default way an agent authors or edits video. It routes the request to the right specialized workflow and points to the HyperFrames domain sk
- **Teknoloji:** api-anahtari, css, gsap, html, lottie, node, react, remotion, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 20 KB (SKILL.md 16.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-animation  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP 
- **Teknoloji:** canvas, css, gsap, html, lottie, node, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 2521 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-cli  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, render, publish, lambda, doctor, browser, info, upgrade, skills, compositions, docs, benchmark, telemetry, transcribe, tts, or remove-background, or when troubleshooting the HyperFrames build/render environment. Entry point for AWS Lambda cloud rendering
- **Teknoloji:** api-anahtari, canvas, css, docker, ffmpeg, html, node, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 54 KB (SKILL.md 9.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-core  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.
- **Teknoloji:** gsap, html, lottie, node, tailwind, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 78 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-creative  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`.
- **Teknoloji:** api-anahtari, css, gsap, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1000 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-media  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), background music + sound effects (HeyGen audio-library retrieval by default, with local Lyria / MusicGen BGM generation and a bundled SFX library as the no-credential fallback), Whisper transcription, background removal, and capti
- **Teknoloji:** api-anahtari, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 1396 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### hyperframes-registry  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, registry discovery, and authoring a new block or component to contribute upstr
- **Teknoloji:** canvas, css, gsap, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 49 KB (SKILL.md 4.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### media-use  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Agent Media OS — resolve any media need (BGM, SFX, image, icon) into a frozen local file + ledger record. One verb (`resolve`) handles the full cascade — project cache, global cache, HeyGen catalog search, freeze, register. Keeps search noise on disk, hands the agent a path. Use when a composition needs background music, sound effects, images, or icons.
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 66 KB (SKILL.md 5.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### music-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. The music drives everything: one analyzer reads it once, the orchestrator lays out the frames and fills a per-frame plan, and one sub-agent builds each frame. Typography and templates are the floor — a complete video needs zero assets — but any images 
- **Teknoloji:** canvas, gsap, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6053 KB (SKILL.md 15.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### playwright-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Record browser interactions as video using Playwright. Use for capturing demo videos, app walkthroughs, and UI flows for Remotion videos. Triggers include recording a demo, capturing browser video, screen recording a website, or creating walkthrough footage.
- **Teknoloji:** css, ffmpeg, node, playwright, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### remotion  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Toolkit-specific Remotion patterns — custom transitions, shared components, and project conventions. For core Remotion framework knowledge (hooks, animations, rendering, etc.), see the `remotion-official` skill.
- **Teknoloji:** css, ffmpeg, node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### remotion-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Best practices for Remotion - Video creation in React
- **Teknoloji:** ffmpeg, lottie, react, remotion, tailwind, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### remotion-to-hyperframes  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion source. Do NOT use: (a) authoring a new HyperFrames composition; (b) Remotion mentioned in passing; (c) Remotion code shared as reference only; (d) "same video as my Remotion one" without explicit migrate request — treat as fresh build. Doubt → `/ge
- **Teknoloji:** css, gsap, html, lottie, node, python, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 168 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### synthetic-screen-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Synthetic terminal-style screen recording guidance for Remotion `TerminalScene`.
- **Teknoloji:** api-anahtari, ffmpeg, git, playwright, python, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### video-download  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Download video and audio from YouTube and 1000+ sites using yt-dlp. No API keys needed. Use when: (1) Downloading a video from YouTube or other sites, (2) Extracting audio from a video URL, (3) Downloading subtitles/captions from a video, (4) Getting video metadata without downloading.
- **Teknoloji:** api-anahtari, ffmpeg, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### video-edit  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Edit videos locally using ffmpeg. Trim, concat, resize, speed, overlay, extract audio, compress, and convert. Use when: (1) Trimming or cutting video segments, (2) Concatenating multiple clips, (3) Resizing video for social platforms, (4) Extracting or replacing audio, (5) Compressing video, (6) Converting video formats, (7) Getting video info.
- **Teknoloji:** ffmpeg _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### video-toolkit  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Create professional videos autonomously using claude-code-video-toolkit — AI voiceovers, image generation, music, talking heads, and Remotion rendering.
- **Teknoloji:** api-anahtari, docker, ffmpeg, node, python, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### video-translate  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Translate and dub existing videos into multiple languages using HeyGen. Use when: (1) Translating a video into another language, (2) Dubbing video content with lip-sync, (3) Creating multi-language versions of existing videos, (4) Audio-only translation without lip-sync, (5) Working with HeyGen's /v2/video_translate endpoint.
- **Teknoloji:** api-anahtari, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### video-understand  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Understand video content locally using ffmpeg frame extraction and Whisper transcription. No API keys needed. Use when: (1) Understanding what a video contains, (2) Transcribing video audio locally, (3) Extracting key frames for visual analysis, (4) Getting video content without API keys.
- **Teknoloji:** api-anahtari, ffmpeg, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### website-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 88 (A)

- **Ne yapar:** Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots + brand assets. Use when intent is general — portfolio/blog/landing-page showcase or social clip from the site. NOT for: product/SaaS launch or promo (→ /product-launch-video, even from a URL); topic explainer with no site (→ /facele
- **Teknoloji:** canvas, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 1541 KB (SKILL.md 11.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 2
- **İnceleme:** otomatik
