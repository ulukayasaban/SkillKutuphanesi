# SkillKutuphanesi yapısında gereken değişiklikler

Ana plan: [00-plan.md](00-plan.md). Bu belge **öneridir**; onay gelmeden hiçbir araç ya da kural değişmez.

Bugün kütüphane sadece **projeleri** yönetiyor: projeye kurar, kilit kaydı tutar, günceller. Bilgisayarın genelindeki skilleri
sadece okuyor (`globalde` alanı), araç sürümlerini (HyperFrames aracı, OpenMontage) hiç bilmiyor. "Her şey buradan yönetilsin"
için kütüphaneye ikinci bir katman gerekiyor: **makine katmanı**.

Değişiklikler üç aşamada gelir; her aşama ayrı onayla ve ayrı yerel kayıtla (commit) yapılır.

| Aşama | Ne zaman | Ne eklenir | Nereye yazar |
|---|---|---|---|
| A | Dalga 1 | Sadece okuyan makine aracı, makine kaydı, rapor, proje taraması, yedek alma | Kütüphane deposu ve yedek klasörü. Genel skill klasörlerine yazmaz. |
| B | Dalga 2'den önce | Saklama kopyaları, yedeğe taşıma / geri koyma, araç sürümü uyum kontrolü, kural metni | Kütüphane arşivine yazar (paket 0). Genel klasörlere sadece onaylı paketlerle. |
| C | Kapanış | Aylık akış, rehber, promptlar, eski notların düzeltilmesi | Sadece kütüphane deposu |

Aşama B'nin sırası: önce araç değişikliği ve testi → iki skille deneme → kalanlar (ayrıntı 2.2).

---

## 1. Aşama A — sadece okuyan makine katmanı

### 1.1 Yeni araç: `araclar/makine.py`

| Komut | Ne yapar | Nereye yazar |
|---|---|---|
| `--rapor` | Genel skill klasörlerini, bağlantıları, araç sürümlerini, diğer yapay zekâ araçlarının klasörlerini okur; `makine.json` ile karşılaştırır | `notlar/makine-durumu.md` |
| `--kaydet` | Bugünkü durumu `makine.json`'a yazar (ilk kayıt ve senin onayladığın her değişiklikten sonra) | `makine.json` |
| `--proje-tara` | Projeleri sadece okuyarak tarar: kilit kaydı olmayan skill klasörleri · kırık bağlantılar · sabit yol sayısı · HyperFrames sürümü · projedeki kopya ile genel kopya aynı mı | Kendisi dosya yazmaz. Sonucu `proje-kullanimi.py` kendi raporuna (`notlar/proje-kullanimi.md`) ekler; proje adları sadece orada durur. |
| `--yedek <klasör>` | 00-plan 1.2'deki tam yedeği alır, içerik özetlerini ve bağlantı tablosunu yazar | Sadece verilen yedek klasörü (kütüphane deposunun içine yazmayı reddeder) |
| `--yedek-dogrula <klasör>` | Yedeği geçici klasöre açıp asıllarıyla karşılaştırır (geri yükleme provası) | Sadece geçici klasör |

Raporun tabloları:
1. **Genel skiller:** ad · nerede (Claude / Codex / ikisi) · gerçek klasör mü bağlantı mı · bağlantının yazılı hedefi ve gerçekte
   vardığı yer · sınıf · kopyalar aynı mı · **tek kopya mı** · kütüphanede karşılığı var mı (aynı içerik / farklı içerik / yok).
2. **Öne geçenler:** kütüphanede tercih edilen bir skille aynı adı taşıyan genel skiller (bugün 17 ad).
3. **Araçlar:** HyperFrames aracı sürümü, `npx` önbelleğindeki HyperFrames sürümü, OpenMontage sürümü ve yerel yamalı dosyaların
   adları, Python ortamındaki sabit sürümler, dondurma satırları var mı.
4. **Diğer yapay zekâ araçları:** klasör, bugünkü giriş sayısı, beklenen durum (boş / yerleşik).
5. **Değişenler:** `makine.json`'a göre yeni, eksik, içeriği değişmiş girişler.

