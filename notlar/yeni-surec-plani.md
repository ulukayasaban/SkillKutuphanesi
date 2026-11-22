# SkillKutuphanesi — Yeni Süreç Planı (Detaylandırılmış Kesin Uygulama Dokümanı)

**Tarih:** 2026-11-21

**Durum:** Tüm 9 adım onaylandı; mevcut 10 tür süreci ve 187 repoluk kaynak listesiyle doğrulandı.

**Kapsam:** [SkillKutuphanesi `gemini-plan`](https://github.com/ulukayasaban/SkillKutuphanesi/tree/gemini-plan) belgeleri, `surecler/` altındaki 10 tür dosyası ve [Yapay Zeka Skillleri](https://github.com/stars/ulukayasaban/lists/yapay-zeka-skillleri) kaynak listesi temel alınarak mevcut yapının üzerine kurulacak sade, ölçülebilir, otonom ve hata korumalı süreç tasarımıdır. Bu doküman yalnızca plan ve kesin tanım belgesidir; hiçbir dosya kurulmaz veya silinmez.

## Dayanak Kaynaklar

* Ana plan belgeleri: [İstenen Süreç](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/notlar/istenen-surec.md), [İstenen ve Mevcut Karşılaştırma](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/notlar/istenen-ve-mevcut-karsilastirma.md), [Çalışma Planı](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/notlar/yeni-surec-plani-calisma.md), [Tür Süreçleri Planı](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/notlar/plan-tur-surecleri.md), [Yeni Skill Ekleme Rehberi](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/notlar/rehber-03-yeni-skill-ekleme.md)

* Süreç dosyaları: [Süreçler Dizini](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/README.md), [Yeni Repo Akışı](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/yeni-repo.md), [Dev Koleksiyon](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-dev-koleksiyon.md), [Kendi ve Site](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-kendi-ve-site.md), [Kit](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-kit.md), [Koleksiyon](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-koleksiyon.md), [Program](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-program.md), [Referans](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-referans.md), [Repo-içi](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-repo-ici.md), [Riskli](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-riskli.md), [Tek Skil](https://www.google.com/search?q=https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-tek-skil.md), [Ürün ve Skil](https://github.com/ulukayasaban/SkillKutuphanesi/blob/gemini-plan/surecler/tur-urun-skil.md)

* Kaynak listeler: [Yapay Zeka Skillleri](https://github.com/stars/ulukayasaban/lists/yapay-zeka-skillleri) (tek ana kaynak, 187 repo) ve [Güvenlik ve Riskli Skiller](https://github.com/stars/ulukayasaban/lists/g%C3%BCvenlik-ve-riskli-skiller) (kütüphaneye eklenmeyen yer imi listesi)

## 1–3. Temel Kararlar, Kapsam ve 4 Bölümlü Veri Düzeni

### 1. Amaç ve 4 Temel Kısıt (TAMAM)

* **K1 Hafıza:** Her bilgi tek bir yerde tutulur; çift kayıt (`kaynaklar.json` vs `kitler.json`, ayrı `bekleyenler` dosyası vb.) yasaktır.

* **K2 Maliyet:** Disk, süre ve kullanıcı onay sayısı ölçülür ve düşük tutulur.

* **K3 Bağımsızlık:** Kullanıcının rutin tek işi GitHub listesine repo eklemektir; yeni repo girişi ve aylık tarama kullanıcı beklemeden yürür.

* **K4 Token ve hata maliyeti:** Kural işleri Python'da (0 token) çalışır; oturum açılış yükü en aza indirilir; hatalar ön-kapı ve çıkış kapılarıyla engellenir.

### 2. Temizlik Düzeyi — Ortadaki Yol (TAMAM)

* **Korunan çekirdek:** `skill-ekle`, `kilit.json`, `tur-belirle`, `boyut-hesapla`, `dogrula`, `kapsam-denetimi`, `konu-takip`, `--geri-al` ve mevcut 324 test korunur.

* **Temizlenecekler (aşamalı):** 8/8 çift kayıt, `tip`/`tur` senkron bozuklukları (138 kayıt), açılış yükü (\~32,5 KB) ve gereksiz büyük medya/kopya dosyaları.

### 3. Dört Bölümlü Veri Düzeni ve Geçici `tip` Eşlemesi (TAMAM)

| Bölüm (`bolum`) | Kapsama Giren Türler (`tur`) | Tutulan Dosya ve Kayıtlar | Kesinlikle Tutulmayanlar | Faz 1–2 Geçici `tip` Senkronu | 
| ----- | ----- | ----- | ----- | ----- | 
| **`arsiv`** | `tek-skil`, `koleksiyon`, `urun-skil`, `kendi`, `site`, mevcut `repo-ici` (112 kayıt) | `arsiv/` skill dosyaları, `kaynaklar.json`, `registry.json` (`site` için ek `site-takip.json` + `KAYNAK.md`) | Büyük medya, model ağırlıkları, `.claude-plugin` kanca/MCP/ayarları, yeni `repo-ici` | `tek-skil`/`koleksiyon` → `T1`, `urun-skil` → `T2`, `repo-ici` → `T3`, `kendi` → `T7`, `site` → `T8` | 
| **`fihrist`** | `dev-koleksiyon` (200+ skill) | `fihrist/<owner>__<ad>.json` (ad, tek cümle açıklama, kaynak yolu, commit), `kaynaklar.json` | Skill dosyalarının kendisi (tek istisna: aktif kullanılan `arsivde_tut` yolları) | `T1` + `bolum: fihrist` | 
| **`katalog`** | `kit`, `program` | `kaynaklar.json` + `kitler.json` (kit) veya `programlar.json` (program; kaynak kopyalıysa `programlar/<ad>/`) | Kit skill dosyaları (arşive çekilmez); `programlar.json` yeniden serileştirilmez | `kit` → `T1` + `bolum: katalog`, `program` → `T5` (skilsiz) veya `T1`/`T2` (skilli) | 
| **`not`** | `referans` (`alt_tur`: `kutuphane` | `tasarim_teknolojisi`) | `kaynaklar.json` + `notlar/referans/kutuphaneler.md` (`T5`) veya `tasarim-teknolojileri.md` (`T6`) | Repo dosyaları ve skill kurulumları | 
| **Red (kayıt yok)** | `riskli` (K-58) | Yalnız `konu-takip.json` içinde `reddedildi "K-58"` kaydı | Arşiv, fihrist, katalog, not ve kategori kaydı açılmaz | Açılmaz | 

* **Tekilleştirme kuralı:** Faz 1–2 boyunca tek doğruluk kaynağı `tur` + `bolum` (+ referansta `alt_tur`) olur; `tip` alanı yalnız `dogrula` ve 324 testin kırılmaması için otomatik senkronlanır. Tüm araçlar güncellendikten sonra Faz 3'te `tip` alanı kaldırılır.

## 4. Giriş Süreçleri (Kesin Adım Akışı ve Kapsam)

### A. Uçtan Uca Yeni Repo Giriş Akışı (Karar 4.1-B ve 4.2-B)

1. **Ön-kapı (Python, 0 token):** `git status --short` kontrol edilir. Çalışma ağacı boş değilse süreç **hemen durur**, hiçbir dosya yazılmaz.

2. **Liste tarama ve fark çıkarma (Python, 0 token):** [Yapay Zeka Skillleri](https://github.com/stars/ulukayasaban/lists/yapay-zeka-skillleri) listesi mevcut `kaynaklar.json` ve `konu-takip.json` ile karşılaştırılır; `yeni`, `degisen`, `yonlendirilen (301)` ve `kesin_404` kümeleri ayrılır.

3. **Hızlı kural kapısı — Hafif Kapı (Python, 0 token):** Her yeni repo için 10 sıralı tür kuralı çalıştırılır:

   1. Saldırgan güvenlik / K-58 mi? → **Otomatik reddet** (`konu-takip.json`: `reddedildi "K-58"`), boyut/çakışma çalıştırma. *(Savunma amaçlı güvenlik bu kurala girmez.)*

   2. Lisans yok veya kısıtlı mı? → Akışı kesme, `konu-takip.json` kuyruğuna ekle (`neden: lisans_yok`).

   3. Gri alan güvenlik (tersine mühendislik, yerel proxy, sistem komutu çalıştıran betik) mi? → `konu-takip.json` kuyruğuna ekle (`neden: gri_guvenlik`).

   4. Açıklama boş, `SKILL.md` yok veya standart dışı (`CLAUDE.md`/`DESIGN.md`) mı? → `ADAY` olarak `konu-takip.json` kuyruğuna ekle (`neden: aciklama_veya_skill_yok`).

   5. Tür sırası (`program` → `kit` → `dev-koleksiyon (200+)` → `repo-ici (alınmaz)` → `urun-skil` → `koleksiyon` → `tek-skil` → `referans`) `KESİN` mi, `ADAY` mı? → `ADAY` ise kuyruğa ekle (`neden: tur_aday`).

4. **Boyut, medya ve çakışma kapısı (Python, 0 token):**

   * Arşivlenecek türlerde (`tek-skil`, `koleksiyon`, `urun-skil`) `boyut-hesapla` ve `tur-belirle` medya kontrolü çalışır; eşik üstü medya/model `skill_ici_haric` / `dosya_haric` ile dışlanır, `ne_indirir` yazılır.

   * Mevcut bir skill veya `yerel/kendi` ile ad çakışması varsa o repo onaysız girmez, `konu-takip.json` kuyruğuna alınır (`neden: ad_cakismasi`); birebir kopya arşive ikinci kez alınmaz (`rehber/09`).

5. **Bölüme göre onaysız kayıt (Python + `kim: "kural"`):**

   * `tek-skil` / `koleksiyon` / `urun-skil` → `arsiv` (`kaynak-cek` + `arsiv-yerlestir` + `katalog-uret` + `skill-readme`).

   * `dev-koleksiyon` → `fihrist` (`fihrist-uret`; yalnız `arsivde_tut` yolları arşivde kalır).

   * `kit` / `program` → `katalog` (`kitler.json` veya `programlar.json` hedefli metin ekleme; kurulum ve betik çalıştırma yapılmaz).

   * `referans` → `not` (`notlar/referans/` kartı + `kaynaklar.json`).

6. **3'lü çıkış kapısı ve commit (Ana oturum):** Her kaynak için `dogrula` (0 hata) + `kapsam-denetimi` (0 sorun) + `test` (%100 yeşil) geçerse **kaynak bazında ayrı commit** atılır; hata çıkarsa commit engellenir ve o kaynak geri alınır.

7. **Oturum sonu özet ve kuyruk sunumu (Ana oturum):** `olcum.jsonl` satırı yazılır; kuyrukta biriken tüm `ADAY`/belirsiz repolar **tek toplu mesajla** kullanıcıya sunulur.

## 5. Projelerdeki Skiller (Kesin Mod Davranışları ve Toplu Onay)

### A. Proje Sürüm Modu Davranış Matrisi (Karar 5.1-A)

Her projenin kendi `kilit.json` dosyasında tek bir `surum_modu` bulunur; yeni projeler varsayılan olarak **`yalniz_onayli`** açılır.

| Mod | İlk Kurulum | Aylık Tarama | Etki Raporu | Toplu Onay Grubu | Güncelleme | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| **`yalniz_onayli`** (varsayılan) | Tekil kullanıcı onayı | Taranır | Görünür | Yalnız açık onay verilirse girer | Kullanıcı onayı olmadan değişmez | 
| **`takip`** | Tekil kullanıcı onayı | Taranır | Görünür | Eşleşen skill + hedef sürüm grubuna otomatik dahil olur | Toplu onayla (yedekli) güncellenir | 
| **`dondur`** | Tekil onay (mod kilidi uyarısı) | Güncelleme önerilmez | **Görünmez** | **Girmez** | Hiçbir güncelleme yapılmaz | 

### B. Toplu Onay ve Atomik Güncelleme Akışı (Karar 5.2-A)

1. **Gruplama kuralı:** Aynı `kaynak + skill_adi + hedef_surum` üçlüsüne geçecek ve `elle_degistirildi: false`, lisans/ücret değişmemiş projeler tek toplu grupta birleştirilir.

2. **Tekil onaya düşen istisnalar:** `elle_degistirildi: true` olan skill'ler, eski ve yeni sürüm arasında lisans veya ücret durumu değişen kaynaklar ve `dondur` modundaki projeler toplu gruptan çıkarılıp ayrı satırda tek tek onaya sunulur.

3. **Atomik uygulama ve geri alma:** Onaylanan her proje için sırasıyla **(a)** yedek alınır, **(b)** hedef klasöre (`.claude/skills` veya `.agents/skills`) yeni sürüm yazılır, **(c)** `kilit.json` güncellenir, **(d)** doğrulama (`skill-ekle --dogrula`) çalıştırılır. Herhangi bir projede hata çıkarsa yalnız o proje `--geri-al` ile geri alınır, diğer projeler etkilenmez.

## 6. Kalite, Güvenlik, Ücret, Özel Tür Kısıtları ve Onay Merdiveni

### A. İki Aşamalı İnceleme Kapsamı (Karar 6.1-A)

| İnceleme Aşaması | Ne Zaman Çalışır? | Kim Yapar? | Kontrol Edilenler | Karar Çıktısı | 
| ----- | ----- | ----- | ----- | ----- | 
| **1. Hafif Kapı (Giriş)** | Her yeni repo ve aylık taramada | Python araçları (0 token) | K-58 saldırgan güvenlik filtresi, lisans varlığı/değişimi, ücret etiketi (`ucret-siniflandirma.json`), `SKILL.md` varlığı, medya/MB eşiği, ad çakışması | `GEÇER (KESİN)` | 
| **2. Derin Kapı (Kurulum Öncesi)** | Bir skill ilk kez bir projeye kurulmadan hemen önce | **İnceleme yapan** rolü + `skill-calistir` | Komut/betik güvenlik okuması, prompt enjeksiyonu ("onay isteme / şunu da kur" yönergesi), `.claude-plugin` yasaklı parçalar, bağımlılık/yazılım gereksinimi (`ne_ister`), `skill-calistir` çalışma testi | `KURULUMA UYGUN` | 

### B. Özel Tür Kısıtları (Değiştirilemez Sınırlar)

* **Kendi ve site (`yerel/kendi` T7, `yerel/site` T8):** GitHub taramasına girmez; `site` ekleme/güncelleme her zaman kullanıcı onaylı ve `site-takip.json` (sha256) tabanlıdır; `ERİŞİLEMEDİ` olsa bile 404/KAYIP sayılmaz; `yerel/kendi` çıplak adı halka açık skille el değiştirmez (`ad@yerel`).

* **Repo-içi (`tur-repo-ici`):** Yeni repo-içi skiller alınmaz; mevcut 112 kayıt yalnız o yazılımın kendi projesinde önerilir.

* **Program ve programa bağlı skiller (`tur-program`, `tur-urun-skil`):** Program bilgisayara tek kurulumdur (ayrı onay + yedek); programa bağlı skiller projeye kopyalanmaz, bağ (symlink) verilir (K-28) ve Windows'ta reddedilir. `programlar.json` elle biçimlidir, **yeniden serileştirilmez**.

* **Kit (`tur-kit`):** Kit kurulum betikleri eklemede asla çalıştırılmaz (yalnız statik okuma); projeye kurulumda ancak kullanıcı raporu onaylarsa çalışır.

* **Eklenti paketleri (`.claude-plugin`):** Bütün olarak kurulmaz; kanca, ayar ve MCP sunucuları dışlanır ve `kurulmayan_parcalar` alanına yazılır.

### C. Kesin Onay Merdiveni

| Seviye | Tetikleyen İşlemler | Onay Biçimi | 
| ----- | ----- | ----- | 
| **Onaysız** | `KESİN` yeni repo kaydı (`kim: "kural"`), K-58 otomatik ret, fihrist/katalog/`not` güncellemesi, aylık tarama, kullanılmayan 404 işaretleme, raporlama, yedek denetimi | Yok (kayıt + özet rapor) | 
| **Toplu onay** | Aynı skill + aynı hedef sürüm birden çok projede eşleşmesi; oturum sonu `konu-takip.json` belirsiz repo kuyruğu | Tek toplu liste + tek onay | 
| **Tek tek onay** | Projeye ilk kurulum/kaldırma, tekil sürüm değişikliği, `elle_degistirildi: true`, lisans/ücret değişen güncelleme, `dondur` projede işlem, `site` ekleme/güncelleme, program kurulum/güncelleme, `fihriste-tasi` | İşlem başına açık onay (`--kuru` → `--evet`) | 
| **Her zaman kullanıcıya** | Ücretli (`"ücretli"`) kullanım/ödeme, kalıcı silme, güvenlik istisnası (K-58/gri alan), GitHub'a `push` veya GitHub yıldız listesine yazma | Her seferinde açık kullanıcı kararı | 

## 7. Token ve Maliyet Süreçleri (Ölçüm ve Açılış Yükü)

### A. Beş Metriğin Kesin Ölçüm Tanımı (Karar 7.1-A)

1. **`sure_sn`:** İşlem başlangıcından commit/rapor bitişine kadar geçen toplam duvar saati süresi (saniye).

2. **`token_veya_kota`:** Oturumda YZ'ye giden/gelen toplam token (ölçülebiliyorsa) veya YZ çağrı adedi (0 = tamamen Python).

3. **`disk_mb`:** İşlem sonrası `arsiv/` + `fihrist/` + `.git/` toplam boyutu (MB) ve önceki tura göre farkı.

4. **`onay_sayisi`:** Oturum boyunca kullanıcıdan istenen toplam onay turu sayısı (hedef: rutin yeni repo girişinde `0`, belirsizler varsa en fazla `1` toplu onay).

5. **`hata_tekrar`:** Başarısız doğrulama, geri alma veya tekrar denenen adım sayısı.

* **Hedef belirleme protokolü:** Sayısal üst sınırlar tahmini yazılmaz; Faz 3'te **1 gerçek yeni repo girişi + 1 gerçek aylık takip** ölçülüp taban değerler (`olcum.jsonl`) çıkarıldıktan sonra her 5 metrik için üst sınır sabitlenir.

* **Sabitlenen Sayısal Üst Sınırlar (Faz 3b Taban Ölçümleri Sonrası):**

| Metrik | `yeni_repo` (Taban: `olcum.jsonl`) | `yeni_repo` Üst Sınır | `aylik_takip` (Taban: `olcum.jsonl`) | `aylik_takip` Üst Sınır |
| ----- | ----- | ----- | ----- | ----- |
| **`sure_sn`** | `1.0 sn` (Python aracı) | `≤ 15 sn` (`KESİN` Python); `≤ 60 sn` (`ADAY` YZ) | `2920.0 sn` (~48.6 dk, 198 repo) | `≤ 3600 sn` (tüm aktif kaynak taraması + rapor) |
| **`token_veya_kota`** | `0` çağrı (Python aracı) | `0` (`KESİN`); `≤ 1` YZ çağrısı (`ADAY` oturum başı) | `0` çağrı (Python aracı) | `0` (tarama); `≤ 1` YZ çağrısı (yalnız lisans/gri alan farkı) |
| **`disk_mb`** | `458.32 MB` (`disk_fark_mb: +0.21 MB`) | Repo başına `disk_fark_mb ≤ 5 MB` (medya/model hariç) | `458.36 MB` (`disk_fark_mb: +0.04 MB`) | Tur başına `disk_fark_mb ≤ 25 MB` (toplam büyüme kontrollü) |
| **`onay_sayisi`** | `0` (`KESİN`) / `1` (kuyruk) | `0` (rutin `KESİN`); `≤ 1` toplu onay (belirsizler) | `0` (tarama ve yerleşim) | `0` (salt tarama/rapor); `≤ 1` toplu onay (uygulama turunda) |
| **`hata_tekrar`** | `0` | `0` (3'lü çıkış kapısı ilk denemede yeşil; en fazla `1` kurtarma) | `1` (upstream `earshot` uyarısı) | `0` (rutin); en fazla `1` upstream uyarı düzeltmesi |

### B. İnce Açılış Kuralı (Açılış Yükü ≤ 3 KB)

* **Açılışta okunacak tek dosya (`BASLA.md` özeti):** Aktif faz, 4 temel kısıt (K1–K4), 4 satırlık onay merdiveni ve "hangi iş için hangi dosya açılır" yönlendirme tablosu.

* **Açılışta kesinlikle okunmayacaklar:** `surecler/tur-*.md` (10 dosya), `rehber-03`, `plan-tur-surecleri`, `kaynaklar.json` tam metni, `fihrist/*.json`. Bunlar yalnız ilgili adım tetiklendiğinde açılır.

## 8. Roller, Ajan Dönüşümü, Python İş Bölümü ve YZ Araç Uyumu

### A. Modele ve Araca Bağımsız 4 Rolün Kesin Tanımı (Karar 8.1-A)

Yeni veya araca kilitli bir ajan dosyası tanımlanmaz; tüm süreç aşağıdaki 4 rol üzerinden yürür:

| Rol | Ne Zaman Devreye Girer? | Kesin Yetki ve Görevleri | Kesin Yasakları | Kullandığı Araç / Çıktı | 
| ----- | ----- | ----- | ----- | ----- | 
| **1. Ana oturum** | Her oturumun başında ve sonunda | Ön-kapı (`git status`), rol yönlendirme, onay merdiveni yönetimi, `konu-takip.json` toplu kuyruk sunumu, **tüm git commit'leri**, `olcum.jsonl` kapanışı | Kendi başına büyük dosya inceleme; onaysız `push` veya kalıcı silme | `git`, `konu-takip`, `olcum.jsonl` | 
| **2. Kaynak işini yapan** | Yeni repo girişinde veya `ADAY` sınıflamasında | `tur-belirle` / `boyut-hesapla` çıktısını yorumlama; yalnız belirsiz (`ADAY`) repoda tür önerisi üretme; arşiv/fihrist/katalog/`not` yazım adımlarını yürütme | Git commit atma; K-58 istisnası verme; kit kurulum betiği çalıştırma; `programlar.json` yeniden serileştirme | `tur-belirle`, `boyut-hesapla`, `kaynak-cek`, `arsiv-yerlestir`, `fihrist-uret`, `katalog-uret` | 
| **3. İnceleme yapan** | İlk kurulum öncesi derin kapıda, gri alan güvenlikte veya yeni proje önerisinde | Derin güvenlik ve prompt enjeksiyonu okuması; `skill-calistir` testi; lisans/ücret değişikliği değerlendirmesi; yeni proje için skill öneri raporu | Dosya silme; proje `kilit.json` yazma; kullanıcı onayı olmadan kurulum yapma | `skill-calistir`, `skill-ekle --oner / --kuru`, güvenlik/öneri raporu | 
| **4. Denetim yapan** | Commit öncesi 3'lü çıkış kapısında ve aylık takip sonunda | `dogrula`, `kapsam-denetimi`, `test` sonuçlarını doğrulama; aylık etki raporu ve toplu onay gruplarını üretme; `son-aylik-calisma.json` kontrolü | Hatalı testle commit'e onay verme; `dondur` projeyi güncelleme listesine alma | `dogrula`, `kapsam-denetimi`, `test`, `arsiv-guncelle --aylik`, `proje-kullanimi` | 

### B. Sıfır Token (Python) vs. YZ Yargı Sınırı

* **Python araçları (0 token — tam otomatik):** Liste farkı, `KESİN` tür önerisi, boyut/medya filtresi, çakışma kontrolü, fihrist/katalog/`not` üretimi, `kilit.json`, yedekleme, `--geri-al`, `son-aylik-calisma.json`, 3'lü çıkış kapısı ve `olcum.jsonl`.

* **YZ yalnız 3 yargı noktasında çağrılır:** (1) `ADAY` / standart dışı / boş açıklamalı repo sınıflaması, (2) ilk kurulum öncesi derin güvenlik ve gri alan incelemesi, (3) yeni proje için skill öneri raporu.

### C. Mevcut 7 Ajanın 4 Role Sadeleştirme Eşlemesi

* Mevcut K-60 yapısındaki 7 Sonnet tabanlı ayrı ajan dosyası yeni kurguda sabit model/araç bağımlılığı taşımadan 4 role indirilir:

  * **Kaynak / tarama / yerleştirme ajanları** → **Kaynak işini yapan** rolünde birleşir (tekrarlı adımlar Python'a iner).

  * **Güvenlik / kalite / öneri inceleme ajanları** → **İnceleme yapan** rolünde birleşir.

  * **Doğrulama / aylık özet / denetim ajanları** → **Denetim yapan** rolünde birleşir.

  * **Orkestrasyon / kullanıcı iletişimi / commit** → **Ana oturum** rolünde kalır.

### D. YZ Araç Uyumluluk Matrisi

| YZ Aracı | Proje İçi Skill Klasörü | Genel Klasör Kuralı | Destek Düzeyi | 
| ----- | ----- | ----- | ----- | 
| **Claude Code** | `.claude/skills` | `~/.claude` boş kalır (`.claude-plugin` bütün kurulmaz) | Tam uyum (test ve garanti) | 
| **Codex** | `.agents/skills` | Genel klasör boş kalır | Tam uyum (test ve garanti) | 
| **Antigravity** | `.agents/skills` | Genel klasör boş kalır | Tam uyum (test ve garanti) | 
| **Diğer YZ araçları** | Ortak `SKILL.md` düzeni | Ek çaba / ayrı test yok | Pasif uyum | 

## 9. Geçiş Planı (Faz 1–3) ve 14 Kabul Senaryosu

### A. Faz Bazlı Kesin Kapsam, Dokunulmayacaklar ve Geri Dönüş (Karar 9.1-A)

| Faz | Değişecek Alanlar | Dokunulmayacaklar | Çıkış Kapısı | Geri Dönüş (Rollback) | 
| ----- | ----- | ----- | ----- | ----- | 
| **Faz 1 — Temel ve ölçüm** | `kaynaklar.json` (`tur`+`bolum` ana kaynak, `tip` geçici senkron, `onay` içinde `kim: "kural"`); 4 projenin `kilit.json` dosyasına `surum_modu: "yalniz_onayli"`; `olcum.jsonl` yazıcısı; ince `BASLA.md` özeti | Mevcut onay akışı, 112 `repo-ici` kayıt, `programlar.json` biçimi, arşiv dosyaları | 324 test yeşil; `dogrula` 0 hata; açılış özeti ≤ 3 KB | Tek git revert (yalnız şema/doküman) | 
| **Faz 2 — Akış, onay ve eksik araçlar** | `yeni-repo` onaysız `KESİN` akışı + `konu-takip.json` kuyruğu; K-58 otomatik ret (savunma istisnalı); aylık zincire fihrist/kit/referans/program + `son-aylik-calisma.json` + rate-limit/301 koruması; eksik dev koleksiyon/kit/referans/ürün+skil kurulum-öneri akışları; toplu onay etki raporu aracı | Eski sürümler silinmez; mevcut `tip` alanı hâlâ senkronlu kalır | Etki raporu ve toplu onay çalışıyor; girişte gereksiz onay yok; 3'lü çıkış kapısı yeşil | Faz 2 dalı/commit'i geri alınır, Faz 1 düzeni çalışmaya devam eder | 
| **Faz 3 — Ölçüm ve temizlik** | 1 yeni repo + 1 aylık takip ölçümüyle 5 metriğe sayısal üst sınır yazılması; 8/8 çift kaydın temizlenmesi; tüm araçlar güncellendikten sonra `tip` alanının kaldırılması; 7 eski ajanın 4 role sadeleştirilmesi | Proje içi kurulu skill'ler ve `yerel/kendi` kayıtları | Sayısal hedefler yazılı; çift kayıt 0; 14 kabul senaryosu + tüm testler yeşil | Her temizlik kalemi ayrı commit ile geri alınabilir | 

### B. Kabul Senaryoları (14 Senaryo)

| \# | Senaryo | Beklenen Sonuç | 
| ----- | ----- | ----- | 
| 1 | Listeye `KESİN` tek skill eklenir | Onaysız (`kim: "kural"`) arşive alınır, 3'lü çıkış kapısından geçer, `olcum.jsonl` yazılır | 
| 2 | Listeye saldırgan güvenlik reposu (K-58) eklenir | Sorulmadan reddedilir, `konu-takip.json`'a işlenir; GitHub listesine ekleme kullanıcı onayına bırakılır | 
| 3 | Listeye savunma amaçlı güvenlik skili eklenir | Riskli sayılmaz, normal türle işlenir | 
| 4 | Listeye belirsiz (`ADAY`), açıklaması boş, standart dışı (`CLAUDE.md`), gri alan güvenlik veya lisanssız repo eklenir | Akış durmaz; mevcut `konu-takip.json` kuyruğundan oturum sonunda tek toplu mesajda sorulur | 
| 5 | Listeye 200+ dev koleksiyon, kit, program veya referans eklenir | Dev koleksiyon fihriste (`arsivde_tut` hariç), kit/program kataloga, referans `not` bölümüne işlenir; büyük medya dışlanır | 
| 6 | Yeni projeye ilk kez skill kurulur | Önce derin güvenlik + `skill-calistir` çalışır; `kilit.json` `yalniz_onayli` açılır (kit betiği yalnız kullanıcı onayıyla çalışır) | 
| 7 | Aylık kontrolde aynı skill 2+ projede güncellenebilir | Tek toplu onay grubunda sunulur; onay sonrası yedekli ve atomik güncellenir | 
| 8 | Projede elle değiştirilmiş skill veya lisans/ücret değişikliği bulunur | Toplu gruba girmez; ayrı tekil onaya düşer | 
| 9 | Dondurulmuş (`dondur`) proje | Güncellenmez ve aylık etki raporunda görünmez | 
| 10 | Kullanılan kaynak kesin 404 verir (`site` hariç) | Yerel eski sürüm silinmez; uyarı kaydı düşer (`site` erişilemezse KAYIP sayılmaz) | 
| 11 | Taramada GitHub API hız sınırı (403/429) veya zaman aşımı oluşur | Kaynak KAYIP işaretlenmez; geçici hata kaydedilir ve kontrol noktasından devam edilir | 
| 12 | Mevcut `yerel/kendi` veya arşiv skiliyle ad çakışması oluşur | Eski ad ezilmez (`ad@yerel` kuralı); yeni repo `konu-takip.json` kuyruğuna alınır | 
| 13 | Çalışma ağacı kirli (`git status` dolu) veya güncelleme yarıda kesilir | Kirli ağaçta süreç başlamaz; yarıda kalan tek proje/kaynak `--geri-al` ile geri alınır | 
| 14 | İlk 1 yeni repo + 1 aylık tur tamamlanır | `olcum.jsonl` 5 metriği kaydeder ve sayısal hedefler belirlenir | 

## 10. Kesin Veri Şemaları (Mevcut Dosyalarla Uyumlu)

| Dosya | Zorunlu Alanlar ve Geçerli Değerler | İsteğe Bağlı / Koşullu Alanlar | Yazma ve Bakım Kuralı | 
| ----- | ----- | ----- | ----- | 
| **Proje `kilit.json`** | `surum_modu`: `"yalniz_onayli"` | `"takip"` | `"dondur"`; her skill'de `kaynak`, `surum`, `son_islem_tarihi`, `elle_degistirildi` (`bool`), `durum`: `"guncel"` | 
| **Kaynak `kaynaklar.json`** | `repo`, `tur`, `bolum`: `"arsiv"` | `"fihrist"` | `"katalog"` | 
| **Maliyet `olcum.jsonl`** | `tarih`, `tur`: `"yeni_repo"` | `"aylik_takip"`, `islenen_repo`, `sure_sn`, `token_veya_kota`, `disk_mb`, `onay_sayisi`, `hata_tekrar` | `not` | 
| **Kuyruk `konu-takip.json`** | `repo`, `durum`: `"bekliyor"` | `"karar_verildi"` | `"reddedildi"`, `neden`: `"tur_aday"` | 
| **Aylık `son-aylik-calisma.json`** | `son_tarih`, `durum`: `"tamamlandi"` | `"yarim_kaldi"`, `taranan_arsiv`, `taranan_fihrist`, `taranan_katalog`, `taranan_not`, `etkilenen_proje_sayisi`, `toplu_onay_grubu_sayisi` | `kaldigi_kaynak`, `gecici_hata_sayisi` | 

## 11. Olası Hatalar ve Önleyici Kontroller (Hata Matrisi)

| \# | Olası Hata / Risk | Algılama Sinyali | Otomatik Tepki ve Önlem | Kurtarma Adımı | 
| ----- | ----- | ----- | ----- | ----- | 
| 1 | **Kirli çalışma ağacı veya yarıda kalan güncelleme** | `git status --short` boş değil veya yazım sırasında hata | Kirli ağaçta süreç başlamaz; her proje güncellemesi atomik ve yedekli yürür | Hatalı tek proje/kaynak `--geri-al` ile geri alınır, diğerleri korunur | 
| 2 | **GitHub API hız sınırı (403/429) veya ağ kesintisi** | HTTP `403`, `429`, `5xx` veya zaman aşımı | Kaynak asla KAYIP işaretlenmez; `son-aylik-calisma.json` `yarim_kaldi` + `kaldigi_kaynak` yazar | Limit açılınca kaldığı kaynaktan devam edilir; yalnız kesin `404`/`410` kayıp adayıdır | 
| 3 | **Medya, model ağırlığı ve dev repo disk şişmesi** | `boyut-hesapla` veya `tur-belirle` medya/MB eşik aşımı (`OpenMontage`, `blender`, `FFmpeg`, `whisper`, `herk-edit-kit` vb.) | Eşik üstü dosyalar `skill_ici_haric`/`dosya_haric` ile dışlanır, `ne_indirir` yazılır; tek skilde yalnız `kok_dosyalari` alınır | Yanlışlıkla şişen kayıt varsa `kaynak-cikar --kuru` sonrası temizlenir | 
| 4 | **Boş açıklama, çok dilli veya standart dışı (`SKILL.md` yok) repo** | Açıklama boş (`android/skills`, `ag-kit`), Çince (`MoneyPrinterTurbo`) veya yalnız `CLAUDE.md`/`DESIGN.md` | Tahminle `KESİN` atanmaz; `ADAY` olarak `konu-takip.json` kuyruğuna düşer | Oturum sonunda kullanıcı onayıyla doğru türe atanır | 
| 5 | **Ad çakışması ve `yerel/kendi` skilinin ezilmesi** | `registry.json` veya `kendi/` içinde aynı skill adı | Onaysız giriş o repo için durur, `konu-takip.json` (`ad_cakismasi`) kuyruğuna düşer; `yerel/kendi` adı el değiştirmez (`ad@yerel`) | Kullanıcı kararıyla yeni gelen adlandırılır veya kopya ise alınmaz (`rehber/09`) | 
| 6 | **Aylık güncellemede gizli lisans veya ücret değişikliği** | Eski ve yeni commit arasında lisans veya `ucret-siniflandirma.json` farkı | Kaynak toplu güncelleme grubundan çıkarılır | Aylık etki raporunda tekil kullanıcı onayına sunulur | 
| 7 | **Gri alan güvenlik ve prompt enjeksiyonu** | Tersine mühendislik (`morluto/rea`), yerel proxy (`caveman`), "onay isteme / şunu da kur" yönergesi veya `.claude-plugin` kancası | K-58 otomatik reddedilir; gri alan `konu-takip.json` (`gri_guvenlik`) kuyruğuna alınır; repo metni veri sayılır, kanca/MCP dışlanır | Derin inceleme raporu sonrası yalnız kullanıcı açık onayıyla istisna verilir | 
| 8 | **Repo ad/sahip değişikliği (301) ve çift kayıt** | GitHub `301` yönlendirmesi veya aynı repoda hem kullanıcı hem repo-içi skil | `301` yeni kayıt açmaz, mevcut kaynağın adresini günceller; repo-içi klasörler `haric` ile ayrılır | Her `SKILL.md`nin tek kayda düşmesi `kapsam-denetimi` ile doğrulanır | 
| 9 | **Şema veya kapsam hatasının sessizce commit edilmesi** | `dogrula` > 0 hata, `kapsam-denetimi` > 0 sorun veya herhangi bir test kırmızı | 3'lü çıkış kapısı commit'i engeller, `olcum.jsonl` `hata_tekrar` sayacı artar | Hatalı kaynak geri alınır, düzeltme sonrası 3'lü kapı yeniden koşulur | 

## 12. Antigravity + Claude Code Ortak Yapılandırma, Model/Efor ve Uygulama Rehberi

### A. Tek Doğruluk Kaynağıyla Çift Araç (Antigravity + Claude Code) Kurulumu

Çift bakım ve senkron bozulması olmaması için kural ve süreç skilleri tek yerde tutulur, iki araç aynı kaynağı okur:

| Katman | Ana Kaynak (Antigravity + Codex) | Claude Code Köprüsü | Amaç ve Kural | 
| ----- | ----- | ----- | ----- | 
| **İnce açılış kuralı (≤ 3 KB)** | Repo kökünde `AGENTS.md` (veya `.agents/rules/`) | Repo kökünde 3 satırlık `CLAUDE.md` → `@AGENTS.md` | K1–K4, onay merdiveni ve 3'lü çıkış kapısı tek metinde tutulur; global klasörler (`~/.gemini`, `~/.claude`) boş kalır | 
| **4 süreç skili (on-demand)** | `.agents/skills/` altında 4 klasör: `yeni-repo-giris`, `skill-kurulum-inceleme`, `aylik-takip-ve-denetim`, `proje-oneri` | Mac'te `.claude/skills` → `../.agents/skills` bağı (symlink); Windows'ta kopya senkronu | Açılışta token yakmaz; yalnız ilgili iş istendiğinde yüklenir | 
| **Kural ve veri motoru (0 token)** | `araclar/` (Python betikleri) + `kaynaklar.json`, `konu-takip.json`, `olcum.jsonl`, `son-aylik-calisma.json` | Birebir aynı dosyalar ve komutlar | İki araç arasında oturum geçişinde tam süreklilik sağlar (bir gün Antigravity, ertesi gün Claude Code) | 
| **Hedef projelere kurulum** | Hedef projede `.agents/skills/` (Antigravity + Codex) | Hedef projede `.claude/skills/` (Claude Code) | `skill-ekle` seçilen araca göre proje içine kurar; genel klasörler boş kalır | 

### B. Hangi Antigravity Aracı Ne Zaman Kullanılmalı?

* **Antigravity App (Sürüm 2.34.0 — Agent odaklı masaüstü uygulaması, ANA ARAÇ):** Faz 1–3 geliştirme, `/plan` ile onaylı plan çıkarma, Orchestrator ile çok adımlı araç yazımı, test koşma ve rutin kütüphane yönetimi burada yürütülür ([Projects](https://antigravity.google/docs/projects/), [Plan](https://antigravity.google/docs/plan/)).

* **Antigravity IDE / Editör eklentisi (YARDIMCI):** Tek tek Python dosyası veya `programlar.json` gibi elle biçimli dosyalarda ince diff kontrolü ve manuel düzenleme yaparken kullanılır ([IDE Extensions](https://antigravity.google/docs/ide/extensions/)).

* **Antigravity CLI (`agy`, OPSİYONEL):** Terminalden hızlı aylık tarama çalıştırma veya `/effort` ile efor bütçesini tek komutla değiştirme için kullanılır ([Effort komutu](https://antigravity.google/docs/cli/commands/effort/)).

### C. Göreve Göre Model ve Efor (Thinking Level) Matrisi

[Antigravity Model ve Efor dokümantasyonuna](https://antigravity.google/docs/models/) göre gereksiz kota harcamamak için her iş kendi ağırlığında çalıştırılır:

| İş Türü | Antigravity Modu ve Modeli | Efor (Thinking Level) | Claude Code Karşılığı | 
| ----- | ----- | ----- | ----- | 
| **Rutin `KESİN` repo girişi, test koşma, küçük doküman işi** | Python (0 token); YZ gerekirse varsayılan model | `Low` veya `Medium` | Varsayılan hızlı/dengeli model | 
| **Faz 1–3 araç geliştirme, şema geçişi, toplu onay aracı** | **Orchestrator** (planlayıcı üst model + hızlı uygulayıcı) + `/plan` | `Medium` (plan aşamasında `High`) | Plan modu + standart kodlama modeli | 
| **Derin güvenlik okuması, gri alan (proxy/tersine mühendislik), mimari çakışma** | Tek üst seviye akıl yürütme modeli (ör. `Gemini 4 Neon`) | `High` (kritik riskte `Extra`) | Yüksek akıl yürütme / planlama modeli | 
| **Aylık takip ve etki raporu** | Önce Python (`arsiv-guncelle --aylik`), YZ yalnız belirsiz/değişenlerde | `Low` / `Medium` | Aynı Python komutu + kısa özet | 

* **Kota koruma kuralı:** Küçük işlerde `/teamwork` veya `Extra` efor açılmaz; her büyük adımdan önce `/plan` ile kısa uygulama planı görülüp onaylanır.

### D. Uygulama Akışı (Birlikte Yürütme Sırası)

1. **Ortak iskeleti kur (10 dk):** `notlar/` içine bu plan dosyasını koy; kök dizinde `AGENTS.md`, `CLAUDE.md` (`@AGENTS.md`) ve `.agents/skills/` (4 süreç skili) + `.claude/skills` bağını oluştur.

2. **Faz 1'i Antigravity App'te `/plan` ile başlat:** `yeni-surec-faz1` dalında yalnız Faz 1'i (şema + `surum_modu` + `olcum.jsonl` + ince açılış) yaptır; 324 test ve `dogrula` 0 hata verince commit at.

3. **Faz 2'yi Orchestrator + `/plan` ile tamamla:** `yeni-surec-faz2` dalında onaysız giriş, `konu-takip` kuyruğu, K-58 otomatik ret, aylık zincir genişletme ve toplu onay aracını kur; 3'lü çıkış kapısı yeşil olunca commit at.

4. **Faz 3'ü gerçek ölçümle kapat:** 1 gerçek yeni repo + 1 gerçek aylık takip çalıştır, `olcum.jsonl` ile 5 sayısal hedefi belirle, çift kayıtları ve `tip` alanını temizle, 14 kabul senaryosunu geçir.

5. **Günlük kullanım:** İster Antigravity App'te ister Claude Code'da aynı komutu ver ("listeyi tara ve yeni repoları işle", "aylık etki raporunu çıkar", "şu projeye skill öner"); ikisi de aynı `AGENTS.md`, aynı 4 skill ve aynı Python araçlarıyla birebir aynı sonucu üretir.

## 13. Git Kontrol, Dallanma, Etiketleme ve Geri Dönüş Protokolü (Adım 0)

Hiçbir plan, kural veya araç değişikliği yapılmadan önce mevcut çalışan yapı Git üzerinde kilitlenir; böylece sürecin her anında sıfır veri kaybıyla eski düzene veya önceki faza dönülebilir.

### A. Başlangıç Güvenlik Kilidi (Hiçbir Dosyaya Dokunmadan Önce)
1. Çalışma ağacının temiz olduğunu doğrula: `git status --short` (boş değilse önce mevcut değişiklikleri commit'le veya stash'le).
2. Mevcut çalışan durumun sabit geri dönüş noktasını etiketle:
   * `git tag -a v0-eski-surec-yedek -m "Yeni surec oncesi calisan kararli durum"`
3. Ana dalı (`main`) koru; hiçbir faz doğrudan `main` üzerinde uygulanmaz.

### B. Faz Bazlı İzole Dallar ve Etiketler
| Aşama | Çalışma Dalı | Bitiş Koşulu | Faz Sonu Etiketi |
| :--- | :--- | :--- | :--- |
| **Adım 0 — Ortak iskelet** | `yeni-surec-iskelet` | `AGENTS.md`, `CLAUDE.md`, `.agents/skills/` (4 skill) ve `.claude/skills` bağı hazır; 324 test yeşil | `v0.1-iskelet-hazir` |
| **Faz 1 — Temel ve ölçüm** | `yeni-surec-faz1` | Şema + `surum_modu` + `olcum.jsonl` + ince açılış; `dogrula` 0 hata + 324 test yeşil | `v1-faz1-tamam` |
| **Faz 2 — Akış ve onay** | `yeni-surec-faz2` | Onaysız giriş + `konu-takip` kuyruğu + K-58 ret + aylık zincir + toplu onay; 3'lü çıkış kapısı yeşil | `v2-faz2-tamam` |
| **Faz 3 — Ölçüm ve temizlik** | `yeni-surec-faz3` | 1 yeni repo + 1 aylık ölçüm, sayısal hedefler, çift kayıt temizliği, `tip` kaldırma, 14 kabul senaryosu yeşil | `v3-yeni-surec-canli` |

* Her faz bir öncekinin temiz dalından açılır; tüm fazlar doğrulandıktan sonra yalnız kullanıcı onayıyla `main` dalına birleştirilir ve GitHub'a `push` edilir.

### C. İstediğin An Geri Dönüş (Rollback) Kuralları
* **Eski düzene anında dönmek (gözlem/karşılaştırma için):** `git switch main` (ana dal hiç bozulmadığı için anında eski çalışan yapıya geçilir).
* **Belirli bir güvenlik etiketinden yeni kurtarma dalı açmak:** `git switch -c kurtarma v0-eski-surec-yedek` (veya `v1-faz1-tamam` / `v2-faz2-tamam`).
* **Tek bir hatalı commit'i güvenle geri almak:** `git revert <commit_hash>` (geçmişi korur).
* **Kesin yasak:** Onaysız `git reset --hard`, `git push --force` ve geçmişi silen rebase komutları yasaktır.