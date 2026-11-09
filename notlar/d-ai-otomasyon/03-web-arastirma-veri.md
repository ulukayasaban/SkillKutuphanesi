# 03-web-arastirma-veri — AI ve Otomasyon

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **7/24**

### agent-reach  ·  Panniantong/Agent-Reach @ 7a38047  ·  puan 94 (A)

- **Ne yapar:** Çok platformlu salt-okunur içerik erişimi için tek CLI (`agent-reach <kanal> <eylem>`, `read <url>`): GitHub, YouTube, Bilibili, Reddit, X/Twitter, Xiaohongshu, Instagram, Facebook, LinkedIn, V2EX, Xueqiu, podcast ve anonim web arama/okuma. JSON çıktı ve hata kodlarıyla çalışır; tarayıcı gerektiren kanallar ortak özel tarayıcıyı (CloakBrowser/Chrome + OpenCLI) kullanır. Önce agent'ın kendi araçlarını dener, Reach boşlukları doldurur. SKILL.md Çince (SKILL_en.md İngilizce).
- **Ne zaman:** Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. · **Ne zaman değil:** Yazma işlemleri (gönderi, yorum, beğeni) için değil; agent-reach CLI kurulu değilse (kanal tablosu kurulumda doldurulan şablon). Gizlilik: kullanıcının Chrome'una OpenCLI eklentisi bağlıysa o sitenin giriş çerezleri özel tarayıcıya kopyalanır; açık onay olmadan kurma. 2026-11'de eski Exa/RSS/jina/yt-dlp doğrudan komutları kaldırıldı.
- **Teknoloji:** python, cli, web-arama · **Paketler:** agent-reach CLI (pip/uv; browser setup ile Node, OpenCLI, CloakBrowser/Chrome indirilir), platforma göre: yt-dlp, gh, bili CLI, opsiyonel: Groq anahtarı (podcast transkripsiyonu), github-token, proxy
- **Claude / Codex:** tam / tam
- **Geliştirici:** Panniantong (kisi, ★108808, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → birincil · **Roller:** ai-entegrasyon, icerik-pazarlama
- **Boyut:** 23 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 2026-11 yeniden yazımı: hata kodlarına göre dallanan akış, döngüsel yeniden deneme yasağı, 'yazma/giriş/şifre isteme yok' çizgileri, önce yerleşik araç ilkesi; MIT. Eksiler: SKILL.md varsayılan Çince, CLI kurulumu şart, tarayıcı indirme ve çerez kopyalama ile izin yüzeyi büyüdü; RSS, Exa genel arama ve bazı yorum okuma eylemleri artık yok.

### browser  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Web browser automation with AI-optimized snapshots for claude-flow agents
- **Teknoloji:** css, html, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-auth-flow  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Probe a site's authentication flow for redirect leaks, missing CSRF, weak session cookies, and OAuth misconfiguration; produces an auth findings.md
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-extract  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Extract structured data via stored browser-templates or one-shot DOM queries, with mandatory AIDefence PII + prompt-injection gates before content reaches the model
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-form-fill  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Fill a web form by mapping field-name → value, with optional template lookup from browser-templates for known forms
- **Teknoloji:** css, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-intent  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Execute a natural-language browser intent via page-agent (browser_act) when the target is easier to describe than to select — degrades gracefully when page-agent or an OpenAI-compatible LLM provider isn't configured
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-login  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Drive an authentication flow once, sanitize cookies through AIDefence, and vault a reusable cookie handle in browser-cookies for future sessions
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-record  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Open a named, traced browser session into an RVF cognitive container with a ruvector trajectory recording every action
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-replay  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Replay a recorded session trajectory against the same URL or a mutated variant; uses browser-selectors embedding similarity to recover from DOM drift
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-scrape  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** DEPRECATED in v0.2.0 -- use browser-extract instead; this is a thin shim for backward compatibility, kept as a shim and slated for removal in the next minor release
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-screenshot-diff  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Visual + DOM diff between two recorded sessions at matching trajectory step ids; used for visual regression and replay verification
- **Teknoloji:** html, node, playwright _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### browser-test  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** UI test recipe -- composes browser-record (capture) + browser-replay (verify) so every test produces a replayable RVF artifact, not an ephemeral run
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### context7-cli  ·  upstash/context7 @ 078c0c7  ·  puan 94 (A)

- **Ne yapar:** `ctx7` CLI'siyle kütüphane dokümanı getirir ve Context7 MCP sunucusunu yapay zekâ kodlama aracına kurar (`ctx7 setup`). Giriş, API anahtarı ve istek sınırı kullanımını anlatır.
- **Ne zaman:** Context7'yi bir araca kurmak ya da ctx7 komutlarını doğrudan kullanmak. · **Ne zaman değil:** Yalnızca doküman getirmek için find-docs yeterli. `ctx7 setup` giriş ya da API anahtarı ister ve aracın yapılandırma dosyasını değiştirir.
- **Teknoloji:** context7, node, cli · **Paketler:** ctx7
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★64385, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → tamamlayıcı · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 11 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (guncel-dokuman-getirme grubunda tamamlayıcı: kurulum ve CLI kullanımı). Resmî ürün reposu (MIT). Çalıştırma testi yapılmadı.

### context7-docs  ·  upstash/context7 @ 078c0c7  ·  puan 94 (A)

- **Ne yapar:** Context7'nin pi aracı için paketlenmiş doküman getirme skili: kütüphane, SDK, CLI ya da bulut servisi için güncel doküman ve örnek getirir; CONTEXT7_API_KEY ile kimlik doğrular.
- **Ne zaman:** pi aracıyla ya da API anahtarlı doğrudan Context7 kullanımı. · **Ne zaman değil:** Claude Code ve Codex için find-docs ya da context7-mcp daha uygun. API anahtarı gerekir.
- **Teknoloji:** context7, api-anahtari
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★64385, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → alternatif · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (başka bir araç için paketlenmiş sürüm; aynı iş). Resmî ürün reposu (MIT).

### context7-mcp  ·  upstash/context7 @ 078c0c7  ·  puan 94 (A)

- **Ne yapar:** Kütüphane, framework ya da API sorulduğunda Context7 MCP sunucusu üzerinden güncel doküman ve kod örneği getirir: önce kütüphane kimliğini çözer, sonra ilgili dokümanı sorgular.
- **Ne zaman:** Context7 MCP sunucusu kurulu ortamlarda kütüphane dokümanı getirme. · **Ne zaman değil:** Context7 MCP sunucusu kurulu değilse çalışmaz; o durumda find-docs (CLI). Sorgu metni Context7'ye gider.
- **Teknoloji:** context7, mcp · **Paketler:** context7-mcp
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★64385, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → tamamlayıcı · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (guncel-dokuman-getirme grubunda tamamlayıcı: MCP yolu). Resmî ürün reposu (MIT). Birebir kopyaları başka araç eklentilerinde durur. Çalıştırma testi yapılmadı.

### context7-mcp@upstash  ·  upstash/context7 @ 078c0c7  ·  puan 94 (A)

- **Ne yapar:** context7-mcp skilinin eklenti paketindeki (plugins/agent-plugins) sürümü: aynı işi yapar, açıklaması daha ayrıntılıdır ve tetikleyicileri daha geniştir.
- **Ne zaman:** Çıplak adlı context7-mcp yerine daha ayrıntılı tetikleme açıklaması isteniyorsa. · **Ne zaman değil:** İkisini birlikte kurma (aynı iş). Context7 MCP sunucusu gerekir.
- **Teknoloji:** context7, mcp · **Paketler:** context7-mcp
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★64385, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** guncel-dokuman-getirme → alternatif · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (aynı repodaki ikinci sürüm; aynı iş). Resmî ürün reposu (MIT).

### deep-research  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Orchestrate multi-phase deep research with web search, memory retrieval, pattern matching, and synthesis into structured findings
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### dossier-collect  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Build a graph-structured dossier on a seed entity via parallel fan-out + recursive expansion across web, memory, knowledge-graph, codebase, ADR index, and git intel
- **Teknoloji:** api-anahtari, git, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### find-docs  ·  upstash/context7 @ 078c0c7  ·  puan 94 (A)

- **Ne yapar:** Herhangi bir kütüphane, framework, SDK, CLI aracı ya da bulut servisi için güncel doküman, API referansı ve kod örneği getirir. `ctx7` CLI'sini kullanır (npx ctx7@latest); önce kütüphaneyi çözer, sonra konuya özel sorguyla ilgili bölümleri alır.
- **Ne zaman:** Modelin eğitim verisi eskimiş olabilecek her kütüphane sorusu: kurulum, yapılandırma, sürüm geçişi, API sözdizimi. · **Ne zaman değil:** Sorgu metni Context7 API'sine gider; gizli bilgi, anahtar ya da özel kod yazılmamalı. MCP sunucusu kuruluysa context7-mcp de aynı işi yapar.
- **Teknoloji:** context7, node, cli · **Paketler:** ctx7
- **Claude / Codex:** tam / tam
- **Geliştirici:** upstash (kurum, ★64385, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guncel-dokuman-getirme → birincil · **Roller:** frontend-muhendis, backend-muhendis
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk) · **Bağımlılık:** Context7 servisine bağlanır: MCP sunucusu ya da `ctx7` CLI (npx ctx7@latest). Girişsiz çalışır; daha yüksek istek sınırı için ücretsiz hesap ya da CONTEXT7_API_KEY. Sorgu metni Context7 API'sine gönderilir (gizli bilgi yazılmamalı).
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (guncel-dokuman-getirme grubunda birincil). Resmî ürün reposu (MIT, 64k★), etkin bakım. MCP kurulumu gerektirmez, girişsiz çalışır. Çalıştırma testi yapılmadı.

### goal-plan  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Create and execute Goal-Oriented Action Plans (GOAP) with precondition analysis, cost optimization, and adaptive replanning
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.2 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### graphify  ·  Graphify-Labs/graphify @ 32e5efe  ·  puan 98 (A)

- **Ne yapar:** Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools.
- **Teknoloji:** api-anahtari, git, html, node, obsidian, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Graphify-Labs (kurum, ★142439, son güncelleme 2026-11-03, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5655 KB (SKILL.md 47.3 KB, yük buyuk) · **Bağımlılık:** graphify Python paketi (pip install graphifyy) kurulu olmalı.
- **İnceleme:** otomatik

### horizon-track  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Track long-horizon objectives across multiple sessions with milestone checkpoints, progress persistence, and drift detection
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### notebooklm  ·  teng-lin/notebooklm-py @ 7db1000  ·  puan 85 (A)

- **Ne yapar:** Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi), not defteri/kaynak yönetimi, kaynaklara dayalı sohbet ve derin araştırma, sesli özet/podcast gibi artefakt üretimi ve indirme; yetki sınırları ve hata giderme kuralları.
- **Ne zaman:** Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. · **Ne zaman değil:** Genel Gemini API işleri için değil; resmi olmayan bir istemci (Google hesap çerezleri/master token kullanır) — kurumsal hesapta politikaya aykırı olabilir.
- **Teknoloji:** python, notebooklm, cli · **Paketler:** notebooklm-py[browser] (pip, Python 3.10+), Google hesabı oturumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** teng-lin (kisi, ★20096, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 16 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kimlik doğrulama ve yetki sınırları özenle yazılmış, --json ve açık ID kullanımı ile güvenli otomasyon; MIT. Resmi olmayan API riski taşıyor.

### research-synthesize  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Synthesize research findings from memory into structured reports with evidence grading, contradiction resolution, and actionable recommendations
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik
