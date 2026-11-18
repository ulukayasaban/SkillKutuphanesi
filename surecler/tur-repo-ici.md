# Tür: repo-içi

## Ne
Bir yazılım ekibinin kendi **geliştiricileri** için yazdığı skiller. Örnek: `remotion-dev/remotion` içindeki `add-effect`. Bölüm: **arşiv** (var olanlar).

## Kütüphanede ne durur
Arşivde bugün 112 skil var (`arsiv/f-repo-ici`, kaynak kaydı tipi T3). Bu skiller yalnız o yazılımın kendisini geliştiren projede önerilir.

## Ekleme adımları
**Yeni repo-içi skil alınmaz.** Repo tür sorusunun 6. sırasında repo-içi çıkarsa: kullanıcıya "repo-içi, alınmıyor" denir; kayıt açılmaz. Aynı repoda kullanıcılar için de skil varsa o parça `tur-urun-skil.md` ile ayrı kayıt olarak alınır
(Next.js ve Playwright böyle iki kayıtlıdır). Kullanıcı yine de isterse karar onundur: kayıt `rehber/03` A4 tablosundaki T3 biçimiyle açılır (`{"repo": "owner/ad", "tip": "T3", "oncelik": 8, "dahil": ["^\\.claude/"], "kimlik": "owner__ad__repo-ici"}`).

## Kayda yazılacak alanlar
Var olan T3 kayıtları aynen kalır. Yeni kayıt açılırsa `tur-koleksiyon.md` örneği; fark: `"tip": "T3"`, `"tur": "repo-ici"`, `"bolum": "arsiv"`.

## Aylık güncelleme
Var olan 112 skilin güncellemeleri bugünkü zincirle sürer.

## Projeye kurulum
Arşivden (`skill-ekle.py`); öneri yalnız o yazılımı geliştiren projede yapılır (öneri kuralı HENÜZ YOK, plan adım 4: o zamana dek `--oner` çıktısını kaynak işini yapan eler).

## Çıkarma
`python3 araclar/kaynak-cikar.py --repo owner/ad --kuru`.

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Skil yazılımı kullananlara önerilir ama geliştiriciler için yazılmıştır | Yeni alınmaz; mevcutlar yalnız ilgili projede önerilir |
