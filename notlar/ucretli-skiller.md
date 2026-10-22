# Ücretli ve Kısmen Ücretli Skiller

> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.

## 💲 Ücretli (ücretli API/abonelik olmadan çalışmaz) — 32

| Skill | Kategori | Neden |
|---|---|---|
| `substance-3d-texturing` | 05-3d-webgl | Adobe Substance 3D Painter lisansı/aboneliği |
| `claude-api` | 01-claude-api-mcp | Anthropic API kullanımı ücretli (token bazlı) |
| `claude-opus-4-5-migration` | 01-claude-api-mcp | Claude API ile çalışan kodun geçişi; API kullanımı ücretli |
| `create-video` | 01-video-uretim-montaj | HeyGen Video Agent API |
| `video-toolkit` | 01-video-uretim-montaj | Açık modelleri bulut GPU'da (Modal/RunPod) çalıştırır; GPU kullanımı ücretli |
| `video-translate` | 01-video-uretim-montaj | HeyGen API |
| `acestep` | 02-ses-muzik-konusma | RunPod uç noktası (RUNPOD_API_KEY) |
| `agents` | 02-ses-muzik-konusma | ElevenLabs sesli agent platformu (API anahtarı) |
| `azure-speech-to-text` | 02-ses-muzik-konusma | Azure Speech kaynağı (ücretsiz F0 katmanı sınırlı, kart gerektirir) |
| `azure-text-to-speech` | 02-ses-muzik-konusma | Azure Speech kaynağı (ücretsiz F0 katmanı sınırlı, kart gerektirir) |
| `dashscope` | 02-ses-muzik-konusma | Alibaba Cloud DashScope API |
| `doubao-tts` | 02-ses-muzik-konusma | Volcengine Doubao API |
| `elevenlabs` | 02-ses-muzik-konusma | ElevenLabs API anahtarı (ELEVENLABS_API_KEY); ücretsiz deneme kotası sınırlı. Ücretsiz yol: media-use (Kokoro TTS, MusicGen, Openverse SFX) |
| `fish-audio-tts` | 02-ses-muzik-konusma | fish.audio API |
| `lyria` | 02-ses-muzik-konusma | Google Lyria (Gemini/Vertex API) |
| `music` | 02-ses-muzik-konusma | ElevenLabs Music API. Ücretsiz yol: media-use (yerel MusicGen) |
| `setup-api-key` | 02-ses-muzik-konusma | ElevenLabs API anahtarı kurulum rehberi |
| `sound-effects` | 02-ses-muzik-konusma | ElevenLabs SFX API. Ücretsiz yol: media-use (Openverse + 21 yerleşik çevrimdışı efekt) |
| `speech-to-text` | 02-ses-muzik-konusma | ElevenLabs Scribe API. Ücretsiz yol: media-use transcribe (Parakeet/Whisper), video-understand |
| `text-to-speech` | 02-ses-muzik-konusma | HeyGen Starfish TTS (HEYGEN_API_KEY). Ücretsiz yol: media-use (Kokoro) |
| `ai-video-gen` | 03-ai-gorsel-video-modelleri | HeyGen / fal.ai / Kling / Gemini API ağ geçitleri |
| `atlas-cloud` | 03-ai-gorsel-video-modelleri | Atlas Cloud API (ATLASCLOUD_API_KEY) |
| `avatar-video` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `bfl-api` | 03-ai-gorsel-video-modelleri | Black Forest Labs FLUX API (BFL_API_KEY) |
| `faceswap` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `gemini-omni` | 03-ai-gorsel-video-modelleri | Gemini API / fal.ai (video üretimi ücretli kotada) |
| `grok-media` | 03-ai-gorsel-video-modelleri | xAI API |
| `heygen` | 03-ai-gorsel-video-modelleri | HeyGen API (kullanımdan kaldırıldı; create-video / avatar-video) |
| `kling-official` | 03-ai-gorsel-video-modelleri | Kling / fal.ai API |
| `minimax-h3` | 03-ai-gorsel-video-modelleri | MiniMax / fal.ai API |
| `seedance-2-0` | 03-ai-gorsel-video-modelleri | Seedance (Atlas Cloud / fal.ai / BytePlus) API |
| `seedance-2-5` | 03-ai-gorsel-video-modelleri | Seedance API sağlayıcıları |