Sınırlar:
- **Bağlantıları izlemez.** Yedekte bağlantı, bağlantı olarak kopyalanır; kendine dönen bağlantı çifti "döngü" diye kaydedilir.
- **Anahtar dosyalarını açmaz.** Yedeğe olduğu gibi kopyalar (yedek klasörü 700, anahtar dosyaları 600 izinli; karar 7).
  Raporda sadece adı, boyutu ve izinleri görünür; içeriği hiçbir yere yazılmaz.
- **Hiçbir araç çalıştırmaz, hiçbir şey kurmaz.** `npx` önbelleğini sadece okur; `npx` komutu çalıştırmaz.
- Kayıt dosyasını (`~/.agents/.skill-lock.json`) sadece okur.
- Sayımda gizli dosyalar (`.DS_Store`, kayıt dosyaları) ve yerleşik alt klasörler (`.system`, `synced`, `.trash`) hesaba katılmaz;
  bunlar "fazla giriş" diye raporlanmaz.

### 1.2 Yeni kayıt dosyası: `makine.json` (depo kökünde)

İçinde ne var:
- Okunan klasörler ve her birinin beklenen durumu.
- Her genel skill: ad, sınıf, içerik özeti, bağlantı hedefi, karar (`kalacak` / `projeye inecek` / `yedeğe gidecek` / `kararsız`).
- Araçlar: ad, kurulu sürüm, sürümü okuyan komut, sabit tutulacak sürümler, yamalı dosya adları.
- Son yedeğin yeri ve tarihi.

İçinde ne **yok**: proje adı, "şu proje için kalıyor" gerekçesi, anahtar, kullanıcı adı içeren tam yol (yollar `~` ile yazılır).
Hangi projenin hangi genel skile bağlı olduğu yine tek yerde durur: `notlar/proje-kullanimi.md` (kural 6 değişmez).

### 1.3 Proje taramasının genişlemesi

Bugünkü durum: `proje-kullanimi.py` kilit kaydı olmayan projeyi **sessizce atlıyor**. Yani `projeler.json`'a böyle bir proje
yazmak tek başına hiçbir şey göstermez. Bu yüzden sıra şöyledir:

1. **Kod değişikliği (önce):**
   - `proje-kullanimi.py`: proje bulma kısmı kilit kaydı şartı olmadan da çalışabilir. Kilit kaydı olmayan proje raporda
     "kilit yok" diye görünür; rapor boş kilitle de düzgün çıkar.
   - `dogrula.py`: proje adı denetiminin ad listesi kilit kaydından bağımsız üretilir (`projeler.json` → `ek_projeler` adları ve
     `notlar` anahtarları da listeye girer).
   - Ek sütunlar `makine.py --proje-tara` ile gelir (1.1).
   - `test.py`: kilit kaydı olmayan sahte bir projeyle test.
2. **Sonra kayıt:** kilit kaydı olmayan projeler `projeler.json` → `ek_projeler` içine eklenir; `notlar` alanına "üretimde",
   "arşiv, asla temizlenmez", "başkasının deposu, sadece bilgi" gibi elle notlar yazılır.

### 1.4 Denetimler

- `dogrula.py` (**kod değişikliği**; Aşama A yapılacaklar listesindedir): proje adı denetiminin dosya listesine `makine.json` ve
  `notlar/makine-durumu.md` eklenir. Bugün sadece 4 json dosyası taranıyor, `notlar/` hiç taranmıyor. Bu iki dosya yoksa denetim atlanır.
- `dogrula.py` bugün sadece UYARI ve HATA basıyor; BİLGİ düzeyi yok. Bu yüzden "`makine.json` yok ya da 45 günden eski" durumu
  UYARI satırı olur. (İstersen BİLGİ düzeyi ayrıca eklenir; küçük bir tercih, o adımda sorarım.)
- `test.py`: makine aracı için sahte ev klasörüyle testler (gerçek ev klasörüne dokunmadan): bağlantı okuma, kendine dönen
  bağlantı, tek kopya tespiti, yedeğin depo içine yazılmasının reddi, bu iki dosyada proje adı geçince UYARI çıkması.
- `kapsam-denetimi.py`: Aşama A'da değişiklik yok.

---

