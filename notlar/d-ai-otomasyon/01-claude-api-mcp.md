# 01-claude-api-mcp — AI ve Otomasyon

_Claude API, MCP sunucusu, model geçişi_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **10/14**

### academy-guide  ·  anthropics/skills @ dbd4588  ·  puan 79 (B)

- **Ne yapar:** Claude veya bir Claude ürününün nasıl kullanılacağına dair sorulara verilen cevabın sonuna, Claude Academy'den (academy.claude.com) yalnızca güçlü eşleşme varsa uygun kurs/eğitim/kullanım örneği önerisi ekler. Katalog skill içine gömülü değil; güncel JSON katalog çalışma anında çekilir ve tazeliği kontrol edilir.
- **Ne zaman:** Claude öğrenmeye yönelik destek/eğitim asistanları; ekibe Claude yaygınlaştırma soruları. · **Ne zaman değil:** Kod/proje agent'larında (iş ortasındaki kullanıcıya kurs önermek gürültü); web erişimi yoksa (katalog çekilemez, uydurma yasak). Skill yazımı ile ilgisi yok — kategorisi Claude ürün desteği.
- **Teknoloji:** web-fetch
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★185499, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 7.6 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV (projelere gerek yok). Anthropic resmi, uydurmayı engelleyen tazelik kuralları iyi; ama proje agent'ları için kullanım alanı yok.

### build-mcp-app  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model,
- **Teknoloji:** css, html, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45472, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 47 KB (SKILL.md 18.9 KB, yük orta)
- **İnceleme:** otomatik

### build-mcp-server  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP,
- **Teknoloji:** api-anahtari, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45472, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 49 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### build-mcpb  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 100 (A)

- **Ne yapar:** This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set 
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45472, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### claude-api  ·  anthropics/skills @ dbd4588  ·  puan 81 (A)

