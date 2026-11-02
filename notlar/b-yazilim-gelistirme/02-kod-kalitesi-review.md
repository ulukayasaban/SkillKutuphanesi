# 02-kod-kalitesi-review — Yazılım Geliştirme

_Code review, sadeleştirme, temiz kod_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **9/17**

### clean-code  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** ag-kit'in her kod yazımında açık tutulan pragmatik kodlama standardı: SRP/DRY/KISS/YAGNI, isimlendirme kuralları, küçük fonksiyon ve sığ iç içelik, gereksiz yorum/yardımcı/dosya yasakları; bir dosyayı düzenlemeden önce onu kimin içe aktardığını ve hangi testlerin kapsadığını kontrol etmeyi şart koşar.
- **Ne zaman:** Kod yazan agent'lar için kısa, her zaman açık stil ve disiplin kuralı olarak. · **Ne zaman değil:** Projenin kendi stil rehberi/lint kuralları güçlü ve farklıysa (çatışabilir); 'hata bildirilince açıklama yapma, düzelt' kuralı açıklama isteyen kullanıcılarla uyumsuz olabilir.
- **Teknoloji:** playwright, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** temiz-kod → birincil
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, temiz-kod grubunun tek üyesi. 7 KB, yararlı kurallar ve 'düzenlemeden önce bağımlıları kontrol et' adımı değerli; ancak katı sayılar (fonksiyon ≤20 satır) ve 'priority: CRITICAL, her zaman aktif' iddiası bağlam dışı uygulanabilir.

### code-review-and-quality  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Beş eksenli kod incelemesi yaptırır: doğruluk, okunabilirlik/sadelik, mimari, güvenlik, performans. Önce testleri sonra uygulamayı okur, bulguları ciddiyete göre sınıflar, değişiklik boyutu ve açıklama kuralları, çoklu model inceleme deseni, ölü kod hijyeni, bağımlılık disiplini ve hazır inceleme şablonu verir.
- **Ne zaman:** Birleştirmeden önce her değişiklikte; kendi, başka agent'ın veya insanın yazdığı diff/PR'ı incelerken (diff satır içi yapıştırılmış olsa da). · **Ne zaman değil:** Yalnız YAGNI/aşırı mühendislik taraması istendiğinde (pragmatic-review daha odaklı); inceleme alt-agent'ını başlatma akışı (requesting-code-review).
- **Teknoloji:** node, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-inceleme → birincil · **Roller:** kod-inceleyici · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 21 KB (SKILL.md 20.8 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Karar: TUT, kod-inceleme grubunun birincili. Gerekçe: en kapsamlı ve yığından bağımsız inceleme yöntemi; 'önce testleri oku' ve 'doğrulamayı doğrula' adımları agent incelemelerinin tipik açığını kapatıyor. obra requesting-code-review inceleme yapmaz, inceleyiciyi başlatır (ayrı grup); pragmatic-review ve code-review-checklist daha dar.

### code-review-checklist  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Kısa kod inceleme kontrol listesi: doğruluk, güvenlik (enjeksiyon, XSS, gizli anahtar, prompt injection), performans, kod kalitesi, test ve dokümantasyon maddeleri; AI/LLM kodu için ek kontroller ve 🔴/🟡/🟢 yorum etiketleri.
- **Ne zaman:** Hızlı, hafif bir kontrol listesi yeterli olduğunda; ag-kit iş akışı kullanan projelerde. · **Ne zaman değil:** Derinlemesine inceleme gerektiğinde (code-review-and-quality).
- **Teknoloji:** typescript
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-inceleme → alternatif
- **Boyut:** 3 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. 3 KB, yararlı ama yüzeysel; maddeler code-review-and-quality'nin alt kümesi. AI'ya özgü kontroller (prompt injection, çıktı temizleme) küçük bir artı.

### code-review-graph  ·  vudovn/ag-kit @ 549ba3d  ·  puan 75 (B)

- **Ne yapar:** code-review-graph MCP sunucusunun kullanım rehberi: Tree-sitter ile kod tabanını SQLite'ta AST grafiğine çevirip değişikliğin etki alanını (blast radius) hesaplar; büyük depolarda inceleme ve çok dosyalı değişikliklerde yalnız ilgili dosyaları okutarak token tasarrufu sağlar. Kurulum ve indeks oluşturmayı kullanıcı onayına bağlar.
- **Ne zaman:** 500+ dosyalı depolar, monorepo'lar, modüller arası bağımlılıklı değişiklikler; ölü kod tespiti ve refactor önizlemesi. · **Ne zaman değil:** ~200 dosyanın altındaki projeler; yoğun dinamik import/yansıma kullanan kod; MCP kurmak istenmiyorsa.
- **Teknoloji:** python, tree-sitter, sqlite, mcp · **Paketler:** code-review-graph (pip), MCP sunucu yapılandırması
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** buyuk-depo-baglami → birincil
- **Boyut:** 11 KB (SKILL.md 10.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel, --skill ile). Dürüst kullan/kullanma eşikleri ve onaysız kurulum yasağı iyi. Üçüncü taraf PyPI paketine ve MCP kurulumuna bağlı; skill tek başına iş yapmaz. Rol çekirdeğine alınmadı.

### code-simplification  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Davranışı birebir koruyarak kodu açıklık için sadeleştirir: Chesterton'ın çiti (önce neden var olduğunu anla), proje geleneklerine uyma, zekice yerine açık kod, denge ve yalnız değişen kapsama odaklanma ilkeleri; TypeScript/JavaScript, Python ve React için dile özgü örnekler.
- **Ne zaman:** Çalışan ama okunması/bakımı zor koda refactor; incelemede biriken karmaşıklık fark edildiğinde; yeni yazılan kodu teslim öncesi toparlamak. · **Ne zaman değil:** Depo genelinde ölü kod/katman denetimi (simplify-codebase); davranış değiştiren yeniden tasarım; performans ayarı.
- **Teknoloji:** typescript, javascript, python, react
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-sadelestirme → birincil · **Roller:** kod-inceleyici · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 13 KB (SKILL.md 13.4 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Karar: TUT, kod-sadelestirme grubunun birincili. Gerekçe: davranış koruma ve 'değişen kapsamla sınırla' kuralları varsayılan kullanım için en güvenli sürüm; dile özgü rehber somut. simplify-codebase depo geneli denetim için tamamlayıcı; simplify-code (vudovn) daha yüzeysel alternatif.

### lint-and-validate  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Her kod değişikliğinden sonra ekosisteme göre lint, tip denetimi ve güvenlik taramasını çalıştırır (Node/TS: eslint, tsc --noEmit, npm audit; Python: ruff, mypy, bandit) ve hata kalmadan işi bitmiş saymaz; proje tipini algılayıp uygun komutları çalıştıran lint_runner.py ve type_coverage.py betikleri içerir.
- **Ne zaman:** TypeScript/JavaScript veya Python projelerinde her değişiklik sonrası otomatik kalite kapısı. · **Ne zaman değil:** Lint/tip araçları yapılandırılmamış projeler (önce yapılandırma); farklı ekosistemler (Go, Rust…) için komut yok.
- **Teknoloji:** node, typescript, python · **Paketler:** eslint, typescript, ruff/mypy/bandit (Python)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** lint-dogrulama → birincil
- **Boyut:** 16 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT. Kısa ve uygulanabilir; betikler proje tipini algılıyor. 'FINAL AUDIT REPORT' bölümüne atıf betik çıktısıyla tam örtüşmüyor; npm audit her değişiklikte gereksiz yavaş olabilir.

### ponytail  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 100 (A)

- **Ne yapar:** Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing, refactoring, reviewing, choosing dependencies) and when the user says "ponytail", "be lazy", "simplest solution", "yagni", or complains about over-engineering or bloat. Levels: lite, full (default), ultra.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** otomatik

### ponytail-audit  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 100 (A)

- **Ne yapar:** Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Ranked, each finding explained in plain English. One-shot report, changes nothing. Use for "audit this codebase", "review the whole repo", "find bloat", "what can I delete", /ponytail-audit.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.3 KB, yük kucuk)
- **İnceleme:** otomatik

