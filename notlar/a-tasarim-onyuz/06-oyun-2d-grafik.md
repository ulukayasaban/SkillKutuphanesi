# 06-oyun-2d-grafik — Tasarım ve Ön Yüz

_Oyun geliştirme, PixiJS, 2D grafik_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **12/12**

### 2d-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** 2D oyun ilkeleri: sprite atlas ve animasyon, tilemap katmanları, 2D fizik şekilleri, kamera tipleri ve ekran sarsıntısı, platformer (coyote time, jump buffer) ve top-down kalıpları.
- **Ne zaman:** 2D oyun mekaniği, sprite/tilemap ve kamera kararlarında hızlı hatırlatma. · **Ne zaman değil:** Motorun gerçek API'si veya render kodu için değil; PixiJS için pixijs-2d.
- **Teknoloji:** 2d, sprite, tilemap
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. 2.1 KB'lık özlü kontrol listesi; faydalı ama sığ (tablolar, kod yok). Dikkat: SKILL.md `game-development/2d-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### 3d-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** 3D oyun ilkeleri: render hattı aşamaları, culling/LOD/batching, shader türleri ve ne zaman özel shader yazılır, 3D çarpışma şekilleri, kamera tipleri, ışık türleri ve LOD stratejisi.
- **Ne zaman:** 3D oyun performans ve kamera kararlarında kısa hatırlatma. · **Ne zaman değil:** Three.js/WebGL kodu için threejs-* skill'leri; derin render bilgisi için değil.
- **Teknoloji:** 3d, shader, lod
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. En sığ olanlardan (2.5 KB): ders kitabı özeti, uygulanabilir yönerge yok; threejs-* skill'leri 3D tarafında çok daha somut. Dikkat: SKILL.md `game-development/3d-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-art  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun sanatı ilkeleri: sanat stili karar ağacı (pixel, vektör, el boyaması, PBR, low-poly, cel-shaded) ve karşılaştırma matrisi, 2D/3D varlık hattı araç seçenekleri, renk kararları, 12 animasyon ilkesi, çözünürlük ve adlandırma/klasör düzeni.
- **Ne zaman:** Oyunun görsel stilini seçerken ve varlık hattı/adlandırma standardı kurarken. · **Ne zaman değil:** Gerçek sprite/model üretimi için değil (üretim yapmaz, karar çerçevesi verir).
- **Teknoloji:** pixel-art, blender, aseprite
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Stil karar ağacı ve adlandırma düzeni gerçekten işe yarar (4.9 KB), ama sığ bir çerçeve. Dikkat: SKILL.md `game-development/game-art/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-audio  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun sesi ilkeleri: ses kategorileri ve öncelik hiyerarşisi, SFX katmanlama, müzik durum sistemi ve geçiş teknikleri, uyarlanabilir (vertical/horizontal) ses, 3D konumlandırma, platform formatları, mix seviyeleri ve ducking kuralları.
- **Ne zaman:** Oyunda ses mimarisi ve mix dengesi kararlarında. · **Ne zaman değil:** Ses üretmek için değil (elevenlabs/music skill'leri); motora özel ses API'si için değil.
- **Teknoloji:** web-audio, fmod, wwise
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Mix seviyeleri ve ducking tabloları somut (5.2 KB); yine de ilke düzeyinde. Dikkat: SKILL.md `game-development/game-audio/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-design  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun tasarımı ilkeleri: 30 saniyelik çekirdek döngü, GDD bölümleri, oyuncu motivasyon tipleri ve ödül takvimleri, zorluk dengeleme (flow), ilerleme türleri ve tempo.
- **Ne zaman:** GDD yazarken ve çekirdek döngü/zorluk kararlarında. · **Ne zaman değil:** Seviye tasarımı, hikâye veya ekonomi dengeleme derinliği için değil.
- **Teknoloji:** gdd, game-design
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa (2.6 KB) ve sağlam temel, fakat tamamı genel geçer maddeler. Dikkat: SKILL.md `game-development/game-design/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### game-development  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oyun geliştirme orkestratörü: oyun döngüsü (sabit zaman adımı), desen seçim matrisi (state machine, pooling, ECS), girdi soyutlama, 60 FPS bütçesi, AI ve çarpışma stratejisi gibi platformdan bağımsız ilkeleri verir ve platforma/boyuta göre 10 alt skill'e (web, mobil, PC, VR/AR, 2D, 3D, tasarım, multiplayer, sanat, ses) yönlendirir.
- **Ne zaman:** Hangi motor/platformla olursa olsun oyun projesine başlarken ilke ve yönlendirme için; alt skill'lerin hepsi tek klasörde gelir. · **Ne zaman değil:** Somut motor/API kodu aramak için değil (içerik ilke ve tablo düzeyinde). Sadece web 2D render kodu için pixijs-2d, 3D web için threejs-* skill'leri.
- **Teknoloji:** game-design, unity, godot, unreal, phaser
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → birincil
- **Boyut:** 35 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kütüphanedeki tek oyun giriş noktası; kısa (4.7 KB) ve alt skill'leri iç içe taşıyor (10 alt klasör, byte aynı). Dikkat: içerik genel ilke tablolarından ibaret, kod/motor özelliği yok; kalite orta. Yönlendirme `game-development/web-games` gibi iç içe yollara dayanır ve alt klasörler ayrı skill olarak otomatik keşfedilmez; ajan o dosyaları açıkça okumalı. Uygun rol yok (oyun rolü tanımlı değil), role eklenmedi.

### mobile-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Mobil oyun ilkeleri: dokunmatik girdi (44pt hedef), pil/ısıl yönetim, performans hedefleri, App Store / Google Play gereklilikleri ve para kazanma modelleri.
- **Ne zaman:** iOS/Android oyun kısıtlarını ve mağaza gerekliliklerini hatırlamak için. · **Ne zaman değil:** Motor veya SDK entegrasyonu için değil.
- **Teknoloji:** ios, android, touch
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa (2.2 KB) kontrol listesi; mağaza gereksinimleri tarih bağımlı ve hızla eskir. Dikkat: SKILL.md `game-development/mobile-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### multiplayer  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Çok oyunculu ilkeleri: mimari seçimi (dedicated, P2P, host), durum/girdi senkronizasyonu, tahmin-enterpolasyon-uzlaştırma ve lag compensation, bant genişliği azaltma, sunucu otoritesi ve hile önleme, eşleştirme.
- **Ne zaman:** Ağ mimarisi ve senkronizasyon stratejisi kararlarında. · **Ne zaman değil:** Belirli ağ kütüphanesi (Photon, Colyseus, Netcode) kullanımı için değil.
- **Teknoloji:** networking, websocket
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. 'İstemciye güvenme' ilkesini ve teknik adları doğru sıralıyor (2.7 KB); uygulama ayrıntısı yok. Dikkat: SKILL.md `game-development/multiplayer/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### pc-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** PC/konsol oyun ilkeleri: motor seçimi (Unity 6, Godot 4, Unreal 5) karar ağacı ve karşılaştırması, Steam özellikleri, konsol sertifikasyonu, kontrolcü girdi soyutlama, profilleme araçları ve motora özel ipuçları.
- **Ne zaman:** PC/konsol için motor seçerken ve platform özelliklerini planlarken. · **Ne zaman değil:** Web oyunları için web-games; motor içi kodlama için değil.
- **Teknoloji:** unity, godot, unreal, steam
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Motor karşılaştırma tablosu işe yarar (2.9 KB) ancak lisans/ücret bilgisi tarih bağımlı ve eskimiş olabilir. Dikkat: SKILL.md `game-development/pc-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### pixijs-2d  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 73 (B)

