# 04-not-alma-bilgi-yonetimi — Doküman ve İçerik

_Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **15/35**

### add-frontmatter  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 71 (B)

- **Ne yapar:** Obsidian notlarını (tek dosya ya da klasör) okuyup not türüne göre (toplantı, günlük, referans, proje) YAML frontmatter özellikleri ekler veya normalleştirir; mevcut geçerli özellikleri korur, adlandırma ve değer tipi kurallarını uygular.
- **Ne zaman:** Obsidian kasasında etiket/özellik düzeni kurmak, Bases görünümlerine veri hazırlamak. · **Ne zaman değil:** Obsidian dışı Markdown projelerinde (Jekyll/Hugo frontmatter şeması farklı).
- **Teknoloji:** obsidian, markdown, yaml
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Not türüne göre hazır özellik şablonları ve kalite kontrolleri net; MIT, küçük (4 KB).

### autoresearch@agricidaniel  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Run a bounded, source-grounded research loop, draft a cited dossier, and optionally propose a separately reviewed canonical vault merge. Use when the user wants autonomous or deep research that may access the public web. Triggers: /autoresearch, autoresearch, research this topic, deep dive into, investigate, find everything about, research and file, go research, build a wiki on.
- **Teknoloji:** git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 10 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### canvas  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Create, inspect, and update Obsidian JSON Canvas boards with text, file, link, group, and edge nodes. Use for canvas status, canvas lists, visual maps, zones, spatial layouts, adding vault notes or media to a .canvas file, and requests such as create canvas, add to canvas, or put this on the canvas.
- **Teknoloji:** canvas, git, node, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 5.8 KB, yük kucuk)
- **İnceleme:** otomatik

### daily-review  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Gün sonu değerlendirmesi: bugün değişen/oluşan notları bulur, ilerlemeyi, takılan işleri ve içgörüleri çıkarır, yarının ilk 3 önceliğini ve açık döngüleri içeren bir günlük not yazar.
- **Ne zaman:** Obsidian/Markdown kasasında günlük kapanış ve ertesi gün planı. · **Ne zaman değil:** Not kasası yoksa; ekip durum raporu için internal-comms daha uygun.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** periyodik-degerlendirme → tamamlayıcı
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve kullanışlı şablon; weekly-synthesis ile aynı ailede (gün/hafta).

### defuddle  ·  kepano/obsidian-skills @ 3ccff53  ·  puan 88 (A)

