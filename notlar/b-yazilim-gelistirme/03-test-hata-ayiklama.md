# 03-test-hata-ayiklama — Yazılım Geliştirme

_TDD, hata ayıklama, doğrulama_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **11/11**

### debugging-and-error-recovery  ·  addyosmani/agent-skills @ aeac41d  ·  puan 98 (A)

- **Ne yapar:** Kök neden odaklı hata ayıklama: 'hattı durdur' kuralı, yeniden üret → yerelleştir → küçült → kök nedeni düzelt → tekrarı önle → uçtan uca doğrula triyajı; test, build ve çalışma zamanı hataları için ayrı triyaj desenleri, güvenli geri dönüş kalıpları, enstrümantasyon kuralları ve hata çıktısını güvenilmeyen veri sayma uyarısı.
- **Ne zaman:** superpowers zinciri kullanılmayan projelerde hata ayıklama; build/runtime hata tipine göre hazır triyaj listesi istendiğinde. · **Ne zaman değil:** systematic-debugging kuruluysa aynı rolde ikinci hata ayıklama skilli olarak.
- **Teknoloji:** git, node, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112071, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hata-ayiklama → alternatif · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kaliteli ve kısa (11 KB); hata tipine göre triyaj ve 'hata çıktısı talimat değildir' notu obra'da olmayan artılar. Aynı işi yaptığı için alternatif; addyosmani zinciri kullanan projelerde birincil yerine seçilebilir.

