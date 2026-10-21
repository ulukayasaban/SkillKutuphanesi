# 05-3d-webgl — Tasarım ve Ön Yüz

_Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **33/33**

### aframe-webxr  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** A-Frame ile HTML tabanlı (entity-component) 3D, VR ve AR deneyimleri: sahne, bileşen yazımı, WebXR oturumları, kontrolcüler, 360° medya; başlangıç sahnesi ve sahne/bileşen üreteç betikleri.
- **Ne zaman:** Tarayıcıda VR/AR (WebXR) deneyimi, 360° görüntüleyici, az JavaScript ile hızlı immersive prototip. · **Ne zaman değil:** Klasik web sitesindeki 3D hero/ürün sergisi (three.js/R3F daha uygun).
- **Teknoloji:** aframe 1.7, webxr, three.js · **Paketler:** aframe
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** webxr → birincil
- **Boyut:** 176 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. A-Frame 1.7.1 ile güncel sayılır; WebXR için kategoride tek skill. 176 KB, freshtechbro 2025-11'den beri güncellenmedi.

### babylonjs-engine  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 65 (B)

- **Ne yapar:** Babylon.js 3D motoru: sahne, kamera, ışık, PBR materyal, Havok fizik, GUI, WebGPU motoru, model yükleme ve optimizasyon; Vite başlangıç projesi ve sahne/mesh üreteç betikleri.
- **Ne zaman:** Fizik, GUI ve araç zinciri hazır gelen tam bir 3D motoru istenen oyun/simülasyon/konfigüratör projeleri. · **Ne zaman değil:** Pazarlama sitesindeki hafif 3D (three.js/R3F daha küçük ve yaygın).
- **Teknoloji:** babylonjs 7, webgl2, webgpu, havok · **Paketler:** @babylonjs/core, @babylonjs/loaders, @babylonjs/havok
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-motoru → birincil
- **Boyut:** 153 KB (SKILL.md 30.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (three.js yerine motor seçilirse birincil). Başlangıç projesi Babylon ^7.31; güncel ana sürüm 8.x, temel API'ler büyük ölçüde uyumlu. 153 KB.

### blender-web-pipeline  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Blender'dan web'e 3D aktarım: glTF 2.0 dışa aktarma ayarları, bpy ile toplu dışa aktarma ve otomasyon, LOD üretimi, doku pişirme ve model optimizasyonu betikleri.
- **Ne zaman:** Blender'da hazırlanan modelleri three.js/Babylon için otomatik ve tutarlı dışa aktarmak. · **Ne zaman değil:** Blender kurulu değilse; hazır GLB'yi sadece sıkıştırmak (threejs-asset-pipeline).
- **Teknoloji:** blender 4, bpy, gltf 2.0, python · **Paketler:** Blender (bpy)
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-varlik-hazirlama → tamamlayıcı
- **Boyut:** 27 KB (SKILL.md 16.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Varlık hazırlamanın Blender tarafı; betikler Blender içinden (blender --background --python) çalışır.

### lightweight-3d-effects  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 66 (B)

- **Ne yapar:** Ağır çatı kullanmadan dekoratif 3D: Zdog ile sahte 3D illüstrasyon, Vanta.js animasyonlu arka planlar ve Vanilla-Tilt ile parallax eğim efekti; kurulum ve üreteç betikleri.
- **Ne zaman:** Hero arka planı veya kart eğimi gibi küçük dekoratif derinlik efektleri. · **Ne zaman değil:** Gerçek 3D sahne; yeni projelerde Vanta (three r134'e sabit, bakımsız) yerine OGL veya küçük bir three.js shader arka planı tercih et.
- **Teknoloji:** zdog, vanta, vanilla-tilt, three.js · **Paketler:** zdog, vanta, three@0.134, vanilla-tilt
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hafif-3d-efekt → birincil
- **Boyut:** 179 KB (SKILL.md 22.3 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. Vanta ve Zdog yıllardır bakımsız; Vanta eski three r134 gerektiriyor. Kayıtta 1 kırık bağlantı ('illo').

### playcanvas-engine  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** PlayCanvas motoru: entity-component mimarisi, script'ler, editör iş akışı, fizik, girdi ve optimizasyon; başlangıç projesi ve bileşen/proje üreteç betikleri.
- **Ne zaman:** PlayCanvas editörüyle çalışan ekipler veya tarayıcı oyunu. · **Ne zaman değil:** Genel web 3D'si (three.js/R3F); editör kullanılmayacaksa çoğu durumda Babylon/three.js daha yaygın.
- **Teknoloji:** playcanvas 2, webgl2, webgpu · **Paketler:** playcanvas
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-motoru → alternatif
- **Boyut:** 183 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ama genel; Babylon ile aynı ihtiyaç (tam motor) için alternatif. 183 KB.

### react-three-fiber  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** React Three Fiber ile bildirimsel 3D: Canvas, useFrame, useThree, drei yardımcıları, olaylar, Suspense ile yükleme, leva kontrolleri; Vite başlangıç projesi ve sahne/bileşen üreteci betikleri.
- **Ne zaman:** R3F v8 / React 18 kullanan var olan projelerde. · **Ne zaman değil:** Yeni projeler: threejs-react-three-fiber (R3F v9, React 19) daha güncel.
- **Teknoloji:** R3F v8, drei 9, three r172, react 18 · **Paketler:** three, @react-three/fiber, @react-three/drei, leva
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-three-fiber → alternatif
- **Boyut:** 105 KB (SKILL.md 22.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kavramlar doğru ama başlangıç projesi R3F ^8.18 / drei ^9 / React 18 / three 0.172; R3F v9 React 19 gerektirir. freshtechbro 2025-11'den beri güncellenmedi.

### spline-interactive  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Spline (tarayıcı tabanlı 3D tasarım aracı) sahnelerini web'e/React'e gömme: @splinetool/react-spline ve runtime, olaylar, nesneleri koddan kontrol etme, performans ve dışa aktarma seçenekleri.
- **Ne zaman:** Tasarımcının Spline'da hazırladığı 3D sahne siteye konacaksa; kodsuz hızlı 3D prototip. · **Ne zaman değil:** Tam kontrol ve küçük paket gereken sahneler (Spline runtime ağır); Spline hesabı/sahnesi yoksa.
- **Teknoloji:** spline, react · **Paketler:** @splinetool/react-spline, @splinetool/runtime
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kodsuz-3d → birincil
- **Boyut:** 54 KB (SKILL.md 19.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kodsuz 3D için kategoride tek skill; API'ler geçerli. freshtechbro 2025-11'den beri güncellenmedi.

### substance-3d-texturing  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Adobe Substance 3D Painter ile PBR doku iş akışı: kanal rehberi, web/mobil/three.js/Babylon için dışa aktarma şablonları, Painter Python API'siyle toplu dışa aktarma ve doku optimizasyon betikleri.
- **Ne zaman:** Substance Painter kullanan ekiplerde PBR dokuları web'e uygun boyut ve formatta dışa aktarmak. · **Ne zaman değil:** Substance lisansı yoksa; prosedürel/three.js içi materyaller yeterliyse.
- **Teknoloji:** substance-3d-painter, python, pbr · **Paketler:** Adobe Substance 3D Painter (ücretli), python3
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-varlik-hazirlama → tamamlayıcı
- **Boyut:** 126 KB (SKILL.md 15.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Dar ama doğru kapsam; ücretli Adobe aracına bağımlı.

### threejs-animation  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js animasyonu: AnimationMixer, keyframe izleri, iskelet animasyonu, morph target, animasyon karıştırma/geçiş ve prosedürel hareket.
- **Ne zaman:** GLTF animasyonu oynatmak, karakter animasyonu blend'i, prosedürel nesne hareketi. · **Ne zaman değil:** DOM/scroll animasyonu (GSAP skilleri); kamera yolu scroll'a bağlanacaksa gsap-scrolltrigger ile birlikte kullan.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-animation → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 21 KB (SKILL.md 20.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-animation@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-animation skillinin OpenMontage'daki eski sürümü: three.js animasyonu: AnimationMixer, keyframe izleri, iskelet animasyonu, morph target, animasyon karıştırma/geçiş ve prosedürel hareket. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-animation → alternatif · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-asset-pipeline  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** glTF varlıklarını three.js için küçültme: gltf-transform inspect/validate/optimize, Draco, meshopt ve quantization, KTX2/WebP/AVIF dokular, her çıktının gerektirdiği yükleyici ayarı ve React için gltfjsx.
- **Ne zaman:** 3D modeli siteye koymadan önce sıkıştırma, doğrulama ve yükleyici ayarı; büyük GLB'ler. · **Ne zaman değil:** Model üretimi/modelleme (blender-web-pipeline); prosedürel geometri.
- **Teknoloji:** three r186, gltf-transform 4, ktx2, draco, meshopt, gltfjsx · **Paketler:** @gltf-transform/cli, three, gltfjsx (React)
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-varlik-hazirlama → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 18 KB (SKILL.md 17.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). 3d-varlik-hazirlama grubunun birincili: komut düzeyinde somut, yükleyici eşlemesi doğru, güncel (r185/r186). Blender/Substance skilleri araç tarafı tamamlayıcısı.

### threejs-fundamentals  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js temeli: Scene/Camera/Renderer kurulumu, Object3D hiyerarşisi, koordinat sistemi, yeniden boyutlandırma, render döngüsü, renk yönetimi ve WebGPURenderer'a geçiş.
- **Ne zaman:** Her vanilla Three.js projesinin başlangıcı; sahne kurulumu ve dönüşümler. · **Ne zaman değil:** React projesi (threejs-react-three-fiber).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-fundamentals → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 23 KB (SKILL.md 23.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-fundamentals@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-fundamentals skillinin OpenMontage'daki eski sürümü: three.js temeli: Scene/Camera/Renderer kurulumu, Object3D hiyerarşisi, koordinat sistemi, yeniden boyutlandırma, render döngüsü, renk yönetimi ve WebGPURenderer'a geçiş. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-fundamentals → alternatif · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir. r152 dönemine ait renk yönetimi notları içeriyor.

### threejs-geometry  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** Three.js geometri: hazır şekiller, BufferGeometry ile özel geometri, öznitelikler, InstancedMesh/BatchedMesh ile çoğaltma ve geometri birleştirme.
- **Ne zaman:** Özel şekil, prosedürel mesh, binlerce kopya (instancing) gerektiğinde. · **Ne zaman değil:** Sadece hazır GLTF modeli gösterilecekse (threejs-loaders).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-geometry → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 25 KB (SKILL.md 24.8 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-geometry@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-geometry skillinin OpenMontage'daki eski sürümü: three.js geometri: hazır şekiller, BufferGeometry ile özel geometri, öznitelikler, InstancedMesh/BatchedMesh ile çoğaltma ve geometri birleştirme. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-geometry → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-interaction  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js etkileşimi: Raycaster ile seçim, fare/dokunma girdisi, OrbitControls ve diğer kontroller, sürükleme ve nesne seçimi.
- **Ne zaman:** Tıklanabilir/üzerine gelinebilir 3D nesneler, kamera kontrolleri, ürün döndürme. · **Ne zaman değil:** R3F projeleri (pointer olayları threejs-react-three-fiber'da).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-interaction → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 21.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-interaction@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-interaction skillinin OpenMontage'daki eski sürümü: three.js etkileşimi: Raycaster ile seçim, fare/dokunma girdisi, OrbitControls ve diğer kontroller, sürükleme ve nesne seçimi. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-interaction → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 15.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-lighting  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js ışıklandırma: ışık türleri, gölgeler ve gölge ayarı, HDR ortam ışığı (IBL), ışık performansı.
- **Ne zaman:** Ürün sergisi ve sahne ışığı, gölge kalitesi, ortam haritası. · **Ne zaman değil:** Işıksız/unlit stilize sahneler.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-lighting → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 23 KB (SKILL.md 22.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-lighting@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-lighting skillinin OpenMontage'daki eski sürümü: three.js ışıklandırma: ışık türleri, gölgeler ve gölge ayarı, HDR ortam ışığı (IBL), ışık performansı. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-lighting → alternatif · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-loaders  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js varlık yükleme: GLTFLoader (Draco/Meshopt/KTX2), doku/HDR yükleyiciler, LoadingManager ile ilerleme, async kalıplar ve önbellek.
- **Ne zaman:** GLTF/GLB model, HDR ortam veya çok sayıda varlık yüklenecekse. · **Ne zaman değil:** Modellerin önceden optimize edilmesi (threejs-asset-pipeline).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-loaders → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 21.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-loaders@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-loaders skillinin OpenMontage'daki eski sürümü: three.js varlık yükleme: GLTFLoader (Draco/Meshopt/KTX2), doku/HDR yükleyiciler, LoadingManager ile ilerleme, async kalıplar ve önbellek. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-loaders → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir. CDN örneği three@0.160.

### threejs-materials  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** Three.js materyalleri: PBR (MeshStandard/MeshPhysical: transmission, clearcoat, iridescence), basit materyaller, ShaderMaterial, materyal ayarları ve performans.
- **Ne zaman:** Ürün görselleştirme (cam, metal, kumaş), PBR ayarı, materyal seçimi. · **Ne zaman değil:** Tamamen özel shader efektleri (threejs-shaders).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-materials → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 26.1 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-materials@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-materials skillinin OpenMontage'daki eski sürümü: three.js materyalleri: PBR (MeshStandard/MeshPhysical: transmission, clearcoat, iridescence), basit materyaller, ShaderMaterial, materyal ayarları ve performans. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-materials → alternatif · **Globalde:** claude:ayni
- **Boyut:** 13 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-performance  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** Three.js hız ölçümü ve optimizasyonu: renderer.info istatistikleri, bellek sayaçları, merge/instancing/BatchedMesh/LOD ile draw call azaltma, fill rate ve DPR, gölge maliyeti, kare başı CPU işi, shader derleme takılmaları, parçacıklar için GPU compute; WebGL ve WebGPU/TSL.
- **Ne zaman:** Sahne yavaşsa, takılıyorsa, mobilde ısınıyorsa veya bellek büyüyorsa; yayından önce performans bütçesi kontrolü. · **Ne zaman değil:** Henüz çalışan bir sahne yoksa (önce fundamentals).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-performance → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 25 KB (SKILL.md 24.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Ölçmeden optimize etme yaklaşımı; r186 ve WebGPU'ya güncel. Kategoride tek performans skilli.

### threejs-postprocessing  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** Three.js post-processing: EffectComposer, bloom, DOF, SMAA/FXAA, renk düzeltme, özel ekran shader'ları; WebGPU tarafında node tabanlı post-processing.
- **Ne zaman:** Bloom, glow, alan derinliği, sinematik renk düzeltme gerektiğinde. · **Ne zaman değil:** Mobil ağırlıklı ve performans bütçesi dar sahneler (her pass maliyetli).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-postprocessing → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 26.5 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-postprocessing@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-postprocessing skillinin OpenMontage'daki eski sürümü: three.js post-processing: EffectComposer, bloom, DOF, SMAA/FXAA, renk düzeltme, özel ekran shader'ları; WebGPU tarafında node tabanlı post-processing. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-postprocessing → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 14.1 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir. r150 dönemine ait örnekler içeriyor.

### threejs-react-three-fiber  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** React Three Fiber ve drei ile three.js sahnelerini React'ten kurma: Canvas ve renderer ayarı, JSX sahne ağacı, useFrame döngüsü, state/yükleme hook'ları, pointer olayları, uyarlanabilir performans; WebGL veya WebGPU/TSL.
- **Ne zaman:** React/Next.js projesinde 3D sahne, ürün konfigüratörü, hero 3D'si. · **Ne zaman değil:** React kullanılmayan projeler (vanilla threejs-* skilleri).
- **Teknoloji:** R3F v9, drei 10, three r186, react 19 · **Paketler:** three, @react-three/fiber, @react-three/drei
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-three-fiber → birincil · **Roller:** 3d-gelistirici
- **Boyut:** 29 KB (SKILL.md 29.3 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). react-three-fiber grubunun birincili: R3F v9/React 19 ve WebGPU'ya güncel, 2026-10'da bakımı yapılmış. freshtechbro react-three-fiber R3F v8/React 18 dönemine ait.

### threejs-shaders  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 82 (A)

- **Ne yapar:** Three.js shader'ları: GLSL ile ShaderMaterial/RawShaderMaterial, uniform'lar, vertex/fragment efektleri, onBeforeCompile ile hazır materyali genişletme ve TSL (node tabanlı shader).
- **Ne zaman:** Özel görsel efekt, distortion, gradient/noise arka plan, materyal genişletme. · **Ne zaman değil:** Hazır PBR materyalleri yeterliyse (threejs-materials).
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-shaders → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 26 KB (SKILL.md 25.9 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-shaders@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-shaders skillinin OpenMontage'daki eski sürümü: three.js shader'ları: GLSL ile ShaderMaterial/RawShaderMaterial, uniform'lar, vertex/fragment efektleri, onBeforeCompile ile hazır materyali genişletme ve TSL (node tabanlı shader). WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-shaders → alternatif · **Globalde:** claude:ayni
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-textures  ·  CloudAI-X/threejs-skills @ 0e18186  ·  puan 85 (A)

- **Ne yapar:** Three.js dokuları: doku türleri, UV eşleme, renk uzayı, cubemap/HDR ortam haritası, video/canvas dokusu, KTX2 sıkıştırma ve doku ayarları.
- **Ne zaman:** Doku/harita yükleme ve ayarlama, ortam haritaları, doku bellek optimizasyonu. · **Ne zaman değil:** Doku kullanmayan sahneler.
- **Teknoloji:** three r186, webgl2, webgpu, tsl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** CloudAI-X (kisi, ★3668, son güncelleme 2026-10-19, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-textures → birincil · **Roller:** 3d-gelistirici · **Globalde:** claude:farkli
- **Boyut:** 22 KB (SKILL.md 22.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). CloudAI-X sürümü three.js r186'ya göre yazılmış (WebGL + WebGPURenderer/TSL bölümleri), 2026-10'da güncellendi. Seçim gerekçesi: OpenMontage kopyasından daha yeni ve kapsamlı; MIT lisanslı (OpenMontage kopyası AGPL-3.0).

### threejs-textures@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 90 (A)

- **Ne yapar:** threejs-textures skillinin OpenMontage'daki eski sürümü: three.js dokuları: doku türleri, UV eşleme, renk uzayı, cubemap/HDR ortam haritası, video/canvas dokusu, KTX2 sıkıştırma ve doku ayarları. WebGPU/TSL bölümleri yok.
- **Ne zaman:** Yalnızca OpenMontage içinde kurulu kopyayla tutarlılık gerektiğinde (ör. HyperFrames üç boyutlu sahneleri). · **Ne zaman değil:** Normalde: CloudAI-X sürümü (aynı ad, tercih) r186'ya güncel.
- **Teknoloji:** three.js, webgl · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** threejs-textures → alternatif · **Globalde:** claude:ayni
- **Boyut:** 13 KB (SKILL.md 13.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. OpenMontage kopyası CloudAI-X skillinin eski bir sürümü (aynı açıklama, farklı/eski içerik; WebGPU/TSL yok). Kayıttaki 'OpenMontage kurulumu gerekir' bağımlılığı bu skill için geçersiz: içerikte OpenMontage aracı/komutu yok, düz kütüphane dokümantasyonu; tek başına kurulabilir.

### threejs-webgl  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Three.js'e tek dosyalık genel bakış: sahne/kamera/renderer, geometri, materyal, ışık, doku, animasyon, OrbitControls, WebGPU kurulumu, GSAP entegrasyonu ve optimizasyon kontrol listesi; başlangıç sahnesi.
- **Ne zaman:** Bağlam bütçesi dar ve tek skillde Three.js özeti istendiğinde. · **Ne zaman değil:** Ayrıntılı iş (konu bazlı threejs-* skilleri r186'ya güncel ve daha derin).
- **Teknoloji:** three.js, webgl, webgpu, gsap 3.15 · **Paketler:** three
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** threejs-fundamentals → alternatif
- **Boyut:** 62 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Genel ama yüzeysel; CloudAI-X konu skilleriyle örtüşüyor. threejs-fundamentals grubunda alternatif.

### web3d-integration-patterns  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 68 (B)

- **Ne yapar:** Three.js, GSAP ScrollTrigger, React Three Fiber, Motion ve React Spring'i birlikte kullanma mimarisi: scroll'a bağlı 3D kamera, drei ScrollControls, ortak durum (zustand), animasyon döngüsü senkronizasyonu ve performans kalıpları.
- **Ne zaman:** Scroll hikâyesinde 3D sahne + DOM animasyonu birlikte kurulacaksa; kütüphaneler arası koordinasyon. · **Ne zaman değil:** Tek kütüphaneli basit sahneler; zustand örnekleri eski default import (import create from 'zustand') kullanıyor, v5'te { create }.
- **Teknoloji:** three.js, R3F v8, gsap 3.15, motion v14, react-spring 10, zustand · **Paketler:** three, @react-three/fiber, @react-three/drei, gsap, zustand
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-scroll-entegrasyonu → birincil · **Roller:** 3d-gelistirici, scroll-deneyim
- **Boyut:** 21 KB (SKILL.md 20.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kategoride bu entegrasyonu anlatan tek skill; kavramlar değerli ama bazı API'ler eski (zustand default export) ve R3F v8 dönemine ait.
