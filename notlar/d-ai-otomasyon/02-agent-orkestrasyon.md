# 02-agent-orkestrasyon — AI ve Otomasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **13/37**

### batch-operations  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Birçok dosyaya aynı değişikliği güvenle uygulama protokolü: deseni tanımla, önce grep ile etkilenen dosyaları önizle, toplu uygula, sonra doğrula (sayım, derleme, test). Yeniden adlandırma, import ekleme, sürüm güncelleme gibi yaygın kalıplar ve güvenlik kuralları içerir.
- **Ne zaman:** Kod tabanında desen tabanlı toplu değişiklik: fonksiyon yeniden adlandırma, API geçişi, sürüm numarası güncelleme. · **Ne zaman değil:** Tek dosya düzenlemesi ya da her dosyada ayrı yargı gerektiren değişiklik (alt-agent'lara böl). allowed-tools/effort frontmatter alanları Claude Code'a özgü; Codex yok sayar, protokol aynen geçerli.
- **Teknoloji:** bash, git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Roller:** agent-orkestra
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru 'önizle → uygula → doğrula' disiplini; içerik genel bilgi düzeyinde. Aslında yazılım geliştirme konusu ama alt-agent'a bölme kararıyla bağlantılı.

### behavioral-modes  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** Görev türüne göre yedi çalışma modu tanımlar (brainstorm, implement, debug, review, teach, ship, orchestrate); her mod için davranış kuralları ve çıktı biçimi verir.
- **Ne zaman:** ag-kit ailesini kuran projelerde agent'ın tonunu/yaklaşımını göreve göre değiştirmek. · **Ne zaman değil:** Diğer ailelerle (superpowers, agent-skills) birlikte — süreç skilleri zaten bu davranışları tanımlıyor ve çakışır; IMPLEMENT modu kütüphanede olmayan 'clean-code' skill'ine atıf yapıyor. allowed-tools Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Genel istem metni; ag-kit'in diğer skillerine bağımlı, ek değeri düşük.

### claude-automation-recommender  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 95 (A)

- **Ne yapar:** Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.
- **Teknoloji:** docker, git, next.js, node, playwright, react, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (agents, settings); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 42 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** otomatik

### claude-md-improver  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 15 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### codex-radar  ·  lemomo-ai/codex-radar @ c388223  ·  puan 61 (C)

- **Ne yapar:** Analyze local Codex session history and create an evidence-grounded HTML collaboration report. Use when the user asks to run Codex Radar, score how they work with Codex, analyze Codex collaboration, or generate a Codex Radar report. Do not use for Claude Code history, generic code review, or workspace usage analytics.
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★39, son güncelleme 2026-09-20, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 179 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** otomatik

### context-compression  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Uzun oturumlarda bağlamı sıkıştırma: büyük araç çıktılarını anlamsal özete indirme (mikro), biten iş aşamalarını özetleme ve oturum kontrol noktası yazma; kararları ve değişen dosyaları koruma protokolü.
- **Ne zaman:** 20+ turluk oturumlar, agent tekrar etmeye başladığında, iş aşaması değişiminde. · **Ne zaman değil:** Kısa oturumlarda; harness otomatik sıkıştırma yapıyorsa (Claude Code/Codex compaction) çoğu zaman gereksiz — yalnızca elle kontrol noktası yazımı için. allowed-tools/effort Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** api-anahtari, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → tamamlayıcı · **Roller:** agent-orkestra
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Üç seviyeli sıkıştırma ve kontrol noktası şablonu kullanışlı; token kazancı rakamları tahmini.

### context-engineering  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Agent'a doğru bağlamı doğru zamanda verme: kalıcıdan geçiciye bağlam hiyerarşisi (kural dosyaları CLAUDE.md/AGENTS.md, spec, ilgili kaynak dosyalar, hata çıktısı, konuşma), yeniden başlatılabilir oturum sınırları ve bağlam paketleme stratejileri.
- **Ne zaman:** Yeni oturum/proje kurulumu, kural dosyası yazımı, agent çıktı kalitesi düştüğünde, kod tabanının farklı bölümüne geçerken. · **Ne zaman değil:** Tek seferlik küçük sorularda gereksiz.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → birincil · **Roller:** agent-orkestra · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 15 KB (SKILL.md 15.2 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Karar: TUT (birincil). addyosmani; araçtan bağımsız (CLAUDE.md ve AGENTS.md'yi birlikte anıyor), somut kural dosyası şablonu ve oturum sınırı önerileri. Bağlam grubunda birincil.

### coordinator-mode  ·  vudovn/ag-kit @ 549ba3d  ·  puan 84 (A)

- **Ne yapar:** Koordinatör olarak çok agent'lı orkestrasyon: görevi ayrıştır, sınıflandır (araştırma/uygulama/doğrulama), okuma işlerini paralel yazma işlerini sıralı dağıt, izle, sentezle ve doğrula. 'Anlamayı devretme' kuralı, işçi istem şablonları ve fork kuralları içerir.
- **Ne zaman:** Birden çok alanı kapsayan büyük görevde agent'ın kendisi kod yazmadan işçi alt-agent'ları yönetmesi. · **Ne zaman değil:** Tek alanlı işlerde; yazılı bir uygulama planı varsa subagent-driven-development daha disiplinli. allowed-tools içinde Claude Code'un 'Agent' aracı geçiyor; Codex'te alt-agent desteği olan sürümde aynı akış, yoksa işçi görevleri ayrı Codex oturumları/`codex exec` çağrılarıyla çalıştırılır.
- **Teknoloji:** api-anahtari, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İşçi istemi yazma rehberi ve eşzamanlılık kuralları güçlü; ama plan tabanlı inceleme döngüsü yok. Orkestrasyon grubunda birincil subagent-driven-development.

### creative-director  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calibrated against Cannes/D&AD/HumanKind, 5-phase process from brief to presentation.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### diagnosing-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 98 (A)

- **Ne yapar:** Bir superpowers oturumu kötü gittiğinde (tekrar eden iş, yok sayılan plan, tetiklenmeyen skill, pahalılık) diskteki transkriptleri okuyup kanıta dayalı rapor çıkarır; her bulgu path:line ile alıntılanır. Oturum bulma, gizli veri karartma ve GitHub issue paketi rehberleri içerir.
- **Ne zaman:** superpowers skill ailesiyle çalışan oturumların neden yanlış gittiğini incelemek, bakımcılara hata raporu hazırlamak. · **Ne zaman değil:** superpowers kullanılmıyorsa; genel kod hata ayıklaması için (systematic-debugging).
- **Teknoloji:** bash, jsonl
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (dar). Kanıt disiplini ve redaksiyon politikası örnek alınacak düzeyde; çok harness'li (Claude Code, Codex vb.) oturum keşfi var. Yalnızca superpowers kullanıcıları için.

### discernment-nudge  ·  anthropics/skills @ ca45fc4  ·  puan 89 (A)

- **Ne yapar:** Kullanıcının üzerine karar vereceği önemli bir cevap ya da taslaktan sonra, cevaptaki belirli noktalara bağlı 2-3 kısa takip sorusu ekler: önemli olguları doğrulama, varsayımları sorgulama, eksik bağlamı fark etme. Konuşma başına en fazla bir kez; basit sorularda, kodda ve yaratıcı yazıda devreye girmez.
- **Ne zaman:** Tavsiye, plan, tahmin, veri yorumu gibi kullanıcının harekete geçeceği çıktılar üreten sohbet/asistan agent'ları. · **Ne zaman değil:** Kod yazan agent'larda (skill zaten kapsam dışı sayar); otomatik iş hatlarında (kullanıcı yokken soru eklemek gürültü).
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★186390, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Roller:** dokuman-yazari
- **Boyut:** 21 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi; ne zaman kullanılmayacağı ve çıktı biçimi çok net. Orkestrasyon değil 'cevap kalitesi' skill'i; rapor/tavsiye üreten rollere opsiyonel.

### dispatching-parallel-agents  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Bağımsız 2+ problemi (farklı test dosyaları, alt sistemler) her birine izole bağlamlı ayrı bir agent vererek paralel çözme kalıbı: bağımsız alanları belirle, odaklı görev istemi yaz, paralel dağıt, sonuçları incele ve birleştir.
- **Ne zaman:** Birbirinden bağımsız birden çok hata/araştırma işini paralel yürütmek. · **Ne zaman değil:** Görevler ortak durum paylaşıyor ya da aynı dosyalara yazıyorsa; tek kök nedenli hatalarda. Codex'te alt-agent yoksa paralel `codex exec` süreçleri ya da ayrı worktree'lerle uygulanır.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → tamamlayıcı · **Roller:** agent-orkestra, planlayici
- **Boyut:** 6 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (tamamlayıcı). superpowers; kısa (6 KB), karar ağacı ve istem yapısı net. subagent-driven-development ile birlikte kullanılır.

### full-output-enforcement  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output.
- **Teknoloji:** api-anahtari, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### intelligent-routing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 67 (B)

- **Ne yapar:** Her kullanıcı isteğini sessizce analiz edip anahtar kelime/alan/karmaşıklığa göre uygun uzman agent'ı (security-auditor, frontend-specialist, orchestrator…) otomatik seçen yönlendirme kuralları.
- **Ne zaman:** ag-kit'in uzman agent tanımlarının kurulu olduğu projelerde. · **Ne zaman değil:** ag-kit agent'ları (security-auditor, backend-specialist vb.) kurulu değilse — bu kütüphanede yoklar, rol sistemi zaten skill-ekle.py ile kuruluyor. 'Her zaman aktif' talimatı bağlamı ve davranışı etkiler. allowed-tools Claude Code'a özgü.
- **Teknoloji:** api-anahtari, css, docker, html, node, playwright, react, tailwind, vue _(otomatik tespit)_ · **Paketler:** ag-kit agent tanımları
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Var olmayan agent adlarına bağımlı; bu kütüphanenin rol sistemiyle çakışır.

### memory-system  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Oturumlar arası kalıcı bellek: .agents/memory/MEMORY.md indeksi (en fazla 200 satır) ve konu dosyaları (kullanıcı tercihleri, proje kuralları, teknik kararlar, geri bildirim); kaydetme, hatırlama, arama işlemleri ve neyin kaydedilmeyeceği kuralları.
- **Ne zaman:** Harness'in yerleşik belleği olmayan ortamlarda (ya da projeye taşınabilir, git'te tutulan bellek istendiğinde) tercih ve kararları saklamak. · **Ne zaman değil:** Claude Code'un yerleşik auto-memory'si veya claude-mem gibi bir bellek eklentisi zaten kullanılıyorsa (çift kayıt olur); gizli bilgi saklamak için. Codex'te uygundur — AGENTS.md'ye 'oturum başında .agents/memory/MEMORY.md oku' satırı eklenmeli.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel). İndeks + konu dosyası yapısı sağlam ve Claude Code belleğine benzer; harness belleğiyle çakışma riski var.

### n8n-agents  ·  czlonkowski/n8n-skills @ e037563  ·  puan 88 (A)

- **Ne yapar:** Design n8n AI agents the right way. Use when building or editing any @n8n/n8n-nodes-langchain.* AI node — an AI Agent, LLM chain, Text Classifier, or Information Extractor — and whenever the user mentions AI agents, LLM with tools, tool calling, $fromAI, system prompts, agent memory, sessionId, structured/JSON output, output parser, RAG, vector store, a chat assistant/bot, or human-in-the-loop rev
- **Teknoloji:** api-anahtari, canvas, node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 124 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** otomatik

### n8n-binary-and-data  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Handle files and binary data in n8n correctly. Use when working with files, images, PDFs, attachments, uploads or downloads, base64, vision/multimodal input, or when an AI agent needs a file as tool input or output — and whenever the user mentions $binary, binaryPropertyName, "read the PDF", "attach the file", "send the image", Merge losing binary, or a CDN for chat images. Covers the $binary vs $
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 61 KB (SKILL.md 15.5 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-javascript  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Write, review, or debug JavaScript in an n8n Code node. Use when a Code node is already in the workflow (editing it, fixing an error, choosing its mode, making it faster), or when a new one is justified: no native node fits (check the job-to-node table in using-n8n-mcp-skills first) and the job is on the closed list — loops or recursion no node expresses, state across runs, parsing no node handles
- **Teknoloji:** api-anahtari, canvas, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 134 KB (SKILL.md 22.4 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-python  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Write Python in n8n Code nodes (native Python, `language` pythonNative, n8n 2.x). Use when the user explicitly wants Python in a Code node, when migrating old Pyodide/"Python (Beta)" code that used _input/_json/_node/_now, or when a Python Code node fails with NameError, "Security violations detected", "Import of standard library module … is disallowed", "__build_class__ not found", "A 'json' prop
- **Teknoloji:** html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-code-tool  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Write JavaScript or Python for the n8n Custom Code Tool (@n8n/n8n-nodes-langchain.toolCode) — the AI-agent-callable tool, NOT the workflow Code node. Use when building a Code Tool attached to an AI Agent, writing code that an LLM will invoke, parsing the `query` input, returning a string result, defining an input schema for structured arguments (specifyInputSchema, jsonSchemaExample, DynamicStruct
- **Teknoloji:** node, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 36 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### n8n-error-handling  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Wire n8n error handling so failures are loud, structured, and recoverable. Use when building any webhook/API workflow, a scheduled or unattended workflow, or any path where a silent failure would drop user-visible work — and whenever the user mentions error handling, onError, continueErrorOutput, error branches/outputs, retries, retryOnFail, Respond to Webhook status codes, 4xx/5xx, Error Trigger,
- **Teknoloji:** api-anahtari, canvas, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 20.6 KB, yük orta)
- **İnceleme:** otomatik

### n8n-expression-syntax  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, mapping data between nodes, or referencing webhook data in workflows. Use this skill whenever configuring node fields that reference data from previous nodes — expressions are how n8n passes data between nodes, and getting th
- **Teknoloji:** api-anahtari, canvas, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 22.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-mcp-tools-expert  ·  czlonkowski/n8n-skills @ e037563  ·  puan 88 (A)

- **Ne yapar:** Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, organizing workflows into folders, managing credentials, auditing instance security, or using any n8n-mcp tool. Provides tool selection guidance, parameter formats, and common patterns. IMPORTANT — Always consult this skill before calling any n8n-m
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 107 KB (SKILL.md 30.0 KB, yük buyuk)
- **İnceleme:** otomatik

### n8n-multi-instance  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Use when an n8n-mcp account targets more than one n8n instance — i.e. the `n8n_instances` tool is available, the user mentions multiple n8n instances or environments (prod vs staging, several teams or clients), several agents or chats work on one account in parallel, a workflow / datatable / credential / execution call returns an unexpected NOT_FOUND or reads data you don't recognize, or a call is
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 14.5 KB, yük orta)
- **İnceleme:** otomatik

### n8n-node-configuration  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration patterns by node type — including the native nodes that replace Code (Summarize, Aggregate, Split Out, Merge, Compare Datasets, Remove Duplicates, Sort, Limit, Date & Time, HTTP Request p
- **Teknoloji:** api-anahtari, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 108 KB (SKILL.md 19.7 KB, yük orta)
- **İnceleme:** otomatik

### n8n-self-hosting  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Deploy a production self-hosted n8n end-to-end to a fresh Linux VM over SSH, using Docker Compose behind a Caddy reverse proxy with automatic HTTPS. Use whenever the user wants to self-host, install, provision, or deploy n8n on their own server/VPS (Hetzner, DigitalOcean, AWS EC2, bare metal) — single/regular mode or queue mode with workers — or to update, back up, restore, or harden such an insta
- **Teknoloji:** api-anahtari, docker, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 13.7 KB, yük orta)
- **İnceleme:** otomatik

### n8n-subworkflows  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Build reusable, composable n8n sub-workflows. Use when extracting shared logic, building anything multi-step or reused across workflows, or any workflow over ~10 nodes — and whenever the user mentions sub-workflows, Execute Workflow, reuse, shared/common logic, modular workflows, "Define Below" inputs, waitForSubWorkflow, mode each vs all, or exposing a workflow as an agent tool. Covers typed sub-
- **Teknoloji:** api-anahtari, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 19.8 KB, yük orta)
- **İnceleme:** otomatik

