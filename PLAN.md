# Skill Kütüphanesi — Sürdürülebilir ve Mükerrersiz Yapı Planı

> Durum: **UYGULANDI (2026-10-21)** — güncel kullanım için `README.md` ve `rehber/` klasörüne bak. Bu dosya karar geçmişi olarak duruyor.
> Uygulamada eklenenler: OpenMontage ve repo-içi skiller de arşivde; `g-video-ses-medya` alanı; Claude/Codex araç sürümleri;
> kapsam denetimi; ön kontrol + yedek + geri alma; geliştirici bilgisi ve değerlendirme puanı. Sürüm 3
> Konum: `~/Documents/SkillKutuphanesi`
> Kaynaklar: GitHub'da yıldızlanan **49 reponun tamamı** (2 liste + listesiz 10 repo)
> Kapsam: Tüm konular; 5 ana alan (tasarım, yazılım geliştirme, doküman/içerik, AI/otomasyon, entegrasyon kataloğu).
> Not: Bölüm 6'daki 14 kategorilik tablo ilk taslaktır; geçerli yapı bölüm 5'teki 5 alan / 23 alt kategoridir.

---

## 1. Hedef

1. **Kaybetmemek:** Listedeki skillerin tam kopyası, hangi commit'ten geldiği bilinerek bu klasörde arşivlenir.
2. **Tekrar yok:** Aynı skill bir kez durur. Aynı konuyu anlatan farklı skiller için "hangisi tercih edilir" kararı bir kez verilir ve yazılır.
3. **Konuya göre düzen:** Skiller kategorilere ayrılır, her kategori bir kez sistemli şekilde incelenir, Türkçe not alınır.
4. **Projeye göre dağıtım:** Yeni projede proje tipi ve agent rolleri seçilir; sadece gereken skiller o projeye kopyalanır. **Global kurulum yok.**
5. **Claude + Codex:** Aynı proje klasörü iki araçta da aynı skilleri görür.
6. **Sürdürülebilirlik:** Repolar güncellenince, listeye yeni repo eklenince, yapı tek komutla güncel kalır; projeler hangi sürümü kullandığını bilir.

---

## 2.0 TÜM STAR'LAR — envanter ve boyut (Sürüm 3, 2026-10-21 ölçümü)

Kapsam artık **yıldızladığın 49 reponun tamamı** (2 listedeki 39 repo + listede olmayan 10 repo).

