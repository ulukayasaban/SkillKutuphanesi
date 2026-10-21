# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **46/46**

### captions-overlay  ·  heygen-com/hyperframes @ 4371981  ·  puan 88 (A)

- **Ne yapar:** embedded-captions iş akışının üzerine uygulanan overlay doktrini: altyazı modeli (at / ray / göm) ve altyazının filme bindirilen bir katman olduğu, içerik yukarı kaydırılarak ayrılmış alt bant olmadığı kuralı; sahneyi altyazı altında gerçek kare merkezine hizalama.
- **Ne zaman:** Konuşan kafa veya lansman videosuna altyazı eklerken; altyazı taşıyacak kompozisyon düzenlenirken. · **Ne zaman değil:** Altyazısız işlerde; embedded-captions olmadan tek başına.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa ve net, embedded-captions ve product-launch-video kurallarını alıntılayarak birleştiriyor.

### changelog-video  ·  heygen-com/hyperframes @ 4371981  ·  puan 71 (B)

- **Ne yapar:** Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka planı, sahte UI görselleştirmeleri ve sakin altyazılar; fontlar, arka plan müziği ve betikler skill içinde paketli.
- **Ne zaman:** Yalnız HeyGen'in kendi haftalık changelog videosu için; kendi markan için örnek/şablon olarak incelenebilir. · **Ne zaman değil:** Kendi ürününün changelog videosunda doğrudan (pr-to-video veya product-launch-video kullan); marka varlıkları HeyGen'e ait.
- **Teknoloji:** hyperframes, html, gsap, node, heygen · **Paketler:** hyperframes (npx), node>=22, ffmpeg, HeyGen hesabı (TTS)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 521 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. HeyGen iç skilli (internal:true): HeyGen marka kimliğine, sabit seslendirmene ve repo köküne bağlı; paketlenen TT Norms Pro / ABC Solar ticari fontlarının yeniden kullanım lisansı belirsiz. Rollere eklenmedi.

