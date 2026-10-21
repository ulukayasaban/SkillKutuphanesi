# 04-motion-graphics-karakter — Video, Ses ve AI Medya Üretimi

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **10/14**

### canvas-procedural-animation  ·  calesthio/OpenMontage @ c806645  ·  puan 79 (B)

- **Ne yapar:** p5.js/Canvas ile karakter destekleyici prosedürel hareket: parçacık, hava efekti, yaprak, squash/stretch ve basit yürüme döngüleri; zaman/kare tabanlı deterministik durum önerir.
- **Ne zaman:** Karaktere eşlik eden çevre efektleri veya basit prosedürel gövdeler gerektiğinde. · **Ne zaman değil:** Karmaşık yüz oyunculuğu (SVG rig daha uygun) veya kare-kesin final render.
- **Teknoloji:** p5js, canvas, javascript · **Paketler:** p5
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → alternatif · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Çok kısa (ipucu düzeyi); kaynak bağlantıları doğru.

### character-animation-qa  ·  calesthio/OpenMontage @ c806645  ·  puan 79 (B)

- **Ne yapar:** Karakter animasyonunu sunmadan önce katmanlı kontrol: şema doğrulama, varlık kontrolü, Playwright ile tarayıcı önizleme ve ekran görüntüsü, kare örnekleme, ffprobe ile final MP4 kontrolü ve pass/revise/fail kararı.
- **Ne zaman:** Karakter animasyonu önizlemesi veya finali teslim edilmeden önce. · **Ne zaman değil:** Karakter içermeyen genel video kontrolü (hyperframes-cli inspect/validate).
- **Teknoloji:** playwright, ffmpeg · **Paketler:** playwright, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, qa-erisilebilirlik · **Globalde:** claude:ayni
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa kontrol listesi; OpenMontage karakter hattının şema adlarına atıf yapıyor.

### character-rigging  ·  calesthio/OpenMontage @ c806645  ·  puan 79 (B)

- **Ne yapar:** Yerel 2D karakter animasyonu için veri güdümlü rig paketi: parçalar, pivotlar, katman sırası, kısıtlar ve görünümler; her karakteri jenerik çalışma zamanına veri paketi olarak tanımlar.
- **Ne zaman:** SVG/2D karakter animasyonu için rig planı hazırlarken. · **Ne zaman değil:** 3D rig (Blender/Three.js); hazır Lottie animasyonu yeterliyse.
- **Teknoloji:** svg, gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ama doğru kalıplar; OpenMontage rig_plan artefaktına göre yazılmış.

### cut-the-curve  ·  heygen-com/hyperframes @ 25126bc  ·  puan 92 (A)

