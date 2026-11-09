# 08-onyuz-test-kalite — Tasarım ve Ön Yüz

_Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **7/12**

### agent-browser  ·  nexu-io/open-design @ 987b247  ·  puan 95 (A)

- **Ne yapar:** Browser automation CLI for AI agents. Use when the user needs to inspect, test, or automate browser behavior: navigating pages, filling forms, clicking buttons, taking screenshots, extracting page data, reading selected OpenDesign browser-tab context, testing web apps, dogfooding OpenDesign previews, QA, bug hunts, or reviewing app quality. Prefer local OpenDesign preview URLs unless the user expl
- **Teknoloji:** api-anahtari, css, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta)
- **İnceleme:** otomatik

### browser-testing-with-devtools  ·  addyosmani/agent-skills @ 301b02b  ·  puan 94 (A)

- **Ne yapar:** Chrome DevTools MCP ile ajana canlı tarayıcı gözü kazandırır: ekran görüntüsü, DOM, konsol, ağ istekleri, performans izi (LCP/CLS/INP), hesaplanmış stiller ve erişilebilirlik ağacı. UI/ağ/performans hata ayıklama akışları, test planı şablonu ve tarayıcı içeriğini güvenilmez veri sayan güvenlik sınırları içerir.
- **Ne zaman:** Çalışan sayfada konsol hatası, ağ sorunu, performans veya erişilebilirlik ağacı doğrulaması gerektiğinde (özellikle gerçek tarayıcı verisiyle). · **Ne zaman değil:** chrome-devtools MCP sunucusu kurulu değilse çalışmaz; yalnız backend/CLI işlerinde değil. Betikli, yeniden çalıştırılabilir E2E testi için webapp-testing / Playwright.
- **Teknoloji:** chrome-devtools-mcp, chrome, javascript · **Paketler:** chrome-devtools-mcp (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★113281, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** canli-tarayici-denetimi → birincil · **Roller:** qa-erisilebilirlik, frontend-muhendis · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 14 KB (SKILL.md 14.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). Hata ayıklama akışları somut ve güvenlik bölümü örnek niteliğinde (profil izolasyonu, DOM/konsol çıktısını talimat saymama, JS yürütmeyi salt-okunur tutma, kimlik bilgisi erişimi yasağı). Dikkat: `npx -y chrome-devtools-mcp@latest --isolated` sürümsüz uzak paket çalıştırır ve MCP kurulumu kullanıcıya bırakılmıştır; `--autoConnect` gerçek Chrome oturumlarını açar, skill bunu açıkça uyarıyor. Bu ortamda zaten playwright/Claude Browser MCP'leri olduğu için gerekirse işlev örtüşür. 14.2 KB. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### export-download-debugging  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Diagnose and fix browser, preview, or Electron export/download failures, especially image export issues involving Save As, Blob/Data URLs, the File System Access API, createWritable failures, and 0 KB files.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** otomatik

### impeccable-design-polish  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Follow-up design polish skill inspired by Impeccable. Use after a web or HTML artifact exists to audit, critique, polish, animate, harden, and prepare the page for a live/share pass.
- **Teknoloji:** css, gsap, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### playwright-component-testing  ·  microsoft/playwright @ 3b3ac25  ·  puan 98 (A)

- **Ne yapar:** Playwright ile React/Vue bileşenlerini 'hikâye galerisi' sayfası üzerinden, dahili `mount` fixture'ı ve düz Playwright testleriyle izole test etme kurulumu. Galeri sözleşmesi, tiplendirme, Vite entegrasyonu ve eski `@playwright/experimental-ct-react/-vue`'dan geçiş rehberi içerir.
- **Ne zaman:** Bileşenleri tarayıcıda ayrı ayrı (props, olay, görsel regresyon) test etmek veya experimental-ct'den geçmek için. · **Ne zaman değil:** Salt E2E akışları için değil (webapp-testing / playwright-cli); Playwright'sız projelerde ve React/Vue dışı çatılarda hazır şablon yok.
- **Teknoloji:** playwright, react, vue, vite, typescript · **Paketler:** @playwright/test, vite
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★99306, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** playwright-test-altyapisi → birincil · **Roller:** qa-erisilebilirlik
- **Boyut:** 38 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). Resmî Microsoft skill'i; kavram (hikâye + galeri + mount fixture) net ve geçiş yolu belgeli. Dikkat: galeri sayfasını (`references/gallery-spec.md`'ye göre) projede kendin yazman gerekir, hazır şablon yok; yeni bir Playwright sürümünü varsayar (mount fixture/`reuseContext`), eski sürümde çalışmayabilir. Next.js/webpack'te ayrı Vite sunucusu ekler (devDependency). 10.2 KB + 5 referans.

