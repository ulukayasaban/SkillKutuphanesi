# Tür: riskli

## Ne
Saldırgan güvenlik (sızma testi, exploit, C2, saldırgan keşif) ya da ikili kullanımlı, zararlı kullanım riski olan skil ve repolar (K-58, `notlar/guvenlik-riskli-skiller.md`). Savunma amaçlı güvenlik skilleri (sağlamlaştırma, güvenlik denetimi, açık ve bağımlılık taraması) bu türe GİRMEZ; normal türle işlenir.

## Kütüphanede ne durur
Hiçbir şey. Kaynak kaydı açılmaz, arşive çekilmez, fihrist ya da katalog kaydı yazılmaz, kategori açılmaz.

## Ekleme adımları
1. Repo `yeni-repo.md` 3. adımın 1. sorusunda (ya da `rehber/03` A1 "K-58 kapısı"nda) riskli çıkarsa akış BURADA durur: boyut, çakışma, ücret, A2-A9 çalıştırılmaz.
2. Ana oturum kullanıcıya bildirir. Kullanıcı isterse repo YALNIZ GitHub'daki "Güvenlik ve Riskli Skiller" (`güvenlik-ve-riskli-skiller`) yıldız listesine yer imi olarak eklenir (ayrı onay; GitHub işlemi). Kütüphane kaydı yine açılmaz.
3. Aday listelerinde (`github-trend.py`, `populer-tarama.py`, `konu-takip.py`) görünüyorsa: `python3 araclar/konu-takip.py --karar owner/ad reddedildi "K-58"` ile aday listesinden düşülür (kararı kullanıcı verir). Başka hiçbir işlem yapılmaz.

## Kayda yazılacak alanlar
Yok (kaynak kaydı açılmaz). Tek kayıt aday kararıdır (`konu-takip.json`).

## Aylık güncelleme
Yok.

## Projeye kurulum
Yok; riskli repodan skil önerilmez ve kurulmaz.

## Çıkarma
Yok. Yanlışlıkla kayıt açıldıysa `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` ile etkisi okunur ve kullanıcı onayıyla çıkarılır.

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Savunma ve saldırı arasındaki sınır belirsiz | Ajan karar vermez, durur ve ana oturuma raporlar; karar kullanıcınındır |
| Aday araçları reddedilen repoyu tekrar getirir | `konu-takip.py --karar ... reddedildi "K-58"` |
