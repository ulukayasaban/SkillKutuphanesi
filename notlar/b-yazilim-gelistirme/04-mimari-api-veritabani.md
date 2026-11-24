# 04-mimari-api-veritabani — Yazılım Geliştirme

_Mimari, API/arayüz tasarımı, veritabanı, backend_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **7/61**

### alloydb-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Manages clusters, instances, and backups for AlloyDB for PostgreSQL, and integrates with AlloyDB Model Context Protocol (MCP) tools for automated database operations. Use when creating, configuring, or administering AlloyDB databases. Do NOT use for general PostgreSQL instances (e.g. Cloud SQL) or other GCP databases.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 27 KB (SKILL.md 7.2 KB, yük kucuk)
- **İnceleme:** otomatik

### api-and-interface-design  ·  addyosmani/agent-skills @ 8c99fa3  ·  puan 100 (A)

- **Ne yapar:** Kararlı API ve modül arayüzü tasarımı: Hyrum yasası ve tek sürüm kuralı, önce sözleşme, tutarlı hata semantiği, sınırda doğrulama, değiştirmek yerine ekleme, öngörülebilir isimlendirme ve idempotency anahtarını doğru uygulama; REST kaynak tasarımı, sayfalama, filtreleme, PATCH ve TypeScript arayüz desenleri (ayrık birleşimler, girdi/çıktı ayrımı, markalı ID tipleri).
- **Ne zaman:** REST/GraphQL endpoint'i, modül sınırı veya ön yüz-arka yüz sözleşmesi tasarlarken; herkese açık bir arayüzü değiştirirken. · **Ne zaman değil:** Yalnız iç, tek kullanımlık fonksiyonlar; API stil seçimi (REST mi GraphQL mi tRPC mi) ağırlıklıysa api-patterns ile birlikte.
- **Teknoloji:** typescript, rest, graphql
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★120187, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** api-tasarimi → birincil · **Roller:** backend-muhendis
- **Boyut:** 15 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, api-tasarimi grubunun birincili. Gerekçe: ilkeler (Hyrum, ekleme > değiştirme, idempotency) ve TS desenleri somut ve sürüm bağımsız; api-patterns ise stil seçimi, kimlik doğrulama ve rate limit dosyalarıyla tamamlayıcı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### api-gateway-backend-security-and-rate-limiting  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Secures and rate limits backend services behind Google Cloud API Gateway across OpenAPI 2.0 and OpenAPI 3.0.x API configurations, including MCP-enabled gateways. Use when configuring API key or JWT authentication, locking down Cloud Run or Cloud Run functions backends with a gateway service account, reading authenticated claims from X-Apigateway-Api-Userinfo, setting per-project request quotas, or
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 63 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### api-gateway-mcp-server  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Configures Google Cloud API Gateway to act as a remote Model Context Protocol (MCP) server (Public Preview) that exposes REST APIs as agent tools over HTTP (POST /mcp). Use when migrating OpenAPI 2.0 specs to OpenAPI 3.x for MCP, annotating specs with x-google-api-management.mcp and x-google-mcp-tool, securing tools/list with JWTs or API keys, connecting Google ADK (McpToolset) or Apigee API hub a
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 80 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** otomatik

### api-gateway-openapi-spec-authoring  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Writes, migrates, and fixes OpenAPI specs for Google Cloud API Gateway. Use when converting an OpenAPI 2.0 (Swagger) spec to OpenAPI 3.x, writing a new OpenAPI 3.x spec, or fixing a failed "gcloud api-gateway api-configs create", such as "extension is only supported in OpenAPI 2.x". Also use when quotas set with x-google-quota are never enforced, or when a backend receives path parameters as query
- **Teknoloji:** api-anahtari, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 119 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** otomatik

### api-gateway-troubleshooting  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Diagnoses failing requests and deployment errors on Google Cloud API Gateway. Use when calls through a gateway return 4xx or 5xx errors, including 429 and other quota errors, time out, or fail a CORS preflight; when `api-configs create` fails with a service account, concurrency, or limit error, or `gateways create` or `gateways update` fails; when a custom domain, load balancer, or TLS finding inv
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 86 KB (SKILL.md 19.2 KB, yük orta)
- **İnceleme:** otomatik

