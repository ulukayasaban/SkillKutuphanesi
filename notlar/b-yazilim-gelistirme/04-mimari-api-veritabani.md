# 04-mimari-api-veritabani — Yazılım Geliştirme

_Mimari, API/arayüz tasarımı, veritabanı, backend_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **8/15**

### api-and-interface-design  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Kararlı API ve modül arayüzü tasarımı: Hyrum yasası ve tek sürüm kuralı, önce sözleşme, tutarlı hata semantiği, sınırda doğrulama, değiştirmek yerine ekleme, öngörülebilir isimlendirme ve idempotency anahtarını doğru uygulama; REST kaynak tasarımı, sayfalama, filtreleme, PATCH ve TypeScript arayüz desenleri (ayrık birleşimler, girdi/çıktı ayrımı, markalı ID tipleri).
- **Ne zaman:** REST/GraphQL endpoint'i, modül sınırı veya ön yüz-arka yüz sözleşmesi tasarlarken; herkese açık bir arayüzü değiştirirken. · **Ne zaman değil:** Yalnız iç, tek kullanımlık fonksiyonlar; API stil seçimi (REST mi GraphQL mi tRPC mi) ağırlıklıysa api-patterns ile birlikte.
- **Teknoloji:** typescript, rest, graphql
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★113281, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** api-tasarimi → birincil · **Roller:** backend-muhendis
- **Boyut:** 15 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, api-tasarimi grubunun birincili. Gerekçe: ilkeler (Hyrum, ekleme > değiştirme, idempotency) ve TS desenleri somut ve sürüm bağımsız; api-patterns ise stil seçimi, kimlik doğrulama ve rate limit dosyalarıyla tamamlayıcı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### api-breaking-change-detector  ·  github/awesome-copilot @ 7e40881  ·  puan 100 (A)

