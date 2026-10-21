# 04-scroll-deneyimi — Tasarım ve Ön Yüz

_Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **6/6**

### barba-js  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Barba.js ile çok sayfalı sitelerde SPA benzeri sayfa geçişleri: wrapper/container yapısı, transition hook'ları, view'lar, prefetch ve GSAP ile geçiş animasyonları; proje kurulum ve geçiş üreteci betikleri.
- **Ne zaman:** Statik/çok sayfalı (CMS, Webflow benzeri) sitelerde sayfalar arası animasyonlu geçiş. · **Ne zaman değil:** React/Next/Astro gibi kendi yönlendiricisi olan projeler (View Transitions API veya çatı çözümü daha uygun); geçişin önemsiz olduğu sayfalar.
- **Teknoloji:** barba 2, gsap 3.15 · **Paketler:** @barba/core, gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** sayfa-gecisi → birincil · **Roller:** scroll-deneyim
- **Boyut:** 129 KB (SKILL.md 19.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. @barba/core v2 API'si hâlâ geçerli; ama native View Transitions API (artık tüm büyük tarayıcılarda) alternatifinden bahsetmiyor ve Locomotive v4 entegrasyonu eski. 129 KB.

### gsap-scrolltrigger  ·  greensock/gsap-skills @ aed9cfd  ·  puan 95 (A)

- **Ne yapar:** Resmî GSAP ScrollTrigger skilli: scroll'a bağlı animasyon, pin, scrub, start/end, toggleActions, batch, matchMedia, React'te useGSAP ile temizlik, refresh ve smooth scroll (ScrollSmoother/Lenis) ile birlikte kullanım.
- **Ne zaman:** Scroll ile tetiklenen veya scroll'a bağlı (scrub) animasyon, pinlenen bölümler, parallax, yatay kaydırma bölümleri. · **Ne zaman değil:** Sadece görünür olunca basit fade (CSS scroll-driven animation veya IntersectionObserver yeter).
- **Teknoloji:** gsap 3.15, scrolltrigger, lenis 1.3 · **Paketler:** gsap, @gsap/react (React)
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★16829, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-deneyimi → birincil · **Roller:** scroll-deneyim, motion-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 18 KB (SKILL.md 18.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). scroll-deneyimi grubunun birincili: resmî, güncel, kısa (18 KB) ve kütüphane seviyesinde varsayılan. freshtechbro kopyası daha uzun ama eski; locomotive v4 entegrasyonu içeriyor. OpenMontage kopyası birebir aynı.

### gsap-scrolltrigger@freshtechbro  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** GSAP tween/timeline temelleri ile ScrollTrigger'ı tek skillde anlatan kapsamlı rehber: pin, scrub, parallax, yatay kaydırma, batch, Three.js ve React entegrasyonu, görüntü dizisi scrub'ı, easing görselleştirici ve başlangıç projesi.
- **Ne zaman:** Tek dosyada hem GSAP temeli hem ScrollTrigger örnek koleksiyonu istendiğinde; görüntü dizisi (image sequence) scrub örneği için. · **Ne zaman değil:** Normalde: resmî gsap-scrolltrigger + gsap-core daha güncel ve doğru; Locomotive Scroll entegrasyon bölümü eski v4 API'sine dayanıyor.
- **Teknoloji:** gsap 3.15, scrolltrigger, three.js, react · **Paketler:** gsap, @gsap/react
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** scroll-deneyimi → alternatif · **Globalde:** claude:farkli
- **Boyut:** 159 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Örnek zengin ama resmî skillerle örtüşüyor; 159 KB, freshtechbro 2025-11'den beri güncellenmedi.

### locomotive-scroll  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Locomotive Scroll ile smooth scroll, data-scroll öznitelikleriyle parallax ve görünürlük tespiti, ScrollTrigger entegrasyonu; yapılandırma ve entegrasyon yardımcı betikleri, Vite başlangıç projesi.
- **Ne zaman:** Projede Locomotive Scroll v4 zaten kullanılıyorsa bakım için. · **Ne zaman değil:** Yeni projeler: Lenis (gsap-scrolltrigger ve scroll-craft içinde anlatılıyor) tercih edilmeli; Locomotive v5 Lenis tabanlı ve API'si farklı.
- **Teknoloji:** locomotive-scroll 4, gsap 3.15 · **Paketler:** locomotive-scroll@4
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-deneyimi → alternatif
- **Boyut:** 81 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Eski v4 API'si (data-scroll-container, scrollerProxy); başlangıç projesi ^4.1.4. Locomotive Scroll v5 (Lenis üzerine) bu kalıpları değiştirdi; native scroll'u ele geçiren v4 yaklaşımı sticky/erişilebilirlik sorunları çıkarır.
- **Not:** Locomotive v4 API; yeni projede Lenis + ScrollTrigger kullan.

### scroll-craft  ·  nateherkai/scroll-craft @ 75d81f7  ·  puan 80 (A)

- **Ne yapar:** Hizmet, ürün, yiyecek-içecek markaları için premium scroll odaklı landing page üreten uçtan uca iş akışı: brief röportajı, sayfa grameri, müşteri yolculuğu ve duygu eğrisi, imza hareketi, katmanlı (çok düzlemli) hero, kendi scroll motoru (scrollcraft.js/css) ve masaüstü/mobil/reduced-motion ekran görüntüsüyle doğrulama. İsteğe bağlı olarak kie.ai ile fotogerçekçi görsel/video üretir.
- **Ne zaman:** 'Deneyim gibi' hissettiren, şablon görünmeyen scroll hikâyesi/kampanya sitesi sıfırdan kurulurken; sanat yönetimi + uygulama + görsel doğrulama birlikte isteniyorsa. · **Ne zaman değil:** Var olan React/Next projesine birkaç scroll animasyonu eklemek (gsap-scrolltrigger); uzun içerikli doküman/uygulama ekranları; Node ve Chrome/Chromium yoksa doğrulama betikleri çalışmaz.
- **Teknoloji:** html, css, javascript, node, chromium, kie.ai · **Paketler:** node, Chrome/Edge/Chromium, ffmpeg (encode.sh), KIE_AI_API_KEY (isteğe bağlı, görsel üretimi)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** nateherkai (kisi, ★3806, son güncelleme 2026-09-30, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-deneyimi → tamamlayıcı · **Roller:** scroll-deneyim
- **Boyut:** 380 KB (SKILL.md 24.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Site seviyesinde sanat yönetimi ve doğrulama; ScrollTrigger'ın yerine değil üstüne gelir (kendi hafif motorunu kullanır). Aktif (0.3.1, 2026-09-30; serve.mjs varsayılan 127.0.0.1). Dikkat: kie.mjs görsel üretimi için api.kie.ai'ye istek atar ve KIE_AI_API_KEY ister (ücretli); 24 KB SKILL.md + çok sayıda referans, bağlam yükü yüksek.

### scroll-reveal-libraries  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** AOS (Animate On Scroll) ile data-aos öznitelikleri üzerinden basit fade/slide/zoom scroll açılış animasyonları; animasyon kataloğu ve yapılandırma üreteci betikleri.
- **Ne zaman:** Projede AOS zaten varsa veya derleme adımı olmayan çok basit statik sayfada hızlı açılış efekti. · **Ne zaman değil:** Yeni projeler: CSS scroll-driven animations (animation-timeline: view()) veya IntersectionObserver + CSS, ya da gsap-scrolltrigger batch daha güncel ve hafif.
- **Teknoloji:** aos, css · **Paketler:** aos@next
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-deneyimi → alternatif
- **Boyut:** 94 KB (SKILL.md 16.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. AOS uzun süredir bakımsız (aos@next hâlâ beta); skill native CSS scroll-driven animation seçeneğinden hiç bahsetmiyor.
