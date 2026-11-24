# 03-ai-gorsel-video-modelleri — Video, Ses ve AI Medya Üretimi

_AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **24/27**

### 3d-asset-generation  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** OpenMontage dünyaları için üretim kalitesinde 3D varlık üretir/yönlendirir: Atlas Tripo, fal Hunyuan 3D, SAM 3D ve CC0 kataloglar arasından role göre seçim, ücretli çağrı disiplini ve Blender'da zorunlu mesh kontrolü.
- **Ne zaman:** Video/3D sahne için gerçek mesh (kahraman obje, sahne objeleri) gerektiğinde. · **Ne zaman değil:** Tüm sahneyi tek mesh olarak üretmek; web 3D arayüzü (a-tasarim/05 skilleri).
- **Teknoloji:** blender, three.js, atlas-cloud, fal-ai, api-anahtari · **Paketler:** ATLASCLOUD_API_KEY, FAL_KEY, blender, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** 3d-varlik-uretimi → birincil · **Roller:** ai-medya-uretici, 3d-gelistirici
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Maliyet ve kalite disiplini örnek düzeyde; OpenMontage araçlarına bağımlı.

### ai-video-gen  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** Metinden ve görselden AI video üretimini fal.ai, HeyGen ve Gemini API ağ geçitleri üzerinden yönetir; Seedance 2.0'ı premium varsayılan sayar ve sağlayıcıyı video_selector ile seçmeyi şart koşar.
- **Ne zaman:** AI video klibi üretilecek ve hangi model/ağ geçidinin kullanılacağına karar verilecekse; model seçiminin giriş noktası. · **Ne zaman değil:** Belirli bir modelin ayrıntılı prompt rehberi gerektiğinde (seedance-2-0, gemini-omni, kling-official).
- **Teknoloji:** fal-ai, heygen, google-gemini, api-anahtari · **Paketler:** FAL_KEY|HEYGEN_API_KEY|GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İyi yönlendirici; video_selector önerisi OpenMontage'a bağlı. Sıralama bilgileri tarihe duyarlı. · 2026-11-12 yeniden incelendi: içerik değişmedi (kaynak OpenMontageInc/OpenMontage fecb9a1'e taşındı), değerlendirme aynı.

### antigravity-gorsel  ·  yerel/kendi @ 3c8d08e  ·  puan 75 (B)

- **Ne yapar:** Google Antigravity'nin komut satırı aracı (agy) üzerinden görsel üretir ve dosyayı istenen klasöre kaydeder. Kullanıcı "Antigravity ile resim üret", "antigravity'den görsel yap", "agy ile görsel", "Antigravity'ye bağlanıp ... resmi çiz" gibi bir şey dediğinde kullan. Antigravity adı geçmeyen genel görsel isteklerinde kullanma.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** kullanıcı (kisi, resmî, ★0, son güncelleme 2026-11-25, lisans Kendi (özel))
- **Durum:** tercih
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk)
- **İnceleme:** otomatik

### atlas-cloud  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Atlas Cloud ağ geçidiyle tek anahtarla Seedance 2.5/2.0, Gemini Omni, MiniMax H3, Seedream 5, GPT Image 2, Nano Banana 2 görsel/video üretimi ve düzenlemesi; her ücretli çağrı öncesi katalog ve maliyet kontrolünü zorunlu tutar.
- **Ne zaman:** Kullanıcı Atlas Cloud istediğinde veya tek ATLASCLOUD_API_KEY ile çok model ailesine erişilecekse. · **Ne zaman değil:** Doğrudan sağlayıcı anahtarı varken (seedance, gemini-omni); Atlas hesabı yoksa.
- **Teknoloji:** atlas-cloud, python, api-anahtari · **Paketler:** ATLASCLOUD_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-saglayici-yonlendirme → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kesin rota/fiyat tabloları ve 'sessizce sınırlama' yasağı iyi.

### avatar-video  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** HeyGen v2 API ile avatar, ses, metin, sahne ve arka plan üzerinde tam kontrollü avatar videosu üretir; çok sahneli, şeffaf WebM ve Remotion entegrasyonu dahil.
- **Ne zaman:** Belirli avatar/sesle birebir metin okutulacak, sahne bazlı kontrol gerekecek veya toplu üretim yapılacaksa. · **Ne zaman değil:** Tek istemden hızlı video (create-video); avatar gerekmiyorsa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → tamamlayıcı · **Roller:** ai-medya-uretici, video-kompozisyon
- **Boyut:** 177 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmi ve iyi bölümlenmiş referanslar.

