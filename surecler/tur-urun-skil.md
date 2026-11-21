# Tür: ürün + skil

## Ne
Asıl işi bir yazılım olan, yanında o yazılımı **kullananlar** için skil veren repo. Örnek: `microsoft/playwright`, `heygen-com/hyperframes`, `vercel/next.js`. Bölüm: **arşiv** (yalnız skil kısmı).
Skiller yazılımı geliştirenler içinse tür repo-içidir: `tur-repo-ici.md`. Aynı repoda ikisi de varsa iki kayıt açılır.

## Kütüphanede ne durur
Yalnız skil klasörleri (`arsiv/`, `registry.json`). Yazılımın kendisi alınmaz; "gereksinim" olarak kayda yazılır.

## Ekleme adımları
`tur-koleksiyon.md` "Ekleme adımları" (1-5) ile aynı. Fark:
1. `dahil` / `haric` ile yalnız skil klasörleri seçilir (`rehber/03` A4: `{"repo": "owner/ad", "tip": "T2", "oncelik": 1, "dahil": ["^skills/"]}`). Her SKILL.md tam olarak bir kayıt tarafından alınmalıdır (`kapsam-denetimi.py` kontrol eder).
2. Skilin dayandığı yazılım sürümü ve gereksinimi kayda yazılır (`ne_ister`: örn. "Playwright 1.x"); proje öneri raporunda (`--rapor --oner`) bu gereksinim kullanıcıya gösterilir.
3. Yazılım aynı zamanda programsa (HyperFrames) skil programa bağlıdır ve projeye kopyalanmaz, bağ verilir (K-28): kayda `"program": "<ad>"` yazılır, program kartı ile kaynak kaydı birbirine işaret eder (`rehber/11-program-yonetimi.md`).
4. Repo çok büyükse `boyut-hesapla.py owner/ad --yol <skil klasörü>` ile yalnız alınacak klasörün boyutu hesaplanır; repo indirilmez.

## Kayda yazılacak alanlar
```json
{"repo": "owner/ad", "tip": "T2", "oncelik": 1, "dahil": ["^skills/"], "tur": "urun-skil", "bolum": "arsiv",
 "tur_gerekce": "asıl iş bir yazılım (skil dışı 340/420 kod dosyası); skiller kullanıcılar için",
 "ne_ister": "Playwright (npm), Node 20", "ne_indirir": "tarayıcılar (playwright install ile, ~300 MB; hesaplanamaz)", "tek_basina": true,
 "son_kontrol": {"tarih": "2026-11-18", "commit": "<40 haneli sha>"},
 "arac_uyumu": {"claude": true, "codex": true, "antigravity": true, "windows": true},
 "boyut": {"kutuphane_kb": 80, "kurulum_mb": 150, "hesaplanamayan": ["tarayıcı indirmeleri"], "tarih": "2026-11-18"},
 "eklendi": "2026-11-18", "onay": {"kim": "kullanıcı", "tarih": "2026-11-18", "oturum": "<kısa not>", "commit": "<40 haneli sha>"}}
```

## Aylık güncelleme
Bugünkü zincir (`rehber/02` bölüm 1b); skil kısmı değişir, yazılım indirilmez.

## Projeye kurulum
Arşivden (`python3 araclar/skill-ekle.py <proje> --skill <ad> --kuru`, programa bağlıysa `--program-skill <program>:<ad> --kuru`). Proje önerisi ve gereksinim kontrolü için `python3 araclar/skill-ekle.py <proje> --rapor --oner "<ihtiyaç>"` çalıştırılır; kayıttaki `ne_ister` ve `bagimlilik` bilgisi raporda gösterilir.

## Çıkarma
`python3 araclar/kaynak-cikar.py --repo owner/ad --kuru`; programa bağlıysa `rehber/11` ve `proje-kullanimi.py --program <ad>` önce.

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Skil yazılımın yeni sürümünü anlatır, projede eski sürüm var | Kayıtta `ne_ister` sürümü yazılır; `--rapor --oner` ve kurulum öncesi derin incelemede projedeki sürümle uyum kullanıcıya işaretlenir |
| Yazılım program olarak da kayıtlı | `program` alanı ve K-28 (bağ verilir, kopyalanmaz) |
| Repo çok büyük | Repo indirilmez; yalnız skil klasörü çekilir, `--yol` ile hesaplanır |
