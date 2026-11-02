# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **18/56**

### 8-bit-orbit-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Hyperframes-based video template for retro pixel deck motion design. Use when users want a high-fidelity, multi-scene HTML-to-video composition with advanced transitions, interactive preview controls, and ready-to-render default style.
- **Teknoloji:** css, gsap, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### after-hours-editorial-template  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Luxury dark-editorial HyperFrames template for three-page cinematic storyboards, inspired by haute couture title cards and magazine chapter spreads. Use when the user asks for premium fashion-style motion pages, moody serif-led storytelling, or a high-end dark presentation aesthetic with rich transitions.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** otomatik

### captions-overlay  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videolarında altyazı doktrini: her cümle drop / rail / embed olarak sınıflanır (embed nadir zirve), altyazı alttan rezerve bir şerit değil filmin üstüne bindirilen overlay'dir; kompozisyon gerçek dikey merkeze göre yerleşir.
- **Ne zaman:** Konuşan kafa, tanıtım ya da explainer videolarına altyazı eklerken yerleşim ve vurgu kararları. · **Ne zaman değil:** Altyazısız videolar; altyazının teknik kurulumu için hyperframes references/captions.md yeterli.
- **Teknoloji:** hyperframes · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** altyazi → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede hyperframes'in references/captions.md dosyasının üstüne uygulanan doktrin olarak konumlandı (metadata internal: true). Emekli embedded-captions iş akışına atıf içeriyor; artık hyperframes skiliyle birlikte kullanılır.

### changelog-video  ·  heygen-com/hyperframes @ f8309b3  ·  puan 82 (A)

- **Ne yapar:** Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka planı, sahte UI görselleştirmeleri ve sakin altyazılar; fontlar, arka plan müziği ve betikler skill içinde paketli.
- **Ne zaman:** Yalnız HeyGen'in kendi haftalık changelog videosu için; kendi markan için örnek/şablon olarak incelenebilir. · **Ne zaman değil:** Kendi ürününün changelog videosunda doğrudan (pr-to-video veya product-launch-video kullan); marka varlıkları HeyGen'e ait.
- **Teknoloji:** hyperframes, html, gsap, node, heygen · **Paketler:** hyperframes (npx), node>=22, ffmpeg, HeyGen hesabı (TTS)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 521 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. HeyGen iç skilli (internal:true): HeyGen marka kimliğine, sabit seslendirmene ve repo köküne bağlı; paketlenen TT Norms Pro / ABC Solar ticari fontlarının yeniden kullanım lisansı belirsiz. Rollere eklenmedi.

### chat-motion-overlay  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat containers, optional device frames, preset or uploaded avatars, nickname display rules, and transparent-video-ready Remotion bundles. Use when Codex needs to create reusable short-form chat clips for Douyin, demo videos, story reenactments, social-message proof scenes, or embed
- **Teknoloji:** python, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1308 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### create-video  ·  calesthio/OpenMontage @ 195eab2  ·  puan 97 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-kompozisyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### ffmpeg  ·  calesthio/OpenMontage @ 195eab2  ·  puan 96 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### figma  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** Figma içeriğini HyperFrames videosuna getirir: asset (SVG/PNG), marka token'ları, frame'leri düzenlenebilir HTML bileşen olarak, connector ile motion (GSAP'e çevirip doğrulama), shader ve storyboard (frame'ler slayt değil, aynı öğenin durumları).
- **Ne zaman:** Figma linki verildiğinde; marka renkleri/tipografisi, logo, bileşen ya da storyboard'u videoya taşımak. · **Ne zaman değil:** FIGMA_TOKEN yoksa ve kullanıcı oluşturmak istemiyorsa; Figma dışı tasarım kaynakları.
- **Teknoloji:** hyperframes, figma api, gsap · **Paketler:** hyperframes (npx), FIGMA_TOKEN
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede komutlar sadeleşti, storyboard kuralları (frame = keyframe) ve motion doğrulama betiği netleşti. Token sohbete yapıştırılmaz; kullanıcı kendisi ayarlar.