### n8n-validation-expert  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Interpret validation errors and guide fixing them. Use when encountering validation errors, validation warnings, false positives, operator structure issues, or need help understanding validation results. Also use when asking about validation profiles, error types, the validation loop process, or auto-fix capabilities. Consult this skill whenever a validate_node or validate_workflow call returns er
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 91 KB (SKILL.md 22.4 KB, yük orta)
- **İnceleme:** otomatik

### n8n-workflow-patterns  ·  czlonkowski/n8n-skills @ e037563  ·  puan 91 (A)

- **Ne yapar:** Proven workflow architectural patterns from real n8n workflows. Use when building new workflows, designing workflow structure, choosing workflow patterns, planning workflow architecture, or asking about webhook processing, HTTP API integration, database operations, AI agent workflows, batch processing, or scheduled tasks. Always consult this skill when the user asks to create, build, or design an 
- **Teknoloji:** html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 101 KB (SKILL.md 21.5 KB, yük orta)
- **İnceleme:** otomatik

### parallel-agents  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Güvenli paralel agent kullanımı: ne zaman paralelleştirilir/paralelleştirilmez, çalışma ortamından bağımsız yetenek keşfi, güven sınırı, delegasyon bütçesi, izolasyon politikası (worktree/sandbox), delegasyon şablonu, ilerleme yok tespiti ve sentez protokolü. Google Antigravity öncelikli yazılmış.
- **Ne zaman:** Güvenlik/izolasyon kuralları önemli olan çok agent'lı işler; delegasyon bütçesi ve izleme gerektiğinde. · **Ne zaman değil:** Claude Code/Codex'te Antigravity'ye özgü kısımlar uygulanamaz — genel kurallar geçerli. Plan yürütmek için subagent-driven-development, basit paralel hata ayıklama için dispatching-parallel-agents. allowed-tools/effort Claude Code'a özgü.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Güvenlik ve izolasyon bölümleri iyi; Antigravity odaklı olması diğer harness'lerde gürültü yaratıyor.

