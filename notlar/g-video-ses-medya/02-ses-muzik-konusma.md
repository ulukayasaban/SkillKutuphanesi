# 02-ses-muzik-konusma — Video, Ses ve AI Medya Üretimi

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **17/26**

### acestep  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 83 (A)

- **Ne yapar:** ACE-Step 1.5 ile yapay zeka müziği: arka plan müziği, sözlü parça, cover, enstrüman ayrıştırma (stem), ses onarma ve devam ettirme; tools/music_gen.py üstünden. Varsayılan acemusic bulut API'si (ücretsiz anahtar, GPU gerekmez); isteğe bağlı Modal ya da RunPod'da kendi barındırma. Sahne ön ayarları (corporate-bg, tension...), BPM ve tonalite denetimi, varyasyon üretip seçme.
- **Ne zaman:** Video için telifsiz-benzeri üretilmiş arka plan müziği, jingle ya da şarkı; ücretsiz yol arandığında (acemusic anahtarı). · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla). Gerçek sanatçı ya da şarkı taklidi için; hazır stok müzik yeterliyse media-use; sorunsuz ticari lisans belgesi gerektiğinde acemusic ve model şartlarını ayrıca kontrol et.
- **Teknoloji:** python, api-anahtari, modal, runpod · **Paketler:** claude-code-video-toolkit (tools/music_gen.py), ACEMUSIC_API_KEY (ücretsiz)
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2697, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 14 KB (SKILL.md 13.8 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Ücretsiz müzik yolu (acemusic anahtarı) ve ayrıntılı kullanım kılavuzu iyi; ancak toolkit'teki music_gen.py'ye bağlı. muzik-uretimi grubunda music (ElevenLabs, ücretli) birincil; bu ücretsiz seçenek. Eski OpenMontage kopyası acestep@openmontageinc yalnız RunPod yolunu kullanıyordu (ücretli), bu sürüm onun yerine geçer. Lisans MIT (toolkit); ACE-Step modeli ve acemusic bulut hizmetinin ticari kullanım şartlarını ayrıca doğrula. Güvenlik: echo >> .env ile anahtar yazma, modal deploy, istemler acemusic.ai'ya gider (üçüncü taraf bulut). Betik indirmesi yok. Ücret: kismen.

### acestep@openmontageinc  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 77 (B)

- **Ne yapar:** ACE-Step 1.5 açık kaynak modeliyle RunPod üzerinde enstrümantal müzik, sözlü şarkı, cover/stil aktarımı ve stem ayırma yapar; sahne ön ayarları (corporate-bg, tension, cta) içerir.
- **Ne zaman:** Açık kaynak/ucuz müzik üretimi veya stem ayırma gerektiğinde ve tools/music_gen.py bulunan toolkit kuruluysa. · **Ne zaman değil:** OpenMontage kurulumunda (tools/music_gen.py yok); hızlı sonuç için music veya lyria.
- **Teknoloji:** python, runpod, ffmpeg · **Paketler:** RUNPOD_API_KEY, claude-code-video-toolkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** muzik-uretimi → alternatif
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu tools/music_gen.py OpenMontage c806645'te yok (claude-code-video-toolkit'ten taşınmış); --brand digital-samba gibi örnekler yabancı projeye ait.

### agents  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** ElevenLabs Agents Platform ile gerçek zamanlı sesli yapay zekâ ajanı (asistan, müşteri hizmetleri botu, etkileşimli karakter) kurar; CLI, Python, JS ve web gömme örnekleri içerir.
- **Ne zaman:** Uygulamaya konuşan, dinleyen sesli asistan veya telefon/web sesli bot eklenecekse. · **Ne zaman değil:** Tek seferlik seslendirme/medya üretimi (elevenlabs, text-to-speech).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js, @elevenlabs/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** sesli-ajan → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 64 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmi ElevenLabs skill'i, güncel. Medya üretimi değil uygulama entegrasyonu; video rollerine eklenmedi.

### azure-speech-to-text  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Azure AI Speech Fast Transcription REST API ile ses/videoyu kelime zaman damgalı, konuşmacı ayrımlı yazıya döker; OpenMontage'da azure_stt aracı olarak transcriber şemasıyla birebir uyumludur.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve bulutta hızlı transkript/altyazı gerekiyorsa. · **Ne zaman değil:** Azure hesabı yoksa (speech-to-text veya yerel whisper); OpenMontage dışında araç sarmalayıcısı yok.
- **Teknoloji:** azure, python, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Düzgün belgelenmiş; OpenMontage registry'sine bağlı kod örnekleri.

