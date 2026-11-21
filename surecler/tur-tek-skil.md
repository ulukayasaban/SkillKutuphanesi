# Tür: tek skil

## Ne
Yalnız bir skil içeren repo. Örnek: `kajisho5/ffmpeg-skill`. Bölüm: **arşiv**. Kurallar `tur-koleksiyon.md` ile aynıdır; bu dosya yalnız farkı yazar.

## Kütüphanede ne durur
Skilin dosyaları `arsiv/` altında, tek `registry.json` kaydı, tek `kaynaklar.json` kaydı.

## Ekleme adımları
`tur-koleksiyon.md` "Ekleme adımları" (1-5) aynen. Fark: tek skilli repo kök klasörde SKILL.md taşıyabilir; bu durumda `kok_dosyalari` ile yalnız skilin dosyaları alınır
(`rehber/03` A4 "kok_dosyalari", "dosya_haric") ve repodaki örnek, önizleme, rapor klasörleri `dosya_haric` ile dışarıda bırakılır.
Tek skilli repolar örnek videolarla çok büyüyebilir (bir skil 28 MB görüldü): `tur-belirle.py` çıktısındaki medya MB'ı ve `boyut-hesapla.py` sonucu kullanıcıya söylenir; medya kuralı en çok bu türde yer kazandırır.

## Kayda yazılacak alanlar
`tur-koleksiyon.md` örneği; fark: `"tur": "tek-skil"`, `"tur_gerekce": "1 SKILL.md"`; kökte duran skilde `"kok_dosyalari": ["SKILL.md"]` ya da `dosya_haric` desenleri.

## Aylık güncelleme
`tur-koleksiyon.md` ile aynı.

## Projeye kurulum
`tur-koleksiyon.md` ile aynı (arşivden, `skill-ekle.py`).

## Çıkarma
`tur-koleksiyon.md` ile aynı.

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Repodaki örnek videolar ve önizlemeler arşivi şişirir | `dosya_haric`; bugünkü video koruması `skill_ici_haric`; medya ihtiyacı `ne_indirir`e yazılır |
| Tek skilin kopyası başka kaynakta var | `rehber/09-ad-kimlik-ve-cakisma.md`; kopya arşive ayrı girmez |
