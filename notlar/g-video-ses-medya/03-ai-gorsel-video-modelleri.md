# 03-ai-gorsel-video-modelleri — Video, Ses ve AI Medya Üretimi

_AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **39/39**

### 3d-asset-generation  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** OpenMontage dünyaları için üretim kalitesinde 3D varlık üretir/yönlendirir: Atlas Tripo, fal Hunyuan 3D, SAM 3D ve CC0 kataloglar arasından role göre seçim, ücretli çağrı disiplini ve Blender'da zorunlu mesh kontrolü.
- **Ne zaman:** Video/3D sahne için gerçek mesh (kahraman obje, sahne objeleri) gerektiğinde. · **Ne zaman değil:** Tüm sahneyi tek mesh olarak üretmek; web 3D arayüzü (a-tasarim/05 skilleri).
- **Teknoloji:** blender, three.js, atlas-cloud, fal-ai, api-anahtari · **Paketler:** ATLASCLOUD_API_KEY, FAL_KEY, blender, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** 3d-varlik-uretimi → birincil · **Roller:** ai-medya-uretici, 3d-gelistirici · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 4.8 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Maliyet ve kalite disiplini örnek düzeyde; OpenMontage araçlarına bağımlı.

### ai-video-gen  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** Metinden ve görselden AI video üretimini fal.ai, HeyGen ve Gemini API ağ geçitleri üzerinden yönetir; Seedance 2.0'ı premium varsayılan sayar ve sağlayıcıyı video_selector ile seçmeyi şart koşar.
- **Ne zaman:** AI video klibi üretilecek ve hangi model/ağ geçidinin kullanılacağına karar verilecekse; model seçiminin giriş noktası. · **Ne zaman değil:** Belirli bir modelin ayrıntılı prompt rehberi gerektiğinde (seedance-2-0, gemini-omni, kling-official).
- **Teknoloji:** fal-ai, heygen, google-gemini, api-anahtari · **Paketler:** FAL_KEY|HEYGEN_API_KEY|GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam — Araca özel sürümler mevcut: codex -> kurulumda her araca kendi sürümü konur
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → birincil · **Roller:** ai-medya-uretici · **Globalde:** claude:farkli
- **Boyut:** 11 KB (SKILL.md 11.0 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. İyi yönlendirici; video_selector önerisi OpenMontage'a bağlı. Sıralama bilgileri tarihe duyarlı.

### atlas-cloud  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Atlas Cloud ağ geçidiyle tek anahtarla Seedance 2.5/2.0, Gemini Omni, MiniMax H3, Seedream 5, GPT Image 2, Nano Banana 2 görsel/video üretimi ve düzenlemesi; her ücretli çağrı öncesi katalog ve maliyet kontrolünü zorunlu tutar.
- **Ne zaman:** Kullanıcı Atlas Cloud istediğinde veya tek ATLASCLOUD_API_KEY ile çok model ailesine erişilecekse. · **Ne zaman değil:** Doğrudan sağlayıcı anahtarı varken (seedance, gemini-omni); Atlas hesabı yoksa.
- **Teknoloji:** atlas-cloud, python, api-anahtari · **Paketler:** ATLASCLOUD_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-saglayici-yonlendirme → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 5 KB (SKILL.md 4.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kesin rota/fiyat tabloları ve 'sessizce sınırlama' yasağı iyi.

### avatar-video  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** HeyGen v2 API ile avatar, ses, metin, sahne ve arka plan üzerinde tam kontrollü avatar videosu üretir; çok sahneli, şeffaf WebM ve Remotion entegrasyonu dahil.
- **Ne zaman:** Belirli avatar/sesle birebir metin okutulacak, sahne bazlı kontrol gerekecek veya toplu üretim yapılacaksa. · **Ne zaman değil:** Tek istemden hızlı video (create-video); avatar gerekmiyorsa.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → tamamlayıcı · **Roller:** ai-medya-uretici, video-kompozisyon · **Globalde:** claude:ayni
- **Boyut:** 177 KB (SKILL.md 6.5 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Resmi ve iyi bölümlenmiş referanslar.

### bfl-api  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** Black Forest Labs FLUX API entegrasyon rehberi: uç noktalar, bölgesel sunucular, fiyatlar, asenkron sorgulama, hız sınırı, hata yönetimi ve webhook örnekleri (Python/TypeScript).
- **Ne zaman:** FLUX'u bir uygulamaya veya üretim hattına API ile bağlarken. · **Ne zaman değil:** Sadece iyi prompt yazmak gerekiyorsa (flux-best-practices).
- **Teknoloji:** bfl-flux, python, typescript, api-anahtari · **Paketler:** BFL_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-uretimi → tamamlayıcı · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 79 KB (SKILL.md 9.7 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi BFL skill'i; sonuç URL'lerinin 10 dk'da düştüğü gibi kritik uyarılar var.

### comfyui  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** OpenMontage'da ComfyUI iş akışlarıyla (comfyui_image/video/music) yerel üretim: sunucu sözleşmesi, API formatlı iş akışı, output_node seçimi, eksik model kurulumu, düşük VRAM seçenekleri ve ücretli Partner Node ayrımı.
- **Ne zaman:** Yerel GPU'da açık ağırlıklı modellerle (Wan, LTXV, MiniMax H3 local) üretim yapılacak veya topluluk iş akışı içe alınacaksa. · **Ne zaman değil:** GPU yoksa; barındırılan API yeterliyse.
- **Teknoloji:** comfyui, python, gpu · **Paketler:** ComfyUI sunucusu, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** yerel-uretim-comfyui → birincil · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 8 KB (SKILL.md 7.9 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 'Partner Node yerel/ücretsiz değildir' gibi dürüst ayrımlar değerli; GPU/VRAM gerektirir.

### faceswap  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** HeyGen FaceswapNode iş akışıyla kaynak görseldeki yüzü hedef videoya aktarır; iş gönderme, durum sorgulama ve TypeScript/Python örnekleri içerir.
- **Ne zaman:** Kişinin açık izniyle kişiselleştirilmiş video veya kendi yüzünü sahneye yerleştirme gerektiğinde. · **Ne zaman değil:** Rızası olmayan kişilerle, yanıltıcı/deepfake amaçlı içerikte.
- **Teknoloji:** heygen, api-anahtari, rest-api · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** yuz-degistirme → birincil · **Globalde:** claude:ayni
- **Boyut:** 7 KB (SKILL.md 7.1 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: SADECE ARŞİV. Teknik olarak düzgün; rıza ve kötüye kullanım riski nedeniyle rollere eklenmedi, açık istekle --skill ile kurulur.

### fal-3d  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate 3D models from text or images via fal.ai. Useful for game assets, AR previews, product mockups, and concept sculpting.
- **Teknoloji:** webgl _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-generate  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate images and videos using fal.ai AI models. Production-grade catalogue covering Flux, SDXL, ideogram, and other community-hosted endpoints.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-image-edit  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** AI-powered image editing with style transfer, background removal, object removal, and inpainting via fal.ai hosted models.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-kling-o3  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate images and videos with Kling O3 — Kling's most powerful model family — via fal.ai.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-lip-sync  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Create talking head videos and lip sync audio to video via fal.ai. Useful for explainer avatars, multilingual dubbing previews, and social cuts.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-realtime  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Real-time and streaming AI image generation via fal.ai. Suited for moodboard exploration, draft variations, and rapid creative iteration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-restore  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Restore and fix image quality — deblur, denoise, fix faces, and restore old documents using fal.ai's hosted restoration models.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-train  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Train custom AI models (LoRA) on fal.ai for personalized image generation tailored to a brand, character, or style.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-tryon  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Virtual try-on — see how clothes look on a person via fal.ai's hosted try-on models. Useful for ecommerce, lookbooks, and styling experiments.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-upscale  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Upscale and enhance image and video resolution using AI super-resolution models hosted on fal.ai.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-video-edit  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Edit existing videos using AI — remix style, upscale, remove background, and add audio via fal.ai's hosted video models.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### fal-vision  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Analyze images — segment objects, detect, run OCR, describe, and answer visual questions via fal.ai vision models.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### flux-best-practices  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** BFL FLUX görsel modelleri için kapsamlı prompt rehberi: prompt yapısı, model seçimi (klein/pro/max/flex), T2I, I2I, JSON yapılandırılmış prompt, HEX renk, tipografi ve çoklu referans düzenleme kuralları.
- **Ne zaman:** FLUX ile görsel üretirken veya düzenlerken prompt kalitesini artırmak için. · **Ne zaman değil:** Başka görsel modellerinde (GPT Image, Seedream) — kurallar FLUX'a özgü; API kurulumu için bfl-api.
- **Teknoloji:** bfl-flux
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-gorsel-uretimi → birincil · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 122 KB (SKILL.md 4.2 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. Resmi BFL rehberi, kural dosyalarına iyi bölünmüş.

### gemini-omni  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** Google Gemini Omni Flash ile 3-10 sn 720p sesli video üretimi ve aynı klibi doğal dille durum korumalı (interaction_id) düzenleme; referans görsel etiketleri, zaman kodlu vuruşlar ve rota sınırlamaları.
- **Ne zaman:** Üretilen bir klibi yeniden üretmeden adım adım düzeltmek veya mevcut videoyu düzenlemek gerektiğinde. · **Ne zaman değil:** Tek seferlik sinematik kahraman klip (seedance-2-0), 10 sn'den uzun veya 720p üstü çıktı, İngilizce dışı anlatım.
- **Teknoloji:** google-gemini, api-anahtari · **Paketler:** GEMINI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Ne zaman seçilip seçilmeyeceği tablosu çok net; benzersiz düzenleme yeteneği.

### gif-sticker-maker  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Convert photos into animated GIF stickers in Funko Pop / Pop Mart style via the MiniMax API. Useful for personalized chat stickers and avatar packs.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### grok-media  ·  calesthio/OpenMontage @ c806645  ·  puan 89 (A)

- **Ne yapar:** xAI Grok görsel ve video üretimi rehberi: kimlik doğrulama, uç noktalar, görsel düzenleme/birleştirme, referans görselli video, asenkron sorgulama, fiyatlar ve Grok'a özgü prompt önerileri.
- **Ne zaman:** XAI_API_KEY ile kısa referans koşullu video veya çok kaynaklı görsel birleştirme gerektiğinde. · **Ne zaman değil:** Uzun klip, deterministik seed veya yüksek çözünürlük gerektiğinde.
- **Teknoloji:** xai-grok, api-anahtari · **Paketler:** XAI_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 4 KB (SKILL.md 3.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa ve doğru; derinliği diğer model rehberlerinden az.

### heygen  ·  calesthio/OpenMontage @ c806645  ·  puan 81 (A)

- **Ne yapar:** [KULLANIMDAN KALKMIŞ] HeyGen Video Agent ve v2 avatar iş akışlarını birleştiren eski skill; yerini create-video ve avatar-video aldı, geriye uyumluluk için duruyor.
- **Ne zaman:** Sadece eski bir projede 'heygen' adıyla başvuru varsa. · **Ne zaman değil:** Yeni işlerde — create-video veya avatar-video kullan.
- **Teknoloji:** heygen, api-anahtari · **Paketler:** HEYGEN_API_KEY
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** heygen-video → alternatif · **Globalde:** claude:ayni
- **Boyut:** 225 KB (SKILL.md 5.7 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Kaynak skill kendini deprecated ilan ediyor; ai-medya-uretici rolünden çıkarıldı.

### imagegen  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate and edit images using OpenAI's Image API for project assets — UI mockups, icons, illustrations, social cards, and visual references.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### imagen  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### kling-official  ·  calesthio/OpenMontage @ c806645  ·  puan 96 (A)

- **Ne yapar:** Kling resmi doğrudan API'si (KLING_API_KEY) için OpenMontage sağlayıcı kuralları: fal.ai Kling'den ayrımı, klasik/turbo görev protokolleri, Omni referans yapıları, TTS/avatar/lip-sync sınırları.
- **Ne zaman:** Resmi Kling API'si ile video/görsel/avatar üretilecekse. · **Ne zaman değil:** fal.ai üzerinden Kling (ai-video-gen); OpenMontage kullanılmıyorsa sağlayıcı sarmalayıcıları yok.
- **Teknoloji:** kling, python, api-anahtari · **Paketler:** KLING_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 9 KB (SKILL.md 9.2 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Ayrıştırıcıların karıştırılmaması gibi titiz kurallar; ağırlıkla geliştirici/entegrasyon odaklı.

### ltx2  ·  calesthio/OpenMontage @ c806645  ·  puan 81 (A)

- **Ne yapar:** LTX-2.3 22B modeliyle Modal (A100) üzerinde ~5 sn metinden/görselden video üretir; kare sayısı kuralı, çözünürlükler ve sinematik prompt rehberi içerir.
- **Ne zaman:** Kendi Modal uç noktası kurulu, ucuz b-roll/arka plan klibi üretilecekse. · **Ne zaman değil:** OpenMontage kurulumunda (tools/ltx2.py yok); uç nokta yoksa.
- **Teknoloji:** ltx, modal, python · **Paketler:** MODAL_LTX2_ENDPOINT_URL, claude-code-video-toolkit
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Globalde:** claude:ayni
- **Boyut:** 7 KB (SKILL.md 7.0 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Başvurduğu tools/ltx2.py OpenMontage c806645'te yok (claude-code-video-toolkit'ten); prompt rehberi yine de faydalı. LTX-2.5 için provider-model-refresh'e bak.

### minimax-h3  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** MiniMax H3 (Hailuo 3.0) videosunu resmi API, fal.ai, Runway, ComfyUI Partner Node veya yerel açık ağırlıklarla üretir; rotalar arası model kimliği farklarını ve ilk/son kare, referans koşullu üretimi açıklar.
- **Ne zaman:** 4-15 sn 2K klip, ilk/son kare animasyonu veya ses/görsel referanslı video gerektiğinde. · **Ne zaman değil:** Uzun tek üretim (seedance-2-5); bu sağlayıcılardan hiçbirine erişim yoksa.
- **Teknoloji:** minimax, comfyui, api-anahtari · **Paketler:** MINIMAX_API_KEY|FAL_KEY|RUNWAY_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 2 KB (SKILL.md 2.3 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: ALTERNATİF. Kısa ama net; 'yalnız açık ağırlık rotası yereldir' uyarısı doğru.

### nanobanana-ppt  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** AI-powered PPT generation with document analysis and styled images via the NanoBanana stack. Combines image generation with structured deck output.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### pixelbin-media  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate and edit images and videos with an 85+ API portfolio and build visually appealing website pages via Pixelbin.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### provider-model-refresh  ·  calesthio/OpenMontage @ c806645  ·  puan 97 (A)

- **Ne yapar:** Eylül 2026 görsel, video, konuşma ve Avatar V adaptörleri (GPT Image 2.5, Gemini 3 Pro Image, Ideogram 4.5, Wan 3.0, LTX-2.5, Eleven v4, Lyria 3.5…) için kesin model/host sözleşmeleri; mevcut olmayan modelin sessizce değiştirilmemesini şart koşar.
- **Ne zaman:** OpenMontage'ın yeni nesil adaptörleriyle belirli bir model/host zorunlu tutularak üretim yapılacaksa. · **Ne zaman değil:** OpenMontage dışında; genel model seçimi için ai-video-gen.
- **Teknoloji:** openmontage, python, api-anahtari · **Paketler:** OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** medya-saglayici-yonlendirme → birincil · **Roller:** ai-medya-uretici
- **Boyut:** 5 KB (SKILL.md 5.4 KB, yük kucuk) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Güncel model kataloğu ve katı yönlendirme kuralları; tamamen OpenMontage registry'sine bağlı.

### replicate  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Discover, compare, and run AI models using Replicate's API. Strong fit for image, audio, and video generation pipelines that swap models frequently.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.2 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### seedance-2-0  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** ByteDance Seedance 2.0 için yetkili prompt ve parametre rehberi: tek geçişte senkron ses, tek üretimde çoklu çekim, yönetmen düzeyi kamera kontrolü, alıntılı diyalogdan dudak senkronu ve 12 varlıklı referans koşullama; ağ geçidi rotaları.
- **Ne zaman:** Fragman, teaser, sinematik kahraman klip veya karakter tutarlılığı gereken premium AI video işlerinde. · **Ne zaman değil:** Sıkı bütçe (fast varyantı veya LTX), 15 sn'den uzun tek üretim (seedance-2-5), klip düzenleme (gemini-omni).
- **Teknoloji:** seedance, fal-ai, api-anahtari · **Paketler:** FAL_KEY|REPLICATE_API_TOKEN|HEYGEN_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → tamamlayıcı · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 17 KB (SKILL.md 17.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT. OpenMontage'ın premium varsayılan modeli; en ayrıntılı model rehberi. Elo/sıralama iddiaları tarihe duyarlı.

### seedance-2-5  ·  calesthio/OpenMontage @ c806645  ·  puan 100 (A)

- **Ne yapar:** Seedance 2.5 ile 4-30 sn sinematik video: fal.ai, Volcengine Ark, Runway, ComfyUI rotaları; bölümlü prompt sözleşmesi, 'Hard cut' çoklu çekim, kesmeler arası adlı kilitler, karakter sayfası yöntemi ve yineleme disiplini.
- **Ne zaman:** 15 sn'den uzun tek üretim, büyük referans seti (30 görsel/10 video/10 ses) veya çekimler arası süreklilik gerektiğinde. · **Ne zaman değil:** Kısa tek aksiyonlu sahnelerde (2.0 yeterli); 1080p gerekiyorsa (desteklenen rotalar 720p).
- **Teknoloji:** seedance, fal-ai, api-anahtari · **Paketler:** FAL_KEY|RUNWAY_API_KEY, OpenMontage kurulumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** calesthio (kisi, ★73510, son güncelleme 2026-10-28, lisans AGPL-3.0)
- **Durum:** tercih · **Örtüşme:** ai-video-uretimi → alternatif · **Roller:** ai-medya-uretici · **Globalde:** claude:ayni
- **Boyut:** 23 KB (SKILL.md 12.4 KB, yük orta) · **Bağımlılık:** OpenMontage kurulumu gerekir (~/.openmontage). 'python tools/...', 'pipeline_defs/...' komutları OpenMontage repo kökünden ve onun venv python'u ile çalışır.
- **İnceleme:** incelendi · kalite 5/5 — Karar: ALTERNATİF. Prompt sözleşmesi çok güçlü; uzun/çok çekimli işlerde 2.0 yerine seçilir.

### sora  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Generate, remix, and manage short video clips via OpenAI's Sora API. Useful for cinematic shots, b-roll, and rapid concept video iteration.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### venice-image-edit  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Image edits, upscaling, and background removal via the Venice.ai API.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### venice-image-generate  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Image generation endpoints and available styles via the Venice.ai API.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.

### venice-video  ·  nexu-io/open-design @ e03d5c2  ·  puan 65 (B)

- **Ne yapar:** Video generation and transcription workflows via the Venice.ai API.
- **Teknoloji:** - _(otomatik tespit)_
- **Claude / Codex:** tam / tam
- **Geliştirici:** nexu-io (kurum, ★105063, son güncelleme 2026-10-31, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 1 KB (SKILL.md 1.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Sadece yönlendirme: talimat yok, asıl skill upstream repoda (SKILL.md 'Source' bölümüne bak). Kurmak yerine upstream'i ya da kütüphanedeki tam sürümü kullan.
