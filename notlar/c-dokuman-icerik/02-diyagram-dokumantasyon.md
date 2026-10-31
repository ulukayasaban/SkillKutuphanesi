# 02-diyagram-dokumantasyon — Doküman ve İçerik

_Diyagram, teknik dokümantasyon, ADR, ortak yazım_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **5/8**

### archify  ·  tt-a1i/archify @ 25cf370  ·  puan 93 (A)

- **Ne yapar:** Mimari, iş akışı, sequence, veri akışı, yaşam döngüsü, ERD, class, ağaç, zaman çizelgesi ve waterfall diyagramlarını doğrulanmış, temalı, animasyonlu tek dosyalık HTML olarak üretir; Mermaid girdisini de anlamına göre yeniden yazar. Kod tabanından kanıta dayalı diyagram çıkarır ve bir cevabı tek sayfalık 'explainer' sayfasına çevirebilir. `node bin/archify.mjs finalize` şema, teslim ve gerçek tarayıcı kontrollerinden geçirir.
- **Ne zaman:** Sistem/mimari açıklama, kod tabanı haritası, API çağrı zinciri, veritabanı şeması, olay zaman çizelgesi; paylaşılabilir etkileşimli diyagram ya da tek sayfa açıklama. · **Ne zaman değil:** Hızlı statik SVG/PNG (beautiful-mermaid) ya da Markdown içine gömülecek Mermaid kodu yeterliyse; dashboard için; Node.js olmayan ortamda (yalnızca elle SVG yedeği var).
- **Teknoloji:** node, html, svg · **Paketler:** node (paket içinde, ek kurulum yok), chromium/playwright (browser-check için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★91869, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** diyagram-uretimi → birincil · **Roller:** dokuman-yazari
- **Boyut:** 7616 KB (SKILL.md 18.4 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). 10 diyagram tipi, şema doğrulama + gerçek tarayıcı kontrolü, onarım akışı ve explainer modu; MIT. Klasör çok büyük (7.6 MB) ve SKILL.md 18 KB; ama referanslar ihtiyaç anında okunuyor. Diyagram grubunda en kapsamlı ve doğrulanabilir seçenek.
- **Not:** Ön kontroldeki 'kirik-baglanti: /abs/path/checkout-timing.html' uyarısı yanlış alarm: SKILL.md satır 133'teki çıktı biçimi örneğindeki yer tutucu yol; eksik dosya yok.

### beautiful-mermaid  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Mermaid diyagramlarını Beautiful Mermaid kütüphanesiyle temalı SVG'ye, ardından tarayıcı ekran görüntüsüyle yüksek çözünürlüklü PNG'ye çevirir. Flowchart, sequence, state, class ve ER diyagramlarını, 13 hazır temayı (Tokyo Night, Nord, GitHub…) destekler.
- **Ne zaman:** Belgeye, slayta ya da videoya konacak statik, temalı diyagram görseli (SVG/PNG) gerektiğinde. · **Ne zaman değil:** Etkileşimli/keşfedilebilir diyagram ya da kod tabanından kanıtlı mimari gerekiyorsa (archify). PNG adımı 'agent-browser' skill'ini istiyor; kütüphanede yok — PNG için playwright/chromium ile ekran görüntüsü alınarak uyarlanmalı.
- **Teknoloji:** typescript, bun, mermaid, svg · **Paketler:** bun veya tsx/deno, beautiful-mermaid (npm), agent-browser CLI (PNG için; yoksa playwright)
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** diyagram-uretimi → alternatif · **Roller:** dokuman-yazari · **Globalde:** claude:ayni
- **Boyut:** 19 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kısa, net, sözdizimi tuzakları belgelenmiş. AGPL-3.0 (OpenMontage). PNG adımı kütüphanede olmayan agent-browser'a bağlı. Statik görsel için iyi; birincil archify.

### d3-visualization  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Teaches the agent to produce D3 charts and interactive data visualizations. A comprehensive D3.js skill with examples across chart types and techniques giving the agent expert-level knowledge to generate complex, interactive visualizations. Useful for editorial dashboards, reports, data-rich prototypes, and explanatory graphics.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### data-report  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Turns CSV, Excel, or JSON data into a polished visual report page.
- **Teknoloji:** canvas, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### doc-coauthoring  ·  anthropics/skills @ dbd4588  ·  puan 92 (A)

- **Ne yapar:** Kullanıcıyla birlikte doküman (spec, öneri, karar dokümanı, PRD, RFC) yazmak için üç aşamalı bir süreç yürütür: bağlam toplama, bölüm bölüm yapılandırma/iyileştirme ve bağlamsız bir alt-agent ile 'okuyucu testi'. Format değil içerik ve okunabilirlik odaklı.
- **Ne zaman:** Önemli bir teknik/iş dokümanı yazılırken; okuyucunun soru işaretlerini önceden yakalamak için. · **Ne zaman değil:** Kısa not, README ya da ADR şablonu yeterliyse (documentation-and-adrs); dosya formatı üretimi için (docx/pptx/pdf).
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★185402, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** teknik-dokumantasyon → tamamlayıcı · **Roller:** dokuman-yazari
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Anthropic resmi; okuyucu testi (taze bağlamlı alt-agent) diğer doküman skillerinde yok. Codex'te alt-agent yoksa yeni oturumla aynı test elle yapılabilir. Doküman ve format skilleriyle tamamlayıcı.

### documentation-and-adrs  ·  addyosmani/agent-skills @ aeac41d  ·  puan 100 (A)

- **Ne yapar:** Kararları ve 'neden'i belgelemeyi öğretir: projedeki mevcut ADR düzenine uyarak ADR yazma, satır içi yorum kuralları, bilinen tuzakları belgeleme, API dokümantasyonu (TSDoc, OpenAPI), README ve changelog. Gereksiz yorumdan kaçınmayı vurgular.
- **Ne zaman:** Mimari karar, public API değişikliği, özellik teslimi; kod tabanına gelecek mühendis/agent için bağlam bırakmak. · **Ne zaman değil:** Uzun iş/strateji dokümanı ortak yazımı (doc-coauthoring); atılacak prototip; Word/PDF teslimatı.
- **Teknoloji:** markdown, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112018, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** teknik-dokumantasyon → birincil · **Roller:** dokuman-yazari · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). addyosmani/agent-skills; 'önce mevcut düzene uy' kuralı ve ne zaman yazılmayacağı net. documentation-templates'ten daha derin ve eylem odaklı; birincil bu.

