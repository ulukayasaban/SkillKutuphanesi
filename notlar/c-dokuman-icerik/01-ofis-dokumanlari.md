# 01-ofis-dokumanlari — Doküman ve İçerik

_Word, Excel, PowerPoint, PDF üretme/düzenleme_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **4/8**

### article-magazine  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### doc-kami-parchment  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography.
- **Teknoloji:** canvas, css, html, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### docx  ·  anthropics/skills @ ca45fc4  ·  puan 98 (A)

- **Ne yapar:** Word (.docx/.dotx) belgelerini oluşturur, okur ve düzenler. Yeni belge için docx-js (npm), mevcut belge için unzip → XML düzenleme → zip akışı kullanır; run birleştirme, XSD doğrulama, izlenen değişiklik (redline) ve yorum ekleme betikleri içerir. Çıktıyı LibreOffice ile PDF'e çevirip görsel olarak kontrol ettirir.
- **Ne zaman:** Rapor, mektup, sözleşme, şablon gibi teslimatın Word dosyası olduğu her iş; mevcut .docx üzerinde izlenen değişiklik veya yorum. · **Ne zaman değil:** Teslimat PDF (pdf), Google Docs ya da Markdown/HTML ise; içerik yazımı/yapılandırma için doc-coauthoring.
- **Teknoloji:** node, python, docx-js, libreoffice · **Paketler:** docx (npm), pandoc, libreoffice, poppler (pdftoppm), defusedxml, lxml
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-docx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1102 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic'in güncel sürümü: kısa SKILL.md (6.7 KB), net görev tablosu, docx-js tuzakları, merge_runs/validate/comment betikleri ve render ile doğrulama. ComposioHQ kopyası bunun eski anlık görüntüsü; bu yüzden birincil bu.

### pdf  ·  anthropics/skills @ ca45fc4  ·  puan 89 (A)

- **Ne yapar:** PDF okuma, metin/tablo çıkarma, birleştirme, bölme, döndürme, filigran, form doldurma, şifreleme ve OCR işlerini Python (pypdf, pdfplumber, reportlab) ve CLI araçlarıyla yapar. Form doldurma için ayrı forms.md, ileri kullanım için reference.md içerir.
- **Ne zaman:** Girdi ya da çıktı PDF olduğunda: rapor PDF'i üretmek, PDF'ten veri çekmek, form doldurmak, sayfa işlemleri. · **Ne zaman değil:** Teslimat düzenlenebilir Word/Excel/PowerPoint ise (docx/xlsx/pptx); HTML'den tasarımlı PDF gerekiyorsa önce HTML üretip tarayıcıyla dönüştürmek daha iyi olabilir.
- **Teknoloji:** python · **Paketler:** pypdf, pdfplumber, reportlab, pypdfium2, poppler-utils, qpdf, pytesseract (OCR)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-pdf → birincil · **Roller:** dokuman-yazari
- **Boyut:** 57 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Kapsamlı ve pratik kod örnekleri; form doldurma betikleri iyi. Diğer ofis skillerine göre daha az 'doğrula' disiplini var. ComposioHQ sürümü neredeyse aynı (39 satır fark) ama eski; birincil bu.

### pptx  ·  anthropics/skills @ ca45fc4  ·  puan 97 (A)

- **Ne yapar:** PowerPoint (.pptx/.potx) sunumlarını oluşturur, okur ve düzenler. Yeni deste için pptxgenjs, şablon/düzenleme için XML akışı kullanır; slayt kopyalama, temizlik, küçük resim ızgarası ve doğrulama betikleri içerir. Renk paleti, tipografi, yerleşim önerileri ve zorunlu içerik/görsel QA adımları vardır.
- **Ne zaman:** Sunum, pitch deck, eğitim slaytı üretimi; mevcut desteyi ya da kurumsal şablonu düzenleme; .pptx'ten metin çıkarma. · **Ne zaman değil:** Web tabanlı/HTML slayt (slides, reveal.js) ya da video istenirse; sadece içerik/metin taslağı gerekiyorsa.
- **Teknoloji:** node, python, pptxgenjs, libreoffice · **Paketler:** pptxgenjs (npm), markitdown[pptx], Pillow, defusedxml, lxml, libreoffice, poppler (pdftoppm)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-pptx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1112 KB (SKILL.md 20.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Güncel Anthropic sürümü; betik tablosu, pptxgenjs tuzakları, tasarım rehberi ve zorunlu render QA'sı tek dosyada. ComposioHQ sürümü html2pptx tabanlı eski akış; birincil bu.

### resume-modern  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Modern minimal resume, single A4 page, ready for print or PDF export.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### view-pdf  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, place signature/initials, or review markup together. Not for summarization or text extraction (use native Read instead).
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★34734, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### xlsx  ·  anthropics/skills @ ca45fc4  ·  puan 97 (A)

- **Ne yapar:** Excel/CSV/TSV dosyalarını openpyxl ve pandas ile oluşturur, okur, düzenler ve temizler. Formül kullanımını zorunlu tutar, LibreOffice ile yeniden hesaplatıp hata raporlayan recalc.py içerir; finansal model renk ve sayı biçimi kuralları tanımlar.
- **Ne zaman:** Teslimatın elektronik tablo olduğu işler: finansal model, veri temizleme, formüllü tablo, format dönüştürme. · **Ne zaman değil:** Teslimat Word/HTML rapor, bağımsız Python betiği, veritabanı hattı ya da Google Sheets API entegrasyonu ise.
- **Teknoloji:** python, libreoffice · **Paketler:** openpyxl, pandas, markitdown, libreoffice
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ofis-xlsx → birincil · **Roller:** dokuman-yazari
- **Boyut:** 1077 KB (SKILL.md 8.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). 'Yeşil recalc doğru demek değil' gibi doğrulama disiplini ve mevcut dosya kurallarına uyma talimatı çok iyi. ComposioHQ sürümünden güncel ve daha net; birincil bu.
