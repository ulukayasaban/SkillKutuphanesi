# 04-scroll-deneyimi — Tasarım ve Ön Yüz

_Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **6/7**

### barba-js  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** Barba.js ile çok sayfalı sitelerde sayfalar arası geçiş animasyonu: hook'lar, router/prefetch/head eklentileri, GSAP entegrasyonu, geçiş kalıpları ve proje kurulum betikleri.
- **Ne zaman:** SPA hissi veren sayfa geçişleri (ör. perde/fade) çok sayfalı statik sitelerde. · **Ne zaman değil:** React/Next.js router geçişleri (framework'ün kendi çözümü); tek sayfalık siteler.
- **Teknoloji:** barba 2, gsap 3.15 · **Paketler:** @barba/core, @barba/prefetch, @barba/router
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1248, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** sayfa-gecisi → birincil · **Roller:** scroll-deneyim
- **Boyut:** 129 KB (SKILL.md 19.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Konusunda tek skill, kapsamlı (19 KB); 'scroll' kategorisine sınırda oturuyor ama sayfa geçişi scroll sıfırlama ve ScrollTrigger yenileme ile iç içe. Dikkat: bundan sonra ScrollTrigger kill/refresh unutulursa sızıntı olur; 335 gün eski.

### gsap-scrolltrigger  ·  greensock/gsap-skills @ aed9cfd  ·  puan 86 (A)

- **Ne yapar:** GSAP ScrollTrigger resmî rehberi: scroll'a bağlı animasyon, pinleme, scrub, tetikleyiciler, refresh ve temizlik. Parallax, pinli bölüm ve scroll hikayeleri için varsayılan seçimdir.
- **Ne zaman:** Scroll'a bağlı animasyon, pinli bölüm, parallax, scrub gerektiğinde (özellikle kütüphane belirtilmemişse). · **Ne zaman değil:** Basit fade-in reveal (scroll-reveal-libraries yeter).
- **Teknoloji:** gsap 3.15, scrolltrigger, lenis 1.3 · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** greensock (kurum, resmî, ★17884, son güncelleme 2026-07-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-animasyonu → birincil · **Roller:** scroll-deneyim, motion-gelistirici
- **Boyut:** 18 KB (SKILL.md 18.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmî, güncel (18 KB), pin/scrub/cleanup kuralları doğru; gsap-core ile birlikte kullanılmalı. Dikkat: yok.

### gsap-scrolltrigger@freshtechbro  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** GSAP ve ScrollTrigger için kapsamlı (765 satır) genel rehber: tween, timeline, ScrollTrigger, kalıplar, ease referansı, başlangıç projesi ve üretici betikler (generate_animation.py, timeline_builder.py).
- **Ne zaman:** Resmî sürümün yetmediği, başlangıç projesi/ease görselleştirici gibi ek varlıklar istendiğinde. · **Ne zaman değil:** Normal durumda resmî gsap-scrolltrigger + gsap-core/timeline.
- **Teknoloji:** gsap 3.15, scrolltrigger, three.js, react · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1248, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** scroll-animasyonu → alternatif · **Roller:** scroll-deneyim
- **Boyut:** 159 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Aynı ad, farklı içerik: resmî sürüm yalnız ScrollTrigger'a odaklı ve güncel; bu sürüm tween+timeline+ScrollTrigger'ı tek dosyada jenerik anlatıyor, 335 gün eski, resmî rehberlerde olan matchMedia/cleanup disiplininden yoksun. Betikler yerel kod üretici, risk yok.

### gsap-scrolltrigger@nexu-io  ·  nexu-io/open-design @ 987b247  ·  puan 95 (A)

- **Ne yapar:** Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or when the user asks about ScrollTrigger, scroll animations, or pinning. Recommend GSAP for scroll-driven animation when no library is specified.
- **Teknoloji:** gsap, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 20 KB (SKILL.md 18.6 KB, yük orta)
- **İnceleme:** otomatik

### locomotive-scroll  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** Locomotive Scroll ile yumuşak (smooth) kaydırma, parallax ve viewport algılama; GSAP ScrollTrigger entegrasyon notları ve başlangıç projesi.
- **Ne zaman:** Smooth-scroll + parallax içeren sürükleyici sitelerde (kategorideki tek smooth-scroll skill'i). · **Ne zaman değil:** Erişilebilirlik/mobil önceliği olan siteler; ScrollTrigger tek başına yeterliyse.
- **Teknoloji:** locomotive-scroll 4, gsap 3.15 · **Paketler:** locomotive-scroll
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1248, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** yumusak-kaydirma → birincil · **Roller:** scroll-deneyim
- **Boyut:** 81 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kategoride smooth-scroll için tek seçenek. Dikkat: v4 tarzı API ('el', 'data-scroll-container'); v5 Lenis tabanlı ve API farklı; Lenis için ayrı skill yok. Smooth-scroll mobil ve reduced-motion'da kapatılmalı.
- **Not:** Locomotive v4 API; yeni projede Lenis + ScrollTrigger kullan.

### scroll-craft  ·  nateherkai/scroll-craft @ 75d81f7  ·  puan 78 (B)

- **Ne yapar:** Premium scroll-driven landing page üretir: brief/röportaj, sayfa grameri, duygu eğrisi, 'imza hamle', çok katmanlı (dimensional) hero, kendi scrollcraft.js motoru ve ekran görüntüsüyle masaüstü/mobil/reduced-motion doğrulaması. Varlıkları kie.ai ile üretebilir.
- **Ne zaman:** Hizmet/ürün/yiyecek markaları için sinematik, katmanlı hero'lu, 'şablon gibi görünmeyen' scroll hikaye sitesi kurarken. · **Ne zaman değil:** Küçük scroll efekti eklemek; GSAP ScrollTrigger'a bağlı mevcut proje; dashboard/uygulama arayüzleri.
- **Teknoloji:** html, css, javascript, node, chromium, kie.ai · **Paketler:** playwright-core, ffmpeg (tam sürüm), KIE_AI_API_KEY (isteğe bağlı)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** nateherkai (kisi, ★4529, son güncelleme 2026-09-30, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-hikaye-uretimi → birincil · **Roller:** scroll-deneyim
- **Boyut:** 380 KB (SKILL.md 24.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güçlü süreç (brief, çeşitlilik kapısı, doğrulama), güncel (21 gün) ve MIT; büyük ama gerçek bir uçtan uca sistem. Dikkat: SKILL.md 24 KB + ~170 KB referans; GSAP değil kendi motorunu kullanıyor; varlık üretimi kie.ai API anahtarı ister ve api.kie.ai'ye istek atar (isteğe bağlı); tam ffmpeg ve playwright-core gerekir; serve.mjs varsayılan 127.0.0.1 (--lan açık uyarılı); 'Windows/OtherWorlds' yol örnekleri taşıyor.

### scroll-reveal-libraries  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** AOS (Animate On Scroll) ile basit scroll reveal animasyonları: data-aos öznitelikleri, yerleşik animasyonlar, özel animasyon, karşılaştırma tablosu ve yapılandırma betikleri.
- **Ne zaman:** Pazarlama sayfasında karmaşıklık olmadan fade/slide reveal gerektiğinde. · **Ne zaman değil:** Pin, scrub, timeline; React'te animasyon (motion-framer).
- **Teknoloji:** aos, css · **Paketler:** aos
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1248, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** scroll-animasyonu → alternatif
- **Boyut:** 94 KB (SKILL.md 16.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İşini yapıyor ama 820 satır (17 KB) AOS için fazla ve kütüphane yıllardır durağan; 'aos@next' kullanıyor. Dikkat: reveal için CSS/IntersectionObserver veya ScrollTrigger yeterli; unpkg CDN örnekleri.
