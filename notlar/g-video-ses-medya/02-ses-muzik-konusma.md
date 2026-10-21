# 02-ses-muzik-konusma — Video, Ses ve AI Medya Üretimi

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/13**

### acestep  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** AI music generation with ACE-Step 1.5 — background music, vocal tracks, covers, stem extraction for video production. Use when generating music, soundtracks, jingles, or working with audio stems. Triggers include background music, soundtrack, jingle, music generation, stem extraction, cover, style transfer, or musical composition tasks.
- **Teknoloji:** api-anahtari, ffmpeg, python, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### agents  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots, interactive voice characters, or any real-time voice conversation experience.
- **Teknoloji:** api-anahtari, html, node, python, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 64 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### azure-speech-to-text  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Transcribe audio to text using Azure AI Speech (Fast Transcription REST API). Use when converting audio/video to text, generating subtitles, or processing spoken content in OpenMontage. Optional cloud STT provider — preferred when AZURE_SPEECH_KEY is configured; the local faster-whisper `transcriber` is the default offline path.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### azure-text-to-speech  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate neural narration audio using Azure AI Speech (REST text-to-speech). Use when synthesizing voiceovers or narration in OpenMontage. Optional cloud TTS provider — preferred when AZURE_SPEECH_KEY is configured; the local piper_tts remains the default offline path. Shares one Speech resource with azure_stt.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### dashscope  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** DashScope (Alibaba Cloud Bailian / 阿里云百炼) integration — image generation (qwen-image-2.0-pro), text-to-speech (qwen3-tts-flash), and ASR with word-level timestamps (qwen3-asr-flash-filetrans). Use when generating images via Qwen-Image, narrating via Qwen-TTS, or transcribing with word-level timestamps via Qwen-ASR.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### doubao-tts  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate Mandarin and multilingual narration with Volcengine Doubao Speech 2.0. Use when creating Chinese voiceovers, when the user prefers Doubao/Volcengine/火山引擎/豆包 TTS, or when narration needs character-level timestamp metadata for subtitles.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### elevenlabs  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate AI voiceovers, sound effects, and music using ElevenLabs APIs. Use when creating audio content for videos, podcasts, or games. Triggers include generating voiceovers, narration, dialogue, sound effects from descriptions, background music, soundtrack generation, voice cloning, or any audio synthesis task.
- **Teknoloji:** api-anahtari, ffmpeg, python, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli
- **Boyut:** 16 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### fish-audio-tts  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate expressive, multilingual narration with fish.audio (S1 / S2-generation models) and reuse cloned voices via reference_id. Use when the user prefers fish.audio/Fish Audio TTS, wants a specific playground voice model, or needs high-emotion voice-clone narration.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### lyria  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate and validate music with Google Lyria 3 through the Gemini Interactions API. Use before calling OpenMontage `google_music`, designing Lyria 3 Clip or Pro prompts, using image-to-music or custom lyrics, choosing between Lyria 3 and Lyria RealTime, diagnosing Google music-generation failures, or preparing exact-duration music for a video.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### music  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-generated music composition. Supports prompt-based generation, composition plans for granular control, and detailed output with metadata.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### sound-effects  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambient sounds, cinematic impacts, UI sounds, or any audio that isn't speech. Supports looping, duration control, and prompt influence tuning.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### speech-to-text  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content.
- **Teknoloji:** api-anahtari, python, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 40 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### text-to-speech  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate speech audio from text using HeyGen's Starfish TTS model. Use when: (1) Generating standalone speech audio files from text, (2) Converting text to speech with voice selection, speed, and pitch control, (3) Creating audio for voiceovers, narration, or podcasts, (4) Working with HeyGen's /v1/audio endpoints, (5) Listing available TTS voices by language or gender.
- **Teknoloji:** api-anahtari, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik
