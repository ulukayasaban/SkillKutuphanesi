# HyperFrames + OpenMontage: merkezi yönetim planı

**Tarih:** 2026-11-10 · **Durum:** ONAY BEKLİYOR · **Bu belge sadece plandır.** Onay gelmeden hiçbir kurulum, kaldırma,
taşıma ya da GitHub'a gönderme yapılmaz.

Ek belgeler: [01-proje-promptlari.md](01-proje-promptlari.md) · [02-yapilacaklar-listesi.md](02-yapilacaklar-listesi.md) ·
[03-kutuphane-degisiklikleri.md](03-kutuphane-degisiklikleri.md)

Sözcükler: **genel skill** = bilgisayarın genelinde duran, her projede görünen skill (`~/.claude/skills`, `~/.agents/skills`,
`~/.codex/skills`). **proje skili** = projenin kendi klasöründe duran skill. Diğer terimler ve araç adları en altta (bölüm 10).

Bu plan, yazıldıktan sonra yedi ayrı açıdan bağımsız olarak denetlendi; bulunan 37 eksik bu sürümde düzeltildi.

---

## 1. Kısa cevap

**Senin sorularına tek cümlelik cevaplar**

| Soru | Cevap |
|---|---|
| Kaldırıp temiz kurulum yapalım mı? | Hayır. Bugün kaldırırsak geri gelmeyecek parçalar var (bölüm 3). Yerinde, adım adım düzenliyoruz. |
| Projelerde ne yapacağım? | IstatistikYoutube oturumuna 1A promptunu yapıştır; sonra Akıl Dışı'na 2A, Psikolojik Danışman'a 3A (01 numaralı belge). İlk promptların hepsi sadece okur ve rapor yazar. |
| Her şeyi buradan yönetebilecek misin? | Evet. Kütüphaneye `makine.py` adlı bir araç eklenir. Dalga 1'de sadece okur. Dalga 2'de yalnızca onayladığın paket için iki iş yapar: "yedeğe taşı" ve "geri koy". |
| Yapılacaklar listesi nerede? | 02 numaralı belge: bölüm 2 (bu geçiş), bölüm 3 (güncelleme, sürüm değişikliği gibi tekrarlayan işler). |
| Kütüphanenin yapısında ne değişecek? | 03 numaralı belge: üç aşama (A: sadece okuyan araç, B: taşıma ve saklama kopyaları, C: kalıcı akış). |

**Özet**

1. **Temiz kurulum yapmıyoruz.** Bunun yerine her şeyi yerinde, adım adım ve geri alınabilir biçimde düzenliyoruz.
   Hiçbir şey silinmez; kalkan her şey yedeğe taşınır.
2. **İki dalga var.**
   - **Dalga 1:** yedek, rapor, proje denetimi. **Genel skill klasörlerine dokunulmaz.** Değişen dört şey olur:
     (1) `~/.zshenv` dosyasına senin ekleyeceğin 3 satır, (2) yaklaşık 27–32 GB'lık yedek klasörü, (3) kütüphaneye eklenen
     sadece okuyan araç ve raporlar, (4) projelerde senin onayladığın onarımlar.
   - **Dalga 2:** genel skillerin azaltılması ve (istersen) sürüm yükseltmeleri. Dalga 1'in bütün kontrolleri yeşil olmadan başlamaz.
3. **Sonunda:** her projenin skilleri kendi içinde durur ve kütüphanedeki kilit kaydıyla izlenir. Bilgisayar genelinde sadece
   bilerek bırakılan birkaç skill kalır ve onlar da kütüphanede kayıtlıdır. HyperFrames ve OpenMontage sürümleri kütüphanede
   tek bir dosyada yazılıdır; bir şey kendiliğinden değişirse aylık kontrol bunu söyler.