### project-artifact  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a
- **Teknoloji:** css, git, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 19.9 KB, yük orta)
- **İnceleme:** otomatik

### receipts  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying Claude Code usage/spend to a manager, self-review, or "what have I been using this for" check-ins. Mines ~/.claude/projects locally (no extra API calls beyond one final write-up), cross-references local git history, and writes a markdown report plus a self-contained HTM
- **Teknoloji:** api-anahtari, git, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### session-report  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 97 (A)

- **Ne yapar:** Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.
- **Teknoloji:** api-anahtari, css, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 56 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### subagent-driven-development  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Yazılı uygulama planını görev başına taze bir uygulayıcı alt-agent göndererek yürütür; her görevden sonra spec uyumu + kod kalitesi incelemesi, düzeltme döngüsü ve sonda tüm dal incelemesi yapar. Rol başına model seçimi, karar defteri (ledger), kesintisiz yürütme kuralları ve görev özeti/inceleme paketi betikleri içerir.
- **Ne zaman:** Bağımsız görevlere bölünmüş bir planı tek oturumda yüksek kaliteyle uygulamak. · **Ne zaman değil:** Plan yoksa (önce writing-plans/planning-and-task-breakdown); görevler sıkı bağımlıysa; küçük tek dosyalık işlerde. Codex'te alt-agent desteği yoksa her görev için ayrı `codex exec` çağrısı ya da executing-plans ile sıralı yürütme kullanılır.
- **Teknoloji:** git, bash
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → birincil · **Roller:** agent-orkestra, planlayici
- **Boyut:** 56 KB (SKILL.md 19.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi: düzeltme döngüsü ve final inceleme ayrıntıları references/fix-loop.md ve references/final-review.md dosyalarına taşındı; SKILL.md 260 satır kısaldı, akış diyagramı sadeleşti. Davranış aynı, bağlam yükü azaldı.

### using-agent-skills  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** addyosmani/agent-skills ailesinin meta-skill'i: işin geliştirme aşamasına göre hangi skill'in uygulanacağını gösteren karar ağacı (interview-me, spec, plan, incremental-implementation, test, review, ship…) ve temel çalışma davranışları (varsayımları açığa çıkar, karışıklığı yönet, sadeliği koru, kapsamı koru, doğrula).
- **Ne zaman:** agent-skills ailesinden birden çok skill kurulu projelerde oturum başında doğru skill'i seçmek. · **Ne zaman değil:** Ailenin skilleri kurulu değilse karar ağacındaki adlar boşa düşer; superpowers ailesi kullanılıyorsa using-superpowers ile birlikte kurma (iki meta-skill çakışır).
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → birincil · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil, meta grubunda). Zorlayıcı dil kullanmadan net yönlendirme yapıyor; çalışma davranışları bölümü aileden bağımsız da değerli.

