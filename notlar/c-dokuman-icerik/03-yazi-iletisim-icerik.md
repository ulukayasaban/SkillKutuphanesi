# 03-yazi-iletisim-icerik — Doküman ve İçerik

_Yazı, iletişim, pazarlama/içerik, kariyer_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **21/59**

### ad-creative  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Generate and iterate ad creative including headlines, descriptions, and primary text. Useful for paid social and search ad iteration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### competitive-ads-extractor  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 62 (C)

- **Ne yapar:** Rakiplerin Facebook Ad Library, LinkedIn gibi reklam kütüphanelerindeki reklamlarını toplayıp mesaj, vurgulanan problem, hedef kitle ve kreatif kalıplarını analiz etmeyi tarif eder. Betik yok; tarayıcı/kazıma yeteneği agent'ın kendi araçlarına bırakılmış.
- **Ne zaman:** Reklam kampanyası öncesi rakip mesajlarını ve kreatif kalıplarını çıkarmak. · **Ne zaman değil:** Tarayıcı otomasyonu ya da web kazıma aracı yoksa (skill kendi aracını getirmiyor); platform kullanım şartlarının kazımaya izin vermediği durumlarda.
- **Teknoloji:** web-arama, tarayici-otomasyonu · **Paketler:** tarayıcı aracı (playwright/MCP)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** pazarlama-arastirma → alternatif
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sadece istem şablonu; örnek çıktı uydurma ilerleme çubukları içeriyor, kazıma yöntemi tanımsız. Lisans belirtilmemiş.

### competitive-ads-extractor@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Extract and analyze competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### content-research-writer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Blog, makale, bülten gibi içerikleri kullanıcıyla birlikte yazar: taslak/ana hat oluşturma, araştırma ve kaynak gösterme, giriş (hook) iyileştirme, bölüm bölüm geri bildirim ve kullanıcının üslubunu koruma adımlarını tarif eder.
- **Ne zaman:** Kaynaklı blog yazısı, makale, vaka çalışması, düşünce liderliği içeriği. · **Ne zaman değil:** Kurumsal teknik/karar dokümanı (doc-coauthoring); kısa sosyal medya metni; dosya formatı üretimi.
- **Teknoloji:** markdown, web-arama
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** icerik-yazimi → birincil · **Roller:** icerik-pazarlama
- **Boyut:** 14 KB (SKILL.md 13.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). İçerik yazımı için en derli toplu süreç; ana hat şablonu ve kaynak formatı faydalı. Lisans belirtilmemiş; araştırma adımı agent'ın web aracına bağlı.

### copywriting  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Write and rewrite marketing copy for landing pages, homepages, and ads. Useful as a copy chief partner during launches.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### de-ai-ify  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 72 (B)

- **Ne yapar:** Metindeki yapay zekâ kokan kalıpları (aşırı geçiş kelimeleri, klişeler, kaçamak ifadeler, kurumsal jargon, üçlü sıralamalar) temizleyip doğal insan sesine çevirir; '-HUMAN' ekli kopya ve değişiklik listesi üretir.
- **Ne zaman:** Yayın öncesi metni insansılaştırmak; AI tonu taşıyan blog/e-posta/sosyal medya metinleri. · **Ne zaman değil:** Türkçe metinde kalıp listesi doğrudan uymaz (İngilizce odaklı); teknik doküman doğruluğu kontrolü için değil.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** icerik-yazimi → tamamlayıcı · **Roller:** icerik-pazarlama, dokuman-yazari
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Çok küçük (2 KB), net kalıp listesi ve somut önce/sonra örneği; MIT. Her yazı skilline tamamlayıcı son rötuş.

### developer-growth-analysis  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 60 (C)

