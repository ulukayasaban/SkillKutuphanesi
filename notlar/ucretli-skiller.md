# Ücretli ve Kısmen Ücretli Skiller

> `araclar/katalog-uret.py` üretir. Kaynak: `ucret-siniflandirma.json` (elle, gerekçeli). Kural: ücretsiz yol önce; ücretli skill rollerin çekirdeğine ancak gerekçeyle (`ucretli_bilincli`) girer, ön kontrol `ucretli` UYARISI verir.

## 💲 Ücretli (ücretli API/abonelik olmadan çalışmaz) — 54

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
| `speech` | 02-ses-muzik-konusma | OpenAI TTS API: karakter başına ücret |
| `speech-to-text` | 02-ses-muzik-konusma | ElevenLabs Scribe API. Ücretsiz yol: media-use transcribe (Parakeet/Whisper), video-understand |
| `text-to-speech` | 02-ses-muzik-konusma | HeyGen Starfish TTS (HEYGEN_API_KEY). Ücretsiz yol: media-use (Kokoro) |
| `venice-audio-music` | 02-ses-muzik-konusma | Venice.ai API anahtarı ve ücretli kullanım |
| `venice-audio-speech` | 02-ses-muzik-konusma | Venice.ai API anahtarı ve ücretli kullanım |
| `ai-video-gen` | 03-ai-gorsel-video-modelleri | HeyGen / fal.ai / Kling / Gemini API ağ geçitleri |
| `atlas-cloud` | 03-ai-gorsel-video-modelleri | Atlas Cloud API (ATLASCLOUD_API_KEY) |
| `avatar-video` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `bfl-api` | 03-ai-gorsel-video-modelleri | Black Forest Labs FLUX API (BFL_API_KEY) |
| `faceswap` | 03-ai-gorsel-video-modelleri | HeyGen API |
| `fal-3d` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-generate` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-image-edit` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-kling-o3` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-lip-sync` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-realtime` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-restore` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-train` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-tryon` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-upscale` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-video-edit` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `fal-vision` | 03-ai-gorsel-video-modelleri | fal.ai API anahtarı (FAL_KEY) ve kullanım başına ücret |
| `gemini-omni` | 03-ai-gorsel-video-modelleri | Gemini API / fal.ai (video üretimi ücretli kotada) |
| `gif-sticker-maker` | 03-ai-gorsel-video-modelleri | MiniMax API ile görsel/video üretimi: ücretli |
| `grok-media` | 03-ai-gorsel-video-modelleri | xAI API |
| `heygen` | 03-ai-gorsel-video-modelleri | HeyGen API (kullanımdan kaldırıldı; create-video / avatar-video) |
| `imagegen` | 03-ai-gorsel-video-modelleri | OpenAI Image API (OPENAI_API_KEY): görsel başına ücret |
| `kling-official` | 03-ai-gorsel-video-modelleri | Kling / fal.ai API |
| `minimax-h3` | 03-ai-gorsel-video-modelleri | MiniMax / fal.ai API |
| `replicate` | 03-ai-gorsel-video-modelleri | Replicate API: model çalıştırma başına ücret |
| `seedance-2-0` | 03-ai-gorsel-video-modelleri | Seedance (Atlas Cloud / fal.ai / BytePlus) API |
| `seedance-2-5` | 03-ai-gorsel-video-modelleri | Seedance API sağlayıcıları |
| `sora` | 03-ai-gorsel-video-modelleri | OpenAI Sora video API: ücretli |
| `venice-image-edit` | 03-ai-gorsel-video-modelleri | Venice.ai API anahtarı ve ücretli kullanım |
| `venice-image-generate` | 03-ai-gorsel-video-modelleri | Venice.ai API anahtarı ve ücretli kullanım |
| `venice-video` | 03-ai-gorsel-video-modelleri | Venice.ai API anahtarı ve ücretli kullanım |