### playwright-trace  ·  microsoft/playwright @ 3b3ac25  ·  puan 100 (A)

- **Ne yapar:** Playwright trace (.zip) dosyalarını komut satırından inceler: eylem listesi, ağ istekleri, konsol, hatalar, DOM/erişilebilirlik anlık görüntüleri ve ekran görüntüleri; tarayıcı açmadan başarısız testi adım adım teşhis ettirir.
- **Ne zaman:** Başarısız bir Playwright testinin trace.zip'ini ajanla çözümlerken. · **Ne zaman değil:** Trace üretmek veya test yazmak için değil; trace yoksa işe yaramaz.
- **Teknoloji:** playwright · **Paketler:** playwright (npx playwright trace)
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★99306, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** playwright-test-altyapisi → tamamlayıcı · **Roller:** qa-erisilebilirlik
- **Boyut:** 5 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (opsiyonel). Kısa (4.7 KB), odaklı ve resmî; komutlar tutarlı ve tipik bir inceleme akışı veriyor. Dikkat: yalnızca `npx playwright trace` alt komutunu içeren yeni Playwright sürümlerinde çalışır; `allowed-tools: Bash(npx playwright trace:*)` ile kapsam sınırlı, ek kurulum/ağ yok.

### react-doctor  ·  darkroomengineering/satus @ 5cb0547  ·  puan 75 (B)

