# Skill Rehberi (Türkçe)

Bu kütüphanedeki **2930 skill'in** ne işe yaradığı ve nasıl çağrıldığı. Kategori sayfaları otomatik üretilir:
`python3 araclar/skill-readme.py`. Test sonuçları: [TEST_RAPORU.md](TEST_RAPORU.md) · kurulum ve araçlar: [README.md](README.md).

## Skill nedir?
Skill, bir agent'a belirli bir işi nasıl yapacağını öğreten klasördür: `SKILL.md` (talimatlar) ve gerekirse betikler,
şablonlar ve referans dosyaları. Agent başta sadece her skill'in **adını ve açıklamasını** (`description`) görür; iş buna
uyunca skill'in tamamını yükler. Bu yüzden skill'in "doğru durumda tetiklenmesi" açıklamasına bağlıdır.

## Nasıl kurulur?
Skiller globale değil, **sadece seçtiğin projeye** kurulur:
```bash
python3 araclar/skill-ekle.py --oner "etsy mağazası seo"                     # ne kullanmalıyım?
python3 araclar/skill-ekle.py ~/Projeler/magaza --skill etsy-seller-guide --kuru   # ön kontrol raporu
python3 araclar/skill-ekle.py ~/Projeler/magaza --skill etsy-seller-guide --evet   # kur
```
Claude Code `.claude/skills/<ad>/`, Codex `.agents/skills/<ad>/` klasöründen okur; araç ikisine de kurar.

## Nasıl çağrılır?
| Yol | Claude Code | Codex |
|---|---|---|
| **Otomatik** (varsayılan) | İsteğin skill'in açıklamasına uyar ("Etsy listing başlıklarımı iyileştir"); agent skill'i kendisi yükler | Aynı |
| **Elle** | `/<skill-adı> [argümanlar]` yaz (ör. `/etsy-seller-guide`) | İstemde `$<skill-adı>` ile an |
| **Adını söyleyerek** | "etsy-seller-guide skill'ini kullanarak …" | Aynı |
| **Agent rolüyle** | Rol kurulduysa (`--rol`) `.claude/agents/<rol>.md` skilleri önyükler | `.codex/agents/<rol>.toml` |

