---
name: antigravity-gorsel
description: Google Antigravity'nin komut satırı aracı (agy) üzerinden görsel üretir ve dosyayı istenen klasöre kaydeder. Kullanıcı "Antigravity ile resim üret", "antigravity'den görsel yap", "agy ile görsel", "Antigravity'ye bağlanıp ... resmi çiz" gibi bir şey dediğinde kullan. Antigravity adı geçmeyen genel görsel isteklerinde kullanma.
---

# Antigravity ile görsel üretme

Antigravity bu Mac'te kurulu. Komut satırı aracı `~/.local/bin/agy`. Google hesabıyla giriş zaten yapılmış, giriş ya da API anahtarı isteme.

## Adımlar

1. **İsteği netleştir.** Kullanıcının tarifini İngilizce, ayrıntılı bir görsel tarifine çevir (konu, ortam, ışık, stil). Kullanıcı stil belirtmediyse "photorealistic" kullan. Dosya adını Türkçe karakter ve boşluk olmadan seç (örnek: `yuzen-araba.png`).

2. **Görseli kaydedeceğin klasöre geç ve agy'yi çalıştır.** agy dosyayı o anki klasöre kaydeder, o yüzden önce `cd` ile hedef klasöre gir:

   ```bash
   cd "<hedef klasör>" && agy -p "Use your image generation tool to create <İNGİLİZCE TARİF>. Save the resulting image file into the current directory as <dosya-adi>.png. Reply with the saved file path." --print-timeout 280s 2>&1 | tail -30
   ```

   - Bash aracında `timeout: 300000` ver. Üretim genelde 1-2 dakika sürer.
   - `--mode auto` ekleme: bu hesapta açık değil, uyarı verip varsayılan moda geçiyor.
   - Birden fazla görsel istenirse her biri için ayrı bir `agy -p` çağrısı yap.

3. **Doğrula.** `ls -la` ile dosyanın oluştuğuna ve boyutunun 0 olmadığına bak. Sonra Read aracıyla görseli aç ve isteğe uyup uymadığını kendin kontrol et. Uymuyorsa tarifi düzeltip bir kez daha dene.

4. **Kullanıcıya göster.** `SendUserFile` ile `display: "render"` vererek görseli gönder. Cevapta dosyaya bağlantı ver ve görselde ne olduğunu bir iki cümleyle anlat.

## Sorun çıkarsa

- `agy: command not found` → tam yolu kullan: `~/.local/bin/agy`.
- Dosya oluşmadıysa agy çıktısının son satırlarını kullanıcıya göster, tahminle başka araca geçme. Başka bir görsel aracı kullanmadan önce kullanıcıya sor.
- Zaman aşımı olursa `--print-timeout` değerini artırıp komutu arka planda (`run_in_background`) çalıştır.