## ½ Kısmen (ücretsiz yolu var; ücretli kısım isteğe bağlı/koşullu) — 31

| Skill | Kategori | Neden |
|---|---|---|
| `design` | 02-tasarim-sistemi-marka | Logo/görsel üretimi Gemini/MuAPI anahtarı ister; tasarım rehberi ücretsiz |
| `rive-interactive` | 03-animasyon-motion | Rive ücretsiz plan; bazı özellikler ücretli |
| `spline-interactive` | 05-3d-webgl | Spline ücretsiz plan; bazı dışa aktarma/ekip özellikleri ücretli |
| `init-bootstrap` | 04-not-alma-bilgi-yonetimi | Gemini API anahtarı isteğe bağlı (ücretsiz katman var) |
| `connect` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `connect-apps` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `langsmith-fetch` | 01-claude-api-mcp | LangSmith hesabı (ücretsiz katman var) |
| `notebooklm` | 03-web-arastirma-veri | Google hesabı; NotebookLM kullanım kotaları/planları |
| `changelog-video` | 01-video-uretim-montaj | Yerel Whisper; HeyGen sesi isteğe bağlı |
| `faceless-explainer` | 01-video-uretim-montaj | HeyGen isteğe bağlı |
| `figma` | 01-video-uretim-montaj | FIGMA_TOKEN (ücretsiz planla çalışır); değişkenler (variables) Enterprise ister |
| `hyperframes` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `hyperframes-media` | 01-video-uretim-montaj | Ücretsiz yerel yol var; ElevenLabs/HeyGen/Lyria isteğe bağlı |
| `hyperframes-registry@calesthio` | 01-video-uretim-montaj | Eski OpenMontage kopyası; HeyGen isteğe bağlı |
| `hyperframes@calesthio` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `media-use` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HeyGen isteğe bağlı ve ücretli çağrıdan önce onay ister |
| `media-use@calesthio` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HeyGen isteğe bağlı ve ücretli çağrıdan önce onay ister |
| `music-to-video` | 01-video-uretim-montaj | Ücretsiz yol var; ElevenLabs/HeyGen/Lyria isteğe bağlı |
| `music-to-video@heygen-com-eski` | 01-video-uretim-montaj | Ücretsiz yol var; ElevenLabs/HeyGen/Lyria isteğe bağlı |
| `pr-to-video` | 01-video-uretim-montaj | HeyGen isteğe bağlı |
| `product-launch-video` | 01-video-uretim-montaj | HeyGen/Gemini isteğe bağlı |
| `remotion` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `remotion-best-practices` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion-to-hyperframes@calesthio` | 01-video-uretim-montaj | Eski OpenMontage kopyası; HeyGen isteğe bağlı |
| `website-to-video` | 01-video-uretim-montaj | Ücretsiz yol var; ElevenLabs/HeyGen isteğe bağlı |
| `3d-asset-generation` | 03-ai-gorsel-video-modelleri | Üretim Atlas Cloud / fal.ai ile ücretli; CC0 Kenney kataloğu ve Blender yolu ücretsiz |
| `comfyui` | 03-ai-gorsel-video-modelleri | Yerel ComfyUI ücretsiz; 'Partner Nodes' Comfy hesabı ve ön ödemeli kredi ister |
| `ltx2` | 03-ai-gorsel-video-modelleri | Açık model (topluluk lisansı: 10M$ altı gelirde ücretsiz); büyük GPU ya da bulut GPU gerekir |
| `provider-model-refresh` | 03-ai-gorsel-video-modelleri | Ücretli sağlayıcı adaptörleri; bazı modeller yerel (Qwen Image yerel) |
| `motion-graphics` | 04-motion-graphics-karakter | GEMINI/GOOGLE anahtarları isteğe bağlı; yoksa yerel/varlıksız yol |
| `motion-graphics@heygen-com-eski` | 04-motion-graphics-karakter | GEMINI/GOOGLE anahtarları isteğe bağlı; yoksa yerel/varlıksız yol |

Gizli entegrasyon kataloğundaki 832 Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var).
