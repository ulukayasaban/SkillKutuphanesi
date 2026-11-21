# Tür: program

## Ne
Bilgisayara kurulan, kendi sürümü olan yazılım; skiller ona bağlıdır. Bugün: OpenMontage, HyperFrames, nlm, etsyotomasyon (kayıtlı ama kurulu olmayan: claude-code-video-toolkit). Bölüm: **katalog** (`programlar.json` kartı).
Program olduğunu belirleyen soru (yeni-repo.md sıra 3): bilgisayara kurulan bir yazılım mı ve skiller onun kurulu olmasına mı bağlı?

## Kütüphanede ne durur
`programlar.json` kartı (elle biçimlenmiştir: yeniden serileştirilmez, yalnız hedefli metin düzenlenir), kaynak kopyalı kartta `programlar/<ad>/kaynak/`, `programlar/<ad>/KAYNAK.md`, `kaynaklar.json` kaydı (`program` alanıyla). Yerinde izlenen programda kaynak kopyası yoktur.

## Ekleme adımları
Ayrıntı ve yöntem tek yerde: `rehber/11-program-yonetimi.md` "Yeni program eklemek". Özet:
1. `yeni-repo.md` adım 1-6; boyut: `python3 araclar/boyut-hesapla.py owner/ad --dev` (klonlanıp kurulan programda geliştirme bağımlılıkları sayılır; hazır paket olarak kurulanda `--dev-yok`).
2. Kart iskeleti: `python3 araclar/program-denetim.py --iskelet <tür>` (`kaynak`, `npm-global`, `uv-tool`, `git-checkout`); doldurma ve onaylı kurulum `rehber/11`, hazır istem `promptlar/13-program-kur-guncelle.md`. KURULUM YAPILMAZ: program kurmak kullanıcının adını sayarak verdiği ayrı onayı ister.
3. Kaynak kaydı: `kaynaklar.json` içinde `"program": "<ad>"` alanı. Skil barındırmayan programda `tip` T5 (`notlar/referans/kutuphaneler.md` satırı da gerekir); `tur` program, `bolum` katalog.
4. Kontroller: `python3 araclar/program-denetim.py --sema --siki`, `python3 araclar/dogrula.py`, `python3 araclar/test.py`. Commit ana oturumdadır.

## Kayda yazılacak alanlar
`kaynaklar.json` (skilsiz program):
```json
{"repo": "owner/program", "tip": "T5", "program": "programadi", "tur": "program", "bolum": "katalog",
 "tur_gerekce": "uv ile kurulan komut satırı yazılımı; skiller ona bağlı",
 "ne_ister": "Python 3.12, uv", "ne_indirir": "paketler ve çalışırken modeller (hesaplanamaz)", "tek_basina": false,
 "son_kontrol": {"tarih": "2026-11-18", "commit": "<40 haneli sha>"},
 "arac_uyumu": {"claude": true, "codex": true, "antigravity": true, "windows": false},
 "boyut": {"kutuphane_kb": 0, "kurulum_mb": 900, "hesaplanamayan": ["modeller"], "tarih": "2026-11-18"},
 "eklendi": "2026-11-18", "onay": {"kim": "kullanıcı", "tarih": "2026-11-18", "oturum": "<kısa not>", "commit": "<40 haneli sha>"}}
```
Kart alanları (`programlar.json`) `rehber/11` "Kart şeması" tablosundadır; burada tekrarlanmaz.

## Aylık güncelleme
Sürüm takibi bugünkü gibi: `python3 araclar/program-denetim.py` (yerinde kartta kurulu, karttaki ve son sürüm; `rehber/11`). Kurulu boyut ölçümü HENÜZ YOK (plan adım 5).

## Projeye kurulum
Program projeye kurulmaz, bilgisayarda tek kurulumdur. Programla gelen skiller bağ olarak verilir: `python3 araclar/skill-ekle.py <proje> --program-skill PROGRAM:AD --kuru` (K-28; `rehber/01`, `rehber/11`). Bağlar Windows'ta çalışmaz (araç reddeder).
Program kurulu değilse raporda "program kurulu değil" yazar; "kurulumu … yer tutar" satırı HENÜZ YOK (plan adım 4). Program kurulumu ayrı onay ister.

## Çıkarma
Her güncelleme, geri alma ve kaldırma kullanıcının AYRI onayıyla ve önce yedekle yapılır: `rehber/11` "Taze ajan: istek → adımlar". Önce `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demeli; `python3 araclar/proje-kullanimi.py --program <ad>` projelerdeki bağları gösterir.

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Güncelleme projeleri bozar | `proje-kullanimi.py --program <ad>`; kırıcı sürümde ayrı klasörde deneme (`rehber/11`) |
| Bağlar Windows'ta çalışmaz | `--program-skill` Windows'ta reddedilir; raporda yazar |
| Program çalışırken model ve paket indirir | Karttaki "ne indirir" alanında ve kaynak kaydının `ne_indirir` alanında tutulur |
| Yedekler yer tutar | Aylık raporda yedeklerin toplam boyutu (HENÜZ YOK, plan adım 5); silme yalnız kullanıcı isteyince (`rehber/13`) |
| Skil barındıran program T1/T2 kayıtlı ve arşive çekiliyor | Bugünkü kayıtlara dokunulmaz (plan adım 3); bu tür kayda `bolum: katalog` yazılırsa arşive çekilmez, bu yüzden mevcut kayıtlarda karar adım 3'te verilir |
