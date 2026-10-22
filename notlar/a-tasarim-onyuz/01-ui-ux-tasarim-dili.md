# 01-ui-ux-tasarim-dili — Tasarım ve Ön Yüz

_Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **17/34**

### design-brief  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** Parse a structured design brief written in I-Lang protocol format into a concrete design spec. Eliminates ambiguity from vague requests like "make it professional" by requiring explicit dimensions: palette, typography, layout, mood, density, and constraints. Trigger keywords: "design brief", "create a design brief", "ilang brief", "structured brief".
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** otomatik

### design-dna  ·  zanwei/design-dna @ 593e39b  ·  puan 82 (A)

- **Ne yapar:** Tasarım DNA'sını üç boyutta çıkarır, tanımlar ve uygular: tasarım sistemi (token), tasarım stili (nitel his) ve görsel efektler (Canvas, WebGL, 3D, parçacık, shader, scroll efektleri). Referans görsel/URL'leri yapılandırılmış JSON profile çevirir ve bu profilden yeni tasarım üretir; renk ölçümü için betik içerir.
- **Ne zaman:** Referans sitelerin/ekran görüntülerinin stilini analiz edip yeniden kullanılabilir profile çevirmek; stil aktarımı. · **Ne zaman değil:** Referans yoksa sıfırdan yön belirleme (design-taste-frontend); tek bir DESIGN.md yazımı (design-spec).
- **Teknoloji:** html, css, node, webgl · **Paketler:** node (renk betiği)
- **Claude / Codex:** tam / tam
- **Geliştirici:** zanwei (kisi, ★2014, son güncelleme 2026-08-28, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tasarim-referans-analizi → birincil · **Roller:** ui-tasarimci · **Globalde:** claude:farkli
- **Boyut:** 709 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Üç boyutlu şema ve fazlar net; efekt boyutu diğer skillerde yok. Çok dilli README'ler boyutu şişiriyor (709 KB).

### design-taste-frontend  ·  Leonxlnx/taste-skill @ 6010f91  ·  puan 93 (A)

- **Ne yapar:** tasteskill v2: 247 seçkin galeri sitesinden damıtılmış 'anti-slop' sanat yönetimi. Betik araştırılmış 20 yönden üçünü dağıtır, seçilen yöne göre tip sistemi, palet, hero ve bölüm kompozisyonlarını verir; katı ev kuralları, gerçek tarayıcı denetçisi (inspect.mjs) ve ekran görüntüsü üzerinden bak-düzelt döngüsü uygular. Uygulama ekranları (dashboard, ayarlar, gelen kutusu) için ayrı kurallar içerir.
- **Ne zaman:** Landing page, pazarlama sitesi, portfolyo, ürün sayfası veya uygulama ekranı tasarlanır/yeniden tasarlanırken; sayfa 'şablon / AI yapımı' görünüyorsa. · **Ne zaman değil:** Mobil uygulama (mobile-design); var olan tasarım sistemine sıkı bağlı küçük bileşen işleri; Node 22 ve Chrome/Chromium yoksa betikler çalışmaz (yalnız lint.mjs).
- **Teknoloji:** html, css, node, chromium · **Paketler:** node>=22, Chrome/Edge/Chromium
- **Claude / Codex:** tam / tam
- **Geliştirici:** Leonxlnx (kisi, ★100552, son güncelleme 2026-10-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-gorsel-yon → birincil · **Roller:** ui-tasarimci
- **Boyut:** 2363 KB (SKILL.md 37.6 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kararları betikle dağıtıp doğrulamayı gerçek tarayıcıyla yapması 'ortalama sayfa' sorununa en güçlü çözüm; hiçbir şey kurmaz, API anahtarı istemez, eval seti var. Bağlam yükü yüksek (37 KB SKILL.md).

### design-taste-frontend-v1  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. Use this v1 install name only if you need exact backward compatibility.
- **Teknoloji:** canvas, css, gsap, html, motion, next.js, node, react, tailwind, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 21.3 KB, yük orta)
- **İnceleme:** otomatik

### design-taste-frontend@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 25 (D)

- **Ne yapar:** Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.
- **Teknoloji:** api-anahtari, canvas, css, git, gsap, html, motion, next.js, node, react, tailwind, three.js, typescript, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 87 KB (SKILL.md 85.9 KB, yük buyuk)
- **İnceleme:** otomatik

### faq-page  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** A Frequently Asked Questions (FAQ) page with collapsible accordion sections, search functionality, and category filtering. Use when the brief asks for "FAQ", "help center", "questions", or "support page".
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### frontend-design@anthropics  ·  anthropics/skills @ dbd4588  ·  puan 84 (A)

- **Ne yapar:** frontend-design'ın anthropics/skills kopyası: içerik claude-code eklentisindekiyle birebir aynı, ayrıca LICENSE.txt içerir.
- **Ne zaman:** Lisans metninin skill içinde bulunması gerektiğinde tercih sürümü yerine. · **Ne zaman değil:** Normalde (tercih sürümü aynı içeriği taşır).
- **Teknoloji:** html, css
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** alternatif · **Örtüşme:** web-gorsel-yon → alternatif
- **Boyut:** 19 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İçerik tercih sürümüyle aynı; tek fark LICENSE.txt.

### frontend-design@anthropics-2  ·  anthropics/claude-code @ 5ed799e  ·  puan 84 (A)

- **Ne yapar:** Anthropic'in kısa tasarım ilkeleri skilli: tasarım stüdyosu yöneticisi gibi konuya özgü, şablon gibi görünmeyen palet/tipografi/düzen kararları al; konuyu belirle, planla, brief'e göre gözden geçir, uygula ve eleştir; ölçülü ol.
- **Ne zaman:** Herhangi bir yeni UI veya yeniden tasarım işinde hafif, her zaman açık tutulabilecek estetik ilke seti olarak. · **Ne zaman değil:** Ayrıntılı yön/kontrol listesi gereken işlerde tek başına (design-taste-frontend veya impeccable daha kapsamlı).
- **Teknoloji:** html, css
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★152857, son güncelleme 2026-10-22, lisans yok)
- **Durum:** tercih · **Örtüşme:** web-gorsel-yon → tamamlayıcı · **Roller:** ui-tasarimci, frontend-muhendis
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa (9 KB) ve bağlam dostu. anthropics/skills kopyasıyla SKILL.md birebir aynı; bu kopyada SKILL.md'nin andığı LICENSE.txt yok (lisans metni alternatif kopyada). Rol adları id ile eşleştiği için tercih bu kopyada bırakıldı.

### frontend-design@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** Create distinctive, production-grade frontend interfaces with strong visual direction, polished typography, considered layout, and working HTML/CSS/JS or framework code. Use for websites, landing pages, dashboards, React components, application screens, and UI beautification.
- **Teknoloji:** api-anahtari, css, html, react, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 15 KB (SKILL.md 5.1 KB, yük kucuk)
- **İnceleme:** otomatik

### frontend-design@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 74 (B)

- **Ne yapar:** ag-kit'in 'anti-slop' web UI skilli: brief çıkarımı, üç kadranlı (varyans/hareket/yoğunluk) yapılandırma, gerçek tasarım sistemi eşlemesi, tipografi/renk/düzen yanlılık düzeltmeleri, minimalist ve brutalist stil dosyaları, yeniden tasarım denetimi ve UX/erişilebilirlik betikleri. taste-skill v1 kurallarından uyarlanmış.
- **Ne zaman:** ag-kit iş akışı kullanan projelerde veya kadran tabanlı yapılandırma istendiğinde. · **Ne zaman değil:** Genel kullanımda (design-taste-frontend v2 daha güncel ve hafif); mobil uygulama.
- **Teknoloji:** html, css, react, next.js, tailwind, python · **Paketler:** python3 (denetim betikleri)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** web-gorsel-yon → alternatif
- **Boyut:** 161 KB (SKILL.md 86.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kapsamlı ama 86 KB SKILL.md ile bağlam yükü çok yüksek; taste-skill v1 türevi, kaynağı v2'ye geçti. Kendi yoluna sabit referans içeriyor (yol bağımlılığı).

### frontend-dev  ·  nexu-io/open-design @ e03d5c2  ·  puan 26 (D)

- **Ne yapar:** Full-stack frontend with cinematic animations, AI-generated media via MiniMax API, and generative art. Useful for hero pages and showcase sites.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### frontend-skill  ·  nexu-io/open-design @ e03d5c2  ·  puan 26 (D)

- **Ne yapar:** Create visually strong landing pages, websites, and app UIs with restrained composition. OpenAI's production frontend playbook.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### high-end-visual-design  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic.
- **Teknoloji:** css, html, react, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** otomatik

### image-to-code  ·  nexu-io/open-design @ e03d5c2  ·  puan 25 (D)

- **Ne yapar:** Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex, it must prefer large, readable, section-specific images instead of tiny compressed boards, generate fresh standalone images for sections or detail views instead of cropping o
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 36.1 KB, yük buyuk)
- **İnceleme:** otomatik

### imagegen-frontend-mobile  ·  nexu-io/open-design @ e03d5c2  ·  puan 25 (D)

- **Ne yapar:** Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mo
- **Teknoloji:** canvas, html, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 39.9 KB, yük buyuk)
- **İnceleme:** otomatik

