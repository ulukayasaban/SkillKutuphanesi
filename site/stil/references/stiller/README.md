# Hazır stiller

Kaynak: Smokich "Video Stilleri" sitesi (https://smokich.gosem.dev/stil/), `site.js` içindeki `STILLER` dizisi. Uzun prompt'lar
Michael Szach'ın stil kütüphanesinden Claude Code'a uyarlanmıştır. İndirme tarihi: 2026-11-15. Ayrıntı ve dosya özetleri: `../../KAYNAK.md`.

| id | Ad | Kısa tanım | Neye iyi | Örnek konu | Uzun prompt |
|---|---|---|---|---|---|
| `kagit-poster` | Kâğıt Poster | Düz mürekkep, kâğıt, büyük çizim | Kanal anlatımları, fikir videoları | Claude Code nasıl çalışır | yok |
| `kesik-kagit` | Kesik Kâğıt | Elle kesilmiş sıcak katmanlar | Süreçler, sıcak anlatım | Arılar bal nasıl yapar | `kesik-kagit.txt` |
| `konstruktivist` | Konstrüktivist | Çapraz kırmızı, siyah, krem bloklar | Sert fikirler, kıyaslar | Kalabalıklar neden aynı anda hareket eder | yok |
| `bilim` | Bilim Atlası | Eski kâğıtta teknik çizim | Bir şeyin içi nasıl çalışır | DNA kendini nasıl kopyalar | yok |
| `risograf` | Risograf | Üst üste basılmış parlak mürekkep | Kültür, müzik, hikâye | Plak nasıl ses çıkarır | `risograf.txt` |
| `izometrik` | İzometrik Çizim | Kendini çizen teknik yapılar | Sistemler, akışlar | Su musluğa nasıl gelir | `izometrik.txt` |
| `duz-vektor` | Düz Vektör | Temiz, renkli 2D çizim | Eğitici açıklamalar | Uyurken beyin ne yapar | `duz-vektor.txt` |
| `kinetik` | Kinetik Tipografi | Yazının kendisi görüntü | Fikirler, ipuçları, alıntılar | Neden sürekli erteliyoruz | `kinetik.txt` |
| `cam` | Sıvı Cam | Görüntüyü büken cam mercekler | Uygulama ve ürün anlatımı | Bir mesaj arkadaşına nasıl ulaşır | `cam.txt` |
| `ascii` | ASCII Atlas | Karakterlerden örülmüş renkli imgeler | İnternet, veri, teknoloji | İnternet nasıl çalışır | yok |
| `parcacik` | Parçacık | Şekle dönüşen binlerce ışık | Bilim, uzay, teknoloji | Kara delik nasıl oluşur | `parcacik.txt` |

**Uzun prompt'u olmayan 4 stil:** `kagit-poster`, `konstruktivist`, `bilim`, `ascii`. Sitede bu dosyaların yerinde yalnız ana sayfaya
yönlendirme var. Bu stiller için ya aşağıdaki kısa şablon kullanılır ya da SKILL.md'deki yolla referans görselden yeni uzun prompt yazılır.

## Uzun prompt'ların kullanımı
Her `<id>.txt` kendi başına tam bir prompt'tur. Başındaki yapılandırma bölümünde şu yer tutucular doldurulur (sitenin doldurduğu değerler):

| Yer tutucu | Değer |
|---|---|
| `{{KONU}}` | Konu metni (boşsa tablodaki örnek konu) |
| `{{STORYBOARD}}` | `Enabled` ya da `Disabled` |
| `{{SES}}` | `Enabled (the recording is in this folder)` ya da `Disabled` |
| `{{BICIM}}` | `Horizontal, 16:9, native resolution 1920 × 1080` ya da `Vertical, 9:16, native resolution 1080 × 1920` |
| `{{EFEKT}}` | `Enabled` ya da `Disabled` |
| `{{MUZIK}}` | Sitede her zaman `Disabled` |

## Kısa şablon (uzun prompt'u olmayan stiller için)
Sitenin `site.js` → `promptParcalari()` işlevinden çıkarıldı. `<KONU>` ve `<BİÇİM>` doldurulur (biçim: `Yatay 1920×1080` ya da dikey).
`<STİL KARTI>` yerine sitede stile ait kısa stil metni gelir; bu metinler `site.js`'te değil, ana sayfanın (`stil.html`)
`<script type="text/plain" id="stil-<id>">` bloklarındadır; 11 stilin kartı `kartlar/<id>.md` dosyalarına alındı (2026-11-15, ana sayfadan aynen).

```
Bu klasörde stüdyo kalitesinde bir motion graphics videosu yap. Slayt gösterisi değil: sahneler birbirinin içinden doğsun, görüntü anlatsın.

Konu: <KONU>
Biçim: <BİÇİM>

Stil:
<STİL KARTI>

Video bir anlatıma eşlik ediyor; görüntü takip edilebilecek kadar sakin kalsın. Çoğu sahne değişimi düz kesme ya da kamera hareketi olsun, özel geçişi birkaç büyük ana sakla. Ekrandaki yazılar Türkçe, okunurken sabit; cümleleri ekrana yazma.
[koşullu satırlar, açık olanlar bu sırayla]

HTML, CSS ve JavaScript ile yap, her kare window.seek(t) ile çizilsin. Kareleri headless Chrome ile çek, ffmpeg ile MP4 yap; eksikse kur. Birçok kareye bak, gurur duyana kadar düzelt.
```

Koşullu satırlar:
- Sahne planı açıksa: `Önce sahne planını çıkar, onaylamadan video yapma.`
- Ses açıksa: `Ses dosyası bu klasörde: süreyi ondan al, Whisper ile kelime zamanlarını çıkar, görüntüyü söylenene oturt.`
- Ses efekti açıksa: `Ses efektlerini Openverse API'den al (https://api.openverse.org/v1/audio/?q=whoosh&license=cc0), anahtar gerekmez; az ve yerinde kullan, kullandıklarını CREDITS.md'ye yaz.`