## 2. Aşama B — saklama kopyaları, taşıma, sürüm uyumu

### 2.1 `makine.py --tasi` ve `--geri-koy` (sadece karar 3 = (a) ise)

Tek işi: bir genel skill girişini **yedeğe taşımak** ya da **yedekten geri koymak**. Silmez, kopyalayıp üzerine yazmaz, içerik değiştirmez.

Güvenlik kuralları (araca gömülü):
- Sadece üç klasörde çalışır: `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`. Kayıt dosyasına, `~/.openmontage`'a,
  talimat ve ayar dosyalarına, `.system` / `synced` / `.trash` gibi yerleşik alt klasörlere **asla** dokunmaz.
- Önce `--kuru` ile paket raporu üretir: hangi girişler, nereye gidecek, her biri için "başka yerde aynısı var mı", kaç proje bu
  ada bağlı. Rapora bir paket numarası verir. `--evet` sadece **görülmüş ve değişmemiş** o paket numarasıyla çalışır.
- Tek kopyası genelde duran bir girişi, kütüphanede ya da doğrulanmış yedekte aynısı yoksa taşımayı reddeder.
- Son tam yedek 30 günden eskiyse çalışmaz.
- Aylık güncellemenin kilidi (`.guncelleme-kilidi`) duruyorsa çalışmaz. Bu, makine aracının yazan bütün komutları için geçerlidir.
- Bir bağlantının gösterdiği asıl klasörü, o bağlantı dururken taşımayı reddeder (önce bağlantı).
- Her işlemi `makine-gunlugu.json`'a yazar (ne, nereden, nereye, ne zaman, paket numarası). `--geri-koy <paket>` bu günlükten çalışır.
- Testlerde gerçek ev klasöründe çalışmayı reddeder; bütün yollar tek bir kök parametresinden türetilir.

Karar 3 = (b) olursa bu iki komut yazılmaz; yerine `--tasi-betigi <paket>` aynı kontrolleri yapıp senin çalıştıracağın tek bir
komut dosyası üretir.

### 2.2 Saklama kopyaları (dondurulmuş HyperFrames skilleri)

**Saklama kopyası:** bir skilin bugün bilgisayarında kurulu duran hâlinin, kütüphanede değişmeden tutulan kopyası.

Bugünkü durum:
- Kütüphanede HyperFrames'ten 14 skill var (eski bir sürümden).
- Emekli 14 skill 2026-10-22'de senin kararınla arşivden çıkarılmıştı (`arsivden_cikarilanlar`). O gün doğru karardı; ama bugün
  iki projen bunlara bağlı ve tek kopyaları genel klasörde.
- Kütüphanenin bugünkü "kaynakta kaldırıldı, eski kopyası korunur" düzeni bu iş için **yetmiyor**. O düzen sadece kütüphanede
  zaten kayıtlı olup kaynaktan sonradan kalkan skilleri korur. Listeden çıkarılmış skilleri atlar, hâlâ yayımlanan bir skilin
  eski hâlini korumaz ve genel klasörden kopya alan bir araç yoktur.

Bu yüzden önce araç değişir. **Araç değişiklikleri (saklama kopyasının ön koşulu):**

1. **Koruma kuralı.** `arsiv-yerlestir.py` ve `arsiv-guncelle.py`, `dondurulmus: true` yazan kayıtları her yeniden kurulumda
   olduğu gibi taşır; kaynakla eşleştirmeye sokmaz. Her saklama kopyası kendine özel bir yol kaydı taşır
   (örnek: `dondurulmus/hyperframes@0.9.23`), böylece güncel kayıtla karışmaz.
2. **Diğer araçlar saklama kopyasını ayrı görür.** `dogrula.py`, `kapsam-denetimi.py`, `proje-kullanimi.py`, bayatlık uyarısı ve
   `skill-ekle.py`'nin kaynak bulma kısmı. Kartında "saklama kopyası" yazar. `skill-ekle.py` kurarken BİLGİ satırı verir
   ("saklama kopyası; güncelleme gelmez").