- **Ne yapar:** Extract clean Markdown from HTML pages with Defuddle CLI.
- **Teknoloji:** api-anahtari, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kepano (kisi, ★50753, son güncelleme 2026-09-15, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** otomatik

### defuddle@agricidaniel  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Plan optional Defuddle extraction and retain already available local source files through reviewed filesystem capture. Use for defuddle, clean this URL, strip page clutter, readable Markdown from a web page, or preparing a web source for later wiki ingestion. Network extraction remains unavailable until an enforcing adapter is verified.
- **Teknoloji:** api-anahtari, html, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### download-attachment  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Verilen URL'lerden dosyaları Obsidian kasasının 05_Attachments klasörüne indirir (yalnızca http/https, dosya adı temizleme, zaman aşımı), içeriğe göre anlamlı adlandırır, dizini günceller ve git commit atar.
- **Ne zaman:** Claudesidian düzenindeki kasaya web'den PDF/görsel ek kaydetmek. · **Ne zaman değil:** Claudesidian klasör düzeni (05_Attachments, organize-attachments) yoksa yolları uyarlamadan; güvenilmeyen kaynaklardan dosya indirmek için.
- **Teknoloji:** bash, obsidian · **Paketler:** curl veya wget, pdftotext (poppler)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (dar). URL doğrulama ve yol temizleme gibi güvenlik adımları iyi; claudesidian'a özgü klasör adları ve komutlara bağımlı.

### file-organizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Bilgisayardaki klasörleri (İndirilenler, Belgeler, projeler) analiz eder; kopya dosyaları bulur, mantıklı klasör yapısı önerir ve kullanıcı onayıyla taşıma/yeniden adlandırma yapar.
- **Ne zaman:** Dağınık İndirilenler/Belgeler klasörünü düzenlemek, kopyaları bulmak, proje arşivleme öncesi temizlik. · **Ne zaman değil:** Onay almadan toplu taşıma/silme gerektiğinde (geri alınamaz işler); Obsidian kasası için inbox-processor daha uygun.
- **Teknoloji:** bash
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78745, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** dosya-duzenleme → birincil
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Onay isteyen adımlar ve örnekler makul; betik yok, kopya tespiti agent'ın komutlarına bağlı. Lisans belirtilmemiş.

### inbox-processor  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Kasanın 00_Inbox klasöründeki notları PARA yöntemine göre (Projects/Areas/Resources/Archive/Sil) sınıflandırır; her not için hedef klasör, gerekçe ve ilişkili notlar içeren bir eylem planı sunar.
- **Ne zaman:** PARA düzenli Obsidian kasasında gelen kutusu temizliği. · **Ne zaman değil:** PARA klasör yapısı yoksa (klasör adları uyarlanmalı); genel dosya düzeni için file-organizer.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve net sınıflandırma kuralları; claudesidian klasör adlarına bağlı.

### init-bootstrap  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 60 (C)

- **Ne yapar:** Claudesidian kasası için etkileşimli kurulum sihirbazı: klasör adı, bağımlılık kurulumu (pnpm/npm), git durumu, mevcut kasa yapısı ve çalışma alışkanlıkları hakkında sorular sorup kişiselleştirilmiş CLAUDE.md üretir.
- **Ne zaman:** claudesidian şablonuyla yeni Obsidian kasası kurarken ilk yapılandırma. · **Ne zaman değil:** claudesidian dışındaki projelerde. Codex'te: allowed-tools (Task, MultiEdit) Claude Code'a özgü; üretilen dosyayı CLAUDE.md yerine AGENTS.md olarak yazdırmak gerekir.
- **Teknoloji:** obsidian, node, git · **Paketler:** pnpm veya npm, git
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → birincil
- **Boyut:** 30 KB (SKILL.md 29.6 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV (şablona özgü). Ayrıntılı ama 30 KB ve tamamen claudesidian deposuna bağlı; git origin silme gibi geri alınması zor adımlar içeriyor.

### install-claudesidian-command  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 59 (C)

- **Ne yapar:** Kabuğa (bash/zsh/fish) `claudesidian` adlı bir alias/fonksiyon ekler: kasa klasörüne geçip `claude --resume` ile oturumu sürdürür ya da yeni oturum açar; yol kaçışlama ve güvenlik notları içerir.
- **Ne zaman:** claudesidian kasasını terminalden tek komutla açmak. · **Ne zaman değil:** Codex kullanıcıları için olduğu gibi kullanma: komut `claude` CLI'ını çağırıyor; Codex'te alias içindeki komutu `codex resume --last || codex` olarak değiştirerek uyarlanabilir. Kabuk yapılandırma dosyasını değiştirir — onaysız çalıştırma.
- **Teknoloji:** bash, claude-code · **Paketler:** claude CLI
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → tamamlayıcı
- **Boyut:** 10 KB (SKILL.md 10.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. İşini iyi tarif ediyor (fish desteği, özel karakter kaçışı) ama tek amaçlı ve Claude CLI'a bağlı.

### invoice-organizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Fatura ve fişleri (PDF, taranmış görsel, e-posta eki) okuyup satıcı, tarih, tutar, fatura no gibi bilgileri çıkarır; `YYYY-AA-GG Satıcı - Fatura - Ürün.pdf` biçiminde yeniden adlandırıp satıcıya/kategoriye/döneme göre klasörler, CSV özet üretir; orijinalleri korur.
- **Ne zaman:** Vergi dönemi hazırlığı, gider mutabakatı, muhasebeciye belge hazırlama. · **Ne zaman değil:** Muhasebe kaydı/vergi beyanı yerine geçmez; OCR doğruluğu kontrol edilmeden finansal karar için kullanma.
- **Teknoloji:** python, pdf · **Paketler:** pdftotext veya pdfplumber, OCR aracı (taranmış fişler için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78745, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** dosya-duzenleme → tamamlayıcı
- **Boyut:** 12 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Adlandırma standardı ve klasör stratejileri iyi; çıkarma için pdf skilliyle birlikte kullanılır. Lisans belirtilmemiş.

### json-canvas@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** Obsidian'ın kullandığı JSON Canvas 1.0 (.canvas) dosyalarını oluşturur ve düzenler: text/file/link/group düğümleri, kenarlar, renkler, yerleşim önerileri ve doğrulama kuralları. Zihin haritası, proje panosu ve akış şeması örnekleri içerir.
- **Ne zaman:** Obsidian kasasında görsel tuval, zihin haritası ya da not bağlantı haritası üretmek. · **Ne zaman değil:** Obsidian/JSON Canvas kullanılmıyorsa; yayınlanacak diyagram için archify veya beautiful-mermaid.
- **Teknoloji:** json, obsidian
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Spesifikasyonu eksiksiz ve örnekli anlatıyor; dar kapsamlı. Asıl yeri Obsidian not yönetimi olduğu için 04-not-alma-bilgi-yonetimi kategorisine taşındı.

### knap  ·  kepano/obsidian-skills @ 3ccff53  ·  puan 88 (A)

- **Ne yapar:** Render Markdown from templates and structured data using Knap CLI. Use when the user asks to apply a Knap template, turn JSON or CSV data into notes, batch-generate Markdown files, or format Defuddle output into a note.
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kepano (kisi, ★50753, son güncelleme 2026-09-15, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### obsidian-bases@agricidaniel  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 86 (A)

- **Ne yapar:** Explain, draft, and validate Obsidian Bases .base files with filters, formulas, properties, summaries, and table, card, list, or version-gated kanban views. Use for Obsidian Bases, database-like vault views, dynamic tables, reading lists, task trackers, filters, formulas, summaries, and .base file edits.
- **Teknoloji:** git, obsidian, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 7 KB (SKILL.md 7.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### obsidian-bases@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** Obsidian Bases (.base) dosyalarını oluşturur ve düzenler: tam YAML şeması, global/görünüm filtreleri, formül sözdizimi ve fonksiyon başvurusu, tablo/kart/liste/harita görünümleri, özet formülleri.
- **Ne zaman:** Obsidian'da notlardan veritabanı benzeri tablo/kart görünümü kurmak. · **Ne zaman değil:** Obsidian Bases kullanılmıyorsa (Dataview eklentisi farklı sözdizimi kullanır).
- **Teknoloji:** obsidian, yaml
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 16 KB (SKILL.md 16.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Şema ve fonksiyon başvurusu eksiksiz ve örnekli (kaynak kepano/obsidian-skills içeriğiyle uyumlu); MIT.

### obsidian-bases@kepano  ·  kepano/obsidian-skills @ 3ccff53  ·  puan 86 (A)

- **Ne yapar:** Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card views, filters, or formulas in Obsidian.
- **Teknoloji:** obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kepano (kisi, ★50753, son güncelleme 2026-09-15, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 12.7 KB, yük orta)
- **İnceleme:** otomatik

### obsidian-cli  ·  kepano/obsidian-skills @ 3ccff53  ·  puan 88 (A)

- **Ne yapar:** Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. Also supports plugin and theme development with commands to reload plugins, run JavaScript, capture errors, take screenshots, and inspect the DOM. Use when the user asks to interact with their Obsidian vault, manage notes, search vault content, perform vault operations from 
- **Teknoloji:** css, obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kepano (kisi, ★50753, son güncelleme 2026-09-15, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### obsidian-markdown@agricidaniel  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Explain, draft, or validate Obsidian Flavored Markdown syntax: properties, wikilinks, embeds, callouts, tags, comments, highlights, block references, math, and Mermaid. Use when the user explicitly requests Obsidian note formatting or syntax help, not for general Markdown or broad vault operations.
- **Teknoloji:** html, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 5 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### obsidian-markdown@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 69 (B)

- **Ne yapar:** Obsidian Flavored Markdown yazımı: wikilink, gömme (embed), callout, özellikler (properties), etiketler, blok referansları, LaTeX matematik ve diğer Obsidian'a özgü sözdizimi; örneklerle eksiksiz başvuru.
- **Ne zaman:** Obsidian kasasına not yazan/düzenleyen her iş; diğer Obsidian skillerinin temeli. · **Ne zaman değil:** Obsidian dışında (GitHub/GFM) Markdown yazarken wikilink ve callout kullanımı uyumsuz olur.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** obsidian-kasasi → birincil
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Obsidian sözdiziminin en eksiksiz başvurusu; diğer kasa skilleri buna yaslanır.

### obsidian-markdown@kepano  ·  kepano/obsidian-skills @ 3ccff53  ·  puan 86 (A)

- **Ne yapar:** Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when the user mentions wikilinks, callouts, frontmatter, tags, embeds, or Obsidian notes.
- **Teknoloji:** css, obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kepano (kisi, ★50753, son güncelleme 2026-09-15, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 5.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### research-assistant  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Bir konuyu kasadaki notlar üzerinden araştırır: ilgili notları bulup okur, temaları, çelişkileri ve boşlukları çıkarır, wikilink'li bir araştırma özeti ve sonraki adımlar yazar.
- **Ne zaman:** Kasada bir konu hakkında birikmiş bilgiyi sentezlemek. · **Ne zaman değil:** Web araştırması gerekiyorsa (agent-reach, content-research-writer); kasa yoksa.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa, net çıktı yapısı; çelişkileri öne çıkarması değerli.

### save  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 81 (A)

- **Ne yapar:** Save a user-selected answer, decision, insight, or session summary into an Obsidian vault as one reviewed transaction. Use only when the user explicitly asks to preserve specific conversation content, not when they supply a file or URL to ingest. Triggers: /save, save this, save that answer, file this conversation, save this analysis, keep this insight, preserve this chat result.
- **Teknoloji:** obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### think  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Apply the Fable-derived 10-stage OBSERVE, OBSERVE, LISTEN, THINK, CONNECT, CONNECT, FEEL, ACCEPT, CREATE, GROW loop to consequential or ambiguous reasoning and decisions. Use for think this through, deep think, architecture review, postmortem, tradeoff analysis, or challenges to assumptions. This is a reasoning review, not a deterministic vault health check or repair workflow.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### thinking-partner  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Karmaşık bir problemi çözüme koşmadan sorularla birlikte düşünme modu: önce sorar, varsayımları yüzeye çıkarır, içgörüleri kaydeder, kasadaki ilgili notlarla bağlantı kurar ve periyodik özet çıkarır.
- **Ne zaman:** Fikir keşfi, sesli düşünme, karar öncesi problem çerçeveleme. · **Ne zaman değil:** Kullanıcı doğrudan çözüm/uygulama istiyorsa; yapılandırılmış spec gerekiyorsa (planlama skilleri).
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Çok kısa davranış tarifi; brainstorming/idea-refine ile benzer ama 'çözüm üretme' yasağı ayırt edici.

### upgrade  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 59 (C)

- **Ne yapar:** claudesidian kurulumunu GitHub'daki son sürüme yükseltir: sürüm kontrolü, yedek, upstream çekme, dosya dosya anlamsal karşılaştırma ile kullanıcı özelleştirmelerini koruyarak birleştirme, .agents/skills sembolik bağlantı hijyeni ve eski düzenden geçiş.
- **Ne zaman:** claudesidian tabanlı kasayı güncellemek. · **Ne zaman değil:** claudesidian dışı her yerde. Codex'te: allowed-tools (WebFetch, MultiEdit) Claude Code'a özgü; .claude/skills sembolik bağlantı adımları Codex için .agents/skills kanonik konumuyla zaten uyumlu, yalnızca .claude ve .pi bağlantı adımları atlanabilir.
- **Teknoloji:** git, bash, obsidian · **Paketler:** git, curl
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (commands, hooks, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → tamamlayıcı
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV (şablona özgü). Yedek ve çatışma çözüm felsefesi iyi düşünülmüş ama sadece claudesidian'a yarar.

### weekly-synthesis  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Haftanın notlarını ve çalışmalarını tarayıp tekrar eden temaları, içgörüleri, proje ilerlemesini, ortaya çıkan soruları, enerji denetimini ve not bağlantılarını içeren haftalık sentez notu yazar.
- **Ne zaman:** Haftalık değerlendirme, bir sonraki haftanın planı. · **Ne zaman değil:** Kasa/not geçmişi yoksa; ekip haftalık raporu için internal-comms (3P).
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2606, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** periyodik-degerlendirme → birincil
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). Haftalık şablon günlükten daha kapsamlı; daily-review ile birlikte kullanılır.

### wiki  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 86 (A)

- **Ne yapar:** Initialize, adopt, and route work for a separate Obsidian knowledge vault through the portable claude-obsidian core. Use for vault setup, scaffolding, workspace selection, cross-project configuration, or choosing the correct wiki sub-skill. Triggers: /wiki, set up wiki, scaffold vault, create knowledge base, adopt this vault, Obsidian vault, second brain setup, persistent wiki.
- **Teknoloji:** canvas, css, git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 6.1 KB, yük kucuk) · **Kırık bağlantı:** 3
- **İnceleme:** otomatik

### wiki-cli  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Detect and use the official Obsidian command-line interface for read-only vault access; use for wiki-cli, Obsidian CLI, Obsidian read, Obsidian search, vault transport, which transport, transport detection, backlinks, tags, or Obsidian command line. Mutations always go through the claude-obsidian transaction core.
- **Teknoloji:** git, obsidian _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik

### wiki-fold  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Create a bounded, extractive, structurally idempotent rollup of recent Obsidian wiki log entries, with dry-run preview by default and one optional transaction apply. Use for manual log compression without modifying child pages. Triggers: fold the log, run a fold, run wiki-fold, log rollup, roll up log entries, commit the fold.
- **Teknoloji:** git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### wiki-ingest  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 84 (A)

- **Ne yapar:** Ingest supplied source material into an Obsidian vault with provenance and claim tracking: pasted text, files staged in the selected vault's inbox or .raw archive, or explicitly approved URLs. Use for a single source or bounded batch, not for saving an assistant answer. Triggers: ingest, ingest this file, ingest this URL, process this source, read and file this source, batch ingest, ingest these s
- **Teknoloji:** git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.9 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik

### wiki-lint  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Run a deterministic, read-only health check on an Obsidian wiki. Use for lint, vault health check, audit wiki health, find orphans, find dead links, frontmatter audit, provenance audit, or wiki audit. Reports graph, link, frontmatter, provenance-ledger, empty-section, and stale-index findings; it does not reason broadly or repair files.
- **Teknoloji:** git, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### wiki-mode  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Read or configure the vault filing methodology and suggest destinations for planned knowledge creation under Generic, LYT, PARA, or Zettelkasten. Use for wiki mode, methodology mode, what is my vault mode, set vault mode, switch to PARA, use LYT, Zettelkasten setup, change mode, configure mode, or methodology routing. This skill does not save content or migrate notes.
- **Teknoloji:** obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 5.3 KB, yük kucuk)
- **İnceleme:** otomatik

### wiki-query  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 88 (A)

- **Ne yapar:** Answer an explicitly vault-scoped question from an Obsidian wiki without changing it. Use when the user selects the vault as the evidence source: query the wiki, query quick, query deep, explain from the wiki, summarize the vault, find in wiki, search the wiki, or based on the wiki. Do not route ordinary general-knowledge questions here.
- **Teknoloji:** obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### wiki-retrieve  ·  AgriciDaniel/claude-obsidian @ 2e54556  ·  puan 86 (A)

- **Ne yapar:** Build and query a vault-local contextual BM25 retrieval index with optional multilingual Nomic cosine reranking; use for retrieve, hybrid retrieval, BM25, rerank, contextual retrieval, chunk search, vault search, semantic search, find relevant passages, or retrieval diagnostics. Derived caches stay under .vault-meta, remote egress requires explicit consent, and unavailable reranking falls back det
- **Teknoloji:** api-anahtari, obsidian, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** AgriciDaniel (kisi, ★16171, son güncelleme 2026-10-25, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk) · **Kırık bağlantı:** 2
- **İnceleme:** otomatik
