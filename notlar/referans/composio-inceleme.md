# Composio Entegrasyon Kataloğu — İnceleme Raporu

> Elle yazıldı (2026-10-21, claude). Kapsam: `e-entegrasyon-katalogu/01-uygulama-entegrasyonlari`, 832 skill,
> kaynak `ComposioHQ/awesome-claude-skills` @ `be2a406` (`composio-skills/`). Gruplu liste: `KATALOG-entegrasyon.md` (katalog-uret üretir).
> Kayıt alanları `registry.json`'da: `uygulama_grubu`, `ozet_tr`, `kullanim_alani`, `kullanma`, `teknoloji`, `kalite`, `kalite_notu`, `notlar`, `inceleme`.

## Özet
- **832 skill'in 757'si iki şablondan üretilmiş metin**; yalnızca uygulama adı değişiyor. Uygulamaya özel bilgi taşımıyorlar.
- **75 skill elle yazılmış**: somut araç adları (`AHREFS_FETCH_ALL_BACKLINKS` gibi), parametre tabloları ve "Known Pitfalls" içeriyor. Asıl değer bunlarda.
- Hepsi **Rube MCP** (`https://rube.app/mcp`, Composio'nun barındırdığı MCP sunucusu) üzerinden çalışıyor. **`COMPOSIO_API_KEY` hiçbir dosyada geçmiyor**;
  768 dosya "No API keys needed" diyor. Kimlik doğrulama uygulama başına: `RUBE_MANAGE_CONNECTIONS` bir OAuth/yetkilendirme bağlantısı döndürür,
  bazı uygulamalar (Apollo, Neon, PhantomBuster…) uygulamanın kendi API anahtarını Composio'ya girmenizi ister.
- **Gmail, Slack, Notion, GitHub, HubSpot, Stripe, Jira, Linear bu katalogda YOK.** Upstream commit'teki 832 klasörün tamamı arşivlendi
  (GitHub ağacıyla doğrulandı); popüler uygulamalar bu repoda değil. En yakınlar: `slackbot-automation` (şablon), `googledrive/docs/calendar/…`,
  Stripe araçlarını kullanan `braintree-automation`.
- Codex uyumu: hepsi düz SKILL.md; MCP kurulu olan her istemcide çalışır. 92 skill'de `name` alanı standart dışı (ör. "Ahrefs Automation",
  "-21risk-automation"); kurulumda klasör adına eşitleniyor. Lisans: repo'da lisans dosyası yok ("belirtilmemiş").

## Yapı karşılaştırması (betikle)
Her SKILL.md'de uygulama adı, toolkit slug'ı, `name` ve `description` yer tutucuyla değiştirilip hash'lendi; başlık yapısı ve geçen araç adları sayıldı.

