# 01-ofis-dokumanlari — Doküman ve İçerik

_Word, Excel, PowerPoint, PDF üretme/düzenleme_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **14/18**

### article-magazine  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### doc  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Read, create, and edit .docx documents with formatting and layout fidelity via OpenAI's document skill.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### doc-kami-parchment  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography.
- **Teknoloji:** canvas, css, html, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### docx  ·  anthropics/skills @ dbd4588  ·  puan 93 (A)

- **Ne yapar:** Word (.docx/.dotx) belgelerini oluşturur, okur ve düzenler. Yeni belge için docx-js (npm), mevcut belge için unzip → XML düzenleme → zip akışı kullanır; run birleştirme, XSD doğrulama, izlenen değişiklik (redline) ve yorum ekleme betikleri içerir. Çıktıyı LibreOffice ile PDF'e çevirip görsel olarak kontrol ettirir.
- **Ne zaman:** Rapor, mektup, sözleşme, şablon gibi teslimatın Word dosyası olduğu her iş; mevcut .docx üzerinde izlenen değişiklik veya yorum. · **Ne zaman değil:** Teslimat PDF (pdf), Google Docs ya da Markdown/HTML ise; içerik yazımı/yapılandırma için doc-coauthoring.
- **Teknoloji:** node, python, docx-js, libreoffice · **Paketler:** docx (npm), pandoc, libreoffice, poppler (pdftoppm), defusedxml, lxml
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-docx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1102 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic'in güncel sürümü: kısa SKILL.md (6.7 KB), net görev tablosu, docx-js tuzakları, merge_runs/validate/comment betikleri ve render ile doğrulama. ComposioHQ kopyası bunun eski anlık görüntüsü; bu yüzden birincil bu.