3. **Yeni komut:** `python3 araclar/makine.py --dondur <skill> [--kuru]`. Genel klasördeki skili sadece okur, kütüphane arşivine
   kopyalar ve kaydını yazar: `dondurulmus`, alındığı klasör, tarih, o günkü araç sürümü. Kimliği `ad@heygen-0.9.23` biçimindedir,
   yani bugünkü tercihleri değiştirmez. Geçerli yedek yoksa çalışmaz.
4. **"Aynı adla kur" seçeneği (`ad_sabit`).** Bugün `@` içeren kimlikler projeye `ad--sonek` klasör adıyla kurulur ve skilin
   içindeki ad da değişir. Projeler ise skili çıplak adıyla çağırıyor. Bu seçenekle saklama kopyası projeye **çıplak adıyla**
   kurulur; kilit kaydı ve çakışma kontrolü yine kimlikle yapılır. Bu seçenek yazılıp `test.py`'de denenmeden saklama
   kopyasından hiçbir projeye kurulum yapılmaz.
5. **"Aylık güncellemede değişmez" sözü** ancak bu değişiklikler ve bunu doğrulayan bir `test.py` testi geçtikten sonra verilir.

**Sıra (paket 0; 00-plan 2.0):**
1. Araç değişiklikleri + testler.
2. **İki skille deneme:** emekli bir skill (`hyperframes-keyframes`) ve hâlâ yayımlanan bir skill (`hyperframes`).
3. Aylık güncellemenin kuru çalıştırması: ikisi de yerinde ve değişmemiş mi.
4. Temizse kalanlar. Emekli 14 skilin `arsivden_cikarilanlar` listesinden çıkarılması tek, ayrı bir yerel kayıtla yapılır.

Deneme başarısız olursa: hâlâ yayımlanan skillerin bugünkü hâli sadece yedekte tutulur, kütüphaneye yalnız emekli olanlar alınır
ve bu bölüm yeniden tasarlanır.

Diğer kurallar:
- Tek kopyası `~/.agents/skills` içinde duran emekli skill (`hyperframes-keyframes`) o hâliyle ana kopya olarak saklanır.
- İki genel klasörde içeriği farklı olan skillerde **iki hâl de** saklanır; varsayılan `~/.claude` hâlidir (karar 9 bunu değiştirebilir).
- Güncel arşiv kaydı ayrı durur; saklama kopyası onu değiştirmez.
- Ücret, lisans, inceleme alanları her kayıt gibi doldurulur (kural 6: sadece kendi niteliğiyle).
- Saklama kopyaları düzenlenmez (kural 3).

### 2.3 Araç sürümü uyumu

- `kaynaklar.json` kaynak kaydına isteğe bağlı alan: `arac_zinciri` = `{ad, kontrol_komutu, uyumlu_surumler}`.
  HyperFrames için: araç `hyperframes`, komut `hyperframes --version`; skillerin alındığı etiket = `v<araç sürümü>`.
- `skill-ekle.py` ön kontrolü: kurulacak skilin istediği araç sürümü ile `makine.json`'daki kurulu sürüm uyuşmuyorsa UYARI
  (kurulumu durdurmaz; rapora yazar).
- `arsiv-guncelle.py` raporu: araç zinciri olan kaynaklarda "kaynak sürümü X, kurulu araç Y" satırı; yeni yayımlanan ya da
  kalkan skill adları; sende başka kaynaktan duran bir adla çakışan yeni ad uyarısı.

### 2.4 Proje kontrollerine eklenenler (`skill-ekle.py --durum` / `--dogrula`)

BİLGİ düzeyinde, kurulumu durdurmadan:
- Projedeki skille aynı adlı bir genel skill var ve içeriği farklı ("bu projede Claude Code genel olanı kullanır").
- Projede kilit kaydı dışında skill klasörü var.
- Projede kırık ya da kendine dönen bağlantı var.

### 2.5 Kural metni (CLAUDE.md ve AGENTS.md) — öneri

Sadece karar 3 = (a) ise kural 1 değişir. Karar 3 = (b) olursa kural 1 bugünkü gibi kalır (genel klasörlere ben hiç yazmam;
hazır komut dosyasını sen çalıştırırsın). Diğer maddeler her iki durumda da eklenir.

