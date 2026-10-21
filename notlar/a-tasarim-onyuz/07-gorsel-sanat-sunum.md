# 07-gorsel-sanat-sunum — Tasarım ve Ön Yüz

_Poster/canvas tasarımı, generative art, slayt, GIF_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **10/10**

### algorithmic-art  ·  anthropics/skills @ dbd4588  ·  puan 76 (B)

- **Ne yapar:** Önce bir 'algoritmik felsefe' (manifesto .md) yazdırıp ardından bunu seed'li rastgelelik ve parametre paneliyle p5.js üretken sanatına (akış alanları, parçacık sistemleri) çevirir. Çıktı .md + etkileşimli HTML görüntüleyici + .js algoritmadır; şablon olarak viewer.html ve generator_template.js verilir.
- **Ne zaman:** Kodla üretken sanat, akış alanı/parçacık görselleri, seed ile tekrarlanabilir etkileşimli sanat parçası istendiğinde. · **Ne zaman değil:** Ürün arayüzü, veri görselleştirme (d3-viz) veya 3D sahne (threejs-*) için değil; statik poster için canvas-design daha uygun. Mevcut bir sanatçının işini taklit etmek için kullanılmaz.
- **Teknoloji:** p5.js, canvas, html, javascript · **Paketler:** p5.js (CDN)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** uretken-sanat → birincil
- **Boyut:** 58 KB (SKILL.md 19.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Niş ama iyi kurgulanmış; felsefe -> kod iki adımı ve seed'li parametre paneli tutarlı çıktı verir. Dikkat: viewer.html p5.js (cdnjs) ve Google Fonts'u CDN'den çeker, çevrimdışı çalışmaz; lisans alanı 'LICENSE.txt' (Anthropic) ve açık kaynak değil; sanat odaklı olduğundan çoğu ürün projesinde gerekmez.

### artifacts-builder  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** React 18 + TypeScript + Vite + Tailwind + shadcn/ui ile karmaşık claude.ai HTML artifact'ı kurar (init-artifact.sh) ve Parcel + html-inline ile tek bir bundle.html'e paketler. web-artifacts-builder'ın eski adıyla yayımlanmış kopyasıdır; SKILL.md yalnızca ad/başlık satırlarında farklıdır.
- **Ne zaman:** Durum yönetimi, yönlendirme veya shadcn bileşeni gerektiren tek dosyalık paylaşılabilir HTML çıktısı. · **Ne zaman değil:** web-artifacts-builder ile birebir aynı içerik; ikisini birden kurmayın. Basit tek dosya HTML/JSX için gereksiz ağır.
- **Teknoloji:** react, typescript, vite, tailwind, shadcn-ui, parcel · **Paketler:** node>=18, pnpm, parcel, html-inline
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** artifact-uygulama-paketleme → alternatif
- **Boyut:** 45 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. web-artifacts-builder (Anthropic) ile aynı betikler ve metin, yalnızca ad farkı var; yinelenen kopya. Dikkat: init-artifact.sh 'npm install -g pnpm' ile global kurulum yapar ve ~40 Radix/shadcn paketi indirir; bundle betiği paket kurar.

### canvas-design  ·  anthropics/skills @ dbd4588  ·  puan 84 (A)

- **Ne yapar:** Bir 'tasarım felsefesi' (hareket adı + 4-6 paragraf manifesto) yazdırıp ardından bunu %90 görsel / %10 metin olan özgün PNG veya PDF posterine, sanat parçasına dönüştürür. Yaklaşık 5 MB'lık OFL lisanslı font klasörü (canvas-fonts) ile gelir ve iki geçişli iyileştirme ister.
- **Ne zaman:** Poster, kapak görseli, statik sanat/tasarım parçası, marka kampanya görseli üretirken (PNG/PDF). · **Ne zaman değil:** Etkileşimli/web arayüzü (frontend-design, design-taste-frontend); çok sayfalı sunum (slides, pptx); veri grafiği (d3-viz).
- **Teknoloji:** canvas, python, png, pdf · **Paketler:** pillow / reportlab (agent ortamına göre)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** statik-gorsel-poster → birincil · **Roller:** ui-tasarimci
- **Boyut:** 5424 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Marka-sunum profilinin ek skilli; özgünlük ve 'zanaat' vurgusu ile şablon görünümünü engeller, fontlar yerel ve OFL. Dikkat: skill klasörü ~5,4 MB (ağırlıkla ttf); SKILL.md 11,7 KB. Yalnızca SKILL.md bağlama girer. Betik yok, ağ/anahtar yok. LICENSE.txt Anthropic'e ait, repo lisans alanı boş.

### canvas-design@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Anthropic canvas-design'ın ComposioHQ kopyası; SKILL.md ve font klasörü birebir aynıdır, yalnızca LICENSE.txt farklı (şablon Apache metni, telif sahibi boş).
- **Ne zaman:** Yalnızca upstream sürümü erişilemezse; aynı işi yapar. · **Ne zaman değil:** Anthropic sürümü varken kurmayın (yinelenen, lisans metni eksik).
- **Teknoloji:** canvas, png, pdf
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** statik-gorsel-poster → alternatif
- **Boyut:** 5424 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. diff -rq: tek fark LICENSE.txt ve KAYNAK.md; içerik birebir upstream ile aynı. Dikkat: ~5,4 MB font tekrar eder; lisans başlığı '[yyyy] [name of copyright owner]' doldurulmamış.

### d3-viz  ·  calesthio/OpenMontage @ c806645  ·  puan 86 (A)

- **Ne yapar:** d3.js ile özel, etkileşimli veri görselleştirmeleri (ağ/grafik, hiyerarşi, coğrafi harita, geçişli grafikler) kurmayı anlatır; React ve vanilla JS şablonları (chart-template.jsx, interactive-template.jsx), renk şeması ve ölçek başvuruları ile örnek veri içerir. Hazır grafik kütüphanesinin yetmediği özgün işler içindir.
- **Ne zaman:** Standart grafik kütüphanesinde olmayan özel SVG görselleştirme, force-directed ağ, zoom/brush etkileşimi, haritalar. · **Ne zaman değil:** Hızlı standart grafik/dashboard (dataviz skilli veya grafik kütüphanesi); 3D görselleştirme (threejs-*).
- **Teknoloji:** d3, svg, react, javascript · **Paketler:** d3
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70579, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** veri-gorsellestirme → birincil · **Roller:** frontend-muhendis · **Globalde:** claude:ayni
- **Boyut:** 80 KB (SKILL.md 21.3 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Konu odaklı, başvuru dosyaları ve şablonlar kaliteli; kategoride tek veri görselleştirme skilli. Dikkat: registry'de bagimlilik uyarısı var ama d3-viz'in kendi içeriği OpenMontage komutu çağırmıyor, bağımsız çalışır. Repo lisansı AGPL-3.0 (skill dosyasında ayrı lisans yok); aynı skill ~/.claude/skills'te zaten global kurulu (globalde: ayni). d3 CDN'den yüklenebilir.

### image-enhancer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Ekran görüntüsü ve görsellerin çözünürlüğünü, keskinliğini ve sıkıştırma artefaktlarını iyileştirmeyi anlatan, betiği olmayan yalnızca yönerge niteliğinde kısa bir skill. Örnek çıktı biçimi verir ama gerçek bir araç/kütüphane belirtmez.
- **Ne zaman:** Dokümantasyon veya sunum öncesi ekran görüntüsü iyileştirme isteğinde başvuru metni olarak. · **Ne zaman değil:** Gerçek yapay zekâ upscale için: ai-medya-uretici akışındaki upscale araçları, ffmpeg veya ImageMagick doğrudan kullanılmalı.
- **Teknoloji:** imagemagick
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** gorsel-iyilestirme → birincil
- **Boyut:** 2 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Hangi aracı çalıştıracağını söylemiyor; örnek çıktı uydurma gibi ("Enhancements applied") ve agent'ı yanlış beklentiye sokabilir. Dikkat: 2,5 KB, ek dosya yok, kurulum yok; değer katmıyor. Gerçek işi görsel upscale/arka plan araçları yapar.

### slack-gif-creator  ·  anthropics/skills @ dbd4588  ·  puan 77 (B)

- **Ne yapar:** Slack için animasyonlu GIF üretimi: PIL ile kare çizimi, GIFBuilder, easing fonksiyonları, kare birleştirici ve Slack boyut/FPS/renk sınırlarını denetleyen doğrulayıcı. Emoji (128x128) ve mesaj (480x480) GIF'leri için kısa, sade bir araç seti.
- **Ne zaman:** Slack emoji veya mesaj GIF'i, kısa döngülü basit animasyon isteklerinde. · **Ne zaman değil:** Video/hareketli grafik (hyperframes, motion-graphics); karmaşık sahneler ve gerçek görsel efektler.
- **Teknoloji:** python, pillow, imageio, numpy, gif · **Paketler:** pillow, imageio, imageio-ffmpeg, numpy
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** slack-gif → birincil
- **Boyut:** 43 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Küçük, bağımsız, Python modülleri düzenli; Slack sınırlarını doğrulaması işe yarar. Dikkat: 'pip install pillow imageio numpy' ister (--break-system-packages yok; venv önerilir). Composio sürümü eski ve farklı bir kod tabanı (ayrı alternatif).

### slack-gif-creator@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Aynı skill'in ComposioHQ'daki daha eski/geniş sürümü: SKILL.md 16,7 KB, ek color_palettes.py, typography.py, visual_effects.py ve templates/ klasörü içerir; Slack sınırları (emoji 64 KB, mesaj ~2 MB) ayrıntılıdır.
- **Ne zaman:** Anthropic sürümündeki yardımcılar yetmezse; hazır şablon, tipografi ve görsel efekt modülleri gerektiğinde. · **Ne zaman değil:** Varsayılan olarak Anthropic sürümünü kullanın; ikisini birden kurmayın (aynı ad/iş).
- **Teknoloji:** python, pillow, imageio, numpy, gif · **Paketler:** pillow, imageio, numpy
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** slack-gif → alternatif
- **Boyut:** 208 KB (SKILL.md 16.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Daha zengin ama ağır (16,7 KB SKILL.md, 208 KB) ve güncel upstream ile ayrışmış; core/*.py dosyaları farklı. Dikkat: pip install pillow imageio numpy; aynı ad nedeniyle iki sürüm birlikte kurulursa çakışır.

### slides  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 3eccfd8  ·  puan 81 (A)

- **Ne yapar:** Chart.js, tasarım token'ları, yerleşim kalıpları ve metin yazım formülleri ile stratejik HTML sunum (pitch deck, pazarlama slaytı) üretir; `slides create` alt komutu references/create.md'yi yükler. Yerleşim, strateji ve copywriting bilgisini ayrı referans dosyalarında tutar.
- **Ne zaman:** HTML tabanlı pitch deck, veri destekli pazarlama sunumu; marka-sunum profili için. · **Ne zaman değil:** PowerPoint/.pptx çıktısı gerekiyorsa pptx; video slayt gösterisi için slideshow (HyperFrames); sıfırdan görsel poster için canvas-design.
- **Teknoloji:** html, chart.js, css · **Paketler:** chart.js (CDN)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138431, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** html-sunum → birincil · **Roller:** dokuman-yazari
- **Boyut:** 19 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. İçerik stratejisi ve yerleşim bilgisi iyi, MIT. Dikkat: referanslar `python ../design-system/scripts/search-slides.py` (kardeş design-system skill'ine ve onun veri tabanına) başvurur; design-system kurulu değilse bu komutlar kırık kalır, registry bunu bağımlılık olarak işaretlemiyor. Chart.js jsdelivr CDN'den yüklenir. SKILL.md yalnızca 1,7 KB. slideshow (video) ve design (claudekit) ile karıştırılmamalı.

### web-artifacts-builder  ·  anthropics/skills @ dbd4588  ·  puan 85 (A)

- **Ne yapar:** React + TypeScript + Vite + Tailwind + shadcn/ui ile çok bileşenli claude.ai HTML artifact'ı kurar ve Parcel/html-inline ile tek dosyalık bundle.html üretir; 'AI slop'tan kaçınma (mor gradient, Inter, aşırı yuvarlak köşe) uyarısı içerir. 40+ shadcn bileşeni hazır tarball olarak gelir.
- **Ne zaman:** Paylaşılabilir tek HTML dosyası olarak teslim edilecek React tabanlı araç/dashboard/prototip. · **Ne zaman değil:** Üretim uygulaması (Next.js proje kurulumu); basit tek sayfa HTML. Artifact aracının doğrudan HTML yayınladığı durumlarda gerekmez.
- **Teknoloji:** react, typescript, vite, tailwind, shadcn-ui, parcel · **Paketler:** node>=18, pnpm, parcel, html-inline
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** artifact-uygulama-paketleme → birincil · **Roller:** frontend-muhendis
- **Boyut:** 45 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Tek dosyalık dağıtım için kanıtlanmış akış; frontend-muhendis rolünde zaten opsiyonel. Dikkat: init-artifact.sh 'npm install -g pnpm' ile global kurulum yapar ve çok sayıda paket indirir (ağ + disk); betikler skill klasörüne göre göreli çağrılır. Eski adı artifacts-builder aynı içeriktir.
