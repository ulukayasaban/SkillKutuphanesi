# 06-devops-guvenlik-performans — Yazılım Geliştirme

_CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **10/41**

### agents-sdk  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Build, debug, or review Cloudflare Agents SDK applications using the agents package.
- **Teknoloji:** api-anahtari, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** otomatik

### api-monitoring  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### basin  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build and troubleshoot Cloudflare Basin analytics workflows with Basin Pipelines, Basin Catalog, and Basin SQL. Use for streaming data into R2 Iceberg tables, managing catalogs, or querying those tables; also use for requests using the former Data Platform, Pipelines, R2 Data Catalog, or R2 SQL names.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 52 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### cf-cli  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Cloudflare's official cf CLI (beta) for the public Cloudflare API and Workers projects. Use for finding and running Cloudflare commands from the terminal — sign-in and profiles, cf cli search, cf schema, cf deploy/dev/build, resource commands for DNS, zones, D1, KV, and R2 — and for choosing between cf and Wrangler in a project.
- **Teknoloji:** api-anahtari, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk)
- **İnceleme:** otomatik

### ci-cd-and-automation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 98 (A)

- **Ne yapar:** CI/CD hattı kurulumu: kalite kapısı sırası (lint → tip → birim → build → entegrasyon → E2E → güvenlik), GitHub Actions örnekleri (veritabanlı entegrasyon ve E2E dahil), CI hatalarını agent'a geri besleme, preview deploy, feature flag, kademeli yayın ve geri alma planı, ortam yönetimi, Dependabot/Renovate ve CI hızlandırma.
- **Ne zaman:** Build/deploy hattı kurarken veya değiştirirken; kalite kapılarını otomatikleştirirken; test çalıştırıcısını CI'a bağlarken. · **Ne zaman değil:** GitHub Actions dışı CI'da örnekler doğrudan uymaz (ilkeler geçerli); tek seferlik yerel betikler.
- **Teknoloji:** github-actions, node, playwright
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112028, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ci-cd → birincil · **Roller:** devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, ci-cd grubunun birincili. Pratik YAML örnekleri ve 'CI hatasını agent'a besle' bölümü agent iş akışına özgü bir artı.

### claude-security  ·  anthropics/claude-plugins-official @ af59ee3  ·  puan 97 (A)

- **Ne yapar:** Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or suggest patches (findings turned into targeted patch files, each verified by a panel of agents, that you apply when you choose). Use when the user asks to scan, audit or check code with Claude Security, to scan their changes with Claude Security
- **Teknoloji:** api-anahtari, git, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** anthropics (kurum, resmî, ★45466, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 133 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### cloudflare  ·  cloudflare/skills @ 86505e4  ·  puan 92 (A)

- **Ne yapar:** Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when the user describes a need without naming a Cloudflare product; then find the relevant skill or documentation.
- **Teknoloji:** api-anahtari, git, next.js, node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 320 KB (SKILL.md 26.5 KB, yük buyuk)
- **İnceleme:** otomatik

### cloudflare-email-service  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration.
- **Teknoloji:** api-anahtari, html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 6.5 KB, yük kucuk)
- **İnceleme:** otomatik

### cloudflare-one  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. Use cloudflare-one-migrations for migration planning from other vendors.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 23.3 KB, yük orta)
- **İnceleme:** otomatik

### cloudflare-one-migrations  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.2 KB, yük orta)
- **İnceleme:** otomatik

### deploy-to-vercel  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 85 (A)

- **Ne yapar:** Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".
- **Teknoloji:** git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33272, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 11.5 KB, yük orta)
- **İnceleme:** otomatik

### deployment-procedures  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Üretim deploy ilkeleri: platform seçim ağacı (Vercel/Netlify, Railway/Render/Fly, VPS+PM2/Docker, Kubernetes, serverless), deploy öncesi dört doğrulama kategorisi, beş fazlı deploy akışı, deploy sonrası doğrulama penceresi ve geri alma ilkeleri; betik değil karar öğretir.
- **Ne zaman:** Barındırma platformu seçerken veya deploy prosedürü yazarken; ag-kit /deploy iş akışında. · **Ne zaman değil:** Kademeli yayın ve izleme ayrıntısı (shipping-and-launch); CI hattı yazımı (ci-cd-and-automation).
- **Teknoloji:** docker, git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** deploy-yayin → tamamlayıcı · **Roller:** devops-muhendis
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. Kısa (6 KB) platform karar tablosu yararlı; içerik genel ilkeler, shipping-and-launch ile kısmen örtüşüyor.

### domain-monitoring  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### durable-objects  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 19 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** otomatik

