# 06-devops-guvenlik-performans — Yazılım Geliştirme

_CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **10/10**

### ci-cd-and-automation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 87 (A)

- **Ne yapar:** CI/CD hattı kurulumu: kalite kapısı sırası (lint → tip → birim → build → entegrasyon → E2E → güvenlik), GitHub Actions örnekleri (veritabanlı entegrasyon ve E2E dahil), CI hatalarını agent'a geri besleme, preview deploy, feature flag, kademeli yayın ve geri alma planı, ortam yönetimi, Dependabot/Renovate ve CI hızlandırma.
- **Ne zaman:** Build/deploy hattı kurarken veya değiştirirken; kalite kapılarını otomatikleştirirken; test çalıştırıcısını CI'a bağlarken. · **Ne zaman değil:** GitHub Actions dışı CI'da örnekler doğrudan uymaz (ilkeler geçerli); tek seferlik yerel betikler.
- **Teknoloji:** github-actions, node, playwright
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109322, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ci-cd → birincil · **Roller:** devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, ci-cd grubunun birincili. Pratik YAML örnekleri ve 'CI hatasını agent'a besle' bölümü agent iş akışına özgü bir artı.

### deployment-procedures  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Üretim deploy ilkeleri: platform seçim ağacı (Vercel/Netlify, Railway/Render/Fly, VPS+PM2/Docker, Kubernetes, serverless), deploy öncesi dört doğrulama kategorisi, beş fazlı deploy akışı, deploy sonrası doğrulama penceresi ve geri alma ilkeleri; betik değil karar öğretir.
- **Ne zaman:** Barındırma platformu seçerken veya deploy prosedürü yazarken; ag-kit /deploy iş akışında. · **Ne zaman değil:** Kademeli yayın ve izleme ayrıntısı (shipping-and-launch); CI hattı yazımı (ci-cd-and-automation).
- **Teknoloji:** docker, git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** deploy-yayin → tamamlayıcı · **Roller:** devops-muhendis
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. Kısa (6 KB) platform karar tablosu yararlı; içerik genel ilkeler, shipping-and-launch ile kısmen örtüşüyor.

### observability-and-instrumentation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 87 (A)

