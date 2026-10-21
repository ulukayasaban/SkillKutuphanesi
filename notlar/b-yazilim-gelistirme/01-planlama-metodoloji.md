# 01-planlama-metodoloji — Yazılım Geliştirme

_Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **15/15**

### app-builder  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** ag-kit'in uygulama kurma orkestratörü: doğal dil isteğinden proje tipini tespit eder, 2026 varsayılan teknoloji yığınını (Next.js 16, Tailwind v4, Prisma/Drizzle, Auth.js) seçer, klasör iskeletini kurar ve planlayıcı/frontend/backend/veritabanı agent'larını sıraya koyar. 13 proje şablonunu (Next.js SaaS, FastAPI, Expo, Flutter, Electron, Chrome eklentisi, CLI, Turborepo…) alt klasörde taşır.
- **Ne zaman:** Sıfırdan full-stack uygulama başlatırken yığın seçimi ve iskelet kurulumu; hangi şablonun uygun olduğuna hızlı karar. · **Ne zaman değil:** Var olan kod tabanında özellik ekleme (writing-plans + incremental-implementation); ag-kit agent'ları (project-planner, frontend-specialist…) ve /create iş akışı projede yoksa orkestrasyon kısmı boşa düşer.
- **Teknoloji:** next.js, react, node, python, vue, flutter, react-native
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** proje-iskeleti → birincil · **Roller:** planlayici
- **Boyut:** 63 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (yığın/şablon rehberi olarak). Şablonlar güncel (2026-05 sürümleri) ve seçici okuma kuralı bağlamı korur. Ancak agent koordinasyon bölümü ag-kit'in kendi agent'larına ve /create iş akışına bağlı; kütüphanede bu agent'lar yok. templates/ alt klasörü ayrı 'templates' skill'iyle birebir aynı.

