# 02 — Skill Güncelleme Yönergesi

Güncelleme **iki ayrı katmanda** yapılır. Kütüphane güncellenince projeler kendiliğinden değişmez;
her projeyi sen ayrıca güncellersin. Böylece çalışan bir proje habersiz bozulmaz.

```
GitHub repoları ──(1) arsiv-guncelle.py──► SkillKutuphanesi ──(2) skill-ekle.py --guncelle──► Proje
                                             (git kayıt noktası)                    (proje yedeği)
```

## 1) Kütüphaneyi güncelleme — aylık, git dalıyla (önerilen)

> **Güncelleme sürerken:** kütüphane geçici olarak `guncelleme/*` dalındadır ve `.guncelleme-kilidi` vardır; `skill-ekle.py` kurulum/güncellemeyi "BEKLE" diyerek durdurur (15–40 dk). Başlamadan GitHub API hakkı (≥1500) denetlenir. Ölü ya da 6 saatten eski kilit yok sayılır. Bekleyen bir dal (`guncelleme/*` ya da `takip/*`) varken yeni dal açılmaz; dal 45 günden eskiyse rapor uyarır.

Güncelleme **ayda bir** yapılır ve **git ile takip edilir**: her güncelleme kendi dalında (`guncelleme/YYYY-AA`) hazırlanır,
`master` sen onaylayana kadar değişmez.

```
master ──┬──────────────────────────────── (onay) ── merge --no-ff ──► master
         └─ guncelleme/2026-11: indir → yerleştir → denetle → geçmiş kaydı → commit
```

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/arsiv-guncelle.py                      # 1. RAPOR: hangi repoda yeni commit var, yeni yıldız var mı
python3 araclar/arsiv-guncelle.py --uygula --dal       # 2. guncelleme/YYYY-AA dalında güncelle (master değişmez)
git log master..guncelleme/2026-11                     # 3. incele (ve dalda notlar/guncelleme-gecmisi.md)
python3 araclar/arsiv-guncelle.py --birlestir guncelleme/2026-11   # 4a. onay: master'a birleştir + kontroller + dal silinir
git branch -D guncelleme/2026-11                       # 4b. ret: dalı sil, hiçbir şey değişmez
```

- **Aylık zincir tek komut:** `python3 -u araclar/arsiv-guncelle.py --aylik` ("SkillKutuphanesi aylık güncelleme" zamanlanmış görevi bunu
  her ayın 1'inde 10:00'da çalıştırır; elle de çalıştırılır). Ön kontrol, kaynak raporu, güncelleme dalı, aylık özet ve damga sırayla yapılır;
  sonunda tek sayfa özet basılır. **Birleştirmez, göndermez.** Birleştirme her zaman senin onayınla yapılır (4a). Ayrıntı: bölüm 1b.
- **Aylık özet:** `python3 araclar/aylik-ozet.py` tüm rapor araçlarını tek sayfada toplar (karar bekleyenler + dikkat gerektirenler,
  `notlar/aylik-ozet.md`); her oturum başında `python3 araclar/aylik-ozet.py --hizli` (ağsız, yazmasız, en çok 15 satır). Ayrıntı: bölüm 1b.
- **Takip:** her güncelleme `notlar/guncelleme-gecmisi.md`'ye kayıt düşer (kaynak commit'leri, içeriği değişen / yeni /
  kaynakta kaldırılan skiller, yeniden incelenecekler, durum: bekliyor → birleştirildi). Ayrıntı: `git log --oneline -- registry.json`.
- Bekleyen bir güncelleme dalı varken yeni `--dal` güncellemesi başlamaz (önce birleştir ya da sil). Bekleyen dal hem `guncelleme/*`
  hem `takip/*` desenine bakılarak aranır.
- `--birlestir` hem `guncelleme/*` hem `takip/*` dalı için tek yoldur (kontroller + otomatik geri alma). `git merge --no-ff` ile
  elle birleştirme KULLANILMAZ.
- `--birlestir` sonrası doğrulama, kapsam denetimi ya da testler geçmezse `master` otomatik eski hâline döner, dal kalır.

`--uygula` tek başına (dal olmadan) da çalışır: güncellemeyi bulunulan dalda yapar. Aylık rutin için `--dal` kullan.

## 1b) Aylık özet, kuru plan, çevrimdışı

```bash
python3 araclar/aylik-ozet.py --hizli          # oturum başı: ağsız, yazmasız, en çok 15 satır (takma ad: --oturum)
python3 araclar/aylik-ozet.py                  # tam: tüm rapor araçları (--ozet-json) + kendi kontrolleri -> notlar/aylik-ozet.md
python3 araclar/aylik-ozet.py --ozet-json      # aynısı, stdout'ta tek JSON nesnesi (tam modda bu da rapor dosyalarını yeniler: notlar/aylik-ozet.md, notlar/proje-kullanimi.md, notlar/proje-durumu.md; yazmasız çağrı yalnız --hizli; --hizli yapay zeka aracı sürüm komutlarını da çalıştırmaz)
python3 araclar/arsiv-guncelle.py --aylik --kuru   # aylık zincirin YAN ETKİSİZ planı: ön kontrol + rapor + PLAN + hızlı özet
python3 araclar/arsiv-guncelle.py --siki       # rapor modu; GitHub'a ulaşılamadıysa ya da kaynak kontrol edilemediyse çıkış 2
```
- **Özet ne gösterir:** "Senin kararını bekleyen N şey" (bekleyen dal, yeni aday repolar, push edilmemiş commit, boşaltma onayı…)
  ve "Dikkat gerektirenler". Hiçbir şeyi değiştirmez; bir araç yoksa ya da çökerse o araç "dikkat" olur, özet sürer.
  `notlar/aylik-ozet.md` ve `notlar/son-aylik-calisma.json` bu makineye özgüdür, `.gitignore`'dadır, git geçmişinde yoktur
  (`.gitignore`'da değilse özet dosyayı yazmaz).
- **Aday triyajı:** özet her aday kaynağından en çok 5 ad gösterir (toplam sayıyla). Kapatmak: `konu-takip.py --karar owner/ad eklendi|reddedildi|izle`.
  Kabul ettiğin bekleyen bir kararın özette bir daha çıkmaması için ifadesini `notlar/kararlar.md` → "Kabul edilen bekleyenler" bölümüne yaz.
- **Kaçan ay:** aylık çalışma damgası (`notlar/son-aylik-calisma.json`) 35 günden eskiyse özet sorar. Ayrı bir telafi koşusu yoktur: kaynak
  karşılaştırması tarihe değil registry'deki commit'e dayanır; tek koşu birikmiş tüm değişiklikleri yakalar. Damga yoksa en yeni
  `guncelleme-gecmisi.md` kaydının tarihine bakılır; o da yoksa (ilk kurulum) soru çıkmaz.
- **Kuru plan ön kontrolleri:** master dalı mı, kaydedilmemiş değişiklik var mı (rapor dosyaları dahil), bekleyen dal var mı, `gh` oturumu var mı.
  Biri takılırsa PLAN "yalnız rapor" der ve nedenini yazar; hiçbir dal açılmaz, commit atılmaz, damga yazılmaz.
- **GitHub oturumu yoksa:** kendi terminalinde `gh auth login` (tarayıcıda onayla); sonra komutu yeniden çalıştır. Oturum yokken rapor kaynak
  karşılaştırmasını atlar ("ATLANDI"), yalnız yerel kontrolleri yapar.
- **Çıkış kodları (rapor modu):** 0 = sorun yok, 1 = erişilemeyen kaynak, 2 = yalnız `--siki` ile: GitHub'a ulaşılamadı ya da bazı kaynaklar kontrol edilemedi.
- **Rapor sırasında `AD DEĞİŞMİŞ` satırı** (commit yanıtındaki adresten, ek çağrı olmadan) çıkabilir; kesin kaynak `github-skill-listesi.py` raporudur.
### Tek komut: `--aylik`
```bash
python3 -u araclar/arsiv-guncelle.py --aylik          # zincirin tamamı (15–40 dk sürebilir); zamanlanmış görev yalnız bunu çalıştırır
python3 araclar/arsiv-guncelle.py --aylik --kuru      # yan etkisiz plan (yukarıda)
```
Sırası, her adım düz Türkçe bildirilir: **1/5 ön kontrol** (master mı, ağaç temiz mi, bekleyen dal var mı, `gh` oturumu var mı) →
**2/5 kaynak raporu** (+ yıldız listesi raporu) → **3/5 güncelleme** (kaynaklarda değişiklik varsa `guncelleme/YYYY-AA` dalı, `--uygula --dal`
ile aynı kod; yoksa `takip/YYYY-AA` dalında trend + popüler + konu taraması) → **4/5 aylık özet** (tek sayfa; program denetimi, proje sağlığı,
yedek, git durumu, bekçi) → **5/5 damga**. Hiçbir zaman birleştirmez, push etmez, başka dal silmez (yalnız kendi hata geri almasını yapar).
`master` değişmez; sonunda master'dasın.

- **Erişilemeyen kaynak zinciri durdurmaz:** kaynak `kaynak-cek.py --atla` ile atlanır, arşiv kopyası korunur; "Bu ay erişilemedi: <repo>" diye
  raporlanır, `guncelleme-gecmisi.md` kaydına ve damgaya yazılır. Hiçbir zaman kendiliğinden `KAYIP` işaretlenmez: işaretlemek senin onaylı,
  elle yapacağın adımdır (`rehber/03` E3). Geçen ay da erişilemeyen kaynak "geçen ay da erişilemiyordu" notuyla gelir.
- **Bekleyen dal kuralı:** `guncelleme/*` ya da `takip/*` dalı onay beklerken YENİ dal açılmaz. Zincir dalın adını ve yaşını yazar (45 günden
  eskiyse uyarır), salt okuma adımlarını (rapor, özet) yine yapar ve sonucu `bekleyen-dal` damgalar. Çözüm: dalı incele ve birleştir
  (`--birlestir <dal>`) ya da reddet (`git branch -D <dal>`), sonra `--aylik`'i yeniden çalıştır.
- **Damga:** `notlar/son-aylik-calisma.json` bu makineye özgüdür, `.gitignore`'dadır, git geçmişinde yoktur. Zincir güncelleme düşse bile yazar.
  Alanlar: `tarih`, `sonuc`, `dal`, `neden`, `atlanan_kaynaklar`, `ad_degisen`, `ozet_durumu`, `son_basarili`, `gecmis` (son 12 koşu).
  `sonuc` değerleri: **`tamam`** (güncelleme ya da takip bitti; dal hazırsa onayını bekler), **`kismi`** (yazma adımı yapılmadı: kirli ağaç,
  master dışındayız, GitHub'a ulaşılamıyor ya da kaynaklar geçici olarak kontrol edilemedi; salt okuma rapor ve özet çalıştı),
  **`basarisiz`** (bir adım düştü; koşunun açtığı dal geri alındı), **`bekleyen-dal`** (eski dal onay beklediği için yeni dal açılmadı).
  Fresh klonda damga yoktur: özet en yeni `guncelleme-gecmisi.md` tarihine bakar.
- **`kismi` ne demek:** güncelleme yapılmadı ama kontroller yapıldı. Son satırdaki `NEDEN:` işini yap (kirli ağaç → kaydet ya da geri al, onayınla;
  GitHub yok → aşağıdaki), sonra yeniden çalıştır. Çıkış kodu: `tamam`, `kismi`, `bekleyen-dal` = 0; `basarisiz` = 1; `--siki` ile `kismi` = 2.
- **Çevrimdışı / `gh` oturumu yok:** zincir takılmadan yerel kontrolleri yapar (kaynak karşılaştırması atlanır), damgaya `kismi` yazar ve
  seni uyarır: kendi terminalinde `gh auth login` çalıştır (tarayıcıda onayla), sonra `--aylik`'i yeniden çalıştır.
- **Kirli ağaç:** master'da kaydedilmemiş değişiklik varsa (rapor dosyaları dahil) yazma adımı yapılmaz; otomatik commit yoktur. `NEDEN:` satırındaki
  `git add … && git commit` (onayınla) ya da `git checkout -- …` komutunu sen çalıştırırsın.
- **Son satırlar:** `SONUÇ:`, varsa `NEDEN:`, `DAL:`, `ATLANAN KAYNAKLAR:`, `AD DEĞİŞMİŞ:`.

### Zamanlanmış görev metni
Görevin metni kütüphanede `zamanlanmis/aylik-guncelleme.SKILL.md` olarak durur (kaynak doğru odur). Canlı dosya:
`~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md`. Tam `aylik-ozet.py` ikisini karşılaştırır (`zamanlanmis-gorev`):
aynıysa `temiz`, farklıysa ya da canlı dosya yoksa `dikkat`. Canlıyı güncellemek senin onayınla yapılır: (1) `diff -u <canlı> zamanlanmis/aylik-guncelleme.SKILL.md`
göster; (2) yedek: `cp <canlı> ~/Documents/Claude/yedek/zamanlanmis-gorev-<tarih>.SKILL.md`; (3) `cp zamanlanmis/aylik-guncelleme.SKILL.md <canlı>`;
(4) `cmp` ile doğrula. Geri alma = yedeği geri kopyalamak. Zamanlayıcı Mac uykudayken ya da uygulama kapalıyken tetiklenmeyebilir; asıl tetik
oturum başındaki `aylik-ozet.py --hizli`'dir (damga 35 günü aşınca sorar).


`--uygula` önce iki şeyi şart koşar: kütüphanede **kaydedilmemiş değişiklik olmayacak** (elle düzenlemeni önce `git commit` et) ve tüm kaynaklara **erişilebilecek** (tek başına `--uygula --dal` için; `--aylik` erişilemeyeni atlar). Sonra bu sırayla çalışır; herhangi bir adım hata verirse durur ve **git kaydı atmaz**:
0. `github-trend.py --aday` — GitHub Trending (günlük/haftalık/aylık; tüm diller + Python/TS/JS/Shell) taranır, `trend.json`
   geçmişine eklenir; kütüphanedeki kaynakların trend durumu ve trend'deki yeni skill repoları `notlar/github-trend.md`'ye yazılır.
   Trend'deki aday repolar otomatik EKLENMEZ: rapordaki eksik alanlara uyanlar `03-yeni-skill-ekleme.md` ile, onayla eklenir.
0a2. `populer-tarama.py` — GitHub REST aramasıyla popüler skill repoları, adayda `SKILL.md` sayımı → `notlar/populer-skiller.md`.
   `github-skill-listesi.py` (GraphQL) ve `github-trend.py` (trending HTML) bulut/kısıtlı ağda çalışmaz; bu araç onların yedeğidir.
0b. `konu-takip.py` — `kaynaklar.json` → `takip_konulari` (e-ticaret/Etsy, mobil…) için GitHub'da yeni skill repoları aranır;
   adaylar `notlar/konu-takip.md`'ye yazılır (eklenmez). Değerlendirdiğin adayı `--karar owner/ad reddedildi "neden"` ile kapat.
-1. `gelistirici-bilgisi.py` — geliştirici bilgileri (`gelistiriciler.json`).
(`--aylik` ayrıca 2/5 adımında, dal açmadan önce `site-takip.py`'yi çalıştırır: siteden alınan skillerin adresleri; rapor git dışı
`notlar/site-takip.md`, sonuç aylık özete girer; ayrıntı rehber/03 B3.)
1. `kaynak-cek.py` — tüm kaynaklar sabit commit'ten yeniden iner (indirme hatası varsa durur).
2. `arsiv-yerlestir.py` — tekilleştirme, kategori, değerlendirme. **Elle yaptığın inceleme alanları korunur**
   (`ozet_tr`, `kullanim_alani`, `teknoloji`, `roller`, `kalite`, `ortusme_grubu`, `kategori_elle`…). Kaynak kaydında `medya_haric`
   varsa listedeki tam repo-göreli tek dosya yolları (NFC, harf duyarlı; klasör/joker yok) arşive konmaz ve güncellemede geri gelmez
   (`klasor_hash`/`atlanan_dosyalar` farkı üretmez; `SKILL.md`'den bu dosyalara giden bağlantı kırık sayılmaz, `KAYNAK.md`'de "dışlandı" yazar).
2b. `yol-tara.py` — skill metinlerinde sabit genel yol taraması → `notlar/yol-denetimi.md` (hata zinciri durdurmaz).
2c. `program-denetim.py` — programların sürüm denetimi → `notlar/program-denetimi.md` (hata zinciri durdurmaz).
3. `kapsam-denetimi.py` — her SKILL.md'nin açıklandığını bağımsız olarak doğrular.
4. `katalog-uret.py` — KATALOG.md ve rehberleri yeniden üretir.
4b. `skill-readme.py` — Türkçe skill rehberi (`README-SKILLER.md`, `skiller/`). Yeni/değişen skillerin çevirisi için
   ayrıca `ceviri-tr.py` (claude -p, ücretli ama ucuz: ~2600 skill ≈ $0,7) sonra yeniden `skill-readme.py`.
4c. `skill-calistir.py` — her skill kurulup yükleme/bağlantı/betik sözdizimi sınanır → `TEST_RAPORU.md` (agent'sız; HATA
   güncellemeyi durdurmaz). Yeni HATA varsa yama: `rehber/03` → "Çalışmayan skill". `yama eskidi` uyarısında yamayı yenile.
5. `dogrula.py` — roller/profiller var olan skillere mi bakıyor, tekrar isim var mı.
6. `git commit` — kayıt noktası.

### GitHub'a gönderme (private depo)
Kütüphane `ulukayasaban/SkillKutuphanesi` (private) deposuna yedeklenir. Güncelleme dalı GitHub'da **PR olarak incelenir**, ama
**birleştirme yerelde** `--birlestir` ile yapılır (birleştirme sonrası kontroller ve otomatik geri alma sadece orada var):

```bash
git push -u origin guncelleme/2026-11                                   # 1. dalı gönder
gh pr create --base master --head guncelleme/2026-11 \
  --title "Aylık güncelleme 2026-11" --body-file notlar/guncelleme-gecmisi.md   # 2. inceleme kaydı (PR)
python3 araclar/arsiv-guncelle.py --birlestir guncelleme/2026-11        # 3. onaydan sonra yerelde birleştir
git push origin master                                                  # 4. PR kendiliğinden "merged" görünür
git push origin --delete guncelleme/2026-11                             # 5. uzak dalı sil
```
- Ret: `gh pr close <no>` + `git push origin --delete <dal>` + `git branch -D <dal>`.
- GitHub'daki **Merge düğmesini kullanma**; yerel ve uzak `master` ayrışır.
- Push/PR sadece kullanıcı isteyince yapılır. Zamanlanmış aylık görev sadece yerelde rapor ve dal hazırlar; push etmez.

### Güncellemeden sonra kontrol et
- `git -C ~/Documents/SkillKutuphanesi show --stat HEAD` → hangi skiller değişti.
- Rollerde kullanılan bir skill **kaldırıldıysa** `dogrula.py` HATA verir → rol dosyasını düzelt.
- Bir skill'in globaldeki durumu değiştiyse (ör. global sürüm güncellendi; genel klasörler boş olduğundan bugün nadir) kurulum adı değişebilir;
  `skill-ekle.py --guncelle` bunu `ad-degisti` uyarısıyla bildirir.

### Güncellemeden sonra yeniden inceleme
İçeriği değişen ve daha önce incelenmiş her skill otomatik olarak `inceleme: yeniden-incelenecek` olur
(eski inceleme `onceki_inceleme` alanında saklanır). `arsiv-guncelle.py --uygula` bunların listesini yazar;
ön kontrol `inceleme-eskidi` UYARISI, dogrula çekirdek rol skilleri için UYARI verir.
Yapılacak: `rehber/07-kategori-inceleme.md` adımlarıyla sadece bu skilleri yeniden incele, `inceleme: incelendi` yap, kaydet.

### Kaynakta kaldırılan skiller
Repo duruyor ama skill yeni commit'te yoksa skill arşivde kalır: `kaynak_durumu: kaynakta-kaldirildi`, katalogda 🗄️emekli.
Rollerde kullanılıyorsa dogrula UYARI verir: rolü güncel karşılığına geçir (örnek: 2026-10'da HyperFrames iş akışı skilleri
emekliye ayrıldı, video rolleri `hyperframes` + `media-use` + `hyperframes-cli` yapısına taşındı).

### Geri alma
```bash
git -C ~/Documents/SkillKutuphanesi log --oneline | head     # kayıt noktaları
git -C ~/Documents/SkillKutuphanesi revert HEAD              # son güncellemeyi geri al (doğrudan --uygula commit'i için)
git -C ~/Documents/SkillKutuphanesi revert -m 1 <birleştirme-commit>   # --birlestir ile gelen birleştirmeyi geri al (--no-ff olduğu için -m 1 şart)
```
Birleştirme push edilmişse geri alma da yeni bir commit'tir ve `git push origin master` ile ayrıca (kullanıcı isteyince) gönderilir; force-push yapılmaz.

## 2) Projeyi güncelleme

```bash
python3 araclar/skill-ekle.py <proje> --durum                 # hangi skillde GÜNCELLEME VAR / ELLE DEĞİŞTİRİLMİŞ
python3 araclar/skill-ekle.py <proje> --guncelle --kuru       # ne değişecek (rapor)
python3 araclar/skill-ekle.py <proje> --guncelle --evet       # uygula (önce yedek)
python3 araclar/skill-ekle.py <proje> --dogrula               # kontrol
python3 araclar/skill-ekle.py <proje> --geri-al               # beğenmediysen geri dön
```

Kurallar:
- Projede **elle değiştirdiğin** bir skill güncellenmez (HATA: `elle-degistirilmis`). Değişikliğini korumak istiyorsan
  dokunma. Kütüphane sürümünü istiyorsan `--zorla` ver; önce yedek alınır.
- Kaynağı kütüphaneden **kaldırılmış** bir skill projede olduğu gibi kalır (UYARI `kaynak-yok`). Skill kimliği kaynağa (repo + yol) bağlıdır; öncelikler değişse bile güncelleme başka bir repo'nun aynı adlı skill'ini **asla** koymaz.
- Sadece Claude ya da Codex sürümü değişse bile güncelleme görünür (kurulum parmak izi ana + araç sürümlerini kapsar).
- `--guncelle` eksik/bozuk kurulumları (silinmiş symlink vb.) da onarır.
- Güncelleme sonrası agent dosyaları (`.claude/agents`, `.codex/agents`) ve AGENTS.md/CLAUDE.md blokları yeniden üretilir.
- Sadece Claude kullanan projede (`--arac claude`, kilit `araclar: [claude]`) güncelleme skilleri `.claude/skills`'e gerçek kopya olarak yazar; Codex dosyası üretmez.

## 3) Skill'i projede özelleştirmek istersen
Kütüphane kopyasını elle değiştirmek yerine:
1. Skill'i kendi adınla kopyala (ör. `.claude/skills/benim-tasarim-kurallarim/`). Bu senin skill'in olur; araç ona hiç dokunmaz.
2. Ya da kütüphanede `registry.json`'a not ekle ve iyileştirmeyi kaynağa (GitHub) öner.

## 3b) Bir kaynak repo silinirse / private olursa
`arsiv-guncelle.py` bunu `! erişilemiyor` diye raporlar. Tek başına `--uygula` durur; `--aylik` ise kaynağı `kaynak-cek.py --atla` ile atlar, arşiv kopyasını korur ve "bu ay erişilemedi" diye raporlar (kendiliğinden işaretlemez). Kalıcıysa `kaynaklar.json`'da o kaydın `tip` alanını
`"KAYIP"` yap: arşivdeki kopyalar ve registry kayıtları korunur (`kaynak_durumu: kayip`), projeler etkilenmez.

## 3c) Bir kaynak repo GitHub'da taşınırsa / adı değişirse
`github-skill-listesi.py` bunu **AD DEĞİŞMİŞ** diye raporlar. `kaynaklar.json`'da `repo` yeni adla değiştirilir, eski ad
`eski_adlar` listesine yazılır; kimlikler ve projelerdeki kurulumlar değişmez. Adımlar: `rehber/09-ad-kimlik-ve-cakisma.md`.

## 3d) Güncelleme hangi projeleri etkiler
`arsiv-guncelle.py` raporu, değişen kaynaklardan skill kullanan projeleri listeler. Elle: `python3 araclar/proje-kullanimi.py --repo owner/ad`.
Birleştirmeden sonra o projelerde `skill-ekle.py <proje> --durum` / `--guncelle --kuru`.

## 4) Global skiller
Makine genelindeki skill klasörleri (`~/.claude/skills`, `~/.agents/skills`) 2026-11-12'de boşaltıldı (K-40); orada skill yoktur ve `globalde` karşılaştırması boş kalır.
Orada bir şey yeniden belirirse bu sistemle (`arsiv-guncelle.py`) güncellenmez. Ama **OpenMontage ve HyperFrames programlarının** ve skillerinin güncellemesi, programların kendi güncelleme komutuyla
(`hyperframes update`, `/openmontage`) tek başına yapılmaz: kütüphane oturumu yapar, her seferinde kullanıcı onayıyla (`rehber/11-program-yonetimi.md`, "Yerinde program").
Takip: `python3 araclar/program-denetim.py`.

Kalıcı kural: `HYPERFRAMES_SKIP_SKILLS=1` tanımlı değilken HyperFrames'in `init`, `skills`, `skills update` ve `update`
komutları çalıştırılmaz; bu komutlar genel skill klasörlerine yazabilir. Kartta hangi komutun neyi yazdığı listelidir
(`programlar.json` → `hyperframes`). Genel skill klasörleri 2026-11-12'de boşaltıldı; değişken `~/.zshenv`, `~/.zshrc` ve `~/.claude/settings.json` → `env`
içine yazıldı (dört HyperFrames kilidi tanımlı: SKIP_SKILLS, NO_AUTO_INSTALL, NO_UPDATE_CHECK, NO_TELEMETRY) (kabuk başlatmadan süreç çalıştıran masaüstü uygulamalarını kapsamaz). Güncel durum için kartın `simdi` alanına bak.
OpenMontage makine genelinde skill bağı kurmaz; güncellemesi bağları yeniden kurmaz.

## Güncelleme takvimi (öneri)
| Ne zaman | Ne |
|---|---|
| Ayda bir | `python3 -u araclar/arsiv-guncelle.py --aylik` (tek komut; zamanlanmış görev çalıştırır); önce istersen `--aylik --kuru` ile plan |
| Her oturum başında | `aylik-ozet.py --hizli` (35 günü aşan aylık çalışma burada sorulur) |
| Kaçan ay | aynı komut; tek koşu birikmiş hepsini kapsar |
| İstediğin zaman | `konu-takip.py [--konu e-ticaret]` (aylık özette de görünür) → `notlar/konu-takip.md`: takip edilen alanlarda yeni skill repoları |
| İstediğin zaman | `github-trend.py --aday` → `notlar/github-trend.md`: trend'e giren kaynaklar ve aday skill repoları |
| Yeni repo yıldızladığında | `arsiv-guncelle.py` raporu "yıldızlı ama kaynaklar.json'da yok" der → `03-yeni-skill-ekleme.md` |
| Projeye başlamadan önce | `skill-ekle.py <proje> --durum` |
| Büyük sürüm (ör. GSAP 4, three r200) | İlgili kategori incelemesini tekrarla (`07-kategori-inceleme.md`) |

## Güvenli deneme (araçlarda değişiklik yaptıysan, yarınki gerçek güncellemeden ÖNCE)
Gerçek kütüphaneye dokunmadan aylık akışı tam veriyle dene (yaklaşık 40 dk, GitHub'dan her şeyi yeniden indirir):
```bash
S=$(mktemp -d); rsync -a --exclude '.gecici' ~/Documents/SkillKutuphanesi/ $S/ && cd $S && python3 -u araclar/arsiv-guncelle.py --uygula --dal
```
Kontrol: (1) `DURDU`/güvenlik kilidi yok, (2) kopyada `master`a dönülmüş, `.guncelleme-kilidi` silinmiş, `guncelleme/YYYY-AA` dalı var,
(3) git HEAD'e göre `id`, `durum`, `kategori`, `ucret` kayması **0** (yalnızca upstream'in gerçekten eklediği skiller yeni görünür),
(4) `notlar/guncelleme-gecmisi.md` kaydında "Karar bekleyen yeni skiller" satırı. Kısmi (`--repo`) çalıştırma bu hataları gizler.
**Karar bekleyen yeni skiller:** upstream bir repoya yeni skill eklediyse arşive alınmaz ve güncellemeyi durdurmaz; listeyi gör, `kaynaklar.json`'da
repo kaydının `dahil` listesine ekle (almak için) ya da `haric`e yaz (almamak için).