- Tablolardaki **"Sadece elle"** skiller (`disable-model-invocation: true`) otomatik tetiklenmez; adlarıyla çağrılır.
- **"Menüde görünmez"** skiller (`user-invocable: false`) `/` menüsünde çıkmaz; agent gerekince kendisi yükler.
- Argüman alan skillerde `/ad <argüman>` biçimi tabloda yazar (ör. `/design-handoff <Figma URL>`).
- **Claude hesabında aynı adlı skill varsa** (ör. claude.ai'deki `docx`, `pdf`, `xlsx`, `pptx`): Claude Code onu
  `anthropic-skills:<ad>` olarak yükler ve agent çoğu zaman onu seçer. `skill-ekle.py` kurulumda hesaptakini o projede
  gizler (`.claude/settings.json` → `skillOverrides`), böylece kütüphane sürümü kullanılır. Ön kontrol `hesap-cakismasi` der.

## Tablolar nasıl okunur?
- **Ne yapar / Ne zaman:** elle incelenmiş 448 skill'de inceleme notu; 2120 skill'de açıklamanın
  otomatik Türkçe çevirisi (`aciklama-tr.json`, `araclar/ceviri-tr.py`); 362 skill'de henüz İngilizce.
- **Puan:** 0–100 otomatik değerlendirme ve derece (A–D): kaynağın bakımı, GitHub güveni, yapı, inceleme notu.
- **Not:** alternatif sürüm, ücretli/kısmen ücretli (`notlar/ucretli-skiller.md`), Codex uyumu, 🔥trend.
- **Gizli katalog:** entegrasyon kataloğu (tek bir uygulama için hazır otomasyon) ve repo-içi (bir projenin kendi
  geliştiricilerine yönelik) skiller; öneri listesinde varsayılan olarak çıkmazlar ama `--skill <id>` ile kurulabilir.

## Dizin

### Tasarım ve Ön Yüz (273)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-ui-ux-tasarim-dili](skiller/a-tasarim-onyuz/01-ui-ux-tasarim-dili.md) | Görsel dil, layout, tipografi, renk, 'AI görünümünden kaçış', tasarım denetimi | 39 |
| [02-tasarim-sistemi-marka](skiller/a-tasarim-onyuz/02-tasarim-sistemi-marka.md) | Design token, tema, marka kimliği, banner/logo | 12 |
| [03-animasyon-motion](skiller/a-tasarim-onyuz/03-animasyon-motion.md) | GSAP, Motion/Framer, anime.js, Lottie, Rive, mikro-etkileşim | 32 |
| [04-scroll-deneyimi](skiller/a-tasarim-onyuz/04-scroll-deneyimi.md) | Scroll hikâyesi, smooth scroll, ScrollTrigger, sayfa geçişleri | 7 |
| [05-3d-webgl](skiller/a-tasarim-onyuz/05-3d-webgl.md) | Three.js, React Three Fiber, Babylon, PlayCanvas, Spline, WebXR, shader | 33 |
| [06-oyun-2d-grafik](skiller/a-tasarim-onyuz/06-oyun-2d-grafik.md) | Oyun geliştirme, PixiJS, 2D grafik | 117 |
| [07-gorsel-sanat-sunum](skiller/a-tasarim-onyuz/07-gorsel-sanat-sunum.md) | Poster/canvas tasarımı, generative art, slayt, GIF | 23 |
| [08-onyuz-test-kalite](skiller/a-tasarim-onyuz/08-onyuz-test-kalite.md) | Tarayıcı testi, görsel QA, erişilebilirlik, React kod sağlığı | 10 |

### Yazılım Geliştirme (567)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-planlama-metodoloji](skiller/b-yazilim-gelistirme/01-planlama-metodoloji.md) | Fikir geliştirme, spec, plan yazma, görev bölme, uygulama disiplini | 80 |
| [02-kod-kalitesi-review](skiller/b-yazilim-gelistirme/02-kod-kalitesi-review.md) | Code review, sadeleştirme, temiz kod | 19 |
| [03-test-hata-ayiklama](skiller/b-yazilim-gelistirme/03-test-hata-ayiklama.md) | TDD, hata ayıklama, doğrulama | 11 |
| [04-mimari-api-veritabani](skiller/b-yazilim-gelistirme/04-mimari-api-veritabani.md) | Mimari, API/arayüz tasarımı, veritabanı, backend | 61 |
| [05-git-pr-surum](skiller/b-yazilim-gelistirme/05-git-pr-surum.md) | Git, worktree, PR, sürüm/release, changelog | 9 |
| [06-devops-guvenlik-performans](skiller/b-yazilim-gelistirme/06-devops-guvenlik-performans.md) | CI/CD, deploy, güvenlik, gözlemlenebilirlik, performans | 163 |
| [07-framework-ozel](skiller/b-yazilim-gelistirme/07-framework-ozel.md) | Belirli framework/araç rehberleri (Next.js, Playwright CLI, Claude Code plugin geliştirme) | 19 |
| [08-mobil-uygulama](skiller/b-yazilim-gelistirme/08-mobil-uygulama.md) | Android (Jetpack Compose, Play), Expo / React Native, iOS; mağaza yayını, mobil performans | 205 |

### Doküman ve İçerik (106)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-ofis-dokumanlari](skiller/c-dokuman-icerik/01-ofis-dokumanlari.md) | Word, Excel, PowerPoint, PDF üretme/düzenleme | 8 |
| [02-diyagram-dokumantasyon](skiller/c-dokuman-icerik/02-diyagram-dokumantasyon.md) | Diyagram, teknik dokümantasyon, ADR, ortak yazım | 11 |
| [03-yazi-iletisim-icerik](skiller/c-dokuman-icerik/03-yazi-iletisim-icerik.md) | Yazı, iletişim, pazarlama/içerik, kariyer | 47 |
| [04-not-alma-bilgi-yonetimi](skiller/c-dokuman-icerik/04-not-alma-bilgi-yonetimi.md) | Obsidian, günlük/haftalık not, bilgi yönetimi, dosya düzeni | 40 |

### AI ve Otomasyon (160)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-claude-api-mcp](skiller/d-ai-otomasyon/01-claude-api-mcp.md) | Claude API, MCP sunucusu, model geçişi | 38 |
| [02-agent-orkestrasyon](skiller/d-ai-otomasyon/02-agent-orkestrasyon.md) | Alt-agent, paralel agent, bağlam mühendisliği, agent davranış modları | 59 |
| [03-web-arastirma-veri](skiller/d-ai-otomasyon/03-web-arastirma-veri.md) | Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma | 11 |
| [04-skill-plugin-yazimi](skiller/d-ai-otomasyon/04-skill-plugin-yazimi.md) | Skill yazma, plugin/hook/komut geliştirme | 52 |

### Video, Ses ve AI Medya Üretimi (208)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-video-uretim-montaj](skiller/g-video-ses-medya/01-video-uretim-montaj.md) | Video kurgu, HyperFrames/Remotion kompozisyon, ekran kaydı, video indirme/çeviri/analiz, FFmpeg | 119 |
| [02-ses-muzik-konusma](skiller/g-video-ses-medya/02-ses-muzik-konusma.md) | Seslendirme (TTS), konuşma tanıma (STT), müzik ve ses efekti üretimi | 26 |
| [03-ai-gorsel-video-modelleri](skiller/g-video-ses-medya/03-ai-gorsel-video-modelleri.md) | AI görsel/video model sağlayıcıları (Kling, Seedance, Flux, HeyGen, ComfyUI…), API anahtarı kurulumu | 27 |
| [04-motion-graphics-karakter](skiller/g-video-ses-medya/04-motion-graphics-karakter.md) | Motion graphics, Manim, karakter animasyonu/rig, görsel stil | 36 |

### Entegrasyon Kataloğu (varsayılan listede gizli) (1)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-uygulama-entegrasyonlari](skiller/e-entegrasyon-katalogu/01-uygulama-entegrasyonlari.md) (gizli katalog) | Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Composio API anahtarı gerekir | 1 |

### Repo-İçi Geliştirici Skilleri (varsayılan listede gizli) (122)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-repo-gelistirici-skilleri](skiller/f-repo-ici/01-repo-gelistirici-skilleri.md) (gizli katalog) | Next.js, React, Playwright, Lighthouse, Motion repolarına KATKI yapanlar için iç süreç skilleri; kendi projelerinde nad… | 122 |

### İş Alanları (Bilgi Çalışanı) (1110)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-satis-pazarlama-musteri](skiller/h-is-alanlari/01-satis-pazarlama-musteri.md) | Satış, pazarlama, müşteri desteği, marka sesi, CRM iş akışları | 208 |
| [02-finans-hukuk-ik](skiller/h-is-alanlari/02-finans-hukuk-ik.md) | Finans/muhasebe, hukuk/sözleşme, insan kaynakları | 37 |
| [03-operasyon-urun-isletme](skiller/h-is-alanlari/03-operasyon-urun-isletme.md) | Operasyon, ürün yönetimi, küçük işletme, verimlilik, kurumsal arama | 83 |
| [04-veri-analizi-raporlama](skiller/h-is-alanlari/04-veri-analizi-raporlama.md) | İş verisi analizi, SQL, pano/rapor, öngörü | 12 |
| 05-e-ticaret-pazaryeri: [1](skiller/h-is-alanlari/05-e-ticaret-pazaryeri-1.md) · [2](skiller/h-is-alanlari/05-e-ticaret-pazaryeri-2.md) | E-ticaret ve pazaryerleri: Etsy, Amazon, Shopify, WooCommerce, eBay, TikTok Shop, Walmart — ürün/niş araştırma, listele… | 770 |

### Bilim, Araştırma ve Mühendislik (383)
| Kategori | Kapsam | Skill |
|---|---|---|
| [01-yasam-bilimleri-kimya](skiller/i-bilim-muhendislik/01-yasam-bilimleri-kimya.md) | Biyoinformatik, genomik, ilaç/kimya, klinik ve tıbbi veri, laboratuvar otomasyonu | 97 |
| [02-fizik-kuantum-malzeme](skiller/i-bilim-muhendislik/02-fizik-kuantum-malzeme.md) | Fizik, kuantum hesaplama, malzeme/astronomi, simülasyon | 19 |
| [03-veri-bilimi-ml](skiller/i-bilim-muhendislik/03-veri-bilimi-ml.md) | Bilimsel Python, istatistik, makine öğrenmesi, görselleştirme, büyük veri | 124 |
| [04-bilimsel-yazim-literatur](skiller/i-bilim-muhendislik/04-bilimsel-yazim-literatur.md) | Literatür tarama, makale/hibe yazımı, atıf, hakem değerlendirmesi, bilimsel sunum | 124 |
| [05-cad-imalat-robotik](skiller/i-bilim-muhendislik/05-cad-imalat-robotik.md) | CAD (STEP/DXF), 3D baskı/G-code, imalat (DFM), robot tanımı (URDF/SRDF) | 19 |
