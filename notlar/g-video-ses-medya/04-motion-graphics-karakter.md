# 04-motion-graphics-karakter — Video, Ses ve AI Medya Üretimi

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **13/18**

### canvas-procedural-animation  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 85 (A)

- **Ne yapar:** p5.js/Canvas ile karakter destekleyici prosedürel hareket: parçacık, hava efekti, yaprak, squash/stretch ve basit yürüme döngüleri; zaman/kare tabanlı deterministik durum önerir.
- **Ne zaman:** Karaktere eşlik eden çevre efektleri veya basit prosedürel gövdeler gerektiğinde. · **Ne zaman değil:** Karmaşık yüz oyunculuğu (SVG rig daha uygun) veya kare-kesin final render.
- **Teknoloji:** p5js, canvas, javascript · **Paketler:** p5
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → alternatif · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Çok kısa (ipucu düzeyi); kaynak bağlantıları doğru.

### character-animation-qa  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 86 (A)

- **Ne yapar:** Karakter animasyonunu sunmadan önce katmanlı kontrol: şema doğrulama, varlık kontrolü, Playwright ile tarayıcı önizleme ve ekran görüntüsü, kare örnekleme, ffprobe ile final MP4 kontrolü ve pass/revise/fail kararı.
- **Ne zaman:** Karakter animasyonu önizlemesi veya finali teslim edilmeden önce. · **Ne zaman değil:** Karakter içermeyen genel video kontrolü (hyperframes-cli inspect/validate).
- **Teknoloji:** playwright, ffmpeg · **Paketler:** playwright, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, qa-erisilebilirlik
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa kontrol listesi; OpenMontage karakter hattının şema adlarına atıf yapıyor.

### character-rigging  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 85 (A)

- **Ne yapar:** Yerel 2D karakter animasyonu için veri güdümlü rig paketi: parçalar, pivotlar, katman sırası, kısıtlar ve görünümler; her karakteri jenerik çalışma zamanına veri paketi olarak tanımlar.
- **Ne zaman:** SVG/2D karakter animasyonu için rig planı hazırlarken. · **Ne zaman değil:** 3D rig (Blender/Three.js); hazır Lottie animasyonu yeterliyse.
- **Teknoloji:** svg, gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ama doğru kalıplar; OpenMontage rig_plan artefaktına göre yazılmış.

### cut-the-curve  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** Hız eşlemeli sahne geçişleri kataloğu: zoom-through, ters zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut; ayrıca sahne içi waterfall giriş ve üç fazlı 'nudge' grup kaydırma. Ayna power4 easing ile kısmi hareket eşleme, boyuta göre bulanıklık ve 10/65/25 kaydırma oranı gibi sayısal kurallar verir.
- **Ne zaman:** Herhangi bir geçiş, metin vuruşu devri, kinetik metin girişi veya grup yeniden konumlandırma yazılmadan önce. · **Ne zaman değil:** Tek sahnelik statik işlerde; HyperFrames/GSAP dışı ortamlarda.
- **Teknoloji:** gsap, hyperframes · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 28 KB (SKILL.md 18.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Sayısal, uygulanabilir teknik kataloğu; GSAP örnekleri dahil. Ev stili kökenli olsa da genel geçer değerde.

### huashu-art-motion  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** 辅助艺术动画与解说任务：35 种艺术风格配方、9 种解说语法、分镜与确定性 Canvas 绘制工具。按宿主时间轴实现，素材与导出使用宿主能力。
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 424 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### layers  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 66 (B)

- **Ne yapar:** Split one image into editable layers (PSD + PNG). 把一张图拆成图层（PSD + PNG）。
- **Teknoloji:** api-anahtari, canvas, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★256, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 12.4 KB, yük orta)
- **İnceleme:** otomatik