### Boyut özeti
| Senaryo | Boyut |
|---|---|
| 49 repoyu git geçmişiyle tam klonlamak | **10.7 GB** ❌ yapılmayacak |
| Sadece güncel dosyalar (geçmişsiz) | 2.2 GB ❌ gereksiz |
| Tüm skill klasörleri (ham, tekrarlar dahil) | 165 MB |
| Tüm skill klasörleri, tekrarsız | 101 MB |
| OpenMontage hariç (zaten `~/.openmontage`'da kurulu, 50 MB) | 51 MB |
| + demo videoları / örnek render HTML'leri hariç | **≈ 38 MB** ✅ önerilen arşiv |

### Skill sayısı
| | Sayı |
|---|---|
| Bulunan SKILL.md | 1366 |
| Tekil içerik | 1229 |
| OpenMontage hariç tekil | 1143 |
| Bunun içinde Composio uygulama-entegrasyon skilleri | 832 |
| → **Gerçek, birbirinden farklı "iş yapan" skill** | **≈ 310** |

### Repoların 5 tipe ayrılması
| Tip | Repolar | Ne yapılır |
|---|---|---|
| **T1 — Skill koleksiyonu** (ana kaynak) | anthropics/skills, obra/superpowers, addyosmani/agent-skills, vudovn/ag-kit, heyitsnoah/claudesidian, ComposioHQ/awesome-claude-skills (genel kısım), nextlevelbuilder/ui-ux-pro-max-skill, freshtechbro/claudedesignskills, CloudAI-X/threejs-skills, greensock/gsap-skills, pbakaus/impeccable, Leonxlnx/taste-skill, nateherkai/scroll-craft, zanwei/design-dna, tt-a1i/archify, Panniantong/Agent-Reach, teng-lin/notebooklm-py | Tam arşiv + inceleme + kategori |
| **T2 — Ürünün kullanıcıya verdiği skiller** | vercel/next.js (`skills/next-*` 6 adet), microsoft/playwright (playwright-cli, component-testing, trace), anthropics/claude-code (frontend-design, plugin-dev 7 skill, hookify…), darkroomengineering/satus (react-doctor) | Sadece bu skiller arşive |
| **T3 — Repo-içi geliştirici skilleri** | next.js `.agents/` (21), react (14), playwright `.claude/` (6), lighthouse (3), motion (2) — o repoya katkı yapanlar için | Arşivlenmez; katalogda tek satır not |
| **T4 — Entegrasyon kataloğu** | Composio `composio-skills/` (832 uygulama: Gmail, Slack, Notion… Composio API anahtarı gerektirir) | Arşivlenir (~8 MB) ama "sadece-arşiv" katmanı; varsayılan listede görünmez, `--entegrasyon <uygulama>` ile aranır |
| **T5 — Kütüphane / araç (skill yok)** | three.js, GSAP, motion, lenis, r3f, drei, tailwind, lottie, lighthouse, axe-core, playwright, FFmpeg, fontsource, capsize, open-props, ogl, partytown, size-limit, number-flow, r3f-scroll-rig, react-three-a11y, figma/code-connect, pixeljury, awesome-nextjs, the-delegation, SanalFuar, tweetinvi | Kod indirilmez; `notlar/kutuphaneler.md` referans notu + eşleştiği skill |
| **Zaten kurulu** | calesthio/OpenMontage (91 skill, `~/.openmontage`) | Kopyalanmaz; katalogda "yerelde kurulu" olarak listelenir, yol gösterilir |

### Mevcut kurulumla örtüşme (dokunulmayacak)
- `~/.claude/skills` → 139 skill (OpenMontage + addyosmani'nin 25'i + GSAP/threejs)
- `~/.agents/skills` (Codex kullanıcı seviyesi) → 55 skill (addyosmani + OpenMontage video)
- `~/.codex/skills` → 28 skill (OpenMontage video)
- Örtüşenler: gsap-* (7 birebir aynı, 1 farklı), threejs-* (10 aynı isim/farklı içerik), addyosmani 25 skill (zaten iki tarafta kurulu), test-driven-development (3 farklı sürüm: superpowers, addyosmani, ag-kit).

---

## 2. Mevcut durum (ilk ölçüm, sadece tasarım listesi)

| Ölçüm | Değer |
|---|---|
| Listedeki repo | 36 (9 skill reposu + 1 CLI aracı + 26 kütüphane/araç) |
| Bulunan SKILL.md | **162** |
| Benzersiz içerik (SKILL.md hash) | **89** → %45 birebir tekrar |
| Benzersiz isim | 87 |
| Aynı isim, farklı içerik | 2 → `gsap-scrolltrigger` (greensock ↔ freshtechbro), `skill-creator` (anthropics ↔ freshtechbro) |
| Tasarım dışı ama değerli | ~9: docx, xlsx, pptx, pdf, claude-api, mcp-builder, internal-comms, slack-gif-creator, academy-guide → **artık arşive alınıyor** (+~6 MB) |
| "Claude" listesindeki ek skill repoları | pbakaus/impeccable (tasarım dili: impeccable, audit), tt-a1i/archify (diyagram + kod sadeleştirme: archify, archify-review, archify-tuning, simplify-codebase, test-value), Panniantong/Agent-Reach (web/sosyal medya okuma) → +8 skill |
| Tahmini arşiv boyutu (hepsi dahil) | **≈ 30–35 MB** |

**Yer kaplar mı?** Hayır. Tüm konular dahil ~30–35 MB; bir fotoğraf albümünden küçük. Asıl risk repoları komple klonlamak: `impeccable` 77 MB, `archify` 98 MB, ama skill klasörleri sadece birkaç MB. Bu yüzden **sadece skill klasörleri** sparse olarak çekilir; git geçmişi, demo siteler ve görseller inmez. Projeye ise sadece seçilenler gider (tipik 4–10 skill, 1–5 MB).

**Bilgisayarında zaten olanlarla örtüşme** (`~/.claude/skills`, OpenMontage üzerinden):

| Skill | Durum |
|---|---|
| gsap-core, gsap-performance, gsap-plugins, gsap-react, gsap-scrolltrigger, gsap-timeline, gsap-utils | **Birebir aynı** |
| gsap-frameworks | Farklı sürüm |
| threejs-* (10 adet, CloudAI-X) | **Aynı isim, farklı içerik** (global olanlar OpenMontage sürümü) |
| test-driven-development (superpowers) | Aynı isim, farklı içerik |

→ Bu örtüşmeler aşağıdaki "isim çakışması" kuralıyla çözülecek.

---

## 3. Temel ilkeler

1. **Tek gerçek kaynak = `registry.json`.** Katalog, notlar, rol ve profil dosyaları ya bundan üretilir ya da buna referans verir. Elle iki yerde aynı bilgi tutulmaz.
2. **Kimlik = içerik.** Bir skill'in kimliği `kaynak/isim` + SKILL.md hash'idir. Dosya yolu değil.
3. **Arşiv salt-okunur.** `arsiv/` altındaki orijinal dosyalar düzenlenmez; kendi notumuz sadece `KAYNAK.md` ve `notlar/` içinde. Böylece güncellemede çakışma olmaz.
4. **Projeye kopya + kilit.** Proje kendi kopyasını taşır, hangi commit'ten geldiği `SKILLS.lock.json`'da yazar.
5. **Global'e yazılmaz.** `~/.claude/skills`, `~/.codex/skills`, `~/.agents/skills` asla değiştirilmez.

---

## 4. Mükerrerlik politikası (4 seviye)

### Seviye 1 — Birebir kopya (aynı hash)
Örn. freshtechbro'daki 4 klasördeki aynı `animejs`. **Tek kopya saklanır**, diğer yollar `registry.json` → `diger_yollar` alanına yazılır. Otomatik.

### Seviye 2 — Aynı isim, farklı içerik
Örn. `gsap-scrolltrigger` (resmî greensock ↔ freshtechbro).
- İkisi de arşivlenir: `arsiv/.../gsap-scrolltrigger/` (tercih edilen) ve `arsiv/.../gsap-scrolltrigger@freshtechbro/` (alternatif).
- Registry'de `tercih: true/false` + gerekçe.
- **Projeye her zaman sadece biri gider** (aynı isimli iki skill agent'ı karıştırır). Alternatif istenirse kurulumda klasör adı `gsap-scrolltrigger-freshtechbro` olur ve SKILL.md'deki `name` sadece **proje kopyasında** buna göre değiştirilir (arşiv bozulmaz).
- Varsayılan tercih: resmî/kaynak üretici > tek konuya odaklı repo > çok konulu toplama repo.

### Seviye 3 — Farklı isim, aynı konu (anlamsal örtüşme)
En önemli seviye; otomatik bulunamaz, kategori incelemesinde karar verilir. Bilinen adaylar:

| Örtüşme grubu | Adaylar |
|---|---|
| Genel UI estetiği / "AI görünümünden kaçış" | taste-skill, ui-ux-pro-max, design, frontend-design, modern-web-design, design-dna |
| Three.js temel | threejs-fundamentals (CloudAI-X), threejs-webgl (freshtechbro) |
| React Three Fiber | threejs-react-three-fiber (CloudAI-X), react-three-fiber (freshtechbro) |
| Scroll animasyonu | scroll-craft, gsap-scrolltrigger, locomotive-scroll, scroll-reveal-libraries |
| React animasyon | motion-framer, react-spring-physics, animated-component-libraries |
| Marka / tema | brand, brand-guidelines, theme-factory, design-system |
| Skill yazma | skill-creator ×2, writing-skills |
| Sunum | slides (ui-ux-pro-max), canvas-design |

Her grup için registry'de bir `ortusme_grubu` kaydı: `{grup, birincil, tamamlayici[], alternatif[], karar_notu}`.
- **birincil:** profillerde varsayılan gelen
- **tamamlayıcı:** birincil ile birlikte kullanılabilen, farklı şey ekleyen
- **alternatif:** aynı işi yapan, sadece özel ihtiyaçta seçilen
- Kural: Bir rol/profil aynı gruptan **en fazla 1 birincil + 1 tamamlayıcı** alabilir. `dogrula.py` bunu denetler.

### Seviye 4 — Bilgisayarda global olarak zaten var (KARAR: mevcut agent'lar bozulmaz)
`registry.json` → `globalde: {claude: "ayni"|"farkli"|null, codex: "ayni"|"farkli"|null}`.

**Değişmez kural:** `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage` **hiçbir zaman** yazılmaz, silinmez, symlink'i değiştirilmez. Bu klasördeki her şey sadece yeni projelere kopyalanır.

| Durum | Claude tarafı (proje) | Codex tarafı (proje) |
|---|---|---|
| Globalde **birebir aynı** var | Eklenmez (zaten görüyor; çift görünmez) | O tarafta da aynı varsa eklenmez, yoksa kopyalanır |
| Globalde **aynı isim, farklı içerik** var | Varsayılan: **eklenmez**, global sürüm kullanılır (mevcut davranış korunur) | Aynı kural |
| Arşivdeki sürüm özellikle istenirse | İsim çakışmasın diye ekli adla kurulur: `threejs-fundamentals-cloudai` | Aynı |
| Globalde yok | Normal kurulur | Normal kurulur |

Böylece yeni bir projede bile mevcut global skillerin adı "gölgelenmez"; çalışan agent'ların davranışı aynı kalır.

---

## 5. Klasör yapısı

**Ana klasör: `~/Documents/SkillKutuphanesi`** (eski `TasarımSkilleri` artık sadece tasarımı değil tüm skilleri kapsadığı için yeniden adlandırıldı; isimde Türkçe karakter yok, böylece betiklerde ve Codex/Claude yollarında sorun çıkmaz).

Arşiv **5 ana alan → alt kategori → skill** şeklinde 3 seviyelidir. Klasör adları küçük harf, Türkçe karaktersiz, numaralı (sıralama sabit kalsın diye).

```
SkillKutuphanesi/
├─ PLAN.md                  ← bu dosya
├─ README.md                ← kısa kullanım kılavuzu
├─ CLAUDE.md / AGENTS.md    ← "proje + agent verilince katalogdan seç" talimatı (Claude & Codex)
├─ registry.json            ← TEK GERÇEK KAYNAK
├─ KATALOG.md               ← registry'den üretilir (elle düzenlenmez)
│
├─ arsiv/
│  ├─ a-tasarim-onyuz/
│  │  ├─ 01-ui-ux-tasarim-dili/      taste-skill, ui-ux-pro-max, impeccable, design-dna, frontend-design…
│  │  │   └─ taste-skill/  (orijinal dosyalar) + KAYNAK.md
│  │  ├─ 02-tasarim-sistemi-marka/   design-system, brand, theme-factory, brand-guidelines…
│  │  ├─ 03-animasyon-motion/        gsap-*, motion-framer, animejs, lottie, rive…
│  │  ├─ 04-scroll-deneyimi/         scroll-craft, gsap-scrolltrigger, locomotive, barba…
│  │  ├─ 05-3d-webgl/                threejs-*, react-three-fiber, babylon, playcanvas, spline…
│  │  ├─ 06-oyun-2d-grafik/          pixijs-2d, ag-kit game-development/*
│  │  ├─ 07-gorsel-sanat-sunum/      canvas-design, algorithmic-art, slides, slack-gif-creator…
│  │  └─ 08-onyuz-test-kalite/       webapp-testing, playwright-cli, browser-testing, react-doctor…
│  │
│  ├─ b-yazilim-gelistirme/
│  │  ├─ 01-planlama-metodoloji/     superpowers (brainstorming, writing-plans…), spec-driven, idea-refine…
│  │  ├─ 02-kod-kalitesi-review/     code-review, simplify-codebase, test-value, clean-code…
│  │  ├─ 03-test-hata-ayiklama/      TDD (tek sürüm), systematic-debugging, verification…
│  │  ├─ 04-mimari-api-veritabani/   api-patterns, architecture, database-design…
│  │  ├─ 05-git-pr-surum/            git-worktrees, finishing-branch, pull-request, release…
│  │  ├─ 06-devops-guvenlik-performans/  ci-cd, security, observability, performance…
│  │  └─ 07-framework-ozel/          next-* (Next.js), playwright-*, plugin-dev (Claude Code)…
│  │
│  ├─ c-dokuman-icerik/
│  │  ├─ 01-ofis-dokumanlari/        docx, xlsx, pptx, pdf
│  │  ├─ 02-diyagram-dokumantasyon/  archify, doc-coauthoring, documentation-and-adrs…
│  │  ├─ 03-yazi-iletisim-icerik/    internal-comms, content-research-writer, de-ai-ify…
│  │  └─ 04-not-alma-bilgi-yonetimi/ claudesidian (obsidian-*, daily-review, weekly-synthesis…)
│  │
│  ├─ d-ai-otomasyon/
│  │  ├─ 01-claude-api-mcp/          claude-api, mcp-builder, mcp-integration…
│  │  ├─ 02-agent-orkestrasyon/      subagent-driven-development, dispatching-parallel-agents, coordinator-mode, context-engineering…
│  │  ├─ 03-web-arastirma-veri/      Agent-Reach, notebooklm, research-assistant…
│  │  └─ 04-skill-plugin-yazimi/     skill-creator (tek tercih + alternatif), writing-skills, hook/command-development…
│  │
│  └─ e-entegrasyon-katalogu/
│     └─ composio/                   832 uygulama skilli (Gmail, Slack, Notion…) — varsayılan listede gizli
│
├─ notlar/                    ← arsiv/ ile AYNI ağaç; her alt kategori için 1 inceleme raporu
│  ├─ a-tasarim-onyuz/01-ui-ux-tasarim-dili.md …
│  ├─ b-yazilim-gelistirme/…
│  ├─ c-dokuman-icerik/…
│  ├─ d-ai-otomasyon/…
│  ├─ referans/
│  │  ├─ kutuphaneler.md          ← T5: 27 kütüphane/araç (three.js, GSAP, lenis, tailwind…)
│  │  ├─ repo-ici-skiller.md      ← T3: next.js/react/lighthouse/motion iç geliştirme skilleri
│  │  └─ yerelde-kurulu.md        ← OpenMontage (91) + addyosmani (25) gibi zaten global olanlar
│  └─ teknoloji-secim-rehberi.md  ← "Next.js + GSAP → bu skiller" tabloları
│
├─ roller/      *.json   ← agent rolü → skiller
├─ profiller/   *.json   ← proje tipi → roller + ek skiller
├─ sablonlar/            ← Claude agent .md ve Codex agent .toml şablonları
└─ araclar/
   ├─ arsiv-olustur.py   ← ilk kurulum
   ├─ arsiv-guncelle.py  ← repo güncellemesi + listeye yeni eklenen repo tespiti
   ├─ katalog-uret.py    ← registry → KATALOG.md
   ├─ dogrula.py         ← tutarlılık kontrolü
   └─ skill-ekle.py      ← projeye skill/rol/profil ekleme, güncelleme, kaldırma
```

---

## 6. Kategoriler ve atanan skiller (ilk dağılım)

İki üst alan, toplam 14 kategori. Tasarım (01–08) ağırlıklı; diğer konular (09–14) aynı kurallarla yönetilir.

**A) Tasarım ve ön yüz**

| # | Kategori | Skiller | Sayı |
|---|---|---|---|
| 01 | Tasarım dili / UI-UX | taste-skill, ui-ux-pro-max, design, ui-styling, frontend-design, modern-web-design, design-dna, impeccable, audit (impeccable) | 9 |
| 02 | Tasarım sistemi / marka | design-system, brand, banner-design, brand-guidelines, theme-factory | 5 |
| 03 | Animasyon / motion | gsap-core, gsap-timeline, gsap-plugins, gsap-utils, gsap-react, gsap-frameworks, gsap-performance, motion-framer, animejs, react-spring-physics, lottie-animations, rive-interactive, animated-component-libraries | 13 |
| 04 | Scroll deneyimi | scroll-craft, gsap-scrolltrigger (+@freshtechbro), locomotive-scroll, barba-js, scroll-reveal-libraries | 6 |
| 05 | 3D / WebGL | threejs-* (13, CloudAI-X), threejs-webgl, react-three-fiber, lightweight-3d-effects, web3d-integration-patterns, babylonjs-engine, playcanvas-engine, aframe-webxr, spline-interactive, blender-web-pipeline, substance-3d-texturing | 23 |
| 06 | 2D / interaktif | pixijs-2d | 1 |
| 07 | Görsel sanat / sunum | canvas-design, algorithmic-art, slides, web-artifacts-builder, slack-gif-creator | 5 |
| 08 | Kalite / test (ön yüz) | webapp-testing (+ pixeljury, lighthouse, axe-core, playwright notları) | 1 |

**B) Diğer konular**

| # | Kategori | Skiller | Sayı |
|---|---|---|---|
| 09 | Geliştirme süreci / metodoloji | superpowers: brainstorming, writing-plans, executing-plans, subagent-driven-development, dispatching-parallel-agents, systematic-debugging, test-driven-development, verification-before-completion, requesting-code-review, receiving-code-review, using-git-worktrees, finishing-a-development-branch, using-superpowers, diagnosing-superpowers | 14 |
| 10 | Kod kalitesi / mimari | simplify-codebase, test-value, archify-review, archify-tuning | 4 |
| 11 | Diyagram / dokümantasyon | archify, doc-coauthoring | 2 |
| 12 | Ofis dokümanları | docx, xlsx, pptx, pdf | 4 |
| 13 | AI / API / entegrasyon | claude-api, mcp-builder, Agent-Reach (web & sosyal medya okuma) | 3 |
| 14 | Meta / skill yazımı / iletişim | skill-creator (+@freshtechbro), writing-skills, discernment-nudge, internal-comms, academy-guide | 5 |
| — | Atlanan | `template` (boş şablon) | 1 |

Toplam ≈ **95 benzersiz skill**. Bu dağılım inceleme sırasında değişebilir; kesin karar registry'de durur. Bir skill birden fazla alana dokunuyorsa **tek klasörde** durur, diğer alanlar etiketle bulunur (klasör kopyalanmaz).

---

## 6.1 Seçimi kolaylaştıran bilgiler (her skill için)

Her skill registry'de şu alanlarla tutulur; KATALOG.md ve `--listele` bunlara göre filtrelenir:

| Alan | Örnek | Ne işe yarar |
|---|---|---|
| `kullanim_alani` | "Scroll ile ilerleyen ürün hikâyesi, pinlenen bölümler, parallax" | Ne için seçilir |
| `kullanma` | "Basit fade-in için gereksiz; CSS yeter" | Ne zaman seçilmez |
| `teknoloji` | `gsap@3`, `three@r17x`, `react`, `next.js`, `tailwind`, `vanilla-js`, `python` | Hangi stack'te çalışır |
| `framework_bagimsiz` | true/false | React şart mı |
| `gerekli_paketler` | `gsap`, `@react-three/fiber`, `lenis` | Projeye eklenecek npm/pip paketleri |
| `proje_tipleri` | landing, kurumsal, 3d-sergi, dashboard, sunum, doküman | Hangi profillerde çıkar |
| `roller` | motion-gelistirici, qa | Hangi agent'a verilir |
| `zorluk` | başlangıç / orta / ileri | |
| `baglam_yuku` | küçük / orta / büyük (token) | Agent'ı ne kadar doldurur |
| `uyum` | claude ✓ · codex ✓ | Claude'a özel araç varsayımı var mı |
| `ortusme_grubu` + `rolu` | scroll / birincil | Benzerleriyle ilişkisi |
| `globalde` | ayni / farkli / – | Bilgisayarında zaten var mı |