### create-video  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-kompozisyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### embedded-captions  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Tek kişilik konuşan kafa videosuna görüntüyü düzenlemeden altyazı ekler: düz birebir altyazı, öznenin arkasına gömülü sinematik altyazı, VFX altyazı veya 35 stillik katalogdan adlı bir kimlik. Varsayılan sakin 'anchor' rayıdır; transkripsiyon ve özne maskeleme dahil uçtan uca yerel çalışır.
- **Ne zaman:** Var olan konuşan kafa videosuna altyazı/sinematik yazı eklenmek istendiğinde. · **Ne zaman değil:** Grafik overlay kartları (talking-head-recut); çok çekimli görüntü (önce bölünmeli); altyazı dosyası (SRT) üretimi yeterliyse.
- **Teknoloji:** hyperframes, html, gsap, ffmpeg, whisper, python · **Paketler:** hyperframes (npx), node>=22, ffmpeg, python3
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 3421 KB (SKILL.md 33.8 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Karar kapısı ve ön kontroller güçlü, DNA stil kayıt defteri zengin; kurulum ağır (özne maskeleme modeli) ve SKILL.md büyük (34 KB). captions-overlay ile birlikte kullanılır. Kardeş skillere (../hyperframes, ../hyperframes-*) bağlantı verir; tek başına kurulursa bağlantılar kırılır, hyperframes çekirdeğiyle birlikte kurulmalı.

### faceless-explainer  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Makale, not, konu veya brief gibi düz metni yüzsüz (faceless) açıklayıcı videoya çevirir: yakalanacak site/görüntü olmadığı için görseller sahne başına tipografi, soyut grafik, diyagram ve veri görselleştirmesiyle icat edilir. Brief→tasarım sistemi→storyboard/senaryo→ses→kare tasarımı→kare yapımı→birleştirme adımları kapılıdır, kareler alt ajanlara dağıtılır.
- **Ne zaman:** Konu anlatımı, kavram açıklaması, nasıl yapılır ve liste videolarında; elde yalnız metin varken. · **Ne zaman değil:** Web sitesinden ürün/tanıtım videosu (product-launch-video); PR anlatımı (pr-to-video); müzik videosu.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 284 KB (SKILL.md 30.5 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Olgun, testli betikler ve kapılı aşamalar; çok ajanlı olduğu için uzun/maliyetli. Bağlam yükü yüksek (30 KB SKILL.md). Kardeş skillere (../hyperframes, ../hyperframes-*) bağlantı verir; tek başına kurulursa bağlantılar kırılır, hyperframes çekirdeğiyle birlikte kurulmalı.

### ffmpeg  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### figma  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** Figma içeriğini HyperFrames kompozisyonuna aktarır: render edilmiş varlıklar, marka token'ları, bileşenler (REST/CLI), bir SECTION içindeki sahne karelerinden hareket kurgusu, bağlayıcı varsa Figma hareketleri ve shader'lar. İki ayrı kimlik bilgisi (token) kapsamını tanımlar.
- **Ne zaman:** Kullanıcı figma.com bağlantısı verdiğinde veya Figma tasarımını/logosunu/animasyonunu videoya getirmek istediğinde. · **Ne zaman değil:** Figma'dan web/uygulama kodu üretmek için (video dışı); Figma erişimi yoksa.
- **Teknoloji:** hyperframes, figma-api, node · **Paketler:** hyperframes (npx), FIGMA_TOKEN
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 11 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Faz faz net akış ve determinizm bölümü iyi; adı genel ama yalnız HyperFrames'e aktarım içindir (Figma→kod değil). Kardeş skillere (../hyperframes, ../hyperframes-*) bağlantı verir; tek başına kurulursa bağlantılar kırılır, hyperframes çekirdeğiyle birlikte kurulmalı.

### general-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Uzmanlaşmış bir iş akışına uymayan özel HyperFrames kompozisyonları için genel iş akışı: uzun veya çok sahneli işler, marka/sizzle reel, montaj, statik döngü ve başlık kartı, mevcut görüntü remiksi; BRIEF.md 'flow: companion' dediğinde eşlikçi akış. Proje durumundan başlar, aşama başına gerekli bilgi skillerini yükletir ve kapıları uygular.
- **Ne zaman:** hyperframes yönlendiricisi başka iş akışı bulamadığında; serbest, çok sahneli kompozisyonlarda. · **Ne zaman değil:** Kısa anlatımsız motion graphic (motion-graphics); web sitesi/PR/metin/müzik/konuşan kafa girdili işler (ilgili özel akış); yönlendirici okunmadan doğrudan.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → birincil · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 36 KB (SKILL.md 21.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İş akışlarının 'her şey dahil' yedeği; kapsamı dar tutma ve tasarımı HTML'den önce kurma kuralları iyi. Kardeş skillere (../hyperframes, ../hyperframes-*) bağlantı verir; tek başına kurulursa bağlantılar kırılır, hyperframes çekirdeğiyle birlikte kurulmalı.

### hyperframes  ·  heygen-com/hyperframes @ 4371981  ·  puan 93 (A)

- **Ne yapar:** HyperFrames ekosisteminin zorunlu giriş noktası: proje durumunu okur, gerekirse niyet görüşmesi yapar, isteği girdi türüne göre tek bir iş akışına (general-video, faceless-explainer, product-launch-video, pr-to-video, music-to-video, motion-graphics, embedded-captions, talking-head-recut, slideshow, remotion-to-hyperframes) yönlendirir ve alan skillerini gerektikçe yükletir. Brief, storyboard, senaryo ve alt ajan sözleşmeleri references/ altındadır.
- **Ne zaman:** Herhangi bir video/animasyon/motion graphic oluşturma, düzenleme veya render isteğinde ilk okunacak skill; mevcut HyperFrames projesini incelerken de. · **Ne zaman değil:** Kullanıcı açıkça Remotion veya başka bir çerçeve istiyorsa; sadece hazır videoyu kesip biçen FFmpeg işlerinde; yalnız tarayıcı oturumu kaydı istendiğinde.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → birincil · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1112 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Ekosistemin yönlendiricisi; rota tablosu ve 'bir kez yönlendir, sonra çık' kuralı net. OpenMontage c806645 kopyasındaki kırık iş akışı yönlendirmeleri bu kaynakla çözüldü. Her oluşturmada 'npx hyperframes usage' ile kota kontrolü ister. Kütüphane kurulumunda HYPERFRAMES_SKIP_SKILLS=1 ayarlanmalı; aksi halde 'npx hyperframes skills update/init' skill setini kendi kurar/günceller.

### hyperframes-animation  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri ve GSAP, Lottie, Three.js, Anime.js, CSS, WAAPI, TypeGPU çalışma zamanı adaptörleri. Tek duraklatılmış, seek-güvenli zaman çizelgesi ilkesine dayanır.
- **Ne zaman:** HyperFrames kompozisyonunda hareket, geçiş veya sahne koreografisi yazarken. · **Ne zaman değil:** HyperFrames dışı web animasyonu (gsap-* veya framer-motion skilleri daha uygun); Remotion projeleri.
- **Teknoloji:** hyperframes, gsap, html, css, lottie, three.js · **Paketler:** hyperframes (npx), gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 2521 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes-animation, heygen-com/hyperframes). Çok zengin kural/blueprint kütüphanesi (2.5 MB); SKILL.md kısa yönlendirici, ayrıntı isteğe bağlı yükleniyor.

### hyperframes-animation@heygen-com-eski  ·  heygen-com/hyperframes @ 25126bc  ·  puan 92 (A)

- **Ne yapar:** HyperFrames için tüm animasyon bilgisi: atomik hareket kuralları, çok fazlı sahne şablonları (blueprint), sahne geçişleri, 24 adlı metin efekti ve GSAP, Lottie, Three.js, Anime.js, CSS, WAAPI, TypeGPU çalışma zamanı adaptörleri. Mevcut kompozisyonun koreografisini denetlemeyi (animation map) de kapsar.
- **Ne zaman:** HyperFrames kompozisyonunda hareket, geçiş veya sahne koreografisi yazarken ya da denetlerken. · **Ne zaman değil:** HyperFrames dışı web animasyonu (gsap-* veya framer-motion); tek bir kamera hareketi/punch-in için (hyperframes-keyframes daha dar).
- **Teknoloji:** hyperframes, gsap, html, css, lottie, three.js · **Paketler:** hyperframes (npx), gsap
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1240 KB (SKILL.md 20.2 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çok zengin kural/blueprint kütüphanesi; SKILL.md kısa yönlendirici, ayrıntı isteğe bağlı yükleniyor.

### hyperframes-audio  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Kompozisyona yerleşmiş sesin miksajı: fade/crossfade, iz kazancı, otomasyon zarfları, seslendirme altında müzik kısma (voiceover carve), EQ/kompresör/limiter/reverb gibi efekt zincirleri ve birden çok izi taşıyan <hf-audio-group> alt miks veriyolu. Belirtiden başlayan teşhis tablosu sunar.
- **Ne zaman:** Müzik seslendirmeyle çakıştığında, ses seviyesi/geçişler kötü olduğunda veya izlere efekt gerektiğinde. · **Ne zaman değil:** Ses bulma/üretme için (media-use); klip zamanlaması ve iz düzeni için (hyperframes-core).
- **Teknoloji:** hyperframes, html, web-audio, node · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-kurgu-render, ses-tasarimci · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 100 KB (SKILL.md 25.9 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Belirti→çözüm yaklaşımı iyi; carve betiği testli. OpenMontage kopyasında yoktu (yeni).

### hyperframes-cli  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** HyperFrames CLI geliştirme döngüsü: init, add, capture, check (lint dahil), snapshot, preview, render (yerel, HeyGen bulut, AWS Lambda, Cloud Run), beats, keyframes, tts, transcribe, remove-background ve sorun giderme. validate/inspect/layout yerine artık 'check' kullanılır.
- **Ne zaman:** HyperFrames projesi kurarken, doğrularken, önizlerken, render alırken veya render hatası ayıklarken. · **Ne zaman değil:** Kompozisyon HTML'inin içeriği için (hyperframes-core); HyperFrames kullanılmayan projelerde.
- **Teknoloji:** hyperframes, node, ffmpeg, aws-lambda, cloud-run · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 120 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik ve ajan dostu. Dikkat: başarılı renderdan sonra ve eksik özellik durumunda varsayılan olarak 'hyperframes feedback' ile herkese açık kanala geri bildirim gönderilmesini ister (telemetri kapatılmadıkça); gizli projelerde kullanıcıya sorulmalı veya telemetri kapatılmalı. Kütüphane kurulumunda HYPERFRAMES_SKIP_SKILLS=1 ayarlanmalı; aksi halde 'npx hyperframes skills update/init' skill setini kendi kurar/günceller.

### hyperframes-cli@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HyperFrames CLI geliştirme döngüsü: init, add, lint, validate, inspect, preview, render, AWS Lambda render ve sorun giderme. Render öncesi lint/validate/inspect zorunluluğunu ve --json kullanımını tanımlar.
- **Ne zaman:** HyperFrames projesi kurarken, doğrularken, önizlerken ve render alırken. · **Ne zaman değil:** Kompozisyon HTML'inin içeriği/sözleşmesi için (hyperframes-core); HyperFrames kullanılmayan projelerde.
- **Teknoloji:** hyperframes, node, ffmpeg, docker, aws-lambda · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 54 KB (SKILL.md 9.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes-cli, heygen-com/hyperframes). Pratik ve ajan dostu. Not: 'init' global skill setini otomatik güncelliyor; kütüphane kuralı gereği bu davranış izlenmeli.

### hyperframes-core  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönettiği medya oynatma ve deterministik render kuralları. Kompozisyon HTML'i yazmadan önce okunur.
- **Ne zaman:** Renderlanabilir bir HyperFrames projesi kurarken veya mevcut kompozisyonu düzenlerken. · **Ne zaman değil:** Sadece hareket tarifi arıyorsan (hyperframes-animation); HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 78 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes-core, heygen-com/hyperframes). Net teknik sözleşme ve referans dizini; diğer alt skillerin temeli.

### hyperframes-core@heygen-com-eski  ·  heygen-com/hyperframes @ 25126bc  ·  puan 92 (A)

- **Ne yapar:** HyperFrames kompozisyon sözleşmesi: data-* zamanlama öznitelikleri, class="clip", izler, alt kompozisyonlar, değişkenler, çerçevenin yönettiği medya oynatma ve deterministik render kuralları; mevcut kompozisyonu düzenleme tarifleri (creator-editing-recipes) de burada.
- **Ne zaman:** Kompozisyon HTML'i yazmadan veya düzenlemeden önce; bölme, kırpma, yeniden zamanlama gibi tekil düzenlemelerde. · **Ne zaman değil:** Sadece hareket tarifi arıyorsan (hyperframes-animation / hyperframes-keyframes); HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → birincil · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 98 KB (SKILL.md 12.6 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Net teknik sözleşme; 'ilk lint hataları' ve sessiz hata listeleri pratik. Diğer alt skillerin temeli.

### hyperframes-creative  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, sese duyarlı görseller ve marka kararları. 'Web sayfası gibi görünen' jenerik çıktıyı önleyen ev stili kurallarını içerir.
- **Ne zaman:** Çok sahneli veya markalı bir HyperFrames videosunun görsel dilini ve ritmini planlarken. · **Ne zaman değil:** Atomik hareket ve geçişler için (hyperframes-animation); tek satırlık düzenlemelerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1000 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes-creative, heygen-com/hyperframes). Çıktı kalitesini en çok etkileyen alt skill; house-style ve video-composition referansları güçlü.

### hyperframes-creative@heygen-com-eski  ·  heygen-com/hyperframes @ 25126bc  ·  puan 93 (A)

- **Ne yapar:** HyperFrames videoları için animasyon dışı yaratıcı yön: frame.md/design.md tasarım spesifikasyonu, palet, tipografi, anlatım, vuruş planı, sese duyarlı görseller ve marka kararları; 25+ hazır frame preset (FRAME.md + altyazı derisi) içerir.
- **Ne zaman:** Çok sahneli veya markalı bir HyperFrames videosunun görsel dilini ve ritmini planlarken. · **Ne zaman değil:** Atomik hareket ve geçişler için (hyperframes-animation); tek satırlık düzenlemelerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1176 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Çıktı kalitesini en çok etkileyen alt skill; frame preset kütüphanesi güçlü.

### hyperframes-keyframes  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Seek-güvenli 2D/3D anahtar kare tarifleri: punch-in/out, zoom, yeniden çerçeveleme, Ken Burns, kamera hareketi, whip/match geçişleri, maske, yol, SVG morph/draw, metin izleri ve 'hyperframes keyframes' teşhis çıktısının okunması.
- **Ne zaman:** Tek bir kamera hareketi, zoom veya maske animasyonu gerektiğinde ya da keyframes teşhisi okunurken. · **Ne zaman değil:** Genel sahne stratejisi, marka tasarımı, medya temini, altyazı veya video planlaması için.
- **Teknoloji:** hyperframes, gsap, css, svg, three.js · **Paketler:** hyperframes (npx), gsap
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 23 KB (SKILL.md 15.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar ve kesin kapsam; CLI kanıtı (proof) ile bitiş kriteri iyi. hyperframes-animation ile tamamlayıcı. Yeni (OpenMontage'da yoktu).

### hyperframes-media  ·  calesthio/OpenMontage @ c806645  ·  puan 78 (B)

- **Ne yapar:** Tek ses motoru (scripts/audio.mjs) ile HyperFrames için TTS (HeyGen/ElevenLabs/Kokoro), arka plan müziği, ses efekti, Whisper transkripsiyonu, arka plan silme ve altyazı/karaoke üretimi. HeyGen anahtarı yoksa yerel/ücretsiz yollara düşer.
- **Ne zaman:** HyperFrames kompozisyonuna seslendirme, müzik, efekt veya kelime zamanlı altyazı eklerken. · **Ne zaman değil:** HyperFrames dışı projelerde; belirli bir sağlayıcının ayrıntılı API'si gerekiyorsa (elevenlabs, lyria vb.).
- **Teknoloji:** hyperframes, node, heygen, elevenlabs, whisper · **Paketler:** node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:ayni
- **Boyut:** 1396 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. HyperFrames HEAD'de ayrı skill olarak kaldırıldı; TTS, transkripsiyon ve arka plan silme media-use (heygen-com/hyperframes) içine taşındı. Eski projeler için arşivde tutuluyor.

### hyperframes-registry  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** HyperFrames kayıt defterindeki ~400 hazır blok ve bileşeni arar, 'hyperframes add' ile kurar ve kompozisyona bağlar; adı geçen bir görünüm/efekt (CRT, glitch, grain, grafik, terminal, harita…) elle yazılmadan önce katalog taranır. Yeni blok/bileşen yazıp üst projeye katkı akışını da anlatır.
- **Ne zaman:** Brief veya storyboard adlandırılmış bir efekt/geçiş/görsel istediğinde, elle yazmadan önce. · **Ne zaman değil:** Katalogda karşılığı olmayan tamamen özel sahnelerde; HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, node · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 83 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 'Önce katalog' kuralı tekrar üretimi azaltır; registry ağ erişimi gerektirir. Repodaki registry/blocks/* SKILL.md'leri bu skill ile kurulan şablonlardır (kütüphanede ayrıca arşivlenmedi).

### hyperframes-registry@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** HyperFrames kayıt defterindeki hazır blok ve bileşenleri 'hyperframes add' ile kurar ve ana kompozisyona bağlar; yeni blok/bileşen yazıp üst projeye katkı akışını da anlatır.
- **Ne zaman:** Hazır grafik/efekt bloklarını (data-chart, grain-overlay…) kompozisyona eklerken. · **Ne zaman değil:** Sıfırdan özel sahne yazarken; HyperFrames dışı projelerde.
- **Teknoloji:** hyperframes, html, node · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-alt-skilleri → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 49 KB (SKILL.md 4.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes-registry, heygen-com/hyperframes). Dar ama net kapsam; registry ağ erişimi gerektirir.

### hyperframes-studio  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** HyperFrames Studio'da bir kişiyle birlikte çalışma kuralları: mesaj gerçekten değişiklik istiyor mu önce anla; yeni film için plan→storyboard→yapım sırası; her sahne alt kompozisyon, tek altyazı izi, iz başına tek öğe türü ve güvenli alanlar.
- **Ne zaman:** Studio/masaüstü uygulamasında kullanıcıyla etkileşimli düzenleme yaparken; zaman çizelgesini okunur düzenlemek gerektiğinde. · **Ne zaman değil:** Tekil düzenleme işleminin nasıl yapılacağı için (hyperframes-core/creator-editing-recipes); Studio kullanılmayan toplu üretimde.
- **Teknoloji:** hyperframes, html · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-alt-skilleri → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, codex:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, davranış odaklı ('değiştirme deme, önce konuş'). Yeni (OpenMontage'da yoktu).

### hyperframes@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** HTML'den video render eden HyperFrames'in giriş ve yönlendirme skill'i: alt skillerin (core, animation, creative, media, cli, registry) haritasını ve 'video yap' isteğini doğru iş akışına yönlendiren tabloyu verir.
- **Ne zaman:** Herhangi bir video/animasyon/motion graphic isteğinde ilk okunacak skill; HyperFrames ile video yazılacaksa. · **Ne zaman değil:** Kullanıcı açıkça Remotion veya başka bir çerçeve istiyorsa; sadece hazır videoyu kesip biçen FFmpeg işlerinde.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 20 KB (SKILL.md 16.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (hyperframes, heygen-com/hyperframes). Ekosistemin yönlendiricisi, iyi yapılandırılmış. Dikkat: /general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions yönlendirmeleri arşivde yok (OpenMontage c806645'te bulunmuyor).

### media-use  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** HyperFrames projesinin medya işletim katmanı: BGM, SFX, görsel, ikon, marka logosu, ses, renk/LUT ihtiyacını tek 'resolve' komutuyla bulup yerelde dondurur ve deftere kaydeder; katalog yetmezse TTS/müzik/görsel modelleriyle üretir; seslendirme, transkripsiyon, altyazı ve arka plan silme için ortak ses motoru sunar; kesme/yeniden çerçeveleme gibi medya işlemlerini yapar.
- **Ne zaman:** Kompozisyona stok/üretilmiş müzik, efekt, görsel, ses veya transkript gerektiğinde; 'görüntü karanlık/sıkıcı/retro olsun' gibi medya geri bildirimlerinde. · **Ne zaman değil:** Yerleşmiş sesin miksajı için (hyperframes-audio); HyperFrames dışı projelerde; HeyGen hesabı olmadan BGM araması (SFX hesapsız çalışır).
- **Teknoloji:** node, heygen, ffmpeg, api-anahtari · **Paketler:** node, heygen CLI (BGM/TTS için), ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** medya-varlik-temini → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1842 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. OpenMontage kopyasına göre çok genişlemiş: hyperframes-media'nın TTS/transkripsiyon/arka plan silme işlevlerini devraldı. HeyGen CLI girişine (OAuth) bağımlı kısımlar var; SFX hesapsız.

### media-use@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** BGM, ses efekti, görsel ve ikon ihtiyacını tek 'resolve' komutuyla HeyGen kataloğunda arayıp indirir, yerelde dondurur ve manifest'e kaydeder; ajana sadece dosya yolunu döndürür.
- **Ne zaman:** Kompozisyona hazır stok müzik, efekt, görsel veya ikon gerektiğinde, bağlamı arama gürültüsüyle doldurmadan. · **Ne zaman değil:** Özgün üretim gerekiyorsa (music, sound-effects, flux); HeyGen anahtarı yoksa katalog araması sınırlı.
- **Teknoloji:** node, heygen, api-anahtari · **Paketler:** node, HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** medya-varlik-temini → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 66 KB (SKILL.md 5.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (media-use, heygen-com/hyperframes). Bağlam dostu tasarım (tek satır çıktı, önbellek). HeyGen kataloğuna bağımlı.

### music-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Bir müzik parçasından vuruşa senkron HyperFrames videosu üretir: parçayı tek analizörle (beatgrid) çözümler, kareleri planlar, her kareyi ayrı alt ajana yaptırır ve render eder. Şarkı sözü videosu, slayt gösterisi veya kinetik tanıtım bu akıştan çıkar.
- **Ne zaman:** Elinde müzik (veya sesinden yararlanılacak video) olan, ritme oturan klip/lyric video isteklerinde. · **Ne zaman değil:** Anlatımlı veya web sitesinden üretilecek videolarda; müziği olmayan işlerde.
- **Teknoloji:** hyperframes, python, html, gsap · **Paketler:** hyperframes (npx), python3, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6053 KB (SKILL.md 15.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (music-to-video, heygen-com/hyperframes). Kapılı (gate) iş akışı ve alt ajan dağıtımı olgun; çok ajanlı olduğu için maliyetli/uzun.

### music-to-video@heygen-com-eski  ·  heygen-com/hyperframes @ 25126bc  ·  puan 84 (A)

- **Ne yapar:** Bir müzik parçasından (ses dosyası, sesi alınacak video veya ruh hali brief'inden üretilen parça) vuruşa senkron video üretir: lyric video, slayt gösterisi veya kinetik tanıtım. Müzik tüm ritmi belirler; kullanıcı görselleri aynı vuruş ızgarasına kesilir, hiç varlık olmadan da tam video çıkar. 80+ hareket primitifi içerir.
- **Ne zaman:** Elinde müzik olan, ritme oturan klip/lyric video isteklerinde. · **Ne zaman değil:** Anlatımlı işler (girdiye uygun diğer akış); müziği olmayan işler.
- **Teknoloji:** hyperframes, html, gsap, node · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6081 KB (SKILL.md 18.6 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kullanıcı onaylı plan adımı ve devam (resume) tablosu olgun; çok ajanlı olduğu için maliyetli/uzun.

### oversized-cursor  ·  heygen-com/hyperframes @ 4371981  ·  puan 88 (A)

- **Ne yapar:** Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasası, uç hedefleme ve tıklama vuruşu, tıklamanın bir sonraki vuruşu ateşlemesi ve sahneler arası çıkış/devir.
- **Ne zaman:** UI sahnesinde imleç/işaretçi eylemi olduğunda veya sahne durağan kaldığında ucuz hareket kaynağı olarak. · **Ne zaman değil:** İmleç içermeyen sahneler; gerçek ekran kaydı (playwright-recording).
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa, kontrol listeli ve UI demo videolarında yüksek getirili.

### playwright-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### pr-to-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** GitHub pull request'ini (URL, owner/repo#N veya 'bu PR') kod değişikliği açıklayıcı videoya çevirir: changelog, özellik duyurusu, hata düzeltmesi veya refactor anlatımı. gh ile diff, commit ve dosyaları deterministik çeker, katkıcı avatarlarıyla jenerik kapanışı kurar.
- **Ne zaman:** Bir PR'ın ne değiştirdiğini video olarak anlatmak istendiğinde. · **Ne zaman değil:** Ürün tanıtımı (product-launch-video); PR'sız konu anlatımı (faceless-explainer).
- **Teknoloji:** hyperframes, html, gsap, node, github-cli · **Paketler:** hyperframes (npx), node>=22, ffmpeg, gh
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 358 KB (SKILL.md 33.3 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Büyük PR'larda sayfalı çekme ve özel repo hatalarını açık ele alıyor. Katkıcı adları/avatarları videoya girer; özel repolarda paylaşmadan önce kontrol edilmeli.

### product-launch-video  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Ürün/pazarlama URL'si, yapıştırılmış senaryo veya brief'ten ürün lansmanı/tanıtım videosu üretir: SaaS tanıtımları, özellik duyuruları, ürün demoları, şirket/uygulama lansmanları ve web sitesi turları. Siteden varlık yakalar, tasarım sistemi çıkarır, storyboard/senaryo/ses ve kareleri kapılı adımlarla kurar.
- **Ne zaman:** Ticari bir URL veya ürünü tanıtma/lanse etme isteğinde; bir web sitesini olduğu gibi gezdiren tur videolarında. · **Ne zaman değil:** Metinden konu anlatımı (faceless-explainer); kod değişikliği anlatımı (pr-to-video); 10 sn altı tek motion graphic.
- **Teknoloji:** hyperframes, html, gsap, node, playwright · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 341 KB (SKILL.md 35.1 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. OpenMontage'daki website-to-video'nun güncel halefi (site turları da buraya yönleniyor). Testli betikler ve yakalama korkulukları güçlü; bağlam yükü yüksek (35 KB).

### remotion  ·  calesthio/OpenMontage @ c806645  ·  puan 71 (B)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### remotion-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 94 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil.

### remotion-to-hyperframes  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** Mevcut bir Remotion (React) kompozisyonunun kaynağını HyperFrames HTML'ine taşır; yalnızca açık taşıma isteğinde, tek yönlü. Eşlenebilen kalıpları çevirir, uyumsuzları işaretler ve SSIM eşikli test korpusuyla çeviriyi doğrular.
- **Ne zaman:** Kullanıcı açıkça Remotion projesini HyperFrames'e taşımak istediğinde. · **Ne zaman değil:** Remotion sadece referans olarak geçiyorsa veya 'Remotion videom gibi bir şey' isteniyorsa (general-video); ters yönde dönüşüm.
- **Teknoloji:** remotion, hyperframes, react, html, gsap · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 170 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar kapsamlı ama disiplinli (SSIM eval). /general-video yönlendirmesi artık arşivde.

### remotion-to-hyperframes@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Mevcut bir Remotion (React) kompozisyonunu HyperFrames HTML'ine taşır; eşlenebilen kalıpları çevirir, useState/useEffect gibi uyumsuz kalıpları işaretler ve SSIM eşikli test korpusuyla çeviriyi doğrular.
- **Ne zaman:** Kullanıcı açıkça Remotion projesini HyperFrames'e taşımak istediğinde. · **Ne zaman değil:** Yeni kompozisyon yazarken veya Remotion sadece referans olarak geçiyorsa; ters yönde dönüşüm.
- **Teknoloji:** remotion, hyperframes, react, html, gsap · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 168 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. OpenMontage'ın eski kopyası; tercih üreticinin güncel sürümü (remotion-to-hyperframes, heygen-com/hyperframes). Dar kapsamlı ama disiplinli (eval zorunlu). /general-video yönlendirmesi arşivde yok.

### slideshow  ·  heygen-com/hyperframes @ 4371981  ·  puan 85 (A)

- **Ne yapar:** HyperFrames ile gezilebilir sunum/pitch deck yazar: ayrık slaytlar, parça parça açılma (fragment), dallanma, hotspot gezinme ve konuşmacı notlu sunum modu; mevcut bir sayfayı desteye çevirebilir. Çıktı render edilmiş MP4 değil, etkileşimli destedir.
- **Ne zaman:** Kullanıcı açıkça sunum, pitch deck veya etkileşimli deste istediğinde. · **Ne zaman değil:** Doğrusal video istendiğinde; kullanıcı slayt istemediyse (önce onay alınmalı); ofis formatı (.pptx) gerektiğinde.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 48 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Şema (SlideshowManifest) ve çalışan örnek net. Bağımsız çalıştırma için geçici harness gerekiyor; kategori sınırında (sunum).

### synthetic-screen-recording  ·  calesthio/OpenMontage @ c806645  ·  puan 78 (B)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### talking-head-recut  ·  heygen-com/hyperframes @ 25126bc  ·  puan 82 (A)

- **Ne yapar:** Mevcut konuşan kafa/röportaj/podcast videosunu transkripte senkron tasarlanmış grafik overlay kartlarıyla paketler: kinetik başlık, lower-third, veri vurgusu, alıntı, yan panel, resim içinde resim; 16:9, 9:16 veya 4:5 tuvalde orijinal klip altta dokunulmadan oynar. Yerel Whisper transkripsiyonu, kart HTML sözleşmesi ve render adımlarını içerir.
- **Ne zaman:** 'Videomu grafiklerle süsle', 'ekran grafikleri ekle' isteklerinde; konuşan kafa videosunu sosyal formata uyarlarken. · **Ne zaman değil:** Düz altyazı (embedded-captions); görüntüyü kesip yeniden kurgulamak (video-edit/ffmpeg).
- **Teknoloji:** hyperframes, html, gsap, ffmpeg, whisper · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 509 KB (SKILL.md 64.0 KB, yük buyuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Ayrıntılı ve kendi kendine yeterli (font, GSAP, stil kütüphanesi paketli; NOTICE.md lisansları belirtiyor). Çok büyük SKILL.md (64 KB) — bağlam yükü yüksek.

### video-download  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-toolkit  ·  calesthio/OpenMontage @ c806645  ·  puan 70 (B)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-kompozisyon-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-kurgu-render, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### website-to-video  ·  calesthio/OpenMontage @ c806645  ·  puan 77 (B)

- **Ne yapar:** Bir web sitesini headless Chrome ile yakalayıp marka varlıklarıyla HyperFrames videosuna (site turu, vitrin, sosyal klip) dönüştüren 7 adımlı, kapılı iş akışı. Varlık denetimi ve 'doğrulamadıklarım' açıklaması zorunludur.
- **Ne zaman:** Portföy/blog/landing sayfasından tanıtım turu veya sosyal medya klibi üretilecekse. · **Ne zaman değil:** Ürün lansman/promosyon videosu, konu anlatımı veya PR videosu (yönlendirdiği skiller arşivde yok).
- **Teknoloji:** hyperframes, html, node, chrome-headless · **Paketler:** hyperframes (npx), node>=22
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-is-akislari → alternatif · **Globalde:** claude:ayni
- **Boyut:** 1541 KB (SKILL.md 11.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. HyperFrames HEAD'de kaldırıldı; site turları ve web sitesinden tanıtım artık product-launch-video'da (heygen-com/hyperframes). Eski projeler için arşivde tutuluyor.
- **Not:** Kırık bağlantılar (SKILL.md, references/step-3-storyboard.md, references/beat-builder-guide.md): ../hyperframes/references/techniques.md ve ../hyperframes/references/html-in-canvas-patterns.md. Bu skill heygen-com/hyperframes v0.7.17'den alınmış eski bir kopya; dosyalar upstream'de hyperframes-animation skilline taşındı: hyperframes-animation/techniques.md ve hyperframes-animation/adapters/html-in-canvas-patterns.md. Skill upstream'de kaldırıldı; site turu ve web sitesinden tanıtım için product-launch-video kullan. Yine de kurulursa hyperframes-animation'ı da ekle ve bu iki dosyayı oradan oku.

### youtube-downloader  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 77 (B)

- **Ne yapar:** yt-dlp kullanan download_video.py betiğiyle YouTube videosu indirir: kalite (best…360p), format (mp4/webm/mkv) ve yalnızca ses (MP3) seçenekleri; yt-dlp yoksa kendisi kurar.
- **Ne zaman:** Tek bir YouTube videosunu ya da sesini hızlıca indirmek. · **Ne zaman değil:** Varsayılan çıktı yolu /mnt/user-data/outputs/ (claude.ai sandbox'ı) — yerelde -o ile yol ver. Altyazı/transkript, oynatma listesi veya çok platform için OpenMontage video-download (birincil). Telif hakkı korumalı içerikte.
- **Teknoloji:** python, yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** video-indirme → alternatif
- **Boyut:** 7 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Basit ve çalışır betik; sandbox'a özgü varsayılan yol ve otomatik pip kurulumu eksi. Kategori: video indirme g-video-ses-medya/01 kapsamında, oraya taşındı ve video-indirme grubuna alternatif olarak eklendi.