- **Ne yapar:** Son 24-48 saatlik Claude Code sohbet geçmişini (~/.claude/history.jsonl) okuyup kodlama kalıplarını, eksik alanları ve gelişim önerilerini çıkarır; HackerNews'ten ilgili kaynak toplar ve raporu Rube MCP üzerinden kullanıcının Slack DM'ine gönderir.
- **Ne zaman:** Kişisel geliştirici gelişim raporu; kendi Claude Code çalışma geçmişinden öğrenme listesi. · **Ne zaman değil:** Codex'te doğrudan çalışmaz: geçmiş ~/.codex/sessions altında farklı biçimde tutulur; Codex'te kullanılacaksa okunacak dosya yolu ve JSONL alanları elle uyarlanmalı. Rube/Composio Slack bağlantısı yoksa son adımı atla, raporu dosyaya yaz. Gizli veri içeren geçmişi dışarı göndermek istenmiyorsa kullanma.
- **Teknoloji:** claude-code, mcp, slack · **Paketler:** Rube MCP (Composio) — Slack gönderimi için
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 15.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Claude Code geçmiş dosyasına ve Composio Rube MCP'ye sıkı bağlı; sohbet geçmişini dış servise gönderiyor. Kategorisi de içerikten çok kişisel geliştirici analizi.

### domain-name-brainstormer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 62 (C)

- **Ne yapar:** Proje için yaratıcı alan adı fikirleri üretir ve .com/.io/.dev/.ai gibi uzantılarda müsaitlik kontrolü yapılmasını tarif eder; marka açısından neden iyi olduklarını açıklar ve TLD rehberi verir.
- **Ne zaman:** Yeni ürün/şirket/yan proje için isim ve alan adı beyin fırtınası. · **Ne zaman değil:** Müsaitlik kontrolü için gerçek whois/DNS aracı yoksa sonuçlar tahmin olur — kayıt kararını buna dayandırma.
- **Teknoloji:** web-arama · **Paketler:** whois/DNS sorgu aracı (önerilir)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İsim önerisi kısmı makul ama müsaitlik kontrolünün nasıl yapılacağı tanımsız; örnek çıktı uydurma 'available' işaretleri içeriyor.