### brainstorming  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** superpowers'ın tasarım öncesi sohbet skilli: kullanıcının ne istediğini ve nedenini tek seferde tek soruyla açar, gerektiğinde kodu/web'i keşfetmeyi ve tarayıcıda çalışan görsel yardımcıyla (yerel Node sunucusu) maket göstermeyi önerir, sonra yazılı tasarım belgesi üretip writing-plans'a devreder.
- **Ne zaman:** Yeni özellik, bileşen veya proje fikrinde gereksinim belirsizken; kodlamaya başlamadan önce ortak anlayış ve yazılı tasarım gerektiğinde. · **Ne zaman değil:** İstekte her şey açıksa (küçük, net görev); etkileşimsiz ortamlar (CI, zamanlanmış çalışma). Hızlı niyet doğrulaması yeterliyse interview-me daha hafif.
- **Teknoloji:** node, html · **Paketler:** node (görsel yardımcı sunucusu, isteğe bağlı)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → birincil · **Roller:** planlayici
- **Boyut:** 72 KB (SKILL.md 9.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, fikir-netlestirme grubunun birincili. Gerekçe: en olgun ve en çok kullanılan sürüm (★300k+), soru disiplini (tek soru, somut örnek) ve tasarımdan plana devir zinciri net; görsel yardımcı farklılaştırıcı. vudovn sürümü 3 zorunlu soru şablonuna indirgenmiş, interview-me ise yalnız niyet çıkarıyor. Not: superpowers:writing-plans gibi ad alanlı referanslar proje kurulumunda düz adla çözülür.

### brainstorming@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** ag-kit'in Sokratik soru protokolü: belirsiz isteklerde kodlamadan önce en az 3 soru (amaç, kullanıcı, kapsam) sorar, soruları seçenek/artı-eksi tablosuyla biçimlendirir; ilerleme panosu, hata iletişimi ve tamamlanma mesajı kalıplarını da içerir. .agents/memory klasörünü okur.
- **Ne zaman:** ag-kit iş akışı kullanan projelerde; seçenek tablolu, karar odaklı soru listesi tercih edildiğinde. · **Ne zaman değil:** Genel kullanımda (obra brainstorming daha doğal ve olgun); aynı adı taşıdığı için birincille birlikte kurulamaz.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** fikir-netlestirme → alternatif
- **Boyut:** 17 KB (SKILL.md 5.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Soru biçimi (öncelik + seçenek tablosu + varsayılan) yararlı ama 'her zaman 3 soru' kuralı küçük işlerde sürtünme yaratıyor; ag-kit'e özgü /remember ve .agents/memory varsayımları var.

### constraint-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Projenin kalite çıtasını CONSTRAINTS.md'de yazılı sözleşmeye çevirir: kullanıcıya hangi boyutların önemli olduğunu sorar, sayı yoksa makul varsayılan eşikler önerir, gereken araçları kurdurur ve diff'te çıtanın sessizce düşürülmesini (yeni @ts-ignore/eslint-disable, atlanan/silinen test, kaldırılan assertion, eşik düşürme) yakalar.
- **Ne zaman:** Yazılı kalite çıtası yoksa; agent testleri atlayıp/susturup yeşile ulaşmaya çalışıyorsa; erişilebilirlik, performans veya kapsama eşiği tanımlanacaksa. · **Ne zaman değil:** Kısa ömürlü prototip/spike; zaten CI'da zorlanan, belgelenmiş standartları olan ekip.
- **Teknoloji:** git, node, python
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kalite-sozlesmesi → birincil · **Roller:** kod-inceleyici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 31 KB (SKILL.md 20.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Agent'ların çıtayı düşürme davranışına özel tek skill; varsayılan eşik tablosu ve floor-guard referansı pratik. 20 KB SKILL.md ile bağlam yükü orta-yüksek.

### doubt-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Önemsiz olmayan her kararı (iddia → en küçük incelenebilir birim → taze bağlamlı karşıt inceleme → uzlaştırma → dur) döngüsünden geçirir; gerekirse Codex veya Gemini CLI ile çapraz model incelemesi yaptırır. Ana oturum orkestratörü için tasarlanmıştır.
- **Ne zaman:** Yüksek riskli işler (üretim kimlik doğrulama, güvenlik, geri alınamaz migrasyon), tanıdık olmayan kod, planın gizli hata modlarının sınanması. · **Ne zaman değil:** Alt-agent/persona içinde (iç içe agent çağıramaz); hızın önemli olduğu düşük riskli işler.
- **Teknoloji:** api-anahtari _(otomatik tespit)_ · **Paketler:** isteğe bağlı: codex CLI veya gemini CLI (çapraz model inceleme)
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** karsit-dogrulama → birincil · **Roller:** planlayici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, opsiyonel. Sınırlı döngü ve 'iç içe çalışamaz' uyarısı iyi düşünülmüş. Maliyetli (her kararda ek agent); yalnız planlayıcı/orkestratör rolüne uygun, persona skill listesine konmamalı.

### executing-plans  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** Yazılmış bir planı alt-agent kullanmadan, aynı oturumda görev görev uygular: her görev için brief ve kayıt defteri (ledger) tutar, TDD ile ilerler, plan sorunlarında 'karar' kaydı düşerek durmadan devam eder, sonunda tek bir taze bağlamlı inceleme yaptırıp finishing-a-development-branch'e geçer. task-start/task-done betikleri içerir.
- **Ne zaman:** writing-plans planı hazır ve kullanıcı satır içi yürütmeyi seçtiyse; alt-agent aracı olmayan ortamlarda (ör. bazı Codex kurulumları). · **Ne zaman değil:** Her görevde ayrı inceleme kapısı isteniyorsa veya plan çok uzunsa (subagent-driven-development); planı olmayan işler.
- **Teknoloji:** git · **Paketler:** bash (task-start/task-done betikleri)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** plan-yurutme → birincil · **Roller:** planlayici
- **Boyut:** 23 KB (SKILL.md 19.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, plan-yurutme grubunun birincili (bu kategoride). Durma koşulları ve ledger disiplini çok net. Not: alt-agent'lı yürütme d-ai-otomasyon'daki subagent-driven-development'ta; planlayıcı rolü onu çekirdekte, bunu opsiyonelde tutar. ../using-superpowers/references bağlantısı ayrı skill'e işaret ediyor.

### idea-refine  ·  addyosmani/agent-skills @ aeac41d  ·  puan 86 (A)

- **Ne yapar:** Ham fikirleri ıraksak (genişlet) ve yakınsak (değerlendir, daralt) düşünme aşamalarıyla keskin bir konsepte çevirir; sonuçta problem tanımı, önerilen yön, doğrulanacak varsayımlar, MVP kapsamı ve 'yapmayacaklarımız' içeren bir belge (docs/ideas/) üretir.
- **Ne zaman:** Ürün/özellik fikri henüz bulanıkken, seçenekleri açıp sonra birine indirmek ya da bir planın varsayımlarını sınamak istendiğinde. · **Ne zaman değil:** Ne yapılacağı belli, yalnız gereksinim ayrıntısı eksikse (brainstorming / interview-me); kod düzeyi planlama (writing-plans).
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → alternatif · **Roller:** planlayici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 40 KB (SKILL.md 9.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, alternatif. Çerçeveler (frameworks.md) ve örnekler iyi; ürün/konsept aşamasında brainstorming'den daha yapılandırılmış. Betik yalnız docs/ideas klasörü açıyor.

### incremental-implementation  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Değişiklikleri ince, doğrulanabilir dilimlerle teslim ettirir: dikey/sözleşme-önce/risk-önce dilimleme, 'önce sadelik' ve kapsam disiplini, her adımda derlenebilir kalma, yarım özellikleri feature flag arkasına alma, güvenli varsayılanlar ve geri alınabilirlik kuralları.
- **Ne zaman:** Birden çok dosyaya dokunan her özellik/değişiklikte; plandan sıradaki görevi alırken; büyük kod bloğu yazma eğilimi olduğunda. · **Ne zaman değil:** Tek satırlık düzeltmeler; planın kendisini yazmak (writing-plans).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** plan-yurutme → tamamlayıcı · **Roller:** planlayici, frontend-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 9 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tamamlayıcı. Kısa (9 KB), yığından bağımsız; 'Rule 0.5 kapsam disiplini' agent'ların taşmasını iyi engelliyor. ../../references/definition-of-done.md arşivde yok (yalnız 'ayrıca bkz').

### interview-me  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Kullanıcının gerçekte ne istediğini (yapması gerektiğini düşündüğü şeyi değil) bulmak için tek soruluk turlarla ~%95 güvene kadar görüşme yapar; her soruya bir tahmin ekler, niyeti kullanıcının kendi sözleriyle özetleyip açık onay ister ve durur.
- **Ne zaman:** İstek 'kimin için / neden şimdi' bilgisi olmadan geldiğinde; kullanıcı 'beni sorgula', 'emin miyiz?' dediğinde; plan veya spec yazılmadan önce kısa niyet doğrulaması. · **Ne zaman değil:** Etkileşimsiz bağlamlar (CI, /loop); gereksinim zaten netse; tam tasarım belgesi gerekiyorsa (brainstorming).
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** fikir-netlestirme → tamamlayıcı · **Roller:** planlayici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 15 KB (SKILL.md 14.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tamamlayıcı. Net durma kuralı ve 'istek vs. olması gereken' ayrımı brainstorming'den farklı bir boşluğu dolduruyor; kısa ve yan etkisiz.

### plan-writing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** ag-kit'in kısa plan yazma rehberi (obra/superpowers'tan uyarlanmış): 5-10 görevlik, her görevin doğrulaması belli, bir sayfayı geçmeyen planı proje kökünde {görev-adı}.md olarak yazdırır; proje tipine göre ag-kit doğrulama betiklerini önerir.
- **Ne zaman:** ag-kit kullanan projelerde veya çok kısa, tek sayfalık plan yeterliyse. · **Ne zaman değil:** Alt-agent'lara devredilecek ayrıntılı plan gerektiğinde (writing-plans); ag-kit betikleri (ux_audit.py, security_scan.py…) projede yoksa betik önerileri boşa düşer.
- **Teknoloji:** node, python, react, tailwind, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → alternatif
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısalık ilkesi iyi ama içerik writing-plans'ın sadeleştirilmiş türevi; plan dosyasını proje köküne yazma kuralı ve var olmayan ag-kit betiklerine atıf zayıflık.

### planning-and-task-breakdown  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Spec'i bağımlılık grafiği çıkarıp dikey dilimlere bölerek sıralı, boyutlandırılmış görevlere çevirir; her görev için kabul ölçütü ve doğrulama, fazlar arası kontrol noktaları, riskler ve paralelleştirme fırsatları içeren plan şablonu verir.
- **Ne zaman:** Spec hazır, iş büyük ve dilimlenmesi gerekiyorsa; tahmin/kapsam çıkarma veya paralel iş fırsatı aranırken; superpowers zinciri kullanılmayan projelerde. · **Ne zaman değil:** writing-plans kurulu bir rolde ikinci plan skilli olarak (aynı iş); tek adımlık işler.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → alternatif · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İyi yapılandırılmış ve kısa; dikey dilim ve kontrol noktası anlatımı güçlü. writing-plans'tan daha az ayrıntılı (arayüz sözleşmesi, TDD adımları yok), bu yüzden alternatif. ../../references/ bağlantıları arşivde yok (yalnız 'ayrıca bkz').

### source-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Her uygulama kararını resmî dokümantasyona dayandırır: yığını ve sürümleri tespit eder, resmî belgeyi çeker (çekilen içeriği talimat değil veri sayar), belgelenmiş kalıpla uygular ve kaynakları kodda/yanıtta alıntılar.
- **Ne zaman:** Framework/kütüphane sürümüne duyarlı işler; güncelliğini yitirmiş kalıp riski olan hızlı değişen API'ler (Next.js, React 19, Tailwind v4…). · **Ne zaman değil:** İnternet erişimi yoksa; saf algoritma/iş mantığı değişiklikleri.
- **Teknoloji:** api-anahtari, css, html, next.js, node, python, react, svelte, tailwind, typescript, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** resmi-dokuman-dayanagi → birincil · **Roller:** frontend-muhendis · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 9.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa ve yığından bağımsız; 'çekilen içeriği veri say' güvenlik notu değerli. Model bilgisinin eskidiği framework işlerinde frontend rolüne iyi bir tamamlayıcı.

### spec-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 91 (A)

- **Ne yapar:** Kodlamadan önce spec yazdırır: kapsam kontrolü (gerekirse yetenek haritasına bölme), amaç/yığın/komutlar/yapı/test stratejisi/sınırlar/başarı ölçütü içeren spec, ardından plan, görevler ve uygulama aşamalarını kapılı bir akışla yürütür; spec'i canlı tutma kurallarını verir.
- **Ne zaman:** Yeni proje/özellik başlarken spec veya PRD yoksa; tek bir isteğin birden çok bağımsız yeteneğe bölünmesi gerektiğinde. · **Ne zaman değil:** Küçük, net değişiklikler; gereksinim hâlâ belirsizse önce brainstorming/interview-me.
- **Teknoloji:** node, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** spec-yazimi → birincil · **Roller:** planlayici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, birincil (spec yazımı). superpowers'ta brainstorming'in ürettiği tasarım belgesine karşılık gelir ama daha yapılandırılmış şablon ve 'spec'i canlı tut' kuralları sunar; writing-plans ile birlikte kullanılır.

### templates  ·  vudovn/ag-kit @ 549ba3d  ·  puan 89 (A)

- **Ne yapar:** 13 proje iskelet şablonunun (Next.js fullstack/SaaS/static, Nuxt, Express, FastAPI, Expo, Flutter, Electron, Chrome MV3, CLI, Turborepo, Astro) dizini; her şablon yığın, sürüm ve klasör yapısını verir.
- **Ne zaman:** Sadece şablon dosyaları istenip app-builder'ın orkestrasyon kısmı istenmediğinde. · **Ne zaman değil:** app-builder kuruluysa (aynı dosyaları templates/ altında zaten taşıyor); adı genel olduğundan başka 'templates' skilleriyle çakışabilir.
- **Teknoloji:** next.js, react, node, python, vue, flutter, react-native
- **Claude / Codex:** tam / tam
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** proje-iskeleti → alternatif
- **Boyut:** 43 KB (SKILL.md 1.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV / ALTERNATİF. İçerik app-builder/templates ile birebir aynı (diff: yalnız KAYNAK.md farkı); ayrı kurulması yinelenen bağlam. Durum alternatife çekildi.

### writing-plans  ·  obra/superpowers @ b739a8a  ·  puan 91 (A)

- **Ne yapar:** Spec'ten, kod tabanını hiç görmemiş bir mühendisin uygulayabileceği ayrıntılı uygulama planı yazdırır: dosya yapısı, her görev için dosyalar, arayüz imzaları (üretir/tüketir), TDD adımları (başarısız test → minimum kod → geçen test → commit), global kısıtlar ve inceleme odağı. Plan subagent-driven-development veya executing-plans'a devredilir.
- **Ne zaman:** Çok adımlı bir iş için spec/gereksinim hazırsa, koda dokunmadan önce; alt-agent'lara dağıtılacak görevler gerektiğinde. · **Ne zaman değil:** Tek dosyalık küçük düzeltmeler; spec henüz yoksa (önce brainstorming/spec-driven-development).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** uygulama-plani → birincil · **Roller:** planlayici
- **Boyut:** 10 KB (SKILL.md 10.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, uygulama-plani grubunun birincili. Gerekçe: arayüz sözleşmeleri, görev boyutlandırma ve 'inceleme odağı' bölümüyle en uygulanabilir plan biçimi; superpowers yürütme zinciriyle (subagent-driven-development, executing-plans, TDD, verification) uçtan uca bağlı. addyosmani planning-and-task-breakdown daha hafif ve yığından bağımsız; vudovn plan-writing kısa ama ag-kit betiklerine atıf yapıyor.
