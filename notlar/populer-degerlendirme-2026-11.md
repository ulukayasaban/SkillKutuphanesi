# Popüler skill taraması — değerlendirme (2026-11-04)

Tarama: `araclar/populer-tarama.py` (15 REST sorgusu, son 120 günde push, ★150+) → 373 aday, **320'sinde SKILL.md var**
(`notlar/populer-skiller.md`). Burada o listeden elenmiş öneriler var. **Hiçbiri eklenmedi**; ekleme kararı senin
(`rehber/03-yeni-skill-ekleme.md`: çakışma + ücret kontrolü, onay). Reddettiklerini kaydet:
`python3 araclar/populer-tarama.py --karar owner/ad reddedildi "neden"` (konu-takip ile aynı defter, bir daha çıkmaz).

## Bu oturumda yapılamayanlar
| İş | Durum | Neden | Nerede yapılır |
|---|---|---|---|
| "Yapay Zeka Skillleri" yıldız listesi ↔ kütüphane karşılaştırması (`github-skill-listesi.py`) | **yapılamadı** | GitHub GraphQL bulut oturumundan kapalı; liste için REST uç noktası yok, github.com HTML sayfası proxy'den 403 | Kendi bilgisayarında: `python3 araclar/github-skill-listesi.py` |
| GitHub Trending taraması (`github-trend.py`) | **yapılamadı** | github.com/trending proxy'den geçmiyor. Araç artık ilk sayfada durur (eskiden 15 sayfa × 3 deneme bekliyordu) | Kendi bilgisayarında: `python3 araclar/github-trend.py --aday` |
| Konu takibi (`konu-takip.py`) | ✅ yenilendi | — | e-ticaret 32 odaklı aday, mobil 71 (`notlar/konu-takip.md`) |
| Popüler tarama (yeni) | ✅ | REST araması çalışıyor | `notlar/populer-skiller.md` |

## A) Kütüphaneye aday skill repoları (öncelik sırasıyla)
★ ve SKILL.md sayısı taramadan; lisans GitHub'ın bildirdiği. "Çakışma" sütunu kütüphanedeki benzerlerle ad/iş örtüşmesi (03'teki zorunlu kontrol).

