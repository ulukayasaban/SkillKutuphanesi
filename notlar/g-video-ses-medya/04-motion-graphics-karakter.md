# 04-motion-graphics-karakter — Video, Ses ve AI Medya Üretimi

_Motion graphics, Manim, karakter animasyonu/rig, görsel stil_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **28/36**

### blender  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 80 (A)

- **Ne yapar:** Çekim tanımından (JSON shot spec) Blender'da 3D sahne, karakter oyunculuğu ve ürün çekimi üretir: tam film, başka yapılar için klipler (moviepy, video işi, kurgu programı) ya da Remotion içinde öğeler (şeffaf karakter, 3D dizüstü/telefon üzerinde ekran, kameranın geri çekildiği kart, içe aktarılan 3D model). JSON ile tarif edilen çizgi film kadrosu, sahneler, geometriyle doğrulanan kameralar ve harekete oturtulmuş ses olayları.
- **Ne zaman:** Toolkit ve Blender 4.2+ kuruluysa 3D karakterli kısa film, ürün/arayüz 3D tanıtımı ve başka videoya gömülecek 3D klipler. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) ve Blender 4.2+. Basit 2D video için gereksiz ağır (karakterli film 2.2 sn/kare, 2-3 saatlik oturumlar). Kütüphanedeki 3d-asset-generation (varlık üretimi) ya da Three.js işleri için değil.
- **Teknoloji:** blender, python, ffmpeg, remotion, node · **Paketler:** Blender 4.2+, claude-code-video-toolkit (tools/blender_render.py, lib/blender/), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2697, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** 3d-sahne-render → birincil · **Roller:** 3d-gelistirici, motion-graphics-sanatcisi
- **Boyut:** 64 KB (SKILL.md 64.0 KB, yük buyuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (koşullu). Çok ayrıntılı (47 KB): spec biçimi, kamera ve oyunculuk eylemleri, süre tahmini, çok oturumlu film süreci; çıktıların deterministik ve denetlenebilir olması güçlü. Boyut büyük (bağlam yükü büyük), Blender kurulu değilse kullanılamaz. Lisans MIT (toolkit); Blender GPL, içe aktarılan 3D modellerin lisansı ayrıca denetlenmeli. Açıklama 1068 karakterdi (Codex 1024 sınırı): aciklama_duzeltme ile 897'ye indirilmiş; skill dosyası değişmedi. Güvenlik: betik yok; Blender'ı ayrı sürece açan yerel render, dış ağ adımı yok. Ücret: ucretsiz (Blender ve toolkit kodu ücretsiz). Sabit yol yok. Örtüşme: yeni grup 3d-sahne-render (3d-varlik-uretimi ve Three.js grupları farklı iş).

### canvas-procedural-animation  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 85 (A)

- **Ne yapar:** p5.js/Canvas ile karakter destekleyici prosedürel hareket: parçacık, hava efekti, yaprak, squash/stretch ve basit yürüme döngüleri; zaman/kare tabanlı deterministik durum önerir.
- **Ne zaman:** Karaktere eşlik eden çevre efektleri veya basit prosedürel gövdeler gerektiğinde. · **Ne zaman değil:** Karmaşık yüz oyunculuğu (SVG rig daha uygun) veya kare-kesin final render.
- **Teknoloji:** p5js, canvas, javascript · **Paketler:** p5
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → alternatif · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Çok kısa (ipucu düzeyi); kaynak bağlantıları doğru.

### character-animation-qa  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** Karakter animasyonunu sunmadan önce katmanlı kontrol: şema doğrulama, varlık kontrolü, Playwright ile tarayıcı önizleme ve ekran görüntüsü, kare örnekleme, ffprobe ile final MP4 kontrolü ve pass/revise/fail kararı.
- **Ne zaman:** Karakter animasyonu önizlemesi veya finali teslim edilmeden önce. · **Ne zaman değil:** Karakter içermeyen genel video kontrolü (hyperframes-cli inspect/validate).
- **Teknoloji:** playwright, ffmpeg · **Paketler:** playwright, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, qa-erisilebilirlik
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa kontrol listesi; OpenMontage karakter hattının şema adlarına atıf yapıyor.

### character-rigging  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 85 (A)

- **Ne yapar:** Yerel 2D karakter animasyonu için veri güdümlü rig paketi: parçalar, pivotlar, katman sırası, kısıtlar ve görünümler; her karakteri jenerik çalışma zamanına veri paketi olarak tanımlar.
- **Ne zaman:** SVG/2D karakter animasyonu için rig planı hazırlarken. · **Ne zaman değil:** 3D rig (Blender/Three.js); hazır Lottie animasyonu yeterliyse.
- **Teknoloji:** svg, gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 2 KB (SKILL.md 1.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ama doğru kalıplar; OpenMontage rig_plan artefaktına göre yazılmış.

### cut-the-curve  ·  heygen-com/hyperframes @ 8a69ea0  ·  puan 100 (A)

- **Ne yapar:** Hız eşlemeli sahne geçişleri kataloğu: zoom-through, ters zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut; ayrıca sahne içi waterfall giriş ve üç fazlı 'nudge' grup kaydırma. Ayna power4 easing ile kısmi hareket eşleme, boyuta göre bulanıklık ve 10/65/25 kaydırma oranı gibi sayısal kurallar verir.
- **Ne zaman:** Herhangi bir geçiş, metin vuruşu devri, kinetik metin girişi veya grup yeniden konumlandırma yazılmadan önce. · **Ne zaman değil:** Tek sahnelik statik işlerde; HyperFrames/GSAP dışı ortamlarda.
- **Teknoloji:** gsap, hyperframes · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★87822, son güncelleme 2026-11-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 28 KB (SKILL.md 18.4 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Sayısal, uygulanabilir teknik kataloğu; GSAP örnekleri dahil. Ev stili kökenli olsa da genel geçer değerde.

### explainer-default  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 72 (B)

- **Ne yapar:** Herhangi bir yazılım ürünü için temiz, 45-90 saniyelik ürün demo videosu (varsayılan 60 sn) üretir, koddan MP4'e, müzikle: ferah açık tuval, kısa ortalanmış satırlar, kamera ürünün kendi arayüzüne yaklaşır. Tek mesajlık bir brif ister (ürün, akılda kalacak tek şey, marka, biçim, süre, müzik, yönlendirme), sonra tek HTML sayfası (kare = zamanın saf fonksiyonu) ve hareket bulanıklığı + ses ile render eder.
- **Ne zaman:** Bir yazılım ürününün ana sayfasına konacak sakin, premium ürün demosu (60 sn); sahte sayı/logo/alıntı uydurmadan, gerçek arayüz metniyle. · **Ne zaman değil:** 10-20 sn'lik hype/promo (explainer-high-energy), 10-30 sn'lik tek çekim iş akışı filmi (explainer-engaging) ya da anlatımlı/seslendirmeli video için değil.
- **Teknoloji:** html-canvas, node, ffmpeg, hyperframes · **Paketler:** node, ffmpeg, başsız tarayıcı
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 23 KB (SKILL.md 21.2 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). 21 KB tek dosyada brif, senaryo ve yapım kuralları; 'asla gerçek olmayan olgu uydurma', logo yalnız verilmişse, sayı yalnız kaynaktan kuralları iyi. Ücret: ucretsiz (müzik koddan sentezlenir). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: temiz — kullanıcı URL verirse sayfayı okur (web fetch); betik/anahtar yok. Örtüşme: urun-tanitim-filmi grubunda alternatif (onetake birincil); üç explainer-* stil kardeşidir.

### explainer-engaging  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 72 (B)

- **Ne yapar:** Herhangi bir ürün için 10-30 saniyelik kesintisiz tek çekim açıklayıcı (varsayılan 12 sn, sorunsuz döngü) üretir: tek bir kahraman öğe (top, imleç, dosya, mesaj) ürünün iş akışını büyük bir tuval üzerinde istasyonlar olarak gezer, her istasyon ona tepki verir; sonda 'şimdi nasıl çalıştığını anladın' geri çekilmesi vardır. Koddan MP4'e, sesle.
- **Ne zaman:** Ürünün iş akışını (3-6 adım) tek kesintisiz çekimde anlatan kısa film. · **Ne zaman değil:** Uzun anlatımlı demolar (explainer-default), hype promo (explainer-high-energy) ya da çok adımlı detaylı eğitim için değil.
- **Teknoloji:** html-canvas, node, ffmpeg · **Paketler:** node, ffmpeg, başsız tarayıcı
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 25 KB (SKILL.md 23.2 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Kahraman öğe ve istasyon fikri güçlü; kurallar (hiçbir şey kesilmez, kahraman yok olmaz) net. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: temiz — betik yok. Örtüşme: urun-tanitim-filmi grubunda alternatif; fikren onetake ('kesintisiz tanıtım filmi') ile en çok örtüşen bu skil.

### explainer-high-energy  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 72 (B)

- **Ne yapar:** Herhangi bir ürün için 12-20 saniyelik yüksek enerjili hareket grafiği promosu (varsayılan 15 sn, 128 BPM, 8 ölçü) üretir: vuruşa kilitli sahne değişimleri, kinetik tipografi, her geçişte göz taşıyan şekil (kıvılcım → çizgi → ...), HUD mikro yazısı ve sentezlenmiş müzik. 6-8 sahne planı ve 'spark open', 'brand slam', 'kinetic triplet' gibi sahne türleri anlatılır.
- **Ne zaman:** Ürün lansmanı için kısa, sosyal paylaşıma uygun vuruşlu tanıtım. · **Ne zaman değil:** Sakin ürün demosu (explainer-default), kesintisiz iş akışı filmi (explainer-engaging), anlatımlı video için değil.
- **Teknoloji:** html-canvas, node, ffmpeg · **Paketler:** node, ffmpeg, başsız tarayıcı
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 22 KB (SKILL.md 20.3 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Vuruş ızgarası ve 'taşıyıcı şekil' disiplini iyi, sahne türleri somut. Ücret: ucretsiz (sentezlenmiş müzik). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: temiz — betik yok. Örtüşme: urun-tanitim-filmi grubunda alternatif; kinetic-reel/motion-showreel ile üslup benzerliği var.

### huashu-art-motion  ·  nexu-io/open-design @ e033aad  ·  puan 97 (A)

- **Ne yapar:** 辅助艺术动画与解说任务：35 种艺术风格配方、9 种解说语法、分镜与确定性 Canvas 绘制工具。按宿主时间轴实现，素材与导出使用宿主能力。
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★108838, son güncelleme 2026-11-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 424 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### kinetic-reel  ·  tuzhechen2005/opus-video-skills @ dafed5b  ·  puan 72 (B)

- **Ne yapar:** Kinetik tipografi hareket reelleri (MP4) kodla yapar: showreel, portföy/iş reel'i, ürün promosu, giriş filmi; kalın daraltılmış yazı, HUD mikro yazısı, siyah/krem/limon paleti, three.js üretken katmanları, WebGL son işlem. Her kare t'nin saf fonksiyonudur; çalıştırılabilir bir template/ (17 sn demo) ve 84 sn'lik tam örnek (work-reel-26) ile gelir, müzik Node'da aynı ipucu dosyasından sentezlenir.
- **Ne zaman:** Editoryal, yüksek enerjili kinetik tipografi reel/portföy filmi; gerçek veri/rakam kaynağı net olan işler. · **Ne zaman değil:** Ürün arayüzü demosu, anlatımlı açıklayıcı ya da gerçek çekim kurgusu için değil. Veri yoksa şematik olarak etiketler, uydurmaz.
- **Teknoloji:** three.js, webgl, html-canvas, node, ffmpeg, chrome · **Paketler:** node, headless Chrome, ffmpeg, three.js (npm)
- **Claude / Codex:** tam / tam
- **Geliştirici:** tuzhechen2005 (kisi, ★553, son güncelleme 2026-11-16, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** kodla-showreel → birincil · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 1433 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** Node, headless Chrome ve ffmpeg gerekir (p5.js + p5.brush / three.js ile kare kare çizim); ilk kullanımda npm paketleri kurulur.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT. 'Gerçekler kutsaldır' ilkesi (yalnız kaynaktaki rakamlar, şematik olanlar HUD'da SCHEMATIC etiketli, tıbbi işte etkililik iddiası yok), sağlam çalışma akışı ve çalıştırılabilir şablon. Sabit yol: SKILL.md:22'deki bash ~/.claude/skills/kinetic-reel/scripts/new_project.sh kurulumda proje içi yola çevrilir. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION; render.mjs kısmı John Heibel MIT notuyla). Güvenlik: DİKKAT (orta) — new_project.sh npm paketleri kurar (ilk kullanımda), başsız Chrome ve ffmpeg çalıştırır; anahtar yok. Örtüşme: kodla-showreel grubunda birincil (self-contained şablonlu); motion-showreel alternatif.

### layers  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 65 (B)

- **Ne yapar:** Split one image into editable layers (PSD + PNG). 把一张图拆成图层（PSD + PNG）。
- **Teknoloji:** api-anahtari, canvas, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★375, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 12.4 KB, yük orta)
- **İnceleme:** otomatik

### manim-composer  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Belirsiz bir video fikrini 3Blue1Brown tarzında sahne sahne plana (scenes.md) dönüştürür: konuyu araştırır, hedef kitle/kapsam sorularını sorar, anlatı yayı, görsel öğeler, renk paleti ve uygulama sırasını yazar.
- **Ne zaman:** Matematik/bilim açıklayıcı videosu planlanırken, Manim kodundan önce. · **Ne zaman değil:** Kod yazımı (manimce/manimgl-best-practices); matematik dışı tanıtım videoları.
- **Teknoloji:** manim
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, planlayici
- **Boyut:** 22 KB (SKILL.md 4.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İyi planlama şablonu ve 3b1b ilkeleri; references/ dosyaları faydalı.

### manim-video  ·  browser-use/video-use @ 43cfc56  ·  puan 84 (A)

- **Ne yapar:** Manim Community Edition ile matematik ve teknik animasyon hattı: 3Blue1Brown tarzı kavram anlatımı, denklem türetme, algoritma görselleştirme, mimari diyagram, veri hikayesi, makale özeti ve 3B sahneler. PLAN (plan.md) → KOD (tek script.py, sahne başına sınıf) → RENDER → BİRLEŞTİR → isteğe bağlı SES → İNCELE akışı; geometri önce cebir sonra yaklaşımı ve referans belgeleri (denklemler, kamera/3B, grafikler, sorun giderme).
- **Ne zaman:** Algoritma, matematik ve sistem mimarisi anlatan kısa eğitim videoları; sahne sahne planlı, kodla üretilen deterministik animasyonlar; arka plan ve tarayıcı gerektirmez. · **Ne zaman değil:** Serbest biçimli tasarım/hareket grafiği için HyperFrames ya da Remotion; yalnız Manim API bilgisi isteniyorsa manimce-best-practices; fikri sahnelere dökmek için manim-composer. video-use içinde de aynı içerikli kopya vardır (ust_skill).
- **Teknoloji:** manim, python, latex, ffmpeg · **Paketler:** manim (Community Edition 0.20+), LaTeX (pdflatex; macOS: mactex), ffmpeg, Python 3.10+, isteğe bağlı: manim-voiceover (ElevenLabs/gTTS/Azure/pyttsx3)
- **Claude / Codex:** tam / tam
- **Geliştirici:** browser-use (kurum, ★31399, son güncelleme 2026-10-08, lisans MIT)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 98 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** Manim Community Edition (pip install manim; v0.20+), LaTeX (pdflatex; macOS: mactex), ffmpeg ve Python 3.10+. scripts/setup.sh bunları denetler (kurmaz). Anahtar, ağ ya da hesap gerekmez; isteğe bağlı sesli anlatım için manim-voiceover (ElevenLabs/gTTS/Azure/pyttsx3).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı; manimce-best-practices API birincili, bu skill üretim hattı). Yaratıcı çıtası yüksek ve referansları geniş (13 belge). Güvenlik: betik tek dosya scripts/setup.sh ve yalnız komut varlığı kontrol eder (kurulum yapmaz); SKILL.md pip install manim / brew install mactex önerir (kullanıcı çalıştırır); ağdan indirip çalıştıran satır, gizli anahtar isteği ya da genel klasöre yazma yok. İsteğe bağlı TTS (ElevenLabs) metni üçüncü tarafa gönderir (yalnız o seçilirse). Ücret: ücretsiz; LaTeX kurulumu büyük (~GB).

### manimce-best-practices  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** Manim Community Edition için en iyi uygulamalar: sahne yapısı, mobject'ler, animasyonlar, LaTeX/MathTex, 3D sahneler, kamera, stil, CLI ve yapılandırma; çalışan örnekler ve şablonlar içerir.
- **Ne zaman:** 'from manim import *' kullanan matematik/bilim animasyonlarında. · **Ne zaman değil:** ManimGL (manimlib) projelerinde; matematik dışı motion graphic işlerinde.
- **Teknoloji:** manim, python, latex · **Paketler:** manim, latex, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 206 KB (SKILL.md 5.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kapsamlı kural seti, test edilmiş örnekler; CE topluluk sürümü daha yaygın olduğu için birincil.

### manimgl-best-practices  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** ManimGL (Grant Sanderson'ın 3b1b sürümü) için en iyi uygulamalar: InteractiveScene, t2c ile Tex renklendirme, kamera çerçevesi, -se etkileşimli mod, checkpoint_paste ve 3D render.
- **Ne zaman:** 'from manimlib import *' kullanan veya etkileşimli geliştirme isteyen projelerde. · **Ne zaman değil:** Manim Community Edition projelerinde (API'ler farklı).
- **Teknoloji:** manim, python, opengl, latex · **Paketler:** manimgl, latex
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** manim-animasyon → alternatif · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 729 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 5
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kaliteli; kurulumu ve sürüm uyumu CE'ye göre zahmetli.

### motion-broll  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 69 (B)

- **Ne yapar:** Konuşan kafa videosu ve transkriptinden, konuşmacının sözlerine zamanlanmış hareket grafiği B-roll klipleri üretir: tek bir şekil hiç kesilmeden boyut, köşe ve renk değiştirir, içerik kısa bulanıklıkla değişir, imleç gerçek tıklamalarla yönlendirir, yay hareketi kullanır. Çıktı: editöre bırakılacak klip seti, B-roll'lü önizleme render'ı ve iki HTML sayfası (klipleri gez, önce/sonra karşılaştır). Motor (engine/), referans ve 6 bitmiş örnek paketli.
- **Ne zaman:** Konuşan kafa videosuna (transkript ya da SRT ile) tek şekilli, imleç güdümlü hareket grafiği B-roll eklemek; hafif/orta/yoğun yoğunluk seçilir. · **Ne zaman değil:** Tam kompozisyon motoru istenen ürün filmleri ya da transkript/sözler olmayan videolar için değil.
- **Teknoloji:** playwright, gsap, node, python, ffmpeg · **Paketler:** node, python3, ffmpeg, playwright + chromium (setup.sh), faster-whisper (transkript yoksa)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusan-kafa-gorsel-katman → birincil · **Roller:** motion-graphics-sanatcisi, video-kurgu-render
- **Boyut:** 209 KB (SKILL.md 8.7 KB, yük orta) · **Bağımlılık:** Videolar HyperFrames/Remotion/GSAP, Node ve ffmpeg ile yerelde render edilir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kendi kendine yeten (engine, build/render betikleri, yazı tipleri, referans, 6 bitmiş örnek), tek turluk görüşme, kalite çıtası olarak örnekler. Motor API'si referansta. Codex uyumu 'uyarlanabilir' (AskUserQuestion varsayımı). Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION), yazı tipi Geist OFL. Güvenlik: DİKKAT (orta) — setup.sh Playwright + Chromium'u motion/node_modules altına kurar, yerel Python/JS betikleri; anahtar yok. Örtüşme: konusan-kafa-gorsel-katman grubunda birincil (kendi kendine yeten, transkript güdümlü).

### motion-doctrine  ·  heygen-com/hyperframes @ 8a69ea0  ·  puan 99 (A)

- **Ne yapar:** Çok sahneli videonun bağımsız slaytlar yığını değil tek kesintisiz kamera hareketi gibi hissettirmesi için üst düzey hareket yasası: vektör yasası (çıkış girişi belirler, Z ölçek işareti), filmin akıntısı, taşıyıcı öğeler, nedensel hareket, Seam Gate doğrulayıcısı, boşta sallanma yasağı ve doruk öncesi durgunluk. Alt teknik skillere (cut-the-curve, seam-craft, oversized-cursor) yönlendirir.
- **Ne zaman:** Çok sahneli HyperFrames videosunda geçiş ve hareket dili kurulmadan önce. · **Ne zaman değil:** Tek sahnelik kısa grafiklerde; HyperFrames dışı web animasyonunda.
- **Teknoloji:** hyperframes, gsap, node · **Paketler:** hyperframes (npx), node
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★87822, son güncelleme 2026-11-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 44 KB (SKILL.md 11.7 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kendini genel/üst akış hareket rehberlerinin ÜSTÜNDE ilan ediyor — bu bir ev stili tercihi, evrensel kural değil. seam-gate doğrulayıcı betiği somut. · 2026-11-12 yeniden incelendi (ab66e5b): seam-gate betiği `__player.seek` artık asenkron beklendiği için await ile çalışıyor (eskiden t=0'ı ölçüp tüm dikişleri hatalı gösterebilirdi); referans notu eklendi. Değerlendirme aynı.

### object-separation  ·  Barty-Bart/motion-graphics @ 3d83d98  ·  puan 72 (B)

- **Ne yapar:** Videodaki bir kişiyi, ürünü ya da eli arka plandan kullanıcının kendi bilgisayarında SAM 2 ile ayırır: önce makineyi tarar (GPU/Apple Silicon/CPU) ve uygun model boyutunu seçer (large 898 MB, base-plus 323 MB, tiny 156 MB), çıktı olarak ayrılan özneyi yeşille vurgulanmış aynı videoyu verir. Hiçbir şey yüklenmez; silinebilir tek klasörde sanal ortam kurar.
- **Ne zaman:** Videoda öznenin (kişi/ürün/el) arka plandan ayrılması, maske üretmek (ör. konuşmacının arkasına metin koymak). · **Ne zaman değil:** Uzun klipler CPU'da (kare başı ~5 sn) için; öznesi belirsiz sahneler için; sabit kare hızı olmayan videolar için.
- **Teknoloji:** python, pytorch, sam2, opencv, ffmpeg · **Paketler:** python 3.10+, torch, transformers, opencv-python-headless, pillow, numpy, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** Barty-Bart (kisi, ★1428, son güncelleme 2026-10-13, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** video-nesne-ayirma → birincil · **Roller:** ai-medya-uretici, video-kurgu-render
- **Boyut:** 11 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** SAM 2 modelini yerelde çalıştırır: pip install ile Python bağımlılıkları kurulur, model dosyaları indirilir (disk, RAM; GPU önerilir). Hiçbir şey yüklenmez.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Hazır, test edilmiş kod blokları, model seçimi tablosu ve süre beklentileri, silinebilir sanal ortam, açık 'hiçbir şey yüklenmez'. Kategori: 04-motion-graphics-karakter'de bırakıldı (taşımak arşiv yolunu değiştirir; keşif açısından 01-video-uretim-montaj daha uygun olabilir, karar kullanıcıda). Ücret: ucretsiz (yerel). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION); SAM 2 modeli Meta'nın Apache-2.0 lisanslı. Güvenlik: DİKKAT (orta) — pip install (torch, transformers) ve Hugging Face'ten model indirir (898 MB'a kadar). Örtüşme: video-nesne-ayirma grubunda birincil (HyperFrames remove-background daha hafif alternatiftir).

### oil-motion  ·  nexu-io/open-design @ e033aad  ·  puan 95 (A)

- **Ne yapar:** 处理视频和序列帧，编译滚动、指针、拖动与状态驱动的网页动效；内含本地媒体处理脚本和运行时。新素材生成使用宿主工具。
- **Teknoloji:** api-anahtari, css, ffmpeg, html, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★108838, son güncelleme 2026-11-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 318 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### painted-animation  ·  tuzhechen2005/opus-video-skills @ dafed5b  ·  puan 64 (C)

- **Ne yapar:** Kodla suluboya ve mürekkep görünümlü el boyaması çizgi film videoları (MP4) yapar: p5.js + p5.brush, başsız Chrome'da kare kare render, ffmpeg ile kodlama; Clawd ya da herhangi bir karakter başrolde. Önce hikâye panosu (STORYBOARD.md), sahne sahne inşa, hareketi çıplak gözle kontrol; 156 sn'lik müzik klibinden damıtılmış yöntem, şablon, örnek ve ritim ızgarası (beat_grid.py).
- **Ne zaman:** Karakterli, boyalı görünümlü kısa çizgi film ya da şarkı/lirik klibi (LRC ile) istendiğinde. · **Ne zaman değil:** Fotoğraf/metin/video'yu boyalı görünüme çevirmek için (p5-paint-animation); marka/net tipografi gereken işler; hızlı üretim için değil (kare başı render pahalı).
- **Teknoloji:** p5-brush, p5js, node, ffmpeg, chrome · **Paketler:** node, headless Chrome, ffmpeg, p5 + p5.brush (npm), python3 (beat_grid.py)
- **Claude / Codex:** tam / tam
- **Geliştirici:** tuzhechen2005 (kisi, ★553, son güncelleme 2026-11-16, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** p5-boyali-animasyon → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 1268 KB (SKILL.md 7.4 KB, yük kucuk) · **Bağımlılık:** Node, headless Chrome ve ffmpeg gerekir (p5.js + p5.brush / three.js ile kare kare çizim); ilk kullanımda npm paketleri kurulur.
- **İnceleme:** yeniden-incelenecek · kalite 3/5 — Karar: ALTERNATİF (niş). Yöntem sağlam (storyboard önce, her kare t'nin saf fonksiyonu, hareketi kare kare izleme), ama belirli bir karaktere (Clawd) ve görsel dile bağlı örneklerle yüklü. Sabit yol: SKILL.md:17'deki bash ~/.claude/skills/painted-animation/scripts/new_project.sh kurulumda proje içi yola çevrilir. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION; şablon kısmı John Heibel MIT). Güvenlik: DİKKAT (orta) — new_project.sh npm install çalıştırır, Chrome/ffmpeg denetler. Örtüşme: p5-boyali-animasyon grubunda alternatif (hikâye/karakter çizgi film); p5-paint-animation birincil.

### pose-library-design  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** Veri güdümlü 2D animasyon için yeniden kullanılabilir poz kütüphanesi, aksiyon döngüleri ve ifade durumları tasarlar; hazırlık→aksiyon→bekleme→oturma oyunculuk kalıbını önerir.
- **Ne zaman:** Karakterin duygu ve aksiyonlarını tutarlı pozlarla anlatmak gerektiğinde. · **Ne zaman değil:** Tek seferlik basit hareketler; rig henüz yoksa (önce character-rigging).
- **Teknoloji:** gsap, remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru; tek başına derinliği sınırlı.

### product-launch-motion  ·  AbubakrChan/product-launch-motion @ edbfb10  ·  puan 72 (B)

- **Ne yapar:** Lansman videosu, ürün filmi, hareket tasarımı parçası, UI hareket reel'i ya da animasyonlu marka damgası üretir (HTML'den MP4): imleç, şekil dönüştüren arayüz, yaylar, vuruşa oturan kesimler. 'Tek şekil, hiç kesme', içerik kısa bulanıklıkla değişir, yaylar (hafif aşım), öndeki/arkadaki kenar farklı yaylarla gibi katı hareket kuralları; yazarın verbatim istemleri (references/prompts.md) şartname olarak verilir.
- **Ne zaman:** Dribbble tarzı UI hareketi / lansman filmi; yönetmen duruşuyla (yaratıcı karar günlüğü: DECISION) özgün bir kompozisyon. · **Ne zaman değil:** Şablon ya da ürün sitesini kopyalama işleri için değil (kendi kuralı da bunu yasaklıyor); hızlı, ölçülmüş şablon istenirse onetake/explainer-* kullan.
- **Teknoloji:** html-canvas, node, ffmpeg, gsap · **Paketler:** node, ffmpeg, HTML'den MP4 render hattı (HyperFrames benzeri)
- **Claude / Codex:** tam / tam
- **Geliştirici:** AbubakrChan (kisi, ★518, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 51 KB (SKILL.md 8.9 KB, yük orta) · **Bağımlılık:** Node, ffmpeg ve HyperFrames benzeri HTML'den MP4 render hattı gerekir; müzik/SFX için yerel araçlar.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Hareket kuralları değerli ve somut; ama metin yazarın kişisel tercih belgesi gibi yazılmış (kişi adıyla, belirli bir müşteri filmine atıflarla), 'yaratıcılıkta kısıt yok, izin isteme' duruşu bazı kullanıcılar için uygunsuz olabilir. Kurulum, betik yok. Ücret: ucretsiz. Lisans: MIT. Güvenlik: temiz — yalnız belge. Örtüşme: urun-tanitim-filmi grubunda alternatif (aynı 'tek şekil hiç kesme' ilkesi onetake'te de var; onetake birincil).

### remotion-explainer-video  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 82 (A)

- **Ne yapar:** Remotion'da seslendirmeli 30-90 saniyelik açıklayıcı video: senaryo → seslendirme → kelime zamanlamaları → her vuruş için bir snapcn sahnesi → yakılmış altyazılar → render. Her vuruşta elle yazılmış slayt yerine snapcn bileşenleri (punch-lines, status-cycle, count-grid, laptop-frame, word-captions, karaoke-captions...) kullanılır; 'bileşen adı uydurma, her metin prop'unu doldur' kuralları.
- **Ne zaman:** Ürün/özellik/süreç açıklayan anlatımlı Remotion videosu ("explainer video", "how it works video"). · **Ne zaman değil:** Remotion kullanılmıyorsa; sade tek şekilli ürün filmi için (explainer-*, onetake); Pro bileşen lazımsa abonelik gerekir.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI, TTS sağlayıcısı (kullanıcının seçimi)
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 8 KB (SKILL.md 7.2 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Akış net, kural listesi (her vuruş bir bileşen, ad uydurmama) iyi. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: urun-tanitim-filmi grubunda alternatif (Remotion + snapcn yolu, seslendirmeli açıklayıcıya uygun).

### remotion-kinetic-typography  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 82 (A)

- **Ne yapar:** Remotion'da kinetik tipografi: animasyonlu metin, başlık kartları, başlık reveal'ı, dönen kelimeler, vurgulu ifade, ödeme cümlesine dönüşen satır. snapcn metin bileşenleri (text-reveal, type-morph, text-highlight, word-flip, punch-lines, text-swell...) ölçülmüş taban çizgisinde ölçeklendirir ve geometricPrecision kullanır; tarayıcıda elle yazılan metnin 'takılma' ve 'titreme' hatalarından kaçınır, 30 fps için ayarlı yavaşlamalar.
- **Ne zaman:** Remotion projesinde yazının taşıdığı kısa video: başlık animasyonu, metin reveal, 'kelimeleri patlat'. · **Ne zaman değil:** Remotion dışında; showreel/portföy reel'i için kinetic-reel; uzun anlatım için değil.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** remotion-kisa-grafik → tamamlayıcı · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 8 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Teknik gerekçe ölçüme dayalı (piksel titreşimi 0,284→0,014 px, şekil kayması %3,41→%0,22 iddiası). Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: remotion-kisa-grafik grubunda tamamlayıcı (remotion-motion-graphics birincil); showreel işi için kodla-showreel grubuna da yakın.

### remotion-launch-video  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 81 (A)

- **Ne yapar:** Remotion'da brife dayalı 15-30 saniyelik ürün lansman filmi: lansman, özellik duyurusu, sürüm çıkışı, Product Hunt/X/LinkedIn tanıtımı ya da landing hero videosu. snapcn'in el ayarlı sahneleri (announce-title, hero-launch, type-morph, count-grid, wordmark-cut...) ile brif → storyboard → bileşen kurulumu → kompozisyon → render denetimi → yayın akışı; 'AI video gibi görünmeme' hedefi.
- **Ne zaman:** Remotion projesinde lansman/duyuru videosu ("launch video", "release video", "Product Hunt video"). · **Ne zaman değil:** Remotion yoksa; kodundan hızlı proje tanıtımı için brag; ayrı ve özgün hareket kuralları için product-launch-motion/onetake.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 14 KB (SKILL.md 12.1 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Net iş akışı ve 'önce katalog, sonra interpolate/spring' kuralı. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: urun-tanitim-filmi grubunda alternatif (Remotion yolu); aynı işi brag/product-launch-motion/onetake yapar. saas-motion-kit bu kütüphanede kayıtlı değil (izle kararı), bu karşılaştırmaya girmedi.

### remotion-logo-animation  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 74 (B)

- **Ne yapar:** Remotion'da 2-6 saniyelik logo animasyonu: logo reveal, damga, giriş/çıkış kartı, marka açılışı. snapcn logo sahneleri (logo-flicker, logo-assemble, logo-collapse, block-wordmark, wordmark-cut) kullanıcının gerçek logosu ve adıyla; 'solarak girip ölçeklenen' sıradan logo yerine gerçek marka filmlerinden çıkarılmış kalıplar.
- **Ne zaman:** Remotion'da logo açılışı, intro/outro bumper'ı ya da bitiş kartı. · **Ne zaman değil:** Remotion dışı işler; gerçek logo/ad verilmeyen işler (sahneler snapcn markasıyla gelir, mutlaka prop değiştirilmeli).
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** remotion-kisa-grafik → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 8 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı, dar). Kısa ve odaklı, ama kapsamı tek bir iş. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: remotion-kisa-grafik grubunda tamamlayıcı.

### remotion-motion-graphics  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 81 (A)

- **Ne yapar:** Remotion'da hareketin mesaj olduğu kısa, tasarım odaklı hareket grafiği (genellikle <10 sn, en çok ~30 sn): kinetik tipografi, başlık kartı, istatistik sayacı, logo damgası, sosyal kanıt bindirmesi, görsel galeri açılışı, yakılmış altyazı. snapcn bileşenleri (text-reveal, type-morph, punch-lines, logo-flicker, count-grid, orbit-gallery...) ile 'üretilmiş değil tasarlanmış' görünüm.
- **Ne zaman:** Remotion'da tek satır/tek sayı/tek logo odaklı kısa hareket grafiği. · **Ne zaman değil:** Remotion yoksa; uzun anlatımlı videolar için değil.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** remotion-kisa-grafik → birincil · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 10 KB (SKILL.md 8.5 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Remotion hareket grafiği için genel giriş noktası, diğer remotion-* skillerinin üst kümesi gibi. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: remotion-kisa-grafik grubunda birincil; kinetic-typography ve logo-animation bunun özelleşmiş dilimleridir.

### remotion-product-demo  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 81 (A)

- **Ne yapar:** Gerçek bir ekran kaydı ya da ekran görüntülerinden Remotion'da 20-45 saniyelik ürün demosu: SaaS yürüyüşü, özellik demosu, onboarding, CLI/geliştirici aracı demosu, AI uygulaması demosu, App Store önizlemesi. snapcn bileşenleriyle (screen-recording, cursor-track, laptop-frame, phone-frame, terminal-simulator, prompt-send, answer-stream, status-cycle) kamera yaklaşması, tıklamalar, cihaz çerçeveleri ve yazılan komutlar hazır gelir.
- **Ne zaman:** Elde ekran kaydı olan bir ürünün cilalı demo videosunu Remotion'da yapmak. · **Ne zaman değil:** Ekran kaydı üretmek için değil (playwright-recording gibi); Remotion kullanılmıyorsa; sahte arayüz üretimi için synthetic-ui-demo.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 12 KB (SKILL.md 10.3 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Elle animasyonda ele veren kısımları (sabit hızlı imleç, sonsuz ease'li zoom, bir anda dolan terminal) bileşenlere bırakıyor. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: ekran-kaydi-demo grubunda tamamlayıcı (kayıt alınır, bu skil ile cilalanır; playwright-recording birincil).

### seam-craft  ·  heygen-com/hyperframes @ 8a69ea0  ·  puan 92 (A)

- **Ne yapar:** Sahneden sahneye geçişlerin ana zaman çizelgesinde doğru birleşmesi için render önkoşulları: koyu filmlerde kesmede beyaz parlamayı önleyen opak sahne zemini, enjektörün sarmalayıcıları nasıl örtüştürdüğü, son kareyi tuttuğu ve şablon kodunu nasıl yerleştirdiği.
- **Ne zaman:** Ana index.html birleştirilirken veya geçişte beyaz parlama/opaklık sızması görüldüğünde. · **Ne zaman değil:** Geçiş seçimi için (cut-the-curve); tek sahnelik işlerde.
- **Teknoloji:** hyperframes, html, css · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★87822, son güncelleme 2026-11-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa ve tek bir hata sınıfına odaklı, HeyGen launch-video enjektörüne özgü ayrıntılar içeriyor.

### snapcn  ·  shadcn-labs/snapcn @ 3f09f3a  ·  puan 81 (A)

- **Ne yapar:** Remotion videoları için snapcn: kopyala-yapıştır animasyon bileşenleri ve zaman çizelgesi güdümlü arayüz ilkellerinin shadcn kayıt defteri (shadcn add @snapcn/text-reveal). Metin animasyonları, geçişler, arka planlar, UI blokları, marka/sosyal kartlar, terminal simülatörü, cihaz çerçeveleri, karaoke altyazılar ve tam kompozisyonlar; kod proje içinde components/snap-cn/ altında sana aittir. 50'den fazla referans dosyası (anatomi, anti-desenler, arketipler, bileşen sayfaları) paketli.
- **Ne zaman:** Remotion projesinde cilalı video sahneleri, metin reveal'ları, cihaz çerçeveleri, altyazı bileşenleri gerektiğinde ("remotion component", "text reveal", "terminal simulator"). · **Ne zaman değil:** Remotion olmayan projelerde (HyperFrames vb.) için değil; Pro bileşen gerektiren işler abonelik ister.
- **Teknoloji:** remotion, react, typescript, shadcn · **Paketler:** remotion, shadcn CLI, isteğe bağlı: @snapcn/mcp ve SNAPCN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** shadcn-labs (kurum, ★670, son güncelleme 2026-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 176 KB (SKILL.md 12.1 KB, yük orta) · **Bağımlılık:** Remotion ve Node gerekir; snapcn Pro bileşenleri SNAPCN_API_KEY ister (ücretli kısım isteğe bağlı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve düzenli (bileşen kataloğu, anatomi, tasarım ve hareket ilkeleri, anti-desen listesi); kod sende kalır. Güvenlik: DİKKAT (orta) — çalışma anında snapcn.dev'den katalog ve bileşen sayfalarını çeker (uzak içerik, yönlendirici ?ref= izleme parametreli) ve shadcn CLI ile bileşen kodunu projeye indirir; Pro bileşenler SNAPCN_API_KEY ister. Uzak içerik talimat sayılmamalı. Ücret: kismen (açık bileşenler MIT/ücretsiz; Pro isteğe bağlı abonelik). Lisans: MIT. Örtüşme: remotion-cercevesi grubunda tamamlayıcı (bileşen kayıt defteri, çerçeve skili değil); remotion-* kardeşleri bu skilin üstüne kurulu iş akışlarıdır.

### stil  ·  yerel/site @ 23cb314  ·  puan 68 (B)

- **Ne yapar:** Referans görselden (poster, reklam, ekran görüntüsü) yeniden kullanılabilir bir animasyonlu anlatım videosu stili çıkarır ve bunu her konuda çalışan uzun, kendi başına yeten bir stil prompt'u (stil-prompt.md) olarak yazar; prompt'u taze oturumda test edip düzeltir. Yanında 11 hazır stilin tablosu ve 7'sinin uzun prompt'u gelir (cam, risograf, kesik kâğıt, izometrik, düz vektör, kinetik tipografi, parçacık).
- **Ne zaman:** Bir görselin tarzında motion graphics / explainer video serisi yapılacaksa ya da hazır stillerden biriyle (HTML + window.seek + başsız Chrome + ffmpeg) konu anlatım videosu üretilecekse. · **Ne zaman değil:** Görseli birebir kopyalamak, logo ya da düzen almak için değil; HyperFrames/Remotion kompozisyonu ya da genel tasarım sistemi dosyası gerekiyorsa (visual-style) değil. Kurulu araç istemeyen hızlı tek görsel işi için ağır.
- **Teknoloji:** html, canvas, webgl, ffmpeg, playwright · **Paketler:** puppeteer ya da playwright (başsız Chrome), ffmpeg, mlx-whisper ya da openai-whisper (ses açıksa)
- **Claude / Codex:** tam / tam
- **Geliştirici:** Smokich (kisi, ★0, son güncelleme 2026-11-22, lisans belirtilmemiş)
- **Durum:** tercih · **Örtüşme:** gorsel-stil-sistemi → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 295 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Yazar Smokich (YouTube @DevSmokich, smokich.gosem.dev/stil); uzun prompt'lar Michael Szach'ın stil kütüphanesinden uyarlama; lisans belirtilmemiş, kişisel kullanım (2026-11-15'ten beri kaynak yerel/site; sahip ve lisans site-takip.json'dan gelir, K-57). Güvenlik: eksik araçları kendisi kurar (Puppeteer/Playwright Chromium indirir, Whisper, ffmpeg); ses efekti açıksa Openverse'ten anahtarsız CC0 ses indirir; stil testi taze oturum/alt ajanda 2-3 tur çalışır, jeton harcar; site genel ~/.claude/skills klasörüne kurmayı söyler, kütüphanede yalnız skill-ekle.py ile projeye kurulur. Gizli değer ya da sistem dosyasına yazan komut yok. Ayrıntı ve dosya özetleri: site/stil/KAYNAK.md.
- **Not:** visual-style ile aynı iş ailesi (görselden stil çıkarma); stil, explainer videosuna özel ve kendi render yolunu (window.seek + başsız Chrome + ffmpeg) tanımlar. Uzun prompt'u olmayan 4 stil: kagit-poster, konstruktivist, bilim, ascii. 2026-11-15: 11 kısa stil kartı references/stiller/kartlar/ altına eklendi (yalnız stil metni, komut yok); yeniden inceleme ana oturumda kapatıldı.

### svg-character-animation  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** SVG parçalarından oluşan karakter rig'lerini GSAP, CSS dönüşümleri, Remotion kare kontrolü ve HyperFrames uyumlu önizlemeyle canlandırır; pivot, zaman çizelgesi ve kare örnekleme kurallarını verir.
- **Ne zaman:** Açıklayıcı videoda konuşan/hareket eden 2D karakter gerektiğinde. · **Ne zaman değil:** 3D karakter; hazır Lottie dosyası oynatılacaksa (lottie-bodymovin).
- **Teknoloji:** svg, gsap, remotion, hyperframes · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** karakter-animasyonu → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Remotion'da GSAP'ı kareye bağlama gibi kritik kuralları doğru veriyor.

### threejs-world-generation  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** Metinden veya yapılandırılmış özetten belirlenimci, düzenlenebilir Three.js dünyaları: arazi, semantik bölgeler, prosedürel biyomlar, landmark'lar, kamera fly-through; OpenMontage threejs_world aracı ve HyperFrames ile entegre.
- **Ne zaman:** OpenMontage/HyperFrames hattında sinematik 3D ortam videosu. · **Ne zaman değil:** Web sayfasına gömülü 3D, tek nesne, düz paralaks sahne; OpenMontage yoksa.
- **Teknoloji:** three.js, hyperframes, openmontage, python, blender · **Paketler:** OpenMontage (~/.openmontage), hyperframes
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** three-dunya-uretimi → birincil · **Roller:** video-kompozisyon
- **Boyut:** 16 KB (SKILL.md 8.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Fidelity katmanları ve kalite kapıları titiz yazılmış. Dikkat: OpenMontage kurulumu ve threejs_world aracı şart (~/.openmontage/tools/graphics/threejs_world.py mevcut); 3d-asset-generation, hyperframes-* skillerine atıf yapıyor; kategori olarak video hattına yakın ama Three.js içeriği nedeniyle burada kalabilir. Kategori düzeltildi (05-3d-webgl → g-video-ses-medya/04-motion-graphics-karakter): web 3D'si değil, OpenMontage video boru hattının parçası (tools.graphics.threejs_world).

### upload  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 67 (B)

- **Ne yapar:** Share a film to the lemo-wake gallery. 把动图投稿到作品墙。
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★375, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 6.3 KB, yük kucuk)
- **İnceleme:** otomatik

### visual-style  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Taşınabilir görsel tasarım sistemi dosyası (visual-style.md) oluşturur, web sitesi/video/PDF'den çıkarır ve HeyGen, HTML slayt, Figma, paper.design'a uygular; hazır stil galerisi (Swiss, Saul Bass, Game Boy…) içerir.
- **Ne zaman:** Video veya sunum serisinde tutarlı renk, tipografi, hareket ve ruh hali tanımlanacaksa. · **Ne zaman değil:** Kod tabanlı web tasarım sistemi/token kurulumu (a-tasarim/02 skilleri daha uygun).
- **Teknoloji:** markdown, html
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★82109, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** gorsel-stil-sistemi → birincil · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 81 KB (SKILL.md 6.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik mod tablosu ve galeri; a-tasarim/02 tasarım sistemi skilleriyle kısmen örtüşür.

### wake  ·  lemomo-ai/lemo-wake @ f070df8  ·  puan 65 (B)

- **Ne yapar:** Turn one image into a ~5 s looping animation. 把一张图做成约 5 秒的循环动图。
- **Teknoloji:** api-anahtari, canvas, ffmpeg, html, node, python, react, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** lemomo-ai (kisi, ★375, son güncelleme 2026-10-17, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 549 KB (SKILL.md 21.7 KB, yük orta)
- **İnceleme:** otomatik
