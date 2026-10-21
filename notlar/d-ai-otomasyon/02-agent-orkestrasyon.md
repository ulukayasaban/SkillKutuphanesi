# 02-agent-orkestrasyon — AI ve Otomasyon

_Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **14/14**

### batch-operations  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Birçok dosyaya aynı değişikliği güvenle uygulama protokolü: deseni tanımla, önce grep ile etkilenen dosyaları önizle, toplu uygula, sonra doğrula (sayım, derleme, test). Yeniden adlandırma, import ekleme, sürüm güncelleme gibi yaygın kalıplar ve güvenlik kuralları içerir.
- **Ne zaman:** Kod tabanında desen tabanlı toplu değişiklik: fonksiyon yeniden adlandırma, API geçişi, sürüm numarası güncelleme. · **Ne zaman değil:** Tek dosya düzenlemesi ya da her dosyada ayrı yargı gerektiren değişiklik (alt-agent'lara böl). allowed-tools/effort frontmatter alanları Claude Code'a özgü; Codex yok sayar, protokol aynen geçerli.
- **Teknoloji:** bash, git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Roller:** agent-orkestra
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve doğru 'önizle → uygula → doğrula' disiplini; içerik genel bilgi düzeyinde. Aslında yazılım geliştirme konusu ama alt-agent'a bölme kararıyla bağlantılı.

### behavioral-modes  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** Görev türüne göre yedi çalışma modu tanımlar (brainstorm, implement, debug, review, teach, ship, orchestrate); her mod için davranış kuralları ve çıktı biçimi verir.
- **Ne zaman:** ag-kit ailesini kuran projelerde agent'ın tonunu/yaklaşımını göreve göre değiştirmek. · **Ne zaman değil:** Diğer ailelerle (superpowers, agent-skills) birlikte — süreç skilleri zaten bu davranışları tanımlıyor ve çakışır; IMPLEMENT modu kütüphanede olmayan 'clean-code' skill'ine atıf yapıyor. allowed-tools Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 6 KB (SKILL.md 6.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Genel istem metni; ag-kit'in diğer skillerine bağımlı, ek değeri düşük.

### context-compression  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Uzun oturumlarda bağlamı sıkıştırma: büyük araç çıktılarını anlamsal özete indirme (mikro), biten iş aşamalarını özetleme ve oturum kontrol noktası yazma; kararları ve değişen dosyaları koruma protokolü.
- **Ne zaman:** 20+ turluk oturumlar, agent tekrar etmeye başladığında, iş aşaması değişiminde. · **Ne zaman değil:** Kısa oturumlarda; harness otomatik sıkıştırma yapıyorsa (Claude Code/Codex compaction) çoğu zaman gereksiz — yalnızca elle kontrol noktası yazımı için. allowed-tools/effort Claude Code'a özgü; Codex yok sayar.
- **Teknoloji:** api-anahtari, next.js, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → tamamlayıcı · **Roller:** agent-orkestra
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Üç seviyeli sıkıştırma ve kontrol noktası şablonu kullanışlı; token kazancı rakamları tahmini.

### context-engineering  ·  addyosmani/agent-skills @ aeac41d  ·  puan 95 (A)

- **Ne yapar:** Agent'a doğru bağlamı doğru zamanda verme: kalıcıdan geçiciye bağlam hiyerarşisi (kural dosyaları CLAUDE.md/AGENTS.md, spec, ilgili kaynak dosyalar, hata çıktısı, konuşma), yeniden başlatılabilir oturum sınırları ve bağlam paketleme stratejileri.
- **Ne zaman:** Yeni oturum/proje kurulumu, kural dosyası yazımı, agent çıktı kalitesi düştüğünde, kod tabanının farklı bölümüne geçerken. · **Ne zaman değil:** Tek seferlik küçük sorularda gereksiz.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** baglam-yonetimi → birincil · **Roller:** agent-orkestra · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 15 KB (SKILL.md 15.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). addyosmani; araçtan bağımsız (CLAUDE.md ve AGENTS.md'yi birlikte anıyor), somut kural dosyası şablonu ve oturum sınırı önerileri. Bağlam grubunda birincil.

### coordinator-mode  ·  vudovn/ag-kit @ 549ba3d  ·  puan 85 (A)

- **Ne yapar:** Koordinatör olarak çok agent'lı orkestrasyon: görevi ayrıştır, sınıflandır (araştırma/uygulama/doğrulama), okuma işlerini paralel yazma işlerini sıralı dağıt, izle, sentezle ve doğrula. 'Anlamayı devretme' kuralı, işçi istem şablonları ve fork kuralları içerir.
- **Ne zaman:** Birden çok alanı kapsayan büyük görevde agent'ın kendisi kod yazmadan işçi alt-agent'ları yönetmesi. · **Ne zaman değil:** Tek alanlı işlerde; yazılı bir uygulama planı varsa subagent-driven-development daha disiplinli. allowed-tools içinde Claude Code'un 'Agent' aracı geçiyor; Codex'te alt-agent desteği olan sürümde aynı akış, yoksa işçi görevleri ayrı Codex oturumları/`codex exec` çağrılarıyla çalıştırılır.
- **Teknoloji:** api-anahtari, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 8 KB (SKILL.md 7.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İşçi istemi yazma rehberi ve eşzamanlılık kuralları güçlü; ama plan tabanlı inceleme döngüsü yok. Orkestrasyon grubunda birincil subagent-driven-development.

### diagnosing-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 88 (A)

- **Ne yapar:** Bir superpowers oturumu kötü gittiğinde (tekrar eden iş, yok sayılan plan, tetiklenmeyen skill, pahalılık) diskteki transkriptleri okuyup kanıta dayalı rapor çıkarır; her bulgu path:line ile alıntılanır. Oturum bulma, gizli veri karartma ve GitHub issue paketi rehberleri içerir.
- **Ne zaman:** superpowers skill ailesiyle çalışan oturumların neden yanlış gittiğini incelemek, bakımcılara hata raporu hazırlamak. · **Ne zaman değil:** superpowers kullanılmıyorsa; genel kod hata ayıklaması için (systematic-debugging).
- **Teknoloji:** bash, jsonl
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** superpowers-ailesi → tamamlayıcı
- **Boyut:** 41 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (dar). Kanıt disiplini ve redaksiyon politikası örnek alınacak düzeyde; çok harness'li (Claude Code, Codex vb.) oturum keşfi var. Yalnızca superpowers kullanıcıları için.

### discernment-nudge  ·  anthropics/skills @ dbd4588  ·  puan 84 (A)

- **Ne yapar:** Kullanıcının üzerine karar vereceği önemli bir cevap ya da taslaktan sonra, cevaptaki belirli noktalara bağlı 2-3 kısa takip sorusu ekler: önemli olguları doğrulama, varsayımları sorgulama, eksik bağlamı fark etme. Konuşma başına en fazla bir kez; basit sorularda, kodda ve yaratıcı yazıda devreye girmez.
- **Ne zaman:** Tavsiye, plan, tahmin, veri yorumu gibi kullanıcının harekete geçeceği çıktılar üreten sohbet/asistan agent'ları. · **Ne zaman değil:** Kod yazan agent'larda (skill zaten kapsam dışı sayar); otomatik iş hatlarında (kullanıcı yokken soru eklemek gürültü).
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Roller:** dokuman-yazari
- **Boyut:** 21 KB (SKILL.md 10.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi; ne zaman kullanılmayacağı ve çıktı biçimi çok net. Orkestrasyon değil 'cevap kalitesi' skill'i; rapor/tavsiye üreten rollere opsiyonel.

### dispatching-parallel-agents  ·  obra/superpowers @ 2ce8aa1  ·  puan 96 (A)

- **Ne yapar:** Bağımsız 2+ problemi (farklı test dosyaları, alt sistemler) her birine izole bağlamlı ayrı bir agent vererek paralel çözme kalıbı: bağımsız alanları belirle, odaklı görev istemi yaz, paralel dağıt, sonuçları incele ve birleştir.
- **Ne zaman:** Birbirinden bağımsız birden çok hata/araştırma işini paralel yürütmek. · **Ne zaman değil:** Görevler ortak durum paylaşıyor ya da aynı dosyalara yazıyorsa; tek kök nedenli hatalarda. Codex'te alt-agent yoksa paralel `codex exec` süreçleri ya da ayrı worktree'lerle uygulanır.
- **Teknoloji:** typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → tamamlayıcı · **Roller:** agent-orkestra, planlayici
- **Boyut:** 6 KB (SKILL.md 5.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (tamamlayıcı). superpowers; kısa (6 KB), karar ağacı ve istem yapısı net. subagent-driven-development ile birlikte kullanılır.

### intelligent-routing  ·  vudovn/ag-kit @ 549ba3d  ·  puan 68 (B)

- **Ne yapar:** Her kullanıcı isteğini sessizce analiz edip anahtar kelime/alan/karmaşıklığa göre uygun uzman agent'ı (security-auditor, frontend-specialist, orchestrator…) otomatik seçen yönlendirme kuralları.
- **Ne zaman:** ag-kit'in uzman agent tanımlarının kurulu olduğu projelerde. · **Ne zaman değil:** ag-kit agent'ları (security-auditor, backend-specialist vb.) kurulu değilse — bu kütüphanede yoklar, rol sistemi zaten skill-ekle.py ile kuruluyor. 'Her zaman aktif' talimatı bağlamı ve davranışı etkiler. allowed-tools Claude Code'a özgü.
- **Teknoloji:** api-anahtari, css, docker, html, node, playwright, react, tailwind, vue _(otomatik tespit)_ · **Paketler:** ag-kit agent tanımları
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 11 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Var olmayan agent adlarına bağımlı; bu kütüphanenin rol sistemiyle çakışır.

### memory-system  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Oturumlar arası kalıcı bellek: .agents/memory/MEMORY.md indeksi (en fazla 200 satır) ve konu dosyaları (kullanıcı tercihleri, proje kuralları, teknik kararlar, geri bildirim); kaydetme, hatırlama, arama işlemleri ve neyin kaydedilmeyeceği kuralları.
- **Ne zaman:** Harness'in yerleşik belleği olmayan ortamlarda (ya da projeye taşınabilir, git'te tutulan bellek istendiğinde) tercih ve kararları saklamak. · **Ne zaman değil:** Claude Code'un yerleşik auto-memory'si veya claude-mem gibi bir bellek eklentisi zaten kullanılıyorsa (çift kayıt olur); gizli bilgi saklamak için. Codex'te uygundur — AGENTS.md'ye 'oturum başında .agents/memory/MEMORY.md oku' satırı eklenmeli.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel). İndeks + konu dosyası yapısı sağlam ve Claude Code belleğine benzer; harness belleğiyle çakışma riski var.

### parallel-agents  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Güvenli paralel agent kullanımı: ne zaman paralelleştirilir/paralelleştirilmez, çalışma ortamından bağımsız yetenek keşfi, güven sınırı, delegasyon bütçesi, izolasyon politikası (worktree/sandbox), delegasyon şablonu, ilerleme yok tespiti ve sentez protokolü. Google Antigravity öncelikli yazılmış.
- **Ne zaman:** Güvenlik/izolasyon kuralları önemli olan çok agent'lı işler; delegasyon bütçesi ve izleme gerektiğinde. · **Ne zaman değil:** Claude Code/Codex'te Antigravity'ye özgü kısımlar uygulanamaz — genel kurallar geçerli. Plan yürütmek için subagent-driven-development, basit paralel hata ayıklama için dispatching-parallel-agents. allowed-tools/effort Claude Code'a özgü.
- **Teknoloji:** react _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → alternatif
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Güvenlik ve izolasyon bölümleri iyi; Antigravity odaklı olması diğer harness'lerde gürültü yaratıyor.

### subagent-driven-development  ·  obra/superpowers @ 2ce8aa1  ·  puan 95 (A)

- **Ne yapar:** Yazılı uygulama planını görev başına taze bir uygulayıcı alt-agent göndererek yürütür; her görevden sonra spec uyumu + kod kalitesi incelemesi, düzeltme döngüsü ve sonda tüm dal incelemesi yapar. Rol başına model seçimi, karar defteri (ledger), kesintisiz yürütme kuralları ve görev özeti/inceleme paketi betikleri içerir.
- **Ne zaman:** Bağımsız görevlere bölünmüş bir planı tek oturumda yüksek kaliteyle uygulamak. · **Ne zaman değil:** Plan yoksa (önce writing-plans/planning-and-task-breakdown); görevler sıkı bağımlıysa; küçük tek dosyalık işlerde. Codex'te alt-agent desteği yoksa her görev için ayrı `codex exec` çağrısı ya da executing-plans ile sıralı yürütme kullanılır.
- **Teknoloji:** git, bash
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** alt-agent-orkestrasyon → birincil · **Roller:** agent-orkestra, planlayici
- **Boyut:** 56 KB (SKILL.md 19.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Orkestrasyon ailesinde en olgun süreç: görev başına inceleme, düzeltme döngüsü eskalasyonu, model katmanlama ve betik desteği. 32 KB SKILL.md ağır ama tek başına bir yürütme sistemi. coordinator-mode ve parallel-agents alternatif, dispatching-parallel-agents tamamlayıcı.

### using-agent-skills  ·  addyosmani/agent-skills @ aeac41d  ·  puan 87 (A)

- **Ne yapar:** addyosmani/agent-skills ailesinin meta-skill'i: işin geliştirme aşamasına göre hangi skill'in uygulanacağını gösteren karar ağacı (interview-me, spec, plan, incremental-implementation, test, review, ship…) ve temel çalışma davranışları (varsayımları açığa çıkar, karışıklığı yönet, sadeliği koru, kapsamı koru, doğrula).
- **Ne zaman:** agent-skills ailesinden birden çok skill kurulu projelerde oturum başında doğru skill'i seçmek. · **Ne zaman değil:** Ailenin skilleri kurulu değilse karar ağacındaki adlar boşa düşer; superpowers ailesi kullanılıyorsa using-superpowers ile birlikte kurma (iki meta-skill çakışır).
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★109268, son güncelleme 2026-10-13, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → birincil · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 10 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (birincil, meta grubunda). Zorlayıcı dil kullanmadan net yönlendirme yapıyor; çalışma davranışları bölümü aileden bağımsız da değerli.

### using-superpowers  ·  obra/superpowers @ 2ce8aa1  ·  puan 88 (A)

- **Ne yapar:** superpowers ailesinin meta-skill'i: '%1 ihtimal bile varsa skill'i çağır' kuralı, süreç skillerinin önceliği, rasyonalizasyon kırmızı bayrakları ve Claude Code, Codex, Pi, Antigravity, Gemini, Hermes, Muse için araç eşleme dosyaları.
- **Ne zaman:** superpowers ailesinin (brainstorming, writing-plans, systematic-debugging, subagent-driven-development…) birlikte kurulduğu projeler. · **Ne zaman değil:** Aile kurulu değilse; agent-skills ailesinin meta-skill'iyle birlikte. Çok agresif tetikleme dili küçük işlerde gereksiz süreç yükü yaratabilir. Codex'te references/codex-tools.md araç eşlemesini kullanır — ek uyarlama gerekmez.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** agent-davranis-meta → alternatif
- **Boyut:** 20 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF (meta grubunda). Çok harness'li araç eşlemesi en güçlü yanı; aile dışında kullanılmaz. superpowers ailesi seçilen projede birincil olur.
