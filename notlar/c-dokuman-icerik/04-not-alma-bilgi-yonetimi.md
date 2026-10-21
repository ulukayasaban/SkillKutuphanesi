# 04-not-alma-bilgi-yonetimi — Doküman ve İçerik

_Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **15/15**

### add-frontmatter  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 75 (B)

- **Ne yapar:** Obsidian notlarını (tek dosya ya da klasör) okuyup not türüne göre (toplantı, günlük, referans, proje) YAML frontmatter özellikleri ekler veya normalleştirir; mevcut geçerli özellikleri korur, adlandırma ve değer tipi kurallarını uygular.
- **Ne zaman:** Obsidian kasasında etiket/özellik düzeni kurmak, Bases görünümlerine veri hazırlamak. · **Ne zaman değil:** Obsidian dışı Markdown projelerinde (Jekyll/Hugo frontmatter şeması farklı).
- **Teknoloji:** obsidian, markdown, yaml
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Not türüne göre hazır özellik şablonları ve kalite kontrolleri net; MIT, küçük (4 KB).

### daily-review  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Gün sonu değerlendirmesi: bugün değişen/oluşan notları bulur, ilerlemeyi, takılan işleri ve içgörüleri çıkarır, yarının ilk 3 önceliğini ve açık döngüleri içeren bir günlük not yazar.
- **Ne zaman:** Obsidian/Markdown kasasında günlük kapanış ve ertesi gün planı. · **Ne zaman değil:** Not kasası yoksa; ekip durum raporu için internal-comms daha uygun.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** periyodik-degerlendirme → tamamlayıcı
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve kullanışlı şablon; weekly-synthesis ile aynı ailede (gün/hafta).

### download-attachment  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Verilen URL'lerden dosyaları Obsidian kasasının 05_Attachments klasörüne indirir (yalnızca http/https, dosya adı temizleme, zaman aşımı), içeriğe göre anlamlı adlandırır, dizini günceller ve git commit atar.
- **Ne zaman:** Claudesidian düzenindeki kasaya web'den PDF/görsel ek kaydetmek. · **Ne zaman değil:** Claudesidian klasör düzeni (05_Attachments, organize-attachments) yoksa yolları uyarlamadan; güvenilmeyen kaynaklardan dosya indirmek için.
- **Teknoloji:** bash, obsidian · **Paketler:** curl veya wget, pdftotext (poppler)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (dar). URL doğrulama ve yol temizleme gibi güvenlik adımları iyi; claudesidian'a özgü klasör adları ve komutlara bağımlı.

### file-organizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Bilgisayardaki klasörleri (İndirilenler, Belgeler, projeler) analiz eder; kopya dosyaları bulur, mantıklı klasör yapısı önerir ve kullanıcı onayıyla taşıma/yeniden adlandırma yapar.
- **Ne zaman:** Dağınık İndirilenler/Belgeler klasörünü düzenlemek, kopyaları bulmak, proje arşivleme öncesi temizlik. · **Ne zaman değil:** Onay almadan toplu taşıma/silme gerektiğinde (geri alınamaz işler); Obsidian kasası için inbox-processor daha uygun.
- **Teknoloji:** bash
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** dosya-duzenleme → birincil
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Onay isteyen adımlar ve örnekler makul; betik yok, kopya tespiti agent'ın komutlarına bağlı. Lisans belirtilmemiş.

### inbox-processor  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Kasanın 00_Inbox klasöründeki notları PARA yöntemine göre (Projects/Areas/Resources/Archive/Sil) sınıflandırır; her not için hedef klasör, gerekçe ve ilişkili notlar içeren bir eylem planı sunar.
- **Ne zaman:** PARA düzenli Obsidian kasasında gelen kutusu temizliği. · **Ne zaman değil:** PARA klasör yapısı yoksa (klasör adları uyarlanmalı); genel dosya düzeni için file-organizer.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve net sınıflandırma kuralları; claudesidian klasör adlarına bağlı.

### init-bootstrap  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 64 (C)