### manim-composer  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını sorar, anlatı yayı, görsel öğeler, renk paleti ve uygulama sırasını yazar.
- **Ne zaman:** Matematik/bilim açıklayıcı videosu planlanırken, Manim kodundan önce. · **Ne zaman değil:** Kod yazımı (manimce/manimgl-best-practices); matematik dışı tanıtım videoları.
- **Teknoloji:** manim
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, planlayici
- **Boyut:** 22 KB (SKILL.md 4.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İyi planlama şablonu ve 3b1b ilkeleri; references/ dosyaları faydalı.

### manimce-best-practices  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve yapılandırma; çalışan örnekler ve şablonlar içerir.
- **Ne zaman:** 'from manim import *' kullanan matematik/bilim animasyonlarında. · **Ne zaman değil:** ManimGL (manimlib) projelerinde; matematik dışı motion graphic işlerinde.
- **Teknoloji:** manim, python, latex · **Paketler:** manim, latex, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 206 KB (SKILL.md 5.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kapsamlı kural seti, test edilmiş örnekler; CE topluluk sürümü daha yaygın olduğu için birincil.

### manimgl-best-practices  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşimli mod, checkpoint_paste ve 3D render.
- **Ne zaman:** 'from manimlib import *' kullanan veya etkileşimli geliştirme isteyen projelerde. · **Ne zaman değil:** Manim Community Edition projelerinde (API'ler farklı).
- **Teknoloji:** manim, python, opengl, latex · **Paketler:** manimgl, latex
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → alternatif · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 729 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 5
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kaliteli; kurulumu ve sürüm uyumu CE'ye göre zahmetli.

### motion-doctrine  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 99 (A)

- **Ne yapar:** Çok sahneli videonun bağımsız slaytlar yığını değil tek kesintisiz kamera hareketi gibi hissettirmesi için üst düzey hareket yasası: vektör yasası (çıkış girişi belirler, Z ölçek işareti), filmin akıntısı, taşıyıcı öğeler, nedensel hareket, Seam Gate doğrulayıcısı, boşta sallanma yasağı ve doruk öncesi durgunluk. Alt teknik skillere (cut-the-curve, seam-craft, oversized-cursor) yönlendirir.
- **Ne zaman:** Çok sahneli HyperFrames videosunda geçiş ve hareket dili kurulmadan önce. · **Ne zaman değil:** Tek sahnelik kısa grafiklerde; HyperFrames dışı web animasyonunda.
- **Teknoloji:** hyperframes, gsap, node · **Paketler:** hyperframes (npx), node
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 44 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kendini genel/üst akış hareket rehberlerinin ÜSTÜNDE ilan ediyor — bu bir ev stili tercihi, evrensel kural değil. seam-gate doğrulayıcı betiği somut. · 2026-11-12 yeniden incelendi (ab66e5b): seam-gate betiği `__player.seek` artık asenkron beklendiği için await ile çalışıyor (eskiden t=0'ı ölçüp tüm dikişleri hatalı gösterebilirdi); referans notu eklendi. Değerlendirme aynı.

### oil-motion  ·  nexu-io/open-design @ 987b247  ·  puan 95 (A)

- **Ne yapar:** 处理视频和序列帧，编译滚动、指针、拖动与状态驱动的网页动效；内含本地媒体处理脚本和运行时。新素材生成使用宿主工具。
- **Teknoloji:** api-anahtari, css, ffmpeg, html, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 318 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### pose-library-design  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 86 (A)

- **Ne yapar:** Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekleme→oturma oyunculuk kalıbını önerir.
- **Ne zaman:** Karakterin duygu ve aksiyonlarını tutarlı pozlarla anlatmak gerektiğinde. · **Ne zaman değil:** Tek seferlik basit hareketler; rig henüz yoksa (önce character-rigging).
- **Teknoloji:** gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru; tek başına derinliği sınırlı.

### seam-craft  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 92 (A)

- **Ne yapar:** Sahneden sahneye geçişlerin ana zaman çizelgesinde doğru birleşmesi için render önkoşulları: koyu filmlerde kesmede beyaz parlamayı önleyen opak sahne zemini, enjektörün sarmalayıcıları nasıl örtüştürdüğü, son kareyi tuttuğu ve şablon kodunu nasıl yerleştirdiği.
- **Ne zaman:** Ana index.html birleştirilirken veya geçişte beyaz parlama/opaklık sızması görüldüğünde. · **Ne zaman değil:** Geçiş seçimi için (cut-the-curve); tek sahnelik işlerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa ve tek bir hata sınıfına odaklı, HeyGen launch-video enjektörüne özgü ayrıntılar içeriyor.

### svg-character-animation  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pivot, zaman çizelgesi ve kare örnekleme kurallarını verir.
- **Ne zaman:** Açıklayıcı videoda konuşan/hareket eden 2D karakter gerektiğinde. · **Ne zaman değil:** 3D karakter; hazır Lottie dosyası oynatılacaksa (lottie-bodymovin).
- **Teknoloji:** svg, gsap, remotion, hyperframes · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Remotion'da GSAP'ı kareye bağlama gibi kritik kuralları doğru veriyor.

### threejs-world-generation  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** Metinden veya yapılandırılmış özetten belirlenimci, düzenlenebilir Three.js dünyaları: arazi, semantik bölgeler, prosedürel biyomlar, landmark'lar, kamera fly-through; OpenMontage threejs_world aracı ve HyperFrames ile entegre.
- **Ne zaman:** OpenMontage/HyperFrames hattında sinematik 3D ortam videosu. · **Ne zaman değil:** Web sayfasına gömülü 3D, tek nesne, düz paralaks sahne; OpenMontage yoksa.
- **Teknoloji:** three.js, hyperframes, openmontage, python, blender · **Paketler:** OpenMontage (~/.openmontage), hyperframes
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** three-dunya-uretimi → birincil · **Roller:** video-kompozisyon
- **Boyut:** 16 KB (SKILL.md 8.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Fidelity katmanları ve kalite kapıları titiz yazılmış. Dikkat: OpenMontage kurulumu ve threejs_world aracı şart (~/.openmontage/tools/graphics/threejs_world.py mevcut); 3d-asset-generation, hyperframes-* skillerine atıf yapıyor; kategori olarak video hattına yakın ama Three.js içeriği nedeniyle burada kalabilir. Kategori düzeltildi (05-3d-webgl → g-video-ses-medya/04-motion-graphics-karakter): web 3D'si değil, OpenMontage video boru hattının parçası (tools.graphics.threejs_world).

### upload  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 68 (B)

- **Ne yapar:** Share a film to the lemo-wake gallery. 把动图投稿到作品墙。
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★256, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 6.3 KB, yük kucuk)
- **İnceleme:** otomatik

### visual-style  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper.design'a uygular; hazır stil galerisi (Swiss, Saul Bass, Game Boy…) içerir.
- **Ne zaman:** Video veya sunum serisinde tutarlı renk, tipografi, hareket ve ruh hali tanımlanacaksa. · **Ne zaman değil:** Kod tabanlı web tasarım sistemi/token kurulumu (a-tasarim/02 skilleri daha uygun).
- **Teknoloji:** markdown, html
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** gorsel-stil-sistemi → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 81 KB (SKILL.md 6.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik mod tablosu ve galeri; a-tasarim/02 tasarım sistemi skilleriyle kısmen örtüşür.

### wake  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 66 (B)

- **Ne yapar:** Turn one image into a ~5 s looping animation. 把一张图做成约 5 秒的循环动图。
- **Teknoloji:** api-anahtari, canvas, ffmpeg, html, node, python, react, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★256, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 549 KB (SKILL.md 21.7 KB, yük orta)
- **İnceleme:** otomatik
