# 02-ses-muzik-konusma — Video, Ses ve AI Medya Üretimi

_Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **18/18**

### acestep  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** ACE-Step 1.5 açık kaynak modeliyle RunPod üzerinde enstrümantal müzik, sözlü şarkı, cover/stil aktarımı ve stem ayırma yapar; sahne ön ayarları (corporate-bg, tension, cta) içerir.
- **Ne zaman:** Açık kaynak/ucuz müzik üretimi veya stem ayırma gerektiğinde ve tools/music_gen.py bulunan toolkit kuruluysa. · **Ne zaman değil:** OpenMontage kurulumunda (tools/music_gen.py yok); hızlı sonuç için music veya lyria.
- **Teknoloji:** python, runpod, ffmpeg · **Paketler:** RUNPOD_API_KEY, claude-code-video-toolkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 9 KB (SKILL.md 9.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu tools/music_gen.py OpenMontage c806645'te yok (claude-code-video-toolkit'ten taşınmış); --brand digital-samba gibi örnekler yabancı projeye ait.

### agents  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** ElevenLabs Agents Platform ile gerçek zamanlı sesli yapay zekâ ajanı (asistan, müşteri hizmetleri botu, etkileşimli karakter) kurar; CLI, Python, JS ve web gömme örnekleri içerir.
- **Ne zaman:** Uygulamaya konuşan, dinleyen sesli asistan veya telefon/web sesli bot eklenecekse. · **Ne zaman değil:** Tek seferlik seslendirme/medya üretimi (elevenlabs, text-to-speech).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js, @elevenlabs/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** sesli-ajan → birincil · **Roller:** ai-entegrasyon · **Globalde:** claude:ayni
- **Boyut:** 64 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmi ElevenLabs skill'i, güncel. Medya üretimi değil uygulama entegrasyonu; video rollerine eklenmedi.

### ai-music-album  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Full-lifecycle AI music album production — concept, lyric drafting, track sequencing, and export. Useful for indie album experiments and brand soundtracks.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105071, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### azure-speech-to-text  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Azure AI Speech Fast Transcription REST API ile ses/videoyu kelime zaman damgalı, konuşmacı ayrımlı yazıya döker; OpenMontage'da azure_stt aracı olarak transcriber şemasıyla birebir uyumludur.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve bulutta hızlı transkript/altyazı gerekiyorsa. · **Ne zaman değil:** Azure hesabı yoksa (speech-to-text veya yerel whisper); OpenMontage dışında araç sarmalayıcısı yok.
- **Teknoloji:** azure, python, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Düzgün belgelenmiş; OpenMontage registry'sine bağlı kod örnekleri.

### azure-text-to-speech  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Azure nöral TTS ile SSML prozodi ve konuşma stili kontrollü çok dilli seslendirme üretir; OpenMontage'da azure_tts aracı olarak tts_selector üzerinden çalışır.
- **Ne zaman:** AZURE_SPEECH_KEY tanımlıysa ve SSML ile ince ayarlı, uygun maliyetli anlatım gerekiyorsa (Türkçe nöral sesler dahil). · **Ne zaman değil:** Ses klonlama gerekiyorsa (elevenlabs); Azure hesabı yoksa.
- **Teknoloji:** azure, python, ssml, api-anahtari · **Paketler:** AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güvenilir kurumsal TTS; STT ile aynı kaynak.

### dashscope  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** Alibaba DashScope (Bailian) entegrasyonu: Qwen-Image ile görsel üretimi, Qwen-TTS ile seslendirme ve kelime zaman damgalı Qwen-ASR transkripsiyonu; yerel (OpenAI uyumlu olmayan) uç noktaları doğru kullanmayı anlatır.
- **Ne zaman:** Çince içerik veya DASHSCOPE_API_KEY olan, Çin bölgesi modelleri tercih edilen projelerde. · **Ne zaman değil:** Türkçe/İngilizce odaklı genel işlerde (elevenlabs, flux); DashScope anahtarı yoksa.
- **Teknoloji:** dashscope, python, api-anahtari · **Paketler:** DASHSCOPE_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ve pratik; çoklu yetenek (görsel+TTS+ASR) olduğu için kategori sınırında. Çin pazarına odaklı.

### doubao-tts  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** Volcengine Doubao Speech 2.0 ile Mandarin ve çok dilli seslendirme üretir; asenkron uç noktadan karakter düzeyinde zaman damgası alıp altyazı kurmayı ve önce kısa örnekle onay almayı öğretir.
- **Ne zaman:** Çince seslendirme veya Doubao/Volcengine tercih edildiğinde. · **Ne zaman değil:** Türkçe/İngilizce anlatımda; Doubao anahtarı yoksa.
- **Teknoloji:** volcengine, python, api-anahtari · **Paketler:** DOUBAO_SPEECH_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İş akışı (örnek → onay → tam üretim) örnek alınacak kadar iyi; kullanım alanı dar.

### elevenlabs  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile seslendirme, ses klonlama, ses efekti ve müzik üretimini tek skillde toplar; model seçimi, stile göre ses ayarları, duraklama/telaffuz kontrolü ve yinelemeli üretim akışını verir.
- **Ne zaman:** Video seslendirmesi, anlatım veya ses klonlama gereken her işte varsayılan TTS olarak. · **Ne zaman değil:** Sadece müzik (music) veya sadece efekt (sound-effects) için ayrıntılı API gerekiyorsa; sesli ajan (agents).
- **Teknoloji:** elevenlabs, python, ffmpeg, api-anahtari · **Paketler:** elevenlabs, ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → birincil · **Roller:** ses-tasarimci · **Globalde:** claude:farkli
- **Boyut:** 16 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Pratik üretim bilgisi (ayar tabloları, SSML sınırları, ellipsis uyarısı) çok değerli; Türkçe destekli multilingual_v2.

