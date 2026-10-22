# 02-tasarim-sistemi-marka — Tasarım ve Ön Yüz

_Design token, tema, marka kimliği, banner/logo_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **27/30**

### apple-hig  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Apple Human Interface Guidelines as 14 agent skills covering platforms, foundations, components, patterns, inputs, and technologies for iOS, macOS, visionOS, watchOS, and tvOS.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### banner-design  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 78 (B)

- **Ne yapar:** Sosyal medya kapakları, reklam bannerları, web hero görselleri ve baskı bannerları için çok formatlı tasarım akışı. Gereksinimleri sorar, 2-3 sanat yönü üretir, bannerı tam piksel boyutunda HTML/CSS olarak kurar ve PNG'ye aktarır; platform ölçüleri ve 22 stil için bundled referans içerir.
- **Ne zaman:** Belirli bir platform boyutuna (Twitter başlığı, LinkedIn kapağı, Google Display, hero) birden fazla sanat yönü alternatifli banner gerekince. · **Ne zaman değil:** Video düzenleme, tam web sitesi tasarımı veya baskı üretimi (CMYK/bleed ayrıntısı) için değil; marka kuralı yoksa kendi marka kuralını uydurmaz, önce brand/design gerekir.
- **Teknoloji:** html, css
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** marka-gorsel-varlik → tamamlayıcı · **Roller:** tasarim-sistemi
- **Boyut:** 12 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel). Kısa ve kendi kendine yeten (6.9 KB); beceri, kurulum, anahtar ve ağ istemez, görsel üretimi ve PNG dışa aktarımını 'varsa' kaydıyla opsiyonel bırakıyor. Dikkat: kalite doğası gereği `design` skill'indeki banner alt akışıyla büyük ölçüde örtüşüyor; yalnız banner iş akışı gerekiyorsa tercih edilir. PNG aktarımı için ayrı bir tarayıcı/ekran görüntüsü aracı gerekir.

### brand  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 89 (A)