| # | Repo | ★ | SKILL.md | Lisans | Hedef kategori | Neden / dikkat | Çakışma kontrolü |
|---|---|---|---|---|---|---|---|
| 1 | `mattpocock/skills` | 313k | 40 | MIT | b-yazilim-gelistirme/01–03 | Tanınmış eğitmen (Total TypeScript); mühendislik disiplin skilleri; en çok yıldızlanan skill reposu | `obra/superpowers`, `addyosmani/agent-skills` ile iş örtüşmesi olası (TDD, debugging, planning) |
| 2 | `coreyhaines31/marketingskills` | 58k | 59 | MIT | h-is-alanlari (pazarlama) | CRO, copywriting, SEO, analitik, growth; Etsy/e-ticaret profiline doğrudan katkı | nexscope `ecommerce-marketing-*`, `conversion-rate-optimization` ile ad değil iş örtüşmesi |
| 3 | `AgriciDaniel/claude-seo` | 27k | 35 | MIT | h-is-alanlari / b-yazilim | 26 alt skill + 19 agent; teknik SEO, GEO, e-ticaret SEO. Aynı yazarın `claude-ads` (11k, 34, 12 reklam platformu) ve `claude-obsidian` (16k, 16) | `etsy-seo`, `ecommerce-seo`, `shopify-seo`, `woocommerce-seo` ile iş örtüşmesi; `claude-ads` ↔ `ebay-advertising`, `walmart-advertising-strategy` |
| 4 | `kepano/obsidian-skills` | 51k | 6 | MIT | c-dokuman-icerik/04 | Obsidian'ın kendi CEO'sunun resmî skilleri (Agent Skills spesifikasyonuna uygun) | Kütüphanedeki `obsidian-markdown`, `obsidian-bases`, `add-frontmatter` **`heyitsnoah/claudesidian`**'dan geliyor; aynı adlar burada da olabilir → `durum: alternatif`/öncelik kararı gerekir |
| 5 | `google/elephant-goldfish-model` | 12k | 14 | Apache-2.0 | b-yazilim-gelistirme/01-planlama | Google'ın resmî spec yazma/inceleme (deep-context + zero-context subagent) yöntemi | `brainstorming`, `writing-plans` (superpowers) ile yöntem örtüşmesi |
| 6 | `openai/plugins` | 7.7k | **488** | yok (GitHub bildirmiyor) | d-ai-otomasyon + çok kategori | **`openai/skills` kullanımdan kaldırıldı**, resmî Codex kaynağı artık bu. `anthropics/claude-plugins-official`'ın Codex karşılığı. Önce lisans dosyasına bak | 488 SKILL.md: çoğu başka repoların kopyası olabilir → `kapsam-denetimi` kopya kontrolü; T2 (seçmeli) olarak al |
| 7 | `github/awesome-copilot` | 41k | 475 | MIT | çok kategori | GitHub'ın resmî topluluk kataloğu; kalite karışık | Büyük katalog: seçmeli (T2), tamamı değil |
| 8 | `Vincentwei1021/video-shotcraft` | 17k | 1 | Apache-2.0 | g-video-ses-medya/01 | Remotion ile ürün tanıtım videosu, 150 hazır "shot"; Remotion skilleriyle birlikte çalışır | `remotion-*` kardeş; çakışma değil tamamlayıcı |
| 9 | `dreammis/social-auto-upload` | 16k | 18 | MIT | g-video-ses-medya | YouTube/TikTok/Douyin/Bilibili'ye video yükleme CLI + skiller. YouTube kanalı işine uygun. Çince; tarayıcı oturumu gerektirir → **ücret/erişim sınıfı** bakılmalı | `youtube-downloader`, `upload` (lemo-wake) ile ad örtüşmesi yok |
| 10 | `krillinai/OpenCreator` | 14k | 15 | Apache-2.0 | g-video-ses-medya/02 | Video çeviri + dublaj (120 dil); kütüphanede dublaj skill'i yok | Uygulama + skill karışık; **kısmen ücretli** olabilir (LLM/TTS API) |
| 11 | `blader/humanizer` | 65k | 1 | MIT | c-dokuman-icerik/03 | AI yazı izlerini temizleme; tek skill, çok popüler | Kütüphanede yok |
| 12 | `cathrynlavery/diagram-design` | 65k | 1 | MIT | c-dokuman-icerik/02 | Editoryal diyagram tasarımı; çok araçlı | `documentation-and-adrs` ile değil, diyagram kategorisiyle tamamlayıcı |
| 13 | `Nutlope/hallmark` | 48k | 1 | MIT | a-tasarim-onyuz/01 | "Anti-AI-slop" tasarım | `pbakaus/impeccable`, `Leonxlnx/taste-skill`, `design-taste-frontend` ile **doğrudan iş örtüşmesi** → örtüşme grubuna `alternatif` |
| 14 | `JuliusBrussee/caveman` | 117k | 28 | Apache-2.0 | d-ai-otomasyon/02 | Token tasarrufu için kısa çıktı skill'i (+ proxy uygulaması) | Yalnız skill kısmı alınır (`konum_haric`) |
| 15 | `Orchestra-Research/AI-Research-SKILLs` (14k, 98, MIT) · `wanshuiyin/Auto-claude-code-research-in-sleep` (19k, 199, MIT) | | | | i-bilim-muhendislik | ML araştırma skilleri | `K-Dense-AI/scientific-agent-skills` (177) ile örtüşme büyük; önce karşılaştır |
| 16 | `zubair-trabzada/geo-seo-claude` (12k, 16, MIT) · `Ryze-AI-Adgent/open-seo-mcp-skills` (9k, 8, MIT) | | | | SEO | 3'ün alternatifleri; 3 alınırsa bunlar `alternatif` | — |