### domain-name-brainstormer@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Generate creative domain name ideas and check availability across multiple TLDs including .com, .io, .dev, and .ai.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### geo-fundamentals  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Generative Engine Optimization: içeriğin ChatGPT, Claude, Perplexity, Gemini gibi AI arama motorlarında kaynak gösterilmesi için ilkeler, alıntılanan içerik türleri, kontrol listesi, AI tarayıcı (user-agent) erişimi ve ölçüm. Sayfaları denetleyen geo_checker.py betiği içerir.
- **Ne zaman:** Web sitesi/blog içeriğini AI aramada görünür kılmak; llms.txt, FAQ şeması, AI bot erişim kararı. · **Ne zaman değil:** Klasik Google SEO için seo-fundamentals; uygulama içi metinler için gereksiz. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** html, python · **Paketler:** python3 (geo_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** seo-geo → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 14 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Kısa ve tablolu; ağırlık yüzdeleri gibi bazı rakamlar kaynaksız tahmin. seo-fundamentals ile birlikte kullanılır.

### i18n-localization  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Uluslararasılaştırma ve yerelleştirme kalıpları: react-i18next, next-intl, gettext örnekleri, locale dosya yapısı, çoğul/tarih/sayı biçimleri, RTL desteği ve kontrol listesi. Kodda sabit metinleri bulan i18n_checker.py betiği içerir.
- **Ne zaman:** Uygulamaya çok dil desteği eklemek, sabit metinleri ayıklamak, Türkçe/Arapça (RTL) yerelleştirme. · **Ne zaman değil:** Metin çevirisinin kendisi (içerik yazımı) için değil; tek dilli küçük projelerde. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** react, next.js, python · **Paketler:** react-i18next veya next-intl (projeye göre), python3 (i18n_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Roller:** frontend-muhendis
- **Boyut:** 12 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru temel bilgiler + betik. Aslında yazılım geliştirme konusu; kategori incelemesi b-yazilim oturumunda ele alındığı için burada bırakıldı (frontend-muhendis rolüne uygun).

### ig-audit  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 78 (B)

- **Ne yapar:** Post-mortem on what the user has already posted - which reels actually worked, why, and what to stop making. Use when the user pastes their Instagram insights or past posts and asks "what's working", "why did this flop", "read my analytics", "audit my content", or wants to know what to do more of.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-caption  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Write the Instagram caption - the line that survives the "... more" cut, the body, the single ask, the search terms and the three hashtags - and lint it before it goes out. Use when the user says "write the caption", "caption this", "what do I put in the description", has a reel or a carousel ready and needs the text, or asks about hashtags.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-carousel  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Build an Instagram carousel - the cover that earns the swipe, slide-by-slide copy, and the 1080x1350 files to upload. Use when the user says "carousel", "slides", "swipe post", "turn this into a carousel", or has a list-shaped or step-shaped idea that would die as a single image.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-comment  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Write comments on other people's Instagram posts and reels that read as a person with an opinion, not a bot. Use when the user pastes a post or a reel and wants a comment, says "comment on this", "engage with this", "what do I say here", or wants a batch for their daily engagement round.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-dm  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Write Instagram DMs that get replies - the keyword delivery, the first message to someone who engaged, the collab pitch, and the two follow-ups. Use when the user says "DM this person", "what do I send them", "outreach message", "how do I follow up", "pitch this brand", or is reaching out to someone specific.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-human  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Strip the machine fingerprint out of any draft - em dashes, AI slop words, invisible watermark characters - and score it against a five-check detection panel before it goes out. Use whenever text needs to sound human, when the user says humanize, "does this sound like AI", "remove the em dashes", "de-slop this", "this sounds like ChatGPT", or before any caption, script, comment, reply or DM is sho
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 45 KB (SKILL.md 5.1 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-plan  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 78 (B)

- **Ne yapar:** Build the week on Instagram - what to post, which format, when, and who to engage with. Use when the user says "plan my week", "what should I post", "content calendar", "I have nothing to post about", or wants a posting schedule and an engagement list.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-profile  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Score an Instagram profile out of 100 against a 12-part rubric and rewrite the parts that lose points - name field, bio, link, highlights, pinned three, grid. Use when the user says "optimize my profile", "fix my bio", "score my Instagram", "why don't people follow me", or pastes their profile and asks how it reads.
- **Teknoloji:** three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-reel  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 78 (B)

- **Ne yapar:** Write an Instagram Reel from a raw idea - hook options off 26 formulas, the spoken script, the on-screen text, and a timed beat sheet - in the user's own voice and scored before they shoot it. Use whenever the user wants a Reel, a short-form video script, a hook, a voiceover, "make a reel about X", "what should I say in this video", or is about to record and does not have the first line yet.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-reply  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Handle the comments under the user's own reels and posts - draft replies to the ones worth answering, sorted by which ones are. Use when the user pastes their comments, says "reply to these", "handle my comments", "someone said X on my reel", or is dealing with a critic, a hater or a lead in the comments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-repurpose  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 78 (B)

- **Ne yapar:** Turn one long asset - a YouTube video, podcast, livestream, newsletter, blog post or client call - into a week of reels and carousels. Use when the user says "repurpose this", "turn this into reels", "I have a video/podcast/ transcript", "cut this up", or pastes something long and wants it on Instagram.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-story  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 83 (A)

- **Ne yapar:** Write the day's Instagram Stories - the frame-by-frame sequence, which stickers to use where, and the one that moves people into the DMs. Use when the user says "stories", "what do I post on my story", "story sequence", "poll idea", "I have nothing to story about", or wants to sell something without making a post about it.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### ig-viral  ·  Jakeschincariol/instagram-agent-skill @ d03c56b  ·  puan 78 (B)

- **Ne yapar:** Go and find the reels that are actually working right now in the user's niche, rank them by how far each beat its own account, name the hook formula each one used, and turn that into a swipe file they can shoot from. Use when the user says "find viral videos", "what's working right now", "what are people posting in my niche", "reverse engineer this account", "build me a swipe file", "why is this r
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3977, son güncelleme 2026-09-13, lisans MIT)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** otomatik

### internal-comms  ·  anthropics/skills @ dbd4588  ·  puan 80 (A)

- **Ne yapar:** Şirket içi iletişim metinleri yazar: 3P güncellemeleri (Progress/Plans/Problems), şirket bülteni, SSS cevapları, durum raporu, liderlik ve proje güncellemesi, olay raporu. Türüne göre examples/ altındaki yönerge dosyasını yükler.
- **Ne zaman:** Haftalık durum güncellemesi, yönetime rapor, olay sonrası bilgilendirme, bülten. · **Ne zaman değil:** Dışa dönük pazarlama metni ya da uzun teknik doküman için.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★185499, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ic-iletisim → birincil · **Roller:** dokuman-yazari
- **Boyut:** 22 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil). Anthropic resmi; küçük SKILL.md, türe göre ayrı örnek dosyalar. ComposioHQ kopyası birebir aynı içerik; birincil resmi kaynak.

### internal-comms@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 70 (B)

- **Ne yapar:** Anthropic internal-comms skill'inin ComposioHQ'daki birebir kopyası: 3P güncellemesi, bülten, SSS ve genel iç iletişim yönergeleri.
- **Ne zaman:** Resmi sürüm kullanılamıyorsa yedek. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/internal-comms ile aynı içerik.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** ic-iletisim → alternatif
- **Boyut:** 22 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Dosyalar resmi sürümle aynı; ek değer yok.

### lead-research-assistant  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 62 (C)

- **Ne yapar:** Ürünü/kod tabanını analiz edip ideal müşteri profiline uyan şirketleri bulmayı, uygunluk puanıyla sıralamayı ve kişiselleştirilmiş iletişim stratejisi önermeyi tarif eder.
- **Ne zaman:** B2B satış/iş geliştirme için potansiyel müşteri listesi ve yaklaşım önerisi. · **Ne zaman değil:** Web araması yoksa (şirket listesi uydurulabilir); kişisel veri toplama/zenginleştirme hukuki açıdan sorunluysa.
- **Teknoloji:** web-arama
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** pazarlama-arastirma → birincil
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İstem şablonu düzeyinde; doğrulama ve veri kaynağı tanımı yok. Lisans belirtilmemiş.

### li-audit  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 77 (B)

- **Ne yapar:** Post-mortem on what the user has already published - which posts actually worked, why, and what to stop doing. Use when the user pastes their LinkedIn analytics or past posts and asks "what's working", "why did this flop", "read my analytics", "audit my content", or wants to know what to double down on.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk)
- **İnceleme:** otomatik