- **Ne yapar:** Claudesidian kasası için etkileşimli kurulum sihirbazı: klasör adı, bağımlılık kurulumu (pnpm/npm), git durumu, mevcut kasa yapısı ve çalışma alışkanlıkları hakkında sorular sorup kişiselleştirilmiş CLAUDE.md üretir.
- **Ne zaman:** claudesidian şablonuyla yeni Obsidian kasası kurarken ilk yapılandırma. · **Ne zaman değil:** claudesidian dışındaki projelerde. Codex'te: allowed-tools (Task, MultiEdit) Claude Code'a özgü; üretilen dosyayı CLAUDE.md yerine AGENTS.md olarak yazdırmak gerekir.
- **Teknoloji:** obsidian, node, git · **Paketler:** pnpm veya npm, git
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → birincil
- **Boyut:** 30 KB (SKILL.md 29.6 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV (şablona özgü). Ayrıntılı ama 30 KB ve tamamen claudesidian deposuna bağlı; git origin silme gibi geri alınması zor adımlar içeriyor.

### install-claudesidian-command  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** Kabuğa (bash/zsh/fish) `claudesidian` adlı bir alias/fonksiyon ekler: kasa klasörüne geçip `claude --resume` ile oturumu sürdürür ya da yeni oturum açar; yol kaçışlama ve güvenlik notları içerir.
- **Ne zaman:** claudesidian kasasını terminalden tek komutla açmak. · **Ne zaman değil:** Codex kullanıcıları için olduğu gibi kullanma: komut `claude` CLI'ını çağırıyor; Codex'te alias içindeki komutu `codex resume --last || codex` olarak değiştirerek uyarlanabilir. Kabuk yapılandırma dosyasını değiştirir — onaysız çalıştırma.
- **Teknoloji:** bash, claude-code · **Paketler:** claude CLI
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → tamamlayıcı
- **Boyut:** 10 KB (SKILL.md 10.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. İşini iyi tarif ediyor (fish desteği, özel karakter kaçışı) ama tek amaçlı ve Claude CLI'a bağlı.

### invoice-organizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Fatura ve fişleri (PDF, taranmış görsel, e-posta eki) okuyup satıcı, tarih, tutar, fatura no gibi bilgileri çıkarır; `YYYY-AA-GG Satıcı - Fatura - Ürün.pdf` biçiminde yeniden adlandırıp satıcıya/kategoriye/döneme göre klasörler, CSV özet üretir; orijinalleri korur.
- **Ne zaman:** Vergi dönemi hazırlığı, gider mutabakatı, muhasebeciye belge hazırlama. · **Ne zaman değil:** Muhasebe kaydı/vergi beyanı yerine geçmez; OCR doğruluğu kontrol edilmeden finansal karar için kullanma.
- **Teknoloji:** python, pdf · **Paketler:** pdftotext veya pdfplumber, OCR aracı (taranmış fişler için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** dosya-duzenleme → tamamlayıcı
- **Boyut:** 12 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Adlandırma standardı ve klasör stratejileri iyi; çıkarma için pdf skilliyle birlikte kullanılır. Lisans belirtilmemiş.

### json-canvas  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 74 (B)

- **Ne yapar:** Obsidian'ın kullandığı JSON Canvas 1.0 (.canvas) dosyalarını oluşturur ve düzenler: text/file/link/group düğümleri, kenarlar, renkler, yerleşim önerileri ve doğrulama kuralları. Zihin haritası, proje panosu ve akış şeması örnekleri içerir.
- **Ne zaman:** Obsidian kasasında görsel tuval, zihin haritası ya da not bağlantı haritası üretmek. · **Ne zaman değil:** Obsidian/JSON Canvas kullanılmıyorsa; yayınlanacak diyagram için archify veya beautiful-mermaid.
- **Teknoloji:** json, obsidian
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 14 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Spesifikasyonu eksiksiz ve örnekli anlatıyor; dar kapsamlı. Asıl yeri Obsidian not yönetimi olduğu için 04-not-alma-bilgi-yonetimi kategorisine taşındı.

### obsidian-bases  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 74 (B)

- **Ne yapar:** Obsidian Bases (.base) dosyalarını oluşturur ve düzenler: tam YAML şeması, global/görünüm filtreleri, formül sözdizimi ve fonksiyon başvurusu, tablo/kart/liste/harita görünümleri, özet formülleri.
- **Ne zaman:** Obsidian'da notlardan veritabanı benzeri tablo/kart görünümü kurmak. · **Ne zaman değil:** Obsidian Bases kullanılmıyorsa (Dataview eklentisi farklı sözdizimi kullanır).
- **Teknoloji:** obsidian, yaml
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → tamamlayıcı
- **Boyut:** 16 KB (SKILL.md 16.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Şema ve fonksiyon başvurusu eksiksiz ve örnekli (kaynak kepano/obsidian-skills içeriğiyle uyumlu); MIT.

### obsidian-markdown  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 73 (B)

- **Ne yapar:** Obsidian Flavored Markdown yazımı: wikilink, gömme (embed), callout, özellikler (properties), etiketler, blok referansları, LaTeX matematik ve diğer Obsidian'a özgü sözdizimi; örneklerle eksiksiz başvuru.
- **Ne zaman:** Obsidian kasasına not yazan/düzenleyen her iş; diğer Obsidian skillerinin temeli. · **Ne zaman değil:** Obsidian dışında (GitHub/GFM) Markdown yazarken wikilink ve callout kullanımı uyumsuz olur.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** obsidian-kasasi → birincil
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta) · **Kırık bağlantı:** 2
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Obsidian sözdiziminin en eksiksiz başvurusu; diğer kasa skilleri buna yaslanır.

### research-assistant  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Bir konuyu kasadaki notlar üzerinden araştırır: ilgili notları bulup okur, temaları, çelişkileri ve boşlukları çıkarır, wikilink'li bir araştırma özeti ve sonraki adımlar yazar.
- **Ne zaman:** Kasada bir konu hakkında birikmiş bilgiyi sentezlemek. · **Ne zaman değil:** Web araştırması gerekiyorsa (agent-reach, content-research-writer); kasa yoksa.
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa, net çıktı yapısı; çelişkileri öne çıkarması değerli.

### thinking-partner  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Karmaşık bir problemi çözüme koşmadan sorularla birlikte düşünme modu: önce sorar, varsayımları yüzeye çıkarır, içgörüleri kaydeder, kasadaki ilgili notlarla bağlantı kurar ve periyodik özet çıkarır.
- **Ne zaman:** Fikir keşfi, sesli düşünme, karar öncesi problem çerçeveleme. · **Ne zaman değil:** Kullanıcı doğrudan çözüm/uygulama istiyorsa; yapılandırılmış spec gerekiyorsa (planlama skilleri).
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Çok kısa davranış tarifi; brainstorming/idea-refine ile benzer ama 'çözüm üretme' yasağı ayırt edici.

### upgrade  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 63 (C)

- **Ne yapar:** claudesidian kurulumunu GitHub'daki son sürüme yükseltir: sürüm kontrolü, yedek, upstream çekme, dosya dosya anlamsal karşılaştırma ile kullanıcı özelleştirmelerini koruyarak birleştirme, .agents/skills sembolik bağlantı hijyeni ve eski düzenden geçiş.
- **Ne zaman:** claudesidian tabanlı kasayı güncellemek. · **Ne zaman değil:** claudesidian dışı her yerde. Codex'te: allowed-tools (WebFetch, MultiEdit) Claude Code'a özgü; .claude/skills sembolik bağlantı adımları Codex için .agents/skills kanonik konumuyla zaten uyumlu, yalnızca .claude ve .pi bağlantı adımları atlanabilir.
- **Teknoloji:** git, bash, obsidian · **Paketler:** git, curl
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (commands, hooks, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** claudesidian-kurulum → tamamlayıcı
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV (şablona özgü). Yedek ve çatışma çözüm felsefesi iyi düşünülmüş ama sadece claudesidian'a yarar.

### weekly-synthesis  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 67 (B)

- **Ne yapar:** Haftanın notlarını ve çalışmalarını tarayıp tekrar eden temaları, içgörüleri, proje ilerlemesini, ortaya çıkan soruları, enerji denetimini ve not bağlantılarını içeren haftalık sentez notu yazar.
- **Ne zaman:** Haftalık değerlendirme, bir sonraki haftanın planı. · **Ne zaman değil:** Kasa/not geçmişi yoksa; ekip haftalık raporu için internal-comms (3P).
- **Teknoloji:** obsidian, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** periyodik-degerlendirme → birincil
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). Haftalık şablon günlükten daha kapsamlı; daily-review ile birlikte kullanılır.