### bfl-api  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** Black Forest Labs FLUX API entegrasyon rehberi: uç noktalar, bölgesel sunucular, fiyatlar, asenkron sorgulama, hız sınırı, hata yönetimi ve webhook örnekleri (Python/TypeScript).
- **Ne zaman:** FLUX'u bir uygulamaya veya üretim hattına API ile bağlarken. · **Ne zaman değil:** Sadece iyi prompt yazmak gerekiyorsa (flux-best-practices).
- **Teknoloji:** bfl-flux, python, typescript, api-anahtari · **Paketler:** BFL_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-uretimi → tamamlayıcı · **Roller:** ai-medya-uretici
- **Boyut:** 79 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi BFL skill'i; sonuç URL'lerinin 10 dk'da düştüğü gibi kritik uyarılar var.

### comfyui  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** OpenMontage'da ComfyUI iş akışlarıyla (comfyui_image/video/music) yerel üretim: sunucu sözleşmesi, API formatlı iş akışı, output_node seçimi, eksik model kurulumu, düşük VRAM seçenekleri ve ücretli Partner Node ayrımı.
- **Ne zaman:** Yerel GPU'da açık ağırlıklı modellerle (Wan, LTXV, MiniMax H3 local) üretim yapılacak veya topluluk iş akışı içe alınacaksa. · **Ne zaman değil:** GPU yoksa; barındırılan API yeterliyse.
- **Teknoloji:** comfyui, python, gpu · **Paketler:** ComfyUI sunucusu, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** yerel-uretim-comfyui → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 'Partner Node yerel/ücretsiz değildir' gibi dürüst ayrımlar değerli; GPU/VRAM gerektirir.

### faceswap  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** HeyGen FaceswapNode iş akışıyla kaynak görseldeki yüzü hedef videoya aktarır; iş gönderme, durum sorgulama ve TypeScript/Python örnekleri içerir.
- **Ne zaman:** Kişinin açık izniyle kişiselleştirilmiş video veya kendi yüzünü sahneye yerleştirme gerektiğinde. · **Ne zaman değil:** Rızası olmayan kişilerle, yanıltıcı/deepfake amaçlı içerikte.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** yuz-degistirme → birincil
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Teknik olarak düzgün; rıza ve kötüye kullanım riski nedeniyle rollere eklenmedi, açık istekle --skill ile kurulur.

### flux-best-practices  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** BFL FLUX görsel modelleri için kapsamlı prompt rehberi: prompt yapısı, model seçimi (klein/pro/max/flex), T2I, I2I, JSON yapılandırılmış prompt, HEX renk, tipografi ve çoklu referans düzenleme kuralları.
- **Ne zaman:** FLUX ile görsel üretirken veya düzenlerken prompt kalitesini artırmak için. · **Ne zaman değil:** Başka görsel modellerinde (GPT Image, Seedream) — kurallar FLUX'a özgü; API kurulumu için bfl-api.
- **Teknoloji:** bfl-flux
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-uretimi → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 122 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi BFL rehberi, kural dosyalarına iyi bölünmüş.

### gemini-omni  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** Google Gemini Omni Flash ile 3-10 sn 720p sesli video üretimi ve aynı klibi doğal dille durum korumalı (interaction_id) düzenleme; referans görsel etiketleri, zaman kodlu vuruşlar ve rota sınırlamaları.
- **Ne zaman:** Üretilen bir klibi yeniden üretmeden adım adım düzeltmek veya mevcut videoyu düzenlemek gerektiğinde. · **Ne zaman değil:** Tek seferlik sinematik kahraman klip (seedance-2-0), 10 sn'den uzun veya 720p üstü çıktı (model destekler ama adaptör henüz uygulamıyor), İngilizce dışı anlatım.
- **Teknoloji:** google-gemini, api-anahtari · **Paketler:** GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 10 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Ne zaman seçilip seçilmeyeceği tablosu net; benzersiz düzenleme yeteneği. 2026-11: kararlı gemini-omni-1.1-flash modeline geçti; maliyet ~$0.10/sn, süre ipucu faturayı sınırlamıyor (en kötü ~$1.01/klip).

