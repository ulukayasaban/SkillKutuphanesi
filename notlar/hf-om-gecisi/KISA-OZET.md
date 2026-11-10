# Kısa özet (tek sayfa, 2. sürüm)

Karar için bu sayfa yeter. Ayrıntı `00-plan.md` içinde; okuman gerekmiyor.

## Ne değişti
Eleştiriden sonra plan küçüldü. **Skiller yerinden oynamıyor.** Taşıma işi rafa kalktı: faydası kanıtlanamadı, riski vardı.

## Sorun (tek tane)
HyperFrames aracı kendini ve skillerini kendiliğinden güncelliyor (son 4 haftada 8 sürüm değişti). Yedek de yok.
Bir güncelleme projeleri bozarsa geri dönecek yer yok.

## Yapım süreci
| Adım | İş | Kim | Projelere dokunur mu |
|---|---|---|---|
| 0 | Kütüphanenin bozuk denetim aracını onar, aylık otomatik görevi duraklat | Ben | Hayır |
| 1 | Tek komut: HyperFrames kendiliğinden güncellenmesin (Terminal'den çalışan işler için) | **Sen** | Hayır |
| 2 | Skillerin, araçların ve dört projenin yedeği (~30 GB, birkaç on dakika) | Ben | Hayır, sadece okur |
| 3 | Bilgisayarın ve projelerin durum raporu | Ben | Hayır, sadece okur |
| 4 | Hazır metinler: Claude yasak listesi, OpenMontage yamalarını kayda alma, 2 küçük düzeltme | Ben hazırlar, **sen** uygularsın | Hayır |
| 5 | Kısa promptları proje oturumlarına yapıştırırsın; projeler kendini raporlar | **Sen** | Hayır, sadece okur |
| Kapanış | Duraklatılan aylık görevi yeniden aç | Ben, sana sorarak | Hayır |
| – | **Dur.** Raporlarda arıza yoksa iş biter | | |

## "Evet" dersen neyi kabul etmiş olursun
- Adım 0: kütüphane içinde bir aracın onarımı ve aylık görevin duraklatılması.
- Adım 2: yedeğin `~/Documents/Claude/yedek/` altına alınması.
- Adım 3: sadece okuyan küçük bir rapor aracı.
- Adım 4 ve 5 için hazır metinlerin yazılması.

Koruma tam engel değildir: aşılırsa aylık rapor gösterir, yedekten dönülür.

**Kabul etmiş olmazsın:** bilgisayarın genelindeki skillerde ya da projelerde herhangi bir kurulum, kaldırma, taşıma;
HyperFrames ya da OpenMontage güncellemesi; GitHub'a gönderme.

## Senden istenen
| # | Soru | Önerim |
|---|---|---|
| 1 | Adım 0, 2, 3'e başlayayım mı? | Evet |
| 2 | Adım 1'deki tek komutu çalıştıracak mısın? | Evet |
| 3 | OpenMontage anahtar dosyaları yedeğe girsin mi? (açılmadan) | Evet |
| 4 | İkinci kopya için uygun diskin var mı? (takılı "ADIL HD" uygun değil: 4.6 GB boş) | Yoksa tek kopyayla devam |
