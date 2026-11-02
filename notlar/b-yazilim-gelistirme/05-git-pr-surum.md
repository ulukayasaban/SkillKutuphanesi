# 05-git-pr-surum — Yazılım Geliştirme

_Git, worktree, PR, sürüm/release, changelog_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **6/10**

### changelog-generator  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 70 (B)

- **Ne yapar:** Git commit geçmişini tarayıp değişiklikleri kategorilere (yeni özellik, iyileştirme, düzeltme, kırıcı değişiklik, güvenlik) ayırır, iç commit'leri eler ve teknik mesajları son kullanıcının anlayacağı sürüm notlarına çevirir; isteğe bağlı stil rehberi dosyası okur.
- **Ne zaman:** Sürüm notları, haftalık/aylık ürün güncellemesi, app store değişiklik metni veya herkese açık changelog sayfası hazırlarken. · **Ne zaman değil:** Geliştirici odaklı Keep a Changelog bakımı (release / git-workflow-and-versioning); commit mesajları anlamsızsa sonuç zayıf.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78523, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** surum-yayini → tamamlayıcı
- **Boyut:** 3 KB (SKILL.md 3.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT, tamamlayıcı. Kısa (3 KB) ve tek amaçlı; 'kullanıcı diline çevir' odağı diğer git skillerinde yok. İçerik çoğunlukla örnek; kategori kuralları yüzeysel.

### deprecation-and-migration  ·  addyosmani/agent-skills @ 301b02b  ·  puan 98 (A)

- **Ne yapar:** Eski sistem, API veya özellikleri kaldırma ve kullanıcıları yeni uygulamaya taşıma: 'kod bir yüktür' ve Hyrum yasası ilkeleri, kaldırma kararı, zorunlu/öneri niteliğinde kullanımdan kaldırma, yerini yap → duyur → kademeli taşı → kaldır süreci; strangler, adapter ve feature flag geçiş desenleri, üretimde kesintisiz şema migrasyonu (expand/contract) ve zombi kod.
- **Ne zaman:** Bir API/özelliği emekliye ayırırken; kullanıcıları yeni sisteme taşırken; üretimde kolon yeniden adlandırma/silme gibi kesintisiz şema değişikliğinde; bakım mı emeklilik mi kararında. · **Ne zaman değil:** Yeni özellik geliştirme; sürüm/tag işlemleri (git-workflow-and-versioning).
- **Teknoloji:** sql
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kullanimdan-kaldirma → birincil · **Roller:** backend-muhendis · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 13 KB (SKILL.md 12.5 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT. Bu konudaki tek skill; expand/contract ve strangler desenleri pratik. Git/PR değil yaşam döngüsü konusu olduğu için kategorisi tartışılabilir, ama 'sürüm' kapsamında 05'te bırakıldı.

### finishing-a-development-branch  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** Uygulama bittiğinde işi nasıl birleştireceğine karar verdirir: tam test paketini çalıştır (kırmızıysa dur), ortamı (normal repo / worktree / detached HEAD) algıla, temel dalı doğrulat, sabit seçenek menüsü sun (yerelde birleştir, push + PR, olduğu gibi bırak), seçimi uygula ve worktree'yi kökenine göre güvenle temizle. İşi atma yalnız açık istekle.
- **Ne zaman:** Tüm testler geçtikten sonra dalı birleştirme/PR/bekletme kararı ve worktree temizliği. · **Ne zaman değil:** Testler kırmızıyken; ekip PR'ları başka bir araçla yönetiyorsa.
- **Teknoloji:** git, gh · **Paketler:** gh CLI (PR seçeneği için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dal-bitirme → birincil · **Roller:** planlayici
- **Boyut:** 8 KB (SKILL.md 7.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, dal-bitirme grubunun birincili. Gerekçe: kullanıcıya karar bırakan sabit menü, temel dal doğrulaması ve kökene dayalı worktree temizliği ile en güvenli kapanış; pull-request (heyitsnoah) onaysız push eğilimli tek komut → alternatif.

### git-workflow-and-versioning  ·  addyosmani/agent-skills @ 301b02b  ·  puan 100 (A)

- **Ne yapar:** Git iş akışı disiplini: trunk tabanlı geliştirme, erken ve sık commit, atomik commit ve açıklayıcı mesajlar, konuları ayırma, değişiklik boyutu, dal stratejisi ve isimlendirme, worktree ile paralel iş, 'kayıt noktası' deseni, değişiklik özetleri, commit öncesi hijyen, üretilmiş dosyalar, git ile hata ayıklama (bisect), semantik sürümleme, tag'i doğruluk kaynağı yapma ve insanlar için changelog.
- **Ne zaman:** Her kod değişikliğinde commit/dal/PR düzeni; karışık çalışma ağacını temiz atomik commit'lere bölmek; sürüm numarası seçmek ve release kesmek. · **Ne zaman değil:** Ekibin farklı ve yazılı bir git akışı (ör. git-flow) varsa çatışabilir; salt worktree kurulumu (using-git-worktrees).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** addyosmani (kisi, ★112570, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** git-is-akisi → birincil · **Roller:** backend-muhendis, devops-muhendis · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 14 KB (SKILL.md 14.1 KB, yük orta)
- **İnceleme:** yeniden-incelenecek · kalite 5/5 — Karar: TUT, git-is-akisi grubunun birincili. Kapsamlı ama 14 KB; atomik commit ve 'kayıt noktası' kuralları agent'ların büyük, karışık commit'lerini önlüyor; semver ve changelog bölümü release skillerinin temelini de veriyor.

### git-worktrees  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 64 (C)

- **Ne yapar:** git worktree komut başvurusu: oluşturma (yeni/var olan dal), .worktrees/ dizin düzeni, kurulum sonrası adımlar (bağımlılık, env dosyası), commit edilmemiş değişiklik varken silmeme kuralı, kaldırma karar matrisi ve temizlik/prune.
- **Ne zaman:** Elle worktree yönetimi, PR incelemesi için ayrı checkout veya birleşme sonrası temizlik komutları gerektiğinde. · **Ne zaman değil:** Agent iş akışında yalıtım kurulumu (using-git-worktrees daha güvenli ve harness farkında).
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** worktree → alternatif
- **Boyut:** 4 KB (SKILL.md 4.3 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Doğru ve kısa komut başvurusu; mevcut worktree'yi algılama veya yerel araç tercih etme yok. '.env kopyala' önerisi gizli bilgiyi çoğaltabilir.

### pr-feedback-quality-gate  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Safely track pull request feedback, resolve review comments or merge conflicts, validate fixes, and use a read-only cross-review before committing or pushing follow-up changes.
- **Teknoloji:** git _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### pull-request  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 64 (C)

- **Ne yapar:** Tek komutla PR akışı: önkoşulları kontrol eder (git, gh), başlıktan dal adı üretir, değişiklikleri gösterip onay ister, conventional commit mesajıyla commit eder, push eder ve özet/değişiklikler/test listesi içeren gövdeyle gh pr create çalıştırır.
- **Ne zaman:** Kullanıcı açıkça 'PR aç' dediğinde hızlı dal + commit + push + PR. · **Ne zaman değil:** Kullanıcı birleştirme yöntemini henüz seçmediyse (finishing-a-development-branch); push'un onay gerektirdiği ortamlar; değişiklikler zaten bir dalda düzenliyse.
- **Teknoloji:** git, gh · **Paketler:** gh CLI (oturum açık)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** dal-bitirme → alternatif
- **Boyut:** 5 KB (SKILL.md 4.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kullanışlı ama 'staged yoksa git add -A' ve sabit 'Generated with Claude Code' imzası körlemesine; push ve PR dışa dönük eylem, yalnız kullanıcı isteğiyle çalışmalı.

### release-notes-one-pager  ·  nexu-io/open-design @ 987b247  ·  puan 96 (A)

- **Ne yapar:** Release notes one-page HTML with highlights, Added, Fixed, Breaking changes, Known issues, and Upgrade note. Writes explicit "None" style sections whenever the user does not provide details.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105353, son güncelleme 2026-11-02, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 41 KB (SKILL.md 3.7 KB, yük kucuk)
- **İnceleme:** otomatik

### release@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 64 (C)

- **Ne yapar:** Release akışını otomatikleştirir: son tag'den beri commit'leri analiz edip (BREAKING/feat/fix) sürüm artışını belirler, package.json sürümünü günceller, CHANGELOG.md'deki Unreleased bölümünü yeni sürüme taşır, commit + annotated tag atar, push eder ve gh release create ile GitHub sürümü yayınlar.
- **Ne zaman:** package.json ve CHANGELOG.md (Keep a Changelog) kullanan Node projelerinde sürüm kesmek. · **Ne zaman değil:** package.json olmayan projeler (Python, Rust…); sürüm otomasyonu CI'da (release-please, changesets) yapılıyorsa; push/yayın onayı alınmadan.
- **Teknoloji:** git, gh, node · **Paketler:** gh CLI (oturum açık)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2607, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** tercih · **Örtüşme:** surum-yayini → birincil
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (opsiyonel, --skill ile). Sürüm artış kuralları net; ancak push ve GitHub release yayını geri alınması zor dışa dönük eylemler, skill bunları onay adımı olmadan zincirliyor. Yalnız Node/package.json varsayımı.

### using-git-worktrees  ·  obra/superpowers @ 2ce8aa1  ·  puan 100 (A)

- **Ne yapar:** İşin yalıtılmış bir çalışma alanında yapılmasını sağlar: önce zaten bir worktree içinde olunup olunmadığını (alt modül korumasıyla) tespit eder, kullanıcı onayı ister, platformun yerel worktree aracını (EnterWorktree, /worktree…) tercih eder, yoksa git worktree'ye düşer; proje kurulumu yapıp temiz test tabanını doğrular.
- **Ne zaman:** Yalıtım gerektiren özellik işine başlarken veya bir uygulama planını yürütmeden önce (superpowers zinciri). · **Ne zaman değil:** Zaten harness tarafından yönetilen bir worktree'deyken (skill bunu kendisi algılar); tek dosyalık hızlı düzeltmeler.
- **Teknoloji:** git
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★310663, son güncelleme 2026-10-29, lisans MIT)
- **Durum:** tercih · **Örtüşme:** worktree → birincil · **Roller:** planlayici
- **Boyut:** 7 KB (SKILL.md 6.7 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT, worktree grubunun birincili. Gerekçe: 'harness ile kavga etme' ilkesi, var olan yalıtımı algılama, alt modül koruması ve onay adımı; Claude Code/Codex worktree araçlarıyla uyumlu. heyitsnoah git-worktrees yalnız komut başvurusu → alternatif.