### grok-media  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 86 (A)

- **Ne yapar:** xAI Grok görsel ve video üretimi rehberi: kimlik doğrulama, uç noktalar, görsel düzenleme/birleştirme, referans görselli video, asenkron sorgulama, fiyatlar ve Grok'a özgü prompt önerileri.
- **Ne zaman:** XAI_API_KEY ile kısa referans koşullu video veya çok kaynaklı görsel birleştirme gerektiğinde. · **Ne zaman değil:** Uzun klip, deterministik seed veya yüksek çözünürlük gerektiğinde.
- **Teknoloji:** xai-grok, api-anahtari · **Paketler:** XAI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa ve doğru; derinliği diğer model rehberlerinden az.

### heygen  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 78 (B)

- **Ne yapar:** [KULLANIMDAN KALKMIŞ] HeyGen Video Agent ve v2 avatar iş akışlarını birleştiren eski skill; yerini create-video ve avatar-video aldı, geriye uyumluluk için duruyor.
- **Ne zaman:** Sadece eski bir projede 'heygen' adıyla başvuru varsa. · **Ne zaman değil:** Yeni işlerde — create-video veya avatar-video kullan.
- **Teknoloji:** heygen, api-anahtari · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → alternatif
- **Boyut:** 225 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Kaynak skill kendini deprecated ilan ediyor; ai-medya-uretici rolünden çıkarıldı.

### higgsfield-generate  ·  avenoxai/higgsfield-studio @ a655cf5  ·  puan 59 (C)

- **Ne yapar:** Higgsfield üzerinden görsel, video, 3D varlık ve ses üretir. İşe göre model seçer: görsel/tasarım/metin için GPT Image 2, video için Seedance 2.0, karakter ve referans görseller için Nano Banana, reklam için Marketing Studio. Model kataloğu, medya girdileri, reklam kipleri ve sorun giderme referansları içerir.
- **Ne zaman:** Higgsfield hesabıyla tek yerden görsel/video/ses üretimi; model seçimini skile bırakmak isteniyorsa. · **Ne zaman değil:** DİKKAT: Higgsfield hesabı ve CLI (ya da MCP bağlayıcısı) gerekir; CLI yoksa skill kurulum betiğini ağdan indirip çalıştırır. Üretim kredi harcar. Repoda lisans dosyası yok. Başka sağlayıcı (fal.ai, Atlas Cloud, yerel ComfyUI) kullanılacaksa o sağlayıcının skili.
- **Teknoloji:** higgsfield, api-anahtari · **Paketler:** higgsfield-cli
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** avenoxai (kisi, ★18, son güncelleme 2026-11-17, lisans yok)
- **Durum:** tercih · **Örtüşme:** higgsfield-uretim → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 76 KB (SKILL.md 23.3 KB, yük orta) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (higgsfield-uretim grubunda birincil). Kişisel koleksiyon (14★), lisans dosyası yok. Kapsamlı model kataloğu ve referanslar. Çalıştırma testi yapılmadı. DİKKAT: CLI'yi ağdan kurar, üretim kredi harcar.

### higgsfield-marketplace-cards  ·  avenoxai/higgsfield-studio @ a655cf5  ·  puan 61 (C)

- **Ne yapar:** Higgsfield ile pazaryeri ürün görsel kartları üretir: kurallara uygun ana görsel, ikincil ürün görselleri ve A+ tarzı içerik modülleri.
- **Ne zaman:** Pazaryeri ilan görselleri, ürün detay kartları ve A+ içerik modülleri. · **Ne zaman değil:** DİKKAT: Higgsfield hesabı ve CLI (ya da MCP bağlayıcısı) gerekir; CLI yoksa skill kurulum betiğini ağdan indirip çalıştırır. Üretim kredi harcar. Repoda lisans dosyası yok. Serbest ürün çekimi için higgsfield-product-photoshoot.
- **Teknoloji:** higgsfield, api-anahtari · **Paketler:** higgsfield-cli
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** avenoxai (kisi, ★18, son güncelleme 2026-11-17, lisans yok)
- **Durum:** tercih · **Örtüşme:** higgsfield-uretim → tamamlayıcı · **Roller:** ai-medya-uretici
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (higgsfield-uretim grubunda tamamlayıcı). Kişisel koleksiyon, lisans dosyası yok; kısa (88 satır). Çalıştırma testi yapılmadı.