### frame-data-chart-nyt  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band).
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-flowchart-sticky  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-glitch-title  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-light-leak-cinema  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-liquid-bg-hero  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters.
- **Teknoloji:** canvas, css, html, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-logo-outro  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-macos-notification  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### hyperframes  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames'in yeni tek giriş skili: HTML'i kare kare render ederek videoya çeviren sistemin render sözleşmesini (12 kural), düzenlenebilirlik kurallarını, iş döngüsünü (story → SPEC → check → snapshot → review → render) ve video türlerine göre okunacak referansları (launch, explainer, müzik, data, dikey, 3D, karakter, altyazı, overlay, motion) tek yerde toplar.
- **Ne zaman:** HyperFrames ile her türlü video: tanıtım filmi, explainer, müzik videosu, grafik/harita, dikey sosyal klip, altyazı ve overlay; eskiden ayrı iş akışı skilleri olan türlerin hepsi artık buradaki references/types dosyalarıyla yürür. · **Ne zaman değil:** Remotion ya da başka bir çerçeve açıkça istenirse; sadece tarayıcı ekran kaydı gerekiyorsa (playwright-recording).
- **Teknoloji:** hyperframes, html, gsap, node 22+, ffmpeg · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → birincil · **Roller:** video-kompozisyon, video-kurgu-render, motion-graphics-sanatcisi · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 1117 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — 2026-10 güncellemesi (heygen-com/hyperframes 6882293): iş akışı skilleri emekliye ayrıldı, içerikleri bu skilin references/types ve references/*.md dosyalarına taşındı; SKILL.md 7 KB'a indi, sözleşme daha net. Önceki iş akışı skillerinin (general-video, faceless-explainer, product-launch-video…) yerine birincil seçim budur.

### hyperframes-cli  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames CLI'yi işe göre anlatır: init/capture, check, snapshot, timeline düzenleme (move/trim/split…), preview, yerel/bulut render, proje geçmişi (history begin/undo/end) ve hata tablosu. Render öncesi doğrulama döngüsünü tanımlar.
- **Ne zaman:** HyperFrames projesini kontrol etme, görsel olarak inceleme, zaman çizelgesi düzenleme ve render alma. · **Ne zaman değil:** Kompozisyonun içeriğine karar verirken tek başına yetmez; hyperframes skiliyle birlikte kullanılır.
- **Teknoloji:** hyperframes, node 22+, ffmpeg, chrome · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 124 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Güncellemede komutlar iş bazlı tabloya, render ve hata kurtarma tablolara toplandı; proje geçmişi (history) eklendi. Node 22+ ve FFmpeg gerekir.

### hyperframes-registry  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** ~450 hazır HyperFrames bloğu ve bileşenini (geçişler, overlay, başlık, kinetik tipografi, altyazı stilleri, grafik, harita, 3D, kamera hareketi) arama (`catalog --query`) ve projeye düzenlenebilir kaynak olarak kurma (`add`) rehberi.
- **Ne zaman:** Adı olan bir görsel efekti (glitch, film grain, bar chart race, lower third…) elle yazmadan önce; blok/bileşen bağlama. · **Ne zaman değil:** Kayıt defterinde karşılığı olmayan, tamamen özgün sahneler.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 83 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Güncellemede ~400 → ~450 öğe; yerel arama katmanları (words / on-device) ve 'gap' raporlama eklendi. Arama İngilizce yapılmalı.

### lemo-opuscar  ·  lemomo-ai/lemo-opuscar @ bebbbe1  ·  puan 85 (A)

- **Ne yapar:** Lemo-Opuscar film stili kütüphanesine giriş skili: 59 hazır stilden birini seçip (ya da kendi stilini oluşturup) video modeli kullanmadan, tamamen kodla kısa film yönetir ve üretir. Kütüphaneyi ilk çalıştırmada GitHub'dan ev dizinine (~/lemo-opuscar) seyrek klonlar, gerekli Node/Python paketlerini kurar ve kütüphanenin AGENTS.md akışını izler.
- **Ne zaman:** Belirli bir görsel stilde (yağlı boya, suluboya, ukiyo-e, uydu brifingi, ürün parçalama vb.) kodla üretilmiş kısa film, tanıtım, açıklayıcı video; uydu görüntüsü/lazer tarama/CAD/arşiv gibi gerçek malzemeden veri anlatımı; kendi film stilini oluşturma. · **Ne zaman değil:** Mevcut bir videoyu sadece kesip birleştirmek/dönüştürmek (video-edit, ffmpeg); HyperFrames projesi içinde sahne kurmak (hyperframes).
- **Teknoloji:** node, three.js, ffmpeg, python, kokoro tts · **Paketler:** node, ffmpeg, python3 (seslendirme için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★10618, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kodla-film-stilleri → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 10 KB (SKILL.md 3.4 KB, yük kucuk) · **Bağımlılık:** Çalışınca kendi kütüphanesini ev dizinine indirir/kopyalar (~/lemo-opuscar veya ~/.lemo-opuscar), Node + ffmpeg (+ seslendirme için Python/Kokoro) ister. Ücretsiz: varsayılan TTS çevrimdışı Kokoro; edge-tts metni Microsoft'a gönderir (sadece kullanıcı onaylarsa).
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — MIT, ücretsiz; varsayılan seslendirme çevrimdışı Kokoro, edge-tts sadece onayla. DİKKAT: kodun asıl kısmı çalışma anında GitHub'ın main dalından (sabit commit değil) ~/lemo-opuscar'a indirilir; yani arşivlenen skill küçük bir başlatıcıdır, davranış upstream değiştikçe değişir. Proje klasörü dışına (ev dizinine) yazar. HyperFrames'e alternatif değil, farklı bir motor (kendi render araçları).

### lemo-opuscar@lemomo-ai  ·  lemomo-ai/lemo-opuscar @ bebbbe1  ·  puan 69 (B)

- **Ne yapar:** Aynı Lemo-Opuscar skilinin 'dizin/eklenti paketi' sürümü: kütüphanenin yanında paketlenmiş (library/) gelmesini bekler, ~/.lemo-opuscar'a kopyalar.
- **Ne zaman:** Belirli bir görsel stilde (yağlı boya, suluboya, ukiyo-e, uydu brifingi, ürün parçalama vb.) kodla üretilmiş kısa film, tanıtım, açıklayıcı video; uydu görüntüsü/lazer tarama/CAD/arşiv gibi gerçek malzemeden veri anlatımı; kendi film stilini oluşturma. · **Ne zaman değil:** Doğrudan kurulum: library/ klasörü olmadan çalışmaz; birincil lemo-opuscar'ı kullan.
- **Teknoloji:** node, three.js, ffmpeg, python, kokoro tts · **Paketler:** node, ffmpeg, python3 (seslendirme için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★10618, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** kodla-film-stilleri → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 123 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** Çalışınca kendi kütüphanesini ev dizinine indirir/kopyalar (~/lemo-opuscar veya ~/.lemo-opuscar), Node + ffmpeg (+ seslendirme için Python/Kokoro) ister. Ücretsiz: varsayılan TTS çevrimdışı Kokoro; edge-tts metni Microsoft'a gönderir (sadece kullanıcı onaylarsa).
- **İnceleme:** incelendi · kalite 2/5 — Tek başına ÇALIŞMAZ: beklediği library/ klasörü bu repo yolunda yok (yalnızca paketlenmiş eklenti dağıtımında bulunur). Kurulum için birincil sürüm (lemo-opuscar) kullanılmalı.

### media-use  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videosu için her türlü medyayı tek komutla (`media-use resolve`) bulur ya da üretir: müzik, ses efekti, görsel/ikon/logo, seslendirme, avatar/üretilmiş video, transkript, arka plan silme, renk düzeltme; ayrıca yerleştirilen sesleri miksler. Her ihtiyaç için HeyGen (ücretli, en iyi kalite) ve ücretsiz yerel yolu tablo hâlinde verir.
- **Ne zaman:** Videoya müzik, SFX, seslendirme (Kokoro TTS dahil), avatar, transkript, renk/LUT, yüz gizleme gibi medya eklemek; eski hyperframes-audio işlerinin yerine. · **Ne zaman değil:** HyperFrames dışı projeler; özel bir sağlayıcı (ElevenLabs, Kling…) açıkça istenirse o sağlayıcının kendi skili.
- **Teknoloji:** hyperframes, heygen, ffmpeg, python 3.10+ (kokoro tts) · **Paketler:** node, heygen CLI (BGM/TTS için), ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-medya → birincil · **Roller:** video-kompozisyon, ses-tasarimci, video-kurgu-render · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1860 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Güncellemede ses (hyperframes-audio) bu skile katıldı; ücretli çağrıdan önce onay kuralı ve 'sessizce ekleme, bir kez öner' ilkesi net. HeyGen için heygen CLI + OAuth, ücretsiz yol için yerel modeller gerekir.

### motion-design  ·  nexu-io/open-design @ 987b247  ·  puan 91 (A)

- **Ne yapar:** Apply motion craft to an active task: refine a brief, beat map, visual continuity, typography, pacing, and timeline implementation. Use when planning or improving motion graphics; the host task owns artifact creation, output format, and export.
- **Teknoloji:** api-anahtari, canvas, css, gsap, html, node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli
- **Boyut:** 35 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** otomatik

### oversized-cursor  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasası, uç hedefleme ve tıklama vuruşu, tıklamanın bir sonraki vuruşu ateşlemesi ve sahneler arası çıkış/devir.
- **Ne zaman:** UI sahnesinde imleç/işaretçi eylemi olduğunda veya sahne durağan kaldığında ucuz hareket kaynağı olarak. · **Ne zaman değil:** İmleç içermeyen sahneler; gerçek ekran kaydı (playwright-recording).
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa, kontrol listeli ve UI demo videolarında yüksek getirili.

### playwright-recording  ·  calesthio/OpenMontage @ 195eab2  ·  puan 96 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### provider-refresh-oct23  ·  calesthio/OpenMontage @ 195eab2  ·  puan 100 (A)

- **Ne yapar:** API contracts and production routing for the October 23, 2026 provider refresh.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### remotion  ·  calesthio/OpenMontage @ 195eab2  ·  puan 81 (A)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### remotion-best-practices  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Router for all Remotion skills
- **Teknoloji:** node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 6 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir. · **Kırık bağlantı:** 12
- **İnceleme:** otomatik

### remotion-best-practices@calesthio  ·  calesthio/OpenMontage @ 195eab2  ·  puan 100 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** remotion-cercevesi → birincil · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil.

### remotion-captions  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Transcribing, displaying and animating captions
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-create  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Create a new Remotion video
- **Teknoloji:** git, node, react, remotion, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-docs  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Search Remotion documentation
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-interactivity  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Structure Remotion markup for interactivity
- **Teknoloji:** css, html, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-license  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Find Remotion license information, FAQs, terms, and where to buy a license.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 0.5 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-maps  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Remotion Map animation knowledge
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 477 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-markup  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 87 (A)

- **Ne yapar:** Content, animation and effects best practices
- **Teknoloji:** canvas, css, ffmpeg, html, lottie, node, react, remotion, tailwind, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 123 KB (SKILL.md 13.2 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### remotion-multimedia  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Interacting with Mediabunny
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 0.7 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-render  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Export a Remotion video
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-saas  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Build an app with Remotion
- **Teknoloji:** node, react, remotion, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-studio  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Preview a Remotion video
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-to-hyperframes  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** Başka araçlarla yapılmış video kodunu ya da çıktısını HyperFrames'e alır ve kare kare karşılaştırarak doğrular: Native (Remotion/HTML/GSAP çevirisi), Hosted (canvas, p5, Three.js, Lottie kodunu HyperFrames zamanıyla sürme), Media (Manim, After Effects, Blender çıktısını klip olarak koyma).
- **Ne zaman:** Remotion projesini taşımak; Lottie/Three.js/p5 animasyonlarını ya da Manim/AE renderlarını HyperFrames videosunda kullanmak. · **Ne zaman değil:** Sıfırdan yeni video (hyperframes yeter).
- **Teknoloji:** hyperframes, remotion, react, python · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 164 KB (SKILL.md 4.9 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Güncellemede kapsam Remotion'dan tüm araçlara genişledi (üç seviye modeli); SSIM ile kare kare doğrulama betikleri korunuyor.

### remotion-upgrade  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Upgrade Remotion, and related packages
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★69773, son güncelleme 2026-11-01, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### slideshow  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** HyperFrames ile canlı sunulan slayt gösterisi kurar: her slayt bir sahne, JSON adası ile fragment reveal, dallanan hotspot'lar ve konuşmacı notları; `hyperframes present` ile sunulur; var olan bir sayfayı desteye çevirme kuralları içerir.
- **Ne zaman:** MP4 yerine canlı sunulacak deste/pitch deck; mevcut bir web sayfasını sunuma çevirmek. · **Ne zaman değil:** Render edilmiş video isteniyorsa (hyperframes); PowerPoint dosyası gerekiyorsa (pptx).
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★77137, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** sunum-desteleri → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 48 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede SKILL.md 497 satırdan ~45 satıra indi; kurallar özlü. ttsScript alanları henüz bağlı değil.

### social-reddit-card  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** otomatik

### social-spotify-card  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepages.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### social-x-post-card  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### swiss-user-research-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Swiss-style user-research narrative template in warm-paper editorial aesthetics. Use when users ask for a premium research deck or story-first live artifact with minimalist typography, high-clarity layout, subtle motion, donut breakdowns, and keyboard/click navigation across slides in a single HTML file.
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### synthetic-screen-recording  ·  calesthio/OpenMontage @ 195eab2  ·  puan 88 (A)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### vfx-text-cursor  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### video-download  ·  calesthio/OpenMontage @ 195eab2  ·  puan 97 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  calesthio/OpenMontage @ 195eab2  ·  puan 100 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-hyperframes  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Hyperframes / Remotion-compatible continuous frame animation with autoplay support.
- **Teknoloji:** html, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### video-toolkit  ·  calesthio/OpenMontage @ 195eab2  ·  puan 80 (A)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  calesthio/OpenMontage @ 195eab2  ·  puan 96 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-kurgu-render, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  calesthio/OpenMontage @ 195eab2  ·  puan 97 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★74392, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### weread-year-in-review-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** WeRead-inspired HyperFrames video template for vertical annual reading reports, personal reading dashboards, book-note recaps, and shareable year-in-review stories. Use when users want a 9:16 HTML-to-MP4 reading report with warm paper texture, editorial Chinese typography, book-page metaphors, data highlights, and deterministic motion.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### youtube-downloader  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 70 (B)

- **Ne yapar:** yt-dlp kullanan download_video.py betiğiyle YouTube videosu indirir: kalite (best…360p), format (mp4/webm/mkv) ve yalnızca ses (MP3) seçenekleri; yt-dlp yoksa kendisi kurar.
- **Ne zaman:** Tek bir YouTube videosunu ya da sesini hızlıca indirmek. · **Ne zaman değil:** Varsayılan çıktı yolu /mnt/user-data/outputs/ (claude.ai sandbox'ı) — yerelde -o ile yol ver. Altyazı/transkript, oynatma listesi veya çok platform için OpenMontage video-download (birincil). Telif hakkı korumalı içerikte.
- **Teknoloji:** python, yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78523, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** video-indirme → alternatif
- **Boyut:** 7 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Basit ve çalışır betik; sandbox'a özgü varsayılan yol ve otomatik pip kurulumu eksi. Kategori: video indirme g-video-ses-medya/01 kapsamında, oraya taşındı ve video-indirme grubuna alternatif olarak eklendi.