### imagegen-frontend-web  ·  nexu-io/open-design @ e03d5c2  ·  puan 25 (D)

- **Ne yapar:** Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied he
- **Teknoloji:** canvas _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 38 KB (SKILL.md 36.6 KB, yük buyuk)
- **İnceleme:** otomatik

### impeccable  ·  pbakaus/impeccable @ 89097b9  ·  puan 95 (A)

- **Ne yapar:** Ön yüz arayüzlerini tasarlama, yeniden tasarlama, eleştirme, denetleme, cilalama ve sağlamlaştırma için komut tabanlı tasarım direktörü: shape, audit/critique, animate, bolder/quieter, colorize, typeset, harden, polish, document/extract gibi alt komutlar. PRODUCT.md/DESIGN.md bağlamını yükleyen bir başlatıcı ve canlı tarayıcı DOM denetimi içerir; iOS/Android ekranlarını da kapsar.
- **Ne zaman:** Var olan arayüzü denetleme/iyileştirme, UX eleştirisi, erişilebilirlik ve responsive sağlamlaştırma; yeni yüzeyde tasarım yönü belirleme. · **Ne zaman değil:** Backend veya UI dışı işler; tek seferlik küçük stil düzeltmesi (fazla ağır).
- **Teknoloji:** html, css, node · **Paketler:** impeccable başlatıcısı (ilk çalıştırmada GitHub releases'ten indirilir)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint, user-invocable (Codex bunları yok sayar) · Araca özel sürümler mevcut: claude, codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** pbakaus (kisi, ★84432, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** ui-denetim-iyilestirme → birincil · **Roller:** ui-tasarimci, qa-erisilebilirlik
- **Boyut:** 2140 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi: SKILL.md değişmedi; referanslara Arapça alfabesi yerelleştirme kuralları (ZWNJ, Yeh/Kaf varyantları, yerel rakamlar, Hicri/Celali takvim) eklendi. Kalite 5 korunur; Claude ve Codex için ayrı uyarlanmış sürümleri var. · 2026-10-22 (yeniden kurulum): Windows PowerShell çağrısı düzeltildi (`& "…/impeccable.cmd"`); davranış ve kalite değişmedi.

### industrial-brutalist-ui  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 8.8 KB, yük orta)
- **İnceleme:** otomatik

### login-flow  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** Mobile login and authentication flow screens
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 1.4 KB, yük kucuk)
- **İnceleme:** otomatik

### minimalist-ui  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows.
- **Teknoloji:** canvas, css, html, react, tailwind, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.3 KB, yük orta)
- **İnceleme:** otomatik

### mobile-design  ·  vudovn/ag-kit @ 549ba3d  ·  puan 84 (A)

- **Ne yapar:** iOS ve Android uygulamaları için mobil öncelikli tasarım düşüncesi: dokunma etkileşimi, başparmak bölgesi, platform gelenekleri, performans ilkeleri (React Native, Flutter), yasaklı AI mobil kalıpları listesi ve bir mobil UX denetim betiği. Sabit değerler değil ilke öğretir; platform belirtilmediyse sormayı zorunlu tutar.
- **Ne zaman:** React Native, Flutter veya native mobil uygulama ekranı tasarlanırken. · **Ne zaman değil:** Web uygulamaları ve responsive web (frontend skilleri).
- **Teknoloji:** react-native, flutter, python · **Paketler:** python3 (denetim betiği)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** mobil-ui-tasarimi → birincil · **Roller:** ui-tasarimci
- **Boyut:** 216 KB (SKILL.md 15.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kategoride mobile özgü tek skill; referans dosyaları kapsamlı. 'Önce oku' zorunlulukları bağlamı hızla dolduruyor.

### modern-web-design  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 55 (C)

- **Ne yapar:** 2024-2025 web tasarım trendleri ve kalıpları özeti: performans öncelikli tasarım, cesur minimalizm, mikro etkileşim, scrollytelling, imleç UX'i, glassmorphism; hero, yatay kaydırma galerisi, 3D ürün görüntüleyici gibi kalıplar ve erişilebilirlik/performans kontrol listeleri.
- **Ne zaman:** Trend taraması veya fikir listesi gerektiğinde referans olarak. · **Ne zaman değil:** Gerçek tasarım kararı/uygulaması için (genel ve tarihli; 'AI ortalaması' sayfaya iter).
- **Teknoloji:** html, css, gsap, three.js, react · **Paketler:** python3 (yardımcı betikler)
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-gorsel-yon → alternatif
- **Boyut:** 151 KB (SKILL.md 26.0 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Yüzeysel trend listesi, tarihli (2024-2025) ve diğer skillerin özeti; anti-slop skillerinin kaçındığı varsayılanları öneriyor. Bakımı eski (2025-11).

### redesign-existing-projects  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS.
- **Teknoloji:** css, html, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 15.3 KB, yük orta)
- **İnceleme:** otomatik

### reference-design-contract  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** Turn vague taste, screenshots, URLs, product notes, or "make it feel like this" references into a grounded DESIGN.md plus an implementation handoff. Use it before prototypes, decks, redesigns, or image remix work when the user needs a reusable visual direction rather than a one-off prompt.
- **Teknoloji:** api-anahtari, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** otomatik

### shadcn-ui  ·  nexu-io/open-design @ e03d5c2  ·  puan 26 (D)

- **Ne yapar:** Build UI components with shadcn/ui. Pairs with the Stitch design loop to ship structured, accessible components quickly.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### swiftui-design  ·  nexu-io/open-design @ e03d5c2  ·  puan 26 (D)

- **Ne yapar:** SwiftUI 前端设计 skill — anti AI-slop rules, design direction advisor, brand asset protocol, and five-dimension review. Works with Claude Code, Cursor, Codex, and OpenCode.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### ui-skills  ·  nexu-io/open-design @ e03d5c2  ·  puan 26 (D)

- **Ne yapar:** Opinionated, evolving constraints to guide agents when building interfaces. Useful for keeping output coherent across many small UI pieces.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### ui-styling  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 88 (A)

- **Ne yapar:** shadcn/ui (Radix + Tailwind) bileşenleri, Tailwind yardımcı sınıf stili ve canvas tabanlı görsel tasarımla erişilebilir arayüz kurma: tema/karanlık mod, responsive düzen, erişilebilir bileşen kalıpları ve shadcn ekleme / Tailwind yapılandırma betikleri; poster için OFL lisanslı font paketi.
- **Ne zaman:** React tabanlı projede shadcn/ui + Tailwind ile bileşen ve tema kurarken. · **Ne zaman değil:** shadcn kullanılmayan yığınlar; estetik yön belirleme (bu skill uygulama katmanıdır).
- **Teknoloji:** react, tailwind, shadcn-ui, radix, python · **Paketler:** shadcn (npx), tailwindcss, python3
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** shadcn-tailwind-uygulama → birincil · **Roller:** ui-tasarimci, frontend-muhendis
- **Boyut:** 5627 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Pratik ve kod odaklı; canvas fontları lisanslarıyla birlikte paketlenmiş (5.6 MB). design skillinin kardeş alt skilli.

### ui-ux-pro-max  ·  nextlevelbuilder/ui-ux-pro-max-skill @ 623a9a9  ·  puan 85 (A)

- **Ne yapar:** Yerel aranabilir UI/UX veri tabanı: 79 stil, 192 ürün paleti ve gerekçe profili, 74 font eşleşmesi, 119 UX kuralı, ikonlar, GSAP ön ayarları, grafik türleri ve 22 teknoloji yığını. Python betiğiyle ürün/sektöre göre tasarım sistemi üretir, isteğe bağlı MASTER + sayfa bazlı geçersiz kılma dosyalarına kaydeder.
- **Ne zaman:** Yeni sayfa/proje için palet, font ve stil kararlarını veriye dayandırmak; UX kural kontrol listesi gerektiğinde. · **Ne zaman değil:** Sanat yönetimi gerektiren özgün sayfalarda tek başına (veri tabanı ortalama sonuçlar verir; design-taste-frontend ile birlikte kullan); Python yoksa.
- **Teknoloji:** python, html, css, tailwind · **Paketler:** python3
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** nextlevelbuilder (kurum, ★138484, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-gorsel-yon → tamamlayıcı · **Roller:** ui-tasarimci
- **Boyut:** 3499 KB (SKILL.md 15.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Zengin, bağımlılıksız veri ve kural seti; veri kökeni ve font lisansları belgelenmiş. Dikkat: betik yolu `${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/...` biçiminde; projeye kurulduğunda CLAUDE_PLUGIN_ROOT boş kalır ve yol bozulur (skill-ekle bu kalıbı düzeltmiyor). Ajan betiği skill klasöründen çağırmalı.

### ui-ux-pro-max@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** Catalog-only UI/UX Pro Max entry. The full upstream templates, data, and search workflow are not bundled in OpenDesign.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** otomatik

### web-clone  ·  nexu-io/open-design @ e03d5c2  ·  puan 28 (D)

- **Ne yapar:** 网站复刻 / 克隆方法论。USE WHEN 用户说 复刻网站、克隆网站、clone website、抄个站、仿站、 照着这个站做一个、reproduce site、还原某个网页效果、把这个站搬下来改成我的、 复刻某个交互/WebGL/Canvas/Three.js 效果。提供「先拿真源码 → 判路径 → 逆向拆解 → 搭工程 → 替换内容」的可移植决策树，覆盖静态站 / React-Vue-Next 内容站 / WebGL-Canvas 重前端站三大分支，并强制核对任何 AI 二手分析里的可执行代码。
- **Teknoloji:** api-anahtari, canvas, css, git, gsap, html, lenis, node, playwright, react, tailwind, three.js, vue, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 198 KB (SKILL.md 20.8 KB, yük orta)
- **İnceleme:** otomatik

### web-design-guidelines  ·  vudovn/ag-kit @ 549ba3d  ·  puan 85 (A)

- **Ne yapar:** UI kodunu Vercel'in Web Interface Guidelines kurallarına göre denetler: kuralları her çalıştırmada GitHub'dan (vercel-labs/web-interface-guidelines) çeker, belirtilen dosyaları okuyup bulguları kısa 'dosya:satır' biçiminde raporlar.
- **Ne zaman:** 'UI'ımı incele', 'erişilebilirliği kontrol et', 'tasarımı denetle' isteklerinde hızlı kural denetimi. · **Ne zaman değil:** Ağ erişimi yoksa; görsel/estetik eleştiri (impeccable critique) gerektiğinde.
- **Teknoloji:** html, css, react · **Paketler:** WebFetch / ağ erişimi
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ui-denetim-iyilestirme → tamamlayıcı · **Roller:** qa-erisilebilirlik · **Globalde:** claude:farkli
- **Boyut:** 2 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Çok kısa ve etkili. Dikkat: talimatların asıl gövdesi çalışma anında uzak bir URL'den çekiliyor (sürüm sabitlenmemiş); kaynak güvenilir (vercel-labs) ama içerik değişebilir.

### web-design-guidelines@calesthio  ·  calesthio/OpenMontage @ c806645  ·  puan 87 (A)

- **Ne yapar:** web-design-guidelines'ın OpenMontage kopyası; ag-kit sürümünün 'İlgili skiller' ve iş akışı bölümleri olmadan aynı içerik.
- **Ne zaman:** Globalde kurulu sürümle birebir aynı içerik gerektiğinde. · **Ne zaman değil:** Normalde (tercih sürümü aynı işi yapar).
- **Teknoloji:** html, css · **Paketler:** WebFetch / ağ erişimi
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★70788, son güncelleme 2026-10-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** ui-denetim-iyilestirme → alternatif · **Globalde:** claude:ayni
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Tercih sürümüyle aynı denetim; ek bölümler yok. Globaldeki kopyayla aynı.

### web-design-guidelines@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 30 (D)

- **Ne yapar:** Review UI code for Web Interface Guidelines compliance by the Vercel engineering team. Covers layout, typography, color, motion, and accessibility for product UI.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ? (?, ★?, son güncelleme ?, lisans Apache-2.0)
- **Durum:** alternatif · **Globalde:** claude:farkli
- **Boyut:** 10 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** otomatik