- **Ne yapar:** Cross-references C# Web API controllers/DTOs against their TypeScript/JavaScript consumers (React, Angular, Vue, Svelte, Node.js, or hand-written/auto-generated HTTP clients like Fetch, Axios, NSwag) to catch contract drift in both directions: backend changes that break client applications (renamed/removed JSON keys, new required parameters, status code shifts) and frontend code sending fields the
- **Teknoloji:** node, react, svelte, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** github (kurum, ★40799, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### api-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in API tasarım karar rehberi: REST/GraphQL/tRPC seçim ağacı, kaynak isimlendirme ve durum kodları, zarf/hata/sayfalama yanıt biçimleri, sürümleme, kimlik doğrulama (JWT, OAuth, Passkey, API anahtarı), rate limiting, OpenAPI dokümantasyonu ve OWASP API Top 10 güvenlik testini ayrı dosyalarda seçici okumayla sunar; api_validator.py betiği içerir.
- **Ne zaman:** API stili ve kimlik doğrulama yöntemi seçerken; rate limiting veya sürümleme stratejisi belirlerken. · **Ne zaman değil:** Sözleşme/arayüz ilkeleri ağırlıklı işlerde tek başına (api-and-interface-design); UI işleri.
- **Teknoloji:** rest, graphql, trpc, typescript, python · **Paketler:** python3 (api_validator.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** api-tasarimi → tamamlayıcı · **Roller:** backend-muhendis
- **Boyut:** 20 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. Seçici okuma kuralı bağlamı küçük tutuyor (SKILL.md 2.5 KB), auth ve rate-limiting dosyaları yararlı. İçerik yer yer yüzeysel; @[skills/...] biçimindeki çapraz referanslar ag-kit sözdizimi.

### architecture-blueprint-generator  ·  github/awesome-copilot @ 7e40881  ·  puan 100 (A)

- **Ne yapar:** Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks and architectural patterns, generates visual diagrams, documents implementation patterns, and provides extensible blueprints for maintaining architectural consistency and guiding new development.
- **Teknoloji:** node, python, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** github (kurum, ★40799, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.0 KB, yük orta)
- **İnceleme:** otomatik

### architecture@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Mimari karar çerçevesi: bağlam keşfi soruları ve proje sınıflandırması, ödünleşim (trade-off) analizi ve ADR şablonları, desen seçimi karar ağaçları, MVP/SaaS/kurumsal örnekler ve desen hızlı başvurusu; 'basit başla, karmaşıklığı ancak kanıtlanınca ekle' ilkesi.
- **Ne zaman:** Sistem tasarımı, desen seçimi (monolit/mikroservis, katmanlar), önemli kararların ADR olarak kaydı. · **Ne zaman değil:** Doğrudan kod uygulaması; ayrıntılı ADR/dokümantasyon süreci (c-dokuman'daki documentation-and-adrs daha kapsamlı olabilir).
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** mimari-karar → birincil · **Roller:** backend-muhendis
- **Boyut:** 12 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Tek mimari karar skilli; seçici okuma ile hafif (SKILL.md 1.9 KB). İçerik genel ve yer yer ders kitabı düzeyinde ama ADR ve ödünleşim şablonları iş görüyor.

### database-design  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Veritabanı tasarım kararları: PostgreSQL/Neon/Turso/SQLite seçimi, Drizzle/Prisma/Kysely ORM seçimi, normalizasyon ve ilişkiler, indeks tipleri, N+1 ve EXPLAIN ANALYZE ile sorgu optimizasyonu, güvenli migrasyonlar; schema_validator.py betiği içerir. Tercih belirsizse kullanıcıya sormayı şart koşar.
- **Ne zaman:** Şema tasarlarken, ORM/veritabanı seçerken, migrasyon planlarken veya yavaş sorgu optimize ederken (Prisma, Drizzle, SQL). · **Ne zaman değil:** Kesintisiz üretim migrasyonu (expand/contract) ayrıntısı gerekiyorsa deprecation-and-migration ile birlikte; NoSQL ağırlıklı projeler (sınırlı içerik).
- **Teknoloji:** postgresql, sqlite, prisma, drizzle, sql · **Paketler:** python3 (schema_validator.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** veritabani-tasarimi → birincil · **Roller:** backend-muhendis
- **Boyut:** 13 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, veritabani-tasarimi grubunun tek üyesi. 'Her şeye PostgreSQL deme' ve seçim tabloları dengeli; içerik ilke düzeyinde, derin şema örnekleri az.

### ddd-aggregate  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Scaffold an aggregate root with entity, value objects, repository interface, domain events, and test stubs. Use when adding a new aggregate to an existing bounded context, modeling a new business concept that owns invariants, or generating the boilerplate for an entity + repo + events triplet.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ddd-context  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Create and manage a DDD bounded context with standard directory structure. Use when starting a new subdomain, splitting a monolith into bounded contexts, or scaffolding the domain/application/infrastructure layout for a fresh module.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### ddd-validate  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Validate domain boundaries -- detect cross-context import violations and aggregate invariant issues. Use when auditing a DDD codebase for leaks between bounded contexts, before merging cross-cutting changes, or as a CI gate to catch boundary erosion early.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### frontend-architecture  ·  vudovn/ag-kit @ 549ba3d  ·  puan 82 (A)

- **Ne yapar:** Ön yüz kodunu ölçeklenir biçimde düzenleme kuralları: UI / mantık (hook, composable) / veri (servis dosyaları) / tip / doğrulama (şema) katmanlarına ayırma, dosya sorumluluğu ve boyutu, Next.js'te varsayılan Server Component, Vue Composition API, durumu yerelden başlatma, form şeması, prop ve isimlendirme kuralları, 'god component' önleme, Tailwind sınıf hijyeni ve minimum test/erişilebilirlik tabanı.
- **Ne zaman:** React/Next veya Vue kod tabanını yapılandırırken ya da organizasyonunu incelerken: mantık, API çağrısı, durum ve tiplerin nerede yaşayacağı. · **Ne zaman değil:** Görsel tasarım (frontend-design, design-taste-frontend); React/Next performans kuralları (vercel-react-best-practices).
- **Teknoloji:** react, next.js, vue, typescript, tailwind
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** frontend-mimarisi → birincil · **Roller:** frontend-muhendis
- **Boyut:** 8 KB (SKILL.md 7.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, frontend-mimarisi grubunun birincili. ag-kit'in en somut skillerinden; React ve Vue'yu birlikte kapsaması ve 'görsel tasarım değil yapı' sınırı net. ../app-builder ve ../frontend-design kardeş bağlantıları kurulumda o skiller yoksa boşa düşer (yalnız atıf).
- **Not:** ../app-builder ve ../nextjs-react-expert kardeş bağlantıları yalnız 'ayrıca bkz' atfı; bu skiller kurulmasa da skill çalışır (kardes-eksik uyarısı göz ardı edilebilir).

### frontend-ui-engineering  ·  addyosmani/agent-skills @ 301b02b  ·  puan 94 (A)

- **Ne yapar:** Üretim kalitesinde, erişilebilir ve responsive arayüz kurma: bileşen dosya yapısı ve desenleri, durum yönetimi, tasarım sistemine bağlılık ve 'AI estetiğinden' kaçınma, boşluk/tipografi/renk, WCAG 2.1 AA (klavye, ARIA, odak yönetimi, anlamlı boş/hata durumları), responsive tasarım, yükleme ve geçiş durumları.
- **Ne zaman:** Arayüz, sayfa veya bileşen yazarken/değiştirirken; erişilebilirlik gereksinimi olduğunda; çıktının 'AI yapımı' değil üretim kalitesinde görünmesi gerektiğinde. · **Ne zaman değil:** Sanat yönetimi/görsel yön belirleme (a-tasarim skilleri); salt backend işleri.
- **Teknoloji:** react, typescript, css, tailwind
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★113281, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** frontend-ui-uygulama → birincil · **Roller:** frontend-muhendis
- **Boyut:** 12 KB (SKILL.md 11.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, frontend-ui-uygulama grubunun birincili; frontend-muhendis çekirdeğinde kalır. Erişilebilirlik ve durum (boş/hata/yükleme) bölümleri güçlü; görsel yön için a-tasarim skilleriyle birlikte kullanılmalı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### migrate-create  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Create a new sequentially numbered database migration with up/down SQL files
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar. · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### migrate-validate  ·  ruvnet/ruflo @ 98ddf41  ·  puan 100 (A)

- **Ne yapar:** Validate pending migrations for foreign key consistency, rollback safety, and best practices
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** ruvnet (kisi, ★81282, son güncelleme 2026-11-09, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk) · **Bağımlılık:** Skillerin çoğu Ruflo (eski adıyla claude-flow) komut satırını ve MCP sunucusunu ister (npx ruflo / npx @claude-flow/cli, mcp__plugin_ruflo-* araçları); eklenti skilleri kendi eklentisinin araçlarını çağırır. Ruflo kurulu değilse yalnızca kavram referansı olarak işe yarar.
- **İnceleme:** otomatik

### nodejs-best-practices  ·  vudovn/ag-kit @ 549ba3d  ·  puan 74 (B)

- **Ne yapar:** Node.js arka yüz karar ilkeleri: Hono/Fastify/NestJS/Express seçim ağacı, yerel TypeScript ve modül sistemi kararları, katmanlı mimari, merkezi hata işleme, async desenleri, doğrulama ve güvenlik ilkeleri; sabit kod yerine bağlama göre karar vermeyi öğretir.
- **Ne zaman:** Node.js backend kurarken veya framework seçerken; mevcut Node servisinin yapısını gözden geçirirken. · **Ne zaman değil:** Next.js API route'larıyla sınırlı basit işler; ayrıntılı API sözleşmesi tasarımı (api-and-interface-design).
- **Teknoloji:** node, typescript, express, fastify, hono, nestjs
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** node-backend → birincil · **Roller:** backend-muhendis
- **Boyut:** 8 KB (SKILL.md 8.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Güncel seçenekleri (Hono, yerel TS) kapsıyor ve benchmark iddialarında temkinli; ilke düzeyinde, kod örneği az.

### python-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 74 (B)

- **Ne yapar:** Python geliştirme karar ilkeleri: FastAPI/Django/Flask seçim ağacı, async/sync kararı ve kütüphane seçimi, tip ipucu stratejisi ve Pydantic doğrulama, proje yapısı, hata işleme ve test ilkeleri.
- **Ne zaman:** Python backend/servis kurarken veya framework seçerken; tip ipucu ve proje yapısı kararlarında. · **Ne zaman değil:** Veri bilimi/notebook işleri (kapsam dışı); tek dosyalık betikler.
- **Teknoloji:** python, fastapi, django, flask, pydantic
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** python-gelistirme → birincil · **Roller:** backend-muhendis
- **Boyut:** 9 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve dengeli karar rehberi; ilke düzeyinde, derinlik sınırlı. Backend bağlamında kaldığı için kategorisi 04'te bırakıldı.