### li-carousel  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Build a LinkedIn document post (carousel) - slide-by-slide copy, the cover that earns the swipe, and the PDF to upload. Use when the user says "carousel", "document post", "slides for LinkedIn", "turn this into a carousel", or has a list-shaped idea that would die as a text post.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### li-comment  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Write comments on other people's LinkedIn posts that read as a person with an opinion, not a bot. Use when the user pastes a post and wants a comment, says "comment on this", "engage with this", "what do I say here", or wants a batch of comments for their engagement round.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** otomatik

### li-dm  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Write connection notes and DM follow-ups that get replies - the 200-character invite, the first message, and the two follow-ups. Use when the user says "write a connection request", "DM this person", "outreach message", "how do I follow up", or is reaching out to someone specific on LinkedIn.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** otomatik

### li-human  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Strip the machine fingerprint out of any draft - em dashes, AI slop words, invisible watermark characters - and score it against a five-check detection panel before it goes out. Use whenever text needs to sound human, when the user says humanize, "does this sound like AI", "remove the em dashes", "de-slop this", "will this get flagged", or before any LinkedIn post, comment, reply or DM is shown to
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 37 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### li-inbox  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Triage the LinkedIn inbox - sort connection requests and DMs into leads, recruiters, peers and spam, and draft the replies worth sending. Use when the user says "my inbox is a mess", "triage my DMs", "should I reply to this", pastes a batch of LinkedIn messages, or is drowning in connection requests.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### li-plan  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 77 (B)

- **Ne yapar:** Build the week on LinkedIn - what to post, when to post it, and who to engage with. Use when the user says "plan my week", "what should I post", "content calendar", "I have nothing to post about", or wants a posting schedule and an engagement list.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** otomatik

### li-post  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 77 (B)

- **Ne yapar:** Write a LinkedIn post from a raw idea using 21 proven hook formulas, in the user's own voice, humanized so it does not read as AI. Use whenever the user wants a LinkedIn post, a hook, a draft for the feed, "post about X", "turn this into a LinkedIn post", or asks for hook options. Produces three hook options, one full draft, and a copy-ready block that is never published without an explicit yes.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### li-profile  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Score a LinkedIn profile out of 100 against a 12-part rubric and rewrite the parts that lose points - headline, about, experience, featured, banner. Use when the user says "optimize my profile", "score my LinkedIn", "rewrite my headline", "fix my about section", or pastes their profile and asks how it reads.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** otomatik

### li-reply  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 82 (A)