- **Ne yapar:** PixiJS v8 ile 2D WebGL/WebGPU render rehberi: Application, sprite/texture, Graphics API, ParticleContainer ile on binlerce parçacık, filtreler ve özel shader filtreleri, sprite sheet animasyonu, metin ve performans kalıpları. Başlangıç şablonu, parçacık/sprite üretici betikler ve referans belgeleri içerir.
- **Ne zaman:** Tarayıcıda 2D oyun, parçacık efekti, yoğun sprite sahnesi veya 3D sahne üstü HUD yapılırken. · **Ne zaman değil:** 3D için Three.js/R3F; basit UI animasyonu için GSAP/Motion; tam oyun motoru (fizik, sahne yönetimi) gerekiyorsa Phaser.
- **Teknoloji:** pixi.js, webgl, webgpu, javascript · **Paketler:** pixi.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** pixijs-2d-render → birincil
- **Boyut:** 253 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kütüphanedeki tek somut 2D render rehberi; v8 API'si (async `app.init`, `Graphics.rect().fill()`, `Particle`) doğru ve kod örnekleri çalışır düzende. Dikkat: büyük (20.6 KB SKILL.md, 935 satır; klasör 280 KB). Şablon ve betikler PixiJS'i sürümsüz `https://pixijs.download/release/pixi.js` CDN adresinden yüklüyor (sürüm sabitlenmemiş). 'Related Skills' bölümü var olmayan adlara (threejs-webgl, motion-framer) başvuruyor. Son güncelleme 335 gün önce. Betikler yalnız stdlib python, HTML/JS şablonu üretir; kurulum/anahtar yok. Oyun rolü olmadığı için role eklenmedi.

### vr-ar  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** VR/AR ilkeleri: platformlar (Quest, PCVR, WebXR, ARKit/ARCore), hareket hastalığı önleme ve konfor ayarları, kare hızı hedefleri, kontrolcü/el takibi etkileşimi, ölçek ve derinlik ipuçları.
- **Ne zaman:** VR/AR projesinde konfor ve performans hedeflerini belirlerken. · **Ne zaman değil:** WebXR kodu için aframe-webxr (05); cihaza özel SDK için değil.
- **Teknoloji:** webxr, quest, arkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. İlkeler doğru ama çok kısa (2.3 KB); cihaz metrikleri hızla eskir. Başlık 2D grafik kategorisine uymuyor (VR/AR 3D) ama oyun ailesi için kalabilir. Dikkat: SKILL.md `game-development/vr-ar/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.

### web-games  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Tarayıcı oyunu ilkeleri: çatı seçimi (Phaser, PixiJS, Three.js, Babylon.js), WebGPU benimseme durumu, tarayıcı kısıtları ve optimizasyon sırası, varlık sıkıştırma (KTX2, Draco, Opus), PWA ve Web Audio kuralları.
- **Ne zaman:** Web tabanlı oyun için çatı ve varlık/performans stratejisi seçerken. · **Ne zaman değil:** Kod örneği arıyorsan değil; PixiJS için pixijs-2d, 3D için threejs-*.
- **Teknoloji:** phaser, pixi.js, three.js, webgpu, pwa
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** oyun-gelistirme-rehberi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Web oyunu için en uygulanabilir ilke seti (3.0 KB); tarayıcı destek yüzdeleri (~%73 WebGPU) tarih bağımlı. Dikkat: SKILL.md `game-development/web-games/SKILL.md` ile birebir aynı (diff doğrulandı); game-development kurulursa zaten gelir, ayrıca kurmak gereksiz.