### file-integrity-monitoring  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### gateway-workers  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build, debug, or review Cloudflare Workers invoked by the Forward action in Gateway HTTP policies, including the GatewayMiddleware entrypoint, Gateway types, context, and continuation.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** otomatik

### k2  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build and troubleshoot Cloudflare K2 or K2 Streams durable logs. Use for stream setup, producing from Workers or HTTP, configuring retention and inputs, and consuming through subscriptions.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### localization-testing  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### nextjs-on-cloudflare  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers, choosing between vinext and OpenNext, or setting up vinext for Workers. For setup, migration, or deployment, install vinext's upstream skills with `npx skills add cloudflare/vinext` if missing, then read and follow the applicable skill and
- **Teknoloji:** next.js, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### observability-and-instrumentation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 98 (A)

- **Ne yapar:** Kodu üretimde görünür ve teşhis edilebilir kılar: önce 'çalışıyor'un tanımı, her soru için doğru sinyal (log, metrik, iz), yapılandırılmış loglama, metrikler, dağıtık izleme, uyarılar ve runbook yazımı, son olarak telemetrinin kendisini doğrulama.
- **Ne zaman:** Loglama/metrik/izleme/uyarı eklerken; üretime çıkan her özellikte çalıştığına dair kanıt gerektiğinde; üretim sorunu mevcut veriden anlaşılamıyorsa. · **Ne zaman değil:** Yerel prototip; belirli bir APM ürününün kurulumu (ürün belgeleri).
- **Teknoloji:** opentelemetry, node, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112028, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gozlemlenebilirlik → birincil · **Roller:** backend-muhendis, devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 14 KB (SKILL.md 13.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, gozlemlenebilirlik grubunun birincili. 'Telemetriyi de doğrula' ve runbook bölümleri pratik; satıcıdan bağımsız.

### performance-optimization  ·  addyosmani/agent-skills @ aeac41d  ·  puan 98 (A)

- **Ne yapar:** Ölçüme dayalı performans iyileştirme: Core Web Vitals hedefleri, önce ölç → darboğazı bul → düzelt → doğrula (tut ya da geri al, geri alınan denemeleri de kaydet) → regresyona karşı koru akışı; ön yüz, arka yüz, sorgu ve veritabanı için nereden ölçmeye başlanacağı ve optimization-patterns.md desen dosyası.
- **Ne zaman:** Performans gereksinimi veya regresyon şüphesi olduğunda; Core Web Vitals/yükleme süresi iyileştirmede; N+1 sorgu düzeltmede; profil çıkarılmış darboğazlarda. · **Ne zaman değil:** Ölçüm yapılmadan 'erken optimizasyon'; React'e özgü kural listesi gerekiyorsa vercel-react-best-practices ile birlikte.
- **Teknoloji:** node, react, css
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112028, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** performans → birincil · **Roller:** devops-muhendis, kod-inceleyici, qa-erisilebilirlik · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 26 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, performans grubunun birincili. Gerekçe: 'tut ya da geri al' ve 'geri alınan denemeyi de kaydet' disiplini ölçümsüz optimizasyonu engelliyor; tüm katmanları kapsıyor. performance-profiling Lighthouse/bundle betikleriyle tamamlayıcı.

### performance-profiling  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Performans profil çıkarma ilkeleri: Core Web Vitals hedefleri, taban → tespit → düzelt → doğrula süreci, sorun tipine göre araç seçimi (Lighthouse, bundle analyzer, DevTools Performance/Memory/Network), bundle ve çalışma zamanı analizi, yaygın darboğazlar; lighthouse_audit.py ve bundle_analyzer.py betikleri.
- **Ne zaman:** Lighthouse denetimi çalıştırmak, bundle boyutunu analiz etmek veya DevTools ile çalışma zamanı profili çıkarmak gerektiğinde. · **Ne zaman değil:** Optimizasyon kararı ve doğrulama disiplini (performance-optimization); backend/veritabanı darboğazları (sınırlı içerik).
- **Teknoloji:** lighthouse, python, node · **Paketler:** python3, lighthouse (npx)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** performans → tamamlayıcı
- **Boyut:** 13 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı (opsiyonel). Kısa ve betikli; içerik büyük ölçüde performance-optimization'ın ölçüm bölümünün tablo özeti.

### public-status-page  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### red-team-tactics  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** MITRE ATT&CK tabanlı kırmızı takım ilkeleri: saldırı yaşam döngüsü fazları ve amaçları, pasif/aktif keşif, ilk erişim vektörleri, Windows/Linux yetki yükseltme ilkeleri, tespitten kaçınma ve operasyonel güvenlik, raporlama. İlke düzeyinde; exploit kodu içermez.
- **Ne zaman:** Yalnız yetkili sızma testi veya kırmızı takım tatbikatında saldırı yüzeyini çerçevelemek ve rapor yapısı kurmak. · **Ne zaman değil:** Yetkisiz hedefler; uygulama geliştirme rolleri (savunma tarafı için security-and-hardening).
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** saldiri-simulasyonu → birincil
- **Boyut:** 4 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Çift kullanımlı (tespitten kaçınma bölümü var) ve yüzeysel; web uygulaması projelerinde savunmaya katkısı düşük. Hiçbir role eklenmedi.

### reverse-engineer-anything  ·  morluto/rea @ 6e2404b  ·  puan 100 (A)

- **Ne yapar:** Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA, and build agent environments (AgentEnv bundles) of web applications from a live instance or a capture. Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction. Skip REA for ordinary source-repository architecture analys
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** morluto (kisi, ★412877, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih
- **Boyut:** 151 KB (SKILL.md 34.7 KB, yük buyuk) · **Bağımlılık:** REA aracı (repo) kurulu olmalı.
- **İnceleme:** otomatik

### sandbox-migrate-to-next  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-next for apps already on the preview.
- **Teknoloji:** docker, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** otomatik

### sandbox-next  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-migrate-to-next when porting a stable app.
- **Teknoloji:** docker, next.js, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** otomatik

### sandbox-stable  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. Use sandbox-next for preview apps and sandbox-migrate-to-next for stable-to-preview migrations.
- **Teknoloji:** docker, git, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.1 KB, yük orta)
- **İnceleme:** otomatik

### security-and-hardening  ·  addyosmani/agent-skills @ aeac41d  ·  puan 100 (A)

- **Ne yapar:** Kodu güvenlik açıklarına karşı sertleştirir: önce tehdit modeli, 'her zaman yap / önce sor / asla yapma' üç katmanlı sınır sistemi; enjeksiyon, XSS, erişim kontrolü, kimlik doğrulama ve oturum, başlıklar/CORS, girdi doğrulama ve yüklemeler, SSRF, türetilmiş yollarda yıkıcı işlemler, rate limit, gizli anahtarlar, bağımlılık ve tedarik zinciri, kişisel veri ve AI/LLM özellikleri için kontroller; inceleme kontrol listesi ve hardening-patterns.md.
- **Ne zaman:** Kullanıcı girdisi, kimlik doğrulama, veri saklama veya dış entegrasyon içeren her özellikte; OWASP Top 10'a karşı giriş akışı denetimi; bağımlılık denetimi. · **Ne zaman değil:** Saldırı simülasyonu/sızma testi (red-team-tactics); otomatik tarama betiği gerektiğinde vulnerability-scanner ile birlikte.
- **Teknoloji:** node, html
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112028, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guvenlik-sertlestirme → birincil · **Roller:** backend-muhendis, devops-muhendis, kod-inceleyici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 30 KB (SKILL.md 17.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, guvenlik-sertlestirme grubunun birincili. Gerekçe: tehdit modeli öncelikli, SSRF ve 'türetilmiş yolda silme' gibi agent'a özgü riskleri ve AI/LLM özelliklerini kapsıyor; 'önce sor' katmanı insan onayı gereken işlemleri net ayırıyor. vulnerability-scanner betikli tarama ile tamamlayıcı.

### security-audit  ·  cloudflare/security-audit-skill @ c1c8a8c  ·  puan 92 (A)

- **Ne yapar:** Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete workflow only for explicit codebase audit or pen-test requests, full/comprehensive/end-to-end reviews, or requested report artifacts.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** cloudflare (kurum, resmî, ★54315, son güncelleme 2026-09-14, lisans MIT)
- **Durum:** tercih
- **Boyut:** 307 KB (SKILL.md 21.5 KB, yük orta)
- **İnceleme:** otomatik

### server-management  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** Sunucu işletim ilkeleri: süreç yöneticisi seçimi (PM2, systemd, Docker, Kubernetes), izleme metrikleri ve uyarı seviyeleri, izleme aracı seçimi, log yönetimi (rotasyon, yapılandırılmış log), ölçekleme kararları ve sağlık kontrolü ilkeleri.
- **Ne zaman:** VPS/kendi sunucusunda çalışan uygulamalarda PM2/systemd yapılandırması, izleme ve ölçekleme kararları. · **Ne zaman değil:** Yönetilen platformlar (Vercel, Railway) — çoğu konu platformca çözülür; ayrıntılı gözlemlenebilirlik (observability-and-instrumentation).
- **Teknoloji:** pm2, systemd, docker, node
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** sunucu-yonetimi → birincil
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: TUT (opsiyonel). Yalnız tablo düzeyinde ilkeler; komut veya yapılandırma örneği yok, modelin zaten bildiğini özetliyor.

### shipping-and-launch  ·  addyosmani/agent-skills @ aeac41d  ·  puan 98 (A)

- **Ne yapar:** Üretime çıkış hazırlığı: kod kalitesi, güvenlik, performans, erişilebilirlik, altyapı ve dokümantasyon için ön yayın kontrol listesi; feature flag stratejisi, eşik değerli kademeli yayın sırası ve geri alma koşulları, izlenecek metrikler ve hata raporlama, yayın sonrası doğrulama, hata bütçesi kapısı ve geri alma planı şablonu.
- **Ne zaman:** Üretime deploy öncesi 'neler hazır olmalı?' sorusunda; kademeli yayın ve geri alma stratejisi planlarken. · **Ne zaman değil:** Platforma özgü deploy komutları (deployment-procedures veya platform belgeleri); CI kurulumu (ci-cd-and-automation).
- **Teknoloji:** git, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112028, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** deploy-yayin → birincil · **Roller:** devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, deploy-yayin grubunun birincili. Gerekçe: somut eşikli kademeli yayın ve hata bütçesi kapısı; deployment-procedures (vudovn) platform seçimi ve deploy fazlarıyla tamamlayıcı.

### synthetic-monitoring  ·  nexscope-ai/eCommerce-Skills @ ee0fb29  ·  puan 80 (A)

- **Ne yapar:** 
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexscope-ai (kurum, ★1304, son güncelleme 2026-08-26, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### turnstile-spin  ·  cloudflare/skills @ 86505e4  ·  puan 92 (A)

- **Ne yapar:** Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify.
- **Teknoloji:** api-anahtari, git, html, next.js, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 92 KB (SKILL.md 28.0 KB, yük buyuk)
- **İnceleme:** otomatik

### vercel-cli-with-tokens  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 85 (A)

- **Ne yapar:** Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel".
- **Teknoloji:** api-anahtari, git, next.js, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33272, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** otomatik

### vercel-optimize  ·  vercel-labs/agent-skills @ 063bee9  ·  puan 85 (A)

- **Ne yapar:** Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel metrics, usage, project config, and code scan results first; investigate only metric-backed candidates; produce ranked recommendations grounded in verified files and version-aware Vercel/framework docs. Trigger for Vercel bill reduction, slow or expensi
- **Teknoloji:** api-anahtari, next.js, node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33272, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih
- **Boyut:** 808 KB (SKILL.md 16.9 KB, yük orta)
- **İnceleme:** otomatik

### vulnerability-scanner  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Güvenlik açığı analizi ilkeleri: varsayılan ihlal, sıfır güven, derinlemesine savunma; OWASP Top 10:2025 (yeni A03 tedarik zinciri), saldırı yüzeyi haritalama ve risk önceliklendirme; checklists.md ile OWASP/kimlik doğrulama/API/veri koruma kontrol listeleri, security_scan.py ve dependency_analyzer.py tarama betikleri.
- **Ne zaman:** Projede güvenlik taraması, OWASP 2025 uyum kontrolü veya tedarik zinciri (bağımlılık) analizi yaparken. · **Ne zaman değil:** Özellik geliştirirken güvenli kodlama kuralları (security-and-hardening); gerçek bir SAST/DAST aracının yerine (betikler basit desen taraması).
- **Teknoloji:** python · **Paketler:** python3 (security_scan.py, dependency_analyzer.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guvenlik-sertlestirme → tamamlayıcı · **Roller:** devops-muhendis
- **Boyut:** 35 KB (SKILL.md 7.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. OWASP 2025 güncel ve kontrol listeleri iş görüyor; betikler hafif desen taraması, gerçek tarayıcıların (npm audit, semgrep, osv-scanner) yerini tutmaz.

### web-perf  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores.
- **Teknoloji:** css, next.js, node, svelte, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.1 KB, yük orta)
- **İnceleme:** otomatik

### workers-best-practices  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 28 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### workers-profiling  ·  cloudflare/skills @ 86505e4  ·  puan 97 (A)

- **Ne yapar:** Profile or debug CPU usage and memory allocation in deployed Cloudflare Workers and Durable Objects. Then use this information to optimize your code.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** otomatik

### wrangler  ·  cloudflare/skills @ 86505e4  ·  puan 95 (A)

- **Ne yapar:** Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, deployment, and resource management. For new projects and projects without a Wrangler configuration file, use the cf CLI instead.
- **Teknoloji:** api-anahtari, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** cloudflare (kurum, resmî, ★3226, son güncelleme 2026-10-30, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 11.4 KB, yük orta)
- **İnceleme:** otomatik