### using-n8n-mcp-skills  ·  czlonkowski/n8n-skills @ e037563  ·  puan 86 (A)

- **Ne yapar:** Use when building, editing, validating, testing, or debugging an n8n workflow through the n8n-mcp MCP server — designing a flow, configuring a node, writing an expression or Code node, wiring credentials, or fixing one that misbehaves. The entry-point skill for the n8n-mcp-skills pack: it routes you to the right specialist skill, gives working knowledge of every n8n-mcp tool from turn one, and sta
- **Teknoloji:** api-anahtari, canvas, docker, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** czlonkowski (kisi, ★6564, son güncelleme 2026-10-24, lisans MIT)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 17.2 KB, yük orta)
- **İnceleme:** otomatik

### using-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 98 (A)

- **Ne yapar:** superpowers ailesinin meta-skill'i: '%1 ihtimal bile varsa skill'i çağır' kuralı, süreç skillerinin önceliği, rasyonalizasyon kırmızı bayrakları ve Claude Code, Codex, Pi, Antigravity, Gemini, Hermes, Muse için araç eşleme dosyaları.
- **Ne zaman:** superpowers ailesinin (brainstorming, writing-plans, systematic-debugging, subagent-driven-development…) birlikte kurulduğu projeler. · **Ne zaman değil:** Aile kurulu değilse; agent-skills ailesinin meta-skill'iyle birlikte. Çok agresif tetikleme dili küçük işlerde gereksiz süreç yükü yaratabilir. Codex'te references/codex-tools.md araç eşlemesini kullanır — ek uyarlama gerekmez.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 20 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (meta grubunda). Çok harness'li araç eşlemesi en güçlü yanı; aile dışında kullanılmaz. superpowers ailesi seçilen projede birincil olur.
