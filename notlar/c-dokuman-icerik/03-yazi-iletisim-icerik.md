# 03-yazi-iletisim-icerik — Doküman ve İçerik

_Yazı, iletişim, pazarlama/içerik, kariyer_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **21/24**

### ad-creative  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate and iterate ad creative including headlines, descriptions, and primary text. Useful for paid social and search ad iteration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### competitive-ads-extractor  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Rakiplerin Facebook Ad Library, LinkedIn gibi reklam kütüphanelerindeki reklamlarını toplayıp mesaj, vurgulanan problem, hedef kitle ve kreatif kalıplarını analiz etmeyi tarif eder. Betik yok; tarayıcı/kazıma yeteneği agent'ın kendi araçlarına bırakılmış.
- **Ne zaman:** Reklam kampanyası öncesi rakip mesajlarını ve kreatif kalıplarını çıkarmak. · **Ne zaman değil:** Tarayıcı otomasyonu ya da web kazıma aracı yoksa (skill kendi aracını getirmiyor); platform kullanım şartlarının kazımaya izin vermediği durumlarda.
- **Teknoloji:** web-arama, tarayici-otomasyonu · **Paketler:** tarayıcı aracı (playwright/MCP)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** pazarlama-arastirma → alternatif
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sadece istem şablonu; örnek çıktı uydurma ilerleme çubukları içeriyor, kazıma yöntemi tanımsız. Lisans belirtilmemiş.

### competitive-ads-extractor@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Extract and analyze competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### content-research-writer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Blog, makale, bülten gibi içerikleri kullanıcıyla birlikte yazar: taslak/ana hat oluşturma, araştırma ve kaynak gösterme, giriş (hook) iyileştirme, bölüm bölüm geri bildirim ve kullanıcının üslubunu koruma adımlarını tarif eder.
- **Ne zaman:** Kaynaklı blog yazısı, makale, vaka çalışması, düşünce liderliği içeriği. · **Ne zaman değil:** Kurumsal teknik/karar dokümanı (doc-coauthoring); kısa sosyal medya metni; dosya formatı üretimi.
- **Teknoloji:** markdown, web-arama
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** icerik-yazimi → birincil · **Roller:** icerik-pazarlama
- **Boyut:** 14 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). İçerik yazımı için en derli toplu süreç; ana hat şablonu ve kaynak formatı faydalı. Lisans belirtilmemiş; araştırma adımı agent'ın web aracına bağlı.

### copywriting  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Write and rewrite marketing copy for landing pages, homepages, and ads. Useful as a copy chief partner during launches.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### de-ai-ify  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 75 (B)

- **Ne yapar:** Metindeki yapay zekâ kokan kalıpları (aşırı geçiş kelimeleri, klişeler, kaçamak ifadeler, kurumsal jargon, üçlü sıralamalar) temizleyip doğal insan sesine çevirir; '-HUMAN' ekli kopya ve değişiklik listesi üretir.
- **Ne zaman:** Yayın öncesi metni insansılaştırmak; AI tonu taşıyan blog/e-posta/sosyal medya metinleri. · **Ne zaman değil:** Türkçe metinde kalıp listesi doğrudan uymaz (İngilizce odaklı); teknik doküman doğruluğu kontrolü için değil.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** icerik-yazimi → tamamlayıcı · **Roller:** icerik-pazarlama, dokuman-yazari
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Çok küçük (2 KB), net kalıp listesi ve somut önce/sonra örneği; MIT. Her yazı skilline tamamlayıcı son rötuş.

### developer-growth-analysis  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Son 24-48 saatlik Claude Code sohbet geçmişini (~/.claude/history.jsonl) okuyup kodlama kalıplarını, eksik alanları ve gelişim önerilerini çıkarır; HackerNews'ten ilgili kaynak toplar ve raporu Rube MCP üzerinden kullanıcının Slack DM'ine gönderir.
- **Ne zaman:** Kişisel geliştirici gelişim raporu; kendi Claude Code çalışma geçmişinden öğrenme listesi. · **Ne zaman değil:** Codex'te doğrudan çalışmaz: geçmiş ~/.codex/sessions altında farklı biçimde tutulur; Codex'te kullanılacaksa okunacak dosya yolu ve JSONL alanları elle uyarlanmalı. Rube/Composio Slack bağlantısı yoksa son adımı atla, raporu dosyaya yaz. Gizli veri içeren geçmişi dışarı göndermek istenmiyorsa kullanma.
- **Teknoloji:** claude-code, mcp, slack · **Paketler:** Rube MCP (Composio) — Slack gönderimi için
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Claude Code geçmiş dosyasına ve Composio Rube MCP'ye sıkı bağlı; sohbet geçmişini dış servise gönderiyor. Kategorisi de içerikten çok kişisel geliştirici analizi.

