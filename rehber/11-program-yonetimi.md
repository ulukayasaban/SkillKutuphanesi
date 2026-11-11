# 11 — Program yönetimi (skill olmayan yapılar)

Kütüphane yalnızca skilleri değil, kullanıcının kütüphaneye "dahil et" dediği **programları** da takip eder: kendi sürümü,
kendi kurulumu olan yapılar. Program skill değildir; `skill-ekle.py` ile projeye kurulmaz. İki tür kart var:
- **Kaynak kopyalı** (varsayılan, `kopya` alanı yok): kaynak `programlar/<ad>/kaynak/` altında durur. Örnek: `etsyotomasyon`.
- **Yerinde** (`"kopya": "yerinde"`): kaynak kopyalanmaz; program bu bilgisayarda kurulu haliyle izlenir. Örnek: `hyperframes`, `openmontage`.

## Nerede ne var
- `programlar.json` — her program için kart: repo, kütüphanedeki sürüm/commit, kurulum yolları (Windows/macOS/kaynaktan),
  veri yeri, bağlantı, ağ, güncelleme adımları, `asla` listesi.
- `programlar/<ad>/kaynak/` — programın sabit sürümdeki kaynak kopyası (değiştirilmez; yalnız kaynak kopyalı kartta).
  `programlar/<ad>/KAYNAK.md` — repo, sürüm/commit, lisans, alınmayan klasörler (yerinde kartta: neden kopya yok, nasıl yeniden edinilir).
- `kaynaklar.json` — programın reposu kayıtlıdır ve kayıtta `"program": "<ad>"` alanı bulunur (GitHub listesiyle eşleşme ve kapsam
  denetimi için). Tip repoya göre değişir: T5 ya da skill barındıran T1/T2.
- `notlar/referans/kutuphaneler.md` — programın tek satırlık özeti (yalnız T5 kayıtta).
- `notlar/program-denetimi.md` — `python3 araclar/program-denetim.py` çıktısı.

## Yeni program eklemek (kullanıcı "dahil et" deyince)
Önce türü seç: program küçük ve repodan kurulabiliyorsa kaynak kopyalı; büyükse (venv, node_modules, kendi git klonu), kendini
güncelliyorsa ya da zaten bu bilgisayarda kurulu ve yerel değişiklik taşıyorsa yerinde. Yerinde kart için 1. ve 3. adım aynıdır,
2. adımın yerine aşağıdaki "Yerinde program" bölümündeki alanlar doldurulur.
1. Repoyu oku: SKILL.md var mı (varsa normal skill akışı, `03-yeni-skill-ekleme.md`), lisans, son release, bağımlılıklar,
   ağ trafiği, kendini güncelleyip güncellemediği, anahtar istiyor mu.
2. Son release etiketinin kaynağını ayrı bir geçici klasöre indir (`gh api repos/<repo>/tarball/<etiket>`), çalıştırma;
   demo/medya (`docs/`) ve CI (`.github/`) hariç `programlar/<ad>/kaynak/`'a kopyala; `KAYNAK.md` yaz.
3. `programlar.json`'a kart, `kaynaklar.json`'a kayıt (`program` alanıyla), T5 ise `kutuphaneler.md`'ye satır. Repo skill barındırıp
   `kaynaklar.json`'da zaten T1/T2 kayıtlıysa yeni kayıt açma, mevcut kayda `program` alanını ekle; T1/T2 kayıtta `kutuphaneler.md` satırı aranmaz.
4. `python3 araclar/listeye-ekle.py owner/ad` (GitHub listesi), sonra her zamanki kontroller ve commit.

## Yerinde program (kopyasız)
**Ne zaman:** program çok büyük ya da kendi sürümünü kendi yönetiyor (npm genel paketi, git klonu + venv). Kopya hemen eskirdi
ya da yerel yamalarla karışırdı. Kütüphane yalnızca *neyin kurulu olduğunu, hangi sürümün onaylı olduğunu ve nasıl güncelleneceğini* tutar.