**Kural 1 (yeni metin önerisi; karar 3 = (a)):**
> 1. **Proje katmanı:** skiller sadece kullanıcının verdiği proje klasörüne, sadece `skill-ekle.py` ile kurulur.
>    **Makine katmanı** (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`): elle yazma, kopyalama, bağlantı koyma, silme
>    yok. Tek izinli işlem `makine.py --tasi` / `--geri-koy`: geçerli yedek varken, kuru rapor kullanıcıya gösterilip onaylandıktan
>    sonra, sadece yedeğe taşıma ve geri koyma. `~/.openmontage` (içinde git komutu dahil), `~/.agents/.skill-lock.json`, genel
>    talimat ve ayar dosyaları, anahtar dosyası, kabuk ayar dosyası ve genel araç kurulumları (npm, pip) her durumda
>    kullanıcınındır; kütüphane sadece hazır komut ve metin verir.

**Yeni kural 7:**
> 7. Makine katmanında hiçbir işlem yedeksiz yapılmaz ve hiçbir şey silinmez. Her değişiklikten önce `makine.py --rapor`,
>    sonra `--kaydet`. `makine.json` ve makine raporu sadece bilgisayarı anlatır; proje adı ve projeye göre gerekçe yazılmaz.

**Yeni kural 8:**
> 8. Şu komutlar çalıştırılmaz: `hyperframes update`, `upgrade` (`--check` dışında), `skills update`, `init`, `clean`
>    (`--dry-run` dışında); `npx skills …`; `~/.openmontage` içinde `git pull`, `git checkout .`, `git reset --hard`, `git clean`,
>    `make setup`, `make install`, `pip install -U`. Gerekirse kullanıcıya anlatılır, kararı ve çalıştırması kullanıcıdadır.

**Kural 3'e ek:** dondurulmuş saklama kopyaları da düzenlenmez.

**Skill ekleme akışına 0. adım:** makine raporu güncel mi bak; kurulacak adla aynı genel skill varsa raporda söyle.

**Bakım isteklerine yeni satırlar:** "makine raporu", "HyperFrames / OpenMontage sürümü" (02 numaralı belgedeki 3.3 ve 3.10),
"aylık görevden önce depo temiz olmalı" (02 numaralı belgedeki 3.16).

### 2.6 Rol ve profil metinleri

- `roller/video-kompozisyon.json` ve HyperFrames skili içeren diğer roller: ajan talimatına bir satır — "`hyperframes update`,
  `upgrade --project`, `clean`, `skills update` çalıştırma; skiller kütüphaneden gelir".
- `hesap_gizle` ve `skillOverrides` üretimi değişmez. Deney 1'in sonucu "genel skili kapatınca proje kopyası açık kalıyor" çıkarsa,
  `skill-ekle.py`'ye isteğe bağlı "aynı adlı genel skili bu projede kapat" seçeneği ayrıca önerilir (şimdi değil).

---

## 3. Aşama C — kalıcı akış ve belgeler

| Ne | Değişiklik |
|---|---|
| Aylık görev (`skill-kutuphanesi-aylik-guncelleme`) | Sonuna `makine.py --rapor` eklenir; özet, makine değişikliklerini ve araç sürümü farklarını da içerir. Hiçbir şeyi taşımaz, yükseltmez. |
| `rehber/11-makine-katmani.md` (yeni) | Genel klasörler, hangi araç neyi okur, rapor nasıl okunur, taşıma ve geri koyma, yedek düzeni. |
| `rehber/12-hyperframes-ve-openmontage.md` (yeni) | Sürüm eşleşmesi, dondurma satırları, yasak komutlar, yükseltme ve geri dönüş adımları, yamalar, saklama kopyaları. |
| `rehber/02`, `04`, `05` | Aylık akışa makine kontrolü; kontrol listesine yeni maddeler; risk listesine bu plandaki kayıp yolları. |
| `promptlar/13-makine-raporu.md` (yeni) | "Bilgisayarın genelindeki skillerin durumunu göster." |
| `promptlar/14-arac-surumu-degisikligi.md` (yeni) | "HyperFrames / OpenMontage'ın yeni sürümü var; ne yapalım?" |
| `promptlar/15-proje-denetimi.md` (yeni) | 01 numaralı belgedeki genel denetim promptunun (4A) kalıcı hâli. |
| `promptlar/README.md`, `README.md`, `AGENTS.md` | Yeni araç, yeni kurallar, yeni promptlar. |
| `PLAN.md` | "Makine katmanı" bölümü. |

---

## 4. Bu vesileyle düzeltilecek eski kayıtlar

| # | Sorun | Düzeltme |
|---|---|---|
| 1 | `kaynaklar.json` → HyperFrames `bagimlilik` notu emekli skill adlarını (`/general-video`, `/faceless-explainer`…) güncelmiş gibi anıyor | Not güncellenir |
| 2 | Kütüphanedeki HyperFrames arşivi eski (`f8309b3`); yeni yayımlanan `style-sampling` yok | Araç sürümüyle aynı etikete çekilir (ayrı dal, onay). Aylık güncelleme çalışırken yapılmaz; saklama kopyaları yerine oturduktan sonra yapılır. |
| 3 | OpenMontage'dan gelen kayıtların hepsi AGPL-3.0 etiketli; çoğu başka kaynaklardan alınmış MIT skiller | Lisans alanı skil bazında düzeltilir; emin olunamayan "belirsiz" yazılır |
| 4 | OpenMontage kaynak notu "genelde zaten kurulu" diyor; Dalga 2'den sonra yanlış olacak | Dalga 2 kapanışında güncellenir |
| 5 | OpenMontage'ın 75 bağlantı kaydı (`~/.config/openmontage/global-skill-links.txt`) 79 satır, 4'ü ölü | Dosya senin. Önce yedeği alınır; düzeltilmiş hâlini ve farkı tek dosya olarak hazır veririm, sen uygularsın. |
| 6 | `elle-kurulan.json` sadece raporda okunuyor, kurulum kontrolünde kullanılmıyor | 2.4'teki "kilit kaydı dışında skill" kontrolüyle birleştirilir |
| 7 | `~/Documents/Claude/yedek/global-skills-2026-11-08` yedeğindeki bağlantılar yerinde kırık | Yeni tam yedek alınınca "eski, eksik" diye not düşülür; silme kararı senin |
| 8 | Oturum hafızasındaki "global skill temizliği" notu eski | Güncellenir |
| 9 | 17 ad: kütüphanenin tercih ettiği skil yerine her projede OpenMontage kopyası öne geçiyor | 00-plan 2.2 kararına (6a) bağlı |

---

## 5. Bilerek yapılmayacak yapı değişiklikleri

- **HyperFrames eklenti kanalına geçiş:** sadece 9 skill, Codex'e yaramıyor, kilit kaydıyla izlenemiyor. Aylık raporda yeniden bakılır.
- **Genel klasörlere kütüphaneden kurulum** (`skill-ekle.py --global` gibi): genel skill her projede öne geçer; hedefin tersine çalışır.
- **`npx skills` kayıt dosyasını kütüphanenin yönetmesi:** dosya başka bir aracın; düzenlenirse o araç yanlış karar verir.
- **Uzun ömürlü ayrı dal:** her aşama küçük, ayrı kayıtla ana dala girer; aylık güncelleme düzeni değişmez.
- **OpenMontage kodunun kütüphaneye alınması:** kütüphane sadece skilleri arşivler; kod, Python ortamı ve yamalar yerinde kalır, yedekle korunur.
- **Kendiliğinden düzeltme:** makine raporu fark bulunca hiçbir şeyi kendisi düzeltmez.
- **Diğer yapay zekâ araçlarına (Cursor, Gemini, Copilot, OpenCode) kurulum hedefi:** bugün ihtiyaç yok; istenirse `skill-ekle.py`'ye
  yeni hedef olarak ayrıca tasarlanır.

---

## 6. Her aşamanın sonunda

`python3 araclar/kapsam-denetimi.py` (0 sorun) · `python3 araclar/dogrula.py` (0 hata) · `python3 araclar/test.py` · yerel kayıt
(commit). GitHub'a gönderme sadece sen isteyince. Yerel kayıt, 1 Aralık aylık görevinin çalışabilmesi için de gereklidir
(02 numaralı belge, 3.16).