- **Ne yapar:** The technique catalog: five velocity-matched SEAMS (zoom-through, INVERSE zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut) plus the two in-scene techniques — waterfall ENTRY (staggered arrival cascades for title cards / segment openers) and the nudge curve (slow-fast-slow three-phase group slides). Covers partial-travel (~12% of frame) velocity matching via mirrored power4 eases, t
- **Teknoloji:** canvas, css, gsap _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 28 KB (SKILL.md 18.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### manim-composer  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını sorar, anlatı yayı, görsel öğeler, renk paleti ve uygulama sırasını yazar.
- **Ne zaman:** Matematik/bilim açıklayıcı videosu planlanırken, Manim kodundan önce. · **Ne zaman değil:** Kod yazımı (manimce/manimgl-best-practices); matematik dışı tanıtım videoları.
- **Teknoloji:** manim
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, planlayici · **Globalde:** claude:ayni
- **Boyut:** 22 KB (SKILL.md 4.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İyi planlama şablonu ve 3b1b ilkeleri; references/ dosyaları faydalı.

### manimce-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 95 (A)

- **Ne yapar:** Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve yapılandırma; çalışan örnekler ve şablonlar içerir.
- **Ne zaman:** 'from manim import *' kullanan matematik/bilim animasyonlarında. · **Ne zaman değil:** ManimGL (manimlib) projelerinde; matematik dışı motion graphic işlerinde.
- **Teknoloji:** manim, python, latex · **Paketler:** manim, latex, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → birincil · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 206 KB (SKILL.md 5.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kapsamlı kural seti, test edilmiş örnekler; CE topluluk sürümü daha yaygın olduğu için birincil.

### manimgl-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşimli mod, checkpoint_paste ve 3D render.
- **Ne zaman:** 'from manimlib import *' kullanan veya etkileşimli geliştirme isteyen projelerde. · **Ne zaman değil:** Manim Community Edition projelerinde (API'ler farklı).
- **Teknoloji:** manim, python, opengl, latex · **Paketler:** manimgl, latex
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → alternatif · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 729 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 5
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kaliteli; kurulumu ve sürüm uyumu CE'ye göre zahmetli.

### motion-doctrine  ·  heygen-com/hyperframes @ 25126bc  ·  puan 92 (A)

- **Ne yapar:** GATEWAY — load FIRST before composing any HyperFrames animation or video. The high-level motion law that makes a multi-scene video feel like ONE continuous camera move instead of a stack of independently-animated slides. Covers the vector law (how you exit determines how you enter, incl. the Z scale-sign rule), the film's current, carrier elements, causal motion, the Seam Gate (build-gate enforcem
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 44 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### motion-graphics  ·  heygen-com/hyperframes @ 25126bc  ·  puan 85 (A)

- **Ne yapar:** Use when creating a short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout / social overlay, animated map (highlight regions, connect places, zoom to a location), animated tweet / news-article / headline, webpage / UI animation (scroll, cursor, callouts), or fusing a real image's geometr
- **Teknoloji:** api-anahtari, ffmpeg, gsap, html, node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 113 KB (SKILL.md 15.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır. · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### motion-graphics@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** Hareketin mesaj olduğu kısa (~10-30 sn), anlatımsız motion graphic üretimi: kinetik tipografi, sayı sayacı, grafik, logo sting, lower-third, sosyal overlay. Varlık-önce yaklaşımla plan→kaynak→tasarım→yapım→render→doğrulama aşamalarını alt ajanlarla yürütür.
- **Ne zaman:** Kısa, tasarım odaklı, seslendirmesiz grafik/overlay (MP4 veya şeffaf) istendiğinde. · **Ne zaman değil:** Uzun, çok sahneli veya anlatımlı videolarda (yönlendirdiği general-video vb. arşivde yok); mevcut görüntüye altyazı.
- **Teknoloji:** hyperframes, html, gsap, ffmpeg · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** hyperframes-is-akislari → birincil · **Roller:** motion-graphics-sanatcisi, video-produksiyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 108 KB (SKILL.md 13.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Olgun kategori modülleri; /general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions yönlendirmeleri arşivde yok.

### pose-library-design  ·  calesthio/OpenMontage @ c806645  ·  puan 79 (B)

- **Ne yapar:** Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekleme→oturma oyunculuk kalıbını önerir.
- **Ne zaman:** Karakterin duygu ve aksiyonlarını tutarlı pozlarla anlatmak gerektiğinde. · **Ne zaman değil:** Tek seferlik basit hareketler; rig henüz yoksa (önce character-rigging).
- **Teknoloji:** gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru; tek başına derinliği sınırlı.

### seam-craft  ·  heygen-com/hyperframes @ 25126bc  ·  puan 94 (A)

- **Ne yapar:** Render-correctness doctrine for scene-to-scene seams in HyperFrames launch videos — the prerequisites that make transitions composite correctly on the master timeline. Load when assembling the master timeline / index.html, when a white flash appears at a cut or crossfade seam (especially on dark films), when reasoning about why a transition opacity dip shows through, or when verifying the render-s
- **Teknoloji:** api-anahtari, canvas, gsap, html, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, ★69086, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** otomatik

### svg-character-animation  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pivot, zaman çizelgesi ve kare örnekleme kurallarını verir.
- **Ne zaman:** Açıklayıcı videoda konuşan/hareket eden 2D karakter gerektiğinde. · **Ne zaman değil:** 3D karakter; hazır Lottie dosyası oynatılacaksa (lottie-bodymovin).
- **Teknoloji:** svg, gsap, remotion, hyperframes · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → birincil · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Remotion'da GSAP'ı kareye bağlama gibi kritik kuralları doğru veriyor.

### visual-style  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper.design'a uygular; hazır stil galerisi (Swiss, Saul Bass, Game Boy…) içerir.
- **Ne zaman:** Video veya sunum serisinde tutarlı renk, tipografi, hareket ve ruh hali tanımlanacaksa. · **Ne zaman değil:** Kod tabanlı web tasarım sistemi/token kurulumu (a-tasarim/02 skilleri daha uygun).
- **Teknoloji:** markdown, html
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** gorsel-stil-sistemi → birincil · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni
- **Boyut:** 81 KB (SKILL.md 6.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik mod tablosu ve galeri; a-tasarim/02 tasarım sistemi skilleriyle kısmen örtüşür.
