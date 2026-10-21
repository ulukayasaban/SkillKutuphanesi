# 01-repo-gelistirici-skilleri — Repo-İçi Geliştirici Skilleri (varsayılan listede gizli)

_Next.js, React, Playwright, Lighthouse, Motion repolarına KATKI yapanlar için iç süreç skilleri; kendi projelerinde nadiren gerekir_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **46/46**

### authoring-skills  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js repo'sunun .agents/skills/ altındaki skilleri nasıl yazdığını anlatır: desteklenen frontmatter alanları, iyi description yazımı (dosya adı + anahtar kelime), AGENTS.md ile skill arasındaki iş bölümü, isimlendirme ve hub+detay dosya yapısı.
- **Ne zaman:** Kendi projen veya kütüphanen için yeni SKILL.md yazarken/düzenlerken; description ve AGENTS.md ayrımına karar verirken. · **Ne zaman değil:** Next.js'e özel kural listesi değil, genel rehber; çok ayrıntılı skill-yazım süreci için d-ai-otomasyon/04 altındaki skill-creator türleri daha kapsamlı.
- **Teknoloji:** claude-code, agent-skills
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (genel kullanım). Kısa, doğru ve pratik; yalnızca örnekler Next.js'ten. Desteklenen alan listesi Claude Code'a göre, Codex bazı alanları yok sayar.
- **Not:** Kendi projende de işe yarar: skill/AGENTS.md yazım rehberi olarak doğrudan kullanılabilir.

### backport-pr  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js'te canary'ye birleşmiş bir PR'ı LTS sürüm dalına (releases/lts/active|maintenance) taşır: birleşme commit'ini bulur, sürüm dalından backport dalı açar, cherry-pick -x yapar, doğrular ve taslak PR açar.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. LTS dalına düzeltme taşırken. · **Ne zaman değil:** Kendi projelerinde: dal adları, PR başlık biçimi ve $create-pr bağımlılığı Next.js'e özel.
- **Teknoloji:** git, github-cli, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Güvenli adımlar (kullanıcı değişikliklerini koru, boş cherry-pick kontrolü) iyi; genel backport için şablon olarak okunabilir.

### compiler-commit  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React Compiler değişikliklerini /compiler-verify ve /compiler-review'dan geçirip [compiler] veya [rust-compiler] önekiyle commit'ler; Rust portu için orkestratör günlüğünü günceller.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. compiler klasöründe commit atarken. · **Ne zaman değil:** Diğer tüm projeler.
- **Teknoloji:** git, react-compiler, rust
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. compiler-verify/compiler-review ve repo içi alt-agent'lara bağlı; tek başına çalışmaz.

### compiler-orchestrator  ·  react/react @ ab0d927  ·  puan 83 (A)

- **Ne yapar:** React Compiler'ın TypeScript→Rust portunu döngü halinde ilerletir: sınırdaki geçişi bulur, hataları düzeltir, yeni geçişleri port eder, inceler ve commit'ler. 50+ geçişin sıralı tablosunu içerir.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. Rust portu üzerinde çalışırken. · **Ne zaman değil:** Diğer tüm projeler.
- **Teknoloji:** react-compiler, rust, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Uzun-süreli agent döngüsü örneği olarak ilginç; içerik tamamen porta özel (13 KB).

### compiler-port  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** Tek bir React Compiler geçişini TypeScript'ten Rust'a port eder: geçiş adını doğrular, TS dosyalarını ve hedef crate'i eşler, plan çıkarır, port-pass alt-agent'ıyla test-düzelt döngüsü yürütür, inceleme döngüsüyle bitirir.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. Rust portunda. · **Ne zaman değil:** Diğer tüm projeler.
- **Teknoloji:** react-compiler, rust, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Repo içindeki port-pass agent'ına bağımlı.

### compiler-review  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** Rust port kodunu orijinal TypeScript ile karşılaştırarak port sadakati, konvansiyon ve hata işleme açısından inceletir; diff'i repo içindeki compiler-review agent'ına verir.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. Rust port değişikliklerini incelerken. · **Ne zaman değil:** Genel kod incelemesi (b-yazilim-gelistirme/02 altındaki review skilleri).
- **Teknoloji:** react-compiler, rust
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. İnce sarmalayıcı; asıl mantık arşivde olmayan agent tanımında. 'React compiler review' adı yanıltıcı: React Compiler kullanan uygulamaları değil, compiler'ın Rust portunu inceler.

### compiler-verify  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React Compiler'da değişen kodu (TS mi Rust mı) tespit edip ilgili test, lint ve biçimlendirme komutlarını (yarn snap, test-rust-port.sh, prettier-all) sırayla çalıştırır.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. compiler commit'i öncesi. · **Ne zaman değil:** Diğer tüm projeler.
- **Teknoloji:** react-compiler, rust, yarn
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Net ve doğru, ama komutların hepsi repoya özel.

### create-pr  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js'te yerel değişikliği dal, commit, push ve taslak PR'a çevirir: <agent-adı>/ dal öneki, sadece ilgili dosyaları stage etme, canary tabanı, Summary/Verification PR gövdesi, fork PR politikası ve kurtarma adımları.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. PR açarken. · **Ne zaman değil:** Kendi projelerinde: canary tabanı, NEXT_JS_LLM işareti ve 'co-author ekleme' kuralı sana uymayabilir.
- **Teknoloji:** git, github-cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. PR gövdesi formatı (ne + neden + doğrulama) iyi bir örnek; genel git/PR akışı için b-yazilim-gelistirme/05 skilleri tercih edilmeli.

### dce-edge  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js iç kodunda webpack ölü kod elemesine (DCE) uygun require() kalıplarını ve edge runtime kısıtlarını anlatır: if/else zorunluluğu, TypeScript kesin atama, NEXT_RUNTIME'ın özellik bayrağı olmadığı, edge için bayrakları false'a zorlama.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. koşullu require/edge kodu yazarken. · **Ne zaman değil:** Uygulama geliştirme; Next.js kullanan bir sitede bu iç ayrıntılar gerekmez.
- **Teknoloji:** next.js, webpack, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Webpack DCE bilgisi genel olarak doğru ve öğretici, ama dosya yolları Next.js iç yapısına ait.

### deploy-release-test  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** Next.js PR'ının commit'e özel önizleme paketini doğrulayıp test_e2e_deploy_release.yml iş akışını gh ile elle tetikler; dal SHA'sının değişip değişmediğini tekrar kontrol eder ve oluşan run'ı doğrular.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. (yalnızca dahili dallar) tüm deploy test paketini çalıştırırken. · **Ne zaman değil:** Diğer projeler; fork dalları.
- **Teknoloji:** github-actions, github-cli, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Yarış durumlarına karşı dikkatli yazılmış; gizli anahtarlı workflow tetiklediği için başka yerde kullanılmamalı.

