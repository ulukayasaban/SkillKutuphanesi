# 03-ai-gorsel-video-modelleri — Video, Ses ve AI Medya Üretimi

_AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **0/18**

### 3d-asset-generation  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate, reconstruct, inspect, and route production 3D assets for OpenMontage worlds using Atlas Cloud, fal.ai, licensed catalogs, and Blender.
- **Teknoloji:** three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### ai-video-gen  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate AI videos from text prompts using multiple provider gateways. Use when: (1) Generating videos from text descriptions, (2) Creating AI-generated video clips for content production, (3) Image-to-video generation with a reference image, (4) Choosing between video generation providers (VEO, Kling, Sora, Runway, Seedance, MiniMax, Gemini Omni). Supports gateways: HeyGen API, fal.ai API, and th
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:farkli
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### atlas-cloud  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate or edit images and videos through the Atlas Cloud gateway. Use for Atlas-hosted Seedance 2.5/2.0, Gemini Omni Flash, MiniMax H3, Seedream 5.0, GPT Image 2, Nano Banana 2, or when one ATLASCLOUD_API_KEY should access multiple media model families.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### avatar-video  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Create AI avatar videos with precise control over avatars, voices, scripts, scenes, and backgrounds using HeyGen's v2 API. Use when: (1) Choosing a specific avatar and voice for a video, (2) Writing exact scripts for an avatar to speak, (3) Building multi-scene videos with different backgrounds per scene, (4) Creating transparent WebM videos for compositing, (5) Using talking photos as video prese
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 177 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### bfl-api  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** BFL FLUX API integration guide covering endpoints, async polling patterns, rate limiting, error handling, webhooks, and regional endpoints with Python and TypeScript code examples.
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 79 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### comfyui  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Use when working with ComfyUI workflows in OpenMontage, including comfyui_image/comfyui_video/comfyui_music, custom workflow_json/workflow_path inputs, output_node selection, missing model setup, LoRAs, low-VRAM workflow choices, and community workflow imports.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### faceswap  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Swap faces in a video using AI via the HeyGen API. Use when: (1) Replacing a face in a video with another face, (2) Face swapping from a source image onto a target video, (3) Creating personalized videos by swapping in a person's face, (4) Working with HeyGen's /v1/workflows/executions endpoint for face swap processing.
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### flux-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Comprehensive guide for BFL FLUX image generation models. Covers prompting, T2I, I2I, structured JSON, hex colors, typography, multi-reference editing, and model-specific best practices for FLUX.2 and FLUX.1 families.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 122 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### gemini-omni  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate and conversationally edit short videos with Google Gemini Omni Flash (`gemini-omni-flash-preview`). Use when: (1) iterating on a clip with natural-language edits instead of regenerating ("make the phone invisible, keep everything else the same"), (2) generating 3-10s 720p clips with synthesized audio, rendered on-screen text, or timecoded beats, (3) binding reference images to roles with 
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### grok-media  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** xAI Grok image and video generation guide covering authentication, endpoints, prompt structure, image editing, reference-image video, and async polling.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### heygen  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** [DEPRECATED] Use `create-video` for prompt-based video generation or `avatar-video` for precise avatar/scene control. This legacy skill combines both workflows — the newer focused skills provide clearer guidance.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 225 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### kling-official  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Official Kling direct API guidance for OpenMontage providers. Use before calling `kling_official_video`, `kling_official_image`, `kling_tts`, `kling_avatar`, or `kling_lip_sync`.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### ltx2  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** AI video generation with LTX-2.3 22B — text-to-video, image-to-video clips for video production. Use when generating video clips, animating images, creating b-roll, animated backgrounds, or motion content. Triggers include video generation, animate image, b-roll, motion, video clip, text-to-video, image-to-video.
- **Teknoloji:** api-anahtari, docker, ffmpeg, python, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 7 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### minimax-h3  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Generate MiniMax H3 (Hailuo 3.0) video through the official MiniMax v2 API, fal.ai, Runway, ComfyUI Partner Nodes, or local open weights in ComfyUI. Use for 4-15 second 2K clips, first/last-frame animation, and image/video/audio reference-conditioned video.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### provider-model-refresh  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Use the September 2026 image, video, speech and Avatar V adapters with explicit model/host contracts.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### seedance-2-0  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate cinematic clips with ByteDance Seedance 2.0 — the preferred premium video model in OpenMontage when a paid gateway is configured. Use when: (1) producing trailers, teasers, hype edits, or premium cinematic clips, (2) needing native synchronized audio (speech, SFX, ambience) in a single pass, (3) needing multi-shot cuts inside one generation, (4) needing director-level camera control, (5) 
- **Teknoloji:** api-anahtari, python, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 17.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### seedance-2-5  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** Generate 4-30 second cinematic video with ByteDance Seedance 2.5 through fal.ai, Volcengine Ark, Runway, or ComfyUI Partner Nodes. Use for long single generations, synchronized audio, and large multimodal reference sets (up to 30 images, 10 videos, and 10 audio clips). Also covers the 2.5 prompt contract: section order, multi-shot "Hard cut" breakdown, named locks for continuity across cuts, the a
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 23 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### setup-api-key  ·  calesthio/OpenMontage @ c806645  ·  puan 92 (A)

- **Ne yapar:** Guides users through setting up an ElevenLabs API key for ElevenLabs MCP tools. Use when the user needs to configure an ElevenLabs API key, when ElevenLabs tools fail due to missing API key, or when the user mentions needing access to ElevenLabs. First checks whether ELEVENLABS_API_KEY is already configured and valid, and only runs full setup when needed.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik
