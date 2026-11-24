# 03-web-arastirma-veri — AI ve Otomasyon

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **4/11**

### agent-reach  ·  Panniantong/Agent-Reach @ c70ae6d  ·  puan 95 (A)

- **Ne yapar:** Çok platformlu salt-okunur içerik erişimi için tek CLI (`agent-reach <kanal> <eylem>`, `read <url>`): GitHub, YouTube, Bilibili, Reddit, X/Twitter, Xiaohongshu, Instagram, Facebook, LinkedIn, V2EX, Xueqiu, podcast ve anonim web arama/okuma. JSON çıktı ve hata kodlarıyla çalışır; tarayıcı gerektiren kanallar ortak özel tarayıcıyı (CloakBrowser/Chrome + OpenCLI) kullanır. Önce agent'ın kendi araçlarını dener, Reach boşlukları doldurur. SKILL.md Çince (SKILL_en.md İngilizce).
- **Ne zaman:** Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. · **Ne zaman değil:** Yazma işlemleri (gönderi, yorum, beğeni) için değil; agent-reach CLI kurulu değilse (kanal tablosu kurulumda doldurulan şablon). Gizlilik: kullanıcının Chrome'una OpenCLI eklentisi bağlıysa o sitenin giriş çerezleri özel tarayıcıya kopyalanır; açık onay olmadan kurma. 2026-11'de eski Exa/RSS/jina/yt-dlp doğrudan komutları kaldırıldı.
- **Teknoloji:** python, cli, web-arama · **Paketler:** agent-reach CLI (pip/uv; browser setup ile Node, OpenCLI, CloakBrowser/Chrome indirilir), platforma göre: yt-dlp, gh, bili CLI, opsiyonel: Groq anahtarı (podcast transkripsiyonu), github-token, proxy
- **Claude / Codex:** tam / tam
- **Geliştirici:** Panniantong (kisi, ★114497, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → birincil · **Roller:** ai-entegrasyon, icerik-pazarlama
- **Boyut:** 24 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT. 2026-11 yeniden yazımı: hata kodlarına göre dallanan akış, döngüsel yeniden deneme yasağı, 'yazma/giriş/şifre isteme yok' çizgileri, önce yerleşik araç ilkesi; MIT. Eksiler: SKILL.md varsayılan Çince, CLI kurulumu şart, tarayıcı indirme ve çerez kopyalama ile izin yüzeyi büyüdü; RSS, Exa genel arama ve bazı yorum okuma eylemleri artık yok.

### context7-cli  ·  upstash/context7 @ b1e3611  ·  puan 88 (A)

- **Ne yapar:** `ctx7` CLI'siyle kütüphane dokümanı getirir ve Context7 MCP sunucusunu yapay zekâ kodlama aracına kurar (`ctx7 setup`). Giriş, API anahtarı ve istek sınırı kullanımını anlatır.
- **Ne zaman:** Context7'yi bir araca kurmak ya da ctx7 komutlarını doğrudan kullanmak. · **Ne zaman değil:** Yalnızca doküman getirmek için find-docs yeterli. `ctx7 setup` giriş ya da API anahtarı ister ve aracın yapılandırma dosyasını değiştirir.
- **Teknoloji:** context7, node, cli · **Paketler:** ctx7
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → tamamlayıcı · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 11 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (guncel-dokuman-getirme grubunda tamamlayıcı: kurulum ve CLI kullanımı). Resmî ürün reposu (MIT). Çalıştırma testi yapılmadı.

### context7-docs  ·  upstash/context7 @ b1e3611  ·  puan 80 (A)

- **Ne yapar:** Context7'nin pi aracı için paketlenmiş doküman getirme skili: kütüphane, SDK, CLI ya da bulut servisi için güncel doküman ve örnek getirir; CONTEXT7_API_KEY ile kimlik doğrular.
- **Ne zaman:** pi aracıyla ya da API anahtarlı doğrudan Context7 kullanımı. · **Ne zaman değil:** Claude Code ve Codex için find-docs ya da context7-mcp daha uygun. API anahtarı gerekir.
- **Teknoloji:** context7, api-anahtari
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → alternatif · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (başka bir araç için paketlenmiş sürüm; aynı iş). Resmî ürün reposu (MIT).

### context7-mcp  ·  upstash/context7 @ b1e3611  ·  puan 88 (A)

- **Ne yapar:** Kütüphane, framework ya da API sorulduğunda Context7 MCP sunucusu üzerinden güncel doküman ve kod örneği getirir: önce kütüphane kimliğini çözer, sonra ilgili dokümanı sorgular.
- **Ne zaman:** Context7 MCP sunucusu kurulu ortamlarda kütüphane dokümanı getirme. · **Ne zaman değil:** Context7 MCP sunucusu kurulu değilse çalışmaz; o durumda find-docs (CLI). Sorgu metni Context7'ye gider.
- **Teknoloji:** context7, mcp · **Paketler:** context7-mcp
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → tamamlayıcı · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (guncel-dokuman-getirme grubunda tamamlayıcı: MCP yolu). Resmî ürün reposu (MIT). Birebir kopyaları başka araç eklentilerinde durur. Çalıştırma testi yapılmadı.

### context7-mcp@upstash  ·  upstash/context7 @ b1e3611  ·  puan 88 (A)

- **Ne yapar:** context7-mcp skilinin eklenti paketindeki (plugins/agent-plugins) sürümü: aynı işi yapar, açıklaması daha ayrıntılıdır ve tetikleyicileri daha geniştir.
- **Ne zaman:** Çıplak adlı context7-mcp yerine daha ayrıntılı tetikleme açıklaması isteniyorsa. · **Ne zaman değil:** İkisini birlikte kurma (aynı iş). Context7 MCP sunucusu gerekir.
- **Teknoloji:** context7, mcp · **Paketler:** context7-mcp
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** guncel-dokuman-getirme → alternatif · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: ALTERNATİF (aynı repodaki ikinci sürüm; aynı iş). Resmî ürün reposu (MIT).

### context7-mcp@upstash-2  ·  upstash/context7 @ b1e3611  ·  puan 94 (A)

- **Ne yapar:** This skill should be used when the user asks about libraries, frameworks, API references, or needs code examples. Activates for setup questions, code generation involving libraries, or mentions of specific frameworks like React, Vue, Next.js, Prisma, Supabase, etc.
- **Teknoloji:** next.js, react, svelte, tailwind, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** otomatik

### find-docs  ·  upstash/context7 @ b1e3611  ·  puan 95 (A)

- **Ne yapar:** Herhangi bir kütüphane, framework, SDK, CLI aracı ya da bulut servisi için güncel doküman, API referansı ve kod örneği getirir. `ctx7` CLI'sini kullanır (npx ctx7@latest); önce kütüphaneyi çözer, sonra konuya özel sorguyla ilgili bölümleri alır.
- **Ne zaman:** Modelin eğitim verisi eskimiş olabilecek her kütüphane sorusu: kurulum, yapılandırma, sürüm geçişi, API sözdizimi. · **Ne zaman değil:** Sorgu metni Context7 API'sine gider; gizli bilgi, anahtar ya da özel kod yazılmamalı. MCP sunucusu kuruluysa context7-mcp de aynı işi yapar.
- **Teknoloji:** context7, node, cli · **Paketler:** ctx7
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★65407, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → birincil · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Karar: TUT (guncel-dokuman-getirme grubunda birincil). Resmî ürün reposu (MIT, 64k★), etkin bakım. MCP kurulumu gerektirmez, girişsiz çalışır. Çalıştırma testi yapılmadı.

### graphify  ·  Graphify-Labs/graphify @ 3671f31  ·  puan 94 (A)

- **Ne yapar:** Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools.
- **Teknoloji:** api-anahtari, git, html, node, obsidian, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Graphify-Labs (kurum, ★152966, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6434 KB (SKILL.md 49.7 KB, yük buyuk) · **Bağımlılık:** graphify Python paketi (pip install graphifyy) kurulu olmalı.
- **İnceleme:** otomatik

### nlm-skill  ·  yerel/kendi @ 92683f1  ·  puan 74 (B)

- **Ne yapar:** Gemini Notebook (eski adıyla Google NotebookLM) için nlm komut satırı aracı ve MCP sunucusu rehberi: not defteri ve kaynak yönetimi, kaynak ekleme (URL, YouTube, metin, Drive), sohbet ve araştırma, podcast, rapor, test, bilgi kartı, zihin haritası, slayt, infografik, video ve veri tablosu üretimi, kota takibi, kimlik doğrulama ve sorun giderme.
- **Ne zaman:** nlm ile Gemini Notebook'u komut satırından ya da MCP ile otomatikleştirmek, kaynaklara dayalı içerik üretmek. · **Ne zaman değil:** nlm programı kurulu değilse ya da Google oturumu açılmamışsa; genel Gemini API işleri için değil.
- **Teknoloji:** python, cli · **Paketler:** nlm (notebooklm-mcp-cli, uv aracı), Google hesabı oturumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** kullanıcı (kisi, resmî, ★0, son güncelleme 2026-11-25, lisans Kendi (özel))
- **Durum:** tercih · **Örtüşme:** notebooklm-cli → birincil · **Roller:** icerik-pazarlama
- **Boyut:** 183 KB (SKILL.md 61.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. nlm programının paketinde gelen skilin anlık kopyası (notebooklm-mcp-cli 0.15.8, MIT; kaynak: paketin notebooklm_tools/data klasörü, AGENTS_SECTION.md hariç). Skil sürümü CLI sürümüne bağlıdır: nlm güncellenince klasör paketten yeniden kopyalanmalı. 'nlm skill install' ile aynı dosyalar makine geneline yazılabilir; kullanılmaz. Metin kimlik doğrulama yöntemlerini anlatır, değer içermez.

### notebooklm  ·  teng-lin/notebooklm-py @ c526cba  ·  puan 85 (A)

- **Ne yapar:** Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi), not defteri/kaynak yönetimi, kaynaklara dayalı sohbet ve derin araştırma, sesli özet/podcast gibi artefakt üretimi ve indirme; yetki sınırları ve hata giderme kuralları.
- **Ne zaman:** Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. · **Ne zaman değil:** Genel Gemini API işleri için değil; resmi olmayan bir istemci (Google hesap çerezleri/master token kullanır) — kurumsal hesapta politikaya aykırı olabilir.
- **Teknoloji:** python, notebooklm, cli · **Paketler:** notebooklm-py[browser] (pip, Python 3.10+), Google hesabı oturumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** teng-lin (kisi, ★20366, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 16 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kimlik doğrulama ve yetki sınırları özenle yazılmış, --json ve açık ID kullanımı ile güvenli otomasyon; MIT. Resmi olmayan API riski taşıyor.

### youtube-arama  ·  yerel/kendi @ 3c8d08e  ·  puan 77 (B)

- **Ne yapar:** yt-dlp ile YouTube'da arama yapar; her sonuç için başlık, URL, kanal, izlenme sayısı, süre ve yayın tarihini döndürür. Sıralama (ilgi, izlenme, tarih) ve JSON çıktısı vardır; kanal ve oynatma listesi sonuçları elenir.
- **Ne zaman:** YouTube'dan gerçek video listesi ve metadata gerektiğinde: konu araştırması, rakip kanal incelemesi, içerik fikri için izlenme karşılaştırması. · **Ne zaman değil:** Tek bir videonun altyazısı/transkripti ya da video indirmek için değil.
- **Teknoloji:** python · **Paketler:** yt-dlp
- **Claude / Codex:** tam / tam
- **Geliştirici:** kullanıcı (kisi, resmî, ★0, son güncelleme 2026-11-25, lisans Kendi (özel))
- **Durum:** tercih · **Örtüşme:** youtube-arastirma → birincil · **Roller:** icerik-pazarlama
- **Boyut:** 7 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Küçük, standart kütüphaneli tek betik; yt-dlp dışında bağımlılık yok. Betik yolu skilde sabit yazılı, kurulumda proje içine çevrilir. Claude hesabı eklentisinde aynı adlı başka bir sürüm var (farklı betik).