### fish-audio-tts  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** fish.audio S1/S2 modelleriyle duygu etiketli ([laugh], [whispers]) çok dilli seslendirme ve reference_id ile klonlanmış sesleri yeniden kullanma; bayt bazlı fiyatlandırmayı açıklar.
- **Ne zaman:** Yüksek duygu ifadeli anlatım veya fish.audio'da hazırlanmış klon ses gerektiğinde. · **Ne zaman değil:** Ücretsiz promosyon modeli (s2.1-pro-free) ile ticari/müşteri işi; fish.audio anahtarı yoksa.
- **Teknoloji:** fish-audio, python, api-anahtari · **Paketler:** FISH_AUDIO_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Güncel ve dürüst (promosyon kısıtları açıkça yazılmış).

### lyria  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** Google Lyria 3 ile Gemini Interactions API üzerinden müzik üretir ve doğrular; Clip/Pro/RealTime model seçimi, yapılandırılmış prompt sözleşmesi, maliyet duyurusu ve videoya tam süreli master çıkarma adımlarını tanımlar.
- **Ne zaman:** Google anahtarı varken altyapı müziği, döngü veya sözlü şarkı gerektiğinde; ucuz ve hızlı deneme için. · **Ne zaman değil:** ElevenLabs Music tercih edildiğinde; OpenMontage google_music adaptörü sadece Pro modelini destekliyor.
- **Teknoloji:** google-gemini, api-anahtari · **Paketler:** GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Disiplinli iş akışı ve adaptör kısıtlarını açıkça söylüyor; kalite yüksek.

### music  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Music API ile metin isteminden enstrümantal parça, sözlü şarkı, jingle üretir; bölüm bazlı ince kontrol için kompozisyon planı oluşturup düzenlemeyi gösterir.
- **Ne zaman:** Video için arka plan müziği, jingle veya şarkı üretilecekse. · **Ne zaman değil:** Hazır stok müzik yeterliyse (media-use); sanatçı/şarkı taklidi istenirse (API reddeder).
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** muzik-uretimi → birincil · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi ElevenLabs skill'i; bağımsız SDK ile her yerde çalışır.

### setup-api-key  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** ElevenLabs API anahtarını kurar: önce mevcut ELEVENLABS_API_KEY'i bulup doğrular, yoksa kullanıcıyı adım adım anahtar oluşturmaya yönlendirir ve .env'e yazar.
- **Ne zaman:** ElevenLabs skilleri anahtar eksikliğinden çalışmadığında veya anahtar değiştirilecekken. · **Ne zaman değil:** Diğer sağlayıcıların anahtarları (genel bir anahtar kurulum aracı değil); anahtar zaten tanımlıyken.
- **Teknoloji:** elevenlabs, api-anahtari · **Paketler:** ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** api-anahtari-kurulumu → birincil · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Sadece ElevenLabs'a özel olduğu için 03'ten 02'ye taşındı. Anahtarı sohbete yapıştırtması güvenlik açısından dikkat ister.

### sound-effects  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs ile metin tarifinden ses efekti, ambiyans, döngü ve UI sesi üretir; süre, prompt etkisi ve döngü parametrelerini açıklar.
- **Ne zaman:** Video, oyun veya arayüz için özgün efekt/ambiyans gerektiğinde. · **Ne zaman değil:** Hazır efekt kütüphanesi yeterliyse (media-use, hyperframes-media); konuşma veya müzik için.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ses-efekti → birincil · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 3.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi, kısa ve eksiksiz.

### speech  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Generate spoken audio from text using OpenAI's API with built-in voices. Useful for narrated explainers, lecture audio, and quick voiceover tracks.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105071, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### speech-to-text  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** ElevenLabs Scribe v2 ile 90+ dilde kelime zaman damgalı, konuşmacı ayrımlı transkripsiyon yapar; anahtar terim ipucu, dil tespiti ve gerçek zamanlı model seçeneklerini gösterir.
- **Ne zaman:** Altyazı, toplantı/röportaj dökümü veya kelime senkronlu altyazı gereken video işlerinde. · **Ne zaman değil:** Tamamen çevrimdışı çalışılacaksa (video-understand/whisper); Azure tercih edildiğinde.
- **Teknoloji:** elevenlabs, python, typescript, api-anahtari · **Paketler:** elevenlabs, @elevenlabs/elevenlabs-js
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** stt-transkripsiyon → birincil · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 40 KB (SKILL.md 7.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi skill, Türkçe dahil yüksek doğruluk.

### text-to-speech  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** HeyGen'in Starfish TTS modeliyle bağımsız ses dosyası üretir; ses listeleme, hız/perde kontrolü ve MCP araçlarını tercih etme kuralını içerir.
- **Ne zaman:** Zaten HeyGen kullanılan projelerde, HeyGen avatarlarıyla tutarlı ses gerektiğinde. · **Ne zaman değil:** Genel seslendirme için (elevenlabs daha esnek); ses klonlama gerekiyorsa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73527, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** tts-saglayici → alternatif · **Roller:** ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Adı genel olsa da HeyGen'e özel; önceki ses-tasarimci çekirdeğinden opsiyonele alındı.

### venice-audio-music  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Music generation queueing, retrieval, and completion endpoints via Venice.ai. Suited for jingles, background loops, and prototype scoring.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105071, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### venice-audio-speech  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Text-to-speech models, voices, formats, and streaming via Venice.ai. Useful for narration, voiceover, and conversational agent voices.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105071, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.
