# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **30/97**

### 8-bit-orbit-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Hyperframes-based video template for retro pixel deck motion design. Use when users want a high-fidelity, multi-scene HTML-to-video composition with advanced transitions, interactive preview controls, and ready-to-render default style.
- **Teknoloji:** css, gsap, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 20 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### after-hours-editorial-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Luxury dark-editorial HyperFrames template for three-page cinematic storyboards, inspired by haute couture title cards and magazine chapter spreads. Use when the user asks for premium fashion-style motion pages, moody serif-led storytelling, or a high-end dark presentation aesthetic with rich transitions.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 2.4 KB, yük kucuk)
- **İnceleme:** otomatik

### alipay-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau alipay` 登录支付宝生活号并发布视频。Use when 用户要向支付宝生活号发布视频或检查创作账号状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### baijiahao-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau baijiahao` 登录百家号、检查账号并发布视频。Use when 用户要向百家号发布视频或核验百家号登录状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### bilibili-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 当 agent 需要通过已安装的 `sau` CLI 完成 Bilibili 登录、账号校验或视频上传时使用这个 skill。优先使用 `sau bilibili ...`，程序会自动准备 `biliup`，不要求用户手动安装。
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 2.1 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### captions-overlay  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videolarında altyazı doktrini: her cümle drop / rail / embed olarak sınıflanır (embed nadir zirve), altyazı alttan rezerve bir şerit değil filmin üstüne bindirilen overlay'dir; kompozisyon gerçek dikey merkeze göre yerleşir.
- **Ne zaman:** Konuşan kafa, tanıtım ya da explainer videolarına altyazı eklerken yerleşim ve vurgu kararları. · **Ne zaman değil:** Altyazısız videolar; altyazının teknik kurulumu için hyperframes references/captions.md yeterli.
- **Teknoloji:** hyperframes · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** altyazi → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede hyperframes'in references/captions.md dosyasının üstüne uygulanan doktrin olarak konumlandı (metadata internal: true). Emekli embedded-captions iş akışına atıf içeriyor; artık hyperframes skiliyle birlikte kullanılır.

### changelog-video  ·  heygen-com/hyperframes @ f8309b3  ·  puan 83 (A)

