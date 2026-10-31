# 05-3d-webgl — Tasarım ve Ön Yüz

_Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **35/35**

### aframe-webxr  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 63 (C)

- **Ne yapar:** A-Frame ile HTML tabanlı WebXR/VR/AR deneyimleri: entity-component yapısı, sahne, kameralar, ışık, animasyon, özel bileşenler, VR kontrolcü etkileşimi, 360° galeri; sahne/bileşen betikleri ve başlangıç projesi.
- **Ne zaman:** VR/AR/360° içerik, az JavaScript ile immersif sayfalar. · **Ne zaman değil:** Klasik masaüstü 3D sayfalar; yüksek performanslı oyunlar.
- **Teknoloji:** aframe 1.7, webxr, three.js · **Paketler:** aframe
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** webxr-aframe → birincil
- **Boyut:** 176 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş). WebXR için tek kaynak. Dikkat: SKILL.md CDN script'lerine (jsdelivr, cdnjs) bağlanıyor; 335 gün eski, 26.7 KB.

### babylonjs-engine  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 63 (C)

- **Ne yapar:** Babylon.js 3D motoru: engine/sahne başlatma, kameralar, ışık, mesh, materyaller, model yükleme, fizik (Havok), animasyon; sahne ve mesh üreten betikler, Vite başlangıç projesi.
- **Ne zaman:** Three.js dışında tam özellikli motor (fizik, GUI, editör) gereken oyun/görselleştirme projeleri. · **Ne zaman değil:** Standart Three.js/R3F işleri; hafif dekoratif efekt.
- **Teknoloji:** babylonjs 7, webgl2, webgpu, havok · **Paketler:** @babylonjs/core, @babylonjs/loaders, @babylonjs/gui, @babylonjs/havok
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** babylon-motoru → birincil
- **Boyut:** 153 KB (SKILL.md 30.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş). Başka skill Babylon.js'i kapsamıyor; içerik düzenli ve hacimli. Dikkat: 30 KB (en büyük freshtechbro skilli); 335 gün eski; scene_generator.py yalnız npm komutu yazdırır.

### blender-web-pipeline  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Blender'dan web için glTF/GLB dışa aktarma: bpy betikleri, toplu işleme, LOD üretimi, model optimizasyonu, Three.js/Babylon.js için hazırlama.
- **Ne zaman:** Blender'da hazırlanan modelleri web'e aktarırken otomasyon. · **Ne zaman değil:** Blender kurulu değilse; yalnız küçültme için threejs-asset-pipeline.
- **Teknoloji:** blender 4, bpy, gltf 2.0, python · **Paketler:** Blender (bpy)
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dcc-3d-aktarim → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 27 KB (SKILL.md 16.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Blender tarafı için tek kaynak, betikler yararlı. Dikkat: Blender kurulu olmalı; scripts/ içeriği bpy ile yerel dosya yazar, ağ çağrısı yok; 335 gün eski.

### lightweight-3d-effects  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 64 (C)

- **Ne yapar:** Zdog (sözde-3D vektör çizimler), Vanta.js (animasyonlu 3D arka planlar) ve Vanilla-Tilt (paralaks eğim) ile hafif dekoratif 3D efektler; kurulum ve efekt üretici betikler.
- **Ne zaman:** Hero arka planı, dekoratif 3D illüstrasyon, kart tilt efekti; ağır framework istemeyen sayfalar. · **Ne zaman değil:** Gerçek 3D sahne/model (Three.js skilleri); erişilebilirlik kritikse sürekli hareket.
- **Teknoloji:** zdog, vanta, vanilla-tilt, three.js · **Paketler:** zdog, vanta, vanilla-tilt, three
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hafif-3d-efekt → birincil · **Roller:** ui-tasarimci
- **Boyut:** 179 KB (SKILL.md 22.3 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş). Hafif efekt için tek kaynak. Dikkat: kırık bağlantı 'illo' yanlış alarm (JS değişkeni, dosya değil); örnekler CDN'den eski three@0.134 ve vanta@0.5 yüklüyor; reduced-motion uyarısı yok.

### playcanvas-engine  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** PlayCanvas motoru: Application, entity-component sistemi, güncelleme döngüsü, glTF, materyal, fizik, özel script ve girdi; hazır başlangıç projesi (kamera/girdi script'leri) içerir.
- **Ne zaman:** Hafif WebGL/WebGPU oyun motoru ve PlayCanvas editörüyle çalışan projeler. · **Ne zaman değil:** Three.js/R3F tabanlı projeler.
- **Teknoloji:** playcanvas 2, webgl2, webgpu · **Paketler:** playcanvas
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** playcanvas-motoru → birincil
- **Boyut:** 183 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş). Ayrı bir motor için tek kaynak. Dikkat: 335 gün eski; starter README'si terser/vercel gibi küresel npm kurulumu öneriyor (otomatik çalışmaz).