### docs-diagrams  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** Next.js dokümanlarındaki diyagram stilini (ızgara arka plan, gölgeli paneller, gri iskelet UI, anlamlı renk paleti) koddan üretir: el yazımı SVG primitif kütüphanesi (lib.mjs/gen.mjs), headless Chrome ile 2x açık/koyu PNG, kenar boşluğu ölçümü ve inceleme listesi. AI görsel üretimi yok.
- **Ne zaman:** Next.js docs'a diyagram eklerken; kendi dokümanların için tutarlı açık/koyu teknik diyagram üretmek istersen yöntem ve betikler uyarlanabilir. · **Ne zaman değil:** Mermaid/hızlı diyagram (c-dokuman-icerik/02 altındaki diyagram skilleri daha pratik); renk tokenları Next.js'e ait.
- **Teknoloji:** svg, node, headless-chrome, python
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: disable-model-invocation (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 59 KB (SKILL.md 11.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (uyarlanabilir). disable-model-invocation: true (sadece elle çağrılır). Betikli, ölçülebilir kalite kontrollü nadir bir docs-diyagram skili.
- **Not:** Kendi projende de işe yarar: SVG primitif + Chrome render + ölçüm yaklaşımı kendi docs diyagramlarına uyarlanabilir (tokenları değiştir).

### extract-errors  ·  react/react @ ab0d927  ·  puan 76 (B)

- **Ne yapar:** React'e yeni hata mesajı eklendiğinde yarn extract-errors çalıştırıp yeni hata kodlarını raporlar.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer tüm projeler.
- **Teknoloji:** yarn, react
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 0 KB (SKILL.md 0.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Üç satırlık komut hatırlatıcısı.

### feature-flags  ·  react/react @ ab0d927  ·  puan 92 (A)

- **Ne yapar:** React'in özellik bayrağı dosyalarını, @gate pragması ve gate() satır içi kullanımını, yeni bayrak ekleme ve __VARIANT__ (www/RN) testlerini anlatır; kanal farklarından doğan test hatalarını ayıklama adımları.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz. bayrak/test işlerinde. · **Ne zaman değil:** Kendi projendeki feature-flag sistemi için değil.
- **Teknoloji:** react, jest
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Açık tablo ve 'sık hatalar' bölümü iyi; flags ve test skilleriyle birlikte çalışır.

### fix  ·  motiondivision/motion @ a03a6da  ·  puan 91 (A)

- **Ne yapar:** Motion repo'sunda bir GitHub issue'yu, açık PR'ı ya da plans/ altındaki plan dosyasını birleşmeye hazır PR'a dönüştüren 'yürütücü' skill: önce başarısız test, sonra en küçük düzeltme, repo kapılarıyla doğrulama, PR açma. 'Plan spesifikasyondur' ve 'repro yoksa düzeltme yok' kuralları.
- **Ne zaman:** Motion'a katkıda; ayrıca improve skill'inin ürettiği plans/ dosyalarını başka bir projede uygulatırken (improve ile çift). · **Ne zaman değil:** Plan/issue olmadan serbest geliştirme. Yarn/Cypress/React 18-19 komutları Motion'a özel, uyarlamak gerekir.
- **Teknoloji:** git, github-cli, jest, cypress
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiondivision (kurum, resmî, ★34417, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (improve ile birlikte). Sağlam yürütücü disiplini (TDD, sadık raporlama, main'e commit yok). Doğrulama adımları Motion'a göre yazılmış.
- **Not:** Kendi projende de işe yarar: improve'un planlarını uygulatan yürütücü olarak; doğrulama komutlarını kendi projene göre değiştir.

### fix@react  ·  react/react @ ab0d927  ·  puan 76 (B)

- **Ne yapar:** React'te yarn prettier ve yarn linc ile biçim/lint düzeltir, kalan elle düzeltmeleri raporlar.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** yarn, prettier
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 0 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV (alternatif; aynı adlı fix'in tercihi Motion sürümü). Komut hatırlatıcısı.

### flags  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React'te yarn flags ile özellik bayraklarının kanallar (www, canary, experimental, RN…) arası durumunu gösterir, --diff ile karşılaştırır ve çıktıyı açıklar.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** yarn, react
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. feature-flags skill'inin yardımcısı.

### flags@vercel  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js'e deneysel özellik bayrağı eklemenin uçtan uca kablolamasını anlatır: config-shared.ts tipi, zod şeması, define-env ile derleme zamanı enjeksiyonu, çalışma zamanı env değişkeni ya da ayrı bundle varyantı kararı.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Next.js kullanan uygulamalar (next.config bayrağı açmak bu skill'i gerektirmez).
- **Teknoloji:** next.js, webpack, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV (alternatif; 'flags' adının tercihi React sürümü).

### flow  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React'te Flow tip denetimini doğru renderer ile (dom-node, native, fabric…) çalıştırır ve hataları dosya konumlarıyla raporlar.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Flow kullanmayan projeler.
- **Teknoloji:** flow, yarn
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV.

### gate-tests  ·  vercel/next.js @ 691ec2a  ·  puan 90 (A)

- **Ne yapar:** Next.js testlerinde it.skip / 'dev modda atla' gibi sahte-yeşil kalıplar yerine @gate / @force-gate yönergelerini kullanmayı öğretir: yönerge seçimi, koşul katmanları, test-ekseni fixture kalıbı, tuzaklar ve doğrulama komutları.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. test yazarken. · **Ne zaman değil:** Diğer projeler (yönerge Next.js test altyapısına ait). Fikir — bilinen hatayı atlamak yerine 'beklenen hata' olarak işaretlemek — genel olarak değerli.
- **Teknoloji:** jest, next.js
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 10.8 KB, yük orta) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. İyi gerekçelendirilmiş; 'fake-green' kavramı genel test kültürü için okunmaya değer.

### gh-stack  ·  vercel/next.js @ 691ec2a  ·  puan 99 (A)

- **Ne yapar:** GitHub'ın gh-stack eklentisiyle yığın (stacked) PR yönetir: yığın kurma, katman ekleme, push/submit/sync/rebase/merge; agent'lar için TTY'siz güvenli bayraklar tablosu, çoklu remote kuralları, yığın tasarımı ve sorun giderme referansları.
- **Ne zaman:** Herhangi bir GitHub reposunda büyük işi gözden geçirilebilir bağımlı PR'lara bölmek istediğinde (gh extension install github/gh-stack gerekir). · **Ne zaman değil:** Tek PR'lık küçük işler; gh-stack kurulu değilse.
- **Teknoloji:** git, github-cli, gh-stack
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 29 KB (SKILL.md 9.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (genel kullanım). Kaynağı GitHub (metadata author: github); Next.js repo'suna kopyalanmış. Agent'ların TUI'de takılmasını önleyen bayrak tablosu çok değerli.
- **Not:** Kendi projende de işe yarar: repo-bağımsız, herhangi bir GitHub projesinde stacked PR için.

### improve  ·  motiondivision/motion @ a03a6da  ·  puan 98 (A)

- **Ne yapar:** Bir kod tabanını kıdemli danışman gibi salt-okunur tarar (doğruluk, güvenlik, performans, test, teknik borç, bağımlılık, DX, doküman, yön) ve başka bir modelin/agent'ın sıfır bağlamla uygulayabileceği önceliklendirilmiş, kendi kendine yeterli planları plans/ altına yazar. Kaynak koda asla dokunmaz; isteğe bağlı execute varyantı ayrı worktree'deki yürütücüyü inceler.
- **Ne zaman:** Herhangi bir projede denetim/iyileştirme fırsatı bulma, yol haritası, başka agent'a devredilecek uygulama planları üretme. · **Ne zaman değil:** Hemen kod değişikliği istiyorsan (skill bilerek uygulamaz); çok küçük repolar.
- **Teknoloji:** git, github-cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** motiondivision (kurum, resmî, ★34417, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 39 KB (SKILL.md 12.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (genel kullanım). Yazarı shadcn (MIT); Motion repo'sunda barınıyor ama repo-bağımsız. Pahalı model planlar / ucuz model uygular ekonomisi, sır değeri yazmama kuralı ve plan şablonu güçlü.
- **Not:** Kendi projende de işe yarar: repo-bağımsız denetim + plan üretici; fix skill'i yürütücü olarak eşlik eder. mevcut-kod-iyilestirme profiline aday.

### insight-error-page  ·  vercel/next.js @ 691ec2a  ·  puan 82 (A)

- **Ne yapar:** Next.js dev overlay'deki 'insight' türü hata sayfalarını (errors/<slug>.mdx) yazar veya denetler: zorunlu sayfa yapısı, overlay FixCard verisiyle başlık/ID eşleşmesi, kopyalanabilir prompt kartları, terminoloji doğrulama ve Vercel teknik yazım üslubu.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. errors/ sayfaları için. · **Ne zaman değil:** Diğer projeler; 22 KB ile bağlam yükü yüksek.
- **Teknoloji:** next.js, mdx
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 22 KB (SKILL.md 21.6 KB, yük orta) · **Kırık bağlantı:** 5
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Çok ayrıntılı ve kaynak-zinciri disiplini iyi, ama tamamen Next.js'e özel ve büyük.

### lighthouse-verification  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 75 (B)

- **Ne yapar:** Lighthouse'ta değişiklik sonrası seçili mocha testleri, type-check, lint ve update:sample-json çalıştırmayı hatırlatır.
- **Ne zaman:** Sadece o repoya (GoogleChrome/lighthouse) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Lighthouse'u araç olarak kullanmak (performans denetimi) için değil.
- **Teknoloji:** yarn, mocha
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Kısa komut listesi.

### next-rspack  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** Next.js içindeki @next/rspack-core ve @next/rspack-binding paketlerinin bakımını anlatır: @rspack/core ve rspack_* crate sürüm yükseltme, rspack/ altındaki Rust toolchain, yerel derleme/bağlama ve NEXT_RSPACK kullanımı.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. rspack/ klasöründe. · **Ne zaman değil:** Rspack'i kendi projende kullanmak (bu skill paket bakımı içindir).
- **Teknoloji:** rspack, rust, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Kapsam sınırı (kök rust-toolchain Turbopack'e ait) açıkça belirtilmiş.

### plan-update  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React Compiler Rust portu için bir konunun tüm compiler geçişlerine etkisini 8 paralel alt-agent'la araştırıp plan dokümanını yerinde günceller.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler; paralel araştırma kalıbı için d-ai-otomasyon/02 orkestrasyon skilleri daha genel.
- **Teknoloji:** react-compiler, rust
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Paralel alt-agent fan-out örneği; analyze-pass-impact agent'ına bağımlı.

### playwright-cherry-pick  ·  microsoft/playwright @ 66070a1  ·  puan 84 (A)

- **Ne yapar:** Playwright'ta bir commit/PR'ı release-<sürüm> dalına cherry-pick edip 'cherry-pick(#pr): başlık' olarak yeniden adlandırır; asla kendiliğinden push etmez.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Kısa ve güvenli.

### playwright-dev  ·  microsoft/playwright @ 66070a1  ·  puan 91 (A)

- **Ne yapar:** Playwright geliştirme rehberine giriş: kütüphane mimarisi, API ekleme, MCP araçları ve CLI komutları, vendored bağımlılıklar, WebKit/WebView, sürümler arası bisect ve dashboard için repo içi rehberlere bağlantı verir.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Playwright ile test yazmak (a-tasarim-onyuz/08 ve b-yazilim-gelistirme/03 skilleri).
- **Teknoloji:** playwright, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 95 KB (SKILL.md 1.3 KB, yük kucuk) · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Hub + 9 ayrıntı dosyası (library, api, tools, vendor, bisect, webview…) arşivde mevcut; yalnızca AGENTS.md bağlantısı repo dışında kalıyor.

### playwright-devops  ·  microsoft/playwright @ 66070a1  ·  puan 84 (A)

- **Ne yapar:** Playwright CI başarısızlık analizi ve sürüm operasyonları için repo içi rehberlere (commit-failures.md, fetch-commit-logs.sh) yönlendirir.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** github-actions, github-cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 0.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. SKILL.md ince bir dizin; asıl içerik commit-failures.md ve fetch-commit-logs.sh dosyalarında (arşivde mevcut).

### playwright-release-notes  ·  microsoft/playwright @ 66070a1  ·  puan 82 (A)

- **Ne yapar:** Playwright sürüm notlarını yazar: Node.js notları + Python/Java/.NET çevirileri (dile özgü API adları, langs filtreleri), dokümantasyon link makroları ve her dil için GitHub release markdown'ı.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Kendi projenin changelog'u (genel sürüm notu skilleri daha uygun).
- **Teknoloji:** playwright, markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 13 KB (SKILL.md 13.3 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Çok dilli doküman çevirisinin titiz bir örneği; tamamen repoya özel (13 KB).

### playwright-test-results  ·  microsoft/playwright @ 66070a1  ·  puan 91 (A)

- **Ne yapar:** Playwright CI test sonuçlarını toplanmış DuckDB veritabanından SQL ile sorgular: flaky testler, hata oranları, yavaş testler, run/SHA/PR bazında sonuçlar; GitHub API bütçesini korumak için veritabanını silmeme kuralı.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Kendi CI'ın (şema ve CLI repoya özel). Fikir — CI sonuçlarını parquet/DuckDB'ye toplamak — uyarlanabilir.
- **Teknoloji:** duckdb, node, github-actions
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.7 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Şema tablosu ve örnek sorgular iyi.

### playwright-triage  ·  microsoft/playwright @ 66070a1  ·  puan 90 (A)

- **Ne yapar:** Playwright hata raporunu sınıflandırır (bug, özellik isteği, upstream, soru) ve bug'ı tip-of-tree üzerinde, tarayıcılar arası, gerekirse sürüm bisect ederek yeniden üretir; amaç düzeltme değil doğrulanmış durum raporu.
- **Ne zaman:** Sadece o repoya (microsoft/playwright) katkı yaparken; kendi projende komut/yol adları tutmaz. issue triage'ında. · **Ne zaman değil:** Kendi projendeki issue'lar için doğrudan değil; yöntem (önce sınıflandır, ToT'ta dene, kabul testi yaz) uyarlanabilir.
- **Teknoloji:** playwright, github-cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** microsoft (kurum, resmî, ★98228, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.3 KB, yük orta) · **Kırık bağlantı:** 4
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Triage yöntemi iyi; kardeş playwright-dev skill'indeki bisect rehberine bağlı, test dosyası bağlantıları repo dışında kalıyor.

### pr-status-triage  ·  vercel/next.js @ 691ec2a  ·  puan 84 (A)

- **Ne yapar:** Next.js PR'ının CI hatalarını ve inceleme yorumlarını scripts/pr-status.js ile toplar; build > lint > types > test öncelik sırası, bilinen flaky test ayrımı, CI ortamıyla yerel yeniden üretim ve thread yanıtla-çöz komutları.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler (pr-status.js betiği yok).
- **Teknoloji:** github-cli, next.js
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 3.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Öncelik sırası genel olarak iyi bir pratik; workflow.md ve local-repro.md arşivde mevcut, pr-status.js betiği repoda.

### react-sync  ·  vercel/next.js @ 691ec2a  ·  puan 84 (A)

- **Ne yapar:** Yerel React değişikliklerini Next.js'in kullandığı bundle varyantlarında derler, pnpm sync-react ile yerel Next.js checkout'una aktarır ve entegrasyonu test eder; Codex PATH/Corepack hatasına çözüm içerir.
- **Ne zaman:** react/react ve vercel/next.js'e birlikte katkı yaparken. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** react, next.js, pnpm
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. scripts/build-for-next.sh arşivde mevcut; iki repo checkout'u gerektirir.

### react-vendoring  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js'in React'i App Router için nasıl vendor'ladığını ve react-server katman sınırlarını anlatır: entry-base.ts sınırı, kanal ayrımı, $$compiled.internal.d.ts tip bildirimleri, Turbopack remap ve ComponentMod erişimi.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Next.js ile uygulama geliştirme.
- **Teknoloji:** next.js, react, typescript
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. İç mimariyi anlamak için değerli not.

### router-act  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** Next.js e2e testlerinde createRouterAct ve LinkAccordion ile prefetch/navigasyon isteklerinin zamanlamasını kontrol etmeyi ve yanıtlarını doğrulamayı öğretir; 'no-requests' iddiası, sahte saat, flaky kalıplardan kaçınma.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. router testlerinde. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** next.js, playwright, typescript
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Retry/polling yerine deterministik act ilkesi genel test kültürü için iyi örnek.

### runtime-debug  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js runtime-bundle ve modül çözümleme gerilemelerini ayıklama akışı: CI env değişkenlerini aynalama, __NEXT_SHOW_IGNORE_LISTED ile tam yığın izi, nft.json trace incelemesi, webpack stats diff'iyle dahil edilme kanıtı.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Uygulama hatası ayıklama (b-yazilim-gelistirme/03).
- **Teknoloji:** next.js, webpack
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. webpack stats ile 'neden dahil edildi' kanıtı kendi Next.js uygulamanda bundle şişmesi araştırırken de fikir verebilir.

### rust-port-status  ·  react/react @ ab0d927  ·  puan 76 (B)

- **Ne yapar:** React Compiler Rust port plan dokümanlarının durumunu ve ilgili son commit'leri tablo halinde gösterir.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** git, react-compiler
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV.

### sandbox-bench  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** React veya Next.js revizyonlarını Vercel Sandbox VM'lerinde eşleştirilmiş A/B istatistikle ölçer (rps, gecikme, p95, TTFB, RSS, Flight byte); doğruluk kapıları, içerik-adresli önbellek, boot düzeyinde güven aralıkları. Faturalanan Vercel takım/proje bilgisini asla tahmin etmez.
- **Ne zaman:** react/react ya da vercel/next.js değişikliklerinin sunucu tarafı performans etkisini ölçerken. · **Ne zaman değil:** Kendi uygulamanın performansı (b-yazilim-gelistirme/06); Vercel Sandbox erişimi yoksa. Faturalı kaynak kullanır.
- **Teknoloji:** vercel-sandbox, node, next.js, react
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 160 KB (SKILL.md 16.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. İstatistik yaklaşımı (boot = replikasyon birimi) örnek niteliğinde; 16 KB, betikli.

### test  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React çekirdek testlerini kanal (source, experimental, www, stable, classic) ve __VARIANT__ seçenekleriyle doğru yarn komutuna çevirip çalıştırır; --silent ve --no-watchman zorunlu.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** jest, yarn
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV.

### update-ard-port  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 90 (A)

- **Ne yapar:** Lighthouse'un Agentic Resource Discovery (ARD) uygunluk portunu upstream ards-project/ard-spec ile 1:1 eşitler: değişen dosyaların karşılaştırması, şema senkronu, mesaj metinlerini kelimesi kelimesine koruma, hash'li inceleme kaydı ve testler.
- **Ne zaman:** Sadece o repoya (GoogleChrome/lighthouse) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** node, json-schema
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 8.6 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. Vendored kodu upstream'le senkron tutmanın iyi belgelenmiş örneği.

### update-docs  ·  vercel/next.js @ 691ec2a  ·  puan 92 (A)

- **Ne yapar:** Next.js'te dal değişikliklerine göre etkilenen dokümanları bulur (kaynak→doküman eşleme tablosu), mevcut MDX'i okuyup güncellemeyi kullanıcı onayıyla yürütür, yeni özellik için iskelet açar ve pnpm lint ile doğrular.
- **Ne zaman:** Sadece o repoya (vercel/next.js) katkı yaparken; kendi projende komut/yol adları tutmaz. docs/ altında. · **Ne zaman değil:** Kendi projen: eşleme tablosu ve MDX kuralları Next.js'e ait; 'kod değişince docs etkisini bul' akışı uyarlanabilir.
- **Teknoloji:** next.js, mdx, git
- **Claude / Codex:** tam / tam
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 21 KB (SKILL.md 7.4 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: SADECE ARŞİV. references/ klasörüyle birlikte eksiksiz.

### update-trace-engine  ·  GoogleChrome/lighthouse @ d94c35d  ·  puan 82 (A)

- **Ne yapar:** Chrome DevTools'un trace işlemcisini @paulirish/trace_engine paketi olarak derleyip yayınlar ve Lighthouse'a aktarır: devtools-frontend birleştirme, gn/autoninja derleme, shim'ler, sürüm artırma ve npm yayını.
- **Ne zaman:** Sadece o repoya (GoogleChrome/lighthouse) katkı yaparken; kendi projende komut/yol adları tutmaz. (paket bakımcıları). · **Ne zaman değil:** Diğer herkes; npm publish yetkisi gerektirir.
- **Teknoloji:** node, npm, devtools
- **Claude / Codex:** tam / tam
- **Geliştirici:** GoogleChrome (kurum, resmî, ★30922, son güncelleme 2026-10-21, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Çok kişiye özel (Paul Irish'in fork'u, yerel yollar).

### v8-jit  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** V8 JIT optimizasyon kalıpları: Ignition→Sparkplug→Maglev→Turbofan katmanları, hidden class/shape tutarlılığı, monomorfik çağrı noktaları, inline cache, megamorfik deopt, closure tahsisi, dizi paketleme ve --trace-opt/--trace-deopt ile profilleme.
- **Ne zaman:** Node.js/JS'te sıcak yol (istek başına çalışan kod, render, stream, döngü) performansı yazarken veya incelerken; kendi Node sunucularında da geçerli. · **Ne zaman değil:** Sıradan uygulama kodu; ölçmeden mikro-optimizasyon. Örnek dosya yolları Next.js'e ait.
- **Teknoloji:** javascript, node, v8
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: user-invocable (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 14 KB (SKILL.md 14.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (genel kullanım). İçerik %90 genel V8 bilgisi; yalnızca örnek bağlamı Next.js. 14 KB, bağlam yükü orta.
- **Not:** Kendi projende de işe yarar: Node/JS sıcak yol performans incelemesi için genel V8 rehberi.

### verify  ·  react/react @ ab0d927  ·  puan 84 (A)

- **Ne yapar:** React katkı gereksinimlerinin tamamını doğrular: önce prettier ve linc, sonra alt-agent'larla paralel /flow, /test ve /test www; hata olursa durup öneriyle raporlar.
- **Ne zaman:** Sadece o repoya (react/react) katkı yaparken; kendi projende komut/yol adları tutmaz.. · **Ne zaman değil:** Diğer projeler.
- **Teknoloji:** yarn, jest, flow
- **Claude / Codex:** tam / tam
- **Geliştirici:** react (kurum, resmî, ★251616, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. flow ve test skillerine bağlı.

### write-api-reference  ·  vercel/next.js @ 691ec2a  ·  puan 91 (A)

- **Ne yapar:** Next.js API'leri (fonksiyon, bileşen, dosya konvansiyonu, direktif, config) için tek API'lik referans sayfası üretir: kategoriye göre şablon, TS/JS switcher örnekleri, Reference/Behavior/Examples bölümleri ve yazım kuralları.
- **Ne zaman:** Next.js docs'a katkı; ayrıca kendi kütüphanen/framework'ün için API referans sayfası yazarken şablon olarak. · **Ne zaman değil:** Uzun anlatımlı rehber (write-guide); Next.js'e özel frontmatter ve switcher sözdizimi uyarlama ister.
- **Teknoloji:** mdx, markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (uyarlanabilir). Kategori bazlı şablonlar ve 'sayfa başına tek API' kuralı genel geçer. context: fork + agent: Plan alanları Claude Code'a özgü.
- **Not:** Kendi projende de işe yarar: kendi kütüphanenin API referans dokümanı için şablon (Next.js docs yazım tarzı).

### write-guide  ·  vercel/next.js @ 691ec2a  ·  puan 100 (A)

- **Ne yapar:** Gerçek bir kullanım senaryosunu aşamalı örneklerle öğreten teknik rehber yazar: giriş → örnek → 2-4 adım (çalışan kod → yeni gereksinim → sürtünme → açıklama → çözüm → gözlemlenebilir kanıt) → sonraki adımlar; em dash yok, satış dili yok, SEO için eski terimle köprü.
- **Ne zaman:** Next.js docs; ayrıca kendi ürünün/kütüphanen için tutorial/how-to rehberi yazarken. · **Ne zaman değil:** API referansı (write-api-reference); pazarlama metni.
- **Teknoloji:** mdx, markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: agent, context (Codex bunları yok sayar)
- **Geliştirici:** vercel (kurum, resmî, ★143121, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 6.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (genel kullanım). Next.js docs ekibinin yazım ilkeleri; 'sürtünme anında kavramı adlandır' döngüsü her teknik rehbere uygulanabilir.
- **Not:** Kendi projende de işe yarar: teknik rehber/tutorial yazımı (Next.js docs tarzı). Docs yazarı rolüne aday.