## ½ Kısmen (ücretsiz yolu var; ücretli kısım isteğe bağlı/koşullu) — 24

| Skill | Kategori | Neden |
|---|---|---|
| `frontend-dev` | 01-ui-ux-tasarim-dili | Arayüz kodu ücretsiz; AI medya üretimi MiniMax API (ücretli) |
| `design` | 02-tasarim-sistemi-marka | Logo/görsel üretimi Gemini/MuAPI anahtarı ister; tasarım rehberi ücretsiz |
| `rive-interactive` | 03-animasyon-motion | Rive ücretsiz plan; bazı özellikler ücretli |
| `spline-interactive` | 05-3d-webgl | Spline ücretsiz plan; bazı dışa aktarma/ekip özellikleri ücretli |
| `hatch-pet` | 06-oyun-2d-grafik | Yerel yol ücretsiz; ikincil yedek yol OPENAI_API_KEY ister (ücretli) |
| `init-bootstrap` | 04-not-alma-bilgi-yonetimi | Gemini API anahtarı isteğe bağlı (ücretsiz katman var) |
| `connect` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `connect-apps` | 01-claude-api-mcp | Composio hesabı (ücretsiz katman var) |
| `langsmith-fetch` | 01-claude-api-mcp | LangSmith hesabı (ücretsiz katman var) |
| `notebooklm` | 03-web-arastirma-veri | Google hesabı; NotebookLM kullanım kotaları/planları |
| `changelog-video` | 01-video-uretim-montaj | Yerel Whisper; HeyGen sesi isteğe bağlı |
| `figma` | 01-video-uretim-montaj | FIGMA_TOKEN (ücretsiz planla çalışır); değişkenler (variables) Enterprise ister |
| `hyperframes` | 01-video-uretim-montaj | HyperFrames ücretsiz/açık kaynak; HeyGen medya ve bulut render isteğe bağlı |
| `media-use` | 01-video-uretim-montaj | Ücretsiz yerel yol her medya türü için var (Kokoro, MusicGen, Openverse, yerel FLUX/LTX, Whisper); HeyGen isteğe bağlı ve ücretli çağrıdan önce onay ister |
| `remotion` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `remotion-best-practices` | 01-video-uretim-montaj | Remotion lisansı: şirketler için ticari lisans gerekebilir |
| `remotion@calesthio` | 01-video-uretim-montaj | Remotion lisansı: bireyler ve küçük ekipler ücretsiz, şirketler için ticari lisans gerekebilir |
| `3d-asset-generation` | 03-ai-gorsel-video-modelleri | Üretim Atlas Cloud / fal.ai ile ücretli; CC0 Kenney kataloğu ve Blender yolu ücretsiz |
| `comfyui` | 03-ai-gorsel-video-modelleri | Yerel ComfyUI ücretsiz; 'Partner Nodes' Comfy hesabı ve ön ödemeli kredi ister |
| `imagen` | 03-ai-gorsel-video-modelleri | Google Gemini görsel API: sınırlı ücretsiz kota, sonrası ücretli |
| `ltx2` | 03-ai-gorsel-video-modelleri | Açık model (topluluk lisansı: 10M$ altı gelirde ücretsiz); büyük GPU ya da bulut GPU gerekir |
| `nanobanana-ppt` | 03-ai-gorsel-video-modelleri | Gemini (Nano Banana) görsel üretimi: sınırlı ücretsiz kota, sonrası ücretli; deste yapısı yerel |
| `pixelbin-media` | 03-ai-gorsel-video-modelleri | Pixelbin hesabı: ücretsiz kredi var, sonrası ücretli |
| `provider-model-refresh` | 03-ai-gorsel-video-modelleri | Ücretli sağlayıcı adaptörleri; bazı modeller yerel (Qwen Image yerel) |

Gizli entegrasyon kataloğundaki 832 Composio skili toplu olarak 'kısmen' (Composio hesabı; ücretsiz katman var).
