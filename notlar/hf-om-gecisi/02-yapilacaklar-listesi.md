# Yapılacaklar listesi: skill işlemlerinin tamamı

Ana plan: [00-plan.md](00-plan.md). Bu belge üç parçadır:

1. **Kim neyi okur, kim yönetir** (bütün yapay zekâ araçları için tek tablo).
2. **Bu geçiş için tek seferlik liste** (Dalga 1 ve Dalga 2).
3. **Tekrarlayan olaylar** (yeni sürüm, yeni skill, emekli skill, yeni araç… her biri için ne yapılır).

Bütün işlemler **kütüphane oturumundan** başlar. Bir olay olduğunda bana ne olduğunu söylemen yeter; aşağıdaki listeyi ben uygularım.
Başında **Sen:** yazan satırlar senin yapacağın işlerdir; diğerlerini ben yaparım.

---

## 1. Kim neyi okur, kim yönetir

| Araç | Bilgisayarın genelinde okuduğu yer | Projede okuduğu yer | Bugün | Kim yönetir |
|---|---|---|---|---|
| Claude Code | `~/.claude/skills` · eklentiler · hesap skilleri | `.claude/skills` | 104 giriş (75 OpenMontage bağlantısı, 6 `~/.agents` bağlantısı, 21 gerçek skill, 2 yerleşik klasör) | Proje: kütüphane (`skill-ekle.py`). Genel: plan onaylanırsa kütüphanenin makine aracı. |
| Codex | `~/.agents/skills` (belgeli) · `~/.codex/skills` (belgesiz; denenecek) · kendi yerleşik skilleri | `.agents/skills` | 27 + 13 giriş (13'ün biri yerleşik `.system`; sayıma katılmaz, "fazla giriş" diye raporlanmaz) | Aynı |
| Cursor | `~/.cursor/skills` | — | Boş (yerleşik 26 skili ayrı klasörde) | Yönetilmez; aylık kontrol "boş mu" diye bakar |
| Gemini / Antigravity | `~/.gemini/skills` | — | Boş (yerleşik 33 skili ayrı klasörde) | Aynı |
| Copilot | `~/.copilot/skills` | — | Boş | Aynı |
| OpenCode | `~/.config/opencode/skills` | — | Boş | Aynı |
| Claude masaüstü hesap skilleri | Hesaptan gelir (`anthropic-skills:…`) | — | Hesapta tanımlı | Sen (hesap ayarı). Kütüphane, istenen projede gizleyebilir. |
| Claude eklentileri | `~/.claude/plugins` | — | `claude-mem` 14.0.1 | Sen. Kütüphane sadece kaydeder. |
| Palmier | `~/.palmier/skills` | — | 8 skill klasörü | Yönetilmez; sadece kayıt |
| HyperFrames aracı | `~/.claude/skills` ve `~/.agents/skills` içine **kendisi yazabilir** | — | 0.9.23; dondurma satırları henüz yok | Sürüm kararı sende; kurulumu sen yaparsın |
| OpenMontage | Kendi klasörü `~/.openmontage` (skilleri klasör yolundan okur) | — | `c806645` + 9 yerel yama | Kod ve Python ortamı sende; kütüphane sürümü ve yamaları kaydeder |
| `npx skills` aracı | `~/.agents/.skill-lock.json` kayıt dosyası | — | 27 kayıt | **Kullanılmaz.** Kayıt dosyası sadece yedeklenir, düzenlenmez. |

Sayılar 2026-11-10'da, gizli dosyalar (`.DS_Store`, kayıt dosyaları) sayılmadan ölçüldü.

İki temel kural:
- **Claude Code'da genel skill, aynı adlı proje skilinin önüne geçer.** Bu yüzden genel klasörde ne kadar az skill varsa, projeler o kadar öngörülebilir çalışır.
- **Aynı ad tek yerde durmalı.** Codex aynı adlı iki skili birleştirmez; hangisini seçeceği belirsizdir.

---

## 2. Bu geçiş için tek seferlik liste

Adım numaraları 00-plan'daki numaralardır (1.0–1.7 ve 2.0–2.6).

### Dalga 1 (genel skill klasörlerine dokunulmaz)

- [ ] **Sen:** şimdi verilecek kararlar: 1, 2a, 2b, 4, 7 (00-plan, bölüm 9). Raporlar gelince: 8, 9, 10, 11. Dalga 2 öncesi: 3, 5, 6a, 6b.
- [ ] Ön kontrol (1.0): çalışan başka oturum, yetişecek üretim, disk, kütüphane deposu temiz mi, 1 Aralık aylık görevi (bu belge, 3.16).
- [ ] Rapor klasörünü açarım: `~/Documents/Claude/hf-om-raporlar/` (proje oturumları raporlarını buraya yazar).
- [ ] **Sen:** dondurma satırlarını ekle (00-plan 1.1'deki tek komut). Ben yeni oturumdan doğrularım.
- [ ] Makine aracının yedek kısmı yazılır ve test edilir (`makine.py --yedek`, `--yedek-dogrula`; 03 numaralı belge, 1.1).
- [ ] Tam yedek (1.2) → `~/Documents/Claude/yedek/makine-2026-11-10/`.
- [ ] **Sen (harici diskin varsa; karar 4):** yedeği harici diske kopyala (00-plan 1.2). Komut:

```bash
cp -R ~/Documents/Claude/yedek/makine-2026-11-10 "/Volumes/<disk adı>/"
```

  Kontrol: `du -sh` ile iki klasörün boyutuna bak; aynı olmalı. Anahtar dosyaları yedekteyse disk şifreli olmalı.
- [ ] Geri yükleme provası (1.3). Bu geçmeden Dalga 2 başlamaz.
- [ ] Kütüphane, Aşama A (03 numaralı belge, bölüm 1), bu sırayla:
  - [ ] `makine.py --rapor`, `--kaydet`, `--proje-tara` + testleri.
  - [ ] `dogrula.py`: proje adı denetimi `makine.json` ve `notlar/makine-durumu.md` dosyalarını da tarar; `test.py`'ye bu iki dosyada proje adı geçince UYARI çıktığını doğrulayan test eklenir.
  - [ ] `proje-kullanimi.py`: kilit kaydı olmayan projeleri de gösterecek kod değişikliği + testi.
  - [ ] Ancak bundan sonra: kilit kaydı olmayan projeler `projeler.json`'a eklenir.
  - [ ] İlk makine raporu, `makine.json` ilk kaydı, bütün projelerin taraması (1.4).
- [ ] OpenMontage taban ölçümü (1.4): sadece okuyan durum komutları; istersen, onayınla, ücretsiz kısa bir yerel render.
- [ ] Genel skillerin sınıflandırma tablosu → **sen:** "kalacak / projeye inecek / yedeğe gidecek" onayı.
- [ ] Üç deney (1.5): sonuç ya da "doğrulanmadı".
- [ ] **Sen:** IstatistikYoutube oturumunda 1A promptu → rapor. (Taban testini onaylarsan test, projenin kendi test klasörüne
      `tools/kurgu/_test/duman-cikti/` ve HyperFrames önbelleğine `~/.cache/hyperframes` çıktı yazar. Başka hiçbir şey değişmez.)
- [ ] **Sen:** Akıl Dışı oturumunda 2A ve 2A-Codex → rapor → karar 9 ve 10 → 2B (onarım) → 2C (doğrulama).
- [ ] Akıl Dışı'ndaki kırık `hyperframes-creative` bağlantı çifti (karar 8): yedek ve provadan sonra, kütüphane oturumundan.
      İki kırık bağlantı yedeğe taşınır; gerçek kopya `skill-ekle.py` ile önce raporlanır, onayınla kurulur. (Karar 9 "bugünkü
      genel hâl" çıkarsa kopya saklama kopyasından gelir; o zaman kurulum Dalga 2'de 2.1'e kalır.)
- [ ] **Sen:** Psikolojik Danışman oturumunda 3A → karar 11 → 3B.
- [ ] **Sen (isteğe bağlı):** diğer projelerde 4A, Etsy-Arif'te 5A.
- [ ] Her adımdan sonra kütüphane deposuna yerel kayıt (3.16).
- [ ] Dalga 1 kapanış raporu (1.7): 1–8 numaralı kapıların durumu (00-plan, bölüm 7).

### Dalga 2 (ayrı onay; her satır ayrı paket)

- [ ] **Sen:** kararlar 3, 5, 6a, 6b.
- [ ] Kütüphane, Aşama B araç değişiklikleri ve testleri (03 numaralı belge, bölüm 2): saklama kopyasını koruyan kural,
      `makine.py --dondur`, "aynı adla kur" seçeneği, (karar 3 = a ise) `--tasi` ve `--geri-koy`, kural metni.
- [ ] **Paket 0 (2.0; karar 5):** bugünkü HyperFrames skillerinin kütüphanede saklanması. Sıra: iki skille deneme
      (`hyperframes-keyframes` ve hâlâ yayımlanan bir skill) → aylık güncellemenin kuru çalıştırmasında ikisinin de yerinde
      durduğunun görülmesi → geri kalanlar.
- [ ] Projelere kurulum (2.1), her biri rapor + onayla:
  - [ ] IstatistikYoutube: `hyperframes`, `hyperframes-cli`, `hyperframes-core`, `hyperframes-animation`, `motion-graphics`.
  - [ ] Akıl Dışı: `faceless-explainer`, `general-video`, `hyperframes-animation`, `hyperframes-audio`, `hyperframes-keyframes`.
  - [ ] Ad kontrolü (klasör adı ve skilin içindeki ad genel kopyayla aynı) ve içerik karşılaştırması (karar 9).
  - [ ] **Sen:** Akıl Dışı'nda yeni kurulan skiller için ajan yolu çevirme (2B'nin 1. onarımı, güncel eşleme tablosuyla) → 2C.
  - [ ] **Sen:** IstatistikYoutube'da 1C; taban testi yeniden.
- [ ] OpenMontage'ın 75 bağlantısı (2.2): dene → karar 6a → (taşınırsa) **sen:** iki dosyadaki cümleyi hazır metinle düzelt.
- [ ] 9–13 numaralı kapıların kontrolü (00-plan, bölüm 7): saklama kopyaları yerinde · her skill adının projede karşılığı var ·
      devreye girecek içerik aynı · Akıl Dışı eşleme tablosu tamam · sabit yolların çözümü belli.
- [ ] Genel HyperFrames kopyalarının azaltılması (2.3), dört ayrı paket, bu sırayla:
  - [ ] `~/.codex/skills` içindeki 11 bağlantı.
  - [ ] `~/.claude/skills` içindeki, `~/.agents/skills`'e giden 6 bağlantı.
  - [ ] `~/.claude/skills` içindeki gerçek HyperFrames klasörleri (`design-dna` taşınmaz).
  - [ ] `~/.agents/skills` içindeki HyperFrames klasörleri.
- [ ] Her paketten sonra: kırık bağlantı taraması + 1C ve 2C doğrulama promptları + `makine.py --kaydet` + yerel kayıt.
- [ ] (İsteğe bağlı; karar 6b) OpenMontage güncellemesi (2.4): kopya üzerinde prova → karar. Gerçek klasördeki git adımlarını sen çalıştırırsın.
- [ ] (İsteğe bağlı) HyperFrames 0.9.29 (2.5): geçici klasörde karşılaştırma → **sen:** kurulum → kütüphane arşivi aynı sürüme.
- [ ] Aylık göreve makine kontrolünün eklenmesi (2.6).
- [ ] Kapanış: `makine.json` son hâli, rehber ve promptların güncellenmesi, eski notların düzeltilmesi (03 numaralı belge, bölüm 3 ve 4).

---

## 3. Tekrarlayan olaylar

Her olayda sıra aynı: **rapor → karar → yedek → değişiklik → doğrulama → kayıt.**

### 3.1 Yeni bir skill ya da skill reposu eklemek istiyorsun
1. GitHub "Yapay Zeka Skillleri" listesine ekle, bana "yeni skill ekledim, kontrol et" de.
2. Ben: çakışma kontrolü + ücret sınıflandırması + rapor (mevcut akış, `promptlar/07`).
3. **Yeni:** makine raporuna bakarım; aynı adda bir genel skill varsa söylerim (o projede öne geçer).
4. Skill projeye kurulur, bilgisayarın geneline kurulmaz.

Yapma: skilin kendi kurulum komutunu (`npx skills add …`, "install globally") çalıştırma.

### 3.2 Aylık güncelleme
1. Görev başlamadan kütüphane deposu temiz olmalı (3.16).
2. Mevcut akış: rapor → ayrı dalda güncelleme → özet → onayınla birleştirme.
3. **Yeni:** HyperFrames ve OpenMontage kaynaklarındaki değişiklikler ayrıca özetlenir: yeni skill, kalkan skill, yeni araç sürümü.
4. **Yeni:** sonunda sadece okuyan makine kontrolü çalışır: genel klasörlerde yeni / eksik / değişmiş bir şey var mı, diğer araçların
   klasörleri hâlâ boş mu, araç sürümleri kayıtla aynı mı. (Gizli dosyalar sayılmaz.)
5. Saklama kopyaları güncellenmez; projeler kendiliğinden güncellenmez.

### 3.3 HyperFrames aracının yeni sürümü çıktı
1. Hiçbir şey kurma. Bana "yeni sürüm var" de ya da aylık rapor söylesin.
2. Ben değişiklik notlarını okurum: skill listesi değişti mi, görüntü çıktısı değişir mi, emekli olan var mı.
3. Geçici bir klasörde yeni sürüm denenir (genel kurulum yok); aynı sahne iki sürümle karşılaştırılır.
4. Projelerin taban testleri (1C, 2C) bugünkü sürümle kayıtlı olmalı.
5. Karar "yükselt" ise: **sen** `npm install -g hyperframes@X` çalıştırırsın. Geri dönüş: `npm install -g hyperframes@<eski>`.
6. Ben: kütüphanedeki HyperFrames arşivini aynı sürüme çekerim (ayrı dal, onay); önceki sürümün skilleri saklama kopyasına geçer
   (`makine.py --dondur`); `makine.json` güncellenir.
7. Her proje için `skill-ekle.py <proje> --durum`; güncelleme istenen projede `--guncelle --kuru` → onay → `--evet`.
8. Projelerde taban testi yeniden; OpenMontage taban ölçümü yeniden (OpenMontage, HyperFrames'i sürüm belirtmeden çağırıyor).

Yapma: `hyperframes update`, `hyperframes upgrade`, `hyperframes upgrade --project`, `hyperframes skills update`.
Not: bir projenin HyperFrames skilleri, o projenin render aldığı araç sürümünden yeni olmamalı.

### 3.4 HyperFrames skilleri kaynakta değişti (araç aynı)
1. Aylık güncellemede dalda görünür; özetini veririm.
2. Araç sürümünle uyumlu değilse (skiller daha yeni bir araç istiyorsa) arşiv güncellenir ama projelere uygulanmaz.
3. Projeye uygulama her zaman ayrı karar: `--guncelle --kuru` raporu → onay.

### 3.5 Bir skill emekli oldu ya da kaynaktan kalktı
1. Aylık rapor "kaynakta artık yok" der. Kütüphanede kayıtlı olan kopya kendiliğinden korunur (mevcut düzen).
2. Skilin bilgisayarda kurulu hâli kütüphanedeki kopyadan farklıysa ya da kütüphanede hiç yoksa: kurulu hâl
   `makine.py --dondur` ile saklama kopyasına alınır (rapor + onay; 03 numaralı belge, 2.2).
3. `proje-kullanimi.py --skill <kimlik>` ile kullanan projeleri listelerim.
4. Projelerdeki kopyalar yerinde kalır, silinmez.
5. Yerine geçen yeni skill varsa farkını yazarım; geçiş kararı senin.

### 3.6 Kaynak depo taşındı ya da adı değişti
1. Kütüphanede `repo` güncellenir, eski ad `eski_adlar`'a yazılır (mevcut akış, `rehber/09`).
2. OpenMontage klasöründeki kaynak adresi (hâlâ eski adı gösteriyor, yönlendirme çalışıyor) değişecekse komutu ben hazırlarım,
   **sen** çalıştırırsın.

### 3.7 Yeni proje başlatıyorsun
1. `promptlar/01` ile başla; ben önce makine raporuna bakarım.
2. Proje HyperFrames kullanacaksa: skiller projeye kurulur; projenin hangi araç sürümüyle render aldığı proje notuna yazılır.
3. Proje OpenMontage kullanacaksa: Python ortamı yolu `~/.openmontage/.venv/bin/python`; proje içine ikinci bir ortam kurulmaz.
4. Kurulum sonrası `--dogrula`.

### 3.8 Bir projeyi taşıyacak ya da yeniden adlandıracaksın
1. **Önce bana söyle.** HyperFrames, klasörü bulunamayan projelerin geçmiş kayıtlarını kendiliğinden siliyor.
2. Ben: `~/.cache/hyperframes/history` yedeği + proje yedeği.
3. Taşıdıktan sonra: `promptlar/09` (`--yenile`), `projeler.json` güncellemesi, proje içinde sabit yol taraması.

### 3.9 Bir projeyi sileceksin ya da arşive kaldıracaksın
1. Ben: o projede başka yerde kopyası olmayan skill var mı bakarım (`proje-kullanimi.py`, proje taraması).
2. Varsa önce kütüphaneye ya da yedeğe alınır.
3. Tam yedek alınır; `projeler.json` "arşivlendi" diye güncellenir.

### 3.10 OpenMontage kaynakta güncellendi
1. Aylık rapor farkı özetler: yeni skill, değişen araç, yamalarınla çakışan dosyalar.
2. Varsayılan: **güncelleme yok.** Sadece kütüphane arşivi güncellenir (onayınla).
3. Güncelleme istersen: tam yedek → kopya üzerinde prova → çakışma çözümü önerisi → gerçek klasördeki git adımları.
   `~/.openmontage` içinde ben git komutu çalıştırmam; hazır betiği veririm, **sen** çalıştırırsın.
4. Öncesinde ve sonrasında OpenMontage taban ölçümü ve OpenMontage kullanan projelerde aynı test.
5. Python ortamı yeniden kurulmaz, paketler toplu yükseltilmez. Yeni paket gerekiyorsa tek tek, adıyla ve sürümüyle eklenir.

Yapma: `git pull`, `git checkout .`, `git reset --hard`, `git clean`, `make setup`, `make install`, `pip install -U`.

### 3.11 Yeni bir yapay zekâ aracı kurdun (ya da biri güncellendi)
1. Bana aracın adını söyle.
2. Ben: hangi klasörleri okuduğunu belgesinden bulurum, `makine.json`'a eklerim, klasörün bugünkü hâlini kaydederim.
3. Araç "skilleri içe aktar / eşitle" önerirse **kabul etme**; önce bana sor.
4. Aracın kütüphane tarafından yönetilmesi (projeye onun klasörüne de kurulum) ayrı bir karardır; `skill-ekle.py`'ye yeni hedef eklenir.
5. Claude Code ya da Codex güncellendiyse ve skill davranışı değişmiş görünüyorsa üç deney yeniden yapılır.

### 3.12 Genel klasörde beklenmeyen bir değişiklik çıktı
(Makine raporu "yeni", "eksik" ya da "değişmiş" diyor.)
1. Hemen düzeltme yok. Önce kaynağı bulunur: bir kurulum komutu mu, bir araç mı, bir oturum mu.
2. Yedek tazelenir.
3. Karar: yedeğe taşı · olduğu gibi kabul et ve `makine.json`'a yaz · projeye indir.
4. Kaynağı kapatılır (ortam ayarı, alışkanlık, prompt kuralı).

### 3.13 Ad çakışması
1. HyperFrames ya da başka bir kaynak, sende başka kaynaktan duran bir adla yeni skill yayımlarsa aylık rapor uyarır
   (örnek: OpenMontage'ın `hyperframes-media` skili, HyperFrames aynı adı yayımlarsa çakışır).
2. Çıplak ad kendiliğinden el değiştirmez (mevcut kural, `rehber/09`). Devir ancak onayınla.

### 3.14 Yedek yenileme
- Üç ayda bir, her Dalga 2 paketinden önce ve her araç sürümü değişikliğinden önce.
- Yedek `makine.py --yedek` ile alınır, `makine.py --yedek-dogrula` ile denenir.
- 30 günden eski yedekle genel klasörlerde işlem yapılmaz.
- Harici disk kopyası sende (komut: bölüm 2, Dalga 1).

### 3.15 Eklenti ya da hesap skili geldi
1. Eklentiyle gelen skiller adının önünde eklenti adıyla görünür; kütüphane bunları yönetmez, sadece kaydeder.
2. HyperFrames'in eklenti kanalı şimdilik **kullanılmıyor** (sadece 9 skill, Codex'e yaramıyor, kilit kaydıyla izlenemiyor);
   aylık raporda yeniden değerlendirilir.
3. Hesap skilleri bir projede fazlalıksa kütüphane o projede gizleyebilir (mevcut özellik).

### 3.16 Aylık görev ve bu plan
Aylık güncelleme görevi **1 Aralık 2026 10:00**'da çalışacak. Görev, kütüphane deposunda kaydedilmemiş dosya görürse hiçbir
şey yapmadan durur (tek istisna: `notlar/proje-kullanimi.md`).
1. Bu planın her adımından sonra depoya yerel kayıt yapılır: plan belgeleri (`notlar/hf-om-gecisi/`), yeni araç, `makine.json`, raporlar.
2. 30 Kasım'da hâlâ kaydedilmemiş iş varsa görevi bir kereliğine ertelerim ve sana söylerim.
3. Dalga 2 projelere ya da genel klasörlere yazarken görev çalışmamalı: o günlerde görev kapalı tutulur, iş bitince açılır.
4. Makine aracının yazan komutları ve kütüphane arşivine yazan işler, aylık güncellemenin kilidi (`.guncelleme-kilidi`)
   dururken çalışmaz.
5. Görev "depo temiz değil, durduruldu" derse bu bir hata değildir; beklenen davranıştır. Kayıt yapılır, görev yeniden çalıştırılır.

---

## 4. Hiçbir olayda değişmeyenler

- Önce rapor, sonra onay. Yedeksiz işlem yok. Silme yok; yedeğe taşıma var.
- Skiller projeye `skill-ekle.py` ile kurulur.
- Bir proje dosyası değişecekse önce zaman damgalı yedeği alınır (`.yedek-YYYYMMDD-HHMMSS`) ve kontrol kodu kaydedilir.
- `hyperframes update / upgrade / init / clean / skills update` ve `npx skills` çalıştırılmaz.
- Python ortamı yeniden kurulmaz; OpenMontage klasöründe ben git komutu çalıştırmam, kimse toplu git ya da kurulum komutu çalıştırmaz.
- Başka araçların ve Claude'un genel talimat dosyalarına, ayar dosyalarına, anahtar dosyasına ben yazmam.
- Kütüphane deposundaki her değişiklikten sonra yerel kayıt yapılır.
- GitHub'da sadece `ulukayasaban/SkillKutuphanesi`; gönderme sadece sen isteyince.