### api-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in API tasarım karar rehberi: REST/GraphQL/tRPC seçim ağacı, kaynak isimlendirme ve durum kodları, zarf/hata/sayfalama yanıt biçimleri, sürümleme, kimlik doğrulama (JWT, OAuth, Passkey, API anahtarı), rate limiting, OpenAPI dokümantasyonu ve OWASP API Top 10 güvenlik testini ayrı dosyalarda seçici okumayla sunar; api_validator.py betiği içerir.
- **Ne zaman:** API stili ve kimlik doğrulama yöntemi seçerken; rate limiting veya sürümleme stratejisi belirlerken. · **Ne zaman değil:** Sözleşme/arayüz ilkeleri ağırlıklı işlerde tek başına (api-and-interface-design); UI işleri.
- **Teknoloji:** rest, graphql, trpc, typescript, python · **Paketler:** python3 (api_validator.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** api-tasarimi → tamamlayıcı · **Roller:** backend-muhendis
- **Boyut:** 20 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. Seçici okuma kuralı bağlamı küçük tutuyor (SKILL.md 2.5 KB), auth ve rate-limiting dosyaları yararlı. İçerik yer yer yüzeysel; @[skills/...] biçimindeki çapraz referanslar ag-kit sözdizimi.

### apigee-agent-gateway-governance  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Stands up an Apigee API proxy that a Google Cloud Agent Gateway calls as an ext-proc (Service Extension) callout on an agent's LLM traffic, to meter token usage per model, extract caller identity, and apply Model Armor prompt screening or a semantic cache. Use when wiring Apigee in as an AI gateway behind an Agent Gateway, when an agent's model egress needs governing, or when a callout proxy retur
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 397 KB (SKILL.md 26.1 KB, yük buyuk)
- **İnceleme:** otomatik

### application-design-center-design-deploy  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Processes GCP infrastructure design and deployment workflows within Application Design Center (ADC). Use when: - Designing GCP infrastructure with Terraform. - Validating local HCL. - Performing best-practice plan scans. - Importing templates to Application Design Center (ADC). - Deploying templates. - Troubleshooting deployment failures. Boundaries: - Only use for GCP-specific cloud infrastructur
- **Teknoloji:** docker _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 88 KB (SKILL.md 17.7 KB, yük orta)
- **İnceleme:** otomatik

### application-integration-authoring  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Builds, versions, publishes, tests, and executes Google Cloud Application Integration workflows through the REST API and Python discovery client, and promotes versions across environments. Use when listing integrations, downloading or uploading integration versions as JSON, configuring API triggers or config variables, publishing drafts, invoking integrations, or automating CI/CD promotion. Do not
- **Teknoloji:** api-anahtari, git, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 112 KB (SKILL.md 33.7 KB, yük buyuk)
- **İnceleme:** otomatik

### application-integration-basics  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Explains Google Cloud Application Integration concepts, region provisioning, IAM roles, run-as service accounts, interface choices (REST, Python discovery client, Terraform, ADK), and platform limits. Use when setting up Application Integration in a Google Cloud project, enabling required APIs, provisioning a region, configuring IAM or run-as service accounts, choosing between Application Integrat
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 22.6 KB, yük orta)
- **İnceleme:** otomatik

### application-integration-troubleshooting  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Diagnoses failed, stuck, or silent Google Cloud Application Integration runs and Integration Connectors tasks using the REST API, Cloud Logging, and Cloud Monitoring. Use when an integration fails, returns HTTP 200 without doing the expected work, hangs in a suspended or retry state, or hits IAM, run-as service account, connector health, or quota errors. Do not use for initial region provisioning 
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 91 KB (SKILL.md 23.7 KB, yük orta)
- **İnceleme:** otomatik