- **Ne yapar:** Claude API / Anthropic SDK için kapsamlı ve güncel başvuru: model kimlikleri ve fiyatlar, adaptive thinking, streaming, araç kullanımı, prompt caching, compaction, MCP, Managed Agents, Files/Skills API. Dil algılayıp (Python, TS, Go, Java, C#, PHP, Ruby, cURL) ilgili klasörü okutur; migrate, prompt-audit, upgrade, cost-optimize, build-eval, hillclimb alt komutları içerir.
- **Ne zaman:** Claude çağıran her kod: yeni LLM özelliği, agent/araç tanımı, model geçişi, maliyet optimizasyonu, eval kurma, SDK sürüm yükseltme. · **Ne zaman değil:** Projede başka sağlayıcı (OpenAI, Gemini, Ollama…) kullanılıyorsa — skill bunu kendisi kontrol eder. SKILL.md 103 KB: rol bütçesinin büyük kısmını yer; sadece Claude entegrasyonu yapan agent'a ver. Codex'te: WebFetch gibi Claude araç adları geçiyor; Codex'in web/arama aracıyla aynı adımlar uygulanır, içerik ve kod kalıpları aynen geçerli.
- **Teknoloji:** anthropic-sdk, python, typescript, go, java, csharp, php, ruby, curl · **Paketler:** anthropic (pip) veya @anthropic-ai/sdk (npm) — dile göre resmi SDK, ANTHROPIC_API_KEY
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★185499, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-api-gecis → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 2031 KB (SKILL.md 102.7 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic resmi, sürekli güncel (model listesi 2026-10-06), API kayması uyarı tablosu ve dil başına doğrulanmış kalıplar. Tek eksi: SKILL.md 103 KB, klasör 2.2 MB. claude-opus-4-5-migration'ın işini 'migrate' alt komutu güncel modellerle yapıyor.

### claude-opus-4-5-migration  ·  anthropics/claude-code @ 5ed799e  ·  puan 76 (B)

- **Ne yapar:** Sonnet 4.0/4.5 ve Opus 4.1'den Opus 4.5'e tek seferlik geçiş: platforma göre (Anthropic, Bedrock, Vertex, Azure) model dizgelerini değiştirir, desteklenmeyen beta başlığını kaldırır, effort parametresi ekler ve Opus 4.5 davranış farklarına göre (araç aşırı tetikleme, aşırı mühendislik) istem ayarı önerir.
- **Ne zaman:** Yalnızca hedef özellikle Opus 4.5 ise (eski kod tabanlarını tam bu sürüme sabitlemek). · **Ne zaman değil:** Güncel modellere (Opus 5.5, Sonnet 5.5, Fable 5.1) geçişte — claude-api 'migrate' alt komutu kullanılmalı. Haiku 4.5 geçişi kapsam dışı.
- **Teknoloji:** anthropic-sdk
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★153995, son güncelleme 2026-10-31, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-api-gecis → alternatif
- **Boyut:** 12 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. İyi yazılmış ama eskidi: hedef model Opus 4.5 ve 1M bağlam notu artık geçerli değil. Aynı iş claude-api/shared/model-migration.md'de güncel.

### connect  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 70 (B)

- **Ne yapar:** Composio SDK (Python/TS) ile agent'ı Gmail, Slack, GitHub, Notion gibi 1000+ uygulamaya bağlar; e-posta gönderme, issue açma, mesaj atma gibi gerçek eylemler yaptırır. API anahtarı, OAuth akışı, framework desteği ve sorun giderme anlatılır.
- **Ne zaman:** Kendi uygulamasında/agent'ında harici servislere eylem yaptırmak isteyen projeler (Composio kullanmayı kabul ederek). · **Ne zaman değil:** Üçüncü taraf aracı servise (Composio) veri/OAuth yetkisi vermek istenmiyorsa; tek bir servis için resmi MCP sunucusu varsa. Gerçek e-posta/mesaj gönderir — onaysız çalıştırma.
- **Teknoloji:** composio, python, typescript, oauth · **Paketler:** composio (pip) veya @composio/core (npm), COMPOSIO_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** composio-baglanti → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (birincil, Composio grubunda). Kurulum ve kod örnekleri kısa ve çalışır; pazarlama dili yoğun. Araçtan bağımsız (SDK) olduğu için connect-apps'e tercih edildi.

### connect-apps  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 59 (C)

- **Ne yapar:** Claude Code'a `/plugin install composio-toolrouter` ile Composio Tool Router eklentisini kurup 1000+ uygulamada (Gmail, Slack, GitHub, Notion) eylem yaptırmayı anlatan hızlı başlangıç.
- **Ne zaman:** Claude Code kullanıcısının kendi oturumundan harici uygulamalara eylem yaptırması. · **Ne zaman değil:** Codex'te plugin komutları yok: Composio'nun MCP sunucusunu `~/.codex/config.toml` içine `[mcp_servers.composio]` olarak ekle ya da SDK tabanlı connect skill'ini kullan. Uygulama koduna entegrasyon için connect.
- **Teknoloji:** composio, claude-code, mcp · **Paketler:** composio-toolrouter Claude Code eklentisi, Composio API anahtarı
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** composio-baglanti → alternatif
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF. Çok kısa bir kurulum tarifi; skill'den çok eklenti reklamı. Claude Code eklenti sistemine bağlı.

### langsmith-fetch  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** LangChain/LangGraph agent'larını hata ayıklamak için langsmith-fetch CLI ile LangSmith'ten çalışma izlerini (trace) çeker; son etkinlik, belirli iz derin incelemesi, hata tespiti, bellek işlemleri, araç çağrıları, süre ve token kullanımını raporlar.
- **Ne zaman:** LangSmith izlemesi açık LangChain/LangGraph agent projelerinde hata ayıklama ve performans analizi. · **Ne zaman değil:** LangChain kullanmayan projelerde (Claude Agent SDK, ham API); LangSmith hesabı/API anahtarı yoksa.
- **Teknoloji:** langchain, langgraph, langsmith, python · **Paketler:** langsmith-fetch (pip), LANGSMITH_API_KEY, LANGSMITH_PROJECT
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (dar). İş akışları ve komutlar somut; yalnızca LangSmith ekosistemine yarar. Lisans belirtilmemiş.

### mcp-builder  ·  anthropics/skills @ dbd4588  ·  puan 87 (A)

- **Ne yapar:** Yüksek kaliteli MCP sunucusu geliştirme rehberi: araştırma/planlama (araç adlandırma, bağlam yönetimi, hata mesajları), Python FastMCP veya TypeScript MCP SDK ile uygulama, MCP Inspector ile test ve 10 soruluk değerlendirme (eval) seti oluşturma; değerlendirmeyi çalıştıran evaluation.py betiği içerir.
- **Ne zaman:** Harici bir API/servisi agent'lara açan yeni MCP sunucusu yazmak ve değerlendirmek. · **Ne zaman değil:** Mevcut bir MCP sunucusunu Claude Code eklentisine bağlamak (mcp-integration); protokol sürüm geçişi/güvenlik denetimi ağırlıklı işler (mcp-builder@vudovn daha güncel).
- **Teknoloji:** mcp, python, typescript · **Paketler:** mcp / fastmcp (pip) veya @modelcontextprotocol/sdk (npm), @modelcontextprotocol/inspector, anthropic (eval betiği için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★185499, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** mcp-sunucu-gelistirme → birincil · **Roller:** ai-entegrasyon
- **Boyut:** 119 KB (SKILL.md 8.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Anthropic resmi, ComposioHQ kopyasından daha güncel ve kısa; dil rehberleri ve eval betiği tek pakette. vudovn sürümü spec/güvenlik tarafını tamamlıyor; birincil bu çünkü uçtan uca iş akışı ve değerlendirme aracı içeriyor.

### mcp-builder@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 68 (B)

- **Ne yapar:** Anthropic mcp-builder'ın ComposioHQ'daki eski sürümü: 'iş akışı odaklı araç tasarımı' ilkeleri, ayrıntılı uygulama planı, dil rehberleri ve değerlendirme adımları.
- **Ne zaman:** Eski sürümdeki daha ayrıntılı 'ajan merkezli tasarım ilkeleri' bölümü özellikle istenirse. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/mcp-builder güncel ve daha az bağlam tüketir.
- **Teknoloji:** mcp, python, typescript · **Paketler:** mcp / fastmcp (pip) veya @modelcontextprotocol/sdk (npm)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78372, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** mcp-sunucu-gelistirme → alternatif
- **Boyut:** 144 KB (SKILL.md 13.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Güncel sürümün eski kopyası (350 satır fark); tasarım ilkeleri bölümü daha uzun ama 'iş akışı araçları' önerisi güncelde dengelenmiş.

### mcp-builder@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 83 (A)

- **Ne yapar:** MCP sunucu ve istemci mühendisliği: kararlı 2026-07-28 spesifikasyonuna göre durumsuz istek modeli, taşıma ve kimlik doğrulama, araç girdi/çıktı şemaları, $ref güvenliği, araç/kaynak/istem tasarımı, güvenlik gereksinimleri, eklentiler (Tasks, Skills over MCP, MCP Apps), eski sürümlerden geçiş ve test matrisi.
- **Ne zaman:** MCP sunucu/istemcisini güncel spesifikasyona taşımak, güvenlik/birlikte çalışabilirlik incelemesi, şema tasarımı. · **Ne zaman değil:** Sıfırdan sunucu yazıp değerlendirme seti kurmak için anthropics/mcp-builder ile birlikte kullan (tek başına iş akışı/kod iskeleti vermez). allowed-tools frontmatter'ı Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** mcp, json-schema
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** mcp-sunucu-gelistirme → tamamlayıcı · **Roller:** ai-entegrasyon
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Üç sürüm içinde en güncel spesifikasyon bilgisi ve güvenlik kontrol listesi; MIT, 10 KB. İş akışı ve eval aracı olmadığı için birincil değil.

### mcp-integration  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 95 (A)

- **Ne yapar:** This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for 
- **Teknoloji:** api-anahtari, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★45472, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 45 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### mcp-integration@anthropics  ·  anthropics/claude-code @ 5ed799e  ·  puan 83 (A)

- **Ne yapar:** Claude Code eklentilerine MCP sunucusu paketleme rehberi: .mcp.json ya da plugin.json içinde mcpServers, stdio/SSE/HTTP/WebSocket sunucu tipleri, ${CLAUDE_PLUGIN_ROOT} ve ortam değişkeni genişletme, MCP araç adlandırması (mcp__eklenti__sunucu__araç), yaşam döngüsü ve OAuth/token kimlik doğrulama kalıpları.
- **Ne zaman:** Bir Claude Code eklentisine hazır MCP sunucusu eklemek/yapılandırmak. · **Ne zaman değil:** MCP sunucusunun kendisini yazmak için (mcp-builder). Codex'te eklenti paketleme yok: MCP sunucusu `~/.codex/config.toml` dosyasında `[mcp_servers.<ad>]` tablosuyla (command, args, env ya da url) tanımlanır; .mcp.json ve ${CLAUDE_PLUGIN_ROOT} kullanılmaz. Sunucu tipleri, kimlik doğrulama ve güvenlik bölümleri Codex'te de geçerli, plugin.json kısımlarını atla.
- **Teknoloji:** mcp, claude-code, json
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★153995, son güncelleme 2026-10-31, lisans yok)
- **Durum:** alternatif · **Örtüşme:** claude-plugin-mcp → birincil · **Roller:** skill-gelistirici
- **Boyut:** 46 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi plugin-dev setinin parçası; örnek ve referans dosyaları zengin. Claude Code eklentisine özgü; Codex için yukarıdaki uyarlama gerekir.
