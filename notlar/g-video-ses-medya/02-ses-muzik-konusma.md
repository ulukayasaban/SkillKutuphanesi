# 02-ses-muzik-konusma — Video, Ses ve AI Medya Üretimi

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **16/30**

### acestep  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 77 (B)

- **Ne yapar:** ACE-Step 1.5 açık kaynak modeliyle RunPod üzerinde enstrümantal müzik, sözlü şarkı, cover/stil aktarımı ve stem ayırma yapar; sahne ön ayarları (corporate-bg, tension, cta) içerir.
- **Ne zaman:** Açık kaynak/ucuz müzik üretimi veya stem ayırma gerektiğinde ve tools/music_gen.py bulunan toolkit kuruluysa. · **Ne zaman değil:** OpenMontage kurulumunda (tools/music_gen.py yok); hızlı sonuç için music veya lyria.
- **Teknoloji:** python, runpod, ffmpeg · **Paketler:** RUNPOD_API_KEY, claude-code-video-toolkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu tools/music_gen.py OpenMontage c806645'te yok (claude-code-video-toolkit'ten taşınmış); --brand digital-samba gibi örnekler yabancı projeye ait.

### agents  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** ElevenLabs Agents Platform ile gerçek zamanlı sesli yapay zekâ ajanı (asistan, müşteri hizmetleri botu, etkileşimli karakter) kurar; CLI, Python, JS ve web gömme örnekleri içerir.
- **Ne zaman:** Uygulamaya konuşan, dinleyen sesli asistan veya telefon/web sesli bot eklenecekse. · **Ne zaman değil:** Tek seferlik seslendirme/medya üretimi (elevenlabs, text-to-speech).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js, @elevenlabs/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** sesli-ajan → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 64 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmi ElevenLabs skill'i, güncel. Medya üretimi değil uygulama entegrasyonu; video rollerine eklenmedi.

### azure-speech-to-text  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** Azure AI Speech Fast Transcription REST API ile ses/videoyu kelime zaman damgalı, konuşmacı ayrımlı yazıya döker; OpenMontage'da azure_stt aracı olarak transcriber şemasıyla birebir uyumludur.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve bulutta hızlı transkript/altyazı gerekiyorsa. · **Ne zaman değil:** Azure hesabı yoksa (speech-to-text veya yerel whisper); OpenMontage dışında araç sarmalayıcısı yok.
- **Teknoloji:** azure, python, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Düzgün belgelenmiş; OpenMontage registry'sine bağlı kod örnekleri.

### azure-text-to-speech  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** Azure nöral TTS ile SSML prozodi ve konuşma stili kontrollü çok dilli seslendirme üretir; OpenMontage'da azure_tts aracı olarak tts_selector üzerinden çalışır.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve SSML ile ince ayarlı, uygun maliyetli anlatım gerekiyorsa (Türkçe nöral sesler dahil). · **Ne zaman değil:** Ses klonlama gerekiyorsa (elevenlabs); Azure hesabı yoksa.
- **Teknoloji:** azure, python, ssml, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güvenilir kurumsal TTS; STT ile aynı kaynak.

### dashscope  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 86 (A)

- **Ne yapar:** Alibaba DashScope (Bailian) entegrasyonu: Qwen-Image ile görsel üretimi, Qwen-TTS ile seslendirme ve kelime zaman damgalı Qwen-ASR transkripsiyonu; yerel (OpenAI uyumlu olmayan) uç noktaları doğru kullanmayı anlatır.
- **Ne zaman:** Çince içerik veya DASHSCOPE_API_KEY olan, Çin bölgesi modelleri tercih edilen projelerde. · **Ne zaman değil:** Türkçe/İngilizce odaklı genel işlerde (elevenlabs, flux); DashScope anahtarı yoksa.
- **Teknoloji:** dashscope, python, api-anahtari · **Paketler:** DASHSCOPE_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci, ai-medya-uretici
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ve pratik; çoklu yetenek (görsel+TTS+ASR) olduğu için kategori sınırında. Çin pazarına odaklı.

### doubao-tts  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 86 (A)

- **Ne yapar:** Volcengine Doubao Speech 2.0 ile Mandarin ve çok dilli seslendirme üretir; asenkron uç noktadan karakter düzeyinde zaman damgası alıp altyazı kurmayı ve önce kısa örnekle onay almayı öğretir.
- **Ne zaman:** Çince seslendirme veya Doubao/Volcengine tercih edildiğinde. · **Ne zaman değil:** Türkçe/İngilizce anlatımda; Doubao anahtarı yoksa.
- **Teknoloji:** volcengine, python, api-anahtari · **Paketler:** DOUBAO_SPEECH_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İş akışı (örnek → onay → tam üretim) örnek alınacak kadar iyi; kullanım alanı dar.

### earshot  ·  Leonxlnx/earshot @ 591fa3e  ·  puan 82 (A)

- **Ne yapar:** Agent'a 'kulak' kazandırır: ses dosyasını tarif eder, metinle eşleştirir ve puanlar (CLAP + AST, CPU'da). Film/video için ses zaman çizelgesi ve eleştiri çıkarır, kodla ses efekti üretir; MCP sunucusu da sunar.
- **Ne zaman:** Video/ses üretiminde hazır ses efektlerini ya da müziği dinleyip doğru olanı seçmek, miksi kontrol etmek. · **Ne zaman değil:** Kurulum ağır: Python paketi + torch/transformers, ilk çalışmada Hugging Face'ten model indirir. Önerdiği `claude mcp add --scope user` komutu GENEL Claude ayarına yazar; isteğe bağlı, onaysız yapılmamalı. `llm` komutu sesi Gemini'ye yükler (sadece --yes-upload + kendi anahtarınla).
- **Teknoloji:** python, torch · **Paketler:** earshot (pip install -e), torch, transformers
- **Claude / Codex:** tam / tam
- **Geliştirici:** Leonxlnx (kisi, ★3898, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ses-analiz → birincil
- **Boyut:** 21 KB (SKILL.md 21.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (ses-analiz grubunda birincil). MIT, 3,9k★. Ücretsiz, yerel; rol çekirdeğine girmez (kurulum yükü).

### elevenlabs  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile seslendirme, ses klonlama, ses efekti ve müzik üretimini tek skillde toplar; model seçimi, stile göre ses ayarları, duraklama/telaffuz kontrolü ve yinelemeli üretim akışını verir.
- **Ne zaman:** Video seslendirmesi, anlatım veya ses klonlama gereken her işte varsayılan TTS olarak. · **Ne zaman değil:** Sadece müzik (music) veya sadece efekt (sound-effects) için ayrıntılı API gerekiyorsa; sesli ajan (agents).
- **Teknoloji:** elevenlabs, python, ffmpeg, api-anahtari · **Paketler:** elevenlabs, ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → birincil · **Roller:** ses-tasarimci
- **Boyut:** 16 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Pratik üretim bilgisi (ayar tabloları, SSML sınırları, ellipsis uyarısı) çok değerli; Türkçe destekli multilingual_v2. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### fish-audio-tts  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** fish.audio S1/S2 modelleriyle duygu etiketli ([laugh], [whispers]) çok dilli seslendirme ve reference_id ile klonlanmış sesleri yeniden kullanma; bayt bazlı fiyatlandırmayı açıklar.
- **Ne zaman:** Yüksek duygu ifadeli anlatım veya fish.audio'da hazırlanmış klon ses gerektiğinde. · **Ne zaman değil:** Ücretsiz promosyon modeli (s2.1-pro-free) ile ticari/müşteri işi; fish.audio anahtarı yoksa.
- **Teknoloji:** fish-audio, python, api-anahtari · **Paketler:** FISH_AUDIO_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güncel ve dürüst (promosyon kısıtları açıkça yazılmış).

### krillinai-cli  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when an agent needs to build or operate the embedded KrillinAI CLI, choose a supported command, or interpret its JSON, manifest, subtitle, dubbing, render, cover, speech, and voice outputs.
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.4 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-cover  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when generating a cover image with the KrillinAI CLI from a complete image prompt, including validating image-provider configuration and inspecting the generated image and saved prompt.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-pipeline  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when validating or documenting a multi-stage KrillinAI CLI output plan; the current pipeline command supports dry-run planning only, not end-to-end execution.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-render-horizontal  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when rendering landscape videos with KrillinAI CLI, including original video plus bilingual subtitles or dubbed video plus target-language subtitles.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-render-vertical  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when rendering portrait videos with KrillinAI CLI, including converting source video to vertical format, adding short bilingual subtitles, rendering dubbed vertical videos, and checking vertical subtitle readability.
- **Teknoloji:** ffmpeg, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-subtitle  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when generating subtitles with KrillinAI CLI from a YouTube link, Bilibili/local video, or existing media, including platform caption download, Whisper fallback, translation, bilingual SRT, and short vertical subtitle output.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### krillinai-tts  ·  krillinai/OpenCreator @ b5b9235  ·  puan 89 (A)

- **Ne yapar:** Use when generating target-language dubbing with KrillinAI CLI from SRT subtitles, including TTS audio creation and optional dubbed video generation.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** krillinai (kisi, ★14157, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** OpenCreator / krillinai CLI (video çeviri, altyazı, TTS, render). TTS/LLM için sağlayıcı anahtarı gerekebilir → kismen.
- **İnceleme:** otomatik

### lyria  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** Google Lyria 3 ile Gemini Interactions API üzerinden müzik üretir ve doğrular; Clip/Pro/RealTime model seçimi, yapılandırılmış prompt sözleşmesi, maliyet duyurusu ve videoya tam süreli master çıkarma adımlarını tanımlar.
- **Ne zaman:** Google anahtarı varken altyapı müziği, döngü veya sözlü şarkı gerektiğinde; ucuz ve hızlı deneme için. · **Ne zaman değil:** ElevenLabs Music tercih edildiğinde; OpenMontage google_music adaptörü sadece Pro modelini destekliyor.
- **Teknoloji:** google-gemini, api-anahtari · **Paketler:** GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 18 KB (SKILL.md 8.6 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Disiplinli iş akışı ve adaptör kısıtlarını açıkça söylüyor; kalite yüksek. · 2026-11-12 yeniden incelendi (fecb9a1): skill artık Lyria 3.5 (varsayılan `lyria-3.5`, ~$0.08/istek) ve Clip'i anlatıyor; `lyria-3-pro-preview` açıkça istenen eski seçenek; OpenMontage adaptörü artık iki modeli kabul ediyor, süre 5-184 sn doğrulanıyor (gerçek süre yine prob edilmeli), 3.5 maliyet tahmini güncel fiyat teklifi ister; GOOGLE_GENAI_USE_VERTEXAI=true ile Vertex yolu. Bağımlılık aynı (GEMINI_API_KEY, ücretli). Lisans notu: model/adaptör rehberi andromia3 katkısı, depo AGPL-3.0.

### music  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Music API ile metin isteminden enstrümantal parça, sözlü şarkı, jingle üretir; bölüm bazlı ince kontrol için kompozisyon planı oluşturup düzenlemeyi gösterir.
- **Ne zaman:** Video için arka plan müziği, jingle veya şarkı üretilecekse. · **Ne zaman değil:** Hazır stok müzik yeterliyse (media-use); sanatçı/şarkı taklidi istenirse (API reddeder).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → birincil · **Roller:** ses-tasarimci
- **Boyut:** 10 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi ElevenLabs skill'i; bağımsız SDK ile her yerde çalışır.

### music-connect  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** One-time setup — mint a Cognitum Music personal access token and register the cogmusic MCP server with Claude Code
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### music-generate  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Generate a new song from a creative brief (genre, mood, language, BPM, theme) via the cogmusic MCP create_production tool
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### music-get  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Fetch metadata and audio_url for a single production by id
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### music-list  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** List the account's saved music productions with metadata and audio_url
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### music-master  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run a mastering pass (LUFS loudness normalization + peak limiting) on an existing production
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### music-midi  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Extract MIDI/score from an existing production
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### music-stems  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Run 4-stem separation (vocals/drums/bass/other) on an existing production
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### real-sound  ·  Leonxlnx/earshot @ 591fa3e  ·  puan 82 (A)

- **Ne yapar:** Ses efekti ve müzik için gerçek, lisanslı kayıtları (Freesound, Mixkit, Pixabay; CC0/CC-BY) bulur, seçer, miksler ve masterlar; lisans bilgisini kaydeder.
- **Ne zaman:** Sentetik değil gerçek kayıt ses efekti istenen video/oyun projeleri. · **Ne zaman değil:** Sesi kodla üretmek için sound-effects (OpenMontage) ya da hyperframes-audio. CC-BY seslerde atıf zorunlu. Sitelerden dosya indirir.
- **Teknoloji:** python, ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** Leonxlnx (kisi, ★3898, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ses-efekti → alternatif
- **Boyut:** 321 KB (SKILL.md 15.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (ses-efekti grubu; sound-effects birincil). MIT. Ücretsiz kaynaklar.

### setup-api-key  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 86 (A)

- **Ne yapar:** ElevenLabs API anahtarını kurar: önce mevcut ELEVENLABS_API_KEY'i bulup doğrular, yoksa kullanıcıyı adım adım anahtar oluşturmaya yönlendirir ve .env'e yazar.
- **Ne zaman:** ElevenLabs skilleri anahtar eksikliğinden çalışmadığında veya anahtar değiştirilecekken. · **Ne zaman değil:** Diğer sağlayıcıların anahtarları (genel bir anahtar kurulum aracı değil); anahtar zaten tanımlıyken.
- **Teknoloji:** elevenlabs, api-anahtari · **Paketler:** ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** api-anahtari-kurulumu → birincil · **Roller:** ses-tasarimci
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Sadece ElevenLabs'a özel olduğu için 03'ten 02'ye taşındı. Anahtarı sohbete yapıştırtması güvenlik açısından dikkat ister.

### sound-effects  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile metin tarifinden ses efekti, ambiyans, döngü ve UI sesi üretir; süre, prompt etkisi ve döngü parametrelerini açıklar.
- **Ne zaman:** Video, oyun veya arayüz için özgün efekt/ambiyans gerektiğinde. · **Ne zaman değil:** Hazır efekt kütüphanesi yeterliyse (media-use, hyperframes-media); konuşma veya müzik için.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ses-efekti → birincil · **Roller:** ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi, kısa ve eksiksiz.

### speech-to-text  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Scribe v2 ile 90+ dilde kelime zaman damgalı, konuşmacı ayrımlı transkripsiyon yapar; anahtar terim ipucu, dil tespiti ve gerçek zamanlı model seçeneklerini gösterir.
- **Ne zaman:** Altyazı, toplantı/röportaj dökümü veya kelime senkronlu altyazı gereken video işlerinde. · **Ne zaman değil:** Tamamen çevrimdışı çalışılacaksa (video-understand/whisper); Azure tercih edildiğinde.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → birincil · **Roller:** ses-tasarimci
- **Boyut:** 40 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi skill, Türkçe dahil yüksek doğruluk.

### text-to-speech  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** HeyGen'in Starfish TTS modeliyle bağımsız ses dosyası üretir; ses listeleme, hız/perde kontrolü ve MCP araçlarını tercih etme kuralını içerir.
- **Ne zaman:** Zaten HeyGen kullanılan projelerde, HeyGen avatarlarıyla tutarlı ses gerektiğinde. · **Ne zaman değil:** Genel seslendirme için (elevenlabs daha esnek); ses klonlama gerekiyorsa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Adı genel olsa da HeyGen'e özel; önceki ses-tasarimci çekirdeğinden opsiyonele alındı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.
