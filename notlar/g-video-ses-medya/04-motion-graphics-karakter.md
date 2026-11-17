# 04-motion-graphics-karakter — Video, Ses ve AI Medya Üretimi

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **16/36**

### blender  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 80 (A)

- **Ne yapar:** Çekim tanımından (JSON shot spec) Blender'da 3D sahne, karakter oyunculuğu ve ürün çekimi üretir: tam film, başka yapılar için klipler (moviepy, video işi, kurgu programı) ya da Remotion içinde öğeler (şeffaf karakter, 3D dizüstü/telefon üzerinde ekran, kameranın geri çekildiği kart, içe aktarılan 3D model). JSON ile tarif edilen çizgi film kadrosu, sahneler, geometriyle doğrulanan kameralar ve harekete oturtulmuş ses olayları.
- **Ne zaman:** Toolkit ve Blender 4.2+ kuruluysa 3D karakterli kısa film, ürün/arayüz 3D tanıtımı ve başka videoya gömülecek 3D klipler. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) ve Blender 4.2+. Basit 2D video için gereksiz ağır (karakterli film 2.2 sn/kare, 2-3 saatlik oturumlar). Kütüphanedeki 3d-asset-generation (varlık üretimi) ya da Three.js işleri için değil.
- **Teknoloji:** blender, python, ffmpeg, remotion, node · **Paketler:** Blender 4.2+, claude-code-video-toolkit (tools/blender_render.py, lib/blender/), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-sahne-render → birincil · **Roller:** 3d-gelistirici, motion-graphics-sanatcisi
- **Boyut:** 48 KB (SKILL.md 47.5 KB, yük buyuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (koşullu). Çok ayrıntılı (47 KB): spec biçimi, kamera ve oyunculuk eylemleri, süre tahmini, çok oturumlu film süreci; çıktıların deterministik ve denetlenebilir olması güçlü. Boyut büyük (bağlam yükü büyük), Blender kurulu değilse kullanılamaz. Lisans MIT (toolkit); Blender GPL, içe aktarılan 3D modellerin lisansı ayrıca denetlenmeli. Açıklama 1068 karakterdi (Codex 1024 sınırı): aciklama_duzeltme ile 897'ye indirilmiş; skill dosyası değişmedi. Güvenlik: betik yok; Blender'ı ayrı sürece açan yerel render, dış ağ adımı yok. Ücret: ucretsiz (Blender ve toolkit kodu ücretsiz). Sabit yol yok. Örtüşme: yeni grup 3d-sahne-render (3d-varlik-uretimi ve Three.js grupları farklı iş).

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

### explainer-default  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 66 (B)

- **Ne yapar:** Make a clean 45–90 second product demo video for any software product, rendered from code to MP4 with music. Airy light canvas, short centred lines the camera pushes into, the product's own UI rebuilt and shown up close as it is used (typing, results, tables, clicks), integrations, and a logo close. Use when someone wants a product demo, launch video, feature walkthrough or "how it works" video fo
- **Teknoloji:** canvas, css, ffmpeg, html, node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1347, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 21.2 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** otomatik

### explainer-engaging  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 66 (B)

- **Ne yapar:** Make a 10–30 second continuous-shot explainer for any product, rendered from code to MP4 with sound. One hero element (a ball, a cursor, a file, a message) travels through the product's workflow laid out as stations on one big canvas; the camera follows it, each station reacts as it passes, then the camera pulls out to reveal the whole journey. Use when someone wants an engaging, story-driven, one
- **Teknoloji:** canvas, css, ffmpeg, html, node, playwright, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1347, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 23.2 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** otomatik

### explainer-high-energy  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 66 (B)

- **Ne yapar:** Make a 12–20 second high-energy motion-graphics promo for any product, rendered from code to MP4 with synthesised music. Fast beat-locked scene changes, kinetic typography, a shape that carries across every transition, a HUD frame. Use when someone wants a hype reel, teaser, launch sting or showreel-style promo for a product, app or brand.
- **Teknoloji:** canvas, css, ffmpeg, html, node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1347, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 20.3 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** otomatik

### huashu-art-motion  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** 辅助艺术动画与解说任务：35 种艺术风格配方、9 种解说语法、分镜与确定性 Canvas 绘制工具。按宿主时间轴实现，素材与导出使用宿主能力。
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 424 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### kinetic-reel  ·  tuzhechen2005/opus-video-skills @ dafed5b  ·  puan 66 (B)

- **Ne yapar:** Make kinetic-typography motion reels (MP4) in code: showreels, portfolio or work reels, product promos, intro films, "motion design"-style videos with bold condensed type, HUD micro-type, black/cream/lime palette, three.js generative layers (particle terrain, liquid marble, chrome knot, particle clouds), shape-continuity transitions and a synthesized, beat-locked score. Canvas 2D + WebGL rendered 
- **Teknoloji:** canvas, css, ffmpeg, html, node, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tuzhechen2005 (kisi, ★525, son güncelleme 2026-11-16, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3637 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** Node, headless Chrome ve ffmpeg gerekir (p5.js + p5.brush / three.js ile kare kare çizim); ilk kullanımda npm paketleri kurulur.
- **İnceleme:** otomatik

### layers  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 65 (B)

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

### manim-video  ·  browser-use/video-use @ 43cfc56  ·  puan 84 (A)

- **Ne yapar:** Manim Community Edition ile matematik ve teknik animasyon hattı: 3Blue1Brown tarzı kavram anlatımı, denklem türetme, algoritma görselleştirme, mimari diyagram, veri hikayesi, makale özeti ve 3B sahneler. PLAN (plan.md) → KOD (tek script.py, sahne başına sınıf) → RENDER → BİRLEŞTİR → isteğe bağlı SES → İNCELE akışı; geometri önce cebir sonra yaklaşımı ve referans belgeleri (denklemler, kamera/3B, grafikler, sorun giderme).
- **Ne zaman:** Algoritma, matematik ve sistem mimarisi anlatan kısa eğitim videoları; sahne sahne planlı, kodla üretilen deterministik animasyonlar; arka plan ve tarayıcı gerektirmez. · **Ne zaman değil:** Serbest biçimli tasarım/hareket grafiği için HyperFrames ya da Remotion; yalnız Manim API bilgisi isteniyorsa manimce-best-practices; fikri sahnelere dökmek için manim-composer. video-use içinde de aynı içerikli kopya vardır (ust_skill).
- **Teknoloji:** manim, python, latex, ffmpeg · **Paketler:** manim (Community Edition 0.20+), LaTeX (pdflatex; macOS: mactex), ffmpeg, Python 3.10+, isteğe bağlı: manim-voiceover (ElevenLabs/gTTS/Azure/pyttsx3)
- **Claude / Codex:** tam / tam
- **Geliştirici:** browser-use (kurum, ★31088, son güncelleme 2026-10-08, lisans MIT)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 98 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** Manim Community Edition (pip install manim; v0.20+), LaTeX (pdflatex; macOS: mactex), ffmpeg ve Python 3.10+. scripts/setup.sh bunları denetler (kurmaz). Anahtar, ağ ya da hesap gerekmez; isteğe bağlı sesli anlatım için manim-voiceover (ElevenLabs/gTTS/Azure/pyttsx3).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı; manimce-best-practices API birincili, bu skill üretim hattı). Yaratıcı çıtası yüksek ve referansları geniş (13 belge). Güvenlik: betik tek dosya scripts/setup.sh ve yalnız komut varlığı kontrol eder (kurulum yapmaz); SKILL.md pip install manim / brew install mactex önerir (kullanıcı çalıştırır); ağdan indirip çalıştıran satır, gizli anahtar isteği ya da genel klasöre yazma yok. İsteğe bağlı TTS (ElevenLabs) metni üçüncü tarafa gönderir (yalnız o seçilirse). Ücret: ücretsiz; LaTeX kurulumu büyük (~GB).

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

### motion-broll  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 61 (C)

- **Ne yapar:** Turn a talking-head video and its transcript into motion-graphic B-roll timed to the speaker's words, in a continuous one-shape style (one element that morphs and never cuts, driven by a cursor, spring motion). Use when someone gives a video (and ideally a transcript) and asks for motion graphics, B-roll, animated cutaways or overlays.
- **Teknoloji:** canvas, css, ffmpeg, html, node, playwright, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Barty-Bart (kisi, ★1347, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 209 KB (SKILL.md 8.7 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** otomatik

### motion-doctrine  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 99 (A)

- **Ne yapar:** Çok sahneli videonun bağımsız slaytlar yığını değil tek kesintisiz kamera hareketi gibi hissettirmesi için üst düzey hareket yasası: vektör yasası (çıkış girişi belirler, Z ölçek işareti), filmin akıntısı, taşıyıcı öğeler, nedensel hareket, Seam Gate doğrulayıcısı, boşta sallanma yasağı ve doruk öncesi durgunluk. Alt teknik skillere (cut-the-curve, seam-craft, oversized-cursor) yönlendirir.
- **Ne zaman:** Çok sahneli HyperFrames videosunda geçiş ve hareket dili kurulmadan önce. · **Ne zaman değil:** Tek sahnelik kısa grafiklerde; HyperFrames dışı web animasyonunda.
- **Teknoloji:** hyperframes, gsap, node · **Paketler:** hyperframes (npx), node
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 44 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kendini genel/üst akış hareket rehberlerinin ÜSTÜNDE ilan ediyor — bu bir ev stili tercihi, evrensel kural değil. seam-gate doğrulayıcı betiği somut. · 2026-11-12 yeniden incelendi (ab66e5b): seam-gate betiği `__player.seek` artık asenkron beklendiği için await ile çalışıyor (eskiden t=0'ı ölçüp tüm dikişleri hatalı gösterebilirdi); referans notu eklendi. Değerlendirme aynı.

### object-separation  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 66 (B)

- **Ne yapar:** Separate a person, product or hand from the background in a video, on the user's own computer with SAM 2. Scans the machine first to pick the right model size, then outputs the same video with the separated subject highlighted in green, plus frame-by-frame masks. Use when someone wants to separate, isolate, cut out or rotoscope something in a video.
- **Teknoloji:** ffmpeg, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1347, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** SAM 2 modelini yerelde çalıştırır: pip install ile Python bağımlılıkları kurulur, model dosyaları indirilir (disk, RAM; GPU önerilir). Hiçbir şey yüklenmez.
- **İnceleme:** otomatik

### oil-motion  ·  nexu-io/open-design @ 987b247  ·  puan 95 (A)

- **Ne yapar:** 处理视频和序列帧，编译滚动、指针、拖动与状态驱动的网页动效；内含本地媒体处理脚本和运行时。新素材生成使用宿主工具。
- **Teknoloji:** api-anahtari, css, ffmpeg, html, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 318 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### painted-animation  ·  tuzhechen2005/opus-video-skills @ dafed5b  ·  puan 66 (B)

- **Ne yapar:** Make hand-painted watercolour-and-ink cartoon videos (MP4) with code — p5.js + p5.brush rendered frame by frame in headless Chrome, encoded with ffmpeg — starring Clawd or any character. Use when the user asks to make an animation, animated short, cartoon, music video, lyric video, animated GIF/loop or "a video of Clawd…", or mentions the PDoomVideo / ClaudeAnimationBase approach. Covers storyboar
- **Teknoloji:** ffmpeg, html, node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** tuzhechen2005 (kisi, ★525, son güncelleme 2026-11-16, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 6169 KB (SKILL.md 7.4 KB, yük kucuk) · **Bağımlılık:** Node, headless Chrome ve ffmpeg gerekir (p5.js + p5.brush / three.js ile kare kare çizim); ilk kullanımda npm paketleri kurulur.
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

### product-launch-motion  ·  AbubakrChan/product-launch-motion @ edbfb10  ·  puan 80 (A)

- **Ne yapar:** Use when asked to make a launch video, product film, motion design piece, UI motion reel, Dribbble-style UI animation or animated brand/logo sting — anything rendered to MP4 from HTML with a cursor, morphing UI, springs, beat-synced music and SFX. Carries Chan's full creative direction (one shape never cut, blur content swaps, springs, real data, logo slams, no creative limits) and the proven buil
- **Teknoloji:** canvas, css, ffmpeg, html, playwright, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AbubakrChan (kisi, ★487, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 51 KB (SKILL.md 8.9 KB, yük orta) · **Bağımlılık:** Node, ffmpeg ve HyperFrames benzeri HTML'den MP4 render hattı gerekir; müzik/SFX için yerel araçlar.
- **İnceleme:** otomatik

### remotion-explainer-video  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 83 (A)

- **Ne yapar:** Make an explainer video in Remotion: a narrated 30–90s video that explains a product, feature, idea or process, with a voiceover and burned-in captions. Script → voiceover → word timings → one snapcn scene per beat → captions → render. Uses snapcn's Remotion components (@snapcn/punch-lines, status-cycle, count-grid, laptop-frame, word-captions, karaoke-captions and more) for every beat instead of 
- **Teknoloji:** api-anahtari, node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.2 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### remotion-kinetic-typography  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 83 (A)

- **Ne yapar:** Make kinetic typography in Remotion: animated text, title cards, a headline reveal, rotating words, a highlighted phrase, a line that morphs into its payoff, or a run of bold statements. Uses snapcn's text components (@snapcn/text-reveal, type-morph, text-highlight, word-flip, punch-lines, text-swell and more), which pivot scale on the measured baseline so type doesn't judder or shake the way hand
- **Teknoloji:** api-anahtari, node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### remotion-launch-video  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 81 (A)

- **Ne yapar:** Build a product launch video in Remotion from a brief: a launch film, feature announcement, version release, Product Hunt / X / LinkedIn promo or landing-page hero video. Composes snapcn's hand-tuned Remotion scenes (@snapcn/announce-title, hero-launch, type-morph, count-grid, wordmark-cut and more) instead of hand-animating every shot, so the result does not look like every other AI video. Brief 
- **Teknoloji:** api-anahtari, canvas, css, ffmpeg, node, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 12.1 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### remotion-logo-animation  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 83 (A)

- **Ne yapar:** Make a logo animation in Remotion: a logo reveal, logo sting, intro or outro bumper, brand reveal or end card for a video, launch or YouTube channel. Uses snapcn's hand-tuned Remotion logo scenes (@snapcn/logo-flicker, logo-assemble, logo-collapse, block-wordmark, wordmark-cut) with your real logo, instead of a logo that fades in and scales up. Triggers: logo animation, logo reveal, logo sting, an
- **Teknoloji:** api-anahtari, node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### remotion-motion-graphics  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 81 (A)

- **Ne yapar:** Make a short, design-led motion graphic in Remotion, where the motion is the message: kinetic typography, a title card, a stat count-up, a logo sting or brand reveal, a social-proof overlay, an image-gallery opener or burned-in captions. Usually under 10s, up to about 30s. Built from snapcn's hand-tuned Remotion components (@snapcn/text-reveal, type-morph, punch-lines, logo-flicker, count-grid, or
- **Teknoloji:** api-anahtari, css, node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 8.5 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### remotion-product-demo  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 81 (A)

- **Ne yapar:** Build a product demo video in Remotion from a real screen recording or screenshots: a SaaS walkthrough, feature demo, onboarding clip, CLI or developer-tool demo, AI app demo or App Store preview. Uses snapcn's Remotion components (@snapcn/screen-recording, cursor-track, laptop-frame, phone-frame, terminal-simulator, prompt-send, answer-stream, status-cycle) so the camera push, clicks, device fram
- **Teknoloji:** api-anahtari, canvas, node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 10.3 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### seam-craft  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 92 (A)

- **Ne yapar:** Sahneden sahneye geçişlerin ana zaman çizelgesinde doğru birleşmesi için render önkoşulları: koyu filmlerde kesmede beyaz parlamayı önleyen opak sahne zemini, enjektörün sarmalayıcıları nasıl örtüştürdüğü, son kareyi tuttuğu ve şablon kodunu nasıl yerleştirdiği.
- **Ne zaman:** Ana index.html birleştirilirken veya geçişte beyaz parlama/opaklık sızması görüldüğünde. · **Ne zaman değil:** Geçiş seçimi için (cut-the-curve); tek sahnelik işlerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa ve tek bir hata sınıfına odaklı, HeyGen launch-video enjektörüne özgü ayrıntılar içeriyor.

### snapcn  ·  shadcn-labs/snapcn @ 18b973d  ·  puan 81 (A)

- **Ne yapar:** Build Remotion videos with snapcn — a shadcn registry of copy-paste animation components and timeline-driven UI primitives. Use when composing video scenes, adding text animations, transitions, backgrounds, UI blocks, brand/social cards, or full compositions in a Remotion project. Triggers include "snapcn", "video component", "add animation", "text reveal", "product demo video", "remotion componen
- **Teknoloji:** api-anahtari, canvas, node, react, remotion, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★652, son güncelleme 2026-11-12, lisans MIT)
- **Durum:** tercih
- **Boyut:** 176 KB (SKILL.md 12.1 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** otomatik

### stil  ·  yerel/site @ 23cb314  ·  puan 68 (B)

- **Ne yapar:** Referans görselden (poster, reklam, ekran görüntüsü) yeniden kullanılabilir bir animasyonlu anlatım videosu stili çıkarır ve bunu her konuda çalışan uzun, kendi başına yeten bir stil prompt'u (stil-prompt.md) olarak yazar; prompt'u taze oturumda test edip düzeltir. Yanında 11 hazır stilin tablosu ve 7'sinin uzun prompt'u gelir (cam, risograf, kesik kâğıt, izometrik, düz vektör, kinetik tipografi, parçacık).
- **Ne zaman:** Bir görselin tarzında motion graphics / explainer video serisi yapılacaksa ya da hazır stillerden biriyle (HTML + window.seek + başsız Chrome + ffmpeg) konu anlatım videosu üretilecekse. · **Ne zaman değil:** Görseli birebir kopyalamak, logo ya da düzen almak için değil; HyperFrames/Remotion kompozisyonu ya da genel tasarım sistemi dosyası gerekiyorsa (visual-style) değil. Kurulu araç istemeyen hızlı tek görsel işi için ağır.
- **Teknoloji:** html, canvas, webgl, ffmpeg, playwright · **Paketler:** puppeteer ya da playwright (başsız Chrome), ffmpeg, mlx-whisper ya da openai-whisper (ses açıksa)
- **Claude / Codex:** tam / tam
- **Geliştirici:** Smokich (kisi, ★0, son güncelleme 2026-11-17, lisans belirtilmemiş)
- **Durum:** tercih · **Örtüşme:** gorsel-stil-sistemi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 295 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Yazar Smokich (YouTube @DevSmokich, smokich.gosem.dev/stil); uzun prompt'lar Michael Szach'ın stil kütüphanesinden uyarlama; lisans belirtilmemiş, kişisel kullanım (2026-11-15'ten beri kaynak yerel/site; sahip ve lisans site-takip.json'dan gelir, K-57). Güvenlik: eksik araçları kendisi kurar (Puppeteer/Playwright Chromium indirir, Whisper, ffmpeg); ses efekti açıksa Openverse'ten anahtarsız CC0 ses indirir; stil testi taze oturum/alt ajanda 2-3 tur çalışır, jeton harcar; site genel ~/.claude/skills klasörüne kurmayı söyler, kütüphanede yalnız skill-ekle.py ile projeye kurulur. Gizli değer ya da sistem dosyasına yazan komut yok. Ayrıntı ve dosya özetleri: site/stil/KAYNAK.md.
- **Not:** visual-style ile aynı iş ailesi (görselden stil çıkarma); stil, explainer videosuna özel ve kendi render yolunu (window.seek + başsız Chrome + ffmpeg) tanımlar. Uzun prompt'u olmayan 4 stil: kagit-poster, konstruktivist, bilim, ascii. 2026-11-15: 11 kısa stil kartı references/stiller/kartlar/ altına eklendi (yalnız stil metni, komut yok); yeniden inceleme ana oturumda kapatıldı.

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

### upload  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 67 (B)

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

### wake  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 65 (B)

- **Ne yapar:** Turn one image into a ~5 s looping animation. 把一张图做成约 5 秒的循环动图。
- **Teknoloji:** api-anahtari, canvas, ffmpeg, html, node, python, react, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★256, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 549 KB (SKILL.md 21.7 KB, yük orta)
- **İnceleme:** otomatik