| Tür | Adet | İçerik | inceleme |
|---|---|---|---|
| **Şablon A** | 731 | Prerequisites → Setup → Tool Discovery → 3 adımlı Core Workflow (`RUBE_SEARCH_TOOLS` → `RUBE_MANAGE_CONNECTIONS` → `RUBE_MULTI_EXECUTE_TOOL`) → 6 genel pitfall → Quick Reference. 720'si normalize sonrası bayt bayt aynı; 11'i (21risk, 2chat, cal, mem, kit, exa…) yalnızca kısa adların normalizasyonu yüzünden farklı göründü, içerik aynı. | toplu-incelendi (21risk, googledrive, slackbot okundu; bigmailer, salesforce-service-cloud, googlecalendar, googlesuper hash ile birebir aynı → incelendi) |
| **Şablon B** | 26 | Alt çizgili adlar (`google_admin`, `zoho_mail`, `capsule_crm`…). A'ya ek olarak description'da kullanım anahtar kelimeleri, hata işleme, toplu işlem (`RUBE_REMOTE_WORKBENCH` + ThreadPoolExecutor) notları. **26'sının da tire'li ikizi var** (aynı toolkit, iki kayıt). | toplu-incelendi (`google_admin` tam okundu) |
| **Elle yazılmış** | 75 | Uygulamaya özel iş akışları ve araç adları (1–15 araç). Yapı: Setup → Core Workflows (4–6) → Known Pitfalls → Quick Reference. | incelendi (hepsi tek tek: açıklama, iş akışı başlıkları, araç adları, uyarılar betikle çıkarılıp okundu; 11'i baştan sona) |

Kullanılan araçlar: 758 dosya beş `RUBE_*` aracının hepsini anıyor (`SEARCH_TOOLS`, `MANAGE_CONNECTIONS`, `MULTI_EXECUTE_TOOL`, `REMOTE_WORKBENCH`, `GET_TOOL_SCHEMAS`);
elle yazılmışların çoğu yalnızca uygulama araçlarını adıyla çağırıyor. Her klasörde yalnızca `SKILL.md` (+ arşivin `KAYNAK.md`'si) var; betik, referans dosyası yok.
Boyut 1,5–8,5 KB (bağlam yükü küçük).

**Baştan sona okunan 15 temsilî skill:** şablon A: `21risk`, `googledrive`, `slackbot` · şablon B: `google_admin` · elle yazılmış: `google-admin`,
`braintree`, `xero`, `apollo`, `neon`, `snowflake`, `facebook`, `phantombuster`, `googlebigquery`, `wave-accounting`, `zoho-desk`.
(Gmail, Slack, Notion, GitHub, HubSpot, Stripe katalogda olmadığı için en yakın karşılıkları seçildi.)

## Şablondan sapanlar ve sorunlu olanlar
**Çalışmayan yer tutucular (kalite 1):** `wave-accounting-automation`, `ringcentral-automation`, `zoho-desk-automation` — "toolkit Composio'da bulunamadı" diyor.
Çelişki: alt çizgili ikizleri (`wave_accounting`, `ring_central`, `zoho_desk`) şablon B ile "çalışır" gibi yazılmış; büyük olasılıkla onlar da çalışmaz.

**Adı ile araçları uyuşmayanlar (kalite 2–3):**
| Skill | Gerçekte kullandığı toolkit |
|---|---|
| `braintree-automation` | `STRIPE_*` (Stripe bağlantısı ister; Braintree hesabıyla çalışmaz) |
| `googlebigquery-automation` | `METABASE_*` (BigQuery'ye bağlı bir Metabase örneği gerekir) |
| `googleads-automation` | `GOOGLE_ANALYTICS_*` (GA4 raporları; kampanya yönetimi yok) |
| `excel-automation` | 1 Excel aracı + Google Sheets araçları |

**Dar kapsamlı:** `coinbase` (1 araç), `contentful` (3 araç, içerik girdisi yok), `freshbooks` (2 liste aracı; açıklama faturalama vaat ediyor), `microsoft-clarity` (1 araç).

**Güvenlik/ToS bayrağı:** `phantombuster-automation` → `PHANTOMBUSTER_POST_HCAPTCHA` ile **CAPTCHA çözme** iş akışı. Bot korumasını aşmak site kurallarını
ihlal edebilir; bu iş akışını kullanma.

**Kalıcı/yan etkili işlemler içerenler** (agent'a onaysız çalıştırtma): `google-admin` (kullanıcı silme — skill uyarıyor), `googletasks` (tamamlananları
temizleme — uyarıyor), `launchdarkly` (tetikleyici silme — uyarıyor), `facebook` (Messenger mesajı — "açık onay" istiyor), `capsule-crm`, `clockify`,
`lever`, `new-relic`, `zoho-books`, `webex` (silme), `xero` (ödeme ve banka kaydı oluşturma), `braintree` (abonelik/ödeme yöntemi), `customer.io`
(broadcast tetikleme), `instantly` (toplu soğuk e-posta), `snowflake` (`EXECUTE_SQL` yazma sorgularını da çalıştırır), `neon` (API anahtarı oluşturma;
bağlantı URI'si kimlik bilgisi içerir — skill "gizli tut" diyor). Şablon A/B skillerinde bu tür uyarı hiç yok; hangi aracın yıkıcı olduğu çalışma anında bulunur.

## Güvenlik
- **Veri akışı:** Agent'ın gönderdiği her argüman (e-posta içeriği, müşteri kaydı, SQL, dosya) ve uygulamadan dönen yanıt Composio'nun bulut
  sunucusundan (rube.app → Composio → uygulama API'si) geçer. Composio üçüncü taraf bir veri işleyicidir; KVKK/GDPR kapsamındaki veride sözleşme gerekir.
- **Yetki:** Uygulama hesabına verilen OAuth izni ya da girilen API anahtarı Composio tarafında saklanır. İzinler genellikle geniş kapsamlıdır
  (okuma + yazma + silme). Bağlantıyı Composio panelinden kaldırmak gerekir; skill'i projeden silmek yetkiyi geri almaz.
- **Kişisel veri toplayanlar:** lead/kişi zenginleştirme (`apollo`, `hunter`, `zoominfo`, `peopledatalabs`, `findymail`, `tomba`…), İK (`workday`, `ashby`,
  `lever`), görüşme kaydı (`gong`, `fireflies`).
- **Komut enjeksiyonu riski:** Uygulamalardan dönen içerik (e-posta, ticket, web sayfası) agent'ın bağlamına girer; içindeki talimatlar veri olarak ele alınmalı.
- Skiller yerelde kod çalıştırmaz, betik içermez; risk tamamen MCP bağlantısı ve verilen yetkilerdedir.

## Gruplar (`uygulama_grubu`)
Uygulama adına göre elle sınıflandırıldı (şablon açıklamalar yalnızca adı içerdiği için). Bir uygulama birden çok gruba girebiliyorsa baskın kullanım seçildi.

| Grup | Adet | Örnekler |
|---|---|---|
| gelistirici | 219 | API/altyapı, AI modelleri, web kazıma, izleme, güvenlik: openai, replicate, firecrawl, apify, neon, cloudflare, sentry-benzeri (bugsnag, honeybadger), docker-hub, google-admin |
| pazarlama | 100 | e-posta pazarlama, soğuk e-posta, SEO, link kısaltma, e-posta doğrulama: mailerlite, lemlist, instantly, semrush, ahrefs, bitly-benzeri (cutt-ly, short-io) |
| iletisim | 76 | mesajlaşma, SMS, telefon, toplantı/webinar, chatbot: slackbot, webex, telnyx, dialpad, googlemeet, wati |
| finans | 74 | muhasebe, ödeme, kripto, piyasa verisi: xero, quickbooks, netsuite, zoho-books, braintree, coinbase, alpha-vantage |
| dosya-depolama | 72 | dosya/doküman, PDF üretimi, OCR, e-imza: googledrive, googledocs, sharepoint, cloudinary, pandadoc, documenso, docuseal |
| crm | 58 | CRM, destek masası, lead zenginleştirme: dynamics-365, attio, kommo, capsule-crm, gorgias, apollo, hunter |
| proje-yonetimi | 49 | görev, zaman takibi, takvim/randevu: shortcut, productboard, clockify, toggl, harvest, googlecalendar, googletasks |
| analitik | 34 | ürün/web analitiği, anket, veri ambarı: microsoft-clarity, googlebigquery, snowflake, surveymonkey, similarweb |
| sosyal-medya | 10 | facebook, twitch, typefully, ayrshare, hashnode |
| diger | 140 | İK/işe alım (workday, lever, workable), konum/harita (google-maps, mapbox), hava durumu, e-ticaret/lojistik, form oluşturucular, oyun/spor verisi |

## Ne zaman kullanılır
- **Kullan:** Projede agent'ın bir SaaS hesabında gerçek iş yapması gerekiyorsa (ör. Xero'dan fatura listesi, SharePoint'te dosya arama) ve
  verinin Composio'dan geçmesi kabul edilebiliyorsa. Önce **elle yazılmış 75 skill**'e bak; uygulamaya özel araç adları ve tuzakları içeriyor.
- **Şablon A/B skillerini tek tek kurmaya gerek yok:** Rube MCP bağlıyken agent `RUBE_SEARCH_TOOLS` ile aynı bilgiye zaten ulaşır. Gerekirse
  tek bir şablon skill (ör. hangi uygulama olduğunu agent'a hatırlatmak için) yeterli; 731 kopya bağlam ve liste kirliliğidir.
- **Kullanma:** Uygulamanın resmî MCP sunucusu varsa (GitHub, Notion, Slack, Linear, Stripe vb.) onu tercih et — ara katman ve ek veri işleyici yok.
  Hassas/kişisel veride, offline ortamlarda, ya da Rube MCP kurulamıyorsa kullanma. Yer tutucu 3 skill'i ve CAPTCHA iş akışını hiç kullanma.
- **Kurulum:** `skill-ekle.py <proje> --skill <id>`; ön kontrol BİLGİ `gizli-katalog` verir. Rube MCP'yi istemciye (Claude Code / Codex) ayrıca eklemek gerekir;
  skill-ekle MCP sunucusu kurmaz.

## Öneriler (kullanıcı onayı gerektirir, bu incelemede yapılmadı)
1. 26 tire/alt çizgi ikiz çiftinden birini `durum: alternatif` yap (elle yazılmış olan varsa o tercih).
2. 3 yer tutucu + 3 çelişkili ikizi "sadece arşiv" olarak işaretle (ör. `durum_elle`), aramada çıkmasınlar.
3. `skill-ekle.py --oner` gizli katalogda eşleşme saydığında 731 şablon skill yerine elle yazılmış 75'i öne çıkarsın (ör. `kalite >= 3` filtresi).