- **Ne yapar:** Marka sesi, görsel kimlik, mesajlaşma çerçeveleri, varlık yönetimi ve tutarlılık denetimi için kapsamlı kılavuz seti. `docs/brand-guidelines.md`'yi tek doğruluk kaynağı yapar; betikler renkleri çıkarır, varlıkları doğrular ve markayı `assets/design-tokens.json/css` dosyalarına senkronlar.
- **Ne zaman:** Yeni bir marka kimliği/ses rehberi yazılırken veya mevcut marka kurallarını tasarım token'larına bağlarken; marka uyum denetimlerinde. · **Ne zaman değil:** Tek seferlik logo üretimi veya hazır tema seçimi için değil (design / theme-factory). Projede zaten token/`@theme` dosyaları varsa sync betiği durur; üzerine yazmaz.
- **Teknoloji:** node, css, markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** marka-gorsel-varlik → tamamlayıcı · **Roller:** tasarim-sistemi
- **Boyut:** 106 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İçerik düzenli (ses, mesaj, tipografi, logo, onay kontrol listeleri) ve betikler yalnız Node standart kütüphanesini kullanıyor; sync betiği mevcut token dosyalarını görünce durup `--force` istiyor, bu güvenli bir tasarım. Dikkat: `sync-brand-to-tokens.cjs` kardeş `../design-system/scripts/generate-tokens.cjs` yoluna bağlı (yoksa yalnız uyarı verip CSS'i üretmez); design-system ile birlikte kurulmalı. `/brand:update` komutu ve `docs/` yolları proje köküne göre çalışır.

### brand-extract  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Extract a complete Brand Kit from a live website by driving the in-app browser. Use when a brand-extraction project opens with a site in the Browser tab, or when the user asks to "extract a brand", "pull the brand from <url>", "get the colors/fonts/logo from this site", or build a brand/design system from a reference website. Pairs with the agent-browser tool for measurement and pauses for the use
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 68 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### brand-guidelines  ·  anthropics/skills @ dbd4588  ·  puan 69 (B)

- **Ne yapar:** Anthropic'in kurumsal renk (koyu #141413, açık #faf9f5, turuncu/mavi/yeşil vurgu) ve tipografi (Poppins başlık, Lora gövde) kurallarını sunum ve belgelere uygulayan kısa skill. python-pptx RGBColor ile renk uygular, yazı tipi yoksa Arial/Georgia'ya düşer.
- **Ne zaman:** Yalnızca Anthropic markalı sunum/belge üretirken veya tek bir markanın kuralının skill'e nasıl yazıldığına örnek olarak. · **Ne zaman değil:** Kullanıcının kendi markası için değil: renk ve yazı tipleri Anthropic'e sabit. Genel marka rehberi için brand, hazır tema için theme-factory kullan.
- **Teknoloji:** python-pptx · **Paketler:** python-pptx
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** hazir-tema-marka-stili → tamamlayıcı
- **Boyut:** 13 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İçerik tek bir kuruma (Anthropic) bağlı ve dar; kullanıcı projelerinde yanlış marka renkleri uygulama riski taşır, rol önyüklemesine girmemeli. Dikkat: registry 'lisans yok' diyor ama klasörde Apache-2.0 LICENSE.txt var (telif satırı Anthropic). Yapı olarak temiz, hiçbir şey kurmaz/indirmez.

### brand-guidelines@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** anthropics/skills'teki brand-guidelines'ın birebir kopyası: Anthropic renk ve tipografi kurallarını sunum/belgelere uygular.
- **Ne zaman:** Yalnızca birincil kopya (anthropics/skills) alınamazsa; aynı Anthropic marka içeriği. · **Ne zaman değil:** Birincil kopya varken kullanma. Kullanıcının kendi markası için değil.
- **Teknoloji:** python-pptx · **Paketler:** python-pptx
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** hazir-tema-marka-stili → alternatif
- **Boyut:** 13 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. SKILL.md anthropics/skills sürümüyle birebir aynı (diff: yalnız KAYNAK.md ve LICENSE.txt). Dikkat: bu kopyanın LICENSE.txt'inde telif satırı doldurulmamış şablon ('Copyright [yyyy] [name of copyright owner]'), yani lisans sahipliği net değil; resmî kopya tercih edilmeli.

### brand-guidelines@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Apply Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards. A reference for shaping your own.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### brandkit  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, p
- **Teknoloji:** canvas, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 17 KB (SKILL.md 16.1 KB, yük orta)
- **İnceleme:** otomatik

### color-expert  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Color science expert skill with 286K words of reference material covering OKLCH/OKLAB, palette generation, accessibility/contrast, color naming, pigment mixing, and historical color theory.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### design  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 77 (B)

- **Ne yapar:** claudekit birleşik tasarım skilli: marka kimliği, token, UI stili, AI ile logo üretimi (55 stil; Gemini, Atlas Cloud veya MuAPI), 50 teslimatlı kurumsal kimlik (CIP) maketleri, HTML sunumlar, banner (22 stil), SVG ikon ve sosyal medya görselleri. brand, design-system ve ui-styling kardeş alt skillerine yönlendirir.
- **Ne zaman:** Logo, kurumsal kimlik seti, banner, ikon veya sosyal medya görseli üretimi; marka paketi çıkarma. · **Ne zaman değil:** Web sayfası tasarımı (01 kategorisindeki skiller); API anahtarı olmadan AI logo/ikon üretimi.
- **Teknoloji:** python, html, css, gemini, api-anahtari · **Paketler:** python3, google-genai, pillow, GEMINI_API_KEY veya MUAPI_API_KEY
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** marka-gorsel-varlik → birincil · **Roller:** tasarim-sistemi
- **Boyut:** 284 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Geniş kapsamlı 'her şey' skilli; marka/banner/logo işleri için 02 kategorisine taşındı. Kardeş skiller (brand, design-system, ui-styling) olmadan eksik çalışır; AI üretimi için ücretli API anahtarı ve pip kurulumu gerekir.

### design-consultation  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Build a complete design system from scratch with creative risks and realistic product mockups. Useful for kickoff workshops and brand-from-zero work.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### design-md  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Create and manage DESIGN.md files. Useful for capturing design direction, tokens, and visual rules in a single source of truth.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### design-spec  ·  vudovn/ag-kit @ 549ba3d  ·  puan 85 (A)

- **Ne yapar:** DESIGN.md dosyası yazma rehberi: makinece okunur tasarım token'ları (YAML ön bilgi: renk, tipografi, boşluk, köşe, bileşen) ile insan okunur gerekçenin tek gerçek kaynakta birleştiği format; kanonik bölüm sırası, token adlandırma önerileri ve 70+ gerçek DESIGN.md örneği (collection.md). Google Labs DESIGN.md spesifikasyonundan uyarlanmış.
- **Ne zaman:** UI koduna başlamadan önce projenin DESIGN.md'sini oluştururken veya güncellerken. · **Ne zaman değil:** Görsel yön henüz belirsizken (önce design-taste-frontend / design-dna); tek bileşenlik işler.
- **Teknoloji:** markdown, yaml · **Paketler:** @google/design.md (npx, isteğe bağlı linter)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarim-referans-analizi → tamamlayıcı · **Roller:** ui-tasarimci, tasarim-sistemi
- **Boyut:** 21 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Net şema ve gerçek örnek kütüphanesi; impeccable ve design-dna çıktılarıyla uyumlu. Konu itibarıyla tasarım sistemi kategorisine taşındı.

### design-system@nextlevelbuilder  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 89 (A)

- **Ne yapar:** Üç katmanlı (primitive, semantic, component) token mimarisi, CSS değişkenleri, boşluk/tipografi ölçekleri, bileşen durum spesifikasyonları ve token'dan kod üretimi. Ayrıca token'larla uyumlu sunum (slide) üretimi için BM25 arama, 8 karar CSV'si ve Chart.js tabanlı bir slayt sistemi içerir.
- **Ne zaman:** Sıfırdan veya mevcut projede token sistemi kurarken; hardcode renk/boşluk denetimi (`validate-tokens.cjs`) ve Tailwind entegrasyonu için. · **Ne zaman değil:** Sadece Tailwind v4 bileşen kitaplığı yazacaksan tailwind-design-system daha doğrudan; tek seferlik sunum için slides skill'i. Marka sesi/mesaj için brand.
- **Teknoloji:** css, node, python, tailwindcss, chart.js
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarim-token-mimarisi → birincil · **Roller:** tasarim-sistemi, ui-tasarimci
- **Boyut:** 178 KB (SKILL.md 7.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Token hiyerarşisi, durum matrisi ve doğrulama/üretim betikleri (testli, yalnız stdlib) net; hardcode değer denetimi gerçek kazanç. Dikkat: slayt sistemi (7+ py/csv, ~250 KB klasör) token konusundan bağımsız bir yan ürün ve `slides` skill'iyle örtüşüyor. SKILL.md var olmayan dosyalara başvuruyor: `assets/designs/slides/claudekit-pitch-251223.html`, `assets/css/slide-animations.css`, `/slides:create` komutu. 'Skill Dependencies: brand, ui-styling' — ikisi de kütüphanede var (ui-styling 01'de). `fetch-background.py` yalnız hazır Pexels URL'leri döndürür, indirme/anahtar yok; Chart.js CDN'den sabit sürümle (4.4.1) yükleniyor.

### figma-code-connect-components  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Connect Figma design components to code components using Code Connect so design-system updates flow into the codebase automatically.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-create-design-system-rules  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate project-specific design system rules for Figma-to-code workflows. Useful for capturing tokens, naming, and lint rules in one source.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-create-new-file  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Create a new blank Figma Design or FigJam file. Useful as the first step in scripted design-system or workshop workflows.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-generate-design  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Build or update screens in Figma from code or description using design system components. Translate app pages into Figma using design tokens.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-generate-library  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Build or update a professional-grade design system library in Figma from a codebase. Useful for keeping the Figma source of truth in sync with shipped components.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-implement-design  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Translate Figma designs into production-ready code with 1:1 visual fidelity. Useful for handing off Figma frames straight to a frontend agent.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### figma-use  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Run Figma Plugin API scripts for canvas writes, inspections, variables, and design-system work. Prerequisite for every other Figma skill in this catalogue.
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### platform-design  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** 300+ design rules from Apple HIG, Material Design 3, and WCAG 2.2 for cross-platform apps. Useful when shipping a single design across iOS, Android, and the web.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### stitch-design-taste  ·  nexu-io/open-design @ e03d5c2  ·  puan 93 (A)

- **Ne yapar:** Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance.
- **Teknoloji:** api-anahtari, canvas, css _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### stitch-loop  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Iterative design-to-code feedback loop. Critique → adjust → ship cycle for tightening visual fidelity between brief and built UI.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### tailwind-design-system  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** Tailwind CSS v4 ile (CSS-first `@theme`, OKLCH renk) üretim kalitesinde tasarım sistemi kurma tarifi: semantik token'lar, CVA ile bileşen varyantları, React 19 bileşik bileşenler, form bileşenleri, responsive grid, native CSS animasyonlar, @custom-variant ile koyu mod ve v3→v4 geçiş kontrol listesi.
- **Ne zaman:** Tailwind v4 projesinde bileşen kitaplığı/token sistemi yazarken veya v3'ten v4'e geçerken; shadcn tarzı (CVA + Radix Slot) bileşenler gerekince. · **Ne zaman değil:** Tailwind kullanmayan projelerde değil; Tailwind v3 projesinde (yöntemler farklı) uygun değil. Yalnız kısa ilke özeti istiyorsan tailwind-patterns; shadcn bileşen kurulumu için ui-styling.
- **Teknoloji:** tailwindcss, react, typescript, radix-ui · **Paketler:** tailwindcss@4, class-variance-authority, clsx, tailwind-merge, @radix-ui/react-slot, react-hook-form, zod, lucide-react
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70866, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** shadcn-tailwind-uygulama → tamamlayıcı · **Roller:** tasarim-sistemi · **Globalde:** claude:ayni
- **Boyut:** 22 KB (SKILL.md 21.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). tailwind-patterns ile ilişki: ikisi de v4 CSS-first, ama tailwind-patterns kısa ilke/karar özeti (6.8 KB, kod azdır), tailwind-design-system ise kod ağırlıklı uygulama tarifi (21.8 KB; CVA, bileşik bileşen, form, animasyon, koyu mod, geçiş listesi). Çatışmazlar, tamamlayıcıdır; bağlam tasarrufu için önce patterns, bileşen yazarken bu seçilir. Dikkat: büyük (21.8 KB). Registry'deki 'OpenMontage kurulumu gerekir' bağımlılığı yanlış pozitif: SKILL.md'de OpenMontage/python/tools/ referansı yok, düz Tailwind skill'i. Lisans AGPL-3.0 görünüyor ama bu OpenMontage deposunun lisansı; içeriğin kendi lisansı (muhtemelen farklı bir üst kaynaktan alınmış) doğrulanmadı. Örnekler `@/lib/utils` (cn), ThemeProvider gibi proje dosyalarını varsayar.

### tailwind-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Tailwind CSS v4 ilkeleri: CSS-öncelikli @theme yapılandırması, kapsayıcı sorguları, OKLCH renk token mimarisi, karanlık mod, tipografi ölçeği, bileşen çıkarma ve anti-kalıplar.
- **Ne zaman:** Tailwind v4 projesinde token mimarisi ve modern CSS kalıpları kurulurken. · **Ne zaman değil:** Tailwind v3 projeleri (yapılandırma farklı); Tailwind kullanılmayan projeler.
- **Teknoloji:** tailwind, css · **Paketler:** tailwindcss>=4
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** shadcn-tailwind-uygulama → tamamlayıcı · **Roller:** frontend-muhendis
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ilke özeti, v3→v4 farkları faydalı; kod örneği derinliği sınırlı. Konu itibarıyla tasarım sistemi kategorisine taşındı (tailwind-design-system ile birlikte değerlendirilmeli).

### theme-factory  ·  anthropics/skills @ dbd4588  ·  puan 77 (B)

- **Ne yapar:** 10 hazır renk+yazı tipi temasıyla (Ocean Depths, Midnight Galaxy, Tech Innovation vb.) slayt, belge, rapor veya HTML sayfasını tek seferde stillendirir; tema önizleme PDF'i sunar, seçim sonrası ilgili `themes/*.md` dosyasındaki hex ve yazı tiplerini uygular, uygun tema yoksa yenisini üretir.
- **Ne zaman:** Hızlı, tutarlı görünüm gerektiren sunum/belge/landing için hazır palet+font çifti seçerken; marka rehberi yokken. · **Ne zaman değil:** Markanın kurallı renkleri varsa (brand/design-system önce). Kod tabanında token sistemi kurmak için değil.
- **Teknoloji:** html, css, pptx
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** hazir-tema-marka-stili → birincil · **Roller:** tasarim-sistemi
- **Boyut:** 141 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel). 10 tema hazır ve tutarlı, bağımlılığı yok. Dikkat: temalar genel amaçlı/jenerik; 'yapay zeka şablonu' görünümünden kaçınmak isteyen projede tasarım yönü için yeterli değildir (design-taste-frontend). Akış 'PDF'i göster, seçim bekle' diye kullanıcı etkileşimi varsayar; otomatik/tek atışta zorlaşır. Resmî kopya (anthropics/skills) tercih; composiohq kopyası birebir aynı.

### theme-factory@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 77 (B)

- **Ne yapar:** anthropics/skills'teki theme-factory'nin birebir kopyası: 10 hazır tema ile slayt/belge/HTML stillendirme.
- **Ne zaman:** Yalnızca resmî kopya alınamazsa. · **Ne zaman değil:** Resmî kopya varken kullanma.
- **Teknoloji:** html, css, pptx
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** hazir-tema-marka-stili → alternatif
- **Boyut:** 141 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. SKILL.md, themes/ ve PDF resmî sürümle aynı (diff: yalnız KAYNAK.md ve LICENSE.txt). Dikkat: LICENSE.txt'te telif satırı doldurulmamış şablon.

### theme-factory@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Apply professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages. Ships 10 pre-set themes.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### wpds  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** WordPress Design System. Apply WordPress's official design tokens, typography, and component patterns to themes and sites.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103328, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.
