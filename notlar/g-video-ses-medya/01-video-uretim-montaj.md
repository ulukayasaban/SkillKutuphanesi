# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **22/22**

### create-video  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-produksiyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### ffmpeg  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### hyperframes  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** HTML'den video render eden HyperFrames'in giriş ve yönlendirme skill'i: alt skillerin (core, animation, creative, media, cli, registry) haritasını ve 'video yap' isteğini doğru iş akışına yönlendiren tabloyu verir.
- **Ne zaman:** Herhangi bir video/animasyon/motion graphic isteğinde ilk okunacak skill; HyperFrames ile video yazılacaksa. · **Ne zaman değil:** Kullanıcı açıkça Remotion veya başka bir çerçeve istiyorsa; sadece hazır videoyu kesip biçen FFmpeg işlerinde.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 20 KB (SKILL.md 16.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Ekosistemin yönlendiricisi, iyi yapılandırılmış. Dikkat: /general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions yönlendirmeleri arşivde yok (OpenMontage c806645'te bulunmuyor).

### hyperframes-animation  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri ve GSAP, Lottie, Three.js, Anime.js, CSS, WAAPI, TypeGPU çalışma zamanı adaptörleri. Tek duraklatılmış, seek-güvenli zaman çizelgesi ilkesine dayanır.
- **Ne zaman:** HyperFrames kompozisyonunda hareket, geçiş veya sahne koreografisi yazarken. · **Ne zaman değil:** HyperFrames dışı web animasyonu (gsap-* veya framer-motion skilleri daha uygun); Remotion projeleri.
- **Teknoloji:** hyperframes, gsap, html, css, lottie, three.js · **Paketler:** hyperframes (npx), gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 2521 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çok zengin kural/blueprint kütüphanesi (2.5 MB); SKILL.md kısa yönlendirici, ayrıntı isteğe bağlı yükleniyor.

### hyperframes-cli  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HyperFrames CLI geliştirme döngüsü: init, add, lint, validate, inspect, preview, render, AWS Lambda render ve sorun giderme. Render öncesi lint/validate/inspect zorunluluğunu ve --json kullanımını tanımlar.
- **Ne zaman:** HyperFrames projesi kurarken, doğrularken, önizlerken ve render alırken. · **Ne zaman değil:** Kompozisyon HTML'inin içeriği/sözleşmesi için (hyperframes-core); HyperFrames kullanılmayan projelerde.
- **Teknoloji:** hyperframes, node, ffmpeg, docker, aws-lambda · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 54 KB (SKILL.md 9.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik ve ajan dostu. Not: 'init' global skill setini otomatik güncelliyor; kütüphane kuralı gereği bu davranış izlenmeli.

### hyperframes-core  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönettiği medya oynatma ve deterministik render kuralları. Kompozisyon HTML'i yazmadan önce okunur.
- **Ne zaman:** Renderlanabilir bir HyperFrames projesi kurarken veya mevcut kompozisyonu düzenlerken. · **Ne zaman değil:** Sadece hareket tarifi arıyorsan (hyperframes-animation); HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 78 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Net teknik sözleşme ve referans dizini; diğer alt skillerin temeli.

### hyperframes-creative  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, sese duyarlı görseller ve marka kararları. 'Web sayfası gibi görünen' jenerik çıktıyı önleyen ev stili kurallarını içerir.
- **Ne zaman:** Çok sahneli veya markalı bir HyperFrames videosunun görsel dilini ve ritmini planlarken. · **Ne zaman değil:** Atomik hareket ve geçişler için (hyperframes-animation); tek satırlık düzenlemelerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1000 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çıktı kalitesini en çok etkileyen alt skill; house-style ve video-composition referansları güçlü.

### hyperframes-media  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Tek ses motoru (scripts/audio.mjs) ile HyperFrames için TTS (HeyGen/ElevenLabs/Kokoro), arka plan müziği, ses efekti, Whisper transkripsiyonu, arka plan silme ve altyazı/karaoke üretimi. HeyGen anahtarı yoksa yerel/ücretsiz yollara düşer.
- **Ne zaman:** HyperFrames kompozisyonuna seslendirme, müzik, efekt veya kelime zamanlı altyazı eklerken. · **Ne zaman değil:** HyperFrames dışı projelerde; belirli bir sağlayıcının ayrıntılı API'si gerekiyorsa (elevenlabs, lyria vb.).
- **Teknoloji:** hyperframes, node, heygen, elevenlabs, whisper · **Paketler:** node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon, ses-tasarimci · **Globalde:** claude:ayni
- **Boyut:** 1396 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Sağlayıcı zinciri ve yedek yollar iyi tasarlanmış; varsayılanı HeyGen'e bağlı.

### hyperframes-registry  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HyperFrames kayıt defterindeki hazır blok ve bileşenleri 'hyperframes add' ile kurar ve ana kompozisyona bağlar; yeni blok/bileşen yazıp üst projeye katkı akışını da anlatır.
- **Ne zaman:** Hazır grafik/efekt bloklarını (data-chart, grain-overlay…) kompozisyona eklerken. · **Ne zaman değil:** Sıfırdan özel sahne yazarken; HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, node · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 49 KB (SKILL.md 4.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar ama net kapsam; registry ağ erişimi gerektirir.

### media-use  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** BGM, ses efekti, görsel ve ikon ihtiyacını tek 'resolve' komutuyla HeyGen kataloğunda arayıp indirir, yerelde dondurur ve manifest'e kaydeder; ajana sadece dosya yolunu döndürür.
- **Ne zaman:** Kompozisyona hazır stok müzik, efekt, görsel veya ikon gerektiğinde, bağlamı arama gürültüsüyle doldurmadan. · **Ne zaman değil:** Özgün üretim gerekiyorsa (music, sound-effects, flux); HeyGen anahtarı yoksa katalog araması sınırlı.
- **Teknoloji:** node, heygen, api-anahtari · **Paketler:** node, HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-varlik-temini → birincil · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 66 KB (SKILL.md 5.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Bağlam dostu tasarım (tek satır çıktı, önbellek). HeyGen kataloğuna bağımlı.

### music-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Bir müzik parçasından vuruşa senkron HyperFrames videosu üretir: parçayı tek analizörle (beatgrid) çözümler, kareleri planlar, her kareyi ayrı alt ajana yaptırır ve render eder. Şarkı sözü videosu, slayt gösterisi veya kinetik tanıtım bu akıştan çıkar.
- **Ne zaman:** Elinde müzik (veya sesinden yararlanılacak video) olan, ritme oturan klip/lyric video isteklerinde. · **Ne zaman değil:** Anlatımlı veya web sitesinden üretilecek videolarda; müziği olmayan işlerde.
- **Teknoloji:** hyperframes, python, html, gsap · **Paketler:** hyperframes (npx), python3, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-produksiyon, motion-graphics-sanatcisi · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6053 KB (SKILL.md 15.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapılı (gate) iş akışı ve alt ajan dağıtımı olgun; çok ajanlı olduğu için maliyetli/uzun.

### playwright-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### remotion  ·  calesthio/OpenMontage @ c806645  ·  puan 71 (B)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### remotion-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Roller:** video-produksiyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil.

### remotion-to-hyperframes  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Mevcut bir Remotion (React) kompozisyonunu HyperFrames HTML'ine taşır; eşlenebilen kalıpları çevirir, useState/useEffect gibi uyumsuz kalıpları işaretler ve SSIM eşikli test korpusuyla çeviriyi doğrular.
- **Ne zaman:** Kullanıcı açıkça Remotion projesini HyperFrames'e taşımak istediğinde. · **Ne zaman değil:** Yeni kompozisyon yazarken veya Remotion sadece referans olarak geçiyorsa; ters yönde dönüşüm.
- **Teknoloji:** remotion, hyperframes, react, html, gsap · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 168 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar kapsamlı ama disiplinli (eval zorunlu). /general-video yönlendirmesi arşivde yok.

### synthetic-screen-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 78 (B)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### video-download  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-toolkit  ·  calesthio/OpenMontage @ c806645  ·  puan 70 (B)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-produksiyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### website-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 85 (A)

- **Ne yapar:** Bir web sitesini headless Chrome ile yakalayıp marka varlıklarıyla HyperFrames videosuna (site turu, vitrin, sosyal klip) dönüştüren 7 adımlı, kapılı iş akışı. Varlık denetimi ve 'doğrulamadıklarım' açıklaması zorunludur.
- **Ne zaman:** Portföy/blog/landing sayfasından tanıtım turu veya sosyal medya klibi üretilecekse. · **Ne zaman değil:** Ürün lansman/promosyon videosu, konu anlatımı veya PR videosu (yönlendirdiği skiller arşivde yok).
- **Teknoloji:** hyperframes, html, node, chrome-headless · **Paketler:** hyperframes (npx), node>=22
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70531, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-produksiyon · **Globalde:** claude:ayni
- **Boyut:** 1541 KB (SKILL.md 11.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kalite kapıları güçlü. /product-launch-video ve /faceless-explainer yönlendirmeleri arşivde yok.