- **Ne yapar:** Handle the replies under the user's own LinkedIn posts - draft answers to every comment, sorted by which ones are worth answering. Use when the user pastes the comments on their post, says "reply to these", "handle my comments", "someone said X on my post", or is dealing with a critic or a lead in the comments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### li-repurpose  ·  Jakeschincariol/linkedin-agent-skill @ add2c23  ·  puan 77 (B)

- **Ne yapar:** Turn one long asset - a YouTube video, podcast, newsletter, blog post, transcript or client call - into a week of LinkedIn posts. Use when the user says "repurpose this", "turn this into posts", "I have a video/newsletter/ transcript", or pastes a long piece of content and wants it on LinkedIn.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★2962, son güncelleme 2026-09-17, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### marketing-psychology  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Apply psychological principles and behavioral science to copy and design. Useful for tightening hooks, framing, and pricing presentation.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### meeting-insights-analyzer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Toplantı transkriptlerinden iletişim kalıplarını çıkarır: çatışmadan kaçınma, konuşma oranı, dolgu kelimeler, dinleme ve kolaylaştırma; zaman damgalı örneklerle eyleme dönük geri bildirim ve zaman içinde trend karşılaştırması verir.
- **Ne zaman:** Liderlik/iletişim koçluğu, performans değerlendirmesine hazırlık, ekip toplantı analizi (transkript mevcutsa). · **Ne zaman değil:** Ses kaydı tek başına varsa önce STT gerekir (speech-to-text); toplantı özeti/aksiyon listesi çıkarmak tek amaçsa gereğinden ağır.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 9.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Analiz boyutları ve geri bildirim formatı iyi tanımlı; dar kullanım alanı.

### paywall-upgrade-cro  ·  nexu-io/open-design @ e03d5c2  ·  puan 66 (B)

- **Ne yapar:** Design and optimize upgrade screens, paywalls, and upsell modals. Useful for SaaS conversion design and pricing-page experiments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### raffle-winner-picker  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 62 (C)

- **Ne yapar:** Liste, CSV/Excel ya da Google Sheets'ten çekiliş/yarışma kazananını rastgele seçer; çoklu kazanan, tekrar engelleme, ağırlıklı seçim ve yedek kazanan seçeneklerini tarif eder.
- **Ne zaman:** Sosyal medya çekilişi, etkinlik çekilişi, rastgele katılımcı seçimi. · **Ne zaman değil:** Yasal denetim gerektiren çekilişlerde (noter vb.) tek kanıt olarak; Google Sheets erişimi yoksa.
- **Teknoloji:** python · **Paketler:** python secrets modülü (önerilir)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Betik yok; 'kriptografik rastgele' iddiası agent'ın yazacağı koda bağlı. Kategoriye de tam uymuyor (araç).

### research-decision-room  ·  nexu-io/open-design @ e03d5c2  ·  puan 96 (A)

- **Ne yapar:** Turn messy user research notes, interviews, support tickets, surveys, and product context into an evidence-backed decision room: a single HTML artifact with an evidence ledger, theme map, confidence heatmap, opportunity matrix, decision memo, and experiment queue. Use when teams need to move from qualitative signals to product or design decisions without fabricating certainty.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 38 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### seo-fundamentals  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** SEO temelleri: E-E-A-T, Core Web Vitals hedefleri, teknik SEO (sitemap, robots, canonical), sayfa öğeleri, schema türleri, AI içerik kuralları ve ölçüm. HTML/JSX sayfalarını denetleyen seo_checker.py betiği içerir.
- **Ne zaman:** Web sitesi yayın öncesi SEO denetimi; meta etiketleri, başlık hiyerarşisi, schema ekleme. · **Ne zaman değil:** AI arama görünürlüğü için geo-fundamentals; uygulama içi (giriş gerektiren) sayfalarda. allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** html, python · **Paketler:** python3 (seo_checker.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** seo-geo → birincil · **Roller:** icerik-pazarlama, frontend-muhendis
- **Boyut:** 9 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil). Kısa, güncel metrikler (INP) ve betikli denetim. Derinlik sınırlı ama kontrol listesi olarak yeterli.