### documentation-templates  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** README, endpoint bazlı API dokümanı, JSDoc/TSDoc yorumu, Keep-a-Changelog, kısa ADR ve llms.txt gibi AI dostu doküman için hazır şablonlar ve yapı ilkeleri verir.
- **Ne zaman:** Hızlıca README/CHANGELOG/llms.txt iskeleti gerektiğinde; çok kısa bağlam bütçesiyle. · **Ne zaman değil:** Karar kaydı ve 'neden' belgelemesi gerekiyorsa documentation-and-adrs daha iyi. Frontmatter'daki allowed-tools (Read, Glob, Grep) Claude Code'a özgü; Codex bunu yok sayar, skill yine çalışır.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** teknik-dokumantasyon → alternatif
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Küçük (3 KB) ve derli toplu ama yalnızca şablon; süreç/karar rehberi yok. llms.txt şablonu tek ayırt edici yanı.

### live-panel  ·  ythx-101/live-panel-skill @ 439c9ad  ·  puan 83 (A)

- **Ne yapar:** Build a terminal-style, always-running animated architecture diagram (a "live panel") from a JSON config and render it to an mp4. Use when the user wants a system, agent or org architecture diagram that looks like a monitoring dashboard in a terminal window - fixed layout, glowing packets on the wires, scrolling log, counters, bars that flip state - as a screen-recording-style video or a live web 
- **Teknoloji:** canvas, css, ffmpeg, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ythx-101 (kisi, ★827, son güncelleme 2026-10-20, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1704 KB (SKILL.md 10.8 KB, yük orta) · **Bağımlılık:** Python 3 + tarayıcı (Playwright/Chromium) ile kare yakalayıp ffmpeg ile mp4 üretir.
- **İnceleme:** otomatik
