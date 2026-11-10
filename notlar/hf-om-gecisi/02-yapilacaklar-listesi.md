# Olay olursa ne yapılır (2. sürüm)

"Ben" = kütüphane oturumu. "Sen" = kullanıcı. Kural: skille ilgili her iş önce bu oturuma söylenir.

| # | Olay | Ne yapılır | Kim |
|---|---|---|---|
| 1 | Yeni skill ya da skill deposu buldun | GitHub "Yapay Zeka Skillleri" listesine ekle, "yeni skill ekledim, kontrol et" de. Çakışma ve ücret kontrolünden sonra onayınla eklenir | Sen ekler, ben incelerim |
| 2 | Aylık güncelleme | `arsiv-guncelle.py` raporu → ayrı dalda güncelleme → özet → onayınla birleştirme. Sonunda bilgisayar durum raporu | Ben; onay senden |
| 3 | HyperFrames aracının yeni sürümü çıktı | Kendiliğinden kurulmaz (dondurma). İstersen önce yedek yenilenir, sonra sen `npm install -g hyperframes@<sürüm>` çalıştırırsın, projeler taban testini koşar. Eski sürüme dönüş sözü yok | Karar ve kurulum sen; kontrol ben |
| 4 | HyperFrames skilleri kaynakta değişti | Kütüphane arşivi aylık güncellemede yenilenir. Bilgisayarın genelindeki kopyalar **değişmez** | Ben |
| 5 | Bir skill kaynakta emekli oldu | Kütüphanede eski hâli git geçmişinde kalır. Kullanan proje varsa sana söylerim; projeden silinmez | Ben |
| 6 | Kaynak depo taşındı ya da silindi | Taşındıysa `repo` güncellenir, eski ad `eski_adlar`'a yazılır. Silindiyse "erişilemiyor" notu; arşivdeki kopya kalır | Ben |
| 7 | Yeni proje açıyorsun | "Şu projeye skill ekle" de. Öneri → ön kontrol raporu → onay → `skill-ekle.py` ile sadece proje klasörüne kurulum | Ben; onay senden |
| 8 | Proje klasörünü taşıyacak ya da adını değiştireceksin | **Önce bana söyle.** HyperFrames, klasörü bulamadığı projenin geçmişini kendiliğinden siliyor; kütüphanedeki proje kaydı da güncellenmeli | Sen haber verir, ben kaydı düzeltirim |
| 9 | Projeyi silecek ya da arşivleyeceksin | Önce bana söyle; proje kullanım kaydından çıkarılır | Sen, ben |
| 10 | OpenMontage'ın yeni sürümü çıktı | Varsayılan: **güncellenmez** (yerel yamalar ve sabit Python ortamı). İstersen ayrı, küçük bir plan hazırlarım | Karar sen |
| 11 | Yeni bir yapay zekâ aracı kuruyorsun | "Skilleri içe aktar / eşitle" sorusuna hayır de. Sonra bana söyle; aracın skill klasörü rapora eklenir | Sen, ben |
| 12 | Bilgisayarın genelindeki klasörlerde beklenmeyen değişiklik | Aylık rapor gösterir. Hiçbir şeyi geri almadan önce sana sorarım; gerekirse yedekten ilgili klasör geri konur | Ben bulur, karar sen |
| 13 | İki skill aynı adda | Yeni gelen `ad@kaynak` olur; eski kayıt yerinde kalır. Bilerek devir sadece onayınla | Ben; onay senden |
| 14 | Yedek eskidi | Proje dosyasına yazan her işten önce yedek 24 saatten yeni olmalı. Değilse yenilerim | Ben |
| 15 | Bir proje oturumu skill kurmak ya da güncellemek istiyor | Yapmaz. İhtiyacı sana yazar, sen bana getirirsin | Sen, ben |
| 16 | Eklenti ya da hesap üzerinden gelen skiller (Claude uygulamasının kendi skilleri) | Kütüphane bunları yönetmez; raporda sadece listelenir | Ben |

## Hiç değişmeyen kurallar
- Bilgisayarın genelindeki skill klasörlerine ben yazmam. Skill sadece proje klasörüne, sadece `skill-ekle.py` ile kurulur.
- Onay vermeden kurulum, kaldırma, taşıma yok.
- `npx skills …`, `hyperframes update / init / skills update`, OpenMontage'da `git pull` ve `make setup` çalıştırılmaz.
- Kütüphane dışındaki GitHub depolarında işlem yok.
- Her kütüphane değişikliğinden sonra: `kapsam-denetimi.py` (0 sorun), `dogrula.py` (0 hata), sonra commit.
