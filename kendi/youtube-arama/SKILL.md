---
name: youtube-arama
description: yt-dlp kullanarak YouTube'da arama yapar ve her sonuç için video başlığı, URL, izlenme sayısı, süre ve yayın tarihi döndürür. Kullanıcı "YouTube'da ara", "şu konuda video bul", "en çok izlenen videolar hangileri", "video listesi çıkar", "YouTube araştırması yap", "rakip kanalların videolarına bak", "içerik fikri için YouTube'a bak" gibi bir şey söylediğinde bu skill'i kullan. Kullanıcı yt-dlp'yi ismen anmasa bile, YouTube'dan video listesi/metadata gerektiren her istekte tetiklen — arama sonuçlarını web araması veya tahminle üretme, bu skill gerçek veriyi çeker. Tek bir videonun altyazısını almak veya video indirmek için DEĞİL.
---

# YouTube Arama

yt-dlp üzerinden YouTube arama sonuçlarını yapılandırılmış olarak getirir.

## Kullanım

```bash
python3 ~/.claude/skills/youtube-arama/scripts/youtube_search.py "<sorgu>" -n <sayı>
```

### Parametreler

| Parametre | Zorunlu | Varsayılan | Açıklama |
|---|---|---|---|
| `sorgu` | evet | — | Arama sorgusu (tırnak içinde) |
| `-n`, `--sayi` | hayır | `10` | Döndürülecek video sayısı |
| `--sirala` | hayır | `ilgi` | `ilgi` (YouTube sırası), `izlenme`, `tarih` |
| `--json` | hayır | kapalı | Ham JSON çıktısı |

### Örnekler

```bash
python3 ~/.claude/skills/youtube-arama/scripts/youtube_search.py "enflasyon istatistik" -n 5
python3 ~/.claude/skills/youtube-arama/scripts/youtube_search.py "veri görselleştirme" -n 15 --sirala izlenme
python3 ~/.claude/skills/youtube-arama/scripts/youtube_search.py "istatistik shorts" -n 10 --json
```

## Çıktı alanları

Her sonuç için: **başlık**, **URL**, **kanal**, **izlenme sayısı**, **süre**, **yayın tarihi** (YYYY-AA-GG).

`--json` ile alan adları: `baslik`, `url`, `kanal`, `izlenme`, `sure_sn` (saniye), `tarih` (YYYYAAGG).

## Notlar

- Yayın tarihi arama sonucunun düz (flat) çıktısında gelmez; script bu yüzden iki aşamalı çalışır — önce hızlı arama, sonra her video için paralel metadata çekimi. 5 sonuç ≈ 8 sn, 20 sonuç ≈ 20 sn. Çok büyük `-n` değerlerinde beklemeye hazır ol.
- Arama sonuçlarındaki kanal ve oynatma listesi girdileri otomatik elenir; yalnızca videolar döner.
- İzlenme sayısı bazı videolarda gizli olabilir, o durumda `-` gösterilir.
- Gereksinim: `yt-dlp` (kurulu değilse `brew install yt-dlp`). Ek Python paketi gerekmez, standart kütüphane yeterlidir.
- Sonuçları kullanıcıya sunarken tabloya dökmek okunurluğu artırır.