**Teknolojiye göre hızlı seçim** — KATALOG.md'de ayrıca "teknoloji → skill" tablosu üretilir:

```
Next.js + Tailwind + GSAP   → taste-skill, ui-ux-pro-max, gsap-core, gsap-react, gsap-scrolltrigger, scroll-craft
React + R3F                 → threejs-react-three-fiber, threejs-fundamentals, threejs-performance, motion-framer
Vanilla JS + Three.js       → threejs-fundamentals, threejs-shaders, lightweight-3d-effects
Python / ofis çıktısı       → docx, xlsx, pptx, pdf
```

Komut örneği: `skill-ekle.py --listele --teknoloji react --proje-tipi landing`

---

## 7. Kategori inceleme süreci

Her kategori aynı şablonla, **bir oturumda bir kategori** olacak şekilde incelenir. Sonuç `notlar/<kategori>.md` dosyasına ve `registry.json`'a yazılır.

### 7.1 Her skill için doldurulan kart
```
### <skill-adı>  (kaynak: owner/repo @ commit)
- Ne yapar (2–3 cümle, Türkçe)
- Kullanım alanı / ne zaman KULLANILMAZ
- Teknoloji + sürüm: (React? Vanilla? Next.js? Tailwind? Python?) · gerekli paketler
- Uygun proje tipleri · zorluk
- Boyut / bağlam yükü: SKILL.md satır + references toplamı
- Claude uyumu / Codex uyumu: (sadece Claude'a özgü araç adı geçiyor mu?)
- Kalite puanı 1–5 · Güncellik (son commit) · Lisans
- Örtüşme grubu + rolü: birincil / tamamlayıcı / alternatif
- Hangi agent rolleri kullanır
- Karar: TUT | ALTERNATİF | SADECE ARŞİV | ÇIKAR
```