### domain-name-brainstormer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Proje için yaratıcı alan adı fikirleri üretir ve .com/.io/.dev/.ai gibi uzantılarda müsaitlik kontrolü yapılmasını tarif eder; marka açısından neden iyi olduklarını açıklar ve TLD rehberi verir.
- **Ne zaman:** Yeni ürün/şirket/yan proje için isim ve alan adı beyin fırtınası. · **Ne zaman değil:** Müsaitlik kontrolü için gerçek whois/DNS aracı yoksa sonuçlar tahmin olur — kayıt kararını buna dayandırma.
- **Teknoloji:** web-arama · **Paketler:** whois/DNS sorgu aracı (önerilir)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İsim önerisi kısmı makul ama müsaitlik kontrolünün nasıl yapılacağı tanımsız; örnek çıktı uydurma 'available' işaretleri içeriyor.

### domain-name-brainstormer@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate creative domain name ideas and check availability across multiple TLDs including .com, .io, .dev, and .ai.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### geo-fundamentals  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Generative Engine Optimization: içeriğin ChatGPT, Claude, Perplexity, Gemini gibi AI arama motorlarında kaynak gösterilmesi için ilkeler, alıntılanan içerik türleri, kontrol listesi, AI tarayıcı (user-agent) erişimi ve ölçüm. Sayfaları denetleyen geo_checker.py betiği içerir.
- **Ne zaman:** Web sitesi/blog içeriğini AI aramada görünür kılmak; llms.txt, FAQ şeması, AI bot erişim kararı. · **Ne zaman değil:** Klasik Google SEO için seo-fundamentals; uygulama içi metinler için gereksiz. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** html, python · **Paketler:** python3 (geo_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** seo-geo → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 14 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Kısa ve tablolu; ağırlık yüzdeleri gibi bazı rakamlar kaynaksız tahmin. seo-fundamentals ile birlikte kullanılır.

### i18n-localization  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Uluslararasılaştırma ve yerelleştirme kalıpları: react-i18next, next-intl, gettext örnekleri, locale dosya yapısı, çoğul/tarih/sayı biçimleri, RTL desteği ve kontrol listesi. Kodda sabit metinleri bulan i18n_checker.py betiği içerir.
- **Ne zaman:** Uygulamaya çok dil desteği eklemek, sabit metinleri ayıklamak, Türkçe/Arapça (RTL) yerelleştirme. · **Ne zaman değil:** Metin çevirisinin kendisi (içerik yazımı) için değil; tek dilli küçük projelerde. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** react, next.js, python · **Paketler:** react-i18next veya next-intl (projeye göre), python3 (i18n_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Roller:** frontend-muhendis
- **Boyut:** 12 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru temel bilgiler + betik. Aslında yazılım geliştirme konusu; kategori incelemesi b-yazilim oturumunda ele alındığı için burada bırakıldı (frontend-muhendis rolüne uygun).

### internal-comms  ·  anthropics/skills @ dbd4588  ·  puan 85 (A)

- **Ne yapar:** Şirket içi iletişim metinleri yazar: 3P güncellemeleri (Progress/Plans/Problems), şirket bülteni, SSS cevapları, durum raporu, liderlik ve proje güncellemesi, olay raporu. Türüne göre examples/ altındaki yönerge dosyasını yükler.
- **Ne zaman:** Haftalık durum güncellemesi, yönetime rapor, olay sonrası bilgilendirme, bülten. · **Ne zaman değil:** Dışa dönük pazarlama metni ya da uzun teknik doküman için.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★185402, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ic-iletisim → birincil · **Roller:** dokuman-yazari
- **Boyut:** 22 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Anthropic resmi; küçük SKILL.md, türe göre ayrı örnek dosyalar. ComposioHQ kopyası birebir aynı içerik; birincil resmi kaynak.

### internal-comms@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 77 (B)

- **Ne yapar:** Anthropic internal-comms skill'inin ComposioHQ'daki birebir kopyası: 3P güncellemesi, bülten, SSS ve genel iç iletişim yönergeleri.
- **Ne zaman:** Resmi sürüm kullanılamıyorsa yedek. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/internal-comms ile aynı içerik.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ic-iletisim → alternatif
- **Boyut:** 22 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Dosyalar resmi sürümle aynı; ek değer yok.

### lead-research-assistant  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Ürünü/kod tabanını analiz edip ideal müşteri profiline uyan şirketleri bulmayı, uygunluk puanıyla sıralamayı ve kişiselleştirilmiş iletişim stratejisi önermeyi tarif eder.
- **Ne zaman:** B2B satış/iş geliştirme için potansiyel müşteri listesi ve yaklaşım önerisi. · **Ne zaman değil:** Web araması yoksa (şirket listesi uydurulabilir); kişisel veri toplama/zenginleştirme hukuki açıdan sorunluysa.
- **Teknoloji:** web-arama
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** pazarlama-arastirma → birincil
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İstem şablonu düzeyinde; doğrulama ve veri kaynağı tanımı yok. Lisans belirtilmemiş.

### marketing-psychology  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Apply psychological principles and behavioral science to copy and design. Useful for tightening hooks, framing, and pricing presentation.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### meeting-insights-analyzer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Toplantı transkriptlerinden iletişim kalıplarını çıkarır: çatışmadan kaçınma, konuşma oranı, dolgu kelimeler, dinleme ve kolaylaştırma; zaman damgalı örneklerle eyleme dönük geri bildirim ve zaman içinde trend karşılaştırması verir.
- **Ne zaman:** Liderlik/iletişim koçluğu, performans değerlendirmesine hazırlık, ekip toplantı analizi (transkript mevcutsa). · **Ne zaman değil:** Ses kaydı tek başına varsa önce STT gerekir (speech-to-text); toplantı özeti/aksiyon listesi çıkarmak tek amaçsa gereğinden ağır.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Analiz boyutları ve geri bildirim formatı iyi tanımlı; dar kullanım alanı.

### paywall-upgrade-cro  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Design and optimize upgrade screens, paywalls, and upsell modals. Useful for SaaS conversion design and pricing-page experiments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### raffle-winner-picker  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Liste, CSV/Excel ya da Google Sheets'ten çekiliş/yarışma kazananını rastgele seçer; çoklu kazanan, tekrar engelleme, ağırlıklı seçim ve yedek kazanan seçeneklerini tarif eder.
- **Ne zaman:** Sosyal medya çekilişi, etkinlik çekilişi, rastgele katılımcı seçimi. · **Ne zaman değil:** Yasal denetim gerektiren çekilişlerde (noter vb.) tek kanıt olarak; Google Sheets erişimi yoksa.
- **Teknoloji:** python · **Paketler:** python secrets modülü (önerilir)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Betik yok; 'kriptografik rastgele' iddiası agent'ın yazacağı koda bağlı. Kategoriye de tam uymuyor (araç).

### research-decision-room  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Turn messy user research notes, interviews, support tickets, surveys, and product context into an evidence-backed decision room: a single HTML artifact with an evidence ledger, theme map, confidence heatmap, opportunity matrix, decision memo, and experiment queue. Use when teams need to move from qualitative signals to product or design decisions without fabricating certainty.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 38 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### seo-fundamentals  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** SEO temelleri: E-E-A-T, Core Web Vitals hedefleri, teknik SEO (sitemap, robots, canonical), sayfa öğeleri, schema türleri, AI içerik kuralları ve ölçüm. HTML/JSX sayfalarını denetleyen seo_checker.py betiği içerir.
- **Ne zaman:** Web sitesi yayın öncesi SEO denetimi; meta etiketleri, başlık hiyerarşisi, schema ekleme. · **Ne zaman değil:** AI arama görünürlüğü için geo-fundamentals; uygulama içi (giriş gerektiren) sayfalarda. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** html, python · **Paketler:** python3 (seo_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** seo-geo → birincil · **Roller:** icerik-pazarlama, frontend-muhendis
- **Boyut:** 9 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). Kısa, güncel metrikler (INP) ve betikli denetim. Derinlik sınırlı ama kontrol listesi olarak yeterli.

### tailored-resume-generator  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** İş ilanını analiz edip anahtar gereksinimleri çıkarır ve adayın deneyimini buna göre yeniden düzenleyen, ATS uyumlu, ilana özel özgeçmiş üretir; kariyer geçişi senaryosu ve eksik/iyileştirme önerileri içerir.
- **Ne zaman:** Belirli bir iş başvurusu için CV uyarlama. · **Ne zaman değil:** Özgeçmişte olmayan deneyimi uydurmak için asla; tasarımlı PDF/Word çıktısı gerekiyorsa docx/pdf ile birlikte kullan.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Adımlar ve örnek çıktı makul; kişisel kullanım için uygun, proje rollerine eklenmez.

### twitter-algorithm-optimizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** Twitter/X'in açık kaynak öneri algoritması bileşenlerine (Real-graph, SimClusters, TwHIN, Tweepcred) dayanarak tweet taslaklarını analiz edip etkileşim ve erişim için yeniden yazar; olumsuz sinyallerden kaçınma taktikleri verir.
- **Ne zaman:** X/Twitter gönderisi optimizasyonu, içerik stratejisi. · **Ne zaman değil:** Diğer platformlar (LinkedIn, Instagram) için; algoritma 2023 açık kaynak sürümüne dayanıyor, güncel davranış farklı olabilir.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78362, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Roller:** icerik-pazarlama
- **Boyut:** 13 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Algoritma kavramlarını somut yazım taktiklerine bağlıyor; güncellik riski var. Lisans AGPL-3.0 olarak beyan edilmiş.

### writing-guidelines  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 96 (A)

- **Ne yapar:** Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33272, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-guidelines@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 95 (A)

- **Ne yapar:** Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 17 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik
