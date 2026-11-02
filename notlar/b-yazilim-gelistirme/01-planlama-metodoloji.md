# 01-planlama-metodoloji — Yazılım Geliştirme

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **15/40**

### app-builder  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in uygulama kurma orkestratörü: doğal dil isteğinden proje tipini tespit eder, 2026 varsayılan teknoloji yığınını (Next.js 16, Tailwind v4, Prisma/Drizzle, Auth.js) seçer, klasör iskeletini kurar ve planlayıcı/frontend/backend/veritabanı agent'larını sıraya koyar. 13 proje şablonunu (Next.js SaaS, FastAPI, Expo, Flutter, Electron, Chrome eklentisi, CLI, Turborepo…) alt klasörde taşır.
- **Ne zaman:** Sıfırdan full-stack uygulama başlatırken yığın seçimi ve iskelet kurulumu; hangi şablonun uygun olduğuna hızlı karar. · **Ne zaman değil:** Var olan kod tabanında özellik ekleme (writing-plans + incremental-implementation); ag-kit agent'ları (project-planner, frontend-specialist…) ve /create iş akışı projede yoksa orkestrasyon kısmı boşa düşer.
- **Teknoloji:** next.js, react, node, python, vue, flutter, react-native
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** proje-iskeleti → birincil
- **Boyut:** 63 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (yığın/şablon rehberi olarak). Şablonlar güncel (2026-05 sürümleri) ve seçici okuma kuralı bağlamı korur. Ancak agent koordinasyon bölümü ag-kit'in kendi agent'larına ve /create iş akışına bağlı; kütüphanede bu agent'lar yok. templates/ alt klasörü ayrı 'templates' skill'iyle birebir aynı.

### architecture@anthropics  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** alternatif · **Örtüşme:** mimari-karar → tamamlayıcı
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik
- **Not:** ADR (mimari karar kaydı) yazma/değerlendirme; vudovn architecture ile tamamlayıcı.

### brainstorming  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** superpowers'ın tasarım öncesi skili: uygulamaya geçmeden önce sırayla yaklaşımları ayrı bir mesajda sunup birini seçtirmek, kısa ya da tam tasarım dokümanı yazmak, onay almak ve writing-plans'a geçmek. Var olan projede önce okuyup sonra sorar ('Look Before You Ask').
- **Ne zaman:** Yeni özellik, bileşen veya proje fikrinde gereksinim belirsizken; kodlamaya başlamadan önce ortak anlayış ve yazılı tasarım gerektiğinde. · **Ne zaman değil:** İstekte her şey açıksa (küçük, net görev); etkileşimsiz ortamlar (CI, zamanlanmış çalışma). Hızlı niyet doğrulaması yeterliyse interview-me daha hafif.
- **Teknoloji:** node, html · **Paketler:** node (görsel yardımcı sunucusu, isteğe bağlı)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → birincil · **Roller:** planlayici
- **Boyut:** 76 KB (SKILL.md 13.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi: zorunlu sıra (yaklaşımlar → tasarım dokümanı → onay → writing-plans) açık hâle geldi; soru sormadan önce projeyi/bağlamı okuma kuralı eklendi; spike ve 'soruları atla' istisnaları netleşti.

### brainstorming@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in Sokratik soru protokolü: belirsiz isteklerde kodlamadan önce en az 3 soru (amaç, kullanıcı, kapsam) sorar, soruları seçenek/artı-eksi tablosuyla biçimlendirir; ilerleme panosu, hata iletişimi ve tamamlanma mesajı kalıplarını da içerir. .agents/memory klasörünü okur.
- **Ne zaman:** ag-kit iş akışı kullanan projelerde; seçenek tablolu, karar odaklı soru listesi tercih edildiğinde. · **Ne zaman değil:** Genel kullanımda (obra brainstorming daha doğal ve olgun); aynı adı taşıdığı için birincille birlikte kurulamaz.
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** fikir-netlestirme → alternatif
- **Boyut:** 17 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Soru biçimi (öncelik + seçenek tablosu + varsayılan) yararlı ama 'her zaman 3 soru' kuralı küçük işlerde sürtünme yaratıyor; ag-kit'e özgü /remember ve .agents/memory varsayımları var.

### code-review  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### constraint-driven-development  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Projenin kalite çıtasını CONSTRAINTS.md'de yazılı sözleşmeye çevirir: hangi boyutların önemli olduğunu sorar, sayı yoksa makul varsayılan eşikler önerir, gereken araçları kurdurur ve diff'te çıtanın sessizce düşürülmesini (yeni @ts-ignore/eslint-disable, atlanan/silinen test, kaldırılan assertion, eşik düşürme) yakalar. Semgrep/axe çıktısını eşiğe göre zorlayan yerel bir betik (quality-gate.mjs) ve 'her komut gerçekten başarısız oluyor mu' doğrulaması içerir.
- **Ne zaman:** Yazılı kalite çıtası yoksa; agent testleri atlayıp/susturup yeşile ulaşmaya çalışıyorsa; erişilebilirlik, performans veya kapsama eşiği tanımlanacaksa. · **Ne zaman değil:** Kısa ömürlü prototip/spike; zaten CI'da zorlanan, belgelenmiş standartları olan ekip.
- **Teknoloji:** git, node, python
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kalite-sozlesmesi → birincil · **Roller:** kod-inceleyici · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 34 KB (SKILL.md 21.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Agent'ların çıtayı düşürme davranışına özel tek skill; varsayılan eşik tablosu ve floor-guard referansı pratik. 2026-11: semgrep/axe'in bulguda 0 ile çıkması sorunu quality-gate.mjs ile çözüldü; kasıtlı ihlalle doğrulama adımı eklendi. SKILL.md ~21,7 KB.

### debug  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### deploy-checklist  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### documentation  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.5 KB, yük kucuk)
- **İnceleme:** otomatik

### doubt-driven-development  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Önemsiz olmayan her kararı (iddia → en küçük incelenebilir birim → taze bağlamlı karşıt inceleme → uzlaştırma → dur) döngüsünden geçirir; gerekirse Codex veya Gemini CLI ile çapraz model incelemesi yaptırır. Ana oturum orkestratörü için tasarlanmıştır.
- **Ne zaman:** Yüksek riskli işler (üretim kimlik doğrulama, güvenlik, geri alınamaz migrasyon), tanıdık olmayan kod, planın gizli hata modlarının sınanması. · **Ne zaman değil:** Alt-agent/persona içinde (iç içe agent çağıramaz); hızın önemli olduğu düşük riskli işler.
- **Teknoloji:** api-anahtari _(otomatik tespit)_ · **Paketler:** isteğe bağlı: codex CLI veya gemini CLI (çapraz model inceleme)
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** karsit-dogrulama → birincil · **Roller:** planlayici · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 16 KB (SKILL.md 16.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, opsiyonel. Sınırlı döngü ve 'iç içe çalışamaz' uyarısı iyi düşünülmüş. Maliyetli (her kararda ek agent); yalnız planlayıcı/orkestratör rolüne uygun, persona skill listesine konmamalı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### executing-plans  ·  obra/superpowers @ 2ce8aa1  ·  puan 97 (A)

- **Ne yapar:** Yazılmış bir planı alt-agent kullanmadan, aynı oturumda görev görev uygular: her görev için brief ve kayıt defteri (ledger) tutar, TDD ile ilerler, plan sorunlarında 'karar' kaydı düşerek durmadan devam eder, sonunda tek bir taze bağlamlı inceleme yaptırıp finishing-a-development-branch'e geçer. task-start/task-done betikleri içerir.
- **Ne zaman:** writing-plans planı hazır ve kullanıcı satır içi yürütmeyi seçtiyse; alt-agent aracı olmayan ortamlarda (ör. bazı Codex kurulumları). · **Ne zaman değil:** Her görevde ayrı inceleme kapısı isteniyorsa veya plan çok uzunsa (subagent-driven-development); planı olmayan işler.
- **Teknoloji:** git · **Paketler:** bash (task-start/task-done betikleri)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** plan-yurutme → birincil · **Roller:** planlayici
- **Boyut:** 20 KB (SKILL.md 17.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — 2026-10 güncellemesi: uzun örnek iş akışı çıkarıldı, kurallar aynı; SKILL.md kısaldı. Alt-agent kullanmadan aynı oturumda plan yürütme için hâlâ geçerli.

### idea-refine  ·  addyosmani/agent-skills @ 301b02b  ·  puan 95 (A)

- **Ne yapar:** Ham fikirleri ıraksak (genişlet) ve yakınsak (değerlendir, daralt) düşünme aşamalarıyla keskin bir konsepte çevirir; sonuçta problem tanımı, önerilen yön, doğrulanacak varsayımlar, MVP kapsamı ve 'yapmayacaklarımız' içeren bir belge (docs/ideas/) üretir.
- **Ne zaman:** Ürün/özellik fikri henüz bulanıkken, seçenekleri açıp sonra birine indirmek ya da bir planın varsayımlarını sınamak istendiğinde. · **Ne zaman değil:** Ne yapılacağı belli, yalnız gereksinim ayrıntısı eksikse (brainstorming / interview-me); kod düzeyi planlama (writing-plans).
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 40 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, alternatif. Çerçeveler (frameworks.md) ve örnekler iyi; ürün/konsept aşamasında brainstorming'den daha yapılandırılmış. Betik yalnız docs/ideas klasörü açıyor. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### incident-response  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 5.5 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### incremental-implementation  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Değişiklikleri ince, doğrulanabilir dilimlerle teslim ettirir: dikey/sözleşme-önce/risk-önce dilimleme, 'önce sadelik' ve kapsam disiplini, her adımda derlenebilir kalma, yarım özellikleri feature flag arkasına alma, güvenli varsayılanlar ve geri alınabilirlik kuralları.
- **Ne zaman:** Birden çok dosyaya dokunan her özellik/değişiklikte; plandan sıradaki görevi alırken; büyük kod bloğu yazma eğilimi olduğunda. · **Ne zaman değil:** Tek satırlık düzeltmeler; planın kendisini yazmak (writing-plans).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** plan-yurutme → tamamlayıcı · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 9 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tamamlayıcı. Kısa (9 KB), yığından bağımsız; 'Rule 0.5 kapsam disiplini' agent'ların taşmasını iyi engelliyor. ../../references/definition-of-done.md arşivde yok (yalnız 'ayrıca bkz').

### interview-me  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Kullanıcının gerçekte ne istediğini (yapması gerektiğini düşündüğü şeyi değil) bulmak için tek soruluk turlarla ~%95 güvene kadar görüşme yapar; her soruya bir tahmin ekler, niyeti kullanıcının kendi sözleriyle özetleyip açık onay ister ve durur.
- **Ne zaman:** İstek 'kimin için / neden şimdi' bilgisi olmadan geldiğinde; kullanıcı 'beni sorgula', 'emin miyiz?' dediğinde; plan veya spec yazılmadan önce kısa niyet doğrulaması. · **Ne zaman değil:** Etkileşimsiz bağlamlar (CI, /loop); gereksinim zaten netse; tam tasarım belgesi gerekiyorsa (brainstorming).
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → tamamlayıcı · **Roller:** planlayici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 15 KB (SKILL.md 14.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tamamlayıcı. Net durma kuralı ve 'istek vs. olması gereken' ayrımı brainstorming'den farklı bir boşluğu dolduruyor; kısa ve yan etkisiz.

### karpathy-guidelines  ·  multica-ai/andrej-karpathy-skills @ 2c60614  ·  puan 73 (B)

- **Ne yapar:** Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** multica-ai (kurum, ★228018, son güncelleme 2026-04-20, lisans yok)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** otomatik

### math-olympiad  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 100 (A)

- **Ne yapar:** Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked to 'solve this IMO problem', 'prove this olympiad inequality', 'verify this competition proof', 'find a counterexample', 'is this proof correct', or for any problem with 'IMO', 'Putnam', 'USAMO', 'olympiad', or 'competition math' in it. Use
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 62 KB (SKILL.md 19.5 KB, yük orta)
- **İnceleme:** otomatik

### plan-writing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in kısa plan yazma rehberi (obra/superpowers'tan uyarlanmış): 5-10 görevlik, her görevin doğrulaması belli, bir sayfayı geçmeyen planı proje kökünde {görev-adı}.md olarak yazdırır; proje tipine göre ag-kit doğrulama betiklerini önerir.
- **Ne zaman:** ag-kit kullanan projelerde veya çok kısa, tek sayfalık plan yeterliyse. · **Ne zaman değil:** Alt-agent'lara devredilecek ayrıntılı plan gerektiğinde (writing-plans); ag-kit betikleri (ux_audit.py, security_scan.py…) projede yoksa betik önerileri boşa düşer.
- **Teknoloji:** node, python, react, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → alternatif
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısalık ilkesi iyi ama içerik writing-plans'ın sadeleştirilmiş türevi; plan dosyasını proje köküne yazma kuralı ve var olmayan ag-kit betiklerine atıf zayıflık.

### planning-and-task-breakdown  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Spec'i bağımlılık grafiği çıkarıp dikey dilimlere bölerek sıralı, boyutlandırılmış görevlere çevirir; her görev için kabul ölçütü ve doğrulama, fazlar arası kontrol noktaları, riskler ve paralelleştirme fırsatları içeren plan şablonu verir.
- **Ne zaman:** Spec hazır, iş büyük ve dilimlenmesi gerekiyorsa; tahmin/kapsam çıkarma veya paralel iş fırsatı aranırken; superpowers zinciri kullanılmayan projelerde. · **Ne zaman değil:** writing-plans kurulu bir rolde ikinci plan skilli olarak (aynı iş); tek adımlık işler.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → alternatif · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İyi yapılandırılmış ve kısa; dikey dilim ve kontrol noktası anlatımı güçlü. writing-plans'tan daha az ayrıntılı (arayüz sözleşmesi, TDD adımları yok), bu yüzden alternatif. ../../references/ bağlantıları arşivde yok (yalnız 'ayrıca bkz').

### replica-architect  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Plans the stack, database schema and API for an app clone, from the recon map replica-recon wrote. Picks boring, managed tech, turns the inferred data model into real SQL with indexes and access rules, lists every route by flow, and orders the build as a thin vertical slice first. Use when the user says "plan the clone", "what stack should I use", "design the database", "write the schema", "plan t
- **Teknoloji:** api-anahtari, css, next.js, react, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-backend  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Builds the backend of an app clone: auth, database migrations and access rules, payments with Stripe, email, background jobs and third-party integrations through official APIs only, plus a security checklist. Use when the user says "add login", "set up auth", "wire up the database", "add payments", "connect Stripe", "add Google Calendar", "send emails", "backend for my clone", or when /replica-bui
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-brand  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Names and rebrands an app clone so it is the user's own: name candidates with the trademark, domain, store and handle checks to run, a new palette checked for contrast, a logo brief, a voice guide, and a sweep tool that finds anything of the original left in the codebase. Use when the user says "name my app", "rebrand the clone", "make it mine", "pick a name and colours", "logo brief", "brand voic
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-build  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Rebuilds an app screen by screen from the recon map: app shell first, then the core flow as a vertical slice, then every screen with all its states, ticking off the feature matrix as it goes. Writes every line fresh, never the original's code, assets or copy. Use when the user says "build the clone", "build screen S07", "start building", "rebuild this screen", "implement the booking page", or afte
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-deploy  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Ships an app clone live on the user's own domain: a preflight gate (tests green, parity must-haves done, rebrand sweep clean, listing linted, legal pages up), production database and env vars, the host, DNS records for the domain and for email, Stripe live mode, OAuth redirects, monitoring, and mobile builds to TestFlight and Play. Use when the user says "deploy it", "ship it", "put it live", "con
- **Teknoloji:** next.js, node, playwright, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-design  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Rebuilds an app's design system for a clone: colour roles, type scale, spacing, radius, shadows and every component with its states, as design tokens plus component specs, with original assets instead of the target's logos, icons, illustrations or licensed fonts. Includes a WCAG contrast checker. Use when the user says "match the design", "rebuild the design system", "get the colours and fonts", "
- **Teknoloji:** api-anahtari, css, python, react, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-diff  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Compares an app clone against the original: a feature parity score from the feature matrix (weighted by must, should, could) with the missing list in build order, plus a screenshot layout diff that ignores colour so a rebrand does not count against you. Two standard-library Python tools. Use when the user says "how close is my clone", "compare it to the original", "what's missing", "parity check",
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-entrepreneur  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Researches the app being cloned and reads what its real users say in public reviews (App Store, Google Play, G2, Capterra, Trustpilot, Reddit, Hacker News, its own feature-request board), then ranks what they hate, what is missing and what is unsolved, turns it into a fix plan for the clone and a positioning angle you can sell. Every quote is real, verbatim and linked. Use when the user says "what
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-launch  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Writes the launch for an app clone: the landing page built on the positioning angle, pricing set against the original's public pricing and its users' complaints, and the App Store and Google Play listing linted against the stores' limits and copycat rules. Use when the user says "landing page", "pricing", "how much should I charge", "App Store listing", "store screenshots", "launch plan", "Product
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-recon  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Reverse-engineers any app into a recon map: screen inventory, user flows, component list, inferred data model and a feature matrix, from public pages, screenshots, app store listings, help docs and the user's own account. The first step of the Replica pack. Use when the user says "clone this app", "reverse engineer X", "how does X work", "map out X", "what screens does X have", "I want to build my
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 5.4 KB, yük kucuk)
- **İnceleme:** otomatik

### replica-test  ·  Jakeschincariol/replica-skill @ 77c9436  ·  puan 85 (A)

- **Ne yapar:** Clicks through every flow of an app clone and tests it for bugs: a test plan generated from the recon flows with happy paths and edge cases, Playwright end-to-end tests where possible, a browser click-through where not, and bug reports in a fixed format with severity, steps and evidence. Use when the user says "test my clone", "find bugs", "QA this", "click through everything", "write e2e tests", 
- **Teknoloji:** css, node, playwright, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Jakeschincariol (kisi, ★6998, son güncelleme 2026-10-03, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.2 KB, yük kucuk)
- **İnceleme:** otomatik

### siege  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 92 (A)

- **Ne yapar:** Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, independent workers answer them, and the judge keeps a ledger of what is proved, refuted and open, until the judge concludes or the rounds run out, and then a proof.md says plainly what is and is not proved. A run takes hours and dozens of worker runs. Usage: /math-proof:siege [NAME=value sett
- **Teknoloji:** api-anahtari, python _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, disallowed-tools (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 104 KB (SKILL.md 73.7 KB, yük buyuk)
- **İnceleme:** otomatik

### solo  ·  anthropics/claude-plugins-official @ a7ba5b9  ·  puan 97 (A)

- **Ne yapar:** Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in a notes file so that nothing written is lost if a response is cut off, and end with a self-contained proof.md. Usage: /math-proof:solo <the problem, stated in full, or the path of a file holding it>.
- **Teknoloji:** api-anahtari _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint, disable-model-invocation, disallowed-tools (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★45728, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** otomatik

### source-driven-development  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Her uygulama kararını resmî dokümantasyona dayandırır: yığını ve sürümleri tespit eder, resmî belgeyi çeker (çekilen içeriği talimat değil veri sayar), belgelenmiş kalıpla uygular ve kaynakları kodda/yanıtta alıntılar.
- **Ne zaman:** Framework/kütüphane sürümüne duyarlı işler; güncelliğini yitirmiş kalıp riski olan hızlı değişen API'ler (Next.js, React 19, Tailwind v4…). · **Ne zaman değil:** İnternet erişimi yoksa; saf algoritma/iş mantığı değişiklikleri.
- **Teknoloji:** api-anahtari, css, html, next.js, node, python, react, svelte, tailwind, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** resmi-dokuman-dayanagi → birincil · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 10 KB (SKILL.md 9.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa ve yığından bağımsız; 'çekilen içeriği veri say' güvenlik notu değerli. Model bilgisinin eskidiği framework işlerinde frontend rolüne iyi bir tamamlayıcı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### spec-driven-development  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Kodlamadan önce spec yazdırır: kapsam kontrolü (gerekirse yetenek haritasına bölme), amaç/yığın/komutlar/yapı/test stratejisi/sınırlar/başarı ölçütü içeren spec, ardından plan, görevler ve uygulama aşamalarını kapılı bir akışla yürütür; spec'i canlı tutma kurallarını verir.
- **Ne zaman:** Yeni proje/özellik başlarken spec veya PRD yoksa; tek bir isteğin birden çok bağımsız yeteneğe bölünmesi gerektiğinde. · **Ne zaman değil:** Küçük, net değişiklikler; gereksinim hâlâ belirsizse önce brainstorming/interview-me.
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** spec-yazimi → birincil · **Roller:** planlayici · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, birincil (spec yazımı). superpowers'ta brainstorming'in ürettiği tasarım belgesine karşılık gelir ama daha yapılandırılmış şablon ve 'spec'i canlı tut' kuralları sunar; writing-plans ile birlikte kullanılır. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### standup  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, formatting work into yesterday/today/blockers, or structuring a few rough notes into a shareable update.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.2 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### system-design  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### tech-debt  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk)
- **İnceleme:** otomatik

### templates  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** 13 proje iskelet şablonunun (Next.js fullstack/SaaS/static, Nuxt, Express, FastAPI, Expo, Flutter, Electron, Chrome MV3, CLI, Turborepo, Astro) dizini; her şablon yığın, sürüm ve klasör yapısını verir.
- **Ne zaman:** Sadece şablon dosyaları istenip app-builder'ın orkestrasyon kısmı istenmediğinde. · **Ne zaman değil:** app-builder kuruluysa (aynı dosyaları templates/ altında zaten taşıyor); adı genel olduğundan başka 'templates' skilleriyle çakışabilir.
- **Teknoloji:** next.js, react, node, python, vue, flutter, react-native
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** proje-iskeleti → alternatif
- **Boyut:** 43 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV / ALTERNATİF. İçerik app-builder/templates ile birebir aynı (diff: yalnız KAYNAK.md farkı); ayrı kurulması yinelenen bağlam. Durum alternatife çekildi.

### testing-strategy  ·  anthropics/knowledge-work-plugins @ 2574e29  ·  puan 100 (A)

- **Ne yapar:** Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★34376, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik

### writing-plans  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Spec'ten, kod tabanını hiç görmemiş bir mühendisin uygulayabileceği ayrıntılı uygulama planı yazdırır: dosya yapısı, her görev için dosyalar, arayüz imzaları (üretir/tüketir), TDD adımları (başarısız test → minimum kod → geçen test → commit), global kısıtlar ve inceleme odağı. Plan subagent-driven-development veya executing-plans'a devredilir.
- **Ne zaman:** Çok adımlı bir iş için spec/gereksinim hazırsa, koda dokunmadan önce; alt-agent'lara dağıtılacak görevler gerektiğinde. · **Ne zaman değil:** Tek dosyalık küçük düzeltmeler; spec henüz yoksa (önce brainstorming/spec-driven-development).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → birincil · **Roller:** planlayici
- **Boyut:** 10 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, uygulama-plani grubunun birincili. Gerekçe: arayüz sözleşmeleri, görev boyutlandırma ve 'inceleme odağı' bölümüyle en uygulanabilir plan biçimi; superpowers yürütme zinciriyle (subagent-driven-development, executing-plans, TDD, verification) uçtan uca bağlı. addyosmani planning-and-task-breakdown daha hafif ve yığından bağımsız; vudovn plan-writing kısa ama ag-kit betiklerine atıf yapıyor.
