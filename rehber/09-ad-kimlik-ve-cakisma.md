# 09 — Ad, Kimlik ve Çakışma Kuralları

Bir skill üç ayrı adla anılır. Hangisinin ne zaman değiştiğini bilmek, "aynı adlı başka skill kuruldu" sorununu önler.

| Kavram | Nerede | Örnek | Ne zaman değişir |
|---|---|---|---|
| **Ad** (`ad`) | SKILL.md `name` | `security-scan` | Kaynak repo değiştirirse |
| **Kimlik** (`id`) | `registry.json` | `security-scan` · `security-scan@ruvnet` | **Değişmez** (aşağıdaki tek istisna dışında) |
| **Kurulum adı** | Projede klasör + `kilit.json` anahtarı | `security-scan` · `security-scan--ruvnet` · `x--kutuphane` | **Değişmez** (kilitte kaynağa bağlıdır) |

Kurulu bir skill **kaynağıyla** (repo + repo içi yol) izlenir, adıyla değil. Bu yüzden kütüphanede öncelikler ya da kimlikler
değişse bile projedeki skill sessizce başka bir skile dönüşmez (`kaynak_bul`); kaynak yoksa "kaynak yok" denir, yerine aynı adlı
başka repo **asla** konmaz.

## Değişmez kurallar
1. **Çıplak ad kendiliğinden el değiştirmez.** Bir adı ilk alan kayıt o kimliği korur. Sonradan gelen aynı adlı skill, önceliği
   daha yüksek olsa bile `ad@kaynak` kimliği alır. Tam çalıştırmada (`kimlik_ata` 1. geçiş) ve tek repo eklemede (`kimlik_devri`)
   kural aynıdır.
2. **Aynı ad her zaman aynı iş değildir.** Ekleme raporunda aynı adlı her çift içerik olarak karşılaştırılır:

   | Durum | Ne olur |
   |---|---|
   | İçerik birebir aynı | Tek kayıt; diğeri `kopya_kaynaklar`'a yazılır |
   | Ad aynı, iş aynı, içerik farklı | Öncelik "tercih"i belirler; diğeri `ad@kaynak` "alternatif". İkisi de kurulabilir |
   | Ad aynı, **iş farklı** | Kimlikler değişmez; eski kayıt `durum_elle` ile "tercih" sabitlenir; iki kaydın `notlar` alanına fark yazılır |
   | Globalde aynı adlı farklı skill | Projeye `ad--kutuphane` adıyla kurulur (kişisel skill proje skilini ezmesin diye) |
   | Projede kütüphaneden gelmeyen aynı adlı klasör | HATA `projede-kendi-skillin`; üzerine yazılmaz |
   | Claude hesabında aynı adlı skill | Projede `skillOverrides` ile gizlenir (`hesap-cakismasi`) |

3. **Bilerek devir** (ör. resmî üretici, topluluk kopyasının adını devralsın): yeni kaynağın `kaynaklar.json` kaydına
   `"ad_devral": ["<ad>"]` yazılır. Eski kayıt `ad@eski-kaynak` olur, çıplak ad yenisine geçer. Bu, kullanıcıya gösterilip onay
   alınan bir karardır; önce `python3 araclar/proje-kullanimi.py --skill <ad>` ve rollerde kullanım kontrol edilir.
4. **"Tercih" ile kimlik ayrı şeylerdir.** `--skill <ad>` ve roller önce **kimliği birebir** arar. Çıplak kimlik "alternatif"
   durumdaysa ön kontrol `alternatif-surum` UYARISI ile tercih edileni gösterir; karar kullanıcınındır.
5. **Ön kontrol her zaman söyler:** kurulacak skilin adaşı varsa `ayni-ad` BİLGİSİ kurulan kimliği, kaynağını ve diğer sürümleri
   listeler. Başka sürüm isteniyorsa tam kimlik yazılır: `--skill security-scan@ruvnet`.

## Repo adı değişirse (taşınma / yeniden adlandırma)
GitHub eski adı yenisine yönlendirir; ama eski ad boşa çıktığı için başkası aynı adla repo açabilir. Bu yüzden ad güncellenir:

1. `python3 araclar/github-skill-listesi.py` bunu **AD DEĞİŞMİŞ** diye raporlar (YENİ kaynak saymaz; yalnız `yeni` ve `eksik` birlikte doluyken) ve
   `python3 araclar/kaynak-cikar.py --repo <eski ad> --kuru --github` da **AD DEĞİŞMİŞ** der (yalnız okur).
2. `kaynaklar.json`'da kaydın `repo` alanını yeni adla değiştir, eski adı `"eski_adlar": ["eski-sahip/ad"]` listesine yaz.
3. Kayıt dosyalarındaki eski adı yenisiyle değiştir: `registry.json`, `kategori-kurallari.json`, `ucret-siniflandirma.json`,
   `gelistiriciler.json`, `trend.json` ve ayrıca `programlar.json` (kartın `repo`su), `konu-takip.json` (`konular.*.repolar`,
   `degerlendirilen`, `izlenen` anahtarları), `notlar/referans/*.md` (T5/T6 kart/satır). `yol-istisnalari.json` ve `projeler.json`
   el değmez (anahtarlar `eski_adlar` ile eşlenir / proje→skill kimliği tutar). Hangi dosyada kaç satır geçtiği:
   `python3 araclar/kaynak-cikar.py --repo <eski ad> --kuru`. Kimlikler (`ad@eski-sahip`) **değişmez**.
4. `gelistirici-bilgisi.py --repo yeni/ad` → `katalog-uret.py` → `kapsam-denetimi.py` → `dogrula.py --github` → `test.py`.
5. Projelere dokunmak gerekmez: kilitteki eski repo adı `eski_adlar` haritasıyla güncel kaynağa eşlenir; sonraki `--guncelle`
   kilide yeni adı yazar.

## Kaynak çıkarılırsa
Çıkarılan kaynağın `ad_devral` ile devraldığı çıplak ad boşalır; eski sahibin kimliği `ad@kaynak` olarak kalır (kimlikler değişmez).
Çıkarmadan sonra `skill-ekle.py --listele --ara <ad>` ile tercihin kimde olduğuna bak; istenmiyorsa `durum_elle` ile sabitle.
`ad_devral` devirden sonra kayıtta kalır (zararsız); kayıt çıkarılınca birlikte gider. Bilerek devir geri alınacaksa devralanın
`ad_devral` girdisini sil ve eski kaydı `durum_elle` ile tercih yap (kullanıcı onayı). Çıkarma adımları: `rehber/03` D; etki raporu:
`python3 araclar/kaynak-cikar.py --repo owner/ad --kuru`.

## Kontrol komutları
```bash
python3 araclar/skill-ekle.py --listele --ara <ad>            # aynı adlı tüm sürümler, kimlikleri ve durumları
python3 araclar/skill-ekle.py <proje> --skill <ad> --kuru     # hangi kaynak kurulacak? (ayni-ad / alternatif-surum / ekli-ad)
python3 araclar/proje-kullanimi.py --skill <ad>               # bu skili hangi projeler kullanıyor
python3 araclar/dogrula.py                                    # rollerde bir adın kaynağı değiştiyse UYARI verir
```