- **Ne yapar:** React kod tabanını güvenlik, performans, doğruluk, erişilebilirlik ve mimari açısından tarayıp 0-100 sağlık puanı veren `react-doctor` CLI'ının skill'i. Değişiklik sonrası `--diff` ile gerileme kontrolü, tam tarama ve `/doctor` ile uzaktan çekilen triyaj playbook'u akışı vardır.
- **Ne zaman:** React kodu bitirirken/commit öncesi puan gerilemesini yakalamak, lint-erişilebilirlik-bundle sorunlarını önceliklendirmek için. · **Ne zaman değil:** React olmayan projelerde değil. Ağdan talimat çekmek istemeyen/izole ortamlarda `/doctor` akışı kullanılmamalı.
- **Teknoloji:** react, next.js, eslint · **Paketler:** react-doctor (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** darkroomengineering (kurum, resmî, ★1012, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih · **Örtüşme:** react-kod-sagligi → birincil · **Roller:** frontend-muhendis
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel, uyarılı). Çekirdek kullanım (`npx react-doctor@latest --verbose --diff`) basit ve işe yarar. Dikkat (risk): `/doctor` akışı `curl https://www.react.doctor/prompts/react-doctor-agent.md` ile uzaktan talimat metni çekip 'her adımını izle' diyor ve çalışma ağacını düzenleten bir döngü başlatıyor; içerik üçüncü tarafça istenildiği an değişebilir (prompt-injection yüzeyi). `npx ...@latest` sürümsüz uzak paket çalıştırır. Referans verilen `doctor-explain` skill'i kütüphanede yok. Kullanılırsa yalnız yerel `--diff` komutu önerilir. Kaynak, satus başlangıç şablonunun içindeki kopya.

### web-design-guidelines  ·  vercel-labs/agent-skills @ 1a2c79d  ·  puan 84 (A)

- **Ne yapar:** Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel-labs (kurum, resmî, ★33547, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** ui-denetim-iyilestirme → birincil · **Globalde:** claude:ayni
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** otomatik
- **Not:** Vercel'in resmî kaynağı (OpenMontage kopyalarının güncel aslı).

### webapp-testing  ·  anthropics/skills @ ca45fc4  ·  puan 90 (A)

- **Ne yapar:** Yerel web uygulamalarını Python Playwright betikleriyle test etme araç seti: statik/dinamik karar ağacı, `with_server.py` ile bir veya birden fazla sunucunun yaşam döngüsü yönetimi, 'önce keşfet, sonra eyle' deseni ve networkidle beklemesi. Konsol günlüğü, öğe keşfi ve statik HTML otomasyonu için örnek betikler içerir.
- **Ne zaman:** Çalışan yerel uygulamada UI davranışını doğrulamak, ekran görüntüsü almak ve tarayıcı günlüklerini görmek için. · **Ne zaman değil:** MCP tabanlı canlı denetim (browser-testing-with-devtools) veya Node tarafı Playwright test koşucusu istiyorsan değil; erişilebilirlik denetimi yapmaz.
- **Teknoloji:** playwright, python · **Paketler:** playwright (pip)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★187417, son güncelleme 2026-10-28, lisans yok)
- **Durum:** tercih · **Örtüşme:** tarayici-otomasyon-testi → birincil · **Roller:** qa-erisilebilirlik
- **Boyut:** 22 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Küçük (3.8 KB), net karar ağacı; betikleri 'kara kutu' kullandırarak bağlamı koruyor. Dikkat: python `playwright` paketi ve tarayıcıların (`pip install playwright && playwright install chromium`) kurulu olduğunu varsayıyor ama bunu belirtmiyor. `with_server.py` verilen komutları `shell=True` ile çalıştırıyor (cd/&& desteği için; komutu kullanıcı/ajan verir, dış girdi değil). Registry 'lisans yok' diyor ama LICENSE.txt (Apache-2.0) mevcut.

### webapp-testing@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 78 (B)

- **Ne yapar:** anthropics/skills webapp-testing'in kopyası: Python Playwright ile yerel web uygulaması testi, with_server.py ve örnek betikler.
- **Ne zaman:** Yalnızca resmî kopya alınamazsa. · **Ne zaman değil:** Resmî kopya varken kullanma.
- **Teknoloji:** playwright, python · **Paketler:** playwright (pip)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78745, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** tarayici-otomasyon-testi → alternatif
- **Boyut:** 22 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. SKILL.md, scripts/ ve examples/ resmî kopyayla aynı (diff: yalnız KAYNAK.md ve LICENSE.txt). Dikkat: LICENSE.txt'te doldurulmamış şablon telif satırı.

### webapp-testing@github  ·  github/awesome-copilot @ 7e40881  ·  puan 100 (A)

- **Ne yapar:** Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
- **Teknoloji:** css, node, playwright, react _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** github (kurum, ★40799, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 5 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### webapp-testing@vudovn  ·  vudovn/ag-kit @ 549ba3d  ·  puan 76 (B)

- **Ne yapar:** Web testi ilkeleri (derin denetim, test piramidi, E2E, Playwright kavramları, görsel test, API test, CI) ve hafif `playwright_runner.py` betiği: URL'yi açar, ekran görüntüsü alır, temel erişilebilirlik kontrolü (alt, buton/link adı, input etiketi) ve konsol hatası raporu verir.
- **Ne zaman:** Hızlı bir sayfa duman testi ve temel erişilebilirlik kontrolü için; test stratejisi hatırlatması. · **Ne zaman değil:** Karmaşık akışlı testler ve sunucu yönetimi için değil (resmî webapp-testing).
- **Teknoloji:** playwright, python · **Paketler:** playwright (pip)
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8207, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** tarayici-otomasyon-testi → alternatif
- **Boyut:** 10 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Aynı adlı resmî skill'den farklı içerik (ilke ağırlıklı + tek betik). `--a11y` bayrağı resmî sürümde olmayan hafif bir erişilebilirlik kontrolü sağlıyor ama axe benzeri gerçek denetim değil. Dikkat: `pip install playwright && playwright install chromium` gerektirir (betik yoksa bunu söyler); ekran görüntülerini sistem temp klasörüne (`agkit_screenshots`) yazar. Betik yalnız http/https URL kabul ediyor.
