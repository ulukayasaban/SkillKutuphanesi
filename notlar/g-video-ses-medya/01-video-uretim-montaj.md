# 01-video-uretim-montaj — Video, Ses ve AI Medya Üretimi

_Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **68/119**

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

### ajanla-video-kurgu  ·  avenoxai/avenox-video-kurgu-notlari @ dba60a2  ·  puan 69 (B)

- **Ne yapar:** Kodlama ajanıyla (Claude Code, Codex vb.) 'slop' çıkarmayan video kurgu atölyesi düzeni: ses/transkript temizliği, boşluk ve tekrar kesimi, pano haritası, tek şef altında paralel ajanlar, dosya sözleşmesi ve teslim formu, 'aynı hata iki kez olursa koda yaz' kapıları, marka kilidi, dört parçalı prompt, görsel/video üretim maliyeti, render kuyruğu ve kısa form/dikey motion. Bir araç değil, yöntem; Türkçe.
- **Ne zaman:** Ajanla çok adımlı video üretimi kurarken iş bölümü, kalite kapısı ve marka tutarlılığı için çerçeve; marka/atölye dosyalarını (atolye/atolye.md, marka.md) şablonlarla başlatmak. · **Ne zaman değil:** Doğrudan kesim/render komutları isteniyorsa araç skilleri (auto-editor, video-use, HyperFrames); küçük tek seferlik işte gereksiz ağır olur. Kaynak tek kişilik küçük bir repo (27 yıldız).
- **Teknoloji:** metodoloji, whisper, hyperframes · **Paketler:** yok (yalnız .md; whisper/HyperFrames/görsel üretim araçları isteğe bağlı)
- **Claude / Codex:** tam / tam
- **Geliştirici:** avenoxai (kisi, ★27, son güncelleme 2026-11-06, lisans MIT)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → tamamlayıcı · **Roller:** video-kurgu-render, planlayici
- **Boyut:** 38 KB (SKILL.md 7.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Özgün ve uygulanabilir süreç fikirleri (tek şef, teslim formu, kapılar, sayı ver), ama kaynak küçük/yeni, kod ya da betik içermez ve bazı bölümler yazarın kendi araç/marka bağlamına özgü. Güvenlik: yalnız Markdown, betik/kurulum/ağ satırı, gizli anahtar istemi ya da genel klasöre yazma yok; ücretli görsel/video üretimini yalnız maliyet gerekçesiyle anlatır (isteğe bağlı). Örtüşme: video-use'un yöntem tarafını tamamlar.

### alipay-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 social-auto-upload 的 `sau alipay` 登录支付宝生活号并发布视频。Use when 用户要向支付宝生活号发布视频或检查创作账号状态。
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### auto-editor  ·  WyattBlue/auto-editor @ 0f808d8  ·  puan 84 (A)

- **Ne yapar:** auto-editor komut satırı aracıyla video ve ses kurgusunun çekirdeği: sessizliği, hareketsizliği ya da siyah kareleri bulup keser; eşik, boşluk payı ve tempo ayarlar; el ile kesme ve hız aralıkları verir; mikrofondan kayıt alıp doğrudan düzenler. Önizleme (--preview) ve etiket (--edit:N / --when:N) sistemiyle birden çok kesim sınıfı tanımlanabilir.
- **Ne zaman:** Konuşmalı videolardan, podcast ve ders kayıtlarından ölü anları otomatik atmak; kaydı kısaltmak; sesle ya da harekete göre kesim yapmak; mikrofonu kaydedip hemen kırpmak. · **Ne zaman değil:** Yaratıcı efekt, geçiş, editöre aktarma ya da konuşma metnine göre kesim için kardeş skiller (auto-editor-effects, -transitions, -export, -transcribe) gerekir; sahne/plan düzeyinde kurgu kararı için video-use gibi konuşmayla kurgu skilleri.
- **Teknoloji:** auto-editor, ffmpeg · **Paketler:** auto-editor (CLI), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** WyattBlue (kisi, ★5918, son güncelleme 2026-11-15, lisans Unlicense)
- **Durum:** tercih · **Örtüşme:** auto-editor-kurgu → birincil · **Roller:** video-kurgu-render
- **Boyut:** 7 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** auto-editor komut satırı aracı kurulu olmalı (kurulum yolu: https://auto-editor.com/installing; ya da repodaki ./auto-editor) ve ffmpeg. auto-editor-transcribe skili whisper.cpp (HuggingFace'ten ggml model indirir) ya da Apple Speech arka ucunu kullanır; hepsi yereldir, ücretli API yok.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (ailenin birincili). Ölçülü, doğru ve örneklerle dolu başvuru: yöntem tablosu, bool işleçleri, 'Bad kind' tuzağı, etiket sistemi. Lisans Unlicense. Güvenlik: betik ya da ağdan indirip çalıştıran satır yok, gizli anahtar istemiyor, genel klasöre yazmıyor; yalnız yerel auto-editor komutları. Sabit yol yok. Örtüşme: ffmpeg-kurgu ve video-edit ile aynı işi yerel CLI ile yapar; auto-editor ailesi kendi içinde birlikte kullanılır.

### auto-editor-effects  ·  WyattBlue/auto-editor @ 0f808d8  ·  puan 84 (A)

- **Ne yapar:** auto-editor'da bölümlere eylem ve animasyon uygulama: hız (perde korunarak), ses kısma/çıkarma, de-esser, high/low-pass, hum temizleme, zoom/Ken Burns, döndürme, kutu çizme, logo ya da resim-içinde-resim bindirme; değerler 'a..b' rampası, easing ve zamanlı anahtar karelerle canlandırılır.
- **Ne zaman:** Sessiz bölümleri hızlandırmak ya da kısmak, konuşmayı temizlemek (de-ess, rumble, hum), basit zoom ve fade animasyonları, logo ve PiP bindirmek; hepsini tek komutta, ayrı bir editör açmadan. · **Ne zaman değil:** Düz sessizlik kesimi için auto-editor; geçişler için auto-editor-transitions; çok katmanlı, tasarımlı kompozisyon için HyperFrames ya da Remotion.
- **Teknoloji:** auto-editor, ffmpeg · **Paketler:** auto-editor (CLI), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** WyattBlue (kisi, ★5918, son güncelleme 2026-11-15, lisans Unlicense)
- **Durum:** tercih · **Örtüşme:** auto-editor-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 7 KB (SKILL.md 7.4 KB, yük kucuk) · **Bağımlılık:** auto-editor komut satırı aracı kurulu olmalı (kurulum yolu: https://auto-editor.com/installing; ya da repodaki ./auto-editor) ve ffmpeg. auto-editor-transcribe skili whisper.cpp (HuggingFace'ten ggml model indirir) ya da Apple Speech arka ucunu kullanır; hepsi yereldir, ücretli API yok.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Eylem tablosu ve rampa/easing sözdizimi eksiksiz. Not: otomatik etiket 'api-anahtari' yanlış pozitif; SKILL.md'deki `ease:` ('token' sözcüğü) API anahtarı istemez, API anahtarı gerekmiyor. Güvenlik: betik ya da ağdan indirip çalıştıran satır yok, gizli anahtar istemiyor, genel klasöre yazmıyor; yalnız yerel auto-editor komutları. Sabit yol yok. Örtüşme: ffmpeg-kurgu ve video-edit ile aynı işi yerel CLI ile yapar; auto-editor ailesi kendi içinde birlikte kullanılır.

### auto-editor-export  ·  WyattBlue/auto-editor @ 0f808d8  ·  puan 84 (A)

- **Ne yapar:** auto-editor'ün kurgusunu bitmiş video yerine düzenleyici projesi olarak dışa aktarma: Premiere (XML), DaVinci Resolve, Final Cut Pro, ShotCut, Kdenlive, EDL, parça parça klipler ve .v1/.v2/.v3 zaman çizelgesi dosyaları; mikrofon kaydını kayıpsız (FLAC) yan dosyayla saklar; XML/EDL/FCPXML dosyalarını geri içe aktarıp render eder.
- **Ne zaman:** Otomatik kesimi bir editörde elle inceleyip cilalamak; kesim noktalarından klip dizisi çıkarmak; bir zaman çizelgesini tekrar videoya çevirmek. · **Ne zaman değil:** Doğrudan bitmiş video isteniyorsa auto-editor yeterli; geçişlerin editöre taşınması için auto-editor-transitions ile birlikte okunmalı.
- **Teknoloji:** auto-editor, ffmpeg · **Paketler:** auto-editor (CLI), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** WyattBlue (kisi, ★5918, son güncelleme 2026-11-15, lisans Unlicense)
- **Durum:** tercih · **Örtüşme:** auto-editor-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 5 KB (SKILL.md 4.9 KB, yük kucuk) · **Bağımlılık:** auto-editor komut satırı aracı kurulu olmalı (kurulum yolu: https://auto-editor.com/installing; ya da repodaki ./auto-editor) ve ffmpeg. auto-editor-transcribe skili whisper.cpp (HuggingFace'ten ggml model indirir) ya da Apple Speech arka ucunu kullanır; hepsi yereldir, ücretli API yok.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Hedef biçim tablosu ve içe aktarma kapsamı net. Güvenlik: betik ya da ağdan indirip çalıştıran satır yok, gizli anahtar istemiyor, genel klasöre yazmıyor; yalnız yerel auto-editor komutları. Sabit yol yok. Örtüşme: ffmpeg-kurgu ve video-edit ile aynı işi yerel CLI ile yapar; auto-editor ailesi kendi içinde birlikte kullanılır.

### auto-editor-transcribe  ·  WyattBlue/auto-editor @ 0f808d8  ·  puan 84 (A)

- **Ne yapar:** auto-editor'ün whisper alt komutuyla ses/video ya da canlı mikrofonu metne ve altyazıya (SRT/JSON) çevirme; Whisper (ggml), Parakeet ve Apple Speech (macOS 26+) arka uçları. Çıkan altyazıya göre 'subtitle'/'word' yöntemiyle konuşulan söze bakarak kesme (ör. dolgu sözcüklerini atma) sağlar.
- **Ne zaman:** Yerelde, API anahtarsız transkript ve altyazı üretmek; 'şu kelimenin geçtiği yeri tut/at' tarzı söze dayalı kesim. · **Ne zaman değil:** Kelime düzeyi hassas, çok konuşmacılı, ticari kalite transkript gerekirse bulut servisli skiller (ör. video-use + ElevenLabs Scribe); ggml model dosyası (HuggingFace'ten) önceden elle indirilmelidir.
- **Teknoloji:** auto-editor, ffmpeg, whisper.cpp · **Paketler:** auto-editor (CLI), ffmpeg, ggml Whisper/Parakeet model dosyası (isteğe bağlı: Apple Speech)
- **Claude / Codex:** tam / tam
- **Geliştirici:** WyattBlue (kisi, ★5918, son güncelleme 2026-11-15, lisans Unlicense)
- **Durum:** tercih · **Örtüşme:** auto-editor-kurgu → tamamlayıcı · **Roller:** video-kurgu-render, ses-tasarimci
- **Boyut:** 5 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** auto-editor komut satırı aracı kurulu olmalı (kurulum yolu: https://auto-editor.com/installing; ya da repodaki ./auto-editor) ve ffmpeg. auto-editor-transcribe skili whisper.cpp (HuggingFace'ten ggml model indirir) ya da Apple Speech arka ucunu kullanır; hepsi yereldir, ücretli API yok.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Üç arka ucu ve sidecar .srt otomatik yüklemesini doğru anlatıyor. Ağ: yalnız model dosyası (kullanıcı HuggingFace'ten kendisi indirir) ve Apple modelinin ilk kullanımı; ses yerelde kalır. Güvenlik: betik ya da ağdan indirip çalıştıran satır yok, gizli anahtar istemiyor, genel klasöre yazmıyor; yalnız yerel auto-editor komutları. Sabit yol yok. Örtüşme: ffmpeg-kurgu ve video-edit ile aynı işi yerel CLI ile yapar; auto-editor ailesi kendi içinde birlikte kullanılır.

### auto-editor-transitions  ·  WyattBlue/auto-editor @ 0f808d8  ·  puan 84 (A)

- **Ne yapar:** auto-editor'ün kesim noktalarına geçiş ekleme: çapraz geçiş, Premiere Pro'nun bütün geçiş adları (push, clock-wipe, glitch, page-peel, iris-round vb.) ve ses çapraz solmaları; süre ve en kısa kesim eşiği ayarı; v3 zaman çizelgesinde kesim başına özel geçiş; geçişlerin hangi editör dışa aktarmalarında korunduğunu tablolar (premiere-otio'da hepsi).
- **Ne zaman:** Konuşmalı videoda yumuşak kesimler, açılış/kapanış solması, belirli bir geçiş stili; geçişleri Premiere/Resolve/Final Cut'a taşımak. · **Ne zaman değil:** Yalnız sert kesim yeterliyse gerek yok; Premiere'in birebir görünümü için premiere-otio dışa aktarımı ve editörde render önerilir (auto-editor'ün kendi render'ı 'glitch' gibi etkilerde farklı olur).
- **Teknoloji:** auto-editor, ffmpeg · **Paketler:** auto-editor (CLI), ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** WyattBlue (kisi, ★5918, son güncelleme 2026-11-15, lisans Unlicense)
- **Durum:** tercih · **Örtüşme:** auto-editor-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 7 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** auto-editor komut satırı aracı kurulu olmalı (kurulum yolu: https://auto-editor.com/installing; ya da repodaki ./auto-editor) ve ffmpeg. auto-editor-transcribe skili whisper.cpp (HuggingFace'ten ggml model indirir) ya da Apple Speech arka ucunu kullanır; hepsi yereldir, ücretli API yok.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (tamamlayıcı). Sınırları dürüstçe belirtiyor (hangi geçişin Premiere ile ölçüldüğü, editörde ne kaybolduğu). Güvenlik: betik ya da ağdan indirip çalıştıran satır yok, gizli anahtar istemiyor, genel klasöre yazmıyor; yalnız yerel auto-editor komutları. Sabit yol yok. Örtüşme: ffmpeg-kurgu ve video-edit ile aynı işi yerel CLI ile yapar; auto-editor ailesi kendi içinde birlikte kullanılır.

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

### brag  ·  latent-spaces/brag @ 0637943  ·  puan 85 (A)

- **Ne yapar:** Çalışılan projenin kodunu okuyup 15-25 saniyelik, paylaşılabilir bir tanıtım videosu üretir (HyperFrames ile): konsept, senaryo, storyboard, kompozisyon, doğrulama, render ve paylaşım metni. Hazır müzik (CC BY 4.0) ve 228 ses efektiyle gelir; ton ön ayarları (chaotic, polished, yc-parody, cinematic...), dikey/yatay/kare biçim ve isteğe bağlı yerel Kokoro anlatım (--voice) var.
- **Ne zaman:** Yeni yapılan bir uygulama ya da site için hızlı, esprili ya da cilalı tanıtım/paylaşım videosu ("/brag", "make a launch video") istendiğinde. · **Ne zaman değil:** Çok kareli ayrıntılı ürün filmi, anlatımlı eğitim videosu ya da proje kodu olmayan işler için değil. Yeni modellerde (Opus/Sonnet 5.5, Fable) otomatik olarak brag-slim'e yönlendirir; tam akış için --full gerekir.
- **Teknoloji:** hyperframes, gsap, node, ffmpeg, python · **Paketler:** hyperframes (npx), ffmpeg, python3 (müzik ipucu betiği)
- **Claude / Codex:** tam / tam
- **Geliştirici:** latent-spaces (kurum, ★21811, son güncelleme 2026-11-15, lisans MIT)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 16211 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** brag HyperFrames (npx hyperframes) ile çalışır; brag-slim ek kurulum istemez, makinedeki araçları kullanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Dar ve kararlı bir iş akışı; proje kodundan başlayıp kapı kapı ilerliyor, ton ve süre kuralları net, GitHub'da çok ilgi görmüş (21 bin yıldız). Yukarı akım notu: SKILL.md'deki references/format.md, look.md, motion.md ve story.md brag'a ait değil, kütüphanedeki hyperframes skilinin referanslarıdır (hyperframes'te bulundu); skill-calistir'in 'eksik' uyarısı yanlış alarmdır, brag yalnız hyperframes ile birlikte kurulursa tam çalışır. Lisans: kod MIT; paketli müzik (Sascha Ende, CC BY 4.0) repo lisansının dışında, kullanımda atıf gerekir. 291 dosya (228 ogg, 32 wav, 5 mp3) boyutu şişirir. Ücret: ucretsiz (Kokoro anlatım yerel). Güvenlik: DİKKAT (orta) — npx hyperframes ve bir Python analiz betiği; ağdan çalıştırılan satır yok, gizli anahtar istemiyor. Sabit yol: references/audio.md:36'daki ~/.claude/skills/brag örnek metindir (yol yalnız sayım sütununda, uyarı değil). Örtüşme: urun-tanitim-filmi grubunda onetake birincil kalır; projenin kendi kodundan hızlı tanıtım teaseri için brag/brag-slim ilk tercihtir.

### brag-slim  ·  latent-spaces/brag @ 0637943  ·  puan 85 (A)

- **Ne yapar:** Tek dosyalık, paketli varlığı olmayan brag sürümü: bir proje klasörünü ya da web sitesi URL'sini alıp müzik, hareket ve paylaşım metniyle 15-25 saniyelik tanıtım videosu üretir; modelin makinedeki araçlarla (ffmpeg, başsız tarayıcı) kendi yaptığı iş akışı. Proje kodunu doğrudan içe aktarır, gizli dosyaları (.env, anahtar) okumaz.
- **Ne zaman:** Tam brag'ın paketli varlıklarına gerek olmadan, hafif ve model odaklı tanıtım videosu; proje ya da canlı site girdisi. · **Ne zaman değil:** --voice (anlatım) desteklemez; HyperFrames şablon disiplinine ihtiyaç varsa brag'ı seç. Sıfır varlık demek müzik/SFX'i modelin üretmesi demek, kalite modele bağlıdır.
- **Teknoloji:** ffmpeg, node, html-canvas · **Paketler:** ffmpeg, başsız tarayıcı
- **Claude / Codex:** tam / tam
- **Geliştirici:** latent-spaces (kurum, ★21811, son güncelleme 2026-11-15, lisans MIT)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta) · **Bağımlılık:** brag HyperFrames (npx hyperframes) ile çalışır; brag-slim ek kurulum istemez, makinedeki araçları kullanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif). Kısa ve disiplinli: yaratıcı yasalar (kısa, yabancıya net, ritme kesim), gizli veri sızdırmama kuralı (anahtar, e-posta, iç URL videoya girmez) ve eksik araç için 'önce sor, curl | sh yerine paket yöneticisi' kuralı güvenli bir tasarım. Web sitesi girdisinde indirilen işaretlemeyi 'inert içerik' sayar ve betiklerini ayıklar, indirilen hiçbir şeyi çalıştırmaz. Ücret: ucretsiz. Lisans: MIT. Güvenlik: temiz — betik/kurulum komutu yok; tek 'curl | sh' geçişi yasaklayıcı bağlamda. Örtüşme: urun-tanitim-filmi grubunda alternatif.

### camera-3d-captions  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 79 (B)

- **Ne yapar:** Sabit kameralı konuşan kafa görüntüsünde altyazıları 3B uzayda oynatır: kamera konuşmacı ile kelimeler arasında uçar, kelime grupları farklı derinlikte durur, vurgu kelimeleri alfa matte ile konuşmacının ARKASINA saklanır, kelime halkası etrafında döner, derinlik odağı kayar. After Effects hareketini HyperFrames'te kare kare deterministik çizerek yeniden kurar.
- **Ne zaman:** Avatar ya da gerçek konuşmacı çekiminde (yatay, orta plan ve geniş, 5-20 sn) kelimelerin konuşmacının etrafında derinlikte performans göstermesi istendiğinde ("3D text", "text behind the speaker"). · **Ne zaman değil:** Düz altyazı, hareketli/elde kamera, aşırı yakın plan ya da kişiyi ayıramayan modeller için değil.
- **Teknoloji:** hyperframes, gsap, ffmpeg, python · **Paketler:** hyperframes@0.8.62 (npx), ffmpeg, fonttools, numpy, pillow, p5-paint-animation (elle çizim stili için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** altyazi → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 90 KB (SKILL.md 8.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (koşullu, niş). Gereksinimler ve yan etkiler 'tam liste' olarak yazılmış (sürüm sabitli HyperFrames, 170 MB kişi segmentasyon modeli indirir, GSAP CDN'den yüklenir), sınırlar dürüstçe anlatılmış, QC adımları var. Çok özelleşmiş ve ileri düzey. Ücret: ucretsiz (yerel; hiçbir şey yüklenmez). Lisans: Apache-2.0. Güvenlik: DİKKAT (orta) — npx ile CLI indirir, model indirir, yerel Python/shell betikleri (prep-take.sh, build-sprites.py); anahtar yok. Örtüşme: altyazi grubunda captions-overlay ile tamamlayıcı (3B stil).

### captions-overlay  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videolarında altyazı doktrini: her cümle drop / rail / embed olarak sınıflanır (embed nadir zirve), altyazı alttan rezerve bir şerit değil filmin üstüne bindirilen overlay'dir; kompozisyon gerçek dikey merkeze göre yerleşir.
- **Ne zaman:** Konuşan kafa, tanıtım ya da explainer videolarına altyazı eklerken yerleşim ve vurgu kararları. · **Ne zaman değil:** Altyazısız videolar; altyazının teknik kurulumu için hyperframes references/captions.md yeterli.
- **Teknoloji:** hyperframes · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** altyazi → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 6 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede hyperframes'in references/captions.md dosyasının üstüne uygulanan doktrin olarak konumlandı (metadata internal: true). Emekli embedded-captions iş akışına atıf içeriyor; artık hyperframes skiliyle birlikte kullanılır.

### changelog-video  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 83 (A)

- **Ne yapar:** Haftalık changelog markdown'ını HeyGen markalı kare (1080) changelog videosuna çevirir: 'Annie' HeyGen seslendirmesi, animasyonlu marka arka planı, sahte UI görselleştirmeleri ve sakin altyazılar; fontlar, arka plan müziği ve betikler skill içinde paketli.
- **Ne zaman:** Yalnız HeyGen'in kendi haftalık changelog videosu için; kendi markan için örnek/şablon olarak incelenebilir. · **Ne zaman değil:** Kendi ürününün changelog videosunda doğrudan (pr-to-video veya product-launch-video kullan); marka varlıkları HeyGen'e ait.
- **Teknoloji:** hyperframes, html, gsap, node, heygen · **Paketler:** hyperframes (npx), node>=22, ffmpeg, HeyGen hesabı (TTS)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → alternatif
- **Boyut:** 521 KB (SKILL.md 13.2 KB, yük orta) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. HeyGen iç skilli (internal:true): HeyGen marka kimliğine, sabit seslendirmene ve repo köküne bağlı; paketlenen TT Norms Pro / ABC Solar ticari fontlarının yeniden kullanım lisansı belirsiz. Rollere eklenmedi. · 2026-11-12 yeniden incelendi: yalnız __player.seek çağrısı artık await ile (asenkron); değerlendirme aynı. Telemetri işareti yok (bu skill'de eklenmedi).

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

### create-video  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** HeyGen Video Agent ile tek bir metin isteminden komple video üretir; senaryo, avatar, görsel, seslendirme ve altyazıyı ajan kendisi seçer. Önce prompt-optimizer referansıyla sahne/zamanlama yapılandırılmış prompt yazılır, sonra iş gönderilip durum sorgulanır.
- **Ne zaman:** Hızlı taslak, tanıtım veya açıklayıcı videoyu avatar/ses ayrıntısı belirtmeden tek adımda almak istendiğinde. · **Ne zaman değil:** Tam metin, belirli avatar/ses veya sahne bazlı kontrol gerekiyorsa (avatar-video); kendi kompozisyonunu kurmak istiyorsan (hyperframes).
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → birincil · **Roller:** video-kompozisyon, ai-medya-uretici
- **Boyut:** 92 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı ve güncel HeyGen resmi skill'i; MCP varsa onu tercih ediyor. Ücretli API, sonuç kontrolü sınırlı.

### cut-mistakes  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 65 (B)

- **Ne yapar:** Konuşan kafa kaydındaki konuşma hatalarını (kekeleme, tekrarlanan kelime, yarım bırakılıp baştan alınan cümle, yeniden çekilen satırlar) bulur ve keser. Mekanik aday bulucu (find-cut-candidates) önerir, ajan her adayı bağlamda okur, kullanıcı onaylar, apply-cuts onaylı kesimleri ffmpeg ile uygular. Vurgu amaçlı tekrarı hata saymamak için inceleme kapısı zorunludur.
- **Ne zaman:** Video kurgu hattının 2. adımı: sessizlik kırpıldıktan sonra "cut the mistakes", "remove stutters", "keep the best take". · **Ne zaman değil:** Sessizlik kırpma (cut-silences), ham transkript yokken ya da bir doğal konuşmayı kota için kesmek için değil.
- **Teknoloji:** node, ffmpeg · **Paketler:** node, ffmpeg, kelime düzeyi transkript JSON
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 21 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Karar-kapılı ve dürüst (mekanik dedektör vurgu ile kekelemeyi ayıramaz, bu yüzden inceleme zorunlu). Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Bu skil için eksik olan scripts/build-edl-review.mjs (inceleme sayfası). Girdisi cut-silences'ın transkriptidir. Transkript için varsayılan sağlayıcı ElevenLabs Scribe: ses dosyası dış servise yüklenir (anahtar ve kota gerekir); yerel Whisper alternatifi anlatılıyor. Ücret: ucretsiz (skilin kendi betikleri yerel; transkript üretimi başka skilde). Lisans: MIT (repodaki LICENSE okundu; GitHub NOASSERTION gösteriyor). Güvenlik: DİKKAT (düşük) — yerel node betikleri ve ffmpeg. Örtüşme: konusmayla-kurgu grubunda cut-silences'ın ikinci adımı (tamamlayıcı); asıl birincil video-use.

### cut-silences  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 65 (B)

- **Ne yapar:** Konuşan kafa kaydından yalnız sessizliği ve boş havayı kırpar: ilk kelimeden önceki ve son kelimeden sonraki boşluk ile eşik üstü (varsayılan 0,55 sn) kelime arası duraklar, doğal nefes payı bırakılarak kısaltılır. Kelime düzeyi transkripti girdi alır; EDL, yeniden zamanlanmış transkript ve (--apply ile) ffmpeg trim+concat çıktısı üretir.
- **Ne zaman:** Kurgu hattının 1. adımı: "cut the silences", "remove dead air", "tighten the pacing" (transkript hazırsa). · **Ne zaman değil:** Kelime düzeyi transkript yoksa (önce transkripsiyon gerekir) ya da yalnız ses seviyesinden sessizlik kırpmak isteniyorsa (auto-editor ya da ffmpeg-skill silence.py daha uygun).
- **Teknoloji:** node, ffmpeg · **Paketler:** node, ffmpeg, kelime düzeyi transkript JSON
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → alternatif · **Roller:** video-kurgu-render
- **Boyut:** 16 KB (SKILL.md 4.7 KB, yük kucuk) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Deterministik, kurallar açık (eşikler, nefes payı kuralları, çıktı dosyaları tabloda). Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Doğrulandı: skill-calistir'in işaret ettiği scripts/validate-beat-sync.mjs ve önkoşuldaki scripts/transcribe-elevenlabs.mjs repo kökündedir, skill klasöründe yok. Transkript için varsayılan sağlayıcı ElevenLabs Scribe: ses dosyası dış servise yüklenir (anahtar ve kota gerekir); yerel Whisper alternatifi anlatılıyor. Ücret: kismen (varsayılan transkriptör ücretli kotalı, ücretsiz yol var; kayıt zaten ucret-siniflandirma.json'da). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — yerel node betiği + ffmpeg. Örtüşme: konusmayla-kurgu grubunda alternatif; yalnız sessizlik için auto-editor-kurgu (auto-editor birincil) ya da ffmpeg-kurgu (ffmpeg-skill silence.py) daha bağımsız.

### day-in-my-life  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 73 (B)

- **Ne yapar:** Ajanın kullanıcısıyla geçirdiği tipik bir oturumu, yerel Claude Code konuşma geçmişinden toplayıp 60-75 saniyelik elle çizilmiş mürekkep filmine çevirir (p5.brush, 8 fps kaynayan çizgi, nota nota bestelenmiş yaylı çalgı müziği). Ekrandaki her satır kullanıcının gerçek sözüdür; render öncesi her satır kullanıcı onayından geçer.
- **Ne zaman:** Claude Code kullanıcısı kendi çalışmasından kişisel bir film istediğinde (en az 10 oturum, 5 gün yerel geçmiş). · **Ne zaman değil:** Başkasının geçmişi, ekip günlükleri, ürün pazarlaması ya da kullanıcının gözden geçirmeyeceği içerik için değil; yerel kayıt yoksa (yalnız claude.ai) durur, söz uydurmaz.
- **Teknoloji:** p5-brush, hyperframes, node, python, ffmpeg · **Paketler:** hyperframes@0.8.70 (npx), p5 2.3.2, p5.brush, puppeteer, numpy, scipy
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** ajan-oturum-filmi → alternatif · **Roller:** video-kompozisyon
- **Boyut:** 196 KB (SKILL.md 6.6 KB, yük kucuk) · **Bağımlılık:** GİZLİLİK: Yerel Claude konuşma geçmişini (~/.claude/projects/*/*.jsonl, memory dosyaları) okur; skill yalnız kullanıcı 'evet' dedikten sonra okuduğunu söyler. HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (niş, dikkatle). Eğlenceli ve özenli (gizlilik kapısı, 'her satır bir makbuz' ilkesi), ama kullanım alanı çok dar ve iş akışı ağır. Güvenlik: DİKKAT (yüksek) — yerel Claude konuşma geçmişini (~/.claude/projects/*/*.jsonl, hafıza dosyaları, ilgili projelerin CLAUDE.md'si) okur; 'evet' denmeden okumaz ve hiçbir şey yüklemez diyor, ama çıktı dosyaları (receipts.json, story.json) kullanıcının gerçek sözlerini taşır, paylaşılmamalı. Ayrıca npm ci / pip install ile bağımlılık indirir (setup.sh elle). Bu skilin kurulumu için kullanıcı onayı şart; ana oturum karar verir. Ücret: ucretsiz (anahtar ve ücretli çağrı yok; Gochi Hand yazı tipi Google Fonts'tan yüklenir). Lisans: Apache-2.0 (p5 LGPL-2.1 bağımlılığı). Örtüşme: ajan-oturum-filmi grubunda session-story ile aynı iş.

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

### duo  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 71 (B)

- **Ne yapar:** İki HTML ekranını, açık katlanabilir telefonu tutan ellerin sabit fotoğraf plakasına (1448x1086, iki boş ekran yuvası) yerleştirir; TikTok vs Reels, ChatGPT vs Claude, önce/sonra gibi yan yana meme ve karşılaştırma videoları için. Telefon ve eller bir fotoğraftır, yeniden çizilmez; ajan yalnız iki ekranın içinde oynayanı yazar ve render eder.
- **Ne zaman:** "Foldable phone meme", "X sol ekranda Y sağ ekranda" gibi iki uygulamayı/akışı/sohbeti aynı anda gösteren kısa video. · **Ne zaman değil:** Tek telefon, dizüstü, kullanıcının getirdiği cihaz çerçevesi ya da başka plaka için değil (geometri yeniden ölçülmeli).
- **Teknoloji:** hyperframes, gsap, node · **Paketler:** hyperframes (npx), node 18+
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** cift-ekran-karsilastirma-videosu → birincil · **Roller:** video-kompozisyon
- **Boyut:** 449 KB (SKILL.md 7.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (niş). İyi tanımlı, tek amaçlı rig; plaka ve geometri piksel ölçülmüş, 'rig'e dokunma' kuralı net. Gereksinimler arasında npx hyperframes@latest (sürüm sabit değil; yeniden üretilebilirlik için sürüm sabitle) ve GSAP'ın jsdelivr'den yüklenmesi var. Ücret: ucretsiz. Lisans: Apache-2.0. Güvenlik: DİKKAT (düşük) — yerel build.mjs, ağ yalnız npm kaydı ve CDN (tam liste yazılmış). Sabit yol: SKILL.md:68'deki ~/.claude/skills/duo örnek metin. Örtüşme: grup yok (tek başına).

### edit-video  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 65 (B)

- **Ne yapar:** Ham konuşan kafa videosunu uçtan uca kurgulayan orkestratör: transkript, sessizlik kırpma, hata incelemesi, görsel hikâye (video-storytelling), hareketli grafik katmanları (hyperframes-video-beats, style-library) ve doğrulanmış HyperFrames render. Proje çıktıları video-projects/<slug>/ altına gider; son teslim: MP4, kurgu kararları, yeniden zamanlanmış transkript ve VERIFY.md.
- **Ne zaman:** "Bu videoyu baştan sona kurgula": tam kurgu hattı istendiğinde (tek bir işlem isteniyorsa doğrudan ilgili skile yönlendirir). · **Ne zaman değil:** Tek bir adım (yalnız sessizlik, yalnız altyazı) ya da konuşan kafa olmayan videolar için; repo kökündeki yönergeler olmadan bu skil tek başına çalışmaz.
- **Teknoloji:** hyperframes, node, ffmpeg, gsap · **Paketler:** hyperframes, ffmpeg, node, kardeş skiller (cut-silences, cut-mistakes, video-storytelling...)
- **Claude / Codex:** tam / tam
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → alternatif · **Roller:** video-kurgu-render, video-kompozisyon
- **Boyut:** 3 KB (SKILL.md 2.6 KB, yük kucuk) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa ve iyi sıralı kontrol listesi; asıl iş kardeş skillere bağlı. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Ayrıca ../hyperframes/SKILL.md, ../cut-silences ve diğer kardeş yollara göreli başvuru yapıyor; yol-tara 'göreli kardeş yolu' UYARISI veriyor (hyperframes kütüphanede başka yerde var; kardeşler aynı projeye birlikte kurulmalı). docs/TOOLS-AND-API-KEYS.md ve MOTION_PHILOSOPHY.md repo kökündedir (arşivde yok). Transkript için varsayılan sağlayıcı ElevenLabs Scribe: ses dosyası dış servise yüklenir (anahtar ve kota gerekir); yerel Whisper alternatifi anlatılıyor. Ücret: kismen (kayıt var). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — betik yok, yönlendirir. Örtüşme: konusmayla-kurgu grubunda alternatif (video-use birincil).

### facebook-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 sau CLI 登录 Facebook 个人主页，立即发布视频或图文，查询原作品、移至垃圾箱或永久删除。
- **Teknoloji:** python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 4 KB (SKILL.md 3.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### ffmpeg  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** FFmpeg ile format dönüştürme, yeniden boyutlandırma, sıkıştırma, ses çıkarma, kırpma ve Remotion'a uygun varlık hazırlama tariflerini toplar. Bayrakların neden kullanıldığını da açıklar.
- **Ne zaman:** Remotion/HyperFrames projesine girecek GIF, video ve ses dosyalarını hazırlarken ya da derin FFmpeg tarifi gerektiğinde. · **Ne zaman değil:** Basit kırp/birleştir/boyutlandır işleri için video-edit daha kısa ve yeterli.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 17 KB (SKILL.md 12.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kapsamlı ve doğru tarifler; Remotion odaklı örnekler ağırlıkta. video-edit ile birlikte kullanılır.

### ffmpeg-skill  ·  kajisho5/ffmpeg-skill @ f1c97cb  ·  puan 94 (A)

- **Ne yapar:** Yerel FFmpeg ile video ve ses düzenleme: kesme, birleştirme, yeniden çerçeveleme, hız, altyazı, bindirme, sessizlik kırpma, senkron, ses yüksekliği, HDR→SDR, platform dışa aktarımı ve denetim. 42 araçlı Python betik seti (probe, check, verify, look, render...), isteğe bağlı MCP sunucusu, '--dry-run --json' ile plan-sonra-çalıştır, lossless-önce ve orijinali koruma kuralları.
- **Ne zaman:** Bir video/ses dosyası (mp4, mov, mp3...) üzerinde ffmpeg işi: kes, birleştir, formatla, altyazı yak, sessizlik/ses düzeyi, platforma hazırla. · **Ne zaman değil:** Yaratıcı kompozisyon/hareket grafiği için değil (HyperFrames/Remotion). Çok ağır bir skil: yalnız ffmpeg işi gerekirse yükle.
- **Teknoloji:** ffmpeg, python · **Paketler:** ffmpeg, ffprobe, python3, isteğe bağlı: ASR/yazı tipi araçları
- **Claude / Codex:** tam / tam
- **Geliştirici:** kajisho5 (kisi, ★7677, son güncelleme 2026-11-16, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → alternatif · **Roller:** video-kurgu-render, ses-tasarimci
- **Boyut:** 2733 KB (SKILL.md 16.9 KB, yük orta) · **Bağımlılık:** ffmpeg/ffprobe ve Python 3 gerekir (scripts/ altındaki betikler); bazı betikler isteğe bağlı olarak ASR/yazı tipi araçları ister.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif, ffmpeg işlerinde birincil adayı). Çok kapsamlı ve disiplinli: önce probe, lossless-önce, --dry-run ile plan, çıktıyı check/verify ile sayılarla doğrulama, orijinali ezmeme, ne sorulur/ne varsayılır kuralları. SKILL.md 16,9 KB (referanslar kademeli yüklenir) ve 61 Python dosyası: bağlam ve inceleme maliyeti yüksek. Yerel çalışır, ağ yok; sudo/apt satırları yalnız eksik ffmpeg için kullanıcıya gösterilen öneri metni. Sabit yol: references/scripts.md:1597'deki ~/.claude/skills/ffmpeg-skill/mcp/server.py kurulumda proje içi yola çevrilir (yol onayı verilmişti). Ücret: ucretsiz. Lisans: MIT. Güvenlik: DİKKAT (orta) — 42 yerel betik ffmpeg alt süreçleri çalıştırır, --overwrite ve 'redact' gibi yazan araçlar var; anahtar/ağ yok. Örtüşme: ffmpeg-kurgu grubunda alternatif (video-edit birincil kalır); sessizlik için silence.py (ses ölçümü tabanlı, transkript gerekmez) cut-silences'ten bağımsızdır.

### figma  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 97 (A)

- **Ne yapar:** Figma içeriğini HyperFrames videosuna getirir: asset (SVG/PNG), marka token'ları, frame'leri düzenlenebilir HTML bileşen olarak, connector ile motion (GSAP'e çevirip doğrulama), shader ve storyboard (frame'ler slayt değil, aynı öğenin durumları).
- **Ne zaman:** Figma linki verildiğinde; marka renkleri/tipografisi, logo, bileşen ya da storyboard'u videoya taşımak. · **Ne zaman değil:** FIGMA_TOKEN yoksa ve kullanıcı oluşturmak istemiyorsa; Figma dışı tasarım kaynakları.
- **Teknoloji:** hyperframes, figma api, gsap · **Paketler:** hyperframes (npx), FIGMA_TOKEN
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 12 KB (SKILL.md 6.2 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede komutlar sadeleşti, storyboard kuralları (frame = keyframe) ve motion doğrulama betiği netleşti. Token sohbete yapıştırılmaz; kullanıcı kendisi ayarlar. · 2026-11-12: yeniden incelendi; eklenen: Windows için exe arama yardımcısı, başlangıç telemetri işareti. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Değerlendirme aynı.

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

### hyperframes  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** HyperFrames'in yeni tek giriş skili: HTML'i kare kare render ederek videoya çeviren sistemin render sözleşmesini (12 kural), düzenlenebilirlik kurallarını, iş döngüsünü (story → SPEC → check → snapshot → review → render) ve video türlerine göre okunacak referansları (launch, explainer, müzik, data, dikey, 3D, karakter, altyazı, overlay, motion) tek yerde toplar.
- **Ne zaman:** HyperFrames ile her türlü video: tanıtım filmi, explainer, müzik videosu, grafik/harita, dikey sosyal klip, altyazı ve overlay; eskiden ayrı iş akışı skilleri olan türlerin hepsi artık buradaki references/types dosyalarıyla yürür. · **Ne zaman değil:** Remotion ya da başka bir çerçeve açıkça istenirse; sadece tarayıcı ekran kaydı gerekiyorsa (playwright-recording).
- **Teknoloji:** hyperframes, html, gsap, node 22+, ffmpeg · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → birincil · **Roller:** video-kompozisyon, video-kurgu-render, motion-graphics-sanatcisi
- **Boyut:** 1135 KB (SKILL.md 7.3 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-10 güncellemesi (heygen-com/hyperframes 6882293): iş akışı skilleri emekliye ayrıldı, içerikleri bu skilin references/types ve references/*.md dosyalarına taşındı; SKILL.md 7 KB'a indi, sözleşme daha net. Önceki iş akışı skillerinin (general-video, faceless-explainer, product-launch-video…) yerine birincil seçim budur. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi. · 2026-11-12 yeniden incelendi (ab66e5b): `init` artık hep `--skip-skills --skill=hyperframes` ile çağrılıyor (agent skill kurmaz/güncellemez; kurulum kullanıcının adımı); yeni skill yönlendirmeleri: /reverse-any-video (bir videoyu kopyala) ve /style-sampling (hazır stilde bölüm); plugin kurulumunda npm ev klasöründen çalışır (projedeki node_modules/.npmrc CLI'yi seçemez); yol-yürütme betikleri Windows exe aramasını kısıtlıyor; 3D için path-tracing referansı eklendi. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Kalite aynı.

### hyperframes-cli  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** HyperFrames CLI'yi işe göre anlatır: init/capture, check (lint/validate/inspect, ses denetimleri dahil), snapshot, timeline düzenleme, preview, yerel render (fps 1-240, bitrate/keyframe ayarı) ve isteğe bağlı bulut/Lambda/Cloud Run render, proje geçmişi ve hata tablosu. Render öncesi doğrulama döngüsünü tanımlar.
- **Ne zaman:** HyperFrames projesini kontrol etme, görsel olarak inceleme, zaman çizelgesi düzenleme ve render alma. · **Ne zaman değil:** Kompozisyonun içeriğine karar verirken tek başına yetmez; hyperframes skiliyle birlikte kullanılır.
- **Teknoloji:** hyperframes, node 22+, ffmpeg, chrome · **Paketler:** hyperframes (npx), node>=22, ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 129 KB (SKILL.md 7.4 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-11: ses (audio_*) lint denetimleri ve yeni render bayrakları eklendi; bulut render ayrı HyperFrames OAuth'una (~/.hyperframes) taşındı, ücretli planda son render için cloud render öneriliyor (yerel render ücretsiz). Telemetri girişten sonra hesaba bağlanır; HYPERFRAMES_NO_TELEMETRY=1 ile kapatılır. Node 22+ ve FFmpeg gerekir. · 2026-11-12 yeniden incelendi (ab66e5b): `init` her zaman `--skip-skills`; `skills` komutu agent'ın değil kullanıcının adımı olarak kaldı; yeni `share` (inceleme paylaşımı: --public yalnızca açık istekle, ücretsiz katmanda 5 proje; legacy `publish` 60 günlük bildirim penceresiyle duruyor); 1440p ön ayarları, --chroma-subsampling 444, 1080p'de her en-boy oranı; `check` lint hatasında bile tarayıcı denetimlerini çalıştırıyor, `npm run` yerine doğrudan `npx hyperframes check`; FFmpeg/FFprobe'u proje klasöründen otomatik bulmuyor (güvenlik: PATH ya da ortam değişkeni). Bulut kimlik sırası: host token > `auth login` oturumu > API anahtarları. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Kalite aynı.

### hyperframes-registry  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 97 (A)

- **Ne yapar:** ~450 hazır HyperFrames bloğu ve bileşenini (geçişler, overlay, başlık, kinetik tipografi, altyazı stilleri, grafik, harita, 3D, kamera hareketi) arama (`catalog --query`) ve projeye düzenlenebilir kaynak olarak kurma (`add`) rehberi.
- **Ne zaman:** Adı olan bir görsel efekti (glitch, film grain, bar chart race, lower third…) elle yazmadan önce; blok/bileşen bağlama. · **Ne zaman değil:** Kayıt defterinde karşılığı olmayan, tamamen özgün sahneler.
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 83 KB (SKILL.md 4.4 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede ~400 → ~450 öğe; yerel arama katmanları (words / on-device) ve 'gap' raporlama eklendi. Arama İngilizce yapılmalı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi. · 2026-11-12 yeniden incelendi; tek değişiklik başlangıç telemetri işareti. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Değerlendirme aynı.

### hyperframes-video-beats  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 64 (C)

- **Ne yapar:** Uzun konuşan kafa HyperFrames videoları için hareketli grafik 'vuruşlarını' planlar, yazar, zamanlar ve doğrular: büyük tez/liste/istatistik anları için tam ekran buruşuk kâğıt kapanışları, destekleyici bilgi için cam efektli alt üçlük kartları. Transkripte dayalı kapsama haritası, vuruş türü karar kuralları ve kısa süre/seyrek renk kuralları içerir.
- **Ne zaman:** Konuşan kafa videosuna görsel vuruş eklerken ya da mevcut vuruş programını iyileştirirken ("lower third", "paper takeover", "add beats"). · **Ne zaman değil:** Videonun kendisinin görsel dünyasını tasarlamak için değil (video-storytelling); boşluk dolduran gereksiz grafikler için değil.
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** hyperframes
- **Claude / Codex:** tam / tam
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusan-kafa-gorsel-katman → alternatif · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İlkeler iyi (her vuruş bir soruya cevap vermeli, boşluk için grafik eklenmez), kurallar somut. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Windows PowerShell/Codex komut ipuçları içerir (Select-String); Claude'a özgü araç varsayımı yok. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: temiz — betik yok. Örtüşme: konusan-kafa-gorsel-katman grubunda alternatif (motion-broll birincil).

### instagram-upload  ·  dreammis/social-auto-upload @ 3847fff  ·  puan 89 (A)

- **Ne yapar:** 使用 sau CLI 在 Instagram 独立网页登录、立即发布 Reels/单图/轮播、核验原作品并移至最近删除。
- **Teknoloji:** git, python _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** dreammis (kisi, ★16118, son güncelleme 2026-10-22, lisans MIT)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 4.0 KB, yük kucuk) · **Bağımlılık:** sau CLI (Python 3 + Playwright; her platform için tarayıcıda bir kez giriş yapılır, oturum çerezi saklanır).
- **İnceleme:** otomatik

### kalem  ·  leodavincs/kalem @ ba19c9f  ·  puan 62 (C)

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

### make-a-video  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 61 (C)

- **Ne yapar:** HyperFrames için yeni başlayana uygun uçtan uca video üretici: iki aşama, sekiz sıralı kapı. 1-4 kapıda amaç, biçim, senaryo/ses, stil ve varlıklar görüşmeyle toplanıp BRIEF.md'ye bağlanır ve onay beklenir; 5-8 kapıda iskele, storyboard, kompozisyon, lint, Studio önizleme, taslak render, görsel doğrulama ve final MP4 gelir.
- **Ne zaman:** "Make a video", "video from scratch": HyperFrames'e yeni olan, konsept/senaryo/ana hatla başlayan kullanıcı. · **Ne zaman değil:** URL'den video (website-to-hyperframes), 9:16 yüz kameralı kısa video (short-form-edit) ya da yalnız çerçeve kuralı (hyperframes) için devretmeli.
- **Teknoloji:** hyperframes, gsap, node, ffmpeg · **Paketler:** hyperframes (npx), ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** hyperframes-cekirdek → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 44 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kapılı, görüşmeli akış iyi (her kapı bir çıktı üretir, onaysız kod yazılmaz), ama bu işi hyperframes + diğer skiller zaten karşılıyor. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Ücret: ucretsiz (TTS yerel hyperframes tts). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — npx hyperframes komutları; betik yok. Örtüşme: hyperframes-cekirdek grubunda tamamlayıcı.

### media-use  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** HyperFrames videosu için medyayı tek komutla (`media-use resolve` / `media-use generate`) bulur ya da üretir: müzik, ses efekti, görsel/ikon/logo, seslendirme, avatar/üretilmiş video, transkript, arka plan silme/cutout, dudak senkronu (lipsync), renk düzeltme; yerleştirilen sesleri miksler. Kaynaklar: ücretsiz (HyperFrames girişi: Voice Turbo Free planda ayda 3 dk, müzik kataloğu, asset arama; Openverse, Whisper), HyperFrames kredisi (üretilmiş görsel/video/avatar, ses klonlama) ve yerel modeller (Kokoro, MusicGen, FLUX, LTX).
- **Ne zaman:** Videoya müzik, SFX, seslendirme (Kokoro TTS dahil), avatar, transkript, renk/LUT, yüz gizleme gibi medya eklemek; eski hyperframes-audio işlerinin yerine. · **Ne zaman değil:** HyperFrames dışı projeler; özel bir sağlayıcı açıkça istenirse o sağlayıcının skili. DİKKAT (2026-11): skill 'ucuz/ücretsiz seçeneğe kendiliğinden geçme, fiyat söyleme' diyor; ücretli çağrıdan önce onay yerine artık `.hyperframes/credit-limit.json` kredi sınırı var. Ücretsiz yol tercih ediliyorsa agent'a yerel/ücretsiz sağlayıcıyı (--local-only) açıkça söyle.
- **Teknoloji:** hyperframes, heygen, ffmpeg, python 3.10+ (kokoro tts) · **Paketler:** node, hyperframes auth login (HyperFrames OAuth), heygen CLI (yardımcı tarifler için), ffmpeg
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-medya → birincil · **Roller:** video-kompozisyon, ses-tasarimci, video-kurgu-render
- **Boyut:** 1900 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 5/5 — 2026-11: giriş 'npx hyperframes auth login' (HyperFrames OAuth); 'media-use generate' ile heygen CLI olmadan üretim eklendi. Kredi harcamada ücretsiz yola geçmeme ve fiyat söylememe yönergesi kullanıcının ücretsiz-önce tercihiyle çelişir. Telemetri girişten sonra HeyGen hesabına bağlanır; HYPERFRAMES_NO_TELEMETRY=1 ile kapatılır. · 2026-11-12 yeniden incelendi (ab66e5b): Voice Turbo artık Free planda ayda 3 dk (ücretli planda sınırsız değil kota), HeyGen giriş oturumu env API anahtarının önüne geçti; kredi sınırı artık `.hyperframes/credit-limit.json` dosyasına yazılıyor ve her ücretli çağrı onu aşmayı reddediyor (--max-credits yalnızca sıkılaştırır); yeni lipsync ve cutout (arka plan silme) türleri, kendi ses kaydını (audio) kullanma, nano-banana-2.1 / gpt-image-2.6 modelleri; Python yardımcıları çalışma klasörünü sys.path'ten çıkarıyor, proje .env yalnızca sağlayıcı anahtarlarını okuyor (HEYGEN_API_BASE vb. yok sayılır: güvenlik sıkılaştırması). Fiyat söylememe / ücretsize kendiliğinden geçmeme yönergesi sürüyor. Telemetri artık skill başlangıç işaretiyle de (`npx hyperframes events --skill=media-use`) gidiyor; kapatma ayarı HYPERFRAMES_CONFIG_DIR'a da uyuyor.

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

### motion-design  ·  lottiefiles/motion-design-skill @ f9a8a04  ·  puan 64 (C)

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

### motion-showreel  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 62 (C)

- **Ne yapar:** 10-30 saniyelik hareket tasarımı showreel'i ya da marka reeli kurar: tek bir marka motifi etiketli zanaat bölümlerinde dönüşür, kalıcı HUD, 120-130 BPM ızgarasına kilitli kesimler, saniyenin altındaki 'flurry' ve açılışa cevap veren logo kilidi. Referans reel'in saniye saniye analizi, bölüm kütüphanesi ve HUD şablonu ile gelir; sfx/müzik/ritim betikleri vardır.
- **Ne zaman:** "Showreel", "sizzle reel", "brand reel", "15 saniyelik markalı film" ya da bir reel'in neden çalıştığını inceleyip başka marka için yeniden kurmak. · **Ne zaman değil:** Düz ürün demosu, anlatımlı video ya da kendi görsel kimliği olmayan işler için değil; ücretli üretim çağrıları (müzik, görsel, video) kullanıcı onayı olmadan yapılmamalı.
- **Teknoloji:** hyperframes, gsap, node, ffmpeg · **Paketler:** hyperframes, ffmpeg, node, isteğe bağlı: KIE_API_KEY, ELEVENLABS_API_KEY
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** kodla-showreel → alternatif · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 58 KB (SKILL.md 10.8 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Tasarım dilbilgisi güçlü (tek motif, ritme kesim, kalıcı HUD), ama yöntem belirli bir referans reel'e bağlı ve ağır. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Frontmatter sorunu: description tırnaksız ve ': ' içeriyor, YAML bozuluyor; kurulumda frontmatter_onar otomatik olarak JSON tırnağına çeviriyor (elle iş yok). Ücret: kismen — sfx.mjs (ElevenLabs) ve kie.mjs (Kie.ai: müzik, görsel, video) ücretli çağrılar yapar, anahtarı ortamdan ya da çalışma alanı .env dosyasından okur; skil 'önce onay iste' diyor, çekirdek iş (kod ve kendi müziğinle) ücretsiz. Güvenlik: DİKKAT (orta) — ücretli API anahtarı okuyan yerel betikler ve dış servise veri gönderen üretim komutları; kullanıcı onayı şart. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Örtüşme: kodla-showreel grubunda alternatif (kinetic-reel birincil).

### moviepy  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 83 (A)

- **Ne yapar:** moviepy 2.x ile Python'da video birleştirme: yapay zekanın ürettiği videonun (LTX-2, SadTalker) üstüne PIL ile çizilmiş, kesin okunur başlık, alt bant ve kaynak yazısı bindirme; 30 saniyenin altındaki reklam benzeri klipleri tek build.py'de kurma; matplotlib grafiklerini mp4'e çevirme. Metin doğruluğu şart olan türlerde (haber, fiyat, kaynak) yapay zekanın kare içi yazı üretmesi yerine bu yolu önerir.
- **Ne zaman:** Videonun üstüne güvenilir (yazım hatası olmayan) metin, etiket, alt bant koymak; Node ve React olmadan kısa tek dosyalık video yapmak; veriyle çizilen grafik videosu. · **Ne zaman değil:** Uzun, çok sahneli, tasarım sistemi gerektiren işlerde Remotion ya da HyperFrames; tam altyazı (SRT) akışında ffmpeg subtitles filtresi. Örnek klasörler (examples/quick-spot, examples/data-viz-chart) toolkit'te olduğundan arşiv kopyasında bulunmaz; desenler kendi kendine yeter.
- **Teknoloji:** python, ffmpeg · **Paketler:** moviepy, Pillow, matplotlib, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → tamamlayıcı · **Roller:** video-kurgu-render
- **Boyut:** 13 KB (SKILL.md 12.8 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 'Güvenilir metin' ilkesi (AI içi yazıyı değil PIL bindirmeyi kullan) pratik ve doğru; kod parçaları toolkit olmadan da çalışır (yalnız pip paketleri gerekir). Lisans MIT. Güvenlik: betik ya da ağdan indirme yok; yalnız uv sync/pip ile bağımlılık kurulumu. Sabit yol yok. Örtüşme: ffmpeg-kurgu grubuna tamamlayıcı; Remotion/HyperFrames ile aynı iş değil (kodla video motoru seçeneği).

### onetake  ·  feitangyuan/onetake @ abb6d17  ·  puan 72 (B)

- **Ne yapar:** Ürün, sayfa, skill ya da özellik için 10–30 saniyelik (anlatımlı demolarda yaklaşık 60 saniye) kesintisiz tanıtım filmi yapar: tek HTML kompozisyon (her değer zamanın saf fonksiyonu), ölçülmüş hareket kütüphanesi (yay, giriş, taşıma, temas, kamera), gerçek arayüzden malzeme, ortak ses paleti ve ritim ile sürekliliği ölçen denetçi. Referans videoyu çözümleyip hissini yakalar; kare kare, hareket bulanıklığıyla render eder.
- **Ne zaman:** Lansman/teaser klibi, anlatımlı özellik demosu; sahnelerin birbirinden doğduğu tek çekim hissi isteniyorsa. · **Ne zaman değil:** DİKKAT: lisans PolyForm Noncommercial 1.0.0, yalnızca ticari olmayan kullanım. Uzun video, konuşan kafa ve mevcut görüntü kurgusu için değil. HyperFrames ya da Remotion açıkça isteniyorsa onlar.
- **Teknoloji:** html, javascript, python, ffmpeg, node · **Paketler:** ffmpeg, node, python3, kokoro-onnx, faster-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** feitangyuan (kisi, ★3959, son güncelleme 2026-11-05, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** urun-tanitim-filmi → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 2715 KB (SKILL.md 23.7 KB, yük orta) · **Bağımlılık:** Lisans PolyForm Noncommercial 1.0.0: yalnızca ticari olmayan kullanım serbest. ffmpeg, node ve Python 3 ister; seslendirme için Kokoro (~/.cache/kokoro/venv altına kurulur) ve faster-whisper.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (urun-tanitim-filmi grubunda birincil). Tek konulu uzman repo; hareket kütüphanesi (lib/motion.js), 12 betik, ritim ve süreklilik ölçümü, 7 referans belgesi. Yerel ve ücretsiz çalışır. Çalıştırma testi yapılmadı. DİKKAT: lisans PolyForm Noncommercial 1.0.0 (yalnızca ticari olmayan kullanım); GitHub lisansı tanımadığı için kayıtta NOASSERTION görünür. Örnek filmler ve GIF'ler (cases/, gallery/, assets/) arşive alınmadı.

### open-edit  ·  veedstudio/open-edit @ e4dc938  ·  puan 73 (B)

- **Ne yapar:** VEED'in barındırılan servisleri ve bir CLI araç takımıyla video işi: kelime zamanlı transkripsiyon, kesme, arka plan silme, AI sunucu, dudak senkronu, herhangi bir fal modeli, ses karışımı ve HTML kompozisyonlarını yalnız değişen kısmı yeniden render eden Chrome render'ı. Ajan parçayı HTML sayfası olarak yazar ve render eder; her parça runs/<anahtar>/ klasöründe durur.
- **Ne zaman:** VEED hesabı/kredisiyle barındırılan transkript, arka plan silme, AI sunucu ya da lipsync gereken video işlerinde; HTML'den artımlı render istendiğinde. · **Ne zaman değil:** Tamamen yerel/ücretsiz hat isteniyorsa (hyperframes, video-use, ffmpeg-skill, auto-editor kullan); VEED/fal hesabı ve kredisi yoksa.
- **Teknoloji:** veed, html-render, chrome, node, fal · **Paketler:** @veedstudio/openedit-cli (npx), VEED girişi ve fal/VEED kredisi, Chrome
- **Claude / Codex:** tam / tam
- **Geliştirici:** veedstudio (kurum, ★1838, son güncelleme 2026-11-11, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → alternatif · **Roller:** video-kurgu-render, ai-medya-uretici
- **Boyut:** 46 KB (SKILL.md 24.1 KB, yük orta) · **Bağımlılık:** VEED barındırılan servisleri (transkript, arka plan silme, AI sunucu, lipsync) ve fal modelleri için VEED/fal kredisi gerekir; CLI araç takımı npx ile indirilir. Chrome render.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (dikkatle). Kurulum akışı temkinli tasarlanmış (init --dry önce, makineyi etkileyen her adım kullanıcıya açık yazılır ve onay beklenir), araç sınırları belgeli. Güvenlik: DİKKAT (yüksek) — npx --yes @veedstudio/openedit-cli çalıştırır (ağdan indirip çalıştırır), 'init --auto-approve' ile kurulum adımlarını uygular (skilin kendisi 'kullanıcı açık evet demeden makineyi etkileyen kurulum yapma' diyor), 'update available' çıkınca 'init --update' önerir; VEED girişi (kimlik) ve barındırılan servislere video/ses yüklenir. Ücret: kismen (kayıt var: VEED/fal kredisi). Lisans: Apache-2.0. Bağlama bağımlı: gövde 24 KB. Örtüşme: konusmayla-kurgu grubunda alternatif (barındırılan-servis tabanlı).

### openmontage  ·  yerel/kendi @ 3c8d08e  ·  puan 73 (B)

- **Ne yapar:** OpenMontage video stüdyosuna giriş skili: video isteğini bilgisayardaki OpenMontage kurulumuna yönlendirir. Önce program kılavuzunu (AGENT_GUIDE.md) okutur, venv python'u ve ffmpeg yolunu içeren komut kalıbını ve ön kontrolü verir, ücretsiz yerel yolu (stok görüntü, Piper Türkçe seslendirme, yerel araçlar) anlatır, bilinen tuzakları ve sabit paket sürümlerini yazar; /backlot, /ink-art, /animated-drawing, /reel isteklerini programın kendi komutlarına yönlendirir.
- **Ne zaman:** Video üretimi, montaj, explainer, seslendirme, altyazı, YouTube indirme/transkript, arka plan silme, upscale gibi işler OpenMontage ile yapılacaksa. · **Ne zaman değil:** OpenMontage kurulu değilse ya da iş HyperFrames/Remotion ile tek başına kurulabilecek kısa bir kompozisyonsa (HyperFrames skilleri yeterli).
- **Teknoloji:** python, ffmpeg, remotion, hyperframes · **Paketler:** OpenMontage kurulumu (~/.openmontage, kendi venv'i), ffmpeg-full (drawtext ve subtitles için), Piper Türkçe modeli (isteğe bağlı)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (commands); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar · Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** kullanıcı (kisi, resmî, ★0, son güncelleme 2026-11-17, lisans Kendi (özel))
- **Durum:** tercih · **Örtüşme:** video-uretim-programi → birincil · **Roller:** video-kurgu-render
- **Boyut:** 11 KB (SKILL.md 11.1 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kullanıcının kendi giriş skili; makineye özgü mutlak yollar içerir (taşınabilir değil, bilerek). Güncelliği OpenMontage kartına bağlıdır (sabit sürümler, yerel yamalar): kart değişince gözden geçirilir. Program lisansı AGPL-3.0; bu skil yalnız giriş notudur.

### oversized-cursor  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 100 (A)

- **Ne yapar:** Lansman videolarında göz taşıyıcı olarak büyük macOS imleci tekniği: boyut/görünüm (marka motifli imleçler dahil), ekran dışından giriş yasası, uç hedefleme ve tıklama vuruşu, tıklamanın bir sonraki vuruşu ateşlemesi ve sahneler arası çıkış/devir.
- **Ne zaman:** UI sahnesinde imleç/işaretçi eylemi olduğunda veya sahne durağan kaldığında ucuz hareket kaynağı olarak. · **Ne zaman değil:** İmleç içermeyen sahneler; gerçek ekran kaydı (playwright-recording).
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** gsap
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-ev-stili → tamamlayıcı · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 6 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. HeyGen iç ev stili (metadata internal:true); kısa, kontrol listeli ve UI demo videolarında yüksek getirili.

### p5-paint-animation  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 81 (A)

- **Ne yapar:** Metin istemini, fotoğrafı ya da kısa video klibi (Live Photo dahil) elle yapılmış gibi görünen p5.js animasyonuna çevirir: kendi kendine yazılan kurşun kalem el yazısı, fırça darbeleriyle yeniden boyanmış fotoğraf (kendini boyayan film, kamera hareketi) ve kare kare yeniden boyanmış canlı resim. %100 kod, p5.brush başsız render, görüntü modeli yok.
- **Ne zaman:** El yapımı görünümlü hareket gerektiğinde: kendini yazan el yazısı, fotoğrafı fırça sanatına çevirme, kısa klibi yaşayan resme çevirme ("painted video", "write-on effect"). · **Ne zaman değil:** Net tipografi/marka yazısı, fotogerçekçi çıktı, ~10 saniyeden uzun görüntü (kare başı 5-20 sn render) ya da canlı/etkileşimli sayfa için değil.
- **Teknoloji:** p5-brush, p5js, node, ffmpeg, puppeteer · **Paketler:** node 22.12+, ffmpeg, puppeteer 25.9.0, p5 2.3.2, p5.brush 2.2.1
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** p5-boyali-animasyon → birincil · **Roller:** motion-graphics-sanatcisi, video-kompozisyon
- **Boyut:** 82 KB (SKILL.md 6.9 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Üç akış (yazı, fotoğraf, video) tek motorla, girdi tablosuyla seçiliyor; 'ne zaman değil' listesi ve başarı doğrulama adımı var, bağımlılıklar kilit dosyasıyla sabit, sketch'lerde ağ ve yerel dosya erişimi engelli. Ücret: ucretsiz. Lisans: Apache-2.0 (p5 LGPL-2.1). Güvenlik: DİKKAT (orta) — setup.sh elle çalıştırılır (npm kaydından sabit sürümler + Google'ın Chrome for Testing'i, ~500 MB), anahtar/ücretli çağrı yok; isteğe bağlı npx hyperframes remove-background. Örtüşme: p5-boyali-animasyon grubunda birincil (genel amaçlı yardımcı), painted-animation hikâye/karakter çizgi filmi için alternatif.

### parody-short  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 75 (B)

- **Ne yapar:** Bir grubun kendi hayatından (ekip lansmanı, çeyrek sonu, taşınma, Noel) ya da herkesin bildiği bir konudan (görüntülü toplantı, ofise dönüş) hicivli kısa video yapma kılavuzu: gerçek yüzlerin canlandırılması, grubun kendi kanallarından iç şakaların toplanması, ödünç alınmış tür (80'ler aksiyon girişi, canavar filmi) eşlemesi, her tür için ayrı görünüm ve ses, kısa tutma kuralları. Yardımcı dosyalar: people.md, context.md, genres.md, formats.md.
- **Ne zaman:** Toolkit kuruluysa bir ekip ya da topluluk için eğlenceli iç video (kişilerin fotoğrafları LTX ile canlandırılır, Remotion'da kurgulanır) ya da uydurma kadrolu halka açık hiciv. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla). Gerçek kişilerin fotoğrafı ve izni olmadan; halka açık yayında her kişinin yazılı izni olmadan; özel mesajlardan alıntı için. Ticari film/dizi karakterleri kullanılamaz (skill de uyarıyor). R2 ayarlı değilse medya halka açık geçici sunuculara (litterbox, 0x0.st) yüklenir: kişisel ya da gizli medyayla R2 olmadan kullanma
- **Teknoloji:** remotion, typescript, node, modal, python, ffmpeg · **Paketler:** claude-code-video-toolkit, Modal hesabı, Hugging Face anahtarı (LTX), ACEMUSIC_API_KEY (ücretsiz)
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** komedi-kisa-video → birincil · **Roller:** ai-medya-uretici, video-kompozisyon
- **Boyut:** 32 KB (SKILL.md 9.9 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (niş, koşullu). Yaratıcı süreç ve güvenlik kuralları ('sevgi çizgidir', halka açıkta yazılı izin, telifli eser yok) düşünülmüş; ama tamamı toolkit bileşenlerine (LivingPhoto, ltx2, acestep, image_edit) bağlı ve ancak belirli bir kullanım durumunda gerekir. Lisans MIT. Güvenlik (dikkat): (1) gerçek kişilerin yüzleri bulut GPU'ya gider ve R2 yoksa halka açık geçici sunuculara yüklenir; (2) grubun kendi sohbet ve belgelerinden şaka toplamayı söyler: gizlilik riski, yalnız herkese açık kanallar (skill de DM'leri hariç tutar); (3) Modal kurulumu ve Hugging Face jetonu isteyen adımlar. Ücret: kismen. Örtüşme: remotion-cercevesi ya da diğer hiciv skillleriyle çakışmaz; kendi grubunun tek üyesi.

### pika-h3-flex  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** Pika H3 Flex ile Pika API üzerinden (`pika_video`) 3-15 sn, senkron sesli video üretir: metinden, ilk/son kareden ya da 9 görsel + 3 video + 3 ses referansından; 480p/768p yerel, 1080p/2k/4k upscale. Prompt yapısı, rewrite kapatma, referans kuralları, fiyat/faturalama ve polling zaman aşımı sonrası devam anlatılır.
- **Ne zaman:** Sesli kısa AI video klibi gerektiğinde ve Pika H3 Flex özellikle isteniyorsa; hızlı taslak (480p) sonra teslim çözünürlüğü. · **Ne zaman değil:** Genel model seçimi (ai-video-gen); Pika hesabı/anahtarı yoksa; ücretsiz yerel yol istenirse (ComfyUI yolu doğrulanmamış).
- **Teknoloji:** pika-api, api-anahtari · **Paketler:** PIKA_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif
- **Boyut:** 7 KB (SKILL.md 6.6 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Ücretli: saniye başı ön ödemeli, kendi Pika kuruluşuna faturalanır (480p $0.01/sn … 4k $0.08/sn; referans modu daha pahalı); başarısız işler ücretlendirilmez; `dry_run` ücretsiz fiyat teklifi verir. Pika'nın tanıtım kotası dışında ücretsiz yol yok. Net prompt yapısı ve referans kuralları; tamamen OpenMontage `pika_video` aracına bağlı.

### playwright-recording  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** Playwright ile tarayıcı etkileşimlerini video olarak kaydeder; form doldurma, gezinti, yavaşlatma ve çözünürlük ayarlarıyla demo ve ürün turu görüntüsü üretir.
- **Ne zaman:** Gerçek bir web uygulamasının demo/walkthrough görüntüsü video kompozisyonuna girecekse. · **Ne zaman değil:** Terminal/CLI demosu (synthetic-screen-recording); masaüstü uygulama kaydı.
- **Teknoloji:** playwright, typescript, node · **Paketler:** playwright, @playwright/test
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → birincil · **Roller:** video-kurgu-render
- **Boyut:** 20 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Genel ve bağımsız çalışan tarifler; Remotion odaklı örnekler.

### prod-by-claude  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 73 (B)

- **Ne yapar:** Bir Strudel (canlı kodlama) parçasının videosunu yapar: kod resmin kendisidir ve her sembol çaldığı notada yanar. Parçayı bestelemek, çevrimdışı kaydetmek ve 1080x1080 videoyu kurmak (yazılan açılış, açılan bölümler, gerçek Strudel tema geçişleri, graffiti ASCII düşüşleri, yazılan imza) akışı içindedir.
- **Ne zaman:** "Strudel video", "live coding video", "prod by claude": Strudel kodunun çalışmasını gösteren video ya da ajanın bestelediği parçanın videosu. · **Ne zaman değil:** Başka ses/DAW projeleri, konuşan kafa videoları ve Strudel kodu olmayan ses görselleştirmeleri için değil (HyperFrames müzik akışı kullanılır).
- **Teknoloji:** strudel, hyperframes, node, puppeteer, ffmpeg · **Paketler:** hyperframes@0.8.70 (npx), @strudel/web 1.3.0, puppeteer-core, Chrome for Testing 149
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** strudel-canli-kod-videosu → birincil · **Roller:** video-kompozisyon, ses-tasarimci
- **Boyut:** 90 KB (SKILL.md 5.2 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (niş). Tek amaçlı, iyi belgelenmiş (sürümler sabit, kayıt süresi ve sorun giderme yazılı). Yukarı akım notu: skill-calistir'in 'assets/bgm.wav yok' uyarısı yanlış alarm: dosya skilin kendi record.mjs betiğinin ürettiği çıktıdır, paketli olması beklenmez. Ücret: ucretsiz. Lisans: Apache-2.0; Strudel AGPL-3.0 (npm'den kurulur, pakete gömülü değil). Güvenlik: DİKKAT (orta) — npm install, Chrome for Testing indirme (npx @puppeteer/browsers), 5-7 dk'lık yerel kayıt; anahtar yok. Örtüşme: grup yok.

### provider-refresh-oct23  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** 23 Ekim 2026 sağlayıcı yenilemesi için API sözleşmeleri ve yönlendirme: Gemini Omni 1.1 Flash, Veo (Vertex), Nano Banana 2.1, ElevenLabs v4/Turbo, HeyGen TTS/katalog/ses dönüştürme, Grok/Mistral/MAI TTS, Voxtral STT, ElevenLabs soundtrack ve yeni görsel/video modelleri (FLUX 3, Vidu Q4, Fibo2, MAI Image 2.6, Grok Imagine 1.5); ana kural: araç, host, tam model ve fiyat duyurulur, otomatik host/model geçişi yok.
- **Ne zaman:** OpenMontage'ın Ekim 2026 adaptörleriyle belirli bir sağlayıcı/model zorunlu tutularak üretim yapılacaksa; model sözleşmesi ve geçiş notları için. · **Ne zaman değil:** OpenMontage dışında; genel model seçimi için ai-video-gen; Eylül yenilemesi için provider-model-refresh.
- **Teknoloji:** api-anahtari, openmontage · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-saglayici-yonlendirme → tamamlayıcı
- **Boyut:** 8 KB (SKILL.md 8.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Güncel ve katı sözleşme listesi; yeni fiyatların çoğu taze hesap teklifi ister, süresi dolmuş promosyonlar kalıcı fiyat sayılmaz. HeyGen ücretsiz Turbo erişimi 30 Kasım 2026'da bitiyor ve hata durumunda ücretliye geçilmiyor. Tamamen OpenMontage araç kayıtlarına bağlı; çoğu yol ücretli API.

### rea-video  ·  JuneYaooo/rea-video @ 6461571  ·  puan 77 (B)

- **Ne yapar:** Bir videonun nasıl yapıldığını tersine mühendislikle çözer: her çekimin altındaki görüntünün kaynağı (gerçek çekim, film klibi, AI video, dijital insan, 3B render, 2D/stop-motion animasyon, kod şablonu, ekran kaydı...), üstündeki kurgu paketi (altyazı, çıkartma, şablon), kullanıcının gerçek malzemesi, ses kaynağı (TTS/BGM/efekt) ve gerçek çekimde ışık/kamera. rea-video CLI'ı VIDEO.md, rapor, storyboard ve çekim kırpıntıları üretir; yeniden yapım (remake) rotası verir.
- **Ne zaman:** Bir referans videonun nasıl çekildiğini/üretildiğini çözmek, aynısını ya da benzerini yeniden yapmak için çekim çekim plan almak. · **Ne zaman değil:** Sıfırdan video üretimi için değil; rea_video Python paketi (pip) kurulu değilse çalışmaz. Gövde Çince yazılmış (araçlar ve çıktılar İngilizce/Çince seçilebilir).
- **Teknoloji:** python, ffmpeg, vlm, ocr · **Paketler:** rea-video[ocr] (pip, git+https), ffmpeg, Python 3.10+, isteğe bağlı: görsel model (VLM) anahtarı
- **Claude / Codex:** tam / tam
- **Geliştirici:** JuneYaooo (kisi, ★10200, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → alternatif · **Roller:** ai-medya-uretici, planlayici
- **Boyut:** 81 KB (SKILL.md 19.7 KB, yük orta) · **Bağımlılık:** Repo kökündeki rea_video Python paketi gerekir (pip install); ilk çalışmada model indirir (ağ, disk).
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (dikkatle). Yöntem güçlü ve dürüst ('her sonuç kanıtlı, emin değilsen 'onay bekliyor' yaz', VLM işlemiyorsa raporda açıkça yaz), kademeli token okuma. Gövde ve çoğu referans Çince; Türkçe özet bu yüzden gereklidir. Yukarı akım eksiği: skil klasörü yalnız SKILL.md ve 12 kadar referanstır; çalışması için gereken rea_video Python paketi repo kökündedir (pip install ile kurulur), arşivde yok. Güvenlik: DİKKAT (yüksek) — references/setup.md `pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video"` ile ağdan paket kurdurur ve 'bash scripts/install_skill.sh' önerir (CLI kurar ve skili 'her ajan klasörüne bağlar', yani genel skill klasörlerine yazar; bu kütüphanede asla kullanılmamalı); references/chatcut.md macOS için `curl -fsSL https://chatcut.io/install.sh | sh` ve Windows için `irm ... | iex` ile üçüncü taraf masaüstü uygulaması kurdurur ve hesap girişi ister; VLM için REA_VLM_API_KEY/BASE_URL ortam değişkenleri. Ücret: kismen — çekirdek ücretsiz; ChatCut üyeliği/kredisi ve VLM API'si isteğe bağlı ücretli (kayıt güncellendi). Lisans: Apache-2.0. Örtüşme: video-analiz grubunda alternatif (video-understand birincil, kalan: üretim yöntemi çözme).

### referans  ·  leodavincs/kalem @ ba19c9f  ·  puan 70 (B)

- **Ne yapar:** Beğenilen bir referans videoyu sahnelere böler, her sahneden kare çıkarır ve kareleri inceleyip sahne başına İngilizce video istemi (prompt) yazar. Çıktı: istemler.md ve kopyala düğmeli istemler.html. Videoyu üretmez, yalnız istem çıkarır.
- **Ne zaman:** Elindeki bir videonun tarzını kendi video aracında (Veo, Kling, Seedance…) yeniden üretmek için sahne sahne istem istediğinde. · **Ne zaman değil:** DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür. Video sitesinden indirme yapmaz; dosya elinde olmalı (indirme için video-download). İstemleri çalıştırmak için ai-video-gen skilleri.
- **Teknoloji:** python, ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** leodavincs (kisi, ★106, son güncelleme 2026-11-06, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** referans-videodan-istem → birincil
- **Boyut:** 4 KB (SKILL.md 4.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (referans-videodan-istem grubunda birincil, tek üye). MIT. Ücretsiz, çevrimdışı; karelerdeki yazıyı veri sayar (prompt enjeksiyonuna karşı açık kural). DİKKAT: skill repo kökünden çalışır (kurulum.sh, motorlar/, birlestir.py, projeler/<ad>/). Kütüphaneden tek başına projeye kurulunca bu yollar bulunmaz; kullanmak için repoyu klonlayıp içinde `claude` açmak gerekir. Lisans: repoda MIT LICENSE var, GitHub otomatik tanımadığı için kayıtta NOASSERTION görünür.

### remotion  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 76 (B)

- **Ne yapar:** Toolkit'e özgü Remotion desenleri: paylaşılan bileşenler (AnimatedBackground, SlideTransition, Label, Vignette, SplitScreen, NarratorPiP...), lib/transitions içindeki özel geçişler (glitch, rgbSplit, lightLeak, clockWipe...), proje kuralları ve ayrı bir hareket kılavuzu (motion-craft.md: süre, yavaşlama eğrisi, yay, okuma süresi, ritim ızgarası). Çekirdek Remotion bilgisi için remotion-official skiline gönderir.
- **Ne zaman:** Toolkit şablonlarında (lib/components, lib/transitions) Remotion videosu yazarken; hareket sürelerini ve yavaşlama eğrisini seçerken (motion-craft.md bağımsız okunabilir). · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) (bileşen ve geçiş içe aktarmaları ../../../../lib/ yollarına bağlı). Çekirdek Remotion API'si için remotion-best-practices; HyperFrames projesinde kullanma. Toolkit'siz Remotion projesinde yalnız motion-craft.md kısmı işe yarar.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions, claude-code-video-toolkit (lib/)
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 26 KB (SKILL.md 6.4 KB, yük kucuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (tamamlayıcı). Kısa (6 KB) ve odaklı; en değerli parçası motion-craft.md (bağımsız hareket ilkeleri, HyperFrames kılavuzlarından uyarlama). Bileşen ve geçiş yolları toolkit'e bağlı, skill çekirdek bilgiyi remotion-official skilline bırakıyor (o skill bu yan klasörde yok; kütüphanede karşılığı remotion-best-practices). yol_bagimliligi: true çünkü metin .claude/skills/remotion yollarına atıf yapıyor; yol-tara sabit kullanıcı yolu bulmadı (0 bulgu). Lisans MIT; Remotion'un kendisi şirketler için ticari lisans isteyebilir (ücret: kismen). Güvenlik: betik ya da ağ adımı yok, temiz. Örtüşme: remotion-cercevesi grubunda remotion-best-practices'in üstüne tamamlayıcı; OpenMontage remotion@openmontageinc alternatif.

### remotion-best-practices  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Entry point and router for Remotion (React video framework) work: points to the right sub-guide for creating a video or project, React markup, animations, captions, maps, multimedia, interactivity, rendering, Studio preview, SaaS apps, docs search, licensing and upgrades. Use whenever the user works on a Remotion project or wants to make videos programmatically with React.
- **Teknoloji:** node, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 6 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-best-practices@calesthio  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** Remotion (React ile video) için resmi en iyi uygulamalar: animasyon, kompozisyon, ses, altyazı, FFmpeg, 3D, grafik, font ve Mediabunny ile medya ölçümü gibi konulara ayrılmış kural dosyaları.
- **Ne zaman:** Remotion kodu yazılan veya düzenlenen her projede. · **Ne zaman değil:** HyperFrames ile yazılan videolarda; Remotion'dan HyperFrames'e taşıma için remotion-to-hyperframes.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/cli
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** remotion-cercevesi → birincil · **Roller:** video-kompozisyon
- **Boyut:** 112 KB (SKILL.md 4.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır. · **Kırık bağlantı:** 1
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Remotion ekibinin resmi kural seti, kaliteli. Varsayılan çerçeve HyperFrames olduğu için alternatif; Remotion projelerinde birincil. · 2026-11-12 yeniden incelendi: içerik değişmedi (kaynak OpenMontageInc/OpenMontage fecb9a1'e taşındı), değerlendirme aynı.

### remotion-captions  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 92 (A)

- **Ne yapar:** Transcribing, displaying and animating captions
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 16 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-create  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Scaffold a new Remotion project and build a new video composition (create-video, layout, Tailwind). Use when the user asks to make, create or build a new video or composition with Remotion, or no Remotion project exists yet.
- **Teknoloji:** git, node, react, remotion, tailwind _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 2.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-docs  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Search and read current Remotion documentation via its docs search API. Use when you need up-to-date Remotion API details, props or examples instead of relying on memory.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.3 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-interactivity  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Structure Remotion markup for interactivity
- **Teknoloji:** css, html, react, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 13.5 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-license  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 92 (A)

- **Ne yapar:** Find Remotion license information, FAQs, terms, and where to buy a license.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 0.5 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-maps  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Animated maps in Remotion videos: static satellite maps, Mapbox, MapLibre, MapTiler, GeoJSON routes and markers, and 3D geographic flyovers. Use when a Remotion video needs a map, animated route, location explainer or globe.
- **Teknoloji:** api-anahtari, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 477 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-markup  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Content, animation and effects best practices
- **Teknoloji:** canvas, css, ffmpeg, html, lottie, node, react, remotion, tailwind, three.js _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 123 KB (SKILL.md 13.2 KB, yük orta) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-multimedia  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Read and process audio/video files in the browser with Mediabunny for Remotion: get audio or video duration and dimensions, trim, crop and inspect metadata. Use when a Remotion composition needs media durations, sizes or browser-side media processing.
- **Teknoloji:** remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 7 KB (SKILL.md 0.7 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-render  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Render and export Remotion videos and stills: npx remotion render/still, codecs, transparent videos and render flags. Use when the user wants to export, render or download an MP4/WebM/GIF/PNG from a Remotion project.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 5 KB (SKILL.md 1.1 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-saas  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Build an app on top of Remotion: SaaS templates and frameworks, embedding @remotion/player in React (or Vue, Angular, Svelte), and client- vs server-side rendering (Lambda, Vercel, Node.js, Cloudflare). Use when making a video-generation product, editor or form-to-video app with Remotion.
- **Teknoloji:** node, react, remotion, svelte, vue _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 8 KB (SKILL.md 1.0 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-studio  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Start and use Remotion Studio to preview a video while building it (npx remotion studio, --no-open with an in-app browser, useful flags). Use when creating or editing a Remotion video and the user should see a live preview.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion-to-hyperframes  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 97 (A)

- **Ne yapar:** Başka araçlarla yapılmış video kodunu ya da çıktısını HyperFrames'e alır ve kare kare karşılaştırarak doğrular: Native (Remotion/HTML/GSAP çevirisi), Hosted (canvas, p5, Three.js, Lottie kodunu HyperFrames zamanıyla sürme), Media (Manim, After Effects, Blender çıktısını klip olarak koyma).
- **Ne zaman:** Remotion projesini taşımak; Lottie/Three.js/p5 animasyonlarını ya da Manim/AE renderlarını HyperFrames videosunda kullanmak. · **Ne zaman değil:** Sıfırdan yeni video (hyperframes yeter).
- **Teknoloji:** hyperframes, remotion, react, python · **Paketler:** hyperframes (npx), remotion
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** hyperframes-iceri-aktarma → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 164 KB (SKILL.md 5.1 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — 2026-11: SSIM karşılaştırması betikler yerine `npx hyperframes diff` komutuna taşındı (render_diff.sh/frame_strip.sh kaldırıldı); box-sizing kuralı ve lottie/timing notları eklendi. Üç seviyeli model (Native/Hosted/Media) korunuyor. · 2026-11-12 yeniden incelendi; tek değişiklik başlangıç telemetri işareti. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Değerlendirme aynı.

### remotion-upgrade  ·  remotion-dev/remotion @ 1e55bdc  ·  puan 90 (A)

- **Ne yapar:** Upgrade Remotion and all @remotion/* packages to the same latest version, align auxiliary dependencies and update installed Remotion skills. Use when the user asks to upgrade or update Remotion, or Remotion package versions are mismatched.
- **Teknoloji:** node, remotion _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** remotion-dev (kurum, resmî, ★70754, son güncelleme 2026-11-04, lisans NOASSERTION)
- **Durum:** tercih
- **Boyut:** 3 KB (SKILL.md 1.9 KB, yük kucuk) · **Bağımlılık:** Remotion (npx create-video / remotion paketleri). Şirketler için Remotion lisansı gerekebilir.
- **İnceleme:** otomatik

### remotion@openmontageinc  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 78 (B)

- **Ne yapar:** claude-code-video-toolkit'e özgü Remotion uzantıları: paylaşılan bileşenler (AnimatedBackground, SlideTransition…) ve özel geçişler (glitch, lightLeak, clockWipe). Temel Remotion bilgisi için 'remotion-official' skill'ine yönlendirir.
- **Ne zaman:** Sadece o toolkit'in lib/components ve lib/transitions klasörleri bulunan bir projede. · **Ne zaman değil:** Genel Remotion işleri (remotion-best-practices); OpenMontage kurulumunda lib/ klasörleri yok.
- **Teknoloji:** remotion, react, typescript · **Paketler:** remotion, @remotion/transitions
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** remotion-cercevesi → alternatif
- **Boyut:** 16 KB (SKILL.md 6.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu lib/components, lib/transitions ve remotion-official bu kurulumda/arşivde yok; tek başına çalışmaz.

### session-story  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 73 (B)

- **Ne yapar:** Ajanın kullanıcısıyla geçirdiği tipik bir oturumu, kullanıcının gerçek mesajlarıyla 40-70 saniyelik animasyon filmine çevirir: ajan bir masada oturur, oda kullanıcıya göre döşenir, istekler kâğıt uçak olarak gelir, düzeltmeler 3B çekiç olur, övgü kelebek olur; ajan kendi orkestra müziğini film saatine göre besteler. p5.brush suluboya, HyperFrames ile render.
- **Ne zaman:** Kullanıcı ajanından birlikte çalışmalarının filmini istediğinde ("a video of our session", "session story") ve ajanın gerçek geçmişi varsa (yerel kayıt ya da yapıştırılan mesajlar). · **Ne zaman değil:** Başkasının geçmişi, ekip günlükleri, uydurma alıntılı pazarlama ya da kullanıcının gözden geçirmeyeceği içerik için; geçmiş yoksa kullanıcıdan mesaj ister, alıntı uydurmaz.
- **Teknoloji:** p5-brush, hyperframes, node, python, ffmpeg, swift · **Paketler:** hyperframes@0.8.71 (npx), p5 2.3.3, p5.brush 2.2.3, swift (macOS) ya da fluidsynth
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** ajan-oturum-filmi → birincil · **Roller:** video-kompozisyon
- **Boyut:** 294 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** GİZLİLİK: Yerel Claude konuşma geçmişini (~/.claude/projects/*/*.jsonl, memory dosyaları) okur; skill yalnız kullanıcı 'evet' dedikten sonra okuduğunu söyler. HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF (niş, dikkatle). Yaratıcı ve titiz (her satır alıntı, kullanıcı her satırı onaylar), ama ağır ve dar. Güvenlik: DİKKAT (yüksek) — ajanın kendi konuşma kayıtlarını okur (~/.claude/projects/<proje>/*.jsonl, ~/.codex/sessions, hafıza ve talimat dosyaları); skill 'kullanıcı evet dedikten sonra' diyor, --all-projects ile tüm projeler taranabilir. GEMINI_API_KEY ortamda varsa 'snapshot' komutu kareleri (kullanıcının sözlerini) Gemini'ye gönderir: her snapshot'a --describe false verilmeli. Çıktılar (session-story-candidates.json) kullanıcının sözlerini taşır, paylaşılmamalı. setup.sh npm ci çalıştırır. Ücret: kismen (Gemini isteğe bağlı; yerel çalışır). Lisans: Apache-2.0. Örtüşme: ajan-oturum-filmi grubunda birincil (Codex geçmişini de kapsar, her rutin türü), day-in-my-life alternatif.

### short-form-edit  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 64 (C)

- **Ne yapar:** Konuşan kafa görüntüsünü bitmiş bir reel, YouTube Short ya da kısa reklama dönüştürür: merak uyandıran açılış, hak edilmiş sonuç, hikâyeye dayalı kesim, transkripte kilitli hareketli grafik, hareketli B-roll, altyazı ve ince müzik. Varsayılan 1080x1920, istenirse ayrı çerçeveli 1920x1080; kayıtlı kurgu planı ve doğrulama betikleriyle.
- **Ne zaman:** Konuşan kafa kaydından dikey kısa video ya da reklam; referans reel verildiyse onun ritmi. · **Ne zaman değil:** Uzun biçimli videolar (video-storytelling), 'viral olur' garantisi isteyen işler (düzenleme bunu garanti edemez) ya da bu hattın bağımlılıkları olmayan ortamlar için değil.
- **Teknoloji:** hyperframes, node, ffmpeg, gsap · **Paketler:** hyperframes, ffmpeg, node
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** dikey-kisa-video → birincil · **Roller:** video-kurgu-render, video-kompozisyon
- **Boyut:** 45 KB (SKILL.md 21.2 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İlk 3 saniye ilkesi ve doğrulama kapıları iyi; ama büyük (21 KB) ve yazarın kişisel kurgu rehberine (docs/EDITING-PLAYBOOK.md) bağlı. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. skill-calistir'in 'assets/*.json yok' uyarısı yanlış alarm: plan.json, transcript.json, edit-decisions.json ve footage-ledger.json çalışma anında video-projects/<slug>/ altında üretilen proje dosyalarıdır (references/plan-schema.md bunları tarif eder); eksik olan gerçek yukarı akım dosyalar docs/EDITING-PLAYBOOK.md ve docs/TOOLS-AND-API-KEYS.md'dir. Transkript için varsayılan sağlayıcı ElevenLabs Scribe: ses dosyası dış servise yüklenir (anahtar ve kota gerekir); yerel Whisper alternatifi anlatılıyor. Üretilmiş ek görüntü için ücretli servis (Kie vb.) ayrıca belirtilmiş. Ücret: kismen (kayıt var). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — yerel doğrulama betikleri (validate-plan, validate-footage). Örtüşme: dikey-kisa-video grubunda birincil.

### short-form-video  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 56 (C)

- **Ne yapar:** Eski 'May Shorts' öğretim kompozisyonlarının bakımı için eski kalıp: yüz modu, sahne bindirmeleri ve karaoke altyazı (1080x1920, 10-30 sn); ses önce kesilir, kompozisyon iskelesi dört katmanlıdır (arka plan, dikiş, altyazı, yüz). Yeni reeller için değil, short-form-edit kullanılmalı.
- **Ne zaman:** Yalnız o örneklerin bakımı ya da bu eski dört katmanlı iskeleyi bilerek istemek. · **Ne zaman değil:** Yeni reel/Short kurgusu için (short-form-edit kullan). Önce /hyperframes çağrılmalı.
- **Teknoloji:** hyperframes, gsap · **Paketler:** hyperframes
- **Claude / Codex:** tam / tam
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** dikey-kisa-video → alternatif · **Roller:** video-kompozisyon
- **Boyut:** 20 KB (SKILL.md 19.8 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Kendini 'legacy' ilan ediyor (yeni işler için short-form-edit). Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Doğrulandı: SKILL.md'nin işaret ettiği scripts/transcribe-elevenlabs.mjs repo kökünde, references/captions.md ise skil klasöründe değil kütüphanedeki hyperframes skilinin references/captions.md dosyasıdır (orada var). Transkript için varsayılan sağlayıcı ElevenLabs Scribe: ses dosyası dış servise yüklenir (anahtar ve kota gerekir); yerel Whisper alternatifi anlatılıyor. Ücret: kismen (kayıt var). Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — transkript için kök betik ses dosyasını ElevenLabs'e yükler (kullanıcı seçimine bağlı); skilin kendisinde betik yok. Örtüşme: dikey-kisa-video grubunda alternatif (eski).

### slideshow  ·  heygen-com/hyperframes @ ab66e5b  ·  puan 97 (A)

- **Ne yapar:** HyperFrames ile canlı sunulan slayt gösterisi kurar: her slayt bir sahne, JSON adası ile fragment reveal, dallanan hotspot'lar ve konuşmacı notları; `hyperframes present` ile sunulur; var olan bir sayfayı desteye çevirme kuralları içerir.
- **Ne zaman:** MP4 yerine canlı sunulacak deste/pitch deck; mevcut bir web sayfasını sunuma çevirmek. · **Ne zaman değil:** Render edilmiş video isteniyorsa (hyperframes); PowerPoint dosyası gerekiyorsa (pptx).
- **Teknoloji:** hyperframes, html, gsap · **Paketler:** hyperframes (npx)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** heygen-com (kurum, resmî, ★82940, son güncelleme 2026-11-12, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** sunum-desteleri → tamamlayıcı · **Roller:** video-kompozisyon
- **Boyut:** 48 KB (SKILL.md 5.0 KB, yük kucuk) · **Bağımlılık:** HyperFrames CLI gerekir (npx hyperframes). Video iş akışı skilleri (/general-video, /faceless-explainer, /product-launch-video, /pr-to-video, /embedded-captions, /talking-head-recut) hyperframes çekirdek skillerine dayanır.
- **İnceleme:** incelendi · kalite 4/5 — Güncellemede SKILL.md 497 satırdan ~45 satıra indi; kurallar özlü. ttsScript alanları henüz bağlı değil. · 2026-11-12: yeniden incelendi; tek değişiklik başlangıç telemetri işareti. Yeni (2026-11-12 güncellemesi): skill başlarken `npx hyperframes events --skill=<ad>` çalıştırıp skill adını CLI telemetrisiyle gönderiyor (giriş yapılmışsa hesaba bağlı; HYPERFRAMES_NO_TELEMETRY=1 / DO_NOT_TRACK ile kapanır). Değerlendirme aynı.

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

### style-library  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 57 (C)

- **Ne yapar:** Projenin yeniden kullanılabilir hareket grafiği kart kütüphanesini ve stil şablonlarını seçmek, özelleştirmek ya da genişletmek için kısa bir yönlendirme: GUIDE.md ve registry.json'u okuyup stile/seviyeye/amaca göre süzer, seçilen kartı kompozisyona kopyalar ve yerelleştirir, slot değerlerini doldurur. Yeni stil için new-style.mjs ve build-registry.mjs betiklerini işaret eder.
- **Ne zaman:** Bir videoya hazır kart/stil seçerken ya da yeni stil paketi eklerken (yalnız stil kütüphanesi de yanında kuruluysa). · **Ne zaman değil:** Kütüphane içeriği olmadan: bu kopyada kartlar, GUIDE.md ve registry.json yok, skil tek başına işe yaramaz.
- **Teknoloji:** hyperframes, gsap, css · **Paketler:** herk-edit-kit repo kökündeki style-library/ ve style-templates/ dizinleri
- **Claude / Codex:** tam / tam
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusan-kafa-gorsel-katman → alternatif · **Roller:** motion-graphics-sanatcisi
- **Boyut:** 2 KB (SKILL.md 1.6 KB, yük kucuk) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. 1,6 KB'lık yönlendirme dosyası; asıl değer repo kökündeki style-library/ (kartlar, registry.json, GUIDE.md) ve style-templates/ dizinlerinde, bunlar arşive alınmadığı için skil boş bir kabuk. Doğrulandı: skill-calistir'in işaret ettiği assets/source.mp4 kullanıcının kendi videosudur (şablon README'sinde isteniyor), eksik paket dosyası değil; gerçek yukarı akım eksiği kart kütüphanesinin kendisi. Katalog taslak içerik olduğunu (her kartın render kalite denetiminden geçmediğini) kendisi söylüyor. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: temiz — betik yok. Örtüşme: konusan-kafa-gorsel-katman grubunda alternatif (kütüphane içeriği ayrıca alınırsa değerlendirilir).

### swiss-user-research-video-template  ·  nexu-io/open-design @ 987b247  ·  puan 97 (A)

- **Ne yapar:** Swiss-style user-research narrative template in warm-paper editorial aesthetics. Use when users ask for a premium research deck or story-first live artifact with minimalist typography, high-clarity layout, subtle motion, donut breakdowns, and keyboard/click navigation across slides in a single HTML file.
- **Teknoloji:** api-anahtari, css, html _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105947, son güncelleme 2026-11-04, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 23 KB (SKILL.md 2.7 KB, yük kucuk)
- **İnceleme:** otomatik

### synthetic-screen-recording  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 85 (A)

- **Ne yapar:** Terminal/CLI demosunu gerçek ekran kaydı yerine Remotion'daki TerminalScene bileşeniyle sentetik olarak üretir; komut ve çıktıyı karakter karakter, kareye kadar kontrollü yazar. Ne zaman sentetik, ne zaman canlı kayıt seçileceğini açıklar.
- **Ne zaman:** Kurulum/CLI eğitimi gibi komut ve çıktısı önceden bilinen terminal demolarında. · **Ne zaman değil:** Gerçek uygulama arayüzü veya tarayıcı akışı (playwright-recording); OpenMontage remotion-composer'ı yoksa.
- **Teknoloji:** remotion, react, typescript · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-kurgu-render
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Fikir iyi; ancak OpenMontage'ın remotion-composer/TerminalScene bileşenine bağımlı.

### synthetic-ui-demo  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 83 (A)

- **Ne yapar:** Ekran kaydı olmadan ürün tanıtım ve sürüm notu videosu: uygulamanın kaynak kodundan yalnızca sahnede görünen ekranlar statik React olarak yeniden kurulur, Remotion'da senaryolu imleç ve kamera (Stage + Cursor bileşenleri) bunları oynatır. Her tıklama bir kare numarasıdır, bu yüzden sahne her seferinde aynı çıkar ve ürün değişince kodu düzenleyerek güncellenir.
- **Ne zaman:** Ürünün kaynağını okuyabildiğin, her sürümde yeniden yapılan sürüm notu / özellik turu videoları; canlı ortam ya da test verisi olmadan akış göstermek. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla). Yalnızca çalışan uygulaman varsa (kaynak yoksa) playwright-recording; tek seferlik gerçek veri yakalama; karmaşık uzun etkileşimler. Yapay zeka ile üretilen kişileri gösteren sahnelerde 'yapay zeka üretimi' notu koymayı unutma.
- **Teknoloji:** remotion, react, typescript, node · **Paketler:** claude-code-video-toolkit (Stage, Cursor), Node, Remotion
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ekran-kaydi-demo → alternatif · **Roller:** video-kompozisyon
- **Boyut:** 10 KB (SKILL.md 10.4 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Tekrar edilebilir, deterministik demo fikri güçlü ve ayrıntılı anlatılmış (kare numaralı zaman çizelgesi, kamera, ses senkronu); ama toolkit'teki Stage/Cursor bileşenlerine ve örnek yapılara (examples/ds-*) dayanır, kendi başına çalışmaz. Lisans MIT; Remotion şirketler için ticari lisans isteyebilir; anlatıcı sesi ve konuşan kafa isteğe bağlı bulut GPU ya da ElevenLabs ister (ücret: kismen). Güvenlik: betik ya da veri gönderen adım yok; ürün deposunu okuduğu için gizli kod yapıştırmamaya dikkat. Sabit yol yok (yol-tara 0 bulgu, ../ yolları toolkit içi). Örtüşme: ekran-kaydi-demo grubunda playwright-recording birincil; synthetic-screen-recording (terminal odaklı) ile benzer fikir, bu daha geniş (tarayıcı arayüzü).

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

### video-design  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 83 (A)

- **Ne yapar:** Videoya özgü görsel tasarım kuralları: renk perde (act) başına değişir, sahne başına değil; yazı ölçeği (5 boyut), tek veri vurgusu, 16:9 ve 9:16 yerleşimi, 'konudan çizilen zemin', design.md devir sözleşmesi ve çıktının temas şeridiyle (contact sheet) jüri gibi eleştirisi. Tasarım kaynağı (taste-skill, frontend-design) isteğe bağlıdır; varsayılan kendi paletleridir.
- **Ne zaman:** Video sahnelerinin, başlık kartlarının, veri sahnelerinin ve paletin tasarlanması ya da 'yapay zeka yapmış gibi' görünen bir videonun düzeltilmesi; render sonrası eleştiri. · **Ne zaman değil:** Web sayfası tasarımı için (scroll, hover yok) ui-ux skilleri; HyperFrames için hyperframes ev stili kılavuzları (motion-doctrine). qc.py --layout ve contact_sheet.py gibi toolkit araçlarına atıf yapar, onlar yoksa eleştiri adımı elle yapılır.
- **Teknoloji:** remotion, typescript · **Paketler:** (yalnız kural; ek paket yok), isteğe bağlı: taste-skill
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** video-tasarim-kurallari → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 25 KB (SKILL.md 8.7 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Videoyu izleme biçiminden çıkan somut, ölçülebilir kurallar (parlaklık farkı, iki satır başlık, tek vurgu) ve eleştiri ölçeği değerli; araçtan bağımsız okunabilir (5 dosya, 9 KB SKILL). Lisans MIT; palet ve eleştirinin bir kısmı taste-skill'den (Leonxlnx, MIT) uyarlanmış ve atıfı var. Güvenlik: betik ya da ağ adımı yok, temiz. Sabit yol yok. Ücret: ucretsiz. Örtüşme: yeni grup video-tasarim-kurallari; stil (gorsel-stil-sistemi) ve hyperframes ev stili skilleriyle konu komşusu ama farklı iş (tasarım kuralı, stil çıkarma değil).

### video-download  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** yt-dlp ile YouTube ve 1000+ siteden video, sadece ses, altyazı ve metadata indirme komutlarını verir; kalite ön ayarları ve çıktı şablonlarını içerir. API anahtarı gerekmez.
- **Ne zaman:** Referans/kaynak video, ses veya altyazı indirmek ya da metadata almak gerektiğinde. · **Ne zaman değil:** YouTube'da arama/listeleme için; telif veya platform koşullarına aykırı kullanımda.
- **Teknoloji:** yt-dlp, ffmpeg · **Paketler:** yt-dlp, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-indirme → birincil · **Roller:** video-kurgu-render
- **Boyut:** 3 KB (SKILL.md 3.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kısa, doğru, bağımsız. Telif sorumluluğu kullanıcıda.

### video-edit  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 100 (A)

- **Ne yapar:** ffmpeg/ffprobe ile yerelde video kırpma, birleştirme, platforma göre boyutlandırma, hız değiştirme, ses çıkarma/değiştirme, sıkıştırma, format dönüştürme ve logo bindirme komutlarını verir.
- **Ne zaman:** Hazır videolar üzerinde hızlı kurgu ve sosyal medya formatına uyarlama işlerinde. · **Ne zaman değil:** Sahne kompozisyonu/animasyon gerekiyorsa (hyperframes); karmaşık filtre zincirleri için ffmpeg skill'i.
- **Teknoloji:** ffmpeg · **Paketler:** ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ffmpeg-kurgu → birincil · **Roller:** video-kurgu-render
- **Boyut:** 12 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Kısa, genel, platform ön ayarlı; bağımlılığı sadece ffmpeg.

### video-edit@yildizdikme  ·  YildizDikme/claude-video-edit @ b7093e2  ·  puan 68 (B)

- **Ne yapar:** Konuşan kişi (talking-head), eğitim ve Short videoları için kurgu: Whisper ile kelime hassasiyetli kesim, HTML+GSAP sahneler, Python'la sentezlenen ses efektleri, ses seviyesi (loudness) ayarı ve kare-doğru render.
- **Ne zaman:** Tek kişilik anlatım videosunu kelime düzeyinde temizleyip hareketli grafik ve SFX ile Short'a çevirmek. · **Ne zaman değil:** DİKKAT: adı 'video-edit'; globalde OpenMontage'in video-edit'i olduğu için Claude onu kullanır, bu skill gölgede kalır. Betik yollarını ~/.claude/skills/video-edit varsayar (projeye kurulunca yollar kırılır); ~/.claude/video-edit/ altına profil ve brand/ yazar. Genel kurgu için OpenMontage video-edit, altyazı için embedded-captions, kesim için talking-head-recut.
- **Teknoloji:** python, ffmpeg, whisper, gsap, html · **Paketler:** ffmpeg, whisper, chrome
- **Claude / Codex:** tam / tam
- **Geliştirici:** YildizDikme (kisi, ★33, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** ffmpeg-kurgu → alternatif
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

### video-storytelling  ·  nateherkai/herk-edit-kit @ 10511e5  ·  puan 72 (B)

- **Ne yapar:** Uzun biçimli konuşan kafa videosunun görsel katmanını ayrı grafiklerin dizisi olarak değil, kameranın içinde gezdiği tek kalıcı dünya olarak tasarlar ve kurar. Dört ilke (kalıcı dünya, uzamsal dilbilgisi, açık döngüler, kamera/spot ışığı), tasarım sistemi referansı ve 'wall-of-slots' örnek geometrisi içerir; seyirci dokuzuncu dakikada hâlâ yönünü bilir.
- **Ne zaman:** Haber, tek konulu derin analiz, karşılaştırma, eğitim ya da liste videosunun görsellerini tasarlarken, 'kafa karıştırıcı' geri bildirimi aldıktan sonra. · **Ne zaman değil:** Kart/alt üçlük yerleştirmek için değil (hyperframes-video-beats); kısa dikey videolar için değil.
- **Teknoloji:** hyperframes, gsap, python · **Paketler:** hyperframes
- **Claude / Codex:** tam / tam
- **Geliştirici:** nateherkai (kisi, ★2929, son güncelleme 2026-10-14, lisans NOASSERTION)
- **Durum:** tercih · **Örtüşme:** konusan-kafa-gorsel-katman → tamamlayıcı · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 47 KB (SKILL.md 19.0 KB, yük orta) · **Bağımlılık:** Skiller repo kökündeki scripts/, style-library/, docs/ ve video-projects/ dizinlerine bağlıdır (skil klasörü dışında; yalnız skil klasörleri alınır); Node, ffmpeg, HyperFrames gerekir. ElevenLabs/Kie.ai isteğe bağlı.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Konsept güçlü ('sahne düşüncesi' hatasına karşı kalıcı dünya), uzamsal dil ve açık döngü fikirleri uygulanabilir ve örnek geometri betikleri var. Yukarı akım eksiği: skill klasörü dışındaki repo kökü dosyalarına (scripts/, docs/, style-library/, MOTION_PHILOSOPHY.md) bağlıdır; arşive yalnız skill klasörleri alındığı için bunlar yoktur, kurulan kopyada ilgili adımlar çalışmaz. Ücret: ucretsiz. Lisans: MIT (LICENSE okundu; GitHub NOASSERTION). Güvenlik: DİKKAT (düşük) — yalnız örnek geometri Python'ı. Örtüşme: konusan-kafa-gorsel-katman grubunda tamamlayıcı (tasarım ilkeleri).

### video-toolkit  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 77 (B)

- **Ne yapar:** claude-code-video-toolkit ile metin brifinden açıklayıcı video üretir: Modal/RunPod bulut GPU'larında seslendirme, görsel, müzik, konuşan kafa üretimi ve Remotion render. Kurulum ve uç nokta yapılandırmasını adım adım anlatır.
- **Ne zaman:** Toolkit ~/.openclaw/workspace/claude-code-video-toolkit yolunda kuruluysa ve bulut GPU kullanılacaksa. · **Ne zaman değil:** OpenMontage veya HyperFrames ile çalışırken; toolkit kurulu değilse.
- **Teknoloji:** remotion, python, node, modal, runpod · **Paketler:** claude-code-video-toolkit, modal, ffmpeg
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** remotion-cercevesi → alternatif
- **Boyut:** 15 KB (SKILL.md 14.8 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Sabit ~/.openclaw yoluna ve ayrı toolkit kurulumuna bağımlı; bu ortamda yok. --break-system-packages önerisi riskli.

### video-translate  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 93 (A)

- **Ne yapar:** HeyGen /v2/video_translate ile mevcut videoyu başka dillere çevirip dudak senkronlu dublaj yapar; sadece ses çevirisi, konuşmacı sayısı ve webhook seçenekleri vardır.
- **Ne zaman:** Hazır bir videonun çok dilli (ör. Türkçe→İngilizce) dublajlı sürümleri gerektiğinde. · **Ne zaman değil:** Sadece altyazı çevirisi yeterliyse; HeyGen anahtarı yoksa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-ceviri-dublaj → birincil · **Roller:** video-kurgu-render, ai-medya-uretici
- **Boyut:** 11 KB (SKILL.md 10.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Odaklı resmi HeyGen skill'i; ücretli.

### video-understand  ·  OpenMontageInc/OpenMontage @ fecb9a1  ·  puan 94 (A)

- **Ne yapar:** ffmpeg ile sahne/anahtar kare çıkarıp Whisper ile sesi yerelde yazıya döken betik; videonun içeriğini JSON olarak özetler. API anahtarı gerekmez, tamamen çevrimdışı çalışır.
- **Ne zaman:** Bir videoyu kurgulamadan önce ne içerdiğini anlamak, kareleri incelemek veya yerel transkript almak gerektiğinde. · **Ne zaman değil:** Yüksek doğruluklu çok dilli transkript (speech-to-text) veya konuşmacı ayrımı gerekiyorsa.
- **Teknoloji:** ffmpeg, python, whisper · **Paketler:** ffmpeg, openai-whisper
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★79720, son güncelleme 2026-11-09, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** video-analiz → birincil · **Roller:** video-kurgu-render
- **Boyut:** 27 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Betiği skill klasöründe; yol skills/video-understand/... diye yazılmış, kurulumda skill yoluna göre çalıştırılmalı.

### video-use  ·  browser-use/video-use @ 43cfc56  ·  puan 82 (A)

- **Ne yapar:** Konuşarak video kurgu: ElevenLabs Scribe ile kelime düzeyi transkript, kesim kararları (EDL), renk düzeltme, bindirme animasyonları (HyperFrames, Remotion, Manim ya da PIL), altyazı ve ses/müzik karışımı; render'dan sonra kendi çıktısını ölçüp doğrular. 12 maddelik 'sert kural' (altyazı en sonda, 30 ms ses solması, sözcüğün içinde kesmeme, transkript önbelleği) dışında yaratıcı özgürlük bırakır.
- **Ne zaman:** Çok çekimli konuşmalı videolar, tanıtım ve eğitim klipleri, mülakat ve montajlar; planı önce düz Türkçe/İngilizce onaylatıp sonra uygulanacak iş akışı. · **Ne zaman değil:** Çevrimdışı ya da anahtarsız çalışılacaksa (transkript ElevenLabs'a gider); basit sessizlik kesimi için auto-editor; saf kodla video üretimi için HyperFrames/Remotion skilleri. Paralel animasyon alt-ajanları Claude Code'un Agent aracına dayanır (Codex'te o kısım çalışmaz).
- **Teknoloji:** python, ffmpeg, elevenlabs, hyperframes, remotion, manim · **Paketler:** ffmpeg/ffprobe, requests, librosa, matplotlib, Pillow, numpy, ELEVENLABS_API_KEY, isteğe bağlı: yt-dlp, HyperFrames, Remotion, Manim
- **Claude / Codex:** tam / tam
- **Geliştirici:** browser-use (kurum, ★31088, son güncelleme 2026-10-08, lisans MIT)
- **Durum:** tercih · **Örtüşme:** konusmayla-kurgu → birincil · **Roller:** video-kurgu-render, video-kompozisyon
- **Boyut:** 205 KB (SKILL.md 25.5 KB, yük buyuk) · **Bağımlılık:** video-use skili ElevenLabs Scribe API'si ister (ELEVENLABS_API_KEY; ücretsiz kota var, yoğun kullanım ücretli) + ffmpeg/ffprobe + Python (requests, librosa, matplotlib, pillow, numpy). Animasyon için isteğe bağlı HyperFrames/Remotion/Manim/yt-dlp (ilk kullanımda npx --yes ile kurulur). Paralel animasyon alt-ajanları Claude Code'un Agent/alt-ajan aracına dayanır (Codex'te bu kısım çalışmaz; temel transkript/kesim/render çalışır). Kurulum kontrolleri SKILL.md 'Setup' bölümünde, bağımlılıklar pyproject.toml'da. install.md arşive alınmaz: global skill klasörüne (~/.claude/skills, ~/.codex/skills) symlink kurma talimatı verir (kural 1), oysa skill projeye skill-ekle.py ile kurulur.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Sert kurallar gerçek üretim hatalarından çıkmış, kendi çıktısını ölçme adımı güçlü; ama 25 KB'lık büyük bağlam, ücretli/kotalı ElevenLabs bağımlılığı ve ilk kullanımda npx --yes ile paket kurma var. Güvenlik (kendim doğruladım): dış bağlantı yalnız helpers/transcribe.py içinde api.elevenlabs.io/v1/speech-to-text'e (ses WAV'ı + ELEVENLABS_API_KEY) gönderim; başka requests/curl/socket yok, diğer yardımcılar yalnız ffmpeg/ffprobe alt süreci. SKILL.md ilk kullanımda npx --yes hyperframes / npx create-video (Remotion) / yt-dlp kurdurur, anahtarı yoksa kullanıcıdan isteyip repo kökündeki .env'e yazdırır (genel klasöre değil). Kısıtlama: install.md arşivde yok (global symlink talimatı). DİKKAT: ses verisi üçüncü tarafa gider; gizli içerikte bilinçli kullan. Ücret: kismen (Scribe ücretsiz kotası).

### video_toolkit  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 80 (A)

- **Ne yapar:** claude-code-video-toolkit'in giriş skili: kısa bir brifi sahne tanımına çevirir, video_job.py ile seslendirme, görsel, altyazı, derleme ve kalite denetimini sırayla yürütüp denetlenmiş bir MP4 üretir. Ayrıca tek tek araçları (yapay zeka sesi, görsel, klip, müzik, konuşan kafa, kesim, YouTube yükleme) hangi işte hangisinin seçileceğini gösteren bir yönlendirme tablosu sunar.
- **Ne zaman:** Toolkit kuruluysa brifden tek istemle kısa açıklayıcı video (Shorts/Reels/16:9) üretmek; mevcut videoda ses, müzik, dikey kesim ya da altyazı değiştirmek; toolkit içindeki hangi şablon ve aracın uygun olduğuna karar vermek. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla). Aynı işi yapan OpenMontage (video-uretim-programi) ya da HyperFrames ile çalışırken kullanma. Proje kopyasında klasör adı video-toolkit olur: eski OpenMontage video-toolkit kopyasıyla aynı projeye birlikte kurma. R2 ayarlı değilse medya halka açık geçici sunuculara (litterbox, 0x0.st) yüklenir: kişisel ya da gizli medyayla R2 olmadan kullanma. Bulut GPU aracı yoksa (Modal/RunPod hesabı) iş akışı çalışmaz.
- **Teknoloji:** remotion, python, node, ffmpeg, modal, runpod, api-anahtari, playwright · **Paketler:** claude-code-video-toolkit (uv sync), uv, ffmpeg, Node, Modal ya da RunPod hesabı
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** video-uretim-programi → alternatif · **Roller:** ai-medya-uretici, video-kurgu-render
- **Boyut:** 35 KB (SKILL.md 34.7 KB, yük buyuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Toolkit'in tek giriş sayfası; iş akışı (tahmin → gönder → durum → sonuç, harcama defteri, kalite kapısı) iyi anlatılmış, 35 KB'lık büyük skill. Sınırı: toolkit kurulu olmadan hiçbir komutu çalışmaz; OpenMontage'a (birincil) yedek yoldur. Lisans MIT (toolkit); kullanılan modellerin ve çıktıların lisansı ayrıdır (LTX topluluk lisansı, Ideogram API ticari). Yol: skill yalnız göreli toolkit yollarını ve VIDEO_TOOLKIT_ROOT ortam değişkenini kullanır, sabit kullanıcı yolu yok (yol-tara 0 bulgu). Örtüşme: aynı işi yapan eski OpenMontage kopyası video-toolkit (kalite 2, SADECE ARŞİV, yine de durum tercih görünüyor, kaynak ajanına rapor) ile ve openmontage/hyperframes ile örtüşür; remotion-best-practices çekirdek Remotion bilgisidir, bu skill onun yerine geçmez. Güvenlik (dikkat): (1) klonlama ve uv sync, modal deploy, echo >> .env gibi kurulum ve anahtar yazma adımları; (2) R2 yoksa kullanıcının medyası litterbox.catbox.moe (24 saat) ve 0x0.st (30 gün) gibi halka açık geçici sunuculara yüklenir, linki bilen herkes görür; (3) dewatermark.py/locate_watermark.py ProPainter ile filigran siler (~2 GB model indirir): yalnız kendi içeriğinde kullan, başkasının filigranını kaldırmak telif ve LTX topluluk lisansındaki 'filigran ve köken özelliklerini kaldırma' yasağıyla çatışır; (4) youtube_upload.py Google OAuth ile video yükler (varsayılan gizli); (5) ses klonlama (--ref-audio) için kişinin izni gerekir. Ücret: kismen (Modal aylık ücretsiz kota, acemusic ve Openverse ücretsiz; ElevenLabs, Ideogram, RunPod ücretli).

### vox-explainer  ·  heygen-com/hyperframes-community-skills @ ba7a0bb  ·  puan 79 (B)

- **Ne yapar:** Günlük gördüğümüz ama hiç üzerinde durmadığımız bir konu ya da verilen belge/bağlantılardan 60-90 saniyelik kolaj stilinde HyperFrames açıklayıcı video yapar: önce tanıma duygusu yaratır, sonra nedensel tarihle karşılığını verir. Vox'un Cooper Black filminden ölçülmüş dilbilgisi ve hareket; bağlantı/atıf kuralları açık.
- **Ne zaman:** "Why is X everywhere?", "plain-sight explainer", "Vox-style history of X" gibi konu belgeseli tarzı kısa açıklayıcı. · **Ne zaman değil:** Ürün tanıtımı/demo için değil (urun-tanitim-filmi ve explainer-* kullan). Vox'la bağlantı ya da onay ima edilmez, logosu kullanılmaz.
- **Teknoloji:** hyperframes, gsap, node, chrome · **Paketler:** hyperframes (seam-gate betiğinde sabitlenmiş sürüm, npx), node 22+
- **Claude / Codex:** tam / tam
- **Geliştirici:** heygen-com (kurum, resmî, ★280, son güncelleme 2026-11-17, lisans Apache-2.0)
- **Durum:** tercih · **Örtüşme:** konu-aciklayici-video → birincil · **Roller:** video-kompozisyon, motion-graphics-sanatcisi
- **Boyut:** 110 KB (SKILL.md 13.9 KB, yük orta) · **Bağımlılık:** HyperFrames CLI (npx hyperframes) gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güven sınırı açıkça yazılmış (yalnız verilen dosya/URL okunur, TTS/transkript API'si kullanmadan önce sağlayıcı, gönderilen veri ve maliyet sorulur, hiçbir şey otomatik yüklenmez), seam doğrulayıcı betikleri yerel; çok sayıda referans dosyasıyla kademeli yükleme. Ücret: ucretsiz (HeyGen yalnız HyperFrames'in kurulum kaynağı olarak anılır). Lisans: Apache-2.0. Güvenlik: DİKKAT (düşük) — yerel önizleme sunucusu yalnız localhost, izole Chrome profili, npx ile sürüm sabitli CLI. Örtüşme: grup yok (konu belgeseli tarzı farklı iş).

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

### youtube-stats  ·  digitalsamba/claude-code-video-toolkit @ 01e85f4  ·  puan 76 (B)

- **Ne yapar:** Yayımlanmış YouTube videolarının performansını okur: izlenme, beğeni, yorum, abone; Analytics yetkisiyle izlenme süresi, tutma ve trafik kaynakları (Shorts akışı, arama, dış bağlantı). Her çalıştırmada anlık görüntü kaydeder, değişimi gösterir; GitHub trafiğini yan yana verir. Sonuçlardan bir sonraki Short için açılış kuralları çıkarır.
- **Ne zaman:** Kanal ya da video performansını, başlık ve kapak kararlarını, Short'un akışta ne yaptığını ölçmek; toolkit ile YouTube'a yükleme yapıldıysa. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) (youtube_stats.py ve youtube_upload.py ile önbelleğe alınmış OAuth jetonu gerekir). Başka kişinin kanalı için kullanılamaz (yalnız kendi hesabınla OAuth). Skill gövdesinde yazarın kendi kanalının bulguları ('ne işe yaradı' listesi) var; kendi verinle değiştir.
- **Teknoloji:** python, api-anahtari · **Paketler:** uv (--extra youtube), Google Cloud OAuth istemcisi, YouTube Data + Analytics API
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2579, son güncelleme 2026-11-14, lisans MIT)
- **Durum:** tercih · **Örtüşme:** youtube-analitik → birincil · **Roller:** video-kurgu-render
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (koşullu). Metrikleri yorumlama rehberi (Short'ta ortalama izlenme yüzdesi, trafik kaynağı okuması) yararlı; ama skill, toolkit'in araç ve jeton yapısına bağlı ve içinde yazarın kendi kanalına ait tarihli bulgular var (genel değil). Lisans MIT. Güvenlik (dikkat): hassas bir Google kapsamı (yt-analytics.readonly) ister, OAuth jetonu toolkit kökünde (_internal/.youtube) saklanır; --github seçeneği GitHub trafik verisini okur; veriyi dışarı göndermez. Ücret: ucretsiz (API kotası kullanıcının kendi Google projesinde, ücretsiz). Sabit yol yok. Örtüşme: yok (youtube-analitik grubunun tek üyesi).

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