- **Ne yapar:** Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka planı, sahte UI görselleştirmeleri ve sakin altyazılar; fontlar, arka plan müziği ve betikler skill içinde paketli.
- **Ne zaman:** Yalnız HeyGen'in kendi haftalık changelog videosu için; kendi markan için örnek/şablon olarak incelenebilir. · **Ne zaman değil:** Kendi ürününün changelog videosunda doğrudan (pr-to-video veya product-launch-video kullan); marka varlıkları HeyGen'e ait.
- **Teknoloji:** hyperframes, html, gsap, node, heygen · **Paketler:** hyperframes (npx), node>=22, ffmpeg, HeyGen hesabı (TTS)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → alternatif · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 521 KB (SKILL.md 13.1 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. HeyGen iç skilli (internal:true): HeyGen marka kimliğine, sabit seslendirmene ve repo köküne bağlı; paketlenen TT Norms Pro / ABC Solar ticari fontlarının yeniden kullanım lisansı belirsiz. Rollere eklenmedi.

### chat-motion-overlay  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat containers, optional device frames, preset or uploaded avatars, nickname display rules, and transparent-video-ready Remotion bundles. Use when Codex needs to create reusable short-form chat clips for Douyin, demo videos, story reenactments, social-message proof scenes, or embed
- **Teknoloji:** python, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1308 KB (SKILL.md 4.7 KB, yük kucuk)
- **İnceleme:** otomatik

### cinecode  ·  sarpstar/cinecode @ 67f9807  ·  puan 67 (B)

- **Ne yapar:** Kullanıcıyla birlikte tamamen kodla kısa film, reklam ya da müzik videosu yapar. İki kip: Hızlı (tek HTML dosyası + Web Audio, düşük çözünürlüklü taslak, iki revizyon, yaklaşık 3 dakikaya kadar) ve Film (stil karesi, animatik, three.js render, katmanlı ses; altı kapılı adım). Kullanıcının şarkısına film, referans videoya benzer film ve kullanıcının çekimlerinden kurgu da yapar; -14 LUFS master'lı MP4 verir. Türkçe tetikleyicileri vardır.
- **Ne zaman:** Koddan üretilen sinematik kısa film, reklam/ürün filmi, müzik videosu; senaryodan sese uçtan uca tek skill isteniyorsa. · **Ne zaman değil:** DİKKAT: SKILL.md hook tanımlar (her istemde ve her araç çağrısında scripts/guard.py yerel denetimi çalışır) ve ev dizinine yazar (~/.cinecode/: anahtar deposu, önbellek). Seslendirme için Gemini TTS anahtarı (ya da ElevenLabs) gerekir; anahtarsız yalnızca Web Audio'lu film. Mevcut görüntüyü kurgulamak için video-edit/ffmpeg; kare-hassas HTML kompozisyon için hyperframes. Repo çok yeni (2026-11-03).
- **Teknoloji:** three.js, html, javascript, python, node, ffmpeg · **Paketler:** ffmpeg, node, python3
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: hooks (Codex bunları yok sayar)
- **Geliştirici:** sarpstar (kisi, ★1614, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kodla-film-stilleri → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 2409 KB (SKILL.md 32.0 KB, yük buyuk) · **Bağımlılık:** SKILL.md frontmatter'ında hook tanımlar (UserPromptSubmit, Stop, PreToolUse: her istemde ve her araç çağrısında scripts/guard.py yerel denetimi çalışır). Ev dizinine yazar: ~/.cinecode/ (python yolu önbelleği, anahtar deposu keys.env, yazı tipi önbelleği). Node, Python 3 ve ffmpeg ister. Varsayılan seslendirme Gemini TTS (GEMINI_API_KEY), ElevenLabs isteğe bağlı; stok arama için ücretsiz Pixabay anahtarı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (kodla-film-stilleri grubunda; birincil lemo-opuscar). MIT, tek konulu uzman repo; 39 betik, 61 stil dosyası, kendi testleri var. Çalıştırma testi yapılmadı; repo 2026-11-03'te oluşturuldu, sürüm kararlılığı izlenmeli. DİKKAT: skill frontmatter'ında hook var (UserPromptSubmit, Stop, PreToolUse) ve ~/.cinecode/ altına yazar; hook ve denetim betiğinde ağ çağrısı görülmedi.

### create-video  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 94 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-kompozisyon, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### dayu-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 通过 social-auto-upload 的 sau CLI 完成大鱼号登录、账号核验、视频和文章的立即或定时发布，以及原作品结果查询。文章接收 HTML、Markdown 或 TXT 文件，Markdown 可选择主题。适用于已安装 sau 的环境，无需先阅读上传器源码。
- **Teknoloji:** html, node, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 5.3 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### douyin-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 当 agent 需要通过已安装的 `sau` CLI 完成抖音登录、cookie 校验、视频上传或图文发布时使用这个 skill。该 skill 适用于已经安装 `social-auto-upload` 且可调用 `sau` 命令的环境。优先使用这个 skill 进行稳定的命令式抖音工作流，而不是一开始就阅读 uploader 源码。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### facebook-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 sau CLI 登录 Facebook 个人主页，立即发布视频或图文，查询原作品、移至垃圾箱或永久删除。
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### ffmpeg  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 93 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### figma  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** Figma içeriğini HyperFrames videosuna getirir: asset (SVG/PNG), marka token'ları, frame'leri düzenlenebilir HTML bileşen olarak, connector ile motion (GSAP'e çevirip doğrulama), shader ve storyboard (frame'ler slayt değil, aynı öğenin durumları).
- **Ne zaman:** Figma linki verildiğinde; marka renkleri/tipografisi, logo, bileşen ya da storyboard'u videoya taşımak. · **Ne zaman değil:** FIGMA_TOKEN yoksa ve kullanıcı oluşturmak istemiyorsa; Figma dışı tasarım kaynakları.
- **Teknoloji:** hyperframes, figma api, gsap · **Paketler:** hyperframes (npx), FIGMA_TOKEN
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 11 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede komutlar sadeleşti, storyboard kuralları (frame = keyframe) ve motion doğrulama betiği netleşti. Token sohbete yapıştırılmaz; kullanıcı kendisi ayarlar.

### frame-data-chart-nyt  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band).
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-flowchart-sticky  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-glitch-title  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 9 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-light-leak-cinema  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.9 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-liquid-bg-hero  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters.
- **Teknoloji:** canvas, css, html, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 4.0 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-logo-outro  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### frame-macos-notification  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### hupu-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau hupu` 登录虎扑并发布视频，可指定封面。Use when 用户要向虎扑发布视频或检查虎扑账号状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### hyperframes  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames'in yeni tek giriş skili: HTML'i kare kare render ederek videoya çeviren sistemin render sözleşmesini (12 kural), düzenlenebilirlik kurallarını, iş döngüsünü (story → SPEC → check → snapshot → review → render) ve video türlerine göre okunacak referansları (launch, explainer, müzik, data, dikey, 3D, karakter, altyazı, overlay, motion) tek yerde toplar.
- **Ne zaman:** HyperFrames ile her türlü video: tanıtım filmi, explainer, müzik videosu, grafik/harita, dikey sosyal klip, altyazı ve overlay; eskiden ayrı iş akışı skilleri olan türlerin hepsi artık buradaki references/types dosyalarıyla yürür. · **Ne zaman değil:** Remotion ya da başka bir çerçeve açıkça istenirse; sadece tarayıcı ekran kaydı gerekiyorsa (playwright-recording).
- **Teknoloji:** hyperframes, html, gsap, node 22+, ffmpeg · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → birincil · **Roller:** video-kompozisyon, video-kurgu-render, motion-graphics-sanatcisi · **Globalde:** claude:farkli, agents:ayni
- **Boyut:** 1117 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi (heygen-com/hyperframes 6882293): iş akışı skilleri emekliye ayrıldı, içerikleri bu skilin references/types ve references/*.md dosyalarına taşındı; SKILL.md 7 KB'a indi, sözleşme daha net. Önceki iş akışı skillerinin (general-video, faceless-explainer, product-launch-video…) yerine birincil seçim budur. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### hyperframes-cli  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames CLI'yi işe göre anlatır: init/capture, check (lint/validate/inspect, ses denetimleri dahil), snapshot, timeline düzenleme, preview, yerel render (fps 1-240, bitrate/keyframe ayarı) ve isteğe bağlı bulut/Lambda/Cloud Run render, proje geçmişi ve hata tablosu. Render öncesi doğrulama döngüsünü tanımlar.
- **Ne zaman:** HyperFrames projesini kontrol etme, görsel olarak inceleme, zaman çizelgesi düzenleme ve render alma. · **Ne zaman değil:** Kompozisyonun içeriğine karar verirken tek başına yetmez; hyperframes skiliyle birlikte kullanılır.
- **Teknoloji:** hyperframes, node 22+, ffmpeg, chrome · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kurgu-render · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 124 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-11: ses (audio_*) lint denetimleri ve yeni render bayrakları eklendi; bulut render ayrı HyperFrames OAuth'una (~/.hyperframes) taşındı, ücretli planda son render için cloud render öneriliyor (yerel render ücretsiz). Telemetri girişten sonra hesaba bağlanır; HYPERFRAMES_NO_TELEMETRY=1 ile kapatılır. Node 22+ ve FFmpeg gerekir.

### hyperframes-cli@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** HyperFrames CLI tool — hyperframes init, lint, inspect, preview, render, transcribe, tts, doctor, browser, info, upgrade, compositions, docs, benchmark. Use when scaffolding a project, linting, validating, inspecting visual layout in compositions, previewing in the studio, rendering to video, transcribing audio, generating TTS, or troubleshooting the HyperFrames environment.
- **Teknoloji:** canvas, docker, ffmpeg, html, node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk)
- **İnceleme:** otomatik

### hyperframes-registry  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** ~450 hazır HyperFrames bloğu ve bileşenini (geçişler, overlay, başlık, kinetik tipografi, altyazı stilleri, grafik, harita, 3D, kamera hareketi) arama (`catalog --query`) ve projeye düzenlenebilir kaynak olarak kurma (`add`) rehberi.
- **Ne zaman:** Adı olan bir görsel efekti (glitch, film grain, bar chart race, lower third…) elle yazmadan önce; blok/bileşen bağlama. · **Ne zaman değil:** Kayıt defterinde karşılığı olmayan, tamamen özgün sahneler.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 83 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede ~400 → ~450 öğe; yerel arama katmanları (words / on-device) ve 'gap' raporlama eklendi. Arama İngilizce yapılmalı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### hyperframes-registry@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, and registry discovery.
- **Teknoloji:** canvas, css, gsap, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 18 KB (SKILL.md 4.2 KB, yük kucuk)
- **İnceleme:** otomatik

### hyperframes@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML. Use when asked to build any HTML-based video content, add captions or subtitles synced to audio, generate text-to-speech narration, create audio-reactive animation (beat sync, glow, pulse driven by music), add animated text highlighting (marker swee
- **Teknoloji:** canvas, css, gsap, html, node, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 157 KB (SKILL.md 21.0 KB, yük orta)
- **İnceleme:** otomatik

### instagram-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 sau CLI 在 Instagram 独立网页登录、立即发布 Reels/单图/轮播、核验原作品并移至最近删除。
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### kalem  ·  leodavincs/kalem @ ba19c9f  ·  puan 63 (C)

- **Ne yapar:** Kodla video üretirken videoyu sahnelere böler ve her sahnenin içeriğine göre çizim motorunu seçer: elle çizim için Paper.js, parçacık için PixiJS, yazı/bilgi kartı için HyperFrames (HTML+GSAP), 3D için Three.js, formül için Manim, defter levhası tarzı makine dersi için kendi Levha motoru. Sahneleri sayfa çevirme gibi geçişlerle birleştirir ve kareye kilitli efekt sesi ekler. Türkçe.
- **Ne zaman:** Tek motorla yapılan videoların birbirine benzemesini istemediğin, sahne sahne farklı görsel dil gereken eğitim/anlatım videoları (özellikle OpenMontage/HyperFrames'in üstünde yönlendirici olarak). · **Ne zaman değil:** DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür. Tek motor yeterse doğrudan hyperframes / manim-composer / threejs-* skilleri. Node 20+, Python 3, ffmpeg ve Chrome ister; Manim isteğe bağlı.
- **Teknoloji:** javascript, python, ffmpeg, gsap, three.js, manim, pixijs · **Paketler:** Node 20+, Python 3, ffmpeg, Google Chrome, manim (isteğe bağlı)
- **Claude / Codex:** tam / tam
- **Geliştirici:** leodavincs (kisi, ★106, son güncelleme 2026-11-06, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** kodla-video-motor-secimi → birincil
- **Boyut:** 6 KB (SKILL.md 6.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (kullanıcı isteği; kodla-video-motor-secimi grubunda birincil, tek üye). MIT, 106★, çok yeni (2026-11). Ücretsiz, yerel; dış servis yok. DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür.

### kuaishou-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 当 agent 需要通过已安装的 `sau` CLI 完成快手登录、cookie 校验、视频上传或图文发布时使用这个 skill。该 skill 适用于已经安装 `social-auto-upload` 且可调用 `sau` 命令的环境。优先使用这个 skill 进行稳定的命令式快手工作流，而不是一开始就阅读 uploader 源码。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.7 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### lemo-opuscar  ·  lemomo-ai/lemo-opuscar @ bebbbe1  ·  puan 85 (A)

- **Ne yapar:** Lemo-Opuscar film stili kütüphanesine giriş skili: 59 hazır stilden birini seçip (ya da kendi stilini oluşturup) video modeli kullanmadan, tamamen kodla kısa film yönetir ve üretir. Kütüphaneyi ilk çalıştırmada GitHub'dan ev dizinine (~/lemo-opuscar) seyrek klonlar, gerekli Node/Python paketlerini kurar ve kütüphanenin AGENTS.md akışını izler.
- **Ne zaman:** Belirli bir görsel stilde (yağlı boya, suluboya, ukiyo-e, uydu brifingi, ürün parçalama vb.) kodla üretilmiş kısa film, tanıtım, açıklayıcı video; uydu görüntüsü/lazer tarama/CAD/arşiv gibi gerçek malzemeden veri anlatımı; kendi film stilini oluşturma. · **Ne zaman değil:** Mevcut bir videoyu sadece kesip birleştirmek/dönüştürmek (video-edit, ffmpeg); HyperFrames projesi içinde sahne kurmak (hyperframes).
- **Teknoloji:** node, three.js, ffmpeg, python, kokoro tts · **Paketler:** node, ffmpeg, python3 (seslendirme için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★12273, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** tercih · **Örtüşme:** kodla-film-stilleri → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 10 KB (SKILL.md 3.4 KB, yük kucuk) · **Bağımlılık:** Çalışınca kendi kütüphanesini ev dizinine indirir/kopyalar (~/lemo-opuscar veya ~/.lemo-opuscar), Node + ffmpeg (+ seslendirme için Python/Kokoro) ister. Ücretsiz: varsayılan TTS çevrimdışı Kokoro; edge-tts metni Microsoft'a gönderir (sadece kullanıcı onaylarsa).
- **İnceleme:** incelendi · kalite 4/5 — MIT, ücretsiz; varsayılan seslendirme çevrimdışı Kokoro, edge-tts sadece onayla. DİKKAT: kodun asıl kısmı çalışma anında GitHub'ın main dalından (sabit commit değil) ~/lemo-opuscar'a indirilir; yani arşivlenen skill küçük bir başlatıcıdır, davranış upstream değiştikçe değişir. Proje klasörü dışına (ev dizinine) yazar. HyperFrames'e alternatif değil, farklı bir motor (kendi render araçları). · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi.

### lemo-opuscar@lemomo-ai  ·  lemomo-ai/lemo-opuscar @ bebbbe1  ·  puan 69 (B)

- **Ne yapar:** Aynı Lemo-Opuscar skilinin 'dizin/eklenti paketi' sürümü: kütüphanenin yanında paketlenmiş (library/) gelmesini bekler, ~/.lemo-opuscar'a kopyalar.
- **Ne zaman:** Belirli bir görsel stilde (yağlı boya, suluboya, ukiyo-e, uydu brifingi, ürün parçalama vb.) kodla üretilmiş kısa film, tanıtım, açıklayıcı video; uydu görüntüsü/lazer tarama/CAD/arşiv gibi gerçek malzemeden veri anlatımı; kendi film stilini oluşturma. · **Ne zaman değil:** Doğrudan kurulum: library/ klasörü olmadan çalışmaz; birincil lemo-opuscar'ı kullan.
- **Teknoloji:** node, three.js, ffmpeg, python, kokoro tts · **Paketler:** node, ffmpeg, python3 (seslendirme için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** lemomo-ai (kisi, ★12273, son güncelleme 2026-10-31, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** kodla-film-stilleri → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 123 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** Çalışınca kendi kütüphanesini ev dizinine indirir/kopyalar (~/lemo-opuscar veya ~/.lemo-opuscar), Node + ffmpeg (+ seslendirme için Python/Kokoro) ister. Ücretsiz: varsayılan TTS çevrimdışı Kokoro; edge-tts metni Microsoft'a gönderir (sadece kullanıcı onaylarsa).
- **İnceleme:** incelendi · kalite 2/5 — Tek başına ÇALIŞMAZ: beklediği library/ klasörü bu repo yolunda yok (yalnızca paketlenmiş eklenti dağıtımında bulunur). Kurulum için birincil sürüm (lemo-opuscar) kullanılmalı.

### media-use  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videosu için medyayı tek komutla (`media-use resolve` / `media-use generate`) bulur ya da üretir: müzik, ses efekti, görsel/ikon/logo, seslendirme, avatar/üretilmiş video, transkript, arka plan silme, renk düzeltme; yerleştirilen sesleri miksler. Kaynaklar: ücretsiz (HyperFrames girişi: Voice Turbo, müzik kataloğu, asset arama; Openverse, Whisper), HyperFrames kredisi (üretilmiş görsel/video/avatar, ses klonlama) ve yerel modeller (Kokoro, MusicGen, FLUX, LTX).
- **Ne zaman:** Videoya müzik, SFX, seslendirme (Kokoro TTS dahil), avatar, transkript, renk/LUT, yüz gizleme gibi medya eklemek; eski hyperframes-audio işlerinin yerine. · **Ne zaman değil:** HyperFrames dışı projeler; özel bir sağlayıcı açıkça istenirse o sağlayıcının skili. DİKKAT (2026-11): skill 'ucuz/ücretsiz seçeneğe kendiliğinden geçme, fiyat söyleme' diyor ve ücretli çağrıdan önce onay kuralı kaldırıldı; ücretsiz yol tercih ediliyorsa agent'a yerel/ücretsiz sağlayıcıyı (--local-only) açıkça söyle.
- **Teknoloji:** hyperframes, heygen, ffmpeg, python 3.10+ (kokoro tts) · **Paketler:** node, hyperframes auth login (HyperFrames OAuth), heygen CLI (yardımcı tarifler için), ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-medya → birincil · **Roller:** video-kompozisyon, ses-tasarimci, video-kurgu-render · **Globalde:** claude:farkli, codex:farkli, agents:farkli
- **Boyut:** 1860 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-11: giriş 'npx hyperframes auth login' (HyperFrames OAuth); 'media-use generate' ile heygen CLI olmadan üretim eklendi. Kredi harcamada ücretsiz yola geçmeme ve fiyat söylememe yönergesi kullanıcının ücretsiz-önce tercihiyle çelişir. Telemetri girişten sonra HeyGen hesabına bağlanır; HYPERFRAMES_NO_TELEMETRY=1 ile kapatılır.

### meta-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 sau CLI 登录 Facebook Page，发布视频或图文、设置北京时间排期、查询原作品并删除。
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### moneyprinterturbo-video  ·  harry0703/MoneyPrinterTurbo @ c235354  ·  puan 98 (A)

- **Ne yapar:** MoneyPrinterTurbo uygulamasını kurup çalıştırarak bir konu ya da metinden bitmiş kısa video üretir: LLM ile metin, Pexels stok görüntüsü, Edge TTS seslendirme, altyazı ve fon müziği. Kurulumu, yapılandırmayı, üretimi ve MP4 teslimini yardımcı betikle (mpt_agent.py) kendisi yürütür; eksik API anahtarlarını tek seferde ister.
- **Ne zaman:** Konu ya da başlıktan stok görüntülü, seslendirmeli dikey/yatay kısa video; MoneyPrinterTurbo'nun kurulumu ve başarısız üretimin onarımı. · **Ne zaman değil:** DİKKAT: skill onay sormadan kurar ve çalıştırır (uygulamayı ev dizinine indirir, uv yoksa ağdan kurar). LLM API anahtarı zorunlu. Varsayılan çıktı Çince 9:16; dil ve biçim açıkça belirtilmeli. Üretilmiş (AI) video sağlayıcıları ücretli görev açar. Kare-hassas kompozisyon ya da özgün görsel için hyperframes/remotion.
- **Teknoloji:** python, ffmpeg, api-anahtari · **Paketler:** uv, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** harry0703 (kisi, ★141094, son güncelleme 2026-11-07, lisans MIT)
- **Durum:** tercih · **Örtüşme:** konudan-stok-video → birincil · **Roller:** ai-medya-uretici, video-kurgu-render
- **Boyut:** 47 KB (SKILL.md 8.8 KB, yük orta) · **Bağımlılık:** Skill MoneyPrinterTurbo'yu kullanıcının ev dizinine kurar ve kurulum/üretim için onay sormaz; uv gerekir (yoksa ağdan kurar). LLM API anahtarı zorunlu, stok görüntü için Pexels anahtarı (ücretsiz) gerekir. Bazı video sağlayıcıları (Seedance/Ark, OFox, MiniMax, MuAPI, Infistar, Jalapeno) ücretli görev açar; her biri ayrıca onay ister. Varsayılan çıktı Çince 9:16.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (konudan-stok-video grubunda birincil). Resmî ürün reposu (MIT), skill sürümü 1.3.2; yardımcı betik kurulum, anahtar doğrulama ve hata onarımını yürütür. Çalıştırma testi yapılmadı. DİKKAT: skill kurulum ve üretim için onay istemez, ev dizinine kurar; LLM anahtarı zorunlu; ücretli video sağlayıcıları ayrı onay ister.

### motion-design  ·  lottiefiles/motion-design-skill @ f9a8a04  ·  puan 72 (B)

- **Ne yapar:** Applies motion design principles to create emotionally-driven, technically sound animations and transitions. Provides timing, easing, choreography, and Disney animation principles adapted for UI. Use when creating animations, transitions, micro-interactions, loading states, page transitions, scroll-triggered effects, or any motion work. Works with CSS, Framer Motion, GSAP, Lottie, Spring, or any a
- **Teknoloji:** css, gsap, lottie _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** LottieFiles (kurum, ★2853, son güncelleme 2026-05-18, lisans MIT)
- **Durum:** tercih
- **Boyut:** 55 KB (SKILL.md 12.3 KB, yük orta)
- **İnceleme:** otomatik

### motion-design@nexu-io  ·  nexu-io/open-design @ 987b247  ·  puan 92 (A)

- **Ne yapar:** Apply motion craft to an active task: refine a brief, beat map, visual continuity, typography, pacing, and timeline implementation. Use when planning or improving motion graphics; the host task owns artifact creation, output format, and export.
- **Teknoloji:** api-anahtari, canvas, css, gsap, html, node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** alternatif
- **Boyut:** 35 KB (SKILL.md 26.7 KB, yük buyuk)
- **İnceleme:** otomatik

### onetake  ·  feitangyuan/onetake @ abb6d17  ·  puan 73 (B)

- **Ne yapar:** Ürün, sayfa, skill ya da özellik için 10–30 saniyelik (anlatımlı demolarda yaklaşık 60 saniye) kesintisiz tanıtım filmi yapar: tek HTML kompozisyon (her değer zamanın saf fonksiyonu), ölçülmüş hareket kütüphanesi (yay, giriş, taşıma, temas, kamera), gerçek arayüzden malzeme, ortak ses paleti ve ritim ile sürekliliği ölçen denetçi. Referans videoyu çözümleyip hissini yakalar; kare kare, hareket bulanıklığıyla render eder.
- **Ne zaman:** Lansman/teaser klibi, anlatımlı özellik demosu; sahnelerin birbirinden doğduğu tek çekim hissi isteniyorsa. · **Ne zaman değil:** DİKKAT: lisans PolyForm Noncommercial 1.0.0, yalnızca ticari olmayan kullanım. Uzun video, konuşan kafa ve mevcut görüntü kurgusu için değil. HyperFrames ya da Remotion açıkça isteniyorsa onlar.
- **Teknoloji:** html, javascript, python, ffmpeg, node · **Paketler:** ffmpeg, node, python3, kokoro-onnx, faster-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** feitangyuan (kisi, ★3959, son güncelleme 2026-11-05, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 2715 KB (SKILL.md 23.7 KB, yük orta) · **Bağımlılık:** Lisans PolyForm Noncommercial 1.0.0: yalnızca ticari olmayan kullanım serbest. ffmpeg, node ve Python 3 ister; seslendirme için Kokoro (~/.cache/kokoro/venv altına kurulur) ve faster-whisper.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (urun-tanitim-filmi grubunda birincil). Tek konulu uzman repo; hareket kütüphanesi (lib/motion.js), 12 betik, ritim ve süreklilik ölçümü, 7 referans belgesi. Yerel ve ücretsiz çalışır. Çalıştırma testi yapılmadı. DİKKAT: lisans PolyForm Noncommercial 1.0.0 (yalnızca ticari olmayan kullanım); GitHub lisansı tanımadığı için kayıtta NOASSERTION görünür. Örnek filmler ve GIF'ler (cases/, gallery/, assets/) arşive alınmadı.

### oversized-cursor  ·  heygen-com/hyperframes @ f8309b3  ·  puan 100 (A)

- **Ne yapar:** Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasası, uç hedefleme ve tıklama vuruşu, tıklamanın bir sonraki vuruşu ateşlemesi ve sahneler arası çıkış/devir.
- **Ne zaman:** UI sahnesinde imleç/işaretçi eylemi olduğunda veya sahne durağan kaldığında ucuz hareket kaynağı olarak. · **Ne zaman değil:** İmleç içermeyen sahneler; gerçek ekran kaydı (playwright-recording).
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi · **Globalde:** claude:ayni, codex:ayni, agents:farkli
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa, kontrol listeli ve UI demo videolarında yüksek getirili.

### playwright-recording  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 93 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### provider-refresh-oct23  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 98 (A)

- **Ne yapar:** API contracts and production routing for the October 23, 2026 provider refresh.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 8.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** otomatik

### referans  ·  leodavincs/kalem @ ba19c9f  ·  puan 71 (B)

- **Ne yapar:** Beğenilen bir referans videoyu sahnelere böler, her sahneden kare çıkarır ve kareleri inceleyip sahne başına İngilizce video istemi (prompt) yazar. Çıktı: istemler.md ve kopyala düğmeli istemler.html. Videoyu üretmez, yalnız istem çıkarır.
- **Ne zaman:** Elindeki bir videonun tarzını kendi video aracında (Veo, Kling, Seedance…) yeniden üretmek için sahne sahne istem istediğinde. · **Ne zaman değil:** DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür. Video sitesinden indirme yapmaz; dosya elinde olmalı (indirme için video-download). İstemleri çalıştırmak için ai-video-gen skilleri.
- **Teknoloji:** python, ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** leodavincs (kisi, ★106, son güncelleme 2026-11-06, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** referans-videodan-istem → birincil
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (referans-videodan-istem grubunda birincil, tek üye). MIT. Ücretsiz, çevrimdışı; karelerdeki yazıyı veri sayar (prompt enjeksiyonuna karşı açık kural). DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür.

### remotion  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 78 (B)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### remotion-best-practices  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Entry point and router for Remotion (React video framework) work: points to the right sub-guide for creating a video or project, React markup, animations, captions, maps, multimedia, interactivity, rendering, Studio preview, SaaS apps, docs search, licensing and upgrades. Use whenever the user works on a Remotion project or wants to make videos programmatically with React.
- **Teknoloji:** node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-best-practices@calesthio  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 100 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** remotion-cercevesi → birincil · **Roller:** video-kompozisyon
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil.

### remotion-best-practices@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Entry point and router for Remotion (React video framework) work: points to the right sub-guide for creating a video or project, React markup, animations, captions, maps, multimedia, interactivity, rendering, Studio preview, SaaS apps, docs search, licensing and upgrades. Use whenever the user works on a Remotion project or wants to make videos programmatically with React.
- **Teknoloji:** node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 1059 KB (SKILL.md 2.9 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-captions  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Transcribing, displaying and animating captions
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-captions@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Transcribing, displaying and animating captions
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 12 KB (SKILL.md 0.9 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-create  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Scaffold a new Remotion project and build a new video composition (create-video, layout, Tailwind). Use when the user asks to make, create or build a new video or composition with Remotion, or no Remotion project exists yet.
- **Teknoloji:** git, node, react, remotion, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-create@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Scaffold a new Remotion project and build a new video composition (create-video, layout, Tailwind). Use when the user asks to make, create or build a new video or composition with Remotion, or no Remotion project exists yet.
- **Teknoloji:** git, node, react, remotion, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 5 KB (SKILL.md 2.2 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-docs  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Search and read current Remotion documentation via its docs search API. Use when you need up-to-date Remotion API details, props or examples instead of relying on memory.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-docs@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Search and read current Remotion documentation via its docs search API. Use when you need up-to-date Remotion API details, props or examples instead of relying on memory.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 1.3 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-interactivity  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Structure Remotion markup for interactivity
- **Teknoloji:** css, html, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-interactivity@openai  ·  openai/plugins @ b767f8f  ·  puan 74 (B)

- **Ne yapar:** Structure Remotion markup for interactivity
- **Teknoloji:** css, html, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 9 KB (SKILL.md 7.3 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-license  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 91 (A)

- **Ne yapar:** Find Remotion license information, FAQs, terms, and where to buy a license.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 0.5 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-maps  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Animated maps in Remotion videos: static satellite maps, Mapbox, MapLibre, MapTiler, GeoJSON routes and markers, and 3D geographic flyovers. Use when a Remotion video needs a map, animated route, location explainer or globe.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 477 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-maps@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Animated maps in Remotion videos: static satellite maps, Mapbox, MapLibre, MapTiler, GeoJSON routes and markers, and 3D geographic flyovers. Use when a Remotion video needs a map, animated route, location explainer or globe.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 454 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-markup  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Content, animation and effects best practices
- **Teknoloji:** canvas, css, ffmpeg, html, lottie, node, react, remotion, tailwind, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 123 KB (SKILL.md 13.2 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-markup@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Content, animation and effects best practices
- **Teknoloji:** canvas, css, ffmpeg, html, lottie, node, react, remotion, tailwind, three.js, webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 548 KB (SKILL.md 10.6 KB, yük orta)
- **İnceleme:** otomatik

### remotion-multimedia  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Read and process audio/video files in the browser with Mediabunny for Remotion: get audio or video duration and dimensions, trim, crop and inspect metadata. Use when a Remotion composition needs media durations, sizes or browser-side media processing.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 0.7 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-multimedia@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Read and process audio/video files in the browser with Mediabunny for Remotion: get audio or video duration and dimensions, trim, crop and inspect metadata. Use when a Remotion composition needs media durations, sizes or browser-side media processing.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 7 KB (SKILL.md 0.7 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-render  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Render and export Remotion videos and stills: npx remotion render/still, codecs, transparent videos and render flags. Use when the user wants to export, render or download an MP4/WebM/GIF/PNG from a Remotion project.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-render@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Render and export Remotion videos and stills: npx remotion render/still, codecs, transparent videos and render flags. Use when the user wants to export, render or download an MP4/WebM/GIF/PNG from a Remotion project.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 4 KB (SKILL.md 0.5 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-saas  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Build an app on top of Remotion: SaaS templates and frameworks, embedding @remotion/player in React (or Vue, Angular, Svelte), and client- vs server-side rendering (Lambda, Vercel, Node.js, Cloudflare). Use when making a video-generation product, editor or form-to-video app with Remotion.
- **Teknoloji:** node, react, remotion, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-saas@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Build an app on top of Remotion: SaaS templates and frameworks, embedding @remotion/player in React (or Vue, Angular, Svelte), and client- vs server-side rendering (Lambda, Vercel, Node.js, Cloudflare). Use when making a video-generation product, editor or form-to-video app with Remotion.
- **Teknoloji:** node, react, remotion, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 8 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-studio  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Start and use Remotion Studio to preview a video while building it (npx remotion studio, --no-open with an in-app browser, useful flags). Use when creating or editing a Remotion video and the user should see a live preview.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-studio@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Start and use Remotion Studio to preview a video while building it (npx remotion studio, --no-open with an in-app browser, useful flags). Use when creating or editing a Remotion video and the user should see a live preview.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 2 KB (SKILL.md 0.9 KB, yük kucuk)
- **İnceleme:** otomatik

### remotion-to-hyperframes  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** Başka araçlarla yapılmış video kodunu ya da çıktısını HyperFrames'e alır ve kare kare karşılaştırarak doğrular: Native (Remotion/HTML/GSAP çevirisi), Hosted (canvas, p5, Three.js, Lottie kodunu HyperFrames zamanıyla sürme), Media (Manim, After Effects, Blender çıktısını klip olarak koyma).
- **Ne zaman:** Remotion projesini taşımak; Lottie/Three.js/p5 animasyonlarını ya da Manim/AE renderlarını HyperFrames videosunda kullanmak. · **Ne zaman değil:** Sıfırdan yeni video (hyperframes yeter).
- **Teknoloji:** hyperframes, remotion, react, python · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:farkli, agents:farkli
- **Boyut:** 164 KB (SKILL.md 4.9 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — 2026-11: SSIM karşılaştırması betikler yerine `npx hyperframes diff` komutuna taşındı (render_diff.sh/frame_strip.sh kaldırıldı); box-sizing kuralı ve lottie/timing notları eklendi. Üç seviyeli model (Native/Hosted/Media) korunuyor.

### remotion-upgrade  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 89 (A)

- **Ne yapar:** Upgrade Remotion and all @remotion/* packages to the same latest version, align auxiliary dependencies and update installed Remotion skills. Use when the user asks to upgrade or update Remotion, or Remotion package versions are mismatched.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-upgrade@openai  ·  openai/plugins @ b767f8f  ·  puan 72 (B)

- **Ne yapar:** Upgrade Remotion and all @remotion/* packages to the same latest version, align auxiliary dependencies and update installed Remotion skills. Use when the user asks to upgrade or update Remotion, or Remotion package versions are mismatched.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** openai (kurum, resmî, ★7752, son güncelleme 2026-11-03, lisans yok)
- **Durum:** alternatif
- **Boyut:** 3 KB (SKILL.md 1.8 KB, yük kucuk)
- **İnceleme:** otomatik

### slideshow  ·  heygen-com/hyperframes @ f8309b3  ·  puan 97 (A)

- **Ne yapar:** HyperFrames ile canlı sunulan slayt gösterisi kurar: her slayt bir sahne, JSON adası ile fragment reveal, dallanan hotspot'lar ve konuşmacı notları; `hyperframes present` ile sunulur; var olan bir sayfayı desteye çevirme kuralları içerir.
- **Ne zaman:** MP4 yerine canlı sunulacak deste/pitch deck; mevcut bir web sayfasını sunuma çevirmek. · **Ne zaman değil:** Render edilmiş video isteniyorsa (hyperframes); PowerPoint dosyası gerekiyorsa (pptx).
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★78940, son güncelleme 2026-11-05, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** sunum-desteleri → tamamlayıcı · **Roller:** video-kompozisyon · **Globalde:** claude:ayni, agents:ayni
- **Boyut:** 48 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede SKILL.md 497 satırdan ~45 satıra indi; kurallar özlü. ttsScript alanları henüz bağlı değil.

### social-auto-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 为 social-auto-upload 提供总入口，按平台和内容类型选择对应发布流程。Use when 用户要在本仓库支持的平台发布视频、文章或图文，或需要把内容分发到多个指定平台。
- **Teknoloji:** node _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 2.5 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### social-reddit-card  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.5 KB, yük kucuk)
- **İnceleme:** otomatik

### social-spotify-card  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepages.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.8 KB, yük kucuk)
- **İnceleme:** otomatik

### social-x-post-card  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards.
- **Teknoloji:** css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### swiss-user-research-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Swiss-style user-research narrative template in warm-paper editorial aesthetics. Use when users ask for a premium research deck or story-first live artifact with minimalist typography, high-clarity layout, subtle motion, donut breakdowns, and keyboard/click navigation across slides in a single HTML file.
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### synthetic-screen-recording  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 85 (A)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### tencent-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau tencent` 登录视频号并发布或定时发布视频、保存草稿。Use when 用户要向微信视频号发布视频或检查视频号账号状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 1.5 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### tiktok-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用仓库现有 Patchright/Playwright Chrome 上传器登录并发布 TikTok 视频。Use when 用户要发布 TikTok 视频，且当前环境可访问本仓库及其本地 Chrome 配置。
- **Teknoloji:** playwright, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### vfx-text-cursor  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 3.6 KB, yük kucuk)
- **İnceleme:** otomatik

### video-download  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 94 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 100 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-edit@yildizdikme  ·  YildizDikme/claude-video-edit @ b7093e2  ·  puan 68 (B)

- **Ne yapar:** Konuşan kişi (talking-head), eğitim ve Short videoları için kurgu: Whisper ile kelime hassasiyetli kesim, HTML+GSAP sahneler, Python'la sentezlenen ses efektleri, ses seviyesi (loudness) ayarı ve kare-doğru render.
- **Ne zaman:** Tek kişilik anlatım videosunu kelime düzeyinde temizleyip hareketli grafik ve SFX ile Short'a çevirmek. · **Ne zaman değil:** DİKKAT: adı 'video-edit'; globalde OpenMontage'in video-edit'i olduğu için Claude onu kullanır, bu skill gölgede kalır. Betik yollarını ~/.claude/skills/video-edit varsayar (projeye kurulunca yollar kırılır); ~/.claude/video-edit/ altına profil ve brand/ yazar. Genel kurgu için OpenMontage video-edit, altyazı için embedded-captions, kesim için talking-head-recut.
- **Teknoloji:** python, ffmpeg, whisper, gsap, html · **Paketler:** ffmpeg, whisper, chrome
- **Claude / Codex:** tam / tam
- **Geliştirici:** YildizDikme (kisi, ★33, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** ffmpeg-kurgu → alternatif · **Globalde:** claude:farkli
- **Boyut:** 730 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (kullanıcı isteğiyle; ffmpeg-kurgu grubu, OpenMontage video-edit tercih). MIT, 32★, çok yeni. Yerel, ücretsiz, ağ yok (serve.py sadece 127.0.0.1).

### video-hyperframes  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Hyperframes / Remotion-compatible continuous frame animation with autoplay support.
- **Teknoloji:** html, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 10 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** otomatik

### video-shotcraft  ·  Vincentwei1021/video-shotcraft @ 1266a3e  ·  puan 97 (A)

- **Ne yapar:** Create cinematic product videos from frontend projects or webpages with Remotion, real page captures, shot cards, the Ink Press template, beat sync and sound design. Use for full product promos, reproducing Ink Press, single shot-card effects, or finding, adding, replacing and aligning sound effects in an existing product video or shot, including candidate-only SFX searches. 用真实页面、镜头卡与 Ink Press 模
- **Teknoloji:** api-anahtari, ffmpeg, git, html, node, python, r3f, react, remotion, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** Vincentwei1021 (kisi, ★16988, son güncelleme 2026-10-29, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 28250 KB (SKILL.md 21.2 KB, yük orta) · **Bağımlılık:** Remotion (Node.js; npx remotion). Ürün videoları için Remotion projesi gerekir.
- **İnceleme:** otomatik

### video-toolkit  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 77 (B)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 93 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-kurgu-render, ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  OpenMontageInc/OpenMontage @ 195eab2  ·  puan 94 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★78702, son güncelleme 2026-11-08, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-kurgu-render · **Globalde:** claude:ayni
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### weibo-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau weibo` 登录微博并发布视频，可指定封面。Use when 用户要向微博发布视频或检查微博账号状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### weread-year-in-review-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** WeRead-inspired HyperFrames video template for vertical annual reading reports, personal reading dashboards, book-note recaps, and shareable year-in-review stories. Use when users want a 9:16 HTML-to-MP4 reading report with warm paper texture, editorial Chinese typography, book-page metaphors, data highlights, and deterministic motion.
- **Teknoloji:** html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 33 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** otomatik

### xiaohongshu-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 当 agent 需要通过已安装的 `sau` CLI 完成小红书登录、cookie 校验、视频上传或图文发布时使用这个 skill。该 skill 适用于已经安装 `social-auto-upload` 且可调用 `sau` 命令的环境。优先使用这个 skill 进行稳定的命令式小红书工作流，而不是一开始就阅读 uploader 源码。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 11 KB (SKILL.md 2.8 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### xueqiu-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 87 (A)

- **Ne yapar:** 通过 social-auto-upload 的 sau CLI 登录和核验雪球账号，发布 HTML、Markdown 或 TXT 长文，保留原稿段间配图、原生文字结构与独立封面，并查询原作品确认结果。适用于雪球创作者平台，不支持定时或视频。
- **Teknoloji:** css, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.3 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır). · **Kırık bağlantı:** 1
- **İnceleme:** otomatik

### youtube-downloader  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 70 (B)

- **Ne yapar:** yt-dlp kullanan download_video.py betiğiyle YouTube videosu indirir: kalite (best…360p), format (mp4/webm/mkv) ve yalnızca ses (MP3) seçenekleri; yt-dlp yoksa kendisi kurar.
- **Ne zaman:** Tek bir YouTube videosunu ya da sesini hızlıca indirmek. · **Ne zaman değil:** Varsayılan çıktı yolu /mnt/user-data/outputs/ (claude.ai sandbox'ı) — yerelde -o ile yol ver. Altyazı/transkript, oynatma listesi veya çok platform için OpenMontage video-download (birincil). Telif hakkı korumalı içerikte.
- **Teknoloji:** python, yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★78745, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** video-indirme → alternatif
- **Boyut:** 7 KB (SKILL.md 2.6 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Basit ve çalışır betik; sandbox'a özgü varsayılan yol ve otomatik pip kurulumu eksi. Kategori: video indirme g-video-ses-medya/01 kapsamında, oraya taşındı ve video-indirme grubuna alternatif olarak eklendi.

### youtube-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau youtube` 登录 YouTube 并上传、安排定时或设置视频可见范围。Use when 用户要向 YouTube 发布或定时发布视频，或检查 Google/YouTube 登录状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.4 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### zhihu-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 87 (A)

- **Ne yapar:** 使用 social-auto-upload 的 sau CLI 登录知乎、发布文章或视频，并按作品链接核对结果；支持原稿位置配图与视频领域、声明选项。
- **Teknoloji:** css, html, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır). · **Kırık bağlantı:** 1
- **İnceleme:** otomatik
