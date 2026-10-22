# 06 — Skill Değerlendirmesi ve Geliştirici Bilgisi

## Geliştirici bilgisi (`gelistiriciler.json`, registry → `gelistirici`)
`araclar/gelistirici-bilgisi.py` her kaynak repo için GitHub'dan şunları toplar:

| Alan | Anlamı |
|---|---|
| `sahip`, `sahip_tipi` | Repo sahibi; `kurum` (organizasyon) ya da `kisi` |
| `resmi_kaynak` | Teknolojinin kendi üreticisi mi (anthropics, greensock, vercel, microsoft, pmndrs…) |
| `yildiz`, `fork`, `katkici`, `acik_issue` | Topluluk büyüklüğü ve ilgi |
| `son_guncelleme`, `olusturulma`, `arsivlenmis` | Bakım durumu |
| `lisans` | Kullanım hakkı (MIT, Apache-2.0, MPL-2.0…; "yok" = belirsiz) |
| `aciklama`, `ana_sayfa` | Kısa tanım, doküman |

Özet tablo: `notlar/gelistiriciler.md` (katalog üretiminde oluşur).

## Otomatik değerlendirme puanı (0–100, registry → `degerlendirme`)

| Ölçüt | Puan | Kural |
|---|---|---|
| Bakım | 25 | Son güncelleme ≤90 gün 25 · ≤180 18 · ≤365 10 · daha eski 3 |
| Topluluk | 20 | 4 × log10(yıldız + 1), en fazla 20 |
| Lisans | 15 | Açık lisans 15 · yok/belirsiz 3 |
| Kaynak | 10 | Resmî üretici 10 · kurum 5 · kişi 3 |
| Codex uyumu | 15 | Tam 15 · uyarlanabilir 10 · Claude'a özel 5 |
| Bağlam yükü | 10 | SKILL.md <8 KB 10 · <25 KB 8 · daha büyük 5 |
| Yapı | 5 | Frontmatter sorunu ve kırık bağlantı başına düşer |
| Arşivlenmiş repo | −15 | |
| GitHub Trending | +10 / +6 / +2 | Kaynak repo son taramada trend'de +10 · son 90 günde görülmüş +6 · daha önce görülmüş +2 (`trend.json`, `araclar/github-trend.py`; puan 100'ü geçmez) |

Not: **A** ≥80 · **B** ≥65 · **C** ≥50 · **D** <50. Elle `kalite` (1–5) girilirse son puan = %60 otomatik + %40 elle.

> Puan bir **risk göstergesidir**, kalite ölçüsü değildir. Yıldızı az ama çok iyi bir skill düşük puan alabilir;
> bu yüzden kategori incelemesinde `kalite` ve `kalite_notu` elle verilir.

## Elle değerlendirme (kategori incelemesinde)
registry'de skill kaydına şu alanlar eklenir (güncellemede korunur):
```json
"kalite": 4,
"kalite_notu": "GSAP 3.13+ API'leriyle güncel; ScrollTrigger örnekleri doğru, cleanup anlatımı eksik",
"inceleme": "incelendi", "inceleyen": "claude", "inceleme_tarihi": "2026-10-22"
```
Ölçütler:
1. **Doğruluk:** API'ler güncel mi (GSAP 3.15, three r186, Motion v14, Tailwind v4, R3F v9, Next 16…)?
2. **Odak:** tek işi mi anlatıyor; tetiklenme açıklaması (`description`) net mi?
3. **Uygulanabilirlik:** adım adım, örnekli mi; "yapma" listesi var mı?
4. **Taşınabilirlik:** Claude'a özgü araç varsayımı var mı?
5. **Güvenlik:** script çalıştırıyor mu, ağdan bir şey indiriyor mu, API anahtarı istiyor mu?
6. **Bağlam maliyeti:** references dosyaları gerektiğinde mi yükleniyor?

## Seçimde nasıl kullanılır
- `--oner` ve `--listele` çıktısında puan görünür.
- Aynı işi yapan iki skill arasında: önce **elle kalite**, sonra **resmî kaynak**, sonra **puan**.
- D notlu skill ön kontrolde UYARI üretir.

## Öneride trend önceliği (`skill-ekle.py --oner`)
Sıralama önce **konuya uygunluğa** (anahtar kelime + teknoloji eşleşmesi) bakar. Eşleşen skiller arasında kaynağı GitHub Trending'e girmiş olanlar öne alınır (trendde +1,5 · son 90 gün +1 · eski +0,3; çıktıda `🔥trend`). Trend tek başına bir skill'i öneriye sokmaz; ücretli (−2), alternatif (−1) ve emekli (−6) cezaları geçerlidir.