### 7.2 Değerlendirme ölçütleri
| Ölçüt | Soru |
|---|---|
| Doğruluk | API'ler güncel mi (ör. GSAP 3.13+, Three r17x, Motion v12)? |
| Odak | Tek işi iyi mi anlatıyor, yoksa dağınık mı? |
| Bağlam maliyeti | Agent'a yüklendiğinde gereksiz çok mu token harcıyor? |
| Taşınabilirlik | Codex'te de çalışır mı (Claude'a özel tool/komut varsayımı yok mu)? |
| Örtüşme | Grubundaki diğerlerine göre ne katıyor? |

### 7.3 İnceleme sırası (bağımlılığa göre)
1. **01 Tasarım dili** — en çok örtüşme burada; profillerin omurgası
2. **02 Tasarım sistemi/marka** — 01 ile sınırı belirlenir
3. **03 Animasyon** — GSAP ailesi + React animasyon grubu
4. **04 Scroll** — 03'teki GSAP kararına bağlı
5. **05 3D/WebGL** — en büyük kategori; CloudAI-X ↔ freshtechbro ↔ global OpenMontage sürümleri karşılaştırılır
6. **06–08** küçük kategoriler (tek oturumda)
7. **09 + 10 Geliştirme süreci & kod kalitesi** — `planlayici` ve `kod-inceleyici` rollerine bağlanır
8. **11–14 Diyagram, ofis, AI/API, meta** (tek oturumda) + kütüphane notları (`kutuphaneler.md`)

Tasarım (A) ve diğer konular (B) birbirinden bağımsız: 03, 05 ve 09–14 ayrı oturumlarda paralel incelenebilir; 01 → 02 sıralı olmalı.

### 7.4 Kategori bitiş kriteri
- Her skill kartı dolu, kararı registry'de
- Örtüşme grubu kararları yazılmış (birincil belli)
- `dogrula.py` hatasız
- Etkilenen roller/profiller güncel

---

## 8. Agent rolleri ve proje profilleri

### Roller (ilk taslak — kategori incelemesinden sonra kesinleşir)
| Rol | Görevi | Çekirdek skill (öneri) |
|---|---|---|
| `ui-tasarimci` | görsel dil, layout, tipografi | taste-skill, ui-ux-pro-max, design-dna |
| `tasarim-sistemi` | token, tema, marka | design-system, brand, theme-factory |
| `motion-gelistirici` | animasyon, mikro-etkileşim | gsap-core, gsap-timeline, gsap-react / motion-framer |
| `scroll-deneyim` | scroll hikâyesi, smooth scroll | scroll-craft, gsap-scrolltrigger |
| `3d-gelistirici` | Three.js / R3F sahneleri | threejs-fundamentals, threejs-react-three-fiber, threejs-performance |
| `frontend-muhendis` | uygulama kodu | frontend-design, web-artifacts-builder |
| `qa-erisilebilirlik` | görsel QA, a11y, performans | webapp-testing, gsap-performance (+ lighthouse/axe notu) |
| `planlayici` | plan, alt-agent orkestrasyonu | brainstorming, writing-plans, subagent-driven-development, verification-before-completion |
| `kod-inceleyici` | review, sadeleştirme, test değeri | requesting-code-review, simplify-codebase, test-value, systematic-debugging |
| `dokuman-yazari` | rapor, sunum, diyagram | docx, pptx, pdf, archify, doc-coauthoring |
| `ai-entegrasyon` | Claude API, MCP, web veri | claude-api, mcp-builder, Agent-Reach |
| `agent-orkestra` | planı alt-agent'larla yürütme, bağlam yönetimi | subagent-driven-development, dispatching-parallel-agents, context-engineering |
| `skill-gelistirici` | skill, Claude Code eklentisi, hook, komut | skill-creator, writing-skills, plugin-structure |
| `icerik-pazarlama` | blog/makale, sosyal metin, SEO/GEO | content-research-writer, de-ai-ify, seo-fundamentals |

### Profiller (proje tipi → roller)
| Profil | Roller |
|---|---|
| `landing-page` | ui-tasarimci, motion-gelistirici, frontend-muhendis, qa-erisilebilirlik, icerik-pazarlama |
| `kurumsal-site` | ui-tasarimci, tasarim-sistemi, frontend-muhendis, qa-erisilebilirlik, icerik-pazarlama |
| `scroll-hikaye-sitesi` | ui-tasarimci, scroll-deneyim, motion-gelistirici, qa-erisilebilirlik |
| `3d-urun-sergisi` | ui-tasarimci, 3d-gelistirici, scroll-deneyim, qa-erisilebilirlik |
| `dashboard-saas` | ui-tasarimci, tasarim-sistemi, frontend-muhendis, qa-erisilebilirlik |
| `tasarim-sistemi` | tasarim-sistemi, ui-tasarimci |
| `marka-sunum` | tasarim-sistemi, dokuman-yazari |
| `rapor-dokuman` | dokuman-yazari |
| `ai-uygulama` | ai-entegrasyon, frontend-muhendis, kod-inceleyici |
| `mevcut-kod-iyilestirme` | kod-inceleyici, planlayici, agent-orkestra |
| `sosyal-medya-icerik` | ai-medya-uretici, video-kompozisyon, video-kurgu-render, icerik-pazarlama |
| `skill-plugin-gelistirme` | skill-gelistirici, kod-inceleyici (+ mcp-builder) |

Her profile `planlayici` isteğe bağlı eklenir (`--planlayici`).

---

## 9. Projeye kurulum (Claude + Codex) — doğrulanmış davranış

| | Claude Code | Codex |
|---|---|---|
| Proje skill klasörü | `.claude/skills/<ad>/` | `.agents/skills/<ad>/` (cwd → repo köküne kadar taranır) |
| Symlink | destekler (testte teyit edilecek) | **destekler** (resmî doküman) |
| Proje agent tanımı | `.claude/agents/<rol>.md` | `.codex/agents/<rol>.toml` (`name`, `description`, `developer_instructions`) |
| Role özel skill | frontmatter `skills: [a, b]` → sadece bunlar önyüklenir | Allowlist yok; rol dışı skiller `[[skills.config]] path=… enabled=false` ile **kapatılır** |

**Kurulum mantığı (`skill-ekle.py`):**
1. Fiziksel kopya sadece `<proje>/.agents/skills/<ad>/`.
2. `<proje>/.claude/skills/<ad>` → `../../.agents/skills/<ad>` göreli symlink (globalde birebir aynısı varsa konmaz).
3. Her rol için Claude `.md` ve Codex `.toml` üretilir; Codex dosyasına o rolün kullanmadığı proje skilleri `enabled=false` olarak yazılır → her agent sadece kendi skillerini görür.
4. `AGENTS.md` / `CLAUDE.md` içine işaretli bir blok (`<!-- tasarim-skilleri:basla -->…<!-- bitir -->`) eklenir; sadece bu blok yeniden yazılır, kullanıcının diğer içeriğine dokunulmaz.
5. `<proje>/.agents/skills/SKILLS.lock.json`: skill → kaynak, commit, hash, hangi roller.

**Komutlar:**
```bash
python3 araclar/skill-ekle.py <proje> --profil 3d-urun-sergisi [--planlayici]
python3 araclar/skill-ekle.py <proje> --rol motion-gelistirici
python3 araclar/skill-ekle.py <proje> --skill taste-skill gsap-core
python3 araclar/skill-ekle.py <proje> --guncelle      # lock'a göre arşivdeki yeni sürümü uygular
python3 araclar/skill-ekle.py <proje> --kaldir [ad]   # sadece kendi eklediklerini siler
python3 araclar/skill-ekle.py --listele [--kategori 05] [--rol 3d-gelistirici]
python3 araclar/skill-ekle.py <proje> --kuru-calistir # ne yapacağını gösterir, dokunmaz
```