### docx@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Anthropic docx skill'inin ComposioHQ deposundaki eski sürümü. docx-js ile yeni belge, Python 'Document' kütüphanesi (ooxml) ile düzenleme ve markdown planlı redline (izlenen değişiklik) akışı sunar; okumadan önce 500-600 satırlık docx-js.md/ooxml.md dosyalarının tamamını okumayı zorunlu tutar.
- **Ne zaman:** Sadece ooxml Python Document kütüphanesiyle toplu redline yapılması gerekiyorsa (eski API'ye bağlı iş akışları). · **Ne zaman değil:** Varsayılan olarak kullanma; güncel ve daha az bağlam tüketen anthropics/docx birincil.
- **Teknoloji:** node, python, docx-js, libreoffice · **Paketler:** docx (npm), pandoc, libreoffice, poppler (pdftoppm), defusedxml
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ofis-docx → alternatif
- **Boyut:** 1158 KB (SKILL.md 9.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Anthropic sürümünün eski kopyası; 'tamamını oku' talimatları bağlamı şişiriyor (1.1 MB klasör). Redline planlama bölümü ayrıntılı ama güncel sürümde validate --author ile daha sağlam karşılanıyor.

### docx@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Create, edit, and analyze Word documents with tracked changes, comments, and formatting. Useful for design briefs, copy docs, and review-ready deliverables.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### minimax-docx  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Professional DOCX document creation and editing using OpenXML SDK. Useful for branded reports, polished proposals, and template-based authoring.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### minimax-pdf  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate, fill, and reformat PDFs with a token-based design system and 15 cover styles. Useful for branded PDFs, e-guides, and reports.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### pdf  ·  anthropics/skills @ dbd4588  ·  puan 84 (A)

- **Ne yapar:** PDF okuma, metin/tablo çıkarma, birleştirme, bölme, döndürme, filigran, form doldurma, şifreleme ve OCR işlerini Python (pypdf, pdfplumber, reportlab) ve CLI araçlarıyla yapar. Form doldurma için ayrı forms.md, ileri kullanım için reference.md içerir.
- **Ne zaman:** Girdi ya da çıktı PDF olduğunda: rapor PDF'i üretmek, PDF'ten veri çekmek, form doldurmak, sayfa işlemleri. · **Ne zaman değil:** Teslimat düzenlenebilir Word/Excel/PowerPoint ise (docx/xlsx/pptx); HTML'den tasarımlı PDF gerekiyorsa önce HTML üretip tarayıcıyla dönüştürmek daha iyi olabilir.
- **Teknoloji:** python · **Paketler:** pypdf, pdfplumber, reportlab, pypdfium2, poppler-utils, qpdf, pytesseract (OCR)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-pdf → birincil · **Roller:** dokuman-yazari
- **Boyut:** 57 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Kapsamlı ve pratik kod örnekleri; form doldurma betikleri iyi. Diğer ofis skillerine göre daha az 'doğrula' disiplini var. ComposioHQ sürümü neredeyse aynı (39 satır fark) ama eski; birincil bu.

### pdf@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 77 (B)

- **Ne yapar:** Anthropic pdf skill'inin ComposioHQ'daki eski kopyası: pypdf/pdfplumber/reportlab ile PDF okuma, çıkarma, birleştirme/bölme ve form doldurma. İçerik güncel sürümle neredeyse aynı.
- **Ne zaman:** Güncel sürüm erişilemezse yedek olarak. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/pdf aynı içeriğin güncel hâli.
- **Teknoloji:** python · **Paketler:** pypdf, pdfplumber, reportlab, poppler-utils, qpdf
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ofis-pdf → alternatif
- **Boyut:** 63 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Güncel sürümün eski kopyası, kendine özgü katkısı yok.

### pdf@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Extract text, create PDFs, and handle forms. Useful for press releases, branded one-pagers, and printable design deliverables.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### pptx  ·  anthropics/skills @ dbd4588  ·  puan 92 (A)

- **Ne yapar:** PowerPoint (.pptx/.potx) sunumlarını oluşturur, okur ve düzenler. Yeni deste için pptxgenjs, şablon/düzenleme için XML akışı kullanır; slayt kopyalama, temizlik, küçük resim ızgarası ve doğrulama betikleri içerir. Renk paleti, tipografi, yerleşim önerileri ve zorunlu içerik/görsel QA adımları vardır.
- **Ne zaman:** Sunum, pitch deck, eğitim slaytı üretimi; mevcut desteyi ya da kurumsal şablonu düzenleme; .pptx'ten metin çıkarma. · **Ne zaman değil:** Web tabanlı/HTML slayt (slides, reveal.js) ya da video istenirse; sadece içerik/metin taslağı gerekiyorsa.
- **Teknoloji:** node, python, pptxgenjs, libreoffice · **Paketler:** pptxgenjs (npm), markitdown[pptx], Pillow, defusedxml, lxml, libreoffice, poppler (pdftoppm)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-pptx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1112 KB (SKILL.md 20.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Güncel Anthropic sürümü; betik tablosu, pptxgenjs tuzakları, tasarım rehberi ve zorunlu render QA'sı tek dosyada. ComposioHQ sürümü html2pptx tabanlı eski akış; birincil bu.

### pptx@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 74 (B)

- **Ne yapar:** Anthropic pptx skill'inin eski sürümü (ComposioHQ). HTML slaytları playwright ile html2pptx dönüştürerek sunum üretir; şablonlu üretimde slayt envanteri, değiştirme JSON'u ve küçük resim ızgarası kullanan uzun bir iş akışı tarif eder.
- **Ne zaman:** HTML/CSS ile tasarlanıp PowerPoint'e çevrilecek sunumlar (html2pptx akışı özellikle isteniyorsa). · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/pptx daha kısa ve günceldir. Playwright/Chromium kurulumu olmayan ortamlarda.
- **Teknoloji:** node, python, pptxgenjs, playwright, html · **Paketler:** pptxgenjs (npm), playwright, sharp, markitdown, libreoffice
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ofis-pptx → alternatif
- **Boyut:** 1201 KB (SKILL.md 25.0 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. html2pptx yaklaşımı tasarım özgürlüğü veriyor ama SKILL.md 25 KB ve 'tamamını oku' dosyalarıyla bağlam yükü yüksek; bağımlılıkları ağır.

### pptx@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Read, generate, and adjust PowerPoint slides, layouts, and templates. Useful for executive decks, training material, and product reviews.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### resume-modern  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Modern minimal resume, single A4 page, ready for print or PDF export.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★103320, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### view-pdf  ·  anthropics/knowledge-work-plugins @ 33d3dea  ·  puan 100 (A)

- **Ne yapar:** Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★31457, son güncelleme 2026-10-22, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### xlsx  ·  anthropics/skills @ dbd4588  ·  puan 92 (A)

- **Ne yapar:** Excel/CSV/TSV dosyalarını openpyxl ve pandas ile oluşturur, okur, düzenler ve temizler. Formül kullanımını zorunlu tutar, LibreOffice ile yeniden hesaplatıp hata raporlayan recalc.py içerir; finansal model renk ve sayı biçimi kuralları tanımlar.
- **Ne zaman:** Teslimatın elektronik tablo olduğu işler: finansal model, veri temizleme, formüllü tablo, format dönüştürme. · **Ne zaman değil:** Teslimat Word/HTML rapor, bağımsız Python betiği, veritabanı hattı ya da Google Sheets API entegrasyonu ise.
- **Teknoloji:** python, libreoffice · **Paketler:** openpyxl, pandas, markitdown, libreoffice
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182751, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-xlsx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1077 KB (SKILL.md 8.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). 'Yeşil recalc doğru demek değil' gibi doğrulama disiplini ve mevcut dosya kurallarına uyma talimatı çok iyi. ComposioHQ sürümünden güncel ve daha net; birincil bu.

### xlsx@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Anthropic xlsx skill'inin eski kopyası (ComposioHQ): formül zorunluluğu, finansal model renk/sayı biçimi kuralları, pandas/openpyxl örnekleri ve LibreOffice ile recalc.py yeniden hesaplama.
- **Ne zaman:** Güncel sürüm yoksa yedek; içerik büyük ölçüde aynı. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/xlsx daha güncel doğrulama kuralları içerir.
- **Teknoloji:** python, libreoffice · **Paketler:** openpyxl, pandas, libreoffice
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77619, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ofis-xlsx → alternatif
- **Boyut:** 18 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Eski kopya; bölüm başlıkları iki kez tekrarlanıyor, recalc.py tek dosya hâlinde (18 KB, hafif) — tek avantajı küçük olması.