### azure-text-to-speech  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Azure nöral TTS ile SSML prozodi ve konuşma stili kontrollü çok dilli seslendirme üretir; OpenMontage'da azure_tts aracı olarak tts_selector üzerinden çalışır.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve SSML ile ince ayarlı, uygun maliyetli anlatım gerekiyorsa (Türkçe nöral sesler dahil). · **Ne zaman değil:** Ses klonlama gerekiyorsa (elevenlabs); Azure hesabı yoksa.
- **Teknoloji:** azure, python, ssml, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güvenilir kurumsal TTS; STT ile aynı kaynak.

### dashscope  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** Alibaba DashScope (Bailian) entegrasyonu: Qwen-Image ile görsel üretimi, Qwen-TTS ile seslendirme ve kelime zaman damgalı Qwen-ASR transkripsiyonu; yerel (OpenAI uyumlu olmayan) uç noktaları doğru kullanmayı anlatır.
- **Ne zaman:** Çince içerik veya DASHSCOPE_API_KEY olan, Çin bölgesi modelleri tercih edilen projelerde. · **Ne zaman değil:** Türkçe/İngilizce odaklı genel işlerde (elevenlabs, flux); DashScope anahtarı yoksa.
- **Teknoloji:** dashscope, python, api-anahtari · **Paketler:** DASHSCOPE_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci, ai-medya-uretici
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ve pratik; çoklu yetenek (görsel+TTS+ASR) olduğu için kategori sınırında. Çin pazarına odaklı.

### doubao-tts  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** Volcengine Doubao Speech 2.0 ile Mandarin ve çok dilli seslendirme üretir; asenkron uç noktadan karakter düzeyinde zaman damgası alıp altyazı kurmayı ve önce kısa örnekle onay almayı öğretir.
- **Ne zaman:** Çince seslendirme veya Doubao/Volcengine tercih edildiğinde. · **Ne zaman değil:** Türkçe/İngilizce anlatımda; Doubao anahtarı yoksa.
- **Teknoloji:** volcengine, python, api-anahtari · **Paketler:** DOUBAO_SPEECH_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İş akışı (örnek → onay → tam üretim) örnek alınacak kadar iyi; kullanım alanı dar.

### earshot  ·  Leonxlnx/earshot @ 7a7f7c5  ·  puan 81 (A)

- **Ne yapar:** Agent'a 'kulak' kazandırır: ses dosyasını tarif eder, metinle eşleştirir ve puanlar (CLAP + AST, CPU'da). Film/video için ses zaman çizelgesi ve eleştiri çıkarır, kodla ses efekti üretir; MCP sunucusu da sunar.
- **Ne zaman:** Video/ses üretiminde hazır ses efektlerini ya da müziği dinleyip doğru olanı seçmek, miksi kontrol etmek. · **Ne zaman değil:** Kurulum ağır: Python paketi + torch/transformers, ilk çalışmada Hugging Face'ten model indirir. Önerdiği `claude mcp add --scope user` komutu GENEL Claude ayarına yazar; isteğe bağlı, onaysız yapılmamalı. `llm` komutu sesi Gemini'ye yükler (sadece --yes-upload + kendi anahtarınla).
- **Teknoloji:** python, torch · **Paketler:** earshot (pip install -e), torch, transformers
- **Claude / Codex:** tam / tam
- **Geliştirici:** Leonxlnx (kisi, ★5473, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ses-analiz → birincil
- **Boyut:** 47 KB (SKILL.md 46.6 KB, yük buyuk)
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (ses-analiz grubunda birincil). MIT, 3,9k★. Ücretsiz, yerel; rol çekirdeğine girmez (kurulum yükü).

### elevenlabs  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 83 (A)

- **Ne yapar:** ElevenLabs API'leriyle seslendirme, ses efekti ve müzik üretimi: model seçimi (multilingual_v2, v4, flash_v2_5), ses ayarları, SSML/duraklama ve telaffuz denetimi, ses klonlama, konuşmadan metne (scribe_v2), paylaşılan ses arama ve yinelemeli üretim akışı. Python SDK örnekleriyle doğrudan çalışır.
- **Ne zaman:** Video, podcast ya da oyun için yapay zeka sesi, ses efekti, ses klonlama ve transkripsiyon; ELEVENLABS_API_KEY varsa. · **Ne zaman değil:** Tamamen ücretsiz yol için media-use (Kokoro) ya da Qwen3-TTS; sesli ajan için agents; kişinin izni olmadan ses klonlama. Toolkit araçlarına atıflar (voiceover.py, sfx.py) toolkit yoksa geçerli değil; SDK örnekleri toolkit'siz çalışır.
- **Teknoloji:** elevenlabs, python, api-anahtari, ffmpeg · **Paketler:** elevenlabs, ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2697, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → birincil · **Roller:** ses-tasarimci
- **Boyut:** 24 KB (SKILL.md 17.3 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT. SDK tabanlı, toolkit olmadan da kullanılabilen tek toolkit skili; güncel model tablosu (v4, flash, kullanımdan kalkanlar), SSML sınırları ve kopyalanabilir örnekler iyi. Ücret: kismen (ücretsiz plan aylık sınırlı kota; fazlası ücretli). Lisans MIT; ses klonlamada kişi izni, üretilen sesin ticari kullanımı ElevenLabs plan şartlarına bağlı. Güvenlik: API anahtarı .env'de, istem ve ses verisi ElevenLabs'e gider; betik indirmesi yok. Örtüşme: tts-saglayici grubunda eski kopya elevenlabs@openmontageinc de birincil görünüyor ama durumu alternatif; çift birincil çözülmeli (kaynak ajanı/kullanıcı kararı), bu kayıt bare ad'ı devralan tercih sürümdür.

### elevenlabs@openmontageinc  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile seslendirme, ses klonlama, ses efekti ve müzik üretimini tek skillde toplar; model seçimi, stile göre ses ayarları, duraklama/telaffuz kontrolü ve yinelemeli üretim akışını verir.
- **Ne zaman:** Video seslendirmesi, anlatım veya ses klonlama gereken her işte varsayılan TTS olarak. · **Ne zaman değil:** Sadece müzik (music) veya sadece efekt (sound-effects) için ayrıntılı API gerekiyorsa; sesli ajan (agents).
- **Teknoloji:** elevenlabs, python, ffmpeg, api-anahtari · **Paketler:** elevenlabs, ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** tts-saglayici → birincil · **Roller:** ses-tasarimci
- **Boyut:** 16 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Pratik üretim bilgisi (ayar tabloları, SSML sınırları, ellipsis uyarısı) çok değerli; Türkçe destekli multilingual_v2. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### fish-audio-tts  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** fish.audio S1/S2 modelleriyle duygu etiketli ([laugh], [whispers]) çok dilli seslendirme ve reference_id ile klonlanmış sesleri yeniden kullanma; bayt bazlı fiyatlandırmayı açıklar.
- **Ne zaman:** Yüksek duygu ifadeli anlatım veya fish.audio'da hazırlanmış klon ses gerektiğinde. · **Ne zaman değil:** Ücretsiz promosyon modeli (s2.1-pro-free) ile ticari/müşteri işi; fish.audio anahtarı yoksa.
- **Teknoloji:** fish-audio, python, api-anahtari · **Paketler:** FISH_AUDIO_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güncel ve dürüst (promosyon kısıtları açıkça yazılmış).

### krillinai-cli  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when an agent needs to build or operate the embedded KrillinAI CLI, choose a supported command, or interpret its JSON, manifest, subtitle, dubbing, render, cover, speech, and voice outputs.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.4 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-cover  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when generating a cover image with the KrillinAI CLI from a complete image prompt, including validating image-provider configuration and inspecting the generated image and saved prompt.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-pipeline  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when validating or documenting a multi-stage KrillinAI CLI output plan; the current pipeline command supports dry-run planning only, not end-to-end execution.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-render-horizontal  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when rendering landscape videos with KrillinAI CLI, including original video plus bilingual subtitles or dubbed video plus target-language subtitles.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-render-vertical  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when rendering portrait videos with KrillinAI CLI, including converting source video to vertical format, adding short bilingual subtitles, rendering dubbed vertical videos, and checking vertical subtitle readability.
- **Teknoloji:** ffmpeg, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-subtitle  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when generating subtitles with KrillinAI CLI from a YouTube link, Bilibili/local video, or existing media, including platform caption download, Whisper fallback, translation, bilingual SRT, and short vertical subtitle output.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-tts  ·  krillinai/OpenCreator @ f6160b6  ·  puan 90 (A)

- **Ne yapar:** Use when generating target-language dubbing with KrillinAI CLI from SRT subtitles, including TTS audio creation and optional dubbed video generation.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14457, son güncelleme 2026-11-20, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### lyria  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** Google Lyria 3 ile Gemini Interactions API üzerinden müzik üretir ve doğrular; Clip/Pro/RealTime model seçimi, yapılandırılmış prompt sözleşmesi, maliyet duyurusu ve videoya tam süreli master çıkarma adımlarını tanımlar.
- **Ne zaman:** Google anahtarı varken altyapı müziği, döngü veya sözlü şarkı gerektiğinde; ucuz ve hızlı deneme için. · **Ne zaman değil:** ElevenLabs Music tercih edildiğinde; OpenMontage google_music adaptörü sadece Pro modelini destekliyor.
- **Teknoloji:** google-gemini, api-anahtari · **Paketler:** GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 18 KB (SKILL.md 8.6 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Disiplinli iş akışı ve adaptör kısıtlarını açıkça söylüyor; kalite yüksek. · 2026-11-12 yeniden incelendi (fecb9a1): skill artık Lyria 3.5 (varsayılan `lyria-3.5`, ~$0.08/istek) ve Clip'i anlatıyor; `lyria-3-pro-preview` açıkça istenen eski seçenek; OpenMontage adaptörü artık iki modeli kabul ediyor, süre 5-184 sn doğrulanıyor (gerçek süre yine prob edilmeli), 3.5 maliyet tahmini güncel fiyat teklifi ister; GOOGLE_GENAI_USE_VERTEXAI=true ile Vertex yolu. Bağımlılık aynı (GEMINI_API_KEY, ücretli). Lisans notu: model/adaptör rehberi andromia3 katkısı, depo AGPL-3.0.

### music  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Music API ile metin isteminden enstrümantal parça, sözlü şarkı, jingle üretir; bölüm bazlı ince kontrol için kompozisyon planı oluşturup düzenlemeyi gösterir.
- **Ne zaman:** Video için arka plan müziği, jingle veya şarkı üretilecekse. · **Ne zaman değil:** Hazır stok müzik yeterliyse (media-use); sanatçı/şarkı taklidi istenirse (API reddeder).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → birincil · **Roller:** ses-tasarimci
- **Boyut:** 10 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi ElevenLabs skill'i; bağımsız SDK ile her yerde çalışır.

### real-sound  ·  Leonxlnx/earshot @ 7a7f7c5  ·  puan 84 (A)

- **Ne yapar:** Ses efekti ve müzik için gerçek, lisanslı kayıtları (Freesound, Mixkit, Pixabay; CC0/CC-BY) bulur, seçer, miksler ve masterlar; lisans bilgisini kaydeder.
- **Ne zaman:** Sentetik değil gerçek kayıt ses efekti istenen video/oyun projeleri. · **Ne zaman değil:** Sesi kodla üretmek için sound-effects (OpenMontage) ya da hyperframes-audio. CC-BY seslerde atıf zorunlu. Sitelerden dosya indirir.
- **Teknoloji:** python, ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** Leonxlnx (kisi, ★5473, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ses-efekti → alternatif
- **Boyut:** 321 KB (SKILL.md 15.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (ses-efekti grubu; sound-effects birincil). MIT. Ücretsiz kaynaklar.

### setup-api-key  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** ElevenLabs API anahtarını kurar: önce mevcut ELEVENLABS_API_KEY'i bulup doğrular, yoksa kullanıcıyı adım adım anahtar oluşturmaya yönlendirir ve .env'e yazar.
- **Ne zaman:** ElevenLabs skilleri anahtar eksikliğinden çalışmadığında veya anahtar değiştirilecekken. · **Ne zaman değil:** Diğer sağlayıcıların anahtarları (genel bir anahtar kurulum aracı değil); anahtar zaten tanımlıyken.
- **Teknoloji:** elevenlabs, api-anahtari · **Paketler:** ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** api-anahtari-kurulumu → birincil · **Roller:** ses-tasarimci
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Sadece ElevenLabs'a özel olduğu için 03'ten 02'ye taşındı. Anahtarı sohbete yapıştırtması güvenlik açısından dikkat ister.

### sound-effects  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile metin tarifinden ses efekti, ambiyans, döngü ve UI sesi üretir; süre, prompt etkisi ve döngü parametrelerini açıklar.
- **Ne zaman:** Video, oyun veya arayüz için özgün efekt/ambiyans gerektiğinde. · **Ne zaman değil:** Hazır efekt kütüphanesi yeterliyse (media-use, hyperframes-media); konuşma veya müzik için.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ses-efekti → birincil · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi, kısa ve eksiksiz.
- **Not:** Aynı ad farklı iş: bu kayıt (OpenMontage) çıplak adın tercihi olarak sabit; Barty-Bart/motion-graphics sürümü sound-effects@barty-bart (HyperFrames/Remotion/GSAP videolarına ölçülü ses geçişi).

### sound-effects@barty-bart  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 72 (B)

- **Ne yapar:** Claude Code ile yapılmış hareket grafiği videosuna (HyperFrames, Remotion, GSAP, motion-broll) ölçülmüş bir ses geçişi ekler: ipucu listesi çıkarır, müziğin vuruş ızgarasını kick davullarıyla karşılaştırır, ses efektlerini kesim/vuruşlara oturtur, dışa aktarılan MP4'ü ölçer ve kullanıcıya kulaklıkla kontrol için 5 zaman damgası verir. 109 CC0 ses dosyalı paketli kütüphane, varsayılan kit ve CREDITS.txt üretimi var.
- **Ne zaman:** Bir hareket grafiği videosuna 'whoosh/click/pop/riser/impact' ses efektleri ve müzik oturtmak, lisansı kayıt altına alarak. · **Ne zaman değil:** ElevenLabs ile metinden ses efekti üretmek için değil (sound-effects: üretim); sesi dinlemeden 'iyi geliyor' demez. Müzik lisansı kullanıcıdan teyit edilmeden belirsiz işaretlenir.
- **Teknoloji:** python, ffmpeg, hyperframes, remotion · **Paketler:** python bağımlılıkları (pip, ses analizi), ffmpeg, isteğe bağlı: ElevenLabs anahtarı
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** alternatif · **Örtüşme:** video-ses-gecisi → birincil · **Roller:** ses-tasarimci, motion-graphics-sanatcisi
- **Boyut:** 2455 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** pip install ile Python bağımlılıkları (ses analizi) ve ses efekti kütüphanesi indirmesi gerekir; ElevenLabs isteğe bağlı.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (bu işte birincil; ad çakışması yüzünden durum şimdilik alternatif). Ölçüm odaklı ('Claude duyamaz, bu yüzden her adımı ölçer'), lisans denetimi (CC0 ve Mixkit Free), CREDITS.txt, ses efektlerini kütüphane içi paketli dosyalardan alma; atıf yazılı (Voxyz). Kategori kararı: 02-ses-muzik-konusma'da kalır; iş ses (ses efekti yerleştirme, miks, ölçüm) ve ses-efekti grubuyla aynı kategoride durması keşfi kolaylaştırır; 04-motion-graphics'e taşımak bu işi motion kategorisinde ses işinden koparır. Ad çakışması: sound-effects (OpenMontage, ElevenLabs ile üretim) ile aynı ad, FARKLI iş: biri ses ÜRETİR, bu video üzerinde ölçülü ses GEÇİŞİ yapar. Çıplak ad el değiştirmesin diye mevcut tercih korunuyor; durumu tercih yapmak kullanıcı kararı (durum_elle). Ücret: kismen (ElevenLabs isteğe bağlı; ücretsiz yol paketli CC0 kütüphane). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION); ses dosyaları CC0, Mixkit dosyaları çalışma anında indirilir ve repoya konmaz. Güvenlik: DİKKAT (orta) — pip install, çalışma anında Mixkit indirmesi (yalnız proje klasörüne). Örtüşme: video-ses-gecisi grubunda birincil (farklı iş), ses-efekti grubuyla (sound-effects birincil) ilişkili.
- **Not:** Aynı ad farklı iş: OpenMontage'daki sound-effects çıplak adın tercihi; bu kayıt motion-graphics videolarına ölçülü ses geçişi ekler.

### speech-to-text  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Scribe v2 ile 90+ dilde kelime zaman damgalı, konuşmacı ayrımlı transkripsiyon yapar; anahtar terim ipucu, dil tespiti ve gerçek zamanlı model seçeneklerini gösterir.
- **Ne zaman:** Altyazı, toplantı/röportaj dökümü veya kelime senkronlu altyazı gereken video işlerinde. · **Ne zaman değil:** Tamamen çevrimdışı çalışılacaksa (video-understand/whisper); Azure tercih edildiğinde.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → birincil · **Roller:** ses-tasarimci
- **Boyut:** 40 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi skill, Türkçe dahil yüksek doğruluk.

### text-to-speech  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** HeyGen'in Starfish TTS modeliyle bağımsız ses dosyası üretir; ses listeleme, hız/perde kontrolü ve MCP araçlarını tercih etme kuralını içerir.
- **Ne zaman:** Zaten HeyGen kullanılan projelerde, HeyGen avatarlarıyla tutarlı ses gerektiğinde. · **Ne zaman değil:** Genel seslendirme için (elevenlabs daha esnek); ses klonlama gerekiyorsa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Adı genel olsa da HeyGen'e özel; önceki ses-tasarimci çekirdeğinden opsiyonele alındı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.
