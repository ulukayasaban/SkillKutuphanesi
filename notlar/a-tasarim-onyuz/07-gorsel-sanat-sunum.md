# 07-gorsel-sanat-sunum — Tasarım ve Ön Yüz

_Poster/canvas tasarımı, generative art, slayt, GIF_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **8/23**

### algorithmic-art  ·  anthropics/skills @ ca45fc4  ·  puan 81 (A)

- **Ne yapar:** Önce bir 'algoritmik felsefe' (manifesto .md) yazdırıp ardından bunu seed'li rastgelelik ve parametre paneliyle p5.js üretken sanatına (akış alanları, parçacık sistemleri) çevirir. Çıktı .md + etkileşimli HTML görüntüleyici + .js algoritmadır; şablon olarak viewer.html ve generator_template.js verilir.
- **Ne zaman:** Kodla üretken sanat, akış alanı/parçacık görselleri, seed ile tekrarlanabilir etkileşimli sanat parçası istendiğinde. · **Ne zaman değil:** Ürün arayüzü, veri görselleştirme (d3-viz) veya 3D sahne (threejs-*) için değil; statik poster için canvas-design daha uygun. Mevcut bir sanatçının işini taklit etmek için kullanılmaz.
- **Teknoloji:** p5.js, canvas, html, javascript · **Paketler:** p5.js (CDN)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** uretken-sanat → birincil
- **Boyut:** 58 KB (SKILL.md 19.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Niş ama iyi kurgulanmış; felsefe -> kod iki adımı ve seed'li parametre paneli tutarlı çıktı verir. Dikkat: viewer.html p5.js (cdnjs) ve Google Fonts'u CDN'den çeker, çevrimdışı çalışmaz; lisans alanı 'LICENSE.txt' (Anthropic) ve açık kaynak değil; sanat odaklı olduğundan çoğu ürün projesinde gerekmez.

### canvas-design  ·  anthropics/skills @ ca45fc4  ·  puan 89 (A)

- **Ne yapar:** Bir 'tasarım felsefesi' (hareket adı + 4-6 paragraf manifesto) yazdırıp ardından bunu %90 görsel / %10 metin olan özgün PNG veya PDF posterine, sanat parçasına dönüştürür. Yaklaşık 5 MB'lık OFL lisanslı font klasörü (canvas-fonts) ile gelir ve iki geçişli iyileştirme ister.
- **Ne zaman:** Poster, kapak görseli, statik sanat/tasarım parçası, marka kampanya görseli üretirken (PNG/PDF). · **Ne zaman değil:** Etkileşimli/web arayüzü (frontend-design, design-taste-frontend); çok sayfalı sunum (slides, pptx); veri grafiği (d3-viz).
- **Teknoloji:** canvas, python, png, pdf · **Paketler:** pillow / reportlab (agent ortamına göre)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** statik-gorsel-poster → birincil · **Roller:** ui-tasarimci
- **Boyut:** 5424 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Marka-sunum profilinin ek skilli; özgünlük ve 'zanaat' vurgusu ile şablon görünümünü engeller, fontlar yerel ve OFL. Dikkat: skill klasörü ~5,4 MB (ağırlıkla ttf); SKILL.md 11,7 KB. Yalnızca SKILL.md bağlama girer. Betik yok, ağ/anahtar yok. LICENSE.txt Anthropic'e ait, repo lisans alanı boş.

### card-twitter  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Twitter quote or data card designed to pair with a post.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** otomatik

### card-xiaohongshu  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### d3-viz  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** d3.js ile özel, etkileşimli veri görselleştirmeleri (ağ/grafik, hiyerarşi, coğrafi harita, geçişli grafikler) kurmayı anlatır; React ve vanilla JS şablonları (chart-template.jsx, interactive-template.jsx), renk şeması ve ölçek başvuruları ile örnek veri içerir. Hazır grafik kütüphanesinin yetmediği özgün işler içindir.
- **Ne zaman:** Standart grafik kütüphanesinde olmayan özel SVG görselleştirme, force-directed ağ, zoom/brush etkileşimi, haritalar. · **Ne zaman değil:** Hızlı standart grafik/dashboard (dataviz skilli veya grafik kütüphanesi); 3D görselleştirme (threejs-*).
- **Teknoloji:** d3, svg, react, javascript · **Paketler:** d3
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** veri-gorsellestirme → birincil · **Roller:** frontend-muhendis
- **Boyut:** 80 KB (SKILL.md 21.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Konu odaklı, başvuru dosyaları ve şablonlar kaliteli; kategoride tek veri görselleştirme skilli. Dikkat: registry'de bagimlilik uyarısı var ama d3-viz'in kendi içeriği OpenMontage komutu çağırmıyor, bağımsız çalışır. Repo lisansı AGPL-3.0 (skill dosyasında ayrı lisans yok); aynı skill ~/.claude/skills'te zaten global kurulu (globalde: ayni). d3 CDN'den yüklenebilir. · 2026-11-12 yeniden incelendi: içerik değişmedi (kaynak OpenMontageInc/OpenMontage fecb9a1'e taşındı), değerlendirme aynı.

### deck-guizang-editorial  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune).
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### deck-open-slide-canvas  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template.
- **Teknoloji:** canvas, html, react, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### deck-swiss-international  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange).
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 5.8 KB, yük kucuk)
- **İnceleme:** otomatik

### digits-fintech-swiss-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Swiss-grid fintech deck template in black / warm paper / neon-lime contrast. Use when users ask for premium data-story slides with strict modular layout, bold numeric cards, restrained motion, and keyboard/click navigation in one HTML file.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### editorial-burgundy-principles-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Editorial studio deck template in burgundy / blush / muted-gold palette. Use when users ask for premium manifesto or culture slides with pill tags, large typographic statements, principle cards, and guided keyboard/click navigation.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### field-notes-editorial-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Editorial "Field Notes" report template with soft paper background, serif hero typography, rounded pastel insight cards, and a retention chart panel. Use when users ask for a premium magazine-style business report, board memo one-pager, or elegant data storytelling layout.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### frontend-slides  ·  zarazhangrui/frontend-slides @ 9906a34  ·  puan 78 (B)

- **Ne yapar:** Sıfırdan ya da PPTX'ten dönüştürerek, bağımlılıksız tek dosyalık animasyonlu HTML sunum üretir. Sabit 16:9 sahne, stil ön ayarları ve 'bold template' paketiyle önce görsel önizleme gösterip seçtirir; isteğe bağlı PDF dışa aktarma ve Vercel'e yayınlama betikleri var.
- **Ne zaman:** Konuşma/pitch için tarayıcıda çalışan, tasarımı özgün HTML sunum; elindeki .pptx'i web sunumuna çevirmek. · **Ne zaman değil:** Chart.js veri grafikli pazarlama destesi için slides; .pptx çıktısı gerekiyorsa pptx; video slayt gösterisi için slideshow.
- **Teknoloji:** html, css, javascript · **Paketler:** python-pptx (sadece PPTX dönüştürme), playwright chromium (sadece PDF), vercel CLI (isteğe bağlı yayın)
- **Claude / Codex:** tam / tam
- **Geliştirici:** zarazhangrui (kisi, ★31888, son güncelleme 2026-06-23, lisans MIT)
- **Durum:** tercih · **Örtüşme:** html-sunum → alternatif
- **Boyut:** 1770 KB (SKILL.md 27.5 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (html-sunum; birincil slides kalır). MIT, 31,8k★. Repodaki plugins/ kopyası birebir aynı olduğu için dosya_haric ile çıkarıldı. Ücret: kısmen; Vercel yayını isteğe bağlı (hesap açtırır), yerel HTML ücretsiz. Ağ: npx vercel/playwright yalnız istenirse.

### html-ppt-retro-quarterly-review  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Retro Quarterly Review presentation template in a bold blue + orange editorial language. Use when users ask for a high-impact quarterly review / roadmap deck with heavyweight slab headlines, clean cream paper sections, structured grids, and fast premium motion pacing (3 slides, each hold under 3s in video mode).
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### mockup-device-3d  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable composition.
- **Teknoloji:** canvas, css, html, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### playground  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.
- **Teknoloji:** css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★46120, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### poster-hero  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Vertical poster or Moments-style share image with strong visual impact.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### ppt-keynote  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### pptx-html-fidelity-audit  ·  nexu-io/open-design @ 987b247  ·  puan 95 (A)

- **Ne yapar:** Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missing italic/em, lost styling, off-rhythm spacing), and re-export with strict footer-rail + cursor-flow layout discipline. Use this skill whenever the user has a .pptx that was generated from an HTML slide deck and asks to compare/audit/verify/fix the export — including phras
- **Teknoloji:** canvas, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 57 KB (SKILL.md 13.8 KB, yük orta)
- **İnceleme:** otomatik

### slack-gif-creator  ·  anthropics/skills @ ca45fc4  ·  puan 82 (A)

- **Ne yapar:** Slack için animasyonlu GIF üretimi: PIL ile kare çizimi, GIFBuilder, easing fonksiyonları, kare birleştirici ve Slack boyut/FPS/renk sınırlarını denetleyen doğrulayıcı. Emoji (128x128) ve mesaj (480x480) GIF'leri için kısa, sade bir araç seti.
- **Ne zaman:** Slack emoji veya mesaj GIF'i, kısa döngülü basit animasyon isteklerinde. · **Ne zaman değil:** Video/hareketli grafik (hyperframes, motion-graphics); karmaşık sahneler ve gerçek görsel efektler.
- **Teknoloji:** python, pillow, imageio, numpy, gif · **Paketler:** pillow, imageio, imageio-ffmpeg, numpy
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** slack-gif → birincil
- **Boyut:** 43 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Küçük, bağımsız, Python modülleri düzenli; Slack sınırlarını doğrulaması işe yarar. Dikkat: 'pip install pillow imageio numpy' ister (--break-system-packages yok; venv önerilir). Composio sürümü eski ve farklı bir kod tabanı (ayrı alternatif).

### slides  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 3a13158  ·  puan 82 (A)

- **Ne yapar:** Chart.js, tasarım token'ları, yerleşim kalıpları ve metin yazım formülleri ile stratejik HTML sunum (pitch deck, pazarlama slaytı) üretir; `slides create` alt komutu references/create.md'yi yükler. Yerleşim, strateji ve copywriting bilgisini ayrı referans dosyalarında tutar.
- **Ne zaman:** HTML tabanlı pitch deck, veri destekli pazarlama sunumu; marka-sunum profili için. · **Ne zaman değil:** PowerPoint/.pptx çıktısı gerekiyorsa pptx; video slayt gösterisi için slideshow (HyperFrames); sıfırdan görsel poster için canvas-design.
- **Teknoloji:** html, chart.js, css · **Paketler:** chart.js (CDN)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★145229, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih · **Örtüşme:** html-sunum → birincil · **Roller:** dokuman-yazari
- **Boyut:** 19 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. İçerik stratejisi ve yerleşim bilgisi iyi, MIT. Dikkat: referanslar `python ../design-system/scripts/search-slides.py` (kardeş design-system skill'ine ve onun veri tabanına) başvurur; design-system kurulu değilse bu komutlar kırık kalır, registry bunu bağımlılık olarak işaretlemiyor. Chart.js jsdelivr CDN'den yüklenir. SKILL.md yalnızca 1,7 KB. slideshow (video) ve design (claudekit) ile karıştırılmamalı.

### sunum-sitesi  ·  avenoxai/higgsfield-studio @ 6b5fe34  ·  puan 56 (C)

- **Ne yapar:** Bir video, konuşma ya da ders bölümü için koyu temalı, sinematik tek sayfalık sunum sitesi kurar: hareketli panoramalı giriş, bölüm rayı gezinmesi, resimli sözlük kartları ve canlı döngü videoları. Görseller GPT Image 2, döngüler Seedance ile Higgsfield üzerinden üretilir. Türkçe.
- **Ne zaman:** Videoya ya da derse eşlik eden tek sayfalık sunum/özet sitesi. · **Ne zaman değil:** Slayt destesi (PowerPoint, HTML deck) isteniyorsa sunum skilleri. Görsel ve döngü üretimi Higgsfield kredisi harcar; kendi görsellerinle ücretsiz kurulabilir. Repoda lisans dosyası yok.
- **Teknoloji:** html, css, javascript, higgsfield
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** avenoxai (kisi, ★14, son güncelleme 2026-08-19, lisans yok)
- **Durum:** tercih · **Örtüşme:** video-eslikci-sunum-sitesi → birincil · **Roller:** ui-tasarimci
- **Boyut:** 15 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (video-eslikci-sunum-sitesi grubunda birincil, tek üye; slayt destesi değil, tek sayfalık eşlikçi site). Türkçe yazılmış; 70 satır + 4 referans. Kişisel koleksiyon, lisans dosyası yok. Çalıştırma testi yapılmadı.

### swiss-creative-mode-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Swiss-inspired creative-mode presentation template skill with bold editorial typography, high-contrast geometric cards, interactive slide navigation, theme switching, hotspot overlays, and palette choreography in a single-file HTML artifact. Use when users ask for a premium presentation-style landing, a Swiss/brutalist deck look, or a creative launch page with rich interactions.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### web-artifacts-builder  ·  anthropics/skills @ ca45fc4  ·  puan 90 (A)

- **Ne yapar:** React + TypeScript + Vite + Tailwind + shadcn/ui ile çok bileşenli claude.ai HTML artifact'ı kurar ve Parcel/html-inline ile tek dosyalık bundle.html üretir; 'AI slop'tan kaçınma (mor gradient, Inter, aşırı yuvarlak köşe) uyarısı içerir. 40+ shadcn bileşeni hazır tarball olarak gelir.
- **Ne zaman:** Paylaşılabilir tek HTML dosyası olarak teslim edilecek React tabanlı araç/dashboard/prototip. · **Ne zaman değil:** Üretim uygulaması (Next.js proje kurulumu); basit tek sayfa HTML. Artifact aracının doğrudan HTML yayınladığı durumlarda gerekmez.
- **Teknoloji:** react, typescript, vite, tailwind, shadcn-ui, parcel · **Paketler:** node>=18, pnpm, parcel, html-inline
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** artifact-uygulama-paketleme → birincil · **Roller:** frontend-muhendis
- **Boyut:** 45 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Tek dosyalık dağıtım için kanıtlanmış akış; frontend-muhendis rolünde zaten opsiyonel. Dikkat: init-artifact.sh 'npm install -g pnpm' ile global kurulum yapar ve çok sayıda paket indirir (ağ + disk); betikler skill klasörüne göre göreli çağrılır. Eski adı artifacts-builder aynı içeriktir.