### systematic-debugging  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** superpowers'ın hata ayıklama skilli: 'kök neden bulunmadan düzeltme yok' demir yasasıyla dört faz (kök neden araştırması, desen analizi, hipotez ve test, uygulama); çok bileşenli sistemlerde sınırlara tanı günlüğü ekletme, 3 başarısız düzeltmeden sonra mimariyi sorgulama. Ek dosyalar: root-cause-tracing, defense-in-depth, condition-based-waiting (+ TS örneği) ve testleri kirleten testi bulan find-polluter.sh.
- **Ne zaman:** Her hata, test başarısızlığı, build kırılması veya beklenmeyen davranışta düzeltme önermeden önce; özellikle zaman baskısı ve ardışık başarısız düzeltmelerde. · **Ne zaman değil:** Kök nedeni zaten bilinen önemsiz yazım hataları; hata yokken genel kod incelemesi.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★309660, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** hata-ayiklama → birincil · **Roller:** kod-inceleyici
- **Boyut:** 40 KB (SKILL.md 9.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, hata-ayiklama grubunun birincili. Gerekçe (4 aday): obra'nın güncel sürümü ve yardımcı teknik dosyaları (find-polluter.sh, condition-based-waiting) en pratik araç setini veriyor. heyitsnoah sürümü aynı metnin eski bir kopyası (teknikleri SKILL.md içine gömülü) → alternatif; vudovn sürümü obra'dan kısaltılmış şablon → alternatif; addyosmani debugging-and-error-recovery eşdeğer kalitede ama aynı işi yapıyor → alternatif. Not: test-pressure-*.md ve CREATION-LOG.md skill geliştirme kalıntısı, çalışma anında okunmaz.

### systematic-debugging@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 71 (B)

- **Ne yapar:** obra/superpowers systematic-debugging'in claudesidian'daki kopyası: aynı dört faz ve demir yasa; kök neden izleme, stack trace ekleme, kirleten testi bulma ve dört katmanlı savunma tekniklerini ayrı dosya yerine SKILL.md içinde taşır.
- **Ne zaman:** Tek dosyalık (ek dosyasız) sürüm tercih edildiğinde; claudesidian kasası kullanan projeler. · **Ne zaman değil:** obra sürümü kuruluysa (aynı ad, aynı içerik); güncel superpowers değişikliklerini almak istendiğinde.
- **Teknoloji:** git, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** hata-ayiklama → alternatif
- **Boyut:** 13 KB (SKILL.md 12.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. İçerik iyi ama obra'nın eski sürümünden türetilmiş kopya; upstream ile senkron değil.

### systematic-debugging@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** ag-kit'in kısaltılmış hata ayıklama şablonu (obra/superpowers'tan uyarlanmış): yeniden üret, izole et, anla (5 Neden), düzelt ve doğrula fazları; kontrol listeleri ve temel git/grep/pm2 komutları.
- **Ne zaman:** ag-kit /debug iş akışında veya yalnız kısa bir hatırlatıcı yeterliyse. · **Ne zaman değil:** Genel kullanımda (obra sürümü çok daha güçlü); aynı adlı diğer sürümlerle birlikte.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** hata-ayiklama → alternatif
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF / SADECE ARŞİV. 2.5 KB şablon; demir yasa, çok bileşenli tanı ve 'üç düzeltmede dur' gibi asıl değerli kısımlar çıkarılmış.

### tdd-workflow  ·  vudovn/ag-kit @ 549ba3d  ·  puan 69 (B)

- **Ne yapar:** ag-kit'in TDD ilke özeti: RED-GREEN-REFACTOR döngüsü, TDD'nin üç yasası, her faz için kurallar, AAA, TDD'nin ne zaman değerli olduğu tablosu ve test yazan/kod yazan agent'ları ayıran çoklu agent deseni.
- **Ne zaman:** ag-kit iş akışı kullanan projelerde veya çok kısa bir TDD hatırlatıcısı yeterliyse. · **Ne zaman değil:** Gerçek uygulama rehberi gerektiğinde (test-driven-development); diğer TDD sürümleriyle birlikte.
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tdd → alternatif
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: ALTERNATİF / SADECE ARŞİV. 3 KB tablo özeti; 'testi çalıştırıp başarısızlığı gör' gibi uygulama adımları yok, iki birincil sürümün kapsadığı her şeyi daha zayıf veriyor.

### test-driven-development  ·  addyosmani/agent-skills @ aeac41d  ·  puan 100 (A)

- **Ne yapar:** Kırmızı-yeşil-refactor döngüsüyle geliştirme: önce projenin test yığınını keşfeder, başarısız test yazdırır, minimum kodla geçirtir, sonra temizletir. Hata düzeltmeleri için 'önce kanıtla' (hatayı yeniden üreten test) deseni, test piramidi ve test boyutları, davranışı test etme, DAMP, sahte yerine gerçek implementasyon, AAA ve DevTools ile tarayıcı testi rehberi içerir.
- **Ne zaman:** Mantık yazarken, hata düzeltirken veya davranış değiştirirken; kullanıcı test istemese de kod satır içi verilmiş olsa bile. · **Ne zaman değil:** Atılacak prototip/spike; salt yapılandırma veya üretilmiş kod; superpowers zincirinin katı 'test öncesi kodu sil' disiplini isteniyorsa (test-driven-development@obra).
- **Teknoloji:** api-anahtari, css, html, node, playwright, react, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112071, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tdd → birincil · **Roller:** backend-muhendis, frontend-muhendis, kod-inceleyici · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 16 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, tdd grubunun birincili. Gerekçe (3 sürüm karşılaştırması): addyosmani sürümü en kapsamlı ve yığından bağımsız (yığın keşfi, test piramidi/boyutları, prove-it deseni, mock disiplini, tarayıcı testi); tek başına kullanılabiliyor. obra sürümü daha kısa ama katı 'demir yasa' disipliniyle superpowers zincirine bağlı → alternatif. vudovn tdd-workflow yalnız ilke tablosu → alternatif. Not: superpowers skilleri 'test-driven-development' adını çağırır; bu sürüm o adı karşılar.

### test-driven-development@obra  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** superpowers'ın TDD skilli: 'başarısız test olmadan üretim kodu yok' demir yasası; testten önce yazılan kodu silip baştan başlatır, kırmızıyı ve yeşili mutlaka çalıştırıp gözlemletir, iyi/kötü test örnekleri, gerekçe-çürütme tablosu ve writing-good-tests.md ek rehberi sunar.
- **Ne zaman:** superpowers zinciri (writing-plans → subagent-driven-development / executing-plans) uçtan uca kullanılırken; agent'ın TDD'yi atlama eğilimine karşı en katı disiplin istendiğinde. · **Ne zaman değil:** addyosmani sürümü kuruluysa (aynı ad, aynı iş); test yığını keşfi ve test piramidi rehberi gerekiyorsa.
- **Teknoloji:** typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★309660, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** tdd → alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 17 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. İçerik kalitesi çok yüksek ve baskı testleriyle geliştirilmiş; birincilden farkı kapsam değil sertlik. Aynı adı taşıdığı için bir projede yalnız biri kurulmalı.

### test-value  ·  tt-a1i/archify @ 25cf370  ·  puan 96 (A)

- **Ne yapar:** Testlerin değerini ve geri bildirim maliyetini denetler: yavaş, kararsız, yinelenen veya kırılgan testleri bulur; uygulama sırasında hangi testin ekleneceğine/uyarlanacağına/silineceğine karar verdirir. Her yeni test için 'hangi somut hatayı yakalar, eşdeğer refactor'da da kırılır mı, başka bir kontrol zaten yakalıyor mu' sorularını şart koşar; AI'nın hem kodu hem testi aynı yanlış varsayımla yazma riskine dikkat çeker.
- **Ne zaman:** Test paketi yavaş/kararsız olduğunda denetim; commit/PR öncesi test değişikliklerini incelemek; başarısız bir kontrolün gerçek regresyon mu eskimiş assertion mı olduğunu ayırmak. · **Ne zaman değil:** Test yazma yöntemi öğretmek (test-driven-development); kapsam dışı depo geneli denetim (yalnız istenirse).
- **Teknoloji:** dil-bagimsiz, test-araclari
- **Claude / Codex:** tam / tam
- **Geliştirici:** tt-a1i (kisi, ★91956, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** test-degeri → birincil · **Roller:** kod-inceleyici
- **Boyut:** 19 KB (SKILL.md 9.4 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, test-degeri grubunun birincili. Archify'dan ama genel amaçlı (internal işaretli olsa da); test sayısı/kapsama yüzdesini kanıt olarak görüp ürün yargısını öne alması diğer test skillerinde yok. Yalnız ilgili davranışa odaklı kapsam kuralı bağlamı korur.

### testing-patterns  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Test ilkeleri özeti: test piramidi, AAA, birim/entegrasyon/E2E seçimi, iyi birim testi özellikleri, mock ne zaman/hangi tür (stub, spy, mock, fake), isimlendirme ve gruplama, test verisi stratejileri (factory, fixture, builder); test_runner.py betiği proje tipine göre testleri çalıştırır.
- **Ne zaman:** Test çerçevesi ve mock stratejisi seçerken hızlı başvuru; ag-kit kullanan projeler. · **Ne zaman değil:** TDD döngüsü veya test değeri kararları (test-driven-development, test-value bunları daha derin kapsar).
- **Teknoloji:** python · **Paketler:** python3 (test_runner.py)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tdd → alternatif
- **Boyut:** 10 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ama yüzeysel tablo özeti; içerik test-driven-development'ın 'Writing Good Tests' ve test piramidi bölümlerinde daha iyi var.

### verification-before-completion  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** 'Taze doğrulama kanıtı olmadan tamamlandı iddiası yok' kuralı: bir durum iddia etmeden önce kanıtlayan komutu belirle, tam çalıştır, çıktıyı ve çıkış kodunu oku, ancak sonra iddia et. Testler, lint, build, hata düzeltmesi, regresyon testi ve alt-agent raporları için neyin yeterli kanıt olduğunu tablolar.
- **Ne zaman:** İş bitti/düzeldi/geçti demeden önce; commit, PR veya alt-agent sonucunu kabul etmeden önce her zaman. · **Ne zaman değil:** Neredeyse hiçbir zaman gereksiz değildir; yalnız doğrulanacak çalıştırılabilir bir şey yoksa (salt doküman işi) etkisiz.
- **Teknoloji:** dil-bagimsiz
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★309660, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tamamlanma-dogrulama → birincil · **Roller:** backend-muhendis, frontend-muhendis, planlayici
- **Boyut:** 4 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, tamamlanma-dogrulama grubunun birincili. 4 KB ile en yüksek fayda/bağlam oranı; 'alt-agent başarılı dedi → bağımsız doğrula' maddesi orkestratör için kritik. verify-changes yürütme yöntemini, bu skill iddia disiplinini veriyor.

### verify-changes  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Kodun çalıştığını incelemeyle değil çalıştırarak kanıtlatır: değişen dosyaları ve beklenen davranışı belirle, değişiklik tipine göre doğrulama yöntemini seç (hata senaryosunu yeniden üret, endpoint çağır, bileşeni render et, build al), komutları çalıştır ve 'doğrulanamayanlar' bölümü olan kanıt raporu yaz. Web, API ve CLI için kontrol listeleri içerir.
- **Ne zaman:** Özellik/hata düzeltmesi bittikten sonra somut doğrulama planı ve rapor biçimi gerektiğinde; 'çalışıyor mu?' sorusunda. · **Ne zaman değil:** Yeni kod yazımı; yalnız iddia disiplini yeterliyse (verification-before-completion).
- **Teknoloji:** node, python
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8205, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** tamamlanma-dogrulama → tamamlayıcı
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı (opsiyonel). Değişiklik tipi → doğrulama yöntemi tablosu ve 'doğrulanamayanlar' raporu pratik; ilkesi verification-before-completion ile aynı, onun yanında yinelenen bağlam olabilir.