4. **Projeler için:** her proje kendi oturumunda, hazır promptla önce sadece okunur ve raporlanır. Sıra: IstatistikYoutube →
   Akıl Dışı → Psikolojik Danışman → diğerleri (sadece rapor) → Etsy-Arif (sadece bilgi, Arif'in deposu).

---

## 2. Bugünkü durum (2026-11-10'da ölçüldü)

| Konu | Durum |
|---|---|
| HyperFrames komut satırı aracı | `0.9.23` kurulu (`/usr/local/bin/hyperframes`). En yeni sürüm `0.9.29`. |
| HyperFrames'in resmî skill listesi | Artık **9 skill** yayımlıyor. **14 skill emekli** oldu (yayından kalktı), 6 skill sadece kendi iç kullanımları için. |
| Genel skiller, Claude (`~/.claude/skills`) | 104 giriş (`.DS_Store` sayılmadan): 75'i OpenMontage klasörüne bağlantı, 6'sı `~/.agents/skills`'e bağlantı, 21 gerçek skill klasörü, 2 yerleşik klasör (`.trash`, `synced`; bunlara dokunulmaz). |
| Genel skiller, Codex (`~/.agents/skills`) | 27 gerçek klasör. Kayıt dosyasında 16'sı HyperFrames kaynaklı, 11'i "yerel" (nereden kurulduğu kayıtta yok, kaynağı bulunamıyor). |
| `~/.codex/skills` | 13 giriş: 11 bağlantı (8'i `~/.claude/skills`'e, 3'ü `~/.agents/skills`'e) + 1 gerçek skill klasörü (`playwright`) + Codex'in yerleşik klasörü (`.system`; kütüphane buna dokunmaz). |
| Aynı skilin farklı hâlleri | HyperFrames ailesinden 10 skilin `~/.claude` ve `~/.agents` kopyaları birbirinden farklı. |
| OpenMontage | `~/.openmontage`, sürüm `c806645`. Kaynak depo 244 commit (kayıt) ileride; çoğu eski birleştirme kaydı, gerçekte 283 dosya değişmiş. **9 dosyada senin yerel yaman var.** Python ortamı 3,3 GB, sürümleri sabit (yükseltilmemeli). |
| OpenMontage → HyperFrames | OpenMontage, HyperFrames'i sürüm belirtmeden (`npx --yes hyperframes`) çağırıyor. Hangi sürümün çalışacağı bilgisayardaki npx önbelleğine bağlı; bu sürüm bugün hiçbir yerde kayıtlı değil. |
| Kütüphane | HyperFrames arşivi eski bir sürümde (`f8309b3`, 14 kayıt). OpenMontage arşivi `195eab2`. Yani üç farklı OpenMontage sürümü var: kurulu, arşiv, kaynak. |
| Diğer yapay zekâ araçları | Cursor, Gemini, Copilot, OpenCode genel skill klasörleri **boş** (bugün temizlendi). Kendi yerleşik skilleri duruyor. |
| Ortam ayarı | HyperFrames'i donduran satırlar (`HYPERFRAMES_…`) **henüz yok**. |
| Yedek | Disk: 153 GB boş. **Time Machine kurulu değil**, yani şu an ikinci bir kopya yok. `Documents` iCloud'a eşitlenmiyor görünüyor. |
| Aylık görev | Kütüphanenin aylık güncelleme görevi **1 Aralık 2026 10:00**'da çalışacak. Depoda kaydedilmemiş dosya görürse durur (bölüm 5, adım 1.0). |
| O anda çalışan iş | Kontrol sırasında bir HyperFrames render işlemi çalışıyordu (başka bir oturum). Yedek ve denetim, üretim yapılmayan bir anda başlamalı. |

Projeler (ayrıntı: `notlar/proje-kullanimi.md` ve 01 numaralı belge):

| Proje | Bu iki araçla ilişkisi | Bugünkü risk |
|---|---|---|
| IstatistikYoutube | Genel HyperFrames aracıyla render alıyor; 8 genel skili bilerek açık tutuyor; 61 dosya OpenMontage Python ortamının yolunu kullanıyor. Kendi skili ve kodu genel klasördeki iki yola doğrudan bağlı (`hyperframes-core`, `design-dna`). | Genel skiller ya da araç sürümü değişirse üretim hattı etkilenir. Git deposu değil. |
| Akıl Dışı Youtube Kanalı | Kendi içinde 24 kütüphane skili + 8 kendi skili. Codex ajan dosyaları genel klasördeki 9 skill yoluna bağlı; bunların hiçbiri projede aynı adla yok. 34 betik artık olmayan bir geçici klasör yolunu çağırıyor. İki emekli skile (`faceless-explainer`, `general-video`) bağlı. `hyperframes-creative` birbirini gösteren kırık bir bağlantı çifti. | Git deposu değil. Emekli skiller sadece genelde duruyor. Projedeki bazı kopyalar genel kopyalardan eski. |
| Psikolojik Danışman Sosyal Medya | OpenMontage'ı eski yerinde (`~/Documents/OpenMontage`) arıyor; o klasör yok. | Zaten kırık; kayıp riski yok, onarım gerekiyor. |
| blenderTest, Etsy-Yeni, AntigravityTest2, IsBasvuruClaude, Yetisio, Tekfen Araştırma Sonuçları, IstatistikYoutube-Arsiv | Bir kısmında kilit kaydı olmayan skiller var. | Arşiv klasörü eski HyperFrames skillerinin tek kopyası olabilir; asla silinmez. |
| Etsy-Arif | OpenMontage kaynaklı 3 skill kurulu, içerikleri bugün genel kopyalarla aynı. | Arif'in deposu; sadece bilgi. |

---

## 3. Neden temiz kurulum değil

| Kaldırıp yeniden kurarsak | Sonuç |
|---|---|
| HyperFrames skillerini yeniden kurmak | Araç artık sadece 9 skill kuruyor. Emekli 14 skill **geri gelmez**. Akıl Dışı'nın bağlı olduğu `faceless-explainer` ve `general-video` bunların içinde. |
| OpenMontage'ı yeniden indirmek | 9 dosyadaki yerel yamaların, izlenmeyen dosyaların (`gfpgan/`, `clips_cache/`, `projects/`, yedek dosyalar) ve anahtar dosyasının kaybı. |
| Python ortamını yeniden kurmak | Bu bilgisayarda (Intel Mac) sabitlenmiş sürümler (torch 2.2.2, numpy 1.26.4, mediapipe…) ve elle yapılmış yama bozulur. Kaynak depo artık Python 3.11 istiyor; senin ortamın 3.10. |
| Genel skilleri silip kütüphaneden kurmak | Kütüphanedeki HyperFrames arşivi eski; bugün kullandığın sürümle aynı değil. Bazı skillerin tek kopyası genel klasörde (`hyperframes-keyframes`, `nlm-skill`, `youtube-arama`, `openmontage` giriş skili…). |

Karar: **yerinde düzenleme.** "Temiz kurulum" sadece son çare olarak, sadece skill klasörleri için ve şu dört koşulla düşünülür:
yerinde düzenleme başarısız olduysa, yedekten geri yükleme denenmiş ve çalışmışsa, bugünkü skillerin kopyası kütüphanede
duruyorsa, projelerin taban testleri kayıtlıysa. Python ortamı ve OpenMontage klasörü hiçbir koşulda yeniden kurulmaz.

---

## 4. Hedef durum

- **Proje skilleri:** her projenin ihtiyacı olan skiller projenin içinde, `skill-ekle.py` ile kurulmuş ve kilit kaydında.
  Proje, hangi HyperFrames sürümüyle yazıldıysa o sürümün skillerini kendi içinde taşır.
- **Genel skiller:** sadece bilerek bırakılanlar (öneri: `openmontage` giriş skili, `youtube-arama`, `nlm-skill`, `design-dna`;
  kesin liste Dalga 1 raporundaki tablodan senin onayınla çıkar). Hepsi kütüphanede `makine.json` içinde adı ve kontrol
  koduyla (dosya içeriğinin kısa özeti, "checksum") kayıtlı.
- **Emekli ve bugünkü HyperFrames skilleri:** kütüphanede değişmeyen bir saklama kopyası ("dondurulmuş kopya") olarak durur.
  İstenen projeye buradan, **aynı adla** kurulur. Kaynak depoda kaybolsa bile sende kalır.
- **Araç sürümleri:** HyperFrames aracı, OpenMontage sürümü, OpenMontage'ın çağırdığı HyperFrames sürümü, yerel yamalar ve
  sabit Python sürümleri kütüphanede tek dosyada yazılı. Yükseltme ancak senin kararınla, proje testlerinden sonra.
- **Diğer yapay zekâ araçları:** genel skill klasörleri boş kalır; aylık kontrol dolup dolmadığına bakar.
- **Kendiliğinden değişim yok:** HyperFrames'in skilleri ve kendini kendiliğinden güncellemesi ortam ayarıyla kapalı.

---

## 5. Dalga 1 — genel skill klasörlerine dokunulmaz

Her adımda: **ne yapılır · kim yapar · neye dokunur · nasıl geri alınır**.

### 1.0 Ön kontrol
- **Ne:** O anda render, güncelleme ya da kütüphane aracı çalıştıran başka oturum var mı; disk yeterli mi; **kütüphane deposu
  temiz mi** (kaydedilmemiş dosya yok mu); **1 Aralık aylık görevi** bu işle çakışıyor mu.
- **Aylık görev kuralı:** Görev, depoda kaydedilmemiş dosya görürse durur. Bu yüzden bu planın her adımından sonra depoya
  yerel kayıt (commit) yapılır. Dalga 2 projelere ya da genel klasörlere yazarken görev çalışmamalı; gerekirse görevi bir
  kereliğine ertelerim (ayrıntı: 02 numaralı belge, 3.16). Görevin "durduruldu" demesi hata değildir, beklenen davranıştır.
- **Rapor klasörü:** projelerin raporlarını yazacağı `~/Documents/Claude/hf-om-raporlar/` klasörünü ben açarım.
- **Kim:** ben. **Dokunduğu yer:** sadece o boş rapor klasörü.
- **Sana soru:** Bugünkü temizlikten kalan çalışan bir oturum ya da komut var mı? Önümüzdeki günlerde yetişmesi gereken bir video var mı?
  (Varsa o proje için adımlar üretimden sonraya bırakılır.)

### 1.1 Dondurma satırları (ilk iş)
- **Ne:** HyperFrames'in genel skilleri yeniden kurmasını ve kendini güncellemesini kapatan 3 ayar satırı (üstüne 1 açıklama satırı eklenir).
- **Kim:** **sen** (kabuk ayar dosyasına ben yazmıyorum). Tek komut:

```bash
printf '\n# HyperFrames: skiller ve arac kendiliginden guncellenmesin (SkillKutuphanesi plani)\nexport HYPERFRAMES_SKIP_SKILLS=1\nexport HYPERFRAMES_NO_AUTO_INSTALL=1\nexport HYPERFRAMES_NO_UPDATE_CHECK=1\n' >> ~/.zshenv
```

- **Kontrol:** yeni bir Terminal penceresinde `env | grep HYPERFRAMES` çalıştır. Çıktı tam olarak şu 3 satır olmalı:
  `HYPERFRAMES_SKIP_SKILLS=1`, `HYPERFRAMES_NO_AUTO_INSTALL=1`, `HYPERFRAMES_NO_UPDATE_CHECK=1`. Ben de yeni açılan oturumdan doğrularım.
- **Geri alma:** `~/.zshenv` dosyasında `# HyperFrames:` ile başlayan açıklama satırını ve altındaki 3 `export` satırını sil.
- **İsteğe bağlı:** kullanım bilgisi gönderimini (telemetri) de kapatmak istersen ayrıca şunu çalıştır:
  `printf 'export HYPERFRAMES_NO_TELEMETRY=1\n' >> ~/.zshenv`. Eklersen kontrolde 4. satır olarak görünür; geri alırken onu da silersin.
- **Neden ilk iş:** bu satırlar yokken Terminal'de elle çalıştırılan bir `hyperframes` komutu aracı kendiliğinden yükseltebilir;
  `hyperframes init`, `update` ya da `skills update` genel klasördeki skillerin üzerine yazabilir ve boşalttığımız diğer araç
  klasörlerini yeniden doldurabilir.

### 1.2 Tam yedek
- **Ne:** Aşağıdakilerin tam kopyası, `~/Documents/Claude/yedek/makine-2026-11-10/` içine (kütüphane deposunun dışında).
  - Genel skill klasörleri: `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`; kayıt dosyası `~/.agents/.skill-lock.json` ve eski yedeği.
  - Bağlantı tablosu: her bağlantının adı, yazılı hedefi ve gerçekte vardığı yer (yedeğin doğrulanması için şart).
  - `~/.claude` içinden: `commands`, `agents`, `CLAUDE.md`, ayar dosyaları, eklenti kayıtları.
  - `~/.hyperframes` ve `~/.cache/hyperframes/history` (708 MB; proje geçmişi).
  - `~/.openmontage` klasörünün tamamı (Python ortamı ve `node_modules` ayrı paketlerde), uv Python kurulumu
    (`~/.local/share/uv/python/cpython-3.10-macos-x86_64-none`), kurulu paket listesi, yerel yamaların fark dosyası,
    `~/Movies/OpenMontage`, `~/.config/openmontage`.
  - OpenMontage'ın kullandığı model dosyaları: `~/.piper` (60 MB, Türkçe ses), `~/.u2net` (336 MB), `~/.cache/huggingface` (6,0 GB).
  - HyperFrames aracının kurulum paketleri: 0.9.23 ve projelerin sabitlediği 0.8.142 / 0.8.143 (ileride geri dönebilmek için).
  - Git deposu olmayan projeler: Akıl Dışı (3,1 GB), IstatistikYoutube (4,3 GB), IstatistikYoutube-Arsiv (1,1 GB), Psikolojik
    Danışman, blenderTest, Etsy-Yeni, AntigravityTest2, IsBasvuruClaude, Tekfen Araştırma Sonuçları. Yetisio sadece kaydedilmemiş değişiklik varsa.
    Etsy-Arif kopyalanmaz (Arif'in deposu, GitHub'da duruyor).
- **Bağlantılar:** yedek bağlantıları izlemez; her bağlantı bağlantı olarak, yazılı hedefiyle kaydedilir. Akıl Dışı'ndaki
  birbirini gösteren `hyperframes-creative` çifti de böyle kaydedilir ve tabloda "döngü" diye işaretlenir.
- **Anahtar dosyaları** (`~/.config/openmontage/.env` ve eski yedeği): dosya açılmadan ve içeriği hiçbir yere yazdırılmadan,
  olduğu gibi kopyalanır. Yedek klasörü yalnızca senin kullanıcına açık olur (klasör 700, anahtar dosyaları 600). Raporlarda
  sadece dosyanın adı, boyutu ve izinleri görünür. Yedek klasörü bulut eşitlemesine (iCloud vb.) konmaz. İstemezsen bu iki
  dosya yedeğe alınmaz, kendi şifre yöneticinde saklarsın (karar 7).
- **Kim:** ben, onayınla. **Dokunduğu yer:** sadece yedek klasörü. Kaynak klasörlerden sadece okunur.
- **Yer:** yaklaşık 27–32 GB (bunun yaklaşık 6,4 GB'ı model dosyaları); diskte 153 GB boş. Kesin toplam yedek alınırken ölçülüp yazılır.
- **İkinci kopya:** Time Machine kurulu değil. Harici diskin varsa yedek klasörünü oraya da kopyalamanı öneririm (karar 4;
  komut 02 numaralı belgede). Anahtar dosyaları yedekteyse harici disk şifreli olmalı.
- **Geri alma:** yedek klasörünü silmek (hiçbir şeyi etkilemez).

### 1.3 Geri yükleme provası
- **Ne:** Yedek, geçici bir klasöre açılır ve asıllarıyla karşılaştırılır:
  - dosyaların kontrol kodları aynı mı; bağlantılar aynı hedefi gösteriyor mu; kayıt dosyası 27 kayıt mı;
  - OpenMontage kopyasına yama fark dosyası temiz uygulanıyor mu;
  - "bağlantı gerçek klasöre dönüşmüşse nasıl geri konur" ve "birbirini gösteren bağlantı çifti nasıl geri konur" senaryoları;
  - Piper Türkçe sesi, u2net ve diğer model dosyaları yedekte boyut ve kontrol koduyla asılla aynı mı.
- **Python ortamı:** yedekteki kopyanın kendi `python` dosyasıyla yalnızca `import torch, numpy` denenir ve sürümler sabit
  sürümlerle karşılaştırılır. Kopyada paket kurma ya da ortamın içindeki başka komutları çalıştırma **yapılmaz** (bu komutlar
  asıl ortamın yoluna bağlıdır, asıl ortamı değiştirebilir). Deneme sonuç vermezse ortamın geri yüklenebilirliği
  "doğrulanmadı" diye yazılır; o durumda güvence paket listesi ve uv Python kopyasıdır.
- **Kim:** ben. **Dokunduğu yer:** sadece geçici klasör.
- **Kapı:** bu prova geçmeden Dalga 2'nin hiçbir adımı başlamaz.

### 1.4 Makine raporu ve proje taraması
- **Ne:** Kütüphaneye sadece okuyan yeni bir araç eklenir (`araclar/makine.py --rapor`) ve ilk rapor üretilir
  (`notlar/makine-durumu.md`). Raporda:
  - Bütün genel skiller tek tabloda: adı, sınıfı (HyperFrames yayımlanan / emekli / dahili · OpenMontage bağlantısı · sana özel ·
    diğer), kaç yerde kopyası var, kopyalar aynı mı, **tek kopya mı**.
  - Araç sürümleri ve uyum: HyperFrames aracı ↔ skill sürümü ↔ OpenMontage sürümü; yamalar; sabit sürümler; OpenMontage'ın
    `npx` ile çağırdığı HyperFrames sürümü (npx önbelleği sadece okunarak; `npx` çalıştırılmaz).
  - Diğer yapay zekâ araçlarının klasörleri (boş mu).
  - Bütün projelerin taraması: kilit kaydı olmayan skiller, kırık ya da kendine dönen bağlantılar, genel klasöre sabit yollar,
    projenin sabitlediği HyperFrames sürümü, **projedeki kopya ile aynı adlı genel kopya aynı mı**.
- **OpenMontage taban ölçümü:** OpenMontage'ın kendi durum/ön kontrol komutları (sadece okuyan) çalıştırılır ve sonuç
  kaydedilir. İstersen, onayınla, ücretli servis kullanmayan kısa bir yerel render da alınır. Psikolojik Danışman hattı ve
  `ink-art` bu ölçümün dışında ("pasif") diye yazılır.
- **Kim:** ben. **Dokunduğu yer:** sadece kütüphane deposu (yeni araç + rapor; yerel kayıt, GitHub'a gönderme yok).

### 1.5 Üç deney
Geçici bir klasörde, gerçek ayarlara dokunmadan:
1. Bir genel skili bir projede kapatınca, projenin içindeki aynı adlı kopya da kapanıyor mu? (Kapanmıyorsa projeler, genel skill
   dururken bile kendi sürümünü kullanabilir.)
2. Claude Code `~/.agents/skills` klasörünü gerçekten okumuyor mu?
3. Codex `~/.codex/skills` klasörünü okuyor mu; ajan dosyasına yazılı tam yoldaki skili gerçekten yüklüyor mu?

- **Kim:** ben denerim; giriş gerektirirse sana tek satırlık komut veririm.
- **Sonuç alınamazsa:** "doğrulanmadı" yazılır ve en temkinli yol seçilir (ilgili kolaylık kullanılmaz, ilgili klasöre dokunulmaz).

### 1.6 Proje oturumları
Her proje **kendi oturumunda**, 01 numaralı belgedeki promptla. Üç parça: (A) sadece oku ve raporla, (B) onayladığın onarım,
(C) doğrulama. Sıra ve her birinde beklenen iş:

1. **IstatistikYoutube** — taban testi (`duman.sh`, 0.9.23 ile; son kayıt 0.9.20'de 94/0), sabit yolların ve kapatılmış
   skillerin dökümü. **Üretim hattında değişiklik yok;** yalnızca onayladığın taban testi kendi test klasörüne
   (`_test/duman-cikti/`) ve HyperFrames önbelleğine (`~/.cache/hyperframes`) test çıktısı yazar.
   Dokunulmayacaklar: 8 açık genel skill, Python ortamı yolu, 122 kapatma ayarı.
2. **Akıl Dışı** — kırık bağlantılar, Codex ajan dosyalarındaki sabit yollar, 34 betikteki ölü yol, sürüm sabitlemeleri.
   Onayınla onarım: ajan dosyalarındaki yollar, **2.1'deki eşleme tablosuna göre** ve yalnızca hedefi projede bugün var
   olanlar için proje içine çevrilir. Betiklerde yalnızca hâlâ kullandıkların ve sürümü rapordan bilinenler düzeltilir (her
   dosyanın yedeği alınarak). Projede henüz olmayan skiller (`faceless-explainer`, `general-video`,
   `hyperframes-animation`, `-audio`, `-keyframes`) Dalga 2'de (2.0 ve 2.1) kurulur.
   **`hyperframes-creative` bağlantı çifti** proje oturumunda onarılmaz: yedek ve prova bittikten sonra, onayınla, bu
   oturumdan onarılır (iki kırık bağlantı yedeğe taşınır, gerçek kopya `skill-ekle.py` ile önce raporlanıp sonra kurulur; karar 8).
3. **Psikolojik Danışman** — OpenMontage yolu `~/.openmontage` olarak düzeltilir ya da hat "pasif" diye işaretlenir (karar 11).
4. **blenderTest ve diğerleri** — sadece rapor; kilit kaydı önerisi.
5. **Etsy-Arif** — sadece bilgi raporu, sadece istersen; hiçbir dosya değişmez.

Skill kurulumu gerektiren her şey bu oturumdan, `skill-ekle.py` ile ve her zamanki akışla (önce rapor, sonra onay) yapılır.

### 1.7 Dalga 1 kapanışı
Tek sayfalık sonuç: bölüm 7'deki kapıların durumu, açık kalanlar, Dalga 2 için önerilen paketler. Dalga 2 ancak bundan sonra
ve ayrı onayla başlar.

---

## 6. Dalga 2 — bilgisayar genelindeki değişiklikler (ayrı onay, acele yok)

Her adımda: **ne yapılır · kim yapar · neye dokunur · nasıl geri alınır.**

Her adım küçük paketlerle yapılır. Her paket için önce "ne taşınacak" raporu gösterilir, onaylarsan uygulanır, ardından kırık
bağlantı taraması ve proje kontrolü çalışır. Taşınan her şey `~/Documents/Claude/yedek/makine-<tarih>/tasinanlar/` altına
gider; taşınanları geri koymak tek komuttur. Taşıma dışındaki değişikliklerin (proje kopyaları, metin düzeltmeleri,
OpenMontage güncellemesi) geri alma yolu her adımda ayrıca yazılıdır. Hepsinin esas dönüş yolu 1.2'deki yedek ve 1.3'te
denenmiş geri yüklemedir.

### 2.0 Paket 0 — bugünkü HyperFrames skillerini kütüphanede sakla (kütüphaneye yazar)
- **Ne:** Genel klasörlerde bugün duran HyperFrames ailesi (yayımlananlardan kurulu olanlar + emekli 14 + dahili 6), bugünkü
  hâliyle kütüphaneye değişmeyen saklama kopyası olarak alınır. `hyperframes-keyframes` emekli 14'ün içindedir, ayrıca
  sayılmaz; tek kopyası `~/.agents/skills` içindedir ve o hâliyle saklanır. Bir skilin iki klasördeki içeriği farklıysa iki
  hâli de saklanır; varsayılan `~/.claude` hâlidir. Kesin liste ve toplam sayı 1.4 raporundan gelir. Her kopyanın yanına
  nereden, hangi tarihte, hangi araç sürümüyle alındığı yazılır.
- **Ön koşul — önce araç değişikliği:** Kütüphanenin bugünkü araçları saklama kopyasını tanımıyor: aylık güncelleme böyle bir
  kopyayı sessizce düşürebilir ve bu kopyalar projeye farklı bir adla kurulur. Bu yüzden önce 03 numaralı belgedeki araç
  değişiklikleri yapılır ve test edilir (saklama kopyasını koruyan kural, `makine.py --dondur` komutu, "aynı adla kur"
  seçeneği). Bunlar bitmeden hiçbir kopya alınmaz.
- **Sıra:** araç değişikliği + test → iki skille deneme (emekli `hyperframes-keyframes` ve hâlâ yayımlanan bir skill) → aylık
  güncellemenin kuru çalıştırmasında iki kopyanın da yerinde durduğunun görülmesi → geri kalanlar.
- **Kim:** ben. **Dokunduğu yer:** sadece kütüphane deposu. Genel klasörlerden sadece okunur. Depo private kalır.
- **Geri alma:** kütüphane git geçmişinden önceki kayda dönülür.
- **Kapsam dışı:** projelerin kendi yazdığı skiller (Akıl Dışı'nın 8, IstatistikYoutube'un 22 skili) projede kalır; proje
  yedeğiyle korunur ve proje kullanım raporunda "kilit kaydı dışında" diye görünür. Sana özel genel skiller (`openmontage`
  giriş skili, `youtube-arama`, `nlm-skill`) `makine.json`'da kayıtlı, içerikleri yedekte durur.
- **Senin kararın gerekli** (karar 5). "Hayır" dersen kopyalar yalnızca 1.2 yedeğinde kalır; o zaman projelere kurulum
  yapılamaz ve o projelerin bağlı olduğu genel skiller yerinde bırakılır.

### 2.1 Projelere kendi kopyalarını kur
- **Ne:** Bir projenin bağlı olduğu her genel skill, **aynı içerikle ve aynı adla** projenin içine kurulur (`skill-ekle.py`,
  2.0'daki kopyalardan; önce rapor, sonra onay).
- **Ad kontrolü:** kurulan klasörün adı ve skilin içindeki `name` alanı genel kopyayla **aynı** olmalı. Farklı çıkarsa
  (örneğin `hyperframes--heygen-0.9.23`) kurulum reddedilir; çünkü genel kopya kalktığında proje o adı bulamaz.
- **İçerik karşılaştırması:** Genel kopya dururken Claude Code genel olanı kullanır. Genel kopya kalkınca projedeki kopya
  devreye girer. Bu yüzden projede **zaten duran** aynı adlı kopyalar genel kopyayla karşılaştırılır (1.4 raporundaki sütun).
  Farklıysa (Akıl Dışı'nda `hyperframes`, `hyperframes-creative` ve OpenMontage kaynaklı 6 skill için bekleniyor) seçenekler:
  **(A)** bugün kullanılan genel hâl projeye kurulur (önerim) · **(B)** projedeki eski hâl kalır; önce taban testi ve bir
  deneme üretimi yapılır · **(C)** iki hâl de kütüphanede saklanır, proje A ile devam eder. Karar verilmeden 2.3 başlamaz (karar 9).
- **IstatistikYoutube:** `hyperframes`, `hyperframes-cli`, `hyperframes-core`, `hyperframes-animation`, `motion-graphics`.
  `design-dna` genel klasörde **kalır** (projenin kodu renk ölçüm betiğini oradan çalıştırıyor). `openmontage` ve `nlm-skill`
  zaten genelde bırakılacaklar listesinde.
- **Akıl Dışı:** `faceless-explainer`, `general-video` ve aşağıdaki tabloda "kurulacak" yazanlar.

  **Akıl Dışı ajan yolu eşleme tablosu** (taslak; 2A raporuyla kesinleşir):

  | Ajan dosyasındaki genel yol | Projedeki karşılığı |
  |---|---|
  | `~/.codex/skills/seam-craft` | `seam-craft--kutuphane` (projede var) |
  | `~/.codex/skills/motion-doctrine` | `motion-doctrine--kutuphane` (projede var) |
  | `~/.codex/skills/captions-overlay` | `captions-overlay--kutuphane` (projede var) |
  | `~/.codex/skills/hyperframes-registry` | `hyperframes-registry--kutuphane` (projede var) |
  | `~/.codex/skills/hyperframes-creative` | projede içerik yok (kırık bağlantı çifti) → önce karar 8, sonra gerçek kopya kurulur |
  | `~/.codex/skills/hyperframes-animation` | projede yok → kurulacak |
  | `~/.codex/skills/hyperframes-audio` | projede yok → kurulacak |
  | `~/.codex/skills/hyperframes-keyframes` | projede yok → kurulacak (tek kopyası `~/.agents`'te; önce 2.0) |
  | `~/.agents/skills/hyperframes` | projedeki `hyperframes` (içerik farkı için karar 9) |

- **Kontrol:** kurulan kopyanın kontrol kodu genel kopyayla aynı; adı aynı; proje taban testi yine geçiyor.
- **Geri alma:** kurulumdan önce projenin kilit dosyası ve skill klasörü yedeklenir; kurulan kopya proje içinde yeni bir
  klasör olduğundan geri alma onu yedeğe taşımaktır (`skill-ekle.py`'nin o anda desteklediği yolla; önce `--durum` ile
  bakılır). 2.1 sırasında genel kopyalara dokunulmadığı için Claude Code genel olanı kullanmaya devam eder.

### 2.2 OpenMontage'ın 75 bağlantısı
- **Bilgi:** Bu bağlantılar OpenMontage'ın çalışması için gerekli değil. OpenMontage kendi skillerini klasör yolundan okuyor;
  `/openmontage`, `/backlot`, `/ink-art`, `/animated-drawing` komutları ve `openmontage` giriş skili tam yol kullanıyor.
  Bağlantıların tek etkisi: 75 skilin her oturumda listede görünmesi ve kendiliğinden tetiklenebilmesi.
- **Bedeli:** kütüphanenin tercih ettiği 17 skilin (GSAP 4, Three.js 10, Vercel 3) yerine her projede OpenMontage'ın eski
  kopyaları öne geçiyor; skill listesi her oturumda 75 satır uzuyor.
- **Öneri:** bağlantılar yedeğe taşınır, `openmontage` giriş skili ve dört komut kalır. Önce deneme: taşı → OpenMontage'la kısa
  bir iş yap → sorun varsa tek komutla geri koy.
- **Senin yapacağın:** `~/.claude/CLAUDE.md` ve `openmontage` giriş skilindeki "skiller her oturumda yüklenir" cümlesi yanlış
  kalır; düzeltilmiş metni hazır veririm, dosyalara sen yazarsın. **Şimdilik bir şey yapma;** metni o adım geldiğinde veririm.
  Geri alma: bu dosyaların düzeltme öncesi hâli 1.2 yedeğindedir; eski cümleyi de sana ayrıca hatırlatırım.
- **Seçenekler:** (A) kalsın, sadece ölü 4 satır kayıttan düşülsün · (B) yedeğe taşı (öneri) · (C) şimdilik karar verme (karar 6a).

### 2.3 Genel HyperFrames kopyalarını azalt
**Ön koşullar** (bölüm 7'deki 9–13 numaralı kapılar):
- 2.0 ve 2.1 bitti; 1.4'teki "tek kopya" listesindeki her skill kütüphanede ya da yedekte doğrulanmış.
- **Ad çözümlemesi:** her projede kullanılan her skill adı (komutlar, Codex ajan dosyalarındaki yollar ve adlar, `skills:`
  listeleri, IstatistikYoutube'un kapatma ayarındaki adlar, render betiklerindeki `--skill=ad`) projenin kendi skilleri
  arasında aynı adla var. Sadece okuyarak kontrol edilir. Karşılığı olmayan tek bir ad varsa hiçbir şey taşınmaz.
- **İçerik:** genel kopya kalkınca devreye girecek içerik bugün kullanılanla aynı; farklı olanlar için karar 9 verildi.
- **Akıl Dışı:** eşleme tablosundaki her yol proje içine çevrildi, hedef dosya var ve döngü değil; Codex gerçekten oradan
  yüklüyor (deney 3). Ya da senin onayladığın yazılı istisna var.
- **Sabit yollar:** proje raporlarında genel klasöre giden her sabit yol için çözüm (yolu proje içine çevirmek ya da genel
  kopyayı bırakmak) senin onayınla belirlendi. Çözümsüz yolu olan skill taşınmaz.

Sıra — önce başkasına bağlı olanlar, en son asıl klasörler:
1. `~/.codex/skills` içindeki 11 bağlantı.
2. `~/.claude/skills` içindeki, `~/.agents/skills`'e giden 6 bağlantı.
3. `~/.claude/skills` içindeki gerçek HyperFrames klasörleri. (`hyperframes-core`, IstatistikYoutube'un `hyperframes-shorts`
   skilindeki okuma yolu proje içine çevrilmeden taşınmaz. `design-dna` taşınmaz.)
4. `~/.agents/skills` içindeki HyperFrames klasörleri.

Her paketten sonra: kırık bağlantı taraması + IstatistikYoutube ve Akıl Dışı kontrolü. Kayıt dosyası
(`~/.agents/.skill-lock.json`) **düzenlenmez**, sadece yedeklenir. Neyin kalacağı rapordaki tablodan senin onayınla belirlenir.

**Geri alma:** `makine.py --geri-koy <paket>` taşınan girişleri eski yerine koyar. Kayıt dosyası düzenlenmediği ve bu adımda
projelere dokunulmadığı için başka bir geri alma gerekmez. Beklenmedik bir şey olursa ilgili klasör 1.2 yedeğinden geri konur.

### 2.4 OpenMontage güncellemesi (isteğe bağlı; önerim şimdilik ertelemek)
- **Şimdilik bir şey yapma.** Bu adım ancak sen "güncelleyelim" dersen açılır (karar 6b).
- Kazanç: 2 yeni skill, yüz onarma aracının kaynakta düzeltilmiş hâli, sertifika paketi güncellemesi.
- Risk: yeni Python paketleri; kaynak deponun artık Python 3.11 istemesi; yerel yamalarla çakışma. Çakışma adayı dosyalar:
  `package.json`, `package-lock.json`, `Explainer.tsx`, `face_restore.py`. Gerçek çakışma sayısı provada belli olur.
- Yapılırsa: önce bir **kopya** üzerinde prova. Kopyaya Python ortamı alınmaz; prova yalnızca git ve yama çakışmalarını
  dener, kopyada paket komutu çalıştırılmaz (paket denemesi gerekirse yalnızca ayrı, yeni bir ortamda yapılır).
- Gerçek klasörde `make setup`, `make install`, `pip install -U` çalıştırılmaz; Python ortamı yeniden kurulmaz.
  **Gerçek klasördeki git adımlarını (`~/.openmontage` içinde) ben çalıştırmam;** hazır betiği ve komutları sana veririm,
  sen kendin çalıştırırsın.
- Öncesinde ve sonrasında OpenMontage taban ölçümü (1.4) ve IstatistikYoutube'un OpenMontage'a bağlı betikleri aynı testle denenir.
- **Geri alma:** gerçek klasörde git işleminden hemen önce `~/.openmontage` bir kez daha kopyalanır (Python ortamı hariç; o
  hiçbir koşulda değişmez). Yamalı 9 dosya ve izlenmeyen dosyalar (`remotion.config.ts`, `channel-fonts`, `.backlot`,
  `gfpgan/`, `clips_cache/`, `projects/`, yedek dosyalar) adlarıyla listelenir, işlemden sonra kopyayla karşılaştırılır. Fark
  çıkarsa ya da test geçmezse klasör bu kopyadan geri konur. `git clean` ve `git reset --hard` yine yasaktır.

### 2.5 HyperFrames aracı 0.9.29 (isteğe bağlı; en son)
- 0.9.25 ve 0.9.29 görüntü çıktısını değiştirebilir. Bu yüzden önce geçici klasörde aynı sahne iki sürümle alınır ve karşılaştırılır.
- Uygun görürsen kurulumu **sen** yaparsın: `npm install -g hyperframes@0.9.29`. Geri dönüş: `npm install -g hyperframes@0.9.23`.
- Projelerin sabitlediği sürümlere dokunulmaz. `hyperframes upgrade --project` çalıştırılmaz.
- Öncesinde ve sonrasında OpenMontage taban ölçümü de alınır (OpenMontage HyperFrames'i sürümsüz çağırdığı için).
- Araç yükselince kütüphanedeki HyperFrames arşivi ve `makine.json` aynı sürüme çekilir; eski sürüm skilleri saklama
  kopyasında kalır. Geri dönülürse arşiv ve `makine.json` da git geçmişinden önceki hâline döner.

### 2.6 Aylık akışa bağlama
Aylık güncelleme görevinin sonuna sadece okuyan makine kontrolü eklenir (02 numaralı belge). Görev hiçbir şeyi kendiliğinden
yükseltmez, taşımaz.

---

## 7. Geçiş kapıları

**Dalga 2'ye geçmek için** hepsi "evet" olmalı:

| # | Kapı |
|---|---|
| 1 | Dondurma satırları ekli ve yeni oturumda görünüyor. |
| 2 | Tam yedek alındı; geri yükleme provası geçti (kontrol kodları, bağlantılar, döngülü bağlantı çifti, kayıt dosyası). |
| 3 | Makine raporu üretildi; "tek kopya" listesindeki her skill yedekte doğrulandı. |
| 4 | IstatistikYoutube taban testi kayıtlı ve geçiyor. |
| 5 | Akıl Dışı raporu alındı; eşleme tablosu kesinleşti; karar 8, 9 ve 10 verildi. |
| 6 | Deney sonuçları yazıldı ("doğrulanmadı" da bir sonuçtur; o zaman temkinli yol). |
| 7 | OpenMontage taban ölçümü kayıtlı. |
| 8 | O hafta yetişmesi gereken bir üretim yok ya da ilgili proje kapsam dışı bırakıldı. |

**Genel kopyaları taşımadan (2.3) önce** ayrıca:

| # | Kapı |
|---|---|
| 9 | Saklama kopyaları kütüphanede (2.0) ve aylık güncellemenin kuru çalıştırmasında yerinde durdukları görüldü. (Karar 5 "hayır" ise: her skill yedekte doğrulandı ve projelerin bağlı olduğu genel skiller taşınmıyor.) |
| 10 | Ad çözümlemesi: her projede kullanılan her skill adı projenin içinde aynı adla var. |
| 11 | Genel kopya kalkınca devreye girecek içerik bugün kullanılanla aynı; farklılar için karar 9 verildi. |
| 12 | Akıl Dışı eşleme tablosundaki her yol proje içine çevrildi ve hedef dosya var (ya da onayladığın istisna). |
| 13 | Genel klasöre giden her sabit yol için çözüm belirlendi. |

Dalga 2'nin her paketi için ayrıca: paket raporu onaylandı · son yedek 30 günden yeni · kütüphane deposu temiz ve aylık
görev o sırada çalışmıyor · paket sonrası kontroller geçti.

---

## 8. Asla yapılmayacaklar

- Temiz kurulum; Python ortamını ya da OpenMontage klasörünü yeniden kurmak.
- `hyperframes skills update`, `hyperframes update`, `hyperframes init`, `npx skills …` çalıştırmak.
- `hyperframes upgrade --project` (sadece `--check` olur) ve `hyperframes clean` (sadece `--dry-run` olur).
- `~/.agents/.skill-lock.json` dosyasını düzenlemek ya da "onarmak".
- `~/.openmontage` içinde benim herhangi bir git komutu çalıştırmam; kimin çalıştırdığından bağımsız olarak `git pull`,
  `git checkout .`, `git reset --hard`, `git clean`, `make setup`, `pip install -U`.
- Proje denetimi bitmeden HyperFrames aracını yükseltmek.
- Tek kopyası genelde duran bir skili, kütüphanede ya da yedekte kopyası doğrulanmadan taşımak.
- Benim `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, ayar dosyaları, anahtar dosyası ya da kabuk ayar
  dosyasına yazmam. Bunlar için sadece hazır metin veririm.
- Anahtar dosyalarının içeriğini okumak, ekrana ya da bir rapora yazdırmak.
- Silmek. Kalkan her şey yedeğe taşınır; kalıcı silme ancak sen ayrıca istersen.
- Kütüphane dışındaki bir GitHub deposunda işlem; kütüphaneyi GitHub'a senden istek gelmeden göndermek.

---

## 9. Senden beklenen kararlar

**Şimdi (Dalga 1'e başlamak için):**

| # | Karar | Önerim | Hayır dersen ne olur |
|---|---|---|---|
| 1 | Bu planı ve Dalga 1'i onaylıyor musun? (Dalga 1: yedek + rapor + kütüphaneye sadece okuyan araç.) | Evet | Hiçbir şey yapılmaz; her şey bugünkü gibi kalır. |
| 2a | Dondurma satırlarını (1.1'deki tek komut) ekleyecek misin? | Evet | HyperFrames bir gün kendiliğinden güncellenip genel skillerin üzerine yazabilir. Dalga 2'ye geçilmez. |
| 2b | HyperFrames aracı şimdilik 0.9.23'te kalsın mı? | Evet | Yükseltme en erken proje denetimleri bittikten sonra, 2.5'teki sırayla yapılır. |
| 4 | İkinci yedek için harici diskin var mı? | Varsa kullan | Dalga 1 yine yapılır; Dalga 2 öncesi yeniden sorarım. |
| 7 | OpenMontage anahtar dosyaları yedeğe kopyalansın mı? (Açılmadan, sadece sana açık izinlerle.) | Evet; harici disk şifreliyse oraya da | Yedekte olmazlar; kendi şifre yöneticinde saklarsın. |

**Dalga 1 sırasında / raporlar gelince:**

| # | Karar | Önerim | Hayır dersen ne olur |
|---|---|---|---|
| 8 | Akıl Dışı'ndaki kırık `hyperframes-creative` bağlantı çifti onarılsın mı? (İkisi yedeğe taşınır, gerçek kopya kurulur.) | Evet, yedek ve provadan sonra | Çift olduğu gibi kalır; o skill projede kullanılamaz, ajan yolu genel kopyaya bağlı kalır ve o genel kopya taşınmaz. |
| 9 | Akıl Dışı'nda genel kopyadan farklı olan proje kopyaları: (A) bugünkü genel hâl kurulsun · (B) projedeki eski hâl kalsın · (C) ikisi de saklansın, proje A ile devam etsin. | A | Karar verilmeyen skilin genel kopyası taşınmaz. |
| 10 | Akıl Dışı'nda ölü yolu çağıran betiklerden hangileri onarılsın? (Liste 2A raporundan çıkar.) | Yalnızca hâlâ kullandıkların | Betikler olduğu gibi kalır; zaten çalışmıyorlar. |
| 11 | Psikolojik Danışman hattı aktif mi? Aktifse yol düzeltilsin mi? | Rapora göre | Hat "pasif" diye işaretlenir; hiçbir dosya değişmez. |

**Dalga 2 öncesi:**

| # | Karar | Önerim | Hayır dersen ne olur |
|---|---|---|---|
| 3 | Genel klasörlerdeki taşıma işlerini kim yapsın? **(a)** Ben, her paket için onayınla, sadece "yedeğe taşı" ve "geri koy" yapabilen araçla. **(b)** Sen, hazırladığım komut dosyasını çalıştırarak. | (a) | (b) geçerli olur. (a) seçilirse kural 1'e yazılı, dar bir istisna eklenir (metin 03 numaralı belgede). |
| 5 | Bugünkü ve emekli HyperFrames skilleri kütüphanede (private depoda) saklama kopyası olarak dursun mu? | Evet | Kopyalar sadece yedekte kalır; projelere kurulamaz, projelerin bağlı olduğu genel skiller yerinde bırakılır. |
| 6a | OpenMontage'ın 75 bağlantısı deneme sonrası yedeğe taşınsın mı? | Evet (2.2 B) | Bağlantılar kalır; 75 skill her oturumda listede görünmeye devam eder. |
| 6b | OpenMontage güncellemesi şimdi mi yapılsın? | Hayır, sonra | (Önerim zaten "hayır".) "Evet" dersen 2.4'teki prova ile başlanır. |

---

## 10. Sözlük

| Terim | Anlamı |
|---|---|
| HyperFrames | HTML ile video sahnesi hazırlayıp videoya çeviren araç ve onun skill ailesi. |
| OpenMontage | Video üretim hattı (anlatım, kurgu, altyazı…); `~/.openmontage` klasöründe kurulu. |
| Codex | OpenAI'nin kodlama aracı; Claude Code gibi skill ve ajan dosyası okur. |
| Genel skill | Bilgisayarın genelinde duran, her projede görünen skill. |
| Proje skili | Projenin kendi klasöründe duran skill. |
| Ajan dosyası | Bir yapay zekâ yardımcısının görevini ve kullanacağı skilleri anlatan dosya. |
| Bağlantı (symlink) | Bir klasörün başka bir yerdeki asıl klasörü gösteren kısayolu. Asıl klasör taşınırsa bağlantı kırılır. |
| Kilit kaydı | Projeye hangi skilin hangi sürümden kurulduğunu tutan dosya (`.skill-kutuphanesi/kilit.json`). |
| Emekli skill | Kaynağın artık yayımlamadığı skill. Yeniden kurulamaz; eldeki kopya tek kopyadır. |
| Dondurulmuş (saklama) kopya | Bir skilin belli bir tarihteki hâlinin kütüphanede değiştirilmeden tutulan kopyası. |
| Sabitleme (pin) | Bir projenin belli bir araç sürümünü adıyla çağırması (`hyperframes@0.8.143` gibi). |
| Yama | Kaynak dosyada senin yaptığın yerel değişiklik. |
| Render | Sahnenin video dosyasına çevrilmesi. |
| Taban testi / taban ölçümü | Değişiklikten önce alınan, sonra aynısıyla karşılaştırılan test sonucu. |
| Kontrol kodu (checksum) | Dosya içeriğinden üretilen kısa kod. İki dosyanın kodu aynıysa içerikleri aynıdır. |
| Python ortamı (venv) | OpenMontage'ın kullandığı Python paketlerinin durduğu ayrı klasör. |
| Paket | Dalga 2'de tek seferde onaylanıp uygulanan küçük iş parçası. |
| Kapı | Bir sonraki aşamaya geçmeden önce sağlanması gereken koşul. |
| Kuru çalıştırma | Bir komutun hiçbir şeyi değiştirmeden, sadece ne yapacağını gösterdiği çalıştırma. |
| Commit (yerel kayıt) | Depodaki değişikliklerin geçmişe kaydedilmesi. GitHub'a gönderme değildir. |
| Dal | Deponun ana hâlini bozmadan değişiklik yapılan ayrı kopyası. |
| Private depo | Sadece senin görebildiğin GitHub deposu. |
| Telemetri | Bir aracın kullanım bilgisini üreticisine göndermesi. |
| Time Machine / iCloud | macOS'un yedekleme / bulut eşitleme özellikleri. |
| Öne geçme | Aynı adlı iki skilden birinin diğerini gizlemesi. Claude Code'da genel skill, aynı adlı proje skilinin önüne geçer. |