### ponytail-debt  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 100 (A)

- **Ne yapar:** List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did ponytail defer", "list the shortcuts", /ponytail-debt.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.7 KB, yük kucuk)
- **İnceleme:** otomatik

### ponytail-gain  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 100 (A)

- **Ne yapar:** Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytail impact".
- **Teknoloji:** api-anahtari, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.1 KB, yük kucuk)
- **İnceleme:** otomatik

### ponytail-help  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 97 (A)

- **Ne yapar:** Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail help", "how do I use ponytail".
- **Teknoloji:** api-anahtari, node _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### ponytail-review  ·  DietrichGebert/ponytail @ 96608e0  ·  puan 100 (A)

- **Ne yapar:** Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. Reads the connected code, not only the diff. Each finding is explained in plain English. Use for "review this", "code review", "review the last commit", "review my PR", "is this over-engineered", /ponytail-review.
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** DietrichGebert (kisi, ★182163, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 5.0 KB, yük kucuk)
- **İnceleme:** otomatik

### pragmatic-review  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 70 (B)

- **Ne yapar:** YAGNI ve KISS odaklı etkileşimli kod incelemesi: git durumundan kapsamı seçtirir (commit edilmemiş, dal, dosya, son N commit), aşırı mühendislik kalıplarını tarar, temel güvenlik/performans kontrolü yapar ve bulguları kanıtla öz-denetler. --deep altı geçişli kapsamlı inceleme, --ci GitHub Actions için etkileşimsiz mod sunar.
- **Ne zaman:** Aşırı mühendislik, gereksiz soyutlama şüphesi olan değişikliklerde; CI'da otomatik inceleme yorumu üretmek. · **Ne zaman değil:** Genel çok eksenli inceleme varsayılanı olarak (code-review-and-quality); git dışı projeler.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-inceleme → alternatif · **Roller:** kod-inceleyici
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. YAGNI odağı ve CI modu farklılaştırıcı; claudesidian (Obsidian kasası) reposundan geliyor ama içerik genel. Etkileşimli menü varsayılan, --auto/--ci ile atlanır.