**Sohbetten kullanım:** "Şu proje, şu agent'lar" dediğinde `registry.json` + roller + profillerden öneri tablosu çıkarırım → onaylarsın → `skill-ekle.py` çalışır.

---

## 10. Sürdürülebilirlik (bakım döngüsü)

| Ne zaman | Ne | Araç |
|---|---|---|
| Listeye yeni repo ekleyince | `gh` ile listeyi okur, registry'de olmayan repoları raporlar; skill reposuysa arşive aday, kütüphaneyse `kutuphaneler.md`'ye aday | `arsiv-guncelle.py --yeni` |
| Ayda bir | Her repo HEAD commit'i kontrol; değişen SKILL.md'ler için fark özeti; onayla arşiv güncellenir, eski sürüm `arsiv/.eski/<ad>@<commit>/` altında 1 sürüm tutulur | `arsiv-guncelle.py` |
| Her değişiklikte | Tekrar isim yok, her kayıtta KAYNAK.md var, roller var olan skillere bakıyor, örtüşme grubu kuralı | `dogrula.py` |
| Her değişiklikte | KATALOG.md yeniden üretilir | `katalog-uret.py` |
| Proje güncellemesi | Lock dosyasındaki commit ≠ arşiv → uyarı + `--guncelle` | `skill-ekle.py` |
| Repo silinirse | Arşiv yerinde kalır; registry'de `kaynak_durumu: silindi` | `arsiv-guncelle.py` |

**Karar: yerel git kullanılacak.** Bu klasör bir "kayıt defteri" gibi her değişikliği hatırlar: bir repo güncellemesi bir skill'i bozarsa tek komutla önceki hâline dönülür. Sadece bilgisayarında durur, internete gönderilmez. Bu sayede `arsiv/.eski/` yedek klasörüne de gerek kalmaz (yer tasarrufu). Her arşiv güncellemesi ve kategori incelemesi ayrı bir kayıt noktası olur.

İsteğe bağlı: aylık kontrol için zamanlanmış görev (sadece rapor üretir, değişiklik yapmaz).

---

## 11. Uygulama aşamaları

| Aşama | Çıktı | Bitti sayılır |
|---|---|---|
| **A. İskelet** | klasör yapısı, `registry.json` şeması, `dogrula.py`, `git init` | dogrula boş registry'de geçer |
| **B. Arşiv** | `arsiv-olustur.py` → 9 repo sparse çekilir, Seviye 1 tekilleştirme, Seviye 2 ayrıştırma, KAYNAK.md, ilk kategori ataması | ~78 skill arşivde, tekrar hash yok, ~20–25 MB |
| **C. Kurulum aracı** | `skill-ekle.py` + şablonlar; deneme projesinde Claude & Codex testi | iki araç da deneme projesinde skilleri listeliyor; `--kaldir` temiz |
| **D. Kategori incelemeleri** | 10 kategori raporu (bölüm 7), örtüşme kararları | her kategori bitiş kriterini karşılıyor |
| **E. Roller/profiller** | inceleme kararlarına göre kesinleşmiş `roller/`, `profiller/` | dogrula geçer, her profil kurulum testinden geçer |
| **F. Kütüphane notları** | `kutuphaneler.md` (26 araç) | her araç bir profile/skille bağlı |
| **G. Bakım** | `arsiv-guncelle.py`, `katalog-uret.py`, README/CLAUDE.md/AGENTS.md | `--yeni` ve güncelleme raporu çalışıyor |

A–C yapıyı kurar (tek oturum). D en uzun aşamadır; kategori başına bir oturum, 03/05/09 paralel yapılabilir.

---

## 12. Açık kararlar (onayın gerekli)

Kesinleşenler:
1. ✅ Tüm konular ve **49 star reponun tamamı** dahil (bölüm 2.0'daki T1–T5 ayrımıyla).
2. ✅ Yerel git kullanılacak (bölüm 10).
3. ✅ Global skiller ve OpenMontage'a dokunulmayacak; çakışan isimler projeye eklenmeyecek (bölüm 4, Seviye 4).

Açık kalan:
4. Composio'nun 832 uygulama-entegrasyon skilli: arşive alınsın ama varsayılan listede gizli dursun (öneri) — yoksa sadece link olarak mı kalsın?
5. Kategori sayısı ~310 skill ile 14'ten ~20'ye çıkacak (oyun geliştirme, Obsidian/not alma, git/PR, güvenlik, DevOps, kariyer/içerik eklenecek); kesin liste arşiv kurulduktan sonra SKILL.md açıklamalarından çıkarılıp sana sunulacak.