### higgsfield-product-photoshoot  ·  avenoxai/higgsfield-studio @ a655cf5  ·  puan 59 (C)

- **Ne yapar:** Higgsfield'ın ürün çekimi istem geliştirmesiyle GPT Image 2 üzerinde marka kalitesinde ürün görselleri üretir: stüdyo çekimi, yaşam tarzı sahnesi, mevsimsel varyasyon, reklam paketi. Kullanım yerine göre (mağaza, sosyal medya, reklam, site) set kurar.
- **Ne zaman:** Ürün fotoğrafı, stüdyo/lifestyle çekim seti ve reklam görseli paketi. · **Ne zaman değil:** DİKKAT: Higgsfield hesabı ve CLI (ya da MCP bağlayıcısı) gerekir; CLI yoksa skill kurulum betiğini ağdan indirip çalıştırır. Üretim kredi harcar. Repoda lisans dosyası yok. Genel amaçlı üretim için higgsfield-generate.
- **Teknoloji:** higgsfield, api-anahtari · **Paketler:** higgsfield-cli
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** avenoxai (kisi, ★18, son güncelleme 2026-11-17, lisans yok)
- **Durum:** tercih · **Örtüşme:** higgsfield-uretim → tamamlayıcı · **Roller:** ai-medya-uretici
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (higgsfield-uretim grubunda tamamlayıcı). Kişisel koleksiyon, lisans dosyası yok. Çalıştırma testi yapılmadı.

### higgsfield-soul-id  ·  avenoxai/higgsfield-studio @ a655cf5  ·  puan 61 (C)

- **Ne yapar:** Bir kişinin yüzünden kişiselleştirilmiş model (Soul Character) eğitir; Higgsfield bu modeli sonraki görsel ve video üretimlerinde yüz tutarlılığı için kullanır. Fotoğraf seçimi rehberi ve sorun giderme içerir.
- **Ne zaman:** Aynı yüzü tüm üretimlerde korumak (dijital ikiz, avatar, karakter tutarlılığı). · **Ne zaman değil:** DİKKAT: ücretli plan (Basic ve üstü) ister; ücretsiz planda çalışmaz. Kişinin yüz fotoğrafları Higgsfield'a yüklenir; yalnızca izni olan kişiler için kullanılmalı. Higgsfield hesabı ve CLI (ya da MCP bağlayıcısı) gerekir; CLI yoksa skill kurulum betiğini ağdan indirip çalıştırır. Üretim kredi harcar. Repoda lisans dosyası yok.
- **Teknoloji:** higgsfield, api-anahtari · **Paketler:** higgsfield-cli
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: argument-hint (Codex bunları yok sayar)
- **Geliştirici:** avenoxai (kisi, ★18, son güncelleme 2026-11-17, lisans yok)
- **Durum:** tercih · **Örtüşme:** higgsfield-uretim → tamamlayıcı · **Roller:** ai-medya-uretici
- **Boyut:** 5 KB (SKILL.md 3.3 KB, yük kucuk) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (higgsfield-uretim grubunda tamamlayıcı). ÜCRETLİ: Soul eğitimi Basic+ plan ister. Kişisel koleksiyon, lisans dosyası yok. Çalıştırma testi yapılmadı.

### ideogram4  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 85 (A)