- **Ne yapar:** Kodu üretimde görünür ve teşhis edilebilir kılar: önce 'çalışıyor'un tanımı, her soru için doğru sinyal (log, metrik, iz), yapılandırılmış loglama, metrikler, dağıtık izleme, uyarılar ve runbook yazımı, son olarak telemetrinin kendisini doğrulama.
- **Ne zaman:** Loglama/metrik/izleme/uyarı eklerken; üretime çıkan her özellikte çalıştığına dair kanıt gerektiğinde; üretim sorunu mevcut veriden anlaşılamıyorsa. · **Ne zaman değil:** Yerel prototip; belirli bir APM ürününün kurulumu (ürün belgeleri).
- **Teknoloji:** opentelemetry, node, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109322, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** gozlemlenebilirlik → birincil · **Roller:** backend-muhendis, devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 14 KB (SKILL.md 13.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, gozlemlenebilirlik grubunun birincili. 'Telemetriyi de doğrula' ve runbook bölümleri pratik; satıcıdan bağımsız.

### performance-optimization  ·  addyosmani/agent-skills @ aeac41d  ·  puan 87 (A)

- **Ne yapar:** Ölçüme dayalı performans iyileştirme: Core Web Vitals hedefleri, önce ölç → darboğazı bul → düzelt → doğrula (tut ya da geri al, geri alınan denemeleri de kaydet) → regresyona karşı koru akışı; ön yüz, arka yüz, sorgu ve veritabanı için nereden ölçmeye başlanacağı ve optimization-patterns.md desen dosyası.
- **Ne zaman:** Performans gereksinimi veya regresyon şüphesi olduğunda; Core Web Vitals/yükleme süresi iyileştirmede; N+1 sorgu düzeltmede; profil çıkarılmış darboğazlarda. · **Ne zaman değil:** Ölçüm yapılmadan 'erken optimizasyon'; React'e özgü kural listesi gerekiyorsa vercel-react-best-practices ile birlikte.
- **Teknoloji:** node, react, css
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109322, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** performans → birincil · **Roller:** devops-muhendis, kod-inceleyici, qa-erisilebilirlik · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 26 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, performans grubunun birincili. Gerekçe: 'tut ya da geri al' ve 'geri alınan denemeyi de kaydet' disiplini ölçümsüz optimizasyonu engelliyor; tüm katmanları kapsıyor. performance-profiling Lighthouse/bundle betikleriyle tamamlayıcı.

### performance-profiling  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Performans profil çıkarma ilkeleri: Core Web Vitals hedefleri, taban → tespit → düzelt → doğrula süreci, sorun tipine göre araç seçimi (Lighthouse, bundle analyzer, DevTools Performance/Memory/Network), bundle ve çalışma zamanı analizi, yaygın darboğazlar; lighthouse_audit.py ve bundle_analyzer.py betikleri.
- **Ne zaman:** Lighthouse denetimi çalıştırmak, bundle boyutunu analiz etmek veya DevTools ile çalışma zamanı profili çıkarmak gerektiğinde. · **Ne zaman değil:** Optimizasyon kararı ve doğrulama disiplini (performance-optimization); backend/veritabanı darboğazları (sınırlı içerik).
- **Teknoloji:** lighthouse, python, node · **Paketler:** python3, lighthouse (npx)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** performans → tamamlayıcı
- **Boyut:** 13 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı (opsiyonel). Kısa ve betikli; içerik büyük ölçüde performance-optimization'ın ölçüm bölümünün tablo özeti.

### red-team-tactics  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** MITRE ATT&CK tabanlı kırmızı takım ilkeleri: saldırı yaşam döngüsü fazları ve amaçları, pasif/aktif keşif, ilk erişim vektörleri, Windows/Linux yetki yükseltme ilkeleri, tespitten kaçınma ve operasyonel güvenlik, raporlama. İlke düzeyinde; exploit kodu içermez.
- **Ne zaman:** Yalnız yetkili sızma testi veya kırmızı takım tatbikatında saldırı yüzeyini çerçevelemek ve rapor yapısı kurmak. · **Ne zaman değil:** Yetkisiz hedefler; uygulama geliştirme rolleri (savunma tarafı için security-and-hardening).
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** saldiri-simulasyonu → birincil
- **Boyut:** 4 KB (SKILL.md 4.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Çift kullanımlı (tespitten kaçınma bölümü var) ve yüzeysel; web uygulaması projelerinde savunmaya katkısı düşük. Hiçbir role eklenmedi.

### security-and-hardening  ·  addyosmani/agent-skills @ aeac41d  ·  puan 95 (A)

- **Ne yapar:** Kodu güvenlik açıklarına karşı sertleştirir: önce tehdit modeli, 'her zaman yap / önce sor / asla yapma' üç katmanlı sınır sistemi; enjeksiyon, XSS, erişim kontrolü, kimlik doğrulama ve oturum, başlıklar/CORS, girdi doğrulama ve yüklemeler, SSRF, türetilmiş yollarda yıkıcı işlemler, rate limit, gizli anahtarlar, bağımlılık ve tedarik zinciri, kişisel veri ve AI/LLM özellikleri için kontroller; inceleme kontrol listesi ve hardening-patterns.md.
- **Ne zaman:** Kullanıcı girdisi, kimlik doğrulama, veri saklama veya dış entegrasyon içeren her özellikte; OWASP Top 10'a karşı giriş akışı denetimi; bağımlılık denetimi. · **Ne zaman değil:** Saldırı simülasyonu/sızma testi (red-team-tactics); otomatik tarama betiği gerektiğinde vulnerability-scanner ile birlikte.
- **Teknoloji:** node, html
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109322, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guvenlik-sertlestirme → birincil · **Roller:** backend-muhendis, devops-muhendis, kod-inceleyici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 30 KB (SKILL.md 17.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, guvenlik-sertlestirme grubunun birincili. Gerekçe: tehdit modeli öncelikli, SSRF ve 'türetilmiş yolda silme' gibi agent'a özgü riskleri ve AI/LLM özelliklerini kapsıyor; 'önce sor' katmanı insan onayı gereken işlemleri net ayırıyor. vulnerability-scanner betikli tarama ile tamamlayıcı.

### server-management  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** Sunucu işletim ilkeleri: süreç yöneticisi seçimi (PM2, systemd, Docker, Kubernetes), izleme metrikleri ve uyarı seviyeleri, izleme aracı seçimi, log yönetimi (rotasyon, yapılandırılmış log), ölçekleme kararları ve sağlık kontrolü ilkeleri.
- **Ne zaman:** VPS/kendi sunucusunda çalışan uygulamalarda PM2/systemd yapılandırması, izleme ve ölçekleme kararları. · **Ne zaman değil:** Yönetilen platformlar (Vercel, Railway) — çoğu konu platformca çözülür; ayrıntılı gözlemlenebilirlik (observability-and-instrumentation).
- **Teknoloji:** pm2, systemd, docker, node
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** sunucu-yonetimi → birincil
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: TUT (opsiyonel). Yalnız tablo düzeyinde ilkeler; komut veya yapılandırma örneği yok, modelin zaten bildiğini özetliyor.

### shipping-and-launch  ·  addyosmani/agent-skills @ aeac41d  ·  puan 87 (A)

- **Ne yapar:** Üretime çıkış hazırlığı: kod kalitesi, güvenlik, performans, erişilebilirlik, altyapı ve dokümantasyon için ön yayın kontrol listesi; feature flag stratejisi, eşik değerli kademeli yayın sırası ve geri alma koşulları, izlenecek metrikler ve hata raporlama, yayın sonrası doğrulama, hata bütçesi kapısı ve geri alma planı şablonu.
- **Ne zaman:** Üretime deploy öncesi 'neler hazır olmalı?' sorusunda; kademeli yayın ve geri alma stratejisi planlarken. · **Ne zaman değil:** Platforma özgü deploy komutları (deployment-procedures veya platform belgeleri); CI kurulumu (ci-cd-and-automation).
- **Teknoloji:** git, node, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109322, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** deploy-yayin → birincil · **Roller:** devops-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, deploy-yayin grubunun birincili. Gerekçe: somut eşikli kademeli yayın ve hata bütçesi kapısı; deployment-procedures (vudovn) platform seçimi ve deploy fazlarıyla tamamlayıcı.

### vulnerability-scanner  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Güvenlik açığı analizi ilkeleri: varsayılan ihlal, sıfır güven, derinlemesine savunma; OWASP Top 10:2025 (yeni A03 tedarik zinciri), saldırı yüzeyi haritalama ve risk önceliklendirme; checklists.md ile OWASP/kimlik doğrulama/API/veri koruma kontrol listeleri, security_scan.py ve dependency_analyzer.py tarama betikleri.
- **Ne zaman:** Projede güvenlik taraması, OWASP 2025 uyum kontrolü veya tedarik zinciri (bağımlılık) analizi yaparken. · **Ne zaman değil:** Özellik geliştirirken güvenli kodlama kuralları (security-and-hardening); gerçek bir SAST/DAST aracının yerine (betikler basit desen taraması).
- **Teknoloji:** python · **Paketler:** python3 (security_scan.py, dependency_analyzer.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8203, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** guvenlik-sertlestirme → tamamlayıcı · **Roller:** devops-muhendis
- **Boyut:** 35 KB (SKILL.md 7.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. OWASP 2025 güncel ve kontrol listeleri iş görüyor; betikler hafif desen taraması, gerçek tarayıcıların (npm audit, semgrep, osv-scanner) yerini tutmaz.