**Önerim:** 1, 2, 3, 4, 6 (lisans netleşirse), 8, 9'u öncelikli incele; 11–14 tek skill oldukları için ucuz; 7 ve 15'i ihtiyaç çıkınca.

## B) Sürece eklenebilecek araçlar (skill değil, denetim)
| Araç | Ne yapar | Durum | Öneri |
|---|---|---|---|
| `NVIDIA/SkillSpector` (24k★, Apache-2.0) | Skill'de zararlı desen/güvenlik riski tarar (prompt injection, gizli komut, veri sızdırma); NVIDIA Verified Skills hattının parçası | PyPI'da yok; Docker (`docker run --rm -v "$PWD:/scan" skillspector scan ./skill --no-llm`) ya da kaynaktan | `rehber/03` adım "yeni kaynak eklerken": `kaynak-cek.py` sonrası `.gecici/` altındaki yeni klasörleri tara; bulgu varsa kaynak eklenmez. Ayda bir tüm arşiv. |
| `agent-sh/agnix` (npm `agnix@0.61`, 758 kural) | SKILL.md/CLAUDE.md/hooks/MCP yapılandırmalarını lint eder, otomatik düzeltme | `npx agnix <klasör>` (bu oturumda dış kod çalıştırma izni verilmediği için denenmedi) | `skill-calistir.py --lint` seçeneği: bulguları TEST_RAPORU'na UYARI olarak ekle; HATA sayma (kurallar bizim onarımlarımızla çakışabilir) |
| `populer-tarama.py` (bu PR) | REST aramasıyla popüler skill repoları + SKILL.md sayımı | eklendi, aylık güncellemede çalışır | — |
| Kullanımdan kaldırılma uyarısı | `openai/skills` README'si "deprecated" diyor; `gelistirici-bilgisi.py` sadece GitHub'ın `archived` bayrağına bakıyor | önerildi | `gelistirici-bilgisi.py`: README ilk 40 satırda `deprecated|archived|moved to|no longer maintained` → `kaynak_notu`, `dogrula.py` UYARI |

## C) Bilerek önerilmeyenler
- **Uygulama/harness, skill kütüphanesi değil** (SKILL.md'leri kendi iç kullanımı için): `openclaw/openclaw`, `NousResearch/hermes-agent`,
  `affaan-m/ECC` (1026 SKILL.md ama harness), `ruvnet/ruflo` (380), `firecrawl/firecrawl`, `Significant-Gravitas/AutoGPT`, `browser-use/browser-use`,
  `paperclipai/paperclip`, `CherryHQ/cherry-studio`, `LibreChat-AI/LibreChat`, `bytedance/deer-flow`, `thedotmack/claude-mem`, `garrytan/gstack`
  (144 SKILL.md; "sanal mühendislik ekibi" iş akışı — `superpowers` ile çakışır, istersen `izle`).
- **Toplayıcı kataloglar** (başka repoların kopyaları; kütüphane politikası orijinal kaynak): `alirezarezvani/claude-skills` (511),
  `composio-community/awesome-codex-skills` (935, lisans yok), `anbeime/skill` (95, lisans yok), `sickn33/agentic-awesome-skills`,
  `VoltAgent/awesome-openclaw-skills`. `mukul975/Anthropic-Cybersecurity-Skills` (978): adı Anthropic'i çağrıştırıyor ama resmî değil.
- **Lisans sorunlu**: `op7418/guizang-ppt-skill` (AGPL-3.0), `koala73/worldmonitor` (AGPL), `openai/skills` (deprecated, lisans yok).
- **Güvenlik/ofansif**: `zhaoxuya520/reverse-skill` (89), `SnailSploit/Claude-Red` (76) — kütüphanenin kapsamı dışında.