- **Ne yapar:** Ideogram 4 metinden görsele üretiminde yapılandırılmış JSON başlıkla (json_prompt) en iyi sınıftan görsel içi yazı, tam renk paleti ve sınırlayıcı kutularla yerleşim denetimi. Kullanıcının gündelik isteğini modelin eğitildiği JSON başlığa genişleten 'sihirli istem' rehberi; örnekler ve istem desenleri ayrı dosyalarda.
- **Ne zaman:** Okunur yazı gereken görseller: başlık kartı, küçük resim, logo, tabela, alıntı kartı; hex renk ve yerleşim denetimi; çok dilli yazı. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) (tools/ideogram4.py) ve IDEOGRAM_API_KEY. Yazısız atmosferik arka plan ya da ticari lisanslı serbest ağırlık için FLUX; kendi barındırdığın ağırlıklar ticari olmayan lisanslıdır.
- **Teknoloji:** api-anahtari, python · **Paketler:** IDEOGRAM_API_KEY, claude-code-video-toolkit (tools/ideogram4.py)
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2749, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 22 KB (SKILL.md 7.4 KB, yük kucuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: ALTERNATİF. Yazılı görsel için güçlü ve somut kılavuz (JSON şeması, örnekler); istem deseni bölümü araçtan bağımsız yararlı. Ücretli: Ideogram barındırılan API'si görsel başına ücretli anahtar ister, ücretsiz yol yok (ucretli; rol çekirdeğine gerekçesiz alma). Lisans MIT (skill); ücretli API planı çıktıda ticari lisans verir, açık ağırlıklar ticari olmayan. Güvenlik: anahtar .env'de, istemler api.ideogram.ai'ye gider; betik indirmesi yok. ai-gorsel-uretimi grubunda flux-best-practices birincil; yazı gerektiren işte bu tercih edilir.

### kling-official  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 93 (A)

- **Ne yapar:** Kling resmi doğrudan API'si (KLING_API_KEY) için OpenMontage sağlayıcı kuralları: fal.ai Kling'den ayrımı, klasik/turbo görev protokolleri, Omni referans yapıları, TTS/avatar/lip-sync sınırları.
- **Ne zaman:** Resmi Kling API'si ile video/görsel/avatar üretilecekse. · **Ne zaman değil:** fal.ai üzerinden Kling (ai-video-gen); OpenMontage kullanılmıyorsa sağlayıcı sarmalayıcıları yok.
- **Teknoloji:** kling, python, api-anahtari · **Paketler:** KLING_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Ayrıştırıcıların karıştırılmaması gibi titiz kurallar; ağırlıkla geliştirici/entegrasyon odaklı.

### ltx2  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 81 (A)

- **Ne yapar:** LTX-2.3 (22B) ile yaklaşık 5 saniyelik video klip üretimi: metinden videoya ve görselden videoya (fotoğrafı canlandırma); b-roll, hareketli arka plan. Kullanıcının Modal hesabındaki A100 uç noktasında çalışır (MODAL_LTX2_ENDPOINT_URL); çözünürlük, kare sayısı, hız modu ve tohum parametreleri; LTX-2.5 dağıtım sırasında isteğe bağlıdır.
- **Ne zaman:** Toolkit kuruluysa ve Modal uç noktası dağıtıldıysa kısa AI b-roll, hareketli arka plan ya da bir fotoğrafı canlandırma. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) ve dağıtılmış Modal uç noktası. Okunur yazı gereken sahnede (model harfleri uydurur; yazıyı moviepy ile bindir). R2 ayarlı değilse medya halka açık geçici sunuculara (litterbox, 0x0.st) yüklenir: kişisel ya da gizli medyayla R2 olmadan kullanma (--input görseli bulut GPU'ya gider). Hazır servis tercih edilirse ai-video-gen.
- **Teknoloji:** python, modal, api-anahtari · **Paketler:** claude-code-video-toolkit (tools/ltx2.py), Modal hesabı, Hugging Face anahtarı (LTX kapılı)
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** digitalsamba (kurum, ★2749, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 12 KB (SKILL.md 12.3 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Parametre tablosu, istem ve kötü istem örnekleri ve dağıtım adımları net; toolkit'e ve kendi Modal uç noktana bağlı. ai-video-uretimi grubunda ai-video-gen birincil; eski OpenMontage kopyası ltx2@openmontageinc alternatif. Ücret: kismen (Modal aylık ücretsiz kota, fazlası ücretli; klip başı ~0,10$). Lisans MIT (skill); LTX-2.x Topluluk Lisansı: 10M$ yıllık gelirin altında ücretsiz ticari kullanım, üstünde ticari lisans gerekir; filigran ve köken özelliklerini kaldırma. Güvenlik: modal deploy ve echo >> .env adımları, Hugging Face jetonu, R2 yoksa halka açık geçici sunucu (yukarıda); betik indirmesi yok.

### ltx2@openmontageinc  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 78 (B)

- **Ne yapar:** LTX-2.3 22B modeliyle Modal (A100) üzerinde ~5 sn metinden/görselden video üretir; kare sayısı kuralı, çözünürlükler ve sinematik prompt rehberi içerir.
- **Ne zaman:** Kendi Modal uç noktası kurulu, ucuz b-roll/arka plan klibi üretilecekse. · **Ne zaman değil:** OpenMontage kurulumunda (tools/ltx2.py yok); uç nokta yoksa.
- **Teknoloji:** ltx, modal, python · **Paketler:** MODAL_LTX2_ENDPOINT_URL, claude-code-video-toolkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** alternatif · **Örtüşme:** ai-video-uretimi → alternatif
- **Boyut:** 7 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu tools/ltx2.py OpenMontage c806645'te yok (claude-code-video-toolkit'ten); prompt rehberi yine de faydalı. LTX-2.5 için provider-model-refresh'e bak.

### minimax-h3  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** MiniMax H3 (Hailuo 3.0) videosunu resmi API, fal.ai, Runway, ComfyUI Partner Node veya yerel açık ağırlıklarla üretir; rotalar arası model kimliği farklarını ve ilk/son kare, referans koşullu üretimi açıklar.
- **Ne zaman:** 4-15 sn 2K klip, ilk/son kare animasyonu veya ses/görsel referanslı video gerektiğinde. · **Ne zaman değil:** Uzun tek üretim (seedance-2-5); bu sağlayıcılardan hiçbirine erişim yoksa.
- **Teknoloji:** minimax, comfyui, api-anahtari · **Paketler:** MINIMAX_API_KEY|FAL_KEY|RUNWAY_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kısa ama net; 'yalnız açık ağırlık rotası yereldir' uyarısı doğru.

### provider-model-refresh  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 94 (A)

- **Ne yapar:** Eylül 2026 görsel, video, konuşma ve Avatar V adaptörleri (GPT Image 2.5, Gemini 3 Pro Image, Ideogram 4.5, Wan 3.0, LTX-2.5, Eleven v4, Lyria 3.5…) için kesin model/host sözleşmeleri; mevcut olmayan modelin sessizce değiştirilmemesini şart koşar.
- **Ne zaman:** OpenMontage'ın yeni nesil adaptörleriyle belirli bir model/host zorunlu tutularak üretim yapılacaksa. · **Ne zaman değil:** OpenMontage dışında; genel model seçimi için ai-video-gen.
- **Teknoloji:** openmontage, python, api-anahtari · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-saglayici-yonlendirme → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 7 KB (SKILL.md 6.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel model kataloğu ve katı yönlendirme kuralları; tamamen OpenMontage registry'sine bağlı. · 2026-11 yeniden incelendi: küçük düzeltmeler, değerlendirme değişmedi. · 2026-11-12 yeniden incelendi (fecb9a1): Kling O3 (Standard/Pro/4K video, Kling Image O3) fal üzerinden eklendi (kling_o3_fal_video/image; FAL_KEY gerekir, resmi Kling kimlik bilgisi değil; 5 video modu, referans/V2V kuralları; eski Kling isteğinde O3 kendiliğinden seçilmez). Ücretli fal.ai yolu bir seçenek; değerlendirme aynı.

### qwen-edit  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 85 (A)

- **Ne yapar:** Qwen-Image ile yapay zeka görsel düzenleme istemi desenleri: kimliği koruyarak fotoğraf düzenleme, kırpılmış görseli yeniden çerçeveleme, kıyafet ve aksesuar değiştirme, poz ayarı, stil aktarımı, karakter dönüşümü. Varsayılan Qwen-Image-Edit-2511 (Apache-2.0, ticari kullanım serbest); Qwen-Image-2.1 ticari olmayan Modal seçeneğidir. Adımlar, kılavuz değeri, çoklu girdi ve RGBA ayrıntıları ayrı dosyalarda.
- **Ne zaman:** Toolkit kuruluysa fotoğraf düzenleme ve karakter tutarlılığı (ör. aynı kişiyle farklı sahneler); parody-short için kadro hazırlama. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla) (tools/image_edit.py) ve Modal/RunPod uç noktası. R2 ayarlı değilse medya halka açık geçici sunuculara (litterbox, 0x0.st) yüklenir: kişisel ya da gizli medyayla R2 olmadan kullanma. Qwen-Image-2.1 seçeneğini ticari işte kullanma (Qwen Araştırma Lisansı).
- **Teknoloji:** python, modal, runpod · **Paketler:** claude-code-video-toolkit (tools/image_edit.py), Modal ya da RunPod hesabı
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2749, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-duzenleme → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 21 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (koşullu). Düzenleme istemleri, ölçülmüş parametreler (adım, kılavuz) ve örnekler değerli ve model sürümüne göre ayrılmış; ancak yazar 'öğrenmeler yazılmaya devam ediyor' diyor ve 2.1 için sayılar yeniden doğrulanmalı. Ücret: kismen (varsayılan Modal'da aylık ücretsiz kota; RunPod ücretli). Lisans MIT (skill); modeller: 2511 Apache-2.0, 2.1 ticari olmayan. Güvenlik: Modal deploy / RunPod kurulumu, anahtar .env'de; kişi fotoğrafları bulut GPU'ya gider ve R2 yoksa halka açık geçici sunucuya yüklenir (kimlik koruyan düzenleme gerçek kişi görüntüsüyle yapılıyorsa izin gerekir). Örtüşme: yeni grup ai-gorsel-duzenleme.

### runpod  ·  digitalsamba/claude-code-video-toolkit @ ad8b4ec  ·  puan 76 (B)

- **Ne yapar:** RunPod sunucusuz bulut GPU kılavuzu: hesap ve API anahtarı, toolkit'in beş Docker imajını (qwen-edit, realesrgan, propainter, sadtalker, qwen3-tts) --setup ile şablon ve uç noktaya çevirme, uç nokta yönetimi, maliyet tabloları, sorun giderme ve Cloudflare R2 ile dosya aktarımı. Saniye başı ücretlendirme.
- **Ne zaman:** Toolkit'in RunPod seçeneğini kurarken ya da uç nokta sorunlarını çözerken; maliyet tahmini. · **Ne zaman değil:** toolkit kökü gerekir (VIDEO_TOOLKIT_ROOT; bu bilgisayarda kurulu değil, kurulum programlar.json → claude-code-video-toolkit kartıyla ayrı onayla). Modal yolu kullanılıyorsa gerekmez (toolkit varsayılanı Modal). RunPod'un ücretsiz katmanı yoktur. R2 ayarlı değilse medya halka açık geçici sunuculara (litterbox, 0x0.st) yüklenir: kişisel ya da gizli medyayla R2 olmadan kullanma. Gizli ya da kişisel veriyi işleyen işlerde üçüncü taraf imajı kullanma.
- **Teknoloji:** runpod, python, api-anahtari · **Paketler:** RUNPOD_API_KEY, claude-code-video-toolkit, isteğe bağlı: Cloudflare R2 + AWS CLI
- **Claude / Codex:** tam / tam
- **Geliştirici:** digitalsamba (kurum, ★2749, son güncelleme 2026-11-24, lisans MIT)
- **Durum:** tercih · **Örtüşme:** bulut-gpu-calistirma → birincil
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta) · **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
- **İnceleme:** incelendi · kalite 3/5 — Karar: TUT (yalnız toolkit ve RunPod kullanılacaksa; rol çekirdeğine alma). Ücretli: RunPod'da ücretsiz katman yok (ucretli). Lisans MIT. Güvenlik (dikkat): (1) uç noktalar üçüncü taraf Docker imajlarından kurulur (ghcr.io/conalmullan/video-toolkit-*:latest, 'latest' etiketi, sabit özet yok, sürüm sabitlenmemiş); imaj içeriği bu kütüphanede incelenmedi, GPU işçisi kullanıcının medyasını ve istemlerini işler; (2) R2 ayarlı değilse yüklemeler 'ücretsiz yükleme servislerine' (litterbox.catbox.moe 24 saat, 0x0.st 30 gün) gider, bağlantıyı bilen herkes görebilir; (3) RUNPOD_API_KEY ve uç nokta kimlikleri .env'e yazılır; (4) R2 için AWS gizli anahtarları ortam değişkeniyle geçilir. Sabit yol yok.

### seedance-2-0  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** ByteDance Seedance 2.0 için yetkili prompt ve parametre rehberi: tek geçişte senkron ses, tek üretimde çoklu çekim, yönetmen düzeyi kamera kontrolü, alıntılı diyalogdan dudak senkronu ve 12 varlıklı referans koşullama; ağ geçidi rotaları.
- **Ne zaman:** Fragman, teaser, sinematik kahraman klip veya karakter tutarlılığı gereken premium AI video işlerinde. · **Ne zaman değil:** Sıkı bütçe (fast varyantı veya LTX), 15 sn'den uzun tek üretim (seedance-2-5), klip düzenleme (gemini-omni).
- **Teknoloji:** seedance, fal-ai, api-anahtari · **Paketler:** FAL_KEY|REPLICATE_API_TOKEN|HEYGEN_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → tamamlayıcı · **Roller:** ai-medya-uretici
- **Boyut:** 17 KB (SKILL.md 17.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. OpenMontage'ın premium varsayılan modeli; en ayrıntılı model rehberi. Elo/sıralama iddiaları tarihe duyarlı.

### seedance-2-5  ·  OpenMontageInc/OpenMontage @ 2e003e6  ·  puan 100 (A)

- **Ne yapar:** Seedance 2.5 ile 4-30 sn sinematik video: fal.ai, Volcengine Ark, Runway, ComfyUI rotaları; bölümlü prompt sözleşmesi, 'Hard cut' çoklu çekim, kesmeler arası adlı kilitler, karakter sayfası yöntemi ve yineleme disiplini.
- **Ne zaman:** 15 sn'den uzun tek üretim, büyük referans seti (30 görsel/10 video/10 ses) veya çekimler arası süreklilik gerektiğinde. · **Ne zaman değil:** Kısa tek aksiyonlu sahnelerde (2.0 yeterli); 1080p gerekiyorsa (desteklenen rotalar 720p).
- **Teknoloji:** seedance, fal-ai, api-anahtari · **Paketler:** FAL_KEY|RUNWAY_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** OpenMontageInc (kurum, ★83050, son güncelleme 2026-11-16, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici
- **Boyut:** 23 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Prompt sözleşmesi çok güçlü; uzun/çok çekimli işlerde 2.0 yerine seçilir.

### video-prompt-builder  ·  avenoxai/higgsfield-studio @ a655cf5  ·  puan 67 (B)

- **Ne yapar:** Seedance 2.0 için izlenme süresi odaklı yapay zekâ video planı kurar: brief'ten klip klip istemlere, birleştirme ve ses planına, isteğe bağlı Nano Banana varlık hattına kadar. Hedef kitle ön ayarları, anlatı omurgaları, karakter tutarlılığı, içerik filtresi ve kanıtlanmış istem referansları içerir.
- **Ne zaman:** Çok klipli AI video planlama ve storyboard; Seedance istemlerini sistemli yazmak. · **Ne zaman değil:** Plan ve istem üretir, videoyu kendisi üretmez (üretim için higgsfield-generate ya da başka bir Seedance sağlayıcısı). Varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir; proje içi yol verilmeli. Repoda lisans dosyası yok.
- **Teknoloji:** seedance, higgsfield
- **Claude / Codex:** tam / tam
- **Geliştirici:** avenoxai (kisi, ★18, son güncelleme 2026-11-17, lisans yok)
- **Durum:** tercih · **Örtüşme:** seedance-video-plani → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 107 KB (SKILL.md 14.4 KB, yük orta) · **Bağımlılık:** Higgsfield hesabı ve Higgsfield CLI gerekir (CLI yoksa skill resmî kurulum betiğini ağdan indirip çalıştırır: curl … | sh; ilk kullanımda `higgsfield auth login`). Higgsfield MCP bağlayıcısı da kullanılabilir. Üretimler Higgsfield kredisi harcar; Soul eğitimi ücretli plan (Basic+) ister. video-prompt-builder üretilen varlıkları ~/Desktop/claudedump/ altına kaydetmeyi önerir (proje dışı).
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (seedance-video-plani grubunda birincil). 248 satır + 11 referans belgesi; plan aşaması ücretsiz ve sağlayıcıdan bağımsız kullanılabilir. Kişisel koleksiyon, lisans dosyası yok. Çalıştırma testi yapılmadı.