### receiving-code-review  ·  obra/superpowers @ 2ce8aa1  ·  puan 98 (A)

- **Ne yapar:** Gelen kod inceleme geri bildirimine teknik titizlikle yaklaşmayı öğretir: oku, kendi sözlerinle yeniden ifade et, kod tabanında doğrula, değerlendir, gerekirse gerekçeli itiraz et, maddeleri tek tek uygulayıp test et; 'harika fikir!' gibi gösterişli onayı ve doğrulamadan uygulamayı yasaklar.
- **Ne zaman:** İnsan veya inceleyici agent'tan geri bildirim geldiğinde, özellikle belirsiz ya da teknik olarak şüpheli öneriler varken. · **Ne zaman değil:** Geri bildirim yokken; incelemeyi yapan tarafta.
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** inceleme-dongusu → tamamlayıcı
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT, tamamlayıcı. 6 KB, davranışsal açıdan değerli (yaltaklanma ve kör uygulamayı önler); uygulayıcı rollerine uygun.

### requesting-code-review  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** İş bitince veya birleştirmeden önce, oturum geçmişini değil özenle hazırlanmış bağlamı (açıklama, plan, BASE/HEAD SHA) vererek bir inceleyici alt-agent başlatır; code-reviewer.md şablonu ile Kritik/Önemli/Küçük bulguları ister ve bunlara göre ilerler.
- **Ne zaman:** subagent-driven-development'ta her görevden sonra; büyük özellik bitiminde; main'e birleştirmeden önce taze bağlamlı inceleme gerektiğinde. · **Ne zaman değil:** Alt-agent aracı olmayan ortamlar (inceleme satır içi yapılır); incelemenin kendisini yapan agent için yöntem değil (code-review-and-quality).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** inceleme-dongusu → birincil · **Roller:** kod-inceleyici, planlayici
- **Boyut:** 9 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, inceleme-dongusu grubunun birincili. Kısa, superpowers zincirinin parçası; code-reviewer.md şablonu 'spec bir vizyon belgesidir' ilkesiyle güçlü. İnceleme yöntemi değil orkestrasyon olduğu için code-review-and-quality ile çakışmaz.

### simplify-code  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Aşırı mühendislik içeren kodu sadeleştirme kontrol listesi: gereksiz soyutlamalar, ölü kod, derin iç içelik, çok parametreli fonksiyonlar ve erken optimizasyon için koku → çözüm tabloları; sayısal hedefler (iç içelik ≤3, parametre ≤4, fonksiyon ≤30 satır) ve adım adım protokol.
- **Ne zaman:** Hızlı, kontrol listesi tarzı sadeleştirme; ag-kit iş akışı kullanan projeler. · **Ne zaman değil:** Davranış korumaya ve proje geleneklerine özen gereken işlerde (code-simplification daha dikkatli); depo geneli denetim (simplify-codebase).
- **Teknoloji:** typescript, javascript
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kod-sadelestirme → alternatif
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Okunur ve kısa, ama 'tek implementasyonlu arayüzü kaldır' gibi kurallar bağlamsız uygulanırsa zarar verebilir; code-simplification'ın kapsadığı işi daha kaba yapıyor.

### simplify-codebase  ·  tt-a1i/archify @ a406594  ·  puan 97 (A)

- **Ne yapar:** Kod tabanından kazara karmaşıklığı kanıta dayalı olarak ayıklar: Survey (salt okuma, sıralı bulgular) ve Change (yetkili silme/birleştirme) kipleri; sözleşme haritası çıkarır, her aday için yük/erişilebilirlik/gerekçe/kesinti/sonuç/risk/kanıt kaydı tutar; ölü kod, yinelenen durum, gereksiz API/katman, sahipsiz soyutlama ve eskimiş uyumluluk yollarını hedefler. Güvenlik ve veri kaybı korumalarına dokunmaz.
- **Ne zaman:** Var olan bir depoda sadeleştirme denetimi veya açıkça yetkilendirilmiş büyük çaplı temizlik; 'nereler gereksiz?' sorusuna kanıtlı yanıt. · **Ne zaman değil:** Genel code review, onboarding, sadece stil refactor'ü veya performans ayarı (skill kendisi de bunları dışlıyor); küçük diff sadeleştirmesi (code-simplification).
- **Teknoloji:** dil-bagimsiz, git
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★92406, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** kod-sadelestirme → tamamlayıcı · **Roller:** kod-inceleyici
- **Boyut:** 27 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, tamamlayıcı. Bu alanda gördüğüm en titiz sadeleştirme protokolü (kanıt kaydı, kör nokta bildirimi, ürün kararı ayrımı); dil bağımsız. metadata.internal işaretli ama Archify'a bağlı değil. mevcut-kod-iyilestirme profilinin ana skilli.