### react-three-fiber  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** React Three Fiber ile deklaratif 3D sahne: Canvas, useFrame/useThree/useLoader, etkileşimli nesneler, glTF yükleme; sahne/bileşen üreten betikler ve Vite başlangıç projesi içerir.
- **Ne zaman:** Hazır R3F başlangıç projesi ve bileşen üretici betik isteniyorsa; R3F v8/React 18 projeleri. · **Ne zaman değil:** Güncel R3F+drei bilgisi için threejs-react-three-fiber.
- **Teknoloji:** R3F v8, drei 9, three r172, react 18 · **Paketler:** three, @react-three/fiber, @react-three/drei
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** r3f → alternatif
- **Boyut:** 105 KB (SKILL.md 22.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İçerik makul ve başlangıç şablonu işe yarar, ancak CloudAI-X sürümü daha güncel (WebGPU/TSL, Common Mistakes). Dikkat: starter package.json R3F ^8.18 / three ^0.172 sabitler; React 19 için R3F v9 gerekir. npm install adımları şablon README'sinde.

### shader-dev  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** GLSL shader techniques for ray marching, fluid simulation, particle systems, and procedural generation. Useful for hero visuals and motion stills.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### spline-interactive  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Spline: tarayıcı tabanlı görsel 3D tasarım aracı; sahneyi React/web'e @splinetool/react-spline ile gömme, olay yönetimi, nesne kontrolü ve durum tabanlı animasyon; proje/bileşen üretici betikler.
- **Ne zaman:** Kodsuz tasarlanmış 3D sahneyi siteye gömmek; tasarımcı odaklı hızlı prototip. · **Ne zaman değil:** Kod ile tam kontrollü sahne; Spline hesabı/dosyası yoksa.
- **Teknoloji:** spline, react · **Paketler:** @splinetool/react-spline, @splinetool/runtime
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** spline-gorsel-editor → birincil
- **Boyut:** 54 KB (SKILL.md 19.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş). Hızlı landing page 3D'si için pratik. Dikkat: Spline hesabı ve sahne URL'i gerekir (üçüncü taraf barındırma); ağır runtime paketi; 335 gün eski.

### substance-3d-texturing  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** Adobe Substance 3D Painter ile PBR materyal/doku üretimi ve web/oyun motoru için dışa aktarma: export preset'leri, toplu dışa aktarma, çözünürlük geçersiz kılma, Pillow ile web optimizasyonu.
- **Ne zaman:** Substance Painter lisansı olan ekiplerde doku hattı otomasyonu. · **Ne zaman değil:** Substance lisansı yoksa; kodla materyal tanımlama (threejs-materials, threejs-textures).
- **Teknoloji:** substance-3d-painter, python, pbr · **Paketler:** Adobe Substance 3D Painter, Pillow
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dcc-3d-aktarim → tamamlayıcı
- **Boyut:** 126 KB (SKILL.md 15.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Ücretli Adobe aracına bağımlı, web odaklı iş akışında nadir gerekir; Painter yoksa işe yaramaz. Dikkat: web_optimizer.py 'pip install Pillow' ister; 335 gün eski.

### threejs  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Three.js skills for creating 3D elements and interactive experiences in the browser — scenes, materials, controls, and post-processing.
- **Teknoloji:** three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### threejs-animation  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 83 (A)

- **Ne yapar:** Three.js'te keyframe, iskelet ve morph target animasyonu, AnimationMixer ile klip karıştırma, glTF animasyonlarını oynatma, prosedürel hareket. WebGL ve WebGPU/TSL.
- **Ne zaman:** glTF animasyonlarını oynatırken, kemik/morph kontrolünde, klip geçişlerinde. · **Ne zaman değil:** UI/DOM animasyonu (GSAP/Motion skilleri) veya scroll bağlama (web3d-integration-patterns).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-animasyon → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 21 KB (SKILL.md 20.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel ve derli toplu; mixer/crossfade/additive konuları iyi. Dikkat: yok.

### threejs-animation@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js keyframe, iskelet ve morph animasyonu ile AnimationMixer kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-animation) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-animasyon → alternatif · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-animation) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-asset-pipeline  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 91 (A)

- **Ne yapar:** gltf-transform ile glTF/GLB varlıklarını küçültme: inspect, validate, optimize, Draco/meshopt/quantization, KTX2, WebP/AVIF dokular, her çıktı için gereken loader kurulumu ve React için gltfjsx.
- **Ne zaman:** Model yüklenmeden önce sıkıştırma/doğrulama; yükleme süresi ve GPU belleği düşürme. · **Ne zaman değil:** Modeli üretme/Blender'dan dışa aktarma (blender-web-pipeline); sahne kodu yazma.
- **Teknoloji:** three r186, gltf-transform 4, ktx2, draco, meshopt, gltfjsx · **Paketler:** @gltf-transform/cli (npx), gltfjsx (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** glb-optimizasyon → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 18 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Konuyu başka skill kapsamıyor; komutlar net. Dikkat: komutlar npx ile paket indirir (@gltf-transform/cli, gltfjsx); mutlak yol, anahtar veya telemetri yok.

### threejs-fundamentals  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 91 (A)

- **Ne yapar:** Three.js sahne kurulumunun temelleri: sahne ve sis, kameralar, renderer ve tone mapping, animasyon döngüsü, nesne hiyerarşisi, dönüşümler, matematik ve temizlik. WebGL ve WebGPU/TSL yolunu birlikte anlatır.
- **Ne zaman:** Sıfırdan Three.js sahnesi kurulurken, kamera/renderer/resize ayarlarında, nesne hiyerarşisi kurarken. · **Ne zaman değil:** İsteğe özel konular (ışık, materyal, shader) için ilgili threejs-* skilli; React kullanılıyorsa threejs-react-three-fiber.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-sahne-temelleri → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 23 KB (SKILL.md 23.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Serinin temeli; güncel (WebGPU/TSL dahil), kurulum betiği/anahtar yok. Eski calesthio sürümünden kapsamlı. Dikkat: 23 KB; 3d-gelistirici rolünün çekirdeğinde.

### threejs-fundamentals@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js sahne kurulumu, kameralar, renderer, Object3D, koordinat sistemi ve matematik sınıflarına kısa giriş (eski sürüm, WebGPU yok).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-fundamentals) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-sahne-temelleri → alternatif · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-fundamentals) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-geometry  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 81 (A)

- **Ne yapar:** Three.js geometri: yerleşik şekiller, 3D metin, BufferGeometry ve attribute'lar, birleştirme, instancing, batching, nokta bulutu ve çizgiler.
- **Ne zaman:** Özel mesh/vertex verisi, instanced mesh, nokta bulutu, 3D yazı gerektiğinde. · **Ne zaman değil:** Hazır model yüklemek (threejs-loaders).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-geometri → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 25 KB (SKILL.md 24.8 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel ve kapsamlı. Dikkat: 24.8 KB, çekirdeğe girmez; konuya göre çağrılır.

### threejs-geometry@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js yerleşik geometriler, BufferGeometry, instancing ve Points kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-geometry) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-geometri → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-geometry) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-interaction  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 83 (A)

- **Ne yapar:** Three.js'te raycasting ile seçme, kamera kontrolleri (Orbit, Fly, PointerLock vb.), TransformControls, sürükleme, hover ve kutu seçimi; WebGL/WebGPU ortak.
- **Ne zaman:** Tıklanabilir 3D nesneler, kamera kontrolü, sürükle-bırak, ürün konfigüratörü etkileşimi. · **Ne zaman değil:** React içinde (threejs-react-three-fiber pointer events bölümü).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-etkilesim → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 21.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel ve eksiksiz. Dikkat: yok.

### threejs-interaction@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js raycaster, kontroller, dokunma desteği ve seçim kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-interaction) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-etkilesim → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 15.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-interaction) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-lighting  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 91 (A)

- **Ne yapar:** Three.js ışık türleri ve fiziksel birimler, gölge haritaları, HDR ortam aydınlatması (IBL), light probe, gölge ayarları ve ışık performansı.
- **Ne zaman:** Işık kurma/ayarlama, gölge sorunları (acne), IBL kurulumu, ürün sergisi aydınlatması. · **Ne zaman değil:** Materyal seçimi (threejs-materials).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-isik → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 23 KB (SKILL.md 22.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Pratik sorun giderme ve güncel ışık API'leri. Dikkat: yok.

### threejs-lighting@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js ışık türleri, gölge kurulumu ve ortam aydınlatması kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-lighting) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-isik → alternatif · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-lighting) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-loaders  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 91 (A)

- **Ne yapar:** Three.js varlık yükleme: Draco/meshopt/KTX2 destekli glTF, diğer model biçimleri, dokular, HDR/EXR ortamları, ilerleme, önbellek, klonlama ve dispose.
- **Ne zaman:** Model/doku/HDR yüklerken, yükleme ekranı ve bellek yönetimi için. · **Ne zaman değil:** Varlık küçültme (threejs-asset-pipeline).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-yukleme → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 21.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Sıkıştırılmış glTF yükleme ve temizlik konuları güncel. Dikkat: decoder dosyalarını (draco/basis) projeye ayrıca kopyalamak gerekir; skill bunu anlatır.

### threejs-loaders@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js GLTF, doku ve HDR yükleme ile LoadingManager kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-loaders) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-yukleme → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-loaders) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-materials  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 81 (A)

- **Ne yapar:** Three.js materyalleri: unlit, diffuse, PBR (Standard/Physical), toon, nokta/çizgi materyalleri, blending/stencil ve WebGPU node materyal/TSL karşılıkları.
- **Ne zaman:** Mesh stilleme, PBR ayarı, cam/boya gibi gelişmiş materyal, toon görünüm. · **Ne zaman değil:** Özel shader yazımı (threejs-shaders).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-materyal → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 26.1 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel, UV kanalı gibi ince ayrıntılar var. Dikkat: 26 KB; opsiyonel, çekirdeğe konmaz.

### threejs-materials@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js materyal türleri (Basic, Phong, Standard, Physical, Toon) kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-materials) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-materyal → alternatif · **Globalde:** claude:ayni
- **Boyut:** 13 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-materials) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-performance  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 89 (A)

- **Ne yapar:** Three.js performans ölçümü ve iyileştirme: render istatistikleri, bellek, draw call azaltma (birleştirme, instancing, batching, LOD), fill rate, gölge, CPU yükü, shader derleme takılmaları, GPU compute.
- **Ne zaman:** Sahne yavaş/takılıyorsa, mobil bütçesi gerekiyorsa, üretime almadan önce. · **Ne zaman değil:** Temel sahne kurulumu; görsel efektler.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-performans → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 25 KB (SKILL.md 24.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Önce ölç yaklaşımı ve yaygın hatalar listesi değerli; calesthio sürümü bu konuda yok. Dikkat: 24.7 KB.

### threejs-postprocessing  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 81 (A)

- **Ne yapar:** Three.js post-processing: composer pass zinciri, bloom, DOF, SSAO, outline, özel ekran efektleri ve WebGPU/TSL node pipeline.
- **Ne zaman:** Parlama, renk derecelendirme, bulanıklık, ekran uzayı efektleri. · **Ne zaman değil:** Performans kısıtlı mobil sahneler; temel render.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three, postprocessing (isteğe bağlı)
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-postprocessing → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 26.5 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pass sırası ve seçici bloom iyi anlatılmış. Dikkat: 26.5 KB; efektler maliyetli, mobilde dikkat.

### threejs-postprocessing@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js EffectComposer, bloom, DOF, SSAO, film grain kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-postprocessing) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-postprocessing → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 14.1 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-postprocessing) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-react-three-fiber  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 89 (A)

- **Ne yapar:** React Three Fiber ve drei ile Three.js sahnesi: renderer kurulumu, JSX sahne grafı, frame-loop, state ve yükleme hook'ları, pointer olayları, adaptif performans, dispose, WebGPU/TSL.
- **Ne zaman:** React/Next.js uygulamasında 3D sahne, ürün konfigüratörü, drei yardımcıları. · **Ne zaman değil:** React dışı projeler (threejs-fundamentals).
- **Teknoloji:** R3F v9, drei 10, three r186, react 19 · **Paketler:** three, @react-three/fiber, @react-three/drei
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** r3f → birincil · **Roller:** 3d-gelistirici, frontend-muhendis
- **Boyut:** 29 KB (SKILL.md 29.3 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Güncel, 'Common Mistakes' bölümü var; freshtechbro'daki react-three-fiber skilline göre daha yeni. Dikkat: 29.3 KB, bu kategorideki en büyük skill; 3d-gelistirici çekirdeğinde.

### threejs-shaders  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 81 (A)

- **Ne yapar:** Özel GLSL vertex/fragment shader'lar: uniform, varying, shader chunk, yerleşik materyal genişletme, instanced attribute; WebGPU'da TSL node materyal karşılıkları.
- **Ne zaman:** Vertex displacement, fresnel, dissolve gibi özel efektler. · **Ne zaman değil:** Hazır materyal yetiyorsa (threejs-materials).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-shader → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 25.9 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel ve kalıp örnekleri iyi. Dikkat: 25.9 KB.

### threejs-shaders@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js GLSL ShaderMaterial, uniform, varying ve yaygın shader kalıpları kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-shaders) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-shader → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-shaders) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-textures  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 83 (A)

- **Ne yapar:** Three.js dokuları: yükleme, renk uzayı, UV kanalları/dönüşümleri, canvas'tan HDR ve KTX2'ye doku türleri, render target, atlas, doku belleği.
- **Ne zaman:** Materyallere doku bağlama, UV sorunları, cubemap/render target, doku optimizasyonu. · **Ne zaman değil:** Model yükleme (threejs-loaders).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-doku → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 22.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Renk uzayı ve slot tablosu pratik. Dikkat: yok.

### threejs-textures@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 80 (A)

- **Ne yapar:** Three.js doku yükleme, ayarlar, UV, cubemap ve HDR kısa özeti (eski sürüm).
- **Ne zaman:** CloudAI-X sürümü kullanılamıyorsa daha hafif (threejs-textures) özet isteniyorsa; normalde gerek yok. · **Ne zaman değil:** CloudAI-X sürümü varken; WebGPU/TSL gereken işler; bağlam bütçesi önemli değilse ana sürüm daha eksiksiz.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** three-doku → alternatif · **Globalde:** claude:ayni
- **Boyut:** 13 KB (SKILL.md 13.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. CloudAI-X sürümünün (threejs-textures) eski ve daha kısa karşılığı: WebGPU/TSL, güncel API ve 'Common Mistakes' bölümleri yok, açıklaması yüzeysel. İçerik farkı: ana sürümde 800-950 satır diff var. AGPL-3.0 (OpenMontage) lisansı. 'OpenMontage kurulumu gerekir' uyarısı bu skill için gereksiz (içinde OpenMontage komutu yok) ama kayıtta duruyor. Dikkat: ana sürümle aynı anda kurulursa aynı ad çakışır.

### threejs-webgl  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** Three.js/WebGL/WebGPU geliştirmesine genel bakış: sahne grafı, temel bileşenler, hazır sahne kalıbı, mesh/ışık/instancing/glTF/gölge örnekleri; kurulum betiği ve başlangıç sahnesi içerir.
- **Ne zaman:** Hızlı başlangıç şablonu isteniyorsa (setup_scene.py). · **Ne zaman değil:** Güncel Three.js işleri için threejs-fundamentals ve konu skillleri.
- **Teknoloji:** three.js, webgl, webgpu, gsap 3.15 · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** three-sahne-temelleri → alternatif
- **Boyut:** 62 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Konu bazında bölünmüş threejs-* serisinin (CloudAI-X) yüzeysel ve eskimiş özeti; hepsini tek dosyada geçiştirir. 335 gün güncellenmemiş. Dikkat: scripts/setup_scene.py yalnız dosya üretir, ağ/yıkıcı çağrı yok.

### web3d-integration-patterns  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Three.js, GSAP ScrollTrigger, React Three Fiber, Motion ve React Spring'i birleştirme desenleri: katmanlı ayrım, birleşik React bileşeni, hibrit R3F+GSAP, scroll güdümlü kamera, Zustand ile durum, performans.
- **Ne zaman:** Scroll ile hareket eden 3D hikaye siteleri, 3D + animasyon kütüphanelerini birlikte kurarken mimari karar. · **Ne zaman değil:** Tek kütüphaneli basit sahne.
- **Teknoloji:** three.js, R3F v8, gsap 3.15, motion v14, react-spring 10, zustand · **Paketler:** three, gsap, @react-three/fiber, motion, zustand
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-animasyon-entegrasyonu → birincil · **Roller:** scroll-deneyim
- **Boyut:** 21 KB (SKILL.md 20.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Scroll+3D entegrasyonunu başka skill anlatmıyor; mimari kalıplar faydalı. Dikkat: freshtechbro'nun eski sürüm varsayımları (R3F v8); 3d-gelistirici rolünden çıkarıp scroll-deneyim'e opsiyonel konması öneriliyor (bağlam sınırı); kayıtta betik/başlangıç dosyası yok.