**Kart ne taşır** (`programlar.json`):
- `"kopya": "yerinde"`, `repo`; `kaynak_kopyasi` OLMAZ.
- `yerinde`: `tur` = `npm-global` (`yol`, `paket`) ya da `git-checkout` (`yol`, `dal`). `yol` içinde `~` olabilir.
- `kutuphane_surumu` (npm) ya da `kutuphane_commit` (git, tam sha): kütüphane oturumunun en son kaydettiği ve onayladığı kurulu sürüm.
- İsteğe bağlı: `venv` (yol içinde göreli) ve `sabit_surumler` (venv'de yükseltilmemesi gereken paketler: tam sürüm ya da `<5` gibi kısıt).
- Ayrıca: ne yapar, lisans, ücret sınıfı, veri yeri, kendini güncelleme ve skill yazma davranışı, güncelleme adımları, `asla` listesi.
- `programlar/<ad>/KAYNAK.md` ve `kaynaklar.json`'da repo kaydında `"program": "<ad>"` gerekir (`araclar/test.py` bunu denetler).
  Test programın bu bilgisayarda kurulu olmasını istemez.

**`program-denetim.py` ne bildirir:** üç değer: *karttaki*, *kurulu* (şimdi; `package.json`, salt okuma git, dist-info dosyalarından;
program ya da venv çalıştırılmaz) ve *son* (npm kayıt defteri ya da GitHub API'si; `git fetch` yapılmaz). Durum sözcükleri:

| Durum | Anlamı | Ne yapılır |
|---|---|---|
| `güncel` | Kurulu = karttaki, son sürümden geride değil | Bir şey yapılmaz |
| `YENİ SÜRÜM VAR` | Kurulu = karttaki, ama daha yeni sürüm var | Kullanıcıya sürüm farkı ve özet sun; onay gelirse güncelleme adımlarını uygula |
| `KART ESKİ` | Kurulu sürüm karttan farklı: onaylı kayıt olmadan değişmiş (programın kendi güncellemesi olabilir) | Sebebi bul, kullanıcıya söyle; onaylıysa kartı ve `KAYNAK.md`'yi kurulu sürüme çek, değilse nedenini araştır |
| `bu bilgisayarda kurulu değil` | Yol yok; kütüphane programın kurulu olmadığı bir makinede de klonlanır | Hata değil; bir şey yapılmaz |
| `öğrenilemedi` | Ağ ya da ayrıştırma hatası | Sonra yeniden dene; sürüm kararı verme |

Git kartında rapor "N geride" ve yerel değişiklik sayısını (değişen izlenen dosya, izlenmeyen yol) da yazar. `sabit_surumler` varsa
kaç sabitin tuttuğu ve tutmayanlar listelenir. Rapor `notlar/program-denetimi.md` içindeki "Yerinde izlenen programlar" tablosundadır.

**Güncelleme her zaman: önce yedek, sonra ayrı onay.** Her güncelleme için kullanıcıdan ayrıca onay alınır (önceki onay sonrakini
kapsamaz). Önce yedek (yerel değişiklikler, veri klasörü, sabit sürüm listesi), onaydan sonra yalnızca kütüphane oturumu günceller,
sonra yeniden denetim ve kart güncellemesi. Yedek yalnız `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>/` klasörüne alınır; kütüphane
klasörüne ve git'e asla konmaz. `~/.hyperframes` yedeğinde `config.json` alınmaz, `~/.config/openmontage` anahtar klasörü hiç
kopyalanmaz. Yedek, güncelleme doğrulanıp onaylanana kadar saklanır; silmek için kullanıcıya sorulur. Programın kendi kendine güncellemesi ya da skill yazması kartta açıkça yazılıdır;
bunu durduran anahtarlar (ortam değişkenleri) kartta listelenir. Ortam değişkenini kullanıcı kendisi tanımlar; agent tanımlamaz, yalnız hangisinin gerektiğini söyler.

## Takip ve güncelleme
- `python3 araclar/program-denetim.py` durumu raporlar (salt okuma, çıkış 0). Kaynak kopyalı kartta kütüphanedeki sürümü GitHub'daki
  son sürümle karşılaştırır; yerinde kartta karttaki, kurulu ve son değeri karşılaştırır (yukarıdaki bölüm).
- Yeni sürüm varsa, yalnız kaynak kopyalı kart için: CHANGELOG özeti → kullanıcı onayı → kaynak kopyasını yeni etiketten yenile,
  `KAYNAK.md` ve kartı güncelle, commit → programı kullanan makinelerde kullanıcıyla birlikte yenile.
- Yeni sürüm varsa, yerinde kart için: kopya yenilenmez. Yukarıdaki "Güncelleme her zaman: önce yedek, sonra ayrı onay" adımları
  izlenir; güncellemeden sonra yeniden denetim yapılır, `kutuphane_surumu` ya da `kutuphane_commit` ile `KAYNAK.md` güncellenir, commit atılır.

## Kurallar
- Program kopyası proje deposuna konmaz; projeye yalnızca kullanım notu (hangi ekran/komut kullanılır, hangisi kullanılmaz) yazılır.
- Yerinde programlarda yalnız kütüphane oturumu güncelleme yapar; `npx`, `pip install -U`, `git pull`, `make setup` gibi komutlar onaysız
  çalıştırılmaz. Bu, `CLAUDE.md` kural 1'in (genel klasörlere yazma yok) kartlı programlar için tek istisnasıdır: yalnız kullanıcının o
  güncelleme için verdiği ayrı onayla ve kartın adımlarıyla.
- Anahtar, şifre, oturum dosyalarını agent girmez, açmaz, yazdırmaz; hesap bağlama adımlarını kullanıcı yapar.
- Kartlarda proje adı ve "şu projeye uyar" yazılmaz (kütüphane kuralı 6); projeye uygunluk kurulum sırasında incelenir.