### architecture@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Mimari karar çerçevesi: bağlam keşfi soruları ve proje sınıflandırması, ödünleşim (trade-off) analizi ve ADR şablonları, desen seçimi karar ağaçları, MVP/SaaS/kurumsal örnekler ve desen hızlı başvurusu; 'basit başla, karmaşıklığı ancak kanıtlanınca ekle' ilkesi.
- **Ne zaman:** Sistem tasarımı, desen seçimi (monolit/mikroservis, katmanlar), önemli kararların ADR olarak kaydı. · **Ne zaman değil:** Doğrudan kod uygulaması; ayrıntılı ADR/dokümantasyon süreci (c-dokuman'daki documentation-and-adrs daha kapsamlı olabilir).
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** mimari-karar → birincil · **Roller:** backend-muhendis
- **Boyut:** 12 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Tek mimari karar skilli; seçici okuma ile hafif (SKILL.md 1.9 KB). İçerik genel ve yer yer ders kitabı düzeyinde ama ADR ve ödünleşim şablonları iş görüyor.

### bigquery-ai-ml  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write SQL queries that perform time-series forecasting, predict values, detect outliers or anomalies, find key drivers, perform semantic search or vector search, classify text, calculate similarity, summarize content, translate language, evaluate models, filter by semantic condit
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 120 KB (SKILL.md 8.8 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Manages datasets, tables, and jobs in BigQuery. Use when you need to interact with BigQuery, run SQL queries, manage BigQuery resources (datasets, tables, views), or perform basic data ingestion and analysis.
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 25 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### bigquery-bigframes  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Generates Python code using BigQuery DataFrames (BigFrames). Use by default for any Python data task involving BigQuery, including data processing, analysis, and machine learning. Don't use for SQL-first workflows or the google-cloud-bigquery client library — use bigquery-basics.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### bigquery-migration-data-exporter  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Generates type-safe, schema-aligned database data export SQL files (.sql) for Snowflake, Databricks, Teradata, Oracle, and PostgreSQL directly from BigQuery Migration Service (BQMS) translation_output/metadata configs, exporting into target file formats (such as Parquet). Use when generating source database export SQL scripts for BigQuery ingestion without connecting to the source database. Don't 
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 311 KB (SKILL.md 25.5 KB, yük buyuk)
- **İnceleme:** otomatik

### bigquery-migration-data-loader  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provisions BigQuery datasets, ingests staged Parquet files directly into native BigQuery tables by using bq load, and deploys already-translated views from local or Cloud Storage BigQuery Migration Service (BQMS) translation outputs. Use when provisioning target BigQuery datasets for warehouse migrations, batch loading staged Parquet files into native BigQuery tables by using bq load, auditing loa
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 62 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-migration-metadata-extractor  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Extracts database catalog metadata and query logs from data warehouses by running the DWH migration extractor locally or on a temporary Google Cloud VM through the BigQuery Migration Cloud Extractor (credentials held in Secret Manager), and inspects extracted `.zip` archives to report object and volume statistics. Use when extracting database metadata or query logs from Snowflake, Redshift, Terada
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 119 KB (SKILL.md 29.7 KB, yük buyuk)
- **İnceleme:** otomatik

### bigquery-migration-sql-translator  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Translates SQL queries, DDL schemas, and stored procedures from legacy database dialects (Teradata, Oracle, Redshift, Snowflake, SparkSQL, HiveQL) to BigQuery GoogleSQL using the BigQuery Migration Service (BQMS) MCP server. Use when translating legacy SQL queries, migrating schemas or metadata zip archives, or configuring BigQuery Migration Service (BQMS) YAML translation settings. Don't use for 
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 191 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-migration-validator  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Validates that tables migrated to BigQuery match their source (Teradata, Snowflake, Oracle, Redshift, Databricks, PostgreSQL, SQL Server, MySQL, MariaDB, Hive, Impala, Vertica) with the BigQuery Migration Service (BQMS) validation tool: schema and data type comparison, column aggregate comparison, and row-level data comparison. Use when generating or editing a validation config, running a validati
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 91 KB (SKILL.md 16.8 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-observability  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides data-retrieval best practices, tool selection guidance, and performant SQL query syntax for BigQuery telemetry across INFORMATION_SCHEMA, Cloud Monitoring, and the REST API. Use when the telemetry to fetch is already known, selecting telemetry tools, writing performant INFORMATION_SCHEMA queries, retrieving telemetry for diagnosing single-job performance bottlenecks, investigating slot co
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 171 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-optimization  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides workflows to optimize BigQuery environments (capacity planning, editions), storage assets (partitioning, clustering, storage lifecycles, billing models), and SQL queries. Use when optimizing cost, modeling Edition migrations, rightsizing reservations, evaluating logical vs. physical storage, designing table partitioning/clustering, generating table DDL, migrating unpartitioned tables, man
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 82 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-troubleshooting  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides diagnostic workflows and step-by-step root-cause analysis procedures for actively broken, failing, or slow BigQuery jobs, execution graph and query plan stage bottlenecks, system performance issues, or unexpectedly expensive workloads. Use when interpreting symptoms, isolating bottlenecks, diagnosing cost spikes (on-demand query spend, capacity slot autoscaling, storage growth), execution
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 89 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** otomatik

### bigquery-udfs  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Creates, deploys, and troubleshoots BigQuery User-Defined Functions (UDFs) and Remote Functions across SQL, JavaScript, Python, and Cloud Run endpoints. Use when writing custom scalar or aggregate functions in BigQuery, installing PyPI packages or Cloud Storage libraries in a Python or JavaScript UDF, or calling Google Cloud and external APIs from a Python UDF (WITH CONNECTION) or Remote Function.
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 61 KB (SKILL.md 18.8 KB, yük orta)
- **İnceleme:** otomatik

### bigtable-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Assists in provisioning instances/tables, designing performant schemas, and querying data in Bigtable. Use when designing Bigtable row keys, configuring column families, writing SQL queries or client library code (Java, Go, Python) for Bigtable, or diagnosing performance/hotspotting issues. Also use when provisioning Bigtable clusters using gcloud or cbt CLIs. Don't use for generic Cloud SQL admin
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 31 KB (SKILL.md 5.5 KB, yük kucuk)
- **İnceleme:** otomatik

### cloud-databases-onboarding  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Guides users through discovering their database requirements, recommends a Google Cloud database based on a recommendation matrix, and assists in database creation. Use when a user asks 'What database service should I use?', 'Help me pick a database', or when a user wants to create a new database on Google Cloud. Don't use for general Google Cloud maintenance, managing existing databases, or datab
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 72 KB (SKILL.md 6.9 KB, yük kucuk)
- **İnceleme:** otomatik

### cloud-sql-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** This file generates or explains Cloud SQL resources. Use this file when the user asks to create a Cloud SQL instance or database for MySQL, PostgreSQL, or SQL Server. Cloud SQL manages third-party MySQL, PostgreSQL, and SQL Server instances as resources in Cloud SQL. For example, when Cloud SQL creates an open-source MySQL instance, the resulting resource is a Cloud SQL for MySQL instance that Goo
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### database-design  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Veritabanı tasarım kararları: PostgreSQL/Neon/Turso/SQLite seçimi, Drizzle/Prisma/Kysely ORM seçimi, normalizasyon ve ilişkiler, indeks tipleri, N+1 ve EXPLAIN ANALYZE ile sorgu optimizasyonu, güvenli migrasyonlar; schema_validator.py betiği içerir. Tercih belirsizse kullanıcıya sormayı şart koşar.
- **Ne zaman:** Şema tasarlarken, ORM/veritabanı seçerken, migrasyon planlarken veya yavaş sorgu optimize ederken (Prisma, Drizzle, SQL). · **Ne zaman değil:** Kesintisiz üretim migrasyonu (expand/contract) ayrıntısı gerekiyorsa deprecation-and-migration ile birlikte; NoSQL ağırlıklı projeler (sınırlı içerik).
- **Teknoloji:** postgresql, sqlite, prisma, drizzle, sql · **Paketler:** python3 (schema_validator.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** veritabani-tasarimi → birincil · **Roller:** backend-muhendis
- **Boyut:** 13 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, veritabani-tasarimi grubunun tek üyesi. 'Her şeye PostgreSQL deme' ve seçim tabloları dengeli; içerik ilke düzeyinde, derin şema örnekleri az.

### datalineage-bigquery-asset-impact-analysis  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Analyzes the downstream impact (blast radius) using data lineage on Google Cloud when a BigQuery table or view is broken, stale, or modified. Identifies all downstream tables, dashboards, and processes that will be affected. Use when: - Performing a blast radius or impact analysis for a BigQuery table or view. - Assessing the consequences of modifying, deleting, or pausing updates to a BigQuery as
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** otomatik

### datalineage-summary  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Summarizes data lineage graphs on Google Cloud to help users debug data quality issues and understand data provenance for BigQuery and Cloud Storage. Use when summarizing upstream and downstream data flows, and presenting complex lineage data as an intuitive Markdown report. Don't use for generic BigQuery queries, editing lineage relationships, or downstream deprecation. Don't use for downstream b
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** otomatik

### dbt-sf-to-bq-translator  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Translates Snowflake dbt SQL models to Standardized BigQuery SQL. Handles SQL compilation, Jinja macro placeholder masking, BigQuery Translation Service migration workflows, AST-based config transformations, explicit type casting, JSON extraction standardization, and deduplication. Use when migrating Snowflake dbt pipelines or models to BigQuery on Google Cloud. Don't use for generic BigQuery quer
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 119 KB (SKILL.md 15.2 KB, yük orta)
- **İnceleme:** otomatik

### firebase-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Provides foundational Firebase CLI setup, CLI installation, version checks (`firebase-tools@latest --version`), CLI login (including --no-localhost), project creation, project selection (`firebase use`), and app config file downloads (`google-services.json`, `GoogleService-Info.plist`). Use ONLY for CLI login, project creation/switching, or downloading app config files. Don't use for Firebase Host
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 50 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** otomatik

### frontend-architecture  ·  vudovn/ag-kit @ 549ba3d  ·  puan 82 (A)

- **Ne yapar:** Ön yüz kodunu ölçeklenir biçimde düzenleme kuralları: UI / mantık (hook, composable) / veri (servis dosyaları) / tip / doğrulama (şema) katmanlarına ayırma, dosya sorumluluğu ve boyutu, Next.js'te varsayılan Server Component, Vue Composition API, durumu yerelden başlatma, form şeması, prop ve isimlendirme kuralları, 'god component' önleme, Tailwind sınıf hijyeni ve minimum test/erişilebilirlik tabanı.
- **Ne zaman:** React/Next veya Vue kod tabanını yapılandırırken ya da organizasyonunu incelerken: mantık, API çağrısı, durum ve tiplerin nerede yaşayacağı. · **Ne zaman değil:** Görsel tasarım (frontend-design, design-taste-frontend); React/Next performans kuralları (vercel-react-best-practices).
- **Teknoloji:** react, next.js, vue, typescript, tailwind
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** frontend-mimarisi → birincil · **Roller:** frontend-muhendis
- **Boyut:** 8 KB (SKILL.md 7.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, frontend-mimarisi grubunun birincili. ag-kit'in en somut skillerinden; React ve Vue'yu birlikte kapsaması ve 'görsel tasarım değil yapı' sınırı net. ../app-builder ve ../frontend-design kardeş bağlantıları kurulumda o skiller yoksa boşa düşer (yalnız atıf).
- **Not:** ../app-builder ve ../nextjs-react-expert kardeş bağlantıları yalnız 'ayrıca bkz' atfı; bu skiller kurulmasa da skill çalışır (kardes-eksik uyarısı göz ardı edilebilir).

### frontend-ui-engineering  ·  addyosmani/agent-skills @ 8c99fa3  ·  puan 98 (A)

- **Ne yapar:** Üretim kalitesinde, erişilebilir ve responsive arayüz kurma: bileşen dosya yapısı ve desenleri, durum yönetimi, tasarım sistemine bağlılık ve 'AI estetiğinden' kaçınma, boşluk/tipografi/renk, WCAG 2.1 AA (klavye, ARIA, odak yönetimi, anlamlı boş/hata durumları), responsive tasarım, yükleme ve geçiş durumları.
- **Ne zaman:** Arayüz, sayfa veya bileşen yazarken/değiştirirken; erişilebilirlik gereksinimi olduğunda; çıktının 'AI yapımı' değil üretim kalitesinde görünmesi gerektiğinde. · **Ne zaman değil:** Sanat yönetimi/görsel yön belirleme (a-tasarim skilleri); salt backend işleri.
- **Teknoloji:** react, typescript, css, tailwind
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★120187, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** frontend-ui-uygulama → birincil · **Roller:** frontend-muhendis
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT, frontend-ui-uygulama grubunun birincili; frontend-muhendis çekirdeğinde kalır. Erişilebilirlik ve durum (boş/hata/yükleme) bölümleri güçlü; görsel yön için a-tasarim skilleriyle birlikte kullanılmalı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### google-cloud-solution-agentic-ai-bidirectional-streaming  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Guides agents to interactively discover customer requirements for live, bidirectional multi-agent AI systems that process continuous streams of multimodal data for real-time technical guidance and safety monitoring. Generates a custom Google Cloud solution that uses opinionated best practices and architecture guidance. Use when users need agentic assistance to design and create a multi-product sol
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-agentic-ai-borderless-data-lakehouse  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Discovers requirements and designs a borderless open data lakehouse using Lakehouse for Apache Iceberg and BigQuery data agents. Use when architecting multi-cloud storage infrastructure (Cloud Storage, AWS S3, Azure Blob), establishing ingestion and AI serving subsystems, configuring Cross-Cloud Interconnect, or deploying Gemini Enterprise Agent Platform and BigQuery data agents. Don't use for sin
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-agentic-ai-data-science-workflow  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Designs a tailored multi-product agentic data science architecture on Google Cloud that incorporates opinionated best practices. Use when architecting multi-product solutions for agent-based data analytics or ML workloads. Don't use for simple queries, non-agentic pipelines, general cloud reviews, or writing agent code.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-agentic-analytics-spark-knowledge-catalog  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Discovers requirements and designs an end-to-end governed agentic analytics solution using Knowledge Catalog and Managed Service for Apache Spark (Lightning Engine). Use when designing data science and analytics workflows across structured and unstructured distributed data (including in S3, Azure Blob, AlloyDB, and Iceberg), establishing metadata governance with Knowledge Catalog aspect types, or 
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 32 KB (SKILL.md 17.3 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-architecture  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Interactively discovers requirements and designs holistic, multi-product system architectures, solution blueprints, and deployment recommendations for complex workloads on Google Cloud. Use when designing end-to-end cloud solutions, selecting and integrating Google Cloud services, generating architecture diagrams, or conducting requirements discovery for new cloud workloads or migrations. Don't us
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 137 KB (SKILL.md 14.4 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-build-deploy-agents  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Designs, builds, and deploys AI agents or multi-agent systems on Google Cloud. Provides an interactive workflow to gather requirements, recommend a tailored architecture, and generate deployment instructions. Use when designing or implementing agentic systems on Google Cloud. Don't use for general Google Cloud solution architecture (use google-cloud-solution-architecture instead) or for narrow tas
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 43 KB (SKILL.md 13.8 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-event-driven-decoupling  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Decouples tightly coupled services or monoliths with Google Cloud Pub/Sub so services scale and fail independently, using Go reference implementations adaptable to Java, Python, Node.js, and other stacks. Use when breaking apart synchronous chains, defining transaction boundaries, bulkheads, and Transactional Outbox or post-commit publishing; sizing Pub/Sub topics, subscription filters, dead-lette
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 116 KB (SKILL.md 16.9 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-guided-gke-ai-migration  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Guides the migration of existing AI workloads (Cloud Run, Gemini API, Gemini Enterprise Agent Platform) to self-hosted GKE inference using gcloud and kubectl. Use when the user has an existing AI inference workload (on Cloud Run, the Gemini API, Gemini Enterprise Agent Platform, or a custom VM) and wants to move it to self-hosted inference on GKE, or asks follow-up questions during such a migratio
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 40 KB (SKILL.md 32.6 KB, yük buyuk)
- **İnceleme:** otomatik

### google-cloud-solution-hybrid-search-alloydb  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Discovers requirements and generates architectural, design, and deployment guidance for dynamic hybrid search systems by combining semantic search and keyword search. Optimized for AlloyDB hybrid search use cases in Google Cloud. Use when users need vector search combined with structured SQL filtering, faceted attributes, semantic reranking, in-database AI validation, or serverless hosting across 
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 44 KB (SKILL.md 15.7 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-multi-agent-security  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Designs, deploys, and secures Google Cloud Agent Gateway solutions. Use when the user needs to configure multi-agent security, ingress (CLIENT_TO_AGENT), or egress (AGENT_TO_ANYWHERE) patterns involving Model Armor, IAP, and Agent Registry. Don't use for general Cloud Load Balancing or basic VPC setup not related to Agent Gateways.
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 30 KB (SKILL.md 14.6 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-n-tier-serverless-web-app  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Assists in designing and implementing secure n-tier serverless web applications and microservices on Google Cloud. Use when users need architecture designs, security checklists, Terraform code, or deployment guidance for multi-tier serverless apps, regional data residency / European sovereignty compliance, zero-trust private VPC networking, or Private Service Connect. Don't use for VM, GKE, or non
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 106 KB (SKILL.md 21.6 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-solution-rag-enterprise-search-gke-sqldb  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Discovers requirements, and generates architectural, design, and deployment guidance for a retrieval-augmented generation (RAG)-capable enterprise search system in Google Cloud. Use when users need a vector-enabled SQL database as the store and index for the embedding vectors, an open model and open-source inferencing framework, and Kubernetes containers to host all the application components. DON
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 35 KB (SKILL.md 15.7 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-storage-basics  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Stores, retrieves, and manages data as objects in Cloud Storage on Google Cloud (also known colloquially as GCS) buckets. Use when you need to interact with Cloud Storage — set up a Storage MCP server (remote or local Toolbox), create or configure buckets, upload, download, stream, or transfer data, organize objects with folders, generate signed URLs, control access (IAM, ACLs, public access preve
- **Teknoloji:** api-anahtari, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 142 KB (SKILL.md 17.3 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-storage-bucket-architect  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Creates Cloud Storage on Google Cloud (also known colloquially as GCS) buckets. Analyzes the workload (sensitive data, media hosting, ingestion, web hosting, archiving, backup, logging, analytics, AI/ML, or general-purpose), validates project-level security settings, and designs a secure-by-default, cost-effective configuration (location, storage class, uniform bucket-level access, public access p
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 178 KB (SKILL.md 12.5 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-storage-diagnostic  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Troubleshoots and diagnoses Cloud Storage on Google Cloud (also known colloquially as GCS) access and permission denials (403 Permission Denied or Insufficient Permission) and access control conflicts. Use whenever a user encounters or asks to analyze a 403 error on a bucket or object - including analysis-only questions where no commands are run - or needs help with IAM bindings, fine-grained ACLs
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik

### google-cloud-storage-fuse  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Mounts Cloud Storage buckets on Google Cloud as a POSIX file system with Cloud Storage FUSE (gcsfuse). Use when interacting with gcsfuse or Cloud Storage FUSE mounts: decide whether FUSE, native gs:// reads, or Filestore/Managed Lustre fits a workload, deploy tuned mounts on GKE, Compute Engine, or Cloud Run, enable and size file, stat, and list caches, tune mount flags (--implicit-dirs) or config
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 38 KB (SKILL.md 6.3 KB, yük kucuk)
- **İnceleme:** otomatik

### managed-airflow-dag-authoring  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Provides guidance for authoring Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers environment context discovery, Airflow 2 vs 3 compatibility, authoring best practices, and local/remote validation processes. Use when creating or extending an Airflow DAG. Don't use when authoring Python code unrelated to Airflow DAGs.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** otomatik

### managed-airflow-dag-troubleshooting  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance for troubleshooting Apache Airflow DAGs (failed DAG runs and task instances) in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Use when figuring out reasons for DAG run or task instance failures. Don't use when looking for overall recommendations for Managed Airflow environment performance.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 18 KB (SKILL.md 16.4 KB, yük orta)
- **İnceleme:** otomatik

### managed-airflow-migrations  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSAA Gen 2 and 3) and Airflow 3 (MSAA Gen 3), including environment inspection, GCS download/upload and scanning patterns for breaking changes. Use when migrating the DAG code to newer Airflow version. Don't use when checking DAG run failure
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 26 KB (SKILL.md 12.1 KB, yük orta)
- **İnceleme:** otomatik

### managed-airflow-recommendations  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Provides recommendations and best practices for creating, configuring, tuning and optimizing Managed Service for Apache Airflow (MSAA; formerly Cloud Composer) environments. Use when the user asks for guidance, recommendations, or best practices on configuring Managed Airflow environments, scaling Airflow environments, preventing workload restarts, or analyzing system health. Don't use for trouble
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 46 KB (SKILL.md 9.6 KB, yük orta)
- **İnceleme:** otomatik

### nodejs-best-practices  ·  vudovn/ag-kit @ 549ba3d  ·  puan 74 (B)

- **Ne yapar:** Node.js arka yüz karar ilkeleri: Hono/Fastify/NestJS/Express seçim ağacı, yerel TypeScript ve modül sistemi kararları, katmanlı mimari, merkezi hata işleme, async desenleri, doğrulama ve güvenlik ilkeleri; sabit kod yerine bağlama göre karar vermeyi öğretir.
- **Ne zaman:** Node.js backend kurarken veya framework seçerken; mevcut Node servisinin yapısını gözden geçirirken. · **Ne zaman değil:** Next.js API route'larıyla sınırlı basit işler; ayrıntılı API sözleşmesi tasarımı (api-and-interface-design).
- **Teknoloji:** node, typescript, express, fastify, hono, nestjs
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** node-backend → birincil · **Roller:** backend-muhendis
- **Boyut:** 8 KB (SKILL.md 8.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Güncel seçenekleri (Hono, yerel TS) kapsıyor ve benchmark iddialarında temkinli; ilke düzeyinde, kod örneği az.

### python-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 74 (B)

- **Ne yapar:** Python geliştirme karar ilkeleri: FastAPI/Django/Flask seçim ağacı, async/sync kararı ve kütüphane seçimi, tip ipucu stratejisi ve Pydantic doğrulama, proje yapısı, hata işleme ve test ilkeleri.
- **Ne zaman:** Python backend/servis kurarken veya framework seçerken; tip ipucu ve proje yapısı kararlarında. · **Ne zaman değil:** Veri bilimi/notebook işleri (kapsam dışı); tek dosyalık betikler.
- **Teknoloji:** python, fastapi, django, flask, pydantic
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8225, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** python-gelistirme → birincil · **Roller:** backend-muhendis
- **Boyut:** 9 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve dengeli karar rehberi; ilke düzeyinde, derinlik sınırlı. Backend bağlamında kaldığı için kategorisi 04'te bırakıldı.

### spanner-basics  ·  google/skills @ 4bb21eb  ·  puan 100 (A)

- **Ne yapar:** Assists in provisioning instances and databases, designing performant schemas, and querying data in Cloud Spanner on Google Cloud. Use when designing primary keys, writing SQL queries or client library code, or diagnosing performance issues.
- **Teknoloji:** node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 30 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### spanner-graph-query-tuning  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Tunes and troubleshoots Spanner Graph on Google Cloud ISO GQL queries and execution plans. Use when optimizing slow Spanner Graph GQL queries, diagnosing distributed cross apply versus hash join execution operators and index seek prefixes, eliminating multi-arm star query Cartesian products with chained query aggregation, bounding super-node fan-out, decorrelating slow subqueries or optional match
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 48 KB (SKILL.md 22.2 KB, yük orta)
- **İnceleme:** otomatik

### spanner-graph-schema-best-practices  ·  google/skills @ 4bb21eb  ·  puan 95 (A)

- **Ne yapar:** Designs, reviews, and optimizes physical table schemas, indexes, and graph topologies for Spanner Graph on Google Cloud. Use when creating a new Spanner Graph schema, selecting node and edge primary key types, optimizing forward, reverse, or per-node Top-K edge traversals, designing interleaved node or edge tables and covering indexes, configuring cascading deletes and row deletion policies (TTL),
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 64 KB (SKILL.md 30.2 KB, yük buyuk)
- **İnceleme:** otomatik

### spanner-relational-to-graph  ·  google/skills @ 4bb21eb  ·  puan 98 (A)

- **Ne yapar:** Analyzes existing Spanner relational schemas on Google Cloud (DDL, foreign keys, interleaved tables, and junction tables) and generates `CREATE PROPERTY GRAPH` DDL statements (`NODE TABLES`, `EDGE TABLES`) without modifying underlying relational tables. Use when mapping existing Spanner tables to a Spanner Graph, identifying node and edge candidates from relational tables, creating SQL bridge view
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** google (kurum, ★24613, son güncelleme 2026-11-24, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 75 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** otomatik