### tailored-resume-generator  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** İş ilanını analiz edip anahtar gereksinimleri çıkarır ve adayın deneyimini buna göre yeniden düzenleyen, ATS uyumlu, ilana özel özgeçmiş üretir; kariyer geçişi senaryosu ve eksik/iyileştirme önerileri içerir.
- **Ne zaman:** Belirli bir iş başvurusu için CV uyarlama. · **Ne zaman değil:** Özgeçmişte olmayan deneyimi uydurmak için asla; tasarımlı PDF/Word çıktısı gerekiyorsa docx/pdf ile birlikte kullan.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Adımlar ve örnek çıktı makul; kişisel kullanım için uygun, proje rollerine eklenmez.

### twitter-algorithm-optimizer  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Twitter/X'in açık kaynak öneri algoritması bileşenlerine (Real-graph, SimClusters, TwHIN, Tweepcred) dayanarak tweet taslaklarını analiz edip etkileşim ve erişim için yeniden yazar; olumsuz sinyallerden kaçınma taktikleri verir.
- **Ne zaman:** X/Twitter gönderisi optimizasyonu, içerik stratejisi. · **Ne zaman değil:** Diğer platformlar (LinkedIn, Instagram) için; algoritma 2023 açık kaynak sürümüne dayanıyor, güncel davranış farklı olabilir.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Roller:** icerik-pazarlama
- **Boyut:** 13 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Algoritma kavramlarını somut yazım taktiklerine bağlıyor; güncellik riski var. Lisans AGPL-3.0 olarak beyan edilmiş.

### writing-guidelines  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 87 (A)

- **Ne yapar:** Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33274, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-guidelines@nexu-io  ·  nexu-io/open-design @ e03d5c2  ·  puan 96 (A)

- **Ne yapar:** Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105084, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 17 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-audit  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Audit a YouTube channel end to end - packaging, consistency, the first fifteen seconds, and what to fix first. Use for "audit my channel", "why isn't my channel growing", "review my videos", or a pasted channel URL.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-chapters  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Write YouTube chapters from a transcript, validated against YouTube's own rules so they actually render. Use for "add chapters", "timestamps", "break this video into sections".
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-comment  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Draft replies to YouTube comments in the creator's voice, triaged by which ones are worth answering. Use for "reply to my comments", "handle the comment section", "someone asked X", or a pasted comment thread.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-edit  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Turn a raw recording's transcript into an edit decision list - dead air, filler cues and retakes, with timecodes. Use for "edit this", "cut the dead space", "tighten this video", "I rambled", or any request to shorten footage from a transcript.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-package  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Write and lint the title and thumbnail for a YouTube video as one pairing, checking truncation, duplication and vagueness before publish. Use for "title ideas", "what should I call this", "thumbnail text", "my CTR is bad", packaging, or any request to rename or repackage an existing video.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-plan  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Plan a week or a month of YouTube uploads - what to post, when, and in what order, sized to the creator's actual capacity. Use for "plan my week", "content calendar", "what should I post", "I have no idea what to make next".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-retention  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Read a YouTube Studio audience-retention export and find where viewers actually leave, then say what to change. Use for "why do people stop watching", "my retention is bad", a pasted retention chart or CSV, or "fix my pacing".
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-script  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 79 (B)

- **Ne yapar:** Write a YouTube video script from a raw idea - hook options off 21 formulas, scored, then the full spoken script with the retention beats marked. Use whenever the user wants a video script, a hook, an opening line, "what should I say", "write my next video", or is about to record and does not have the first fifteen seconds yet.
- **Teknoloji:** python, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-seo  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Write the description, tags and search-facing text for a YouTube video, aimed at the query a real person types. Use for "write my description", "tags", "SEO", "help this video get found", "nobody is finding this".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-shorts  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 84 (A)

- **Ne yapar:** Find the Shorts hiding inside a long video and write them, using the transcript to pick self-contained moments. Use for "cut this into shorts", "clip this", "repurpose this video", "what should I clip".
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** otomatik

### yt-viral  ·  Jakeschincariol/youtube-agent-skill @ a2feb21  ·  puan 79 (B)

- **Ne yapar:** Find what is actually working in the user's niche on YouTube and rank it by how far each video beat its own channel, then name the formula. Use for "what's working right now", "find viral videos in my niche", "why did this blow up", competitor research, or a swipe file.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Jakeschincariol (kisi, ★3894, son güncelleme 2026-09-16, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik
